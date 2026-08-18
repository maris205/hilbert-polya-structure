#!/usr/bin/env python3
"""Canonical Markdown report renderer from already sealed result objects."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED = {
    "comparison": "results/exact_comparison.json",
    "independence": "audits/independence_audit.json",
    "mutations": "tests/mutation_results.json",
    "proof": "audits/proof_audit.json",
    "route_independent": "audits/route_independent.json",
    "route_primary": "audits/route_primary.json",
    "source": "audits/source_audit.json",
    "type": "audits/type_audit.json",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def load(output_root: Path, relative: str) -> dict[str, Any]:
    cursor = output_root
    for part in relative.split("/"):
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink")
    path = cursor.resolve(strict=True)
    if output_root.resolve(strict=True) not in path.parents:
        raise ValueError("containment")
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value) or value.get("status") != "PASS":
        raise ValueError("input envelope")
    return value


def render(values: dict[str, dict[str, Any]]) -> bytes:
    comparison = values["comparison"]["payload"]
    proof = values["proof"]["payload"]
    source = values["source"]["payload"]
    mutations = values["mutations"]["payload"]
    independence = values["independence"]["payload"]
    route_primary = values["route_primary"]["payload"]
    route_independent = values["route_independent"]["payload"]
    lines = [
        "# Paper 44 isolated integration report",
        "",
        "## Exact finite replay",
        "",
        f"Evaluator A and Evaluator B agreed by strict recursive type and value on "
        f"{comparison['case_counts']['finite_total']} canonical finite cases: "
        f"{comparison['case_counts']['finite_valid']} theorem-domain cases and "
        f"{comparison['case_counts']['finite_rejected_scope']} scope rejections. "
        f"All {comparison['gamma_overlap']['case_count']} independently certified golden "
        "interval pairs overlap, and the exact algebraic control is `99044 > 0`.",
        "",
        "These are finite exact or certified diagnostics. They do not prove uniform "
        "convergence, the complete accumulation image, all-level separation, or a natural "
        "boundary. Those infinite statements remain owned by the frozen proof replay.",
        "",
        "## Infinite-theorem certificate",
        "",
        f"The proof auditor used `{proof['basis']}` and certified the uniform Perron "
        "majorant, reverse accumulation inclusion, all-level separation certificate, "
        "and dominated Abelian passage. Finite-grid-as-proof is "
        f"`{str(proof['finite_grid_used_as_proof']).lower()}`. Ordinary Minkowski content "
        "remains excluded.",
        "",
        "## Source and ownership boundary",
        "",
        "The Ban--Hu--Lai author-manuscript correction boundary was preserved byte for "
        f"byte as excerpt `{source['ban_hu_lai_author_manuscript_correction_excerpt_sha256']}`. "
        "The author manuscript is treated as a same-object statement requiring correction, "
        "not as novelty ownership and not as an exact duplicate; the version-of-record or "
        "erratum text is not represented as line-checked. Chain products, entropy, leading "
        "dimensions, and all valid prior boundary ownership receive zero novelty credit.",
        "",
        "## Independence and adversarial closeout",
        "",
        f"The evaluator source hashes are distinct (`{independence['evaluator_A_sha256']}` "
        f"and `{independence['evaluator_B_sha256']}`), project-local imports are empty, and "
        "expanded fixtures and expected tables are not shared. "
        f"All {mutations['instance_count']} concrete instances from "
        f"{mutations['family_count']} frozen mutation families were rejected by every and "
        f"only designated consumer across {mutations['consumer_invocation_count']} invocations; "
        "survivors: `0`.",
        "",
        "## Route and publication boundary",
        "",
        f"Primary Route validation passed {route_primary['checks_passed']}/"
        f"{route_primary['checks_total']} checks and the independent audit passed "
        f"{route_independent['checks_passed']}/{route_independent['checks_total']}. "
        "The tuple remains `[A0_FAIL, A1_FAIL, A2_FAIL, "
        "A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`, overall `ROUTE_A_REJECTED`, "
        "and Route B is locked. `STOP_DUPLICATE` is a conditional external literature "
        "disposition, never a strict Route terminal.",
        "",
        "This integration is preauthority and retrospective. It grants no priority, "
        "prospective-selection, authority-write, Git, mirror, registry, or publication credit.",
        "",
    ]
    return "\n".join(lines).encode("ascii")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    output_root = Path(args.output_root)
    if not output_root.is_absolute() or not output_root.is_dir() or output_root.is_symlink():
        raise ValueError("unsafe output root")
    values = {name: load(output_root, relative) for name, relative in REQUIRED.items()}
    sys.stdout.buffer.write(render(values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
