#!/usr/bin/env python3
"""Producer-independent checker for HCS-C266."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c266_skew_brownian_evidence.json"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 60


def F(value):
    return Fraction(value)


def M(value):
    value = F(value)
    return mp.mpf(value.numerator) / value.denominator


def ph(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def gaussian(t, z):
    return mp.exp(-z * z / (2 * t)) / mp.sqrt(2 * mp.pi * t)


def q(p, t, x, y):
    sig = 1 if y > 0 else (-1 if y < 0 else 0)
    return gaussian(t, y - x) + (2 * p - 1) * sig * gaussian(t, abs(x) + abs(y))


def close(x, y, tol=mp.mpf("2e-44")):
    return abs(mp.mpf(x) - mp.mpf(y)) <= tol * (1 + abs(mp.mpf(y)))


def check(path: Path) -> int:
    d = json.loads(path.read_text())
    assertions = 0

    def ok(condition):
        nonlocal assertions
        assert condition
        assertions += 1

    ok(d["schema"] == "hcs-c266-skew-brownian-interface-v1")
    ok(d["candidate_id"] == "HCS-C266")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788048000)
    ok(d["scope_literal"] == SCOPE)
    ok(d["evaluator"]["sha256"] == EVAL)
    ok(d["payload_sha256"] == ph(d))
    ok(d["headline"].startswith("Zero-drift symmetric-local-time skew Brownian"))
    ok(d["frozen_model"]["local_time"] == "symmetric semimartingale local time")
    ok(d["frozen_model"]["generator_interface"] == "p f'(0+)=(1-p) f'(0-)")
    ok(d["frozen_model"]["density_reference_measure"].startswith("Lebesgue"))
    ok(d["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"])
    ok(d["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(d["route_a"]["route_b_invocation_allowed"] is False)
    for flag in d["scope_flags"].values():
        ok(flag is False)

    for row in d["regression"]["kernel_rows"]:
        p, t, x, y = map(M, (row["p"], row["t"], row["x"], row["y"]))
        expected = q(p, t, x, y)
        ok(expected >= -mp.mpf("1e-50"))
        ok(close(row["density"], expected))
        ok(close(row["integrated_mass"], 1, mp.mpf("2e-42")))

    for row in d["regression"]["speed_symmetry_rows"]:
        p, x, y = map(M, (row["p"], row["x"], row["y"]))
        mx = 2 * (p if x > 0 else 1 - p)
        my = 2 * (p if y > 0 else 1 - p)
        lhs, rhs = q(p, 1, x, y) / my, q(p, 1, y, x) / mx
        ok(close(row["k_xy"], lhs))
        ok(close(row["k_yx"], rhs))
        ok(close(lhs, rhs))

    for row in d["regression"]["resolvent_rows"]:
        p, lam, x, y = map(M, (row["p"], row["lambda"], row["x"], row["y"]))
        k = mp.sqrt(2 * lam)
        sig = 1 if y > 0 else -1
        closed = (mp.exp(-k * abs(x - y)) + (2 * p - 1) * sig * mp.exp(-k * (abs(x) + abs(y)))) / k
        integral = mp.quad(lambda t: mp.exp(-lam * t) * q(p, t, x, y), [0, 1, mp.inf])
        ok(close(row["closed"], closed))
        ok(close(row["laplace_integral"], integral, mp.mpf("2e-40")))
        ok(close(closed, integral, mp.mpf("2e-40")))

    for row in d["regression"]["exit_rows"]:
        p, a, b, x = map(F, (row["p"], row["a"], row["b"], row["x"]))
        den = p * a + (1 - p) * b
        prob = p * (x + a) / den if x <= 0 else (p * a + (1 - p) * x) / den
        D = (1 - p) * b + p * a
        A = (1 - p) * (b * b - a * a) / D
        C = p * (b * b - a * a) / D
        B = a * b * (p * b + (1 - p) * a) / D
        mean = -x * x + (C if x <= 0 else A) * x + B
        ok(F(row["right_probability"]) == prob)
        ok(F(row["mean_exit_time"]) == mean)
        ok(0 <= prob <= 1)
        ok(mean >= 0)

    for row in d["regression"]["exit_transform_rows"]:
        p, a, b, lam, x = map(M, (row["p"], row["a"], row["b"], row["lambda"], row["x"]))
        k = mp.sqrt(2 * lam)
        rho = (1 - p) / p
        den = mp.cosh(k * b) * mp.sinh(k * a) + rho * mp.sinh(k * b) * mp.cosh(k * a)
        if x <= 0:
            num = mp.sinh(k * (x + a))
        else:
            num = mp.cosh(k * x) * mp.sinh(k * a) + rho * mp.sinh(k * x) * mp.cosh(k * a)
        right = num / den
        pr = 1 - p
        rho2 = (1 - pr) / pr
        den2 = mp.cosh(k * a) * mp.sinh(k * b) + rho2 * mp.sinh(k * a) * mp.cosh(k * b)
        xr = -x
        if xr <= 0:
            num2 = mp.sinh(k * (xr + b))
        else:
            num2 = mp.cosh(k * xr) * mp.sinh(k * b) + rho2 * mp.sinh(k * xr) * mp.cosh(k * b)
        left = num2 / den2
        ok(close(row["right_discounted"], right))
        ok(close(row["left_discounted"], left))
        ok(close(row["total_discounted"], right + left))
        ok(0 < right + left < 1)

    for row in d["regression"]["chapman_kolmogorov_rows"]:
        p, t, s, x, y = map(M, (row["p"], row["t"], row["s"], row["x"], row["y"]))
        convolution = mp.quad(lambda z: q(p, t, x, z) * q(p, s, z, y), [-mp.inf, 0, mp.inf])
        expected = q(p, t + s, x, y)
        ok(close(row["convolution"], convolution, mp.mpf("2e-40")))
        ok(close(row["closed"], expected))
        ok(close(convolution, expected, mp.mpf("2e-40")))

    for row in d["regression"]["occupation_rows"]:
        p = M(row["p"])
        g = lambda th: 2 * p * (1 - p) / (mp.pi * (p * p * mp.cos(th) ** 2 + (1 - p) ** 2 * mp.sin(th) ** 2))
        norm = mp.quad(g, [0, mp.pi / 2])
        mean = mp.quad(lambda th: mp.sin(th) ** 2 * g(th), [0, mp.pi / 2])
        ok(close(row["normalization"], norm))
        ok(close(row["mean"], mean))
        ok(close(norm, 1))
        ok(close(mean, p))

    counts = d["regression"]["counts"]
    for key, value in counts.items():
        ok(value == len(d["regression"][key]))
    ok(len(d["nonclaims"]) == 4)
    return assertions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    count = check(args.path)
    print(f"C266 independent checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
