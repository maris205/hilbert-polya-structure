import numpy as np
import pytest
from scipy.integrate import quad

from henon_zeta.operator import (
    assemble_absorbing_ulam,
    assemble_overlap_ulam,
    assemble_shifted_overlap_ulam,
    assemble_sobol_ulam,
    dominant_spectrum,
    finite_time_survivor_mask,
    quadratic_strip_overlap_area,
)


def _adaptive_overlap_area(
    a,
    x_lower,
    x_upper,
    y_lower,
    y_upper,
    target_x_lower,
    target_x_upper,
):
    def overlap_length(x):
        image_interval_lower = 1.0 - a * x * x - target_x_upper
        image_interval_upper = 1.0 - a * x * x - target_x_lower
        return max(
            0.0,
            min(y_upper, image_interval_upper)
            - max(y_lower, image_interval_lower),
        )

    value, _ = quad(
        overlap_length,
        x_lower,
        x_upper,
        points=np.linspace(x_lower, x_upper, 33)[1:-1],
        epsabs=2.0e-13,
        epsrel=2.0e-13,
        limit=300,
    )
    return value


def test_absorbing_ulam_is_substochastic_without_renormalization():
    assembly = assemble_absorbing_ulam(a=1.02, radius=2.5, cells_per_axis=12, quadrature_order=3)
    assert assembly.matrix.shape == (144, 144)
    assert np.max(assembly.row_sums) <= 1.0 + 1e-12
    assert np.any(assembly.row_sums < 1.0 - 1e-12)
    assert np.any(assembly.row_sums == 0.0)


def test_grid_cell_hole_has_zero_source_rows():
    assembly = assemble_absorbing_ulam(
        a=1.02,
        radius=2.5,
        cells_per_axis=16,
        quadrature_order=2,
        hole_radius=0.35,
    )
    assert np.any(~assembly.active_cells)
    assert np.all(assembly.row_sums[~assembly.active_cells] == 0.0)
    assert assembly.hole_center is not None


def test_dominant_operator_spectrum_has_small_residuals():
    assembly = assemble_absorbing_ulam(a=6.0, radius=1.0, cells_per_axis=8, quadrature_order=3)
    spectrum = dominant_spectrum(assembly, eigenvalue_count=4)
    assert abs(spectrum.leading_eigenvalue) <= 1.0 + 1e-10
    assert max(item.right_residual for item in spectrum.eigenpairs) < 1e-9
    assert max(item.left_residual for item in spectrum.eigenpairs) < 1e-9


def test_random_shift_sobol_ulam_is_reproducible_and_substochastic():
    first = assemble_sobol_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=10,
        samples_per_cell=16,
        seed=17,
    )
    second = assemble_sobol_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=10,
        samples_per_cell=16,
        seed=17,
    )
    assert first.method == "random_shift_sobol"
    assert first.samples_per_cell == 16
    assert first.seed == 17
    assert np.max(first.row_sums) <= 1.0 + 1e-12
    assert np.array_equal(first.matrix.indptr, second.matrix.indptr)
    assert np.array_equal(first.matrix.indices, second.matrix.indices)
    assert np.array_equal(first.matrix.data, second.matrix.data)


def test_sobol_and_gauss_ulam_give_compatible_control_spectra():
    gauss = assemble_absorbing_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=12,
        quadrature_order=4,
    )
    sobol = assemble_sobol_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=12,
        samples_per_cell=64,
        seed=23,
    )
    gauss_value = abs(dominant_spectrum(gauss, eigenvalue_count=4).leading_eigenvalue)
    sobol_value = abs(dominant_spectrum(sobol, eigenvalue_count=4).leading_eigenvalue)
    assert abs(gauss_value - sobol_value) < 0.1


def test_finite_time_survivor_mask_is_nested_and_shared_by_assembly():
    mask0 = finite_time_survivor_mask(6.0, 1.0, 24, horizon=0)
    mask2 = finite_time_survivor_mask(6.0, 1.0, 24, horizon=2)
    mask4 = finite_time_survivor_mask(6.0, 1.0, 24, horizon=4)
    assert np.all(mask0)
    assert np.all(mask4 <= mask2)
    assert np.all(mask2 <= mask0)
    assembly = assemble_absorbing_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=24,
        quadrature_order=3,
        survivor_horizon=4,
    )
    assert np.array_equal(assembly.active_cells, mask4)
    assert np.max(assembly.row_sums) <= 1.0 + 1e-12


def test_quadratic_strip_overlap_matches_adaptive_quadrature():
    representative_cases = [
        (0.0, -0.3, 0.2, 0.0, 0.5, 0.5, 1.0),
        (1.02, -0.2, 0.1, 0.3, 0.6, -0.5, -0.2),
        (6.0, -0.5, -0.25, -0.25, 0.0, 0.0, 0.25),
        (6.0, -0.2, 0.2, -0.4, 0.1, 0.6, 1.0),
        (1.02, 0.3, 0.5, -0.8, -0.4, 1.0, 1.4),
        (
            2.0,
            -2.272727272727273,
            -1.3636363636363638,
            -2.272727272727273,
            -1.3636363636363638,
            -0.45454545454545503,
            0.45454545454545414,
        ),
    ]
    for case in representative_cases:
        analytic = quadratic_strip_overlap_area(*case)
        numerical = _adaptive_overlap_area(*case)
        assert np.isclose(analytic, numerical, rtol=2.0e-11, atol=2.0e-11)

    generator = np.random.default_rng(20260801)
    for _ in range(64):
        a = float(generator.choice([0.0, 0.7, 1.02, 6.0]))
        radius = float(generator.choice([1.0, 2.5]))
        cells_per_axis = int(generator.choice([7, 11, 17]))
        edges = np.linspace(-radius, radius, cells_per_axis + 1)
        source_x, source_y, target_x = generator.integers(
            0, cells_per_axis, size=3
        )
        case = (
            a,
            float(edges[source_x]),
            float(edges[source_x + 1]),
            float(edges[source_y]),
            float(edges[source_y + 1]),
            float(edges[target_x]),
            float(edges[target_x + 1]),
        )
        analytic = quadratic_strip_overlap_area(*case)
        numerical = _adaptive_overlap_area(*case)
        assert np.isclose(analytic, numerical, rtol=2.0e-10, atol=5.0e-11)


def test_overlap_ulam_is_nonnegative_substochastic_and_respects_y_index():
    cells_per_axis = 12
    assembly = assemble_overlap_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=cells_per_axis,
    )
    assert assembly.method == "semi_analytic_overlap"
    assert np.all(assembly.matrix.data >= -1.0e-15)
    assert np.all(assembly.row_sums >= -1.0e-15)
    assert np.max(assembly.row_sums) <= 1.0 + 5.0e-12
    assert np.any(assembly.row_sums < 1.0 - 1.0e-12)

    entries = assembly.matrix.tocoo()
    source_x_indices = entries.row % cells_per_axis
    target_y_indices = entries.col // cells_per_axis
    assert np.array_equal(source_x_indices, target_y_indices)


def test_overlap_and_gauss_q8_have_compatible_small_grid_spectra():
    overlap = assemble_overlap_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=10,
    )
    gauss = assemble_absorbing_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=10,
        quadrature_order=8,
    )
    overlap_value = abs(
        dominant_spectrum(overlap, eigenvalue_count=4).leading_eigenvalue
    )
    gauss_value = abs(
        dominant_spectrum(gauss, eigenvalue_count=4).leading_eigenvalue
    )
    assert abs(overlap_value - gauss_value) < 0.02


def test_overlap_ulam_respects_reversibility_index_symmetry():
    cells_per_axis = 11
    assembly = assemble_overlap_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=cells_per_axis,
    )
    swap = np.arange(cells_per_axis**2).reshape(
        cells_per_axis, cells_per_axis
    ).T.ravel()
    reversed_matrix = assembly.matrix[swap][:, swap]
    difference = assembly.matrix.transpose() - reversed_matrix
    assert np.max(np.abs(difference.data), initial=0.0) < 2.0e-13


def test_overlap_ulam_rejects_currently_unsupported_negative_parameter():
    with pytest.raises(ValueError, match="nonnegative a"):
        assemble_overlap_ulam(a=-0.5, radius=1.0, cells_per_axis=8)


def test_shifted_overlap_zero_offset_matches_uniform_overlap():
    uniform = assemble_overlap_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=12,
    )
    shifted = assemble_shifted_overlap_ulam(
        a=6.0,
        radius=1.0,
        cells_per_axis=12,
        grid_offset=0.0,
    )
    difference = uniform.matrix - shifted.matrix
    assert np.max(np.abs(difference.data), initial=0.0) < 5.0e-13
    assert shifted.grid_offset == 0.0


def test_shifted_overlap_has_weighted_reversibility_and_substochastic_rows():
    radius = 1.0
    cells_per_axis = 12
    offset = 0.25
    assembly = assemble_shifted_overlap_ulam(
        a=6.0,
        radius=radius,
        cells_per_axis=cells_per_axis,
        grid_offset=offset,
    )
    assert assembly.method == "semi_analytic_overlap_shifted"
    assert np.max(assembly.row_sums) <= 1.0 + 5.0e-12
    entries = assembly.matrix.tocoo()
    source_x_indices = entries.row % cells_per_axis
    target_y_indices = entries.col // cells_per_axis
    assert np.array_equal(source_x_indices, target_y_indices)

    nominal_width = 2.0 * radius / cells_per_axis
    edges = np.concatenate(
        (
            np.asarray([-radius]),
            -radius
            + (np.arange(1, cells_per_axis) + offset) * nominal_width,
            np.asarray([radius]),
        )
    )
    widths = np.diff(edges)
    cell_areas = np.outer(widths, widths).ravel()
    unnormalized = assembly.matrix.toarray() * cell_areas[:, None]
    swap = np.arange(cells_per_axis**2).reshape(
        cells_per_axis, cells_per_axis
    ).T.ravel()
    reversed_unnormalized = unnormalized[swap][:, swap].T
    assert np.max(np.abs(unnormalized - reversed_unnormalized)) < 2.0e-13
