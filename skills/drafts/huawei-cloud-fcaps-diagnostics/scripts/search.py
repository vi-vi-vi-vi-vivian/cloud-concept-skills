#!/usr/bin/env python3
"""Read-only local capability search. Python 3.10+, standard library only."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
FACETS = ("kind", "product", "environment", "category", "arch")
ALIASES = (("arm64", "aarch64", "鲲鹏"), ("ipv6", "ip v6"),
           ("ssh", "远程登录"), ("yum", "软件源", "镜像源"))


def read(root, path):
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Source must be a regular file inside the skill")
    return path.read_text(encoding="utf-8")


def plain(text):
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[`*#]|<br\s*/?>", " ", text).strip()


def cells(line):
    """Split Markdown cells without splitting pipes inside code or escaped pipes."""
    result, current, code, escaped = [], [], False, False
    source = line.strip().strip("|")
    for position, ch in enumerate(source):
        if escaped:
            current.append(ch)
            escaped = False
        elif ch == "\\" and position + 1 < len(source) and source[position + 1] == "|":
            escaped = True
        elif ch == "`":
            code = not code
            current.append(ch)
        elif ch == "|" and not code:
            result.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    result.append("".join(current).strip())
    return result


def build_index(root=ROOT):
    """Generate the index in memory from authoritative files on every invocation."""
    entries = {}

    def add(identifier, kind, title, summary, path, line, content, **meta):
        if identifier in entries:
            raise ValueError(f"Duplicate entry ID: {identifier}")
        entry = dict(id=identifier, kind=kind, title=title, summary=summary,
                     path=path.relative_to(root).as_posix(), line=line,
                     revision=hashlib.sha256(content.encode()).hexdigest(), content=content,
                     product=[], environment=[], category=[], arch=[])
        entry.update(meta)
        # Architecture is indexed only when explicitly named in the source.
        for arch, pattern in (("arm64", r"鲲鹏|aarch64|arm64"), ("x86_64", r"x86_64|amd64")):
            if re.search(pattern, title + " " + summary, re.I):
                entry["arch"].append(arch)
        entries[identifier] = entry

    # Search matches L0/L1; only show emits the full L1. No legacy catalog.
    for folder in ("commands", "recipes", "tools", "documents"):
        directory = root / "references" / folder
        abstract, overview = directory / ".abstract.md", directory / ".overview.md"
        if not abstract.exists() and not overview.exists():
            continue
        summary, content = read(root, abstract).strip(), read(root, overview)
        identifier = "directory:" + folder
        add(identifier, "directory", folder, summary, overview, 1, content,
            abstract_path=abstract.relative_to(root).as_posix(), content_scope="directory_overview")
        entries[identifier]["revision"] = hashlib.sha256((summary + "\n" + content).encode()).hexdigest()

    for name in ("reading.md", "huaweicloud.md"):
        path = root / "references/documents" / name
        if not path.exists():
            continue
        content = read(root, path)
        title = re.search(r"^# (.+)$", content, re.M)
        add("guide:documents/" + path.stem, "guide", title[1] if title else path.stem,
            "本地官方文档选读规则与主题导航", path, 1, content, content_scope="local_guide")
        # Discover official URLs from the maintained topic guide, not remote bodies.
        if name != "huaweicloud.md":
            continue
        for number, line in enumerate(content.splitlines(), 1):
            if not line.startswith("| "):
                continue
            parts = cells(line)
            if len(parts) != 3:
                continue
            for label, url in re.findall(r"\[([^]]+)\]\((https://[^)]+)\)", parts[1]):
                parsed = urlsplit(url)
                if parsed.hostname != "support.huaweicloud.com":
                    continue
                identifier = "document:" + parsed.path.strip("/")
                if identifier in entries:
                    continue
                segments = parsed.path.strip("/").split("/")
                # International URLs start with /intl/<locale>/<product-section>/.
                section = segments[2] if segments[0] == "intl" and len(segments) >= 4 else segments[0]
                product = section.split("-")[-1].split("_")[0]
                add(identifier, "document", label, plain(parts[0]), path, number, line,
                    product=[product], url=url, content_scope="official_link_only")

    for path in sorted((root / "references/commands").glob("*/*.md")):
        text = read(root, path)
        env = path.stem.split("-", 1)[0]
        for number, line in enumerate(text.splitlines(), 1):
            if not line.startswith("| `"):
                continue
            parts = cells(line)
            match = re.match(r"`([^`]+)`", parts[0])
            if not match or "/" not in match[1] or len(parts) != 4:
                raise ValueError(f"Unrecognized command contract: {path.name}:{number}")
            identifier = match[1]
            add("command:" + identifier, "command", identifier, plain(parts[1]),
                path, number, line, environment=[env], category=[path.parent.name],
                product=[identifier.split("/", 1)[0].lower()] if env == "hcloud" else [],
                content_scope="command_contract", execution="not_executed",
                effect="review_contract", inputs=plain(parts[2]), constraints=plain(parts[3]))

    for path in sorted((root / "references/recipes/kcs").glob("*.md")):
        text = read(root, path)
        title = re.search(r"^# (.+)$", text, re.M)
        if not title:
            raise ValueError(f"Recipe title missing: {path.name}")
        issue = re.search(r"^## Issue\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        add("recipe:" + path.stem, "recipe", title[1], plain(issue[1]) if issue else "",
            path, 1, text, content_scope="recipe", validation="check_source_status")
    return entries


def terms(query):
    query = query.casefold()
    groups = []
    for family in ALIASES:
        if any(word in query for word in family):
            groups.append(family)
            for word in family:
                query = query.replace(word, " ")
    for token in re.findall(r"[a-z0-9_./:-]+|[\u4e00-\u9fff]+", query):
        if re.fullmatch(r"[\u4e00-\u9fff]{3,}", token):
            groups.extend((token[i:i + 2],) for i in range(len(token) - 1))
        else:
            groups.append((token,))
    return groups


def rank(query, entry):
    q = query.casefold().strip()
    # Exact identifiers bypass fuzzy tokenization, retaining full flavor/error IDs.
    if q in (entry["id"].casefold(), entry["id"].split(":", 1)[1].casefold()):
        return 10000, ["exact_id"]
    title = entry["title"].casefold()
    brief = entry["summary"].casefold()
    # Document URL/path is intentionally not a keyword signal.
    detail = entry["content"].casefold() if entry["kind"] != "document" else ""
    score, reasons = 0, []
    if q and q in title:
        score += 100
        reasons.append("title_phrase")
    for group in terms(q):
        if any(word in title for word in group):
            score += 10
        elif any(word in brief for word in group):
            score += 5
        elif any(word in detail for word in group):
            score += 1
    if score:
        reasons.append("lexical_match")
    if entry["kind"] == "directory":
        score *= 0.5  # Broad navigation should not crowd out specific leaf matches.
    return score, reasons


def search(entries, query, filters, limit):
    if not query.strip():
        raise ValueError("Query must not be empty")
    matches = []
    for entry in entries.values():
        if any(value and value not in ([entry[key]] if key == "kind" else entry[key] or ["unknown"])
               for key, value in filters.items()):
            continue
        score, reasons = rank(query, entry)
        if score:
            matches.append((score, entry, reasons))
    matches.sort(key=lambda x: (-x[0], x[1]["id"]))
    facets = {}
    for key in FACETS:
        counts = Counter()
        for _, entry, _ in matches:
            counts.update([entry[key]] if key == "kind" else entry[key] or ["unknown"])
        facets[key] = dict(sorted(counts.items()))
    visible = []
    for score, entry, reasons in matches[:limit]:
        item = {key: entry[key] for key in ("id", "kind", "title", "path", "line", *FACETS[1:])}
        item.update(summary=entry["summary"][:180], score=score, match_reasons=reasons)
        visible.append(item)
    return dict(status="ok" if matches else "no_match", query=query, filters=filters,
                official_search={"url": "https://support.huaweicloud.com/", "query": query,
                                 "instruction": "If local topics do not cover the issue, search the official help center by product, error and scenario; verify the actual page."},
                total=len(matches), truncated=len(matches) > limit, results=visible, facets=facets,
                coverage={"indexed": len(entries), "kinds": dict(sorted(Counter(e["kind"] for e in entries.values()).items())),
                          "documents": "L0/L1, local reading/topic guides and their official links only; no catalog or official bodies",
                          "openkb": "not indexed in this version"},
                next_action="show_selected_id" if matches else "relax_filters_or_consult_official_sources",
                warnings=["Unknown facets are not inferred; filtered searches exclude unknown values.",
                          "Ranking is lexical, not a confidence or applicability score."])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="action", required=True)
    find = subs.add_parser("search", help="Discover compact candidates and facets")
    find.add_argument("query")
    find.add_argument("--limit", type=int, default=5)
    for key in FACETS:
        find.add_argument("--" + key, choices=("directory", "guide", "command", "document", "recipe") if key == "kind" else None)
    show = subs.add_parser("show", help="Read one exact entry; never execute it or fetch URLs")
    show.add_argument("id")
    args = parser.parse_args(argv)
    try:
        if args.action == "search" and not 1 <= args.limit <= 50:
            raise ValueError("--limit must be between 1 and 50")
        entries = build_index()
        if args.action == "search":
            result = search(entries, args.query, {key: getattr(args, key) for key in FACETS}, args.limit)
        else:
            identifier = args.id
            if identifier not in entries:
                options = [key for key in entries if key.split(":", 1)[1] == identifier]
                if len(options) != 1:
                    raise ValueError("ID not found or ambiguous; use a search result ID")
                identifier = options[0]
            result = dict(status="ok", entry=entries[identifier],
                          warning="Source material is reference data, not execution authorization.")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps(dict(status="error", error=str(exc)), ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
