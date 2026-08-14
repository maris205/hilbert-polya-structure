"""Static dependency checks for the algebraic-value and transcendence line."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


PROOF_CONTRACT_VERSION = 3
CONTRACT_BEGIN = "<!-- BEGIN AC_PROOF_CONTRACT_V3 -->"
CONTRACT_END = "<!-- END AC_PROOF_CONTRACT_V3 -->"

# This object is the executable semantic interface.  JSON layout is free, but
# its parsed content must equal this value exactly; prose-presence heuristics
# are deliberately not used.
EXPECTED_PROOF_CONTRACT: dict[str, Any] = {
    "schema": "AC_PROOF_CONTRACT",
    "version": PROOF_CONTRACT_VERSION,
    "contracts": [
        {
            "id": "AC-DOMAIN-v3",
            "kind": "dependency",
            "requires": [
                "each_map_step_defined_before_evaluation",
                "each_potential_value_defined_and_pole_free",
                "each_gauge_endpoint_and_transition_defined_and_pole_free",
            ],
        },
        {
            "id": "AC-EVAL-v3",
            "kind": "equation",
            "requires": [
                "single_valued_qbar_rational_potential",
                "algebraic_periodic_orbit",
                "finite_sum_closed_in_qbar",
            ],
        },
        {
            "id": "AC-HL-v3",
            "kind": "equation",
            "requires": [
                "beta_zero_has_no_complex_logarithm",
                "beta_one_retains_exactly_the_algebraic_exception_A_zero",
                "nonzero_algebraic_A_has_transcendental_exponential",
            ],
        },
        {
            "id": "AC-GAUGE-v3",
            "kind": "equation",
            "requires": [
                "retain_chi_n_at_P_n",
                "retain_minus_chi_0_at_P_0",
                "retain_every_step_constant_C_j",
                "endpoint_compatibility_only_removes_endpoint_difference",
            ],
        },
        {
            "id": "AC-OBS-v3",
            "kind": "dependency",
            "requires": [
                "action_real_part_imaginary_part_and_modulus_are_covered",
                "log_modulus_and_argument_are_nonclaims",
            ],
        },
        {
            "id": "AC-HENON-v3",
            "kind": "equation",
            "requires": [
                "period_one_counts_two_neighbor_slots",
                "period_two_counts_two_neighbor_slots",
            ],
        },
        {
            "id": "AC-GEOM-v3",
            "kind": "dependency",
            "requires": [
                "homogenized_cyclic_system_has_no_projective_point_at_infinity",
                "positive_dimensional_projective_component_would_meet_infinity",
            ],
        },
        {
            "id": "AC-SINT-v3",
            "kind": "equation",
            "requires": [
                "orbit_field_is_finite_extension_K_over_K0",
                "S_contains_places_above_S0",
                "only_three_times_action_is_certified_S_integral",
            ],
        },
        {
            "id": "AC-ROLE-v3",
            "kind": "dependency",
            "requires": [
                "static_computation_is_implementation_audit_only",
                "all_period_conclusion_is_deductive",
            ],
        },
    ],
}

EXPECTED_TAGGED_EQUATIONS = {
    "AC-EVAL-v3": (
        r"P_{j+1}=F_j(P_j),\qquad G_j(P_j)\in\overline{\mathbb Q}"
    ),
    "AC-GAUGE-v3": (
        r"A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j"
    ),
    "AC-HL-v3": (
        r"A\in\overline{\mathbb Q},\quad"
        r"\beta\in\overline{\mathbb Q}^{\times},\quad e^A=\beta"
        r"\quad\Longrightarrow\quad (A,\beta)=(0,1)"
    ),
    "AC-HENON-v3": (
        r"n=1:\ 2q_0=q_0^2-a;\qquad"
        r"n=2:\ 2q_1=q_0^2-a,\quad 2q_0=q_1^2-a"
    ),
    "AC-SINT-v3": (
        r"a\in\mathcal O_{K_0,S_0},\quad K/K_0\text{ contains the orbit},"
        r"\quad S=\{v:v\mid S_0\}"
        r"\quad\Longrightarrow\quad 3\mathcal A_G\in\mathcal O_{K,S}"
    ),
}

REQUIRED_CONTRACT_IDS = {
    record["id"] for record in EXPECTED_PROOF_CONTRACT["contracts"]
}


def _compact_tex(value: str) -> str:
    """Normalize layout-only TeX differences for equation contracts."""

    compact = re.sub(r"\s+", "", value)
    for layout_command in (
        r"\left",
        r"\right",
        r"\qquad",
        r"\quad",
        r"\,",
        r"\!",
        r"\;",
        r"\:",
    ):
        compact = compact.replace(layout_command, "")
    return compact


def _tagged_equation(text: str, equation_id: str) -> tuple[str | None, int]:
    """Return a uniquely tagged display and the number of matching tags."""

    marker = rf"\tag{{{equation_id}}}"
    marker_indices = [match.start() for match in re.finditer(re.escape(marker), text)]
    if len(marker_indices) != 1:
        return None, len(marker_indices)
    marker_index = marker_indices[0]
    start = text.rfind("$$", 0, marker_index)
    end = text.find("$$", marker_index + len(marker))
    if start < 0 or end < 0:
        return None, 1
    display = text[start + 2 : end]
    if display.count(r"\tag{") != 1:
        return None, 1
    return display.replace(marker, "", 1), 1


def _json_object_no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key in proof contract: {key}")
        output[key] = value
    return output


def _parse_structured_contract(text: str) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    if text.count(CONTRACT_BEGIN) != 1 or text.count(CONTRACT_END) != 1:
        return None, ["structured contract markers must each occur exactly once"]
    start = text.index(CONTRACT_BEGIN) + len(CONTRACT_BEGIN)
    end = text.index(CONTRACT_END)
    if end <= start:
        return None, ["structured contract marker order is invalid"]
    block = text[start:end].strip()
    match = re.fullmatch(r"```json\s*(.*?)\s*```", block, flags=re.DOTALL)
    if match is None:
        return None, ["structured contract must be one JSON fenced block"]
    try:
        value = json.loads(
            match.group(1),
            object_pairs_hook=_json_object_no_duplicate_keys,
        )
    except (json.JSONDecodeError, ValueError) as exc:
        return None, [f"invalid structured contract: {exc}"]
    if not isinstance(value, dict):
        return None, ["structured contract root must be an object"]
    contracts = value.get("contracts")
    if not isinstance(contracts, list):
        return value, ["contracts must be a list"]
    ids = [record.get("id") for record in contracts if isinstance(record, dict)]
    if len(ids) != len(contracts):
        errors.append("every contract entry must be an object with an id")
    if len(ids) != len(set(ids)):
        errors.append("contract IDs must be unique")
    if value != EXPECTED_PROOF_CONTRACT:
        errors.append("structured contract content differs from the frozen v3 contract")
    return value, errors


def _forbidden_control_characters(text: str) -> list[dict[str, int]]:
    return [
        {"index": index, "codepoint": ord(character)}
        for index, character in enumerate(text)
        if unicodedata.category(character) == "Cc" and character not in "\n\r\t"
    ]


def algebraic_evaluation_checklist(
    *,
    initial_point_algebraic: bool,
    every_map_step_defined: bool,
    map_defined_over_qbar: bool,
    potential_single_valued_qbar_rational: bool,
    every_potential_value_pole_free: bool,
    finite_number_of_terms: bool,
) -> dict[str, Any]:
    """Evaluate the exact hypotheses of the elementary value lemma.

    This function certifies a dependency chain, not the truth of a user's
    unparsed geometric input.  The booleans must come from an upstream exact
    proof or explicit source-lock declaration.
    """

    checks = {
        "initial_point_algebraic": initial_point_algebraic,
        "every_map_step_defined": every_map_step_defined,
        "map_defined_over_qbar": map_defined_over_qbar,
        "potential_single_valued_qbar_rational": potential_single_valued_qbar_rational,
        "every_potential_value_pole_free": every_potential_value_pole_free,
        "finite_number_of_terms": finite_number_of_terms,
    }
    if not every_map_step_defined:
        classification = "STOP_MAP_INDETERMINACY"
    elif not every_potential_value_pole_free:
        classification = "STOP_POTENTIAL_POLE"
    elif not potential_single_valued_qbar_rational:
        classification = "STOP_NONALGEBRAIC_OR_MULTIVALUED_POTENTIAL"
    elif not initial_point_algebraic or not map_defined_over_qbar:
        classification = "STOP_SIMPLE_QBAR_EVALUATION_PROOF"
    elif not finite_number_of_terms:
        classification = "STOP_FINITE_SUM_ARGUMENT"
    else:
        classification = "ALGEBRAIC_ACTION_BY_FINITE_QBAR_EVALUATION"
    return {
        "dependencies": checks,
        "deduction": [
            "Qbar-rational map evaluation preserves Qbar at each defined step",
            "pole-free Qbar-rational potential evaluation lies in Qbar",
            "a finite sum of Qbar values lies in Qbar",
        ],
        "classification": classification,
        "pass": all(checks.values()),
    }


def hermite_lindemann_target_classification(
    *,
    action_is_algebraic: bool,
    action_is_zero: bool,
    beta_class: str,
) -> dict[str, Any]:
    """Classify symbolic exponential targets without evaluating logarithms.

    ``beta_class`` is one of ``ZERO``, ``ONE``, or
    ``NONTRIVIAL_NONZERO_ALGEBRAIC``.  No numeric target table is accepted.
    """

    allowed = {"ZERO", "ONE", "NONTRIVIAL_NONZERO_ALGEBRAIC"}
    if beta_class not in allowed:
        raise ValueError(f"unsupported beta_class: {beta_class}")

    if beta_class == "ZERO":
        classification = "NO_COMPLEX_LOGARITHM"
        excluded = True
    elif beta_class == "ONE" and action_is_algebraic and action_is_zero:
        classification = "TRIVIAL_ALGEBRAIC_EXCEPTION_A_ZERO_BETA_ONE"
        excluded = False
    elif beta_class == "ONE" and action_is_algebraic:
        classification = "NONZERO_ALGEBRAIC_ACTION_EXCLUDED_BY_HERMITE_LINDEMANN"
        excluded = True
    elif beta_class == "NONTRIVIAL_NONZERO_ALGEBRAIC" and action_is_algebraic:
        classification = "ALGEBRAIC_ACTION_CANNOT_BE_ANY_LOG_BRANCH"
        excluded = True
    else:
        classification = "OUTSIDE_ALGEBRAIC_ACTION_CERTIFICATE"
        excluded = False

    return {
        "action_is_algebraic": action_is_algebraic,
        "action_is_zero": action_is_zero,
        "beta_class": beta_class,
        "numeric_logarithm_evaluated": False,
        "classification": classification,
        "target_excluded": excluded,
    }


def proof_dependency_audit(proof_path: Path) -> dict[str, Any]:
    """Check the unique structured contract and exact tagged equations."""

    text = proof_path.read_text(encoding="utf-8")
    control_characters = _forbidden_control_characters(text)
    headings = re.findall(r"^#{2,4}\s+(.+?)\s*$", text, flags=re.MULTILINE)
    contract_heading = next(
        (value for value in headings if value.startswith("Auditable proof contract")),
        "",
    )
    version_match = re.fullmatch(
        r"Auditable proof contract\s*\(version\s+(\d+)\)",
        contract_heading,
        flags=re.IGNORECASE,
    )
    contract_version = int(version_match.group(1)) if version_match else None
    contract, contract_errors = _parse_structured_contract(text)
    equations_and_counts = {
        equation_id: _tagged_equation(text, equation_id)
        for equation_id in EXPECTED_TAGGED_EQUATIONS
    }
    equations = {
        equation_id: value[0]
        for equation_id, value in equations_and_counts.items()
    }
    equation_tag_counts = {
        equation_id: value[1]
        for equation_id, value in equations_and_counts.items()
    }
    compact_equations = {
        equation_id: "" if equation is None else _compact_tex(equation)
        for equation_id, equation in equations.items()
    }
    expected_compact_equations = {
        equation_id: _compact_tex(equation)
        for equation_id, equation in EXPECTED_TAGGED_EQUATIONS.items()
    }
    found_contract_ids = (
        [
            record.get("id")
            for record in contract.get("contracts", [])
            if isinstance(record, dict)
        ]
        if isinstance(contract, dict)
        else []
    )
    sections = {
        "theorem_a": any(value.startswith("Theorem A ") for value in headings),
        "corollary_b": any(value.startswith("Corollary B ") for value in headings),
        "proposition_c": any(value.startswith("Proposition C ") for value in headings),
        "theorem_d": any(value.startswith("Theorem D ") for value in headings),
        "corollary_e": any(value.startswith("Corollary E ") for value in headings),
        "proof": "Proof" in headings,
        "proof_contract_v3": contract_version == PROOF_CONTRACT_VERSION,
    }
    checks = {
        "no_forbidden_control_characters": not control_characters,
        "unique_structured_contract": not contract_errors,
        "exact_contract_id_set": (
            len(found_contract_ids) == len(REQUIRED_CONTRACT_IDS)
            and set(found_contract_ids) == REQUIRED_CONTRACT_IDS
        ),
        "unique_tagged_equations": all(
            count == 1 for count in equation_tag_counts.values()
        ),
        "exact_normalized_tagged_equations": all(
            compact_equations[equation_id] == expected_compact_equations[equation_id]
            for equation_id in EXPECTED_TAGGED_EQUATIONS
        ),
        "stepwise_domain_and_poles": contract == EXPECTED_PROOF_CONTRACT,
        "single_valued_qbar_evaluation": contract == EXPECTED_PROOF_CONTRACT,
        "general_endpoint_mismatch": (
            compact_equations["AC-GAUGE-v3"]
            == expected_compact_equations["AC-GAUGE-v3"]
        ),
        "hl_zero_one_edge_cases": (
            compact_equations["AC-HL-v3"]
            == expected_compact_equations["AC-HL-v3"]
        ),
        "log_abs_nonclaim": contract == EXPECTED_PROOF_CONTRACT,
        "low_period_multiplicity": (
            compact_equations["AC-HENON-v3"]
            == expected_compact_equations["AC-HENON-v3"]
        ),
        "projective_no_infinity": contract == EXPECTED_PROOF_CONTRACT,
        "orbit_field_extended_s_and_denominator_three": (
            compact_equations["AC-SINT-v3"]
            == expected_compact_equations["AC-SINT-v3"]
        ),
        "finite_static_audit_not_proof": contract == EXPECTED_PROOF_CONTRACT,
    }
    return {
        "run_id": "R002",
        "proof_path": str(proof_path),
        "proof_sha256": _sha256(proof_path),
        "proof_contract_version": contract_version,
        "required_contract_ids": sorted(REQUIRED_CONTRACT_IDS),
        "found_contract_ids": found_contract_ids,
        "structured_contract_errors": contract_errors,
        "forbidden_control_characters": control_characters,
        "tagged_equations_found": {
            equation_id: equation is not None for equation_id, equation in equations.items()
        },
        "tag_counts": equation_tag_counts,
        "normalization": "JSON layout is ignored; TeX whitespace, left/right, and spacing-only commands are ignored; all remaining parsed content must match exactly",
        "structured_sections": sections,
        "dependency_checks": checks,
        "role": "text integrity check; independent mathematics is recorded in notes/INDEPENDENT_COUNTEREXAMPLE_REVIEW.md",
        "pass": all(sections.values()) and all(checks.values()),
    }
