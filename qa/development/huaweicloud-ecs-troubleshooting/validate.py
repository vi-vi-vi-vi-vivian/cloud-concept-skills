#!/usr/bin/env python3
"""Check the draft against recorded CLI evidence. Does not call cloud APIs."""
import argparse
import collections
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[3]
SKILL = REPO / "development/huaweicloud-ecs-troubleshooting"
META = Path.home() / ".hcloud/metaRepo/template"


def read_log(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def latest(rows):
    return {row["id"]: row for row in rows}


def anchor(title):
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def error_summary(row):
    message = row.get("error") or ""
    codes = re.findall(r"\b[A-Za-z][A-Za-z0-9_-]*\.[0-9]+\b", message)
    message = re.sub(r"\b(?:[0-9a-f]{32}|[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12})\b", "<redacted-id>", message)
    return {"id": row["id"], "error_code": row.get("error_code") or (codes[0] if codes else None), "error": message}


def validate(evidence):
    errors = []
    checks = collections.Counter()

    def check(ok, group, message):
        checks[group] += 1
        if not ok:
            errors.append(message)

    manifest = {r["id"]: r for r in json.loads((evidence / "manifest.json").read_text())}
    help_attempts = read_log(evidence / "help-results.jsonl")
    live_attempts = read_log(evidence / "live-results.jsonl")
    helps, lives = latest(help_attempts), latest(live_attempts)
    cli_rows = json.loads((evidence / "cli-results.json").read_text())
    for row in cli_rows:
        raw = (evidence / row["file"]).read_bytes()
        check(row["status"] == "passed" and hashlib.sha256(raw).hexdigest() == row["sha256"], "cli_meta_tools", f"CLI evidence failed: {row['command']}")
    files = {p.resolve(): p.read_text() for p in SKILL.rglob("*.md")}
    runtime = {p: text for p, text in files.items() if p.name not in {"README.md", "STRUCTURE.md"}}
    contracts = {}
    for path, text in runtime.items():
        for cid, state, purpose, effect, dependency in re.findall(
            r"^\| `([^`]+/[^`]+/v\d+)` · ([^|]+) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$", text, re.M
        ):
            check(cid not in contracts, "canonical", f"Duplicate contract: {cid}")
            contracts[cid] = dict(path=path, state=state.strip(), purpose=purpose.strip(), effect=effect.strip(), dependency=dependency.strip())
    check(set(contracts) == set(manifest), "coverage", f"Coverage mismatch: missing={sorted(set(manifest)-set(contracts))}, extra={sorted(set(contracts)-set(manifest))}")
    check(set(manifest) <= set(helps), "coverage", "Some commands lack an actual help attempt")
    check(set(lives) <= set(manifest), "coverage", "Live calls outside the documented inventory")

    catalogs = {}
    for cid, row in manifest.items():
        if cid not in contracts or cid not in helps:
            continue
        contract, help_row, live_row = contracts[cid], helps[cid], lives.get(cid)
        service = row["service"].lower()
        if service not in catalogs:
            catalogs[service] = json.loads((META / service / "apis_cn.json").read_text())["apiList"]
        entry = catalogs[service].get(row["operation"].lower(), {})
        check(row["version"] in entry.get("Versions", []), "catalog", f"Unknown command/version: {cid}")
        raw_path = evidence / help_row["file"]
        raw = raw_path.read_text()
        check(hashlib.sha256(raw.encode()).hexdigest() == help_row["sha256"], "help_integrity", f"Help hash mismatch: {cid}")
        if help_row["status"] == "passed":
            check(bool(re.search(r"^Service:\s*\n\s*" + re.escape(row["service"]) + r"\s*$", raw, re.M)), "help_content", f"Help service missing: {cid}")
            check(bool(re.search(r"^Method:\s*\n\s*" + help_row["method"] + r"\b", raw, re.M)), "help_content", f"Help method missing: {cid}")
        expected = "阻·帮助" if help_row["status"] != "passed" else {"passed": "实", "empty": "实·空", "blocked": "阻·调用"}[live_row["status"]] if live_row else "助"
        check(contract["state"] == expected, "status", f"Evidence/status mismatch: {cid}")
        check(dt.datetime.fromisoformat(help_row["at"]).timestamp() <= contract["path"].stat().st_mtime, "fact_before_authoring", f"Help was collected after contract authoring: {cid}")
        for dep in re.findall(r"\[([^\]]+/[^\]]+/v\d+)\]", contract["dependency"]):
            check(dep in manifest, "dependency", f"Unknown dependency: {cid} -> {dep}")

    graph = collections.defaultdict(set)
    for path, text in files.items():
        for cid, target in re.findall(r"\[([^\]]+/[^\]]+/v\d+)\]\(([^\s)]+)\)", text):
            dest = (path.parent / target.partition("#")[0]).resolve()
            check(cid in contracts and dest == contracts[cid]["path"], "dependency_target", f"Dependency points outside its canonical contract: {path.name} -> {cid}")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\s)]+)\)", text):
            if re.match(r"[a-z]+://", target):
                continue
            rel, _, fragment = target.partition("#")
            dest = (path.parent / rel).resolve() if rel else path
            check(dest.is_file(), "links", f"Missing link: {path.name} -> {target}")
            graph[path].add(dest)
            if fragment and dest in files:
                anchors = {anchor(t) for t in re.findall(r"^#+ (.+)$", files[dest], re.M)}
                check(fragment in anchors, "anchors", f"Missing anchor: {path.name} -> {target}")
    reached, pending = set(), [SKILL / "SKILL.md"]
    while pending:
        path = pending.pop().resolve()
        if path in reached:
            continue
        reached.add(path)
        pending.extend(graph[path] - reached)
    check(set(runtime) <= reached, "loading", f"Unreachable references: {[str(p.relative_to(SKILL)) for p in set(runtime)-reached]}")

    for path, text in runtime.items():
        check(not re.search(r"\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b", text), "redaction", f"Resource UUID in runtime: {path.name}")
        check(not re.search(r"--cli-(?:ak|sk|token|access-key|secret-key|security-token)=\S+", text), "redaction", f"Credential argument in runtime: {path.name}")
    recipe_paths = sorted((SKILL / "references/recipes").glob("*.md"))
    check(len(recipe_paths) == 9, "recipe_scope", "Recipe planning directory must cover the nine agreed topics")
    for path in recipe_paths:
        text = path.read_text()
        body = "\n".join(line for line in text.splitlines() if line and not line.startswith("#"))
        check("规划" in text and 1 <= body.count("。") <= 2 and "hcloud " not in body and "```" not in body, "recipe_scope", f"Recipe exceeds planning scope: {path.name}")

    semantic_cases = {
        "HSS/RunBaselineDetect/v5": ("主动检测", "GET"),
        "COC/CreateDiagnosisTask/v1": ("安装 Holmes、主机采集", "POST"),
        "ECS/ShowServerRemoteConsole/v2": ("生成登录地址", "POST"),
        "APM/ShowSpanSearch/v1": ("读取", "POST"),
        "SMN/PublishMessage/v2": ("发送消息", "POST"),
    }
    for cid, (effect, method) in semantic_cases.items():
        check(contracts.get(cid, {}).get("effect") == effect and helps.get(cid, {}).get("method") == method, "effect_semantics", f"Known effect/method distinction lost: {cid}")
    for row in lives.values():
        if row["status"] in {"passed", "empty"}:
            check(all(a["passed"] for a in row.get("assertions", [])), "live_assertions", f"Failed assertion labeled successful: {row['id']}")

    recheck_path = evidence / "post-write-checks.json"
    recheck = json.loads(recheck_path.read_text()) if recheck_path.exists() else {}
    check(
        recheck.get("completed") is True
        and len(recheck.get("checks", [])) == 10
        and all(c["passed"] for c in recheck.get("checks", [])),
        "post_write", "Post-write live dependency checks missing or failed",
    )
    report = {
        "at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "scope": "结构、清单覆盖、证据一致性和指定依赖链；不等于全部业务接口实测成功",
        "result": "PASS" if not errors else "FAIL",
        "contracts": len(contracts), "services": len(catalogs),
        "checks": dict(checks), "errors": errors,
        "help": {"unique": len(helps), "attempts": len(help_attempts), **dict(collections.Counter(r["status"] for r in helps.values()))},
        "cli_meta_tools": {"unique": len(cli_rows), **dict(collections.Counter(r["verification"] for r in cli_rows))},
        "live": {"unique": len(lives), "attempts": len(live_attempts), **dict(collections.Counter(r["status"] for r in lives.values()))},
        "contract_states": dict(collections.Counter(r["state"] for r in contracts.values())),
        "blocked": [error_summary(r) for r in lives.values() if r["status"] == "blocked"],
        "help_blocked": [error_summary(r) for r in helps.values() if r["status"] != "passed"],
        "post_write": recheck,
    }
    (evidence / "acceptance.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 真实验收结果", "",
        f"时间：{report['at']}。KooCLI 7.2.12。", "",
        f"验收：**{report['result']}**。{report['scope']}。", "",
        "| 项目 | 实际结果 |", "| --- | --- |",
        f"| 契约覆盖 | {len(contracts)} 个命令版本，{len(catalogs)} 个服务 |",
        f"| 帮助查询 | {report['help']} |",
        f"| CLI 元工具 | {report['cli_meta_tools']} |",
        f"| 真实 API | {report['live']} |",
        f"| 契约标记 | {report['contract_states']} |",
        f"| 检查项 | {sum(checks.values())} 项，失败 {len(errors)} 项 |", "",
        "成功只表示本次请求成功。空列表不证明系统正常。未执行修改、扫描、主机作业、订购或消息发送。",
        "", "## 受阻项", "",
    ]
    for row in report["blocked"] + report["help_blocked"]:
        lines.append(f"- `{row['id']}`：{row.get('error_code') or ''} {row.get('error') or ''}")
    lines += ["", "## 写入后真实复核", ""]
    for item in recheck.get("checks", []):
        lines.append(f"- {'通过' if item['passed'] else '失败'}：{item['name']}")
    lines += ["", "## 本地检查", ""] + [f"- {k}：{v} 项。" for k, v in checks.items()]
    if errors:
        lines += ["", "## 未通过", ""] + ["- " + e for e in errors]
    (evidence / "acceptance.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return not errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, required=True, help="Directory containing the real CLI help and API records")
    args = parser.parse_args()
    sys.exit(0 if validate(args.evidence.resolve()) else 1)
