#!/usr/bin/env python3
"""Process-separated exact verifier for P191 Hostile Review A.

No author code is imported.  Positive compositions are generated recursively
as tuples (never from cut masks), the literal update is executed by direct
merge/flush transitions, global fibres are obtained by inverse-candidate
binning, and interval factors are computed by a memoized backward recurrence.
An additional brute enumeration of interval refinements checks that DP.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve()
PAPER = HERE.parents[3]
MAX_N = 18

PINNED = {
    "main_round0_original.pdf":
        "d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b",
    "main.tex":
        "bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84",
    "code/verify.py":
        "70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50",
    "code/CANONICAL.txt":
        "c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c",
    "PROOF_PACKAGE.md":
        "f89ab89d2f9fa2f82eb6482129f4803870c3b3240d7a9eb8b31bd8579511d9ef",
    "SOURCE_VERIFICATION.md":
        "26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9",
}


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got={got!r}, expected={expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def pin_inputs() -> None:
    for relative, expected in PINNED.items():
        AUDIT.equal(sha256((PAPER / relative).read_bytes()).hexdigest(), expected,
                    f"pinned {relative}")
    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    ledger = (PAPER / "SOURCE_VERIFICATION.md").read_text(encoding="utf-8")
    AUDIT.true("The final\nendpoint $N$ is not a cut and is never tested" in source,
               "final endpoint source boundary")
    AUDIT.true("a non-hit is not evidence of novelty" in source,
               "manuscript non-hit boundary")
    AUDIT.true(r"\texttt{HOLD\_EXTERNAL}" in source,
               "manuscript lifecycle boundary")
    AUDIT.true("This bounded non-hit is not novelty" in ledger,
               "owner-ledger non-hit boundary")
    # Delta acceptance: the false database-footer date is absent and the
    # repaired statement is tied explicitly to the entry history.
    AUDIT.equal(
        (
            ledger.count("modified 27 August 2026"),
            ledger.count("approved/latest entry revision 22 July 2026"),
        ),
        (0, 1),
        "OEIS entry-history delta",
    )


@lru_cache(maxsize=None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    """Recursive first-part construction; no subset/cut-mask representation."""
    if total == 0:
        return ((),)
    return tuple(
        (first,) + suffix
        for first in range(1, total + 1)
        for suffix in compositions(total - first)
    )


def direct_merge_update(source: tuple[int, ...]) -> tuple[int, ...]:
    """Literal simultaneous rule implemented by merge blocks, not cut sets."""
    output = []
    pending = 0
    prefix = 0
    for index, part in enumerate(source):
        pending += part
        prefix += part
        final = index == len(source) - 1
        if final or prefix % part == 0:
            output.append(pending)
            pending = 0
    return tuple(output)


def fixed_predicate(source: tuple[int, ...]) -> bool:
    prefix = 0
    for part in source[:-1]:
        prefix += part
        if prefix % part:
            return False
    return True


def orbit_signature(source: tuple[int, ...]) -> tuple[int, int]:
    first_seen = {}
    state = source
    while state not in first_seen:
        first_seen[state] = len(first_seen)
        state = direct_merge_update(state)
    return first_seen[state], len(first_seen) - first_seen[state]


def fixed_count_recurrence(total: int) -> int:
    stable = [0] * total
    stable[0] = 1
    for endpoint in range(1, total):
        for incoming in range(1, endpoint + 1):
            if endpoint % incoming == 0:
                stable[endpoint] += stable[endpoint - incoming]
    return sum(stable)


def endpoints(target: tuple[int, ...]) -> tuple[int, ...]:
    running = 0
    result = []
    for part in target:
        running += part
        result.append(running)
    return tuple(result)


@lru_cache(maxsize=None)
def interval_factor(left: int, right: int, terminal: bool) -> int:
    """Backward interval DP in the global endpoint coordinates."""

    @lru_cache(maxsize=None)
    def deleted_prefix_ways(endpoint: int) -> int:
        if endpoint == left:
            return 1
        return sum(
            deleted_prefix_ways(previous)
            for previous in range(left, endpoint)
            if endpoint % (endpoint - previous) != 0
        )

    if terminal:
        # The last source part is deliberately not tested.
        return sum(deleted_prefix_ways(previous)
                   for previous in range(left, right))
    return sum(
        deleted_prefix_ways(previous)
        for previous in range(left, right)
        if right % (right - previous) == 0
    )


def factorized_fibre(target: tuple[int, ...]) -> int:
    target_endpoints = endpoints(target)
    left = 0
    answer = 1
    for index, right in enumerate(target_endpoints):
        answer *= interval_factor(left, right,
                                  terminal=(index == len(target_endpoints) - 1))
        left = right
    return answer


def wrong_tested_final_factor(target: tuple[int, ...]) -> int:
    """Deliberately wrong control that imposes divisibility at N."""
    target_endpoints = endpoints(target)
    left = 0
    answer = 1
    for index, right in enumerate(target_endpoints):
        terminal = index == len(target_endpoints) - 1
        if not terminal:
            answer *= interval_factor(left, right, terminal=False)
        else:
            # Treat the final endpoint as an internal retained cut: wrong.
            answer *= interval_factor(left, right, terminal=False)
        left = right
    return answer


def brute_interval_factor(left: int, right: int, terminal: bool) -> int:
    """Enumerate every refinement inside an interval, independent of the DP."""
    count = 0
    for refinement in compositions(right - left):
        endpoint = left
        admissible = True
        for index, part in enumerate(refinement):
            endpoint += part
            at_right = index == len(refinement) - 1
            if at_right:
                if not terminal and endpoint % part != 0:
                    admissible = False
            elif endpoint % part == 0:
                admissible = False
            if not admissible:
                break
        count += int(admissible)
    return count


def interval_dp_attack() -> int:
    boxes = 0
    for right in range(1, MAX_N + 1):
        for left in range(right):
            for terminal in (False, True):
                AUDIT.equal(interval_factor(left, right, terminal),
                            brute_interval_factor(left, right, terminal),
                            f"interval DP left={left} right={right} terminal={terminal}")
                boxes += 1
    return boxes


def claimed_witness(total: int, time: int) -> tuple[int, ...]:
    return (1, 2 + time) + (1,) * (total - 3 - time)


def verify_total(total: int) -> str:
    states = compositions(total)
    expected_state_count = 1 << (total - 1)
    AUDIT.equal(len(states), expected_state_count, f"carrier count N={total}")
    AUDIT.equal(len(set(states)), expected_state_count, f"carrier unique N={total}")

    global_fibres = Counter()
    tails = {}
    fixed = set()
    digest = sha256()

    for source in states:
        target = direct_merge_update(source)
        global_fibres[target] += 1
        digest.update((repr(source) + "->" + repr(target) + "\n").encode("ascii"))
        AUDIT.equal(sum(source), total, f"source mass N={total} source={source}")
        AUDIT.true(all(part > 0 for part in source),
                   f"source positivity N={total} source={source}")
        AUDIT.equal(sum(target), total, f"target mass N={total} source={source}")
        AUDIT.true(all(part > 0 for part in target),
                   f"target positivity N={total} source={source}")
        AUDIT.true(len(target) <= len(source),
                   f"merge monotonicity N={total} source={source}")
        if len(source) > 1:
            AUDIT.equal(target[0], source[0],
                        f"permanent first cut N={total} source={source}")
        AUDIT.equal(target == source, fixed_predicate(source),
                    f"fixed predicate N={total} source={source}")
        if target == source:
            fixed.add(source)
        tail, period = orbit_signature(source)
        tails[source] = tail
        AUDIT.equal(period, 1, f"fixed recurrence N={total} source={source}")
        if source != target:
            AUDIT.true(tail <= len(source) - 2,
                       f"first-cut tail bound N={total} source={source}")

    AUDIT.equal(len(fixed), fixed_count_recurrence(total),
                f"fixed recurrence count N={total}")
    maximum = max(tails.values())
    expected_maximum = max(0, total - 3)
    deepest = {source for source, tail in tails.items() if tail == maximum}
    AUDIT.equal(maximum, expected_maximum, f"sharp height N={total}")

    if total <= 3:
        exact_small = {
            1: {(1,)},
            2: {(1, 1), (2,)},
            3: {(1, 1, 1), (1, 2), (2, 1), (3,)},
        }[total]
        AUDIT.equal(set(states), exact_small, f"small carrier N={total}")
        AUDIT.equal(fixed, exact_small, f"small all fixed N={total}")
        AUDIT.equal(deepest, exact_small, f"small deepest set N={total}")
    else:
        witness = (1, 2) + (1,) * (total - 3)
        AUDIT.equal(deepest, {witness}, f"unique extremizer N={total}")
        state = witness
        for time in range(total - 2):
            AUDIT.equal(state, claimed_witness(total, time),
                        f"extremal orbit N={total} t={time}")
            if time < total - 3:
                state = direct_merge_update(state)
        AUDIT.equal(direct_merge_update(state), state,
                    f"extremal endpoint fixed N={total}")

    predicted_mass = 0
    predicted_image = set()
    maximum_fibre = 0
    for target in states:
        actual = global_fibres.get(target, 0)
        factored = factorized_fibre(target)
        AUDIT.equal(factored, actual,
                    f"every-target fibre N={total} target={target}")
        AUDIT.equal(factored > 0, target in global_fibres,
                    f"every-target image iff N={total} target={target}")
        predicted_mass += factored
        maximum_fibre = max(maximum_fibre, actual)
        if factored:
            predicted_image.add(target)
    AUDIT.equal(predicted_image, set(global_fibres), f"image equality N={total}")
    AUDIT.equal(predicted_mass, expected_state_count, f"factor mass N={total}")
    AUDIT.equal(sum(global_fibres.values()), expected_state_count,
                f"global inverse-candidate mass N={total}")
    AUDIT.equal(factorized_fibre((total,)), global_fibres[(total,)],
                f"one-part empty product N={total}")

    final_gap = 0
    if total >= 3:
        boundary_target = (1, total - 1)
        correct = factorized_fibre(boundary_target)
        wrong = wrong_tested_final_factor(boundary_target)
        AUDIT.true(boundary_target in global_fibres,
                   f"final endpoint target is image N={total}")
        AUDIT.true(correct > wrong,
                   f"untested final endpoint separates wrong DP N={total}")
        AUDIT.equal(direct_merge_update(boundary_target), boundary_target,
                    f"last part untested witness fixed N={total}")
        final_gap = correct - wrong

    return (
        f"N={total:02d} states={len(states)} fixed={len(fixed)} "
        f"image={len(global_fibres)} max_tail={maximum} deepest={len(deepest)} "
        f"fibre_max={maximum_fibre} final_test_gap={final_gap} "
        f"transition_sha256={digest.hexdigest()}"
    )


def main() -> None:
    print("P191_PROCESS_SEPARATED_HOSTILE_REVIEW_A")
    print("representation=recursive_composition_tuples_direct_merge_plus_backward_interval_dp")
    print("author_code_imported=false")
    print("scope=finite_falsification_not_proof_not_novelty")
    pin_inputs()
    print("PINNED_INPUTS=PASS count=6")
    interval_boxes = interval_dp_attack()
    print(f"INTERVAL_DP_BRUTE_BOXES={interval_boxes}")
    for total in range(1, MAX_N + 1):
        print("BOX " + verify_total(total))
    print("FORMAL_COUNTEREXAMPLES=0")
    print("CRITICAL=0")
    print("MAJOR=0")
    print("MINOR=0")
    print("HISTORICAL_FINDING=P191-A-MI-01_OEIS_HISTORY_DATE_IN_SOURCE_LEDGER")
    print("DELTA=P191-A-MI-01_ACCEPTED")
    print(f"TOTALS={MAX_N}")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("OWNER=OWNER_AMBER")
    print("LIFECYCLE=HOLD_EXTERNAL")
    print("VERDICT=PASS_DELTA_ACCEPTED")


if __name__ == "__main__":
    main()
