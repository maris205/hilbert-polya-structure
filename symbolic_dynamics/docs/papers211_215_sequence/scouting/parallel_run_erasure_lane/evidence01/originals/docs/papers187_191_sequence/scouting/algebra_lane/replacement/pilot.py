#!/usr/bin/env python3
"""Deterministic exact controls for the algebra replacement denominator.

Every update is implemented directly here.  These finite checks are
counterexample pressure, not proofs, experiments, or ownership evidence.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path


ASSERTIONS = 0
SOURCE_BINDINGS = {
    "docs/papers187_191_sequence/HISTORICAL_COLLISION_SEED.md":
        "19440c86bd1663367f6aba05600a4b137fe9420855bd0c58aeb5dc954b021a3f",
    "docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md":
        "8e45d2b1d5d0f5dd21904141b9878488972d2d010a5ab62c0f6f7127da00b5fd",
    "docs/papers142_146_sequence/scouting/combinatorial/SCOUT.md":
        "4ed0adffbf60751c96772ad3e3908a83820def5418991c783cf0e86419f20e2e",
    "docs/papers177_181_sequence/scouting/algebra_lane/COLLISION_FIREWALL.md":
        "a20b5ba9f623bcc844706d2dd7fe10311160e879622d6edca361899431d0293d",
    "docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md":
        "c70e3da15106495e5bda56373b81bf07a8393fff19b12d38a674aaf38b5fa23f",
    "docs/papers172_176_sequence/scouting/algebra_arithmetic/SCOUT_AND_KILL_LEDGER.md":
        "2a8e024e6f6c8c6029b74387e4634141ed547d13cbfaf85bf50becab60a060a8",
}


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def bind_sources():
    root = Path(__file__).resolve().parents[5]
    digest = sha256()
    for rel, expected in sorted(SOURCE_BINDINGS.items()):
        actual = sha256((root / rel).read_bytes()).hexdigest()
        check(actual == expected, f"source drift: {rel}")
        digest.update(f"{rel}\0{actual}\n".encode())
    return digest.hexdigest()


def orbit_indices(nxt, start):
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = nxt[x]
    return seen[x], len(seen) - seen[x], x


def analyze(cid, box, states, step):
    states = tuple(states)
    index = {x: i for i, x in enumerate(states)}
    check(len(index) == len(states), f"{cid}/{box}: duplicate state")
    nxt = []
    edge_digest = sha256()
    for i, state in enumerate(states):
        target = step(state)
        check(target in index, f"{cid}/{box}: closure")
        j = index[target]
        nxt.append(j)
        edge_digest.update(f"{i}>{j};".encode())
    fibres = Counter(nxt)
    fibre_hist = Counter(fibres.get(i, 0) for i in range(len(states)))
    check(sum(k * v for k, v in fibre_hist.items()) == len(states),
          f"{cid}/{box}: fibre mass")
    tails = Counter()
    cycles = set()
    recurrent = set()
    max_tail = 0
    max_period = 0
    for start in range(len(states)):
        tail, period, entry = orbit_indices(nxt, start)
        tails[tail] += 1
        max_tail = max(max_tail, tail)
        max_period = max(max_period, period)
        cyc = []
        x = entry
        for _ in range(period):
            recurrent.add(x)
            cyc.append(x)
            x = nxt[x]
        cycles.add(tuple(sorted(cyc)))
    cycle_hist = Counter(len(c) for c in cycles)
    check(sum(k * v for k, v in cycle_hist.items()) == len(recurrent),
          f"{cid}/{box}: recurrent mass")
    image = set(nxt)
    fmt = lambda c: ",".join(f"{k}:{c[k]}" for k in sorted(c)) or "none"
    return (f"{cid} box={box} states={len(states)} image={len(image)} "
            f"recurrent={len(recurrent)} fixed={cycle_hist.get(1,0)} "
            f"max_tail={max_tail} max_period={max_period} "
            f"tails={fmt(tails)} cycles={fmt(cycle_hist)} "
            f"fibres={fmt(fibre_hist)} max_fibre={max(fibres.values())} "
            f"transition_sha256={edge_digest.hexdigest()}")


# R01/R10: aperiodic Brandt semigroup of matrix units.


ZERO = (-1, -1)


def brandt_alphabet(n):
    return (ZERO,) + tuple((i, j) for i in range(n) for j in range(n))


def bmul(x, y):
    if x == ZERO or y == ZERO or x[1] != y[0]:
        return ZERO
    return (x[0], y[1])


def binv(x):
    return ZERO if x == ZERO else (x[1], x[0])


def brandt_sandwich(word):
    m = len(word)
    return tuple(bmul(bmul(word[i], word[(i + 1) % m]), word[i])
                 for i in range(m))


def brandt_product_automaton(word):
    m = len(word)
    return tuple(bmul(word[i], word[(i + 1) % m]) for i in range(m))


def brandt_local(x, y):
    """Literal local output, separate from the global cyclic implementation."""
    return bmul(bmul(x, y), x)


def matmul(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))


def brandt_transfer_fibre(target, alphabet):
    """Count a target by cyclic path DP, without enumerating source words."""
    total = 0
    for first in alphabet:
        paths = {first: 1}
        for output in target[:-1]:
            following = {}
            for left, count in paths.items():
                for right in alphabet:
                    if brandt_local(left, right) == output:
                        following[right] = following.get(right, 0) + count
            paths = following
        total += sum(count for left, count in paths.items()
                     if brandt_local(left, first) == target[-1])
    return total


def longest_cyclic_true_run(bits):
    if all(bits):
        return len(bits)
    best = run = 0
    for bit in bits + bits:
        run = run + 1 if bit else 0
        best = max(best, run)
    return min(best, len(bits) - 1)


def brandt_predicted_tail(word):
    if all(x == ZERO for x in word):
        return 0
    good = tuple(word[i] != ZERO and word[(i + 1) % len(word)] == binv(word[i])
                 for i in range(len(word)))
    return 0 if all(good) else longest_cyclic_true_run(good) + 1


def attack_r01():
    rows = []
    boxes = (tuple((1, m) for m in range(1, 6))
             + tuple((2, m) for m in range(1, 6))
             + tuple((3, m) for m in range(1, 4)))
    for n, m in boxes:
        alphabet = brandt_alphabet(n)
        states = tuple(product(alphabet, repeat=m))
        for word in states:
            current = word
            good = tuple(word[(i + 1) % m] == binv(word[i]) and word[i] != ZERO
                         for i in range(m))
            for t in range(1, m + 2):
                current = brandt_sandwich(current)
                predicted = tuple(word[i] if all(good[(i + j) % m] for j in range(t))
                                  else ZERO for i in range(m))
                check(current == predicted, "R01 alternating-run iterate")
            tail, period, _ = orbit_state(brandt_sandwich, word)
            check(period == 1 and tail == brandt_predicted_tail(word),
                  "R01 exact tail normal form")

        fixed_expected = 1 + (n if m % 2 else n * n)
        fixed_actual = sum(brandt_sandwich(x) == x for x in states)
        check(fixed_actual == fixed_expected, "R01 fixed colored cycles")
        row = analyze("R01/BSE", f"B{n},m={m}", states, brandt_sandwich)
        expected_max_tail = max(0, m - 1) if n == 1 else (m if m % 2 else m - 1)
        observed_max_tail = max(orbit_state(brandt_sandwich, x)[0] for x in states)
        check(observed_max_tail == expected_max_tail, "R01 sharp tail")

        # Every-target transfer calculation and mass conservation.
        global_fibres = Counter(brandt_sandwich(x) for x in states)
        transfer = {}
        for target in states:
            transfer[target] = brandt_transfer_fibre(target, alphabet)
            check(transfer[target] == global_fibres.get(target, 0),
                  "R01 every-target transfer fibre")
        check(sum(transfer.values()) == len(states), "R01 transfer mass")

        # Let A=M_0.  Nonzero target symbols pin adjacent source symbols,
        # producing a product of A-power entries over cyclic zero gaps.
        q = len(alphabet)
        index = {x: i for i, x in enumerate(alphabet)}
        identity = tuple(tuple(int(i == j) for j in range(q)) for i in range(q))
        zero_matrix = tuple(tuple(int(brandt_local(x, y) == ZERO) for y in alphabet)
                            for x in alphabet)
        powers = [identity]
        for _ in range(m):
            powers.append(matmul(powers[-1], zero_matrix))
        all_zero = (ZERO,) * m
        check(transfer[all_zero] == sum(powers[m][i][i] for i in range(q)),
              "R01 zero-target trace")
        for target in states:
            anchors = [i for i, output in enumerate(target) if output != ZERO]
            if not anchors:
                continue
            gap_product = 1
            for j, position in enumerate(anchors):
                following = anchors[(j + 1) % len(anchors)]
                gap = (following - position - 1) % m
                gap_product *= powers[gap][index[binv(target[position])]][index[target[following]]]
            check(transfer[target] == gap_product, "R01 target gap product")

        # Closed trace of A^m.  If r=n^2, the exceptional roots satisfy
        # z^2-rz-1=0 and the residual eigenvalues are +/-1.
        r = n * n
        if m == 1:
            exceptional_sum = r
        else:
            previous, current = 2, r
            for _ in range(2, m + 1):
                previous, current = current, r * current + previous
            exceptional_sum = current
        d_plus = (r + n) // 2
        d_minus = (r - n) // 2
        zero_formula = (exceptional_sum + (-1) ** m * (d_plus - 1) + d_minus)
        check(transfer[all_zero] == zero_formula, "R01 zero-target spectrum")
        rows.append(row)
    return rows


# R02/R09: rectangular bands.


def rband_alphabet(left, right):
    return tuple((i, j) for i in range(left) for j in range(right))


def rbmul(x, y):
    return (x[0], y[1])


def rb_word_step(word):
    return tuple(rbmul(word[i], word[i + 1]) for i in range(len(word) - 1)) + (word[-1],)


def rb_exchange(pair):
    x, y = pair
    return (rbmul(x, y), rbmul(y, x))


def attack_r02():
    rows = []
    alphabet = rband_alphabet(2, 2)
    for m in (3, 4, 5, 6):
        states = tuple(product(alphabet, repeat=m))
        for word in states:
            current = word
            for t in range(1, m):
                current = rb_word_step(current)
                predicted = tuple((word[i][0], word[min(i + t, m - 1)][1])
                                  for i in range(m))
                check(current == predicted, "R02 coordinate-shift iterate")
        rows.append(analyze("R02/RBW", f"2x2,m={m}", states, rb_word_step))
    return rows


def attack_r09():
    rows = []
    for left, right in ((2, 2), (2, 3)):
        alphabet = rband_alphabet(left, right)
        states = tuple(product(alphabet, repeat=2))
        check(all(rb_exchange(rb_exchange(x)) == x for x in states),
              "R09 product-exchange involution")
        rows.append(analyze("R09/RPX", f"{left}x{right}", states, rb_exchange))
    return rows


# R03: nonlinear saturation arrays.


def cap_sum_step(x, cap):
    m = len(x)
    return tuple(min(cap, x[i] + x[(i + 1) % m]) for i in range(m))


def attack_r03():
    rows = []
    for cap in (2, 3):
        for m in (3, 4, 5, 6):
            states = tuple(product(range(cap + 1), repeat=m))
            step = lambda x, cap=cap: cap_sum_step(x, cap)
            for x in states:
                y = step(x)
                check(all(a <= b for a, b in zip(x, y)), "R03 coordinate monotonicity")
                check((y == x) == (x == (0,) * m or x == (cap,) * m),
                      "R03 fixed locus")
            rows.append(analyze("R03/CSA", f"a={cap},m={m}", states, step))
    return rows


# R04/R05: explicit finite groups.


def permutation_table_three():
    elems = tuple(p for p in product(range(3), repeat=3) if len(set(p)) == 3)
    index = {p: i for i, p in enumerate(elems)}
    return tuple(tuple(index[tuple(p[q[i]] for i in range(3))] for q in elems)
                 for p in elems)


def dihedral_table(n):
    elems = tuple((k, e) for e in (0, 1) for k in range(n))
    index = {x: i for i, x in enumerate(elems)}
    def mul(x, y):
        k, e = x
        ell, f = y
        return ((k + (-ell if e else ell)) % n, e ^ f)
    return tuple(tuple(index[mul(x, y)] for y in elems) for x in elems)


def identity_of(table):
    return next(e for e in range(len(table))
                if all(table[e][x] == x and table[x][e] == x for x in range(len(table))))


def inverses_of(table):
    identity = identity_of(table)
    return tuple(next(y for y in range(len(table))
                      if table[x][y] == identity and table[y][x] == identity)
                 for x in range(len(table)))


def hurwitz(pair, table, inverses):
    x, y = pair
    return (table[table[x][y]][inverses[x]], x)


def commuting_swap(pair, table):
    x, y = pair
    return (y, x) if table[x][y] == table[y][x] else pair


def attack_groups():
    rows = []
    for name, table in (("S3", permutation_table_three()), ("D8", dihedral_table(4))):
        inv = inverses_of(table)
        states = tuple(product(range(len(table)), repeat=2))
        hstep = lambda x, table=table, inv=inv: hurwitz(x, table, inv)
        himages = {hstep(x) for x in states}
        check(len(himages) == len(states), "R04 Hurwitz bijection")
        rows.append(analyze("R04/HUR", name, states, hstep))
        cstep = lambda x, table=table: commuting_swap(x, table)
        check(all(cstep(cstep(x)) == x for x in states), "R05 commuting involution")
        rows.append(analyze("R05/CSW", name, states, cstep))
    return rows


# R06: rank-gated vector rotation.


def vector_rank(vectors, q):
    rows = [list(v) for v in vectors]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for col in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] % q), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col], -1, q)
        rows[rank] = [(scale * x) % q for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] % q:
                factor = rows[r][col] % q
                rows[r] = [(a - factor * b) % q for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def rank_gate_rotate(triple, q):
    return triple[1:] + triple[:1] if vector_rank(triple, q) == 3 else triple


def attack_r06():
    rows = []
    for q in (2, 3):
        vectors = tuple(product(range(q), repeat=3))
        states = tuple(product(vectors, repeat=3))
        step = lambda x, q=q: rank_gate_rotate(x, q)
        check(all(step(step(step(x))) == x for x in states), "R06 cube identity")
        rows.append(analyze("R06/MGR", f"F{q}^3", states, step))
    return rows


# R07: synchronous integer floor averaging.


def integer_average(x):
    m = len(x)
    return tuple((x[i] + x[(i + 1) % m]) // 2 for i in range(m))


def attack_r07():
    rows = []
    cap = 3
    for m in (3, 4, 5, 6):
        states = tuple(product(range(cap + 1), repeat=m))
        for x in states:
            check(sum(integer_average(x)) <= sum(x), "R07 sum Lyapunov")
        rows.append(analyze("R07/IAV", f"a={cap},m={m}", states, integer_average))
    return rows


# R08: deterministic parallel cancellation in a free-group alphabet.


INVERSE = {0: 1, 1: 0, 2: 3, 3: 2}


def parallel_free_reduce(word):
    out = []
    i = 0
    while i < len(word):
        if i + 1 < len(word) and INVERSE[word[i]] == word[i + 1]:
            i += 2
        else:
            out.append(word[i])
            i += 1
    return tuple(out)


def stack_reduce(word):
    stack = []
    for letter in word:
        if stack and INVERSE[letter] == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def attack_r08():
    states = tuple(word for length in range(7)
                   for word in product(range(4), repeat=length))
    for word in states:
        tail, period, endpoint = orbit_state(parallel_free_reduce, word)
        check(period == 1, "R08 termination")
        check(endpoint == stack_reduce(word), "R08 free normal form")
        check(tail <= len(word) // 2, "R08 deletion clock bound")
    return [analyze("R08/PFR", "rank2,length<=6", states, parallel_free_reduce)]


def orbit_state(step, start):
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = step(x)
    return seen[x], len(seen) - seen[x], x


def attack_r10():
    rows = []
    alphabet = brandt_alphabet(2)
    for m in (3, 4, 5):
        states = tuple(product(alphabet, repeat=m))
        rows.append(analyze("R10/BPA", f"B2,m={m}", states, brandt_product_automaton))
    return rows


def main():
    binding = bind_sources()
    rows = []
    rows.extend(attack_r01())
    rows.extend(attack_r02())
    rows.extend(attack_r03())
    rows.extend(attack_groups())
    rows.extend(attack_r06())
    rows.extend(attack_r07())
    rows.extend(attack_r08())
    rows.extend(attack_r09())
    rows.extend(attack_r10())
    print("P187-P191 ALGEBRA REPLACEMENT EXACT PILOT")
    print("scope=bounded_falsification_not_proof_not_novelty")
    print("candidate_denominator=10")
    print(f"source_bindings={len(SOURCE_BINDINGS)} aggregate_sha256={binding}")
    for row in rows:
        print(row)
    print(f"assertions={ASSERTIONS}")
    print("survivors=1 ids=R01 status=PROVISIONAL_OWNER_AMBER_HOLD_EXTERNAL_UNNUMBERED")


if __name__ == "__main__":
    main()
