"""Exact scalar, fractional-normalization, selector, and symbolic-q controls."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

from .constants import REPEATS
from .symbolic import fraction_text


def mechanism_audit(record: dict[str, Any]) -> dict[str, Any]:
    p = record.get("prime")
    m_p = record.get("m_p")
    profile = record.get("cycle_profile")
    if type(p) is not int or type(m_p) is not int or type(profile) is not dict:
        raise ValueError("mechanism audit requires an exact shell record")
    lengths: list[int] = []
    for length, count in sorted(profile.items()):
        if type(length) is not int or type(count) is not int:
            raise ValueError("cycle profile must use integers")
        lengths.extend([length] * count)
    if len(lengths) != m_p or sum(lengths) != p * p - 1:
        raise ValueError("cycle list fails the exact shell partition")
    equal_weight = [
        {
            "repeat": repeat,
            "power_sum": fraction_text(Fraction(m_p, m_p**repeat)),
            "target": "1",
            "matches_target": Fraction(m_p, m_p**repeat) == 1,
        }
        for repeat in REPEATS
    ]
    fractions = [Fraction(length, p * p - 1) for length in lengths]
    return {
        "prime": p,
        "pure_scalar_denominator": {
            "unweighted_degree": m_p,
            "target_degree": 1,
            "all_weights_nonzero": True,
            "can_equal_single_factor_by_degree": m_p == 1,
            "odd_prime_obstruction_pass": p == 2 or m_p > 1,
            "zero_weight_boundary": {
                "retained_weight_one_count": 1,
                "zero_weight_count_required": m_p - 1,
                "classification": "DISCARDS_ALL_BUT_ONE_ORBIT",
            },
        },
        "equal_weight_control": {
            "weight": fraction_text(Fraction(1, m_p)),
            "power_sums": equal_weight,
            "repairs_only_first_repeat_when_m_gt_one": m_p == 1
            or (
                equal_weight[0]["matches_target"] is True
                and all(item["matches_target"] is False for item in equal_weight[1:])
            ),
        },
        "fractional_shell_normalization": {
            "outer_exponents": [fraction_text(value) for value in fractions],
            "sum": fraction_text(sum(fractions, Fraction(0, 1))),
            "equals_one": sum(fractions, Fraction(0, 1)) == 1,
            "uses_complete_shell_cardinality": True,
            "classification": "GLOBAL_NORMALIZED_COUNTING",
            "ordinary_local_scalar_potential": False,
        },
        "one_orbit_selector": {
            "retained_cycle_count": 1,
            "discarded_cycle_count": m_p - 1,
            "adds_global_selector": True,
            "canonical_selector_claimed": False,
        },
    }


def symbolic_composite_control() -> dict[str, Any]:
    """Record the proof identity without choosing or enumerating a composite q."""

    return {
        "object": "EXACT_ADDITIVE_ORDER_q_SHELL",
        "q_value": None,
        "q_is_symbolic": True,
        "shell_cardinality": "J_2(q)=q^2*product_(prime ell|q)(1-ell^(-2))",
        "cycle_partition_identity": "sum_gamma |gamma|=J_2(q)",
        "fractional_identity": (
            "product_gamma (1-q^(-s))^(-|gamma|/J_2(q))=(1-q^(-s))^(-1)"
        ),
        "composite_shells_enumerated": 0,
        "numeric_q_inputs": 0,
        "classification": "PROOF_ONLY_NON_PRIME_SPECIFIC_TAUTOLOGY",
    }
