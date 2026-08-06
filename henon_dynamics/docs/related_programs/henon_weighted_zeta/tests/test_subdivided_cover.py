from scripts.audit_subdivided_cover import summarize_configuration


def test_subdivided_strip_tightens_area_enclosure():
    coarse = summarize_configuration("main", 0.6380064794363034, 16, 0.0, 1)
    fine = summarize_configuration("main", 0.6380064794363034, 16, 0.0, 16)
    assert fine["forward_enclosure_area_ratio_median"] < coarse[
        "forward_enclosure_area_ratio_median"
    ]
    assert fine["backward_enclosure_area_ratio_median"] < coarse[
        "backward_enclosure_area_ratio_median"
    ]


def test_subdivided_strip_preserves_full_cell_in_box_decision():
    coarse = summarize_configuration("main", 0.6380064794363034, 16, 0.0, 1)
    fine = summarize_configuration("main", 0.6380064794363034, 16, 0.0, 16)
    assert fine["two_sided_in_box_fraction"] == coarse[
        "two_sided_in_box_fraction"
    ]
