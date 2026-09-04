#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C378; imports no producer code."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c378 checker refuses optimized Python")

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c378_dyson_ou_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C378/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "b70bfed7319e0ebfd5697491a29c11bd803eab74f66fb303a6f3d11c1e475af9"
YAML_SEMANTIC_SHA = "6d374dfee088737ada5dc669e7b597844b6da08d26ce5e7ec13313df03766b3f"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data", "claims_target_euler_factors",
        "claims_root_number", "claims_automorphy",
        "claims_target_divisor_or_counting_law", "claims_target_functional_equation",
        "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b",
    )
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml", "conventions",
    "theorem_contract", "finite_grid", "collision_boundary", "nonclaims", "references",
    "scope_flags", "route_a", "finite_evidence_role", "dimension_rows", "level_rows",
    "partition_rows", "kernel_rows", "section_sha256", "payload_sha256",
}
YAML_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "title", "evaluation_date", "source_commit", "code_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization",
    "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
    "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "adversarial_controls", "claim_boundary", "blocking_conditions", "next_smallest_test", "round2_clues",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key {key}")
        value[key] = item
    return value


def load_json(path: Path):
    return json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def typed_equal(actual, expected):
    if type(actual) is not type(expected):
        return False
    if type(actual) is dict:
        return set(actual) == set(expected) and all(typed_equal(actual[k], expected[k]) for k in expected)
    if type(actual) is list:
        return len(actual) == len(expected) and all(typed_equal(a, b) for a, b in zip(actual, expected))
    return actual == expected


def exact(actual, expected, label):
    if not typed_equal(actual, expected):
        raise AssertionError(f"typed mismatch at {label}")


def exact_keys(actual, expected, label):
    if type(actual) is not dict or set(actual) != set(expected):
        raise AssertionError(f"key mismatch at {label}")


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    value = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge key forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in value:
            raise ValueError("duplicate or non-string YAML key")
        value[key] = loader.construct_object(value_node, deep=deep)
    return value


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def load_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value


def validate_yaml(path: Path):
    raw = path.read_bytes()
    value = load_yaml(path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(value) == YAML_SEMANTIC_SHA
    exact_keys(value, YAML_KEYS, "evaluation YAML")
    frozen = {
        "schema": "route-a-evaluation-v0.2.0",
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "HCS-C378",
        "title": "Beta-two Dyson Ornstein-Uhlenbeck eigenvalue diffusion, exact h-transform kernel, and complete partition spectrum",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "code_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA,
        "obstruction_id": "HEN-O362",
        "artifact_paths": ["results/c378_dyson_ou_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "tuple": TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "scope_flags": FLAGS,
        "theorem_status": "PROVABLE_AS_STATED",
        "source_owner_tokens": [
            "DOI:10.1063/1.1703862", "DOI:10.2140/pjm.1959.9.1141",
            "DOI:10.1007/s004400050092", "DOI:10.1007/s002200050161",
            "NUMDAM:AIHPB_1999__35_2_177_0", "theorem:beta2-dyson-ou-partition-spectrum",
        ],
    }
    for key, expected in frozen.items():
        exact(value[key], expected, f"yaml.{key}")
    statuses = ("PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED")
    for key, verdict, status in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE, statuses):
        expected_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"}
        if key == "a0":
            expected_keys.add("arithmetic_controls")
        exact_keys(value[key], expected_keys, f"yaml.{key}")
        exact(value[key]["verdict"], verdict, f"yaml.{key}.verdict")
        exact(value[key]["evidence_status"], status, f"yaml.{key}.evidence_status")
        assert type(value[key]["metrics"]) is dict and value[key]["metrics"]
        assert type(value[key]["artifacts"]) is list and len(value[key]["artifacts"]) >= 2
        assert all(type(item) is str and item for item in value[key]["artifacts"])
    controls = value["a0"]["arithmetic_controls"]
    assert type(controls) is list and len(controls) >= 3 and len(set(controls)) == len(controls)
    assert all(type(item) is str and item for item in controls)
    exact_keys(value["adversarial_controls"], {"controls_used", "proves_too_much_risk", "verdict"}, "yaml.adversarial_controls")
    assert type(value["adversarial_controls"]["controls_used"]) is list and len(value["adversarial_controls"]["controls_used"]) >= 3
    exact(value["adversarial_controls"]["verdict"], "STOP_SCOPED", "yaml.adversarial_controls.verdict")
    assert type(value["claim_boundary"]) is str and value["claim_boundary"]
    assert type(value["blocking_conditions"]) is list and len(value["blocking_conditions"]) >= 3
    assert type(value["next_smallest_test"]) is str and value["next_smallest_test"]
    assert type(value["round2_clues"]) is list and len(value["round2_clues"]) >= 2
    for key in (
        "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "orbit_cutoff", "precision", "forbidden_data",
        "route_b_lock_reason", "finite_evidence_role",
    ):
        assert type(value[key]) is str and value[key]
    exact(value["training_data"], "none", "yaml.training_data")
    assert "minus one half" in value["parameters"]
    assert "generic beta-two random-matrix statistics are not" in value["arithmetic_origin"]


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


@lru_cache(maxsize=None)
def partition_number(degree: int, max_part: int) -> int:
    if degree == 0:
        return 1
    if degree < 0 or max_part == 0:
        return 0
    return partition_number(degree, max_part - 1) + partition_number(degree - max_part, max_part)


def enumerate_partitions(total: int, maximum_length: int):
    result = []

    def visit(remaining, ceiling, prefix):
        if remaining == 0:
            result.append(tuple(prefix))
            return
        if len(prefix) == maximum_length:
            return
        for part in range(min(ceiling, remaining), 0, -1):
            visit(remaining - part, part, prefix + [part])

    visit(total, total, [])
    return result


def expected_dimensions():
    result = []
    for n in range(1, 17):
        d = n * (n - 1) // 2
        result.append({
            "N": n, "hermitian_real_dimension": n * n, "vandermonde_degree": d,
            "doob_energy_shift": frac(Fraction(d, 2)), "spectral_gap": frac(Fraction(1, 2)),
            "chamber_normalizer_over_(2pi)^(N/2)": math.prod(math.factorial(j) for j in range(n)),
            "ground_slater_indices": list(range(n)), "ground_slater_index_sum": d,
        })
    return result


def expected_levels():
    return [
        {
            "N": n, "degree": degree,
            "partition_multiplicity": partition_number(degree, n),
            "generator_eigenvalue": frac(Fraction(-degree, 2)),
            "semigroup_exponent": frac(Fraction(degree, 2)),
        }
        for n in range(1, 17) for degree in range(65)
    ]


def expected_partitions():
    result = []
    for n in range(1, 9):
        ground_norm = math.prod(math.factorial(j) for j in range(n))
        d = n * (n - 1) // 2
        for degree in range(25):
            values = enumerate_partitions(degree, n)
            assert len(values) == partition_number(degree, n)
            for rank, partition in enumerate(values):
                padded = list(partition) + [0] * (n - len(partition))
                indices = [padded[n - 1 - i] + i for i in range(n)]
                result.append({
                    "N": n, "degree": degree, "rank": rank, "partition": padded,
                    "slater_indices": indices, "slater_index_sum": d + degree,
                    "quotient_degree": degree,
                    "generator_eigenvalue": frac(Fraction(-degree, 2)),
                    "squared_norm": frac(Fraction(math.prod(math.factorial(m) for m in indices), ground_norm)),
                })
    return result


def permutation_sign(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation)) for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def leibniz_determinant(matrix):
    total = mp.mpf(0)
    for permutation in itertools.permutations(range(len(matrix))):
        term = mp.mpf(permutation_sign(permutation))
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def vandermonde(values):
    return math.prod(values[j] - values[i] for i in range(len(values)) for j in range(i + 1, len(values)))


def scalar_kernel(x, y, r):
    variance = 1 - r * r
    return mp.exp(-((y - r * x) ** 2) / (2 * variance)) / mp.sqrt(2 * mp.pi * variance)


def validate_kernels(rows):
    assert type(rows) is list and len(rows) == 12
    mp.mp.dps = 90
    points = {
        2: ((-2, 1), (-1, 2)),
        3: ((-3, 0, 2), (-2, 1, 4)),
        4: ((-4, -1, 1, 5), (-3, 0, 2, 6)),
    }
    contractions = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))
    index = 0
    for n, (x, y) in points.items():
        h_x, h_y = vandermonde(x), vandermonde(y)
        d = n * (n - 1) // 2
        for contraction in contractions:
            row = rows[index]
            index += 1
            exact_keys(row, {
                "N", "x", "y", "contraction_r", "variance", "vandermonde_x",
                "vandermonde_y", "killed_determinant_q_xy_decimal_50",
                "doob_kernel_k_xy_decimal_50", "relative_detailed_balance_residual_decimal_50",
            }, f"kernel[{index - 1}]")
            frozen = {
                "N": n, "x": list(x), "y": list(y), "contraction_r": frac(contraction),
                "variance": frac(1 - contraction * contraction), "vandermonde_x": h_x,
                "vandermonde_y": h_y,
            }
            for key, expected in frozen.items():
                exact(row[key], expected, f"kernel[{index - 1}].{key}")
            r = mp.mpf(contraction.numerator) / contraction.denominator
            matrix = [[scalar_kernel(xi, yj, r) for yj in y] for xi in x]
            q_expected = leibniz_determinant(matrix)
            k_expected = r ** (-d) * mp.mpf(h_y) / h_x * q_expected
            q_actual = mp.mpf(row["killed_determinant_q_xy_decimal_50"])
            k_actual = mp.mpf(row["doob_kernel_k_xy_decimal_50"])
            residual = mp.mpf(row["relative_detailed_balance_residual_decimal_50"])
            assert q_expected > 0 and k_expected > 0
            assert abs(q_actual / q_expected - 1) < mp.mpf("1e-48")
            assert abs(k_actual / k_expected - 1) < mp.mpf("1e-48")
            assert 0 <= residual < mp.mpf("1e-75")


CONVENTIONS = {
    "matrix_sde": "dH=dB-H*dt/2 on Herm_N with trace inner product",
    "ordered_chamber": "W_N={x_1<...<x_N}",
    "eigenvalue_sde": "dX_i=dB_i+sum_{j!=i}1/(X_i-X_j)*dt-X_i*dt/2",
    "scalar_ou_generator": "L0=sum_i(partial_i^2-x_i*partial_i)/2",
    "scalar_ou_contraction": "r=exp(-t/2), variance=1-r^2",
    "vandermonde": "h(x)=product_{i<j}(x_j-x_i)>0 on W_N",
    "vandermonde_degree": "d=N*(N-1)/2 and L0*h=-d*h/2",
    "chamber_density": "pi_N=Z_N^-1*exp(-|x|^2/2)*h(x)^2",
    "normalizer": "Z_N=(2*pi)^(N/2)*product_{j=0}^{N-1}j!",
}
THEOREM = {
    "radial_generator": "L=sum_i partial_i^2/2+sum_i(sum_{j!=i}1/(x_i-x_j)-x_i/2)*partial_i",
    "killed_kernel": "q_t(x,y)=det[p_t(x_i,y_j)]",
    "doob_kernel": "k_t(x,y)=exp(d*t/2)*h(y)*q_t(x,y)/h(x)",
    "conservativity": "integral_W q_t(x,y)h(y)dy=exp(-d*t/2)h(x)",
    "boundary": "the h-transformed diffusion started in W_N is conservative and never collides",
    "partition_index": "m_i=kappa_{N-i}+i for zero-based i and partitions kappa_1>=...>=kappa_N>=0",
    "eigenbasis": "Phi_kappa=det[He_{m_i}(x_j)]/h(x)",
    "spectrum": "L*Phi_kappa=-|kappa|*Phi_kappa/2 with multiplicity p_N(|kappa|)",
    "gap": "the sharp L2 spectral gap is 1/2 and Var_pi(f)<=integral|grad f|^2 d pi",
    "heat_trace": "Tr(P_t)=product_{j=1}^N(1-exp(-j*t/2))^-1",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    validate_yaml(args.evaluation)
    obj = load_json(args.input)
    exact_keys(obj, TOP_KEYS, "evidence root")
    frozen = {
        "schema": "hcs-c378-beta2-dyson-ou-evidence-v1",
        "candidate_id": "HCS-C378", "obstruction_id": "HEN-O362",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C378/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "conventions": CONVENTIONS, "theorem_contract": THEOREM,
        "finite_grid": {
            "dimension_N_min": 1, "dimension_N_max": 16, "dimension_row_count": 16,
            "level_N_min": 1, "level_N_max": 16, "level_degree_max": 64,
            "level_row_count": 1040, "partition_N_min": 1, "partition_N_max": 8,
            "partition_degree_max": 24,
            "partition_row_count": len(expected_partitions()), "kernel_row_count": 12,
        },
        "collision_boundary": {
            "C196": "deterministic rational Calogero-Moser scattering from a Hermitian pencil, not a stochastic confined eigenvalue diffusion",
            "C200": "one-dimensional Jacobi-Wright-Fisher diffusion with beta-polynomial spectrum, not a type-A interacting eigenvalue chamber",
            "C237": "hypoelliptic phase-space Kramers-Langevin flow, not an elliptic noncolliding eigenvalue process",
            "C306": "finite discrete nearest-neighbor walkers killed in a Weyl chamber, not continuous Hermitian Ornstein-Uhlenbeck eigenvalues",
        },
        "nonclaims": [
            "the source Fredholm determinant is not a target dynamical determinant or Euler product",
            "generic GUE statistics are not evidence of arithmetic origin or a target-zero match",
            "finite partition and kernel checks are regression evidence, not proof by sampling",
            "no target Euler factor, root number, automorphy, target divisor, target functional equation, or target zero match",
            "no Hilbert-Polya operator and no Route B",
        ],
        "references": [
            {"doi": "10.1063/1.1703862", "role": "matrix eigenvalue Brownian motion and Coulomb repulsion"},
            {"doi": "10.2140/pjm.1959.9.1141", "role": "determinantal noncoincidence kernel"},
            {"doi": "10.1007/s004400050092", "role": "strong solutions and electrostatic noncollision"},
            {"doi": "10.1007/s002200050161", "role": "generalized Hermite and Calogero-Sutherland spectral context"},
            {"numdam": "AIHPB_1999__35_2_177_0", "role": "Weyl-chamber reflection and noncolliding processes"},
        ],
        "scope_flags": FLAGS,
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED"},
        "finite_evidence_role": "exact dimension, partition, norm, multiplicity, and high-precision kernel regression only; analytic arguments prove the all-N theorem",
    }
    for key, expected in frozen.items():
        exact(obj[key], expected, key)
    temporary = dict(obj)
    claimed = temporary.pop("payload_sha256")
    assert type(claimed) is str and claimed == digest(temporary)
    dimensions = expected_dimensions()
    levels = expected_levels()
    partition_data = expected_partitions()
    exact(obj["dimension_rows"], dimensions, "dimension_rows")
    exact(obj["level_rows"], levels, "level_rows")
    exact(obj["partition_rows"], partition_data, "partition_rows")
    validate_kernels(obj["kernel_rows"])
    for key, value in {
        "dimension_rows": dimensions, "level_rows": levels,
        "partition_rows": partition_data, "kernel_rows": obj["kernel_rows"],
    }.items():
        exact(obj["section_sha256"][key], digest(value), f"section_sha256.{key}")
    exact_keys(obj["section_sha256"], {"dimension_rows", "level_rows", "partition_rows", "kernel_rows"}, "section hashes")
    print(
        "C378 checker PASS: "
        f"dimensions={len(dimensions)} levels={len(levels)} partitions={len(partition_data)} "
        f"kernels={len(obj['kernel_rows'])} payload={claimed}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"C378 checker FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
