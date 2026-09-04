#!/usr/bin/env python3
"""Deterministic exact breadth pilot for the unnumbered P187--P191 algebra lane.

Finite controls are counterexample pressure only.  Every candidate has two
parameter boxes and two reported axes: functional-graph dynamics/spectrum and
the all-target fibre histogram.  No output is a proof or an ownership claim.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def analyze(cid, category, box, states, step):
    states = tuple(states)
    index = {x: i for i, x in enumerate(states)}
    check(len(index) == len(states), f"{cid}/{box}: duplicate carrier state")
    nxt = []
    h = sha256()
    for i, x in enumerate(states):
        y = step(x)
        check(y in index, f"{cid}/{box}: update left carrier")
        j = index[y]
        nxt.append(j)
        h.update(f"{i}>{j};".encode())

    image_chain = []
    current = set(range(len(states)))
    while True:
        image_chain.append(len(current))
        following = {nxt[i] for i in current}
        if following == current:
            break
        current = following

    fibres = Counter(nxt)
    fibre_hist = Counter(fibres.get(i, 0) for i in range(len(states)))
    check(sum(k * v for k, v in fibre_hist.items()) == len(states), f"{cid}/{box}: fibre mass")

    tails = Counter()
    periods = Counter()
    cycle_keys = set()
    recurrent = set()
    terminal_basins = 0
    max_tail = 0
    for start in range(len(states)):
        seen = {}
        path = []
        x = start
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = nxt[x]
        mu = seen[x]
        lam = len(path) - mu
        tails[mu] += 1
        periods[lam] += 1
        max_tail = max(max_tail, mu)
        if lam == 1:
            terminal_basins += 1
        cyc = path[mu:]
        recurrent.update(cyc)
        cycle_keys.add(tuple(sorted(cyc)))
    cycle_hist = Counter(len(c) for c in cycle_keys)
    check(sum(k * v for k, v in cycle_hist.items()) == len(recurrent), f"{cid}/{box}: recurrent mass")
    fixed = sum(1 for i, j in enumerate(nxt) if i == j)
    check(fixed == cycle_hist.get(1, 0), f"{cid}/{box}: fixed/cycle agreement")
    check(image_chain[-1] == len(recurrent), f"{cid}/{box}: stable image/recurrent agreement")

    fmt = lambda c: ",".join(f"{k}:{c[k]}" for k in sorted(c)) or "none"
    return (
        f"{cid} category={category} box={box} states={len(states)} "
        f"image_chain={'/'.join(map(str, image_chain))} recurrent={len(recurrent)} "
        f"fixed={fixed} terminal_basins={terminal_basins} max_tail={max_tail} "
        f"tails={fmt(tails)} periods={fmt(periods)} "
        f"spectral_zero_mult={len(states)-len(recurrent)} cycles={fmt(cycle_hist)} "
        f"fibre_hist={fmt(fibre_hist)} max_fibre={max(fibres.values())} "
        f"transition_sha256={h.hexdigest()}"
    )


# ---------- finite modules / nilpotent matrices ----------


def vectors(q, blocks):
    return tuple(product(range(q), repeat=sum(blocks)))


def nilpotent_step(q, blocks, x):
    out = []
    k = 0
    for size in blocks:
        block = x[k:k + size]
        out.extend(block[1:])
        out.append(0)
        k += size
    return tuple(out)


def last_nonzero(q, blocks, x):
    if not any(x):
        return x
    y = x
    while True:
        z = nilpotent_step(q, blocks, y)
        if not any(z):
            return y
        y = z


def module_last_boxes():
    for q, blocks in ((2, (3, 2)), (3, (3, 1))):
        yield f"q={q},lambda={'+'.join(map(str, blocks))}", vectors(q, blocks), lambda x, q=q, b=blocks: last_nonzero(q, b, x)


def loewy_chain_boxes():
    for a in (6, 9):
        yield f"uniserial_length={a}", tuple(range(a + 1)), lambda k: max(0, k - 1)


def all_subspaces(d):
    subs = {frozenset({0})}
    for v in range(1, 1 << d):
        for u in tuple(subs):
            if v not in u:
                subs.add(frozenset(set(u) | {x ^ v for x in u}))
    return tuple(sorted(subs, key=lambda u: (len(u), tuple(sorted(u)))))


def shift_vector(x):
    return x >> 1


def span_binary(gens):
    out = {0}
    for v in gens:
        out |= {x ^ v for x in tuple(out)}
    return frozenset(out)


def shift_retain(U):
    return span_binary([shift_vector(x) for x in U] + [x for x in U if shift_vector(x) == 0])


def subspace_boxes():
    for d in (3, 4):
        yield f"F2^{d},single_Jordan", all_subspaces(d), shift_retain


# ---------- binary matrices ----------


def matrices(d):
    return tuple(product((0, 1), repeat=d * d))


def madd(A, B):
    return tuple(a ^ b for a, b in zip(A, B))


def mtranspose(A, d):
    return tuple(A[j * d + i] for i in range(d) for j in range(d))


def mmul(A, B, d):
    return tuple(sum(A[i*d+k] * B[k*d+j] for k in range(d)) & 1 for i in range(d) for j in range(d))


def mtrace(A, d):
    return sum(A[i*d+i] for i in range(d)) & 1


def mdet(A, d):
    rows = [sum(A[i*d+j] << j for j in range(d)) for i in range(d)]
    rank = 0
    for col in range(d):
        pivot = next((r for r in range(rank, d) if (rows[r] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(d):
            if r != rank and ((rows[r] >> col) & 1):
                rows[r] ^= rows[rank]
        rank += 1
    return int(rank == d)


def transpose_sym(A, d):
    return madd(A, mtranspose(A, d))


def det_feedback(A, d):
    B = list(A)
    B[0] ^= mdet(A, d)
    return tuple(B)


def square_trace(A, d):
    B = list(mmul(A, A, d))
    tr = mtrace(A, d)
    for i in range(d):
        B[i*d+i] ^= tr
    return tuple(B)


def matrix_boxes(kind):
    fn = {"sym": transpose_sym, "det": det_feedback, "sqtr": square_trace}[kind]
    for d in (2, 3):
        yield f"M{d}(F2)", matrices(d), lambda A, d=d, fn=fn: fn(A, d)


# ---------- finite fields GF(2^m) ----------


IRRED = {3: 0b1011, 4: 0b10011, 5: 0b100101}


def fmul(a, b, m):
    mod = IRRED[m]
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= mod
    return out


def fpow(a, e, m):
    out = 1
    while e:
        if e & 1:
            out = fmul(out, a, m)
        a = fmul(a, a, m)
        e >>= 1
    return out


def finv(a, m):
    return 0 if a == 0 else fpow(a, (1 << m) - 2, m)


def ftrace(a, m):
    out = 0
    y = a
    for _ in range(m):
        out ^= y
        y = fmul(y, y, m)
    check(out in (0, 1), f"GF(2^{m}) trace not in prime field")
    return out


def field_boxes(kind):
    for m in (3, 4):
        carrier = tuple(range(1 << m))
        if kind == "frobtrace":
            step = lambda x, m=m: fmul(x, x, m) ^ ftrace(x, m)
        elif kind == "invfrob":
            step = lambda x, m=m: finv(x, m) ^ fmul(x, x, m)
        else:
            step = lambda x, m=m: x ^ ftrace(x, m)
        yield f"GF(2^{m})", carrier, step


# ---------- dihedral groups and subgroup operators ----------


def dmul(x, y, n):
    a, b = x
    c, d = y
    return ((a + (-c if b else c)) % n, (b + d) % 2)


def dinv(x, n):
    a, b = x
    return ((-a if b == 0 else a) % n, b)


def dpow(x, e, n):
    out = (0, 0)
    while e:
        if e & 1:
            out = dmul(out, x, n)
        x = dmul(x, x, n)
        e >>= 1
    return out


def delems(n):
    return tuple((a, b) for b in (0, 1) for a in range(n))


def conjugate(x, g, n):
    return dmul(dmul(g, x, n), dinv(g, n), n)


def class_power(x, n):
    size = len({conjugate(x, g, n) for g in delems(n)})
    return dpow(x, size, n)


def centralizer_power(x, n):
    size = sum(dmul(x, g, n) == dmul(g, x, n) for g in delems(n))
    return dpow(x, size, n)


def group_element_boxes(kind):
    fn = class_power if kind == "class" else centralizer_power
    # Class-size powers need odd, 2 mod 4, and 0 mod 4 controls; the killed
    # centralizer-size route keeps two boxes because no theorem is promoted.
    for n in ((5, 6, 8) if kind == "class" else (5, 6)):
        yield f"D_{{2*{n}}}", delems(n), lambda x, n=n, fn=fn: fn(x, n)


def is_subgroup(S, n):
    if (0, 0) not in S:
        return False
    return all(dmul(x, y, n) in S and dinv(x, n) in S for x in S for y in S)


def subgroups(n):
    G = delems(n)
    return tuple(
        frozenset(G[i] for i in range(len(G)) if (mask >> i) & 1)
        for mask in range(1 << len(G))
        if (mask & 1) and is_subgroup(frozenset(G[i] for i in range(len(G)) if (mask >> i) & 1), n)
    )


def normalizer(H, n):
    return frozenset(g for g in delems(n) if frozenset(conjugate(h, g, n) for h in H) == H)


def center(S, n):
    return frozenset(x for x in S if all(dmul(x, y, n) == dmul(y, x, n) for y in S))


def center_normalizer(H, n):
    return center(normalizer(H, n), n)


def frattini(S, all_subs):
    proper = [K for K in all_subs if K < S]
    maximal = [K for K in proper if not any(K < L < S for L in proper)]
    if not maximal:
        return frozenset({(0, 0)})
    return frozenset.intersection(*maximal)


def subgroup_boxes(kind):
    for n in (3, 4):
        carrier = subgroups(n)
        if kind == "zn":
            step = lambda H, n=n: center_normalizer(H, n)
        else:
            step = lambda H, n=n, ss=carrier: frattini(normalizer(H, n), ss)
        yield f"D_{{2*{n}}}", carrier, step


# ---------- finite lattices ----------


def cyclic_meet_boxes():
    for r in (2, 3):
        masks = range(1 << r)
        carrier = tuple(product(masks, repeat=3))
        yield f"B_{r}^3", carrier, lambda x: (x[0] & x[1], x[1] & x[2], x[2] & x[0])


def rotate_bits(x, r):
    return ((x << 1) & ((1 << r) - 1)) | (x >> (r - 1))


def automorphism_meet_boxes():
    for r in (4, 5):
        yield f"B_{r}", tuple(range(1 << r)), lambda x, r=r: x & rotate_bits(x, r)


# Fixed complete denominator: IDs, categories, and literal routes are not
# removed after seeing the pilot.
CANDIDATES = (
    ("A01", "modules", "nilpotent_last_nonzero", module_last_boxes),
    ("A02", "groups", "conjugacy_class_size_power", lambda: group_element_boxes("class")),
    ("A03", "finite_fields", "frobenius_plus_absolute_trace", lambda: field_boxes("frobtrace")),
    ("A04", "groups", "centralizer_size_power", lambda: group_element_boxes("centralizer")),
    ("A05", "subgroups", "center_of_normalizer", lambda: subgroup_boxes("zn")),
    ("A06", "subgroups", "frattini_of_normalizer", lambda: subgroup_boxes("frattini")),
    ("A07", "matrices", "transpose_symmetrizer", lambda: matrix_boxes("sym")),
    ("A08", "matrices", "determinant_entry_feedback", lambda: matrix_boxes("det")),
    ("A09", "matrices", "square_plus_trace_identity", lambda: matrix_boxes("sqtr")),
    ("A10", "finite_fields", "inverse_plus_frobenius", lambda: field_boxes("invfrob")),
    ("A11", "finite_fields", "absolute_trace_translation", lambda: field_boxes("trace")),
    ("A12", "lattices", "cyclic_pairwise_meet", cyclic_meet_boxes),
    ("A13", "lattices", "automorphism_meet_erosion", automorphism_meet_boxes),
    ("A14", "modules", "uniserial_socle_lift_index", loewy_chain_boxes),
    ("A15", "modules", "nilpotent_image_kernel_retain", subspace_boxes),
)


def main():
    check(len(CANDIDATES) == 15, "fixed denominator changed")
    check(len({x[0] for x in CANDIDATES}) == 15, "candidate IDs not unique")
    check(len({x[2] for x in CANDIDATES}) == 15, "literal routes not unique")
    check(len({x[1] for x in CANDIDATES}) >= 4, "category breadth below four")
    rows = []
    for cid, category, literal, boxes in CANDIDATES:
        produced = list(boxes())
        check(len(produced) >= 2, f"{cid}: missing second axis box")
        for box, states, step in produced:
            rows.append(analyze(cid, category, box, states, step))
    print("P187_191_ALGEBRA_BREADTH_PILOT_V1")
    print(f"candidate_denominator={len(CANDIDATES)}")
    print(f"categories={','.join(sorted({x[1] for x in CANDIDATES}))}")
    print(f"boxes={len(rows)}")
    print("axis_1=functional_graph_orbit_image_terminal_spectrum")
    print("axis_2=all_target_fibre_histogram")
    for row in rows:
        print(row)
    print(f"exact_assertions={ASSERTIONS}")
    print("finite_controls_are_proofs=false")
    print("owner_nonhit_implies_novelty=false")
    print("numbering_assigned=false")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
