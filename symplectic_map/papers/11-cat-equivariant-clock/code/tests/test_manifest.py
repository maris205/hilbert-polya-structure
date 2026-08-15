from copy import deepcopy
from pathlib import Path

from equivariant_clock.candidate import run_registered_candidate
from equivariant_clock.constants import LOCKED_MODULI
from equivariant_clock.invariants import audit_modulus
from equivariant_clock.manifest import (
    CONTROL_KEYS,
    _result_inventory,
    _validate_audit,
    _validate_row,
)


def test_result_validator_rejects_hollow_rows_and_counter_bypasses() -> None:
    row = audit_modulus(LOCKED_MODULI[0])
    errors: list[str] = []
    _validate_row(row, LOCKED_MODULI[0], errors)
    assert not errors
    forged = dict(row)
    forged["expected"] = dict(row["expected"])
    forged["expected"]["n"] = True
    errors = []
    _validate_row(forged, LOCKED_MODULI[0], errors)
    assert any("ROW_NOT_FRESH_ENGINE_EXACT" in error for error in errors)
    hollow = {
        "q": 2,
        "expected": {"n": 3, "r": 3, "m": 1},
        "torsor": {"pass": True, "direct_group": [0, 0, 0], "direct_cyclic_locus": [0, 0, 0], "r": 3, "m": 1},
        "enumeration_engine": {"engine": "EXPLICIT_FIXED_SET_AND_GROUPOID_ENUMERATION"},
        "formula_engine": {"engine": "REGULAR_TORSOR_THEOREM_FORMULAS"},
        "engine_pair_validation": {"errors": [], "pass": True},
        "checks": {"hollow": True},
        "pass": True,
    }
    errors = []
    _validate_row(hollow, 2, errors)
    assert errors
    assert any("NAMESPACES_NOT_EXACT" in error for error in errors)


def test_externality_and_exact_control_schema_rejects_mutations() -> None:
    audit = run_registered_candidate()
    errors: list[str] = []
    _validate_audit(audit, errors)
    assert not errors
    assert set(audit["controls"]) == CONTROL_KEYS
    for field, expected in (
        ("ambient_ring_varies_with_q", True),
        ("intrinsic_prime_selector", False),
        ("external_modulus_specialization_required", True),
    ):
        assert audit[field] is expected
        missing = deepcopy(audit)
        del missing[field]
        errors = []
        _validate_audit(missing, errors)
        assert errors
        inverted = deepcopy(audit)
        inverted[field] = not expected
        errors = []
        _validate_audit(inverted, errors)
        assert errors
    for mutation in ("missing", "extra", "renamed", "hollow"):
        changed = deepcopy(audit)
        if mutation == "missing":
            del changed["controls"]["K012"]
        elif mutation == "extra":
            changed["controls"]["K013"] = True
        elif mutation == "renamed":
            changed["controls"]["K012_CLOCK"] = changed["controls"].pop("K012")
        else:
            changed["controls"] = {"hollow": True}
        errors = []
        _validate_audit(changed, errors)
        assert any("CONTROL_KEYS_NOT_EXACT" in error for error in errors)
    crosswired = deepcopy(audit)
    crosswired["arithmetic_modulus_records"][0]["formula_engine"]["source_dynamics"]["ordinary_zeta_factors"][0]["support"] += 1
    crosswired["controls"] = {key: True for key in CONTROL_KEYS}
    errors = []
    _validate_audit(crosswired, errors)
    assert any("CONTROLS_NOT_EXACT_RECOMPUTED_TRUE" in error for error in errors)


def test_manifest_rejects_extra_result_file(tmp_path: Path) -> None:
    results = tmp_path / "results"
    results.mkdir()
    (results / "expected.json").write_text("{}\n", encoding="utf-8")
    assert _result_inventory(tmp_path, frozenset({"expected.json"}))["pass"]
    (results / "extra.json").write_text("{}\n", encoding="utf-8")
    assert not _result_inventory(tmp_path, frozenset({"expected.json"}))["pass"]
