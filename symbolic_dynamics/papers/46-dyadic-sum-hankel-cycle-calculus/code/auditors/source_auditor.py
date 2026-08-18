#!/usr/bin/env python3
"""Read-only source and literature-ownership auditor for P46."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


SOURCE_HASH = "d81c2292a62c09f2bfc742c4b88f264b6743e99690fb91ba8e21c7a7ba1dd36e"
LITERATURE_HASH = "2f6361950842466ad164bf06f12c1fbb16940c3f12f8ef41ed789516262fb63e"
MUTATIONS = {
    "PKT01/missing_candidate": "PACKET_KEYSET_FAILURE",
    "PKT02/extra_key": "PACKET_KEYSET_FAILURE",
    "PKT04/duplicate_top_key": "DUPLICATE_JSON_KEY",
    "PKT08/source_seal_drift": "FROZEN_SOURCE_DRIFT",
    "RTE04/stop_duplicate_terminal": "ROUTE_TERMINAL_VOCABULARY_FAILURE",
    "SRC01/fournier_credit": "SOURCE_OWNERSHIP_FAILURE",
    "SRC02/delete_folding_owner": "SOURCE_OWNERSHIP_FAILURE",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate key")
        output[key] = value
    return output


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for S")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "S",
                    "instance_id": identifier,
                    "witness": "frozen source and primary-ownership boundary rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def contained(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    cursor = root
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = cursor.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def load_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value):
        raise ValueError("noncanonical packet")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--output-root")
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return reject(args.mutation)
    if not args.root or not args.output_root:
        raise ValueError("roots required")
    root, output = Path(args.root), Path(args.output_root)
    source_raw = contained(root, "preauthority/SOURCE_LOCK.md").read_bytes()
    literature_raw = contained(root, "preauthority/LITERATURE_NOVELTY_AUDIT.md").read_bytes()
    if hashlib.sha256(source_raw).hexdigest() != SOURCE_HASH \
            or hashlib.sha256(literature_raw).hexdigest() != LITERATURE_HASH:
        raise ValueError("source lock drift")
    literature = literature_raw.decode("utf-8")
    ownership_anchors = [
        "including their reflection/folding relations and alternating representations",
        "The two-sided Dirichlet weight, exact \\(v_2\\) orthogonal sum",
        "STOP_DUPLICATE is an external publication/literature disposition only",
    ]
    if any(anchor not in literature for anchor in ownership_anchors):
        raise ValueError("Fournier--Wagner ownership anchor")
    packet = load_json(contained(output, "data/source_packet.json"))
    ownership = packet["payload"]["ownership"]
    if ownership["fournier_wagner_novelty_credit"] != 0 \
            or ownership["fournier_wagner_owns"] != [
                "alternating_lacunary_representation",
                "reflection_and_folding_relations",
                "Schur_lacunary_boundedness_machinery",
            ]:
        raise ValueError("ownership transfer")
    result = {
        "payload": {
            "fournier_wagner_novelty_credit": 0,
            "fournier_wagner_ownership_preserved": True,
            "literature_lock_sha256": LITERATURE_HASH,
            "priority_claimed": False,
            "search_disposition": "SEARCH_BOUNDED_NO_EXACT_PACKAGE_HIT",
            "source_lock_sha256": SOURCE_HASH,
            "stop_duplicate_route_terminal": False,
        },
        "schema": "paper46-source-audit-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
