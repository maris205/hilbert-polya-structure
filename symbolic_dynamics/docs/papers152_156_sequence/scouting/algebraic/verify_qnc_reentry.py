#!/usr/bin/env python3
"""Independent exact replay for the QNC re-entry gate.

The audited finite system is

    X_{p,e} = p Z / p^e Z,
    Q_{p,e}(x) = x(x+p) mod p^e,

for odd primes p and e >= 2.  This file deliberately imports no code from the
P147--P151 scout.  It checks the literal graph, three affine coordinate
presentations, the pointwise absorption clock, the complete temporal
polynomial, every target fibre, the square-image census, and the
parity-sensitive maximum fibre.

The program verifies mathematics only.  Literature ownership is decided in
QNC_REENTRY_FOCUSED_AUDIT.md.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256


class AuditFailure(RuntimeError):
    """Raised on the first failed exact assertion."""


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AuditFailure(label)

    def equal(self, left, right, label: str) -> None:
        self.require(left == right, f"{label}: {left!r} != {right!r}")


def valuation(value: int, prime: int, cap: int) -> int:
    """Return min(v_p(value), cap), with v_p(0) truncated to cap."""

    if cap == 0:
        return 0
    if value == 0:
        return cap
    order = 0
    while order < cap and value % prime == 0:
        value //= prime
        order += 1
    return order


def square_root_count(delta: int, prime: int, exponent: int) -> int:
    """Exact number of roots of z^2=delta modulo p^exponent, p odd."""

    if exponent == 0:
        return 1
    modulus = prime**exponent
    delta %= modulus
    order = valuation(delta, prime, exponent)
    if order == exponent:
        return prime ** (exponent // 2)
    if order % 2:
        return 0
    half_order = order // 2
    unit = delta // prime**order
    if pow(unit % prime, (prime - 1) // 2, prime) != 1:
        return 0
    return 2 * prime**half_order


def expected_depth(value: int, prime: int, exponent: int) -> int:
    if value == 0:
        return 0
    order = valuation(value, prime, exponent)
    if order >= 2:
        return exponent - order
    unit = value // prime
    cancellation = valuation(unit + 1, prime, exponent)
    return exponent - 1 - min(cancellation, exponent - 2)


def expected_depth_histogram(prime: int, exponent: int) -> Counter[int]:
    if exponent == 2:
        return Counter({0: 1, 1: prime - 1})
    out = Counter({0: 1, 1: 2 * prime - 1})
    for depth in range(2, exponent - 1):
        out[depth] = 2 * (prime - 1) * prime ** (depth - 1)
    out[exponent - 1] = (prime - 2) * prime ** (exponent - 2)
    return out


def expected_positive_fibre_histogram(
    prime: int, exponent: int
) -> Counter[int]:
    """Histogram {positive fibre size: number of targets}."""

    out = Counter({prime ** (exponent // 2): 1})
    for level in range(1, (exponent - 1) // 2 + 1):
        size = 2 * prime**level
        multiplicity = (prime - 1) * prime ** (exponent - 2 * level - 1) // 2
        out[size] += multiplicity
    return out


@dataclass(frozen=True)
class CaseResult:
    prime: int
    exponent: int
    states: int
    image: int
    max_depth: int
    max_fibre: int
    max_multiplicity: int
    depth_coefficients: tuple[int, ...]
    fibre_histogram: tuple[tuple[int, int], ...]

    def line(self) -> str:
        depths = ",".join(str(value) for value in self.depth_coefficients)
        fibres = ",".join(
            f"{size}^{multiplicity}" for size, multiplicity in self.fibre_histogram
        )
        return (
            f"BOX p={self.prime} e={self.exponent} states={self.states} "
            f"image={self.image} max_depth={self.max_depth} "
            f"max_fibre={self.max_fibre} max_mult={self.max_multiplicity} "
            f"depths={depths} positive_fibres={fibres}"
        )


def run_case(prime: int, exponent: int, checks: Checks) -> CaseResult:
    modulus = prime**exponent
    scaled_modulus = prime ** (exponent - 1)
    root_exponent = exponent - 2
    root_modulus = prime**root_exponent
    states = tuple(range(0, modulus, prime))
    state_set = set(states)

    def step(value: int) -> int:
        return value * (value + prime) % modulus

    next_state: dict[int, int] = {}
    fibres: Counter[int] = Counter()
    depths: Counter[int] = Counter()
    inverse_two_modulus = pow(2, -1, modulus)
    inverse_four_modulus = pow(4, -1, modulus)
    inverse_two_scaled = pow(2, -1, scaled_modulus)
    translated_constant = (
        prime * inverse_two_modulus
        - prime * prime * inverse_four_modulus
    ) % modulus

    for value in states:
        image = step(value)
        checks.require(image in state_set, "carrier invariance")
        next_state[value] = image
        fibres[image] += 1

        # Scaled coordinate u=x/p on Z/p^(e-1)Z.
        unit_coordinate = value // prime
        scaled_image = image // prime
        expected_scaled_image = (
            prime * unit_coordinate * (unit_coordinate + 1)
        ) % scaled_modulus
        checks.equal(scaled_image, expected_scaled_image, "scaled-coordinate map")

        # z=1+2u gives g(z)=1+(p/2)(z^2-1).
        z = (1 + 2 * unit_coordinate) % scaled_modulus
        z_image = (1 + 2 * scaled_image) % scaled_modulus
        g_image = (
            1
            + prime * inverse_two_scaled * (z * z - 1)
        ) % scaled_modulus
        checks.equal(z_image, g_image, "z-coordinate conjugacy")

        # Translation y=x+p/2 gives y -> y^2+p/2-p^2/4.
        y = (value + prime * inverse_two_modulus) % modulus
        y_image = (image + prime * inverse_two_modulus) % modulus
        translated_image = (y * y + translated_constant) % modulus
        checks.equal(y_image, translated_image, "translated quadratic conjugacy")

        # Pointwise valuation law and literal first-hitting time.
        if value:
            order = valuation(value, prime, exponent)
            if order >= 2:
                checks.equal(
                    valuation(image, prime, exponent),
                    min(exponent, order + 1),
                    "high-valuation increment",
                )
            else:
                cancellation = valuation(
                    unit_coordinate + 1, prime, exponent
                )
                checks.equal(
                    valuation(image, prime, exponent),
                    min(exponent, 2 + cancellation),
                    "outer-shell cancellation",
                )

        predicted_depth = expected_depth(value, prime, exponent)
        current = value
        first_zero = None
        for time in range(exponent + 1):
            if current == 0:
                first_zero = time
                break
            current = step(current)
        checks.require(first_zero is not None, "orbit did not reach zero")
        checks.equal(first_zero, predicted_depth, "pointwise absorption time")
        depths[first_zero] += 1

    checks.equal(
        [value for value in states if next_state[value] == value],
        [0],
        "unique fixed point",
    )
    checks.equal(depths, expected_depth_histogram(prime, exponent), "depth polynomial")
    checks.equal(max(depths), exponent - 1, "sharp maximum depth")
    checks.equal(expected_depth(prime, prime, exponent), exponent - 1,
                 "explicit sharp witness")

    # Every-target inverse atlas, independently compared with the literal map.
    for target in states:
        if target % (prime * prime):
            expected_fibre = 0
        else:
            w = (target // (prime * prime)) % root_modulus
            delta = (1 + 4 * w) % root_modulus
            expected_fibre = prime * square_root_count(
                delta, prime, root_exponent
            )
        checks.equal(fibres.get(target, 0), expected_fibre, "every-target fibre")

    expected_image = 1
    if root_exponent:
        expected_image += (prime - 1) * sum(
            prime ** (root_exponent - 2 * r - 1)
            for r in range((root_exponent - 1) // 2 + 1)
        ) // 2
    positive_fibres = Counter(fibres.values())
    expected_fibres = expected_positive_fibre_histogram(prime, exponent)
    checks.equal(len(fibres), expected_image, "square-image census")
    checks.equal(positive_fibres, expected_fibres, "positive fibre histogram")
    checks.equal(sum(positive_fibres.values()), expected_image,
                 "fibre histogram image total")
    checks.equal(
        sum(size * multiplicity for size, multiplicity in positive_fibres.items()),
        len(states),
        "fibre mass",
    )

    max_fibre = max(fibres.values())
    maximizers = [target for target, size in fibres.items() if size == max_fibre]
    if root_exponent % 2 == 0:
        expected_max = prime ** (root_exponent // 2 + 1)
        expected_multiplicity = 1
        for target in maximizers:
            w = (target // (prime * prime)) % root_modulus
            checks.equal((1 + 4 * w) % root_modulus, 0,
                         "even-precision maximizer label")
    else:
        expected_max = 2 * prime ** ((root_exponent - 1) // 2 + 1)
        expected_multiplicity = (prime - 1) // 2
        for target in maximizers:
            w = (target // (prime * prime)) % root_modulus
            delta = (1 + 4 * w) % root_modulus
            checks.equal(
                valuation(delta, prime, root_exponent),
                root_exponent - 1,
                "odd-precision maximizer valuation",
            )
            checks.equal(
                pow(
                    (delta // prime ** (root_exponent - 1)) % prime,
                    (prime - 1) // 2,
                    prime,
                ),
                1,
                "odd-precision maximizer square unit",
            )
    checks.equal(max_fibre, expected_max, "maximum fibre")
    checks.equal(len(maximizers), expected_multiplicity, "maximizer multiplicity")

    return CaseResult(
        prime=prime,
        exponent=exponent,
        states=len(states),
        image=len(fibres),
        max_depth=max(depths),
        max_fibre=max_fibre,
        max_multiplicity=len(maximizers),
        depth_coefficients=tuple(depths[depth] for depth in range(exponent)),
        fibre_histogram=tuple(sorted(positive_fibres.items())),
    )


def main() -> None:
    boxes = (
        tuple((3, exponent) for exponent in range(2, 11))
        + tuple((5, exponent) for exponent in range(2, 8))
        + tuple((7, exponent) for exponent in range(2, 7))
        + tuple((11, exponent) for exponent in range(2, 6))
        + tuple((13, exponent) for exponent in range(2, 6))
        + tuple((17, exponent) for exponent in range(2, 5))
        + tuple((19, exponent) for exponent in range(2, 5))
    )
    checks = Checks()
    results = [run_case(prime, exponent, checks) for prime, exponent in boxes]
    lines = [result.line() for result in results]
    digest = sha256("\n".join(lines).encode("utf-8")).hexdigest()
    print("QNC_REENTRY_FOCUSED_EXACT_REPLAY")
    print("MATHEMATICAL_CONTRACT=PASS")
    print("OWNER_DECISION=EXTERNAL_TO_VERIFIER")
    for line in lines:
        print(line)
    print(
        f"TOTAL boxes={len(results)} states={sum(result.states for result in results)} "
        f"assertions={checks.count}"
    )
    print(f"PROFILE_SHA256={digest}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
