#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P191 Round 1.

This script does not import the author verifier or any reviewer code. It
keeps the cut-mask carrier but reopens the inverse theorem through interval-
local deleted-cut subset grammars: inside each target interval it enumerates
deleted source cuts directly and checks retained versus deleted divisibility
conditions pointwise.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT / "papers" / "191-prefix-divisibility-cuts"
FORMAL_REVIEW_A = PAPER / "reviews" / "round1" / "reviewer_a"

PINNED_PAPER = {
    "main_round1.pdf": "d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b",
    "main.tex": "bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84",
    "references.bib": "1141067122be2dc4613007009d732fdcfc1dd35edf0c85d19ced38ef47acad0c",
    "code/verify.py": "70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50",
    "code/CANONICAL.txt": "c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c",
    "PROOF_PACKAGE.md": "f89ab89d2f9fa2f82eb6482129f4803870c3b3240d7a9eb8b31bd8579511d9ef",
    "SOURCE_VERIFICATION.md": "26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9",
}

PINNED_REVIEW_A = {
    "verify_review_a.py": "d85c52c2ca1edae596d60342945887c07af87a6717b27c4e313a752bb4c44f26",
    "CANONICAL.txt": "545f9e9a3d6d9fbbbebff84ebea3778375d8d1857b98a733f6f3eae5eca08a02",
}


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check_pinned_inputs() -> None:
    for name, expected in PINNED_PAPER.items():
        AUDIT.check(digest(PAPER / name) == expected, f"pinned paper artifact changed: {name}")
    for name, expected in PINNED_REVIEW_A.items():
        AUDIT.check(
            digest(FORMAL_REVIEW_A / name) == expected,
            f"pinned Review-A artifact changed: {name}",
        )

    round1 = PAPER / "main_round1.pdf"
    round2 = PAPER / "main_round2.pdf"
    live = PAPER / "main.pdf"
    AUDIT.check(round2.read_bytes() == round1.read_bytes(), "Round-2 PDF differs from Round-1 receipt")
    AUDIT.check(live.read_bytes() == round1.read_bytes(), "live PDF differs from Round-1 receipt")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    proof_package = (PAPER / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    source_verification = (PAPER / "SOURCE_VERIFICATION.md").read_text(encoding="utf-8")
    for needle in (
        r"N-3",
        r"HOLD\_EXTERNAL",
        "3,408,240",
        "no-skip",
    ):
        AUDIT.check(
            needle in source or needle in proof_package or needle in source_verification,
            f"contract missing: {needle}",
        )
    AUDIT.check(
        "approved/latest entry revision 22 July 2026" in source_verification,
        "accepted source-ledger repair missing",
    )
    AUDIT.check("27 August 2026" not in source_verification, "superseded OEIS date remains in source ledger")
    cited = {
        key.strip()
        for group in re.findall(r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", source)
        for key in group.split(",")
        if key.strip()
    }
    bib = {
        match.group(1).strip()
        for match in re.finditer(
            r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
            bibliography,
            flags=re.IGNORECASE,
        )
    }
    AUDIT.check(cited == bib, "citation/bibliography key mismatch")
    AUDIT.check(len(bib) == 5, "unexpected bibliography cardinality")


def cuts(mask: int, total: int) -> tuple[int, ...]:
    return tuple(i for i in range(1, total) if mask & (1 << (i - 1)))


def update_mask(mask: int, total: int) -> int:
    previous = 0
    out = 0
    for cut in cuts(mask, total):
        gap = cut - previous
        if cut % gap == 0:
            out |= 1 << (cut - 1)
        previous = cut
    return out


def fixed_criterion(mask: int, total: int) -> bool:
    previous = 0
    for cut in cuts(mask, total):
        gap = cut - previous
        if cut % gap != 0:
            return False
        previous = cut
    return True


def fixed_count_recurrence(total: int) -> int:
    stable = [0] * total
    stable[0] = 1
    for endpoint in range(1, total):
        stable[endpoint] = sum(
            stable[endpoint - step]
            for step in range(1, endpoint + 1)
            if endpoint % step == 0
        )
    return sum(stable)


def tail_period(mask: int, total: int) -> tuple[int, int]:
    seen = {}
    current = mask
    while current not in seen:
        seen[current] = len(seen)
        current = update_mask(current, total)
    return seen[current], len(seen) - seen[current]


def witness_mask(total: int, time: int = 0) -> int:
    if total <= 3:
        return (1 << (total - 1)) - 1 if total >= 1 else 0
    parts = [1, time + 2] + [1] * (total - time - 3)
    prefix = 0
    mask = 0
    for part in parts[:-1]:
        prefix += part
        mask |= 1 << (prefix - 1)
    return mask


@lru_cache(maxsize=None)
def interval_subset_count(left: int, right: int, terminal: bool) -> int:
    interior = list(range(left + 1, right))
    total = 0
    for subset_mask in range(1 << len(interior)):
        chosen = [interior[i] for i in range(len(interior)) if subset_mask & (1 << i)]
        previous = left
        valid = True
        for cut in chosen:
            gap = cut - previous
            if cut % gap == 0:
                valid = False
                break
            previous = cut
        if not valid:
            continue
        final_gap = right - previous
        if not terminal and right % final_gap != 0:
            continue
        total += 1
    return total


def factorized_fibre(mask: int, total: int) -> int:
    endpoints = cuts(mask, total) + (total,)
    left = 0
    product = 1
    for right in endpoints:
        product *= interval_subset_count(left, right, right == total)
        left = right
    return product


def verify_box(total: int) -> str:
    states = range(1 << (total - 1))
    indegree: Counter[int] = Counter()
    fixed = set()
    recurrent = set()
    tails = {}
    transition_digest = sha256()

    for state in states:
        target = update_mask(state, total)
        indegree[target] += 1
        transition_digest.update(f"{total}:{state}->{target};".encode("ascii"))
        AUDIT.check(target & ~state == 0, f"monotone cut deletion N={total} state={state}")

        tail, period = tail_period(state, total)
        tails[state] = tail
        AUDIT.check(period == 1, f"no nontrivial recurrence N={total} state={state}")
        AUDIT.check((target == state) == fixed_criterion(state, total), f"fixed criterion N={total} state={state}")
        if target == state:
            fixed.add(state)
        if tail == 0:
            recurrent.add(state)

    AUDIT.check(recurrent == fixed, f"recurrent equals fixed N={total}")
    AUDIT.check(len(fixed) == fixed_count_recurrence(total), f"fixed recurrence N={total}")

    maximum_tail = max(tails.values())
    deepest = {state for state, tail in tails.items() if tail == maximum_tail}
    AUDIT.check(maximum_tail == max(0, total - 3), f"sharp tail N={total}")
    if total <= 3:
        AUDIT.check(fixed == set(states), f"small carrier fixed N={total}")
        AUDIT.check(deepest == set(states), f"small carrier deepest N={total}")
    else:
        witness = witness_mask(total, 0)
        AUDIT.check(deepest == {witness}, f"unique deepest N={total}")
        current = witness
        for time in range(total - 2):
            AUDIT.check(current == witness_mask(total, time), f"witness trajectory N={total} t={time}")
            if time < total - 3:
                current = update_mask(current, total)
        AUDIT.check(update_mask(current, total) == current, f"witness endpoint N={total}")

    image = set(indegree)
    formula_image = set()
    total_mass = 0
    fibre_max = 0
    for target in states:
        predicted = factorized_fibre(target, total)
        actual = indegree.get(target, 0)
        AUDIT.check(predicted == actual, f"factorized fibre N={total} target={target}")
        AUDIT.check((predicted > 0) == (target in image), f"image positivity N={total} target={target}")
        if predicted > 0:
            formula_image.add(target)
        total_mass += predicted
        fibre_max = max(fibre_max, predicted)

    AUDIT.check(formula_image == image, f"image equality N={total}")
    AUDIT.check(total_mass == len(states), f"fibre mass N={total}")
    return (
        f"N={total} states={len(states)} fixed={len(fixed)} image={len(image)} "
        f"max_tail={maximum_tail} deepest={len(deepest)} fibre_max={fibre_max} "
        f"transition_sha256={transition_digest.hexdigest()}"
    )


def main() -> None:
    check_pinned_inputs()
    print("P191 process-separated hostile Review B")
    print("reviewer_representation=interval_deleted_cut_subset_grammar")
    print(f"pinned_input_count={len(PINNED_PAPER) + len(PINNED_REVIEW_A)}")
    print("formal_review_a_root=papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a")
    print(f"frozen_round1_pdf_sha256={PINNED_PAPER['main_round1.pdf']}")
    print(f"frozen_main_tex_sha256={PINNED_PAPER['main.tex']}")
    print(f"frozen_references_bib_sha256={PINNED_PAPER['references.bib']}")
    print(f"frozen_author_verifier_sha256={PINNED_PAPER['code/verify.py']}")
    print(f"frozen_author_canonical_sha256={PINNED_PAPER['code/CANONICAL.txt']}")
    print(f"frozen_proof_package_sha256={PINNED_PAPER['PROOF_PACKAGE.md']}")
    print(f"frozen_source_verification_sha256={PINNED_PAPER['SOURCE_VERIFICATION.md']}")
    print(f"formal_review_a_verifier_sha256={PINNED_REVIEW_A['verify_review_a.py']}")
    print(f"formal_review_a_canonical_sha256={PINNED_REVIEW_A['CANONICAL.txt']}")
    print("case_count=15")
    for total in range(1, 16):
        print(verify_box(total))
    print(f"exact_assertions={AUDIT.assertions}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
