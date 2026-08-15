"""Formal raw-return and orbit-label ledgers with exact rational repeats."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

from .constants import REPEATS


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _cycle_profile(record: dict[str, Any]) -> dict[int, int]:
    profile = record.get("cycle_profile")
    if type(profile) is not dict or not profile:
        raise ValueError("cycle profile must be a nonempty exact dictionary")
    checked: dict[int, int] = {}
    for length, count in profile.items():
        if type(length) is not int or type(count) is not int or length < 1 or count < 1:
            raise ValueError("cycle profile contains a nonpositive or noninteger entry")
        checked[length] = count
    return dict(sorted(checked.items()))


def symbolic_product_audit(record: dict[str, Any]) -> dict[str, Any]:
    prime = record.get("prime")
    m_p = record.get("m_p")
    if type(prime) is not int or type(m_p) is not int or m_p < 1:
        raise ValueError("formal product record lacks an exact prime or multiplicity")
    profile = _cycle_profile(record)
    if sum(profile.values()) != m_p:
        raise ValueError("cycle profile does not sum to m_p")
    raw_factors = [
        {
            "formal_base": f"{prime}^(-s*{length})",
            "orbit_length": length,
            "denominator_multiplicity": count,
        }
        for length, count in profile.items()
    ]
    repeats = []
    for repeat in REPEATS:
        raw_terms = [
            {
                "formal_monomial": f"{prime}^(-s*{repeat * length})",
                "coefficient": fraction_text(Fraction(count, repeat)),
                "source_orbit_length": length,
                "source_cycle_count": count,
            }
            for length, count in profile.items()
        ]
        repeats.append(
            {
                "repeat": repeat,
                "raw_return_terms": raw_terms,
                "orbit_label_monomial": f"{prime}^(-s*{repeat})",
                "orbit_label_coefficient": fraction_text(Fraction(m_p, repeat)),
            }
        )
    return {
        "prime": prime,
        "semantics_separated": True,
        "raw_return": {
            "construction": "POINT_POTENTIAL_BIRKHOFF_RETURN",
            "factors": raw_factors,
            "retains_primitive_orbit_length": True,
        },
        "orbit_label": {
            "construction": "GLOBAL_ONE_TIME_SHELL_LABEL_PER_ORBIT",
            "formal_base": f"{prime}^(-s)",
            "denominator_degree": m_p,
            "independent_of_primitive_orbit_length": True,
        },
        "formal_repeats": repeats,
        "numeric_s_evaluations": 0,
        "numeric_log_evaluations": 0,
    }
