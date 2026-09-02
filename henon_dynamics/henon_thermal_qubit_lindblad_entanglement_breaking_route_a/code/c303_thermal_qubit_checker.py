#!/usr/bin/env python3
"""Independent strict checker for HCS-C303; importing the producer is forbidden."""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c303_thermal_qubit_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C303/2026-09-02.yaml"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "evaluation_file_sha256", "model",
    "theorem_contract", "proof_contract", "route_a", "scope_flags", "nonclaims",
    "collision_boundary", "references", "boundary_rows", "choi_exact_rows",
    "liouvillian_rows", "trace_contraction_rows", "semigroup_rows", "threshold_rows",
    "summary", "payload_sha256",
}


def reject_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON number: {value}")


def strict_json(path: Path) -> dict:
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON top level must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("non-string or duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchor/alias forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level must be mapping")
    return value


def exact_tree_equal(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree_equal(actual[k], expected[k]) for k in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree_equal(a, b) for a, b in zip(actual, expected))
    return actual == expected


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def frac(text: str) -> Fraction:
    if type(text) is not str or text.count("/") != 1:
        raise TypeError("canonical rational string required")
    n, d = text.split("/")
    value = Fraction(int(n), int(d))
    if f"{value.numerator}/{value.denominator}" != text:
        raise ValueError("noncanonical rational")
    return value


FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Liouvillian eigenvalues and Choi determinants are finite-dimensional source data, not prime norms or target spectral zeros.",
    "The dissipative GKSL generator is not asserted to be a Hilbert--Polya operator.",
    "No priority claim is made for GKSL, Choi, PPT, or entanglement-breaking channel theory.",
]
REFERENCE_IDS = [
    "10.1063/1.522979", "10.1007/BF01608499", "10.1016/0024-3795(75)90075-0",
    "10.1142/S0129055X03001709", "10.1016/S0375-9601(96)00706-2",
]
COLLISION = {
    "C223": "closed unitary Jaynes--Cummings excitation blocks, not a dissipative qubit channel semigroup",
    "C224": "nonautonomous unitary Landau--Zener scattering, not a time-homogeneous GKSL flow",
    "C237": "classical Kramers Ornstein--Uhlenbeck dynamics, not a CPTP density-matrix channel",
    "C243": "nonlinear Hamiltonian Bose--Josephson Bloch-sphere motion, not affine Bloch-ball contraction",
    "C297": "non-CPTP PT-symmetric gain/loss ray dynamics, not trace-preserving positive density evolution",
    "C298": "Grassmann projection gradient flow, not an open-quantum semigroup",
    "proves_too_much_guard": "finite Choi or characteristic polynomials do not imply an arithmetic determinant or target zero set",
}
EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C303",
    "title": "Exact thermal qubit Lindblad semigroup and entanglement-breaking threshold",
    "evaluation_date": "2026-09-02", "source_commit": SOURCE, "fixed_epoch": EPOCH,
    "scope_literal": SCOPE, "evaluator_authority": "route-a-evaluator", "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR, "obstruction_id": "HEN-O287",
    "candidate_definition": "A qubit GKSL semigroup with thermal excitation, relaxation, Hamiltonian phase rotation, and pure dephasing in the rate-gamma_phi convention.",
    "family": "finite-dimensional phase-covariant open quantum dynamics",
    "phase_space": "qubit density matrices, equivalently the closed Bloch ball",
    "dynamics": "completely positive trace-preserving GKSL semigroup",
    "parameters": "gamma_down>=0; gamma_up>=0; gamma_phi>=0; omega real; t>=0",
    "parameter_provenance": "the theorem covers the full nonnegative rate cone and every degenerate face",
    "arithmetic_origin": "none; all rates, Choi data, and Liouvillian eigenvalues are source-local quantum-channel data",
    "clock": "continuous physical time t",
    "normalization": "normalized Choi state uses the unit vector (|00>+|11>)/sqrt(2)",
    "determinant_convention": "characteristic polynomial is det(lambda I minus L); Choi PPT uses partial transpose on the input factor",
    "orbit_cutoff": "global all-parameter theorem; finite tables are regression evidence only",
    "precision": "exact rational cells plus deterministic high-precision threshold enclosures",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c303_thermal_qubit_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": {"verdict": "A0_FAIL", "evidence_status": "exact negative classification", "strongest_evidence": "the channel has an exact finite Choi matrix and a finite Liouvillian spectrum", "strongest_failure": "no arithmetic local datum or target Euler factor is constructed", "artifacts": ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"]},
    "a1": {"verdict": "A1_FAIL", "evidence_status": "strict contraction obstruction with complete unitary-boundary audit", "strongest_evidence": "the full semigroup and all recurrence degeneracies are solved exactly", "strongest_failure": "positive damping excludes nonconstant recurrence and the unitary face has only one tunable frequency", "artifacts": ["THEOREM_PACKAGE.md", "paper/main.pdf"]},
    "a2": {"verdict": "A2_FAIL", "evidence_status": "exact negative classification", "strongest_evidence": "continuous time produces exponential decay and phase weights", "strongest_failure": "physical time is not an arithmetic logarithmic prime clock", "artifacts": ["THEOREM_PACKAGE.md"]},
    "a3": {"verdict": "A3_FAIL", "evidence_status": "exact negative classification", "strongest_evidence": "Choi and Liouvillian determinants are finite polynomials", "strongest_failure": "no target completed function, divisor, functional equation, or zero set is present", "artifacts": ["THEOREM_PACKAGE.md", "results/c303_thermal_qubit_evidence.json"]},
    "a4": {"verdict": "A4_FORMAL_HINT", "evidence_status": "analogy only", "strongest_evidence": "the generator gives an exact spectral decomposition of a quantum dynamical semigroup", "strongest_failure": "a dissipative CPTP generator is not a certified same-clock self-adjoint Hilbert--Polya operator", "artifacts": ["SOURCE_AUDIT.md", "paper/main.pdf"]},
    "tuple": TUPLE, "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS, "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; the semigroup, spectrum, contraction coefficient, Choi criterion, threshold, and boundaries are analytic",
    "source_owner_tokens": REFERENCE_IDS,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = 0

    def need(condition):
        nonlocal checks
        assert condition
        checks += 1

    need(set(data) == TOP_KEYS)
    need(data["schema"] == "hcs-c303-thermal-qubit-lindblad-v1")
    need(data["candidate_id"] == "HCS-C303" and data["obstruction_id"] == "HEN-O287")
    need(data["evaluation_date"] == "2026-09-02")
    need(data["source_commit"] == SOURCE and type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH)
    need(data["scope_literal"] == SCOPE)
    need(exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}))
    need(data["evaluation_file_sha256"] == hashlib.sha256(EVALUATION.read_bytes()).hexdigest())
    need(type(data["payload_sha256"]) is str and data["payload_sha256"] == payload_hash(data))
    need(set(data["model"]) == {"basis", "sigma_z", "generator", "dephasing_convention", "Gamma1", "Gamma2"})
    need(data["model"]["dephasing_convention"] == "the isolated coherence decay rate is gamma_phi")
    need("(gamma_phi/2)" in data["model"]["generator"])
    need(data["model"]["Gamma2"] == "Gamma1/2+gamma_phi")
    need(set(data["theorem_contract"]) == {"population", "coherence", "liouvillian_spectrum", "trace_contraction", "choi_ppt", "threshold"})
    need(data["theorem_contract"]["coherence"] == "rho_01(t)=exp((-Gamma2+i*omega)*t)rho_01(0)")
    need(data["theorem_contract"]["choi_ppt"] == "p(1-p)(1-eta)^2>=eta^q")
    need(set(data["proof_contract"]) == {"complete_positivity", "ppt_equivalence", "threshold_uniqueness", "no_recurrence", "diagonalizability"})
    need(exact_tree_equal(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}))
    need(exact_tree_equal(data["scope_flags"], FLAGS))
    need(exact_tree_equal(data["nonclaims"], NONCLAIMS))
    need(exact_tree_equal(data["collision_boundary"], COLLISION))
    need("finite Choi" in data["collision_boundary"]["proves_too_much_guard"])
    need(type(data["references"]) is list and len(data["references"]) == 5)
    need([row["identifier"] for row in data["references"]] == REFERENCE_IDS)
    for row in data["references"]:
        need(set(row) == {"identifier", "owner", "role"} and all(type(v) is str for v in row.values()))

    need(type(data["choi_exact_rows"]) is list and len(data["choi_exact_rows"]) == 75)
    for row in data["choi_exact_rows"]:
        need(set(row) == {"p", "eta", "q", "a", "b", "d", "e", "coherence_abs_squared", "choi_corner_minor", "ppt_middle_minor", "choi_positive", "entanglement_breaking"})
        p, eta, q = frac(row["p"]), frac(row["eta"]), row["q"]
        need(0 <= p <= 1 and 0 <= eta <= 1 and type(q) is int and q in {1, 2, 3})
        a, b = 1 - p * (1 - eta), p * (1 - eta)
        d, e, k = (1 - p) * (1 - eta), eta + p * (1 - eta), eta ** q
        expected = [a, b, d, e, k, a * e - k, b * d - k]
        need([frac(row[x]) for x in ["a", "b", "d", "e", "coherence_abs_squared", "choi_corner_minor", "ppt_middle_minor"]] == expected)
        need(type(row["choi_positive"]) is bool and row["choi_positive"] == (a * e - k >= 0))
        need(type(row["entanglement_breaking"]) is bool and row["entanglement_breaking"] == (b * d - k >= 0))
        need(a + b == 1 and d + e == 1)

    need(type(data["liouvillian_rows"]) is list and len(data["liouvillian_rows"]) == 12)
    for row in data["liouvillian_rows"]:
        need(set(row) == {"gamma_down", "gamma_up", "gamma_phi", "omega", "Gamma1", "Gamma2", "characteristic_coefficients_descending", "diagonalizable", "stationary_dimension"})
        gd, gu, gp, w = [frac(row[x]) for x in ["gamma_down", "gamma_up", "gamma_phi", "omega"]]
        g1, g2 = gd + gu, (gd + gu) / 2 + gp
        c = g2 * g2 + w * w
        expected = [Fraction(1), 2 * g2 + g1, c + 2 * g1 * g2, g1 * c, Fraction(0)]
        need(frac(row["Gamma1"]) == g1 and frac(row["Gamma2"]) == g2)
        need([frac(x) for x in row["characteristic_coefficients_descending"]] == expected)
        need(type(row["diagonalizable"]) is bool and row["diagonalizable"] is True)
        expected_kernel = 4 if g1 == 0 and gp == 0 and w == 0 else (2 if g1 == 0 else 1)
        need(type(row["stationary_dimension"]) is int and row["stationary_dimension"] == expected_kernel)

    need(type(data["trace_contraction_rows"]) is list and len(data["trace_contraction_rows"]) == 10)
    for row in data["trace_contraction_rows"]:
        need(set(row) == {"gamma_down", "gamma_up", "gamma_phi", "Gamma1", "Gamma2", "winning_axis", "coefficient_formula", "strict_for_positive_t"})
        gd, gu, gp = [frac(row[x]) for x in ["gamma_down", "gamma_up", "gamma_phi"]]
        g1, g2 = gd + gu, (gd + gu) / 2 + gp
        winner = "transverse" if g2 < g1 else ("longitudinal" if g1 < g2 else "tie")
        need(frac(row["Gamma1"]) == g1 and frac(row["Gamma2"]) == g2 and row["winning_axis"] == winner)
        need(row["coefficient_formula"] == "max(exp(-Gamma1*t),exp(-Gamma2*t))")
        need(type(row["strict_for_positive_t"]) is bool and row["strict_for_positive_t"] is True and g1 > 0 and g2 > 0)

    need(type(data["semigroup_rows"]) is list and len(data["semigroup_rows"]) == 12)
    for row in data["semigroup_rows"]:
        need(set(row) == {"p", "eta1", "eta2", "eta_composed", "translation_composed", "translation_two_step"})
        p, e1, e2 = frac(row["p"]), frac(row["eta1"]), frac(row["eta2"])
        need(frac(row["eta_composed"]) == e1 * e2)
        need(frac(row["translation_composed"]) == p * (1 - e1 * e2))
        need(frac(row["translation_two_step"]) == p * (1 - e2) + e2 * p * (1 - e1))

    getcontext().prec = 100
    need(type(data["threshold_rows"]) is list and len(data["threshold_rows"]) == 8)
    for row in data["threshold_rows"]:
        need(set(row) == {"p", "q", "eta_lower", "eta_upper", "eta_mid", "dimensionless_Gamma1_t", "residual_abs_bound"})
        p_f, q = frac(row["p"]), row["q"]
        need(0 < p_f < 1 and type(q) is int and q >= 1)
        p, lo, hi, mid = Decimal(p_f.numerator) / Decimal(p_f.denominator), Decimal(row["eta_lower"]), Decimal(row["eta_upper"]), Decimal(row["eta_mid"])
        r = p * (1 - p)
        fun = lambda x: r * (1 - x) ** 2 - x ** q
        need(Decimal(0) < lo < mid < hi < Decimal(1))
        need(fun(lo) >= 0 and fun(hi) <= 0 and hi - lo < Decimal("1e-70"))
        need(abs(mid - (lo + hi) / 2) < Decimal("1e-70"))
        need(abs(Decimal(row["dimensionless_Gamma1_t"]) + mid.ln()) < Decimal("1e-70"))
        need(Decimal(row["residual_abs_bound"]) < Decimal("1e-70"))

    need(type(data["boundary_rows"]) is list and len(data["boundary_rows"]) == 7)
    for row in data["boundary_rows"]:
        need(set(row) == {"face", "stationary", "finite_EB", "recurrence"})
        need(type(row["finite_EB"]) is bool and all(type(row[x]) is str for x in ["face", "stationary", "recurrence"]))
    need(data["boundary_rows"][1]["finite_EB"] is False and data["boundary_rows"][2]["finite_EB"] is False)
    need("periodic" in data["boundary_rows"][4]["recurrence"])

    summary = data["summary"]
    need(set(summary) == {"choi_exact_cells", "liouvillian_cases", "trace_cases", "semigroup_cases", "threshold_cases", "boundary_faces", "audited_rows"})
    expected_summary = {"choi_exact_cells": 75, "liouvillian_cases": 12, "trace_cases": 10, "semigroup_cases": 12, "threshold_cases": 8, "boundary_faces": 7, "audited_rows": 124}
    need(exact_tree_equal(summary, expected_summary) and all(type(v) is int for v in summary.values()))

    route_yaml = strict_yaml(EVALUATION)
    need(exact_tree_equal(route_yaml, EXPECTED_EVALUATION))
    need(semantic_hash(route_yaml) == semantic_hash(EXPECTED_EVALUATION))
    print(f"C303 independent thermal-qubit checker: PASS ({checks} assertions; producer import forbidden; strict JSON/YAML exact tree)")


if __name__ == "__main__":
    main()
