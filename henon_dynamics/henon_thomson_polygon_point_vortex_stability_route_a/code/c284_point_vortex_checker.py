#!/usr/bin/env python3
"""Producer-independent raw-Hessian checker for HCS-C284."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get(
    "C284_EVIDENCE", ROOT / "results/c284_point_vortex_evidence.json"
))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
N_MIN, N_MAX = 3, 64
checks = 0

TOP_KEYS = {
    "analytic_proof_obligations", "audit_contract", "block_contract",
    "candidate_id", "evaluation_date", "evaluator", "fixed_epoch",
    "headline", "model_contract", "nonclaims", "payload_sha256",
    "proof_contract", "reduction_contract", "regression", "route_a",
    "schema", "scope_flags", "scope_literal", "source_commit",
    "source_owner_contract",
}
REGRESSION_KEYS = {
    "block_rows", "polygon_rows", "scale_rows", "slice_rows",
    "boundary_rows", "counts",
}
BLOCK_KEYS = {
    "n", "mode", "conjugate_mode", "q_m", "radial_hessian_over_c",
    "tangential_hessian_over_c", "det_hessian_over_c2",
    "lambda_squared_over_c2", "regime", "reduced_role", "spectral_pair",
}
POLYGON_KEYS = {
    "n", "omega_over_c", "max_q", "min_stability_sign",
    "degenerate_modes", "hyperbolic_modes", "hyperbolic_mode_count",
    "classification",
}
SCALE_KEYS = {
    "n", "gamma", "radius", "four_pi_c", "four_pi_omega",
    "stability_class_invariant_under_scale",
}
SLICE_KEYS = {
    "n", "total_dimension", "centered_dimension",
    "fixed_impulse_tangent_dimension", "reduced_dimension",
    "uniform_mode_removed_dimension", "first_harmonic_real_dimension",
    "translation_plane_dimension", "centered_first_harmonic_dimension",
    "centered_first_harmonic_frequency_over_c", "m0_restriction",
    "first_harmonic_restriction",
}
BOUNDARY_KEYS = {"face", "condition", "status"}

EXPECTED_HEADLINE = (
    "The equal positive point-vortex regular N-gon admits a complete "
    "Cartesian-Hessian/DFT block atlas: N=3..6 is reduced linearly "
    "elliptic, N=7 is linearly degenerate in modes 3 and 4 only, "
    "and every N>=8 has a real hyperbolic pair."
)
EXPECTED_AUDIT = {
    "json_policy": (
        "reject duplicate keys, unknown keys, missing keys, nonstandard "
        "constants, and bool-as-int type confusion"
    ),
    "row_policy": (
        "exact key sets, exact types, complete ordered coverage, and "
        "unique semantic keys"
    ),
    "slice_policy": (
        "raw Cartesian Hessian independently checks the m=0 rotation-scale "
        "chain and first-harmonic translation/complement subspaces"
    ),
}
EXPECTED_MODEL = {
    "hamiltonian": "H=-(Gamma^2/(2*pi))*sum_{j<k} log|z_j-z_k|",
    "symplectic_equation": "Gamma*z_j_dot=J*grad_j(H), J=[[0,1],[-1,0]]",
    "polygon": "z_j=R*(cos(2*pi*j/N),sin(2*pi*j/N)), N>=3, Gamma>0, R>0",
    "angular_velocity": "Omega=Gamma*(N-1)/(4*pi*R^2)",
    "augmented_hamiltonian": "G=H+(Gamma*Omega/2)*sum_j |z_j|^2",
    "clock": "physical point-vortex time",
    "scale": "c=Gamma/(4*pi*R^2)",
}
EXPECTED_BLOCK = {
    "local_dft": "radial-tangential unitary DFT in modes m=0,...,N-1",
    "root_sum": "S_m=sum_{k=1}^{N-1}(1-cos(m*theta_k))/(1-cos(theta_k))=m*(N-m)",
    "hessian_block": "Gamma^(-1)*D^2G_hat_m=c*diag(2*(N-1)-q_m,q_m), q_m=m*(N-m)",
    "linear_block": "L_m=c*[[0,q_m],[-(2*(N-1)-q_m),0]]",
    "square": "L_m^2=-c^2*q_m*(2*(N-1)-q_m)*I",
}
EXPECTED_REDUCTION = {
    "center": "fix center of vorticity at zero, removing the physical translation plane inside the first harmonic",
    "rotation_scale": "fix angular impulse and quotient rotations, removing the m=0 scale-rotation Jordan block",
    "first_harmonic_remainder": "the centered complementary first-harmonic plane is elliptic because its Hessian block is c*(N-1)*I",
    "classification": "all remaining signs are governed by 2*(N-1)-m*(N-m)",
}
EXPECTED_PROOF = {
    "status": "PROVABLE AS STATED",
    "dependencies": [
        "direct Cartesian pair-Hessian differentiation",
        "cyclic root-of-unity orthogonality",
        "radial-tangential DFT block diagonalization",
        "Hamiltonian two-by-two spectral classification",
        "explicit symmetry-slice vectors and invariant-subspace residuals",
    ],
    "scope": "equal nonzero point vortices on one finite-radius regular polygon; linearized reduced stability only",
    "heptagon_boundary": "N=7 is asserted only to be linearly degenerate in m=3,4; nonlinear stability is not claimed",
    "novelty_boundary": "classical owner results are reconstructed and executable; no literature-priority claim is made",
}
EXPECTED_SOURCE_OWNER = {
    "classical_owner": "J. J. Thomson, A Treatise on the Motion of Vortex Rings (1883)",
    "linear_stability_owner_doi": "10.1080/14786443109461714",
    "later_stability_context_doi": "10.1137/S0036141098302124",
    "polygonal_relative_equilibrium_doi": "10.1063/1.3646115",
    "use_boundary": "sources establish lineage and classical ownership; every displayed proof and executable count is reconstructed in-package",
}
EXPECTED_OBLIGATIONS = [
    "derive Omega directly from the source Hamiltonian",
    "differentiate the raw Cartesian pair Hessian and add the rotating-frame term",
    "derive every DFT block and prove the root-sum identity",
    "separate rotation, scale, translation, and centered first-harmonic directions",
    "verify symmetry-slice dimensions and invariant subspaces from the raw Hessian",
    "prove the N<=6, N=7, and N>=8 sign trichotomy",
    "keep Gamma=0, R=0, N<3, and N=7 nonlinear stability outside the claim",
]
EXPECTED_NONCLAIMS = [
    "No nonlinear stability theorem is claimed for the Thomson heptagon.",
    "No finite N-table is used as a proof of the all-N theorem.",
    "No rational-prime carrier, logarithmic-prime clock, target determinant, or target zero match is obtained.",
    "A single relative-equilibrium family is not a primitive-orbit census.",
    "The package does not claim invention or literature priority for the classical polygon theorem.",
]
EXPECTED_SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_authorization": False,
}


def claim(value: bool) -> None:
    global checks
    assert value
    checks += 1


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string JSON key: {key!r}")
        result[key] = value
    return result


def reject_constant(token: str) -> None:
    raise ValueError(f"nonstandard JSON constant: {token}")


def load_json_strict(path: Path) -> dict:
    value = json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=reject_constant,
    )
    if type(value) is not dict:
        raise ValueError("top-level JSON value must be an object")
    return value


def exact_keys(value: object, expected: set[str]) -> None:
    claim(type(value) is dict)
    claim(set(value) == expected)  # type: ignore[arg-type]


def exact_int(value: object) -> None:
    claim(type(value) is int)


def exact_str(value: object) -> None:
    claim(type(value) is str)


def exact_int_list(value: object) -> None:
    claim(type(value) is list)
    claim(all(type(item) is int for item in value))  # type: ignore[union-attr]


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(
        clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def regime(m: int, q: int, s: int) -> str:
    if m == 0:
        return "rotation_scale_jordan"
    if s > 0:
        return "elliptic"
    if s == 0:
        return "linear_degenerate_nilpotent"
    return "hyperbolic"


def reduced_role(n: int, m: int) -> str:
    if m == 0:
        return "uniform_rotation_and_scale_generalized_mode"
    if m in (1, n - 1):
        return "first_harmonic_translation_isotypic_and_centered_elliptic_complement"
    return "shape_mode"


def expected_boundaries() -> list[dict]:
    return [
        {"face": "n_below_domain", "condition": "N<3",
         "status": "excluded; N=1 is trivial and the centered N=2 polygon has no reduced shape degree of freedom"},
        {"face": "collision", "condition": "R=0",
         "status": "excluded logarithmic collision singularity"},
        {"face": "zero_circulation", "condition": "Gamma=0",
         "status": "the weighted symplectic form degenerates; only the zero-velocity limit is recorded"},
        {"face": "negative_common_circulation", "condition": "Gamma<0",
         "status": "time reversal of the positive-circulation convention; stability signs are unchanged"},
        {"face": "uniform_mode", "condition": "m=0",
         "status": "rotation kernel plus scale generalized vector; removed by fixed angular impulse and rotation quotient"},
        {"face": "first_harmonic", "condition": "m=1,N-1",
         "status": "contains the translation plane; after centering, its complementary plane remains elliptic with frequency Omega"},
        {"face": "heptagon", "condition": "N=7,m=3,4",
         "status": "nonzero nilpotent linear blocks; linear degeneracy only and no nonlinear-stability claim"},
        {"face": "large_radius", "condition": "R tends to infinity",
         "status": "all frequencies scale as Gamma/(4*pi*R^2) and tend to zero without changing the sign atlas"},
    ]


def mat2_left_right(qj: tuple[tuple[float, float], tuple[float, float]],
                    block: tuple[tuple[float, float], tuple[float, float]],
                    qk: tuple[tuple[float, float], tuple[float, float]]) -> tuple[tuple[float, float], tuple[float, float]]:
    """Return qj^T * block * qk without numerical-library dependencies."""
    temp = [[sum(block[a][b] * qk[b][d] for b in range(2))
             for d in range(2)] for a in range(2)]
    return tuple(tuple(sum(qj[a][c] * temp[a][d] for a in range(2))
                       for d in range(2)) for c in range(2))


def raw_cartesian_hessian(n: int):
    """Build Gamma^{-1} D^2(H+Gamma*Omega*I/2) at Gamma=R=1."""
    size = 2 * n
    points = [(math.cos(2 * math.pi * j / n),
               math.sin(2 * math.pi * j / n)) for j in range(n)]
    hessian = [[0.0 for _ in range(size)] for _ in range(size)]
    coefficient = 1.0 / (2.0 * math.pi)
    omega = (n - 1) / (4.0 * math.pi)
    for i in range(size):
        hessian[i][i] = omega
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            r2 = dx * dx + dy * dy
            pair = (
                (-coefficient * (1.0 / r2 - 2.0 * dx * dx / (r2 * r2)),
                 -coefficient * (-2.0 * dx * dy / (r2 * r2))),
                (-coefficient * (-2.0 * dx * dy / (r2 * r2)),
                 -coefficient * (1.0 / r2 - 2.0 * dy * dy / (r2 * r2))),
            )
            for a in range(2):
                for b in range(2):
                    hessian[2 * i + a][2 * i + b] += pair[a][b]
                    hessian[2 * j + a][2 * j + b] += pair[a][b]
                    hessian[2 * i + a][2 * j + b] -= pair[a][b]
                    hessian[2 * j + a][2 * i + b] -= pair[a][b]

    # Verify the augmented-gradient equilibrium independently.
    equilibrium_error = 0.0
    for i, point in enumerate(points):
        gx = gy = 0.0
        for j, other in enumerate(points):
            if i == j:
                continue
            dx, dy = point[0] - other[0], point[1] - other[1]
            r2 = dx * dx + dy * dy
            gx -= coefficient * dx / r2
            gy -= coefficient * dy / r2
        equilibrium_error = max(
            equilibrium_error,
            abs(gx + omega * point[0]),
            abs(gy + omega * point[1]),
        )
    return points, hessian, equilibrium_error


def local_blocks(n: int, points, hessian):
    rotations = [
        ((x, -y), (y, x)) for x, y in points
    ]
    blocks = []
    for k in range(n):
        raw = tuple(tuple(hessian[a][2 * k + b] for b in range(2))
                    for a in range(2))
        blocks.append(mat2_left_right(rotations[0], raw, rotations[k]))

    # The complete transformed Hessian must be block-circulant, not just its
    # first row.  This check is intentionally independent of the producer.
    cyclic_error = 0.0
    for j in range(n):
        for k in range(n):
            raw = tuple(tuple(hessian[2 * j + a][2 * k + b] for b in range(2))
                        for a in range(2))
            got = mat2_left_right(rotations[j], raw, rotations[k])
            want = blocks[(k - j) % n]
            for a in range(2):
                for b in range(2):
                    cyclic_error = max(cyclic_error, abs(got[a][b] - want[a][b]))
    return blocks, cyclic_error


def dft_block(blocks, m: int):
    n = len(blocks)
    values = [[0j, 0j], [0j, 0j]]
    for k, block in enumerate(blocks):
        angle = 2.0 * math.pi * m * k / n
        root = complex(math.cos(angle), math.sin(angle))
        for a in range(2):
            for b in range(2):
                values[a][b] += block[a][b] * root
    return values


def local_to_global(points, local_vector: list[float]) -> list[float]:
    result: list[float] = []
    for j, (x, y) in enumerate(points):
        radial, tangential = local_vector[2 * j:2 * j + 2]
        result.extend((x * radial - y * tangential,
                       y * radial + x * tangential))
    return result


def matrix_vector(matrix, vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector)))
            for row in matrix]


def apply_global_j(vector: list[float]) -> list[float]:
    result: list[float] = []
    for j in range(len(vector) // 2):
        x, y = vector[2 * j:2 * j + 2]
        result.extend((y, -x))
    return result


def max_residual(left: list[float], right: list[float]) -> float:
    return max(abs(a - b) for a, b in zip(left, right))


def center_sum(vector: list[float]) -> tuple[float, float]:
    return (
        sum(vector[2 * j] for j in range(len(vector) // 2)),
        sum(vector[2 * j + 1] for j in range(len(vector) // 2)),
    )


def main() -> None:
    data = load_json_strict(EVIDENCE)
    exact_keys(data, TOP_KEYS)
    claim(data["payload_sha256"] == payload_hash(data))
    exact_str(data["payload_sha256"])
    claim(data["schema"] == "hcs-c284-thomson-polygon-point-vortex-stability-v1")
    claim(data["candidate_id"] == "HCS-C284")
    claim(data["source_commit"] == SOURCE)
    claim(data["evaluation_date"] == "2026-09-02")
    claim(data["fixed_epoch"] == EPOCH)
    exact_int(data["fixed_epoch"])
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["headline"] == EXPECTED_HEADLINE)
    claim(data["audit_contract"] == EXPECTED_AUDIT)
    claim(data["model_contract"] == EXPECTED_MODEL)
    claim(data["block_contract"] == EXPECTED_BLOCK)
    claim(data["reduction_contract"] == EXPECTED_REDUCTION)
    claim(data["proof_contract"] == EXPECTED_PROOF)
    claim(data["source_owner_contract"] == EXPECTED_SOURCE_OWNER)
    claim(data["analytic_proof_obligations"] == EXPECTED_OBLIGATIONS)
    claim(data["nonclaims"] == EXPECTED_NONCLAIMS)
    claim(type(data["analytic_proof_obligations"]) is list)
    claim(type(data["nonclaims"]) is list)
    claim(data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED",
                               "route_b_invocation_allowed": False})
    exact_keys(data["route_a"], {"tuple", "overall", "route_b_invocation_allowed"})
    claim(type(data["route_a"]["tuple"]) is list)
    claim(data["route_a"]["route_b_invocation_allowed"] is False)
    claim(data["scope_flags"] == EXPECTED_SCOPE_FLAGS)
    exact_keys(data["scope_flags"], set(EXPECTED_SCOPE_FLAGS))
    claim(all(value is False for value in data["scope_flags"].values()))
    for contract, expected in (
        (data["audit_contract"], EXPECTED_AUDIT),
        (data["model_contract"], EXPECTED_MODEL),
        (data["block_contract"], EXPECTED_BLOCK),
        (data["reduction_contract"], EXPECTED_REDUCTION),
        (data["proof_contract"], EXPECTED_PROOF),
        (data["source_owner_contract"], EXPECTED_SOURCE_OWNER),
    ):
        exact_keys(contract, set(expected))

    rows = data["regression"]["block_rows"]
    exact_keys(data["regression"], REGRESSION_KEYS)
    claim(type(rows) is list)
    claim(len(rows) == 2077)
    claim(all(type(row) is dict for row in rows))
    claim(all(set(row) == BLOCK_KEYS for row in rows))
    claim([(row["n"], row["mode"]) for row in rows] == [
        (n, m) for n in range(N_MIN, N_MAX + 1) for m in range(n)
    ])
    seen: set[tuple[int, int]] = set()
    rows_by_n: dict[int, list[dict]] = {n: [] for n in range(N_MIN, N_MAX + 1)}
    for row in rows:
        n, m = row["n"], row["mode"]
        for key in (
            "n", "mode", "conjugate_mode", "q_m",
            "radial_hessian_over_c", "tangential_hessian_over_c",
            "det_hessian_over_c2", "lambda_squared_over_c2",
        ):
            exact_int(row[key])
        for key in ("regime", "reduced_role", "spectral_pair"):
            exact_str(row[key])
        claim(N_MIN <= n <= N_MAX and 0 <= m < n)
        claim((n, m) not in seen)
        seen.add((n, m))
        rows_by_n[n].append(row)
        q = m * (n - m)
        s = 2 * (n - 1) - q
        claim(row["conjugate_mode"] == (-m) % n)
        claim(row["q_m"] == q)
        claim(row["radial_hessian_over_c"] == s)
        claim(row["tangential_hessian_over_c"] == q)
        claim(row["det_hessian_over_c2"] == q * s)
        claim(row["lambda_squared_over_c2"] == -q * s)
        claim(row["regime"] == regime(m, q, s))
        claim(row["reduced_role"] == reduced_role(n, m))
        if m == 0:
            claim(row["spectral_pair"] == "zero_double_nonsemisimple")
        elif s > 0:
            claim(row["spectral_pair"] == f"plus_minus_i_sqrt_{q * s}_times_c")
        elif s == 0:
            claim(row["spectral_pair"] == "zero_double_nonsemisimple")
        else:
            claim(row["spectral_pair"] == f"plus_minus_sqrt_{q * (-s)}_times_c")
    claim(seen == {(n, m) for n in range(N_MIN, N_MAX + 1) for m in range(n)})

    # The central independence gate: reconstruct the raw 2N by 2N Cartesian
    # Hessian, prove its local form is block-circulant, and DFT it numerically.
    raw_tolerance = 3.0e-9
    for n in range(N_MIN, N_MAX + 1):
        points, hessian, equilibrium_error = raw_cartesian_hessian(n)
        claim(equilibrium_error < raw_tolerance)
        symmetry_error = max(abs(hessian[i][j] - hessian[j][i])
                             for i in range(2 * n) for j in range(2 * n))
        claim(symmetry_error < raw_tolerance)
        blocks, cyclic_error = local_blocks(n, points, hessian)
        claim(cyclic_error < raw_tolerance)
        c = 1.0 / (4.0 * math.pi)
        omega = c * (n - 1)

        # Build the symmetry and centered first-harmonic planes directly in
        # local coordinates, then test them against the raw Cartesian Hessian.
        scale_local = [component for _ in points for component in (1.0, 0.0)]
        rotation_local = [component for _ in points for component in (0.0, 1.0)]
        translation_x_local = [component for x, y in points for component in (x, -y)]
        translation_y_local = [component for x, y in points for component in (y, x)]
        complement_one_local = [component for x, y in points for component in (x, y)]
        complement_two_local = [component for x, y in points for component in (-y, x)]
        local_vectors = {
            "scale": scale_local,
            "rotation": rotation_local,
            "translation_x": translation_x_local,
            "translation_y": translation_y_local,
            "complement_one": complement_one_local,
            "complement_two": complement_two_local,
        }
        global_vectors = {
            name: local_to_global(points, vector)
            for name, vector in local_vectors.items()
        }
        hessian_images = {
            name: matrix_vector(hessian, vector)
            for name, vector in global_vectors.items()
        }
        claim(max_residual(
            hessian_images["scale"],
            [2.0 * omega * value for value in global_vectors["scale"]],
        ) < raw_tolerance)
        claim(max_residual(
            hessian_images["rotation"], [0.0] * (2 * n),
        ) < raw_tolerance)
        for name in (
            "translation_x", "translation_y",
            "complement_one", "complement_two",
        ):
            claim(max_residual(
                hessian_images[name],
                [omega * value for value in global_vectors[name]],
            ) < raw_tolerance)

        linear_images = {
            name: apply_global_j(image)
            for name, image in hessian_images.items()
        }
        claim(max_residual(
            linear_images["scale"],
            [-2.0 * omega * value for value in global_vectors["rotation"]],
        ) < raw_tolerance)
        claim(max_residual(
            linear_images["rotation"], [0.0] * (2 * n),
        ) < raw_tolerance)
        claim(max_residual(
            linear_images["translation_x"],
            [-omega * value for value in global_vectors["translation_y"]],
        ) < raw_tolerance)
        claim(max_residual(
            linear_images["translation_y"],
            [omega * value for value in global_vectors["translation_x"]],
        ) < raw_tolerance)
        claim(max_residual(
            linear_images["complement_one"],
            [-omega * value for value in global_vectors["complement_two"]],
        ) < raw_tolerance)
        claim(max_residual(
            linear_images["complement_two"],
            [omega * value for value in global_vectors["complement_one"]],
        ) < raw_tolerance)

        center_tolerance = raw_tolerance * n
        claim(max(abs(value) for value in center_sum(
            global_vectors["complement_one"]
        )) < center_tolerance)
        claim(max(abs(value) for value in center_sum(
            global_vectors["complement_two"]
        )) < center_tolerance)
        claim(max_residual(
            list(center_sum(global_vectors["translation_x"])), [float(n), 0.0]
        ) < center_tolerance)
        claim(max_residual(
            list(center_sum(global_vectors["translation_y"])), [0.0, float(n)]
        ) < center_tolerance)
        claim(abs(sum(scale_local[::2]) - n) < center_tolerance)
        for name in (
            "rotation", "translation_x", "translation_y",
            "complement_one", "complement_two",
        ):
            claim(abs(sum(local_vectors[name][::2])) < center_tolerance)

        for row in rows_by_n[n]:
            m = row["mode"]
            q = m * (n - m)
            s = 2 * (n - 1) - q
            block = dft_block(blocks, m)
            claim(abs(block[0][0].real / c - s) < raw_tolerance)
            claim(abs(block[1][1].real / c - q) < raw_tolerance)
            claim(abs(block[0][0].imag / c) < raw_tolerance)
            claim(abs(block[1][1].imag / c) < raw_tolerance)
            claim(abs(block[0][1] / c) < raw_tolerance)
            claim(abs(block[1][0] / c) < raw_tolerance)
            # J*diag(s,q) squares to -q*s times the identity.
            l01 = block[1][1]
            l10 = -block[0][0]
            # The product amplifies the two O(1e-11) block-entry errors by
            # O(N^2); the absolute dimensionless residual stays below 2e-8.
            claim(abs((l01 * l10).real / (c * c) + q * s) < 1.0e-7)
            reconstructed = (
                "rotation_scale_jordan" if m == 0 else
                "elliptic" if (l01 * l10).real < -raw_tolerance * c * c else
                "linear_degenerate_nilpotent" if abs((l01 * l10).real) <= raw_tolerance * c * c else
                "hyperbolic"
            )
            claim(reconstructed == row["regime"])

    polygons = data["regression"]["polygon_rows"]
    claim(type(polygons) is list)
    claim(len(polygons) == 62)
    claim(all(type(row) is dict and set(row) == POLYGON_KEYS for row in polygons))
    claim([row["n"] for row in polygons] == list(range(N_MIN, N_MAX + 1)))
    for row in polygons:
        for key in (
            "n", "omega_over_c", "max_q", "min_stability_sign",
            "hyperbolic_mode_count",
        ):
            exact_int(row[key])
        exact_int_list(row["degenerate_modes"])
        exact_int_list(row["hyperbolic_modes"])
        exact_str(row["classification"])
        n = row["n"]
        q_values = [m * (n - m) for m in range(n)]
        s_values = [2 * (n - 1) - q for q in q_values]
        degenerates = [m for m in range(n) if m != 0 and s_values[m] == 0]
        hyperbolics = [m for m in range(n) if s_values[m] < 0]
        classification = (
            "reduced_linearly_elliptic" if n <= 6 else
            "reduced_linearly_degenerate_not_a_nonlinear_claim" if n == 7 else
            "reduced_linearly_hyperbolic_unstable"
        )
        claim(row["omega_over_c"] == n - 1)
        claim(row["max_q"] == max(q_values))
        claim(row["min_stability_sign"] == min(s_values))
        claim(row["degenerate_modes"] == degenerates)
        claim(row["hyperbolic_modes"] == hyperbolics)
        claim(row["hyperbolic_mode_count"] == len(hyperbolics))
        claim(row["classification"] == classification)
    claim(polygons[4]["n"] == 7 and polygons[4]["degenerate_modes"] == [3, 4])
    claim(polygons[5]["n"] == 8 and polygons[5]["hyperbolic_modes"] == [3, 4, 5])

    scales = data["regression"]["scale_rows"]
    claim(type(scales) is list)
    claim(len(scales) == 64)
    claim(all(type(row) is dict and set(row) == SCALE_KEYS for row in scales))
    expected_scale_keys = {
        (n, gamma, radius)
        for n in (3, 7, 8, 16)
        for gamma in (Q(1, 2), Q(1), Q(2), Q(5))
        for radius in (Q(1, 2), Q(1), Q(2), Q(4))
    }
    seen_scale_keys = set()
    for row in scales:
        exact_int(row["n"])
        for key in ("gamma", "radius", "four_pi_c", "four_pi_omega"):
            exact_str(row[key])
        claim(type(row["stability_class_invariant_under_scale"]) is bool)
        n, gamma, radius = row["n"], Q(row["gamma"]), Q(row["radius"])
        seen_scale_keys.add((n, gamma, radius))
        four_pi_c = gamma / (radius * radius)
        claim(Q(row["four_pi_c"]) == four_pi_c)
        claim(Q(row["four_pi_omega"]) == (n - 1) * four_pi_c)
        claim(row["stability_class_invariant_under_scale"] is True)
    claim(seen_scale_keys == expected_scale_keys)

    slices = data["regression"]["slice_rows"]
    claim(type(slices) is list)
    claim(len(slices) == 7)
    claim(all(type(row) is dict and set(row) == SLICE_KEYS for row in slices))
    claim([row["n"] for row in slices] == [3, 4, 6, 7, 8, 16, 64])
    for row in slices:
        for key in SLICE_KEYS - {"m0_restriction", "first_harmonic_restriction"}:
            exact_int(row[key])
        exact_str(row["m0_restriction"])
        exact_str(row["first_harmonic_restriction"])
        n = row["n"]
        claim(row == {
            "n": n,
            "total_dimension": 2 * n,
            "centered_dimension": 2 * n - 2,
            "fixed_impulse_tangent_dimension": 2 * n - 3,
            "reduced_dimension": 2 * n - 4,
            "uniform_mode_removed_dimension": 2,
            "first_harmonic_real_dimension": 4,
            "translation_plane_dimension": 2,
            "centered_first_harmonic_dimension": 2,
            "centered_first_harmonic_frequency_over_c": n - 1,
            "m0_restriction": "removed_by_fixed_impulse_and_rotation",
            "first_harmonic_restriction": (
                "translation_plane_removed_centered_complement_elliptic"
            ),
        })

    boundaries = data["regression"]["boundary_rows"]
    claim(type(boundaries) is list)
    claim(all(type(row) is dict and set(row) == BOUNDARY_KEYS for row in boundaries))
    claim(all(all(type(value) is str for value in row.values()) for row in boundaries))
    claim(boundaries == expected_boundaries())
    counts = data["regression"]["counts"]
    exact_keys(counts, {
        "block_rows", "polygon_rows", "scale_rows", "slice_rows",
        "boundary_rows",
    })
    claim(all(type(value) is int for value in counts.values()))
    claim(data["regression"]["counts"] == {
        "block_rows": 2077, "polygon_rows": 62,
        "scale_rows": 64, "slice_rows": 7, "boundary_rows": 8,
    })
    print(
        f"C284 independent raw-Hessian checker: PASS ({checks} assertions; "
        "producer-independent 2N x 2N reconstruction for N=3..64)"
    )


if __name__ == "__main__":
    main()
