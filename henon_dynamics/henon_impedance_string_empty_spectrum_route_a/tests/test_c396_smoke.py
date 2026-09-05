import importlib.util
from pathlib import Path
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("independent",ROOT/"code/c396_checker.py")
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class Smoke(unittest.TestCase):
    def test_canonical(self):self.assertEqual(len(checker.check(ROOT/"results/c396_evidence.json")),64)
    def test_yaml(self):self.assertIs(checker.check_yaml()["route_b_invocation_allowed"],False)
    def test_duplicate(self):
        with tempfile.TemporaryDirectory(prefix="c396-smoke-") as d:
            path=Path(d)/"bad.json";path.write_text('{"x":1,"x":2}')
            with self.assertRaises(ValueError):checker.strict_json(path)
