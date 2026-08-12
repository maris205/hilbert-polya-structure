import numpy as np
from scipy import sparse

from hp_candidate_search.quantum_fd import GridSpec
from hp_candidate_search.quantum_fd4 import build_grid_operator_fourth


def _small_spec(field: float, gauge: str = "symmetric") -> GridSpec:
    return GridSpec(
        a=1.02,
        n=1,
        magnetic_field=field,
        target_energy=40.0,
        nominal_spacing=0.35,
        eigenvalue_count=4,
        wall_factor=10.0,
        gauge=gauge,
    )


def test_fourth_order_operator_is_hermitian_and_zero_field_is_real():
    zero, _ = build_grid_operator_fourth(_small_spec(0.0))
    magnetic, _ = build_grid_operator_fourth(_small_spec(0.7))
    assert np.max(np.abs((zero - zero.getH()).data), initial=0.0) < 1.0e-13
    assert np.max(np.abs((magnetic - magnetic.getH()).data), initial=0.0) < 1.0e-13
    assert np.max(np.abs(zero.data.imag), initial=0.0) == 0.0
    assert np.max(np.abs(magnetic.data.imag), initial=0.0) > 0.0


def test_fourth_order_time_reversal_maps_field_to_minus_field():
    positive, _ = build_grid_operator_fourth(_small_spec(0.7))
    negative, _ = build_grid_operator_fourth(_small_spec(-0.7))
    difference = negative - positive.conjugate()
    assert np.max(np.abs(difference.data), initial=0.0) < 1.0e-13


def test_fourth_order_symmetric_and_landau_gauges_are_equivalent():
    symmetric_spec = _small_spec(0.7)
    symmetric, metadata = build_grid_operator_fourth(symmetric_spec)
    landau, _ = build_grid_operator_fourth(_small_spec(0.7, "landau"))
    xmin, _, ymin, _ = metadata["bounds"]
    x = xmin + metadata["hx"] * np.arange(1, metadata["nx"] + 1)
    y = ymin + metadata["hy"] * np.arange(1, metadata["ny"] + 1)
    xx, yy = np.meshgrid(x, y, indexing="xy")
    phase = np.exp(0.5j * symmetric_spec.magnetic_field * xx * yy).ravel()
    transform = sparse.diags(phase)
    difference = landau - transform @ symmetric @ transform.getH()
    relative = np.max(np.abs(difference.data), initial=0.0) / np.max(
        np.abs(landau.data)
    )
    assert relative < 2.0e-14
