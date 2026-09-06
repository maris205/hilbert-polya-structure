"""Derive affine first-return rules, not a degree census.

An expression (a,b,c) means a*R + b*x + c. R and x remain indeterminates;
only their residue classes modulo six are fixed. Every use of the bulk
rule records the exact interval constraints on x and a sufficient lower
bound on R. All reported identities follow by integer affine arithmetic.
"""

from dataclasses import dataclass


SIGMA = (0, 1, 1, 0, -1, -1)


@dataclass(frozen=True)
class Affine:
    r: int = 0
    x: int = 0
    c: int = 0

    def __add__(self, other):
        if isinstance(other, int):
            other = Affine(c=other)
        return Affine(self.r + other.r, self.x + other.x, self.c + other.c)

    def __neg__(self):
        return Affine(-self.r, -self.x, -self.c)

    def __sub__(self, other):
        return self + (-other)

    def residue(self, r_residue, x_residue):
        return (self.r * r_residue + self.x * x_residue + self.c) % 6

    def evaluate(self, radius, x_value):
        return self.r * radius + self.x * x_value + self.c


def strip_rule(r_residue, x_residue):
    """Return a proved symbolic rule on -R+lower <= x <= R+upper."""
    phase = (-1) ** (r_residue - 1) if r_residue else -1
    phase = int(phase)
    lower, upper, minimum_r = -2, 2, 2
    point = (Affine(x=1), Affine(r=1, c=1))
    itinerary = [point]

    def require_bulk(expression):
        nonlocal lower, upper, minimum_r
        a, b, c = expression.r, expression.x, expression.c
        if b:
            assert a == 0 and abs(b) == 1
            offset = -b * c
            lower, upper = max(lower, offset), min(upper, offset)
        elif a:
            assert abs(a) == 1 and a * c <= 0
            minimum_r = max(minimum_r, (abs(c) + 1) // 2)
        else:
            minimum_r = max(minimum_r, abs(c))

    for elapsed in range(1, 61):
        previous, current = point
        if elapsed == 1:
            value = Affine(c=(-r_residue) % 3)
        else:
            require_bulk(current)
            value = Affine(c=phase * SIGMA[current.residue(r_residue, x_residue)])
        point = (current, value - previous)
        itinerary.append(point)
        y = point[1]
        if y.x == 0 and abs(y.r) == 1 and y.r * y.c > 0:
            level = y.r * y.c
            return {
                "r_mod_6": r_residue, "x_mod_6": x_residue,
                "lower": lower, "upper": upper, "minimum_r": minimum_r,
                "time": elapsed, "out_x": point[0], "out_sign": y.r,
                "out_level": level, "itinerary": tuple(itinerary),
            }
    raise AssertionError("No uniform boundary return within 60 steps")


if __name__ == "__main__":
    for r_residue in range(6):
        for x_residue in range(6):
            rule = strip_rule(r_residue, x_residue)
            print({key: value for key, value in rule.items() if key != "itinerary"})
