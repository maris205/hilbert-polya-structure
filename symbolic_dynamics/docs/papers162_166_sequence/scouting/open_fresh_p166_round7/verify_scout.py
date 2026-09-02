#!/usr/bin/env python3
"""Deterministic exact probes for P166 open scout, round 7.

Six unrelated literal carriers are implemented directly.  The script is a
bounded falsifier and signature recorder; it does not infer an all-parameter
theorem from the enumerated boxes.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from math import comb


ASSERTIONS = 0


def check(statement: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(message)


def functional_signature(states, successor, tag: str):
    nxt = {state: successor(state) for state in states}
    state_set = set(states)
    check(set(nxt) == state_set, f"{tag}: missing domain states")
    for target in nxt.values():
        check(target in state_set, f"{tag}: carrier not closed")

    indegree = Counter(nxt.values())
    tails = Counter()
    periods = Counter()
    recurrent = set()
    for start in states:
        first_seen = {}
        x = start
        step = 0
        while x not in first_seen:
            first_seen[x] = step
            step += 1
            x = nxt[x]
        tail = first_seen[x]
        period = step - tail
        tails[tail] += 1
        periods[period] += 1
        y = x
        for _ in range(period):
            recurrent.add(y)
            y = nxt[y]

    digest = sha256()
    for state in states:
        digest.update(f"{tag}|{state}->{nxt[state]}\n".encode())
    return {
        "states": len(states),
        "image": len(indegree),
        "fixed": sum(nxt[x] == x for x in states),
        "recurrent": len(recurrent),
        "tail": max(tails),
        "period": max(periods),
        "periods": sorted(periods),
        "max_fibre": max(indegree.values()),
        "digest": digest.hexdigest(),
        "next": nxt,
        "indegree": indegree,
        "recurrent_set": recurrent,
    }


def fmt(name: str, box: str, sig) -> str:
    return (
        f"{name} box={box} states={sig['states']} image={sig['image']} "
        f"fixed={sig['fixed']} recurrent={sig['recurrent']} "
        f"max_tail={sig['tail']} max_period={sig['period']} "
        f"periods={sig['periods']} max_fibre={sig['max_fibre']} "
        f"sha256={sig['digest']}"
    )


# ---------------------------------------------------------------------------
# 1. DCF: simultaneous double conjugation on G x G.


Perm = tuple[int, ...]


def compose(a: Perm, b: Perm) -> Perm:
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a: Perm) -> Perm:
    out = [0] * len(a)
    for i, j in enumerate(a):
        out[j] = i
    return tuple(out)


def generated_group(generators: list[Perm]) -> list[Perm]:
    identity = tuple(range(len(generators[0])))
    group = {identity}
    queue = [identity]
    while queue:
        a = queue.pop()
        for b in generators:
            c = compose(a, b)
            if c not in group:
                group.add(c)
                queue.append(c)
    return sorted(group)


def cycle_perm(n: int) -> Perm:
    return tuple((i + 1) % n for i in range(n))


def reflection_perm(n: int) -> Perm:
    return tuple((-i) % n for i in range(n))


def parity(perm: Perm) -> int:
    return sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))) % 2


def audit_dcf() -> list[str]:
    groups = {
        "C3": generated_group([cycle_perm(3)]),
        "S3": list(permutations(range(3))),
        "D4": generated_group([cycle_perm(4), reflection_perm(4)]),
        "A4": [p for p in permutations(range(4)) if parity(p) == 0],
        "S4": list(permutations(range(4))),
    }
    lines = []
    for name, group in groups.items():
        index = {g: i for i, g in enumerate(group)}
        states = [(i, j) for i in range(len(group)) for j in range(len(group))]

        def conjugate(x: Perm, y: Perm) -> Perm:
            return compose(compose(x, y), inverse(x))

        def successor(state):
            i, j = state
            x, y = group[i], group[j]
            return index[conjugate(x, y)], index[conjugate(y, x)]

        sig = functional_signature(states, successor, f"DCF:{name}")
        if name == "C3":
            # In an abelian group DCF is exactly the coordinate swap.
            for i, j in states:
                check(successor((i, j)) == (j, i), "DCF abelian reduction failed")
        lines.append(fmt("DCF", name, sig))
    return lines


# ---------------------------------------------------------------------------
# 2. RPF: nonlinear pair feedback over Z/mZ.


def audit_rpf() -> list[str]:
    lines = []
    for modulus in (2, 3, 4, 5, 7, 8, 9, 11, 13):
        states = [(x, y) for x in range(modulus) for y in range(modulus)]

        def successor(state):
            x, y = state
            xy = x * y
            return (x + xy) % modulus, (y + xy) % modulus

        sig = functional_signature(states, successor, f"RPF:m{modulus}")
        actual_fibres = Counter(successor(state) for state in states)
        for x, y in states:
            u, v = successor((x, y))
            check((u - v) % modulus == (x - y) % modulus, "RPF difference invariant failed")
        for u, v in states:
            d = (u - v) % modulus
            roots = sum(
                (x * x + (1 - d) * x - u) % modulus == 0
                for x in range(modulus)
            )
            check(actual_fibres[(u, v)] == roots, "RPF quadratic target fibre failed")
        lines.append(fmt("RPF", f"Z/{modulus}Z", sig))
    return lines


# ---------------------------------------------------------------------------
# 3. IHI: Hadamard product with inverse in a unitriangular incidence algebra.


def interval_pairs(n: int):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def xor_matrix_product(a, b, n: int):
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    out[i][j] ^= b[k][j]
    return out


def ihi_successor(mask: int, n: int) -> int:
    pairs = interval_pairs(n)
    strict = [[0] * n for _ in range(n)]
    for bit, (i, j) in enumerate(pairs):
        strict[i][j] = (mask >> bit) & 1
    inverse_strict = [[0] * n for _ in range(n)]
    power = [row[:] for row in strict]
    for _ in range(1, n):
        for i in range(n):
            for j in range(n):
                inverse_strict[i][j] ^= power[i][j]
        power = xor_matrix_product(power, strict, n)
    out = 0
    for bit, (i, j) in enumerate(pairs):
        if strict[i][j] and inverse_strict[i][j]:
            out |= 1 << bit
    return out


def audit_ihi() -> list[str]:
    lines = []
    for n in range(1, 7):
        states = list(range(1 << (n * (n - 1) // 2)))
        successor = lambda mask, n=n: ihi_successor(mask, n)
        sig = functional_signature(states, successor, f"IHI:n{n}")
        check(sig["period"] == 1, "IHI unexpectedly has a nontrivial cycle")
        check(sig["tail"] == max(0, n - 2), "IHI small-box tail staircase failed")
        for mask in states:
            check(successor(mask) & ~mask == 0, "IHI created a new interval coefficient")
        lines.append(fmt("IHI", f"chain_{n}/F2", sig))
    return lines


# ---------------------------------------------------------------------------
# 4. AST: an asymmetric sandwich word on the full transformation semigroup.


def audit_ast() -> list[str]:
    lines = []
    for n in range(1, 4):
        transformations = list(product(range(n), repeat=n))
        index = {f: i for i, f in enumerate(transformations)}
        states = [(i, j) for i in range(len(transformations)) for j in range(len(transformations))]

        def successor(state):
            i, j = state
            a, b = transformations[i], transformations[j]
            ab = compose(a, b)
            aba = compose(ab, a)
            return index[aba], index[ab]

        sig = functional_signature(states, successor, f"AST:n{n}")
        for i, j in states:
            a, b = transformations[i], transformations[j]
            u, v = successor((i, j))
            check(len(set(transformations[u])) <= min(len(set(a)), len(set(b))), "AST aba rank bound failed")
            check(len(set(transformations[v])) <= min(len(set(a)), len(set(b))), "AST ab rank bound failed")
        lines.append(fmt("AST", f"T_{n}xT_{n}", sig))
    return lines


# ---------------------------------------------------------------------------
# 5. LHF: flip the leftmost horizontal pair in a 2xn domino tiling.


def compositions_12(total: int):
    if total == 0:
        yield ()
    if total >= 1:
        for rest in compositions_12(total - 1):
            yield (1,) + rest
    if total >= 2:
        for rest in compositions_12(total - 2):
            yield (2,) + rest


def lhf_successor(word: tuple[int, ...]) -> tuple[int, ...]:
    for i, token in enumerate(word):
        if token == 2:
            return word[:i] + (1, 1) + word[i + 1 :]
    return word


def lhf_iterate(word: tuple[int, ...], time: int) -> tuple[int, ...]:
    out = word
    for _ in range(time):
        out = lhf_successor(out)
    return out


def lhf_theoretical_fibre(target: tuple[int, ...], width: int, time: int) -> int:
    if time == 0:
        return 1
    if 2 not in target:
        return sum(comb(width - horizontal, horizontal) for horizontal in range(min(time, width // 2) + 1))
    leading_vertical = target.index(2)
    if leading_vertical < 2 * time:
        return 0
    return comb(leading_vertical - time, time)


def audit_lhf() -> list[str]:
    lines = []
    for width in range(0, 17):
        states = list(compositions_12(width))
        sig = functional_signature(states, lhf_successor, f"LHF:w{width}")
        check(sig["period"] == 1, "LHF has a nonfixed recurrent tiling")
        check(sig["fixed"] == 1, "LHF must have the all-vertical unique fixed tiling")
        check(sig["tail"] == width // 2, "LHF sharp height failed")
        for word in states:
            check(sum(lhf_successor(word)) == width, "LHF changed board width")
            steps = 0
            current = word
            while lhf_successor(current) != current:
                current = lhf_successor(current)
                steps += 1
            check(steps == word.count(2), "LHF point clock is not horizontal-pair count")
        for time in range(width // 2 + 2):
            actual = Counter(lhf_iterate(source, time) for source in states)
            for target in states:
                theory = lhf_theoretical_fibre(target, width, time)
                check(actual[target] == theory, "LHF every-target binomial fibre failed")
        lines.append(fmt("LHF", f"2x{width}", sig))
    return lines


# ---------------------------------------------------------------------------
# 6. MGC: ordered-matroid greedy circuit deletion.


def gf2_rank(vectors: list[int]) -> int:
    pivots = {}
    for vector in vectors:
        x = vector
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def rank_subset(columns: tuple[int, ...], mask: int) -> int:
    return gf2_rank([columns[i] for i in range(len(columns)) if (mask >> i) & 1])


def matroid_circuits(columns: tuple[int, ...]) -> list[int]:
    n = len(columns)
    circuits = []
    for mask in range(1, 1 << n):
        size = mask.bit_count()
        if rank_subset(columns, mask) == size:
            continue
        minimal = True
        for i in range(n):
            if (mask >> i) & 1 and rank_subset(columns, mask ^ (1 << i)) < size - 1:
                minimal = False
                break
        if minimal:
            circuits.append(mask)
    circuits.sort(key=lambda mask: tuple(i for i in range(n) if (mask >> i) & 1))
    return circuits


def audit_mgc() -> list[str]:
    k4_edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    k4_columns = tuple(((1 << i) if i < 3 else 0) ^ ((1 << j) if j < 3 else 0) for i, j in k4_edges)
    c4d_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    c4d_columns = tuple(((1 << i) if i < 3 else 0) ^ ((1 << j) if j < 3 else 0) for i, j in c4d_edges)
    boxes = {
        "triangle": (1, 2, 3),
        "C4_plus_diagonal": c4d_columns,
        "K4_graphic": k4_columns,
        "Fano": tuple(range(1, 8)),
    }
    lines = []
    for name, columns in boxes.items():
        n = len(columns)
        circuits = matroid_circuits(columns)
        states = list(range(1 << n))

        def successor(mask: int) -> int:
            for circuit in circuits:
                if circuit & mask == circuit:
                    largest = circuit.bit_length() - 1
                    return mask ^ (1 << largest)
            return mask

        sig = functional_signature(states, successor, f"MGC:{name}")
        ambient_rank = rank_subset(columns, (1 << n) - 1)
        check(sig["tail"] == n - ambient_rank, "MGC sharp nullity height failed")
        for mask in states:
            target = successor(mask)
            check(rank_subset(columns, target) == rank_subset(columns, mask), "MGC deletion changed rank")
            independent = rank_subset(columns, mask) == mask.bit_count()
            check((target == mask) == independent, "MGC recurrent/fixed criterion failed")
            x = mask
            steps = 0
            while successor(x) != x:
                x = successor(x)
                steps += 1
            check(steps == mask.bit_count() - rank_subset(columns, mask), "MGC point nullity clock failed")
        lines.append(fmt("MGC", name, sig))
    return lines


def main() -> None:
    print("P166_OPEN_FRESH_ROUND7_EXACT_SCOUT")
    print("CANDIDATES 6")
    for line in audit_dcf():
        print(line)
    for line in audit_rpf():
        print(line)
    for line in audit_ihi():
        print(line)
    for line in audit_ast():
        print(line)
    for line in audit_lhf():
        print(line)
    for line in audit_mgc():
        print(line)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")
    print("VERDICT KILL_ALL")
    print("EXTERNAL HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
