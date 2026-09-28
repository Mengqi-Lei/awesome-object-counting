"""Regression checks for safe README generation (standard library only)."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GenerationSafetyTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / "data", self.root / "data")
        (self.root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/generate_readme.py", self.root / "scripts")

    def run_generator(self):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts/generate_readme.py")],
            capture_output=True, text=True,
        )

    def test_valid_data_preserves_generated_output(self):
        result = self.run_generator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "README.md").read_bytes(),
                         (ROOT / "README.md").read_bytes())

    def test_invalid_papers_cannot_overwrite_readme(self):
        papers = self.root / "data/papers.csv"
        valid = papers.read_text()
        malformed = [
            "".join(valid.splitlines(keepends=True)[1:]),
            valid + '"incomplete row"\n',
        ]
        for content in malformed:
            with self.subTest(content=content[:40]):
                papers.write_text(content)
                (self.root / "README.md").write_text("Keep existing README\n")
                result = self.run_generator()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("papers.csv", result.stderr)
                self.assertEqual((self.root / "README.md").read_text(),
                                 "Keep existing README\n")


if __name__ == "__main__":
    unittest.main()
