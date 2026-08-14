from fractions import Fraction

import sdc17_bar_koszul_experiment as audit


def test_subset_alphabet_and_scalar_koszul_identity():
    assert audit.nonempty_subsets(2) == ((0,), (1,), (0, 1))
    assert [audit.edge_sign(edge) for edge in audit.nonempty_subsets(2)] == [1, 1, -1]
    values = (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7))
    assert 1 - audit.subset_scalar_sum(values) == (1 - values[0]) * (
        1 - values[1]
    ) * (1 - values[2])


def test_necklace_rotation_and_primitivity():
    a, b = (0,), (1,)
    assert audit.canonical_necklace((b, a)) == (a, b)
    assert audit.is_primitive((a, b))
    assert not audit.is_primitive((a, b, a, b))
    assert audit.least_period((a, b, a, b)) == 2


def test_pq_and_p2q2_exact_primitive_power_ledger():
    rows = audit.primitive_power_ledger_rows()
    certificate = audit.p2q2_certificate(rows)
    assert certificate["pq_primitives"] == [
        {"word": "[p][q]", "sign": 1},
        {"word": "[pq]", "sign": -1},
    ]
    assert certificate["pq_primitive_pairing_possible"]
    assert certificate["p2q2_positive_primitive_count"] == 1
    assert certificate["p2q2_negative_primitive_count"] == 2
    assert not certificate["primitive_level_bijection_possible"]
    assert certificate["p2q2_primitive_sum"] == "-1"
    assert certificate["pq_r2_repetition_sum"] == "1"
    assert certificate["complete_log_coefficient"] == "0"
    assert certificate["cross_layer_cancellation_required"]


def test_p2q2_primitive_words_are_exactly_the_frozen_three():
    words = {
        audit.word_label(word, ("p", "q")): audit.word_sign(word)
        for word in audit.primitive_necklaces_at_multidegree((2, 2))
    }
    assert words == {
        "[p][p][q][q]": 1,
        "[p][q][pq]": -1,
        "[p][pq][q]": -1,
    }


def test_s3_virtual_character_and_no_equivariant_pairing():
    result = audit.s3_character_certificate()
    assert result["positive_count"] == result["negative_count"] == 3
    assert result["positive_action_orbit_sizes"] == [1, 2]
    assert result["negative_action_orbit_sizes"] == [3]
    assert result["positive_action_orbit_decomposition"] == [
        ["[pqr]"],
        ["[p][q][r]", "[p][r][q]"],
    ]
    assert result["negative_action_orbit_decomposition"] == [
        ["[p][qr]", "[pq][r]", "[pr][q]"]
    ]
    assert result["virtual_character_class_order"]["values"] == [0, 0, 3]
    assert result["irreducible_multiplicities"] == {
        "trivial": "1",
        "sign": "1",
        "standard": "-1",
    }
    assert result["virtual_representation"] == "1 + sign - standard"
    assert not result["equivariant_bijection_possible"]
    assert not result["lexicographic_pairing_natural"]
    assert any(
        row["equivariance_failures"] > 0
        for row in result["lexicographic_equivariance_audit"]
    )


def test_general_stirling_identity_is_exact():
    rows = audit.squarefree_stirling_rows()
    assert len(rows) == audit.STIRLING_CUTOFF
    assert rows[0]["coefficient"] == 1
    assert all(row["coefficient"] == 0 for row in rows[1:])
    assert all(row["identity_exact"] for row in rows)


def test_cyclic_partition_enumeration_matches_formula():
    rows = audit.cyclic_partition_count_rows()
    assert all(row["count_exact"] for row in rows)
    for atom_count in audit.SQUAREFREE_ENUM_CUTOFFS:
        selected = [row for row in rows if row["k"] == atom_count]
        assert sum(row["signed_contribution"] for row in selected) == 0


def test_scalar_sign_is_not_chain_parity_and_r2_leaks():
    rows = audit.scalar_supertrace_rows()
    certificate = audit.scalar_supertrace_certificate(rows)
    assert certificate["single_negative_edge"]["even_repetition_mismatch_count"] == 4
    assert certificate["single_negative_edge"]["r2_scalar_coefficient"] == 1
    assert certificate["single_negative_edge"]["r2_odd_supertrace_coefficient"] == -1
    assert certificate["single_negative_edge"]["r2_difference"] == 2
    assert certificate["non_power_matching_r2_leak"] == "1"
    assert certificate["scalar_two_edge_alphabet"]["length_two_mixed_primitive"]
    block = certificate["contractible_even_odd_block"]
    assert block["differential_matrix"] == ((0, 1), (0, 0))
    assert block["homotopy_matrix"] == ((0, 0), (1, 0))
    assert block["dh_plus_hd_matrix"] == ((1, 0), (0, 1))
    assert block["contraction_exact"]
    assert block["differential_commutes_with_transfer"]
    assert block["all_power_supertraces_zero"]
    assert block["mixed_length_two_primitive"] == "absent"
    assert not certificate["ledger_isomorphism_possible"]


def test_random_controls_all_cancel_and_are_shuffle_invariant():
    rows = audit.random_inventory_rows()
    assert len(rows) == len(audit.RANDOM_ATOM_CUTOFFS) * len(audit.RANDOM_SEEDS)
    assert all(row["exact_product_identity"] for row in rows)
    assert all(row["presentation_shuffle_invariant"] for row in rows)
    assert all(row["mixed_squarefree_log_coefficient"] == 0 for row in rows)
    assert all(row["proves_too_much"] for row in rows)


def test_full_generation_and_frozen_decision(tmp_path):
    result = audit.generate(tmp_path)
    assert result["zero_data_used"] is False
    assert result["general_squarefree_identity_exact"]
    assert result["cyclic_partition_counts_exact"]
    assert result["random_controls_exact"]
    assert result["decision"] == {
        "GO_SCALAR_KOSZUL_DETERMINANT": True,
        "GO_PRIMITIVE_LEVEL_INVOLUTION": False,
        "STOP_PRIMITIVE_LEVEL_INVOLUTION": True,
        "STOP_EQUIVARIANT_SIGN_REVERSAL": True,
        "STOP_PARITY_SUBSTITUTION": True,
        "STOP_ARITHMETIC_SELECTIVITY": True,
        "PROVES_TOO_MUCH": True,
        "ROUTE_B_LOCKED": True,
    }
    assert (tmp_path / "SHA256SUMS.txt").is_file()
