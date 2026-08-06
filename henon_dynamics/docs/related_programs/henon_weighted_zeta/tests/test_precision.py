import mpmath as mp

from henon_zeta.controls import analytic_period3
from henon_zeta.precision import refine_and_audit


def test_high_precision_refinement_of_period3_orbit():
    audit = refine_and_audit(analytic_period3(1.02)[0], 1.02, dps=70)
    assert audit["passed"]
    assert mp.mpf(audit["scaled_residual_inf"]) < mp.mpf("1e-50")
    assert mp.mpf(audit["determinant_error"]) < mp.mpf("1e-50")
