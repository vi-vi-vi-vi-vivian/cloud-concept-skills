"""Read-only search acceptance tests against the shipped knowledge sources."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/search.py"
spec = importlib.util.spec_from_file_location("skill_search", SCRIPT)
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = search.build_index(ROOT)

    def find(self, query, limit=5, **filters):
        return search.search(self.entries, query, filters, limit)

    def test_exact_command_and_contract(self):
        result = self.find("LINUX/block-devices")
        self.assertEqual(result["results"][0]["id"], "command:LINUX/block-devices")
        entry = self.entries[result["results"][0]["id"]]
        self.assertIn("lsblk --json", entry["content"])
        self.assertEqual(entry["execution"], "not_executed")
        line = (ROOT / entry["path"]).read_text().splitlines()[entry["line"] - 1]
        self.assertEqual(line, entry["content"])

    def test_l0_l1_navigation(self):
        result = self.find("官方文档", kind="directory")
        self.assertIn("directory:documents", [x["id"] for x in result["results"]])
        entry = self.entries["directory:documents"]
        self.assertEqual(entry["summary"], (ROOT / entry["abstract_path"]).read_text().strip())
        self.assertEqual(entry["content"], (ROOT / entry["path"]).read_text())
        self.assertNotIn("content", result["results"][0])

    def test_official_links_and_coverage_boundary(self):
        result = self.find("磁盘映射", kind="document", product="ecs")
        self.assertGreater(result["total"], 0)
        entry = self.entries[result["results"][0]["id"]]
        self.assertEqual(entry["content_scope"], "official_link_only")
        self.assertTrue(entry["url"].startswith("https://support.huaweicloud.com/"))
        self.assertIn("云盘标识", entry["content"])
        self.assertEqual(self.find("yum源", kind="document", arch="arm64")["total"], 0)
        self.assertIn("support.huaweicloud.com", self.find("yum源", kind="document")["official_search"]["url"])

    def test_international_product_facet(self):
        result = self.find("健康检查", kind="document", product="elb")
        self.assertGreater(result["total"], 0)
        entry = self.entries[result["results"][0]["id"]]
        self.assertIn("/intl/zh-cn/elb_faq/", entry["url"])
        self.assertNotIn("intl", entry["product"])

    def test_all_entries_have_resolvable_sources(self):
        for entry in self.entries.values():
            with self.subTest(id=entry["id"]):
                source = ROOT / entry["path"]
                lines = source.read_text().splitlines()
                self.assertGreaterEqual(entry["line"], 1)
                self.assertLessEqual(entry["line"], len(lines))
                if entry["kind"] in ("command", "document"):
                    self.assertEqual(lines[entry["line"] - 1], entry["content"])
        command_count = sum(e["kind"] == "command" for e in self.entries.values())
        # Independently count contract rows to catch silent omissions.
        raw_count = sum(line.startswith("| \x60") for path in
                        (ROOT / "references/commands").glob("*/*.md")
                        for line in path.read_text().splitlines())
        self.assertEqual(command_count, raw_count)

    def test_cli_from_other_directory_and_invalid_input(self):
        with tempfile.TemporaryDirectory() as folder:
            for args, code in [
                (["show", "directory:documents"], 0),
                (["search", "  "], 2),
                (["search", "磁盘", "--kind", "invalid"], 2),
                (["search", "磁盘", "--limit", "51"], 2),
            ]:
                result = subprocess.run([sys.executable, str(SCRIPT), *args],
                                        cwd=folder, capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stderr)
                if result.stdout:
                    json.loads(result.stdout)
                else:
                    self.assertIn("usage:", result.stderr)

    def test_markdown_backslashes_and_escaped_pipes(self):
        self.assertEqual(search.cells(r"| id | fact | C:\Windows\logs\ | safe |")[2],
                         "C:\\Windows\\logs\\")
        self.assertEqual(search.cells(r"| id | a \| b | input | safe |")[1], "a | b")
        self.assertEqual(search.cells(r"| id | fact | \\server\share | safe |")[2],
                         r"\\server\share")

    def test_no_nearby_sku_substitution_or_uncovered_product_claim(self):
        result = self.find("ac7-ext.8xlarge.2")
        self.assertEqual(result["status"], "no_match")
        mrs = self.find("yum", product="mrs")
        self.assertEqual(mrs["total"], 0)
        self.assertIn("no catalog", mrs["coverage"]["documents"])
        self.assertIn("official", mrs["next_action"])

    def test_filters_facets_and_truncation(self):
        result = self.find("磁盘", limit=1, kind="command", environment="linux")
        self.assertGreater(result["total"], 1)
        self.assertTrue(result["truncated"])
        self.assertEqual(result["facets"]["kind"], {"command": result["total"]})
        self.assertEqual(result["facets"]["environment"], {"linux": result["total"]})
        unknown = self.find("磁盘", kind="document", environment="unknown")
        self.assertGreater(unknown["total"], 0)

    def test_recipe_and_changed_source_are_read_live(self):
        result = self.find("recipe:network")
        self.assertEqual(result["results"][0]["id"], "recipe:network")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / "references/documents"
            path.mkdir(parents=True)
            (path / ".abstract.md").write_text("First")
            (path / ".overview.md").write_text("# Navigation")
            first = search.build_index(root)
            (path / ".abstract.md").write_text("Updated")
            second = search.build_index(root)
            self.assertNotEqual(first["directory:documents"]["revision"],
                                second["directory:documents"]["revision"])
            # A stale or malformed legacy catalog must have no effect.
            (path / "catalog.jsonl").write_text("invalid legacy JSON")
            self.assertEqual(second, search.build_index(root))

    def test_pipe_in_command_and_symlink_escape(self):
        self.assertEqual(len(search.cells('| `A/b`<br>`a | b` | fact | input | constraint |')), 4)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "skill"
            root.mkdir()
            outside = Path(folder) / "secret"
            outside.write_text("do not read")
            link = root / "link"
            link.symlink_to(outside)
            with self.assertRaises(ValueError):
                search.read(root, link)

    def test_cli_show_error_and_limit(self):
        for args, expected in [(["show", "LINUX/block-devices"], 0),
                               (["show", "../../.env"], 2),
                               (["search", "yum", "--limit", "0"], 2)]:
            result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
            self.assertEqual(result.returncode, expected, result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(data["status"], "ok" if expected == 0 else "error")


if __name__ == "__main__":
    unittest.main()
