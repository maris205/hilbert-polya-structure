#!/usr/bin/env python3
"""Process-separated hostile Review B exact control for P182 Round 1.

Subspaces are represented by their annihilator flats in the dual projective
geometry.  A flat is a frozenset of normalized one-dimensional functionals;
Gaussian elimination is used only as a rank oracle.  Thus this verifier uses
neither author-side RREF subspace objects nor Review-A vector-closure bitsets.
"""

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PAPER = ROOT / "papers" / "182-cyclic-subspace-lattice-comparator"
REVIEW_A = ROOT / "docs" / "papers182_186_sequence" / "reviews" / "paper182" / "reviewer_A_combinatorial"

FROZEN_TEX = "9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7"
FROZEN_ROUND1 = "880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07"

# These terminal lifecycle receipts were appended after the scientific
# Review-B census was frozen.  They remain hard-fail bindings but do not enter
# the original exact-assertion counter, avoiding a manifest/review-count loop.
TERMINAL_LIFECYCLE_ROWS = frozenset({
    "IMPROVEMENT_LOG.md",
    "FINAL_QA.md",
    "main_round1.pdf",
    "main_round2.pdf",
})

ASSERTIONS = 0
TRANSITIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def hard_check(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def verify_manifest(directory, expected_minimum, uncounted_rows=frozenset()):
    manifest = directory / "SHA256SUMS"
    rows = []
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        checksum, relative = line.split(maxsplit=1)
        relative = relative.strip()
        row_check = hard_check if relative in uncounted_rows else check
        row_check(relative != "SHA256SUMS", ("self-referential manifest", directory))
        row_check((directory / relative).is_file(), ("missing manifest object", relative))
        row_check(digest(directory / relative) == checksum,
                  ("manifest mismatch", directory, relative))
        rows.append(relative)
    check(len(rows) >= expected_minimum, ("short manifest", directory, len(rows)))
    hard_check(uncounted_rows.issubset(rows),
               ("terminal lifecycle manifest rows missing", directory))
    return len(rows)


def artifact_audit():
    check(digest(PAPER / "main.tex") == FROZEN_TEX, "frozen main.tex changed")
    check(digest(PAPER / "main_round1.pdf") == FROZEN_ROUND1,
          "frozen Round-1 PDF changed")
    check((PAPER / "main_round1.pdf").read_bytes()
          == (PAPER / "main_round0_original.pdf").read_bytes(),
          "Round 1 is not the no-change Round-0 receipt")
    author_rows = verify_manifest(PAPER, 19, TERMINAL_LIFECYCLE_ROWS)
    review_a_rows = verify_manifest(REVIEW_A, 4)

    tex = (PAPER / "main.tex").read_text()
    proof = (PAPER / "PROOF_PACKAGE.md").read_text()
    source = (PAPER / "SOURCE_VERIFICATION.md").read_text()
    canonical = (PAPER / "code" / "CANONICAL.txt").read_text()
    for token in (
        r"T^4=T^2", r"M\subseteq J", r"\kappa_0<\kappa_1<\cdots<\kappa_d",
        "328{,}700", "1{,}667{,}850", "hold\\_external",
    ):
        check(token in tex, ("missing manuscript contract token", token))
    for token in ("T^4=T^2", "depth 0:", "kappa_k(q)", "d=0"):
        check(token in proof, ("missing proof-package token", token))
    for token in ("OWNER_AMBER", "HOLD_EXTERNAL", "bounded non-hit"):
        check(token in source, ("missing source-control token", token))
    for token in ("boxes=15", "transitions=328700", "exact_assertions=1667850",
                  "external_status=HOLD_EXTERNAL"):
        check(token in canonical, ("missing canonical receipt", token))

    bib = (PAPER / "references.bib").read_text()
    keys = []
    for line in bib.splitlines():
        if line.startswith("@"):
            keys.append(line.split("{", 1)[1].split(",", 1)[0])
    check(len(keys) == 5 and len(set(keys)) == 5, "bibliography key census")
    for key in keys:
        check(("{" + key + "}") in tex or key in tex, ("uncited key", key))
    check("TODO" not in tex and "VERIFY" not in tex, "draft token in manuscript")
    return author_rows, review_a_rows


def fadd(q, x, y):
    return x ^ y if q == 4 else (x + y) % q


def fmul(q, x, y):
    if q != 4:
        return (x * y) % q
    answer = 0
    left, right = x, y
    while right:
        if right & 1:
            answer ^= left
        right >>= 1
        left <<= 1
        if left & 4:
            left ^= 7  # x^2+x+1
    return answer & 3


def fneg(q, x):
    return x if q == 4 else (-x) % q


def finv(q, x):
    check(x != 0, "inverse of zero")
    candidates = [y for y in range(1, q) if fmul(q, x, y) == 1]
    check(len(candidates) == 1, ("nonunique inverse", q, x))
    return candidates[0]


def verify_field(q):
    for x, y, z in product(range(q), repeat=3):
        check(fadd(q, x, y) == fadd(q, y, x), "add commutativity")
        check(fmul(q, x, y) == fmul(q, y, x), "mul commutativity")
        check(fadd(q, fadd(q, x, y), z) == fadd(q, x, fadd(q, y, z)),
              "add associativity")
        check(fmul(q, fmul(q, x, y), z) == fmul(q, x, fmul(q, y, z)),
              "mul associativity")
        check(fmul(q, x, fadd(q, y, z))
              == fadd(q, fmul(q, x, y), fmul(q, x, z)),
              "distributivity")
    for x in range(1, q):
        finv(q, x)


def vadd(q, left, right):
    return tuple(fadd(q, x, y) for x, y in zip(left, right))


def vscale(q, scalar, vector):
    return tuple(fmul(q, scalar, x) for x in vector)


def normalize(q, vector):
    for x in vector:
        if x:
            return vscale(q, finv(q, x), vector)
    raise ValueError("zero has no projective normalization")


def matrix_rank(q, rows):
    matrix = [list(row) for row in rows if any(row)]
    if not matrix:
        return 0
    columns = len(matrix[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, len(matrix))
                      if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = finv(q, matrix[pivot_row][column])
        matrix[pivot_row] = [fmul(q, inverse, x) for x in matrix[pivot_row]]
        for r in range(len(matrix)):
            if r == pivot_row or not matrix[r][column]:
                continue
            factor = fneg(q, matrix[r][column])
            matrix[r] = [fadd(q, x, fmul(q, factor, y))
                         for x, y in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


class DualProjectiveGeometry:
    def __init__(self, q, d):
        self.q = q
        self.d = d
        vectors = product(range(q), repeat=d)
        self.points = tuple(sorted({normalize(q, v) for v in vectors if any(v)}))

        @lru_cache(maxsize=None)
        def closure(seed):
            seed = tuple(seed)
            rank = matrix_rank(q, seed)
            return frozenset(point for point in self.points
                             if matrix_rank(q, seed + (point,)) == rank)

        self.closure = closure
        flats = {frozenset()}
        for r in range(1, d + 1):
            for generators in combinations(self.points, r):
                if matrix_rank(q, generators) == r:
                    flats.add(closure(tuple(generators)))
        self.flats = tuple(sorted(flats,
                                  key=lambda flat: (matrix_rank(q, tuple(flat)),
                                                    tuple(sorted(flat)))))
        self.index = {flat: i for i, flat in enumerate(self.flats)}
        self.dual_rank = tuple(matrix_rank(q, tuple(flat)) for flat in self.flats)
        self.rank = tuple(d - r for r in self.dual_rank)
        self.zero = max(range(len(self.flats)), key=lambda i: self.dual_rank[i])
        self.whole = self.index[frozenset()]
        self.meet = []
        self.join = []
        for left in self.flats:
            meet_row, join_row = [], []
            for right in self.flats:
                # annihilator(A meet B) = ann(A) + ann(B)
                meet_flat = closure(tuple(sorted(left | right)))
                # annihilator(A + B) = ann(A) meet ann(B)
                join_flat = left & right
                check(meet_flat in self.index, "dual meet flat absent")
                check(join_flat in self.index, "dual join flat absent")
                meet_row.append(self.index[meet_flat])
                join_row.append(self.index[join_flat])
            self.meet.append(tuple(meet_row))
            self.join.append(tuple(join_row))
        self.meet = tuple(self.meet)
        self.join = tuple(self.join)

        check(len(self.flats) == galois(d, q), ("Galois count", q, d))
        for i, j in product(range(len(self.flats)), repeat=2):
            m, u = self.meet[i][j], self.join[i][j]
            check(self.contained(m, i) and self.contained(m, j), "meet containment")
            check(self.contained(i, u) and self.contained(j, u), "join containment")
            check(self.rank[i] + self.rank[j] == self.rank[m] + self.rank[u],
                  "modular dimension identity")

    def contained(self, primal_left, primal_right):
        return self.flats[primal_right] <= self.flats[primal_left]


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = prod(q ** (n - i) - 1 for i in range(k))
    denominator = prod(q ** (k - i) - 1 for i in range(k))
    check(numerator % denominator == 0, "Gaussian coefficient integrality")
    return numerator // denominator


def galois(n, q):
    return sum(gaussian(n, k, q) for k in range(n + 1))


def kappa(k, q):
    return sum(gaussian(k, a, q) * q ** (a * (k - a))
               for a in range(k + 1))


def q_disjoint(n, q):
    return sum(gaussian(n, a, q) * gaussian(n - a, s, q) * q ** (a * s)
               for a in range(n + 1) for s in range(n - a + 1))


def lattice_from_order(name, size, leq):
    meet, join = [], []
    for a in range(size):
        mr, jr = [], []
        for b in range(size):
            lowers = [x for x in range(size) if leq(x, a) and leq(x, b)]
            uppers = [x for x in range(size) if leq(a, x) and leq(b, x)]
            maxima = [x for x in lowers if all(not leq(x, y) or x == y for y in lowers)]
            minima = [x for x in uppers if all(not leq(y, x) or x == y for y in uppers)]
            check(len(maxima) == 1 and len(minima) == 1,
                  ("not a lattice", name, a, b, maxima, minima))
            mr.append(maxima[0])
            jr.append(minima[0])
        meet.append(tuple(mr))
        join.append(tuple(jr))
    return tuple(meet), tuple(join), leq


def universal_lattice_checks():
    lattices = []
    for n in (1, 2, 4, 7):
        lattices.append((f"chain{n}",) + lattice_from_order(
            f"chain{n}", n, lambda x, y: x <= y))
    lattices.append(("boolean_B3",) + lattice_from_order(
        "boolean_B3", 8, lambda x, y: x & ~y == 0))
    # M3: 0, three atoms, 1.
    lattices.append(("M3",) + lattice_from_order(
        "M3", 5, lambda x, y: x == y or x == 0 or y == 4))
    # N5: 0<a<b<1 and 0<c<1.
    order_pairs = {(i, i) for i in range(5)} | {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 4), (3, 4)
    }
    lattices.append(("N5",) + lattice_from_order(
        "N5", 5, lambda x, y: (x, y) in order_pairs))

    rows = []
    for name, meet, join, leq in lattices:
        n = len(meet)
        image = set()
        for state in product(range(n), repeat=3):
            a, b, c = state
            step1 = (c, meet[a][b], join[a][b])
            x, y, z = step1
            step2 = (z, meet[x][y], join[x][y])
            x, y, z = step2
            step3 = (z, meet[x][y], join[x][y])
            x, y, z = step3
            step4 = (z, meet[x][y], join[x][y])
            claimed2 = (join[a][b], meet[c][meet[a][b]], join[c][meet[a][b]])
            check(step2 == claimed2, ("universal T2", name, state))
            check(step4 == step2, ("universal T4=T2", name, state))
            recurrent = step2 == state
            expected_recurrent = leq(b, a) and leq(b, c)
            check(recurrent == expected_recurrent, ("universal recurrence", name, state))
            if recurrent:
                check(step1 == (c, b, a), ("outer swap", name, state))
                check((step1 == state) == (a == c), ("fixed criterion", name, state))
            expected_depth = 0 if expected_recurrent else 1 if leq(meet[a][b], c) else 2
            actual_depth = 0 if recurrent else 1 if (
                step1[1] == meet[step1[0]][step1[1]]
                and step1[1] == meet[step1[1]][step1[2]]) else 2
            check(actual_depth == expected_depth, ("universal depth", name, state))
            image.add(step1)
        expected_image = {(c, m, j) for c, m, j in product(range(n), repeat=3)
                          if leq(m, j)}
        check(image == expected_image, ("universal image", name))
        rows.append((name, n, n ** 3, len(image)))
    return rows


def counter_text(counter):
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def audit_box(q, d):
    global TRANSITIONS
    geometry = DualProjectiveGeometry(q, d)
    l = len(geometry.flats)

    def encode(a, b, c):
        return (a * l + b) * l + c

    def decode(state):
        a, c = divmod(state, l)
        a, b = divmod(a, l)
        return a, b, c

    def action(state):
        a, b, c = decode(state)
        return encode(c, geometry.meet[a][b], geometry.join[a][b])

    states = l ** 3
    successor = [action(state) for state in range(states)]
    TRANSITIONS += states
    indegree = [0] * states
    for target in successor:
        indegree[target] += 1

    actual_image = set(successor)
    predicted_image = set()
    recurrent_states = set()
    fixed_states = set()
    strict_cycle_pairs = set()
    depths = Counter()
    for state in range(states):
        a, b, c = decode(state)
        t1 = successor[state]
        t2 = successor[t1]
        t4 = successor[successor[t2]]
        m = geometry.meet[a][b]
        claimed_t2 = encode(geometry.join[a][b], geometry.meet[c][m],
                            geometry.join[c][m])
        check(t2 == claimed_t2, ("field T2", q, d, state))
        check(t4 == t2, ("field T4=T2", q, d, state))
        recurrent = geometry.contained(b, a) and geometry.contained(b, c)
        check((t2 == state) == recurrent, ("field recurrence", q, d, state))
        if recurrent:
            recurrent_states.add(state)
            check(t1 == encode(c, b, a), ("field outer swap", q, d, state))
            if t1 == state:
                fixed_states.add(state)
                check(a == c, ("field fixed only if outer equal", q, d, state))
            else:
                strict_cycle_pairs.add(tuple(sorted((state, t1))))
        expected_depth = 0 if recurrent else 1 if geometry.contained(m, c) else 2
        actual_depth = 0 if t2 == state else 1 if successor[successor[t1]] == t1 else 2
        check(actual_depth == expected_depth, ("field depth", q, d, state))
        depths[actual_depth] += 1

    for c, m, j in product(range(l), repeat=3):
        if geometry.contained(m, j):
            predicted_image.add(encode(c, m, j))
    check(actual_image == predicted_image, ("field image set", q, d))

    gd = galois(d, q)
    alpha = sum(gaussian(d, b, q) * galois(d - b, q) for b in range(d + 1))
    rho = sum(gaussian(d, b, q) * galois(d - b, q) ** 2
              for b in range(d + 1))
    qvals = [q_disjoint(n, q) for n in range(d + 1)]
    eta = sum(gaussian(d, m, q) * qvals[d - m] * galois(d - m, q)
              for m in range(d + 1))
    check(states == gd ** 3, ("carrier count", q, d))
    check(len(actual_image) == gd * alpha, ("image count", q, d))
    check(len(fixed_states) == alpha, ("fixed count", q, d))
    check(len(recurrent_states) == rho, ("recurrent count", q, d))
    check(len(strict_cycle_pairs) == (rho - alpha) // 2,
          ("strict two-cycle count", q, d))
    check(depths == Counter({0: rho, 1: eta - rho, 2: states - eta}),
          ("depth census", q, d, depths))
    if d == 0:
        check(depths == Counter({0: 1}), "d=0 boundary")
    else:
        check(depths[2] > 0, ("sharp height two", q, d))

    # Direct disjoint-pair enumeration attacks Q_n independently.
    direct_disjoint = sum(geometry.meet[a][b] == geometry.zero
                          for a, b in product(range(l), repeat=2))
    check(direct_disjoint == qvals[d], ("Q direct count", q, d))

    kappas = [kappa(k, q) for k in range(d + 1)]
    check(all(kappas[k] < kappas[k + 1] for k in range(d)),
          ("strict kappa chain", q, d, kappas))
    actual_hist = Counter(indegree)
    expected_hist = Counter()
    expected_hist[0] = states - gd * alpha
    for k in range(d + 1):
        intervals = sum(gaussian(d, m, q) * gaussian(d - m, k, q)
                        for m in range(d - k + 1))
        expected_hist[kappas[k]] += gd * intervals
    check(actual_hist == expected_hist,
          ("complete fibre histogram", q, d, actual_hist, expected_hist))
    check(sum(size * count for size, count in actual_hist.items()) == states,
          ("fibre mass", q, d))

    actual_max = {state for state, degree in enumerate(indegree)
                  if degree == kappas[d]}
    expected_max = {encode(c, geometry.zero, geometry.whole) for c in range(l)}
    check(actual_max == expected_max, ("complete maximum set", q, d))
    actual_minpos = {state for state, degree in enumerate(indegree) if degree == 1}
    expected_minpos = {encode(c, m, m) for c, m in product(range(l), repeat=2)}
    check(actual_minpos == expected_minpos, ("complete minimum-positive set", q, d))

    # For every interval and every first summand, count its relative
    # complements.  This is stronger than checking only the aggregate fibre.
    for m, j in product(range(l), repeat=2):
        if not geometry.contained(m, j):
            continue
        k = geometry.rank[j] - geometry.rank[m]
        total = 0
        for a in range(l):
            if not (geometry.contained(m, a) and geometry.contained(a, j)):
                continue
            complement_count = sum(
                geometry.meet[a][b] == m and geometry.join[a][b] == j
                for b in range(l)
            )
            relative_rank = geometry.rank[a] - geometry.rank[m]
            expected = q ** (relative_rank * (k - relative_rank))
            check(complement_count == expected,
                  ("every-A relative complement count", q, d, m, j, a))
            total += complement_count
        check(total == kappas[k], ("every-interval kappa", q, d, m, j))

    return {
        "q": q, "d": d, "L": l, "states": states,
        "image": len(actual_image), "fixed": len(fixed_states),
        "cycles2": len(strict_cycle_pairs), "depths": counter_text(depths),
        "fibres": counter_text(actual_hist), "kappa": ",".join(map(str, kappas)),
    }


def main():
    author_rows, review_a_rows = artifact_audit()
    universal_rows = universal_lattice_checks()
    for q in (2, 3, 4, 5, 7):
        verify_field(q)
    boxes = ([(2, d) for d in range(5)]
             + [(3, d) for d in range(4)]
             + [(4, d) for d in range(4)]
             + [(5, d) for d in range(3)]
             + [(7, d) for d in range(3)])
    rows = [audit_box(q, d) for q, d in boxes]

    print("P182_HOSTILE_REVIEW_B_DUAL_PROJECTIVE_EXACT_V1")
    print(f"frozen_main_tex_sha256={FROZEN_TEX}")
    print(f"frozen_round1_pdf_sha256={FROZEN_ROUND1}")
    print("representation=dual_projective_annihilator_flats")
    print("graph_method=algebraic_pointwise_classification")
    print("terminal_manifest_rows=19")
    print("terminal_lifecycle_checks_excluded_from_exact_assertions=4")
    print(f"author_manifest_rows={author_rows}")
    print(f"review_a_manifest_rows={review_a_rows}")
    for name, size, states, image in universal_rows:
        print(f"lattice={name} size={size} states={states} image={image}")
    for row in rows:
        if (row["q"], row["d"]) in {
            (2, 0), (2, 1), (2, 4), (3, 3), (4, 0), (4, 1), (4, 3),
            (5, 2), (7, 2),
        }:
            print(" ".join((
                f"q={row['q']}", f"d={row['d']}", f"L={row['L']}",
                f"states={row['states']}", f"image={row['image']}",
                f"fixed={row['fixed']}", f"cycles2={row['cycles2']}",
                f"depths={row['depths']}", f"fibres={row['fibres']}",
                f"kappa={row['kappa']}",
            )))
    print(f"boxes={len(rows)}")
    print("gf4_boxes=4")
    print(f"transitions={TRANSITIONS}")
    print(f"exact_assertions={ASSERTIONS}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("decision=ACCEPT_ROUND1_FOR_COORDINATOR_GATE")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
