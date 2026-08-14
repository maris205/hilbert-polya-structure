from fractions import Fraction

import sdc16_tensor_bar_experiment as audit


def test_tensor_factorisation_primitives():
    assert audit.first_tensor_indecomposables(6) == (2, 3, 5, 7, 11, 13)
    assert audit.first_tensor_decomposables(6) == (4, 6, 8, 9, 10, 12)
    assert audit.factor_exponents(360) == ((2, 3), (3, 2), (5, 1))
    assert audit.total_factor_depth(360) == 6
    assert audit.distinct_factor_depth(360) == 3
    assert audit.valuation(360, 2) == 3
    assert audit.divisors(12) == (1, 2, 3, 4, 6, 12)


def test_incidence_mobius_is_computed_from_divisibility():
    mu = audit.incidence_mobius(12)
    assert mu[1:13] == (1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0)
    for value in range(1, 13):
        assert sum(mu[divisor] for divisor in audit.divisors(value)) == int(value == 1)


def test_global_tensor_lambda_exact_prime_power_support():
    mu = audit.incidence_mobius(128)
    assert audit.tensor_lambda_vector(2, mu) == {2: 1}
    assert audit.tensor_lambda_vector(8, mu) == {2: 1}
    assert audit.tensor_lambda_vector(81, mu) == {3: 1}
    assert audit.tensor_lambda_vector(12, mu) == {}
    assert audit.tensor_lambda_vector(18, mu) == {}
    for value in range(1, 129):
        assert audit.tensor_lambda_vector(value, mu) == audit.expected_tensor_lambda(value)


def test_global_incidence_cutoff_and_inventory_source_lock():
    ledger = audit.incidence_ledger_rows()
    controls = audit.incidence_control_rows()
    relabels = audit.entropy_relabel_rows()
    result = audit.incidence_summary(ledger, controls, relabels)
    assert result["mobius_inverse_exact_all"]
    assert result["lambda_identity_exact_all"]
    assert result["cutoff_stable_exact"]
    assert result["entropy_relabel_controls"]["all_random_relabels_break_selector"]
    assert result["inventory_source_lock_boundary"]["shuffled_primes"][
        "order_invariant_all"
    ]
    assert not result["inventory_source_lock_boundary"]["composites"][
        "unit_augmented_divisor_closed_all"
    ]
    assert not result["inventory_source_lock_boundary"]["random_increasing"][
        "unit_augmented_divisor_closed_all"
    ]
    assert result["decision"]["GO_GLOBAL_INCIDENCE_SELECTOR"]
    assert result["not_a_local_cocycle"]
    assert result["not_a_character_or_fourier_mode"]


def test_bar_formal_coefficients_are_exact_mobius_inverse():
    rows = audit.bar_formal_coefficient_rows(256)
    assert len(rows) == 256
    assert all(row["bar_coefficient_exact"] for row in rows)
    assert all(row["determinant_coefficient_exact"] for row in rows)
    assert all(row["independent_inverse_exact"] for row in rows)
    by_n = {row["n"]: row for row in rows}
    assert by_n[2]["bar_endpoint_coefficient"] == "1"
    assert by_n[8]["bar_endpoint_coefficient"] == "0"
    assert by_n[12]["bar_endpoint_coefficient"] == "0"
    assert by_n[30]["bar_endpoint_coefficient"] == "1"


def test_bar_exact_geometric_certificates():
    result = audit.bar_exact_rational_certificates()
    assert result["reciprocal_identity_exact"]
    assert all(row["exact_geometric_identity"] for row in result["word_length_rows"])


def test_bar_sigma_threshold_and_raw_word_region():
    sigma_bar = float(audit.bar_sigma_threshold())
    assert abs(sigma_bar - 1.7286472389981836) < 1e-14
    rows = audit.bar_raw_convergence_rows()
    assert all(row["raw_region_certified"] for row in rows)
    assert max(row["exact_remainder_residual"] for row in rows) < 1e-75
    assert max(row["closed_D_identity_residual"] for row in rows) < 1e-75
    assert all(row["actual_F_residual"] <= row["absolute_geometric_tail_bound"] for row in rows)


def test_independent_mobius_sieve_and_endpoint_completion():
    assert audit.mobius_linear_sieve(512) == audit.incidence_mobius(512)
    rows = audit.bar_endpoint_completion_rows()
    assert len(rows) == len(audit.BAR_ENDPOINT_POINTS) * len(audit.BAR_ENDPOINT_CUTOFFS)
    assert all(row["completion_region"] for row in rows)
    assert all(row["evidence_label"] == "NUMERICAL_OBSERVATION" for row in rows)
    assert all(row["D_residual_observation"] <= row["absolute_tail_majorant"] for row in rows)


def test_trace_log_repetitions_and_universal_controls():
    trace_rows = audit.bar_trace_log_rows()
    assert all(row["abs_zF"] < 1 for row in trace_rows)
    final = [
        row
        for row in trace_rows
        if row["repetition_cutoff"] == max(audit.BAR_TRACE_REPETITIONS)
    ]
    assert max(row["trace_log_residual"] for row in final) < 1e-18
    controls = audit.bar_universal_control_rows()
    assert len(controls) == 10
    assert all(row["universal_inversion_exact"] for row in controls)
    assert all(row["proves_too_much"] for row in controls)


def test_goodness_is_intrinsic_ordered_tensor_adjacency():
    assert audit.edge_goodness((2, 3, 5, 7, 11)) == (1, 1, 1, 1)
    assert audit.edge_goodness((3, 2, 5, 7, 11)) == (0, 0, 1, 1)
    assert audit.edge_goodness((4, 6, 8, 9, 10)) == (0, 0, 0, 0)


def test_mode_two_formula_selected_small_case():
    values = (2, 3)
    xs = (Fraction(1, 4), Fraction(1, 9))
    amplitude = (xs[0] + xs[1]) / 2
    expected = -(Fraction(1, 3) ** 2) * amplitude**2
    assert audit.exact_mode_two_coefficient(values, (2,)) == expected
    assert audit.exact_mode_two_coefficient(values, (3,)) == 0
    assert audit.exact_continuant(values, (2,))[2] == expected


def test_positive_cone_criterion_and_witnesses_exhaustively():
    for length in (1, 2, 3):
        for charges in __import__("itertools").product(range(-2, 3), repeat=length):
            certificate = audit.cone_certificate(charges)
            expected_safe = all(charge > 0 for charge in charges) or all(
                charge < 0 for charge in charges
            )
            assert certificate["safe"] == expected_safe
            if not expected_safe:
                assert certificate["witness"]["total"] == 0
                if len(certificate["witness"]["edges"]) > 1:
                    assert certificate["witness"]["connected_support"]
                    assert min(certificate["witness"]["multiplicities"]) > 0


def test_gauge_coboundaries_leave_roundtrip_class_exactly_fixed():
    values = audit.primary_inventory(16)
    baseline = audit.exact_mode_two_coefficient(values, audit.constant_rule(values))
    baseline_polynomial = audit.exact_continuant(values, audit.constant_rule(values))
    for potential in audit.GAUGE_POTENTIALS.values():
        forward, backward = audit.oriented_gauge_charges(values, potential)
        roundtrip = tuple(left + right for left, right in zip(forward, backward))
        assert roundtrip == (2,) * 15
        assert audit.exact_mode_two_coefficient(values, roundtrip) == baseline
        assert audit.exact_continuant(values, roundtrip) == baseline_polynomial


def test_all_named_rules_preserve_euler_neutral_sector():
    for count in audit.CUTOFFS:
        for values in (
            audit.primary_inventory(count),
            audit.composite_inventory(count),
            audit.shuffled_inventory(count, audit.SHUFFLE_SEEDS[0]),
            audit.random_increasing_inventory(count, audit.RANDOM_INVENTORY_SEEDS[0]),
        ):
            for rule in audit.RULES.values():
                charges = rule(values)
                assert min(charges) >= 2
                assert audit.cone_certificate(charges)["safe"]


def test_planted_controls_are_nontrivial_but_copy_witnesses():
    count = 32
    primary = audit.primary_inventory(count)
    prefix = audit.prefix_preserving_shuffle(count, 6)
    block = audit.block_preserving_shuffle(count, 8)
    assert prefix != primary and set(prefix) == set(primary)
    assert block != primary and set(block) == set(primary)
    assert audit.edge_goodness(prefix)[:5] == (1,) * 5
    assert (1, 1, 1) in tuple(
        zip(
            audit.edge_goodness(block),
            audit.edge_goodness(block)[1:],
            audit.edge_goodness(block)[2:],
        )
    )


def test_exhaustive_local_rules_have_no_robust_selector():
    result = audit.exhaustive_radius_one_summary()
    assert result["truth_tables_exhausted"] == 256
    assert result["primary_active_count"] > 0
    assert result["robust_selectivity_pass_count"] == 0


def test_exhaustive_automatic_rules_have_no_robust_selector():
    result = audit.exhaustive_mealy_summary()
    assert result["by_state_count"]["1"]["machines_exhausted"] == 4
    assert result["by_state_count"]["2"]["machines_exhausted"] == 256
    assert result["robust_selectivity_pass_total"] == 0


def test_full_summary_is_frozen_and_route_b_locked(tmp_path):
    result = audit.generate(tmp_path)
    assert result["zero_data_used"] is False
    assert result["decision"] == {
        "GO_SOURCE_DERIVED_SELECTOR": False,
        "GO_GLOBAL_INCIDENCE_SELECTOR": True,
        "GO_BAR_ANALYTIC_DETERMINANT": True,
        "STOP_FINITE_LOCAL_SELECTOR": True,
        "STOP_FINITE_STATE_SELECTOR": True,
        "PROVES_TOO_MUCH": True,
        "ROUTE_B_LOCKED": True,
    }
    assert result["finite_radius"]["robust_selectivity_pass_count"] == 0
    assert result["finite_state"]["robust_selectivity_pass_total"] == 0
    assert result["global_incidence"]["lambda_identity_exact_all"]
    assert result["global_incidence"]["not_a_determinant"]
    assert result["bar_determinant"]["formal_coefficients_exact_all"]
    assert result["bar_determinant"]["universal_controls_exact_all"]
    assert result["bar_determinant"]["target_zero_metrics"] == "not_applicable"
    assert (tmp_path / "SHA256SUMS.txt").is_file()
