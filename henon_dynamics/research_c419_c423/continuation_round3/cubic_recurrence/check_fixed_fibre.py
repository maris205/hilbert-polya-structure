"""One frozen exact McMillan fibre check; no parameter or point search.

This is author evidence for a partial obstruction, not the full CR2 atlas.
No third-party dependency, subprocess, network call, or persistent write.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mcmillan(point):
    x, y = point
    return y, -5 * y / (1 + y * y) - x


def fibre_value(point):
    x, y = point
    return x * x * y * y + x * x + y * y + 5 * x * y


def on_curve(point):
    if point is None:
        return True
    x, y = point
    return y * y == x * x * x - 74 * x * x + 1625 * x


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == -y2:
        return None
    if left == right:
        slope = (3 * x1 * x1 - 148 * x1 + 1625) / (2 * y1)
    else:
        require(x1 != x2, "unhandled equal-X addition")
        slope = (y2 - y1) / (x2 - x1)
    x3 = slope * slope + 74 - x1 - x2
    y3 = -y1 + slope * (x1 - x3)
    result = (x3, y3)
    require(on_curve(result), "addition left the cubic")
    return result


def to_fibre(point):
    require(point is not None, "inverse undefined at the identity")
    X, Y = point
    require(Y != 0, "inverse chart requires nonzero Y")
    x = 8 * X / Y
    v = (X - 37) * x * x / 8 - 4
    y = (v - 5 * x) / (2 * (1 + x * x))
    result = (x, y)
    require(fibre_value(result) == 4, "inverse left the frozen fibre")
    return result


def encode(point):
    if point is None:
        return None
    return [[z.numerator, z.denominator] for z in point]


def check_three_cycle(point):
    first = mcmillan(point)
    second = mcmillan(first)
    third = mcmillan(second)
    require(third == point, "three-step return failed")
    require(len({point, first, second}) == 3, "least period is not three")


def main():
    seed = (F(1), F(1, 2))
    require(mcmillan(seed) == (F(1, 2), F(-3)), "seed image mismatch")
    check_three_cycle(seed)
    P = (F(125), F(1000))
    require(on_curve(P), "elliptic seed is not on E")
    require(to_fibre(P) == seed, "birational seed mismatch")
    rows = []
    Q = None
    inverse_checks = 0
    for n in range(1, 13):
        Q = add(Q, P)
        require(Q is not None, f"[{n}]P is the identity")
        require(on_curve(Q), f"[{n}]P is not on E")
        if Q[1] != 0:
            check_three_cycle(to_fibre(Q))
            inverse_checks += 1
        rows.append({"n": n, "point": encode(Q)})
    require(rows[1]["point"] == encode((F(49), F(140))), "[2]P mismatch")
    require(rows[3]["point"][0] == [9409, 1225], "[4]P X mismatch")
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    result = {
        "status": "PASS_FIXED_FIBRE_ONLY",
        "utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameter": -5,
        "invariant_level": 4,
        "tested_multiples": 12,
        "identity_multiples": [],
        "inverse_and_exact_period_three_checks": inverse_checks,
        "first_four_multiples": rows[:4],
        "all_twelve_points_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
        "full_parameter_atlas_claimed": False,
        "independent_review_claimed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
