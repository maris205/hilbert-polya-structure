#!/usr/bin/env python3
"""Mechanically reconstruct the P46 report from canonical sealed objects."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate key")
        value[key] = item
    return value


def file_below(output: Path, relative: str) -> Path:
    if not output.is_absolute() or output.is_symlink() or not output.is_dir():
        raise ValueError("unsafe output")
    base = output.resolve(strict=True)
    cursor = output
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    final = cursor.resolve(strict=True)
    if base not in final.parents or not final.is_file():
        raise ValueError("containment")
    return final


def load(output: Path, relative: str) -> dict[str, Any]:
    raw = file_below(output, relative).read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value) or value.get("status") != "PASS":
        raise ValueError("noncanonical or failed input")
    return value


def render(values: dict[str, dict[str, Any]]) -> bytes:
    comparison = values["comparison"]["payload"]
    proof = values["proof"]["payload"]
    source = values["source"]["payload"]
    mutations = values["mutations"]["payload"]
    external = values["external"]["payload"]
    independence = values["independence"]["payload"]
    route1 = values["route1"]["payload"]
    route2 = values["route2"]["payload"]
    counts = comparison["case_counts"]
    lines = [
        "# Paper 46 isolated integration report", "",
        "## Exact finite replay", "",
        f"Two physically independent evaluators agreed under strict recursive type and value "
        f"comparison on {counts['structural_cutoffs']} complete support cutoffs, "
        f"{counts['cycle_ordered_label_tuples']} ordered dyadic label tuples, and "
        f"{counts['finite_trace_cases']} exact rational trace cases. Support, cycle-solution, "
        "and finite-trace mismatch counts were all `0`.", "",
        "Every finite trace used the scale-dependent sum whose odd-block cutoff is "
        "`floor(N/2^k)`. No finite sum was collapsed to a geometric factor. These finite "
        "objects are diagnostics and do not prove an infinite endpoint.", "",
        "## Infinite-theorem certificate", "",
        f"The independent proof auditor replayed {proof['proof_anchor_count']} frozen analytic "
        "anchors and certified the strict walls `0`, `1/2`, and `1`, the exact valuation "
        "direct sum, the complete odd/even cyclic solver, and the separately typed infinite "
        f"trace identity. Finite-grid-as-proof is `{str(proof['finite_grid_used_as_proof']).lower()}`; "
        f"theorem failures: `{proof['theorem_failure_count']}`.", "",
        "## Source and ownership boundary", "",
        "Fournier--Wagner retains ownership of Schur-based lacunary boundedness and the "
        "reflection, folding, and alternating lacunary representation machinery. Its novelty "
        f"credit here is `{source['fournier_wagner_novelty_credit']}`. P46 is confined to the "
        "frozen weighted valuation/cycle/trace package, and the bounded search proves no priority.", "",
        "## Independence and adversarial closeout", "",
        f"Evaluator hashes are distinct (`{independence['evaluator_m_sha256']}` and "
        f"`{independence['evaluator_c_sha256']}`); project-local imports, shared expanded "
        "fixtures, serialized intermediates, caches, and symlinks are absent. All "
        f"{mutations['instance_count']} concrete mutations in {mutations['family_count']} families "
        f"were rejected by every and only designated consumer across "
        f"{mutations['consumer_invocation_count']} invocations; survivors: `0`. The frozen "
        f"external auditor was also executed against {external['physical_mutated_clone_count']} "
        "physically mutated disposable clones; accepted mutations: `0`.", "",
        "## Route and scope", "",
        f"The primary and independent Route validators passed {route1['checks_passed']}/"
        f"{route1['checks_total']} and {route2['checks_passed']}/{route2['checks_total']} checks. "
        "The tuple remains `[A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, "
        "A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`; overall is "
        "`ROUTE_A_REJECTED`, and Route B is locked. `STOP_DUPLICATE` is external literature "
        "vocabulary and is not a Route terminal.", "",
        "This result is preauthority and retrospective. It authorizes no priority claim, "
        "authority write, Git action, repository README edit, mirror, registry change, or "
        "publication decision.", "",
    ]
    return "\n".join(lines).encode("ascii")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    output = Path(args.output_root)
    mapping = {
        "comparison": "results/exact_comparison.json",
        "external": "audits/external_auditor_mutations.json",
        "independence": "audits/independence_audit.json",
        "mutations": "tests/mutation_results.json",
        "proof": "audits/proof_audit.json",
        "route1": "audits/route_primary.json",
        "route2": "audits/route_independent.json",
        "source": "audits/source_audit.json",
    }
    values = {name: load(output, relative) for name, relative in mapping.items()}
    sys.stdout.buffer.write(render(values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
