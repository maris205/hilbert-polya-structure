#!/usr/bin/env python3
"""Exact falsifiers for the focused WEX audit.

The program has three logically separate parts.

* literal permutation enumeration checks the functional graph in small ranks;
* a four-letter FIFO scheduler is cross-checked against literal preimages; and
* the scheduler searches *all* possible WEX targets of sources through rank 11.

The scheduler is not a heuristic.  For selected-position set P and
selected-value set A, read each coordinate as

    U = P only, D = A only, F = both, X = neither.

Complement values are opened at U/X and complement positions close them at
D/X.  The increasing (FIFO) matching minimizes maximum drop.  The inverse of
the target permutation gives the only precedence constraints on P/A events.

Enumeration is used only as a finite falsifier.  The accompanying audit gives
the all-size exchange proof behind the scheduler equivalence.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(1, n + 1))


def standardize(values) -> tuple[int, ...]:
    values = tuple(values)
    rank = {v: i + 1 for i, v in enumerate(sorted(values))}
    return tuple(rank[v] for v in values)


def wex(p: tuple[int, ...]) -> tuple[int, ...]:
    return standardize(v for i, v in enumerate(p, 1) if v >= i)


def maxdrop(p: tuple[int, ...]) -> int:
    return max((i - v for i, v in enumerate(p, 1)), default=0)


@lru_cache(None)
def tail(p: tuple[int, ...]) -> int:
    q = wex(p)
    return 0 if q == p else 1 + tail(q)


def fib(k: int) -> int:
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def source_from_schedule(
    sigma: tuple[int, ...], word: str
) -> tuple[int, ...]:
    """Reconstruct the FIFO source encoded by a U/D/F/X word."""
    P, Q, Aval, Bval = [], [], [], []
    for x, letter in enumerate(word, 1):
        A.check(letter in "UDFX", ("bad schedule letter", letter))
        (P if letter in "UF" else Q).append(x)
        (Aval if letter in "DF" else Bval).append(x)
    A.check(len(P) == len(Aval) == len(sigma), (P, Aval, sigma))
    A.check(len(Q) == len(Bval), (Q, Bval))
    p = [0] * len(word)
    for i, pos in enumerate(P):
        p[pos - 1] = Aval[sigma[i] - 1]
    for pos, val in zip(Q, Bval):
        p[pos - 1] = val
    A.check(sorted(p) == list(range(1, len(word) + 1)), p)
    return tuple(p)


def scheduler_path(
    sigma: tuple[int, ...], n: int, drop_bound: int
) -> str | None:
    """Return one exact schedule, or None if no bounded-drop source exists."""
    m = len(sigma)
    inverse = [0] * (m + 1)
    for i, value in enumerate(sigma, 1):
        inverse[value] = i

    # State: numbers of P/A events and FIFO opening coordinates.
    states: dict[tuple[int, int, tuple[int, ...]], str] = {(0, 0, ()): ""}
    for x in range(n):
        next_states: dict[tuple[int, int, tuple[int, ...]], str] = {}
        remaining = n - x - 1
        for (i, j, queue), path in states.items():
            transitions = []
            if i < m:  # U: selected position, complement value
                transitions.append(((i + 1, j, queue + (x + 1,)), "U"))
            if (
                j < m
                and queue
                and inverse[j + 1] <= i
                and x + 1 - queue[0] <= drop_bound
            ):  # D: complement position, selected value
                transitions.append(((i, j + 1, queue[1:]), "D"))
            if i < m and j < m and inverse[j + 1] <= i + 1:
                transitions.append(((i + 1, j + 1, queue), "F"))
            if queue and x + 1 - queue[0] <= drop_bound:
                transitions.append(((i, j, queue[1:] + (x + 1,)), "X"))

            for state, letter in transitions:
                ii, jj, _ = state
                if m - ii <= remaining and m - jj <= remaining:
                    next_states.setdefault(state, path + letter)
        states = next_states
        if not states:
            return None
    return states.get((m, m, ()))


def scheduler_min_drop(sigma: tuple[int, ...], n: int) -> int | None:
    for D in range(n):
        if scheduler_path(sigma, n, D) is not None:
            return D
    return None


def bounded_drop_permutations(n: int, D: int):
    """Generate exactly {p in S_n: maxdrop(p)<=D}, without filtering S_n."""
    p = [0] * n

    def visit(i: int, unused_mask: int):
        if i == n:
            yield tuple(p)
            return
        position = i + 1
        lower = max(1, position - D)
        for value in range(lower, n + 1):
            bit = 1 << (value - 1)
            if unused_mask & bit:
                p[i] = value
                yield from visit(i + 1, unused_mask ^ bit)

    yield from visit(0, (1 << n) - 1)


def audit_scheduler_against_literal() -> dict[str, int]:
    """Cold cross-check the scheduler on all targets through source rank 7."""
    target_checks = 0
    literal_sources = 0
    for n in range(1, 8):
        A.box()
        literal: dict[tuple[int, ...], int] = {}
        for p in permutations(range(1, n + 1)):
            literal_sources += 1
            q = wex(p)
            literal[q] = min(literal.get(q, n), maxdrop(p))
        for m in range(1, n + 1):
            for sigma in permutations(range(1, m + 1)):
                expected = literal.get(sigma)
                observed = scheduler_min_drop(sigma, n)
                A.check(observed == expected, ("scheduler", n, sigma, observed, expected))
                target_checks += 1
    return {"literal_sources": literal_sources, "target_checks": target_checks}


def audit_small_functional_graph() -> dict[str, object]:
    maxima, min_rank_plus_drop = [], {}
    repaired_slack_checks = 0
    total_states = 0
    for n in range(1, 10):
        A.box()
        maximum = 0
        for p in permutations(range(1, n + 1)):
            total_states += 1
            q = wex(p)
            t = tail(p)
            maximum = max(maximum, t)
            A.check(1 <= len(q) <= n, ("closure", p, q))
            A.check(q == identity(len(q)) or len(q) < n, ("strict rank", p, q))
            A.check(maxdrop(q) <= maxdrop(p), ("drop monotonicity", p, q))
            A.check(n >= fib(t + 2), ("size clock finite box", p, t))

            old = min_rank_plus_drop.get(t)
            value = n + maxdrop(p)
            min_rank_plus_drop[t] = value if old is None else min(old, value)

            # The repaired quantity suggested by the scheduler.  It survives
            # this box but is deliberately *not* promoted to an all-size proof.
            tq = tail(q)
            if tq:
                K = maxdrop(p) + (n - len(q)) - maxdrop(q)
                A.check(K >= fib(tq + 2), ("repaired slack", p, q, K, tq))
                repaired_slack_checks += 1
        maxima.append(maximum)
    A.check(maxima == [0, 1, 2, 2, 3, 3, 3, 4, 4], maxima)
    return {
        "states": total_states,
        "max_tail": maxima,
        "min_rank_plus_drop": dict(sorted(min_rank_plus_drop.items())),
        "repaired_slack_checks": repaired_slack_checks,
    }


def audit_exact_compression_boundary() -> dict[str, object]:
    """Exhaust the compression claim through n=10 and find its n=11 failure."""
    # Minimum rank D for a permutation with tail t, obtained independently in
    # the literal rank boxes D<=8.  A source of drop below threshold[t] would
    # violate tail(W(source))<=M(drop(source)).
    threshold = {1: 2, 2: 3, 3: 5, 4: 8, 5: 13}

    # Handle t=1 separately.  Exactly enumerate every source of drop <=1.
    bounded_sources = 0
    for n in range(1, 12):
        A.box()
        for p in bounded_drop_permutations(n, 1):
            bounded_sources += 1
            A.check(maxdrop(p) <= 1, p)
            A.check(wex(p) == identity(len(wex(p))), ("D=1 target", p, wex(p)))

    # If a nonidentity q has tail t, then d(q)>=t (strict-drop lemma in the
    # audit).  Hence every nonidentity target of a source of rank <=11 has
    # rank <=9.  This makes the following target scan complete, not sampled.
    schedule_decisions = 0
    target_profile = Counter()
    failures_n11 = []
    for m in range(1, 10):
        A.box()
        for sigma in permutations(range(1, m + 1)):
            t = tail(sigma)
            d = maxdrop(sigma)
            A.check(d >= t, ("strict-drop orbit consequence", sigma, d, t))
            if t < 2 or m + d > 11:
                continue
            target_profile[(m, t)] += 1
            limit = threshold[t] - 1

            # Every possible source rank from the exact image lower bound up
            # through 10 is checked by scheduler nonexistence.
            for n in range(m + d, 11):
                path = scheduler_path(sigma, n, limit)
                schedule_decisions += 1
                A.check(path is None, ("unexpected <=10 counter", sigma, n, limit, path))

            # Rank 11 is searched as well; exactly one target breaches C5.
            path = scheduler_path(sigma, 11, limit)
            schedule_decisions += 1
            if path is not None:
                failures_n11.append((sigma, t, d, limit, path))

    expected_failure = ((5, 4, 3, 1, 2), 3, 3, 4, "UUUFXXXFDDD")
    A.check(failures_n11 == [expected_failure], failures_n11)

    sigma, t, d, limit, word = failures_n11[0]
    counterexample = source_from_schedule(sigma, word)
    A.check(len(counterexample) == 11, counterexample)
    A.check(maxdrop(counterexample) == limit == 4, counterexample)
    A.check(wex(counterexample) == sigma, (counterexample, wex(counterexample), sigma))
    A.check(tail(sigma) == 3, sigma)
    A.check(tail(counterexample) == 4, counterexample)

    # Literal M(4)=2, so the displayed source is a direct C5 falsifier.
    M4 = max(tail(p) for p in permutations(range(1, 5)))
    A.check(M4 == 2, M4)
    A.check(tail(wex(counterexample)) > M4, (counterexample, M4))

    return {
        "bounded_D1_sources": bounded_sources,
        "schedule_decisions": schedule_decisions,
        "target_profile": dict(sorted(target_profile.items())),
        "unique_n11_target": sigma,
        "schedule": word,
        "counterexample": counterexample,
        "counterexample_drop": maxdrop(counterexample),
        "target_tail": tail(sigma),
        "M4": M4,
    }


def audit_witnesses() -> dict[str, object]:
    witnesses = [(1,), (2, 1)]
    while len(witnesses) < 6:
        old = witnesses[-1]
        h = maxdrop(old)
        witnesses.append(tuple(v + h for v in old) + tuple(range(1, h + 1)))
    A.check([len(p) for p in witnesses] == [1, 2, 3, 5, 8, 13])
    A.check([maxdrop(p) for p in witnesses] == [0, 1, 2, 3, 5, 8])
    A.check([tail(p) for p in witnesses] == [0, 1, 2, 3, 4, 5])
    return {"witnesses": witnesses}


def audit_naive_tradeoff_falsifiers() -> dict[str, object]:
    """Falsify h+d(p)>=|W(p)|+d(W(p)), even for target tail two."""
    examples = [
        (1, 4, 3, 2),
        (1, 6, 5, 4, 2, 3),
    ]
    rows = []
    expected_targets = [(1, 3, 2), (1, 4, 3, 2)]
    expected_target_tails = [1, 2]
    for p, expected_q, expected_tail in zip(
        examples, expected_targets, expected_target_tails
    ):
        q = wex(p)
        h = len(p) - len(q)
        left = h + maxdrop(p)
        right = len(q) + maxdrop(q)
        A.check(q == expected_q, (p, q, expected_q))
        A.check(tail(q) == expected_tail, (q, tail(q), expected_tail))
        A.check(left < right, ("naive tradeoff unexpectedly holds", p, q, left, right))
        rows.append((p, q, h, maxdrop(p), len(q), maxdrop(q), left, right))
    # Removing direct-sum identity components still does not repair the claim.
    # This target is sum-indecomposable and has tail two.
    p = (7, 2, 5, 4, 1, 6, 3)
    q = wex(p)
    h = len(p) - len(q)
    left = h + maxdrop(p)
    right = len(q) + maxdrop(q)
    proper_sum_cuts = [k for k in range(1, len(q)) if max(q[:k]) == k]
    A.check(q == (5, 1, 3, 2, 4), (p, q))
    A.check(tail(q) == 2, (q, tail(q)))
    A.check(proper_sum_cuts == [], (q, proper_sum_cuts))
    A.check((left, right) == (6, 7), (p, q, left, right))
    return {
        "rows": rows,
        "indecomposable_row": (
            p,
            q,
            h,
            maxdrop(p),
            len(q),
            maxdrop(q),
            left,
            right,
        ),
    }


def main() -> None:
    literal = audit_scheduler_against_literal()
    graph = audit_small_functional_graph()
    boundary = audit_exact_compression_boundary()
    tradeoff = audit_naive_tradeoff_falsifiers()
    witnesses = audit_witnesses()

    print("WEX_FOCUSED_EXACT_AUDIT")
    print("external_status=HOLD_EXTERNAL")
    print(f"scheduler_literal_sources={literal['literal_sources']}")
    print(f"scheduler_target_checks={literal['target_checks']}")
    print(f"functional_graph_states={graph['states']}")
    print(f"max_tail_ranks_1_to_9={graph['max_tail']}")
    print(f"min_rank_plus_drop_by_tail={graph['min_rank_plus_drop']}")
    print(f"repaired_slack_finite_checks={graph['repaired_slack_checks']}")
    print(f"bounded_D1_sources_through_11={boundary['bounded_D1_sources']}")
    print(f"exact_scheduler_decisions={boundary['schedule_decisions']}")
    print(f"dangerous_target_profile={boundary['target_profile']}")
    print(f"unique_n11_target={boundary['unique_n11_target']}")
    print(f"unique_n11_schedule={boundary['schedule']}")
    print(f"counterexample={boundary['counterexample']}")
    print(f"counterexample_drop={boundary['counterexample_drop']}")
    print(f"target_tail={boundary['target_tail']}")
    print(f"literal_M4={boundary['M4']}")
    print(f"naive_tradeoff_falsifiers={tradeoff['rows']}")
    print(f"indecomposable_tradeoff_falsifier={tradeoff['indecomposable_row']}")
    print(f"fibonacci_witnesses={witnesses['witnesses']}")
    print("original_drop_compression=FALSE_AT_RANK_11")
    print("size_only_fibonacci_clock=UNFALSIFIED_NOT_PROVED")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("status=PASS_EXPECTED_FALSIFICATION")


if __name__ == "__main__":
    main()
