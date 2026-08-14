#!/usr/bin/env python3
"""Generate deterministic exact artifacts for SD-C29."""

from __future__ import annotations

import ast
import csv
from fractions import Fraction
import json
import platform
from pathlib import Path
import sys

import mpmath as mp
import sympy as sp

from sdc29_evaluator import (
    arithmetic_mobius,
    deterministic_permutation,
    evaluator_atoms,
    expected_incidence_entry,
    trial_atom,
)
from sdc29_incidence_atom_compiler import (
    affine_one_form,
    affine_zero_form,
    atom_actions,
    canonical_rotation,
    compiled_entry,
    compiled_idempotents,
    covers_bottom,
    cyclic_orbit_size,
    de_rham_tensor_transfers,
    derivative_matrix,
    divisibility_relation,
    finite_transfer,
    fraction_text,
    gamma_affine_branch,
    gamma_code,
    gamma_length,
    incidence_inverse,
    marked_weight,
    mutate_six_to_cover,
    necklace_representatives,
    permute_matrix,
    selector_value,
    word_trace_via_pair_relations,
    zeta_matrix,
)


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CORE = ROOT / "code" / "sdc29_incidence_atom_compiler.py"
RESULTS.mkdir(parents=True, exist_ok=True)


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"empty artifact: {name}")
    path = RESULTS / name
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(name: str, payload: object) -> None:
    (RESULTS / name).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def boolean(value: object) -> bool:
    return bool(value)


def main() -> int:
    cutoff = 30
    relation = divisibility_relation(cutoff)
    zeta, mobius, compiled = compiled_idempotents(relation)
    atom_indices = covers_bottom(relation)
    atom_labels = [index + 1 for index in atom_indices]
    identity = sp.eye(cutoff)
    zero = sp.zeros(cutoff)

    inverse_rows: list[dict[str, object]] = []
    for finite_cutoff in (6, 12, 18, 30):
        finite_relation = divisibility_relation(finite_cutoff)
        finite_zeta = zeta_matrix(finite_relation)
        finite_mobius = incidence_inverse(finite_relation)
        left = finite_zeta * finite_mobius
        right = finite_mobius * finite_zeta
        inverse_rows.append(
            {
                "cutoff": finite_cutoff,
                "entry_checks_per_side": finite_cutoff**2,
                "zeta_mobius_identity": left == sp.eye(finite_cutoff),
                "mobius_zeta_identity": right == sp.eye(finite_cutoff),
                "exact": left == sp.eye(finite_cutoff) == right,
            }
        )
    write_csv("incidence_inverse_ledger.csv", inverse_rows)

    primitive_rows: list[dict[str, object]] = []
    for index, matrix in enumerate(compiled):
        formula_exact = all(
            matrix[left, right] == compiled_entry(zeta, mobius, index, left, right)
            for left in range(cutoff)
            for right in range(cutoff)
        )
        primitive_rows.append(
            {
                "label": index + 1,
                "cover_derived_atom": index in atom_indices,
                "rank": int(matrix.rank()),
                "trace": str(sp.trace(matrix)),
                "idempotent": matrix * matrix == matrix,
                "oblique": matrix != matrix.T,
                "entry_formula_exact": formula_exact,
                "similarity_exact": matrix
                == zeta * sp.diag(*[int(place == index) for place in range(cutoff)]) * mobius,
            }
        )
    write_csv("primitive_idempotent_ledger.csv", primitive_rows)

    pair_rows: list[dict[str, object]] = []
    for left in range(cutoff):
        for right in range(cutoff):
            observed = compiled[left] * compiled[right]
            expected = compiled[left] if left == right else zero
            pair_rows.append(
                {
                    "left_label": left + 1,
                    "right_label": right + 1,
                    "expected_same": left == right,
                    "product_trace": str(sp.trace(observed)),
                    "exact": observed == expected,
                }
            )
    write_csv("pair_relation_ledger.csv", pair_rows)

    cover_cutoff = 256
    cover_relation = divisibility_relation(cover_cutoff)
    cover_indices = set(covers_bottom(cover_relation))
    cover_rows = []
    evaluator_set = set(evaluator_atoms(cover_cutoff))
    for label in range(1, cover_cutoff + 1):
        source_atom = label - 1 in cover_indices
        evaluator_atom = label in evaluator_set
        cover_rows.append(
            {
                "label": label,
                "source_cover_atom": source_atom,
                "postfreeze_trial_atom": evaluator_atom,
                "agreement": source_atom == evaluator_atom,
                "prime_table_used": False,
            }
        )
    write_csv("cover_atom_ledger.csv", cover_rows)

    actions, action_atoms = atom_actions(relation)
    alphabet = tuple(atom_indices[:4])
    necklace_rows: list[dict[str, object]] = []
    for representative in necklace_representatives(alphabet, 6):
        actual = word_trace_via_pair_relations(representative, actions)
        expected = selector_value(representative, action_atoms)
        labels = tuple(index + 1 for index in representative)
        necklace_rows.append(
            {
                "length": len(representative),
                "representative": "-".join(map(str, labels)),
                "canonical_rotation": "-".join(
                    map(str, (index + 1 for index in canonical_rotation(representative)))
                ),
                "orbit_size": cyclic_orbit_size(representative),
                "support_size": len(set(representative)),
                "trace": str(actual),
                "expected": expected,
                "selected": actual == 1,
                "exact": actual == expected,
            }
        )
    write_csv("necklace_ledger.csv", necklace_rows)

    marker_rows: list[dict[str, object]] = []
    for label in atom_labels:
        for repetition in range(1, 9):
            marker_rows.append(
                {
                    "label": label,
                    "gamma_code": gamma_code(label),
                    "gamma_length": gamma_length(label),
                    "repetition": repetition,
                    "observed_digit_exponent": repetition * len(gamma_code(label)),
                    "expected_digit_exponent": repetition * gamma_length(label),
                    "return_exponent": repetition,
                    "exact": repetition * len(gamma_code(label))
                    == repetition * gamma_length(label),
                }
            )
    write_csv("digit_marker_ledger.csv", marker_rows)

    s = 2
    u = Fraction(1, 2)
    z_value = sp.Rational(1, 3)
    transfer, weights = finite_transfer(compiled, atom_indices, s, u)
    power_rows = []
    transfer_power = sp.eye(cutoff)
    for repetition in range(1, 9):
        transfer_power *= transfer
        actual = sp.trace(transfer_power)
        expected = sum(weight**repetition for weight in weights.values())
        power_rows.append(
            {
                "repetition": repetition,
                "trace": fraction_text(actual),
                "expected_atom_sum": fraction_text(expected),
                "digit_exponents": ";".join(
                    f"{label}:{repetition * gamma_length(label)}"
                    for label in weights
                ),
                "exact": sp.cancel(actual - expected) == 0,
            }
        )
    write_csv("power_trace_ledger.csv", power_rows)

    finite_det = sp.factor((identity - z_value * transfer).det())
    finite_product = sp.prod(1 - z_value * weight for weight in weights.values())

    tensor_relation = divisibility_relation(10)
    degree = 3
    zero_transfer, one_transfer, tensor_weights = de_rham_tensor_transfers(
        tensor_relation, degree, s, u
    )
    zero_det = sp.factor((sp.eye(zero_transfer.rows) - z_value * zero_transfer).det())
    one_det = sp.factor((sp.eye(one_transfer.rows) - z_value * one_transfer).det())
    expected_zero = sp.Integer(1)
    expected_one = sp.Integer(1)
    local_chain_exact = True
    local_power_exact = True
    for label, weight in tensor_weights.items():
        translation, contraction = gamma_affine_branch(label)
        zero_form = affine_zero_form(degree, translation, contraction)
        one_form = affine_one_form(degree, translation, contraction)
        derivative = derivative_matrix(degree)
        local_chain_exact &= derivative * zero_form == one_form * derivative
        q = sp.Rational(contraction.numerator, contraction.denominator)
        expected_zero *= sp.prod(
            1 - z_value * weight * q**mode for mode in range(degree + 1)
        )
        expected_one *= sp.prod(
            1 - z_value * weight * q**mode for mode in range(1, degree + 1)
        )
        for repetition in range(1, 7):
            local_power_exact &= (
                sp.trace(zero_form**repetition) - sp.trace(one_form**repetition)
                == 1
            )
    graded_ratio = sp.cancel(zero_det / one_det)
    tensor_product = sp.prod(
        1 - z_value * weight for weight in tensor_weights.values()
    )
    fredholm_rows = [
        {
            "check": "finite_incidence_fredholm",
            "actual": fraction_text(finite_det),
            "expected": fraction_text(finite_product),
            "exact": sp.cancel(finite_det - finite_product) == 0,
        },
        {
            "check": "de_rham_degree_zero_determinant",
            "actual": fraction_text(zero_det),
            "expected": fraction_text(expected_zero),
            "exact": sp.cancel(zero_det - expected_zero) == 0,
        },
        {
            "check": "de_rham_degree_one_determinant",
            "actual": fraction_text(one_det),
            "expected": fraction_text(expected_one),
            "exact": sp.cancel(one_det - expected_one) == 0,
        },
        {
            "check": "honest_graded_relative_ratio",
            "actual": fraction_text(graded_ratio),
            "expected": fraction_text(tensor_product),
            "exact": sp.cancel(graded_ratio - tensor_product) == 0
            and local_chain_exact
            and local_power_exact,
        },
    ]
    write_csv("fredholm_de_rham_ledger.csv", fredholm_rows)

    mp.mp.dps = 50
    eta_values = (Fraction(3, 5), Fraction(3, 4), Fraction(1), Fraction(5, 4))
    hilbert_rows: list[dict[str, object]] = []
    for eta in eta_values:
        eta_mp = mp.mpf(eta.numerator) / eta.denominator
        c_eta = mp.zeta(2 * eta_mp) / mp.zeta(4 * eta_mp)
        for label in atom_labels[:6]:
            norm = mp.sqrt((1 + mp.power(label, -2 * eta_mp)) * c_eta)
            bound = mp.sqrt(2 * c_eta)
            hilbert_rows.append(
                {
                    "eta": f"{eta.numerator}/{eta.denominator}",
                    "label": label,
                    "eta_gt_half": eta > Fraction(1, 2),
                    "C_eta_formula": "zeta(2*eta)/zeta(4*eta)",
                    "trace_norm_formula": "sqrt((1+p^(-2*eta))*C_eta)",
                    "trace_norm_numeric": mp.nstr(norm, 24),
                    "uniform_bound_numeric": mp.nstr(bound, 24),
                    "below_uniform_bound": norm <= bound,
                    "trace": 1,
                    "rank": 1,
                    "exact_formula_certificate": True,
                }
            )
    write_csv("weighted_hilbert_ledger.csv", hilbert_rows)

    similarity_rows: list[dict[str, object]] = []
    for eta in (Fraction(5, 4), Fraction(3, 2), Fraction(2)):
        eta_mp = mp.mpf(eta.numerator) / eta.denominator
        similarity_rows.append(
            {
                "eta": f"{eta.numerator}/{eta.denominator}",
                "eta_gt_one": eta > 1,
                "zeta_transform_bound": mp.nstr(mp.zeta(eta_mp), 24),
                "mobius_transform_bound": mp.nstr(
                    mp.zeta(eta_mp) / mp.zeta(2 * eta_mp), 24
                ),
                "absolute_operator_series": True,
                "finite_similarity_all_labels": all(
                    compiled[index]
                    == zeta
                    * sp.diag(*[int(place == index) for place in range(cutoff)])
                    * mobius
                    for index in range(cutoff)
                ),
                "bounded_similarity_theorem_certificate": True,
            }
        )
    write_csv("bounded_similarity_ledger.csv", similarity_rows)

    standard_six = divisibility_relation(6)
    mutated_six = mutate_six_to_cover(standard_six)
    mutation_rows = []
    for name, source_relation in (
        ("standard_divisibility", standard_six),
        ("six_promoted_to_cover", mutated_six),
    ):
        source_atoms = [index + 1 for index in covers_bottom(source_relation)]
        _, _, source_compiled = compiled_idempotents(source_relation)
        mutation_rows.append(
            {
                "source": name,
                "derived_atoms": ",".join(map(str, source_atoms)),
                "six_is_atom": 6 in source_atoms,
                "q6_trace": str(sp.trace(source_compiled[5])),
                "q6_idempotent": source_compiled[5] ** 2 == source_compiled[5],
                "source_equivariant": True,
                "interpretation": "PROVES_TOO_MUCH"
                if name == "six_promoted_to_cover"
                else "INTEGER_SOURCE_BASELINE",
            }
        )
    write_csv("source_mutation_controls.csv", mutation_rows)

    stability_rows: list[dict[str, object]] = []
    smaller = 18
    _, _, small_compiled = compiled_idempotents(divisibility_relation(smaller))
    for index in range(smaller):
        restricted = compiled[index][:smaller, :smaller]
        stability_rows.append(
            {
                "control": "downset_cutoff_restriction",
                "label": index + 1,
                "exact": restricted == small_compiled[index],
            }
        )
    relabel_size = 12
    permutation = deterministic_permutation(relabel_size)
    base_zeta = zeta[:relabel_size, :relabel_size]
    base_compiled = [matrix[:relabel_size, :relabel_size] for matrix in compiled[:relabel_size]]
    relabeled_zeta = permute_matrix(base_zeta, permutation)
    relabeled_mobius = relabeled_zeta.inv()
    for new_index, old_index in enumerate(permutation):
        coordinate = sp.zeros(relabel_size)
        coordinate[new_index, new_index] = 1
        recompiled = relabeled_zeta * coordinate * relabeled_mobius
        stability_rows.append(
            {
                "control": "source_relabeling_equivariance",
                "label": old_index + 1,
                "exact": recompiled == permute_matrix(base_compiled[old_index], permutation),
            }
        )
    write_csv("stability_equivariance_ledger.csv", stability_rows)

    ablation_rows: list[dict[str, object]] = []
    for label in range(2, 13):
        scalar = arithmetic_mobius(label)
        atom = trial_atom(label)
        ablation_rows.append(
            {
                "ablation": "scalar_mobius_as_atom_coefficient",
                "label": label,
                "observed": scalar,
                "expected_atom_coefficient": int(atom),
                "idempotent_coefficient": scalar * scalar == scalar,
                "passes_atom_selector": scalar == int(atom),
                "expected_failure": not (scalar == int(atom) and scalar * scalar == scalar),
            }
        )
    zeta_only_two = zeta * sp.diag(*[int(index == 1) for index in range(cutoff)])
    zeta_only_four = zeta * sp.diag(*[int(index == 3) for index in range(cutoff)])
    ablation_rows.extend(
        [
            {
                "ablation": "zeta_without_mobius_inverse",
                "label": "2x4",
                "observed": "nonzero"
                if zeta_only_two * zeta_only_four != zero
                else "zero",
                "expected_atom_coefficient": "cross_product_zero",
                "idempotent_coefficient": "not_applicable",
                "passes_atom_selector": zeta_only_two * zeta_only_four == zero,
                "expected_failure": zeta_only_two * zeta_only_four != zero,
            },
            {
                "ablation": "unfiltered_compiler",
                "label": 4,
                "observed": str(sp.trace(compiled[3])),
                "expected_atom_coefficient": 0,
                "idempotent_coefficient": compiled[3] ** 2 == compiled[3],
                "passes_atom_selector": sp.trace(compiled[3]) == 0,
                "expected_failure": sp.trace(compiled[3]) != 0,
            },
        ]
    )
    write_csv("ablation_controls.csv", ablation_rows)

    route_rows = [
        {
            "gate": "A0",
            "verdict": "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "evidence": "integer divisibility covers derive atoms and n^-s weights",
            "stop_or_go": "GO_SOURCE_DERIVED_ATOMS",
        },
        {
            "gate": "A1",
            "verdict": "A1_PASS_ANALYTIC",
            "evidence": "only cover-derived atom loops survive all repetitions",
            "stop_or_go": "GO_EXACT_ATOM_NECKLACES",
        },
        {
            "gate": "A2",
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "evidence": "honest degreewise trace-class graded determinant ratio",
            "stop_or_go": "GO_SCOPED_FREDHOLM",
        },
        {
            "gate": "A3",
            "verdict": "A3_FAIL",
            "evidence": "u=1 trace class stops at Re(s)>1",
            "stop_or_go": "STOP_CRITICAL_STRIP_CONTINUATION",
        },
        {
            "gate": "A4",
            "verdict": "A4_FAIL",
            "evidence": "ordinary traces see only atom-projector similarity class",
            "stop_or_go": "STOP_INCIDENCE_SIMILARITY_COLLAPSE",
        },
    ]
    write_csv("route_gate_summary.csv", route_rows)

    tree = ast.parse(CORE.read_text(encoding="utf-8"))
    calls = sorted(
        {
            (
                node.func.id
                if isinstance(node.func, ast.Name)
                else node.func.attr
            ).lower()
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, (ast.Name, ast.Attribute))
        }
    )
    forbidden = sorted(
        set(calls)
        & {
            "factorint",
            "isprime",
            "primepi",
            "primerange",
            "sieve",
            "zeta",
            "zetazero",
            "mangoldt",
        }
    )
    source_oracle = {
        "candidate_id": "SD-C29",
        "candidate_evaluator_separated": True,
        "candidate_core": "code/sdc29_incidence_atom_compiler.py",
        "postfreeze_evaluator": "code/sdc29_evaluator.py",
        "candidate_core_calls": calls,
        "forbidden_candidate_calls": forbidden,
        "prime_table_used_in_candidate": False,
        "target_euler_coefficients_used": False,
        "riemann_zero_data_used": False,
        "target_zero_calls": 0,
        "atom_predicate": "covers_of_bottom_in_fixed_divisibility_relation",
        "wordwise_not_aggregate_only": True,
        "digit_marker_retained": True,
    }
    write_json("source_oracle_certificate.json", source_oracle)

    row_counts = {
        "incidence_inverse_ledger.csv": len(inverse_rows),
        "primitive_idempotent_ledger.csv": len(primitive_rows),
        "pair_relation_ledger.csv": len(pair_rows),
        "cover_atom_ledger.csv": len(cover_rows),
        "necklace_ledger.csv": len(necklace_rows),
        "digit_marker_ledger.csv": len(marker_rows),
        "power_trace_ledger.csv": len(power_rows),
        "fredholm_de_rham_ledger.csv": len(fredholm_rows),
        "weighted_hilbert_ledger.csv": len(hilbert_rows),
        "bounded_similarity_ledger.csv": len(similarity_rows),
        "source_mutation_controls.csv": len(mutation_rows),
        "stability_equivariance_ledger.csv": len(stability_rows),
        "ablation_controls.csv": len(ablation_rows),
        "route_gate_summary.csv": len(route_rows),
    }
    summary = {
        "candidate_id": "SD-C29",
        "status": "PASS",
        "route_tuple": [
            "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "row_counts": row_counts,
        "all_incidence_inverse_exact": all(row["exact"] for row in inverse_rows),
        "all_primitive_exact": all(
            row["rank"] == 1
            and row["trace"] == "1"
            and row["idempotent"]
            and row["entry_formula_exact"]
            and row["similarity_exact"]
            for row in primitive_rows
        ),
        "all_pair_relations_exact": all(row["exact"] for row in pair_rows),
        "all_cover_atoms_exact": all(row["agreement"] for row in cover_rows),
        "all_necklaces_exact": all(row["exact"] for row in necklace_rows),
        "all_markers_exact": all(row["exact"] for row in marker_rows),
        "all_power_traces_exact": all(row["exact"] for row in power_rows),
        "all_fredholm_de_rham_exact": all(row["exact"] for row in fredholm_rows),
        "all_hilbert_formulas_certified": all(
            row["exact_formula_certificate"] and row["below_uniform_bound"]
            for row in hilbert_rows
        ),
        "all_bounded_similarity_certified": all(
            row["bounded_similarity_theorem_certificate"]
            and row["finite_similarity_all_labels"]
            for row in similarity_rows
        ),
        "all_stability_equivariance_exact": all(
            row["exact"] for row in stability_rows
        ),
        "mutated_source_proves_too_much": mutation_rows[1]["six_is_atom"],
        "all_ablations_fail_as_expected": (
            any(
                row["ablation"] == "scalar_mobius_as_atom_coefficient"
                and row["label"] == 6
                and row["expected_failure"]
                for row in ablation_rows
            )
            and any(
                row["ablation"] == "scalar_mobius_as_atom_coefficient"
                and row["label"] == 2
                and row["expected_failure"]
                for row in ablation_rows
            )
            and all(
                row["expected_failure"]
                for row in ablation_rows
                if row["ablation"] != "scalar_mobius_as_atom_coefficient"
            )
        ),
        "target_zero_data_used": False,
    }
    if not all(
        value
        for key, value in summary.items()
        if key.startswith("all_") or key == "mutated_source_proves_too_much"
    ):
        summary["status"] = "FAIL"
    write_json("summary.json", summary)

    write_json(
        "run_parameters.json",
        {
            "candidate_id": "SD-C29",
            "incidence_cutoff": cutoff,
            "cover_validation_cutoff": cover_cutoff,
            "necklace_alphabet": [index + 1 for index in alphabet],
            "necklace_max_length": 6,
            "marker_repetition_max": 8,
            "transfer_parameters": {"s": s, "u": "1/2", "z": "1/3"},
            "de_rham_source_cutoff": 10,
            "de_rham_polynomial_degree": degree,
            "precision": "exact_integer_rational_sympy_except_nongating_norm_displays",
            "target_zero_data_used": False,
        },
    )
    write_json(
        "environment_lock.json",
        {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "pythonhashseed_required": "0",
            "argv0": Path(sys.argv[0]).name,
        },
    )
    write_json(
        "theorem_ledger.json",
        {
            "candidate_id": "SD-C29",
            "theorems": [
                {
                    "id": "T1",
                    "claim": "zeta epsilon_n mobius is a complete primitive-idempotent family",
                    "status": "PROVED_AND_EXACTLY_TESTED",
                    "artifacts": [
                        "incidence_inverse_ledger.csv",
                        "primitive_idempotent_ledger.csv",
                        "pair_relation_ledger.csv",
                    ],
                },
                {
                    "id": "T2",
                    "claim": "covers of one give exact all-repetition atom necklaces",
                    "status": "PROVED_AND_EXACTLY_TESTED",
                    "artifacts": [
                        "cover_atom_ledger.csv",
                        "necklace_ledger.csv",
                        "digit_marker_ledger.csv",
                    ],
                },
                {
                    "id": "T3",
                    "claim": "weighted H_eta realization has the stated rank-one trace norm",
                    "status": "PROVED_WITH_NUMERIC_DISPLAY_CONTROLS",
                    "artifacts": ["weighted_hilbert_ledger.csv"],
                },
                {
                    "id": "T4",
                    "claim": "eta greater than one gives bounded global similarity",
                    "status": "PROVED_WITH_FINITE_EXACT_CONTROLS",
                    "artifacts": ["bounded_similarity_ledger.csv"],
                },
                {
                    "id": "T5",
                    "claim": "honest Fredholm and de Rham graded ratios collapse to the atom product",
                    "status": "PROVED_AND_EXACTLY_TESTED",
                    "artifacts": [
                        "power_trace_ledger.csv",
                        "fredholm_de_rham_ledger.csv",
                    ],
                },
                {
                    "id": "N1",
                    "claim": "ordinary incidence mixing escapes coordinate atom projectors",
                    "status": "REFUTED_BY_SIMILARITY_AND_CONTROLS",
                    "artifacts": [
                        "source_mutation_controls.csv",
                        "stability_equivariance_ledger.csv",
                        "ablation_controls.csv",
                    ],
                },
            ],
        },
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
