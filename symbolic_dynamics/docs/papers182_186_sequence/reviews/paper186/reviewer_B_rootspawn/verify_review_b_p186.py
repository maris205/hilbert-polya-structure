#!/usr/bin/env python3
"""Hostile Review B control for P186 in weak rank-profile coordinates.

The author enumerates subset masks; Review A uses a minimum plus a positive
gap composition and reconstructs inverse slots recursively.  This verifier
uses neither.  A k-set is encoded by its weakly increasing rank profile
b_j=a_j-j (a partition in a k by n-k rectangle).  Claimed coefficient sums
are evaluated by a signed inclusion-exclusion formula over the number of
short letters, rather than by slot recursion or polynomial multiplication.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path


MAIN_SHA256 = "e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394"
ROUND1_SHA256 = "449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48"
ROUND0_SHA256 = "6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431"
MAX_EXHAUSTIVE_N = 17
ORIENTATION_N = 18
MAX_SYMBOLIC_N = 64


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


def verify_manifest(directory: Path, manifest_name: str = "SHA256SUMS") -> int:
    rows = 0
    for raw in (directory / manifest_name).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        digest, name = raw.split(maxsplit=1)
        name = name.lstrip(" *")
        if name == manifest_name:
            raise AssertionError("self-referential manifest")
        if file_sha256(directory / name) != digest:
            raise AssertionError(f"manifest mismatch: {directory / name}")
        rows += 1
    return rows


def safe_comb(n: int, k: int) -> int:
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def weak_rank_profiles(n: int):
    """All partitions in the disjoint union of k by (n-k) rectangles."""
    yield ()
    for size in range(1, n + 1):
        for profile in combinations_with_replacement(range(n - size + 1),
                                                      size):
            yield profile


def profile_to_points(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value + rank for rank, value in enumerate(profile))


def profile_step(profile: tuple[int, ...]) -> tuple[int, ...]:
    """Apply T entirely in rank-profile coordinates."""
    distinct = tuple(dict.fromkeys(profile))
    return tuple(value - rank for rank, value in enumerate(distinct))


def closed_points(profile: tuple[int, ...], time: int) -> tuple[int, ...]:
    if time == 0:
        return profile_to_points(profile)
    if not profile:
        return ()
    answer = [profile[0]]
    for index in range(1, len(profile)):
        rank_jump = profile[index] - profile[index - 1]
        # Original point gap is rank_jump+1.  It survives precisely when
        # rank_jump >= time and then contributes rank_jump+1-time.
        if rank_jump >= time:
            answer.append(answer[-1] + rank_jump + 1 - time)
    return tuple(answer)


def entrance_time(profile: tuple[int, ...]) -> int:
    if len(profile) <= 1:
        return 0
    return max(profile[index] - profile[index - 1] + 1
               for index in range(1, len(profile)))


def fibonacci(index: int) -> int:
    left, right = 0, 1
    for _ in range(index):
        left, right = right, left + right
    return left


@lru_cache(maxsize=None)
def bounded_words_leq(bound: int, length: int, budget: int) -> int:
    """Length-fixed words in [1,bound] with total at most budget, by IE."""
    if length == 0:
        return 1
    if bound == 0 or budget < length:
        return 0
    return sum(
        (-1) ** excluded * comb(length, excluded)
        * safe_comb(budget - excluded * bound, length)
        for excluded in range(length + 1)
    )


@lru_cache(maxsize=None)
def bounded_words_exact(bound: int, length: int, total: int) -> int:
    """Length-fixed words in [1,bound] with exact total, by IE."""
    if length == 0:
        return int(total == 0)
    if bound == 0 or total < length:
        return 0
    return sum(
        (-1) ** excluded * comb(length, excluded)
        * safe_comb(total - excluded * bound - 1, length - 1)
        for excluded in range(length + 1)
    )


@lru_cache(maxsize=None)
def coefficient_fibre(time: int, target_gaps: int, budget: int) -> int:
    """Inclusive coefficient sum, expanded by number of short letters.

    (1-S)^-(r+1) = sum_L C(L+r,r) S^L.  The second factor below is evaluated
    by inclusion-exclusion, independently of either earlier verifier.
    """
    if budget < 0:
        return 0
    return sum(
        comb(length + target_gaps, target_gaps)
        * bounded_words_leq(time, length, budget)
        for length in range(budget + 1)
    )


def claimed_fibre(n: int, time: int, target: tuple[int, ...]) -> int:
    if not target:
        return 1
    target_gaps = len(target) - 1
    budget = n - 1 - target[-1] - time * target_gaps
    return coefficient_fibre(time, target_gaps, budget)


def image_condition(n: int, time: int, target: tuple[int, ...]) -> bool:
    return not target or target[-1] + time * (len(target) - 1) < n


def image_size(n: int, time: int) -> int:
    return 1 + sum(safe_comb(n - time * gaps, gaps + 1)
                   for gaps in range(n))


@lru_cache(maxsize=None)
def depth_cdf_inclusion(n: int, height: int) -> int:
    answer = 1  # empty state
    for length in range(n):
        for span in range(n):
            answer += (n - span) * bounded_words_exact(height, length, span)
    return answer


def audit_rank(n: int, audit: Audit, transcript: sha256) -> str:
    before = audit.assertions
    profiles = list(weak_rank_profiles(n))
    targets = [profile_to_points(profile) for profile in profiles]
    audit.check(len(profiles) == 2 ** n,
                f"n={n}: rank-profile carrier cardinality")
    audit.check(len(set(profiles)) == len(profiles),
                f"n={n}: repeated rank profile")
    audit.check(len(set(targets)) == len(targets),
                f"n={n}: rank-profile decoding not injective")

    fibres = [Counter() for _ in range(n + 4)]
    depths = Counter()
    basins = Counter()
    fixed = 0

    for profile in profiles:
        size = len(profile)
        audit.check(all(profile[index] <= profile[index + 1]
                        for index in range(size - 1)),
                    f"n={n}: profile is not weakly increasing")
        audit.check(all(0 <= value <= n - size for value in profile),
                    f"n={n}: profile leaves its rectangle")
        points = profile_to_points(profile)
        audit.check(all(points[index] < points[index + 1]
                        for index in range(size - 1)),
                    f"n={n}: decoded points are not strict")

        depth = entrance_time(profile)
        depths[depth] += 1
        basins[-1 if not profile else profile[0]] += 1
        if profile_step(profile) == profile:
            fixed += 1

        value_profile = profile
        for time in range(n + 4):
            if time:
                value_profile = profile_step(value_profile)
            observed = profile_to_points(value_profile)
            closed = closed_points(profile, time)
            audit.check(observed == closed,
                        f"n={n}, t={time}: rank-jump erosion mismatch")
            fibres[time][observed] += 1
            transcript.update(f"{n}|{profile}|{time}|{observed}\n".encode())

    audit.check(fixed == n + 1, f"n={n}: fixed/recurrent census")
    audit.check(basins[-1] == 1, f"n={n}: empty basin")
    for minimum in range(n):
        audit.check(basins[minimum] == 2 ** (n - minimum - 1),
                    f"n={n}: singleton basin at {minimum}")

    for time in range(n + 4):
        observed = fibres[time]
        expected = {target for target in targets
                    if image_condition(n, time, target)}
        audit.check(set(observed) == expected,
                    f"n={n}, t={time}: exact image criterion")
        audit.check(len(observed) == image_size(n, time),
                    f"n={n}, t={time}: image-size sum")
        audit.check(sum(observed.values()) == 2 ** n,
                    f"n={n}, t={time}: fibre mass")

        # Every carrier target is checked, not only image targets.  Thus a
        # negative coefficient budget is checked as an actual zero fibre.
        for target in targets:
            predicted = claimed_fibre(n, time, target)
            audit.check(observed[target] == predicted,
                        f"n={n}, t={time}: every-target coefficient fibre")
            if time == 0:
                audit.check(predicted == 1,
                            f"n={n}: time-zero fibre is not one")
            if time == 1 and target:
                audit.check(predicted == comb(n - target[-1], len(target)),
                            f"n={n}: one-step binomial fibre")
            if target and not image_condition(n, time, target):
                audit.check(predicted == 0,
                            f"n={n}, t={time}: negative budget is not zero")

        if time == 1:
            audit.check(len(observed) == fibonacci(n + 2),
                        f"n={n}: Fibonacci first image")
        if time >= n - 1:
            audit.check(set(observed) == {()} | {(minimum,) for minimum in range(n)},
                        f"n={n}, t={time}: post-height image")

    for height in range(n + 2):
        observed_cdf = sum(mass for depth, mass in depths.items()
                           if depth <= height)
        predicted_cdf = depth_cdf_inclusion(n, height)
        audit.check(observed_cdf == predicted_cdf,
                    f"n={n}, h={height}: bounded-gap CDF")
        if height >= 1:
            prior = sum(mass for depth, mass in depths.items()
                        if depth <= height - 1)
            audit.check(depths[height] == observed_cdf - prior,
                        f"n={n}, h={height}: depth shell")

    height = max(depths)
    expected_height = 0 if n == 1 else n - 1
    audit.check(height == expected_height, f"n={n}: sharp height")
    if n == 1:
        audit.check(depths[0] == 2, "n=1: both fixed states have depth zero")
    else:
        deepest = [profile_to_points(profile) for profile in profiles
                   if entrance_time(profile) == n - 1]
        audit.check(deepest == [(0, n - 1)],
                    f"n={n}: unique deepest state")

    max_first_fibre = max(fibres[1].values())
    used = audit.assertions - before
    return (
        f"n={n} weak_profiles={len(profiles)} height={height} "
        f"deepest={depths[height]} image_t1={len(fibres[1])} "
        f"max_fibre_t1={max_first_fibre} assertions={used}"
    )


def audit_orientation_18(audit: Audit) -> str:
    n = ORIENTATION_N
    profiles = list(weak_rank_profiles(n))
    first_fibres = Counter()
    depths = Counter()
    fixed = 0
    for profile in profiles:
        first = profile_to_points(profile_step(profile))
        first_fibres[first] += 1
        depths[entrance_time(profile)] += 1
        fixed += int(profile_step(profile) == profile)
    audit.check(len(profiles) == 2 ** n, "n=18: orientation carrier")
    audit.check(len(first_fibres) == 6765, "n=18: orientation image")
    audit.check(fixed == 19, "n=18: orientation fixed states")
    audit.check(max(first_fibres.values()) == 2002,
                "n=18: orientation maximum fibre")
    deepest = [profile_to_points(profile) for profile in profiles
               if entrance_time(profile) == 17]
    audit.check(deepest == [(0, 17)], "n=18: orientation deepest state")
    return ("n=18 weak_profiles=262144 image_t1=6765 fixed=19 "
            "max_fibre_t1=2002 unique_deepest=(0,17)")


def main() -> None:
    audit = Audit()
    here = Path(__file__).resolve()
    repo = here.parents[5]
    paper = repo / "papers" / "186-rank-compression-support"
    review_a = (repo / "docs" / "papers182_186_sequence" / "reviews" /
                "paper186" / "reviewer_A_algebra")

    main_tex = paper / "main.tex"
    round1_pdf = paper / "main_round1.pdf"
    observed_main = file_sha256(main_tex)
    observed_round1 = file_sha256(round1_pdf)
    audit.check(observed_main == MAIN_SHA256, "frozen main.tex hash drift")
    audit.check(observed_round1 == ROUND1_SHA256, "frozen Round1 PDF hash drift")
    audit.check(file_sha256(paper / "main.pdf") == ROUND1_SHA256,
                "live PDF is not frozen Round1")
    audit.check(file_sha256(paper / "main_round0_original.pdf") == ROUND0_SHA256,
                "Round0 PDF receipt drift")
    review_a_rows = verify_manifest(review_a)
    audit.check(review_a_rows == 4, "Review-A manifest row count")

    source = main_tex.read_text(encoding="utf-8")
    for needle, label in (
        ("For every $A\\in\\X_n$ and $t\\ge0$", "iterate quantifier"),
        ("g_j-t:g_j>t", "strict gap-survival threshold"),
        ("with a negative upper limit interpreted as zero", "negative budget"),
        ("For every $h\\ge0$", "CDF quantifier"),
        ("for $n\\ge2$, there is a unique", "abstract extremal repair"),
        ("contributes $g-t$ exactly when $g>t$", "abstract positivity repair"),
        ("non-hit is neither novelty nor priority evidence", "owner disclaimer"),
        ("\\textsc{owner\\_amber / hold\\_external}", "external hold"),
        ("\\author{Anonymous}", "anonymous author"),
    ):
        audit.check(needle in source, f"source surface missing: {label}")
    audit.check("\\cite{Stanley2012}" in source, "Stanley citation absent")
    audit.check("\\cite{Fayers2023}" in source, "Fayers citation absent")

    transcript = sha256()
    rows = [audit_rank(n, audit, transcript)
            for n in range(1, MAX_EXHAUSTIVE_N + 1)]
    orientation_row = audit_orientation_18(audit)

    symbolic_before = audit.assertions
    for n in range(1, MAX_SYMBOLIC_N + 1):
        audit.check(image_size(n, 0) == 2 ** n,
                    f"n={n}: symbolic t=0 image")
        audit.check(image_size(n, 1) == fibonacci(n + 2),
                    f"n={n}: symbolic Fibonacci image")
        audit.check(depth_cdf_inclusion(n, 0) == n + 1,
                    f"n={n}: symbolic fixed CDF")
        audit.check(depth_cdf_inclusion(n, n - 1) == 2 ** n,
                    f"n={n}: symbolic terminal CDF")
        for target_gaps in range(n):
            for budget in (-1, 0, n - 1):
                value = coefficient_fibre(n - 1, target_gaps, budget)
                audit.check(value == 0 if budget < 0 else value >= 1,
                            f"n={n}: signed coefficient boundary")
    symbolic_assertions = audit.assertions - symbolic_before

    print("P186_HOSTILE_REVIEW_B_WEAK_RANK_PROFILE_IE_V1")
    print("review_process=process-separated")
    print(f"frozen_main_tex_sha256={observed_main}")
    print(f"frozen_round1_pdf_sha256={observed_round1}")
    print("representation=weak_rank_profiles_bj_equals_aj_minus_j")
    print("inverse_control=signed_inclusion_exclusion_by_short_word_length")
    print("excluded_representations=subset_masks_and_positive_gap_compositions")
    print("boundary_times=t0_t1_tnminus1_and_postheight")
    print(f"review_a_manifest_rows={review_a_rows}")
    for row in rows:
        print(row)
    print(orientation_row)
    print(f"symbolic_stress_n=1..{MAX_SYMBOLIC_N}")
    print(f"symbolic_stress_assertions={symbolic_assertions}")
    print(f"transition_digest={transcript.hexdigest()}")
    print(f"exact_assertions={audit.assertions}")
    print("formal_counterexamples=0")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("decision=ACCEPT_ROUND1_FOR_COORDINATOR_GATE")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
