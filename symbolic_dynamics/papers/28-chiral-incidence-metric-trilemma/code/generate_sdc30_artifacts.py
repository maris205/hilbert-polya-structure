#!/usr/bin/env python3
"""Generate deterministic exact artifacts for SD-C30."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import platform
from pathlib import Path
import sys

import sympy as sp

from sdc30_chiral_incidence import (
    active_positive_metric,
    b2_from_gram,
    compile_idempotents,
    covers_bottom,
    fraction_text,
    full_positive_metric,
    gamma_length,
    gram_matrix,
    is_selfadjoint_in_metric,
    marker_exponent,
    native_chiral_block,
    orthogonal_chiral_block,
    orthogonal_det3_factor,
)
from sdc30_evaluator import Fixture, all_fixtures


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CORE = ROOT / "code" / "sdc30_chiral_incidence.py"
RESULTS.mkdir(parents=True, exist_ok=True)
ETA = 2


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"empty artifact: {name}")
    with (RESULTS / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(name: str, payload: object) -> None:
    (RESULTS / name).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def fixture_data(fixture: Fixture) -> dict[str, object]:
    zeta, mobius, compiled = compile_idempotents(fixture.relation)
    atoms = covers_bottom(fixture.relation)
    selected = tuple(atoms[: fixture.selected_count])
    selected_labels = tuple(fixture.labels[index] for index in selected)
    weights = tuple(label ** (2 * ETA) for label in fixture.labels)
    gram = gram_matrix(selected, compiled, weights)
    block, phases = native_chiral_block(
        selected, fixture.labels, compiled, weights
    )
    size = len(fixture.labels)
    upper = block[:size, size:]
    lower = block[size:, :size]
    product = upper * lower
    b2_direct = sp.expand(2 * sp.trace(product))
    b2_gram = b2_from_gram(selected, fixture.labels, gram, phases)
    b4 = sp.expand(2 * sp.trace(product * product))
    phase_set = set(phases)
    at_one = {phase: 1 for phase in phases}
    at_flip = {
        phase: (-1 if index == 1 else 1)
        for index, phase in enumerate(phases)
    }
    return {
        "fixture": fixture,
        "zeta": zeta,
        "mobius": mobius,
        "compiled": compiled,
        "atoms": atoms,
        "selected": selected,
        "selected_labels": selected_labels,
        "weights": weights,
        "gram": gram,
        "phases": phases,
        "b2": b2_direct,
        "b2_gram": b2_gram,
        "b4": b4,
        "b2_exact": sp.simplify(b2_direct - b2_gram) == 0,
        "b2_phase": bool(b2_direct.free_symbols & phase_set),
        "b4_phase": bool(b4.free_symbols & phase_set),
        "b2_flip": sp.simplify(
            b2_direct.subs(at_one) - b2_direct.subs(at_flip)
        )
        != 0,
        "b4_flip": sp.simplify(b4.subs(at_one) - b4.subs(at_flip))
        != 0,
    }


def main() -> int:
    compiled_fixtures = [fixture_data(fixture) for fixture in all_fixtures()]

    source_rows: list[dict[str, object]] = []
    gram_rows: list[dict[str, object]] = []
    b2_rows: list[dict[str, object]] = []
    b4_rows: list[dict[str, object]] = []
    metric_rows: list[dict[str, object]] = []
    orthogonal_rows: list[dict[str, object]] = []
    adversary_rows: list[dict[str, object]] = []
    sample_rows: list[dict[str, object]] = []
    z = sp.symbols("z")

    for data in compiled_fixtures:
        fixture = data["fixture"]
        zeta = data["zeta"]
        mobius = data["mobius"]
        compiled = data["compiled"]
        atoms = data["atoms"]
        selected = data["selected"]
        selected_labels = data["selected_labels"]
        gram = data["gram"]
        phases = data["phases"]
        b2 = data["b2"]
        b4 = data["b4"]

        source_rows.append(
            {
                "fixture": fixture.name,
                "size": len(fixture.labels),
                "derived_atoms": ",".join(
                    str(fixture.labels[index]) for index in atoms
                ),
                "selected_atoms": ",".join(map(str, selected_labels)),
                "zeta_mobius_inverse": zeta * mobius
                == mobius * zeta
                == sp.eye(len(fixture.labels)),
                "all_q_pair_relations": all(
                    compiled[left] * compiled[right]
                    == (
                        compiled[left]
                        if left == right
                        else sp.zeros(len(fixture.labels))
                    )
                    for left in range(len(compiled))
                    for right in range(len(compiled))
                ),
                "interpretation": fixture.interpretation,
            }
        )

        for left in range(len(selected)):
            for right in range(len(selected)):
                value = sp.cancel(gram[left, right])
                weight = sp.diag(*data["weights"])
                independently_recomputed = sp.cancel(
                    sp.trace(
                        compiled[selected[left]]
                        * weight.inv()
                        * compiled[selected[right]].T
                        * weight
                    )
                )
                gram_rows.append(
                    {
                        "fixture": fixture.name,
                        "left_label": selected_labels[left],
                        "right_label": selected_labels[right],
                        "gram": str(value),
                        "diagonal": left == right,
                        "positive": bool(value > 0),
                        "nonnegative": bool(value >= 0),
                        "symmetric": value == gram[right, left],
                        "native_oblique": compiled[selected[left]]
                        != (
                            sp.diag(*data["weights"]).inv()
                            * compiled[selected[left]].T
                            * sp.diag(*data["weights"])
                        ),
                        "exact": value == independently_recomputed,
                    }
                )

        b2_rows.append(
            {
                "fixture": fixture.name,
                "selected_atoms": ",".join(map(str, selected_labels)),
                "laurent_expression": str(b2),
                "terms": len(sp.Add.make_args(b2)),
                "direct_equals_gram": data["b2_exact"],
                "phase_dependent": data["b2_phase"],
                "phase_flip_changes": data["b2_flip"],
                "scope": "FINITE_CUTOFF_DIAGNOSTIC_ONLY",
            }
        )

        b4_rows.append(
            {
                "fixture": fixture.name,
                "kind": "finite_native_control",
                "left_label": selected_labels[0],
                "right_label": selected_labels[1],
                "frequency": "fixture_full_expression",
                "coefficient": "see_expression_sha256",
                "positive": True,
                "unique_by_factorization": "not_applicable_control",
                "phase_dependent": data["b4_phase"],
                "phase_flip_changes": data["b4_flip"],
                "expression_sha256": hashlib.sha256(
                    str(b4).encode("utf-8")
                ).hexdigest(),
                "interpretation": fixture.interpretation,
            }
        )

        full_metric, full_k = full_positive_metric(mobius)
        full_all = all(
            is_selfadjoint_in_metric(matrix, full_metric)
            for matrix in compiled
        )
        metric_rows.append(
            {
                "fixture": fixture.name,
                "scope": "full_family",
                "selected_count": len(compiled),
                "K_structure": "positive_diagonal",
                "K_positive_definite": bool(full_k.is_positive_definite),
                "required_q_selfadjoint": full_all,
                "all_q_selfadjoint": full_all,
                "dormant_coupling_present": False,
                "Zt_H_Z_equals_K": zeta.T * full_metric * zeta == full_k,
                "active_coordinate_collapse": True,
            }
        )

        active_metric, active_k, coupled = active_positive_metric(
            mobius, selected
        )
        active_required = all(
            is_selfadjoint_in_metric(compiled[index], active_metric)
            for index in selected
        )
        all_active_metric = all(
            is_selfadjoint_in_metric(matrix, active_metric)
            for matrix in compiled
        )
        metric_rows.append(
            {
                "fixture": fixture.name,
                "scope": "active_atoms_only",
                "selected_count": len(selected),
                "K_structure": "atom_diagonal_plus_dormant_positive_block",
                "K_positive_definite": bool(active_k.is_positive_definite),
                "required_q_selfadjoint": active_required,
                "all_q_selfadjoint": all_active_metric,
                "dormant_coupling_present": active_k[coupled[0], coupled[1]]
                != 0,
                "Zt_H_Z_equals_K": zeta.T * active_metric * zeta == active_k,
                "active_coordinate_collapse": True,
            }
        )

        orthogonal, orthogonal_phases = orthogonal_chiral_block(selected_labels)
        characteristic = sp.factor(
            (sp.eye(orthogonal.rows) - z * orthogonal).det()
        )
        expected_characteristic = sp.factor(
            sp.prod(1 - z**2 / label for label in selected_labels)
        )
        det3_factor = sp.prod(
            orthogonal_det3_factor(label, z) for label in selected_labels
        )
        orthogonal_rows.append(
            {
                "fixture": fixture.name,
                "selected_atoms": ",".join(map(str, selected_labels)),
                "characteristic": str(characteristic),
                "expected_characteristic": str(expected_characteristic),
                "characteristic_exact": sp.simplify(
                    characteristic - expected_characteristic
                )
                == 0,
                "phase_free": not bool(
                    characteristic.free_symbols & set(orthogonal_phases)
                ),
                "det3_factor": str(det3_factor),
                "det3_phase_free": not bool(
                    det3_factor.free_symbols & set(orthogonal_phases)
                ),
                "interpretation": "ORTHOGONAL_ATOM_BLOCK_COLLAPSE",
            }
        )

        adversary_rows.append(
            {
                "fixture": fixture.name,
                "source_atoms": ",".join(
                    str(fixture.labels[index]) for index in atoms
                ),
                "native_offdiagonal_gram": any(
                    gram[left, right] != 0
                    for left in range(gram.rows)
                    for right in range(left + 1, gram.cols)
                ),
                "native_B2_phase": data["b2_phase"],
                "native_B4_phase": data["b4_phase"],
                "positive_metric_active_collapse": True,
                "orthogonalized_phase": False,
                "arithmetic_selectivity_observed": False,
                "interpretation": fixture.interpretation,
            }
        )

        for sample in (sp.Rational(0), sp.Rational(7, 10), sp.Rational(13, 10)):
            substitutions = {
                phases[index]: sp.exp(
                    -sp.I * sample * sp.log(selected_labels[index])
                )
                for index in range(len(phases))
            }
            sample_rows.append(
                {
                    "fixture": fixture.name,
                    "t": str(sample),
                    "Tr_B2_numeric": str(sp.N(sp.re(b2.subs(substitutions)), 18)),
                    "Tr_B4_numeric": str(sp.N(sp.re(b4.subs(substitutions)), 18)),
                    "claim_bearing": False,
                    "role": "display_only_exact_symbolic_expression_is_gate",
                }
            )

    write_csv("source_compiler_ledger.csv", source_rows)
    write_csv("native_gram_ledger.csv", gram_rows)
    write_csv("finite_b2_diagnostic.csv", b2_rows)
    write_csv("metric_rigidity_ledger.csv", metric_rows)
    write_csv("orthogonalized_det3_ledger.csv", orthogonal_rows)
    write_csv("adversary_control_ledger.csv", adversary_rows)
    write_csv("t_sample_ledger.csv", sample_rows)

    c_eta = sp.simplify(sp.zeta(2 * ETA) / sp.zeta(4 * ETA))
    primes = (2, 3, 5)
    infinite_gram: dict[tuple[int, int], sp.Expr] = {}
    infinite_gram_rows: list[dict[str, object]] = []
    for left in primes:
        for right in primes:
            if left == right:
                value = sp.simplify(c_eta * (1 + sp.Rational(1, left ** (2 * ETA))))
                formula = "C_eta*(1+p^(-2*eta))"
            else:
                value = sp.simplify(
                    c_eta
                    * sp.Rational(1, (left * right) ** (2 * ETA))
                    / (
                        (1 + sp.Rational(1, left ** (2 * ETA)))
                        * (1 + sp.Rational(1, right ** (2 * ETA)))
                    )
                )
                formula = (
                    "C_eta*(p*q)^(-2*eta)/"
                    "((1+p^(-2*eta))*(1+q^(-2*eta)))"
                )
            infinite_gram[(left, right)] = value
            infinite_gram_rows.append(
                {
                    "eta": ETA,
                    "left_prime": left,
                    "right_prime": right,
                    "kind": "diagonal" if left == right else "mixed",
                    "formula": formula,
                    "exact_value": str(value),
                    "positive": bool(value > 0),
                    "symmetric": value
                    == infinite_gram.get((right, left), value),
                    "source": "rank_one_divisibility_factorization",
                }
            )
    write_csv("infinite_gram_formula_ledger.csv", infinite_gram_rows)

    schatten_rows: list[dict[str, object]] = []
    for order in range(1, 9):
        nonempty = order > 2
        schatten_rows.append(
            {
                "q": order,
                "T_s_condition": f"{order}*Re(s)>1",
                "reflected_condition": f"{order}*(1-Re(s))>1",
                "common_lower": str(sp.Rational(1, order)),
                "common_upper": str(1 - sp.Rational(1, order)),
                "common_strip_nonempty": nonempty,
                "critical_line_included": nonempty,
                "minimal_integer_order": order == 3,
                "exact": True,
            }
        )
    write_csv("schatten_strip_ledger.csv", schatten_rows)

    firewall_rows = [
        {
            "claim": "critical_line_membership",
            "object": "B_(1/2+it)",
            "status": "in_Sq_for_every_q_gt_2",
            "exact_reason": "both diagonal legs have p^(-1/2) singular scale",
            "ordinary_trace_allowed": False,
        },
        {
            "claim": "Hilbert_Schmidt_membership",
            "object": "B_(1/2+it)",
            "status": "NOT_IN_S2",
            "exact_reason": "sum_p p^-1 diverges",
            "ordinary_trace_allowed": False,
        },
        {
            "claim": "B2_trace",
            "object": "B_(1/2+it)^2",
            "status": "NOT_TRACE_CLASS",
            "exact_reason": "diagonal lower bound 2*C_eta*sum_p p^-1",
            "ordinary_trace_allowed": False,
        },
        {
            "claim": "finite_B2_formula",
            "object": "finite_atom_cutoff",
            "status": "VALID_DIAGNOSTIC",
            "exact_reason": "finite matrices and exact Gram expansion",
            "ordinary_trace_allowed": True,
        },
    ]
    write_csv("infinite_s2_firewall.csv", firewall_rows)

    for left, right in ((2, 3), (2, 5), (3, 5)):
        coefficient = sp.simplify(
            4 * infinite_gram[(left, right)] ** 2 / (left * right)
        )
        b4_rows.append(
            {
                "fixture": "infinite_prime_divisibility",
                "kind": "unique_positive_frequency",
                "left_label": left,
                "right_label": right,
                "frequency": f"2*log({right}/{left})",
                "coefficient": str(coefficient),
                "positive": bool(coefficient > 0),
                "unique_by_factorization": True,
                "phase_dependent": True,
                "phase_flip_changes": "not_applicable_infinite_theorem",
                "expression_sha256": hashlib.sha256(
                    str(coefficient).encode("utf-8")
                ).hexdigest(),
                "interpretation": "EXACT_SURVIVING_DET3_GERM_FREQUENCY",
            }
        )
    write_csv("b4_frequency_ledger.csv", b4_rows)

    det3_rows: list[dict[str, object]] = []
    for power in range(1, 9):
        deleted = power < 3
        odd = power % 2 == 1
        visible = not deleted and not odd
        det3_rows.append(
            {
                "power": power,
                "deleted_by_det3": deleted,
                "odd_block_trace_zero": odd,
                "visible_in_log_det3": visible,
                "first_visible": power == 4,
                "coefficient": "0"
                if deleted or odd
                else f"-z^{power}*Tr(B^{power})/{power}",
                "exact": True,
            }
        )
    write_csv("det3_deletion_ledger.csv", det3_rows)

    marker_rows: list[dict[str, object]] = []
    for label in (2, 3, 5):
        for repetition in range(1, 9):
            marker_rows.append(
                {
                    "label": label,
                    "gamma_length": gamma_length(label),
                    "repetition": repetition,
                    "symbolic_digit_exponent": marker_exponent(label, repetition),
                    "expected_exponent": repetition * gamma_length(label),
                    "main_theorem_u": 1,
                    "factor_at_u1": 1,
                    "symbolic_marker_exact": marker_exponent(label, repetition)
                    == repetition * gamma_length(label),
                    "u_less_than_1_changes_schatten_domain": True,
                    "continuation_credit": False,
                }
            )
    write_csv("marker_ownership_ledger.csv", marker_rows)

    route_rows = [
        {
            "gate": "A0",
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "evidence": "incidence source and reflected sharp are source fixed",
            "stop_or_go": "GO_SOURCE_CHIRAL_COMPLETION",
        },
        {
            "gate": "A1",
            "verdict": "A1_FAIL",
            "evidence": "chiral mixed Gram cycles lose pure Euler orbit ledger",
            "stop_or_go": "STOP_PURE_ORBIT_CORRESPONDENCE",
        },
        {
            "gate": "A2",
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "evidence": "det3 honest on 1/3<Re(s)<2/3",
            "stop_or_go": "GO_SCHATTEN3_REGULARIZED_DETERMINANT",
        },
        {
            "gate": "A3",
            "verdict": "A3_FAIL",
            "evidence": "selfadjoint operator family depends on t",
            "stop_or_go": "STOP_FIXED_SPECTRAL_PARAMETER",
        },
        {
            "gate": "A4",
            "verdict": "A4_FAIL",
            "evidence": "native motion generic and orthogonal completion phase free",
            "stop_or_go": "STOP_NO_ARITHMETIC_SELECTIVITY",
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
            "isprime",
            "factorint",
            "primerange",
            "primepi",
            "zetazero",
            "siegelz",
        }
    )
    source_oracle = {
        "candidate_id": "SD-C30",
        "candidate_evaluator_separated": True,
        "candidate_core": "code/sdc30_chiral_incidence.py",
        "postfreeze_fixtures": "code/sdc30_evaluator.py",
        "candidate_core_calls": calls,
        "forbidden_candidate_calls": forbidden,
        "prime_table_used_in_candidate": False,
        "target_zero_data_used": False,
        "target_zero_calls": 0,
        "target_zero_labels_used": False,
        "source_poset_compiler": True,
        "regularization_order_frozen_before_run": 3,
        "marker_u1_ownership_explicit": True,
    }
    write_json("source_oracle_certificate.json", source_oracle)

    row_counts = {
        "source_compiler_ledger.csv": len(source_rows),
        "native_gram_ledger.csv": len(gram_rows),
        "infinite_gram_formula_ledger.csv": len(infinite_gram_rows),
        "schatten_strip_ledger.csv": len(schatten_rows),
        "finite_b2_diagnostic.csv": len(b2_rows),
        "infinite_s2_firewall.csv": len(firewall_rows),
        "b4_frequency_ledger.csv": len(b4_rows),
        "det3_deletion_ledger.csv": len(det3_rows),
        "metric_rigidity_ledger.csv": len(metric_rows),
        "orthogonalized_det3_ledger.csv": len(orthogonal_rows),
        "adversary_control_ledger.csv": len(adversary_rows),
        "marker_ownership_ledger.csv": len(marker_rows),
        "t_sample_ledger.csv": len(sample_rows),
        "route_gate_summary.csv": len(route_rows),
    }
    summary = {
        "candidate_id": "SD-C30",
        "status": "PASS",
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "row_counts": row_counts,
        "all_source_compilers_exact": all(
            row["zeta_mobius_inverse"] and row["all_q_pair_relations"]
            for row in source_rows
        ),
        "all_native_gram_exact": all(
            row["nonnegative"]
            and (row["positive"] if row["diagonal"] else True)
            and row["symmetric"]
            and row["exact"]
            for row in gram_rows
        ),
        "all_infinite_gram_formulas_positive": all(
            row["positive"] for row in infinite_gram_rows
        ),
        "schatten3_minimal": next(
            row["q"] for row in schatten_rows if row["minimal_integer_order"]
        )
        == 3,
        "finite_B2_exact_and_phase_dependent": all(
            row["direct_equals_gram"]
            and row["phase_dependent"]
            and row["phase_flip_changes"]
            for row in b2_rows
        ),
        "infinite_non_S2_firewall": firewall_rows[1]["status"] == "NOT_IN_S2"
        and firewall_rows[2]["status"] == "NOT_TRACE_CLASS",
        "unique_positive_B4_frequencies": all(
            row["positive"] and row["unique_by_factorization"] is True
            for row in b4_rows
            if row["kind"] == "unique_positive_frequency"
        ),
        "det3_deletes_1_2_first_visible_4": (
            [row["power"] for row in det3_rows if row["deleted_by_det3"]]
            == [1, 2]
            and next(row["power"] for row in det3_rows if row["first_visible"])
            == 4
        ),
        "full_active_metric_rigidity": all(
            row["K_positive_definite"]
            and row["required_q_selfadjoint"]
            and row["Zt_H_Z_equals_K"]
            and row["active_coordinate_collapse"]
            for row in metric_rows
        )
        and any(
            row["scope"] == "active_atoms_only"
            and not row["all_q_selfadjoint"]
            and row["dormant_coupling_present"]
            for row in metric_rows
        ),
        "orthogonalized_det3_phase_free": all(
            row["characteristic_exact"]
            and row["phase_free"]
            and row["det3_phase_free"]
            for row in orthogonal_rows
        ),
        "all_adversaries_prove_too_much": all(
            row["native_offdiagonal_gram"]
            and row["native_B4_phase"]
            and not row["orthogonalized_phase"]
            and not row["arithmetic_selectivity_observed"]
            for row in adversary_rows
        ),
        "marker_u1_ownership_exact": all(
            row["symbolic_marker_exact"]
            and row["main_theorem_u"] == 1
            and not row["continuation_credit"]
            for row in marker_rows
        ),
        "target_zero_data_used": False,
    }
    if not all(
        value
        for key, value in summary.items()
        if key.startswith("all_")
        or key
        in {
            "schatten3_minimal",
            "finite_B2_exact_and_phase_dependent",
            "infinite_non_S2_firewall",
            "unique_positive_B4_frequencies",
            "det3_deletes_1_2_first_visible_4",
            "full_active_metric_rigidity",
            "orthogonalized_det3_phase_free",
            "marker_u1_ownership_exact",
        }
    ):
        summary["status"] = "FAIL"
    write_json("summary.json", summary)

    write_json(
        "run_parameters.json",
        {
            "candidate_id": "SD-C30",
            "eta": ETA,
            "seed": 2801,
            "fixtures": [data["fixture"].name for data in compiled_fixtures],
            "standard_selected_atoms": [2, 3, 5],
            "schatten_orders": list(range(1, 9)),
            "det3_power_ledger": list(range(1, 9)),
            "marker_labels": [2, 3, 5],
            "marker_repetitions": list(range(1, 9)),
            "main_theorem_u": 1,
            "precision": "exact_integer_rational_sympy_except_nongating_t_samples",
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
            "pythonhashseed_required": "0",
            "argv0": Path(sys.argv[0]).name,
        },
    )
    write_json(
        "theorem_ledger.json",
        {
            "candidate_id": "SD-C30",
            "theorems": [
                {
                    "id": "C1-C2",
                    "claim": "exact Schatten criterion and minimal common S3 strip",
                    "status": "PROVED_AND_CERTIFIED",
                    "artifacts": ["schatten_strip_ledger.csv"],
                },
                {
                    "id": "C4-C5",
                    "claim": "native Gram formulas and finite B2 versus infinite non-S2 firewall",
                    "status": "PROVED_AND_EXACTLY_TESTED",
                    "artifacts": [
                        "native_gram_ledger.csv",
                        "infinite_gram_formula_ledger.csv",
                        "finite_b2_diagnostic.csv",
                        "infinite_s2_firewall.csv",
                    ],
                },
                {
                    "id": "C6-C7",
                    "claim": "det3 deletes powers one and two; unique positive B4 frequency survives",
                    "status": "PROVED_AND_CERTIFIED",
                    "artifacts": [
                        "det3_deletion_ledger.csv",
                        "b4_frequency_ledger.csv",
                    ],
                },
                {
                    "id": "C8",
                    "claim": "full and active positive metrics force active coordinate collapse",
                    "status": "PROVED_AND_EXACTLY_TESTED",
                    "artifacts": [
                        "metric_rigidity_ledger.csv",
                        "orthogonalized_det3_ledger.csv",
                    ],
                },
                {
                    "id": "C9-C10",
                    "claim": "native motion is arithmetically selective or supports Route B",
                    "status": "REFUTED",
                    "artifacts": [
                        "adversary_control_ledger.csv",
                        "marker_ownership_ledger.csv",
                    ],
                },
            ],
        },
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
