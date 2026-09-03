#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C323."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c323_quantum_search_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C323/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_RAW_SHA256 = "32e01825c6a7337ce34f24a95838c7589ad54a0945b0026ab212feea05c0e0d4"
EVALUATION_SEMANTIC_SHA256 = "c2a1d3bf4d4af87c29c9efb002871d64b0210da3a2fcd4f4a36a9e694b21bdfa"
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
EXPECTED_MODEL = {
    "owner": "permutation-symmetric complete-graph continuous-time quantum search",
    "hamiltonian": "H_g=-g|s><s|-P_W",
    "uniform_state": "|s>=N^(-1/2) sum_x |x>",
    "marked_fraction": "a=M/N",
    "domain": "N>=1, 0<=M<=N, g>=0",
    "success": "squared norm of the projection onto the full marked subspace",
    "clock": "physical unitary time exp(-itH_g)",
}
EXPECTED_THEOREM = {
    "decomposition": "marked dark eigenvalue -1, unmarked dark eigenvalue 0, and a two-dimensional bright block for 0<M<N",
    "bright_spectrum": "lambda_+-lambda_-=sqrt((g-1)^2+4ga), with trace -(g+1) and determinant g(1-a)",
    "success_law": "p_W(t)=a+4ga(1-a)/Omega^2 sin^2(Omega t/2)",
    "perfect_search": "for 0<a<1, perfect success occurs iff g=1 and first occurs at pi/(2sqrt(a))",
    "detuning": "1-p_max=(1-a)(g-1)^2/Omega^2 and g=1+c sqrt(a) has a nontrivial critical window",
    "graph_equivalence": "for g=gamma N, -gamma A(K_N)-P_W=H_g+gamma I",
    "faces": "M=0, M=N, N=1, and g=0 are diagonalized without fictitious negative dark multiplicities",
}
EXPECTED_REFERENCES = [
    {"identifier": "10.1103/PhysRevA.57.2403", "role": "continuous-time analog quantum-search owner"},
    {"identifier": "quant-ph/9612026", "role": "author preprint of the primary source"},
]
EXPECTED_COLLISIONS = {
    "C143": "discrete-time inhomogeneous coined five-cycle walk, not a complete-graph oracle Hamiltonian",
    "C171": "stochastic Ehrenfest Krawtchouk Markov operator, not unitary oracle search",
    "C183": "random-transposition Markov operator, not coherent rank-two search",
    "C223": "Jaynes--Cummings excitation blocks, not permutation-symmetric marked-set search",
    "C318": "local one-dimensional SSH bulk--edge chain, not a complete-graph driver and oracle projection",
}
EXPECTED_NONCLAIMS = [
    "No literature-priority claim is made for continuous-time search, multimarked reduction, or detuning formulas.",
    "The finite characteristic polynomial is not an Euler factor and the energy levels are not target zeros.",
    "No target arithmetic datum, root number, automorphy, target divisor, functional equation, Hilbert--Polya operator, or Route-B input is claimed.",
]
EVALUATION_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
    "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
    "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data",
    "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
    "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
    "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}
GATE_STATUS = {
    "a0": ("A0_FAIL", "PROVED"),
    "a1": ("A1_WEAK", "PROVED"),
    "a2": ("A2_FAIL", "STOP_SCOPED"),
    "a3": ("A3_FAIL", "STOP_SCOPED"),
    "a4": ("A4_NATURAL_QUANTIZATION", "PROVED"),
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def duplicate_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def strict_json(path: Path):
    value = json.loads(
        path.read_text(),
        object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be object")
    return value


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fr(value) -> Fraction:
    if type(value) is not str:
        raise TypeError("rational receipt must be string")
    result = Fraction(value)
    if q(result) != value:
        raise ValueError("noncanonical rational")
    return result


def mpf(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def exact_dict(value, expected, label: str) -> None:
    need(type(value) is dict and value == expected, label)


def exact_keys(value, keys, label: str) -> None:
    need(type(value) is dict and set(value) == set(keys), label)


def schema_need(condition: bool, label: str) -> None:
    """Fail closed on evaluator schema without inflating mathematical receipts."""
    if not condition:
        raise AssertionError(label)


def schema_keys(value, keys, label: str) -> None:
    schema_need(type(value) is dict and set(value) == set(keys), label)


def near(value, expected, label: str, tolerance=mp.mpf("4e-68")) -> None:
    if type(value) is not str:
        raise TypeError(f"{label}: decimal receipt must be string")
    got = mp.mpf(value)
    need(mp.isfinite(got) and abs(got - expected) <= tolerance * max(1, abs(expected)), label)


def full_matrix_check(n: int, m: int, g: Fraction) -> None:
    a = mp.mpf(m) / n
    s = mp.matrix([1 / mp.sqrt(n)] * n)
    h = -mpf(g) * (s * s.T)
    for index in range(m):
        h[index, index] -= 1
    values, _ = mp.eigsy(h)
    got = sorted(mp.re(values[index]) for index in range(n))
    omega = mp.sqrt((mpf(g) - 1) ** 2 + 4 * mpf(g) * a)
    want = [-(mpf(g) + 1 + omega) / 2]
    want.extend([-mp.mpf(1)] * (m - 1))
    want.extend([mp.mpf(0)] * (n - m - 1))
    want.append(-(mpf(g) + 1 - omega) / 2)
    want.sort()
    need(max(abs(x - y) for x, y in zip(got, want)) < mp.mpf("1e-70"), "full matrix spectrum")

    t = mp.pi / omega
    u = mp.expm(-1j * t * h) * s
    probability = sum(abs(u[index]) ** 2 for index in range(m))
    pmax = a + 4 * mpf(g) * a * (1 - a) / (omega * omega)
    need(abs(probability - pmax) < mp.mpf("1e-68"), "full matrix peak probability")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()

    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    top = {
        "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator", "evaluation", "model", "theorem_contract",
        "references", "collision_boundary", "nonclaims", "route_a", "scope_flags",
        "parameter_grid", "interior_rows", "critical_window_rows", "boundary_rows",
        "enumeration", "payload_sha256",
    }
    exact_keys(data, top, "top-level schema")
    need(data["schema"] == "hcs-c323-quantum-search-v1", "schema literal")
    need(data["candidate_id"] == "HCS-C323", "candidate")
    need(data["obstruction_id"] == "HEN-O307", "obstruction")
    need(data["source_commit"] == SOURCE, "source commit")
    need(data["fixed_epoch"] == 1788393600, "fixed epoch")
    need(data["scope_literal"] == SCOPE, "scope")
    exact_dict(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    exact_dict(data["model"], EXPECTED_MODEL, "model lock")
    exact_dict(data["theorem_contract"], EXPECTED_THEOREM, "theorem lock")
    need(data["references"] == EXPECTED_REFERENCES, "reference lock")
    exact_dict(data["collision_boundary"], EXPECTED_COLLISIONS, "collision lock")
    need(data["nonclaims"] == EXPECTED_NONCLAIMS, "nonclaim lock")
    exact_dict(data["scope_flags"], FLAGS, "scope flags")
    exact_dict(
        data["route_a"],
        {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "route A lock",
    )
    need(payload_hash(data) == data["payload_sha256"], "payload digest")

    raw = args.evaluation.read_bytes()
    need(sha(raw) == EVALUATION_RAW_SHA256, "evaluation raw digest")
    need(semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA256, "evaluation semantic digest")
    exact_dict(
        data["evaluation"],
        {
            "path": "evaluations/route_a/HCS-C323/2026-09-03.yaml",
            "raw_sha256": EVALUATION_RAW_SHA256,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        },
        "evidence evaluation lock",
    )
    schema_keys(evaluation, EVALUATION_KEYS, "YAML top-level schema")
    schema_need(evaluation["schema"] == "route-a-evaluation-v0.2.0", "YAML schema literal")
    need(evaluation["candidate_id"] == "HCS-C323", "YAML candidate")
    need(evaluation["source_commit"] == SOURCE, "YAML source")
    need(evaluation["scope_literal"] == SCOPE, "YAML scope")
    need(evaluation["obstruction_id"] == "HEN-O307", "YAML obstruction")
    schema_need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML evaluator authority")
    schema_need(evaluation["evaluator_version"] == "0.2.0", "YAML evaluator version")
    schema_need(evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator digest")
    for gate, (verdict, evidence_status) in GATE_STATUS.items():
        schema_keys(
            evaluation[gate],
            {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"},
            f"YAML {gate} schema",
        )
        schema_need(evaluation[gate]["verdict"] == verdict, f"YAML {gate} verdict")
        schema_need(evaluation[gate]["evidence_status"] == evidence_status, f"YAML {gate} evidence status")
    need(evaluation["tuple"] == data["route_a"]["tuple"], "YAML tuple")
    need(evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(evaluation["route_b_invocation_allowed"] is False, "YAML Route B")
    exact_dict(evaluation["scope_flags"], FLAGS, "YAML flags")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(evaluation["source_owner_tokens"] == ["10.1103/PhysRevA.57.2403", "quant-ph/9612026"], "YAML sources")

    expected_grid = {
        "N": "2..32", "M": "1..N-1",
        "g": ["0", "1/4", "1/2", "1", "3/2", "2", "4"],
        "window_k": [8, 16, 32, 64],
        "window_c": ["-4", "-2", "-1", "0", "1", "2", "4"],
        "boundary_N": "1..32", "boundary_g": ["0", "1/2", "1", "2"],
    }
    exact_dict(data["parameter_grid"], expected_grid, "grid lock")
    drivers = [Fraction(token) for token in expected_grid["g"]]
    expected_count = sum(n - 1 for n in range(2, 33)) * len(drivers)
    need(len(data["interior_rows"]) == expected_count, "interior count")
    row_keys = {
        "N", "M", "a", "g", "omega_squared", "bright_trace", "bright_determinant",
        "lambda_minus", "lambda_plus", "marked_dark_multiplicity",
        "unmarked_dark_multiplicity", "success_at_zero", "success_maximum",
        "success_maximum_defect", "bright_half_period", "resonant",
        "search_oscillation_nonconstant", "graph_gamma", "graph_scalar_shift",
        "zero_driver_minus_one_multiplicity", "zero_driver_zero_multiplicity",
    }
    cursor = 0
    for n in range(2, 33):
        for m in range(1, n):
            a = Fraction(m, n)
            for g in drivers:
                row = data["interior_rows"][cursor]
                cursor += 1
                exact_keys(row, row_keys, "interior row keys")
                need(row["N"] == n and row["M"] == m, "interior row index")
                need(fr(row["a"]) == a and fr(row["g"]) == g, "interior a/g")
                omega2 = (g - 1) ** 2 + 4 * g * a
                need(fr(row["omega_squared"]) == omega2, "omega squared")
                need(fr(row["bright_trace"]) == -(g + 1), "bright trace")
                need(fr(row["bright_determinant"]) == g * (1 - a), "bright determinant")
                root = mp.sqrt(mpf(omega2))
                near(row["lambda_minus"], -(mpf(g) + 1 + root) / 2, "lambda minus")
                near(row["lambda_plus"], -(mpf(g) + 1 - root) / 2, "lambda plus")
                need(row["marked_dark_multiplicity"] == m - 1, "marked dark multiplicity")
                need(row["unmarked_dark_multiplicity"] == n - m - 1, "unmarked dark multiplicity")
                need(fr(row["success_at_zero"]) == a, "initial success")
                pmax = a + 4 * g * a * (1 - a) / omega2
                defect = (1 - a) * (g - 1) ** 2 / omega2
                need(fr(row["success_maximum"]) == pmax, "success maximum")
                need(fr(row["success_maximum_defect"]) == defect, "maximum defect")
                need(pmax + defect == 1, "maximum partition")
                near(row["bright_half_period"], mp.pi / root, "bright half-period")
                need(row["resonant"] is (g == 1), "resonance flag")
                need((pmax == 1) is (g == 1), "perfect iff")
                need(row["search_oscillation_nonconstant"] is (g > 0), "oscillation flag")
                need(fr(row["graph_gamma"]) == g / n, "graph gamma")
                need(fr(row["graph_scalar_shift"]) == g / n, "graph shift")
                need(row["zero_driver_minus_one_multiplicity"] == (m if g == 0 else None), "zero g minus multiplicity")
                need(row["zero_driver_zero_multiplicity"] == (n - m if g == 0 else None), "zero g zero multiplicity")

    need(len(data["critical_window_rows"]) == 28, "window row count")
    cursor = 0
    for k in (8, 16, 32, 64):
        a = Fraction(1, k * k)
        for c in map(Fraction, (-4, -2, -1, 0, 1, 2, 4)):
            row = data["critical_window_rows"][cursor]
            cursor += 1
            exact_keys(
                row,
                {"k", "c", "a", "g", "omega_squared", "success_maximum",
                 "scaled_peak_time", "limit_success_maximum", "limit_scaled_peak_time"},
                "window keys",
            )
            g = 1 + c / k
            omega2 = (g - 1) ** 2 + 4 * g * a
            pmax = a + 4 * g * a * (1 - a) / omega2
            need(row["k"] == k and fr(row["c"]) == c, "window index")
            need(fr(row["a"]) == a and fr(row["g"]) == g, "window parameters")
            need(fr(row["omega_squared"]) == omega2, "window omega")
            need(fr(row["success_maximum"]) == pmax, "window maximum")
            near(row["scaled_peak_time"], mp.sqrt(mpf(a)) * mp.pi / mp.sqrt(mpf(omega2)), "scaled peak")
            near(row["limit_success_maximum"], 4 / (mpf(c) ** 2 + 4), "window limit maximum")
            near(row["limit_scaled_peak_time"], mp.pi / mp.sqrt(mpf(c) ** 2 + 4), "window limit time")

    need(len(data["boundary_rows"]) == 256, "boundary count")
    cursor = 0
    for n in range(1, 33):
        for g in map(Fraction, (0, Fraction(1, 2), 1, 2)):
            empty, full = data["boundary_rows"][cursor:cursor + 2]
            cursor += 2
            keys = {"face", "N", "M", "g", "uniform_eigenvalue", "orthogonal_eigenvalue", "orthogonal_multiplicity", "success_probability"}
            exact_keys(empty, keys, "empty boundary keys")
            exact_keys(full, keys, "full boundary keys")
            need(empty == {"face": "no_marked_states", "N": n, "M": 0, "g": q(g), "uniform_eigenvalue": q(-g), "orthogonal_eigenvalue": "0", "orthogonal_multiplicity": n - 1, "success_probability": "0"}, "empty boundary")
            need(full == {"face": "all_states_marked", "N": n, "M": n, "g": q(g), "uniform_eigenvalue": q(-(g + 1)), "orthogonal_eigenvalue": "-1", "orthogonal_multiplicity": n - 1, "success_probability": "1"}, "full boundary")

    enumeration = data["enumeration"]
    exact_keys(enumeration, {"interior_rows", "critical_window_rows", "boundary_rows", "exact_driver_values", "audited_leaf_count"}, "enumeration keys")
    need(enumeration["interior_rows"] == expected_count, "enumerated interior")
    need(enumeration["critical_window_rows"] == 28, "enumerated window")
    need(enumeration["boundary_rows"] == 256, "enumerated boundary")
    need(enumeration["exact_driver_values"] == 7, "enumerated drivers")
    need(enumeration["audited_leaf_count"] == leaves(data), "leaf count")

    for n, m, g in [(2, 1, Fraction(1)), (5, 2, Fraction(1, 2)), (7, 3, Fraction(1)), (9, 1, Fraction(2)), (12, 7, Fraction(4))]:
        full_matrix_check(n, m, g)

    print(f"C323 independent quantum-search checker: PASS {CHECKS} checks")


if __name__ == "__main__":
    main()
