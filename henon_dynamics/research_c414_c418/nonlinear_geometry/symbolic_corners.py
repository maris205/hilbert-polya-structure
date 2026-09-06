"""Boundary endpoints: affine identities with the radius left free.

This is not a numerical degree census. Each radius residue class carries
its own smallest admissible radius, so the inequalities also check the
smallest radii rather than assuming an asymptotic cutoff.
"""

from symbolic_boundary import Affine, SIGMA, strip_rule


def region(expression, minimum_radius):
    """Classify a*R+c, proving inequalities on a whole radius progression."""
    assert expression.x == 0
    a, c = expression.r, expression.c
    if a == 0:
        assert abs(c) <= minimum_radius
        return "bulk", 0
    if abs(a) == 1:
        level = a * c
        if level <= 0:
            assert 2 * minimum_radius + level >= 0
            return "bulk", 0
        if level <= 2:
            return "boundary", level
        return "escape", 0
    assert abs(a) * minimum_radius + (c if a > 0 else -c) > minimum_radius + 2
    return "escape", 0


def boundary_return(r_residue, x_coefficient, x_offset, level):
    minimum_radius = r_residue if r_residue >= 2 else r_residue + 6
    phase = 1 if r_residue % 2 else -1
    point = (Affine(r=x_coefficient, c=x_offset), Affine(r=1, c=level))
    itinerary = [point]
    for elapsed in range(1, 61):
        previous, current = point
        kind, current_level = region(current, minimum_radius)
        if kind == "bulk":
            value = Affine(c=phase * SIGMA[current.residue(r_residue, 0)])
        elif kind == "boundary":
            sign = current.r
            if current_level == 1:
                value = Affine(c=sign * ((-r_residue) % 3))
            else:
                value = Affine(r=2 * sign, c=sign * (r_residue % 3))
        else:
            raise AssertionError("An escaped point cannot start a step")
        point = (current, value - previous)
        itinerary.append(point)
        kind, next_level = region(point[1], minimum_radius)
        if kind == "escape":
            return {"time": elapsed, "target": None, "itinerary": itinerary}
        if kind == "boundary":
            sign = point[1].r
            x = point[0]
            return {
                "time": elapsed, "sign": sign,
                "target": (sign * x.r, sign * x.c, next_level),
                "itinerary": itinerary,
            }
    raise AssertionError("No endpoint first return in 60 affine steps")


def corner_starts(r_residue):
    """Exact complements of all strips, not a guessed endpoint cutoff.

For each residue, the full interval is [-R-2,R+2], and the proved
generic interval is [-R+L,R+U]. Its two complementary intervals have
offsets [-2,L-1] at -R and [U+1,2] at +R. Their disjointness is checked
at the least R and then holds on the entire increasing progression.
"""
    starts = set()
    minimum_radius = r_residue if r_residue >= 2 else r_residue + 6
    for residue in range(6):
        rule = strip_rule(r_residue, residue)
        lower, upper = rule["lower"], rule["upper"]
        assert 2 * minimum_radius + upper - lower >= 0
        for offset in range(-2, lower):
            if (-r_residue + offset) % 6 == residue:
                starts.add((-1, offset, 1))
        for offset in range(upper + 1, 3):
            if (r_residue + offset) % 6 == residue:
                starts.add((1, offset, 1))
    for offset in range(r_residue % 3 - 2, 3):
        starts.add((1, offset, 2))
    return starts


if __name__ == "__main__":
    for radius_residue in range(6):
        for start in sorted(corner_starts(radius_residue)):
            result = boundary_return(radius_residue, *start)
            print(radius_residue, start,
                  {key: value for key, value in result.items() if key != "itinerary"})
