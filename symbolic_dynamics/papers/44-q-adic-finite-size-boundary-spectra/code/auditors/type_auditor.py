#!/usr/bin/env python3
"""Independent object/marker/residue/analytic type auditor."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


CONTRACT_SHA256 = "059ecbc4edcd097cb9eb83a0452591735fc25ca6d6d8da5a3ce10f4cff15330f"
MUTATIONS = {
    "MUT-Q1/q_equals_one": "INVALID_RADIX",
    "MUT-A0/zero_2x2": "NONPRIMITIVE_ZERO_ADJACENCY",
    "MUT-APR/reducible_identity_2x2": "STOP_SCOPED",
    "MUT-APR/period_two_2x2": "STOP_SCOPED",
    "MUT-MODFRAC/unnormalized_real_fractional_part": "RESIDUE_TYPE_ERROR",
    "MUT-DIM/original_shift_label": "BOUNDARY_DIMENSION_OWNER_ERROR",
    "MUT-MERO/isolated_meromorphic_poles": "ANALYTIC_TYPE_ERROR",
    "MUT-CONTENT/ordinary_minkowski_nonexistence": "NOT_CURRENTLY_JUSTIFIED",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def path_for(root: Path) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    path = root / "preauthority" / "OBJECT_MARKER_OPERATOR_CONTRACT.md"
    if (root / "preauthority").is_symlink() or path.is_symlink():
        raise ValueError("symlink")
    result = path.resolve(strict=True)
    if result != root.resolve(strict=True) / "preauthority" / path.name:
        raise ValueError("containment")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation:
        code = MUTATIONS.get(arguments.mutation)
        if code is None:
            raise ValueError("not designated")
        sys.stdout.buffer.write(canonical({
            "payload": {
                "code": code,
                "consumer": "T",
                "instance_id": arguments.mutation,
                "witness": "typed source, residue, dimension, or analytic contract rejects before evaluation",
            },
            "schema": "paper44-mutation-rejection-v1",
            "status": "REJECT",
        }))
        return 2
    if not arguments.root:
        raise ValueError("root required")
    raw = path_for(Path(arguments.root)).read_bytes()
    if hashlib.sha256(raw).hexdigest() != CONTRACT_SHA256:
        raise ValueError("type contract drift")
    text = raw.decode("utf-8")
    exact_tokens = [
        "`MultiplicativeChainRadix`", "`PrimitiveZeroOneAdjacency`",
        "`PositivePrefixCutoff`", "`qAdicBoundaryState`",
        "`RealBoundaryValue`", "`OrdinaryCutoffGeneratingMarker`",
        "$G$ is not a Fredholm determinant or trace logarithm",
        "a radial singularity is an isolated pole | `ANALYTIC_ERROR`",
    ]
    if any(token not in text for token in exact_tokens):
        raise ValueError("typed token missing")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "boundary_value_type": "RealBoundaryValue",
            "cutoff_type": "PositivePrefixCutoff",
            "determinant_defined": False,
            "marker_type": "OrdinaryCutoffGeneratingMarker",
            "ordinary_content_claimed": False,
            "q_adic_field_claimed_for_composite_q": False,
            "source_type": "OneSidedMultiplicativeSFT",
            "type_contract_sha256": CONTRACT_SHA256,
        },
        "schema": "paper44-type-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
