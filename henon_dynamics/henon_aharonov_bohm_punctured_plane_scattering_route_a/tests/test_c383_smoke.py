import importlib.util
from pathlib import Path
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("checker",ROOT/"code/c383_ab_checker.py")
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class Smoke(unittest.TestCase):
    def test_fraction_rejects_bool(self):
        with self.assertRaises(AssertionError):checker.rational([True,1])
    def test_duplicate_json(self):
        with tempfile.TemporaryDirectory(prefix="c383-smoke-") as d:
            p=Path(d)/"x.json";p.write_text('{"a":1,"a":2}')
            with self.assertRaises(ValueError):checker.strict_json(p)
    def test_yaml_adversaries(self):
        for raw in ('a: 1\na: 2\n','a: &x 1\nb: *x\n','a: {<<: {b: 1}}\n'):
            with tempfile.TemporaryDirectory(prefix="c383-yaml-") as d:
                p=Path(d)/"x.yaml";p.write_text(raw)
                with self.assertRaises(ValueError):checker.strict_yaml(p)
if __name__=="__main__":unittest.main()
