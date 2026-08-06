import numpy as np

from scripts.audit_interval_cover import edge_vector, summarize_configuration


def test_interval_cover_edges_are_valid_for_shifted_cells():
    edges = edge_vector(0.6380064794363034, 16, 0.25)
    widths = np.diff(edges)
    assert len(edges) == 17
    assert np.all(widths > 0.0)
    assert widths.min() < widths.max()


def test_interval_cover_summary_has_bounded_fractions_and_inflation():
    summary = summarize_configuration(
        "main", 0.6380064794363034, 16, 0.0
    )
    assert 0.0 <= summary["two_sided_in_box_fraction"] <= 1.0
    assert summary["forward_enclosure_area_ratio_median"] >= 1.0
    assert summary["backward_enclosure_area_ratio_median"] >= 1.0
    assert summary["maximum_outward_excursion"] >= 0.0
