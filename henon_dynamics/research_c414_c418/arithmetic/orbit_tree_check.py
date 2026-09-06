"""Bounded exact diagnostic for a congruence-compatible conjugacy question.

No files are written. This does not prove the all-height or all-matrix claim.
The signatures retain cycle length AND parent/child incidence, not merely
the unstructured cycle histogram on each quotient.
"""

from collections import Counter
from hashlib import sha256
import json


def cycles(matrix, modulus):
    a, b, c, d = matrix
    permutation = [
        ((a * x + b * y) % modulus) * modulus
        + (c * x + d * y) % modulus
        for x in range(modulus)
        for y in range(modulus)
    ]
    assert sorted(permutation) == list(range(modulus * modulus))
    orbit_of = [-1] * len(permutation)
    orbits = []
    for initial in range(len(permutation)):
        if orbit_of[initial] != -1:
            continue
        orbit = []
        point = initial
        while orbit_of[point] == -1:
            orbit_of[point] = len(orbits)
            orbit.append(point)
            point = permutation[point]
        assert point == initial
        orbits.append(orbit)
    return permutation, orbit_of, orbits


def tower(matrix, prime, height):
    levels = [cycles(matrix, prime**k) for k in range(height + 1)]
    parent_maps = [[]]
    for k in range(1, height + 1):
        modulus = prime**k
        lower = modulus // prime
        parents = []
        for orbit in levels[k][2]:
            projected = {
                levels[k - 1][1][
                    ((point // modulus) % lower) * lower
                    + (point % modulus) % lower
                ]
                for point in orbit
            }
            assert len(projected) == 1
            parents.append(projected.pop())
        parent_maps.append(parents)
    return levels, parent_maps


def signature(levels, parent_maps):
    # Canonical full tuples, not hash equality, establish the diagnostic result.
    sigs = [(len(orbit), ()) for orbit in levels[-1][2]]
    for k in range(len(levels) - 2, -1, -1):
        children = [[] for _ in levels[k][2]]
        for child, parent in enumerate(parent_maps[k + 1]):
            children[parent].append(sigs[child])
        sigs = [
            (len(orbit), tuple(sorted(children[i])))
            for i, orbit in enumerate(levels[k][2])
        ]
    assert len(sigs) == 1
    return sigs[0]


def negative(matrix):
    return tuple(-entry for entry in matrix)


def shear_conjugate(matrix):
    # P A P^-1 for P=((1,1),(0,1)), independently checked below.
    a, b, c, d = matrix
    return a + c, b + d - a - c, c, d - c


def main():
    # Same signed trace and old ordinary census; different local linear class.
    first = (1, 4, 4, 17)
    second = (5, 8, 8, 13)
    # A second depth: trace 66, r=8, (33^2-1)/8^2=17.
    third = (33, 136, 8, 33)
    fourth = (25, 64, 16, 41)
    cases = [
        ("trace18-positive", first, second, 2, 8),
        ("trace18-negative", negative(first), negative(second), 2, 8),
        ("trace66-positive", third, fourth, 2, 8),
        ("trace66-negative", negative(third), negative(fourth), 2, 8),
        ("trace18-prime3", first, second, 3, 4),
        ("trace18-prime5", first, second, 5, 3),
    ]
    boundaries = [(f"trace{t}-companion", (0, -1, 1, t))
                  for t in (-2, -1, 0, 1, 2)]
    boundaries += [("unipotent-content4", (1, 4, 0, 1)),
                   ("negative-unipotent-content4", (-1, 4, 0, -1)),
                   ("identity", (1, 0, 0, 1)),
                   ("negative-identity", (-1, 0, 0, -1))]
    cases += [(name, mat, shear_conjugate(mat), 2, 4)
              for name, mat in boundaries]
    rows = []
    for name, left, right, prime, height in cases:
        assert left[0] * left[3] - left[1] * left[2] == 1
        assert right[0] * right[3] - right[1] * right[2] == 1
        left_levels, left_parents = tower(left, prime, height)
        right_levels, right_parents = tower(right, prime, height)
        left_sig = signature(left_levels, left_parents)
        right_sig = signature(right_levels, right_parents)
        assert left_sig == right_sig, name
        rows.append(
            {
                "case": name,
                "prime": prime,
                "height": height,
                "equal_labelled_orbit_tree": True,
                "terminal_cycles": sorted(
                    Counter(map(len, left_levels[-1][2])).items()
                ),
                "signature_sha256_display_only": sha256(
                    repr(left_sig).encode("ascii")
                ).hexdigest(),
            }
        )
    # Hostile control: a different scalar depth must NOT have the same tree.
    shallow = (1, 2, 2, 5)
    assert signature(*tower(shallow, 2, 5)) != signature(*tower(first, 2, 5))
    assert tuple(entry % 8 for entry in second) == (5, 0, 0, 5)
    assert tuple(entry % 8 for entry in first) != (5, 0, 0, 5)
    assert signature(*tower((1, 0, 0, 1), 2, 2)) != signature(
        *tower((-1, 0, 0, -1), 2, 2))
    print(json.dumps({"status": "PASS", "cases": rows,
                      "different_depth_control_rejected": True,
                      "scalar_nonscalar_mod8_obstruction": True,
                      "signed_scalar_control_rejected": True}, indent=2))


if __name__ == "__main__":
    main()
