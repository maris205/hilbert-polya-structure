#!/usr/bin/env python3
"""Separate SymPy reconstruction for the HCS-C167 theorem constants."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256")
    return sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path,
                        default=root / "results/c167_rectangle_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0
    assert data["payload_sha256"] == payload_hash(data); checks += 1

    alpha, s, j, k = sp.symbols("alpha s j k", positive=True)
    left = (s / alpha) * sp.sqrt(k**2 + alpha**2 * j**2)
    right = s * sp.sqrt(j**2 + k**2 / alpha**2)
    assert sp.simplify(left - right) == 0; checks += 1

    energy, area = sp.symbols("E area", positive=True)
    time = 2 * sp.sqrt(energy)
    magnitude = sp.simplify(
        area * time / (2 * sp.pi) / (2 * time) ** sp.Rational(3, 2)
    )
    assert sp.simplify(magnitude - area / (8 * sp.pi * energy ** sp.Rational(1, 4))) == 0
    checks += 1
    phase = sp.exp(-sp.I * sp.pi / 2) * sp.exp(3 * sp.I * sp.pi / 4)
    assert sp.simplify(phase - sp.exp(sp.I * sp.pi / 4)) == 0; checks += 1

    beta = sp.symbols("beta", real=True)
    m, n, mp_, np_ = sp.symbols("m n mp np", integer=True)
    difference = m**2 + beta * n**2 - mp_**2 - beta * np_**2
    beta_zero = sp.simplify((mp_**2 - m**2) / (n**2 - np_**2))
    assert sp.simplify(difference.subs(beta, beta_zero)) == 0; checks += 1
    assert sp.diff(difference, beta) == n**2 - np_**2; checks += 1
    common_energy = sp.symbols("E0", positive=True)
    time_derivative = sp.simplify(
        sp.diff(2 * sp.sqrt(m**2 + beta * n**2), beta) -
        sp.diff(2 * sp.sqrt(mp_**2 + beta * np_**2), beta)
    )
    collapsed = time_derivative.subs({
        beta * n**2 + m**2: common_energy,
        beta * np_**2 + mp_**2: common_energy,
    }, simultaneous=True)
    assert sp.simplify(collapsed - (n**2 - np_**2) / sp.sqrt(common_energy)) == 0
    checks += 1

    u, v = sp.symbols("u v", positive=True, integer=True)
    rational_energy = m**2 + (u / v) * n**2
    assert sp.simplify(v * rational_energy - (v * m**2 + u * n**2)) == 0; checks += 1

    witnesses = [
        (sp.Integer(1), (1, 2), (2, 1), sp.Integer(5)),
        (sp.Integer(2), (1, 4), (5, 2), sp.Integer(33)),
        (sp.Integer(4), (2, 0), (0, 1), sp.Integer(4)),
        (sp.Integer(1), (1, 8), (4, 7), sp.Integer(65)),
    ]
    for beta_value, first, second, expected in witnesses:
        first_energy = first[0] ** 2 + beta_value * first[1] ** 2
        second_energy = second[0] ** 2 + beta_value * second[1] ** 2
        assert first_energy == second_energy == expected; checks += 3

    sqrt_two = sp.sqrt(2)
    for first in range(0, 13):
        for second in range(0, 13):
            for other_first in range(0, 13):
                for other_second in range(0, 13):
                    equality = sp.expand(
                        first**2 + sqrt_two * second**2 -
                        other_first**2 - sqrt_two * other_second**2
                    ) == 0
                    expected = first**2 == other_first**2 and second**2 == other_second**2
                    assert equality == expected; checks += 1

    assert data["poisson_identity"]["reciprocal_aspect"] == \
        "W_alpha(s)=W_(1/alpha)(s/alpha)"; checks += 1
    assert data["collision_theorem"]["general_divisor_formula_claimed"] is False; checks += 1
    assert data["collision_theorem"]["irrational_uniform_gap_claimed"] is False; checks += 1
    assert data["route_a"]["route_b_invocation_allowed"] is False; checks += 1

    print(json.dumps({
        "status": "C167_SYMPY_PASS",
        "symbolic_checks": checks,
        "quadratic_field_pair_checks": 13 ** 4,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
