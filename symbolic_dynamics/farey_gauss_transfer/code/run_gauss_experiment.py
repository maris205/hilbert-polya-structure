#!/usr/bin/env python3
"""Run the preregistered finite Gauss symbolic-orbit audit."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp

from gauss_orbits import (
    collision_examples,
    enumerate_orbits,
    format_complex,
    parse_complex_grid,
    primitive_necklace_count,
    signed_parity_sums,
    summarize,
)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def flatten_sum(prefix: str, values: dict[str, dict[str, float]], row: dict[str, object]) -> None:
    for s_key, parts in values.items():
        safe = s_key.replace("+", "p").replace("-", "m").replace(".", "d")
        row[f"{prefix}_{safe}_re"] = parts["re"]
        row[f"{prefix}_{safe}_im"] = parts["im"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    mp.mp.dps = int(config["precision_decimal_digits"])
    digit_cutoffs = [int(value) for value in config["digit_cutoffs"]]
    word_cutoffs = [int(value) for value in config["word_cutoffs"]]
    max_word = max(word_cutoffs)
    s_grid = parse_complex_grid(config["s_grid"])
    output = args.output
    output.mkdir(parents=True, exist_ok=True)

    ledgers: dict[int, list] = {}
    cutoff_rows: list[dict[str, object]] = []
    cutoff_summaries: dict[tuple[int, int], dict[str, dict[str, float]]] = {}
    length_rows: list[dict[str, object]] = []
    for digit_max in digit_cutoffs:
        print(f"enumerating alphabet 1..{digit_max}, word length <= {max_word}", flush=True)
        ledger = enumerate_orbits(tuple(range(1, digit_max + 1)), max_word)
        ledgers[digit_max] = ledger
        for length in range(1, max_word + 1):
            exact_length = [orbit for orbit in ledger if orbit.length == length]
            summary = summarize(exact_length, s_grid)
            length_rows.append({
                "digit_min": 1,
                "digit_max": digit_max,
                "word_length": length,
                "primitive_necklaces": summary["orbit_count"],
                "necklace_formula": primitive_necklace_count(digit_max, length),
                "formula_difference": int(summary["orbit_count"]) - primitive_necklace_count(digit_max, length),
                "self_reversal_count": summary["self_reversal_count"],
                "reversal_pair_count": summary["reversal_pair_count"],
                "trace_collision_group_count": summary["trace_collision_group_count"],
                "trace_collision_orbit_excess": summary["trace_collision_orbit_excess"],
                "nonreversal_collision_group_count": summary["nonreversal_collision_group_count"],
                "nonreversal_collision_class_excess": summary["nonreversal_collision_class_excess"],
                "cyclic_invariance_failures": summary["cyclic_invariance_failures"],
                "reversal_transpose_failures": summary["reversal_transpose_failures"],
                "repetition_matrix_failures": summary["repetition_matrix_failures"],
                "roof_min": summary["roof_min"],
                "roof_max": summary["roof_max"],
            })

        previous_sums: dict[str, dict[str, float]] | None = None
        for word_maximum in word_cutoffs:
            subset = [orbit for orbit in ledger if orbit.length <= word_maximum]
            summary = summarize(subset, s_grid)
            row: dict[str, object] = {
                "digit_min": 1,
                "digit_max": digit_max,
                "word_max": word_maximum,
                "primitive_necklaces": summary["orbit_count"],
                "even_orbit_count": summary["even_orbit_count"],
                "odd_orbit_count": summary["odd_orbit_count"],
                "self_reversal_count": summary["self_reversal_count"],
                "reversal_pair_count": summary["reversal_pair_count"],
                "trace_collision_group_count": summary["trace_collision_group_count"],
                "trace_collision_orbit_excess": summary["trace_collision_orbit_excess"],
                "nonreversal_collision_group_count": summary["nonreversal_collision_group_count"],
                "nonreversal_collision_class_excess": summary["nonreversal_collision_class_excess"],
                "cyclic_invariance_failures": summary["cyclic_invariance_failures"],
                "reversal_transpose_failures": summary["reversal_transpose_failures"],
                "repetition_matrix_failures": summary["repetition_matrix_failures"],
                "missing_reverse_orbits": summary["missing_reverse_orbits"],
                "roof_min": summary["roof_min"],
                "roof_max": summary["roof_max"],
            }
            flatten_sum("intrinsic_sum", summary["orbit_sum_intrinsic"], row)
            flatten_sum("additive_control_sum", summary["orbit_sum_additive_log1p_control"], row)
            for s_key, parts in summary["orbit_sum_intrinsic"].items():
                safe = s_key.replace("+", "p").replace("-", "m").replace(".", "d")
                if previous_sums is None:
                    row[f"successive_word_cutoff_drift_{safe}"] = "not_applicable"
                else:
                    delta = complex(parts["re"], parts["im"]) - complex(
                        previous_sums[s_key]["re"], previous_sums[s_key]["im"]
                    )
                    row[f"successive_word_cutoff_drift_{safe}"] = abs(delta)
            cutoff_rows.append(row)
            cutoff_summaries[(digit_max, word_maximum)] = summary["orbit_sum_intrinsic"]
            previous_sums = summary["orbit_sum_intrinsic"]

    for digit_index, digit_max in enumerate(digit_cutoffs):
        for word_maximum in word_cutoffs:
            row = next(
                item for item in cutoff_rows
                if item["digit_max"] == digit_max and item["word_max"] == word_maximum
            )
            for s in s_grid:
                s_key = format_complex(s)
                safe = s_key.replace("+", "p").replace("-", "m").replace(".", "d")
                if digit_index == 0:
                    row[f"successive_digit_cutoff_drift_{safe}"] = "not_applicable"
                else:
                    current = cutoff_summaries[(digit_max, word_maximum)][s_key]
                    previous = cutoff_summaries[(digit_cutoffs[digit_index - 1], word_maximum)][s_key]
                    row[f"successive_digit_cutoff_drift_{safe}"] = abs(
                        complex(current["re"], current["im"])
                        - complex(previous["re"], previous["im"])
                    )

    max_digit = max(digit_cutoffs)
    baseline = ledgers[max_digit]
    neighbor_alphabet = tuple(range(2, max_digit + 2))
    print(f"enumerating neighboring alphabet {neighbor_alphabet[0]}..{neighbor_alphabet[-1]}", flush=True)
    neighbor = enumerate_orbits(neighbor_alphabet, max_word)
    baseline_summary = summarize(baseline, s_grid)
    neighbor_summary = summarize(neighbor, s_grid)
    precision_audit: dict[str, object] = {}
    precision_sums: dict[int, dict[str, mp.mpc]] = {}
    for dps in config["precision_audit_decimal_digits"]:
        with mp.workdps(int(dps)):
            precision_sums[int(dps)] = {
                format_complex(s): mp.mpc(mp.fsum(
                    mp.exp(-mp.mpc(s) * (+orbit.roof)) for orbit in baseline
                ))
                for s in s_grid
            }
    high_dps = max(precision_sums)
    for dps, values in precision_sums.items():
        with mp.workdps(max(high_dps, mp.mp.dps)):
            precision_audit[str(dps)] = {
                s_key: {
                    "value_re": mp.nstr(value.real, int(dps)),
                    "value_im": mp.nstr(value.imag, int(dps)),
                    "absolute_drift_from_highest_precision": mp.nstr(
                        abs(value - precision_sums[high_dps][s_key]), 12
                    ),
                }
                for s_key, value in values.items()
            }

    control_rows: list[dict[str, object]] = []
    for label, ledger, summary in [
        ("baseline_digits_1_to_D_intrinsic_roof", baseline, baseline_summary),
        ("neighbor_digits_2_to_Dplus1_intrinsic_roof", neighbor, neighbor_summary),
    ]:
        parity = signed_parity_sums(ledger, s_grid)
        for s_key, values in parity.items():
            control_rows.append({
                "control": label,
                "s": s_key,
                "orbit_count": len(ledger),
                "unsigned_re": values["unsigned"]["re"],
                "unsigned_im": values["unsigned"]["im"],
                "even_only_re": values["even_only"]["re"],
                "even_only_im": values["even_only"]["im"],
                "odd_only_re": values["odd_only"]["re"],
                "odd_only_im": values["odd_only"]["im"],
                "parity_twist_re": values["parity_twist_even_minus_odd"]["re"],
                "parity_twist_im": values["parity_twist_even_minus_odd"]["im"],
            })
    for s_key, intrinsic in baseline_summary["orbit_sum_intrinsic"].items():
        additive = baseline_summary["orbit_sum_additive_log1p_control"][s_key]
        control_rows.append({
            "control": "same_words_additive_log1p_roof_control",
            "s": s_key,
            "orbit_count": len(baseline),
            "unsigned_re": additive["re"],
            "unsigned_im": additive["im"],
            "even_only_re": "not_applicable",
            "even_only_im": "not_applicable",
            "odd_only_re": "not_applicable",
            "odd_only_im": "not_applicable",
            "parity_twist_re": "not_applicable",
            "parity_twist_im": "not_applicable",
        })

    write_csv(output / "cutoff_table.csv", cutoff_rows)
    write_csv(output / "word_length_table.csv", length_rows)
    write_csv(output / "controls.csv", control_rows)
    orbit_digest = hashlib.sha256()
    with gzip.open(output / "exact_orbit_ledger.csv.gz", "wt", newline="", encoding="utf-8") as handle:
        columns = [
            "word", "word_length", "m00", "m01", "m10", "m11", "trace", "determinant",
            "intrinsic_roof_float64", "reverse_orbit", "self_reversal",
        ]
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for orbit in baseline:
            row = {
                "word": " ".join(map(str, orbit.word)),
                "word_length": orbit.length,
                "m00": orbit.matrix[0],
                "m01": orbit.matrix[1],
                "m10": orbit.matrix[2],
                "m11": orbit.matrix[3],
                "trace": orbit.trace,
                "determinant": orbit.determinant,
                "intrinsic_roof_float64": float(orbit.roof),
                "reverse_orbit": " ".join(map(str, orbit.reverse_orbit)),
                "self_reversal": orbit.reverse_orbit == orbit.word,
            }
            writer.writerow(row)
            orbit_digest.update(
                (f"{orbit.word}|{orbit.matrix}|{orbit.trace}|{orbit.determinant}\n").encode("ascii")
            )
    (output / "collision_examples.json").write_text(
        json.dumps(collision_examples(baseline, int(config["collision_example_limit"])), indent=2),
        encoding="utf-8",
    )

    summary = {
        "experiment_id": config["experiment_id"],
        "candidate_id": "SD-C04",
        "object": "finite primitive necklaces of the countable Gauss shift under explicit digit and word cutoffs",
        "matrix_convention": "A(a)=[[a,1],[1,0]], M(word)=A(a1)...A(an)",
        "intrinsic_roof": "T(word)=2 log(lambda_plus(M(word)))",
        "exact_fields": [
            "primitive word/necklace status", "2x2 monodromy entries", "trace", "determinant",
            "cyclic trace/determinant invariance", "reversal-transpose identity", "matrix repetition identity",
        ],
        "numerical_fields": ["roof evaluations", "finite orbit sums"],
        "precision_decimal_digits": mp.mp.dps,
        "precision_audit": precision_audit,
        "digit_cutoffs": digit_cutoffs,
        "word_cutoffs": word_cutoffs,
        "s_grid_predeclared": [format_complex(value) for value in s_grid],
        "controls": {
            "neighboring_digit": f"alphabet 2..{max_digit + 1}",
            "neighboring_roof": "same words with 2*sum(log(a+1)); predeclared, not a Gauss roof",
            "parity": "even-only, odd-only, and (-1)^word_length twist",
        },
        "baseline_max_cutoff": baseline_summary,
        "baseline_exact_orbit_ledger_sha256": orbit_digest.hexdigest(),
        "neighbor_digit_max_cutoff": neighbor_summary,
        "forbidden_data_audit": {
            "riemann_zero_table_loaded": False,
            "prime_table_used_to_define_grammar": False,
            "parameters_selected_from_target_zeros": False,
        },
        "claim_boundary": (
            "NUMERICAL_OBSERVATION for cutoff behavior. This is a finite primitive-orbit ledger only; "
            "it is not a Fredholm determinant evaluation, does not establish analytic continuation, "
            "and does not identify rational primes or prime powers with primitive Gauss cycles."
        ),
        "route_b_invocation_allowed": False,
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"wrote {len(cutoff_rows)} cutoff rows and {len(length_rows)} length rows to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
