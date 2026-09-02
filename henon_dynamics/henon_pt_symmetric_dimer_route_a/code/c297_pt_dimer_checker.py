#!/usr/bin/env python3
"""Producer-independent exact schema and mathematics audit for HCS-C297."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c297_pt_dimer_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C297/2026-09-02.yaml"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
OBSTRUCTION = "HEN-O281"
ROUTE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
    "automorphy": False, "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_input": False,
}
MODEL = {
    "state_space": "nonzero vectors psi in C^2 and their projective rays",
    "equation": "i d_t psi=H_(gamma,kappa) psi with H=[[i gamma,kappa],[kappa,-i gamma]]",
    "parameters": "kappa>0 and gamma real; physical time t",
    "parity_time": "P=sigma_x and T is componentwise complex conjugation",
    "clock": "physical propagation time; no arithmetic or fitted target clock",
}
THEOREM = {
    "square": "H^2=(kappa^2-gamma^2) I gives the exact exponential in all three chambers",
    "unbroken": "if |gamma|<kappa, eigenvalues are real, generic rays have least period pi/sqrt(kappa^2-gamma^2), and vectors have least period twice that",
    "exceptional": "if |gamma|=kappa, H is nonzero rank-one nilpotent, the eigenline is unique, and generalized states grow linearly",
    "broken": "if |gamma|>kappa, the two projective fixed rays are attracting and repelling and generic vector norms have exponential envelopes",
    "metrics": "sigma_x is an all-parameter conserved indefinite form; eta=I+(gamma/kappa)sigma_y is positive definite exactly in the unbroken chamber and degenerates at the exceptional point",
    "projective": "z=psi_2/psi_1 obeys z_dot=i kappa(z^2-1)-2 gamma z and its complex quadratic discriminant is minus four times (kappa^2-gamma^2)",
    "boundaries": "gamma=0, kappa down to zero, both exceptional sheets, eigenrays, zero state, and vector-versus-ray periods are separated",
}
PROOF = {
    "exponential": "reduce every analytic power series to the basis I,H using the scalar square identity",
    "classification": "use the sign of delta=kappa^2-gamma^2 and the Jordan form at delta=0",
    "metric": "direct multiplication gives H^dagger eta=eta H and eta eigenvalues 1 plus or minus |gamma|/kappa",
    "projective": "differentiate the affine ratio and compactify the Riccati field on CP^1",
    "period": "the scalar exponential is plus or minus I at successive half turns; eigenrays are stationary and are excluded from the generic least-period statement",
    "finite_role": "the integer grid audits exact algebra, phase labels, metrics, and boundary incidence but is not the proof of the all-parameter theorem",
}
REFERENCES = [
    {
        "id": "BenderBoettcher1998",
        "title": "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry",
        "authors": "Carl M. Bender and Stefan Boettcher",
        "venue": "Physical Review Letters 80 (1998), 5243-5246",
        "identifier": "doi:10.1103/PhysRevLett.80.5243",
        "url": "https://doi.org/10.1103/PhysRevLett.80.5243",
        "ownership": "foundational PT-symmetric spectral context; not a priority claim for this two-mode calculation",
    },
    {
        "id": "Mostafazadeh2002",
        "title": "Pseudo-Hermiticity versus PT symmetry: The necessary condition for the reality of the spectrum of a non-Hermitian Hamiltonian",
        "authors": "Ali Mostafazadeh",
        "venue": "Journal of Mathematical Physics 43 (2002), 205-214",
        "identifier": "doi:10.1063/1.1418246",
        "url": "https://doi.org/10.1063/1.1418246",
        "ownership": "direct owner for positive-metric and pseudo-Hermitian interpretation",
    },
    {
        "id": "RuterEtAl2010",
        "title": "Observation of parity-time symmetry in optics",
        "authors": "Christian E. Rueter et al.",
        "venue": "Nature Physics 6 (2010), 192-195",
        "identifier": "doi:10.1038/nphys1515",
        "url": "https://doi.org/10.1038/nphys1515",
        "ownership": "physical balanced-gain/loss coupled-mode context",
    },
]
NONCLAIMS = [
    "the PT dimer, exceptional points, and pseudo-Hermitian metrics are established literature and are not claimed as newly discovered",
    "the positive metric exists only for |gamma|<kappa and is not continued through an exceptional point",
    "the standard Euclidean norm is not conserved when gamma is nonzero",
    "no arithmetic local data, target Euler factor, root number, automorphy, target zero match, Hilbert-Polya operator, or Route-B authorization is produced",
]
BOUNDARIES = [
    {"id": "hermitian_axis", "face": "gamma=0", "result": "H=kappa sigma_x and the standard norm as well as eta is conserved"},
    {"id": "positive_ep", "face": "gamma=kappa>0", "result": "H^2=0 with one eigenline and linear generalized evolution"},
    {"id": "negative_ep", "face": "gamma=-kappa<0", "result": "the second nilpotent sheet has the same Jordan classification"},
    {"id": "uncoupled_limit", "face": "kappa down to zero at gamma nonzero", "result": "the components amplify and decay independently; eta is not a positive metric"},
    {"id": "zero_generator", "face": "kappa=gamma=0 outside the frozen kappa>0 domain", "result": "every vector is fixed and there is no exceptional point"},
    {"id": "eigenrays", "face": "initial ray is an eigenray", "result": "it is projectively stationary and is excluded from the generic least-period claim"},
    {"id": "zero_vector", "face": "psi=0", "result": "the vector solution is fixed but does not define a projective state"},
    {"id": "period_convention", "face": "unbroken generic initial data", "result": "the ray period is pi/omega while the vector period is 2 pi/omega"},
]
EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C297",
    "obstruction_id": OBSTRUCTION,
    "evaluation_date": "2026-09-02", "source_commit": SOURCE,
    "fixed_epoch": EPOCH, "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR, "theorem_status": "PROVABLE AS STATED",
    "tuple": ROUTE, "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "axes": {
        "A0": "no arithmetic source owner", "A1": "exact clean projective periodic family only",
        "A2": "physical time is not an arithmetic clock", "A3": "no transfer or continuation bridge",
        "A4": "finite-dimensional pseudo-Hermitian formal hint only",
    },
    "scope_flags": FLAGS,
}


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value: str):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=reject_duplicate_keys, parse_constant=reject_constant)


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader retaining dates as strings and rejecting noncanonical maps."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or getattr(key_node, "value", None) == "<<":
            raise yaml.constructor.ConstructorError(None, None, "YAML merge keys are forbidden", key_node.start_mark)
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise yaml.constructor.ConstructorError(None, None, "YAML keys must be strings", key_node.start_mark)
        if key in result:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate YAML key: {key}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (AnchorToken, AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("evaluation YAML must be a mapping")
    return value


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_tree(value, expected, label: str, check) -> None:
    check(type(value) is type(expected), f"{label} exact type")
    if type(expected) is dict:
        check(set(value) == set(expected), f"{label} exact keys")
        for key in expected:
            exact_tree(value[key], expected[key], f"{label}.{key}", check)
    elif type(expected) is list:
        check(len(value) == len(expected), f"{label} exact length")
        for index, item in enumerate(expected):
            exact_tree(value[index], item, f"{label}[{index}]", check)
    else:
        check(value == expected, f"{label} exact value")


def expected_row(kappa: int, gamma: int) -> dict:
    delta = kappa * kappa - gamma * gamma
    chamber = "unbroken" if delta > 0 else "exceptional" if delta == 0 else "broken"
    return {
        "kappa": kappa, "gamma": gamma, "delta": delta, "phase": chamber,
        "trace_H": 0, "det_H": -delta, "H_square_scalar": delta,
        "rank_H": 1 if delta == 0 else 2,
        "projective_fixed_rays": 1 if delta == 0 else 2,
        "eta_scaled_determinant": delta,
        "eta_signature": "positive" if delta > 0 else "semidefinite" if delta == 0 else "indefinite",
        "projective_period_over_pi_squared": str(Fraction(1, delta)) if delta > 0 else None,
        "vector_period_over_two_pi_squared": str(Fraction(1, delta)) if delta > 0 else None,
        "krein_signature": ["negative", "positive"] if delta > 0 else [],
        "growth_rate_squared": -delta if delta < 0 else 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract", "route_a", "scope_flags", "enumeration", "phase_cells", "boundary_cells", "references", "nonclaims", "payload_sha256"}
    check(type(data) is dict and set(data) == top, "top-level closure")
    check(data["schema"] == "hcs-c297-pt-symmetric-dimer-v1" and data["candidate_id"] == "HCS-C297" and data["obstruction_id"] == OBSTRUCTION, "identity and obstruction")
    check(data["evaluation_date"] == "2026-09-02" and data["source_commit"] == SOURCE, "date/source")
    check(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH, "epoch exact int")
    check(data["scope_literal"] == SCOPE and data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "scope/evaluator")
    exact_tree(data["route_a"], {"tuple": ROUTE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route", check)
    check(data["scope_flags"] == FLAGS and all(type(v) is bool and v is False for v in data["scope_flags"].values()), "flags")
    check(type(data["payload_sha256"]) is str and data["payload_sha256"] == payload_hash(data), "payload hash")
    exact_tree(data["model"], MODEL, "model", check)
    exact_tree(data["theorem_contract"], THEOREM, "theorem", check)
    exact_tree(data["proof_contract"], PROOF, "proof", check)

    kappas = list(range(1, 9)); gammas = list(range(-10, 11))
    expected_rows = [expected_row(k, g) for k in kappas for g in gammas]
    check(type(data["phase_cells"]) is list and len(data["phase_cells"]) == len(expected_rows), "phase count")
    seen = set()
    for index, (row, expected) in enumerate(zip(data["phase_cells"], expected_rows)):
        exact_tree(row, expected, f"phase[{index}]", check)
        key = (row["kappa"], row["gamma"]); check(key not in seen, f"phase[{index}] unique"); seen.add(key)
        delta = row["delta"]
        check(row["trace_H"] ** 2 - 4 * row["det_H"] == 4 * delta, f"phase[{index}] characteristic discriminant")
        check(row["eta_scaled_determinant"] == row["kappa"] ** 2 - row["gamma"] ** 2, f"phase[{index}] metric determinant")
    check(seen == {(k, g) for k in kappas for g in gammas}, "grid closure")
    counts = {name: sum(row["phase"] == name for row in expected_rows) for name in ("unbroken", "exceptional", "broken")}
    expected_enum = {"kappa_values": kappas, "gamma_values": gammas, "grid_cells": 168, "boundary_cells": 8, "phase_counts": counts}
    exact_tree(data["enumeration"], expected_enum, "enumeration", check)

    exact_tree(data["boundary_cells"], BOUNDARIES, "boundary_cells", check)
    exact_tree(data["references"], REFERENCES, "references", check)
    exact_tree(data["nonclaims"], NONCLAIMS, "nonclaims", check)

    exact_tree(evaluation, EXPECTED_EVALUATION, "evaluation", check)
    semantic_raw = json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    semantic_hash = hashlib.sha256(semantic_raw.encode()).hexdigest()
    print(json.dumps({"status": "C297_CHECKER_PASS", "assertions": assertions, "grid_cells": len(expected_rows), "boundary_cells": 8, "evaluation_semantic_sha256": semantic_hash, "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
