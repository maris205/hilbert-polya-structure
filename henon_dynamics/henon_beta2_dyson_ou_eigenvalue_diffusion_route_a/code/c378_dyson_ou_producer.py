#!/usr/bin/env python3
"""Canonical evidence producer for HCS-C378 beta-two Dyson--OU diffusion."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c378 producer refuses optimized Python")

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c378_dyson_ou_evidence.json"
EVAL = ROOT / "evaluations/route_a/HCS-C378/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "b70bfed7319e0ebfd5697491a29c11bd803eab74f66fb303a6f3d11c1e475af9"
YAML_SEMANTIC_SHA = "6d374dfee088737ada5dc669e7b597844b6da08d26ce5e7ec13313df03766b3f"


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
        raise TypeError("YAML root must be a mapping")
    return value


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def partitions(total: int, max_parts: int, ceiling: int | None = None):
    """Partitions in reverse lexicographic order, padded only by the caller."""
    if max_parts == 0:
        if total == 0:
            yield ()
        return
    if total == 0:
        yield ()
        return
    upper = min(total, total if ceiling is None else ceiling)
    for first in range(upper, 0, -1):
        for tail in partitions(total - first, max_parts - 1, first):
            yield (first,) + tail


def partition_count(total: int, max_part: int) -> int:
    coefficients = [0] * (total + 1)
    coefficients[0] = 1
    for part in range(1, max_part + 1):
        for degree in range(part, total + 1):
            coefficients[degree] += coefficients[degree - part]
    return coefficients[total]


def dimension_rows():
    rows = []
    for n in range(1, 17):
        d = n * (n - 1) // 2
        normalizer_factor = math.prod(math.factorial(j) for j in range(n))
        rows.append(
            {
                "N": n,
                "hermitian_real_dimension": n * n,
                "vandermonde_degree": d,
                "doob_energy_shift": frac(Fraction(d, 2)),
                "spectral_gap": frac(Fraction(1, 2)),
                "chamber_normalizer_over_(2pi)^(N/2)": normalizer_factor,
                "ground_slater_indices": list(range(n)),
                "ground_slater_index_sum": d,
            }
        )
    return rows


def level_rows():
    rows = []
    for n in range(1, 17):
        for degree in range(65):
            count = partition_count(degree, n)
            rows.append(
                {
                    "N": n,
                    "degree": degree,
                    "partition_multiplicity": count,
                    "generator_eigenvalue": frac(Fraction(-degree, 2)),
                    "semigroup_exponent": frac(Fraction(degree, 2)),
                }
            )
    return rows


def partition_rows():
    rows = []
    for n in range(1, 9):
        denominator = math.prod(math.factorial(j) for j in range(n))
        d = n * (n - 1) // 2
        for degree in range(25):
            level_partitions = list(partitions(degree, n))
            assert len(level_partitions) == partition_count(degree, n)
            for rank, raw_partition in enumerate(level_partitions):
                padded = list(raw_partition) + [0] * (n - len(raw_partition))
                indices = [padded[n - 1 - i] + i for i in range(n)]
                assert all(indices[i] < indices[i + 1] for i in range(n - 1))
                assert sum(indices) == d + degree
                numerator = math.prod(math.factorial(value) for value in indices)
                ratio = Fraction(numerator, denominator)
                rows.append(
                    {
                        "N": n,
                        "degree": degree,
                        "rank": rank,
                        "partition": padded,
                        "slater_indices": indices,
                        "slater_index_sum": sum(indices),
                        "quotient_degree": degree,
                        "generator_eigenvalue": frac(Fraction(-degree, 2)),
                        "squared_norm": frac(ratio),
                    }
                )
    return rows


def vandermonde(values):
    product = mp.mpf(1)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            product *= values[j] - values[i]
    return product


def scalar_kernel(x, y, r):
    variance = 1 - r * r
    return mp.exp(-((y - r * x) ** 2) / (2 * variance)) / mp.sqrt(2 * mp.pi * variance)


def determinant_kernel(x, y, r):
    matrix = mp.matrix([[scalar_kernel(xi, yj, r) for yj in y] for xi in x])
    return mp.det(matrix)


def decimal(value) -> str:
    return mp.nstr(value, 50, strip_zeros=False)


def kernel_rows():
    mp.mp.dps = 90
    point_sets = {
        2: ((-2, 1), (-1, 2)),
        3: ((-3, 0, 2), (-2, 1, 4)),
        4: ((-4, -1, 1, 5), (-3, 0, 2, 6)),
    }
    contractions = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))
    rows = []
    for n, (x_raw, y_raw) in point_sets.items():
        x = tuple(mp.mpf(value) for value in x_raw)
        y = tuple(mp.mpf(value) for value in y_raw)
        h_x, h_y = vandermonde(x), vandermonde(y)
        d = n * (n - 1) // 2
        for contraction in contractions:
            r = mp.mpf(contraction.numerator) / contraction.denominator
            q_xy = determinant_kernel(x, y, r)
            q_yx = determinant_kernel(y, x, r)
            k_xy = r ** (-d) * h_y / h_x * q_xy
            k_yx = r ** (-d) * h_x / h_y * q_yx
            rho_x = mp.exp(-sum(value * value for value in x) / 2) * h_x * h_x
            rho_y = mp.exp(-sum(value * value for value in y) / 2) * h_y * h_y
            left, right = rho_x * k_xy, rho_y * k_yx
            residual = abs(left - right) / max(abs(left), abs(right))
            assert q_xy > 0 and k_xy > 0 and residual < mp.mpf("1e-75")
            rows.append(
                {
                    "N": n,
                    "x": list(x_raw),
                    "y": list(y_raw),
                    "contraction_r": frac(contraction),
                    "variance": frac(1 - contraction * contraction),
                    "vandermonde_x": int(h_x),
                    "vandermonde_y": int(h_y),
                    "killed_determinant_q_xy_decimal_50": decimal(q_xy),
                    "doob_kernel_k_xy_decimal_50": decimal(k_xy),
                    "relative_detailed_balance_residual_decimal_50": decimal(residual),
                }
            )
    return rows


FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data",
        "claims_target_euler_factors",
        "claims_root_number",
        "claims_automorphy",
        "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation",
        "claims_target_zero_match",
        "claims_hilbert_polya_operator",
        "invokes_route_b",
    )
}


def build(evaluation_path: Path):
    raw = evaluation_path.read_bytes()
    semantic = load_yaml(evaluation_path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(semantic) == YAML_SEMANTIC_SHA
    dimensions = dimension_rows()
    levels = level_rows()
    partition_data = partition_rows()
    kernels = kernel_rows()
    sections = {
        "dimension_rows": dimensions,
        "level_rows": levels,
        "partition_rows": partition_data,
        "kernel_rows": kernels,
    }
    body = {
        "schema": "hcs-c378-beta2-dyson-ou-evidence-v1",
        "candidate_id": "HCS-C378",
        "obstruction_id": "HEN-O362",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": AUTHORITY_SHA,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C378/2026-09-04.yaml",
            "raw_sha256": YAML_RAW_SHA,
            "semantic_sha256": YAML_SEMANTIC_SHA,
        },
        "conventions": {
            "matrix_sde": "dH=dB-H*dt/2 on Herm_N with trace inner product",
            "ordered_chamber": "W_N={x_1<...<x_N}",
            "eigenvalue_sde": "dX_i=dB_i+sum_{j!=i}1/(X_i-X_j)*dt-X_i*dt/2",
            "scalar_ou_generator": "L0=sum_i(partial_i^2-x_i*partial_i)/2",
            "scalar_ou_contraction": "r=exp(-t/2), variance=1-r^2",
            "vandermonde": "h(x)=product_{i<j}(x_j-x_i)>0 on W_N",
            "vandermonde_degree": "d=N*(N-1)/2 and L0*h=-d*h/2",
            "chamber_density": "pi_N=Z_N^-1*exp(-|x|^2/2)*h(x)^2",
            "normalizer": "Z_N=(2*pi)^(N/2)*product_{j=0}^{N-1}j!",
        },
        "theorem_contract": {
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
        },
        "finite_grid": {
            "dimension_N_min": 1,
            "dimension_N_max": 16,
            "dimension_row_count": len(dimensions),
            "level_N_min": 1,
            "level_N_max": 16,
            "level_degree_max": 64,
            "level_row_count": len(levels),
            "partition_N_min": 1,
            "partition_N_max": 8,
            "partition_degree_max": 24,
            "partition_row_count": len(partition_data),
            "kernel_row_count": len(kernels),
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
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "theorem_status": "PROVABLE_AS_STATED",
        },
        "finite_evidence_role": "exact dimension, partition, norm, multiplicity, and high-precision kernel regression only; analytic arguments prove the all-N theorem",
        **sections,
        "section_sha256": {key: digest(value) for key, value in sections.items()},
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=EVAL)
    args = parser.parse_args()
    value = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n")
    grid = value["finite_grid"]
    print(
        "C378 producer PASS: "
        f"dimensions={grid['dimension_row_count']} levels={grid['level_row_count']} "
        f"partitions={grid['partition_row_count']} kernels={grid['kernel_row_count']} "
        f"payload={value['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
