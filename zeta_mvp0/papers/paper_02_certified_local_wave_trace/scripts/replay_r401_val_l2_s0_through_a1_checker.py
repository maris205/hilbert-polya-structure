#!/usr/bin/env python3
"""Read-only compatibility replay of the public S0 archive through A1 algebra.

This pre-freeze test never invokes the CAPD evaluator and never rewrites the
accepted S0 release.  It verifies the accepted hash manifest, adapts the six
old-format trees in memory, replays their shell/split DAGs with the formal A1
checker, and replays every one of the 3,016 archived node transcripts.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts/check_r401_val_l2_all_slabs_independent.py"
DEFAULT_S0 = ROOT / "results/r401_val_l2_s0_local_complement"
EXPECTED_PAIRS = tuple(
    (bits, slab) for bits in (128, 256) for slab in ("S000", "S025", "S050")
)


class ReplayError(RuntimeError):
    """The immutable S0 archive failed compatibility replay."""


def load_checker() -> Any:
    spec = importlib.util.spec_from_file_location("r401_val_l2_a1_replay_checker", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise ReplayError("cannot load the formal A1 checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayError(message)


def canonical_formal_node(
    checker: Any,
    tree_key: Any,
    old: Mapping[str, Any],
) -> dict[str, Any]:
    task = {
        "tree": tree_key.payload(),
        "node_id": str(old["node_id"]),
        "parent_id": old.get("parent_id"),
        "depth": int(old["depth"]),
        "epsilon": list(old["epsilon"]),
        "box": old["box"],
    }
    status = str(old["evaluator_status"])
    action = checker.status_action(
        status,
        old["returncode"],
        depth=int(old["depth"]),
        max_depth=40,
    )
    evaluator: dict[str, Any] = {
        "evaluator_status": status,
        "returncode": old["returncode"],
        "classification": action,
    }
    if action == "SPLIT":
        evaluator["split"] = {
            "coordinate": str(old["split_coordinate"]),
            "midpoint": str(old["split_midpoint"]),
            "children": list(old["children"]),
        }
    return {"task": task, "evaluator_result": evaluator}


def replay_tree(
    checker: Any,
    project_root: Path,
    s0: Path,
    tree_path: Path,
) -> tuple[int, Counter[str]]:
    old_tree = checker.strict_json_load(tree_path)
    bits = int(old_tree["precision_bits"])
    slab = str(old_tree["slab_id"])
    require((bits, slab) in EXPECTED_PAIRS, f"unexpected S0 tree identity: {bits}:{slab}")
    require(old_tree.get("complete") is True, f"incomplete S0 tree: {bits}:{slab}")
    require(old_tree.get("max_depth") == 40, f"unexpected S0 depth limit: {bits}:{slab}")
    require(old_tree.get("max_nodes") == 20_000, f"unexpected S0 node limit: {bits}:{slab}")
    tree_key = checker.TreeKey(bits, slab)
    old_nodes = old_tree.get("nodes")
    require(isinstance(old_nodes, list) and old_nodes, f"missing S0 nodes: {bits}:{slab}")
    formal_nodes = [canonical_formal_node(checker, tree_key, node) for node in old_nodes]
    formal_payload = {
        "schema_version": 1,
        "protocol_id": checker.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": checker.EXPECTED_PRODUCER_STATES["tree"],
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "tree": tree_key.payload(),
        "epsilon": list(old_tree["epsilon"]),
        "domain": {
            "big_box": old_tree["big_box"],
            "protected_exact_plan_box": old_tree["protected_l1_box"],
        },
        "per_tree_limits": {"max_depth": 40, "max_nodes": 20_000},
        "evaluated_node_count": len(formal_nodes),
        "terminal_counts": {
            "ENERGY_EXCLUDED": int(old_tree["terminal_counts"]["ENERGY_EXCLUDED"]),
            "RETURN_EXCLUDED": int(old_tree["terminal_counts"]["RETURN_EXCLUDED"]),
        },
        "nodes": formal_nodes,
    }
    plan = checker.load_plan(
        project_root / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
    )
    checker.verify_tree_structure(
        tree_key,
        formal_payload,
        plan[slab],
        max_depth=40,
        max_nodes=20_000,
    )

    counts: Counter[str] = Counter()
    for old, formal in zip(old_nodes, formal_nodes, strict=True):
        raw_relative = str(old["raw_file"])
        stderr_relative = str(old["stderr_file"])
        raw_path = checker.resolve_bound_path(s0, raw_relative)
        checker.resolve_bound_path(s0, stderr_relative)
        transcript = checker.Transcript(raw_path.read_text(encoding="utf-8"))
        task = formal["task"]
        status = transcript.scalar("status")
        require(status == old["evaluator_status"], f"status mismatch: {bits}:{slab}/{old['node_id']}")
        checker.verify_transcript_identity(transcript, task)
        checker.verify_energy_proof(transcript, status)
        if status in {
            "RETURN_EXCLUDED",
            "UNKNOWN",
            "ROOT_CANDIDATE",
            "INVALID_EXCLUSION_UNIQUENESS_CONFLICT",
        }:
            checker.verify_return_proof(transcript, status)
        counts[status] += 1
    return len(old_nodes), counts


def replay(project_root: Path, s0: Path) -> dict[str, Any]:
    checker = load_checker()
    s0 = s0.resolve()
    project_root = project_root.resolve()
    require(s0 == project_root / "results/r401_val_l2_s0_local_complement", "noncanonical S0 path")
    manifest = checker.strict_json_load(s0 / "manifest.json")
    release = checker.strict_json_load(s0 / "RELEASE_PROVENANCE.json")
    postcheck = checker.strict_json_load(s0 / "POSTCHECK_STATUS.json")
    require(manifest.get("protocol_id") == "R401-VAL-L2-S0", "wrong S0 manifest protocol")
    require(release.get("release_status") == "PASS_IMPLEMENTATION_SMOKE", "S0 release not accepted")
    require(postcheck.get("checker_status") == "PASS_INDEPENDENT_CHECKER", "S0 postcheck not accepted")
    require(release.get("final_status") is None and postcheck.get("final_status") is None, "S0 final status must be null")

    manifest_files = manifest.get("files")
    require(isinstance(manifest_files, Mapping), "S0 manifest has no file hash map")
    hash_checks = 0
    for relative, expected_hash in manifest_files.items():
        candidate = checker.resolve_bound_path(project_root, str(relative))
        require(checker.sha256(candidate) == expected_hash, f"S0 manifest hash mismatch: {relative}")
        hash_checks += 1

    expected_tree_paths = {
        s0 / "trees" / str(bits) / f"{slab}.json" for bits, slab in EXPECTED_PAIRS
    }
    actual_tree_paths = set((s0 / "trees").glob("*/*.json"))
    require(actual_tree_paths == expected_tree_paths, "S0 tree path matrix is not exact")

    total_nodes = 0
    status_counts: Counter[str] = Counter()
    tree_counts: list[dict[str, Any]] = []
    for bits, slab in EXPECTED_PAIRS:
        tree_path = s0 / "trees" / str(bits) / f"{slab}.json"
        node_count, counts = replay_tree(checker, project_root, s0, tree_path)
        total_nodes += node_count
        status_counts.update(counts)
        tree_counts.append(
            {
                "precision_bits": bits,
                "slab_id": slab,
                "node_count": node_count,
                "status_counts": dict(sorted(counts.items())),
            }
        )

    require(total_nodes == 3_016, f"unexpected S0 node total: {total_nodes}")
    require(
        status_counts
        == Counter({"UNKNOWN": 1_484, "RETURN_EXCLUDED": 1_349, "ENERGY_EXCLUDED": 183}),
        f"unexpected S0 status totals: {dict(status_counts)}",
    )
    return {
        "protocol_id": "R401-VAL-L2-A1-PREFREEZE-S0-REPLAY",
        "status": "PASS_S0_READ_ONLY_COMPATIBILITY_REPLAY",
        "source_release": "R401-VAL-L2-S0",
        "checker_source_sha256": checker.sha256(CHECKER_PATH),
        "adapter_source_sha256": checker.sha256(Path(__file__).resolve()),
        "s0_release_provenance_sha256": checker.sha256(s0 / "RELEASE_PROVENANCE.json"),
        "s0_manifest_sha256": checker.sha256(s0 / "manifest.json"),
        "s0_postcheck_sha256": checker.sha256(s0 / "POSTCHECK_STATUS.json"),
        "tree_count": 6,
        "node_count": total_nodes,
        "manifest_hash_checks": hash_checks,
        "status_counts": dict(sorted(status_counts.items())),
        "tree_counts": tree_counts,
        "claim_boundary": "public S0 compatibility replay only; no held-out A1 slab was read or evaluated",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--s0", type=Path, default=DEFAULT_S0)
    args = parser.parse_args()
    print(json.dumps(replay(args.project_root, args.s0), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
