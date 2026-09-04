#!/usr/bin/env python3
"""Process-separated hostile control for P186 using positive gap compositions.

No subset masks and no author's subset-loop verifier are used.  Every nonempty
state is represented uniquely by its minimum and a positive gap composition.
Fibres are checked by a separate weak-sequence/slot inverse reconstruction.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from math import comb
from pathlib import Path


MAIN_SHA256 = "e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394"
ROUND1_SHA256 = "449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48"
MAX_N = 18
EMPTY = (-1, ())


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


@lru_cache(maxsize=None)
def positive_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    answer = []
    for first in range(1, total + 1):
        for suffix in positive_compositions(total - first):
            answer.append((first,) + suffix)
    return tuple(answer)


def gap_states(n: int):
    """Bijection: empty, or (minimum, positive consecutive-gap word)."""
    yield EMPTY
    for minimum in range(n):
        budget = n - 1 - minimum
        for span in range(budget + 1):
            for gaps in positive_compositions(span):
                yield (minimum, gaps)


def erode_once(state: tuple[int, tuple[int, ...]]):
    minimum, gaps = state
    if minimum < 0:
        return EMPTY
    return (minimum, tuple(gap - 1 for gap in gaps if gap > 1))


def erode_closed(state: tuple[int, tuple[int, ...]], time: int):
    minimum, gaps = state
    if minimum < 0:
        return EMPTY
    return (minimum, tuple(gap - time for gap in gaps if gap > time))


def last_value(state: tuple[int, tuple[int, ...]]) -> int:
    minimum, gaps = state
    return minimum + sum(gaps)


@lru_cache(maxsize=None)
def short_word_count(time: int, span: int) -> int:
    """Ordered positive compositions of span with every part at most time."""
    if span == 0:
        return 1
    if time == 0:
        return 0
    return sum(short_word_count(time, span - part)
               for part in range(1, min(time, span) + 1))


@lru_cache(maxsize=None)
def slot_inverse_count(time: int, slots: int, budget: int) -> int:
    """Exact-total weak-sequence reconstruction across insertion slots."""
    if budget < 0:
        return 0
    if slots == 0:
        return int(budget == 0)
    return sum(short_word_count(time, span)
               * slot_inverse_count(time, slots - 1, budget - span)
               for span in range(budget + 1))


def fibre_formula(n: int, time: int,
                  target: tuple[int, tuple[int, ...]]) -> int:
    minimum, gaps = target
    if minimum < 0:
        return 1
    r = len(gaps)
    budget = n - 1 - minimum - sum(gaps) - time * r
    if budget < 0:
        return 0
    # Sum over total optional short-gap span <= budget.
    return sum(slot_inverse_count(time, r + 1, total)
               for total in range(budget + 1))


def fibonacci(index: int) -> int:
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def audit_n(n: int, audit: Audit, transcript: sha256) -> str:
    states = list(gap_states(n))
    before = audit.assertions
    audit.check(len(states) == 2 ** n,
                f"n={n}: gap-composition carrier size mismatch")
    audit.check(len(set(states)) == len(states),
                f"n={n}: gap representation is not injective")

    counters = [Counter() for _ in range(n + 4)]
    depth = Counter()
    basin = Counter()
    fixed = 0
    for state in states:
        value = state
        minimum, gaps = state
        tail = max(gaps, default=0)
        depth[tail] += 1
        basin[minimum] += 1
        if erode_once(state) == state:
            fixed += 1
        for time in range(n + 4):
            if time > 0:
                value = erode_once(value)
            closed = erode_closed(state, time)
            audit.check(value == closed,
                        f"n={n}, t={time}: erosion law fails at {state}")
            counters[time][value] += 1
            transcript.update(f"{n}|{state}|{time}|{value}\n".encode())

    audit.check(fixed == n + 1, f"n={n}: fixed/recurrent count mismatch")
    audit.check(basin[-1] == 1, f"n={n}: empty basin mismatch")
    for minimum in range(n):
        audit.check(basin[minimum] == 2 ** (n - 1 - minimum),
                    f"n={n}: singleton basin mismatch at {minimum}")

    for time in range(n + 4):
        observed = counters[time]
        expected_targets = {
            state for state in states
            if state == EMPTY or last_value(state) + time * len(state[1]) < n
        }
        audit.check(set(observed) == expected_targets,
                    f"n={n}, t={time}: image criterion mismatch")
        expected_size = 1 + sum(comb(n - time * r, r + 1)
                                if n - time * r >= r + 1 else 0
                                for r in range(n))
        audit.check(len(observed) == expected_size,
                    f"n={n}, t={time}: image-size sum mismatch")
        audit.check(sum(observed.values()) == 2 ** n,
                    f"n={n}, t={time}: fibre mass mismatch")
        for target in expected_targets:
            predicted = fibre_formula(n, time, target)
            audit.check(observed[target] == predicted,
                        f"n={n}, t={time}: inverse reconstruction fails at {target}")
            if time == 0:
                audit.check(predicted == 1,
                            f"n={n}: t=0 fibre is not singleton at {target}")
            if time == 1 and target != EMPTY:
                direct_binomial = comb(n - last_value(target), len(target[1]) + 1)
                audit.check(predicted == direct_binomial,
                            f"n={n}: t=1 binomial specialization fails at {target}")
        if time == 1:
            audit.check(len(observed) == fibonacci(n + 2),
                        f"n={n}: Fibonacci image specialization fails")

    # Clock CDF and depth shells, reconstructed from bounded gap words.
    for height in range(n + 2):
        observed_cdf = sum(mass for tail, mass in depth.items() if tail <= height)
        reconstructed = 1
        for minimum in range(n):
            budget = n - 1 - minimum
            reconstructed += sum(short_word_count(height, span)
                                 for span in range(budget + 1))
        audit.check(observed_cdf == reconstructed,
                    f"n={n}, h={height}: clock CDF mismatch")
        if height >= 1:
            prior = sum(mass for tail, mass in depth.items() if tail <= height - 1)
            audit.check(depth[height] == observed_cdf - prior,
                        f"n={n}, h={height}: depth-shell difference mismatch")

    height = max(depth)
    expected_height = 0 if n == 1 else n - 1
    expected_deepest = 2 if n == 1 else 1
    audit.check(height == expected_height, f"n={n}: global height mismatch")
    audit.check(depth[height] == expected_deepest,
                f"n={n}: deepest-stratum multiplicity mismatch")
    if n >= 2:
        audit.check([state for state in states if max(state[1], default=0) == n - 1]
                    == [(0, (n - 1,))],
                    f"n={n}: unique deepest state is not {{0,n-1}}")

    # Explicit stabilization checks at and beyond the global height.
    for time in (n - 1, n, n + 3):
        audit.check(len(counters[time]) == n + 1,
                    f"n={n}, t={time}: image has not stabilized to fixed states")
        audit.check(counters[time][EMPTY] == 1,
                    f"n={n}, t={time}: empty fibre mismatch")
        for minimum in range(n):
            audit.check(counters[time][(minimum, ())] == 2 ** (n - 1 - minimum),
                        f"n={n}, t={time}: stabilized singleton fibre mismatch")

    used = audit.assertions - before
    return (f"n={n} gap_states={len(states)} height={height} "
            f"deepest={depth[height]} image_t1={len(counters[1])} assertions={used}")


def main() -> None:
    audit = Audit()
    here = Path(__file__).resolve()
    repo = here.parents[5]
    paper = repo / "papers" / "186-rank-compression-support"
    main_tex = paper / "main.tex"
    round1_pdf = paper / "main_round1.pdf"

    observed_main = file_sha256(main_tex)
    observed_pdf = file_sha256(round1_pdf)
    audit.check(observed_main == MAIN_SHA256, "reviewed main.tex hash drift")
    audit.check(observed_pdf == ROUND1_SHA256, "reviewed Round1 PDF hash drift")
    source = main_tex.read_text(encoding="utf-8")
    audit.check("and $t\\ge0$, the empty set remains empty" in source,
                "all-time iterate quantifier missing")
    audit.check("with a negative upper limit interpreted as zero" in source,
                "negative-budget convention missing")
    audit.check("the global height is $n-1$" in source,
                "height theorem missing from source")
    audit.check("contributes $g-t$ exactly when $g>t$" in source,
                "abstract gap-positivity repair missing")
    audit.check("for $n\\ge2$, there is a unique" in source,
                "abstract n>=2 extremal repair missing")

    transcript = sha256()
    rows = [audit_n(n, audit, transcript) for n in range(1, MAX_N + 1)]

    print("P186_REVIEW_A_DELTA_R1_GAP_COMPOSITIONS_V1")
    print("review_process=process-separated")
    print(f"reviewed_main_tex_sha256={observed_main}")
    print(f"reviewed_round1_pdf_sha256={observed_pdf}")
    print("representation=minimum_plus_positive_gap_composition")
    print("inverse_control=weak_sequence_slot_reconstruction")
    print("boundary_times=t0_and_t>=height_explicit")
    for row in rows:
        print(row)
    print("formal_counterexamples=0")
    print("findings=critical:0,major:0,minor:0")
    print(f"transition_digest={transcript.hexdigest()}")
    print(f"exact_assertions={audit.assertions}")
    print("status=PASS_DELTA_ACCEPTED")


if __name__ == "__main__":
    main()
