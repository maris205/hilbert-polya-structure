import math

import numpy as np

import sdc09_successor_experiment as experiment
import virtual_character_context as virtual


def test_internal_atoms_are_generated():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_exact_triangular_ledger_and_periodic_census():
    ledger = experiment.exact_successor_ledger(size=4, max_power=8)
    assert ledger["determinant_exact"]
    assert all(row["exact"] for row in ledger["trace_rows"])
    census = experiment.closed_walk_census(size=5, max_length=8)
    assert all(row["mixed_closed_walks"] == 0 for row in census["rows"])


def test_bidirectional_control_breaks_ledger():
    failure = experiment.bidirectional_failure_exact()
    assert not failure["ledger_exact"]
    assert failure["periodic_census"]["rows"][1]["mixed_closed_walks"] > 0


def test_n2_crossing_formula_and_recurrence():
    for height in [0.0, 0.37, 2.24862330379675, 11.7]:
        expected = (
            3.0
            - 2.0 * math.sqrt(6.0) * math.cos(height * math.log(3.0 / 2.0))
        ) / 24.0
        assert abs(float(experiment.crossing_scalar([2, 3], height)) - expected) < 1e-14
    assert experiment.recurrence_dense_audit()["max_abs_error"] < 1e-12


def test_endpoint_gauges_and_symmetric_motion():
    controls = experiment.alpha_motion_controls(size=4)["rows"]
    by_alpha = {row["alpha"]: row for row in controls}
    assert not by_alpha[0.0]["has_strict_singular_motion"]
    assert not by_alpha[1.0]["has_strict_singular_motion"]
    assert by_alpha[0.5]["has_strict_singular_motion"]


def test_virtual_character_exactness():
    base = virtual.projections()
    radical = virtual.radical()
    even, odd = virtual.minimal_graded()
    assert virtual.audit(base, [], maximum_length=6)["failure_count"] == 0
    assert virtual.audit(radical, [], maximum_length=6)["failure_count"] == 0
    assert virtual.audit(even, odd, maximum_length=6)["failure_count"] == 0
    assert virtual.determinant_identity(even, odd)["exact"]


def test_universal_one_sided_gauge_numerically():
    rows = experiment.one_sided_random_k_gauge()["rows"]
    assert max(row["chiral_gauge_error"] for row in rows) < 1e-12
    assert max(row["singular_max_error"] for row in rows) < 1e-12
