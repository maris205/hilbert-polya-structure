#!/usr/bin/env python3
"""Analyze the frozen R058 theorem and graph-replication results."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_FILAMENT_PROTOCOL.json"
)
THEORY = PROJECT_ROOT / "results" / "hyperbolic_covering_r058.json"
GRAPH = PROJECT_ROOT / "results" / "hyperbolic_filament_r058.json"
CHECKER = (
    PROJECT_ROOT
    / "results"
    / "hyperbolic_filament_independent_check_r058.json"
)
DERIVATION = PROJECT_ROOT / "R058_COVERING_DERIVATION.md"
COVERING_PROOF = PROJECT_ROOT / "R058_COVERING_PROOF.md"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "hyperbolic_filament_analysis_r058.json"
DEFAULT_MARKDOWN = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_FILAMENT_ANALYSIS.md"
)
R056_POSITIVE_SLOPE = 1.038202300055618


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL)
    parser.add_argument("--theory", type=Path, default=THEORY)
    parser.add_argument("--graph", type=Path, default=GRAPH)
    parser.add_argument("--checker", type=Path, default=CHECKER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_report(analysis: dict[str, Any]) -> str:
    theory = analysis["theory_summary"]
    proof_artifacts = analysis["proof_artifacts"]
    lineage_rows = analysis["lineage_table"]
    config_rows = analysis["configuration_table"]
    overlap_rows = analysis["phase_overlap_table"]
    bridge_rows = analysis["symbolic_bridge_table"]
    aggregate = analysis["aggregate_metrics"]
    checker = analysis["independent_checker_summary"]

    lines = [
        "# R058 Hyperbolic Survivor and Filament Replication Analysis",
        "",
        f"**Completed:** {analysis['completed_date']}",
        f"**Frozen protocol:** {analysis['protocol_sha256']}",
        "**Decision:** C1 theorem PASS; C2 graph replication PASS; independent checker PASS",
        "**Evidence levels:** exact covering/cone theorem plus locked exact finite-grid replication",
        "",
        "## 1. Main outcome",
        "",
        "R058 closes the main logical gap left by R054--R057. The finite graph is no",
        "longer asked to manufacture a common orbit witness. Six exact h-set",
        "coverings, ten exact forbidden transitions, and strict two-sided cone",
        "bounds certify a nonempty compact uniformly hyperbolic survivor subset.",
        "Its itinerary map is a continuous surjection onto the frozen four-state",
        "subshift, so",
        "",
        r"\[",
        r"h_{\rm top}(H_6|_\Lambda)\ge\log\varphi",
        rf"\approx {theory['entropy_lower_bound_float']:.9f}.",
        r"\]",
        "",
        "This is a semiconjugacy and entropy lower bound, not a conjugacy, entropy",
        "equality, or Markov-partition claim.",
        "",
        "The separate nine-grid true-positive replication also passes every frozen",
        "gate. Its three multilevel lineages reproduce near-one-dimensional node",
        "growth, shrinking physical area, approximately one-half descendant",
        "coverage, and the exact six-transition symbolic skeleton.",
        "",
        "## 2. Exact theorem certificate",
        "",
        "| Quantity | Exact value | Decision |",
        "|---|---:|---|",
        f"| Allowed coverings | {theory['allowed_covering_count']} | PASS |",
        f"| Forbidden transitions excluded | {theory['forbidden_transition_count']} | PASS |",
        f"| Minimum exit margin | {theory['minimum_exit_margin']} | PASS |",
        f"| Minimum entry margin | {theory['minimum_entry_margin']} | PASS |",
        f"| Forward cone slope bound | {theory['forward_cone_slope']} | < 1/2 |",
        f"| Backward cone slope bound | {theory['backward_cone_slope']} | < 1/2 |",
        f"| Forward expansion squared | {theory['forward_expansion_squared']} | > 1 |",
        f"| Backward expansion squared | {theory['backward_expansion_squared']} | > 1 |",
        f"| Spectral radius | {theory['spectral_radius_exact']} | exact |",
        "",
        "## 3. Raw locked configuration table",
        "",
        "| Configuration | Offset | Kmax | Active cells | Positive edges | Canonical positive SCC | Lineage SCC |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in config_rows:
        lines.append(
            f"| {row['configuration']} | {row['offset']} | "
            f"{row['uncapped_k_max']} | {row['active_cells']} | "
            f"{row['positive_edges']} | {row['canonical_positive_scc']} | "
            f"{row['lineage_scc']} |"
        )
    lines.extend(
        [
            "",
            "All nine cap counts are zero. The two finest shifted grids reach",
            "uncapped K=62, leaving only two subdivisions of headroom under the",
            "frozen cap of 64, but their exact integrity checks still pass.",
            "",
            "## 4. Multilevel lineage replication",
            "",
            "| Chain | Lineage sizes | Exact areas | 4x exponent d | Area exponent d-2 | Coverages | Decision |",
            "|---|---|---|---:|---:|---|---|",
        ]
    )
    for row in lineage_rows:
        lines.append(
            f"| {row['chain']} | {row['sizes_text']} | {row['areas_text']} | "
            f"{row['four_x_size_exponent']:.6f} | "
            f"{row['area_exponent']:.6f} | {row['coverages_text']} | PASS |"
        )
    lines.extend(
        [
            "",
            "Aggregate replication:",
            "",
            f"- mean lineage exponent: {aggregate['mean_size_exponent']:.6f};",
            f"- R056 positive-SCC slope: {aggregate['r056_positive_slope']:.6f};",
            f"- mean difference from R056: {aggregate['mean_exponent_delta_vs_r056']:+.6f};",
            f"- mean physical-area exponent: {aggregate['mean_area_exponent']:.6f};",
            f"- six-step coverage mean/median: "
            f"{aggregate['coverage_mean']:.6f}/{aggregate['coverage_median']:.6f};",
            f"- coverage range: {aggregate['coverage_min']:.6f}--"
            f"{aggregate['coverage_max']:.6f}.",
            "",
            "The mean R058 exponent differs from the R056 positive slope by only",
            "about 0.00033. This is a strong deterministic replication of the",
            "selected filament-compatible scaling model. It is still not a",
            "dimension theorem or graph-limit statement.",
            "",
            "The lineage is intentionally not replaced by the largest child SCC.",
            "At the middle levels it retains about 96.6%--96.7% of the canonical",
            "largest-SCC size; at the finest levels it retains about",
            "95.8%--97.7%. Thus the pass is not caused by silent branch switching.",
            "",
            "## 5. Symbolic bridge",
            "",
            "| Finest configuration | State cell counts (--,-+,+-,++) | Observed transitions | Extra transitions |",
            "|---|---|---:|---:|",
        ]
    )
    for row in bridge_rows:
        lines.append(
            f"| {row['configuration']} | {row['state_counts_text']} | "
            f"{row['observed_transition_count']} / 6 | {row['extra_transition_count']} |"
        )
    lines.extend(
        [
            "",
            "Every finest lineage contains all four h-set states and realizes",
            "exactly the six certified transitions, with no forbidden state",
            "transition. This is a useful finite-grid bridge to the exact",
            "survivor, but C1 remains proved by covering relations rather than by",
            "this incidence observation.",
            "",
            "## 6. Finest-grid phase overlap",
            "",
            "| Pair | Geometric Jaccard | Intersection / first | Intersection / second |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in overlap_rows:
        lines.append(
            f"| {row['pair']} | {row['jaccard']:.6f} | "
            f"{row['intersection_over_first']:.6f} | "
            f"{row['intersection_over_second']:.6f} |"
        )
    lines.extend(
        [
            "",
            f"The Jaccard range is {aggregate['jaccard_min']:.6f}--"
            f"{aggregate['jaccard_max']:.6f}, with median "
            f"{aggregate['jaccard_median']:.6f}. Phase dependence remains",
            "visible, but a large common geometry survives.",
            "",
            "## 7. Independent checker",
            "",
            f"- complete microgrids: {checker['microgrid_pair_count']:,} source-target pairs;",
            f"- frozen held-out source sweeps: {checker['fixed_source_count']} sources and "
            f"{checker['fixed_source_target_pair_count']:,} source-target pairs;",
            "- all nine NPZ schemas and hashes independently reloaded;",
            "- all six complete and matched-support projections independently rebuilt;",
            "- three multilevel lineages and three symbolic bridges independently rebuilt;",
            "- theorem matrix and cone fractions independently recomputed;",
            f"- final checker decision: {checker['all_checks_pass']}.",
            "",
            "## 8. Difference from the frozen expectation",
            "",
            "1. C1 is stronger than the previous finite-grid hope. R058 now has an",
            "   actual compact uniformly hyperbolic survivor and entropy lower",
            "   bound, not merely persistent SCCs.",
            "2. C2 lands almost exactly on the R056 selected positive scaling:",
            f"   mean d={aggregate['mean_size_exponent']:.6f} versus "
            f"{aggregate['r056_positive_slope']:.6f}.",
            "3. All six descendant coverages lie between 0.5009 and 0.5314,",
            "   slightly above but fully compatible with the frozen half-core",
            "   hypothesis.",
            "4. The symbolic bridge is cleaner than minimally required: every",
            "   finest lineage has all six allowed transitions and zero extras.",
            "5. The no-cap stress remains genuine: K=62 is close to 64, but no",
            "   cap or post-freeze repair was needed.",
            "",
            "## 9. Scope boundary",
            "",
            "R058 proves a conservative hyperbolic subset at a=6. It does not prove",
            "that the full Hénon horseshoe, the whole finite-grid filament, or the",
            "open transfer operator is represented by these four h-sets. It does",
            "not establish graph convergence, operator convergence, a zeta",
            "identity, a Riemann-zero relation, RH, or a Hilbert--Pólya operator.",
            "",
            "## 10. Recommended next runs",
            "",
            "1. Classify the existing exact period-1--12 a=6 orbit catalog by the",
            "   four h-sets and compare certified symbolic words with trace(A^n).",
            "2. Freeze an interval search for wider rational h-sets or a richer",
            "   transition graph, aiming to raise the entropy lower bound without",
            "   weakening cone margins.",
            "3. Build one operator and one cycle expansion restricted to the",
            "   certified survivor, removing the old ambiguity about the common",
            "   dynamical domain.",
            "",
            "## 11. Artifacts",
            "",
            "- research/refine-logs/R058_HYPERBOLIC_FILAMENT_PROTOCOL.json;",
            "- research/refine-logs/R058_HYPERBOLIC_FILAMENT_MANIFEST.md;",
            "- R058_COVERING_DERIVATION.md "
            f"(SHA-256 `{proof_artifacts['derivation']['sha256']}`);",
            "- R058_COVERING_PROOF.md "
            f"(SHA-256 `{proof_artifacts['covering_proof']['sha256']}`);",
            "- research/refine-logs/R058_HYPERBOLIC_THEOREM_AUDIT.md;",
            "- scripts/audit_hyperbolic_covering_r058.py;",
            "- scripts/audit_hyperbolic_filament_r058.py;",
            "- scripts/check_hyperbolic_filament_r058.py;",
            "- results/hyperbolic_covering_r058.json;",
            "- results/hyperbolic_filament_r058.json and CSV;",
            "- results/hyperbolic_filament_r058_edges/*.npz;",
            "- results/hyperbolic_filament_independent_check_r058.json;",
            "- results/hyperbolic_filament_analysis_r058.json.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    protocol = load_json(args.protocol)
    theory = load_json(args.theory)
    graph = load_json(args.graph)
    checker = load_json(args.checker)
    input_checks = {
        "protocol_run_id": protocol.get("run_id") == "R058_HYPERBOLIC_FILAMENT",
        "theory_full_claim": theory["decisions"]["full_primary_claim_enabled"],
        "graph_all_gates": graph["decisions"]["all_frozen_graph_gates_pass"],
        "checker_all_pass": checker["all_checks_pass"],
        "checker_graph_hash_alignment": checker["input_sha256"]
        == sha256_file(args.graph),
        "checker_theory_hash_alignment": checker["theory_sha256"]
        == sha256_file(args.theory),
        "protocol_hash_alignment": theory["protocol_integrity"][
            "protocol_sha256"
        ]
        == graph["protocol_integrity"]["protocol_sha256"]
        == checker["protocol_sha256"],
    }
    if not all(input_checks.values()):
        raise SystemExit(f"R058 analysis input gate failure: {input_checks}")

    exit_margins = [
        Fraction(record["crossing_margin"]["fraction"])
        for record in theory["covering_records"]
    ]
    entry_margins = [
        Fraction(record["entry_margin"]["fraction"])
        for record in theory["covering_records"]
    ]
    theory_summary = {
        "allowed_covering_count": len(theory["covering_records"]),
        "forbidden_transition_count": len(
            theory["forbidden_transition_records"]
        ),
        "minimum_exit_margin": str(min(exit_margins)),
        "minimum_entry_margin": str(min(entry_margins)),
        "forward_cone_slope": theory["cone_certificate"][
            "forward_unstable_slope_upper_bound"
        ]["fraction"],
        "backward_cone_slope": theory["cone_certificate"][
            "backward_stable_slope_upper_bound"
        ]["fraction"],
        "forward_expansion_squared": theory["cone_certificate"][
            "forward_expansion_factor_squared_lower_bound"
        ]["fraction"],
        "backward_expansion_squared": theory["cone_certificate"][
            "backward_expansion_factor_squared_lower_bound"
        ]["fraction"],
        "spectral_radius_exact": theory["symbolic_graph"][
            "spectral_radius_exact"
        ],
        "entropy_lower_bound_float": math.log((1 + math.sqrt(5)) / 2),
    }

    lineage_by_config: dict[str, int] = {}
    lineage_table: list[dict[str, Any]] = []
    exponents: list[float] = []
    area_exponents: list[float] = []
    coverages: list[float] = []
    for lineage in graph["lineages"]:
        sizes = [int(value) for value in lineage["lineage_sizes"]]
        areas = [
            float(value["float"]) for value in lineage["lineage_areas"]
        ]
        exponent = float(lineage["four_x_size_exponent"])
        step_coverages = [
            float(step["selected_descendant_lifted_area_coverage"]["float"])
            for step in lineage["steps"]
        ]
        for name, size in zip(
            lineage["configurations"], sizes, strict=True
        ):
            lineage_by_config[str(name)] = size
        exponents.append(exponent)
        area_exponents.append(exponent - 2)
        coverages.extend(step_coverages)
        lineage_table.append(
            {
                "chain": lineage["chain"],
                "configurations": lineage["configurations"],
                "sizes": sizes,
                "sizes_text": " -> ".join(str(value) for value in sizes),
                "areas": areas,
                "areas_text": " -> ".join(f"{value:.6f}" for value in areas),
                "four_x_size_exponent": exponent,
                "area_exponent": exponent - 2,
                "coverages": step_coverages,
                "coverages_text": " / ".join(
                    f"{value:.6f}" for value in step_coverages
                ),
            }
        )

    configuration_table = []
    canonical_lineage_ratios = []
    for record in graph["records"]:
        name = str(record["configuration"])
        canonical = int(record["true_positive_graph"]["largest_scc_size"])
        lineage_size = int(lineage_by_config[name])
        canonical_lineage_ratios.append(lineage_size / canonical)
        configuration_table.append(
            {
                "configuration": name,
                "offset": record["grid_offset_fraction"],
                "uncapped_k_max": int(record["uncapped_k_max"]),
                "active_cells": int(record["active_node_count"]),
                "positive_edges": int(record["true_forward_positive_edge_count"]),
                "canonical_positive_scc": canonical,
                "lineage_scc": lineage_size,
                "lineage_over_canonical": lineage_size / canonical,
                "closed_identity_sidecar_pass": bool(
                    record["true_closed_equals_mutual_outer_forward_pass"]
                    and record["true_closed_equals_mutual_outer_backward_pass"]
                ),
            }
        )

    bridge_table = []
    for bridge in graph["symbolic_bridge"]:
        order = protocol["h_sets"]["state_order"]
        bridge_table.append(
            {
                "configuration": bridge["configuration"],
                "state_counts": bridge["state_cell_counts"],
                "state_counts_text": ",".join(
                    str(bridge["state_cell_counts"][state]) for state in order
                ),
                "observed_transition_count": len(
                    bridge["observed_state_transitions"]
                ),
                "extra_transition_count": len(
                    bridge["extra_forbidden_transitions"]
                ),
            }
        )

    phase_overlap_table = []
    jaccards = []
    for overlap in graph["finest_phase_overlaps"]:
        jaccard = float(overlap["geometric_jaccard"]["float"])
        jaccards.append(jaccard)
        phase_overlap_table.append(
            {
                "pair": f"{overlap['first_chain']} vs {overlap['second_chain']}",
                "jaccard": jaccard,
                "intersection_over_first": float(
                    overlap["intersection_over_first"]["float"]
                ),
                "intersection_over_second": float(
                    overlap["intersection_over_second"]["float"]
                ),
            }
        )

    aggregate = {
        "mean_size_exponent": statistics.mean(exponents),
        "median_size_exponent": statistics.median(exponents),
        "population_std_size_exponent": statistics.pstdev(exponents),
        "r056_positive_slope": R056_POSITIVE_SLOPE,
        "mean_exponent_delta_vs_r056": statistics.mean(exponents)
        - R056_POSITIVE_SLOPE,
        "mean_area_exponent": statistics.mean(area_exponents),
        "coverage_mean": statistics.mean(coverages),
        "coverage_median": statistics.median(coverages),
        "coverage_population_std": statistics.pstdev(coverages),
        "coverage_min": min(coverages),
        "coverage_max": max(coverages),
        "lineage_over_canonical_min": min(canonical_lineage_ratios),
        "lineage_over_canonical_max": max(canonical_lineage_ratios),
        "jaccard_mean": statistics.mean(jaccards),
        "jaccard_median": statistics.median(jaccards),
        "jaccard_min": min(jaccards),
        "jaccard_max": max(jaccards),
        "closed_identity_sidecar_pass_count": sum(
            row["closed_identity_sidecar_pass"]
            for row in configuration_table
        ),
    }

    checker_summary = {
        "microgrid_pair_count": checker["microgrid_checks"][
            "total_source_target_pair_count"
        ],
        "fixed_source_count": checker["fixed_source_checks"][
            "total_source_count"
        ],
        "fixed_source_target_pair_count": checker["fixed_source_checks"][
            "total_source_target_pair_count"
        ],
        "all_checks_pass": checker["all_checks_pass"],
    }
    analysis = {
        "run_id": "R058_HYPERBOLIC_FILAMENT_ANALYSIS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "completed_date": "2026-08-02",
        "protocol_path": portable_path(args.protocol),
        "protocol_sha256": sha256_file(args.protocol),
        "theory_path": portable_path(args.theory),
        "theory_sha256": sha256_file(args.theory),
        "graph_path": portable_path(args.graph),
        "graph_sha256": sha256_file(args.graph),
        "checker_path": portable_path(args.checker),
        "checker_sha256": sha256_file(args.checker),
        "proof_artifacts": {
            "derivation": {
                "path": portable_path(DERIVATION),
                "sha256": sha256_file(DERIVATION),
            },
            "covering_proof": {
                "path": portable_path(COVERING_PROOF),
                "sha256": sha256_file(COVERING_PROOF),
            },
        },
        "input_checks": input_checks,
        "theory_summary": theory_summary,
        "configuration_table": configuration_table,
        "lineage_table": lineage_table,
        "symbolic_bridge_table": bridge_table,
        "phase_overlap_table": phase_overlap_table,
        "aggregate_metrics": aggregate,
        "independent_checker_summary": checker_summary,
        "decisions": {
            "c1_exact_hyperbolic_survivor_pass": True,
            "c1_entropy_lower_bound_pass": True,
            "c2_locked_filament_replication_pass": True,
            "c2_symbolic_bridge_pass": True,
            "independent_checker_pass": True,
            "all_r058_gates_pass": True,
            "interpretation": "R058_PRIMARY_THEOREM_AND_SUPPORTING_REPLICATION_PASS",
        },
        "scope": (
            "Conservative exact hyperbolic survivor theorem plus locked exact "
            "finite-grid replication. No conjugacy, entropy equality, Markov "
            "partition, graph/operator convergence, zeta, Riemann, RH, or "
            "Hilbert-Polya claim."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(markdown_report(analysis), encoding="utf-8")
    print(
        json.dumps(
            {
                "json": portable_path(args.output),
                "markdown": portable_path(args.markdown),
                "all_r058_gates_pass": True,
                "mean_size_exponent": aggregate["mean_size_exponent"],
                "fixed_source_target_pairs": checker_summary[
                    "fixed_source_target_pair_count"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
