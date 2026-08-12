import numpy as np
from scipy import sparse

from hp_candidate_search.quantum_fd import (
    GridSpec,
    build_grid_operator,
    spectral_window,
)


def _small_spec(field: float) -> GridSpec:
    return GridSpec(
        a=1.02,
        n=1,
        magnetic_field=field,
        target_energy=40.0,
        nominal_spacing=0.35,
        eigenvalue_count=4,
        wall_factor=10.0,
    )


def test_lattice_operator_is_hermitian_and_zero_field_is_real():
    zero, _ = build_grid_operator(_small_spec(0.0))
    magnetic, _ = build_grid_operator(_small_spec(0.7))
    assert np.max(np.abs((zero - zero.getH()).data), initial=0.0) < 1.0e-13
    assert np.max(np.abs((magnetic - magnetic.getH()).data), initial=0.0) < 1.0e-13
    assert np.max(np.abs(zero.data.imag), initial=0.0) == 0.0
    assert np.max(np.abs(magnetic.data.imag), initial=0.0) > 0.0


def test_time_reversal_maps_field_to_minus_field():
    positive, _ = build_grid_operator(_small_spec(0.7))
    negative, _ = build_grid_operator(_small_spec(-0.7))
    difference = negative - positive.conjugate()
    assert np.max(np.abs(difference.data), initial=0.0) < 1.0e-13


def test_symmetric_and_landau_gauges_are_isospectral_on_the_grid():
    symmetric_spec = _small_spec(0.7)
    landau_spec = GridSpec(**{**symmetric_spec.__dict__, "gauge": "landau"})
    symmetric, metadata = build_grid_operator(symmetric_spec)
    landau, _ = build_grid_operator(landau_spec)
    xmin, _, ymin, _ = metadata["bounds"]
    x = xmin + metadata["hx"] * np.arange(1, metadata["nx"] + 1)
    y = ymin + metadata["hy"] * np.arange(1, metadata["ny"] + 1)
    xx, yy = np.meshgrid(x, y, indexing="xy")
    phase = np.exp(0.5j * symmetric_spec.magnetic_field * xx * yy).ravel()
    gauge_transform = sparse.diags(phase)
    transformed = gauge_transform @ symmetric @ gauge_transform.getH()
    difference = landau - transformed
    relative_defect = np.max(np.abs(difference.data), initial=0.0) / np.max(
        np.abs(landau.data)
    )
    assert relative_defect < 2.0e-14


def test_symmetric_gauge_plaquette_has_the_prescribed_flux():
    field = 0.7
    hx = 0.13
    hy = 0.17
    x = 0.21
    y = -0.19
    ux_bottom = np.exp(0.5j * field * y * hx)
    uy_right = np.exp(-0.5j * field * (x + hx) * hy)
    ux_top_reverse = np.conjugate(np.exp(0.5j * field * (y + hy) * hx))
    uy_left_reverse = np.conjugate(np.exp(-0.5j * field * x * hy))
    loop = ux_bottom * uy_right * ux_top_reverse * uy_left_reverse
    np.testing.assert_allclose(loop, np.exp(-1.0j * field * hx * hy), atol=2e-15)


def test_frozen_spectral_window_has_140_levels_and_138_adjacent_ratios():
    values = np.arange(180.0)[::-1]
    core = spectral_window(values)
    assert len(core) == 140
    assert len(np.diff(core)) - 1 == 138
    np.testing.assert_array_equal(core, np.arange(25.0, 165.0))
