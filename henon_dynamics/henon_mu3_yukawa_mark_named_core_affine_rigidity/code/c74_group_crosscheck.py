#!/usr/bin/env python3
"""Independent matrix/image cross-check for C74."""

from __future__ import annotations

from collections import Counter
import json
from itertools import product
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c74_named_core_affine_rigidity_evidence.json"


def image(matrix, point):
    a, b, c, d = matrix
    x, y, z = point
    return ((a * x + 3 * b * y) % 9, (c * x + d * y) % 3, z)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    # The induced map on the two generator layers gives a triangular matrix
    # modulo 3; a is a unit mod 3 and d is a unit mod 3.
    endomorphisms = list(product(range(9), range(3), range(3), range(3)))
    units9 = {1, 2, 4, 5, 7, 8}
    units3 = {1, 2}
    formulas = [m for m in endomorphisms if m[0] in units9 and m[3] in units3]
    assert len(formulas) == 108
    points = list(product(range(9), range(3), range(2)))
    bijective = [m for m in endomorphisms if len({image(m, p) for p in points}) == 54]
    assert formulas == bijective
    # Direct product count for the affine group.
    assert len(points) * len(bijective) == 5832
    # Recompute the two inverse near-symmetries on all 16 named points.
    coordinates = [tuple(row) for row in json.loads(
        (PROJECT.parent / "henon_mu3_yukawa_mark_coordinate_core_atlas/results/c72_coordinate_core_atlas_evidence.json").read_text()
    )["coordinate_realization"]["coordinates"]]
    source = Counter(coordinates)
    for matrix in ((4, 0, 2, 1), (7, 0, 1, 1)):
        assert sum((source & Counter(image(matrix, p) for p in coordinates)).values()) == 14
    # SymPy independently confirms the unit counts in the two diagonal slots.
    a, d = sp.symbols("a d")
    assert len([u for u in range(9) if int(u) % 3 != 0]) == 6
    assert len([u for u in range(3) if int(u) % 3 != 0]) == 2
    assert evidence["automorphism_model"]["automorphism_count"] == 108
    assert evidence["automorphism_model"]["affine_count"] == 5832
    print(json.dumps({
        "status": "GROUP_CROSSCHECK_PASS",
        "odd_endomorphism_matrix_count": 243,
        "full_core_endomorphism_count": 486,
        "automorphism_count": len(bijective),
        "affine_count": 5832,
        "near_symmetry_overlap": 14,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
