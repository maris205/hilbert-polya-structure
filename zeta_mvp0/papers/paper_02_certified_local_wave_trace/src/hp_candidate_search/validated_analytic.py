"""Arb-backed implementation smoke for the A4.11 analytic reductions.

This module validates special-function conventions, the exact shell
parameterization, normal coordinates, and the two period-floor bounds.  It is
not a validated ODE integrator and cannot certify whole-shell uniqueness.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from math import factorial
from pathlib import Path
from typing import Iterable

from flint import arb, ctx, fmpq


A_NUM = 51
A_DEN = 50
EPS_CAP_NUM = 101
EPS_CAP_DEN = 1000


def qball(numerator: int, denominator: int = 1) -> arb:
    """Return an Arb enclosure of an exact rational."""

    return arb(fmpq(numerator, denominator))


def interval_ball(
    lower_num: int,
    lower_den: int,
    upper_num: int,
    upper_den: int,
) -> arb:
    """Return one ball enclosing a rational closed interval."""

    lower = fmpq(lower_num, lower_den)
    upper = fmpq(upper_num, upper_den)
    return arb((lower + upper) / 2, (upper - lower) / 2)


def _symmetric_error(radius: arb) -> arb:
    return arb(0, abs(radius).upper())


def exprel_series(value: arb, *, order: int = 18) -> arb:
    """Enclose ``(exp(value)-1)/value``, including balls containing zero."""

    total = arb(1)
    term = arb(1)
    for degree in range(1, order + 1):
        term = term * value / (degree + 1)
        total += term
    radius = abs(value).upper()
    remainder = (
        radius ** (order + 1)
        * radius.exp()
        / factorial(order + 2)
    )
    return total + _symmetric_error(remainder)


def log1prel_series(value: arb, *, order: int = 18) -> arb:
    """Enclose ``log(1+value)/value``, including balls containing zero."""

    radius = abs(value).upper()
    if not radius < arb(1):
        raise ValueError("log1prel series requires |value| < 1")
    total = arb(1)
    power = arb(1)
    for degree in range(1, order + 1):
        power *= value
        coefficient = -1 if degree % 2 else 1
        total += coefficient * power / (degree + 1)
    remainder = (
        radius ** (order + 1)
        / ((order + 2) * (1 - radius))
    )
    return total + _symmetric_error(remainder)


@dataclass(frozen=True)
class ExactModel:
    a: arb
    c: arb
    epsilon_cap: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    e_slow: tuple[arb, arb]
    e_fast: tuple[arb, arb]


def exact_model() -> ExactModel:
    """Construct exact algebraic model data with outward-rounded balls."""

    a = qball(A_NUM, A_DEN)
    epsilon_cap = qball(EPS_CAP_NUM, EPS_CAP_DEN)
    pi_ball = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_norm = (slow_raw[0] ** 2 + slow_raw[1] ** 2).sqrt()
    fast_norm = (fast_raw[0] ** 2 + fast_raw[1] ** 2).sqrt()
    e_slow = (slow_raw[0] / slow_norm, slow_raw[1] / slow_norm)
    e_fast = (fast_raw[0] / fast_norm, fast_raw[1] / fast_norm)
    return ExactModel(
        a=a,
        c=c,
        epsilon_cap=epsilon_cap,
        pi=pi_ball,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_ball * lambda_slow.sqrt(),
        omega_fast=2 * pi_ball * lambda_fast.sqrt(),
        e_slow=e_slow,
        e_fast=e_fast,
    )


def shell_point(
    model: ExactModel,
    epsilon: arb,
    theta: arb,
    alpha: arb,
    beta: arb,
) -> tuple[tuple[arb, arb], tuple[arb, arb], arb]:
    """Construct one rigorously enclosed point on the normalized shell."""

    cosine = theta.cos()
    sine = theta.sin()
    x = epsilon * epsilon * cosine * cosine / (2 * model.pi)
    radius = (
        cosine
        / (qball(2).sqrt() * model.pi)
        * log1prel_series(x).sqrt()
    )
    u = (radius * alpha.cos(), radius * alpha.sin())
    momentum = (
        qball(2).sqrt() * sine * beta.cos(),
        qball(2).sqrt() * sine * beta.sin(),
    )
    q1 = u[1]
    q2 = -model.c * u[1] - model.a * epsilon * u[1] ** 2 - u[0]
    w = (
        -model.c * q1 - q2 - model.a * epsilon * q1**2,
        q1,
    )
    w2 = w[0] ** 2 + w[1] ** 2
    argument = model.pi * epsilon * epsilon * w2
    energy = (
        (momentum[0] ** 2 + momentum[1] ** 2) / 2
        + 2 * model.pi**2 * w2 * exprel_series(argument)
    )
    return (q1, q2), momentum, energy


def analytic_bounds(model: ExactModel) -> dict[str, arb]:
    """Return the two A4.11 period bounds and shell outer bounds."""

    sqrt_two = qball(2).sqrt()
    normalized_radius = 1 / (sqrt_two * model.pi)
    q1_bound = normalized_radius
    q2_bound = (
        (1 + model.c) * normalized_radius
        + model.a * model.epsilon_cap * normalized_radius**2
    )
    p_component_bound = sqrt_two

    physical_radius = model.epsilon_cap / (sqrt_two * model.pi)
    y_bound = (
        (1 + model.c) * physical_radius
        + model.a * physical_radius**2
    )
    f_bound = (
        (1 + 2 * model.c) * physical_radius
        + 2 * model.a * physical_radius**2
    )
    u2_bound = f_bound**2 + physical_radius**2
    d_bound = model.c + 2 * model.a * physical_radius
    trace_bound = d_bound**2 + 2
    jacobian_norm_sq = (
        trace_bound + (trace_bound**2 - 4).sqrt()
    ) / 2
    potential_bound = 2 * model.pi * (model.pi * u2_bound).exp()
    warped_hessian_bound = potential_bound * (
        2 * model.pi * (jacobian_norm_sq + 2 * model.a * f_bound)
        + 4 * model.pi**2 * jacobian_norm_sq * u2_bound
    )
    warped_period_lower = 2 * model.pi / warped_hessian_bound.sqrt()

    delta_cap = model.epsilon_cap**2
    radial_hessian_bound = (
        (2 * model.pi + delta_cap)
        * (2 * model.pi + 2 * delta_cap)
    )
    radial_period_lower = 2 * model.pi / radial_hessian_bound.sqrt()
    return {
        "normalized_q1_bound": q1_bound,
        "normalized_q2_bound": q2_bound,
        "normalized_p_component_bound": p_component_bound,
        "physical_q1_bound": physical_radius,
        "physical_q2_bound": y_bound,
        "warped_u1_bound": f_bound,
        "warped_u_norm_sq_bound": u2_bound,
        "jacobian_norm_sq_bound": jacobian_norm_sq,
        "warped_potential_bound": potential_bound,
        "warped_hessian_bound": warped_hessian_bound,
        "warped_period_lower": warped_period_lower,
        "radial_hessian_bound": radial_hessian_bound,
        "radial_period_lower": radial_period_lower,
    }


def arb_record(value: arb) -> dict[str, str]:
    return {
        "ball": str(value),
        "lower": str(value.lower()),
        "upper": str(value.upper()),
    }


def hash_files(paths: Iterable[Path | str]) -> dict[str, str]:
    records: dict[str, str] = {}
    for raw_path in paths:
        path = Path(raw_path)
        records[str(path)] = sha256(path.read_bytes()).hexdigest()
    return records


def run_analytic_smoke(*, precision: int) -> dict[str, object]:
    """Run one non-claiming analytic/shell implementation smoke."""

    ctx.prec = precision
    model = exact_model()
    bounds = analytic_bounds(model)
    gates: dict[str, bool] = {
        "normal_vectors_orthogonal": (
            model.e_slow[0] * model.e_fast[0]
            + model.e_slow[1] * model.e_fast[1]
        ).contains(0),
        "slow_vector_unit": (
            model.e_slow[0] ** 2 + model.e_slow[1] ** 2
        ).contains(1),
        "fast_vector_unit": (
            model.e_fast[0] ** 2 + model.e_fast[1] ** 2
        ).contains(1),
        "q1_outer_box": bounds["normalized_q1_bound"] < qball(226, 1000),
        "q2_outer_box": bounds["normalized_q2_bound"] < qball(421, 1000),
        "p_outer_box": bounds["normalized_p_component_bound"] < qball(1415, 1000),
        "warped_hessian_lt_103": bounds["warped_hessian_bound"] < qball(103),
        "warped_period_gt_point60": bounds["warped_period_lower"] > qball(60, 100),
        "radial_period_gt_point99": bounds["radial_period_lower"] > qball(99, 100),
    }

    zero_interval = interval_ball(0, 1, 1, 1000)
    exprel_zero = exprel_series(zero_interval)
    log1prel_zero = log1prel_series(zero_interval)
    gates["exprel_zero_safe"] = exprel_zero.contains(1)
    gates["log1prel_zero_safe"] = log1prel_zero.contains(1)

    shell_checks: list[dict[str, object]] = []
    epsilon_values = [(0, 1), (1, 20), (1, 10), (101, 1000)]
    theta_multipliers = [(0, 1), (1, 8), (1, 4), (3, 8), (1, 2)]
    angle_multipliers = [(0, 1), (1, 3), (2, 3)]
    for eps_num, eps_den in epsilon_values:
        epsilon = qball(eps_num, eps_den)
        for theta_num, theta_den in theta_multipliers:
            theta = model.pi * qball(theta_num, theta_den)
            for angle_num, angle_den in angle_multipliers:
                alpha = 2 * model.pi * qball(angle_num, angle_den)
                beta = 2 * model.pi * qball(
                    (angle_num + 1) % angle_den,
                    angle_den,
                )
                _, _, energy = shell_point(
                    model,
                    epsilon,
                    theta,
                    alpha,
                    beta,
                )
                contains_one = energy.contains(1)
                shell_checks.append(
                    {
                        "epsilon": f"{eps_num}/{eps_den}",
                        "theta_over_pi": f"{theta_num}/{theta_den}",
                        "alpha_turn": f"{angle_num}/{angle_den}",
                        "energy": arb_record(energy),
                        "contains_one": contains_one,
                    }
                )
    gates["sampled_shell_identity"] = all(
        bool(item["contains_one"]) for item in shell_checks
    )
    return {
        "precision_bits": precision,
        "status": "PASS_IMPLEMENTATION_SMOKE" if all(gates.values()) else "FAIL",
        "gates": gates,
        "model": {
            "a": arb_record(model.a),
            "c": arb_record(model.c),
            "epsilon_cap": arb_record(model.epsilon_cap),
            "lambda_slow": arb_record(model.lambda_slow),
            "lambda_fast": arb_record(model.lambda_fast),
            "omega_slow": arb_record(model.omega_slow),
            "omega_fast": arb_record(model.omega_fast),
        },
        "special_functions": {
            "input_interval": arb_record(zero_interval),
            "exprel": arb_record(exprel_zero),
            "log1prel": arb_record(log1prel_zero),
        },
        "analytic_bounds": {
            name: arb_record(value) for name, value in bounds.items()
        },
        "shell_checks": shell_checks,
    }
