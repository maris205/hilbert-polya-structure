#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P188 Round 1.

This script does not import the author verifier or Review-A code.  It
compresses each target to the profile `(b, M(B))`, where `b=|B|` and `M(B)` is
the largest occupied position, and evaluates the all-time fibre theorem through
the difference variables `d_j = k_j-k_{j+1}`.  This avoids the author's direct
chain enumeration and Review A's backward interval-capacity implementation.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from math import comb
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT / "papers" / "188-self-cardinality-truncation"
REVIEW_A = ROOT / "docs" / "papers187_191_sequence" / "reviews" / "p188_a"

FROZEN = {
    "main.tex": "f08712d1b1e43f707c1254ebf791724727e9387a5e0794dae3b5c40d4874ab39",
    "references.bib": "519c74bea25fb175dfdd10560e432880f160494edd29e12e40d2aac3f0a9c4f8",
    "verify_p188.py": "94f4aa2b656fcbf291106b63b0b22bf2fe3ca4f5d7ac6f0dfb3dc6693be9741d",
    "CANONICAL.txt": "ff0457f32e495f2405f494af83f461ad6bca310d25f04923fdb413c856d245ef",
    "PROOF_PACKAGE.md": "6307ac2d3f7eb9b82dff1118898225c910d3647e98bd823fc6ae7fc73c785235",
    "SOURCE_VERIFICATION.md": "aa0ccf0a56fe33ddcd087d94f52177369da4bc19d920766c71fe67eddd20dc47",
    "main_round0_original.pdf": "10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3",
    "main_round1.pdf": "10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3",
    "main.pdf": "10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3",
}

FROZEN_REVIEW_A = {
    "HOSTILE_REVIEW_A.md": "aa1ef5975652439bc4566342eed119e3d76a409b03212d69d2b0375acbea287e",
    "DELTA.md": "81793fe0e62a96784f4cd8a4d3ecddcaffcadf470f533fc9c6596039eaab1902",
    "verify_review_a_p188.py": "663c60581e78074de8ec7f6dbff8e46f0b2d54334eaa262fe851bc2f2d696ae8",
    "CANONICAL.txt": "989c6bf33f2e261ec83f79703ac82c29b6fb646fd989ea67eff901aa0e8c2d23",
}


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check_frozen_artifacts() -> None:
    for name, expected in FROZEN.items():
        AUDIT.check(digest(PAPER / name) == expected, f"frozen artifact changed: {name}")
    for name, expected in FROZEN_REVIEW_A.items():
        AUDIT.check(digest(REVIEW_A / name) == expected, f"Review-A artifact changed: {name}")

    payloads = [
        (PAPER / "main.pdf").read_bytes(),
        (PAPER / "main_round0_original.pdf").read_bytes(),
        (PAPER / "main_round1.pdf").read_bytes(),
    ]
    AUDIT.check(payloads[0] == payloads[1] == payloads[2], "live and frozen PDFs differ")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    readme = (PAPER / "README.md").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    for needle in (
        r"\rho(A)",
        r"F_{n+2}",
        r"HOLD\_EXTERNAL",
        "13,283,014",
    ):
        AUDIT.check(needle in source or needle in readme, f"contract missing: {needle}")
    cited = {
        key.strip()
        for group in re.findall(r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", source)
        for key in group.split(",")
        if key.strip()
    }
    bib = {
        match.group(1).strip()
        for match in re.finditer(r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
                                 bibliography, flags=re.IGNORECASE)
    }
    AUDIT.check(cited == bib, "citation/bibliography key mismatch")
    AUDIT.check(len(bib) == 2, "unexpected bibliography cardinality")


def prefix_mask(k: int) -> int:
    return (1 << k) - 1


def update(mask: int) -> int:
    return mask & prefix_mask(mask.bit_count())


def rho(mask: int, n: int) -> int:
    r = 0
    while r < n and (mask & (1 << r)):
        r += 1
    return r


def orbit(mask: int) -> tuple[int, int]:
    seen = {}
    current = mask
    while current not in seen:
        seen[current] = len(seen)
        current = update(current)
    return seen[current], current


def fibonacci(k: int) -> int:
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def suffix_exact(prev_d: int, steps_left: int, lower: int) -> tuple[tuple[int, int], ...]:
    if steps_left == 0:
        return ((0, 1),)
    acc: Counter[int] = Counter()
    minimum = lower if steps_left == 1 else 0
    for current_d in range(minimum, prev_d + 1):
        factor = comb(prev_d, current_d)
        for subtotal, weight in suffix_exact(current_d, steps_left - 1, lower):
            acc[current_d + subtotal] += factor * weight
    return tuple(sorted(acc.items()))


def profile_formula(n: int, b: int, maximum: int, t: int) -> int:
    if t == 0:
        return 1
    lower = max(0, maximum - b)
    budget = n - b
    total = 0
    for d0 in range(lower, budget + 1):
        for rest_sum, weight in suffix_exact(d0, t - 1, lower):
            total_drop = d0 + rest_sum
            if total_drop > budget:
                continue
            leftover = budget - total_drop
            if d0 > leftover:
                continue
            total += comb(leftover, d0) * weight
    return total


def one_step_formula(target: int, n: int) -> int:
    return profile_formula(n, target.bit_count(), target.bit_length(), 1)


def evolve_counts(n: int, max_t: int) -> list[Counter[int]]:
    current = Counter({mask: 1 for mask in range(1 << n)})
    layers = [current]
    for _ in range(max_t):
        nxt: Counter[int] = Counter()
        for state, multiplicity in current.items():
            nxt[update(state)] += multiplicity
        current = nxt
        layers.append(current)
    return layers


def verify_box(n: int, max_t: int) -> str:
    states = range(1 << n)
    endpoints: Counter[int] = Counter()
    depths: Counter[int] = Counter()
    maximum_tail = -1
    deepest: list[int] = []
    digest_orbits = sha256()

    for mask in states:
        tail, endpoint = orbit(mask)
        endpoints[endpoint] += 1
        depths[tail] += 1
        digest_orbits.update(f"{n}:{mask}->{endpoint}:{tail};".encode("ascii"))
        r = rho(mask, n)
        AUDIT.check(endpoint == prefix_mask(r), f"endpoint formula n={n} mask={mask}")
        AUDIT.check(update(endpoint) == endpoint, f"endpoint fixed n={n} mask={mask}")

        source = mask
        k = mask.bit_count()
        for _time in range(1, n + 3):
            source = update(source)
            AUDIT.check(source == (mask & prefix_mask(k)), f"all-time iterate n={n} mask={mask}")
            k = (mask & prefix_mask(k)).bit_count()

        if tail > maximum_tail:
            maximum_tail = tail
            deepest = [mask]
        elif tail == maximum_tail:
            deepest.append(mask)

    expected_tail = max(0, n - 1)
    AUDIT.check(maximum_tail == expected_tail, f"sharp tail n={n}")
    if n >= 2:
        AUDIT.check(deepest == [prefix_mask(n) ^ 1], f"unique deepest n={n}")
    else:
        AUDIT.check(deepest == list(states), f"small deepest boundary n={n}")

    for r in range(n + 1):
        endpoint = prefix_mask(r)
        expected = 1 if r == n else 1 << (n - r - 1)
        AUDIT.check(endpoints[endpoint] == expected, f"terminal basin n={n} r={r}")
    AUDIT.check(len([mask for mask in states if update(mask) == mask]) == n + 1, f"fixed count n={n}")

    layers = evolve_counts(n, max_t)
    for t, actual in enumerate(layers):
        predicted_mass = 0
        for target in states:
            if t == 0:
                predicted = 1
            else:
                predicted = profile_formula(n, target.bit_count(), target.bit_length(), t)
            AUDIT.check(predicted == actual[target], f"all-time fibre n={n} t={t} target={target}")
            predicted_mass += predicted
        AUDIT.check(predicted_mass == 1 << n, f"time-slice mass n={n} t={t}")

    fibres = layers[1] if max_t >= 1 else Counter()
    image_count = 0
    for target in states:
        formula = one_step_formula(target, n)
        AUDIT.check(formula == fibres[target], f"one-step fibre n={n} target={target}")
        condition = 2 * target.bit_length() <= n + target.bit_count()
        AUDIT.check((formula > 0) == condition, f"image criterion n={n} target={target}")
        image_count += int(formula > 0)
    AUDIT.check(sum(fibres.values()) == 1 << n, f"one-step mass n={n}")
    AUDIT.check(image_count == fibonacci(n + 2), f"Fibonacci image count n={n}")
    AUDIT.check(fibres[0] == fibonacci(n + 1), f"empty fibre Fibonacci n={n}")
    for b in range(n + 1):
        layer_count = sum(
            1 for target in states
            if target.bit_count() == b and one_step_formula(target, n) > 0
        )
        AUDIT.check(layer_count == comb((n + b) // 2, b), f"image layer n={n} b={b}")
    largest = max(fibres.values()) if fibres else 1
    AUDIT.check(largest == fibonacci(n + 1), f"largest fibre size n={n}")
    if n >= 2:
        AUDIT.check([target for target in states if fibres[target] == largest] == [0],
                    f"unique largest fibre n={n}")

    if n <= 10:
        terminal_layer = layers[n - 1 if n >= 1 else 0]
        for target in states:
            if target != prefix_mask(target.bit_count()) and n >= 1:
                AUDIT.check(terminal_layer[target] == 0, f"post-height nonterminal fibre n={n} target={target}")

    return (
        f"n={n} states={1 << n} max_tail={maximum_tail} image1={image_count} "
        f"empty_fibre={fibres[0]} deepest={len(deepest)} orbit_sha256={digest_orbits.hexdigest()}"
    )


def main() -> None:
    check_frozen_artifacts()
    print("P188 process-separated hostile Review B")
    print("reviewer_representation=profile_d_sequence_dp")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print(f"review_a_canonical_sha256={FROZEN_REVIEW_A['CANONICAL.txt']}")
    for n in range(0, 11):
        print(verify_box(n, n + 2))
    for n in range(11, 19):
        states = range(1 << n)
        fibres = Counter(update(mask) for mask in states)
        image_count = sum(value > 0 for value in fibres.values())
        maximum_tail = max(orbit(mask)[0] for mask in states)
        AUDIT.check(maximum_tail == n - 1, f"late sharp tail n={n}")
        AUDIT.check(image_count == fibonacci(n + 2), f"late image count n={n}")
        AUDIT.check(fibres[0] == fibonacci(n + 1), f"late empty fibre n={n}")
        print(
            f"n={n} states={1 << n} max_tail={maximum_tail} image1={image_count} "
            f"empty_fibre={fibres[0]} deepest=1"
        )
    print(f"exact_assertions={AUDIT.assertions}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
