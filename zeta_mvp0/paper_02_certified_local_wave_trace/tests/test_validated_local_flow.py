from __future__ import annotations

import pytest


pytest.importorskip("flint")

from flint import arb, ctx

from hp_candidate_search.validated_local_flow import (
    decimal_ball,
    krawczyk_point_certificate,
    integrate_validated_flow,
    local_initial_state,
    local_model,
    normalized_energy,
)


def test_exact_normal_coordinates_are_orthonormal() -> None:
    previous_precision = ctx.prec
    try:
        ctx.prec = 128
        model = local_model()
        slow_norm = model.e_slow[0] ** 2 + model.e_slow[1] ** 2
        fast_norm = model.e_fast[0] ** 2 + model.e_fast[1] ** 2
        dot = model.e_slow[0] * model.e_fast[0] + model.e_slow[1] * model.e_fast[1]
        assert slow_norm.contains(1)
        assert fast_norm.contains(1)
        assert dot.contains(0)
    finally:
        ctx.prec = previous_precision


def test_interval_taylor_closes_exact_fast_harmonic_orbit() -> None:
    previous_precision = ctx.prec
    try:
        ctx.prec = 160
        model = local_model()
        epsilon = arb(0)
        amplitude = decimal_ball("2").sqrt() / model.omega_fast
        period = 1 / model.lambda_fast.sqrt()
        root = [arb(0), amplitude, arb(0), period]
        initial = local_initial_state(model, root)
        assert normalized_energy(model, epsilon, initial).contains(1)

        terminal, diagnostics = integrate_validated_flow(
            model,
            initial,
            epsilon=epsilon,
            period=period,
            steps=64,
            order=14,
        )
        assert all(
            (end - start).contains(0)
            for start, end in zip(initial, terminal, strict=True)
        )
        assert diagnostics.max_picard_ratio < 1
        assert diagnostics.max_output_radius < 1.0e-15
    finally:
        ctx.prec = previous_precision


def test_fixed_point_krawczyk_uses_one_box_and_nonsingular_preconditioner() -> None:
    previous_precision = ctx.prec
    try:
        ctx.prec = 128
        model = local_model()
        root = [
            arb(0),
            decimal_ball("2").sqrt() / model.omega_fast,
            arb(0),
            1 / model.lambda_fast.sqrt(),
        ]
        box, image, diagnostics, _flow, _terminal = krawczyk_point_certificate(
            model,
            root,
            epsilon=arb(0),
            radius=decimal_ball("1e-10"),
            steps=64,
            order=14,
        )
        assert diagnostics.included
        assert diagnostics.preconditioner_nonsingular
        assert diagnostics.max_relative_image_radius < 1.0e-4
        assert all(
            inner.lower() > outer.lower() and inner.upper() < outer.upper()
            for inner, outer in zip(image, box, strict=True)
        )
    finally:
        ctx.prec = previous_precision
