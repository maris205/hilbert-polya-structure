import json, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
C=json.loads((P/'results/c65_certificate.json').read_text()); I=json.loads((P/'results/c65_independent_check.json').read_text())
class T(unittest.TestCase):
 def test_check(self): self.assertTrue(C['check'] and I['check'])
 def test_degrees(self): self.assertEqual([r['primitive_count'] for r in C['rows'][:6]],[2,2,6,14,28,62])
 def test_axis(self): self.assertTrue(all(r['axis_symmetry_mean']=='1' for r in C['rows']))
 def test_gap(self): self.assertEqual(C['transverse_gradient_gap'],'partial_t P_axis-partial_t P_orbit=-1/2')
 def test_minimal(self): self.assertEqual(C['claim_status']['minimality'],'PROVED')
 def test_open(self): self.assertEqual(C['claim_status']['mahler_slope_separation'],'OPEN')
 def test_mutations(self): self.assertEqual(C['mutation_audit']['attempted'],21)
 def test_firewall(self): self.assertEqual(C['claim_status']['arithmetic_advance'],'NO'); self.assertFalse(C['claim_status']['route_b_authorized'])
if __name__=='__main__': unittest.main(verbosity=2)
