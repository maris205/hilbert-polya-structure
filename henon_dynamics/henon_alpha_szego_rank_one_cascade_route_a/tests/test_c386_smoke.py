"""Small, independent-facing regression smoke gates."""
import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("c386_checker",ROOT/"code/c386_szego_checker.py")
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class Smoke(unittest.TestCase):
    def test_01_yaml(self):checker.check_yaml_lock()
    def test_02_constant_counterexample(self):
        d=checker.strict_json(ROOT/"results/c386_szego_evidence.json")
        assert all(r["defect"]==[0,1] and r["cascade"] is False and r["rank"]==0 for r in d["constant_rows"])
    def test_03_same_determinant_opposite_dynamics(self):
        d=checker.strict_json(ROOT/"results/c386_szego_evidence.json")
        for r in d["control_rows"]:
            assert r["bounded"]["M"]==r["cascade"]["M"]==[1,1]
            assert r["bounded"]["regime"]=="compact" and r["cascade"]["regime"]=="cascade"
if __name__=="__main__":unittest.main()
