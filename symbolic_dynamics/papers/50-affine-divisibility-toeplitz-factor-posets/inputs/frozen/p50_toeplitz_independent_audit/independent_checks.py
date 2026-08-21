#!/usr/bin/env python3
"""Independent, read-only audit checks for the frozen P50 Stage-2 package.

This program deliberately does not import either implementation from the
candidate package.  It reconstructs the affine evaluator, the nested-hole
evaluator, the finite graph objects, and the package-integrity checks from
the frozen definitions.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import stat
from itertools import product
from pathlib import Path
from typing import Iterable


CANDIDATE = Path("/tmp/p50_toeplitz_stage2")
EXPECTED_MANIFEST_SHA256 = (
    "c070bd76d8a28e1b918fa040d9346db32776f238e7081d8c3504648b137a583e"
)
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def snapshot_tree(root: Path) -> dict:
    if not root.is_dir() or root.is_symlink():
        raise AssertionError(f"candidate root is not an ordinary directory: {root}")
    records: list[dict] = []
    hygiene = {
        "cache_paths": [],
        "nonregular_paths": [],
        "symlink_paths": [],
    }
    for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        directory = Path(dirpath)
        for name in sorted(dirnames + filenames):
            path = directory / name
            rel = path.relative_to(root).as_posix()
            info = path.lstat()
            mode = stat.S_IMODE(info.st_mode)
            if name in CACHE_NAMES or name.endswith((".pyc", ".pyo")):
                hygiene["cache_paths"].append(rel)
            if stat.S_ISLNK(info.st_mode):
                hygiene["symlink_paths"].append(rel)
                records.append({"kind": "symlink", "mode": f"{mode:04o}", "path": rel})
            elif stat.S_ISDIR(info.st_mode):
                records.append({"kind": "directory", "mode": f"{mode:04o}", "path": rel})
            elif stat.S_ISREG(info.st_mode):
                records.append(
                    {
                        "kind": "file",
                        "mode": f"{mode:04o}",
                        "path": rel,
                        "sha256": sha256_file(path),
                        "size": info.st_size,
                    }
                )
            else:
                hygiene["nonregular_paths"].append(rel)
                records.append({"kind": "nonregular", "mode": f"{mode:04o}", "path": rel})
    for key in hygiene:
        hygiene[key].sort()
    records.sort(key=lambda row: (row["path"], row["kind"]))
    return {
        "hygiene": hygiene,
        "records": records,
        "regular_file_count": sum(row["kind"] == "file" for row in records),
        "root": str(root),
        "tree_sha256": canonical_sha256(records),
    }


def verify_candidate_manifest(root: Path) -> dict:
    manifest = root / "SHA256SUMS.txt"
    observed_manifest_sha = sha256_file(manifest)
    if observed_manifest_sha != EXPECTED_MANIFEST_SHA256:
        raise AssertionError("frozen manifest SHA-256 changed")
    entries: list[tuple[str, str]] = []
    for lineno, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not raw:
            raise AssertionError(f"blank manifest line {lineno}")
        try:
            digest, rel = raw.split("  ", 1)
        except ValueError as exc:
            raise AssertionError(f"bad manifest line {lineno}") from exc
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise AssertionError(f"bad digest at manifest line {lineno}")
        if not rel or rel.startswith("/") or ".." in Path(rel).parts:
            raise AssertionError(f"unsafe manifest path at line {lineno}")
        entries.append((rel, digest))
    rels = [rel for rel, _ in entries]
    if rels != sorted(rels) or len(rels) != len(set(rels)):
        raise AssertionError("manifest paths are not unique and sorted")
    actual_files = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and not path.is_symlink() and path.name != "SHA256SUMS.txt"
    )
    if rels != actual_files:
        raise AssertionError("manifest file set differs from candidate file set")
    for rel, expected in entries:
        if sha256_file(root / rel) != expected:
            raise AssertionError(f"manifest mismatch: {rel}")
    return {
        "entry_count": len(entries),
        "manifest_sha256": observed_manifest_sha,
        "paths_sorted_unique": True,
        "status": "PASS",
    }


def check_engine_import_separation(root: Path) -> dict:
    names = ("impl_formula", "impl_holefill")
    imports: dict[str, list[str]] = {}
    for name in names:
        tree = ast.parse((root / f"{name}.py").read_text(encoding="utf-8"))
        found: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                found.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                found.add(node.module.split(".")[0])
        imports[name] = sorted(found)
    if "impl_holefill" in imports["impl_formula"]:
        raise AssertionError("formula engine imports hole-fill engine")
    if "impl_formula" in imports["impl_holefill"]:
        raise AssertionError("hole-fill engine imports formula engine")
    return {"imports": imports, "status": "PASS"}


def divexp(p: int, value: int) -> int:
    if p < 3 or value == 0:
        raise ValueError("invalid base or zero argument")
    value = abs(value)
    exponent = 0
    while value % p == 0:
        exponent += 1
        value //= p
    return exponent


def affine_value(p: int, directive: tuple[int, ...], k: int) -> int:
    return directive[divexp(p, (p - 1) * k + 1) % len(directive)]


def nested_value(p: int, directive: tuple[int, ...], k: int) -> int:
    residue = 0
    power = 1
    level = 0
    while True:
        next_residue = residue + power
        next_power = power * p
        if k % next_power != next_residue % next_power:
            return directive[level % len(directive)]
        residue = next_residue
        power = next_power
        level += 1


def r_center(p: int, n: int) -> int:
    return (p**n - 1) // (p - 1)


def point_and_hole_checks() -> dict:
    directives = ((0, 1), (0, 1, 2), (0, 1, 0, 2))
    comparisons = 0
    for p in range(3, 11):
        for directive in directives:
            for k in range(-500, 501):
                if affine_value(p, directive, k) != nested_value(p, directive, k):
                    raise AssertionError(("independent evaluators disagree", p, directive, k))
                comparisons += 1

    residue_checks = 0
    progression_checks = 0
    essential_period_checks = 0
    for p in range(3, 9):
        directive = (0, 1, 2)
        for n in range(1, 4):
            modulus = p**n
            hole = r_center(p, n)
            actual_holes: list[int] = []
            for a in range(modulus):
                values = {
                    affine_value(p, directive, a + t * modulus)
                    for t in range(-5, 6)
                }
                if len(values) > 1:
                    actual_holes.append(a)
                else:
                    progression_checks += 1
            if actual_holes != [hole]:
                raise AssertionError(("wrong sampled hole residue", p, n, actual_holes))
            if affine_value(p, directive, hole) == affine_value(
                p, directive, hole + modulus
            ):
                raise AssertionError("successive hole fills should differ")
            residue_checks += modulus
            # The singleton hole set modulo p^n has no positive translation
            # period smaller than p^n.
            for q in range(1, modulus):
                if (hole + q) % modulus == hole:
                    raise AssertionError("unique hole acquired a smaller period")
                essential_period_checks += 1
    return {
        "essential_period_translation_checks": essential_period_checks,
        "formula_nested_comparisons": comparisons,
        "progression_equalities": progression_checks,
        "residue_checks": residue_checks,
        "status": "PASS",
    }


def smallest_prime_divisor(n: int) -> int:
    for q in range(2, math.isqrt(n) + 1):
        if n % q == 0:
            return q
    return n


def is_prime(n: int) -> bool:
    return n >= 2 and smallest_prime_divisor(n) == n


def constructiveness_checks() -> dict:
    directive = (0, 1, 2, 3, 4, 5, 6)
    universal_upper_coordinates = 0
    for p in range(3, 11):
        for n in range(1, 4):
            common = p ** (n + 1)
            for k in range(p**n):
                exponent = divexp(p, (p - 1) * k + 1)
                if exponent > n:
                    raise AssertionError(("upper exponent bound failed", p, n, k))
                for t in (-3, -1, 1, 4):
                    if affine_value(p, directive, k) != affine_value(
                        p, directive, k + t * common
                    ):
                        raise AssertionError(("universal upper failed", p, n, k, t))
                universal_upper_coordinates += 1

    prime_q_rejections = 0
    prime_witness_congruences = 0
    for p in (3, 5, 7, 11):
        for n in range(1, 4):
            upper = p ** (n + 1)
            for q in range(1, upper):
                j = divexp(p, q)
                if j > n:
                    raise AssertionError("q below next power has too large exponent")
                d = q // (p**j)
                solutions = [
                    t
                    for t in range(p * p)
                    if (1 + (p - 1) * d * t - p) % (p * p) == 0
                ]
                if len(solutions) != 1:
                    raise AssertionError(("prime witness not unique mod p^2", p, q))
                t = solutions[0]
                k = r_center(p, j)
                if not (0 <= k < p**n):
                    raise AssertionError(("witness center outside block", p, n, q, k))
                before = divexp(p, (p - 1) * k + 1)
                after = divexp(p, (p - 1) * (k + t * q) + 1)
                if (before, after) != (j, j + 1):
                    raise AssertionError(("prime exponent witness failed", p, n, q))
                if directive[before] == directive[after]:
                    raise AssertionError("adjacent directive witness was merged")
                prime_q_rejections += 1
                prime_witness_congruences += 1

    composite_coordinates = 0
    composite_progression_equalities = 0
    for p in (4, 6, 8, 9, 10, 12):
        ell = smallest_prime_divisor(p)
        if ell >= p:
            raise AssertionError("composite lane received a prime")
        for n in range(1, 4):
            q = ell * p**n
            if not q < p ** (n + 1):
                raise AssertionError("counterperiod is not below next power")
            for k in range(p**n):
                e = divexp(p, (p - 1) * k + 1)
                if e == n and k != r_center(p, n):
                    raise AssertionError("more than one level-n hole representative")
                for t in range(-8, 9):
                    if affine_value(p, directive, k) != affine_value(
                        p, directive, k + t * q
                    ):
                        raise AssertionError(("composite counterperiod failed", p, n, k, t))
                    composite_progression_equalities += 1
                composite_coordinates += 1
    return {
        "composite_counterperiod_coordinates": composite_coordinates,
        "composite_progression_equalities": composite_progression_equalities,
        "prime_q_lower_rejections": prime_q_rejections,
        "prime_witness_congruences": prime_witness_congruences,
        "universal_upper_coordinates": universal_upper_coordinates,
        "status": "PASS",
    }


def high_center_checks() -> dict:
    identity_checks = 0
    window_checks = 0
    directive = (0, 1, 2, 3)
    for p in range(3, 13):
        for j in range(-120, 121):
            if j == 0:
                continue
            e = divexp(p, j)
            for n in (e + 1, e + 2, e + 5):
                left = divexp(p, p**n + (p - 1) * j)
                if left != e:
                    raise AssertionError(("high-center identity failed", p, j, n))
                identity_checks += 1
        for radius in range(0, 7):
            threshold = max(
                (divexp(p, j) for j in range(-radius, radius + 1) if j),
                default=-1,
            )
            signatures: dict[int, tuple[int, ...]] = {}
            for n in range(threshold + 1, threshold + 1 + 4 * len(directive)):
                center = r_center(p, n)
                window = tuple(
                    affine_value(p, directive, center + j)
                    for j in range(-radius, radius + 1)
                )
                center_letter = directive[n % len(directive)]
                prior = signatures.setdefault(center_letter, window)
                if prior != window:
                    raise AssertionError(("same center letter has different high window", p, radius))
                expected = tuple(
                    center_letter if j == 0 else directive[divexp(p, j) % len(directive)]
                    for j in range(-radius, radius + 1)
                )
                if window != expected:
                    raise AssertionError(("high-window normal form failed", p, radius, n))
                window_checks += 1
            if set(signatures) != set(directive):
                raise AssertionError("not every exact-support letter appeared at high centers")
    return {
        "high_center_identity_checks": identity_checks,
        "high_window_normal_forms": window_checks,
        "radii_checked": 7,
        "status": "PASS",
    }


def canonicalize(word: Iterable[int]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    result: list[int] = []
    for value in word:
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


def least_period(word: tuple[int, ...]) -> int:
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and all(word[i] == word[i % d] for i in range(len(word))):
            return d
    raise AssertionError("finite word has no period")


def enumerate_directives(max_length: int = 7, max_letters: int = 4) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []

    def extend(prefix: list[int], target: int) -> None:
        if len(prefix) == target:
            word = tuple(prefix)
            if (
                2 <= max(word) + 1 <= max_letters
                and least_period(word) == len(word)
                and all(word[i] != word[(i + 1) % len(word)] for i in range(len(word)))
            ):
                result.append(word)
            return
        for label in range(min(max(prefix) + 1, max_letters - 1) + 1):
            prefix.append(label)
            extend(prefix, target)
            prefix.pop()

    for length in range(2, max_length + 1):
        extend([0], length)
    return sorted(set(result), key=lambda w: (len(w), max(w), w))


def enumerate_partitions(n: int) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []

    def extend(prefix: list[int]) -> None:
        if len(prefix) == n:
            result.append(tuple(prefix))
            return
        for label in range(max(prefix) + 2):
            prefix.append(label)
            extend(prefix)
            prefix.pop()

    extend([0])
    return sorted(result, key=lambda p: (max(p), p))


def adjacent_edges(word: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        tuple(sorted((word[i], word[(i + 1) % len(word)])))
        for i in range(len(word))
    }


def admissible(word: tuple[int, ...], partition: tuple[int, ...]) -> bool:
    return all(
        partition[word[i]] != partition[word[(i + 1) % len(word)]]
        for i in range(len(word))
    )


def refines(fine: tuple[int, ...], coarse: tuple[int, ...]) -> bool:
    return all(
        fine[a] != fine[b] or coarse[a] == coarse[b]
        for a in range(len(fine))
        for b in range(len(fine))
    )


def falling(q: int, k: int) -> int:
    value = 1
    for j in range(k):
        value *= q - j
    return value


def partition_poset_checks() -> dict:
    directives = enumerate_directives()
    partition_checks = 0
    quotient_checks = 0
    refinement_checks = 0
    chromatic_checks = 0
    for word in directives:
        vertex_count = max(word) + 1
        partitions = enumerate_partitions(vertex_count)
        good = [part for part in partitions if admissible(word, part)]
        edges = adjacent_edges(word)
        for part in partitions:
            graph_condition = all(part[a] != part[b] for a, b in edges)
            if admissible(word, part) != graph_condition:
                raise AssertionError("adjacency and independent-block tests disagree")
            partition_checks += 1
        stirling: dict[int, int] = {}
        for part in good:
            quotient = tuple(part[letter] for letter in word)
            reduced = quotient[: least_period(quotient)]
            if set(reduced) != set(range(max(part) + 1)):
                raise AssertionError("quotient lost exact support under least-period reduction")
            if len(reduced) < 2 or any(
                reduced[i] == reduced[(i + 1) % len(reduced)]
                for i in range(len(reduced))
            ):
                raise AssertionError("admissible quotient left frozen family")
            blocks = max(part) + 1
            stirling[blocks] = stirling.get(blocks, 0) + 1
            quotient_checks += 1
        for fine in good:
            for coarse in good:
                induced: dict[int, int] = {}
                consistent = True
                for vertex in range(vertex_count):
                    a, b = fine[vertex], coarse[vertex]
                    if a in induced and induced[a] != b:
                        consistent = False
                    induced[a] = b
                if consistent != refines(fine, coarse):
                    raise AssertionError("refinement differs from induced quotient existence")
                refinement_checks += 1
        for q in range(0, 7):
            direct = sum(
                all(color[a] != color[b] for a, b in edges)
                for color in product(range(q), repeat=vertex_count)
            )
            by_partitions = sum(count * falling(q, k) for k, count in stirling.items())
            if direct != by_partitions:
                raise AssertionError(("chromatic identity failed", word, q))
            chromatic_checks += 1
        chi = min(stirling)
        if (2 in stirling) != (chi == 2):
            raise AssertionError("binary target and chromatic number disagree")
    return {
        "admissible_quotients": quotient_checks,
        "chromatic_identities": chromatic_checks,
        "directives": len(directives),
        "partition_tests": partition_checks,
        "refinement_pair_tests": refinement_checks,
        "status": "PASS",
    }


def find_point_mismatch(
    p: int, q: int, directive: tuple[int, ...], shift: int = 0
) -> int | None:
    for k in range(-1000, 1001):
        if affine_value(p, directive, k) != affine_value(q, directive, k + shift):
            return k
    return None


def mutation_controls() -> dict:
    directive = (0, 1, 2)
    wrong_base_mismatch = find_point_mismatch(3, 4, directive)
    if wrong_base_mismatch is None:
        raise AssertionError("wrong-base identity mutation was not detected")
    nonpointed_shift_mismatch = find_point_mismatch(3, 3, directive, shift=1)
    if nonpointed_shift_mismatch is None:
        raise AssertionError("nonpointed shift mutation was not detected")
    adjacent_merge = (0, 0, 1)
    if all(
        adjacent_merge[directive[i]] != adjacent_merge[directive[(i + 1) % len(directive)]]
        for i in range(len(directive))
    ):
        raise AssertionError("adjacent-merge mutation was not detected")
    # Composite p=4 has the strict counterperiod 2*4^N, so a mutation that
    # calls every integer-base structure constructive is rejected at N=1.
    p, n, q = 4, 1, 2 * 4
    composite_equalities = all(
        affine_value(p, directive, k) == affine_value(p, directive, k + t * q)
        for k in range(p**n)
        for t in range(-10, 11)
    )
    if not composite_equalities or not q < p ** (n + 1):
        raise AssertionError("composite constructiveness mutation was not detected")
    return {
        "adjacent_merge_partition": list(adjacent_merge),
        "composite_counterperiod": {"N": n, "p": p, "q": q},
        "nonpointed_shift_mismatch_coordinate": nonpointed_shift_mismatch,
        "status": "PASS",
        "typed_scope_rejections": ["wrong_base", "nonpointed", "adjacent_merge"],
        "wrong_base_mismatch_coordinate": wrong_base_mismatch,
    }


def run_all() -> dict:
    snapshot = snapshot_tree(CANDIDATE)
    if any(snapshot["hygiene"].values()):
        raise AssertionError("candidate hygiene failure")
    sections = {
        "candidate_manifest": verify_candidate_manifest(CANDIDATE),
        "constructiveness": constructiveness_checks(),
        "engine_separation": check_engine_import_separation(CANDIDATE),
        "high_centers": high_center_checks(),
        "mutations": mutation_controls(),
        "partition_poset": partition_poset_checks(),
        "points_skeletons_essential_periods": point_and_hole_checks(),
    }
    if any(section.get("status") != "PASS" for section in sections.values()):
        raise AssertionError("one or more independent sections failed")
    return {
        "candidate_tree_sha256": snapshot["tree_sha256"],
        "checker": "auditor-owned; imports no candidate implementation",
        "section_count": len(sections),
        "sections": sections,
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checks-output", type=Path)
    parser.add_argument("--snapshot-output", type=Path)
    parser.add_argument("--snapshot-only", action="store_true")
    args = parser.parse_args()
    snapshot = snapshot_tree(CANDIDATE)
    if args.snapshot_output:
        write_json(args.snapshot_output, snapshot)
    if args.snapshot_only:
        print(json.dumps({"status": "PASS", "tree_sha256": snapshot["tree_sha256"]}, sort_keys=True))
        return
    result = run_all()
    if args.checks_output:
        write_json(args.checks_output, result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
