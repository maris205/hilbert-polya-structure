"""Check the proof's affine certificate with no degree enumeration.

All bulk coordinates and R are indeterminates. Boundary endpoint
inequalities use the smallest R in the entire residue progression.
The only concrete points are the 17 degree-independent exceptional bulk
points. No functional graph of a numerical degree is computed here.
"""

from collections import Counter
from itertools import combinations

from symbolic_bulk import bulk_polynomials, progression_offset, SIGMA
from symbolic_boundary import strip_rule
from symbolic_corners import boundary_return, corner_starts


STRIPS = {
    0: ((0, 0, 2, 0, 1), (2, 0, 10, -2, 1), (4, 0, 14, -4, 1),
        (0, 0, 2, 0, 1), (0, 0, 2, 0, 2), (0, 0, 2, 0, 2)),
    1: ((4, 2, 6, -4, 1), (3, -1, 18, 0, 1), (2, 2, 2, -2, 1),
        (2, 2, 2, -2, 2), (2, 2, 2, -2, 2), (2, 2, 2, -2, 1)),
    2: ((1, 1, 2, -1, 2), (1, 1, 2, -1, 1), (1, -3, 10, 3, 1),
        (1, -1, 6, 1, 1), (1, 1, 2, -1, 1), (1, 1, 2, -1, 2)),
}


# Exact raw endpoint return rows. An outer target with coefficient -1
# escapes on its next step; None means escape before a section return.
ENDPOINTS = {
    0: {
        (-1, -2, 1): (1, 1, (1, 1, 2)),
        (-1, -1, 1): (1, 1, (1, 1, 1)),
        (-1, 1, 1): (7, -1, (1, -1, 1)),
        (-1, 2, 1): (9, 1, (1, -2, 1)),
        (1, -2, 2): (1, 1, (1, 2, 2)),
        (1, -1, 2): (1, 1, (1, 2, 1)),
        (1, 0, 2): (2, -1, (-1, 0, 2)),
        (1, 1, 1): (1, -1, (-1, -1, 1)),
        (1, 1, 2): (2, -1, (-1, 1, 1)),
        (1, 2, 1): (1, -1, (-1, -1, 2)),
        (1, 2, 2): (2, -1, (-1, 2, 1)),
    },
    1: {
        (-1, -2, 1): (1, None, None),
        (-1, -1, 1): (1, None, None),
        (-1, 0, 1): (1, 1, (1, 1, 2)),
        (-1, 1, 1): (1, 1, (1, 1, 1)),
        (-1, 2, 1): (3, -1, (1, 0, 1)),
        (1, -1, 2): (1, 1, (1, 2, 2)),
        (1, 0, 1): (13, -1, (-1, 2, 1)),
        (1, 0, 2): (1, 1, (1, 2, 1)),
        (1, 1, 2): (2, -1, (-1, 0, 1)),
        (1, 2, 2): (2, -1, (-1, 1, 2)),
    },
    2: {
        (-1, -2, 1): (1, None, None),
        (-1, -1, 1): (1, 1, (1, 1, 2)),
        (-1, 0, 1): (1, 1, (1, 1, 1)),
        (1, 0, 1): (5, -1, (-1, 1, 1)),
        (1, 0, 2): (1, 1, (1, 2, 2)),
        (1, 1, 1): (3, 1, (-1, 0, 1)),
        (1, 1, 2): (1, 1, (1, 2, 1)),
        (1, 2, 1): (1, -1, (-1, -1, 1)),
        (1, 2, 2): (2, None, None),
    },
}


def verify_bulk():
    cells, polynomial_counts = bulk_polynomials()
    exceptional = {}
    for datum in cells:
        exceptional.update(datum["exceptions"])
    assert len(exceptional) == 17
    assert {n: sum(v == n for v in exceptional.values()) for n in (1, 5, 6)} == {
        1: 1, 5: 10, 6: 6,
    }
    for point, least_period in exceptional.items():
        current = point
        for elapsed in range(1, least_period + 1):
            assert max(map(abs, current)) <= 2
            current = current[1], -current[0] + SIGMA[current[1] % 6]
            assert (current == point) == (elapsed == least_period)
            if least_period == 6 and elapsed == 3:
                assert current == tuple(-coordinate for coordinate in point)
    # q = 2m + v, v = floor((R mod 6)/3). Compare coefficients,
    # not evaluations at a finite list of m values.
    for r, actual in polynomial_counts.items():
        v, s = r // 3, r % 3
        plus = (4, 4 * v + 2, v * (v + 1))
        minus = (4, 4 * v - 2, v * (v - 1))
        expected = {4: plus, 12: minus if s == 0 else plus,
                    20: plus if s == 2 else minus}
        assert actual == expected, (r, actual, expected)
    return cells


def verify_strips():
    for r in range(6):
        for e in range(6):
            rule = strip_rule(r, (e + 3 * (r // 3)) % 6)
            actual = (rule["lower"], rule["upper"], rule["time"],
                      -rule["out_x"].c, rule["out_level"])
            assert actual == STRIPS[r % 3][e], (r, e, actual)
            assert rule["out_sign"] == -1
            assert (rule["out_x"].r, rule["out_x"].x) == (0, -1)
            assert rule["minimum_r"] <= (r if r >= 2 else r + 6)


def verify_corner_coverage():
    for r in range(6):
        starts = corner_starts(r)
        assert starts == set(ENDPOINTS[r % 3])
        minimum_r = r if r >= 2 else r + 6
        for start in starts:
            result = boundary_return(r, *start)
            actual = result["time"], result.get("sign"), result["target"]
            assert actual == ENDPOINTS[r % 3][start], (r, start, actual)
            target = result["target"]
            if target is not None and target[0] == -1 and target[2] == 2:
                # Its normalized x is below R+s-2 for every admissible R.
                assert 2 * minimum_r + r % 3 - 2 - target[1] > 0
        for first, second in combinations(starts, 2):
            if first[2] != second[2]:
                continue
            a, c = first[0] - second[0], first[1] - second[1]
            if a == 0:
                assert c != 0
            else:
                # The affine difference cannot cross zero after minimum_r.
                assert a * (a * minimum_r + c) > 0
        for e in range(6):
            rule = strip_rule(r, e)
            full = progression_offset(r, e, -2, 2)
            generic = progression_offset(r, e, rule["lower"], rule["upper"])
            minimum_m = 1 if r < 2 else 0
            assert 2 * minimum_m + generic >= 0
            exceptional_count = sum(
                level == 1 and (a * r + c) % 6 == e for a, c, level in starts
            )
            # The coefficients of m are both two and cancel exactly.
            assert full - generic == exceptional_count


def normalized_cycle(r, start):
    current, elapsed, sign, seen = start, 0, 1, set()
    while current not in seen:
        seen.add(current)
        result = boundary_return(r, *current)
        assert result["target"] is not None, (r, current)
        current = result["target"]
        elapsed += result["time"]
        sign *= result["sign"]
    assert current == start
    return len(seen), elapsed, sign


def verify_corner_cycles():
    certificates = {
        0: {(-1, -1, 1): (2, 2, -1), (-1, 2, 1): (4, 14, 1)},
        1: {(-1, 0, 1): (2, 3, -1), (1, 0, 2): (2, 3, -1),
            (-1, 2, 1): (2, 16, 1)},
        2: {(-1, -1, 1): (3, 3, -1), (-1, 0, 1): (2, 4, 1)},
    }
    lifted_counts = {}
    for r in range(6):
        lifted = Counter()
        for start, expected in certificates[r % 3].items():
            actual = normalized_cycle(r, start)
            assert actual == expected
            _, time, sign = actual
            lifted[time if sign == 1 else 2 * time] += 2 if sign == 1 else 1
        lifted_counts[r] = lifted
    return lifted_counts


def verify_cardinality_polynomials(lifted_corner_counts):
    """Derive counts from residue progressions and checked signed cycles."""
    _, bulk = bulk_polynomials()
    expected = {0: (36, -20, 53), 1: (36, 48, 31), 2: (36, 52, 31)}
    for r in range(6):
        v, s = r // 3, r % 3
        point_coefficients = [sum(period * poly[j] for period, poly in bulk[r].items())
                              for j in range(3)]
        point_coefficients[2] += 17
        point_coefficients[2] += sum(period * count
                                     for period, count in lifted_corner_counts[r].items())

        def progression(e):
            residue = (e + 3 * v) % 6
            rule = strip_rule(r, residue)
            return 2, progression_offset(r, residue, rule["lower"], rule["upper"])

        if s == 0:
            first, second = progression(0), progression(3)
            count = first[0] + second[0], first[1] + second[1]
            assert count == (4, 2 * v + 1)  # 2q+1 stationary strip cycles.
            point_coefficients[1] += 4 * count[0]
            point_coefficients[2] += 4 * count[1]
        elif s == 1:
            count = progression(1)
            assert count == (2, v - 1)  # q-1 stationary strip cycles.
            point_coefficients[1] += 36 * count[0]
            point_coefficients[2] += 36 * count[1]
            first, second = progression(2), progression(0)
            assert first == (2, v + 1) and second == (2, v)
            # One initial edge of time 1, q+1 edges of time 2, q of time 6.
            quotient_time = (2 * first[0] + 6 * second[0],
                             1 + 2 * first[1] + 6 * second[1])
            assert (first[0] + second[0]) % 2 == 0
            assert (first[1] + second[1]) % 2 == 1
            # Negative total sign doubles the ordinary period.
            point_coefficients[1] += 2 * quotient_time[0]
            point_coefficients[2] += 2 * quotient_time[1]
        else:
            count = progression(3)
            assert count == (2, v)  # q normalized pairs, two lifts each.
            point_coefficients[1] += 16 * count[0]
            point_coefficients[2] += 16 * count[1]
        a, b, c = expected[s]
        expected_in_m = (4 * a, 4 * a * v + 2 * b, a * v * v + b * v + c)
        assert tuple(point_coefficients) == expected_in_m


if __name__ == "__main__":
    verify_bulk()
    verify_strips()
    verify_corner_coverage()
    corner_counts = verify_corner_cycles()
    verify_cardinality_polynomials(corner_counts)
    print("PASS: 36 affine bulk cells, all 36 affine boundary strips,")
    print("      exact endpoint complements, disjointness at every admissible R,")
    print("      all endpoint return rows and all constant endpoint cycles,")
    print("      central cycles, progression-derived boundary cardinalities,")
    print("      and exact total cardinality polynomials.")
    print("No numerical degree graph was enumerated by this certificate.")
