#!/usr/bin/env python3
"""SymPy and finite-lattice cross-checks for the C85 receipt."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c85_threshold_vector_poset_rigidity_evidence.json"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json"
EXPECTED = "22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152"
C75_EXPECTED = "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def main() -> None:
    raw = EVIDENCE.read_bytes()
    assert sha256(raw).hexdigest() == EXPECTED
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL

    vector_rows = evidence["rigidity"]["vector_rows"]
    vectors = sp.Matrix([row["threshold_vector"] for row in vector_rows])
    inclusion = sp.Matrix(evidence["poset"]["inclusion_matrix"])
    coordinatewise = sp.Matrix(evidence["poset"]["coordinatewise_ge_matrix"])
    assert vectors.shape == inclusion.shape == coordinatewise.shape == (20, 20)
    assert inclusion == coordinatewise
    zero_incidence = sp.Matrix(20, 20, lambda closed, target: int(vectors[closed, target] == 0))
    assert zero_incidence == inclusion.T

    # C75's subgroup order is a linear extension, so the zeta matrix is
    # unitriangular.  Its exact integer inverse is the finite-poset Möbius matrix.
    assert inclusion.det() == 1
    mobius = inclusion.inv()
    assert all(value.is_Integer for value in mobius)
    assert inclusion * mobius == sp.eye(20)

    c75_raw = C75.read_bytes()
    assert sha256(c75_raw).hexdigest() == C75_EXPECTED
    c75 = json.loads(c75_raw)
    subgroups = [
        frozenset(tuple(point) for point in row["subgroup_points"])
        for row in c75["closure_incidence"]["all_subgroups"]
    ]
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}
    assert len(subgroup_index) == 20
    meet_join_pairs = 0
    for left in subgroups:
        for right in subgroups:
            meet = left & right
            join = frozenset(add(x, y) for x in left for y in right)
            assert meet in subgroup_index
            assert join in subgroup_index
            meet_join_pairs += 1
    assert meet_join_pairs == 400

    z = sp.symbols("z")
    spectrum = {int(size): count for size, count in evidence["rigidity"]["fibre_spectrum"].items()}
    polynomial = sp.expand(sum(count * z ** size for size, count in spectrum.items()))
    expected_polynomial = 6*z**32 + 4*z**64 + 4*z**96 + 2*z**192 + 2*z**1760 + 2*z**30400
    assert polynomial == expected_polynomial
    assert polynomial.subs(z, 1) == 20
    assert sp.diff(polynomial, z).subs(z, 1) == 65536

    print(json.dumps({
        "status": "C85_SYMPY_LATTICE_CROSSCHECK_PASS",
        "zeta_determinant": int(inclusion.det()),
        "meet_join_pairs": meet_join_pairs,
        "fibre_polynomial": "6z^32+4z^64+4z^96+2z^192+2z^1760+2z^30400",
        "support_total": 65536,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
