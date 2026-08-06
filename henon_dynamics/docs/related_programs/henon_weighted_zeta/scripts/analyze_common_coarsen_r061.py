#!/usr/bin/env python3
"""Analyze R061 common-cloud coarsening, dyadic paths, and localization."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_PROTOCOL.json"
DEFAULT_COARSEN = PROJECT_ROOT / "results" / "common_coarsen_r061.json"
DEFAULT_CHECK = PROJECT_ROOT / "results" / "common_coarsen_r061_check.json"
DEFAULT_LOCALIZATION = PROJECT_ROOT / "results" / "boundary_localization_r061.json"
DEFAULT_LOCALIZATION_CHECK = PROJECT_ROOT / "results" / "boundary_localization_r061_check.json"
DEFAULT_R060 = PROJECT_ROOT / "results" / "operator_variance_r060.json"
DEFAULT_R059 = PROJECT_ROOT / "results" / "restricted_operator_r059.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "common_coarsen_r061_analysis.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "common_coarsen_r061_analysis.csv"
DEFAULT_REPORT = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_ANALYSIS.md"


def relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), np.finfo(float).tiny)


def stats(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"n": 0, "mean": None, "median": None, "sd": None, "se": None, "min": None, "max": None}
    a = np.asarray(values, dtype=float)
    mean = float(np.mean(a))
    sd = float(np.std(a, ddof=1)) if a.size > 1 else 0.0
    return {"n": int(a.size), "mean": mean, "median": float(np.median(a)), "sd": sd, "se": float(sd / math.sqrt(a.size)), "min": float(np.min(a)), "max": float(np.max(a))}


class Bootstrap:
    def __init__(self, seed: int, reps: int) -> None:
        self.rng = np.random.default_rng(int(seed))
        self.seed = int(seed)
        self.reps = int(reps)

    def mean_ci(self, values: list[float]) -> list[float] | None:
        if not values:
            return None
        a = np.asarray(values, dtype=float)
        if a.size == 1:
            return [float(a[0]), float(a[0])]
        sample = self.rng.choice(a, size=(self.reps, a.size), replace=True)
        means = np.mean(sample, axis=1)
        return [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    p.add_argument("--coarsen", type=Path, default=DEFAULT_COARSEN)
    p.add_argument("--check", type=Path, default=DEFAULT_CHECK)
    p.add_argument("--localization", type=Path, default=DEFAULT_LOCALIZATION)
    p.add_argument("--localization-check", type=Path, default=DEFAULT_LOCALIZATION_CHECK)
    p.add_argument("--r060", type=Path, default=DEFAULT_R060)
    p.add_argument("--r059", type=Path, default=DEFAULT_R059)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    p.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    protocol = load(args.protocol)
    coarsen = load(args.coarsen)
    check = load(args.check)
    localization = load(args.localization)
    localization_check = load(args.localization_check)
    r060 = load(args.r060)
    r059 = load(args.r059)
    grids = [int(x) for chain in protocol["design"]["chains"] for x in chain["target_grids"]]
    target_levels = sorted(set(grids))
    seeds = [int(x) for x in protocol["design"]["seeds"]]
    budgets = [int(x) for x in protocol["design"]["sobol_samples_per_cell"]]
    chains = [str(x["name"]) for x in protocol["design"]["chains"]]
    targets_by_chain = {
        str(x["name"]): [int(y) for y in x["target_grids"]]
        for x in protocol["design"]["chains"]
    }
    bootstrap = Bootstrap(int(protocol["localization"]["bootstrap_seed"]), int(protocol["localization"]["bootstrap_replicates"]))
    r060_by_id = {str(x["config_id"]): x for x in r060.get("records", [])}
    common_by_id = {str(x["config_id"]): x for x in coarsen.get("records", [])}
    localization_by_id = {str(x["config_id"]): x for x in localization.get("records", [])}

    direct_common: list[dict[str, Any]] = []
    for row in coarsen.get("records", []):
        direct = r060_by_id[str(row["direct_config_id"])]
        gap = relative_gap(float(row["leading_modulus"]), float(direct["leading_modulus"]))
        loc = localization_by_id.get(str(row["config_id"]), {})
        direct_common.append({"config_id": row["config_id"], "chain": row["chain"], "target_grid": int(row["target_grid"]), "fine_grid": int(row["fine_grid"]), "method_family": row["method_family"], "samples_per_cell": int(row["samples_per_cell"]), "quadrature_order": int(row["quadrature_order"]), "seed": row.get("seed"), "common_leading_modulus": float(row["leading_modulus"]), "direct_leading_modulus": float(direct["leading_modulus"]), "relative_gap": gap, "total_row_energy": loc.get("total_row_energy"), "mean_row_tv": None if loc.get("total_row_energy") is None else float(loc["total_row_energy"] / max(int(loc.get("row_count", 1)), 1)), "localization": loc.get("tau_summary", {})})

    sobol_groups: list[dict[str, Any]] = []
    for chain in chains:
        for budget in budgets:
            for target in targets_by_chain[chain]:
                rows = [x for x in direct_common if x["chain"] == chain and x["method_family"] == "sobol" and x["samples_per_cell"] == budget and x["target_grid"] == target]
                gaps = [float(x["relative_gap"]) for x in rows]
                sobol_groups.append({"chain": chain, "samples_per_cell": budget, "target_grid": target, "n": len(rows), "gap": stats(gaps), "median_pass_le_2pct": bool(gaps and np.median(gaps) <= 0.02), "seed_values": [{"seed": x["seed"], "relative_gap": x["relative_gap"]} for x in sorted(rows, key=lambda y: int(y["seed"]))]})
    pooled_gaps = [float(x["relative_gap"]) for x in direct_common if x["method_family"] == "sobol"]
    g1_gap_pass = bool(sum(bool(x["median_pass_le_2pct"]) for x in sobol_groups) >= 6 and pooled_gaps and np.median(pooled_gaps) <= 0.02)

    # Dyadic trajectories: fine parent is the common endpoint; coarse and
    # middle values come from the two derived matrices. Direct values are the
    # corresponding R060 records.
    dyadic_per_seed: list[dict[str, Any]] = []
    dyadic_groups: list[dict[str, Any]] = []
    for chain_cfg in protocol["design"]["chains"]:
        chain = str(chain_cfg["name"])
        fine = int(chain_cfg["fine_grid"])
        mid, coarse = [int(x) for x in chain_cfg["target_grids"]]
        for budget in budgets:
            rows = []
            for seed in seeds:
                derived_mid = next(x for x in coarsen.get("records", []) if x["chain"] == chain and int(x["target_grid"]) == mid and x["method_family"] == "sobol" and int(x["samples_per_cell"]) == budget and int(x["seed"]) == seed)
                derived_coarse = next(x for x in coarsen.get("records", []) if x["chain"] == chain and int(x["target_grid"]) == coarse and x["method_family"] == "sobol" and int(x["samples_per_cell"]) == budget and int(x["seed"]) == seed)
                p_fine = next(x for x in r060.get("records", []) if int(x["grid"]) == fine and x["method_family"] == "sobol" and int(x["samples_per_cell"]) == budget and int(x["seed"]) == seed)
                d_mid = r060_by_id[derived_mid["direct_config_id"]]
                d_coarse = r060_by_id[derived_coarse["direct_config_id"]]
                direct_vals = [float(d_coarse["leading_modulus"]), float(d_mid["leading_modulus"]), float(p_fine["leading_modulus"])]
                common_vals = [float(derived_coarse["leading_modulus"]), float(derived_mid["leading_modulus"]), float(p_fine["leading_modulus"])]
                d_first = relative_gap(direct_vals[0], direct_vals[1]); d_final = relative_gap(direct_vals[1], direct_vals[2])
                c_first = relative_gap(common_vals[0], common_vals[1]); c_final = relative_gap(common_vals[1], common_vals[2])
                row = {"chain": chain, "samples_per_cell": budget, "seed": seed, "direct_values": direct_vals, "common_values": common_vals, "direct_first": d_first, "direct_final": d_final, "direct_D": d_final - d_first, "common_first": c_first, "common_final": c_final, "common_D": c_final - c_first, "abs_D_ratio": abs(c_final - c_first) / max(abs(d_final - d_first), np.finfo(float).tiny)}
                rows.append(row); dyadic_per_seed.append(row)
            dvals = [float(x["direct_D"]) for x in rows]; cvals = [float(x["common_D"]) for x in rows]; ratios = [float(x["abs_D_ratio"]) for x in rows]
            agg = {"chain": chain, "samples_per_cell": budget, "direct_D": stats(dvals), "common_D": stats(cvals), "abs_D_ratio": stats(ratios), "direct_pass_fraction": float(np.mean([x["direct_final"] <= x["direct_first"] for x in rows])), "common_pass_fraction": float(np.mean([x["common_final"] <= x["common_first"] for x in rows])), "direct_D_bootstrap_ci": bootstrap.mean_ci(dvals), "common_D_bootstrap_ci": bootstrap.mean_ci(cvals), "median_abs_common_le_direct": bool(np.median(np.abs(cvals)) <= np.median(np.abs(dvals))), "median_abs_ratio_le_0_8": bool(np.median(ratios) <= 0.8)}
            dyadic_groups.append(agg)
    g1_smooth_pass = bool(sum(bool(x["median_abs_common_le_direct"] and x["median_abs_ratio_le_0_8"]) for x in dyadic_groups) >= 3)

    # Localization gate: use tau=1 and accept either h-set or cell exposure;
    # retain both categories and their bootstrap intervals in the report.
    localization_groups: list[dict[str, Any]] = []
    for group in sobol_groups:
        chain, budget, target = group["chain"], group["samples_per_cell"], group["target_grid"]
        rows = [localization_by_id[x["config_id"]] for x in coarsen.get("records", []) if x["chain"] == chain and x["method_family"] == "sobol" and int(x["samples_per_cell"]) == budget and int(x["target_grid"]) == target]
        h_rho = [float(x["tau_summary"]["1.0"]["spearman_h"]) for x in rows if x.get("tau_summary", {}).get("1.0", {}).get("spearman_h") is not None]
        c_rho = [float(x["tau_summary"]["1.0"]["spearman_cell"]) for x in rows if x.get("tau_summary", {}).get("1.0", {}).get("spearman_cell") is not None]
        h_top = [float(x["tau_summary"]["1.0"]["top25_h"]) for x in rows if x.get("tau_summary", {}).get("1.0", {}).get("top25_h") is not None]
        c_top = [float(x["tau_summary"]["1.0"]["top25_cell"]) for x in rows if x.get("tau_summary", {}).get("1.0", {}).get("top25_cell") is not None]
        h_ci = bootstrap.mean_ci(h_rho); c_ci = bootstrap.mean_ci(c_rho)
        h_support = bool(h_rho and h_ci and np.mean(h_rho) >= 0.30 and h_ci[0] > 0.0 and np.mean(h_top) >= 0.40)
        c_support = bool(c_rho and c_ci and np.mean(c_rho) >= 0.30 and c_ci[0] > 0.0 and np.mean(c_top) >= 0.40)
        h_conc = float(np.mean(h_top)) if h_top else None; c_conc = float(np.mean(c_top)) if c_top else None
        category = "unresolved"
        if h_conc is not None and c_conc is not None:
            if h_conc - c_conc >= 0.10: category = "hset"
            elif c_conc - h_conc >= 0.10: category = "cell"
            else: category = "mixed"
        localization_groups.append({"chain": chain, "samples_per_cell": budget, "target_grid": target, "h_rho": stats(h_rho), "cell_rho": stats(c_rho), "h_rho_bootstrap_ci": h_ci, "cell_rho_bootstrap_ci": c_ci, "h_top25_mean": h_conc, "cell_top25_mean": c_conc, "h_support": h_support, "cell_support": c_support, "category": category})
    g2_support = sum(bool(x["h_support"] or x["cell_support"]) for x in localization_groups)
    g2 = bool(g2_support >= 4)

    gauss_gaps: list[dict[str, Any]] = []
    for target in target_levels:
        q8 = [x for x in direct_common if x["method_family"] == "gauss" and int(x["target_grid"]) == target and int(x["quadrature_order"]) == 8]
        q12 = [x for x in direct_common if x["method_family"] == "gauss" and int(x["target_grid"]) == target and int(x["quadrature_order"]) == 12]
        if q8 and q12:
            gap = relative_gap(q8[0]["common_leading_modulus"], q12[0]["common_leading_modulus"])
            gauss_gaps.append({"target_grid": target, "q8_q12_gap": gap, "pass": bool(gap <= 0.01)})
    g3 = bool(sum(bool(x["pass"]) for x in gauss_gaps) >= 3)

    overlay: list[dict[str, Any]] = []
    failures = r059.get("finite_resolution_audit", {}).get("dyadic_change", [])
    for failure in failures:
        if failure.get("pass"): continue
        chain = tuple(int(x) for x in failure["chain"])
        budget = 64
        group = next((x for x in dyadic_per_seed if x["samples_per_cell"] == budget and tuple([24,48,96] if chain == (24,48,96) else [32,64,128]) == tuple([24,48,96] if x["chain"] == "chain_24_48_96" else [32,64,128]) and x["seed"] == int(failure["method_key"].replace("sobol_seed", ""))), None)
        direct_vals = [x["direct_D"] for x in dyadic_per_seed if x["samples_per_cell"] == budget and x["chain"] == ("chain_24_48_96" if chain == (24,48,96) else "chain_32_64_128")]
        common_vals = [x["common_D"] for x in dyadic_per_seed if x["samples_per_cell"] == budget and x["chain"] == ("chain_24_48_96" if chain == (24,48,96) else "chain_32_64_128")]
        observed = float(failure["final_relative_change"] - failure["first_relative_change"])
        overlay.append({"method_key": failure["method_key"], "chain": list(chain), "observed_D": observed, "direct_fraction_ge": float(np.mean(np.asarray(direct_vals) >= observed)), "common_fraction_ge": float(np.mean(np.asarray(common_vals) >= observed)), "direct_mean_D": float(np.mean(direct_vals)), "common_mean_D": float(np.mean(common_vals))})

    localization_integrity = bool(
        len(localization.get("records", [])) == len(coarsen.get("records", []))
        and all(int(x.get("boundary_hits", -1)) == 0 for x in localization.get("records", []))
    )
    localization_checker_pass = bool(localization_check.get("all_checks_pass"))
    gates = {"G0_integrity": bool(check.get("all_checks_pass") and localization_checker_pass and localization_integrity), "G1_common_projection": bool(g1_gap_pass and g1_smooth_pass), "G1_gap_component": g1_gap_pass, "G1_smoothing_component": g1_smooth_pass, "G2_boundary_localization": g2, "G3_quadrature": g3}
    result = {"run_id": "R061_COMMON_CLOUD_ANALYSIS", "protocol_sha256": coarsen.get("protocol_sha256"), "record_count": len(coarsen.get("records", [])), "localization_integrity": localization_integrity, "localization_checker_pass": localization_checker_pass, "direct_common": direct_common, "sobol_groups": sobol_groups, "dyadic_per_seed": dyadic_per_seed, "dyadic_groups": dyadic_groups, "localization_groups": localization_groups, "gauss_gaps": gauss_gaps, "r059_failure_overlay": overlay, "gates": gates, "mechanism_tags": {"common_projection": "supported" if gates["G1_common_projection"] else "mixed_or_unresolved", "boundary_localization": "supported" if g2 else "unresolved_or_mixed", "quadrature": "supported" if g3 else "unresolved", "overall": "FINITE_RESOLUTION_MECHANISM_AUDIT"}, "anti_claim": protocol["claims"]["anti_claim"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    flat: list[dict[str, Any]] = []
    for x in sobol_groups: flat.append({"kind": "spectral_group", "chain": x["chain"], "samples_per_cell": x["samples_per_cell"], "target_grid": x["target_grid"], "gap_median": x["gap"]["median"], "gap_mean": x["gap"]["mean"], "pass": x["median_pass_le_2pct"]})
    for x in dyadic_groups: flat.append({"kind": "dyadic_group", "chain": x["chain"], "samples_per_cell": x["samples_per_cell"], "direct_D_mean": x["direct_D"]["mean"], "common_D_mean": x["common_D"]["mean"], "ratio_median": x["abs_D_ratio"]["median"], "smooth_pass": x["median_abs_common_le_direct"] and x["median_abs_ratio_le_0_8"]})
    for x in localization_groups: flat.append({"kind": "localization_group", "chain": x["chain"], "samples_per_cell": x["samples_per_cell"], "target_grid": x["target_grid"], "h_rho_mean": x["h_rho"]["mean"], "cell_rho_mean": x["cell_rho"]["mean"], "h_top25": x["h_top25_mean"], "cell_top25": x["cell_top25_mean"], "category": x["category"]})
    for x in gauss_gaps: flat.append({"kind": "gauss_gap", "target_grid": x["target_grid"], "q8_q12_gap": x["q8_q12_gap"], "pass": x["pass"]})
    if flat:
        fields = sorted({key for row in flat for key in row})
        with args.csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(flat)
    report = ["# R061 Common-Cloud Coarsening Analysis", "", "**Status:** completed finite-resolution mechanism audit; R059 G4 and R060 gates remain unchanged.", "", f"The production contains {len(coarsen.get('records', []))} derived matrices from 68 read-only R060 parent references. Independent CSR checker: **{check.get('all_checks_pass')}**; independent localization-array checker: **{localization_checker_pass}**; localization records complete with zero exact boundary hits: **{localization_integrity}**.", "", "## Gate summary", "", "| Gate | Result |", "|---|---|", f"| G0 integrity | **{'PASS' if gates['G0_integrity'] else 'FAIL'}** |", f"| G1 common projection | **{'PASS' if gates['G1_common_projection'] else 'FAIL'}** (gap component={'PASS' if g1_gap_pass else 'FAIL'}, smoothing component={'PASS' if g1_smooth_pass else 'FAIL'}) |", f"| G2 boundary localization | **{'PASS' if g2 else 'FAIL'}** ({g2_support}/8 groups supported) |", f"| G3 q8/q12 common control | **{'PASS' if g3 else 'FAIL'}** ({sum(x['pass'] for x in gauss_gaps)}/{len(gauss_gaps)} target levels) |", "", "## Common/direct spectral gaps", "", "| chain | budget | target | median relative gap | pass (<=2%) |", "|---|---:|---:|---:|:---:|"]
    for x in sobol_groups: report.append(f"| {x['chain']} | {x['samples_per_cell']} | {x['target_grid']} | {x['gap']['median']:.6g} | {'yes' if x['median_pass_le_2pct'] else 'no'} |")
    report += ["", "## Dyadic contrasts", "", "| chain | budget | direct mean D | common mean D | median |D_common|/|D_direct| | smooth support |", "|---|---:|---:|---:|---:|:---:|"]
    for x in dyadic_groups: report.append(f"| {x['chain']} | {x['samples_per_cell']} | {x['direct_D']['mean']:.6g} | {x['common_D']['mean']:.6g} | {x['abs_D_ratio']['median']:.6g} | {'yes' if x['median_abs_common_le_direct'] and x['median_abs_ratio_le_0_8'] else 'no'} |")
    report += ["", "## Boundary localization", "", "| chain | budget | target | rho h-set | rho cell | top25 h | top25 cell | class |", "|---|---:|---:|---:|---:|---:|---:|---|"]
    for x in localization_groups: report.append(f"| {x['chain']} | {x['samples_per_cell']} | {x['target_grid']} | {x['h_rho']['mean']:.4g} | {x['cell_rho']['mean']:.4g} | {x['h_top25_mean']:.4g} | {x['cell_top25_mean']:.4g} | {x['category']} |")
    report += ["", "## Gauss control", "", "| target | q8/q12 relative gap | pass |", "|---:|---:|:---:|"]
    for x in gauss_gaps: report.append(f"| {x['target_grid']} | {x['q8_q12_gap']:.6g} | {'yes' if x['pass'] else 'no'} |")
    report += ["", "## Scope boundary", "", "The common-cloud coarse rows inherit (s r^2) fine samples per source cell, so common/direct comparisons are explicitly comparisons of different finite estimators as well as different couplings. R061 measures a common finite-matrix projection and rowwise exposure association; it does not establish continuous operator convergence, a graph limit, a global Hénon zeta identity, or any Riemann/Hilbert--Pólya statement. R059 G4 remains false."]
    args.report.parent.mkdir(parents=True, exist_ok=True); args.report.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "report": str(args.report), "gates": gates, "record_count": len(coarsen.get("records", [])), "localization_groups": len(localization_groups)}, indent=2))


if __name__ == "__main__":
    main()
