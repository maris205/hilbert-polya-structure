#!/usr/bin/env python3
"""Write symbolic/numerical geometry and known-truth control certificates."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
import sympy as sp

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.controls import control_certificate
from henon_zeta.geometry import (
    fixed_points,
    generating_momenta,
    henon_inverse,
    henon_jacobian,
    henon_map,
    reversor,
)


def symbolic_certificate() -> dict[str, object]:
    x, y, a, q, q_next = sp.symbols("x y a q q_next", real=True)
    H = sp.Matrix([1 - a * x**2 - y, x])
    jacobian = H.jacobian((x, y))
    inverse = sp.Matrix([y, 1 - a * y**2 - x])
    Rxy = sp.Matrix([y, x])
    H_at_R = sp.Matrix([1 - a * Rxy[0] ** 2 - Rxy[1], Rxy[0]])
    R_H_R = sp.Matrix([H_at_R[1], H_at_R[0]])
    S = q * q_next - q + a * q**3 / 3
    return {
        "det_DH": str(sp.simplify(jacobian.det())),
        "inverse": [str(value) for value in inverse],
        "RHR_equals_inverse": bool(all(sp.simplify(R_H_R[i] - inverse[i]) == 0 for i in range(2))),
        "generating_function": str(S),
        "minus_dS_dq": str(sp.simplify(-sp.diff(S, q))),
        "dS_dq_next": str(sp.simplify(sp.diff(S, q_next))),
        "fixed_point_polynomial": str(a * q**2 + 2 * q - 1),
    }


def numerical_certificate(a_value: float, samples: int, seed: int) -> dict[str, object]:
    generator = np.random.default_rng(seed)
    inverse_errors: list[float] = []
    reversor_errors: list[float] = []
    determinant_errors: list[float] = []
    generating_errors: list[float] = []
    for _ in range(samples):
        point = generator.uniform(-2.5, 2.5, size=2)
        inverse_errors.append(float(np.max(np.abs(henon_inverse(henon_map(point, a_value), a_value) - point))))
        lhs = reversor(henon_map(reversor(point), a_value))
        rhs = henon_inverse(point, a_value)
        reversor_errors.append(float(np.max(np.abs(lhs - rhs))))
        determinant_errors.append(abs(float(np.linalg.det(henon_jacobian(point, a_value))) - 1.0))

        q = float(point[0])
        q_next = float(henon_map(point, a_value)[0])
        p, p_next = generating_momenta(q, q_next, a_value)
        generating_errors.append(max(abs(p - float(point[1])), abs(p_next - q)))

    fixed = []
    for record in fixed_points(a_value):
        point = np.array([record.coordinate, record.coordinate])
        fixed.append(
            {
                "coordinate": record.coordinate,
                "map_residual_inf": float(np.max(np.abs(henon_map(point, a_value) - point))),
                "trace": record.trace,
                "determinant": record.determinant,
                "stability": record.stability,
                "eigenvalues": [[value.real, value.imag] for value in record.eigenvalues],
            }
        )
    return {
        "a": a_value,
        "samples": samples,
        "seed": seed,
        "max_inverse_error": max(inverse_errors, default=0.0),
        "max_reversor_error": max(reversor_errors, default=0.0),
        "max_determinant_error": max(determinant_errors, default=0.0),
        "max_generating_relation_error": max(generating_errors, default=0.0),
        "fixed_points": fixed,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", nargs="+", type=float, default=[1.0056, 1.02])
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260731)
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "results" / "geometry_certificate.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = {
        "run_id": "R000_geometry_controls",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "sympy": sp.__version__,
        "symbolic": symbolic_certificate(),
        "numerical": [
            numerical_certificate(a_value, args.samples, args.seed + index)
            for index, a_value in enumerate(args.a)
        ],
        "controls": control_certificate(max_period=12),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "run_id": payload["run_id"]}, indent=2))


if __name__ == "__main__":
    main()
