#!/usr/bin/env python3
"""Source-only fixtures for Paper 38.

This module freezes presentations and audit inputs.  It deliberately contains
no evaluator import, no orbit-count formula, no determinant formula, no
trace-class decision, and no target arithmetic support.
"""

from __future__ import annotations

import json
import random
import sys
from typing import Dict, List


INVERSE = {"u": "U", "U": "u", "v": "V", "V": "v"}


def bs_relator(p: int, q: int) -> str:
    """Return v u^p V U^q, the standard BS(p,q) cyclic relator."""
    return "v" + "u" * p + "V" + "U" * q


def random_cyclically_reduced_word(
    rng: random.Random, length: int
) -> str:
    letters = tuple(INVERSE)
    while True:
        word: List[str] = []
        for _ in range(length):
            allowed = [x for x in letters if not word or x != INVERSE[word[-1]]]
            word.append(rng.choice(allowed))
        if word[0] != INVERSE[word[-1]]:
            return "".join(word)


def build_fixture() -> Dict[str, object]:
    parameter_rows = [
        {"r": 1, "declared_class": "balanced_control"},
        {"r": 2, "declared_class": "prime_control"},
        {"r": 3, "declared_class": "prime_control"},
        {"r": 4, "declared_class": "composite_baseline"},
        {"r": 5, "declared_class": "prime_control"},
        {"r": 6, "declared_class": "composite_control"},
        {"r": 7, "declared_class": "prime_control"},
        {"r": 8, "declared_class": "composite_control"},
        {"r": 9, "declared_class": "composite_control"},
        {"r": 10, "declared_class": "composite_control"},
        {"r": 12, "declared_class": "composite_control"},
    ]

    gbs_pairs = [
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (1, 8),
        (2, 1),
        (3, 1),
        (4, 1),
        (2, 2),
        (2, 3),
        (2, 5),
        (3, 4),
        (3, 5),
        (4, 6),
        (5, 7),
    ]
    gbs_controls = [
        {
            "control_id": f"GBS_{p}_{q}",
            "relator": bs_relator(p, q),
            "source_p": p,
            "source_q": q,
        }
        for p, q in gbs_pairs
    ]

    rng = random.Random(380038)
    random_relators = [
        {
            "control_id": f"R{i:02d}",
            "relator": random_cyclically_reduced_word(rng, rng.randint(6, 14)),
        }
        for i in range(64)
    ]

    marker_rows = []
    for r in (1, 2, 4, 5, 6):
        marker_rows.append(
            {
                "r": r,
                "words": [
                    {"name": "stable_letter", "word": "v"},
                    {"name": "elliptic_base", "word": "u" * (r + 2)},
                    {"name": "same_tree_step_a", "word": "v"},
                    {"name": "same_tree_step_b", "word": "u" * (r + 1) + "v"},
                    {"name": "defining_relator", "word": bs_relator(1, r)},
                    {"name": "stable_power", "word": "v" * (r + 1)},
                ],
            }
        )

    return {
        "schema": "paper38-source-fixture-v1",
        "candidate_id": "SD-C40",
        "object": {
            "group": "BS(1,r)",
            "splitting": "original ascending HNN splitting over Z",
            "symbolic_object": "full oriented-edge geodesic shift on the Bass-Serre tree",
            "coefficient": "canonical HNN modular cocycle only",
            "new_object": True,
            "inherits_same_object_credit": False,
            "inherits_same_marker_credit": False,
        },
        "parameter_rows": parameter_rows,
        "gbs_controls": gbs_controls,
        "random_relators": random_relators,
        "marker_rows": marker_rows,
        "limits": {
            "necklace_length_max": 12,
            "explicit_residue_r_max": 5,
            "explicit_residue_k_max": 6,
            "formal_series_degree": 12,
            "noncompact_columns": [1, 2, 4, 8, 16, 32],
            "finite_tree_checks": [
                {"branching": 1, "depth": 8, "walk_length": 10},
                {"branching": 2, "depth": 5, "walk_length": 8},
                {"branching": 3, "depth": 4, "walk_length": 7},
            ],
        },
        "random_seed": 380038,
        "source_oracle_declaration": {
            "prime_or_factor_table_used_by_mechanism": False,
            "accepted_support_table": False,
            "target_coefficients": False,
            "target_zeros": False,
            "network_oracle": False,
            "arbitrary_representation": False,
        },
    }


def main() -> int:
    json.dump(build_fixture(), sys.stdout, sort_keys=True, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
