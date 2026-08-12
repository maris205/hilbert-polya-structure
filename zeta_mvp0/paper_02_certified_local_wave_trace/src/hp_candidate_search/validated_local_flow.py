"""Validated local-flow primitives for the R401-VAL programme.

The implementation uses Arb ball arithmetic and an interval Taylor method.
It is deliberately small and certificate-oriented: a Taylor step first
proves a Picard a-priori enclosure, evaluates all coefficients through
directed rounding, and bounds the last coefficient on the full a-priori
box.  The current production milestone is a *single-parameter point*
certificate at ``epsilon = 0.1``.  It is not a uniform parameter-slab or a
whole-shell proof.

The normalized Hamiltonian is

    K = |P|^2/2 + 2*pi^2*|W_epsilon(Q)|^2
        * exprel(pi*epsilon^2*|W_epsilon(Q)|^2),

where ``W_epsilon(Q) = A Q + epsilon*(-a*Q_1^2, 0)``.  Physical time is
unchanged.  Integration is performed on ``s in [0,1]`` with
``dZ/ds = T X_K(Z)`` so that the unknown return time is an interval
parameter rather than a variable endpoint.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Sequence

from flint import arb, arb_mat, arb_series, ctx, fmpq

from .validated_analytic import exprel_series, qball


def decimal_ball(value: str | int | Decimal) -> arb:
    """Return an exact rational Arb value from a decimal representation."""

    item = Decimal(str(value))
    sign, digits, exponent = item.as_tuple()
    numerator = int("".join(str(digit) for digit in digits) or "0")
    if sign:
        numerator = -numerator
    if exponent >= 0:
        numerator *= 10**exponent
        denominator = 1
    else:
        denominator = 10 ** (-exponent)
    return arb(fmpq(numerator, denominator))


def exact_midpoint(value: arb, *, digits: int = 70) -> arb:
    """Round an Arb midpoint to a reproducible exact decimal rational."""

    return decimal_ball(value.mid().str(digits, 0))


def symmetric_ball(center: arb, radius: arb) -> arb:
    """Return a ball containing ``center + [-radius, radius]``."""

    return center.mid() + arb(0, center.rad() + abs(radius).upper())


def strict_subset(inner: arb, outer: arb) -> bool:
    """Check strict real-interval inclusion using outward endpoints."""

    return bool(inner.lower() > outer.lower() and inner.upper() < outer.upper())


@dataclass(frozen=True)
class LocalValidatedModel:
    a: arb
    c: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    e_slow: tuple[arb, arb]
    e_fast: tuple[arb, arb]


def local_model() -> LocalValidatedModel:
    """Reconstruct the protocol's exact algebraic normal coordinates."""

    a = qball(51, 50)
    pi_ball = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_norm = (slow_raw[0] ** 2 + slow_raw[1] ** 2).sqrt()
    fast_norm = (fast_raw[0] ** 2 + fast_raw[1] ** 2).sqrt()
    return LocalValidatedModel(
        a=a,
        c=c,
        pi=pi_ball,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_ball * lambda_slow.sqrt(),
        omega_fast=2 * pi_ball * lambda_fast.sqrt(),
        e_slow=(slow_raw[0] / slow_norm, slow_raw[1] / slow_norm),
        e_fast=(fast_raw[0] / fast_norm, fast_raw[1] / fast_norm),
    )


def normal_to_physical(
    model: LocalValidatedModel,
    slow: arb,
    fast: arb,
) -> tuple[arb, arb]:
    return (
        model.e_slow[0] * slow + model.e_fast[0] * fast,
        model.e_slow[1] * slow + model.e_fast[1] * fast,
    )


def physical_to_normal(
    model: LocalValidatedModel,
    first: arb,
    second: arb,
) -> tuple[arb, arb]:
    return (
        model.e_slow[0] * first + model.e_slow[1] * second,
        model.e_fast[0] * first + model.e_fast[1] * second,
    )


def _force_and_hessian(
    model: LocalValidatedModel,
    epsilon: arb,
    q1: arb | arb_series,
    q2: arb | arb_series,
) -> tuple[
    tuple[arb | arb_series, arb | arb_series],
    tuple[
        tuple[arb | arb_series, arb | arb_series],
        tuple[arb | arb_series, arb | arb_series],
    ],
]:
    """Return ``-grad K`` and ``Hess K`` in physical Q coordinates."""

    a, c, pi_ball = model.a, model.c, model.pi
    w1 = -c * q1 - q2 - a * epsilon * q1 * q1
    w2 = q1
    j11 = -c - 2 * a * epsilon * q1
    squared_radius = w1 * w1 + w2 * w2
    exponential = (pi_ball * epsilon * epsilon * squared_radius).exp()
    v1 = j11 * w1 + w2
    v2 = -w1
    factor = 4 * pi_ball * pi_ball * exponential

    b11 = j11 * j11 + 1 - 2 * a * epsilon * w1
    b12 = -j11
    b22 = 1
    rank_one_factor = 2 * pi_ball * epsilon * epsilon
    h11 = factor * (b11 + rank_one_factor * v1 * v1)
    h12 = factor * (b12 + rank_one_factor * v1 * v2)
    h22 = factor * (b22 + rank_one_factor * v2 * v2)
    return (-factor * v1, -factor * v2), ((h11, h12), (h12, h22))


def scaled_augmented_rhs(
    model: LocalValidatedModel,
    values: Sequence[arb | arb_series],
    *,
    epsilon: arb,
    period: arb,
) -> list[arb | arb_series]:
    """RHS for state plus optional 4-by-4 variational matrix."""

    q1, q2, p1, p2 = values[:4]
    force, hessian = _force_and_hessian(model, epsilon, q1, q2)
    output: list[arb | arb_series] = [
        period * p1,
        period * p2,
        period * force[0],
        period * force[1],
    ]
    if len(values) == 4:
        return output
    if len(values) != 20:
        raise ValueError("augmented state must have dimension 4 or 20")

    zero = q1 * 0
    one = zero + 1
    flow_jacobian = (
        (zero, zero, one, zero),
        (zero, zero, zero, one),
        (-hessian[0][0], -hessian[0][1], zero, zero),
        (-hessian[1][0], -hessian[1][1], zero, zero),
    )
    matrix = [values[4 + 4 * row : 8 + 4 * row] for row in range(4)]
    for row in range(4):
        for column in range(4):
            output.append(
                period
                * sum(
                    flow_jacobian[row][index] * matrix[index][column]
                    for index in range(4)
                )
            )
    return output


def _taylor_coefficients(
    model: LocalValidatedModel,
    initial: Sequence[arb],
    *,
    epsilon: arb,
    period: arb,
    degree: int,
) -> list[list[arb]]:
    """Enclose normalized time derivatives through ``degree``."""

    coefficients: list[list[arb]] = [[value] for value in initial]
    for index in range(degree):
        series = [
            arb_series(items, prec=degree + 1) for items in coefficients
        ]
        rhs = scaled_augmented_rhs(
            model,
            series,
            epsilon=epsilon,
            period=period,
        )
        for component in range(len(initial)):
            coefficients[component].append(rhs[component][index] / (index + 1))
    return coefficients


@dataclass(frozen=True)
class TaylorStepDiagnostics:
    picard_iterations: int
    max_picard_ratio: float
    max_output_radius: float


def _apriori_enclosure(
    model: LocalValidatedModel,
    initial: Sequence[arb],
    *,
    epsilon: arb,
    period: arb,
    step: arb,
) -> tuple[list[arb], int, float]:
    """Prove a componentwise Picard enclosure for one Taylor step."""

    # Scale the initial Picard radii with the dyadic step.  The constants are
    # outward guard bounds for the normalized energy-one shell.  Starting
    # from fixed radii would remain rigorous, but would artificially spoil
    # the continuous-time slow-tube diagnostic when the step is refined.
    radii = [decimal_ball("1.6") * step, decimal_ball("1.6") * step]
    radii.extend((decimal_ball("16") * step, decimal_ball("16") * step))
    if len(initial) == 20:
        radii.extend(
            decimal_ball("102") * step * (1 + abs(value).upper())
            for value in initial[4:]
        )
    elif len(initial) != 4:
        raise ValueError("state must have dimension 4 or 20")

    largest_ratio = 0.0
    for iteration in range(40):
        enclosure = [
            symmetric_ball(value, radius)
            for value, radius in zip(initial, radii, strict=True)
        ]
        rhs = scaled_augmented_rhs(
            model,
            enclosure,
            epsilon=epsilon,
            period=period,
        )
        required = [
            decimal_ball("1.02") * step * abs(value).upper()
            for value in rhs
        ]
        ratios = [
            float((need / radius).upper()) if not radius.is_zero() else float("inf")
            for need, radius in zip(required, radii, strict=True)
        ]
        largest_ratio = max(ratios)
        if all(need < radius for need, radius in zip(required, radii, strict=True)):
            return enclosure, iteration + 1, largest_ratio
        radii = [
            max(radius, decimal_ball("1.05") * need)
            for radius, need in zip(radii, required, strict=True)
        ]
    raise RuntimeError("failed to close the interval Picard enclosure")


def validated_taylor_step(
    model: LocalValidatedModel,
    initial: Sequence[arb],
    *,
    epsilon: arb,
    period: arb,
    step: arb,
    order: int,
) -> tuple[list[arb], list[arb], TaylorStepDiagnostics]:
    """Advance one rigorously enclosed interval Taylor step.

    The first ``order`` coefficients are evaluated on the incoming box.  The
    final normalized derivative is evaluated on the proven Picard enclosure,
    giving a Lagrange-form remainder valid for every trajectory in the box.
    """

    if order < 6:
        raise ValueError("Taylor order must be at least six")
    apriori, iterations, ratio = _apriori_enclosure(
        model,
        initial,
        epsilon=epsilon,
        period=period,
        step=step,
    )
    principal = _taylor_coefficients(
        model,
        initial,
        epsilon=epsilon,
        period=period,
        degree=order - 1,
    )
    remainder = _taylor_coefficients(
        model,
        apriori,
        epsilon=epsilon,
        period=period,
        degree=order,
    )
    result: list[arb] = []
    for component in range(len(initial)):
        value = arb(0)
        power = arb(1)
        for degree in range(order):
            value += principal[component][degree] * power
            power *= step
        value += remainder[component][order] * power
        result.append(value)
    return result, apriori, TaylorStepDiagnostics(
        picard_iterations=iterations,
        max_picard_ratio=ratio,
        max_output_radius=max(float(value.rad()) for value in result),
    )


@dataclass(frozen=True)
class FlowDiagnostics:
    steps: int
    order: int
    max_picard_iterations: int
    max_picard_ratio: float
    max_output_radius: float
    max_slow_radius_upper: float
    q1_min: float
    q1_max: float
    q2_min: float
    q2_max: float
    p1_min: float
    p1_max: float
    p2_min: float
    p2_max: float


def _slow_radius_upper(
    model: LocalValidatedModel,
    enclosure: Sequence[arb],
) -> float:
    q_slow, _ = physical_to_normal(model, enclosure[0], enclosure[1])
    p_slow, _ = physical_to_normal(model, enclosure[2], enclosure[3])
    # Arb balls do not preserve the dependency in ``x*x`` when the ball
    # crosses zero, so the raw product may have a tiny negative lower bound.
    # Intersect with the mathematically known nonnegative half-line before
    # taking the square root.
    squared = (
        (model.omega_slow * q_slow) ** 2 + p_slow**2
    ).nonnegative_part()
    return float(squared.sqrt().upper())


def integrate_validated_flow(
    model: LocalValidatedModel,
    initial: Sequence[arb],
    *,
    epsilon: arb,
    period: arb,
    steps: int = 512,
    order: int = 16,
) -> tuple[list[arb], FlowDiagnostics]:
    """Integrate state or state+variational matrix over scaled time [0,1]."""

    if steps < 32:
        raise ValueError("validated integration requires at least 32 steps")
    previous_cap = ctx.cap
    ctx.cap = max(ctx.cap, order + 1)
    try:
        value = list(initial)
        step = qball(1, steps)
        max_iterations = 0
        max_ratio = 0.0
        max_radius = 0.0
        max_slow = 0.0
        lows = [float("inf")] * 4
        highs = [float("-inf")] * 4
        for _ in range(steps):
            value, apriori, diagnostics = validated_taylor_step(
                model,
                value,
                epsilon=epsilon,
                period=period,
                step=step,
                order=order,
            )
            max_iterations = max(max_iterations, diagnostics.picard_iterations)
            max_ratio = max(max_ratio, diagnostics.max_picard_ratio)
            max_radius = max(max_radius, diagnostics.max_output_radius)
            max_slow = max(max_slow, _slow_radius_upper(model, apriori))
            for component in range(4):
                lows[component] = min(
                    lows[component], float(apriori[component].lower())
                )
                highs[component] = max(
                    highs[component], float(apriori[component].upper())
                )
        return value, FlowDiagnostics(
            steps=steps,
            order=order,
            max_picard_iterations=max_iterations,
            max_picard_ratio=max_ratio,
            max_output_radius=max_radius,
            max_slow_radius_upper=max_slow,
            q1_min=lows[0],
            q1_max=highs[0],
            q2_min=lows[1],
            q2_max=highs[1],
            p1_min=lows[2],
            p1_max=highs[2],
            p2_min=lows[3],
            p2_max=highs[3],
        )
    finally:
        ctx.cap = previous_cap


def normalized_energy(
    model: LocalValidatedModel,
    epsilon: arb,
    state: Sequence[arb],
) -> arb:
    q1, q2, p1, p2 = state
    w1 = -model.c * q1 - q2 - model.a * epsilon * q1 * q1
    w2 = q1
    squared_radius = w1 * w1 + w2 * w2
    argument = model.pi * epsilon * epsilon * squared_radius
    potential = (
        2
        * model.pi
        * model.pi
        * squared_radius
        * exprel_series(argument, order=24)
    )
    return (p1 * p1 + p2 * p2) / 2 + potential


def local_initial_state(
    model: LocalValidatedModel,
    root: Sequence[arb],
) -> list[arb]:
    """Decode ``(Q_-, Q_+, P_-, T)`` with ``P_+=0``."""

    if len(root) != 4:
        raise ValueError("local root must have four entries")
    q1, q2 = normal_to_physical(model, root[0], root[1])
    p1, p2 = normal_to_physical(model, root[2], arb(0))
    return [q1, q2, p1, p2]


def identity_augmented_state(state: Sequence[arb]) -> list[arb]:
    return list(state) + [
        arb(1 if row == column else 0)
        for row in range(4)
        for column in range(4)
    ]


def residual_and_jacobian(
    model: LocalValidatedModel,
    root: Sequence[arb],
    *,
    epsilon: arb,
    steps: int = 512,
    order: int = 16,
) -> tuple[list[arb], arb_mat, list[arb], FlowDiagnostics]:
    """Enclose the protocol's four local equations and their Jacobian."""

    state0 = local_initial_state(model, root)
    augmented, diagnostics = integrate_validated_flow(
        model,
        identity_augmented_state(state0),
        epsilon=epsilon,
        period=root[3],
        steps=steps,
        order=order,
    )
    terminal = augmented[:4]
    monodromy = [augmented[4 + 4 * row : 8 + 4 * row] for row in range(4)]
    q_initial = physical_to_normal(model, state0[0], state0[1])
    p_initial = physical_to_normal(model, state0[2], state0[3])
    q_terminal = physical_to_normal(model, terminal[0], terminal[1])
    p_terminal = physical_to_normal(model, terminal[2], terminal[3])
    residual = [
        normalized_energy(model, epsilon, state0) - 1,
        q_terminal[0] - q_initial[0],
        p_terminal[0] - p_initial[0],
        p_terminal[1],
    ]

    initial_force, _ = _force_and_hessian(
        model, epsilon, state0[0], state0[1]
    )
    terminal_force, _ = _force_and_hessian(
        model, epsilon, terminal[0], terminal[1]
    )
    terminal_vector = [terminal[2], terminal[3], terminal_force[0], terminal_force[1]]

    # Columns mapping local variables (Q_-, Q_+, P_-) into physical state.
    embedding = (
        (model.e_slow[0], model.e_fast[0], arb(0)),
        (model.e_slow[1], model.e_fast[1], arb(0)),
        (arb(0), arb(0), model.e_slow[0]),
        (arb(0), arb(0), model.e_slow[1]),
    )
    propagated: list[list[arb]] = [[arb(0)] * 3 for _ in range(4)]
    for row in range(4):
        for column in range(3):
            propagated[row][column] = sum(
                monodromy[row][index] * embedding[index][column]
                for index in range(4)
            )

    output_rows = (
        (model.e_slow[0], model.e_slow[1], arb(0), arb(0)),
        (arb(0), arb(0), model.e_slow[0], model.e_slow[1]),
        (arb(0), arb(0), model.e_fast[0], model.e_fast[1]),
    )
    closure_derivatives: list[list[arb]] = []
    for output_index, projection in enumerate(output_rows):
        row = [
            sum(projection[index] * propagated[index][column] for index in range(4))
            for column in range(3)
        ]
        if output_index == 0:
            row[0] -= 1
        elif output_index == 1:
            row[2] -= 1
        row.append(
            sum(projection[index] * terminal_vector[index] for index in range(4))
        )
        closure_derivatives.append(row)

    gradient_force = [-initial_force[0], -initial_force[1]]
    energy_row = [
        gradient_force[0] * model.e_slow[0]
        + gradient_force[1] * model.e_slow[1],
        gradient_force[0] * model.e_fast[0]
        + gradient_force[1] * model.e_fast[1],
        p_initial[0],
        arb(0),
    ]
    jacobian_rows = [energy_row] + closure_derivatives
    jacobian = arb_mat(4, 4, [item for row in jacobian_rows for item in row])
    return residual, jacobian, augmented, diagnostics


def arb_vector_solve(matrix: arb_mat, vector: Sequence[arb]) -> list[arb]:
    right = arb_mat(4, 1, list(vector))
    answer = matrix.solve(right)
    return [answer[row, 0] for row in range(4)]


def newton_refine_root(
    model: LocalValidatedModel,
    seed: Sequence[str | Decimal],
    *,
    epsilon: arb,
    iterations: int = 4,
    steps: int = 512,
    order: int = 16,
    midpoint_digits: int = 70,
) -> tuple[list[arb], list[dict[str, float]]]:
    """Refine a point root; each correction uses validated F and DF balls."""

    root = [decimal_ball(value) for value in seed]
    records: list[dict[str, float]] = []
    for index in range(iterations):
        residual, jacobian, _, diagnostics = residual_and_jacobian(
            model,
            root,
            epsilon=epsilon,
            steps=steps,
            order=order,
        )
        correction = arb_vector_solve(jacobian, residual)
        records.append(
            {
                "iteration": index,
                "max_residual_abs_upper": max(
                    float(abs(value).upper()) for value in residual
                ),
                "max_correction_abs_upper": max(
                    float(abs(value).upper()) for value in correction
                ),
                "max_flow_radius": diagnostics.max_output_radius,
            }
        )
        root = [
            exact_midpoint(value - delta, digits=midpoint_digits)
            for value, delta in zip(root, correction, strict=True)
        ]
    return root, records


def rational_preconditioner(jacobian: arb_mat, *, digits: int = 60) -> arb_mat:
    inverse = jacobian.mid().inv()
    return arb_mat(
        4,
        4,
        [
            exact_midpoint(inverse[row, column], digits=digits)
            for row in range(4)
            for column in range(4)
        ],
    )


@dataclass(frozen=True)
class KrawczykDiagnostics:
    included: bool
    preconditioner_nonsingular: bool
    root_radius: str
    max_relative_image_radius: float
    max_residual_abs_upper: float
    max_jacobian_width: float


def krawczyk_point_certificate(
    model: LocalValidatedModel,
    center: Sequence[arb],
    *,
    epsilon: arb,
    radius: arb,
    steps: int = 512,
    order: int = 16,
) -> tuple[list[arb], list[arb], KrawczykDiagnostics, FlowDiagnostics, list[arb]]:
    """Apply a four-dimensional interval Krawczyk inclusion at fixed epsilon.

    The Krawczyk base point is first frozen to exact decimal rationals.  The
    displacement domain is then formed as the actual ``box - x_bar`` rather
    than reconstructed from a nominal radius; this keeps the operator and the
    final strict-inclusion test on exactly the same mathematical box.
    """

    x_bar = [exact_midpoint(value) for value in center]
    point_residual, point_jacobian, point_augmented, _ = residual_and_jacobian(
        model,
        x_bar,
        epsilon=epsilon,
        steps=steps,
        order=order,
    )
    preconditioner = rational_preconditioner(point_jacobian)
    preconditioner_determinant = preconditioner.det()
    preconditioner_nonsingular = not preconditioner_determinant.contains(0)
    if not preconditioner_nonsingular:
        raise ArithmeticError("Krawczyk preconditioner determinant contains zero")
    box = [symmetric_ball(value, radius) for value in x_bar]
    _, box_jacobian, _, box_flow = residual_and_jacobian(
        model,
        box,
        epsilon=epsilon,
        steps=steps,
        order=order,
    )
    identity = arb_mat(4, 4, [
        arb(1 if row == column else 0)
        for row in range(4)
        for column in range(4)
    ])
    residual_column = arb_mat(4, 1, point_residual)
    delta_box = arb_mat(
        4,
        1,
        [domain - base for domain, base in zip(box, x_bar, strict=True)],
    )
    center_column = arb_mat(4, 1, x_bar)
    image_column = (
        center_column
        - preconditioner * residual_column
        + (identity - preconditioner * box_jacobian) * delta_box
    )
    image = [image_column[index, 0] for index in range(4)]
    included = all(
        strict_subset(item, domain)
        for item, domain in zip(image, box, strict=True)
    )
    relative = max(
        float(
            (
                (item - x_bar[index]).abs_upper()
                / (box[index] - x_bar[index]).abs_upper()
            ).upper()
        )
        for index, item in enumerate(image)
    )
    jacobian_width = max(
        float(box_jacobian[row, column].rad()) * 2
        for row in range(4)
        for column in range(4)
    )
    diagnostics = KrawczykDiagnostics(
        included=included,
        preconditioner_nonsingular=preconditioner_nonsingular,
        root_radius=radius.str(12, 0),
        max_relative_image_radius=relative,
        max_residual_abs_upper=max(float(abs(value).upper()) for value in point_residual),
        max_jacobian_width=jacobian_width,
    )
    return box, image, diagnostics, box_flow, point_augmented
