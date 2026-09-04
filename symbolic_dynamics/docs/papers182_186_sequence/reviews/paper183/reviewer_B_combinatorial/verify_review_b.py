#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P183 Round 1.

This program does not import or execute the author or Review-A verifiers.
States are immutable relations (frozensets of directed arcs), rather than the
author's global bit integer or Review A's four-state unordered-pair tuples.
Time-t kernels are propagated by weighted dynamic programming; exact-support
weights are computed by inclusion-exclusion, rather than literal word
enumeration or direct set-partition generation.  Recurrent classes are found
by a full strongly-connected-component decomposition.  One-step inverse
families are constructed star-by-star from each target.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
PAPER = REPO / "papers" / "183-random-incoming-copy-symmetrization"
REVIEW_A = (
    REPO
    / "docs"
    / "papers182_186_sequence"
    / "reviews"
    / "paper183"
    / "reviewer_A_rootspawn"
)

FROZEN = {
    # Core theorem source/PDF hashes remain the reviewed Round-1 bytes.  The
    # coordinator-authored lifecycle ledgers are rebound to the terminal
    # 19-row manifest without changing the mathematical attack route.
    "SHA256SUMS": "16ea9d16325f0d371c8e43650925d9f0665e1fb93817577ed394d085cdf25ffb",
    "README.md": "3416870cdd08b5ca5b6089cff576572cfeb6627b3d05cc6906f9d098d47e37ad",
    "BUILD.md": "fa1103ab47adeac7c3aa3787256913abe3c16fbd1b874f0094802e298ed5cd15",
    "CLAIMS_EVIDENCE.md": "9ef928b660d6534a77e338c73efb0029b9706a3a43c9f746a33b6c43f394ea2c",
    "FIGURE_PLAN.md": "16ba3109d735aca0a38bf05c75bba0e4eae209c4f67976669afd133a52d3a769",
    "NARRATIVE_REPORT.md": "facab6035f1a2896348b64da8aaeac79221770d279f00f2cfd444c128e661c99",
    "PAPER_PLAN.md": "d714397a01d79a70fb3f6d1a0cc57c24df53bdee95e3e24ba2db9aade0d78991",
    "PROOF_PACKAGE.md": "0c42bf1eea2018e8a0b3032d482c44364660656ad88b42a59cf84d2e58b7194c",
    "SELF_QA.md": "a50f22bc22f497681174ae5b86d09c77ba1bfc3a8b1082ab0da547282214c4f8",
    "SOURCE_VERIFICATION.md": "2fa335bde3c168d0f1386006b451b8779dc58838036a0b14b2e96c717564c8e6",
    "main.tex": "9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678",
    "references.bib": "5b5f0fe2b7e78176d097ab2e919d35954adffff824528b999847be791038912d",
    "code/verify_p183.py": "a7c56aa48783eae09e44a7df39f34109a891d33ac6a11e9b86e4fd22cdfdd472",
    "code/CANONICAL.txt": "f21652d061f409a0833be4900d6cbafee6a034b3121a03750984073893c2dea1",
    "main.pdf": "6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b",
    "main_round0_original.pdf": "6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b",
    "main_round1.pdf": "6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b",
}

FROZEN_REVIEW_A = {
    "verify_review_a_p183.py": "77be19418db725275a6bf3364877021ff1ec8ff163f65fe9390675661a521c38",
    "CANONICAL.txt": "c7054f4d5ed8a317eb0a1f9761aa781b7498fd706ba7603aae66930b7a9baaf4",
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
ACTION_TRANSITIONS = 0
KERNEL_ROWS = 0
VIRTUAL_HISTORY_MASS = 0

Arc = tuple[int, int]
State = frozenset[Arc]


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
        r"Fix $n\geq1$",
        r"\Pr_A(\tau\leq t)",
        r"N_t(A,B)",
        r"\Stir{t}{|S|}",
        r"k(B)2^{n-1}",
        r"1+k(B)(2^{n-1}-1)",
        r"47,033",
        r"HOLD\_EXTERNAL",
    ):
        AUDIT.check(needle in source, f"manuscript contract missing: {needle}")
    for doi in (
        "10.1023/A:1007822931408",
        "10.1016/j.physa.2015.12.008",
        "10.1093/comnet/cnad031",
    ):
        AUDIT.check(bibliography.count(doi) == 1, f"bibliography DOI mismatch: {doi}")

    cited_groups = re.findall(r"\\cite\{([^}]*)\}", source)
    cited = {key for group in cited_groups for key in group.split(",")}
    bib = set(re.findall(r"@article\{([^,]+),", bibliography))
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
        AUDIT.check("47033" in controls[name].replace(",", ""), f"assertion receipt mismatch: {name}")
    for name in ("README.md", "BUILD.md", "SOURCE_VERIFICATION.md", "code/CANONICAL.txt"):
        AUDIT.check("HOLD_EXTERNAL" in controls[name], f"lifecycle mismatch: {name}")
    for claim in (
        "conflict-star deletion",
        "independent-set absorption CDF",
        "first-occurrence-order endpoint kernel",
        "distinct predecessor-state count",
    ):
        AUDIT.check(claim in controls["CLAIMS_EVIDENCE.md"], f"claim ledger omission: {claim}")


@lru_cache(maxsize=None)
def arcs(n: int) -> tuple[Arc, ...]:
    return tuple((i, j) for i in range(n) for j in range(n) if i != j)


@lru_cache(maxsize=None)
def undirected_pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


@lru_cache(maxsize=None)
def states(n: int) -> tuple[State, ...]:
    carrier = arcs(n)
    answer = []
    for size in range(len(carrier) + 1):
        answer.extend(frozenset(chosen) for chosen in combinations(carrier, size))
    return tuple(answer)


def state_text(state: State) -> str:
    return ",".join(f"{i}>{j}" for i, j in sorted(state)) or "-"


def act(state: State, n: int, vertex: int) -> State:
    kept = {edge for edge in state if edge[0] != vertex}
    copied = {
        (vertex, other)
        for other in range(n)
        if other != vertex and (other, vertex) in state
    }
    return frozenset(kept | copied)


def conflicts(state: State, n: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i, j in undirected_pairs(n)
        if ((i, j) in state) != ((j, i) in state)
    )


def isolated_vertices(state: State, n: int) -> frozenset[int]:
    incident = {v for edge in conflicts(state, n) for v in edge}
    return frozenset(range(n)) - incident


def run_order(state: State, n: int, order: tuple[int, ...]) -> State:
    for vertex in order:
        state = act(state, n, vertex)
    return state


@lru_cache(maxsize=None)
def endpoint_from_order(state: State, n: int, order: tuple[int, ...]) -> State:
    rank = {vertex: position for position, vertex in enumerate(order)}
    infinity = n + 1
    answer = set(state)
    original_conflicts = conflicts(state, n)
    for i, j in original_conflicts:
        left, right = rank.get(i, infinity), rank.get(j, infinity)
        if left == right == infinity:
            continue
        early, other = (i, j) if left < right else (j, i)
        value = (other, early) in state
        for arc in ((i, j), (j, i)):
            if value:
                answer.add(arc)
            else:
                answer.discard(arc)
    result = frozenset(answer)
    support = frozenset(order)
    residue = frozenset(
        edge for edge in original_conflicts
        if edge[0] not in support and edge[1] not in support
    )
    AUDIT.check(conflicts(result, n) == residue, "endpoint conflict-residue mismatch")
    AUDIT.check(run_order(state, n, order) == result, "relation action/order endpoint mismatch")
    return result


@lru_cache(maxsize=None)
def stirling2(t: int, r: int) -> int:
    if t == 0:
        return int(r == 0)
    if r == 0:
        return 0
    return stirling2(t - 1, r - 1) + r * stirling2(t - 1, r)


def onto_inclusion(t: int, r: int) -> int:
    return sum((-1) ** (r - j) * comb(r, j) * j**t for j in range(r + 1))


def fixed_first_order_weight(t: int, r: int) -> int:
    onto = onto_inclusion(t, r)
    AUDIT.check(onto % factorial(r) == 0, "surjection/order divisibility")
    answer = onto // factorial(r)
    AUDIT.check(answer == stirling2(t, r), "inclusion-exclusion/Stirling mismatch")
    return answer


def endpoint_formula(state: State, n: int, t: int) -> Counter[State]:
    result: Counter[State] = Counter()
    for r in range(n + 1):
        weight = fixed_first_order_weight(t, r)
        if not weight:
            continue
        for order in permutations(range(n), r):
            result[endpoint_from_order(state, n, order)] += weight
    return result


def independent(missing: frozenset[int], edges: frozenset[tuple[int, int]]) -> bool:
    return all(i not in missing or j not in missing for i, j in edges)


def absorption_formula(state: State, n: int, t: int) -> int:
    edges = conflicts(state, n)
    result = 0
    vertices = tuple(range(n))
    for size in range(n + 1):
        for chosen in combinations(vertices, size):
            missing = frozenset(chosen)
            if independent(missing, edges):
                used = n - size
                inclusion = onto_inclusion(t, used)
                AUDIT.check(
                    inclusion == factorial(used) * stirling2(t, used),
                    "absorption support weight mismatch",
                )
                result += inclusion
    return result


def structural_inverse_family(target: State, n: int, vertex: int) -> frozenset[State]:
    if vertex not in isolated_vertices(target, n):
        return frozenset()
    base = frozenset(edge for edge in target if edge[0] != vertex)
    free = tuple((vertex, other) for other in range(n) if other != vertex)
    family = set()
    for size in range(len(free) + 1):
        for chosen in combinations(free, size):
            family.add(base | frozenset(chosen))
    return frozenset(family)


def sink_scc_states(carrier: tuple[State, ...], adjacency: list[tuple[int, ...]]) -> tuple[set[int], int]:
    reverse = [[] for _ in carrier]
    for source, targets in enumerate(adjacency):
        for target in targets:
            reverse[target].append(source)

    visited = set()
    finish = []

    def first(vertex: int) -> None:
        visited.add(vertex)
        for target in adjacency[vertex]:
            if target not in visited:
                first(target)
        finish.append(vertex)

    for vertex in range(len(carrier)):
        if vertex not in visited:
            first(vertex)

    component = [-1] * len(carrier)
    components: list[list[int]] = []

    def second(vertex: int, label: int) -> None:
        component[vertex] = label
        components[label].append(vertex)
        for source in reverse[vertex]:
            if component[source] < 0:
                second(source, label)

    for vertex in reversed(finish):
        if component[vertex] < 0:
            components.append([])
            second(vertex, len(components) - 1)

    sink_labels = {
        label
        for label, members in enumerate(components)
        if all(component[target] == label for source in members for target in adjacency[source])
    }
    return {
        vertex for vertex, label in enumerate(component) if label in sink_labels
    }, len(sink_labels)


def author_rows() -> dict[int, tuple[int, int, int, int, int]]:
    text = (PAPER / "code/CANONICAL.txt").read_text(encoding="utf-8")
    pattern = re.compile(
        r"n=(\d+) states=(\d+) recurrent=(\d+) max_distinct_fibre=(\d+) "
        r"complete_H_absorbed_tn=(\d+) complete_H_endpoint_support=(\d+)"
    )
    result = {}
    for match in pattern.finditer(text):
        n, state_count, recurrent, maximum, absorbed, support = map(int, match.groups())
        result[n] = (state_count, recurrent, maximum, absorbed, support)
    AUDIT.check(len(result) == 4, "author canonical row count changed")
    AUDIT.check("ASSERTIONS=47033" in text, "author assertion receipt changed")
    return result


def verify_box(n: int, expected: tuple[int, int, int, int, int]) -> str:
    global ACTION_TRANSITIONS, KERNEL_ROWS, VIRTUAL_HISTORY_MASS
    carrier = states(n)
    index = {state: position for position, state in enumerate(carrier)}
    state_count = 2 ** (n * (n - 1))
    AUDIT.check(len(carrier) == state_count, "relation carrier size mismatch")
    AUDIT.check(len(index) == state_count, "duplicate relation state")

    adjacency: list[tuple[int, ...]] = []
    reverse_by_action: dict[tuple[State, int], set[State]] = defaultdict(set)
    reverse_all: dict[State, set[State]] = defaultdict(set)
    for source_position, source in enumerate(carrier):
        targets = []
        old_conflicts = conflicts(source, n)
        for vertex in range(n):
            target = act(source, n, vertex)
            target_position = index[target]
            targets.append(target_position)
            ACTION_TRANSITIONS += 1
            TRANSITION_DIGEST.update(
                f"{n}|{source_position}|{vertex}|{target_position}|{state_text(source)}|{state_text(target)}\n".encode()
            )
            expected_conflicts = frozenset(edge for edge in old_conflicts if vertex not in edge)
            AUDIT.check(conflicts(target, n) == expected_conflicts, "exact conflict-star deletion")
            AUDIT.check(act(target, n, vertex) == target, "local idempotence")
            reverse_by_action[(target, vertex)].add(source)
            reverse_all[target].add(source)
        adjacency.append(tuple(sorted(set(targets))))

        for i, j in old_conflicts:
            left = act(act(source, n, j), n, i)
            right = act(act(source, n, i), n, j)
            AUDIT.check(left != right, "conflict endpoints unexpectedly commute")

    recurrent_positions, sink_count = sink_scc_states(carrier, adjacency)
    predicted_recurrent = {
        position for position, state in enumerate(carrier) if not conflicts(state, n)
    }
    AUDIT.check(recurrent_positions == predicted_recurrent, "closed SCC/recurrent-state mismatch")
    AUDIT.check(sink_count == len(predicted_recurrent), "recurrent classes are not singleton fixed states")
    AUDIT.check(len(predicted_recurrent) == 2 ** comb(n, 2), "recurrent population formula")

    max_labelled = 0
    max_distinct = 0
    for target in carrier:
        isolated = isolated_vertices(target, n)
        structural_union: set[State] = set()
        labelled = 0
        for vertex in range(n):
            predicted_family = structural_inverse_family(target, n, vertex)
            actual_family = frozenset(reverse_by_action.get((target, vertex), set()))
            AUDIT.check(predicted_family == actual_family, "action-labelled inverse family mismatch")
            expected_size = 2 ** (n - 1) if vertex in isolated else 0
            AUDIT.check(len(predicted_family) == expected_size, "action-labelled fibre size")
            labelled += len(predicted_family)
            structural_union.update(predicted_family)
        AUDIT.check(labelled == len(isolated) * 2 ** (n - 1), "labelled pair fibre formula")
        expected_distinct = (
            1 + len(isolated) * (2 ** (n - 1) - 1) if isolated else 0
        )
        AUDIT.check(structural_union == reverse_all.get(target, set()), "distinct inverse union mismatch")
        AUDIT.check(len(structural_union) == expected_distinct, "distinct-source fibre formula")
        max_labelled = max(max_labelled, labelled)
        max_distinct = max(max_distinct, len(structural_union))

    max_t = n + 2
    complete_conflict = frozenset(
        (i, j) for i, j in undirected_pairs(n) if i < j
    )
    representative = frozenset(complete_conflict)
    complete_absorbed_tn = -1
    complete_endpoint_support = -1
    for source in carrier:
        distribution: Counter[State] = Counter({source: 1})
        previous_absorbed = -1
        for t in range(max_t + 1):
            KERNEL_ROWS += 1
            VIRTUAL_HISTORY_MASS += n**t
            formula = endpoint_formula(source, n, t)
            AUDIT.check(distribution == formula, "complete source-target/time kernel")
            AUDIT.check(sum(distribution.values()) == n**t, "kernel row normalization")
            absorbed = sum(
                weight for target, weight in distribution.items() if not conflicts(target, n)
            )
            predicted_absorbed = absorption_formula(source, n, t)
            AUDIT.check(absorbed == predicted_absorbed, "independent-set absorption CDF")
            if previous_absorbed >= 0:
                AUDIT.check(previous_absorbed * n <= absorbed, "absorption CDF decreased")
            previous_absorbed = absorbed
            if source == representative and t == n:
                complete_absorbed_tn = absorbed
                complete_endpoint_support = len(distribution)
            if t < max_t:
                next_distribution: Counter[State] = Counter()
                for current, weight in distribution.items():
                    for vertex in range(n):
                        next_distribution[act(current, n, vertex)] += weight
                distribution = next_distribution

    observed = (
        state_count,
        len(predicted_recurrent),
        max_distinct,
        complete_absorbed_tn,
        complete_endpoint_support,
    )
    AUDIT.check(observed == expected, "author/Review-B published-row mismatch")
    AUDIT.check(max_labelled == n * 2 ** (n - 1), "sharp labelled-fibre maximum")
    AUDIT.check(max_distinct == 1 + n * (2 ** (n - 1) - 1), "sharp distinct-fibre maximum")
    return (
        f"n={n} states={state_count} recurrent={len(predicted_recurrent)} "
        f"sink_scc={sink_count} max_labelled_fibre={max_labelled} "
        f"max_distinct_fibre={max_distinct} complete_H_absorbed_tn={complete_absorbed_tn} "
        f"complete_H_endpoint_support={complete_endpoint_support} times=0..{max_t}"
    )


def main() -> None:
    before = AUDIT.assertions
    check_frozen_artifacts()
    expected = author_rows()
    print("P183_HOSTILE_REVIEW_B_COMBINATORIAL_EXACT_V1")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print("representation=immutable_directed_arc_relations")
    print("kernel_method=weighted_markov_dp_plus_inclusion_exclusion")
    print("recurrence_method=closed_strongly_connected_components")
    print("inverse_method=target_star_family_construction")
    print("terminal_manifest_rows=19")
    print("lifecycle_manifest_checks_excluded_from_assertion_census=4")
    print(f"artifact_assertions={AUDIT.assertions-before}")
    for t in range(7):
        for r in range(5):
            fixed_first_order_weight(t, r)
    for n in range(1, 5):
        start = AUDIT.assertions
        row = verify_box(n, expected[n])
        print(f"{row} assertions={AUDIT.assertions-start}")
    print("boxes=4")
    print("all_targets=4165")
    print(f"action_transitions={ACTION_TRANSITIONS}")
    print(f"kernel_rows={KERNEL_ROWS}")
    print(f"virtual_history_mass={VIRTUAL_HISTORY_MASS}")
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
