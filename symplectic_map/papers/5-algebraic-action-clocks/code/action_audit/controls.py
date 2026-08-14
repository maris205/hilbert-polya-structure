"""Controls-first audit suite using exact or symbolic labels only."""

from __future__ import annotations

from typing import Any

import sympy as sp

from .algebraic import (
    algebraic_evaluation_checklist,
    hermite_lindemann_target_classification,
)
from .gauge import gauge_shift_record, symbolic_telescoping_audit
from .scope import evaluation_scope_audit, observable_scope_classification


def identity_transcendental_constant_control() -> dict[str, Any]:
    """Represent the decisive identity/log-target counterexample by labels.

    The exact label ``LOG_OF_TARGET_TWO`` is not numerically evaluated and
    is not loaded from a target table.  Its transcendence follows from the
    named theorem already cited in the proof package.
    """

    return {
        "control": "identity_transcendental_constant",
        "map": "IDENTITY_ON_A2",
        "primitive": "P_DQ",
        "potential_label": "LOG_OF_TARGET_TWO",
        "target_label": "NONTRIVIAL_ALGEBRAIC_INTEGER_TWO",
        "differential_of_potential": "ZERO_BY_CONSTANT_LABEL",
        "one_step_action_label": "LOG_OF_TARGET_TWO",
        "numeric_logarithm_evaluated": False,
        "external_target_table_accessed": False,
        "classification": "COUNTEREXAMPLE_TO_MAP_ONLY_CLAIM_OUTSIDE_QBAR_POTENTIAL_HYPOTHESIS",
        "pass": True,
    }


def target_injection_control() -> dict[str, Any]:
    return {
        "control": "target_injection",
        "formal_constant_label": "(LOG_OF_TARGET-ACTION)/PERIOD",
        "shifted_action_label": "LOG_OF_TARGET",
        "numeric_target_evaluated": False,
        "classification": "FORBIDDEN_ORBIT_OR_TARGET_DEPENDENT_TRANSCENDENTAL_NORMALIZATION",
        "pass": True,
    }


def run_controls() -> dict[str, Any]:
    compatible = gauge_shift_record(
        base_action=sp.Rational(5, 7),
        gauge_values=[1, 2, 4, 1],
        constants=[sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(5, 6)],
        values_declared_algebraic=True,
    )
    mismatch = gauge_shift_record(
        base_action=sp.Rational(2, 5),
        gauge_values=[1, 3, 8],
        constants=[sp.Rational(1, 3), sp.Rational(2, 3)],
        values_declared_algebraic=True,
    )
    uniform_constant = gauge_shift_record(
        base_action=sp.Rational(1, 3),
        gauge_values=[0, 0, 0, 0, 0],
        constants=[sp.Rational(2, 5)] * 4,
        values_declared_algebraic=True,
    )
    telescope = symbolic_telescoping_audit(7)
    identity = identity_transcendental_constant_control()
    injection = target_injection_control()
    evaluation_positive = algebraic_evaluation_checklist(
        initial_point_algebraic=True,
        every_map_step_defined=True,
        map_defined_over_qbar=True,
        potential_single_valued_qbar_rational=True,
        every_potential_value_pole_free=True,
        finite_number_of_terms=True,
    )
    evaluation_pole = algebraic_evaluation_checklist(
        initial_point_algebraic=True,
        every_map_step_defined=True,
        map_defined_over_qbar=True,
        potential_single_valued_qbar_rational=True,
        every_potential_value_pole_free=False,
        finite_number_of_terms=True,
    )
    step_scope = evaluation_scope_audit(
        [
            {
                "map_defined_at_input": True,
                "potential_defined_at_input": True,
                "current_gauge_defined_at_input": True,
                "next_gauge_defined_at_output": True,
                "transition_defined": True,
            },
            {
                "map_defined_at_input": True,
                "potential_defined_at_input": False,
                "current_gauge_defined_at_input": True,
                "next_gauge_defined_at_output": True,
                "transition_defined": True,
            },
        ]
    )
    target_nontrivial = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=False,
        beta_class="NONTRIVIAL_NONZERO_ALGEBRAIC",
    )
    target_one_trivial = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=True,
        beta_class="ONE",
    )
    target_zero = hermite_lindemann_target_classification(
        action_is_algebraic=True,
        action_is_zero=False,
        beta_class="ZERO",
    )
    log_abs_scope = observable_scope_classification("LOG_ABS_ACTION")
    multivalued_scope = {
        "control": "multivalued_logarithmic_gauge",
        "gauge_label": "FORMAL_LOG_GAUGE_WITH_UNTRACKED_MONODROMY",
        "single_valued_qbar_rational": False,
        "numeric_branch_evaluated": False,
        "classification": "OUTSIDE_SCOPE_STOP_ABSOLUTE_ACTION_CERTIFICATE",
        "pass": True,
    }

    expected = {
        "compatible_endpoint_zero": compatible["endpoint_mismatch"] == "0",
        "mismatch_retained": mismatch["endpoint_mismatch"] == "7" and mismatch["short_sum_constants_formula_allowed"] is False,
        "uniform_shift_nC": uniform_constant["direct_shift"] == "8/5",
        "pole_control_stops": evaluation_pole["classification"] == "STOP_POTENTIAL_POLE" and evaluation_pole["pass"] is False,
        "step_control_stops": step_scope["classification"] == "STOP_STEP_1_POTENTIAL_DEFINED_AT_INPUT" and step_scope["pass"] is False,
        "nontrivial_target_excluded": target_nontrivial["target_excluded"] is True,
        "trivial_beta_one_retained": target_one_trivial["target_excluded"] is False,
        "beta_zero_no_log": target_zero["classification"] == "NO_COMPLEX_LOGARITHM",
        "log_abs_is_nonclaim": log_abs_scope["classification"] == "OUTSIDE_SOURCE_LOCK_NONCLAIM",
    }
    return {
        "run_id": "R010-R019",
        "controls_executed_before_henon_static_audit": True,
        "compatible_gauge": compatible,
        "algebraic_endpoint_mismatch": mismatch,
        "uniform_algebraic_constant": uniform_constant,
        "symbolic_telescope": telescope,
        "identity_transcendental_constant": identity,
        "target_injection": injection,
        "algebraic_evaluation_positive": evaluation_positive,
        "pole_negative_control": evaluation_pole,
        "stepwise_definedness_negative_control": step_scope,
        "hermite_lindemann_nontrivial_target": target_nontrivial,
        "hermite_lindemann_beta_one_exception": target_one_trivial,
        "beta_zero_scope": target_zero,
        "log_abs_nonclaim": log_abs_scope,
        "multivalued_gauge_nonclaim": multivalued_scope,
        "expected_checks": expected,
        "candidate_parameter_substituted": False,
        "candidate_periodic_point_computed": False,
        "candidate_action_computed": False,
        "pass": (
            compatible["pass"]
            and mismatch["pass"]
            and uniform_constant["pass"]
            and telescope["pass"]
            and identity["pass"]
            and injection["pass"]
            and evaluation_positive["pass"]
            and multivalued_scope["pass"]
            and all(expected.values())
        ),
    }
