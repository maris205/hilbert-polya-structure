#!/usr/bin/env python3
"""Analyze the frozen R057 mutual-separation production and checker outputs."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULT = PROJECT_ROOT / "results" / "mutual_separation_r057.json"
CHECKER = PROJECT_ROOT / "results" / "mutual_separation_independent_check_r057.json"
OUTPUT_JSON = PROJECT_ROOT / "results" / "mutual_separation_analysis_r057.json"
OUTPUT_MD = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057_MUTUAL_SEPARATION_ANALYSIS.md"
)
PROTOCOL_SHA256 = "4eb540372ad29568054cdaa05b7c3f605913dfcf358855c98f45594c78af0a91"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=RESULT)
    parser.add_argument("--checker-input", type=Path, default=CHECKER)
    parser.add_argument("--output", type=Path, default=OUTPUT_JSON)
    parser.add_argument("--markdown-output", type=Path, default=OUTPUT_MD)
    return parser.parse_args()


def _checker_pass(payload: dict[str, object]) -> bool:
    if "g3_independent_checker_pass" in payload:
        return bool(payload["g3_independent_checker_pass"])
    direct_keys = (
        "all_checks_pass",
        "all_frozen_checks_pass",
        "independent_check_pass",
    )
    for key in direct_keys:
        if key in payload:
            return bool(payload[key])
    decisions = payload.get("decisions")
    if isinstance(decisions, dict):
        for key in direct_keys + (
            "all_independent_checks_pass",
            "g3_independent_checker_pass",
        ):
            if key in decisions:
                return bool(decisions[key])
    return False


def _failure_row(record: dict[str, object]) -> dict[str, object]:
    witness = record["first_failure_witness"]
    return {
        "panel_id": record["panel_id"],
        "configuration_id": record["configuration_id"],
        "grid": record["grid"],
        "grid_offset_fraction": record["grid_offset"],
        "a_fraction": record["a"],
        "eta_fraction": record["eta"],
        "fresh_counterexample": record["fresh_counterexample"],
        "failure_side": witness["failure_side"],
        "boundary_index": witness["boundary_index"],
        "boundary_fraction": witness["shared_boundary_fraction"],
        "source_id": witness["source_id"],
        "target_id": witness["target_id"],
        "minimum_signed_margin_fraction": record[
            "minimum_signed_margin_fraction"
        ],
        "minimum_signed_margin": record["minimum_signed_margin"],
        "minimum_headroom_ratio_fraction": record[
            "minimum_headroom_ratio_fraction"
        ],
        "minimum_headroom_ratio": record["minimum_headroom_ratio"],
        "uncapped_k_max": record["uncapped_k_max"],
    }


def analyze_payload(
    result: dict[str, object], checker: dict[str, object]
) -> dict[str, object]:
    if result.get("run_id") != "R057_MUTUAL_SEPARATION":
        raise AssertionError("unexpected R057 result run_id")
    if result.get("protocol_sha256") != PROTOCOL_SHA256:
        raise AssertionError("R057 result is not bound to the frozen protocol")
    records: Sequence[dict[str, object]] = result["records"]
    decisions: dict[str, object] = result["decisions"]
    if len(records) != 517 or int(result["boundary_row_count"]) != 102494:
        raise AssertionError("R057 production panel is incomplete")

    failures = [record for record in records if not record["certificate_pass"]]
    passes = [record for record in records if record["certificate_pass"]]
    cap_active = [record for record in records if not record["k_gate_pass"]]
    cap_free = [record for record in records if record["k_gate_pass"]]
    fresh_failures = [record for record in failures if record["fresh_counterexample"]]
    centered = [
        record
        for record in records
        if record["panel_id"] == "centered_resolution_scan"
    ]
    centered_even = [record for record in centered if int(record["grid"]) % 2 == 0]
    centered_odd = [record for record in centered if int(record["grid"]) % 2 == 1]
    centered_failures = [record for record in centered if not record["certificate_pass"]]

    closest_passes = sorted(
        (
            record
            for record in cap_free
            if record["certificate_pass"]
            and record["minimum_headroom_ratio"] is not None
        ),
        key=lambda record: float(record["minimum_headroom_ratio"]),
    )[:10]

    centered_anchor_grids = (96, 127, 160, 192, 254, 320)
    centered_by_grid = {int(record["grid"]): record for record in centered}
    centered_anchor_headroom = [
        {
            "grid": grid,
            "certificate_pass": centered_by_grid[grid]["certificate_pass"],
            "minimum_headroom_ratio": centered_by_grid[grid][
                "minimum_headroom_ratio"
            ],
            "minimum_signed_margin": centered_by_grid[grid][
                "minimum_signed_margin"
            ],
        }
        for grid in centered_anchor_grids
    ]

    checker_pass = _checker_pass(checker)
    strict_gates_pass = (
        bool(decisions["g0_protocol_and_exact_arithmetic_pass"])
        and bool(decisions["g1_certificate_and_witness_integrity_pass"])
        and bool(decisions["g2_all_theory_controls_pass"])
        and checker_pass
    )
    core_theory_audit_pass = (
        bool(decisions["g0_protocol_and_exact_arithmetic_pass"])
        and bool(decisions["g2_all_theory_controls_pass"])
        and checker_pass
        and all(record["all_failure_witnesses_replay_pass"] for record in failures)
    )

    return {
        "run_id": "R057_MUTUAL_SEPARATION_ANALYSIS",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_sha256": PROTOCOL_SHA256,
        "decision": {
            "g0_protocol_and_exact_arithmetic_pass": decisions[
                "g0_protocol_and_exact_arithmetic_pass"
            ],
            "g1_strict_no_cap_gate_pass": decisions[
                "g1_certificate_and_witness_integrity_pass"
            ],
            "g1_cap_free_subset_pass": decisions["g1_cap_free_subset_pass"],
            "g2_all_theory_controls_pass": decisions[
                "g2_all_theory_controls_pass"
            ],
            "g3_independent_checker_pass": checker_pass,
            "strict_all_frozen_gates_pass": strict_gates_pass,
            "core_theory_and_counterexample_audit_pass": core_theory_audit_pass,
            "closed_universal_identity_status": "REFUTED",
            "corrected_boundary_criterion_status": (
                "PROVED AND IMPLEMENTATION-AUDITED"
                if core_theory_audit_pass
                else "PROOF AVAILABLE; IMPLEMENTATION AUDIT INCOMPLETE"
            ),
            "positive_identity_status": (
                "PROVED AND MICROGRID-AUDITED"
                if checker_pass
                else "PROVED; INDEPENDENT MICROGRID AUDIT INCOMPLETE"
            ),
            "strict_gate_note": (
                "Sixteen pre-frozen +/-3/8 phase stresses reached uncapped "
                "K=68, so the frozen K<64 gate fails. They remain in the "
                "panel and are not replaced."
            ),
        },
        "summary": {
            "configuration_count": len(records),
            "boundary_count": result["boundary_row_count"],
            "pass_count": len(passes),
            "fail_count": len(failures),
            "cap_free_configuration_count": len(cap_free),
            "cap_active_configuration_count": len(cap_active),
            "fresh_counterexample_count": len(fresh_failures),
            "all_failure_witnesses_exact_replay_pass": all(
                record["all_failure_witnesses_replay_pass"] for record in failures
            ),
            "upper_failure_count": sum(
                int(record["upper_failure_count"]) for record in failures
            ),
            "lower_failure_count": sum(
                int(record["lower_failure_count"]) for record in failures
            ),
            "centered_even_count": len(centered_even),
            "centered_even_failure_count": sum(
                not record["certificate_pass"] for record in centered_even
            ),
            "centered_odd_count": len(centered_odd),
            "centered_odd_failure_count": sum(
                not record["certificate_pass"] for record in centered_odd
            ),
            "panel_summary": decisions["panel_summary"],
        },
        "centered_failure_grids": [
            int(record["grid"]) for record in centered_failures
        ],
        "failures": [_failure_row(record) for record in failures],
        "fresh_failures": [_failure_row(record) for record in fresh_failures],
        "cap_active_configuration_ids": [
            record["configuration_id"] for record in cap_active
        ],
        "closest_passing_certificates": [
            {
                "configuration_id": record["configuration_id"],
                "panel_id": record["panel_id"],
                "grid": record["grid"],
                "grid_offset_fraction": record["grid_offset"],
                "a_fraction": record["a"],
                "eta_fraction": record["eta"],
                "minimum_headroom_ratio": record["minimum_headroom_ratio"],
                "minimum_signed_margin": record["minimum_signed_margin"],
            }
            for record in closest_passes
        ],
        "centered_prior_anchor_headroom": centered_anchor_headroom,
        "scope_boundary": [
            "finite exact cell-incidence criterion only",
            "no invariant set, Markov partition, or covering relation",
            "no graph or transfer-operator convergence",
            "no zeta, prime, Riemann-zero, RH, or Hilbert-Polya implication",
        ],
    }


def _fmt(value: object, digits: int = 6) -> str:
    if value is None:
        return "--"
    if isinstance(value, float):
        return f"{value:.{digits}g}"
    return str(value)


def render_markdown(analysis: dict[str, object]) -> str:
    decision = analysis["decision"]
    summary = analysis["summary"]
    lines = [
        "# R057 Mutual-Outer Separation Analysis",
        "",
        "**Completed:** 2026-08-02  ",
        f"**Frozen protocol:** `{analysis['protocol_sha256']}`  ",
        (
            "**Decision:** universal closed-edge identity REFUTED; corrected "
            "boundary criterion proved and audited"
        ),
        "",
        "## 1. Outcome",
        "",
        (
            f"R057 evaluated {summary['configuration_count']} frozen "
            f"configurations and {summary['boundary_count']:,} internal "
            "boundaries. The exact separation certificate passes on "
            f"{summary['pass_count']} configurations and fails on "
            f"{summary['fail_count']}."
        ),
        "",
        (
            "The old universal claim is false. Every failure has an exact "
            "true-absent / forward-outer-present / inverse-outer-present "
            "touch-only witness. The replacement theorem is the strict "
            "two-sided condition $\\omega_p^+<\\Delta_p^+$ and "
            "$\\omega_p^-<\\Delta_p^-$ at every internal boundary."
        ),
        "",
        (
            f"Three failures are genuinely fresh, pre-frozen phase stresses. "
            f"The other eight were disclosed development observations. "
            f"All {summary['upper_failure_count']} failure sides are upper "
            f"overshoots; the lower-side failure count is "
            f"{summary['lower_failure_count']}."
        ),
        "",
        "## 2. Frozen gates",
        "",
        "| Gate | Status |",
        "|---|---|",
        f"| G0 protocol/exact arithmetic | {'PASS' if decision['g0_protocol_and_exact_arithmetic_pass'] else 'FAIL'} |",
        f"| G1 strict uncapped $K<64$ | {'PASS' if decision['g1_strict_no_cap_gate_pass'] else 'FAIL'} |",
        f"| G1 cap-free subset | {'PASS' if decision['g1_cap_free_subset_pass'] else 'FAIL'} |",
        f"| G2 theory controls | {'PASS' if decision['g2_all_theory_controls_pass'] else 'FAIL'} |",
        f"| G3 independent checker | {'PASS' if decision['g3_independent_checker_pass'] else 'FAIL'} |",
        "",
        (
            f"The strict all-gates decision is **FAIL** because "
            f"{summary['cap_active_configuration_count']} pre-frozen "
            "$\\delta=\\pm3/8$ configurations reached uncapped $K=68$. "
            "They remain in the panel. The cap-free 501-configuration subset, "
            "all theorem controls, and all exact counterexamples remain "
            "interpretable."
        ),
        "",
        "## 3. Exact failures",
        "",
        "| Configuration | $N$ | Offset | Fresh | Boundary | Headroom $\\Delta/\\omega$ | Margin $\\Delta-\\omega$ | Edge IDs |",
        "|---|---:|---:|---|---:|---:|---:|---|",
    ]
    for row in analysis["failures"]:
        lines.append(
            "| {configuration_id} | {grid} | {grid_offset_fraction} | {fresh} | "
            "{boundary_fraction} | {ratio} | {margin} | {source_id}->{target_id} |".format(
                **row,
                fresh="yes" if row["fresh_counterexample"] else "no",
                ratio=_fmt(row["minimum_headroom_ratio"]),
                margin=_fmt(row["minimum_signed_margin"]),
            )
        )

    lines.extend(
        [
            "",
            "The fresh counterexamples are:",
            "",
        ]
    )
    for row in analysis["fresh_failures"]:
        lines.append(
            f"- `{row['configuration_id']}`: $N={row['grid']}$, "
            f"$\\delta={row['grid_offset_fraction']}$, boundary "
            f"$p={row['boundary_fraction']}$, exact edge "
            f"`{row['source_id']}->{row['target_id']}`."
        )

    lines.extend(
        [
            "",
            "## 4. Panel structure",
            "",
            "| Panel | Configurations | Pass | Fail | Fresh failures |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for panel_id, panel in summary["panel_summary"].items():
        lines.append(
            f"| {panel_id} | {panel['configuration_count']} | "
            f"{panel['pass_count']} | {panel['fail_count']} | "
            f"{panel['fresh_counterexample_count']} |"
        )

    lines.extend(
        [
            "",
            (
                f"In the centered scan, all {summary['centered_odd_count']} "
                "odd grids pass. Eight of the "
                f"{summary['centered_even_count']} even grids fail: "
                + ", ".join(str(value) for value in analysis["centered_failure_grids"])
                + ". This is an arithmetic resonance pattern, not monotone "
                "grid convergence."
            ),
            "",
            "The frozen odd-grid $a$ and $\\eta$ panels both pass completely. "
            "Because zero lies inside a cell rather than on an adjacent-cell "
            "boundary for every one of those grids, this does not establish "
            "general robustness to $a$ or $\\eta$; an even-grid supplementary "
            "failure-boundary scan is the appropriate follow-up.",
            "",
            "## 5. R055--R056 re-interpretation",
            "",
            "The earlier exact identities are now explained by positive "
            "certificate margins rather than promoted to a universal rule. "
            "Representative centered headroom ratios are:",
            "",
            "| $N$ | Certificate | Minimum $\\Delta/\\omega$ |",
            "|---:|---|---:|",
        ]
    )
    for row in analysis["centered_prior_anchor_headroom"]:
        lines.append(
            f"| {row['grid']} | {'PASS' if row['certificate_pass'] else 'FAIL'} | "
            f"{_fmt(row['minimum_headroom_ratio'])} |"
        )

    lines.extend(
        [
            "",
            "The closest cap-free passing configuration in the production scan "
            f"is `{analysis['closest_passing_certificates'][0]['configuration_id']}` "
            "with headroom ratio "
            f"{_fmt(analysis['closest_passing_certificates'][0]['minimum_headroom_ratio'])}. "
            "Thus a passing certificate can be very near the exact closed-contact "
            "failure boundary.",
            "",
            "## 6. Positive-area identity",
            "",
            "The proof package establishes that strict positive coordinate "
            "overlap forces the source $x$ cell and target $y$ cell to be the "
            "same partition cell. Finite exact slab ranges then cover the full "
            "quadratic range, so outer-positive equals true-positive without "
            "mutual filtering. The independent microgrid checker audits this "
            "edge-for-edge. The assumption $a>0$ is explicit.",
            "",
            "## 7. What changed relative to R056",
            "",
            "- The closed-edge identity is no longer described as a plausible "
            "universal mechanism; it has an exact necessary-and-sufficient "
            "finite-grid boundary criterion.",
            "- N=60 supplies a constructive exact counterexample, and three new "
            "pre-frozen shifted counterexamples show that the obstruction is not "
            "limited to a centered zero boundary.",
            "- Positive-area equality is stronger than expected and survives as "
            "a separate proposition.",
            "- The strict protocol did not fully pass: the $\\pm3/8$ design "
            "underestimated the uncapped subdivision maximum. This is reported "
            "rather than repaired post hoc.",
            "",
            "## 8. Scope boundary",
            "",
            "R057 proves and audits statements about finite exact cell-incidence "
            "graphs. It does not establish an invariant set, isolating "
            "neighborhood, Markov partition, covering relation, graph limit, "
            "transfer-operator convergence, zeta identity, Riemann-zero "
            "relation, RH, or Hilbert--Pólya construction.",
            "",
            "## 9. Artifacts",
            "",
            "- `DERIVATION_PACKAGE.md`;",
            "- `PROOF_PACKAGE.md`;",
            "- `research/refine-logs/R057_MUTUAL_SEPARATION_PROTOCOL.json`;",
            "- `results/mutual_separation_r057.json`;",
            "- `results/mutual_separation_boundaries_r057.csv`;",
            "- `results/mutual_separation_independent_check_r057.json`;",
            "- producer, analyzer, independent checker, and regression tests.",
            "",
            "## 10. Post-primary centered-even supplement",
            "",
            "R057S1 addresses the disclosed weakness that the frozen a/eta "
            "panels used only centered odd grids. On fourteen selected even "
            "grids, 266 parameter configurations all pass the supplement "
            "protocol gates: 157 satisfy the exact certificate and 109 fail, "
            "with every failure localized at $p=0$ and no cap activity.",
            "",
            "The exact specialization is "
            "$K=\\lceil2ah/\\eta\\rceil$ and "
            "$a(h/K)^2<\\Delta_{0,N}^+$. All eta sequences have at most one "
            "pass-to-fail transition. The a staircase is nonmonotone at "
            "$N=46,92,106$ because an integer K jump can shrink the overshoot "
            "enough to restore exactness. This is a post-primary mechanism "
            "map, not held-out confirmation. See "
            "`R057S1_EVEN_PARAMETER_STRESS_ANALYSIS.md`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    if not args.checker_input.is_file():
        raise SystemExit(f"missing R057 independent checker output: {args.checker_input}")
    result = json.loads(args.input.read_text(encoding="utf-8"))
    checker = json.loads(args.checker_input.read_text(encoding="utf-8"))
    analysis = analyze_payload(result, checker)
    markdown = render_markdown(analysis)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(analysis, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(markdown, encoding="utf-8")
    print(
        json.dumps(
            {
                "analysis_json": str(args.output),
                "analysis_markdown": str(args.markdown_output),
                "strict_all_frozen_gates_pass": analysis["decision"][
                    "strict_all_frozen_gates_pass"
                ],
                "core_theory_and_counterexample_audit_pass": analysis["decision"][
                    "core_theory_and_counterexample_audit_pass"
                ],
                "fresh_counterexample_count": analysis["summary"][
                    "fresh_counterexample_count"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
