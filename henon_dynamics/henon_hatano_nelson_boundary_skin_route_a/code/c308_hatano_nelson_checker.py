#!/usr/bin/env python3
"""Independent strict checker for HCS-C308; importing the producer is forbidden."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C308 checker requires assertions; python -O is forbidden")

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c308_hatano_nelson_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C308/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVALUATION_SHA = "742a34e17b7f9f5ddaaff5525e55c32cc7e67ffd8d5333e7253939a048dc0042"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "evaluation_file_sha256", "model",
    "theorem_contract", "proof_contract", "route_a", "scope_flags", "nonclaims",
    "collision_boundary", "references", "boundary_rows", "positive_obc_rows",
    "resolvent_rows", "one_sided_rows", "pbc_rows", "summary", "payload_sha256",
}
YAML_TOP_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
    "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
    "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
    "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
    "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
    "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
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
    if not n or not d or (n.startswith("+") or d.startswith(("+", "-"))):
        raise ValueError("invalid rational spelling")
    value = Fraction(int(n), int(d))
    if f"{value.numerator}/{value.denominator}" != text:
        raise ValueError("noncanonical rational")
    return value


def poly_step(p1: list[Fraction], p2: list[Fraction], product: Fraction) -> list[Fraction]:
    out = [Fraction(0)] * (len(p1) + 1)
    for i, value in enumerate(p1):
        out[i + 1] += value
    for i, value in enumerate(p2):
        out[i] -= product * value
    return out


def path_poly(n: int, product: Fraction) -> list[Fraction]:
    p0, p1 = [Fraction(1)], [Fraction(0), Fraction(1)]
    for _ in range(2, n + 1):
        p0, p1 = p1, poly_step(p1, p0, product)
    return p1 if n else p0


def poly_eval(coeffs: list[Fraction], z: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coeffs):
        value = value * z + coefficient
    return value


def matrix_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Fraction(0)) for j in range(n)] for i in range(n)]


def cyclic_matrix(n: int, tr: Fraction, tl: Fraction) -> list[list[Fraction]]:
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        out[j][(j + 1) % n] += tr
        out[j][(j - 1) % n] += tl
    return out


def expected_trace_powers(n: int, tr: Fraction, tl: Fraction) -> list[Fraction]:
    matrix = cyclic_matrix(n, tr, tl)
    power = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    out = []
    for _ in range(n):
        power = matrix_mul(power, matrix)
        out.append(sum((power[i][i] for i in range(n)), Fraction(0)))
    return out


FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_topological_invariant": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "No disorder localization, interaction effect, topological invariant, or topological edge mode is asserted.",
    "The finite non-Hermitian chain is not asserted to be a Hilbert--Polya operator.",
    "No priority claim is made for the Hatano--Nelson model, skin effect, or biorthogonal spectral theory.",
]
REFERENCE_IDS = ["10.1103/PhysRevLett.77.570", "10.1103/PhysRevB.58.8384", "10.1103/PhysRevLett.121.086803"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = 0

    def need(condition):
        nonlocal checks
        assert condition
        checks += 1

    need(set(data) == TOP_KEYS)
    need(data["schema"] == "hcs-c308-hatano-nelson-boundary-skin-v1")
    need(data["candidate_id"] == "HCS-C308" and data["obstruction_id"] == "HEN-O292")
    need(data["evaluation_date"] == "2026-09-03" and data["source_commit"] == SOURCE)
    need(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH)
    need(data["scope_literal"] == SCOPE)
    need(exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}))
    need(type(data["payload_sha256"]) is str and data["payload_sha256"] == payload_hash(data))
    need(data["evaluation_file_sha256"] == hashlib.sha256(args.evaluation.read_bytes()).hexdigest())
    route = strict_yaml(args.evaluation)
    need(hashlib.sha256(args.evaluation.read_bytes()).hexdigest() == EVALUATION_SHA)
    need(set(route) == YAML_TOP_KEYS)
    need(route["candidate_id"] == "HCS-C308" and route["obstruction_id"] == "HEN-O292")
    need(type(route["fixed_epoch"]) is int and route["fixed_epoch"] == EPOCH)
    need(exact_tree_equal(route["tuple"], TUPLE))
    need(route["overall_verdict"] == "ROUTE_A_REJECTED" and type(route["route_b_invocation_allowed"]) is bool and route["route_b_invocation_allowed"] is False)
    need(type(route["artifact_paths"]) is list and route["artifact_paths"] == ["results/c308_hatano_nelson_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"])
    need(exact_tree_equal(route["scope_flags"], FLAGS))
    need(route["source_owner_tokens"] == REFERENCE_IDS)
    for key in ["a0", "a1", "a2", "a3", "a4"]:
        need(set(route[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"})
        need(type(route[key]["artifacts"]) is list and all(type(x) is str for x in route[key]["artifacts"]))

    model = {
        "obc": "H[j,j+1]=t_R and H[j+1,j]=t_L",
        "positive_similarity": "D^{-1}HD=g*A_path with g=sqrt(t_R*t_L), q=sqrt(t_L/t_R), D=diag(1,q,...,q^(N-1))",
        "pbc": "H_per=t_R*C+t_L*C^{-1}, (Cv)_j=v_(j+1 mod N)",
        "time_evolution": "i*dpsi/dt=H*psi",
    }
    theorem = {
        "characteristic": "P_N(z)=g^N*U_N(z/(2g))",
        "obc_spectrum": "E_m=2g*cos(m*pi/(N+1))",
        "biorthogonal_basis": "R=D*S, L^T=S^T*D^{-1}, L^T*R=I",
        "condition_number": "kappa_2(R)=max(q,q^{-1})^(N-1)",
        "propagator": "exp(-itH)=D*S*diag(exp(-itE_m))*S^T*D^{-1}",
        "resolvent": "(zI-H)^{-1}=D*(zI-gA_path)^{-1}*D^{-1}",
        "pbc_spectrum": "t_R*exp(ik_m)+t_L*exp(-ik_m), k_m=2*pi*m/N",
        "one_sided": "OBC is one nilpotent N-Jordan block while PBC is a diagonalizable cyclic shift",
    }
    proof = {
        "similarity": "entrywise diagonal conjugation makes both OBC hoppings equal to g",
        "chebyshev": "continuant recurrence P_N=zP_(N-1)-t_R*t_L*P_(N-2)",
        "left_right": "orthogonality of the sine matrix gives the exact dual basis and condition number",
        "pbc_fourier": "the unitary discrete Fourier basis diagonalizes the cyclic shift",
        "jordan": "H^N=0, H^(N-1)!=0, and rank(H^k)=N-k on a one-sided OBC axis",
    }
    need(exact_tree_equal(data["model"], model))
    need(exact_tree_equal(data["theorem_contract"], theorem))
    need(exact_tree_equal(data["proof_contract"], proof))
    need(exact_tree_equal(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}))
    need(exact_tree_equal(data["scope_flags"], FLAGS))
    need(exact_tree_equal(data["nonclaims"], NONCLAIMS))
    expected_collision = {
        "C267": "a Hermitian infinite Wannier--Stark lattice, not a finite asymmetric-hopping OBC/PBC atlas",
        "C288": "a self-adjoint delta point interaction, not a nonnormal lattice with boundary-sensitive spectra",
        "C297": "PT-symmetric gain/loss ray dynamics, not asymmetric nearest-neighbor hopping",
        "C303": "a dissipative CPTP qubit semigroup, not nonnormal wave-amplitude evolution",
        "proves_too_much_guard": "finite Chebyshev determinants and boundary spectra do not imply arithmetic data, topology, disorder localization, or a target zero set",
    }
    need(exact_tree_equal(data["collision_boundary"], expected_collision))
    need("do not imply" in data["collision_boundary"]["proves_too_much_guard"])
    need(type(data["references"]) is list and len(data["references"]) == 3)
    need([x["identifier"] for x in data["references"]] == REFERENCE_IDS)
    for row in data["references"]:
        need(set(row) == {"identifier", "owner", "role"} and all(type(x) is str for x in row.values()))

    positive = data["positive_obc_rows"]
    need(type(positive) is list and len(positive) == 40)
    seen = set()
    for row in positive:
        need(set(row) == {"N", "t_R", "t_L", "g_squared", "q_squared", "characteristic_coefficients_descending", "determinant_at_zero", "kappa2_squared", "right_skin_edge", "simple_real_spectrum"})
        n, tr, tl = row["N"], frac(row["t_R"]), frac(row["t_L"])
        need(type(n) is int and 2 <= n <= 9 and tr > 0 and tl > 0)
        need((n, tr, tl) not in seen); seen.add((n, tr, tl))
        coeffs = path_poly(n, tr * tl)
        need(frac(row["g_squared"]) == tr * tl and frac(row["q_squared"]) == tl / tr)
        need(type(row["characteristic_coefficients_descending"]) is list and len(row["characteristic_coefficients_descending"]) == n + 1)
        need([frac(x) for x in row["characteristic_coefficients_descending"]] == list(reversed(coeffs)))
        need(frac(row["determinant_at_zero"]) == coeffs[0])
        need(frac(row["kappa2_squared"]) == (max(tr, tl) / min(tr, tl)) ** (n - 1))
        edge = "none" if tr == tl else ("left" if tl < tr else "right")
        need(row["right_skin_edge"] == edge)
        need(type(row["simple_real_spectrum"]) is bool and row["simple_real_spectrum"] is True)

    resolvents = data["resolvent_rows"]
    need(type(resolvents) is list and len(resolvents) == 21)
    seen = set()
    for row in resolvents:
        need(set(row) == {"N", "t_R", "t_L", "z", "det_zI_minus_H", "trace_resolvent", "outside_spectrum"})
        n, tr, tl, z = row["N"], frac(row["t_R"]), frac(row["t_L"]), frac(row["z"])
        need(type(n) is int and 2 <= n <= 8 and tr > 0 and tl > 0)
        need((n, tr, tl, z) not in seen); seen.add((n, tr, tl, z))
        coeffs = path_poly(n, tr * tl); determinant = poly_eval(coeffs, z)
        derivative = poly_eval([Fraction(i) * coeffs[i] for i in range(1, len(coeffs))], z)
        need(frac(row["det_zI_minus_H"]) == determinant and determinant != 0)
        need(frac(row["trace_resolvent"]) == derivative / determinant)
        need(type(row["outside_spectrum"]) is bool and row["outside_spectrum"] is True)

    one_sided = data["one_sided_rows"]
    need(type(one_sided) is list and len(one_sided) == 18)
    seen = set()
    for row in one_sided:
        need(set(row) == {"N", "orientation", "hopping", "rank_sequence_H_power_0_through_N", "nilpotency_index", "geometric_multiplicity_zero", "pbc_Nth_power_scalar", "pbc_diagonalizable"})
        n, hopping = row["N"], frac(row["hopping"])
        need(type(n) is int and 2 <= n <= 10 and hopping > 0 and row["orientation"] in {"right", "left"})
        need((n, row["orientation"]) not in seen); seen.add((n, row["orientation"]))
        ranks = row["rank_sequence_H_power_0_through_N"]
        need(type(ranks) is list and len(ranks) == n + 1 and all(type(x) is int for x in ranks))
        need(ranks == list(range(n, -1, -1)))
        need(type(row["nilpotency_index"]) is int and row["nilpotency_index"] == n)
        need(type(row["geometric_multiplicity_zero"]) is int and row["geometric_multiplicity_zero"] == 1)
        need(frac(row["pbc_Nth_power_scalar"]) == hopping ** n)
        need(type(row["pbc_diagonalizable"]) is bool and row["pbc_diagonalizable"] is True)

    pbc = data["pbc_rows"]
    need(type(pbc) is list and len(pbc) == 36)
    seen = set()
    for row in pbc:
        need(set(row) == {"N", "t_R", "t_L", "ellipse_real_semiaxis", "ellipse_signed_imag_semiaxis", "trace_powers_1_through_N", "normal", "one_sided_cyclic"})
        n, tr, tl = row["N"], frac(row["t_R"]), frac(row["t_L"])
        need(type(n) is int and 3 <= n <= 8 and tr >= 0 and tl >= 0)
        need((n, tr, tl) not in seen); seen.add((n, tr, tl))
        need(frac(row["ellipse_real_semiaxis"]) == tr + tl)
        need(frac(row["ellipse_signed_imag_semiaxis"]) == tr - tl)
        powers = row["trace_powers_1_through_N"]
        need(type(powers) is list and len(powers) == n)
        need([frac(x) for x in powers] == expected_trace_powers(n, tr, tl))
        need(type(row["normal"]) is bool and row["normal"] is True)
        need(type(row["one_sided_cyclic"]) is bool and row["one_sided_cyclic"] == ((tr == 0) != (tl == 0)))

    boundaries = data["boundary_rows"]
    need(type(boundaries) is list and len(boundaries) == 8)
    need(len({row["face"] for row in boundaries}) == 8)
    for row in boundaries:
        need(set(row) == {"face", "obc", "pbc", "warning"} and all(type(x) is str for x in row.values()))
    need("not a single Jordan block" in boundaries[4]["warning"])
    need("coincide" in boundaries[5]["warning"])

    summary = data["summary"]
    expected_summary = {"positive_obc_cases": 40, "resolvent_cases": 21, "one_sided_cases": 18, "pbc_cases": 36, "boundary_faces": 8, "audited_rows": 123}
    need(exact_tree_equal(summary, expected_summary) and all(type(x) is int for x in summary.values()))
    print(f"C308 independent Hatano--Nelson checker: PASS ({checks} assertions; producer import forbidden; strict JSON/YAML exact tree and type checks)")


if __name__ == "__main__":
    main()
