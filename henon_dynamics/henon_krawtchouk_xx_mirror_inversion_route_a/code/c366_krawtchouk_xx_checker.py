#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C366; never imports the producer."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c366_krawtchouk_xx_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C366/2026-09-04.yaml"
SOURCE = "323ea43f6970544467f8a89f0ed9be0c7c39f896"
DATE = "2026-09-04"
EPOCH = 1788480000
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_PATH = "evaluations/route_a/HCS-C366/2026-09-04.yaml"
YAML_RAW = "acc72ba628087e67f52927031ca66ee1798cc8073907133cf7049df49f04cc59"
YAML_SEMANTIC = "a2ab8e3e0d4256ea4058300f66fecac5f6fec5283f9ad80432b21e28b0648ef5"
FINITE_ROLE = (
    "exact spectrum, orthogonality, formal all-time endpoint monomials, subset-energy "
    "and mirror-phase rows, Gaussian q-binomial coefficient polynomials, and boundary "
    "regression only; representation and exterior-power arguments prove the all-size theorem"
)
COLLISION = (
    "C143 owns an inhomogeneous coined quantum walk; C171 owns Ehrenfest/Krawtchouk "
    "Markov lumping; C366 uniquely owns the engineered XX perfect-transfer chain and "
    "full exterior-power phase law"
)
NONCLAIMS = (
    "No arithmetic target data, Euler factor, root number, automorphy, target divisor or "
    "functional equation, target-zero match, Hilbert--Polya operator, perturbative robustness, "
    "or Route B inference is claimed"
)
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
FLAGS = {key: False for key in (
    "claims_target_arithmetic_local_data", "claims_target_euler_factors",
    "claims_root_number", "claims_automorphy",
    "claims_target_divisor_or_counting_law", "claims_target_functional_equation",
    "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b",
)}
TOP = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml", "model",
    "theorem_status", "route_tuple", "overall_verdict", "route_b_invocation_allowed",
    "scope_flags", "exact_claims", "boundary_atlas", "finite_evidence_role",
    "collision_boundary", "nonclaims", "references", "spectral_rows", "subset_rows",
    "energy_multiplicity_rows", "endpoint_rows", "gaussian_q_binomial_rows", "counts",
    "payload_sha256",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
    "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
    "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
    "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3",
    "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
    "source_owner_tokens",
}
MODEL = {
    "sites": "0,...,N",
    "single_particle_hopping": "J_j=(omega/2)*sqrt((j+1)(N-j))",
    "clock": "physical unitary time",
    "propagator": "exp(-itH)",
    "fermion_order": "increasing site order",
    "uniform_field": "B*mhat with mhat the fermion-number operator; main model has B=0",
    "half_form_or_target_fit": False,
}
CLAIMS = {
    "single_particle_owner": "H/omega is the spin-N/2 J_x matrix",
    "spectrum": "omega*(N/2-r), r=0,...,N, with Krawtchouk eigenvectors",
    "endpoint_law": "(-i sign(omega))^k*sqrt(C(N,k))*sin(abs(omega)t/2)^k*cos(abs(omega)t/2)^(N-k)",
    "mirror": "for omega nonzero, perfect reflection at pi/abs(omega)",
    "many_body": "each m-particle propagator is the m-th exterior power",
    "mirror_phase": "(-i sign(omega))^(mN)*(-1)^(m(m-1)/2)",
    "multiplicity_owner": "coefficient of y^m q^s in product_(r=0)^N(1+y*q^r)",
    "gaussian_q_binomial": "[n,m]_q=[n-1,m]_q+q^(n-m)[n-1,m-1]_q with boundary one",
    "uniform_field_revival": "U_B(2pi/abs(omega))=exp(-i*2pi*B*mhat/abs(omega))*(-1)^(N*mhat); U_B(4pi/abs(omega))=exp(-i*4pi*B*mhat/abs(omega))",
    "full_identity_conditions": "2pi time iff 2B/abs(omega)+N is an even integer; 4pi time iff 2B/abs(omega) is an integer",
}
BOUNDARY = {
    "N_zero": "one site; mirror is the identity and the uniform field is the only dynamics",
    "omega_zero": "the hopping Hamiltonian vanishes; revival times pi/abs(omega) are undefined",
    "negative_omega": "time orientation is conjugated and the mirror phase uses sign(omega)",
    "uniform_field": "B*mhat commutes with the hopping; its sector phase is exp(-imBt)",
    "perturbations": "no robustness of perfect transfer under generic coupling perturbations is claimed",
    "full_fock_revival": "at B=0, 2pi/abs(omega) is identity for even N and fermion parity for odd N; 4pi/abs(omega) is identity",
    "vacuum": "the vacuum is always fixed, so full-Fock identity conditions concern every particle sector simultaneously",
}
REFERENCES = [
    {"doi": "10.1103/PhysRevLett.92.187902", "role": "engineered spin-chain lineage"},
    {"doi": "10.1103/PhysRevLett.93.230502", "role": "perfect-state-transfer lineage"},
]


def refuse_optimized() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 checker refuses optimized Python")


def unique_json(pairs):
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def load_json(path: Path) -> dict:
    return json.loads(
        path.read_text(), object_pairs_hook=unique_json,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def exact_keys(value, expected, label: str) -> None:
    if type(value) is not dict or set(value) != set(expected):
        actual = set(value) if isinstance(value, dict) else type(value).__name__
        raise AssertionError(f"{label} exact keys: {actual}")


def typed_equal(actual, expected) -> bool:
    """Recursive equality that never conflates bool/int/float leaves."""
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return (set(actual) == set(expected)
                and all(typed_equal(actual[key], expected[key]) for key in expected))
    if isinstance(expected, list):
        return (len(actual) == len(expected)
                and all(typed_equal(left, right) for left, right in zip(actual, expected)))
    return actual == expected


def require_same(actual, expected, label: str) -> None:
    if not typed_equal(actual, expected):
        raise AssertionError(f"{label} typed value mismatch")


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    output = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge key forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in output:
            raise ValueError("duplicate or non-string YAML key")
        output[key] = loader.construct_object(value_node, deep=deep)
    return output


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def load_yaml(path: Path) -> tuple[dict, bytes]:
    raw = path.read_bytes()
    for token in yaml.scan(raw.decode()):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw.decode(), Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value, raw


def validate_yaml(path: Path) -> int:
    evaluation, raw = load_yaml(path)
    checks = 0
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW; checks += 1
    assert digest(evaluation) == YAML_SEMANTIC; checks += 1
    exact_keys(evaluation, YAML_KEYS, "evaluation"); checks += len(YAML_KEYS)
    fixed = {
        "schema": "route-a-evaluation-v0.2.0",
        "candidate_id": "HCS-C366",
        "title": "Krawtchouk XX-chain spectrum, perfect mirror transfer, and full fermionic exterior-power theorem",
        "evaluation_date": DATE,
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": AUTHORITY,
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA,
        "obstruction_id": "HEN-O350",
        "artifact_paths": ["results/c366_krawtchouk_xx_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "tuple": TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "route_b_lock_reason": "natural source quantization cannot repair the absent arithmetic carrier, target determinant, or target divisor",
        "scope_flags": FLAGS,
        "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": FINITE_ROLE,
        "source_owner_tokens": ["10.1103/PhysRevLett.92.187902", "10.1103/PhysRevLett.93.230502"],
        "parameters": "integer N at least zero and real coupling scale omega, with the main theorem oriented by omega positive; a uniform field B is a separately tracked boundary perturbation",
        "normalization": "hopping J_j equals omega over two times square root of j plus 1 times N minus j; increasing-site fermion order; a uniform field is B times the fermion-number operator",
    }
    for key, expected in fixed.items():
        require_same(evaluation[key], expected, f"evaluation.{key}")
        checks += 1
    for gate, verdict, status in zip(
        ("a0", "a1", "a2", "a3", "a4"), TUPLE,
        ("PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"),
    ):
        exact_keys(evaluation[gate], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, gate)
        require_same(evaluation[gate]["verdict"], verdict, f"{gate}.verdict")
        require_same(evaluation[gate]["evidence_status"], status, f"{gate}.evidence_status")
        assert type(evaluation[gate]["strongest_evidence"]) is str and evaluation[gate]["strongest_evidence"]
        assert type(evaluation[gate]["strongest_failure"]) is str and evaluation[gate]["strongest_failure"]
        checks += 8
    narrative = {
        "candidate_definition", "family", "phase_space", "dynamics", "parameter_provenance",
        "arithmetic_origin", "clock", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data",
    }
    for key in narrative:
        assert type(evaluation[key]) is str and evaluation[key]
        checks += 1
    return checks


def kval(n: int, r: int, j: int) -> int:
    total = 0
    for ell in range(r + 1):
        if ell <= j and r - ell <= n - j:
            total += (-1) ** ell * math.comb(j, ell) * math.comb(n - j, r - ell)
    return total


def add_shift(left: list[int], right: list[int], shift: int) -> list[int]:
    output = [0] * max(len(left), len(right) + shift)
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index + shift] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def validate(data: dict, evaluation: Path) -> tuple[int, str]:
    checks = validate_yaml(evaluation)
    exact_keys(data, TOP, "evidence"); checks += len(TOP)
    payload = dict(data)
    claimed = payload.pop("payload_sha256")
    assert type(claimed) is str and len(claimed) == 64 and claimed == digest(payload); checks += 2
    fixed = {
        "schema": "hcs-c366-evidence-v2",
        "candidate_id": "HCS-C366",
        "obstruction_id": "HEN-O350",
        "evaluation_date": DATE,
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": AUTHORITY, "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": YAML_PATH, "raw_sha256": YAML_RAW,
                         "semantic_sha256": YAML_SEMANTIC},
        "model": MODEL,
        "theorem_status": "PROVABLE_AS_STATED",
        "route_tuple": TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "scope_flags": FLAGS,
        "exact_claims": CLAIMS,
        "boundary_atlas": BOUNDARY,
        "finite_evidence_role": FINITE_ROLE,
        "collision_boundary": COLLISION,
        "nonclaims": NONCLAIMS,
        "references": REFERENCES,
    }
    for key, expected in fixed.items():
        require_same(data[key], expected, f"evidence.{key}")
        checks += 1
    exact_keys(data["evaluator"], {"authority", "version", "sha256"}, "evaluator"); checks += 3
    exact_keys(data["route_a_yaml"], {"relative_path", "raw_sha256", "semantic_sha256"}, "route_a_yaml"); checks += 3
    exact_keys(data["model"], MODEL, "model"); checks += len(MODEL)
    exact_keys(data["exact_claims"], CLAIMS, "exact_claims"); checks += len(CLAIMS)
    exact_keys(data["boundary_atlas"], BOUNDARY, "boundary_atlas"); checks += len(BOUNDARY)
    exact_keys(data["scope_flags"], FLAGS, "scope_flags"); checks += len(FLAGS)
    for reference in data["references"]:
        exact_keys(reference, {"doi", "role"}, "reference"); checks += 2

    spectral = data["spectral_rows"]
    spectral_coords = {(n, r) for n in range(11) for r in range(n + 1)}
    assert type(spectral) is list and len(spectral) == 66; checks += 2
    seen = set()
    row_map = {}
    for row in spectral:
        exact_keys(row, {"N", "r", "twice_energy_over_omega", "krawtchouk_values",
                         "weighted_norm", "expected_weighted_norm"}, "spectral row")
        n, r = row["N"], row["r"]
        assert type(n) is int and type(r) is int and (n, r) in spectral_coords and (n, r) not in seen
        seen.add((n, r)); row_map[(n, r)] = row
        values = [kval(n, r, j) for j in range(n + 1)]
        expected_norm = (2 ** n) * math.comb(n, r)
        expected_row = {
            "N": n, "r": r, "twice_energy_over_omega": n - 2 * r,
            "krawtchouk_values": values, "weighted_norm": expected_norm,
            "expected_weighted_norm": expected_norm,
        }
        require_same(row, expected_row, "spectral row")
        checks += 10 + len(values)
    assert seen == spectral_coords; checks += 1
    for n in range(11):
        for r in range(n + 1):
            for s in range(n + 1):
                inner = sum(math.comb(n, j) * kval(n, r, j) * kval(n, s, j)
                            for j in range(n + 1))
                expected = (2 ** n) * math.comb(n, r) if r == s else 0
                assert inner == expected
                checks += 1

    subset = data["subset_rows"]
    assert type(subset) is list and len(subset) == 65534; checks += 2
    subset_keys = {"N", "mask", "particles", "coordinate_sum", "twice_energy_over_omega",
                   "mirror_mask", "mirror_phase_minus_i_exponent_mod4"}
    histograms = {n: Counter() for n in range(15)}
    sum_histograms = {n: Counter() for n in range(15)}
    cursor = 0
    for n in range(15):
        for mask in range(1 << (n + 1)):
            row = subset[cursor]; cursor += 1
            exact_keys(row, subset_keys, "subset row")
            assert type(row["N"]) is int and type(row["mask"]) is int
            assert (row["N"], row["mask"]) == (n, mask)
            occupied = [j for j in range(n + 1) if mask & (1 << j)]
            particles, coordinate_sum = len(occupied), sum(occupied)
            twice_energy = particles * n - 2 * coordinate_sum
            mirror_mask = sum(1 << (n - j) for j in occupied)
            phase = (particles * n + particles * (particles - 1)) % 4
            expected_row = {
                "N": n, "mask": mask, "particles": particles,
                "coordinate_sum": coordinate_sum,
                "twice_energy_over_omega": twice_energy,
                "mirror_mask": mirror_mask,
                "mirror_phase_minus_i_exponent_mod4": phase,
            }
            require_same(row, expected_row, "subset row")
            histograms[n][(particles, twice_energy)] += 1
            sum_histograms[n][(particles, coordinate_sum)] += 1
            checks += 13

    expected_energy = []
    for n in range(15):
        for (particles, energy), multiplicity in sorted(histograms[n].items()):
            expected_energy.append({"N": n, "particles": particles,
                                    "twice_energy_over_omega": energy,
                                    "multiplicity": multiplicity})
    energy_rows = data["energy_multiplicity_rows"]
    assert type(energy_rows) is list and len(energy_rows) == len(expected_energy); checks += 2
    for actual, expected in zip(energy_rows, expected_energy):
        exact_keys(actual, {"N", "particles", "twice_energy_over_omega", "multiplicity"},
                   "energy multiplicity row")
        require_same(actual, expected, "energy multiplicity row")
        checks += 5

    gaussian_rows = data["gaussian_q_binomial_rows"]
    gaussian_coords = {(n, m) for n in range(16) for m in range(n + 1)}
    assert type(gaussian_rows) is list and len(gaussian_rows) == 136; checks += 2
    table: dict[tuple[int, int], list[int]] = {}
    seen = set()
    for row in gaussian_rows:
        exact_keys(row, {"n", "m", "coefficients"}, "Gaussian row")
        n, m = row["n"], row["m"]
        assert type(n) is int and type(m) is int and (n, m) in gaussian_coords and (n, m) not in seen
        if n == 0 or m in (0, n):
            expected = [1]
        else:
            expected = add_shift(table[(n - 1, m)], table[(n - 1, m - 1)], n - m)
        require_same(row["coefficients"], expected, "Gaussian coefficients")
        assert all(type(value) is int and value >= 0 for value in row["coefficients"])
        table[(n, m)] = expected; seen.add((n, m))
        checks += 8 + len(expected)
    assert seen == gaussian_coords; checks += 1
    for n in range(15):
        for m in range(n + 2):
            actual_hist = sum_histograms[n]
            max_sum = max((total for (particles, total) in actual_hist if particles == m), default=0)
            actual = [actual_hist[(m, total)] for total in range(max_sum + 1)]
            if m == 0:
                actual = [1]
            expected = [0] * (m * (m - 1) // 2) + table[(n + 1, m)]
            while len(actual) > 1 and actual[-1] == 0:
                actual.pop()
            assert actual == expected
            checks += len(expected) + 1

    endpoints = data["endpoint_rows"]
    endpoint_keys = {
        "N", "site", "amplitude_phase_minus_i_exponent_mod4",
        "amplitude_binomial_radicand", "amplitude_sine_power", "amplitude_cosine_power",
        "half_transfer_probability_numerator", "half_transfer_probability_denominator",
        "mirror_probability", "zero_time_probability",
    }
    assert type(endpoints) is list and len(endpoints) == 231; checks += 2
    cursor = 0
    for n in range(21):
        numerator_sum = 0
        for k in range(n + 1):
            row = endpoints[cursor]; cursor += 1
            exact_keys(row, endpoint_keys, "endpoint row")
            expected = {
                "N": n, "site": k,
                "amplitude_phase_minus_i_exponent_mod4": k % 4,
                "amplitude_binomial_radicand": math.comb(n, k),
                "amplitude_sine_power": k, "amplitude_cosine_power": n - k,
                "half_transfer_probability_numerator": math.comb(n, k),
                "half_transfer_probability_denominator": 2 ** n,
                "mirror_probability": int(k == n), "zero_time_probability": int(k == 0),
            }
            require_same(row, expected, "endpoint row")
            numerator_sum += row["half_transfer_probability_numerator"]
            checks += len(endpoint_keys) + 1
        assert numerator_sum == 2 ** n; checks += 1

    counts = {
        "spectral_rows": 66,
        "subset_states": 65534,
        "energy_multiplicity_rows": len(expected_energy),
        "endpoint_cells": 231,
        "gaussian_q_binomial_rows": 136,
    }
    exact_keys(data["counts"], counts, "counts")
    require_same(data["counts"], counts, "counts"); checks += len(counts) + 1
    return checks, claimed


def main() -> None:
    refuse_optimized()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    checks, payload = validate(load_json(args.input), args.evaluation)
    print(f"C366 independent Krawtchouk-XX checker: PASS ({checks} checks; "
          f"subset_rows=65534 gaussian_rows=136 payload={payload})")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"C366 checker FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
