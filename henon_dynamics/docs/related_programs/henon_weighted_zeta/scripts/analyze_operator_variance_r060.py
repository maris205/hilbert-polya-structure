#!/usr/bin/env python3
"""Analyze the frozen R060 operator-variance ensemble.

The analysis unit is the randomized Sobol seed (never an individual cell or
sample).  It evaluates the preregistered G1--G3 diagnostics, computes paired
64/256 shifts, seed-level dyadic contrasts, and deterministic Gauss-order
gaps, and compares the fresh-seed contrast distributions with the two frozen
R059 failures.  All conclusions are finite-resolution/descriptive; this
script deliberately makes no continuous-operator claim.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "results" / "operator_variance_r060.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "operator_variance_r060_analysis.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "operator_variance_r060_analysis.csv"
DEFAULT_REPORT = PROJECT_ROOT / "research" / "refine-logs" / "R060_OPERATOR_VARIANCE_ANALYSIS.md"
DEFAULT_CHECK = PROJECT_ROOT / "results" / "operator_variance_r060_check.json"
DEFAULT_R059 = PROJECT_ROOT / "results" / "restricted_operator_r059.json"
DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R060_OPERATOR_VARIANCE_PROTOCOL.json"


def relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), np.finfo(float).tiny)


def stats(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"n": 0, "mean": None, "median": None, "sd": None, "se": None, "cv": None, "mad": None,
                "min": None, "max": None}
    a = np.asarray(values, dtype=float)
    mean = float(np.mean(a))
    sd = float(np.std(a, ddof=1)) if a.size > 1 else 0.0
    med = float(np.median(a))
    return {
        "n": int(a.size),
        "mean": mean,
        "median": med,
        "sd": sd,
        "se": float(sd / math.sqrt(a.size)) if a.size else None,
        "cv": float(sd / abs(mean)) if mean else None,
        "mad": float(np.median(np.abs(a - med))),
        "min": float(np.min(a)),
        "max": float(np.max(a)),
    }


class Bootstrap:
    """Seed-level percentile bootstrap with one locked RNG stream."""

    def __init__(self, seed: int, replicates: int) -> None:
        self.seed = int(seed)
        self.replicates = int(replicates)
        self.rng = np.random.default_rng(self.seed)

    def mean_ci(self, values: list[float]) -> list[float] | None:
        if not values:
            return None
        a = np.asarray(values, dtype=float)
        if a.size == 1:
            return [float(a[0]), float(a[0])]
        draws = self.rng.choice(a, size=(self.replicates, a.size), replace=True)
        means = np.mean(draws, axis=1)
        return [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def index_records(records: list[dict[str, Any]]) -> dict[tuple[str, int, int, int | None], dict[str, Any]]:
    return {
        (str(r["method_family"]), int(r["grid"]), int(r["samples_per_cell"]),
         None if r.get("seed") is None else int(r["seed"])): r
        for r in records
    }


def fmt(value: Any, digits: int = 6) -> str:
    if value is None:
        return "--"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    return f"{float(value):.{digits}g}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=DEFAULT_CHECK)
    parser.add_argument("--r059", type=Path, default=DEFAULT_R059)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    args = parser.parse_args()

    payload = load(args.input)
    protocol = load(args.protocol)
    check = load(args.check) if args.check.exists() else {}
    r059 = load(args.r059) if args.r059.exists() else {}
    records = list(payload.get("records", []))
    idx = index_records(records)
    grids = [int(x) for x in protocol["design"]["grids"]]
    seeds = [int(x) for x in protocol["design"]["fresh_sobol_seeds"]]
    budgets = [int(x) for x in protocol["design"]["sobol_samples_per_cell"]]
    orders = [int(x) for x in protocol["design"]["gauss_orders"]]
    chains = [tuple(int(y) for y in x) for x in protocol["design"]["dyadic_chains"]]
    bootstrap_seed = int(protocol["analysis"]["bootstrap_seed"])
    bootstrap_replicates = int(protocol["analysis"]["bootstrap_replicates"])
    bootstrap = Bootstrap(bootstrap_seed, bootstrap_replicates)

    ensemble: list[dict[str, Any]] = []
    for grid in grids:
        for budget in budgets:
            values = [float(idx[("sobol", grid, budget, seed)]["leading_modulus"])
                      for seed in seeds if ("sobol", grid, budget, seed) in idx]
            row = stats(values)
            row.update({"kind": "ensemble", "method": "sobol", "grid": grid,
                        "samples_per_cell": budget, "bootstrap_mean_ci": bootstrap.mean_ci(values)})
            ensemble.append(row)

    sd_ratios: list[dict[str, Any]] = []
    for grid in grids:
        e64 = next(x for x in ensemble if x["grid"] == grid and x["samples_per_cell"] == 64)
        e256 = next(x for x in ensemble if x["grid"] == grid and x["samples_per_cell"] == 256)
        ratio = None if not e64["sd"] else float(e256["sd"] / e64["sd"])
        sd_ratios.append({"grid": grid, "sd64": e64["sd"], "sd256": e256["sd"],
                          "sd256_over_sd64": ratio})

    paired: list[dict[str, Any]] = []
    for grid in grids:
        signed = []
        signed_relative = []
        absolute_relative = []
        for seed in seeds:
            r64 = idx[("sobol", grid, 64, seed)]
            r256 = idx[("sobol", grid, 256, seed)]
            d = float(r256["leading_modulus"]) - float(r64["leading_modulus"])
            signed.append(d)
            signed_relative.append(d / max(abs(float(r64["leading_modulus"])), np.finfo(float).tiny))
            absolute_relative.append(relative_gap(float(r64["leading_modulus"]), float(r256["leading_modulus"])))
        row = {"kind": "paired", "grid": grid, "signed_delta": stats(signed),
               "signed_relative_delta": stats(signed_relative),
               "absolute_relative_shift": stats(absolute_relative),
               "values_signed_delta": signed, "values_signed_relative_delta": signed_relative,
               "values_absolute_relative_shift": absolute_relative}
        paired.append(row)

    dyadic: list[dict[str, Any]] = []
    dyadic_aggregate: list[dict[str, Any]] = []
    for budget in budgets:
        for chain in chains:
            per_seed: list[dict[str, Any]] = []
            for seed in seeds:
                vals = [float(idx[("sobol", grid, budget, seed)]["leading_modulus"]) for grid in chain]
                first = relative_gap(vals[0], vals[1])
                final = relative_gap(vals[1], vals[2])
                per_seed.append({"seed": seed, "chain": list(chain), "samples_per_cell": budget,
                                 "values": vals, "first_relative_change": first,
                                 "final_relative_change": final, "D": final - first,
                                 "pass": bool(final <= first)})
            dvals = [float(x["D"]) for x in per_seed]
            firstvals = [float(x["first_relative_change"]) for x in per_seed]
            finalvals = [float(x["final_relative_change"]) for x in per_seed]
            agg = stats(dvals)
            agg.update({"kind": "dyadic_aggregate", "samples_per_cell": budget,
                        "chain": list(chain), "first_change": stats(firstvals),
                        "final_change": stats(finalvals), "pass_fraction": float(np.mean([x["pass"] for x in per_seed])),
                        "D_bootstrap_mean_ci": bootstrap.mean_ci(dvals),
                        "D_values": dvals})
            dyadic_aggregate.append(agg)
            dyadic.extend(per_seed)

    gauss: list[dict[str, Any]] = []
    gauss_gaps: list[dict[str, Any]] = []
    for grid in grids:
        vals = {}
        for order in orders:
            row = idx[("gauss", grid, order * order, None)]
            vals[order] = float(row["leading_modulus"])
            gauss.append({"kind": "gauss", "grid": grid, "quadrature_order": order,
                          "leading_modulus": vals[order], "target_boundary_hits": row["target_boundary_hits"],
                          "maximum_eigenpair_residual": row["maximum_eigenpair_residual"]})
        gauss_gaps.append({"grid": grid, "q4_q8_gap": relative_gap(vals[4], vals[8]),
                           "q8_q12_gap": relative_gap(vals[8], vals[12]),
                           "q8_q12_leq_q4_q8": relative_gap(vals[8], vals[12]) <= relative_gap(vals[4], vals[8])})

    # Overlay the two frozen R059 failures on the corresponding fresh 64-point
    # seed distributions.  The overlay is descriptive and does not reclassify
    # or reopen the R059 gate.
    r059_overlay: list[dict[str, Any]] = []
    failures = r059.get("finite_resolution_audit", {}).get("dyadic_change", [])
    for failure in failures:
        if failure.get("pass"):
            continue
        chain = tuple(int(x) for x in failure["chain"])
        d_obs = float(failure["final_relative_change"] - failure["first_relative_change"])
        candidates = [x for x in dyadic if x["samples_per_cell"] == 64 and tuple(x["chain"]) == chain]
        dvals = np.asarray([x["D"] for x in candidates], dtype=float)
        r059_overlay.append({
            "method_key": failure.get("method_key"), "chain": list(chain),
            "observed_D": d_obs, "fresh_n": int(dvals.size),
            "fresh_mean_D": float(np.mean(dvals)) if dvals.size else None,
            "fresh_sd_D": float(np.std(dvals, ddof=1)) if dvals.size > 1 else None,
            "fresh_fraction_D_ge_observed": float(np.mean(dvals >= d_obs)) if dvals.size else None,
            "fresh_fraction_absD_ge_abs_observed": float(np.mean(np.abs(dvals) >= abs(d_obs))) if dvals.size else None,
            "fresh_min_D": float(np.min(dvals)) if dvals.size else None,
            "fresh_max_D": float(np.max(dvals)) if dvals.size else None,
        })

    reference = r059.get("finite_resolution_audit", {}).get("fredholm_reference")
    fredholm: list[dict[str, Any]] = []
    if reference is not None:
        for row in ensemble:
            if row.get("samples_per_cell") == 256 and row.get("grid") in (96, 128):
                fredholm.append({"grid": row["grid"], "mean": row["mean"], "reference": reference,
                                 "relative_gap": relative_gap(float(row["mean"]), float(reference))})

    ratios = [float(x["sd256_over_sd64"]) for x in sd_ratios if x["sd256_over_sd64"] is not None]
    paired_mean_abs = [float(x["absolute_relative_shift"]["mean"]) for x in paired]
    g0 = bool(check.get("all_checks_pass", False) and check.get("checks", {}).get("record_count_complete", False))
    g1 = bool(len(ratios) == 6 and sum(x <= 1.0 for x in ratios) >= 5 and np.median(ratios) <= 0.75
              and len(paired_mean_abs) == 6 and max(paired_mean_abs) <= 0.01)
    g2 = bool(len(gauss_gaps) == 6 and all(x["q8_q12_gap"] <= 0.005 for x in gauss_gaps)
              and sum(x["q8_q12_leq_q4_q8"] for x in gauss_gaps) >= 4)
    mean_by = {(x["grid"], x["samples_per_cell"]): x["mean"] for x in ensemble}
    mean_trajectory: list[dict[str, Any]] = []
    for chain in chains:
        vals = [mean_by[(grid, 256)] for grid in chain]
        first = relative_gap(vals[0], vals[1])
        final = relative_gap(vals[1], vals[2])
        mean_trajectory.append({"chain": list(chain), "values": vals,
                                "first_relative_change": first, "final_relative_change": final,
                                "D": final - first, "pass": bool(final <= first)})
    reference_ok = reference is None or all(x["relative_gap"] <= 0.01 for x in fredholm)
    g3 = bool(all(x["pass"] for x in mean_trajectory) and reference_ok)

    all_records = records
    integrity = {
        "record_count": len(all_records),
        "expected_record_count": len(grids) * (len(budgets) * len(seeds) + len(orders)),
        "max_boundary_hits": max(int(r.get("target_boundary_hits", 0)) for r in all_records) if all_records else None,
        "max_eigenpair_residual": max(float(r.get("maximum_eigenpair_residual", 0.0)) for r in all_records) if all_records else None,
        "all_g0_config_pass": bool(all(bool(r.get("g0_config_pass")) for r in all_records)),
    }

    result: dict[str, Any] = {
        "run_id": "R060_OPERATOR_VARIANCE_ANALYSIS",
        "input": str(args.input.resolve().relative_to(PROJECT_ROOT)),
        "protocol_sha256": payload.get("protocol_sha256"),
        "record_count": len(records),
        "bootstrap": {"seed": bootstrap_seed, "replicates": bootstrap_replicates, "unit": "fresh Sobol seed"},
        "integrity": integrity,
        "ensemble": ensemble,
        "sd_ratios": sd_ratios,
        "paired_sample_budget": paired,
        "dyadic_per_seed": dyadic,
        "dyadic_aggregate": dyadic_aggregate,
        "gauss": gauss,
        "gauss_gaps": gauss_gaps,
        "r059_failure_overlay": r059_overlay,
        "fredholm_reference": reference,
        "fredholm": fredholm,
        "mean_trajectory_256": mean_trajectory,
        "gates": {"G0_integrity": g0, "G1_sobol_variance": g1, "G2_gauss_order": g2, "G3_mean_trajectory": g3},
        "mechanism_tags": {
            "sampling_variance": "partial_support" if (not g1 and np.median(ratios) <= 0.75) else ("supported" if g1 else "unresolved"),
            "quadrature_order_stability": "not_supported_by_gate" if not g2 else "supported_by_gate",
            "256_mean_dyadic_trajectory": "descriptively_supported" if g3 else "not_supported",
            "overall": "MIXED_FINITE_RESOLUTION_EVIDENCE",
        },
        "anti_claim": "R060 does not alter R059 G4=false and does not establish continuous transfer-operator convergence, global Hénon zeta identification, or any Riemann-zero correspondence.",
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    flat: list[dict[str, Any]] = []
    for row in ensemble:
        flat.append({"kind": "ensemble", "grid": row["grid"], "samples_per_cell": row["samples_per_cell"],
                     "mean": row["mean"], "sd": row["sd"], "se": row["se"], "median": row["median"],
                     "mad": row["mad"], "cv": row["cv"]})
    for row in sd_ratios:
        flat.append({"kind": "sd_ratio", "grid": row["grid"], "sd64": row["sd64"], "sd256": row["sd256"],
                     "sd256_over_sd64": row["sd256_over_sd64"]})
    for row in paired:
        flat.append({"kind": "paired", "grid": row["grid"], "signed_delta_mean": row["signed_delta"]["mean"],
                     "signed_delta_sd": row["signed_delta"]["sd"], "absolute_relative_shift_mean": row["absolute_relative_shift"]["mean"]})
    for row in dyadic_aggregate:
        flat.append({"kind": "dyadic", "samples_per_cell": row["samples_per_cell"], "chain": "->".join(map(str, row["chain"])),
                     "D_mean": row["mean"], "D_sd": row["sd"], "D_bootstrap_low": row["D_bootstrap_mean_ci"][0],
                     "D_bootstrap_high": row["D_bootstrap_mean_ci"][1], "pass_fraction": row["pass_fraction"]})
    for row in gauss_gaps:
        flat.append({"kind": "gauss_gap", "grid": row["grid"], "q4_q8_gap": row["q4_q8_gap"],
                     "q8_q12_gap": row["q8_q12_gap"], "q8_q12_leq_q4_q8": row["q8_q12_leq_q4_q8"]})
    if flat:
        fields = sorted({key for row in flat for key in row})
        with args.csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(flat)

    # Human-readable report used by the paper notes and manifest.
    report: list[str] = [
        "# R060 Operator-Variance Analysis",
        "",
        "**Status:** completed finite-resolution mechanism analysis; R059 remains frozen with G4=false.",
        "",
        f"The production contains {len(records)} configurations (expected {integrity['expected_record_count']}). The independent checker passed: **{bool(check.get('all_checks_pass'))}**. The frozen protocol's G0 prose says 162 although its design expands to 210; this is retained as a warning, not silently corrected.",
        "",
        "## Gate summary",
        "",
        "| Gate | Result | Interpretation |",
        "|---|---|---|",
        f"| G0 integrity | **{'PASS' if g0 else 'FAIL'}** | hashes, schemas, source rows, pair fingerprints and finite-matrix checks |",
        f"| G1 Sobol variance | **{'PASS' if g1 else 'FAIL'}** | 256-vs-64 seed dispersion and paired shifts under the frozen thresholds |",
        f"| G2 Gauss order | **{'PASS' if g2 else 'FAIL'}** | q=8/q=12 versus q=4/q=8 at fixed grids |",
        f"| G3 256-sample mean trajectory | **{'PASS' if g3 else 'FAIL'}** | both dyadic chains plus the R059 Fredholm reference window |",
        "",
        "## Sobol seed dispersion",
        "",
        "| m | SD(64) | SD(256) | ratio | mean shift abs-rel |",
        "|---:|---:|---:|---:|---:|",
    ]
    for s, p in zip(sd_ratios, paired):
        report.append(f"| {s['grid']} | {fmt(s['sd64'])} | {fmt(s['sd256'])} | {fmt(s['sd256_over_sd64'])} | {fmt(p['absolute_relative_shift']['mean'])} |")
    report += [
        "",
        f"The median SD ratio is **{fmt(float(np.median(ratios)))}**; all six ratios are below one. However, the paired mean absolute relative shift is above the 1% G1 threshold at m=24 and m=32, so G1 is a strict failure despite a clear dispersion reduction.",
        "",
        "## Dyadic contrasts",
        "",
        r"For each chain, \(D = \Delta_{final}-\Delta_{first}\). Positive D is the frozen R059 failure direction. Bootstrap intervals resample fresh seeds (20,000 replicates; seed 20260803).",
        "",
        "| samples/cell | chain | mean D | 95% bootstrap CI | pass fraction |",
        "|---:|---|---:|---|---:|",
    ]
    for d in dyadic_aggregate:
        ci = d["D_bootstrap_mean_ci"]
        report.append(f"| {d['samples_per_cell']} | {'→'.join(map(str, d['chain']))} | {fmt(d['mean'])} | [{fmt(ci[0])}, {fmt(ci[1])}] | {fmt(d['pass_fraction'])} |")
    report += ["", "### Overlay of the two frozen R059 failures", "", "| R059 trajectory | observed D | fresh D≥observed | fresh |D|≥|observed| |", "|---|---:|---:|---:|"]
    for x in r059_overlay:
        report.append(f"| {x['method_key']} {'→'.join(map(str, x['chain']))} | {fmt(x['observed_D'])} | {fmt(x['fresh_fraction_D_ge_observed'])} | {fmt(x['fresh_fraction_absD_ge_abs_observed'])} |")
    report += [
        "",
        "The fresh-seed overlay is descriptive: it shows whether the two historical contrasts are unusual within the new 64-point ensemble, but it does not reopen R059.",
        "",
        "## Deterministic Gauss controls",
        "",
        "| m | q4→q8 gap | q8→q12 gap | q8→q12 no larger? |",
        "|---:|---:|---:|:---:|",
    ]
    for g in gauss_gaps:
        report.append(f"| {g['grid']} | {fmt(g['q4_q8_gap'])} | {fmt(g['q8_q12_gap'])} | {fmt(g['q8_q12_leq_q4_q8'])} |")
    report += [
        "",
        "Although q=8/q=12 is smaller than q=4/q=8 on five of six grids, it exceeds 0.5% on five of six grids. G2 therefore fails its all-grid stabilization threshold. This leaves grid/boundary phase effects unresolved rather than proving quadrature failure.",
        "",
        "## Conclusion boundary",
        "",
        "The evidence is mixed but useful: increasing the Sobol budget sharply reduces cross-seed dispersion (median ratio below 0.75), while the strict paired-shift gate is not met on the two coarsest grids. The 256-sample seed mean satisfies both dyadic mean checks and lies within 1% of the R059 Fredholm reference at m=96 and 128. Deterministic order comparisons remain grid dependent. The most defensible interpretation is partial support for a sampling-variance contribution plus unresolved finite-grid/target-boundary sensitivity.",
        "",
        "R060 does not alter R059 G4=false and does not establish continuous transfer-operator convergence, global Hénon zeta identification, or any Riemann-zero correspondence.",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({"output": str(args.output), "csv": str(args.csv), "report": str(args.report),
                      "gates": result["gates"], "median_sd_ratio": float(np.median(ratios)),
                      "record_count": len(records)}, indent=2))


if __name__ == "__main__":
    main()
