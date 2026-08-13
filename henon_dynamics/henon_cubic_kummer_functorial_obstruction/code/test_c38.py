import unittest

from code.c38_kummer_checker import certificate, cocycle


class KummerCertificateTests(unittest.TestCase):
    def test_frozen_certificate(self) -> None:
        result = certificate()
        self.assertEqual(result["closed_holonomy_exponents_mod_3"], [0, 0, 0])
        self.assertEqual(result["functorial_kummer_prime_weight"], "IDENTITY")
        self.assertEqual(result["cocycle_checks"], 13**3)

    def test_independent_telescoping_model(self) -> None:
        n = 11
        f = lambda x: (x * x + 2) % 3
        c = lambda g, x: (f((x + g) % n) - f(x)) % 3
        for g in range(n):
            for h in range(n):
                for x in range(n):
                    self.assertEqual(c((g + h) % n, x), (c(g, (x + h) % n) + c(h, x)) % 3)
        path = (3, 4, 4)
        for j in range(3):
            x = 7
            exponent = 0
            for g in path:
                exponent = (exponent + j * c(g, x)) % 3
                x = (x + g) % n
            self.assertEqual(exponent, 0)


if __name__ == "__main__":
    unittest.main()
