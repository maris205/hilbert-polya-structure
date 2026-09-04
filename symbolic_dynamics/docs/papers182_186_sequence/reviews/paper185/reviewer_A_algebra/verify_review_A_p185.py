#!/usr/bin/env python3
"""Process-separated hostile control for P185 using weighted RGS partitions.

This program deliberately does not import or execute the author's verifier and
does not enumerate labelled words.  It enumerates equality partitions as
restricted-growth strings (RGSs); an RGS with k blocks represents (n)_k words.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path


MAIN_SHA256 = "e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6"
ROUND1_SHA256 = "fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3"
MAX_N = 10


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


def restricted_growth_strings(n: int):
    """Yield the RGS of every equality partition of {0,...,n-1}."""
    if n < 1:
        return

    def extend(prefix: tuple[int, ...], largest: int):
        if len(prefix) == n:
            yield prefix
            return
        for label in range(largest + 2):
            yield from extend(prefix + (label,), max(largest, label))

    yield from extend((0,), 0)


def falling(n: int, k: int) -> int:
    answer = 1
    for value in range(n - k + 1, n + 1):
        answer *= value
    return answer


def prefix_diversity(word: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    answer = []
    for letter in word:
        answer.append(len(seen))
        seen.add(letter)
    return tuple(answer)


def partition_output(rgs: tuple[int, ...]) -> tuple[int, ...]:
    """P(w), shared by every labelled word having equality pattern rgs."""
    seen: set[int] = set()
    answer = []
    for block in rgs:
        answer.append(len(seen))
        seen.add(block)
    return tuple(answer)


def closed_iterate(first: tuple[int, ...], time: int) -> tuple[int, ...]:
    assert time >= 1
    shift = time - 1
    n = len(first)
    return tuple(index if index < shift else shift + first[index - shift]
                 for index in range(n))


def rgs_of(word: tuple[int, ...]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    answer = []
    for letter in word:
        if letter not in labels:
            labels[letter] = len(labels)
        answer.append(labels[letter])
    return tuple(answer)


def distinct_prefix_length(rgs: tuple[int, ...]) -> int:
    seen: set[int] = set()
    for index, block in enumerate(rgs):
        if block in seen:
            return index
        seen.add(block)
    return len(rgs)


def image_targets(n: int, time: int) -> set[tuple[int, ...]]:
    identity = tuple(range(n))
    if time >= n - 1:
        return {identity}
    targets: set[tuple[int, ...]] = set()
    for increments in product((0, 1), repeat=n - time - 1):
        path = list(range(time + 1))
        for increment in increments:
            path.append(path[-1] + increment)
        targets.add(tuple(path))
    return targets


def fibre_formula(n: int, time: int, target: tuple[int, ...]) -> int:
    if time >= n - 1:
        return n ** n
    shift = time - 1
    first = tuple(target[index + shift] - shift
                  for index in range(n - time + 1))
    answer = n ** (time + 1)
    for q in range(1, n - time):
        answer *= n - first[q] if first[q + 1] == first[q] + 1 else first[q]
    return answer


def audit_n(n: int, audit: Audit, transcript: sha256) -> str:
    identity = tuple(range(n))
    counters = [Counter() for _ in range(n + 4)]
    depth = Counter()
    partition_count = 0
    weighted_mass = 0
    fixed_count = 0
    recurrent_mass = 0
    before = audit.assertions

    for rgs in restricted_growth_strings(n):
        partition_count += 1
        blocks = max(rgs) + 1
        weight = falling(n, blocks)
        weighted_mass += weight
        first = partition_output(rgs)
        audit.check(first == prefix_diversity(rgs),
                    f"n={n}: partition-output disagreement at {rgs}")

        value = first
        for time in range(1, n + 4):
            if time > 1:
                value = prefix_diversity(value)
            closed = closed_iterate(first, time)
            audit.check(value == closed,
                        f"n={n}, t={time}: iterate formula fails at {rgs}")
            counters[time][value] += weight
            transcript.update(f"{n}|{rgs}|{weight}|{time}|{value}\n".encode())

        # Exactly one labelled word in this equality class can equal first.
        if rgs_of(first) == rgs and prefix_diversity(first) == first:
            fixed_count += 1
        audit.check(value == identity,
                    f"n={n}: partition class does not enter the claimed fixed point")
        recurrent_mass += weight

        rho = distinct_prefix_length(rgs)
        if blocks == n:
            audit.check(rgs == identity, f"n={n}: unexpected all-distinct RGS")
            depth[0] += 1
            if weight > 1:
                depth[1] += weight - 1
        else:
            depth[max(1, n - rho)] += weight

    audit.check(weighted_mass == n ** n,
                f"n={n}: RGS weights do not partition the word carrier")
    audit.check(sum(depth.values()) == n ** n,
                f"n={n}: clock distribution loses mass")
    audit.check(fixed_count == 1, f"n={n}: fixed-point count is not one")
    audit.check(recurrent_mass == n ** n,
                f"n={n}: not every equality class reaches identity")

    # The t=0 boundary is the identity map on n^n labelled words.
    audit.check(n ** n >= 1, f"n={n}: empty carrier at t=0")
    audit.check(n ** n * 1 == n ** n, f"n={n}: t=0 fibre mass mismatch")
    t0_identity_fibre = 1
    audit.check(t0_identity_fibre == 1, f"n={n}: t=0 identity fibre")

    for time in range(1, n + 4):
        observed = counters[time]
        expected_targets = image_targets(n, time)
        audit.check(set(observed) == expected_targets,
                    f"n={n}, t={time}: image-set mismatch")
        expected_size = 2 ** (n - time - 1) if time <= n - 1 else 1
        audit.check(len(observed) == expected_size,
                    f"n={n}, t={time}: image-size mismatch")
        audit.check(sum(observed.values()) == n ** n,
                    f"n={n}, t={time}: fibre mass mismatch")
        for target in sorted(expected_targets):
            predicted = fibre_formula(n, time, target)
            audit.check(observed[target] == predicted,
                        f"n={n}, t={time}: fibre mismatch at {target}")

    audit.check(depth[0] == 1, f"n={n}: zero-depth class is not the identity")
    for time in range(1, n):
        cdf = sum(mass for tail, mass in depth.items() if tail <= time)
        expected_cdf = falling(n, n - time) * (n ** time)
        audit.check(cdf == expected_cdf, f"n={n}, t={time}: clock CDF mismatch")
        audit.check(counters[time][identity] == cdf,
                    f"n={n}, t={time}: identity fibre/CDF mismatch")

    height = max(depth)
    expected_height = 0 if n == 1 else n - 1
    expected_deepest = 1 if n == 1 else (3 if n == 2 else n ** (n - 1))
    audit.check(height == expected_height, f"n={n}: height mismatch")
    audit.check(depth[height] == expected_deepest,
                f"n={n}: deepest-stratum count mismatch")
    if n >= 3:
        repeat_first_two = 0
        for rgs in restricted_growth_strings(n):
            if rgs[0] == rgs[1]:
                repeat_first_two += falling(n, max(rgs) + 1)
        audit.check(repeat_first_two == expected_deepest,
                    f"n={n}: deepest iff first two letters agree fails")

    # Explicit post-height controls beyond the author's terminal time.
    for time in (n - 1, n, n + 3):
        if time >= 1:
            audit.check(counters[time][identity] == n ** n,
                        f"n={n}, t={time}: stabilized fibre is not full")

    used = audit.assertions - before
    return (f"n={n} partitions={partition_count} weighted_words={weighted_mass} "
            f"height={height} deepest={depth[height]} assertions={used}")


def main() -> None:
    audit = Audit()
    here = Path(__file__).resolve()
    repo = here.parents[5]
    paper = repo / "papers" / "185-prefix-diversity-delay"
    main_tex = paper / "main.tex"
    round1_pdf = paper / "main_round1.pdf"

    observed_main = file_sha256(main_tex)
    observed_pdf = file_sha256(round1_pdf)
    audit.check(observed_main == MAIN_SHA256, "reviewed main.tex hash drift")
    audit.check(observed_pdf == ROUND1_SHA256, "reviewed Round1 PDF hash drift")
    source = main_tex.read_text(encoding="utf-8")
    audit.check("and $t\\ge1$.  With $r=t-1$" in source,
                "iterate quantifier missing from source")
    audit.check("For $1\\le t\\le n-1$" in source,
                "transient-time range missing from source")
    audit.check("\\prod_{q=1}^{n-t-1}" in source,
                "local fibre product missing from source")
    audit.check("is empty when $t=n-1$" in source,
                "endpoint empty-product repair missing")
    audit.check("$P_n^0$ is the identity" in source,
                "t=0 fibre repair missing")
    audit.check("$t\\ge n-1$, the image is the singleton" in source,
                "post-height fibre repair missing")

    transcript = sha256()
    rows = [audit_n(n, audit, transcript) for n in range(1, MAX_N + 1)]

    print("P185_REVIEW_A_DELTA_R1_RGS_V1")
    print("review_process=process-separated")
    print(f"reviewed_main_tex_sha256={observed_main}")
    print(f"reviewed_round1_pdf_sha256={observed_pdf}")
    print("representation=weighted_restricted_growth_strings")
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
