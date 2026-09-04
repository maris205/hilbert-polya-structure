#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P184 Round 1.

This verifier never imports or executes the author or Review-A controls.  A
residue is represented by its least-significant-first base-p digit word, and
the update is performed as a single digit increment with carry at the
valuation-selected position.  Functional graphs are classified by indegree
peeling/reverse breadth-first search and recurrent cycles by union-find,
rather than author orbit tracing or Review A's valuation-by-valuation modular
predecessor solver.  Fibres are reconstructed from a digit grammar for the
low, middle, and high source strata.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
PAPER = REPO / "papers" / "184-co-gcd-translation-prime-powers"
REVIEW_A = (
    REPO
    / "docs"
    / "papers182_186_sequence"
    / "reviews"
    / "paper184"
    / "reviewer_A_rootspawn"
)

FROZEN = {
    # Core theorem source/PDF hashes remain the reviewed Round-1 bytes.  The
    # coordinator-authored lifecycle ledgers are rebound to the terminal
    # 19-row manifest without changing the mathematical attack route.
    "SHA256SUMS": "99f8d2883389d1451d7674b6ea6b2db13ec8040c156889e4ee4c7f87a47c3973",
    "README.md": "182670fd2631b7a7114d9f8b058731cb04e9c4f89318efd25b21110176ec81f2",
    "BUILD.md": "a200dec1936264bb1e2573a467415f3109fbfe5e5a9b5848793700dbedaa028d",
    "CLAIMS_EVIDENCE.md": "d2c1f887ec55fbb4ca6ee822d8828e99b82bd14470d9c2e1e91961c7fea6c02b",
    "FIGURE_PLAN.md": "6006e0a9df92af44ec2f28ab6126f9340161bd7a54353f7d1f260d89386c46ef",
    "NARRATIVE_REPORT.md": "40c1757fc0ea2236dd122d395d9a3a08774a2b988ba3e6d1ec9a47a7084497cb",
    "PAPER_PLAN.md": "a47894d689b323e83f45a79cd3e40a10117b0f6599813011576cb0db5ad33708",
    "PROOF_PACKAGE.md": "24083f2e1527e61db56879ffc045fa958e48cf690ee874dc45c65ffeaa30bed8",
    "SELF_QA.md": "a8873cbe30f96199183c25c94e0e94b8a91413972b7baa123359fe1c10df8b9d",
    "SOURCE_VERIFICATION.md": "679bb79b81e054a427f8355236aa2f48702504e9b492c7966caba3f88bd52a9e",
    "main.tex": "6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a",
    "references.bib": "3c1b98b55d0e6a6215f88e3182173254974b158ba34a0f744be3bf0c12769b66",
    "code/verify_p184.py": "7636127ed7eb4693aa5adb1dd7d68406b21d776299da7b7a64b71b866dbbe653",
    "code/CANONICAL.txt": "616f48c16bc1d335c658bcfded8b0b004b5dafdec79b77cb17a333ce3067acda",
    "main.pdf": "991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab",
    "main_round0_original.pdf": "991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab",
    "main_round1.pdf": "991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab",
}

FROZEN_REVIEW_A = {
    "verify_review_a_p184.py": "af90e6c979f82d933ee2080de70ff67438a10fd258630b0a50a627fdd0f8c558",
    "CANONICAL.txt": "59e65ef2dddeaca41b49eb0f2336ade903483e5161c3c89575cfb26d099d194f",
}

LIFECYCLE_MANIFEST_ROWS = frozenset(
    {"IMPROVEMENT_LOG.md", "FINAL_QA.md", "main_round1.pdf", "main_round2.pdf"}
)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)

    def require(self, condition: bool, message: str) -> None:
        """Hard-fail without extending the original scientific assertion census."""
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()
TRANSITION_DIGEST = sha256()
TOTAL_STATES = 0
TOTAL_TARGETS = 0

Digits = tuple[int, ...]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check_frozen_artifacts() -> None:
    for name, expected in FROZEN.items():
        AUDIT.check(digest(PAPER / name) == expected, f"frozen paper artifact changed: {name}")
    for name, expected in FROZEN_REVIEW_A.items():
        AUDIT.check(digest(REVIEW_A / name) == expected, f"Review-A context changed: {name}")

    payloads = [
        (PAPER / name).read_bytes()
        for name in ("main.pdf", "main_round0_original.pdf", "main_round1.pdf")
    ]
    AUDIT.check(payloads[0] == payloads[1] == payloads[2], "live/Round0/Round1 PDFs differ")

    manifest_rows = []
    for line in (PAPER / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        manifest_rows.append(name)
        valid = digest(PAPER / name) == expected
        if name in LIFECYCLE_MANIFEST_ROWS:
            AUDIT.require(valid, f"author lifecycle manifest mismatch: {name}")
        else:
            AUDIT.check(valid, f"author manifest mismatch: {name}")
    AUDIT.require(
        LIFECYCLE_MANIFEST_ROWS.issubset(manifest_rows),
        "terminal lifecycle manifest rows missing",
    )
    AUDIT.check(len(manifest_rows) == 19, "terminal author manifest row count changed")
    AUDIT.check("SHA256SUMS" not in manifest_rows, "author manifest is self-referential")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    for needle in (
        r"Let $p$ be a prime, $a\geq1$",
        r"\mu(x)=r+1",
        r"\lambda(x)=p^{h-s}",
        r"p^a-p^{\lfloor a/2\rfloor}",
        r"p^{\lfloor(a-1)/2\rfloor}",
        r"\#T^{-1}(y)",
        r"0/1/2",
        r"109,478",
        r"HOLD\_EXTERNAL",
    ):
        AUDIT.check(needle in source, f"manuscript contract missing: {needle}")
    for doi in (
        "10.1016/j.jalgebra.2008.09.029",
        "10.1515/9783110203011",
        "10.1016/j.jctb.2015.07.003",
    ):
        AUDIT.check(bibliography.count(doi) == 1, f"bibliography DOI mismatch: {doi}")

    cited_groups = re.findall(r"\\cite\{([^}]*)\}", source)
    cited = {key for group in cited_groups for key in group.split(",")}
    bib = set(re.findall(r"@(?:article|book)\{([^,]+),", bibliography))
    AUDIT.check(cited == bib, "citation/bibliography key mismatch")
    AUDIT.check(len(bib) == 3, "bibliography entry count changed")

    controls = {
        name: (PAPER / name).read_text(encoding="utf-8")
        for name in (
            "README.md",
            "BUILD.md",
            "CLAIMS_EVIDENCE.md",
            "PROOF_PACKAGE.md",
            "SELF_QA.md",
            "SOURCE_VERIFICATION.md",
            "code/CANONICAL.txt",
        )
    }
    for name in ("README.md", "BUILD.md", "CLAIMS_EVIDENCE.md", "SELF_QA.md", "code/CANONICAL.txt"):
        AUDIT.check("109478" in controls[name].replace(",", ""), f"assertion receipt mismatch: {name}")
    for name in ("README.md", "BUILD.md", "SOURCE_VERIFICATION.md", "code/CANONICAL.txt"):
        AUDIT.check("HOLD_EXTERNAL" in controls[name], f"lifecycle mismatch: {name}")
    for claim in (
        "tail and period formulas",
        "cycles by valuation",
        "tail censuses",
        "double- and empty-target atlases",
        "image defect",
    ):
        AUDIT.check(claim in controls["CLAIMS_EVIDENCE.md"], f"claim ledger omission: {claim}")


def to_digits(value: int, p: int, a: int) -> Digits:
    result = []
    for _ in range(a):
        result.append(value % p)
        value //= p
    AUDIT.check(value == 0, "digit conversion overflow")
    return tuple(result)


def to_int(digits: Digits, p: int) -> int:
    value = 0
    place = 1
    for digit in digits:
        AUDIT.check(0 <= digit < p, "invalid base-p digit")
        value += digit * place
        place *= p
    return value


def valuation_digits(digits: Digits) -> int:
    for position, digit in enumerate(digits):
        if digit:
            return position
    return len(digits)


def vp_integer(value: int, p: int, cap: int) -> int:
    if value == 0:
        return cap
    answer = 0
    while answer < cap and value % p == 0:
        answer += 1
        value //= p
    return answer


def add_unit_at(digits: Digits, p: int, position: int) -> Digits:
    if position == len(digits):
        return digits
    answer = list(digits)
    carry = 1
    while carry and position < len(answer):
        answer[position] += carry
        if answer[position] == p:
            answer[position] = 0
            position += 1
        else:
            carry = 0
    return tuple(answer)


def subtract_unit_at(digits: Digits, p: int, position: int) -> Digits:
    if position == len(digits):
        return digits
    answer = list(digits)
    borrow = 1
    while borrow and position < len(answer):
        if answer[position]:
            answer[position] -= 1
            borrow = 0
        else:
            answer[position] = p - 1
            position += 1
    return tuple(answer)


def digit_step(digits: Digits, p: int) -> Digits:
    a = len(digits)
    value = valuation_digits(digits)
    return add_unit_at(digits, p, a - value)


def predicted_point(digits: Digits, p: int) -> tuple[int, int]:
    a = len(digits)
    value = valuation_digits(digits)
    if 2 * value < a:
        return 0, p**value
    if 2 * value > a:
        return 1, p ** (a - value)
    h = a // 2
    unit = to_int(digits[h:], p)
    run = p - unit % p
    extra = vp_integer(unit + run, p, h)
    return run + 1, p ** (h - extra)


def is_double_digits(target: Digits, p: int) -> bool:
    a = len(target)
    one = (1,) + (0,) * (a - 1)
    if target == one:
        return True
    value = valuation_digits(target)
    if value < 1 or 2 * value >= a:
        return False
    return (
        target[value] == 1
        and all(target[position] == 0 for position in range(value + 1, a - value))
        and target[a - value] != 0
    )


def is_empty_digits(target: Digits, p: int) -> bool:
    a = len(target)
    h = a // 2
    if a % 2:
        return valuation_digits(target) > h
    return all(target[position] == 0 for position in range(h)) and target[h] == 1


def predicted_predecessors(target: Digits, p: int) -> frozenset[Digits]:
    a = len(target)
    h = a // 2
    value = valuation_digits(target)
    result: set[Digits] = set()

    # Unique predecessor from the invariant low stratum.
    if 2 * value < a:
        candidate = subtract_unit_at(target, p, a - value)
        AUDIT.check(valuation_digits(candidate) == value, "low inverse left its stratum")
        result.add(candidate)

    # Unique equality-layer predecessor for an even exponent, when its unit
    # coordinate predecessor remains a unit.
    if a % 2 == 0 and value >= h:
        coordinate = to_int(target[h:], p)
        previous = (coordinate - 1) % (p**h)
        if previous % p:
            result.add((0,) * h + to_digits(previous, p, h))

    # Unique strict-high predecessor of a nontrivial double target, or zero
    # as the second predecessor of target one.
    one = (1,) + (0,) * (a - 1)
    if target == one:
        result.add((0,) * a)
    elif is_double_digits(target, p):
        value = valuation_digits(target)
        result.add((0,) * (a - value) + target[a - value :])

    return frozenset(result)


def peel(successor: list[int]) -> tuple[list[int], list[bool], list[int]]:
    indegree = [0] * len(successor)
    reverse = [[] for _ in successor]
    for source, target in enumerate(successor):
        indegree[target] += 1
        reverse[target].append(source)
    residual = indegree.copy()
    alive = [True] * len(successor)
    queue = deque(i for i, degree in enumerate(residual) if degree == 0)
    while queue:
        source = queue.popleft()
        alive[source] = False
        target = successor[source]
        residual[target] -= 1
        if residual[target] == 0:
            queue.append(target)
    depth = [-1] * len(successor)
    queue = deque(i for i, flag in enumerate(alive) if flag)
    for vertex in queue:
        depth[vertex] = 0
    while queue:
        target = queue.popleft()
        for source in reverse[target]:
            if depth[source] < 0:
                depth[source] = depth[target] + 1
                queue.append(source)
    AUDIT.check(all(value >= 0 for value in depth), "reverse BFS left an unclassified state")
    return indegree, alive, depth


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left, right = self.find(left), self.find(right)
        if left == right:
            return
        if self.size[left] < self.size[right]:
            left, right = right, left
        self.parent[right] = left
        self.size[left] += self.size[right]


def expected_cycle_census(p: int, a: int) -> Counter[int]:
    return Counter(
        {
            p**value: (p - 1) * p ** (a - 2 * value - 1)
            for value in range(a)
            if 2 * value < a
        }
    )


def expected_tail_census(p: int, a: int) -> Counter[int]:
    result = Counter({0: p**a - p ** (a // 2)})
    if a % 2:
        result[1] = p ** (a // 2)
    else:
        for depth in range(1, p + 1):
            result[depth] = p ** (a // 2 - 1)
    return result


def author_rows() -> dict[tuple[int, int], tuple[int, int, int, tuple[int, int, int], Counter[int], Counter[int]]]:
    text = (PAPER / "code/CANONICAL.txt").read_text(encoding="utf-8")
    pattern = re.compile(
        r"p=(\d+) a=(\d+) N=(\d+) recurrent=(\d+) image=(\d+) "
        r"fibres_0_1_2=(\d+)/(\d+)/(\d+) tails=([^ ]+) cycles=([^\n]+)"
    )
    result = {}
    for match in pattern.finditer(text):
        p, a, modulus, recurrent, image, zero, one, two = map(int, match.group(1, 2, 3, 4, 5, 6, 7, 8))
        parse = lambda value: Counter(
            {int(key): int(count) for key, count in (piece.split(":") for piece in value.split(","))}
        )
        result[(p, a)] = (
            modulus,
            recurrent,
            image,
            (zero, one, two),
            parse(match.group(9)),
            parse(match.group(10)),
        )
    AUDIT.check(len(result) == 27, "author canonical carrier count changed")
    AUDIT.check("ASSERTIONS=109478" in text, "author assertion receipt changed")
    return result


def counter_text(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def verify_carrier(
    p: int,
    a: int,
    frozen_rows: dict[tuple[int, int], tuple[int, int, int, tuple[int, int, int], Counter[int], Counter[int]]],
) -> str:
    global TOTAL_STATES, TOTAL_TARGETS
    carrier = tuple(product(range(p), repeat=a))
    index = {state: position for position, state in enumerate(carrier)}
    modulus = p**a
    AUDIT.check(len(carrier) == modulus and len(index) == modulus, "digit carrier size")
    successor = [0] * modulus
    for source_position, source in enumerate(carrier):
        target = digit_step(source, p)
        target_position = index[target]
        successor[source_position] = target_position
        TRANSITION_DIGEST.update(
            f"{p}|{a}|{source_position}|{target_position}|{source}|{target}\n".encode()
        )
        source_integer = to_int(source, p)
        target_integer = to_int(target, p)
        value = valuation_digits(source)
        AUDIT.check(gcd(source_integer, modulus) == p**value, "digit valuation/gcd mismatch")
        AUDIT.check(
            target_integer == (source_integer + modulus // gcd(source_integer, modulus)) % modulus,
            "digit transition/literal map mismatch",
        )
        if 2 * value < a:
            AUDIT.check(valuation_digits(target) == value, "low stratum not invariant")
        elif 2 * value > a:
            AUDIT.check(valuation_digits(target) == a - value, "high stratum fall mismatch")
        else:
            h = a // 2
            unit = to_int(source[h:], p)
            AUDIT.check(
                to_int(target[h:], p) == (unit + 1) % (p**h),
                "middle conveyor mismatch",
            )

    reverse_sources = [[] for _ in carrier]
    for source, target in enumerate(successor):
        reverse_sources[target].append(source)
    indegree, alive, depth = peel(successor)
    union = UnionFind(modulus)
    for source, recurrent in enumerate(alive):
        if recurrent:
            AUDIT.check(alive[successor[source]], "recurrent successor escaped peeled core")
            union.union(source, successor[source])
    component_sizes = Counter()
    for source, recurrent in enumerate(alive):
        if recurrent:
            component_sizes[union.find(source)] += 1
    cycles = Counter(component_sizes.values())

    tails = Counter(depth)
    point_periods = []
    for source, state in enumerate(carrier):
        expected_tail, expected_period = predicted_point(state, p)
        AUDIT.check(depth[source] == expected_tail, "pointwise tail formula")
        recurrent = source
        for _ in range(depth[source]):
            recurrent = successor[recurrent]
        period = component_sizes[union.find(recurrent)]
        AUDIT.check(period == expected_period, "pointwise eventual-period formula")
        point_periods.append(period)

    expected_tails = expected_tail_census(p, a)
    expected_cycles = expected_cycle_census(p, a)
    AUDIT.check(tails == expected_tails, "complete tail census")
    AUDIT.check(cycles == expected_cycles, "complete cycle census")
    recurrent_count = sum(alive)
    AUDIT.check(recurrent_count == modulus - p ** (a // 2), "recurrent population")
    AUDIT.check(max(tails) == (1 if a % 2 else p), "sharp maximum tail")

    defect = p ** ((a - 1) // 2)
    doubles = set()
    empties = set()
    fibre_hist = Counter()
    image = set(successor)
    for target_position, target in enumerate(carrier):
        is_double = is_double_digits(target, p)
        is_empty = is_empty_digits(target, p)
        AUDIT.check(not (is_double and is_empty), "double/empty target overlap")
        doubles.add(target_position) if is_double else None
        empties.add(target_position) if is_empty else None
        predicted = predicted_predecessors(target, p)
        actual = frozenset(carrier[source] for source in reverse_sources[target_position])
        AUDIT.check(predicted == actual, "every-target exact predecessor set")
        expected_size = 0 if is_empty else 2 if is_double else 1
        AUDIT.check(len(actual) == expected_size, "every-target 0/1/2 atlas")
        AUDIT.check(indegree[target_position] == expected_size, "indegree/predecessor mismatch")
        fibre_hist[expected_size] += 1
    AUDIT.check(len(doubles) == defect, "double-target count")
    AUDIT.check(len(empties) == defect, "empty-target count")
    AUDIT.check(doubles.isdisjoint(empties), "double/empty sets not disjoint")
    AUDIT.check(
        fibre_hist == Counter({0: defect, 1: modulus - 2 * defect, 2: defect}),
        "full fibre histogram",
    )
    AUDIT.check(sum(size * count for size, count in fibre_hist.items()) == modulus, "fibre mass")
    AUDIT.check(image == set(range(modulus)) - empties, "exact image complement")
    AUDIT.check(len(image) == modulus - defect, "image defect")

    zero = (0,) * a
    one = (1,) + (0,) * (a - 1)
    AUDIT.check(digit_step(zero, p) == one and digit_step(one, p) == one, "zero-to-one boundary")
    if a == 1:
        AUDIT.check(tails == Counter({0: p - 1, 1: 1}), "a=1 tail boundary")
        AUDIT.check(doubles == {index[one]} and empties == {index[zero]}, "a=1 fibre boundary")
    if a % 2 == 0:
        h = a // 2
        last_middle = (0,) * h + to_digits(p**h - 1, p, h)
        AUDIT.check(digit_step(last_middle, p) == zero, "middle landing-at-zero boundary")
        AUDIT.check(depth[index[last_middle]] == 2, "middle landing exact tail")
        if p == 2:
            AUDIT.check(
                all(depth[position] == 2 for position, state in enumerate(carrier) if valuation_digits(state) == h),
                "binary middle-layer tail boundary",
            )

    observed = (
        modulus,
        recurrent_count,
        len(image),
        (fibre_hist[0], fibre_hist[1], fibre_hist[2]),
        tails,
        cycles,
    )
    if (p, a) in frozen_rows:
        AUDIT.check(observed == frozen_rows[(p, a)], "author/Review-B canonical-row mismatch")

    TOTAL_STATES += modulus
    TOTAL_TARGETS += modulus
    return (
        f"p={p} a={a} N={modulus} recurrent={recurrent_count} image={len(image)} "
        f"fibres_0_1_2={fibre_hist[0]}/{fibre_hist[1]}/{fibre_hist[2]} "
        f"tails={counter_text(tails)} cycles={counter_text(cycles)}"
    )


def prime_controls() -> tuple[tuple[int, int], ...]:
    cases = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        a = 1
        while p**a <= 30000:
            cases.append((p, a))
            a += 1
    return tuple(cases)


def main() -> None:
    before = AUDIT.assertions
    check_frozen_artifacts()
    frozen_rows = author_rows()
    cases = prime_controls()
    AUDIT.check(len(cases) == 48, "review carrier count")
    print("P184_HOSTILE_REVIEW_B_COMBINATORIAL_EXACT_V1")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print("representation=least_significant_first_base_p_digit_words")
    print("graph_method=indegree_peeling_reverse_bfs_plus_union_find_cycles")
    print("inverse_method=low_middle_high_digit_grammar")
    print("terminal_manifest_rows=19")
    print("lifecycle_manifest_checks_excluded_from_assertion_census=4")
    print(f"artifact_assertions={AUDIT.assertions-before}")
    selected = {
        (2, 1), (2, 2), (2, 14), (3, 4), (3, 9), (5, 4), (7, 4),
        (11, 4), (13, 4), (17, 2), (17, 3), (19, 2), (19, 3),
    }
    for p, a in cases:
        start = AUDIT.assertions
        row = verify_carrier(p, a, frozen_rows)
        if (p, a) in selected:
            print(f"{row} assertions={AUDIT.assertions-start}")
    print(f"carriers={len(cases)}")
    print("primes=2,3,5,7,11,13,17,19")
    print("new_prime_controls=17,19")
    print(f"states={TOTAL_STATES}")
    print(f"targets={TOTAL_TARGETS}")
    print(f"exact_assertions={AUDIT.assertions}")
    print(f"review_transition_digest={TRANSITION_DIGEST.hexdigest()}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("decision=ACCEPT_ROUND1_FOR_COORDINATOR_GATE")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
