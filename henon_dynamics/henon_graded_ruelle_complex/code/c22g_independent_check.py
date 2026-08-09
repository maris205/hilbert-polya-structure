#!/usr/bin/env python3
"""Independent, nonimporting checker for the HCS-C22G certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PARENT_CERTIFICATE = (
    PROJECT_ROOT.parent
    / "henon_time_ordered_ruelle_cocycle"
    / "results"
    / "c22_t4_certificate.json"
)
PAPER5 = PROJECT_ROOT.parent / "docs" / "prior_work" / "papers" / (
    "5-An Area-Preserving Henon-Map Model.pdf"
)
DEFAULT_CERTIFICATE = PROJECT_ROOT / "results" / "c22g_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22g_independent_check.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frac(value: object) -> Fraction:
    if isinstance(value, dict):
        value = value["fraction"]
    return Fraction(str(value))


def algebra_checks() -> dict[str, bool]:
    a11, a12, a21, a22, b1, b2, c1, c2, d = sp.symbols(
        "a11 a12 a21 a22 b1 b2 c1 c2 d", nonzero=True
    )
    aa = sp.Matrix([[a11, a12], [a21, a22]])
    bb = sp.Matrix([[b1], [b2]])
    cc = sp.Matrix([[c1, c2]])
    qmat = sp.Matrix([[1, 0, 0], [0, 1, 0], [c1, c2, d]])
    pmat = sp.Matrix([[a11, a12, b1], [a21, a22, b2], [0, 0, 1]])
    residual = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(2) - aa, -bb),
        sp.Matrix.hstack(-cc, sp.Matrix([[1 - d]])),
    )
    return_derivative = pmat * qmat.inv()
    residue_zero = sp.factor(
        residual.det() + d * (sp.eye(3) - return_derivative).det()
    )

    matrix = sp.Matrix(3, 3, sp.symbols("x0:9"))
    e2 = sum(
        matrix.extract(indices, indices).det()
        for indices in ((0, 1), (0, 2), (1, 2))
    )
    exterior_zero = sp.expand(
        1 - sp.trace(matrix) + e2 - matrix.det() - (sp.eye(3) - matrix).det()
    )
    lam = sp.symbols("lam", nonzero=True)
    lifted_zero = sp.factor(
        1
        - (lam + lam**-1 + lam**-2)
        + (1 + lam**-1 + lam**-3)
        - lam**-2
        - (1 - lam) * (1 - lam**-1) * (1 - lam**-2)
    )
    return {
        "signed_residue_identity": residue_zero == 0,
        "exterior_identity": exterior_zero == 0,
        "lifted_eigenvalue_identity": lifted_zero == 0,
    }


def audit(certificate: dict[str, object]) -> dict[str, bool]:
    pinning = certificate.get("g1_lifted_pinning", {})
    convention = pinning.get("bps_convention", {})
    inclusions = pinning.get("strict_inclusions", {})
    nonvanishing = pinning.get("nonvanishing", {})
    graph = pinning.get("graph", {})
    residue = certificate.get("g2_g4_residue_and_supertrace", {})
    raw = residue.get("raw_residue", {})
    exterior = residue.get("exterior", {})
    chronology = residue.get("chronology_control", {})
    nuclear = certificate.get("g3_nuclearity", {})
    decisions = certificate.get("decisions", {})
    sources = certificate.get("source_lock", {})

    beta = Fraction(123, 112)
    c_upper = 2 * Fraction(61, 10) * Fraction(5, 8) + beta * Fraction(1, 2)
    expected_ratios = (
        Fraction(39, 41),
        Fraction(250880, 466211),
        Fraction(907, 915),
    )
    stated_ratios = (
        frac(inclusions.get("stable_base_X_inside_Y_ratio", "0")),
        frac(inclusions.get("stable_slope_GM_inside_M_ratio", "0")),
        frac(inclusions.get("unstable_half_inverse_inside_X_ratio", "0")),
    )

    exponents = exterior.get("fredholm_exponents", [])
    exponent_values = [row.get("exponent") for row in exponents]
    source_ok = (
        PARENT_CERTIFICATE.exists()
        and PAPER5.exists()
        and sources.get("parent_sha256") == sha256(PARENT_CERTIFICATE)
        and sources.get("paper5_sha256") == sha256(PAPER5)
    )
    graph_edges = graph.get("edges", [])
    edge_pairs = {(row.get("source"), row.get("target")) for row in graph_edges}
    expected_edges = {
        ("--", "--"),
        ("--", "+-"),
        ("-+", "--"),
        ("+-", "-+"),
        ("+-", "++"),
        ("++", "-+"),
    }

    checks = {
        "source_hashes": source_ok,
        "correct_bps_mixed_data": convention.get("fixed_mixed_data")
        == "input stable w and output unstable z"
        and convention.get("reverse_stable_output_inverse_used") is False,
        "strict_ratios_exact": stated_ratios == expected_ratios
        and all(ratio < 1 for ratio in stated_ratios),
        "jacobian_bounds_exact": frac(
            nonvanishing.get("full_lifted_jacobian_modulus_lower", "0")
        )
        == Fraction(50176, 3352561)
        and frac(nonvanishing.get("stable_pinning_jacobian_modulus_lower", "0"))
        == Fraction(401408, 204506221)
        and c_upper == Fraction(1831, 224),
        "graph_exact": int(graph.get("state_edges", 0)) == 6
        and int(graph.get("branch_blocks", 0)) == 12
        and edge_pairs == expected_edges
        and graph.get("averaging_used") is False,
        "raw_sign_and_parity": raw.get("raw_trace_sign") == -1
        and raw.get("scalar_variable_order") == ["x", "m", "u"]
        and raw.get("tangent_fibre_basis") == ["e_x", "e_y", "e_m"]
        and raw.get("product_contour_order") == "dx*dm*du"
        and raw.get("product_orientation") == "dx wedge dm wedge du"
        and raw.get("all_word_kernel_trace_proved") is False
        and exterior.get("supertrace_parity") == "(-1)^(k+1)"
        and exponent_values == [-1, 1, -1, 1]
        and exterior.get("alternating_quotient") == "D_inst=D_1*D_3/(D_0*D_2)",
        "chronology_mutation": chronology.get("forward_trace") == 12
        and chronology.get("reversed_trace") == -27
        and chronology.get("mutation_detected") is True
        and chronology.get("averaging_used") is False,
        "nuclear_scope": nuclear.get("nuclear_order") == "OPEN"
        and nuclear.get("all_ratios_below_one") is True
        and nuclear.get("exact_ratio_regression_pass") is True
        and nuclear.get("nuclearity_pass") is False
        and nuclear.get("factorization_status")
        == "OPEN: enlarged intermediate spaces and an output-z restriction have not been constructed"
        and nuclear.get("alternating_product_scope")
        == "conditional meromorphic germ on C^2; no continuation is proved",
        "decision_scope": decisions.get("all_operator_theorem_gates_pass") is False
        and decisions.get("exact_algebraic_regression_checks_pass") is True
        and decisions.get("g0_conceptual_novelty_pass") is False
        and decisions.get("g2_all_word_kernel_composition_pass") is False
        and decisions.get("g3_nuclear_order_zero_pass") is False
        and decisions.get("g4_all_period_nuclear_supertrace_pass") is False
        and decisions.get("g5_meromorphic_continuation_pass") is False
        and decisions.get("promotion_pass") is False
        and decisions.get("lineage_status")
        == "CLOSED_AS_CONDITIONAL_BLUEPRINT_AFTER_THEOREM_AUDIT",
    }
    checks.update(algebra_checks())
    return checks


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    checks = audit(certificate)
    output = {
        "material_passport": {
            "id": "HCS-C22G-INDEPENDENT-CHECK-V1",
            "type": "nonimporting_exact_checker",
            "determinism": "exact rational and symbolic; no random seed",
        },
        "certificate": str(args.certificate),
        "certificate_sha256": sha256(args.certificate),
        "checks": checks,
        "all_checks_pass": all(checks.values()),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["all_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
