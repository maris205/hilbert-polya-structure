from pathlib import Path

from centralizer_q.constants import EXPECTED_LEDGER, LEDGER_FIELDS, LOCKED_MODULI
from centralizer_q.finite_module import audit_modulus
from centralizer_q.manifest import _result_inventory, _validate_row


def test_result_validator_rejects_structural_and_counter_bypasses() -> None:
    rows = [audit_modulus(q) for q in LOCKED_MODULI]
    for row, q in zip(rows, LOCKED_MODULI, strict=True):
        errors: list[str] = []
        _validate_row(row, q, errors)
        assert not errors
    row = rows[0]
    forged = dict(row)
    forged["ledger"] = dict(row["ledger"])
    forged["ledger"]["full_CV_quotient_count"] = 2
    errors = []
    _validate_row(forged, 2, errors)
    assert errors
    bool_forged = dict(row)
    bool_forged["expected"] = dict(row["expected"])
    bool_forged["expected"]["full_CV_quotient_count"] = True
    errors = []
    _validate_row(bool_forged, 2, errors)
    assert errors
    structural = dict(row)
    structural["unreviewed"] = True
    errors = []
    _validate_row(structural, 2, errors)
    assert errors
    q = 2
    expected = dict(zip(LEDGER_FIELDS, EXPECTED_LEDGER[q], strict=True))
    ledger = dict(expected)
    ledger.update({"retained_fraction": {}, "discarded_fraction": {}, "norm_image_size": 1})
    direct = {
        "q": q,
        "commutant": [0, 0, 0],
        "full_centralizer": [0, 0, 0],
        "symplectic_centralizer": [0, 0, 0],
        "exact_order_shell": [[], [], []],
        "cyclic_locus": [[], [], []],
        "discarded_shell": [],
        "cyclic_A_orbits": [[]],
        "full_CV_orbits": [[]],
        "symplectic_CV_orbits": [[]],
        "full_shell_orbits": [[]],
        "symplectic_shell_orbits": [[]],
        "norm_image_from_determinants": [1],
        "full_quotient_transition": {"identity": True, "class_count": 1, "transition": [0]},
        "symplectic_quotient_transition": {"identity": True, "class_count": 1, "transition": [0]},
        "reversing": {
            "shell_orbit_count": 1,
            "constructed_equals_brute": True,
            "group_closed": True,
            "cyclic_noncyclic_mixing": False,
        },
    }
    algebra = {
        "q": q,
        "ring_matrices": [0, 0, 0],
        "unit_matrices": [0, 0, 0],
        "norm_one_matrices": [0, 0, 0],
        "torsor_image": [[], [], []],
        "norm_image": [1],
        "norm_table": [{}, {}, {}, {}],
    }
    hollow = {
        "q": q,
        "expected": expected,
        "ledger": ledger,
        "frozen_expected_match": True,
        "dual_checks": {"hollow": True},
        "direct_engine": direct,
        "algebra_engine": algebra,
        "pass": True,
    }
    errors = []
    _validate_row(hollow, q, errors)
    assert errors
    assert any("ROW_NOT_FRESH_ENGINE_EXACT" in error for error in errors)
    assert any("DIRECT_ENGINE_KEYS_NOT_EXACT" in error for error in errors)


def test_manifest_rejects_extra_result_file(tmp_path: Path) -> None:
    results = tmp_path / "results"
    results.mkdir()
    (results / "expected.json").write_text("{}\n", encoding="utf-8")
    assert _result_inventory(tmp_path, frozenset({"expected.json"}))["pass"]
    (results / "extra.json").write_text("{}\n", encoding="utf-8")
    assert not _result_inventory(tmp_path, frozenset({"expected.json"}))["pass"]
