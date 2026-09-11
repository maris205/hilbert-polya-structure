#!/usr/bin/env python3
"""Process-separated hostile verifier for P191 Round 0.

Representation firewall: a composition of N is encoded only by its internal-cut
bit mask.  The reviewer never imports the author verifier or uses the author's
tuple-of-parts carrier.  Every theorem claim is attacked by cut-mask dynamics,
indegree peeling, reverse breadth-first tails, and two independent one-step
inverse counts.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from pathlib import Path
import re


MAX_N = 18

EXPECTED_TEX_SHA = "bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84"
EXPECTED_ROUND0_SHA = "d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b"
EXPECTED_AUTHOR_VERIFY_SHA = "70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50"
EXPECTED_AUTHOR_CANONICAL_SHA = "c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c"
EXPECTED_PROOF_SHA = "f89ab89d2f9fa2f82eb6482129f4803870c3b3240d7a9eb8b31bd8579511d9ef"
EXPECTED_SOURCE_SHA = "26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9"
EXPECTED_BIB_KEYS = {
    "BenderCanfield2005",
    "BilleraThomasVanWilligenburg2006",
    "HeubachMansour2009",
    "Navarro2026OEISA398023",
    "Stanley2011EC1",
}

TABLE_EXPECTED = {
    4: {"states": 8, "image": 7, "fixed": 7, "tail": 1, "deepest": 1, "max_fibre": 2},
    8: {"states": 128, "image": 73, "fixed": 55, "tail": 5, "deepest": 1, "max_fibre": 11},
    12: {"states": 2048, "image": 801, "fixed": 378, "tail": 9, "deepest": 1, "max_fibre": 59},
    15: {"states": 16384, "image": 4906, "fixed": 1763, "tail": 12, "deepest": 1, "max_fibre": 182},
    18: {"states": 131072, "image": 28535, "fixed": 7398, "tail": 15, "deepest": 1, "max_fibre": 696},
}


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


CHECKS = Checks()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def artifact_gate() -> tuple[str, str, str, str, str, str, str]:
    root = Path(__file__).resolve().parents[4]
    paper = root / "papers" / "191-prefix-divisibility-cuts"
    tex = paper / "main.tex"
    frozen = paper / "main_round0_original.pdf"
    live = paper / "main.pdf"
    verify = paper / "code" / "verify.py"
    canonical = paper / "code" / "CANONICAL.txt"
    proof = paper / "PROOF_PACKAGE.md"
    source = paper / "SOURCE_VERIFICATION.md"
    bib = paper / "references.bib"

    tex_sha = file_sha(tex)
    frozen_sha = file_sha(frozen)
    live_sha = file_sha(live)
    verify_sha = file_sha(verify)
    canonical_sha = file_sha(canonical)
    proof_sha = file_sha(proof)
    source_sha = file_sha(source)
    bib_sha = file_sha(bib)

    CHECKS.require(tex_sha == EXPECTED_TEX_SHA, "Round0 main.tex drift")
    CHECKS.require(frozen_sha == EXPECTED_ROUND0_SHA, "Round0 PDF drift")
    CHECKS.require(live_sha == EXPECTED_ROUND0_SHA, "live PDF differs from Round0")
    CHECKS.require(verify_sha == EXPECTED_AUTHOR_VERIFY_SHA, "author verifier drift")
    CHECKS.require(canonical_sha == EXPECTED_AUTHOR_CANONICAL_SHA, "author canonical drift")
    CHECKS.require(proof_sha == EXPECTED_PROOF_SHA, "proof package drift")
    CHECKS.require(source_sha == EXPECTED_SOURCE_SHA, "source verification drift")
    CHECKS.require(frozen.read_bytes() == live.read_bytes(), "live/frozen bytes differ")

    manuscript = tex.read_text(encoding="utf-8")
    bibliography = bib.read_text(encoding="utf-8")
    cite_keys = set()
    for group in re.findall(r"\\cite[a-zA-Z*]*\{([^}]*)\}", manuscript):
        cite_keys.update(key.strip() for key in group.split(","))
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE))
    CHECKS.require(cite_keys == EXPECTED_BIB_KEYS, "unexpected manuscript cite-key set")
    CHECKS.require(bib_keys == EXPECTED_BIB_KEYS, "unexpected bibliography key set")
    CHECKS.require("hold\\_external" in manuscript.lower(), "HOLD_EXTERNAL missing in manuscript")
    CHECKS.require("N-3" in manuscript, "sharp clock boundary missing")
    manuscript_compact = re.sub(r"\s+", "", manuscript)
    CHECKS.require("a_i\\mids_i" in manuscript_compact, "divisibility predicate missing")

    return (
        tex_sha,
        frozen_sha,
        live_sha,
        bib_sha,
        verify_sha,
        canonical_sha,
        source_sha,
    )


def cut_list(mask: int, total: int) -> list[int]:
    return [position for position in range(1, total) if mask & (1 << (position - 1))]


def parts_from_mask(mask: int, total: int) -> tuple[int, ...]:
    previous = 0
    parts = []
    for cut in cut_list(mask, total):
        parts.append(cut - previous)
        previous = cut
    parts.append(total - previous)
    return tuple(parts)


def mask_from_parts(parts: tuple[int, ...]) -> int:
    mask = 0
    prefix = 0
    for part in parts[:-1]:
        prefix += part
        mask |= 1 << (prefix - 1)
    return mask


def update_mask(mask: int, total: int) -> int:
    previous = 0
    retained = 0
    for cut in cut_list(mask, total):
        step = cut - previous
        if cut % step == 0:
            retained |= 1 << (cut - 1)
        previous = cut
    return retained


def fixed_mask(mask: int, total: int) -> bool:
    previous = 0
    for cut in cut_list(mask, total):
        step = cut - previous
        if cut % step != 0:
            return False
        previous = cut
    return True


def fixed_count_recurrence(total: int) -> int:
    counts = [0] * total
    counts[0] = 1
    for endpoint in range(1, total):
        counts[endpoint] = sum(
            counts[previous]
            for previous in range(endpoint)
            if endpoint % (endpoint - previous) == 0
        )
    return sum(counts)


def witness_mask(total: int) -> int:
    return mask_from_parts((1, 2) + (1,) * (total - 3))


def witness_state(total: int, time: int) -> tuple[int, ...]:
    return (1, time + 2) + (1,) * (total - time - 3)


def global_fibre(total: int, target_mask: int) -> int:
    required = cut_list(target_mask, total)
    required_set = set(required)
    ways = [0] * (total + 1)
    ways[0] = 1
    last_required = 0
    cursor = 0
    for endpoint in range(1, total + 1):
        while cursor < len(required) and required[cursor] < endpoint:
            last_required = required[cursor]
            cursor += 1
        retained_target = endpoint in required_set
        for previous in range(last_required, endpoint):
            if not ways[previous]:
                continue
            if endpoint < total:
                retained_source = endpoint % (endpoint - previous) == 0
                if retained_source != retained_target:
                    continue
            ways[endpoint] += ways[previous]
    return ways[total]


def interval_factor(total: int, left: int, right: int, terminal: bool) -> int:
    ways = [0] * (right + 1)
    ways[left] = 1
    for endpoint in range(left + 1, right + 1):
        for previous in range(left, endpoint):
            if not ways[previous]:
                continue
            step = endpoint - previous
            if endpoint < right:
                if endpoint % step == 0:
                    continue
            elif not terminal:
                if endpoint % step != 0:
                    continue
            ways[endpoint] += ways[previous]
    return ways[right]


def factorized_fibre(total: int, target_mask: int) -> int:
    endpoints = cut_list(target_mask, total) + [total]
    product = 1
    left = 0
    for right in endpoints:
        product *= interval_factor(total, left, right, terminal=(right == total))
        left = right
    return product


def functional_graph(successor: list[int]) -> tuple[list[int], list[int]]:
    size = len(successor)
    indegree = [0] * size
    predecessors = [[] for _ in range(size)]
    for state, target in enumerate(successor):
        indegree[target] += 1
        predecessors[target].append(state)

    queue = deque(state for state, degree in enumerate(indegree) if degree == 0)
    peeled = [False] * size
    while queue:
        state = queue.popleft()
        peeled[state] = True
        target = successor[state]
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)

    cyclic = [state for state, removed in enumerate(peeled) if not removed]
    distance = [-1] * size
    queue = deque(cyclic)
    for state in cyclic:
        distance[state] = 0
    while queue:
        state = queue.popleft()
        for previous in predecessors[state]:
            if distance[previous] == -1:
                distance[previous] = distance[state] + 1
                queue.append(previous)
    CHECKS.require(all(value >= 0 for value in distance), "reverse BFS missed a state")
    return cyclic, distance


def main() -> None:
    tex_sha, frozen_sha, live_sha, bib_sha, verify_sha, canonical_sha, source_sha = artifact_gate()

    digest = sha256()
    total_states = 0
    total_targets = 0

    for total in range(1, MAX_N + 1):
        states = 1 << (total - 1)
        total_states += states
        successor = [update_mask(mask, total) for mask in range(states)]
        indegree = Counter(successor)
        cyclic, distance = functional_graph(successor)
        image = set(indegree)
        fixed = {mask for mask in range(states) if fixed_mask(mask, total)}
        cyclic_set = set(cyclic)

        CHECKS.require(states == 2 ** (total - 1), f"state count N={total}")
        CHECKS.require(cyclic_set == fixed, f"recurrent equals fixed N={total}")
        CHECKS.require(all(successor[state] == state for state in cyclic), f"all cycles fixed N={total}")
        CHECKS.require(len(image) == len(indegree), f"image accounting N={total}")
        CHECKS.require(sum(indegree.values()) == states, f"fibre mass via indegree N={total}")
        CHECKS.require(len(fixed) == fixed_count_recurrence(total), f"fixed recurrence N={total}")

        deepest_masks = []
        max_tail = max(distance)
        if total <= 3:
            CHECKS.require(max_tail == 0, f"small fixed boundary N={total}")
        else:
            witness = witness_mask(total)
            CHECKS.require(max_tail == total - 3, f"sharp tail N={total}")
            CHECKS.require(distance[witness] == total - 3, f"witness tail N={total}")
            deepest_masks = [state for state, tail in enumerate(distance) if tail == max_tail]
            CHECKS.require(deepest_masks == [witness], f"unique deepest state N={total}")
            current = witness
            for time in range(total - 2):
                CHECKS.require(
                    parts_from_mask(current, total) == witness_state(total, time),
                    f"witness orbit state N={total} t={time}",
                )
                current = successor[current]
            CHECKS.require(successor[current] == current, f"witness settles N={total}")

        for state, target in enumerate(successor):
            total_targets += 1
            digest.update(f"{total}:{state}>{target};".encode("ascii"))
            CHECKS.require(target & ~state == 0, f"cut monotonicity N={total} state={state}")
            CHECKS.require((state == target) == fixed_mask(state, total), f"fixed criterion N={total} state={state}")
            if state & 1:
                CHECKS.require(target & 1, f"first cut survives N={total} state={state}")

        for target, multiplicity in indegree.items():
            predicted_global = global_fibre(total, target)
            predicted_local = factorized_fibre(total, target)
            CHECKS.require(predicted_global == multiplicity, f"global fibre N={total} target={target}")
            CHECKS.require(predicted_local == multiplicity, f"factor fibre N={total} target={target}")
            CHECKS.require((target in image) == (predicted_global > 0), f"image iff positivity N={total} target={target}")
            CHECKS.require(predicted_global == predicted_local, f"two fibre forms agree N={total} target={target}")

        CHECKS.require(sum(global_fibre(total, target) for target in range(states)) == states, f"global mass N={total}")
        CHECKS.require(sum(factorized_fibre(total, target) for target in range(states)) == states, f"factor mass N={total}")

        if total in TABLE_EXPECTED:
            expected = TABLE_EXPECTED[total]
            CHECKS.require(len(image) == expected["image"], f"table image N={total}")
            CHECKS.require(len(fixed) == expected["fixed"], f"table fixed N={total}")
            CHECKS.require(max_tail == expected["tail"], f"table tail N={total}")
            CHECKS.require(states == expected["states"], f"table states N={total}")
            CHECKS.require(sum(1 for tail in distance if tail == max_tail) == expected["deepest"], f"table deepest N={total}")
            CHECKS.require(max(indegree.values()) == expected["max_fibre"], f"table max fibre N={total}")

    print("P191 process-separated hostile Review A")
    print(f"reviewer_representation=cut_mask_bitset")
    print(f"carrier_range=N=1..{MAX_N}")
    print(f"total_states={total_states}")
    print(f"total_transitions={total_targets}")
    print("frozen_main_tex_sha256=" + tex_sha)
    print("frozen_round0_pdf_sha256=" + frozen_sha)
    print("live_main_pdf_sha256=" + live_sha)
    print("frozen_references_sha256=" + bib_sha)
    print("frozen_author_verify_sha256=" + verify_sha)
    print("frozen_author_canonical_sha256=" + canonical_sha)
    print("frozen_source_verification_sha256=" + source_sha)
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print(f"review_transition_digest={digest.hexdigest()}")
    print(f"exact_assertions={CHECKS.count}")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
