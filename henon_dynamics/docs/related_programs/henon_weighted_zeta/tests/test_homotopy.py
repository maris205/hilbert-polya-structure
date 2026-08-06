import numpy as np
import pytest

from henon_zeta.geometry import fixed_points
from henon_zeta.homotopy import (
    cluster_endpoints,
    real_primitive_orbits,
    refine_complex_endpoint,
    target_residual,
    total_degree_starts,
    track_path,
)


def tracked_roots(a, period):
    gamma = np.exp(0.371j)
    results = [track_path(start, a, gamma, path_index=index) for index, start in enumerate(total_degree_starts(period))]
    assert all(result.success for result in results)
    roots = cluster_endpoints(results)
    assert len(roots) == 2**period
    return roots


def test_total_degree_homotopy_recovers_fixed_points():
    roots = tracked_roots(1.02, 1)
    recovered = sorted(root[0].real for root in roots)
    expected = sorted(record.coordinate for record in fixed_points(1.02))
    assert recovered == pytest.approx(expected, abs=1e-9)


def test_period2_has_four_complex_roots_and_two_real_roots():
    roots = tracked_roots(1.02, 2)
    refined = [refine_complex_endpoint(root, 1.02, dps=60) for root in roots]
    assert sum(record["is_real"] for record in refined) == 2
    assert max(float(np.linalg.norm(target_residual(root, 1.02), ord=np.inf)) for root in roots) < 1e-9


def test_period3_census_recovers_two_real_primitive_orbits():
    roots = tracked_roots(1.02, 3)
    refined = [refine_complex_endpoint(root, 1.02, dps=60) for root in roots]
    assert sum(record["is_real"] for record in refined) == 8
    assert len(real_primitive_orbits(refined, 3)) == 2
