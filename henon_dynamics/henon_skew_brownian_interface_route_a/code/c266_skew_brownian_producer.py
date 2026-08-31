#!/usr/bin/env python3
"""Deterministic evidence producer for HCS-C266 skew Brownian motion."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import mpmath as mp

SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c266_skew_brownian_evidence.json"
mp.mp.dps = 70


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def dec(x) -> str:
    return mp.nstr(x, 55)


def rat(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def phi(t, z):
    return mp.exp(-(z * z) / (2 * t)) / mp.sqrt(2 * mp.pi * t)


def kernel(p, t, x, y):
    sign = mp.mpf(1) if y > 0 else (mp.mpf(-1) if y < 0 else mp.mpf(0))
    return phi(t, y - x) + (2 * p - 1) * sign * phi(t, abs(x) + abs(y))


def resolvent(p, lam, x, y):
    k = mp.sqrt(2 * lam)
    sign = mp.mpf(1) if y > 0 else (mp.mpf(-1) if y < 0 else mp.mpf(0))
    return (mp.exp(-k * abs(x - y)) + (2 * p - 1) * sign * mp.exp(-k * (abs(x) + abs(y)))) / k


def right_exit_transform(p, lam, x, a, b):
    k = mp.sqrt(2 * lam)
    rho = (1 - p) / p
    den = mp.cosh(k * b) * mp.sinh(k * a) + rho * mp.sinh(k * b) * mp.cosh(k * a)
    if x <= 0:
        num = mp.sinh(k * (x + a))
    else:
        num = mp.cosh(k * x) * mp.sinh(k * a) + rho * mp.sinh(k * x) * mp.cosh(k * a)
    return num / den


def right_exit_probability(p: Fraction, x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    den = p * a + (1 - p) * b
    if x <= 0:
        return p * (x + a) / den
    return (p * a + (1 - p) * x) / den


def mean_exit(p: Fraction, x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    den = (1 - p) * b + p * a
    slope_plus = (1 - p) * (b * b - a * a) / den
    slope_minus = p * (b * b - a * a) / den
    intercept = a * b * (p * b + (1 - p) * a) / den
    return -x * x + (slope_minus if x <= 0 else slope_plus) * x + intercept


def build() -> dict:
    kernel_rows = []
    for p_q in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        for t_q in (Fraction(1, 3), Fraction(1), Fraction(2)):
            t = mp.mpf(t_q.numerator) / t_q.denominator
            for x_q in (Fraction(-1), Fraction(0), Fraction(2, 3)):
                x = mp.mpf(x_q.numerator) / x_q.denominator
                mass = mp.quad(lambda yy: kernel(p, t, x, yy), [-mp.inf, 0, mp.inf])
                for y_q in (Fraction(-3, 4), Fraction(1, 5), Fraction(4, 3)):
                    y = mp.mpf(y_q.numerator) / y_q.denominator
                    kernel_rows.append({
                        "p": rat(p_q), "t": rat(t_q), "x": rat(x_q), "y": rat(y_q),
                        "density": dec(kernel(p, t, x, y)), "integrated_mass": dec(mass),
                    })

    speed_rows = []
    for p_q in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        for x_q, y_q in ((Fraction(-2, 3), Fraction(3, 5)), (Fraction(-1), Fraction(-1, 4)), (Fraction(1, 3), Fraction(5, 4))):
            x, y = mp.mpf(x_q.numerator) / x_q.denominator, mp.mpf(y_q.numerator) / y_q.denominator
            mx = 2 * (p if x > 0 else 1 - p)
            my = 2 * (p if y > 0 else 1 - p)
            speed_rows.append({
                "p": rat(p_q), "x": rat(x_q), "y": rat(y_q),
                "k_xy": dec(kernel(p, 1, x, y) / my),
                "k_yx": dec(kernel(p, 1, y, x) / mx),
            })

    resolvent_rows = []
    for p_q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        for lam_q in (Fraction(1, 2), Fraction(2)):
            lam = mp.mpf(lam_q.numerator) / lam_q.denominator
            for x_q, y_q in ((Fraction(-1), Fraction(2, 3)), (Fraction(1, 4), Fraction(5, 4)), (Fraction(-3, 2), Fraction(-1, 5))):
                x, y = mp.mpf(x_q.numerator) / x_q.denominator, mp.mpf(y_q.numerator) / y_q.denominator
                integ = mp.quad(lambda tt: mp.exp(-lam * tt) * kernel(p, tt, x, y), [0, 1, mp.inf])
                resolvent_rows.append({
                    "p": rat(p_q), "lambda": rat(lam_q), "x": rat(x_q), "y": rat(y_q),
                    "closed": dec(resolvent(p, lam, x, y)), "laplace_integral": dec(integ),
                })

    exit_rows = []
    for p_q in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        for a_q, b_q in ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(3))):
            for x_q in (-a_q, -a_q / 2, Fraction(0), b_q / 3, b_q):
                exit_rows.append({
                    "p": rat(p_q), "a": rat(a_q), "b": rat(b_q), "x": rat(x_q),
                    "right_probability": rat(right_exit_probability(p_q, x_q, a_q, b_q)),
                    "mean_exit_time": rat(mean_exit(p_q, x_q, a_q, b_q)),
                })

    exit_transform_rows = []
    for p_q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        for a_q, b_q in ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(3))):
            a, b = mp.mpf(a_q.numerator) / a_q.denominator, mp.mpf(b_q.numerator) / b_q.denominator
            for lam_q in (Fraction(1, 3), Fraction(1), Fraction(3)):
                lam = mp.mpf(lam_q.numerator) / lam_q.denominator
                for x_q in (-a_q / 2, Fraction(0), b_q / 2):
                    x = mp.mpf(x_q.numerator) / x_q.denominator
                    right = right_exit_transform(p, lam, x, a, b)
                    left = right_exit_transform(1 - p, lam, -x, b, a)
                    exit_transform_rows.append({
                        "p": rat(p_q), "a": rat(a_q), "b": rat(b_q), "lambda": rat(lam_q), "x": rat(x_q),
                        "right_discounted": dec(right), "left_discounted": dec(left), "total_discounted": dec(right + left),
                    })

    ck_rows = []
    for p_q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        for t_q, s_q, x_q, y_q in (
            (Fraction(1, 3), Fraction(2, 5), Fraction(-1), Fraction(2, 3)),
            (Fraction(1), Fraction(1, 2), Fraction(1, 4), Fraction(-3, 5)),
        ):
            t, s = mp.mpf(t_q.numerator) / t_q.denominator, mp.mpf(s_q.numerator) / s_q.denominator
            x, y = mp.mpf(x_q.numerator) / x_q.denominator, mp.mpf(y_q.numerator) / y_q.denominator
            convolution = mp.quad(lambda z: kernel(p, t, x, z) * kernel(p, s, z, y), [-mp.inf, 0, mp.inf])
            ck_rows.append({
                "p": rat(p_q), "t": rat(t_q), "s": rat(s_q), "x": rat(x_q), "y": rat(y_q),
                "convolution": dec(convolution), "closed": dec(kernel(p, t + s, x, y)),
            })

    occupation_rows = []
    for p_q in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
        p = mp.mpf(p_q.numerator) / p_q.denominator
        theta_density = lambda th: 2 * p * (1 - p) / (mp.pi * (p * p * mp.cos(th) ** 2 + (1 - p) ** 2 * mp.sin(th) ** 2))
        norm = mp.quad(theta_density, [0, mp.pi / 2])
        mean = mp.quad(lambda th: mp.sin(th) ** 2 * theta_density(th), [0, mp.pi / 2])
        occupation_rows.append({"p": rat(p_q), "normalization": dec(norm), "mean": dec(mean)})

    data = {
        "schema": "hcs-c266-skew-brownian-interface-v1",
        "candidate_id": "HCS-C266",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Zero-drift symmetric-local-time skew Brownian motion closes its kernel, speed-symmetric semigroup, resolvent, two-sided exits, and occupation law.",
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVAL},
        "frozen_model": {
            "equation": "X_t=x+B_t+(2p-1)L_t^0(X)",
            "local_time": "symmetric semimartingale local time",
            "parameter_range": "0<=p<=1",
            "generator_interface": "p f'(0+)=(1-p) f'(0-)",
            "density_reference_measure": "Lebesgue unless explicitly divided by speed density",
            "fourier_convention": "resolvent is the time-Laplace transform; no Fourier normalization is used",
        },
        "theorem_receipt": {
            "transition_density": "phi_t(y-x)+(2p-1)sgn(y)phi_t(|x|+|y|)",
            "speed_density": "2p on x>0 and 2(1-p) on x<0",
            "resolvent": "[exp(-k|x-y|)+(2p-1)sgn(y)exp(-k(|x|+|y|))]/k, k=sqrt(2lambda)",
            "exit_policy": "tau is first exit from (-a,b); discounted side transforms retain boundary labels",
            "occupation_policy": "start at zero; positive occupation fraction; endpoint p values are atoms",
        },
        "regression": {
            "kernel_rows": kernel_rows, "speed_symmetry_rows": speed_rows, "resolvent_rows": resolvent_rows,
            "exit_rows": exit_rows, "exit_transform_rows": exit_transform_rows,
            "chapman_kolmogorov_rows": ck_rows, "occupation_rows": occupation_rows,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "target_arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "target_divisor_or_counting_law": False,
            "target_functional_equation": False, "hilbert_polya_operator": False,
            "target_zero_match": False, "route_b_claim": False,
        },
        "nonclaims": [
            "Finite regression rows do not prove the all-parameter theorem.",
            "The speed-symmetric Markov generator is not a Hilbert--Polya operator.",
            "No drifted or two-diffusivity interface model is claimed.",
            "Workspace ownership is not a literature-priority claim.",
        ],
    }
    data["regression"]["counts"] = {
        key: len(value) for key, value in data["regression"].items() if key.endswith("_rows")
    }
    data["payload_sha256"] = ph(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C266_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "counts": data["regression"]["counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()
