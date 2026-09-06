"""Exact affine residue-cell proof for the six-periodic bulk map.

There are 36 residue cells, not a bounded list of numerical degrees.
Each coordinate is an affine expression in two free integer variables.
The eventual identity and every earlier possible period are checked.
"""

from fractions import Fraction


SIGMA = (0, 1, 1, 0, -1, -1)
X, Y = (1, 0, 0), (0, 1, 0)


def step(point, x_residue, y_residue):
    x, y = point
    residue = (y[0] * x_residue + y[1] * y_residue + y[2]) % 6
    return y, (-x[0], -x[1], SIGMA[residue] - x[2])


def reduced_period_points(itinerary, x_residue, y_residue):
    generic_period = len(itinerary) - 1
    exceptions = {}
    for period in range(1, generic_period):
        if generic_period % period:
            continue
        first, second = itinerary[period]
        a, b, c = first[0] - 1, first[1], -first[2]
        d, e, f = second[0], second[1] - 1, -second[2]
        determinant = a * e - b * d
        if determinant == 0:
            # A consistent rank-one family would need separate treatment.
            inconsistent = a * f != c * d or b * f != c * e
            inconsistent |= (a == b == 0 and c != 0) or (d == e == 0 and f != 0)
            assert inconsistent, (x_residue, y_residue, period, first, second)
            continue
        x = Fraction(c * e - b * f, determinant)
        y = Fraction(a * f - c * d, determinant)
        if (x.denominator == y.denominator == 1
                and x % 6 == x_residue and y % 6 == y_residue):
            exceptions.setdefault((int(x), int(y)), period)
    return exceptions


def cell(x_residue, y_residue):
    itinerary = [(X, Y)]
    point = (X, Y)
    while True:
        point = step(point, x_residue, y_residue)
        itinerary.append(point)
        if point == (X, Y):
            break
        assert len(itinerary) <= 61
    lower, upper = [0, 0], [0, 0]
    for point in itinerary:
        for a, b, c in point:
            assert abs(a) + abs(b) == 1
            variable, sign = (0, a) if a else (1, b)
            offset = -sign * c
            lower[variable] = max(lower[variable], offset)
            upper[variable] = min(upper[variable], offset)
    return {
        "residues": (x_residue, y_residue), "period": len(itinerary) - 1,
        "lower": tuple(lower), "upper": tuple(upper),
        "exceptions": reduced_period_points(itinerary, x_residue, y_residue),
        "itinerary": tuple(itinerary),
    }


def progression_offset(radius_residue, point_residue, lower, upper):
    # The exact number for R=6m+r is 2m+this constant.
    floor_upper = (radius_residue + upper - point_residue) // 6
    ceil_lower = -((radius_residue - lower + point_residue) // 6)
    return floor_upper - ceil_lower + 1


def bulk_polynomials():
    """Coefficients (m^2,m,1), exact after reduced-period corrections."""
    cells = [cell(x, y) for x in range(6) for y in range(6)]
    outputs = {}
    for r in range(6):
        coefficients = {length: [0, 0, 0] for length in (4, 12, 20)}
        for datum in cells:
            x, y = datum["residues"]
            a = progression_offset(r, x, datum["lower"][0], datum["upper"][0])
            b = progression_offset(r, y, datum["lower"][1], datum["upper"][1])
            minimum_m = 1 if r < 2 else 0
            assert 2 * minimum_m + a >= 0 and 2 * minimum_m + b >= 0
            target = coefficients[datum["period"]]
            for index, value in enumerate((4, 2 * (a + b), a * b)):
                target[index] += value
            # All exceptional orbits have radius <= 2 and R >= 2 here.
            target[2] -= len(datum["exceptions"])
        outputs[r] = {
            length: tuple(Fraction(value, length) for value in polynomial)
            for length, polynomial in coefficients.items()
        }
    return cells, outputs


if __name__ == "__main__":
    cells, polynomials = bulk_polynomials()
    for datum in cells:
        print({key: value for key, value in datum.items() if key != "itinerary"})
    print("POLYNOMIALS", polynomials)
