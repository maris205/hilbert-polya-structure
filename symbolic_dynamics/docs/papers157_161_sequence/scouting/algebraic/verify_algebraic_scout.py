#!/usr/bin/env python3
"""Deterministic exact breadth controls for the P157--P161 algebraic scout.

The program deliberately mixes three retained candidates with thirteen
negative controls.  It uses only exact integer/finite-field arithmetic and the
Python standard library.  Finite enumeration is counterexample pressure, not
an all-parameter proof or an owner/novelty certificate.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
from math import gcd


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
LINES: list[str] = []


def emit(line: str) -> None:
    LINES.append(line)


def iterate(step, state, t: int):
    for _ in range(t):
        state = step(state)
    return state


@dataclass
class Summary:
    states: tuple
    successor: dict
    tail_cycle: dict
    fixed: int
    periodic: int
    max_tail: int
    cycle_hist: Counter
    indegree_hist: Counter
    edge_sha16: str


def summarize(name: str, params: str, states, step) -> Summary:
    states = tuple(states)
    state_set = set(states)
    A.check(len(state_set) == len(states), (name, "duplicate states"))
    successor = {state: step(state) for state in states}
    for state, target in successor.items():
        A.check(target in state_set, (name, "closure", state, target))

    indegree = Counter(successor.values())
    tail_cycle: dict[object, tuple[int, int]] = {}
    cycle_hist: Counter[int] = Counter()
    for start in states:
        if start in tail_cycle:
            continue
        path: list[object] = []
        local: dict[object, int] = {}
        current = start
        while current not in local and current not in tail_cycle:
            local[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in local:
            cut = local[current]
            cycle = path[cut:]
            length = len(cycle)
            cycle_hist[length] += 1
            for state in cycle:
                tail_cycle[state] = (0, length)
            prefix = path[:cut]
        else:
            prefix = path
        for state in reversed(prefix):
            next_tail, length = tail_cycle[successor[state]]
            tail_cycle[state] = (next_tail + 1, length)

    A.check(len(tail_cycle) == len(states), (name, "profile coverage"))
    fixed = sum(successor[state] == state for state in states)
    periodic = sum(tail_cycle[state][0] == 0 for state in states)
    max_tail = max((tail_cycle[state][0] for state in states), default=0)
    indegree_hist = Counter(indegree.get(state, 0) for state in states)
    digest_payload = "\n".join(
        f"{state!r}->{successor[state]!r}" for state in states
    ).encode("utf-8")
    edge_sha16 = sha256(digest_payload).hexdigest()[:16]
    cycle_text = ",".join(f"{k}:{v}" for k, v in sorted(cycle_hist.items()))
    indegree_text = ",".join(f"{k}:{v}" for k, v in sorted(indegree_hist.items()))
    emit(
        f"SIG {name} {params} states={len(states)} fixed={fixed} "
        f"periodic={periodic} components={sum(cycle_hist.values())} "
        f"max_tail={max_tail} cycles={{{cycle_text}}} "
        f"indegrees={{{indegree_text}}} edge_sha16={edge_sha16}"
    )
    A.box()
    return Summary(
        states,
        successor,
        tail_cycle,
        fixed,
        periodic,
        max_tail,
        cycle_hist,
        indegree_hist,
        edge_sha16,
    )


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("valuation(0) is not used")
    answer = 0
    while n % p == 0:
        answer += 1
        n //= p
    return answer


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def phi(n: int) -> int:
    result = n
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            result -= result // d
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        result -= result // x
    return result


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def multiplicative_order(a: int, n: int) -> int:
    if n == 1:
        return 1
    A.check(gcd(a, n) == 1, ("order", a, n))
    x = 1
    for r in range(1, phi(n) + 1):
        x = x * a % n
        if x == 1:
            return r
    raise AssertionError(("order missing", a, n))


# A01: Frobenius-difference dynamics in a normal basis.
def run_fad(q: int, m: int) -> None:
    states = tuple(product(range(q), repeat=m))

    def step(v):
        return tuple((v[(i - 1) % m] - v[i]) % q for i in range(m))

    summary = summarize("A01_FAD", f"q={q},m={m}", states, step)
    p_part = q ** valuation(m, q)
    A.check(summary.periodic == q ** (m - p_part))
    A.check(summary.max_tail == p_part)
    for t in range(p_part + 1):
        observed = sum(tail <= t for tail, _ in summary.tail_cycle.values())
        predicted = q ** (m - p_part + min(t, p_part))
        A.check(observed == predicted, ("FAD census", q, m, t, observed, predicted))


# A02: derivative-gcd multiplicity descent.
def run_dgd(p: int, blocks: int, factors: int) -> None:
    cap = p * (blocks + 1) - 1
    states = tuple(product(range(cap + 1), repeat=factors))

    def step(e):
        return tuple(x if x % p == 0 else x - 1 for x in e)

    summary = summarize(
        "A02_DGD", f"p={p},L={blocks},s={factors},M={cap}", states, step
    )
    A.check(summary.fixed == (blocks + 1) ** factors)
    A.check(summary.periodic == summary.fixed)
    A.check(summary.max_tail == (p - 1 if factors else 0))
    for t in range(p):
        u = min(t, p - 1)
        observed_cdf = sum(tail <= t for tail, _ in summary.tail_cycle.values())
        predicted_cdf = ((u + 1) * (blocks + 1)) ** factors
        A.check(observed_cdf == predicted_cdf)
        predecessors = Counter(iterate(step, state, t) for state in states)
        for target in states:
            expected = 1
            for y in target:
                residue = y % p
                if residue == 0:
                    expected *= u + 1
                elif residue <= p - 1 - u:
                    expected *= 1
                else:
                    expected = 0
                    break
            A.check(predecessors.get(target, 0) == expected,
                    ("DGD fibre", p, blocks, factors, t, target))


# A03: the gcd--lcm comparator on ordered divisor pairs.
def run_dcs(exponents: tuple[int, ...]) -> None:
    divisors_by_valuation = tuple(product(*(range(a + 1) for a in exponents)))
    width = len(exponents)
    states = tuple(left + right
                   for left in divisors_by_valuation
                   for right in divisors_by_valuation)

    def step(state):
        left, right = state[:width], state[width:]
        return (tuple(min(x, y) for x, y in zip(left, right))
                + tuple(max(x, y) for x, y in zip(left, right)))

    summary = summarize(
        "A03_DCS", f"a={','.join(map(str, exponents))}", states, step
    )
    predicted_fixed = 1
    for a in exponents:
        predicted_fixed *= (a + 1) * (a + 2) // 2
    A.check(summary.fixed == predicted_fixed)
    A.check(summary.periodic == predicted_fixed)
    A.check(summary.max_tail == 1)
    predecessors = Counter(step(state) for state in states)
    for target in states:
        left, right = target[:width], target[width:]
        if any(x > y for x, y in zip(left, right)):
            expected = 0
        else:
            expected = 2 ** sum(x < y for x, y in zip(left, right))
        A.check(predecessors.get(target, 0) == expected,
                ("DCS fibre", exponents, target, expected))


# A04: finite-field norm as a self-map, represented by cyclic exponents.
def run_npd(q: int, m: int) -> None:
    ambient_order = q ** m - 1
    scale = ambient_order // (q - 1)
    zero = -1
    states = tuple([zero] + list(range(ambient_order)))

    def step(state):
        if state == zero:
            return zero
        return (scale * (state % (q - 1))) % ambient_order

    summary = summarize("A04_NPD", f"q={q},m={m}", states, step)
    for t in range(1, 6):
        fixed = sum(iterate(step, state, t) == state for state in states)
        A.check(fixed == 1 + gcd(m ** t - 1, q - 1))
        predecessors = Counter(iterate(step, state, t) for state in states)
        g = gcd(m ** (t - 1), q - 1)
        for target in states:
            if target == zero:
                expected = 1
            elif target % scale:
                expected = 0
            else:
                base_exponent = target // scale
                expected = scale * g if base_exponent % g == 0 else 0
            A.check(predecessors.get(target, 0) == expected,
                    ("NPD fibre", q, m, t, target))
    A.check(summary.max_tail <= 1 + max(valuation(q - 1, ell)
                                       for ell in divisors(m) if ell > 1)
            if m > 1 else True)


# A05: coefficient substitution on a cyclic group algebra.
def substitution_step(coeffs, q: int, m: int, k: int):
    out = [0] * m
    for j, coefficient in enumerate(coeffs):
        out[(k * j) % m] = (out[(k * j) % m] + coefficient) % q
    return tuple(out)


def parallel_part_and_height(m: int, k: int) -> tuple[int, int]:
    parallel = 1
    height = 0
    x = m
    prime = 2
    while prime * prime <= x:
        if x % prime == 0:
            exponent = 0
            while x % prime == 0:
                exponent += 1
                x //= prime
            if k % prime == 0:
                k_exponent = valuation(k, prime)
                parallel *= prime ** exponent
                height = max(height, ceil_div(exponent, k_exponent))
        prime += 1
    if x > 1 and k % x == 0:
        parallel *= x
        height = max(height, ceil_div(1, valuation(k, x)))
    return parallel, height


def multiplication_cycle_count(n: int, multiplier: int) -> int:
    if n == 1:
        return 1
    seen = set()
    cycles = 0
    for x in range(n):
        if x in seen:
            continue
        cycles += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = multiplier * y % n
    return cycles


def run_sce(q: int, m: int, k: int) -> None:
    states = tuple(product(range(q), repeat=m))
    step = lambda coeffs: substitution_step(coeffs, q, m, k)
    summary = summarize("A05_SCE", f"q={q},m={m},k={k}", states, step)
    parallel, height = parallel_part_and_height(m, k)
    perpendicular = m // parallel
    A.check(summary.periodic == q ** perpendicular)
    A.check(summary.max_tail == height)
    for t in range(height + 1):
        power = k ** t
        g = gcd(power, m)
        predecessors = Counter(iterate(step, state, t) for state in states)
        fibre_size = q ** (m - m // g)
        for target in states:
            in_image = all(coefficient == 0 or index % g == 0
                           for index, coefficient in enumerate(target))
            A.check(predecessors.get(target, 0) ==
                    (fibre_size if in_image else 0),
                    ("SCE fibre", q, m, k, t, target))
        observed_cdf = sum(tail <= t for tail, _ in summary.tail_cycle.values())
        predicted_cdf = q ** (m - m // g + perpendicular)
        A.check(observed_cdf == predicted_cdf,
                ("SCE census", q, m, k, t, observed_cdf, predicted_cdf))
    for r in range(1, 7):
        actual_fixed = sum(iterate(step, state, r) == state for state in states)
        direct_cycles = multiplication_cycle_count(perpendicular,
                                                   pow(k, r, perpendicular)
                                                   if perpendicular > 1 else 0)
        divisor_cycles = sum(
            phi(d) // multiplicative_order(pow(k, r), d)
            for d in divisors(perpendicular)
        )
        A.check(direct_cycles == divisor_cycles)
        A.check(actual_fixed == q ** direct_cycles,
                ("SCE fixed", q, m, k, r, actual_fixed, direct_cycles))


# A06: Cayley-Newton iteration on principal units.
def run_cni(p: int, exponent: int) -> None:
    modulus = p ** exponent
    states = tuple(x for x in range(modulus) if x % p == 1)
    inv2 = pow(2, -1, modulus)

    def step(x):
        return ((x + pow(x, -1, modulus)) * inv2) % modulus

    def cayley(x):
        return ((x - 1) * pow(x + 1, -1, modulus)) % modulus

    summary = summarize("A06_CNI", f"p={p},a={exponent}", states, step)
    A.check(summary.fixed == 1 and summary.periodic == 1)
    for state in states:
        y = cayley(state)
        A.check(y % p == 0)
        A.check(cayley(step(state)) == y * y % modulus)
        if y == 0:
            predicted_depth = 0
        else:
            value = valuation(y, p)
            predicted_depth = 0
            while (2 ** predicted_depth) * value < exponent:
                predicted_depth += 1
        A.check(summary.tail_cycle[state][0] == predicted_depth)


# A07: shift-boundary extraction on root subsets.
def run_sbe(length: int) -> None:
    states = tuple(product((0, 1), repeat=length))

    def step(bits):
        return tuple(bits[i] & (1 - bits[(i + 1) % length])
                     for i in range(length))

    summary = summarize("A07_SBE", f"cycle={length}", states, step)
    for state in states:
        A.check(step(step(state)) == step(state))
    A.check(summary.max_tail == 1)


# A08: the squaring map on a symmetric group.
def run_psg(n: int) -> None:
    states = tuple(permutations(range(n)))

    def step(sigma):
        return tuple(sigma[sigma[i]] for i in range(n))

    def cycle_lengths(sigma):
        unseen = set(range(n))
        lengths = []
        while unseen:
            start = min(unseen)
            cursor = start
            length = 0
            while cursor in unseen:
                unseen.remove(cursor)
                cursor = sigma[cursor]
                length += 1
            lengths.append(length)
        return lengths

    summary = summarize("A08_PSG", f"n={n}", states, step)
    A.check(summary.fixed == 1)
    for sigma in states:
        lengths = cycle_lengths(sigma)
        predicted_tail = max((valuation(length, 2) for length in lengths), default=0)
        A.check(summary.tail_cycle[sigma][0] == predicted_tail,
                ("PSG tail", n, sigma, lengths))
        A.check((summary.tail_cycle[sigma][0] == 0) == all(length % 2 for length in lengths))


# A09: formal-derivative dynamics on bounded polynomial coefficient vectors.
def run_fpd(p: int, dimension: int) -> None:
    states = tuple(product(range(p), repeat=dimension))

    def step(coeffs):
        out = [0] * dimension
        for degree in range(1, dimension):
            out[degree - 1] = degree * coeffs[degree] % p
        return tuple(out)

    summary = summarize("A09_FPD", f"p={p},d={dimension}", states, step)
    A.check(summary.fixed == 1 and summary.periodic == 1)
    A.check(summary.max_tail == min(p, dimension))


# A10: field trace used as a self-map, again in a normalized normal basis.
def run_tsd(q: int, m: int) -> None:
    states = tuple(product(range(q), repeat=m))

    def step(v):
        trace = sum(v) % q
        return (trace,) * m

    summary = summarize("A10_TSD", f"q={q},m={m}", states, step)
    if m % q == 0:
        A.check(summary.periodic == 1)
        A.check(summary.max_tail == 2)
    else:
        A.check(summary.periodic == q)
        A.check(summary.max_tail == 1)


# A11: p-th power on the principal-unit group.
def run_pup(p: int, exponent: int) -> None:
    modulus = p ** exponent
    states = tuple(x for x in range(modulus) if x % p == 1)
    step = lambda x: pow(x, p, modulus)
    summary = summarize("A11_PUP", f"p={p},a={exponent}", states, step)
    A.check(summary.fixed == 1 and summary.periodic == 1)
    A.check(summary.max_tail == exponent - 1)
    for state in states:
        predicted = 0 if state == 1 else exponent - valuation(state - 1, p)
        A.check(summary.tail_cycle[state][0] == predicted)


# A12: ideal plus annihilator on products of residue-chain ideals.
def run_isa(exponents: tuple[int, ...]) -> None:
    states = tuple(product(*(range(a + 1) for a in exponents)))

    def step(e):
        return tuple(min(x, a - x) for x, a in zip(e, exponents))

    summary = summarize("A12_ISA", f"a={','.join(map(str, exponents))}", states, step)
    for state in states:
        A.check(step(step(state)) == step(state))
    A.check(summary.max_tail == 1)


# A13: scalar Riccati-defect polynomial x -> x-x^2.
def run_rpd(p: int) -> None:
    states = tuple(range(p))
    step = lambda x: (x - x * x) % p
    summarize("A13_RPD", f"p={p}", states, step)


# A14: projective Mobius map x -> 1+1/x.
def run_pmb(p: int) -> None:
    infinity = p
    states = tuple(range(p + 1))

    def step(x):
        if x == infinity:
            return 1
        if x == 0:
            return infinity
        return (1 + pow(x, -1, p)) % p

    summary = summarize("A14_PMB", f"p={p}", states, step)
    A.check(summary.periodic == len(states) and summary.max_tail == 0)


# A15: fixed-element commutator on the Heisenberg group.
def run_hpc(p: int) -> None:
    states = tuple(product(range(p), repeat=3))
    step = lambda g: (0, 0, (g[0] - g[1]) % p)
    summary = summarize("A15_HPC", f"p={p}", states, step)
    for state in states:
        A.check(iterate(step, state, 2) == (0, 0, 0))
    A.check(summary.fixed == 1 and summary.max_tail == 2)


# A16: transpose-commutator descent on 2x2 matrices.
def run_tcd(p: int) -> None:
    states = tuple(product(range(p), repeat=4))

    def step(a):
        x, y, z, w = a
        diagonal = (y * y - z * z) % p
        off_diagonal = ((x - w) * (z - y)) % p
        return (diagonal, off_diagonal, off_diagonal, -diagonal % p)

    summary = summarize("A16_TCD", f"p={p},d=2", states, step)
    A.check(summary.fixed == 1 and summary.periodic == 1)
    A.check(summary.max_tail == 2)
    for state in states:
        A.check(iterate(step, state, 2) == (0, 0, 0, 0))
    predecessors = Counter(step(state) for state in states)
    for target in states:
        in_image = target[1] == target[2] and target[3] == -target[0] % p
        if not in_image:
            expected = 0
        elif target == (0, 0, 0, 0):
            expected = p ** 3 + p * (p - 1)
        else:
            expected = p * (p - 1)
        A.check(predecessors.get(target, 0) == expected,
                ("TCD fibre", p, target, expected))


def main() -> None:
    emit("P157_P161_ALGEBRAIC_BREADTH_SCOUT_EXACT_CONTROL")
    emit("external_status=HOLD_EXTERNAL")
    emit("enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY")

    for q, m in ((2, 3), (2, 4), (3, 3), (2, 6)):
        run_fad(q, m)
    for args in ((3, 1, 2), (5, 0, 2), (3, 2, 3), (3, 1, 0)):
        run_dgd(*args)
    for exponents in ((4,), (2, 3), (1, 1, 1)):
        run_dcs(exponents)
    for args in ((3, 2), (5, 2), (3, 3)):
        run_npd(*args)
    for args in ((2, 6, 2), (2, 12, 6), (3, 4, 2), (2, 10, 4),
                 (2, 5, 2)):
        run_sce(*args)
    for args in ((3, 4), (5, 3), (3, 5)):
        run_cni(*args)
    for length in (5, 7):
        run_sbe(length)
    for n in (3, 4, 5):
        run_psg(n)
    for args in ((3, 6), (2, 7), (5, 4)):
        run_fpd(*args)
    for args in ((2, 3), (3, 3), (3, 4)):
        run_tsd(*args)
    for args in ((3, 4), (5, 3), (3, 5)):
        run_pup(*args)
    for exponents in ((5,), (3, 4)):
        run_isa(exponents)
    for p in (5, 7, 11):
        run_rpd(p)
    for p in (5, 7, 11):
        run_pmb(p)
    for p in (3, 5):
        run_hpc(p)
    for p in (3, 5, 7):
        run_tcd(p)

    emit(f"boxes={A.boxes}")
    emit(f"assertions={A.assertions}")
    emit("status=PASS")
    print("\n".join(LINES))


if __name__ == "__main__":
    main()
