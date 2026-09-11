#!/usr/bin/env python3
"""Exact controls for the first lower-collision Hurwitz scheduler."""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from math import comb

Transposition = tuple[int, int]
Factorization = tuple[Transposition, ...]


def conjugate(t: Transposition, by: Transposition) -> Transposition:
    a, b = t
    c, d = by

    def swap(x: int) -> int:
        return d if x == c else c if x == d else x

    return tuple(sorted((swap(a), swap(b))))


def hurwitz(f: Factorization, i: int) -> Factorization:
    z = list(f)
    x, y = z[i], z[i + 1]
    z[i], z[i + 1] = y, conjugate(x, y)
    return tuple(z)


def hurwitz_inverse(f: Factorization, i: int) -> Factorization:
    z = list(f)
    x, y = z[i], z[i + 1]
    z[i], z[i + 1] = conjugate(y, x), x
    return tuple(z)


def lower(t: Transposition) -> int:
    return t[0]


def scheduler_index(f: Factorization) -> int | None:
    for i in range(len(f) - 1):
        if lower(f[i]) == lower(f[i + 1]):
            return i
    return None


def step(f: Factorization) -> Factorization:
    i = scheduler_index(f)
    return f if i is None else hurwitz(f, i)


def all_factorizations(n: int) -> set[Factorization]:
    seed = tuple((i, i + 1) for i in range(1, n))
    seen = {seed}
    queue = deque([seed])
    while queue:
        f = queue.popleft()
        for i in range(n - 2):
            g = hurwitz(f, i)
            if g not in seen:
                seen.add(g)
                queue.append(g)
    return seen


def trans_perm(n: int, t: Transposition) -> tuple[int, ...]:
    p = list(range(1, n + 1))
    a, b = t
    p[a - 1], p[b - 1] = p[b - 1], p[a - 1]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # Standard product p q: q acts first.
    return tuple(p[q[i] - 1] for i in range(len(p)))


def product_perm(n: int, f: Factorization) -> tuple[int, ...]:
    p = tuple(range(1, n + 1))
    for t in f:
        p = compose(p, trans_perm(n, t))
    return p


def is_parking(a: tuple[int, ...]) -> bool:
    return all(x <= i for i, x in enumerate(sorted(a), 1))


def orbit(f: Factorization) -> tuple[int, tuple[int, ...], Factorization]:
    history: list[int] = []
    x = f
    while (i := scheduler_index(x)) is not None:
        history.append(i + 1)
        x = hurwitz(x, i)
    return len(history), tuple(history), x


def atlas_indegree(y: Factorization) -> int:
    j = scheduler_index(y)
    stop = len(y) - 1 if j is None else j
    ans = int(j is None)
    for i in range(stop):
        a, b = y[i]
        nxt = y[i + 1]
        if b not in nxt:
            continue
        c = nxt[0] if nxt[1] == b else nxt[1]
        ans += c > a
    return ans


def main() -> None:
    assertions = 0
    transitions = 0
    records: list[str] = []
    for n in range(2, 9):
        states = all_factorizations(n)
        assert len(states) == n ** (n - 2)
        assertions += 1
        cycle = tuple(range(2, n + 1)) + (1,)
        lowers = set()
        depths = Counter()
        histories = Counter()
        images = Counter()
        terminal_count = 0
        max_depth_states = 0
        for f in states:
            assert product_perm(n, f) == cycle
            a = tuple(lower(t) for t in f)
            assert is_parking(a)
            lowers.add(a)
            depth, history, terminal = orbit(f)
            assert tuple(sorted(history)) == history
            assert len(set(history)) == len(history)
            assert scheduler_index(terminal) is None
            depths[depth] += 1
            histories[history] += 1
            terminal_count += depth == 0
            max_depth_states += depth == n - 2
            images[step(f)] += 1
            transitions += 1
            assertions += 6
        assert len(lowers) == len(states)
        assert terminal_count == (n - 1) ** (n - 2)
        assert max(depths) == n - 2
        assertions += 3

        # The history product law is recorded as a finite-range conjecture,
        # not promoted to an all-n theorem in the manuscript.
        for mask in range(1 << (n - 2)):
            hist = tuple(i + 1 for i in range(n - 2) if mask >> i & 1)
            assert histories[hist] == (n - 1) ** (n - 2 - len(hist))
            assertions += 1

        for y in states:
            assert images[y] == atlas_indegree(y)
            assertions += 1
        max_fibre = max(images.values())
        maximizers = [y for y in states if images[y] == max_fibre]
        canonical = tuple((i, i + 1) for i in range(1, n))
        assert max_fibre == n - 1
        assert maximizers == [canonical]
        assertions += 2

        expected_hist = {t: comb(n - 2, t) * (n - 1) ** (n - 2 - t)
                         for t in range(n - 1)}
        assert dict(depths) == expected_hist
        assertions += 1
        hist_text = ",".join(f"{t}:{depths[t]}" for t in sorted(depths))
        records.append(
            f"n={n} states={len(states)} fixed={terminal_count} "
            f"max_tail={max(depths)} deepest={max_depth_states} "
            f"max_fibre={max_fibre} depth_hist={hist_text}"
        )

    digest = sha256("\n".join(records).encode()).hexdigest()
    print("first-collision Hurwitz exact controls")
    for line in records:
        print(line)
    print(f"transitions={transitions}")
    print(f"assertions={assertions}")
    print(f"record_digest={digest}")
    print("theorem_status=history_law_verified_n_le_8_not_claimed_all_n")
    print("status=PASS")


if __name__ == "__main__":
    main()
