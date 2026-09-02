#!/usr/bin/env python3
"""Independent exact SymPy reconstruction for HCS-C284."""
from __future__ import annotations

import sympy as s

checks: list[s.Expr] = []


def record_matrix(matrix: s.Matrix) -> None:
    checks.extend(s.simplify(value) for value in matrix)


# Abstract Hamiltonian two-by-two block.
c, q, sigma, lam = s.symbols("c q sigma lambda", real=True)
J = s.Matrix([[0, 1], [-1, 0]])
K = c * s.diag(sigma, q)
L = J * K
record_matrix(L * L + c**2 * q * sigma * s.eye(2))
checks.append(s.factor(L.det() - c**2 * q * sigma))
checks.append(s.factor(L.trace()))
checks.append(s.factor((lam * s.eye(2) - L).det() - (lam**2 + c**2 * q * sigma)))


def exact_raw_hessian(n: int) -> None:
    """Differentiate the Cartesian pair potential and DFT it exactly."""
    size = 2 * n
    points = [s.Matrix([
        s.cos(2 * s.pi * j / n), s.sin(2 * s.pi * j / n)
    ]) for j in range(n)]
    hessian = (n - 1) * s.eye(size) / (4 * s.pi)
    coefficient = 1 / (2 * s.pi)
    for i in range(n):
        for j in range(i + 1, n):
            d = points[i] - points[j]
            r2 = (d.T * d)[0]
            pair = -coefficient * (s.eye(2) / r2 - 2 * d * d.T / r2**2)
            for a in range(2):
                for b in range(2):
                    hessian[2 * i + a, 2 * i + b] += pair[a, b]
                    hessian[2 * j + a, 2 * j + b] += pair[a, b]
                    hessian[2 * i + a, 2 * j + b] -= pair[a, b]
                    hessian[2 * j + a, 2 * i + b] -= pair[a, b]

    # Exact equilibrium gradient at Gamma=R=1.
    omega = s.Rational(n - 1, 1) / (4 * s.pi)
    for i, point in enumerate(points):
        gradient = s.zeros(2, 1)
        for j, other in enumerate(points):
            if i == j:
                continue
            d = point - other
            gradient -= coefficient * d / (d.T * d)[0]
        record_matrix(s.simplify(s.expand_trig(gradient + omega * point)))

    # Independently identify the raw symmetry slice in Cartesian coordinates.
    # These vectors do not use the closed DFT block formula.
    local_vectors = {
        "scale": s.Matrix([value for _ in points for value in (1, 0)]),
        "rotation": s.Matrix([value for _ in points for value in (0, 1)]),
        "translation_x": s.Matrix([
            value for point in points for value in (point[0], -point[1])
        ]),
        "translation_y": s.Matrix([
            value for point in points for value in (point[1], point[0])
        ]),
        "complement_one": s.Matrix([
            value for point in points for value in (point[0], point[1])
        ]),
        "complement_two": s.Matrix([
            value for point in points for value in (-point[1], point[0])
        ]),
    }

    def to_global(local: s.Matrix) -> s.Matrix:
        answer = s.zeros(size, 1)
        for j, point in enumerate(points):
            rotation = s.Matrix([
                [point[0], -point[1]],
                [point[1], point[0]],
            ])
            answer[2 * j:2 * j + 2, 0] = rotation * local[2 * j:2 * j + 2, 0]
        return answer

    global_vectors = {name: to_global(vector) for name, vector in local_vectors.items()}
    record_matrix(s.simplify(hessian * global_vectors["scale"] -
                             2 * omega * global_vectors["scale"]))
    record_matrix(s.simplify(hessian * global_vectors["rotation"]))
    for name in ("translation_x", "translation_y", "complement_one", "complement_two"):
        record_matrix(s.simplify(hessian * global_vectors[name] - omega * global_vectors[name]))

    Jn = s.diag(*([J] * n))
    linear_images = {name: Jn * hessian * vector for name, vector in global_vectors.items()}
    record_matrix(s.simplify(linear_images["scale"] +
                             2 * omega * global_vectors["rotation"]))
    record_matrix(s.simplify(linear_images["rotation"]))
    record_matrix(s.simplify(linear_images["translation_x"] +
                             omega * global_vectors["translation_y"]))
    record_matrix(s.simplify(linear_images["translation_y"] -
                             omega * global_vectors["translation_x"]))
    record_matrix(s.simplify(linear_images["complement_one"] +
                             omega * global_vectors["complement_two"]))
    record_matrix(s.simplify(linear_images["complement_two"] -
                             omega * global_vectors["complement_one"]))
    for name in ("complement_one", "complement_two"):
        checks.append(s.simplify(sum(global_vectors[name][0::2, 0])))
        checks.append(s.simplify(sum(global_vectors[name][1::2, 0])))
    checks.append(s.simplify(sum(local_vectors["scale"][0::2, 0]) - n))
    for name in ("rotation", "translation_x", "translation_y", "complement_one", "complement_two"):
        checks.append(s.simplify(sum(local_vectors[name][0::2, 0])))

    blocks = []
    for k in range(n):
        angle = 2 * s.pi * k / n
        rotation = s.Matrix([
            [s.cos(angle), -s.sin(angle)],
            [s.sin(angle), s.cos(angle)],
        ])
        blocks.append(hessian[:2, 2 * k:2 * k + 2] * rotation)
    for m in range(n):
        block = sum(
            (blocks[k] * s.exp(2 * s.pi * s.I * m * k / n)
             for k in range(n)),
            s.zeros(2),
        )
        q_m = m * (n - m)
        sigma_m = 2 * (n - 1) - q_m
        target = s.diag(sigma_m, q_m) / (4 * s.pi)
        record_matrix(s.simplify(s.expand_complex(block - target)))


# These three polygons exercise rational, square-root, and sixth-root fields.
for polygon_size in (3, 4, 6):
    exact_raw_hessian(polygon_size)


# Exact root-sum identity.  Rather than inserting N*m as an assumption, count
# every exponent pair in the finite orthogonality sum.  Since 0<=r,s<m<N,
# r-s is divisible by N exactly on the diagonal r=s.
for n in range(3, 65):
    for m in range(n):
        full_root_sum = sum(
            n if (r - t) % n == 0 else 0
            for r in range(m) for t in range(m)
        )
        k_zero_term = m * m
        checks.append(s.Integer(full_root_sum - n * m))
        checks.append(s.Integer(full_root_sum - k_zero_term - m * (n - m)))

# Exact singular and first unstable cells.
checks.extend([
    s.Integer(3 * (7 - 3) - 2 * (7 - 1)),
    s.Integer(4 * (7 - 4) - 2 * (7 - 1)),
    s.Integer(2 * (8 - 1) - 3 * (8 - 3) + 1),
    s.Integer(2 * (8 - 1) - 4 * (8 - 4) + 2),
])

bad = [value for value in checks if s.simplify(value) != 0]
assert not bad, bad
print(
    f"C284_SYMPY_PASS ({len(checks)} exact identities; raw Cartesian "
    "Hessians and symmetry slices for N=3,4,6 plus coefficient-counted "
    "N=3..64 root sums)"
)
