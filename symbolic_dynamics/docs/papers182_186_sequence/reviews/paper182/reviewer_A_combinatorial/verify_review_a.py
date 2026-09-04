#!/usr/bin/env python3
"""Process-separated hostile exact audit for frozen P182 Round 0.

This reviewer does not import or execute the author's verifier.  Subspaces
are generated as closure-stable bitsets of vectors rather than canonical RREF
rows.  Functional graphs are classified by indegree peeling rather than
forward orbit tracing.  GF(4) is implemented as F_2[x]/(x^2+x+1), providing
a non-prime-field control for the manuscript's prime-power quantifier.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
PAPER = REPO / "papers" / "182-cyclic-subspace-lattice-comparator"

FROZEN = {
    # The theorem source/PDF hashes below remain the original Review-A input.
    # Coordinator-authored lifecycle ledgers and their manifest are rebound to
    # the terminal 19-row package; this changes no mathematical check.
    "SHA256SUMS": "d52c6ad0132f46629db38ebab0a6a480bcba5c5489f018430a43a7d54cabc9ec",
    "README.md": "9bee59e5b9100ecb363c10797d8b18219e9f1c2734b03f0f6bf03d9a73ee917c",
    "BUILD.md": "324bff3a90d05ab1c935012c698eaf33ebfc84da53bfd48400b978c3d20827f1",
    "CLAIMS_EVIDENCE.md": "81316dc42385b2f6dc9152a78e656d9df57928b9492a2f3782787653cea9619d",
    "FIGURE_PLAN.md": "67db3862490a215f04d0b98073ddfb0bbb1496ef510f2cb8dc1f803834819300",
    "NARRATIVE_REPORT.md": "cede4fce3c01bf363555794e1ca77090e2a52d46301060686185e06db1a2945e",
    "PAPER_PLAN.md": "9ff55da6d7a7ece2577281d2ab63e45bcb06f83104156729a9182d393faebd5b",
    "PROOF_PACKAGE.md": "84d88299f320802f99c284aa40d4110bafc576ebaf67ce332df50be4ae00cb9a",
    "SELF_QA.md": "26c187397a980b86bd0143056401209a960677c77ec921fb3379d89ba6760007",
    "SOURCE_VERIFICATION.md": "47c49520b581b5d6e300bd287ef4e7735656433dfaf97a1303b0a9b18825d228",
    "main.tex": "9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7",
    "main_round0_original.pdf": "880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07",
    "main.pdf": "880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07",
    "references.bib": "5df2e5a1ab48171c72c47f261555d0bbc760b8b55dfa0e271fde59b70b6bc04c",
    "code/verify_p182.py": "e97458b102d00b726594b3b191353b7d44098406bd7e8bffb2f1dac5b83a4348",
    "code/CANONICAL.txt": "993df5e5a286ff4ce42d28c36f417a57b1d212ebdcfd7345524a6498a3ace5e0",
}

# These four terminal lifecycle receipts were appended after the scientific
# Review-A census was frozen.  They remain hard-fail bindings, but are kept
# outside the original exact-assertion counter so that expanding the paper
# manifest cannot recursively change the scientific receipt.
TERMINAL_LIFECYCLE_ROWS = frozenset({
    "IMPROVEMENT_LOG.md",
    "FINAL_QA.md",
    "main_round1.pdf",
    "main_round2.pdf",
})


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()
DIGEST = sha256()
TRANSITIONS = 0


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def field_add(q: int, a: int, b: int) -> int:
    return a ^ b if q == 4 else (a + b) % q


def field_mul(q: int, a: int, b: int) -> int:
    if q != 4:
        return (a * b) % q
    # Polynomial basis modulo x^2+x+1 (binary 111).
    answer = 0
    left, right = a, b
    while right:
        if right & 1:
            answer ^= left
        right >>= 1
        left <<= 1
        if left & 0b100:
            left ^= 0b111
    return answer & 0b11


def verify_field(q: int) -> None:
    for a, b, c in product(range(q), repeat=3):
        AUDIT.check(field_add(q, a, b) == field_add(q, b, a), "field add commutativity")
        AUDIT.check(field_mul(q, a, b) == field_mul(q, b, a), "field mul commutativity")
        AUDIT.check(
            field_add(q, field_add(q, a, b), c)
            == field_add(q, a, field_add(q, b, c)),
            "field add associativity",
        )
        AUDIT.check(
            field_mul(q, field_mul(q, a, b), c)
            == field_mul(q, a, field_mul(q, b, c)),
            "field mul associativity",
        )
        AUDIT.check(
            field_mul(q, a, field_add(q, b, c))
            == field_add(q, field_mul(q, a, b), field_mul(q, a, c)),
            "field distributivity",
        )
    for a in range(q):
        AUDIT.check(field_add(q, a, 0) == a, "field additive identity")
        AUDIT.check(field_mul(q, a, 1) == a, "field multiplicative identity")
        AUDIT.check(any(field_add(q, a, b) == 0 for b in range(q)), "field additive inverse")
        if a:
            AUDIT.check(any(field_mul(q, a, b) == 1 for b in range(1, q)), "field inverse")


def encode(vector: tuple[int, ...], q: int) -> int:
    answer = 0
    scale = 1
    for entry in vector:
        answer += entry * scale
        scale *= q
    return answer


def decode(value: int, q: int, d: int) -> tuple[int, ...]:
    answer = []
    for _ in range(d):
        answer.append(value % q)
        value //= q
    return tuple(answer)


def members(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def gaussian(n: int, k: int, q: int) -> int:
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for j in range(k):
        numerator *= q ** (n - j) - 1
        denominator *= q ** (k - j) - 1
    AUDIT.check(numerator % denominator == 0, "Gaussian integrality")
    return numerator // denominator


def galois(n: int, q: int) -> int:
    return sum(gaussian(n, k, q) for k in range(n + 1))


@dataclass(frozen=True)
class Geometry:
    q: int
    d: int
    vectors: tuple[tuple[int, ...], ...]
    spaces: tuple[int, ...]
    rank: tuple[int, ...]
    meet: tuple[tuple[int, ...], ...]
    join: tuple[tuple[int, ...], ...]
    zero: int
    whole: int


@lru_cache(maxsize=None)
def geometry(q: int, d: int) -> Geometry:
    vectors = tuple(decode(i, q, d) for i in range(q**d))
    nvec = len(vectors)
    add = [[0] * nvec for _ in range(nvec)]
    scalar = [[0] * nvec for _ in range(q)]
    for i, x in enumerate(vectors):
        for j, y in enumerate(vectors):
            add[i][j] = encode(
                tuple(field_add(q, a, b) for a, b in zip(x, y)), q
            )
        for coefficient in range(q):
            scalar[coefficient][i] = encode(
                tuple(field_mul(q, coefficient, a) for a in x), q
            )

    extension_cache: dict[tuple[int, int], int] = {}

    def extend(mask: int, vector: int) -> int:
        key = (mask, vector)
        if key not in extension_cache:
            output = 0
            multiples = [scalar[a][vector] for a in range(q)]
            for old in members(mask):
                for multiple in multiples:
                    output |= 1 << add[old][multiple]
            extension_cache[key] = output
        return extension_cache[key]

    seen = {1}  # the zero vector alone
    queue = deque([1])
    while queue:
        mask = queue.popleft()
        for vector in range(1, nvec):
            if not (mask >> vector & 1):
                enlarged = extend(mask, vector)
                if enlarged not in seen:
                    seen.add(enlarged)
                    queue.append(enlarged)

    powers = {q**r: r for r in range(d + 1)}
    spaces = tuple(sorted(seen, key=lambda mask: (powers[mask.bit_count()], mask)))
    ranks = tuple(powers[mask.bit_count()] for mask in spaces)
    index = {mask: i for i, mask in enumerate(spaces)}
    full_mask = (1 << nvec) - 1
    AUDIT.check(len(spaces) == galois(d, q), "closure enumeration/Galois mismatch")
    AUDIT.check(1 in index and full_mask in index, "missing zero or whole space")
    for mask, rank in zip(spaces, ranks):
        AUDIT.check(mask & 1 == 1, "subspace omitted zero")
        AUDIT.check(mask.bit_count() == q**rank, "subspace cardinality/rank mismatch")
        elems = tuple(members(mask))
        for a in range(q):
            for x in elems:
                AUDIT.check(mask >> scalar[a][x] & 1, "scalar closure failed")
        for x in elems:
            for y in elems:
                AUDIT.check(mask >> add[x][y] & 1, "additive closure failed")

    meet = [[0] * len(spaces) for _ in spaces]
    join = [[0] * len(spaces) for _ in spaces]
    for i, left in enumerate(spaces):
        for j, right in enumerate(spaces):
            intersection = left & right
            AUDIT.check(intersection in index, "intersection absent from closure catalogue")
            meet[i][j] = index[intersection]
            span_mask = left
            for vector in members(right):
                if not (span_mask >> vector & 1):
                    span_mask = extend(span_mask, vector)
            AUDIT.check(span_mask in index, "join absent from closure catalogue")
            join[i][j] = index[span_mask]
            AUDIT.check(left & ~span_mask == 0 and right & ~span_mask == 0, "join containment")
            AUDIT.check(
                ranks[i] + ranks[j] == ranks[meet[i][j]] + ranks[join[i][j]],
                "subspace modular rank identity",
            )

    return Geometry(
        q=q,
        d=d,
        vectors=vectors,
        spaces=spaces,
        rank=ranks,
        meet=tuple(tuple(row) for row in meet),
        join=tuple(tuple(row) for row in join),
        zero=index[1],
        whole=index[full_mask],
    )


def contained(g: Geometry, i: int, j: int) -> bool:
    return g.spaces[i] & ~g.spaces[j] == 0


def kappa_formula(k: int, q: int) -> int:
    return sum(gaussian(k, a, q) * q ** (a * (k - a)) for a in range(k + 1))


def q_pairs_formula(n: int, q: int) -> int:
    return sum(
        gaussian(n, a, q)
        * gaussian(n - a, s, q)
        * q ** (a * s)
        for a in range(n + 1)
        for s in range(n - a + 1)
    )


def counter_text(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def peel_graph(successor: list[int]):
    indegree = [0] * len(successor)
    reverse = [[] for _ in successor]
    for source, target in enumerate(successor):
        indegree[target] += 1
        reverse[target].append(source)
    residual = indegree.copy()
    queue = deque(i for i, value in enumerate(residual) if value == 0)
    alive = [True] * len(successor)
    while queue:
        vertex = queue.popleft()
        alive[vertex] = False
        target = successor[vertex]
        residual[target] -= 1
        if residual[target] == 0:
            queue.append(target)
    recurrent = [i for i, flag in enumerate(alive) if flag]
    depth = [-1] * len(successor)
    queue = deque(recurrent)
    for vertex in recurrent:
        depth[vertex] = 0
    while queue:
        target = queue.popleft()
        for source in reverse[target]:
            if depth[source] < 0:
                depth[source] = depth[target] + 1
                queue.append(source)
    AUDIT.check(all(value >= 0 for value in depth), "peeling left an unclassified state")
    cycles = Counter()
    visited = set()
    for start in recurrent:
        if start in visited:
            continue
        current = start
        length = 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = successor[current]
        cycles[length] += 1
    return indegree, alive, depth, cycles


def parse_counter(text: str) -> Counter[int]:
    return Counter({int(k): int(v) for k, v in (piece.split(":") for piece in text.split(","))})


def author_rows() -> dict[tuple[int, int], tuple[int, int, int, Counter[int], Counter[int], Counter[int]]]:
    rows = {}
    pattern = re.compile(
        r"q=(\d+) d=(\d+) L=(\d+) states=(\d+) image=(\d+) "
        r"cycles=([^ ]+) depths=([^ ]+) fibres=([^\n]+)"
    )
    text = (PAPER / "code/CANONICAL.txt").read_text(encoding="utf-8")
    for match in pattern.finditer(text):
        q, d, size, states, image = map(int, match.group(1, 2, 3, 4, 5))
        rows[(q, d)] = (
            size,
            states,
            image,
            parse_counter(match.group(6)),
            parse_counter(match.group(7)),
            parse_counter(match.group(8)),
        )
    AUDIT.check(len(rows) == 15, "author canonical row count changed")
    AUDIT.check("exact_assertions=1667850" in text, "author assertion receipt changed")
    AUDIT.check("transitions=328700" in text, "author transition receipt changed")
    return rows


def check_frozen_artifacts() -> None:
    for name, expected in FROZEN.items():
        AUDIT.check(digest(PAPER / name) == expected, f"frozen hash changed: {name}")

    # Validate the author's non-self-referential receipt rather than trusting
    # its presence.  Its own frozen hash is bound above.
    manifest_rows = []
    for line in (PAPER / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        manifest_rows.append(name)
        matches = digest(PAPER / name) == expected
        if name in TERMINAL_LIFECYCLE_ROWS:
            if not matches:
                raise AssertionError(f"terminal lifecycle manifest mismatch: {name}")
        else:
            AUDIT.check(matches, f"author manifest mismatch: {name}")
    AUDIT.check(len(manifest_rows) == 19, "terminal author manifest row count changed")
    AUDIT.check("SHA256SUMS" not in manifest_rows, "author manifest is self-referential")
    if not TERMINAL_LIFECYCLE_ROWS.issubset(manifest_rows):
        raise AssertionError("terminal lifecycle manifest rows missing")

    AUDIT.check(
        (PAPER / "main.pdf").read_bytes() == (PAPER / "main_round0_original.pdf").read_bytes(),
        "live and Round-0 PDF differ",
    )
    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    for needle in (
        r"For every prime power $q$ and every $d\ge0$",
        r"T^4=T^2",
        r"\kappa_0<\kappa_1<\cdots<\kappa_d",
        r"g_d^3-g_d\alpha_d",
        r"$328{,}700$ transitions",
        r"$1{,}667{,}850$ explicit",
    ):
        AUDIT.check(needle in source, f"manuscript contract missing: {needle}")
    for doi in (
        "10.1002/sapm1970493239",
        "10.1007/s00500-019-03866-y",
        "10.1016/j.aam.2022.102362",
        "10.1007/s10801-023-01294-8",
    ):
        AUDIT.check(bibliography.count(doi) == 1, f"bibliography DOI mismatch: {doi}")

    # Attack the manuscript/control/source receipt consistency explicitly.
    controls = {
        name: (PAPER / name).read_text(encoding="utf-8")
        for name in (
            "README.md",
            "BUILD.md",
            "CLAIMS_EVIDENCE.md",
            "PROOF_PACKAGE.md",
            "SELF_QA.md",
            "SOURCE_VERIFICATION.md",
        )
    }
    for name in ("README.md", "BUILD.md", "CLAIMS_EVIDENCE.md"):
        AUDIT.check("328700" in controls[name].replace(",", ""), f"transition receipt mismatch: {name}")
    for name in ("README.md", "CLAIMS_EVIDENCE.md", "SELF_QA.md", "SOURCE_VERIFICATION.md"):
        AUDIT.check("HOLD_EXTERNAL" in controls[name], f"external lifecycle mismatch: {name}")
    for claim in ("T^4=T^2", "every target fibre", "complete fibre histogram"):
        AUDIT.check(claim in controls["CLAIMS_EVIDENCE.md"], f"claim ledger omission: {claim}")
    cited_keys = set(re.findall(r"\\cite\{([^}]*)\}", source))
    cited_keys = {key for group in cited_keys for key in group.split(",")}
    bib_keys = set(re.findall(r"@(?:book|article)\{([^,]+),", bibliography))
    AUDIT.check(cited_keys == bib_keys, "citation/bibliography key mismatch")
    AUDIT.check(len(bib_keys) == 5, "bibliography entry count changed")


def check_complements(q: int, d: int) -> None:
    for k in range(d + 1):
        g = geometry(q, k)
        by_first_rank = Counter()
        total = 0
        for i in range(len(g.spaces)):
            count = 0
            for j in range(len(g.spaces)):
                if g.meet[i][j] == g.zero and g.join[i][j] == g.whole:
                    count += 1
            AUDIT.check(
                count == q ** (g.rank[i] * (k - g.rank[i])),
                "fixed-subspace complement count",
            )
            by_first_rank[g.rank[i]] += count
            total += count
        expected_by_rank = Counter(
            {
                a: gaussian(k, a, q) * q ** (a * (k - a))
                for a in range(k + 1)
            }
        )
        AUDIT.check(by_first_rank == expected_by_rank, "ranked complement census")
        AUDIT.check(total == kappa_formula(k, q), "total complement census")


def check_box(q: int, d: int, frozen_rows) -> str:
    global TRANSITIONS
    g = geometry(q, d)
    size = len(g.spaces)
    carrier = size**3

    def pack(a: int, b: int, c: int) -> int:
        return (a * size + b) * size + c

    def unpack(value: int) -> tuple[int, int, int]:
        c = value % size
        value //= size
        b = value % size
        return value // size, b, c

    successor = [0] * carrier
    predicted_depth = [0] * carrier
    predicted_recurrent = [False] * carrier
    for source in range(carrier):
        a, b, c = unpack(source)
        target = pack(c, g.meet[a][b], g.join[a][b])
        successor[source] = target
        TRANSITIONS += 1
        DIGEST.update(f"{q}|{d}|{source}|{target}\n".encode())
        recurrent = contained(g, b, a) and contained(g, b, c)
        predicted_recurrent[source] = recurrent
        predicted_depth[source] = (
            0 if recurrent else 1 if contained(g, g.meet[a][b], c) else 2
        )

    for source in range(carrier):
        a, b, c = unpack(source)
        square = successor[successor[source]]
        expected_square = pack(
            g.join[a][b],
            g.meet[c][g.meet[a][b]],
            g.join[c][g.meet[a][b]],
        )
        AUDIT.check(square == expected_square, "literal square identity")
        AUDIT.check(successor[successor[square]] == square, "literal T^4=T^2")

    indegree, alive, depth, cycles = peel_graph(successor)
    AUDIT.check(alive == predicted_recurrent, "peeled recurrent set/predicate mismatch")
    AUDIT.check(depth == predicted_depth, "peeled depth/predicate mismatch")
    AUDIT.check(all(length in (1, 2) for length in cycles), "period outside 1,2")
    fixed = sum(successor[i] == i for i in range(carrier))
    recurrent = sum(alive)
    image = sum(value > 0 for value in indegree)
    depths = Counter(depth)
    fibres = Counter(indegree)

    interval_count = 0
    direct_image_targets = 0
    kappa = [kappa_formula(k, q) for k in range(d + 1)]
    AUDIT.check(all(kappa[k] < kappa[k + 1] for k in range(d)), "strict kappa growth")
    actual_maximizers = []
    actual_min_positive = []
    for target in range(carrier):
        c, middle, top = unpack(target)
        reachable = contained(g, middle, top)
        AUDIT.check((indegree[target] > 0) == reachable, "complete image predicate")
        if reachable:
            direct_image_targets += 1
            quotient_rank = g.rank[top] - g.rank[middle]
            AUDIT.check(indegree[target] == kappa[quotient_rank], "every-target fibre")
        else:
            AUDIT.check(indegree[target] == 0, "unreachable target has predecessor")
        if indegree[target] == max(kappa):
            actual_maximizers.append((c, middle, top))
        if indegree[target] == 1:
            actual_min_positive.append((c, middle, top))
    for middle in range(size):
        for top in range(size):
            interval_count += int(contained(g, middle, top))
    AUDIT.check(direct_image_targets == size * interval_count, "direct image count")
    AUDIT.check(
        actual_maximizers == [(c, g.zero, g.whole) for c in range(size)],
        "complete maximum-fibre target set",
    )
    AUDIT.check(
        actual_min_positive
        == [(c, middle, middle) for c in range(size) for middle in range(size)],
        "complete minimum-positive-fibre target set",
    )

    alpha = sum(gaussian(d, b, q) * galois(d - b, q) for b in range(d + 1))
    rho = sum(
        gaussian(d, b, q) * galois(d - b, q) ** 2 for b in range(d + 1)
    )
    q_values = [q_pairs_formula(n, q) for n in range(d + 1)]
    eta = sum(
        gaussian(d, m, q) * q_values[d - m] * galois(d - m, q)
        for m in range(d + 1)
    )
    predicted_hist = Counter({0: carrier - size * alpha})
    for k in range(d + 1):
        targets = size * sum(
            gaussian(d, m, q) * gaussian(d - m, k, q)
            for m in range(d - k + 1)
        )
        predicted_hist[kappa[k]] += targets
    predicted_hist += Counter()

    AUDIT.check(size == galois(d, q), "Galois carrier factor")
    AUDIT.check(interval_count == alpha, "interval/fixed formula")
    AUDIT.check(fixed == alpha, "fixed formula")
    AUDIT.check(recurrent == rho, "recurrent formula")
    AUDIT.check(image == size * alpha, "image formula")
    AUDIT.check(cycles == Counter({1: alpha, 2: (rho - alpha) // 2}), "cycle formula")
    AUDIT.check(depths == Counter({0: rho, 1: eta - rho, 2: carrier - eta}), "depth partition")
    AUDIT.check(fibres == predicted_hist, "complete fibre histogram")
    AUDIT.check(sum(indegree) == carrier, "fibre mass")
    if d == 0:
        AUDIT.check(depths == Counter({0: 1}), "d=0 boundary")
        AUDIT.check(kappa == [1], "d=0 complement boundary")
    else:
        AUDIT.check(depths[2] > 0 and max(depths) == 2, "sharp height two")

    # Direct disjoint-pair enumeration attacks Q_n independently.
    direct_disjoint = sum(
        1 for left in range(size) for right in range(size)
        if g.meet[left][right] == g.zero
    )
    AUDIT.check(direct_disjoint == q_values[d], "direct disjoint-pair/Q formula")
    check_complements(q, d)

    key = (q, d)
    if key in frozen_rows:
        expected = frozen_rows[key]
        observed = (size, carrier, image, cycles, depths, fibres)
        AUDIT.check(observed == expected, "author canonical/reviewer representation mismatch")

    return (
        f"q={q} d={d} L={size} states={carrier} image={image} fixed={fixed} "
        f"cycles={counter_text(cycles)} depths={counter_text(depths)} "
        f"fibres={counter_text(fibres)} kappa={','.join(map(str, kappa))}"
    )


def main() -> None:
    before = AUDIT.assertions
    check_frozen_artifacts()
    frozen_rows = author_rows()
    print("P182_HOSTILE_REVIEW_A_COMBINATORIAL_EXACT_V1")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round0_pdf_sha256={FROZEN['main_round0_original.pdf']}")
    print("representation=closure_generated_vector_bitsets")
    print("graph_method=indegree_peeling_reverse_bfs")
    print("terminal_manifest_rows=19")
    print("terminal_lifecycle_checks_excluded_from_exact_assertions=4")
    print(f"artifact_assertions={AUDIT.assertions-before}")

    boxes = [
        *((2, d) for d in range(5)),
        *((3, d) for d in range(4)),
        *((4, d) for d in range(4)),
        *((5, d) for d in range(3)),
    ]
    for q in sorted({q for q, _ in boxes}):
        verify_field(q)
    for q, d in boxes:
        start = AUDIT.assertions
        row = check_box(q, d, frozen_rows)
        print(f"{row} assertions={AUDIT.assertions-start}")
    print(f"boxes={len(boxes)}")
    print(f"gf4_boxes={sum(q == 4 for q, _ in boxes)}")
    print(f"transitions={TRANSITIONS}")
    print(f"exact_assertions={AUDIT.assertions}")
    print(f"review_transition_digest={DIGEST.hexdigest()}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("decision=ACCEPT_ROUND0_FOR_COORDINATOR_GATE")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
