#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C304."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c304_ch_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C304/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
MODEL = {
    "phase_space": "mean-zero L2 on the 2pi-periodic d-torus for every finite integer d>=1",
    "generator": "A_{kappa,alpha}=-kappa Delta^2-alpha Delta with domain H^4 intersect L2_0",
    "parameters": "kappa>0 and alpha real",
    "clock": "physical semigroup time t>=0",
}
THEOREM = {
    "semigroup": "self-adjoint analytic trace-class semigroup for every positive time",
    "spectrum": "sigma_n=alpha n-kappa n^2 with multiplicity r_d(n) on every represented shell n=|k|^2>0",
    "energy": "F=one-half integral(kappa|grad u|^2-alpha u^2) and Fdot=-norm(grad chemical_potential)^2",
    "atlas": "strict stability, critical kernel, spinodal Morse index, fastest represented ties, and actual-support long-time projection",
    "recurrence": "every recurrent state is stationary; there is no nonstationary periodic solution",
    "singular_boundary": "at kappa=0: forward heat for alpha<0, identity for alpha=0, no bounded L2 C0 semigroup for alpha>0",
}
PROOF = {
    "full_dimension": "Fourier diagonalization and lattice-shell multiplicities prove the theorem for every finite d>=1.",
    "fastest_exhaustion": "If alpha/kappa<=1 then shell n=1 is maximal; if alpha/kappa>1 then every n>=alpha/kappa has nonpositive rate while shell n=1 is positive, so only represented n below that bound can maximize.",
    "finite_role": "Finite dimensions and shells are regression receipts only and do not prove the arbitrary-d theorem.",
    "nonlinear_firewall": "The linearized equation does not imply nonlinear saturation, coarsening, or pattern selection.",
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Lattice wavevectors and shell multiplicities are source Fourier geometry, not rational-prime labels or target coefficients.",
    "The self-adjoint source generator is not asserted to be a Hilbert--Polya operator.",
    "No literature novelty or priority is claimed for the classical Cahn--Hilliard linearization or Fourier semigroup.",
]
COLLISION = {
    "C206_C213_C217_C218_C261_C277": "Earlier Fourier packages have different transport, hyperbolic, dispersive, fractional, or damping generators; C304 is the fourth-order spinodal shell and energy-signature atlas.",
    "C195": "C195 is nonlinear periodic viscous Burgers through Cole--Hopf; C304 is a linear fourth-order conserved gradient flow in every finite dimension.",
}
REFERENCES = [
    {"identifier": "10.1063/1.1744102", "role": "historical free-energy owner attribution only"},
    {"identifier": "10.1016/0001-6160(61)90182-1", "role": "historical spinodal-decomposition owner attribution only"},
    {"identifier": "10.1007/BF00251803", "role": "classical Cahn--Hilliard analysis context only"},
]
BOUNDARIES = [
    {"boundary_id": "B0-constant-mode", "statement": "On full L2 the zero Fourier mode is stationary and equals the conserved spatial mean."},
    {"boundary_id": "B1-critical-shell", "statement": "At alpha=kappa exactly the represented shell n=1 is neutral and has real dimension 2d."},
    {"boundary_id": "B2-shell-tie", "statement": "Every fastest-shell tie is retained as a full spectral projection rather than broken numerically."},
    {"boundary_id": "B3-kappa-zero", "statement": "The kappa=0 face is forward heat for alpha<0, identity for alpha=0, and ill posed as a bounded L2 semigroup for alpha>0."},
    {"boundary_id": "B4-nonlinear-exclusion", "statement": "No cubic Cahn--Hilliard dynamics, nonlinear saturation, phase coarsening, or pattern-selection theorem is claimed."},
    {"boundary_id": "B5-dimension", "statement": "The theorem holds for every finite integer d>=1; finite receipts only audit dimensions one through six."},
]
CASE_SPECS = [
    ("D1-STABLE-NEG", 1, "1", "-1"), ("D1-CRITICAL", 1, "1", "1"),
    ("D1-SQUARE-TIE", 1, "1", "5"), ("D2-STABLE-HALF", 2, "2", "1"),
    ("D2-CRITICAL", 2, "1", "1"), ("D2-FIRST-TIE", 2, "1", "3"),
    ("D3-BIHARMONIC", 3, "1", "0"), ("D3-CRITICAL", 3, "1", "1"),
    ("D3-SPINODAL", 3, "2", "7"), ("D4-STABLE-NEG", 4, "2", "-1"),
    ("D4-CRITICAL", 4, "2", "2"), ("D4-FIRST-TIE", 4, "2", "6"),
    ("D5-STABLE", 5, "3", "2"), ("D5-CRITICAL", 5, "3", "3"),
    ("D5-SPINODAL", 5, "3", "15"), ("D6-STABLE-NEG", 6, "1", "-2"),
    ("D6-CRITICAL", 6, "1", "1"), ("D6-HALF-RATIO", 6, "2", "13"),
]
SUPPORT_SPECS = [
    ("P1-D1-TIED", 1, "1", "5", [(1, "1"), (4, "2"), (9, "-1")]),
    ("P2-D2-TIED", 2, "1", "3", [(1, "2"), (2, "1"), (4, "3")]),
    ("P3-D3-UNIQUE", 3, "2", "7", [(1, "1"), (2, "-2"), (3, "3")]),
    ("P4-D4-STABLE", 4, "2", "-1", [(1, "3"), (2, "1")]),
    ("P5-D5-NEUTRAL", 5, "3", "3", [(1, "2"), (2, "-1")]),
    ("P6-D6-ACTUAL-SUPPORT", 6, "2", "13", [(1, "1"), (3, "4"), (4, "-2"), (5, "1")]),
]


def route_branch(verdict, status, evidence, failure, artifacts):
    return {"verdict": verdict, "evidence_status": status, "strongest_evidence": evidence, "strongest_failure": failure, "artifacts": artifacts}


EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C304",
    "title": "Full-dimensional linear periodic Cahn--Hilliard spinodal semigroup atlas",
    "evaluation_date": "2026-09-03",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O288",
    "candidate_definition": "The self-adjoint linear Cahn--Hilliard semigroup -kappa Delta^2-alpha Delta on every finite-dimensional 2pi-periodic torus, with kappa>0.",
    "family": "conserved fourth-order parabolic PDE and lattice-shell spectral dynamics",
    "phase_space": "mean-zero L2(T^d) for every finite integer d>=1",
    "dynamics": "partial_t u=-kappa Delta^2 u-alpha Delta u",
    "parameters": "d>=1 finite, kappa>0, alpha real",
    "parameter_provenance": "all coefficients and wavevectors are source PDE data",
    "arithmetic_origin": "none; lattice shells are Fourier geometry, not rational-prime data",
    "clock": "physical semigroup time t>=0",
    "normalization": "2pi-periodic torus and mean-zero sector; general side length follows by scaling",
    "determinant_convention": "none; no target or source Fredholm determinant is constructed",
    "orbit_cutoff": "one arbitrary-d theorem; finite shell rows are regression evidence only",
    "precision": "canonical rational rates and 72-digit trace-term receipts",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c304_ch_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": route_branch("A0_FAIL", "exact negative classification", "all shell and energy data are source Fourier data", "no rational-prime local datum or target Euler factor is constructed", ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"]),
    "a1": route_branch("A1_FAIL", "exact recurrence classification", "every recurrent state is stationary", "the real diagonal semigroup has no nonstationary primitive periodic orbit ledger", ["THEOREM_PACKAGE.md", "paper/main.pdf"]),
    "a2": route_branch("A2_FAIL", "exact negative classification", "physical time orders exponential Fourier evolution", "physical semigroup time is not a logarithmic rational-prime clock", ["THEOREM_PACKAGE.md"]),
    "a3": route_branch("A3_FAIL", "exact negative classification", "the trace-class heat evolution has an exact source spectral sum", "no target determinant, completed function, or functional equation is constructed", ["results/c304_ch_evidence.json", "paper/main.pdf"]),
    "a4": route_branch("A4_FORMAL_HINT", "source self-adjoint structure only", "the fourth-order generator is self-adjoint with compact resolvent", "its shell spectrum is not certified as a Hilbert--Polya spectrum and no target zero match exists", ["SOURCE_AUDIT.md", "paper/main.pdf"]),
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; the arbitrary-dimensional semigroup theorem is analytic",
    "source_owner_tokens": ["10.1063/1.1744102", "10.1016/0001-6160(61)90182-1", "10.1007/BF00251803"],
}


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML mapping keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return value


def duplicate_rejector(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_rejector, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    return value


def exact_tree(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree(a, e) for a, e in zip(actual, expected))
    return actual == expected


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


RATIONAL_RE = re.compile(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?")
DECIMAL_RE = re.compile(r"-?(?:0|[1-9][0-9]*)\.[0-9]+(?:e[+-]?[1-9][0-9]*)?")


def canonical_fraction(text) -> Fraction:
    if type(text) is not str or RATIONAL_RE.fullmatch(text) is None:
        raise ValueError(f"invalid rational receipt: {text!r}")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational receipt: {text}")
    return value


def canonical_decimal(text, expected: mp.mpf) -> mp.mpf:
    if type(text) is not str or DECIMAL_RE.fullmatch(text) is None:
        raise ValueError(f"invalid decimal receipt: {text!r}")
    canonical = "0.0" if expected == 0 else mp.nstr(expected, 72, strip_zeros=False)
    if text != canonical:
        raise ValueError(f"noncanonical decimal receipt: {text}")
    return mp.mpf(text)


def shells(dimension: int, maximum: int) -> list[int]:
    one = [0] * (maximum + 1)
    radius = int(maximum**0.5)
    for coordinate in range(-radius, radius + 1):
        one[coordinate * coordinate] += 1
    result = [1] + [0] * maximum
    for _ in range(dimension):
        updated = [0] * (maximum + 1)
        for previous_n, previous_count in enumerate(result):
            for square_n, square_count in enumerate(one[: maximum - previous_n + 1]):
                updated[previous_n + square_n] += previous_count * square_count
        result = updated
    return result


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C304 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data, evaluation = strict_json(args.evidence), strict_yaml(args.evaluation)
    count = 0

    def ok(condition, label):
        nonlocal count
        if not bool(condition):
            raise AssertionError(label)
        count += 1

    ok(set(data) == {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract", "route_a", "scope_flags", "nonclaims", "collision_boundary", "references", "enumeration", "cases", "support_probes", "kappa_zero_boundary", "boundaries", "payload_sha256"}, "exact evidence root keys")
    ok(data["payload_sha256"] == payload_hash(data), "canonical payload self-hash")
    ok(type(data["payload_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload hash type")
    ok(type(data["schema"]) is str and data["schema"] == "hcs-c304-linear-cahn-hilliard-v1", "schema")
    ok(type(data["candidate_id"]) is str and data["candidate_id"] == "HCS-C304", "candidate")
    ok(type(data["obstruction_id"]) is str and data["obstruction_id"] == "HEN-O288", "obstruction")
    ok(type(data["evaluation_date"]) is str and data["evaluation_date"] == "2026-09-03", "date")
    ok(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH, "epoch")
    ok(type(data["source_commit"]) is str and data["source_commit"] == SOURCE, "source")
    ok(type(data["scope_literal"]) is str and data["scope_literal"] == SCOPE, "scope")
    ok(exact_tree(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}), "evaluator")
    ok(exact_tree(data["model"], MODEL), "exact model tree")
    ok(exact_tree(data["theorem_contract"], THEOREM), "exact theorem tree")
    ok(exact_tree(data["proof_contract"], PROOF), "exact proof tree")
    ok(exact_tree(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}), "route tree")
    ok(exact_tree(data["scope_flags"], FLAGS), "scope flags")
    ok(exact_tree(data["nonclaims"], NONCLAIMS), "nonclaims")
    ok(exact_tree(data["collision_boundary"], COLLISION), "collision")
    ok(exact_tree(data["references"], REFERENCES), "references")
    ok(exact_tree(data["boundaries"], BOUNDARIES), "boundaries")

    enumeration = data["enumeration"]
    ok(type(enumeration) is dict and set(enumeration) == {"case_count", "case_ids", "shell_rows_per_case", "shell_row_count", "support_probe_count", "kappa_zero_rows", "boundary_rows", "audited_cell_count"}, "enumeration keys")
    expected_ids = [spec[0] for spec in CASE_SPECS]
    ok(type(enumeration["case_ids"]) is list and enumeration["case_ids"] == expected_ids and len(set(enumeration["case_ids"])) == 18, "ordered unique case ids")
    for key, expected in (("case_count", 18), ("shell_rows_per_case", 12), ("shell_row_count", 216), ("support_probe_count", 6), ("kappa_zero_rows", 3), ("boundary_rows", 6)):
        ok(type(enumeration[key]) is int and enumeration[key] == expected, f"enumeration {key}")

    cases = data["cases"]
    ok(type(cases) is list and len(cases) == 18, "case list")
    ok([case.get("case_id") for case in cases] == expected_ids and len({case.get("case_id") for case in cases}) == 18, "case ids")
    for case, spec in zip(cases, CASE_SPECS):
        case_id, dimension, kappa_text, alpha_text = spec
        ok(type(case) is dict and set(case) == {"case_id", "dimension", "kappa", "alpha", "ratio_alpha_over_kappa", "analytic_exhaustion_cutoff", "chamber", "unstable_shells", "neutral_shells", "morse_index", "kernel_dimension", "fastest_shells", "spectral_bound", "shell_rows"}, f"{case_id} keys")
        ok(type(case["case_id"]) is str and case["case_id"] == case_id, f"{case_id} id")
        ok(type(case["dimension"]) is int and not isinstance(case["dimension"], bool) and case["dimension"] == dimension, f"{case_id} dimension")
        kappa, alpha = canonical_fraction(case["kappa"]), canonical_fraction(case["alpha"])
        ok(kappa == Fraction(kappa_text) and alpha == Fraction(alpha_text) and kappa > 0, f"{case_id} parameters")
        ok(canonical_fraction(case["ratio_alpha_over_kappa"]) == alpha / kappa, f"{case_id} ratio")
        ratio = alpha / kappa
        cutoff = 1 if ratio <= 1 else math.ceil(ratio)
        ok(type(case["analytic_exhaustion_cutoff"]) is int and not isinstance(case["analytic_exhaustion_cutoff"], bool) and case["analytic_exhaustion_cutoff"] == cutoff, f"{case_id} analytic cutoff")
        counts = shells(dimension, max(12, cutoff))
        represented = [n for n in range(1, cutoff + 1) if counts[n] > 0]
        rates = {n: alpha * n - kappa * n * n for n in represented}
        unstable = [n for n in represented if rates[n] > 0]
        neutral = [n for n in represented if rates[n] == 0]
        spectral_bound = max(rates.values())
        fastest = [n for n in represented if rates[n] == spectral_bound]
        chamber = "spinodal_unstable" if unstable else "critical_neutral" if neutral else "strictly_stable"
        ok(type(case["chamber"]) is str and case["chamber"] == chamber, f"{case_id} chamber")
        ok(type(case["unstable_shells"]) is list and all(type(n) is int for n in case["unstable_shells"]) and case["unstable_shells"] == unstable, f"{case_id} unstable")
        ok(type(case["neutral_shells"]) is list and all(type(n) is int for n in case["neutral_shells"]) and case["neutral_shells"] == neutral, f"{case_id} neutral")
        ok(type(case["morse_index"]) is int and not isinstance(case["morse_index"], bool) and case["morse_index"] == sum(counts[n] for n in unstable), f"{case_id} Morse index")
        ok(type(case["kernel_dimension"]) is int and not isinstance(case["kernel_dimension"], bool) and case["kernel_dimension"] == sum(counts[n] for n in neutral), f"{case_id} kernel")
        ok(type(case["fastest_shells"]) is list and all(type(n) is int for n in case["fastest_shells"]) and case["fastest_shells"] == fastest, f"{case_id} fastest")
        ok(canonical_fraction(case["spectral_bound"]) == spectral_bound, f"{case_id} bound")
        rows = case["shell_rows"]
        ok(type(rows) is list and len(rows) == 12, f"{case_id} rows")
        for n, row in enumerate(rows, 1):
            ok(type(row) is dict and set(row) == {"n", "multiplicity", "eigenvalue", "energy_coefficient", "classification", "trace_term_t_one_third"}, f"{case_id} row {n} keys")
            ok(type(row["n"]) is int and row["n"] == n, f"{case_id} row {n} n")
            ok(type(row["multiplicity"]) is int and not isinstance(row["multiplicity"], bool) and row["multiplicity"] == counts[n], f"{case_id} row {n} multiplicity")
            eigenvalue = alpha * n - kappa * n * n
            ok(canonical_fraction(row["eigenvalue"]) == eigenvalue, f"{case_id} row {n} eigenvalue")
            ok(canonical_fraction(row["energy_coefficient"]) == kappa * n - alpha, f"{case_id} row {n} energy")
            expected_class = "absent" if counts[n] == 0 else "unstable" if eigenvalue > 0 else "neutral" if eigenvalue == 0 else "stable"
            ok(type(row["classification"]) is str and row["classification"] == expected_class, f"{case_id} row {n} class")
            trace = mp.mpf(counts[n]) * mp.exp(mp.mpf(eigenvalue.numerator) / eigenvalue.denominator / 3)
            canonical_decimal(row["trace_term_t_one_third"], trace)
            ok(True, f"{case_id} row {n} canonical trace")

    probes = data["support_probes"]
    ok(type(probes) is list and len(probes) == 6, "probe list")
    ok([probe.get("probe_id") for probe in probes] == [spec[0] for spec in SUPPORT_SPECS], "probe ids")
    for probe, spec in zip(probes, SUPPORT_SPECS):
        probe_id, dimension, kappa_text, alpha_text, support = spec
        ok(type(probe) is dict and set(probe) == {"probe_id", "dimension", "kappa", "alpha", "support", "leading_shells", "leading_rate", "normalized_limit"}, f"{probe_id} keys")
        ok(type(probe["probe_id"]) is str and probe["probe_id"] == probe_id, f"{probe_id} id")
        ok(type(probe["dimension"]) is int and probe["dimension"] == dimension, f"{probe_id} d")
        kappa, alpha = canonical_fraction(probe["kappa"]), canonical_fraction(probe["alpha"])
        ok(kappa == Fraction(kappa_text) and alpha == Fraction(alpha_text), f"{probe_id} parameters")
        rows = probe["support"]
        ok(type(rows) is list and len(rows) == len(support), f"{probe_id} support list")
        rates = {}
        for row, (n, coefficient) in zip(rows, support):
            ok(type(row) is dict and set(row) == {"n", "coefficient", "rate"}, f"{probe_id} support keys")
            ok(type(row["n"]) is int and row["n"] == n, f"{probe_id} support n")
            ok(canonical_fraction(row["coefficient"]) == Fraction(coefficient) and Fraction(coefficient) != 0, f"{probe_id} coefficient")
            rates[n] = alpha * n - kappa * n * n
            ok(canonical_fraction(row["rate"]) == rates[n], f"{probe_id} rate")
        lead_rate = max(rates.values())
        lead = [n for n, _ in support if rates[n] == lead_rate]
        ok(type(probe["leading_shells"]) is list and all(type(n) is int for n in probe["leading_shells"]) and probe["leading_shells"] == lead, f"{probe_id} leading")
        ok(canonical_fraction(probe["leading_rate"]) == lead_rate, f"{probe_id} leading rate")
        ok(type(probe["normalized_limit"]) is str and probe["normalized_limit"] == "projection_onto_all_leading_supported_shells", f"{probe_id} limit")

    boundary_rows = data["kappa_zero_boundary"]
    ok(type(boundary_rows) is list and len(boundary_rows) == 3, "kappa zero list")
    for row, alpha in zip(boundary_rows, (Fraction(-2), Fraction(0), Fraction(2))):
        ok(type(row) is dict and set(row) == {"alpha", "classification", "first_four_mode_rates", "spectrum_bounded_above"}, "kappa zero keys")
        ok(canonical_fraction(row["alpha"]) == alpha, "kappa zero alpha")
        expected_class = "forward_heat_semigroup" if alpha < 0 else "identity_semigroup" if alpha == 0 else "no_bounded_L2_C0_semigroup"
        ok(type(row["classification"]) is str and row["classification"] == expected_class, "kappa zero class")
        ok(type(row["first_four_mode_rates"]) is list and len(row["first_four_mode_rates"]) == 4 and [canonical_fraction(item) for item in row["first_four_mode_rates"]] == [alpha * n for n in range(1, 5)], "kappa zero rates")
        ok(type(row["spectrum_bounded_above"]) is bool and row["spectrum_bounded_above"] is (alpha <= 0), "kappa zero boundedness")

    audited = leaves(cases) + leaves(probes) + leaves(boundary_rows) + leaves(data["boundaries"])
    ok(type(enumeration["audited_cell_count"]) is int and enumeration["audited_cell_count"] == audited == 1653, "audited cells")
    ok(exact_tree(evaluation, EXPECTED_EVALUATION), "exact YAML semantic tree and types")
    print(f"C304 independent Cahn--Hilliard checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
