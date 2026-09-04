#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P187 Round 1.

This script does not import the author verifier or Review-A code.  For each
prime exponent target it solves the cyclic predecessor problem by explicit
start-value propagation through the difference constraints `(u-v)_+=b`,
rather than by matrix traces or Review A's closed-walk transfer.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import product
from math import gcd
from hashlib import sha256
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT / "papers" / "187-cyclic-divisor-quotient"
REVIEW_A = ROOT / "docs" / "papers187_191_sequence" / "reviews" / "p187_a"

FROZEN = {
    "main.tex": "e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d",
    "references.bib": "b7ead243e824ca143e9726bb83a58dd10a4428e0c58fccb0668f3e195ea274bd",
    "code/verify_p187.py": "bb171bd84a5f614b868c6fd6e6008c646a282045bef484d4552081967743cf1e",
    "code/CANONICAL.txt": "b48c1753908ca9b168803cb6406499945bb59a82ac16d0f1f87e9ef278f8bb8d",
    "PROOF_PACKAGE.md": "095d2370f9c4f4b5d62e909a773f9a2fc05f2577ea8313b39472843b6071955d",
    "SOURCE_VERIFICATION.md": "cdf97a65b4df3ac1f1ea4a3c8959d2db0ffc367777d3e00080c8c9bd854eedac",
    "main_round0_original.pdf": "399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1",
    "main_round1.pdf": "399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1",
    "main.pdf": "399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1",
}

FROZEN_REVIEW_A = {
    "HOSTILE_REVIEW_A.md": "4e65d9c23343f4643d8aaf7a963139ed3cd0990158cf7c7fc636a31eecefdefa",
    "DELTA.md": "3f3266032ecf9876b93163c1c86cb72ba3462f9d7fc1b6730d4cc4d58c8fae20",
    "verify_review_a_p187.py": "70088e5a5b47a58057b64b5ce61ff29d409b9c4297cd5e444b3f314ec1bc9467",
    "CANONICAL.txt": "596ec6ebf0c61042499f51b802a3014f384345ef16d275e8bb41bb324538539c",
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
        r"I_1(z)=1",
        r"I_2(z)=1+2z",
        r"HOLD\_EXTERNAL",
        "278,456",
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


def difference(word: tuple[int, ...]) -> tuple[int, ...]:
    m = len(word)
    return tuple(max(word[i] - word[(i + 1) % m], 0) for i in range(m))


def tail_to_fixed(update, state) -> int:
    seen = {}
    current = state
    while current not in seen:
        seen[current] = len(seen)
        nxt = update(current)
        if nxt == current:
            return seen[current]
        current = nxt
    raise AssertionError("unexpected nonfixed cycle")


@lru_cache(maxsize=None)
def cyclic_difference_fibre(a: int, target: tuple[int, ...]) -> int:
    m = len(target)
    total = 0
    for start in range(a + 1):
        current = Counter({start: 1})
        for i in range(m):
            b = target[i]
            nxt: Counter[int] = Counter()
            for u, count in current.items():
                if b > 0:
                    v = u - b
                    if 0 <= v <= a:
                        nxt[v] += count
                else:
                    for v in range(u, a + 1):
                        nxt[v] += count
            current = nxt
        total += current[start]
    return total


def fixed_factor(a: int, m: int) -> int:
    if m == 1:
        return 1
    if m == 2:
        return 1 + 2 * a
    prev2 = 1
    prev1 = 1 + 2 * a
    for _ in range(3, m + 1):
        prev2, prev1 = prev1, prev1 + a * prev2
    return prev1


def factor(n: int) -> tuple[tuple[int, int], ...]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            out.append((p, exponent))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def divisors(n: int) -> tuple[int, ...]:
    out = [1]
    for p, exponent in factor(n):
        out = [d * p ** e for d in out for e in range(exponent + 1)]
    return tuple(sorted(out))


def valuation(x: int, p: int) -> int:
    exponent = 0
    while x % p == 0:
        x //= p
        exponent += 1
    return exponent


def divisor_update(word: tuple[int, ...]) -> tuple[int, ...]:
    m = len(word)
    return tuple(word[i] // gcd(word[i], word[(i + 1) % m]) for i in range(m))


def exponent_box(a: int, m: int) -> str:
    states = tuple(product(range(a + 1), repeat=m))
    fibres: Counter[tuple[int, ...]] = Counter()
    fixed = 0
    maximum = 0
    digest_transitions = sha256()

    for state in states:
        target = difference(state)
        fibres[target] += 1
        digest_transitions.update(f"{a}:{m}:{state}->{target};".encode("ascii"))
        tail = tail_to_fixed(difference, state)
        maximum = max(maximum, tail)
        AUDIT.check(tail >= 0, f"nonnegative tail a={a} m={m}")
        support_condition = all(state[i] == 0 or state[(i + 1) % m] == 0 for i in range(m))
        AUDIT.check((target == state) == support_condition, f"fixed support a={a} m={m}")
        fixed += int(target == state)

    expected_height = 1 if m <= 2 else a
    AUDIT.check(maximum == expected_height, f"sharp exponent height a={a} m={m}")
    AUDIT.check(fixed == fixed_factor(a, m), f"fixed factor a={a} m={m}")
    total_mass = 0
    for target in states:
        predicted = cyclic_difference_fibre(a, target)
        actual = fibres[target]
        AUDIT.check(predicted == actual, f"exponent fibre a={a} m={m} target={target}")
        if all(b > 0 for b in target):
            AUDIT.check(predicted == 0, f"common-prime obstruction a={a} m={m} target={target}")
        total_mass += predicted
    AUDIT.check(total_mass == len(states), f"exponent mass a={a} m={m}")
    AUDIT.check(cyclic_difference_fibre(a, (0,) * m) == a + 1, f"all-one exponent fibre a={a} m={m}")

    return (
        f"a={a} m={m} states={len(states)} fixed={fixed} max_tail={maximum} "
        f"all_one_fibre={cyclic_difference_fibre(a, (0,) * m)} "
        f"transition_sha256={digest_transitions.hexdigest()}"
    )


def composite_box(n: int, m: int) -> str:
    ds = divisors(n)
    fac = factor(n)
    states = tuple(product(ds, repeat=m))
    fibres: Counter[tuple[int, ...]] = Counter()
    fixed = 0
    maximum = 0
    digest_transitions = sha256()

    for state in states:
        target = divisor_update(state)
        fibres[target] += 1
        digest_transitions.update(f"{n}:{m}:{state}->{target};".encode("ascii"))
        tail = tail_to_fixed(divisor_update, state)
        maximum = max(maximum, tail)
        fixed += int(target == state)
        for p, _ in fac:
            AUDIT.check(
                tuple(valuation(v, p) for v in target) == difference(tuple(valuation(v, p) for v in state)),
                f"primewise conjugacy n={n} m={m} p={p}",
            )

    expected_height = 0 if n == 1 else (1 if m <= 2 else max(exponent for _, exponent in fac))
    AUDIT.check(maximum == expected_height, f"composite sharp height n={n} m={m}")

    predicted_fixed = 1
    for _p, exponent in fac:
        predicted_fixed *= fixed_factor(exponent, m)
    AUDIT.check(fixed == predicted_fixed, f"fixed census n={n} m={m}")

    total_mass = 0
    for target in states:
        predicted = 1
        for p, exponent in fac:
            b = tuple(valuation(v, p) for v in target)
            predicted *= cyclic_difference_fibre(exponent, b)
        AUDIT.check(predicted == fibres[target], f"composite fibre n={n} m={m} target={target}")
        if target == (1,) * m:
            AUDIT.check(predicted == len(ds), f"all-one divisor fibre n={n} m={m}")
        if gcd(*target) > 1:
            AUDIT.check(predicted == 0, f"common-prime obstruction n={n} m={m} target={target}")
        total_mass += predicted
    AUDIT.check(total_mass == len(states), f"composite mass n={n} m={m}")

    return (
        f"N={n} m={m} states={len(states)} fixed={fixed} max_tail={maximum} "
        f"image={len(fibres)} all_one_fibre={fibres[(1,) * m]} "
        f"transition_sha256={digest_transitions.hexdigest()}"
    )


def main() -> None:
    check_frozen_artifacts()
    print("P187 process-separated hostile Review B")
    print("reviewer_representation=cyclic_difference_constraint_dp")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print(f"review_a_canonical_sha256={FROZEN_REVIEW_A['CANONICAL.txt']}")
    for a in range(1, 5):
        for m in range(1, 7):
            print(exponent_box(a, m))
    for n in (1, 2, 4, 6, 12, 18, 36, 60):
        for m in range(1, 5):
            print(composite_box(n, m))
    print(f"exact_assertions={AUDIT.assertions}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
