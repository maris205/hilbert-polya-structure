import unittest

import mpmath as mp

from gauss_orbits import (
    canonical_rotation,
    cyclic_invariance_failures,
    determinant,
    enumerate_orbits,
    intrinsic_roof,
    matpow,
    monodromy,
    primitive_necklace_count,
    primitive_necklaces,
    repetition_identity_holds,
    reversal_identity_holds,
)


class GaussOrbitTests(unittest.TestCase):
    def test_exact_monodromy_and_determinant(self):
        self.assertEqual(monodromy((1, 2, 3)), (10, 3, 7, 2))
        self.assertEqual(determinant(monodromy((1, 2, 3))), -1)

    def test_necklace_count_formula(self):
        for alphabet_size in (2, 3, 4):
            for length in range(1, 7):
                observed = len(list(primitive_necklaces(range(1, alphabet_size + 1), length)))
                self.assertEqual(observed, primitive_necklace_count(alphabet_size, length))

    def test_cyclic_reversal_and_repetition_identities(self):
        for orbit in enumerate_orbits((1, 2, 3), 6):
            self.assertEqual(cyclic_invariance_failures(orbit), 0)
            self.assertTrue(reversal_identity_holds(orbit))
            self.assertTrue(repetition_identity_holds(orbit, 2))
            self.assertEqual(monodromy(orbit.word * 3), matpow(orbit.matrix, 3))

    def test_roof_repeats(self):
        mp.mp.dps = 60
        for word in ((1,), (1, 2), (1, 2, 3), (2, 4, 1, 3)):
            base = intrinsic_roof(monodromy(word))
            repeated = intrinsic_roof(monodromy(word * 3))
            self.assertLess(abs(repeated - 3 * base), mp.mpf("1e-50"))

    def test_reverse_is_an_orbit_in_same_alphabet(self):
        for orbit in enumerate_orbits((1, 2, 3), 5):
            self.assertEqual(canonical_rotation(reversed(orbit.word)), orbit.reverse_orbit)


if __name__ == "__main__":
    unittest.main()
