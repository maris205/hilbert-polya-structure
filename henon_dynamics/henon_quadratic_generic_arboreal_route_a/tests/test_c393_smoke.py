import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("checker",ROOT/"code/c393_arboreal_checker.py")
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
class Smoke(unittest.TestCase):
    def test_release_evidence(self):self.assertIn("payload",c.check(ROOT/"results/c393_arboreal_evidence.json"))
    def test_fraction_types(self):
        for v in ([True,1],[2,4],[1,0]):
            with self.assertRaises(AssertionError):c.frac(v)
    def test_numeric_types(self):
        for v in ({"n":True},{"n":1.0}):
            with self.assertRaises(AssertionError):c.exact_shape(v)
if __name__=="__main__":unittest.main()
