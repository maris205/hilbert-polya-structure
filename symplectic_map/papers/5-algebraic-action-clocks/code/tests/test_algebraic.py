from pathlib import Path

import pytest

from action_audit.algebraic import (
    algebraic_evaluation_checklist,
    hermite_lindemann_target_classification,
    proof_dependency_audit,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _checklist(**overrides):
    values = {
        "initial_point_algebraic": True,
        "every_map_step_defined": True,
        "map_defined_over_qbar": True,
        "potential_single_valued_qbar_rational": True,
        "every_potential_value_pole_free": True,
        "finite_number_of_terms": True,
    }
    values.update(overrides)
    return algebraic_evaluation_checklist(**values)


def test_algebraic_dependency_checklist_passes():
    assert _checklist()["classification"] == "ALGEBRAIC_ACTION_BY_FINITE_QBAR_EVALUATION"


def test_algebraic_dependency_stops_at_indeterminacy():
    record = _checklist(every_map_step_defined=False)
    assert not record["pass"]
    assert record["classification"] == "STOP_MAP_INDETERMINACY"


def test_algebraic_dependency_stops_at_pole():
    record = _checklist(every_potential_value_pole_free=False)
    assert record["classification"] == "STOP_POTENTIAL_POLE"


def test_algebraic_dependency_stops_for_multivalued_potential():
    record = _checklist(potential_single_valued_qbar_rational=False)
    assert record["classification"] == "STOP_NONALGEBRAIC_OR_MULTIVALUED_POTENTIAL"


def test_hl_nontrivial_algebraic_target_excluded():
    record = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=False,
        beta_class="NONTRIVIAL_NONZERO_ALGEBRAIC",
    )
    assert record["target_excluded"]


def test_hl_beta_one_zero_action_is_retained():
    record = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=True,
        beta_class="ONE",
    )
    assert not record["target_excluded"]
    assert "TRIVIAL" in record["classification"]


def test_hl_beta_one_nonzero_algebraic_action_excluded():
    record = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=False,
        beta_class="ONE",
    )
    assert record["target_excluded"]


def test_hl_beta_zero_has_no_complex_log():
    record = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=False,
        beta_class="ZERO",
    )
    assert record["classification"] == "NO_COMPLEX_LOGARITHM"


def test_hl_rejects_unknown_target_class():
    with pytest.raises(ValueError):
        hermite_lindemann_target_classification(
            action_is_algebraic=True,
            action_is_zero=False,
            beta_class="PRIME_TABLE_ROW",
        )


def test_proof_dependency_audit_passes_repaired_proof():
    record = proof_dependency_audit(PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md")
    assert record["pass"]
    assert record["proof_contract_version"] == 3
    assert all(record["dependency_checks"].values())


def test_proof_contract_tolerates_equivalent_tex_whitespace(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace(
        r"A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j",
        "A' - A =  \\chi_n(P_n)\n  - \\chi_0(P_0)\n  + \\sum_{j=0}^{n-1} C_j",
        1,
    )
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    assert proof_dependency_audit(path)["pass"]


def test_proof_contract_detects_endpoint_sign_regression(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace(
        r"A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j",
        r"A'-A=\chi_n(P_n)+\chi_0(P_0)+\sum_{j=0}^{n-1}C_j",
        1,
    )
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert not record["dependency_checks"]["general_endpoint_mismatch"]


def test_proof_contract_detects_missing_dependency_id(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace('"AC-OBS-v3"', '"AC-OBS-REMOVED"', 1)
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["dependency_checks"]["exact_contract_id_set"]


def test_proof_contract_detects_deleted_hl_semantic_dependency(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace(
        '"beta_zero_has_no_complex_logarithm",',
        '"beta_zero_dependency_deleted",',
        1,
    )
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert not record["dependency_checks"]["unique_structured_contract"]


def test_proof_contract_detects_untracked_gauge_equation_term(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace(
        r"A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j",
        r"A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j+T_{untracked}",
        1,
    )
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert not record["dependency_checks"]["general_endpoint_mismatch"]
    assert not record["dependency_checks"]["exact_normalized_tagged_equations"]


def test_proof_contract_detects_duplicate_contract_id(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace('"AC-OBS-v3"', '"AC-GAUGE-v3"', 1)
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert "contract IDs must be unique" in record["structured_contract_errors"]


def test_proof_contract_detects_duplicate_equation_tag(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace(
        r"\tag{AC-GAUGE-v3}",
        r"\tag{AC-GAUGE-v3}\tag{AC-GAUGE-v3}",
        1,
    )
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert not record["dependency_checks"]["unique_tagged_equations"]


def test_proof_contract_detects_non_whitespace_control_character(tmp_path):
    source = (PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    changed = source.replace("beta_zero", "beta\x08_zero", 1)
    path = tmp_path / "proof.md"
    path.write_text(changed, encoding="utf-8")
    record = proof_dependency_audit(path)
    assert not record["pass"]
    assert not record["dependency_checks"]["no_forbidden_control_characters"]
