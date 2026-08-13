import numpy as np

import sdc11_reflection_double_experiment as experiment


def test_internal_atom_source():
    assert experiment.internal_multiplicative_atoms(8) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_exact_reflected_trace_ledger():
    audit = experiment.exact_candidate_audit(power_cutoff=8)
    assert audit["all_exact"]
    assert audit["all_mixed_identity_words_killed"]
    assert audit["all_odd_traces_zero"]
    row = next(row for row in audit["rows"] if row["length"] == 4)
    assert row["target"] == "2*a0**2*b0**2 + 2*a1**2*b1**2 + 2*a2**2*b2**2"


def test_label_leakage_controls():
    controls = experiment.label_controls(cutoff=10)
    assert controls["independent_positive_alphabets"]["first_mixed_identity"] is None
    assert controls["shared_positive_alphabet"]["first_mixed_identity"] is None
    assert controls["inverse_reflected_labels"]["first_mixed_identity"]["length"] == 2
    assert controls["finite_C5_labels"]["first_mixed_identity"]["length"] == 10


def test_common_schatten_strip_and_direct_sum_S1():
    audit = experiment.schatten_audit()
    assert audit["first_integer_q_with_nonempty_common_strip"] == 3
    assert not experiment.common_schatten_strip(2)["nonempty"]
    assert experiment.common_schatten_strip(3)["nonempty"]
    assert not audit["direct_sum_S1_common_domain"]["has_common_domain"]


def test_reflection_and_det3_product():
    masses = [2, 3, 5]
    s = 0.43 + 2.1j
    matrix = experiment.pure_reflection_matrix(masses, s)
    reflected = experiment.pure_reflection_matrix(masses, 1 - s)
    swap = experiment.channel_swap(len(masses))
    assert np.linalg.norm(swap @ matrix @ swap - reflected) < 1e-12
    z = 0.2 + 0.1j
    assert abs(
        experiment.finite_det3(matrix, z) - experiment.det3_product(masses, z)
    ) < 1e-12


def test_cross_atom_cosh_and_motion():
    p, q = 2, 3
    for s in [0.4 + 1.2j, 0.5 + 7j, 0.6 + 0.3j]:
        assert abs(
            experiment.oriented_pair_sum(p, q, s)
            - experiment.oriented_pair_cosh(p, q, s)
        ) < 1e-12
    audit = experiment.pairing_audit(seed_count=4)
    assert audit["random_motion_pass_count"] == 4


def test_random_dag_proves_too_much():
    audit = experiment.random_dag_audit(seed_count=4)
    assert audit["ledger_pass_count"] == 4
    assert audit["singular_motion_count"] == 4
    assert max(row["max_trace_error_r2_r4_r6_r8"] for row in audit["rows"]) < 1e-9


def test_pure_block_eigenvalues_are_s_independent():
    masses = [2, 3, 5]
    matrix = experiment.pure_reflection_matrix(masses, 0.5 + 13j)
    got = sorted(np.linalg.eigvals(matrix).real)
    expected = sorted([sign / np.sqrt(p) for p in masses for sign in [-1, 1]])
    assert np.max(np.abs(np.asarray(got) - np.asarray(expected))) < 1e-12
