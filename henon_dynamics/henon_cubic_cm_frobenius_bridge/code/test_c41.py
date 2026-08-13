import unittest

from code.c41_cm_checker import certificate, count_fp2, trace_fp


class CMTests(unittest.TestCase):
    def test_small_traces(self) -> None:
        self.assertEqual(trace_fp(5), 0)
        self.assertEqual(trace_fp(7), -4)
        self.assertEqual(trace_fp(11), 0)
        self.assertEqual(trace_fp(13), 2)

    def test_extension_recurrence(self) -> None:
        for p in (5, 7):
            a = trace_fp(p)
            self.assertEqual(count_fp2(p), p * p + 1 - (a * a - 2 * p))

    def test_certificate(self) -> None:
        result = certificate(500)
        self.assertEqual(result["inert_trace_failures"], 0)
        self.assertEqual(result["hasse_failures"], 0)


if __name__ == "__main__":
    unittest.main()
