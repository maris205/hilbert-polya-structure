#!/usr/bin/env python3
"""Staged C61 tensor/Burnside group producer and hostile validator.

This file is deliberately self-contained.  Runtime builds read released P60/C60
artifacts as immutable Git blobs and the explicitly frozen C61 target-lock bytes
in the repository.  External selection and audit files are checked only by a
nonpromoted staging harness and are not runtime authority.  In particular the
producer does not import any target-selection pilot or the C60 Python
implementation.  The independent GAP/TomLib call graph lives in
``c61_checker_group.g`` and shares only canonical JSON with this producer.

The component is STAGED/NONRELEASE.  It proves finite-group statements only;
it never claims evaluated resolvents, paper completion, release, bad Euler
factors, epsilon factors, or root numbers.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
from typing import Any, Iterable, Sequence


SCHEMA_ID = "hcs-c61-group-evidence-v1"
CHECKER_SCHEMA_ID = "hcs-c61-gap-group-projection-v1"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
PROJECT_BASENAME = "henon_mu3_yukawa_tensor_fourier_descent"
PROJECT_STATUS = "STAGED_NONRELEASE_GROUP_COMPONENT"
PROMOTED_EVIDENCE_SIZE_CEILING_BYTES = 2_000_000

REPO = Path("/root/autodl-tmp/hilbert-polya-structure")
PROJECT = Path("henon_dynamics/henon_mu3_yukawa_biquadratic_envelope")

P60 = "fe1217810b72840619efdf40a2af31b8b80d96f6"
P60_TREE = "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a"
P60_PARENT = "f3b3726c40519cdd8ac7832f9f22df16d451b890"
FORMAL_13_ROOT_SHA256: str | None = "c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28"
FORMAL_ROUTE_SHA256: str | None = "c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b"
FORMAL_BATCH_SHA256: str | None = "13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814"
FORMAL_EXACT15_SHA256: str | None = "61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5"

EXPECTED_FILES = {
    "c60_full_manifest": (PROJECT / "FULL_PROJECT_HASHES.sha256", "37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4"),
    "c60_live_route": (PROJECT / "route_a_evaluation.yaml", "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
    "c60_archive_route": (PROJECT / "evaluations/route_a/HCS-C60/20260817T000000Z.yaml", "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
    "c60_certificate": (PROJECT / "results/c60_certificate.json", "d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518"),
    "c60_group_evidence": (PROJECT / "results/c60_group_evidence.json", "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2"),
    "c60_resolvent_evidence": (PROJECT / "results/c60_resolvent_evidence.json", "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da"),
    "c60_group_module": (PROJECT / "code/c60_group.py", "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b"),
    "c60_schema": (PROJECT / "results/c60_schema.json", "c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5"),
    "c60_independent_check": (PROJECT / "results/c60_check_report.json", "25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44"),
    "c60_scoped_manifest": (PROJECT / "results/scoped_hash_manifest.json", "f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7"),
    "c59_resolvent_evidence": (Path("henon_dynamics/henon_mu3_yukawa_gassmann_twins/results/c59_resolvent_evidence.json"), "667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6"),
    "released_batch": (Path("henon_dynamics/BATCH_PLAN_C57_C61.md"), "d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5"),
}

TARGET_LOCK_ROOT_FILES = [
    "DERIVATION.md", "EXPERIMENT_PLAN.md", "EXPERIMENT_TRACKER.md",
    "IMPLEMENTATION_CHECKLIST.md", "INTEGRITY_REPORT.md",
    "METHODOLOGY_BLUEPRINT.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md",
    "PROOF_PACKAGE.md", "README.md", "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
]

EXPECTED_C60_PAYLOAD_SHA256 = "dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead"
EXPECTED_C60_SOURCE_CONTRACT_SHA256 = "4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90"
EXPECTED_FROZEN_ARRAYS_SHA256 = "0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5"
EXPECTED_GAP_SHA256 = "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3"

FALSE_SCOPE_LEAVES = {
    "artin_holomorphy_claimed": False,
    "automorphy_claimed": False,
    "bad_artin_euler_claimed": False,
    "brauer_manin_claimed": False,
    "characteristic_zero_coefficient_hash_claimed": False,
    "class_number_claimed": False,
    "d3_branch_selected": False,
    "decomposition_frobenius_claimed": False,
    "expanded_characteristic_zero_resolvent_claimed": False,
    "finite_g_sets_isomorphic_from_character_relation": False,
    "formal_invariant_statement_after_root_relations": False,
    "global_root_number_claimed": False,
    "hasse_principle_claimed": False,
    "hilbert_polya_operator_claimed": False,
    "integral_basis_claimed": False,
    "local_epsilon_factor_claimed": False,
    "local_fields_classified_by_nefd_rows": False,
    "local_root_number_claimed": False,
    "maximal_order_claimed": False,
    "monogenicity_claimed": False,
    "motive_claimed": False,
    "paper_complete_claimed": False,
    "rational_point_claimed": False,
    "raw_tom_defines_fields": False,
    "regulator_claimed": False,
    "release_claimed": False,
    "rh_claimed": False,
    "target_selection_pilot_is_theorem_authority": False,
    "trace_form_claimed": False,
    "weak_approximation_claimed": False,
}

# Durable released-carrier representatives of ToM 147,23,6,2,5.  They are
# source-owned C61 literals and are independently located by the GAP checker.
GLOBAL_LOCAL_ARRAYS = {
    "I5_tom147": [
        [16,23,27,8,26,9,7,11,24,10,25,5,13,6,12,20,2,18,19,22,17,1,21,14,4,15,3],
        [16,2,23,8,18,17,25,4,21,10,11,12,22,27,26,1,6,5,19,20,9,13,3,24,7,15,14],
    ],
    "P5_tom23": [
        [10,7,3,14,4,6,1,12,5,13,15,17,2,19,21,8,27,25,9,11,24,23,26,20,22,18,16],
    ],
    "C3_tom6": [
        [23,25,18,22,17,21,1,14,4,15,12,19,2,20,16,10,24,27,11,8,26,9,7,5,13,6,3],
    ],
    "C2_tom2": [
        [1,2,3,6,5,4,7,8,11,10,9,12,15,14,13,18,17,16,21,20,19,22,23,24,27,26,25],
    ],
    "Cinf_tom5": [
        [6,13,16,12,5,1,18,15,20,22,26,4,2,17,8,3,14,7,19,9,27,10,24,23,25,11,21],
    ],
}

P3_WITNESS_ONE_BASED = [25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5]


class StrictError(RuntimeError):
    """Fail-closed validation error."""


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer:
            raise StrictError(f"duplicate JSON key: {key}")
        answer[key] = value
    return answer


def strict_json(raw: bytes, label: str) -> Any:
    try:
        text = raw.decode("utf-8", errors="strict")
        return json.loads(
            text,
            object_pairs_hook=strict_pairs,
            parse_float=lambda _: (_ for _ in ()).throw(StrictError(f"float in {label}")),
            parse_constant=lambda _: (_ for _ in ()).throw(StrictError(f"constant in {label}")),
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise StrictError(f"invalid JSON in {label}: {exc}") from exc


def stable_read(
    path: Path, *, root: Path | None = None, limit: int = 100_000_000,
    _after_read_hook: Any | None = None,
) -> bytes:
    if path.is_symlink():
        raise StrictError(f"symlink rejected: {path}")
    resolved = path.resolve(strict=True)
    if root is not None:
        root_resolved = root.resolve(strict=True)
        if resolved != root_resolved and root_resolved not in resolved.parents:
            raise StrictError(f"path escapes root: {path}")
    before = resolved.stat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
        raise StrictError(f"invalid/oversized file: {path}")
    raw = resolved.read_bytes()
    if _after_read_hook is not None:
        _after_read_hook(resolved)
    after = resolved.stat()
    fingerprint = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
    if fingerprint(before) != fingerprint(after) or len(raw) != before.st_size:
        raise StrictError(f"stale read detected: {path}")
    return raw


def checked_file(path: Path, expected: str, *, root: Path | None = None) -> dict[str, Any]:
    raw = stable_read(path, root=root)
    got = sha256_bytes(raw)
    if got != expected:
        raise StrictError(f"authority drift for {path}: {got} != {expected}")
    return {"path": str(path), "sha256": got, "size_bytes": len(raw)}


Permutation = tuple[int, ...]
IDENTITY: Permutation = tuple(range(27))


def one_to_zero(rows: Sequence[Sequence[int]]) -> tuple[Permutation, ...]:
    answer: list[Permutation] = []
    target = list(range(1, 28))
    for row in rows:
        if type(row) is not list or any(type(x) is not int for x in row) or sorted(row) != target:
            raise StrictError("row is not a strict permutation of 1..27")
        answer.append(tuple(x - 1 for x in row))
    return tuple(answer)


def one_based(value: Permutation) -> list[int]:
    return [x + 1 for x in value]


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Left after right: (left o right)(i)=left(right(i))."""
    return tuple(left[right[i]] for i in range(27))


def inverse(value: Permutation) -> Permutation:
    out = [0] * 27
    for i, image in enumerate(value):
        out[image] = i
    return tuple(out)


def conjugate(carrier: Permutation, element: Permutation) -> Permutation:
    return compose(carrier, compose(element, inverse(carrier)))


def generated(generators: Sequence[Permutation]) -> frozenset[Permutation]:
    gens = tuple(generators)
    found = {IDENTITY}
    queue: deque[Permutation] = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in gens:
            new = compose(generator, current)
            if new not in found:
                found.add(new)
                queue.append(new)
    return frozenset(found)


def small_generating_set(group: frozenset[Permutation]) -> tuple[Permutation, ...]:
    gens: list[Permutation] = []
    closure = frozenset({IDENTITY})
    for element in sorted(group):
        if element not in closure:
            gens.append(element)
            closure = generated(gens)
    if closure != group:
        raise StrictError("failed to generate subgroup")
    return tuple(gens)


def canonical_group_arrays(group: frozenset[Permutation]) -> list[list[int]]:
    return [one_based(x) for x in sorted(group)]


def group_sha(group: frozenset[Permutation]) -> str:
    return sha256_bytes(canonical(canonical_group_arrays(group)))


def normalizer(ambient: frozenset[Permutation], group: frozenset[Permutation], gens: Sequence[Permutation]) -> frozenset[Permutation]:
    return frozenset(
        g for g in ambient
        if all(conjugate(g, h) in group for h in gens)
    )


def core(ambient_gens: Sequence[Permutation], group: frozenset[Permutation]) -> frozenset[Permutation]:
    current = group
    carriers = tuple(ambient_gens) + tuple(inverse(g) for g in ambient_gens)
    while True:
        old = current
        for carrier in carriers:
            current = frozenset(set(current).intersection(conjugate(carrier, x) for x in current))
        if current == old:
            return current


def find_conjugator(
    ambient: Iterable[Permutation], source: frozenset[Permutation], target: frozenset[Permutation], source_gens: Sequence[Permutation]
) -> Permutation | None:
    if len(source) != len(target):
        return None
    for carrier in ambient:
        if all(conjugate(carrier, h) in target for h in source_gens):
            return carrier
    return None


def canonical_right_cosets(
    ambient: frozenset[Permutation], subgroup: frozenset[Permutation]
) -> tuple[list[Permutation], dict[Permutation, int]]:
    unseen = set(ambient)
    reps: list[Permutation] = []
    mapping: dict[Permutation, int] = {}
    # Scan a once-sorted ambient list.  Repeated min(unseen) is quadratic for
    # the identity subgroup (51,840 singleton cosets).
    for rep in sorted(ambient):
        if rep not in unseen:
            continue
        coset = {compose(rep, h) for h in subgroup}
        if not coset <= unseen:
            raise StrictError("right cosets overlap")
        index = len(reps)
        reps.append(rep)
        for element in coset:
            mapping[element] = index
        unseen.difference_update(coset)
    if unseen:
        raise StrictError("right-coset scan left unseen elements")
    if len(mapping) != len(ambient):
        raise StrictError("right cosets do not cover ambient group")
    return reps, mapping


def double_coset_rows(
    ambient: frozenset[Permutation], left: frozenset[Permutation], left_gens: Sequence[Permutation],
    right: frozenset[Permutation], right_gens: Sequence[Permutation], lane: str,
) -> list[dict[str, Any]]:
    reps, mapping = canonical_right_cosets(ambient, right)
    unseen = set(range(len(reps)))
    rows: list[dict[str, Any]] = []
    while unseen:
        seed = min(unseen)
        representative = reps[seed]
        orbit = {mapping[compose(h, representative)] for h in left}
        if not orbit <= unseen:
            raise StrictError("left orbits on right cosets overlap")
        unseen.difference_update(orbit)
        right_conjugate_gens = tuple(conjugate(representative, h) for h in right_gens)
        right_conjugate = frozenset(conjugate(representative, h) for h in right)
        intersection = left.intersection(right_conjugate)
        join = generated(tuple(left_gens) + right_conjugate_gens)
        if len(orbit) * len(intersection) != len(left):
            raise StrictError("double-coset orbit-stabilizer failure")
        rows.append({
            "lane": lane,
            "seed": seed,
            "representative_one_based": one_based(representative),
            "representative_sha256": sha256_bytes(canonical(one_based(representative))),
            "right_coset_orbit": sorted(orbit),
            "orbit_size": len(orbit),
            "intersection": intersection,
            "join": join,
            "intersection_order": len(intersection),
            "join_order": len(join),
            "simple_factor_degree": len(ambient) // len(intersection),
            "base_field_degree": len(ambient) // len(join),
        })
    rows.sort(key=lambda row: (row["simple_factor_degree"], row["seed"]))
    return rows


class CosetAction:
    def __init__(self, ambient: frozenset[Permutation], subgroup: frozenset[Permutation]) -> None:
        self.representatives, self.mapping = canonical_right_cosets(ambient, subgroup)
        self.degree = len(self.representatives)

    def image(self, element: Permutation, coset: int) -> int:
        return self.mapping[compose(element, self.representatives[coset])]

    def orbits(self, subgroup: frozenset[Permutation], domain: Iterable[int] | None = None) -> list[list[int]]:
        unseen = set(range(self.degree) if domain is None else domain)
        result: list[list[int]] = []
        while unseen:
            seed = min(unseen)
            orbit = {self.image(h, seed) for h in subgroup}
            if not orbit <= unseen:
                raise StrictError("coset action orbits overlap")
            unseen.difference_update(orbit)
            result.append(sorted(orbit))
        return result


def local_prime_rows(
    action: CosetAction, D: frozenset[Permutation], I: frozenset[Permutation],
    P: frozenset[Permutation], Q: frozenset[Permutation],
) -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for orbit in action.orbits(D):
        n = len(orbit)
        f = len(action.orbits(I, orbit))
        p_count = len(action.orbits(P, orbit))
        q_count = len(action.orbits(Q, orbit))
        if n % f:
            raise StrictError("nonintegral local e")
        e = n // f
        numerator = 2 * (n - f) + (n - p_count) + 2 * (n - q_count)
        if numerator % (2 * f):
            raise StrictError("nonintegral local different")
        rows.append({"orbit_seed": orbit[0], "n": n, "e": e, "f": f, "d": numerator // (2 * f)})
    return rows


def local_table(action: CosetAction, D: frozenset[Permutation], I: frozenset[Permutation], P: frozenset[Permutation], Q: frozenset[Permutation]) -> dict[str, Any]:
    raw = local_prime_rows(action, D, I, P, Q)
    counts = Counter((r["n"], r["e"], r["f"], r["d"]) for r in raw)
    collected = [
        {"n": key[0], "e": key[1], "f": key[2], "d": key[3], "multiplicity": counts[key]}
        for key in sorted(counts)
    ]
    return {
        "uncollected_rows": raw,
        "collected_rows": collected,
        "degree_total": sum(r["n"] for r in raw),
        "different_total": sum(r["f"] * r["d"] for r in raw),
        "factor_count": len(raw),
    }


def run_git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO, check=False, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True, env={**os.environ, "LC_ALL": "C"},
    )
    if proc.returncode != 0:
        raise StrictError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def run_git_bytes(*args: str) -> bytes:
    proc = subprocess.run(
        ["git", *args], cwd=REPO, check=False, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env={**os.environ, "LC_ALL": "C"},
    )
    if proc.returncode != 0 or proc.stderr:
        detail = proc.stderr.decode("utf-8", "replace").strip()
        raise StrictError(f"git {' '.join(args)} failed: {detail}")
    return proc.stdout


def released_blob(relative: Path) -> bytes:
    if relative.is_absolute() or ".." in relative.parts:
        raise StrictError(f"unsafe released path: {relative}")
    return run_git_bytes("cat-file", "blob", f"{P60}:{relative.as_posix()}")


def verify_full_manifest(raw: bytes) -> dict[str, Any]:
    lines = raw.decode("ascii", errors="strict").splitlines()
    previous = ""
    seen: set[str] = set()
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise StrictError("malformed C60 full-manifest row")
        digest, relative = line[:64], line[66:]
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise StrictError("invalid C60 manifest digest")
        if relative <= previous or relative in seen or relative.startswith("/") or ".." in Path(relative).parts:
            raise StrictError("C60 full manifest is not unique/path-sorted/safe")
        path = PROJECT / relative
        if sha256_bytes(released_blob(path)) != digest:
            raise StrictError(f"C60 manifest entry drift: {relative}")
        previous = relative
        seen.add(relative)
    return {"entry_count": len(lines), "all_entries_verified": True}


def target_lock_hashes() -> dict[str, Any]:
    """Bind only the frozen target-lock inputs, never the later code/results set."""
    project_root = REPO / "henon_dynamics" / PROJECT_BASENAME
    roots = [project_root / name for name in TARGET_LOCK_ROOT_FILES]
    if any(path.is_symlink() for path in roots):
        raise StrictError("target-lock root symlink rejected")
    root_lines = b"".join(
        f"{sha256_bytes(stable_read(path, root=project_root))}  {path.name}\n".encode("ascii")
        for path in roots
    )
    all_files = [REPO / "henon_dynamics/BATCH_PLAN_C57_C61.md"] + roots + [
        project_root / "route_a_evaluation.yaml"
    ]
    all_files.sort(key=lambda path: path.relative_to(REPO / "henon_dynamics").as_posix())
    exact15_lines = b"".join(
        (
            f"{sha256_bytes(stable_read(path, root=REPO / 'henon_dynamics'))}  "
            f"{path.relative_to(REPO / 'henon_dynamics').as_posix()}\n"
        ).encode("ascii")
        for path in all_files
    )
    route = project_root / "route_a_evaluation.yaml"
    batch = REPO / "henon_dynamics/BATCH_PLAN_C57_C61.md"
    observed = {
        "formal_13_root_sha256": sha256_bytes(root_lines),
        "formal_route_sha256": sha256_bytes(stable_read(route, root=REPO)),
        "formal_batch_sha256": sha256_bytes(stable_read(batch, root=REPO)),
        "formal_exact15_sha256": sha256_bytes(exact15_lines),
        "formal_root_count": 13,
        "formal_exact15_count": 15,
        "formal_exact15_size_bytes": sum(p.stat().st_size for p in all_files),
        "runtime_input_root": str(REPO / "henon_dynamics"),
        "later_code_results_inventory_owned_by_release_runner": True,
    }
    expected_values = (
        FORMAL_13_ROOT_SHA256, FORMAL_ROUTE_SHA256,
        FORMAL_BATCH_SHA256, FORMAL_EXACT15_SHA256,
    )
    if any(v is None for v in expected_values):
        raise StrictError("installed target-lock tuple is incomplete")
    checks = {
        "formal_13_root_sha256": FORMAL_13_ROOT_SHA256,
        "formal_route_sha256": FORMAL_ROUTE_SHA256,
        "formal_batch_sha256": FORMAL_BATCH_SHA256,
        "formal_exact15_sha256": FORMAL_EXACT15_SHA256,
    }
    for key, expected in checks.items():
        if observed[key] != expected:
            raise StrictError(f"formal authority drift in {key}")
    observed["authority_status"] = "INSTALLED_TARGET_LOCK_HASHES_RECOMPUTED"
    observed["all_installed_hashes_recomputed"] = True
    return observed


def bind_authority() -> tuple[dict[str, Any], dict[str, Any]]:
    if not __debug__:
        raise StrictError("optimized Python is forbidden")
    head = run_git("rev-parse", "HEAD")
    tree = run_git("rev-parse", "HEAD^{tree}")
    parent = run_git("rev-parse", "HEAD^")
    origin = run_git("rev-parse", "refs/remotes/origin/main")
    if (head, tree, parent, origin) != (P60, P60_TREE, P60_PARENT, P60):
        raise StrictError("released P60 ref/tree/parent drift")
    files: dict[str, Any] = {}
    raw_by_label: dict[str, bytes] = {}
    for label, (relative, expected) in EXPECTED_FILES.items():
        raw = released_blob(relative)
        got = sha256_bytes(raw)
        if got != expected:
            raise StrictError(f"released file drift: {label}")
        files[label] = {
            "relative_path": relative.as_posix(), "sha256": got,
            "size_bytes": len(raw), "source": f"immutable_git_blob_at_{P60}",
        }
        raw_by_label[label] = raw
    manifest_check = verify_full_manifest(raw_by_label["c60_full_manifest"])
    if raw_by_label["c60_live_route"] != raw_by_label["c60_archive_route"]:
        raise StrictError("C60 live/archive Route bytes differ")
    certificate = strict_json(raw_by_label["c60_certificate"], "C60 certificate")
    if set(certificate) != {"payload", "payload_sha256", "schema", "schema_sha256"}:
        raise StrictError("C60 certificate top-level schema drift")
    if certificate["payload_sha256"] != EXPECTED_C60_PAYLOAD_SHA256 or sha256_bytes(canonical(certificate["payload"])) != EXPECTED_C60_PAYLOAD_SHA256:
        raise StrictError("C60 payload hash drift")
    source_contract = certificate["payload"]["source_contract"]
    if sha256_bytes(canonical(source_contract)) != EXPECTED_C60_SOURCE_CONTRACT_SHA256:
        raise StrictError("C60 source-contract hash drift")
    group_evidence = strict_json(raw_by_label["c60_group_evidence"], "C60 group evidence")
    arrays_block = group_evidence["frozen_permutation_arrays"]
    arrays = arrays_block["arrays"]
    if arrays_block["canonical_sha256"] != EXPECTED_FROZEN_ARRAYS_SHA256 or sha256_bytes(canonical(arrays)) != EXPECTED_FROZEN_ARRAYS_SHA256:
        raise StrictError("C60 frozen arrays hash drift")
    formal = target_lock_hashes()
    authority = {
        "repository": {"head": head, "origin_main": origin, "tree": tree, "sole_parent": parent},
        "released_files": files,
        "c60_manifest_verification": manifest_check,
        "c60_payload_sha256": EXPECTED_C60_PAYLOAD_SHA256,
        "c60_source_contract_sha256": EXPECTED_C60_SOURCE_CONTRACT_SHA256,
        "c60_frozen_arrays_sha256": EXPECTED_FROZEN_ARRAYS_SHA256,
        "formal_input": formal,
        "pilot_runtime_inputs": [],
    }
    return authority, arrays


class Registry:
    def __init__(self, ambient: frozenset[Permutation], ambient_gens: Sequence[Permutation]) -> None:
        self.ambient = ambient
        self.ambient_gens = tuple(ambient_gens)
        self.groups: dict[str, dict[str, Any]] = {}
        self.group_by_sha: dict[str, frozenset[Permutation]] = {}
        self.gens_by_sha: dict[str, tuple[Permutation, ...]] = {}
        self.stats_cache: dict[str, dict[str, Any]] = {}

    def add(self, group: frozenset[Permutation], gens: Sequence[Permutation] | None = None) -> str:
        digest = group_sha(group)
        if digest not in self.groups:
            chosen = tuple(gens) if gens is not None and generated(tuple(gens)) == group else small_generating_set(group)
            self.groups[digest] = {
                "sha256": digest,
                "order": len(group),
                "generators_one_based": [one_based(x) for x in chosen],
            }
            self.group_by_sha[digest] = group
            self.gens_by_sha[digest] = chosen
        return digest

    def stats(self, group: frozenset[Permutation], gens: Sequence[Permutation] | None = None) -> dict[str, Any]:
        digest = self.add(group, gens)
        if digest in self.stats_cache:
            return deepcopy(self.stats_cache[digest])
        chosen = self.gens_by_sha[digest]
        if group == self.ambient:
            nrm = self.ambient
            cr = self.ambient
        else:
            nrm = normalizer(self.ambient, group, chosen)
            cr = core(self.ambient_gens, group)
        nrm_sha = self.add(nrm, self.ambient_gens if nrm == self.ambient else None)
        cr_sha = self.add(cr)
        row = {
            "group_sha256": digest,
            "order": len(group),
            "normalizer_order": len(nrm),
            "normalizer_sha256": nrm_sha,
            "core_order": len(cr),
            "core_sha256": cr_sha,
            "automorphism_order": len(nrm) // len(group),
        }
        self.stats_cache[digest] = row
        return deepcopy(row)


EXPECTED_ROW_TYPES = {
    "Tpp": [(0,"Q1","P1"),(201,"Q1","P1"),(2,"Q2","P2"),(196,"Q2","P2"),(69,"Q3","P3"),(59,"Q4","P4"),(68,"Q4","P4"),(1,"Q5","P4"),(16,"Q5","P4"),(52,"Q6","P4"),(3,"Q7","P4"),(13,"Q7","P4")],
    "Tpm": [(148,"Q8","P5"),(24,"Q9","P3"),(178,"Q9","P3"),(149,"Q10","P6"),(2,"Q11","P4"),(3,"Q11","P4"),(12,"Q12","P4"),(169,"Q12","P4"),(0,"Q13","P4"),(1,"Q13","P4"),(7,"Q14","P4"),(4,"Q15","P4")],
    "Tmm": [(0,"Q16","P7"),(298,"Q16","P7"),(1,"Q17","P8"),(13,"Q17","P8"),(86,"Q3","P3"),(46,"Q4","P4"),(62,"Q4","P4"),(2,"Q18","P4"),(18,"Q18","P4"),(32,"Q6","P4"),(3,"Q7","P4"),(6,"Q7","P4")],
}


def classify_rows(
    rows_by_lane: dict[str, list[dict[str, Any]]], ambient: frozenset[Permutation], registry: Registry
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    q_classes: list[tuple[frozenset[Permutation], tuple[Permutation, ...], str]] = []
    p_classes: list[tuple[frozenset[Permutation], tuple[Permutation, ...], str]] = []
    ambient_ordered = sorted(ambient)
    for lane in ("Tpp", "Tpm", "Tmm"):
        for row in rows_by_lane[lane]:
            for prefix, group_key, class_list in (
                ("Q", "intersection", q_classes), ("P", "join", p_classes)
            ):
                group = row[group_key]
                gens = small_generating_set(group)
                found: tuple[str, Permutation] | None = None
                for representative, _, label in class_list:
                    witness = find_conjugator(ambient_ordered, group, representative, gens)
                    if witness is not None:
                        found = (label, witness)
                        break
                if found is None:
                    label = f"{prefix}{len(class_list)+1}"
                    class_list.append((group, gens, label))
                    witness = IDENTITY
                else:
                    label, witness = found
                row[f"{prefix}_type"] = label
                row[f"{prefix}_type_conjugator_one_based"] = one_based(witness)
                row[f"{prefix}_type_conjugator_sha256"] = sha256_bytes(canonical(one_based(witness)))
            i_stats = registry.stats(row["intersection"])
            j_stats = registry.stats(row["join"])
            row["intersection_stats"] = i_stats
            row["join_stats"] = j_stats
    q_types: dict[str, dict[str, Any]] = {}
    p_types: dict[str, dict[str, Any]] = {}
    for representative, gens, label in q_classes:
        q_types[label] = {"label": label, "representative": registry.stats(representative, gens)}
    for representative, gens, label in p_classes:
        p_types[label] = {"label": label, "representative": registry.stats(representative, gens)}
    if len(q_types) != 18 or len(p_types) != 8:
        raise StrictError(f"unified type count drift: {len(q_types)}/{len(p_types)}")
    return q_types, p_types


def class_label_for(
    group: frozenset[Permutation], types: dict[str, dict[str, Any]], registry: Registry,
    ambient_ordered: Sequence[Permutation], prefix: str,
) -> tuple[str, Permutation]:
    gens = small_generating_set(group)
    for index in range(1, len(types) + 1):
        label = f"{prefix}{index}"
        representative = registry.group_by_sha[types[label]["representative"]["group_sha256"]]
        witness = find_conjugator(ambient_ordered, group, representative, gens)
        if witness is not None:
            return label, witness
    raise StrictError(f"unclassified {prefix} subgroup")


def serialize_tensor_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "lane": row["lane"],
        "seed": row["seed"],
        "representative_one_based": row["representative_one_based"],
        "representative_sha256": row["representative_sha256"],
        "right_coset_orbit": row["right_coset_orbit"],
        "orbit_size": row["orbit_size"],
        "Q_type": row["Q_type"],
        "P_type": row["P_type"],
        "Q_type_conjugator_one_based": row["Q_type_conjugator_one_based"],
        "Q_type_conjugator_sha256": row["Q_type_conjugator_sha256"],
        "P_type_conjugator_one_based": row["P_type_conjugator_one_based"],
        "P_type_conjugator_sha256": row["P_type_conjugator_sha256"],
        "intersection": row["intersection_stats"],
        "join": row["join_stats"],
        "simple_factor_degree": row["simple_factor_degree"],
        "base_field_degree": row["base_field_degree"],
    }


def conjugates_by_normalizer(
    ambient: frozenset[Permutation], subgroup: frozenset[Permutation], subgroup_gens: Sequence[Permutation]
) -> tuple[list[dict[str, Any]], list[frozenset[Permutation]], list[tuple[Permutation, ...]]]:
    nrm = normalizer(ambient, subgroup, subgroup_gens)
    reps, _ = canonical_right_cosets(ambient, nrm)
    conjugates: list[frozenset[Permutation]] = []
    conjugate_gens: list[tuple[Permutation, ...]] = []
    rows: list[dict[str, Any]] = []
    for index, representative in enumerate(reps):
        group = frozenset(conjugate(representative, h) for h in subgroup)
        gens = tuple(conjugate(representative, h) for h in subgroup_gens)
        if generated(gens) != group:
            raise StrictError("conjugate generators failed")
        conjugates.append(group)
        conjugate_gens.append(gens)
        rows.append({
            "index": index,
            "conjugator_one_based": one_based(representative),
            "conjugator_sha256": sha256_bytes(canonical(one_based(representative))),
            "conjugate_group_sha256": group_sha(group),
        })
    if len(set(conjugates)) != len(conjugates):
        raise StrictError("normalizer cosets did not give distinct conjugates")
    return rows, conjugates, conjugate_gens


def character_from_conjugates(
    ambient: frozenset[Permutation], subgroup: frozenset[Permutation], conjugates: Sequence[frozenset[Permutation]]
) -> list[int]:
    if not conjugates or (len(ambient) // len(subgroup)) % len(conjugates):
        raise StrictError("invalid character/conjugate multiplicity")
    multiplicity = (len(ambient) // len(subgroup)) // len(conjugates)
    incidence: Counter[Permutation] = Counter()
    for group in conjugates:
        incidence.update(group)
    return [multiplicity * incidence[element] for element in sorted(ambient)]


def arithmetic_input(
    ambient: frozenset[Permutation], field: frozenset[Permutation],
    local_groups: dict[str, frozenset[Permutation]],
) -> dict[str, Any]:
    action = CosetAction(ambient, field)
    order = ["I3", "P3", "Q3", "I5", "P5", "C3", "C2", "Cinf"]
    counts = [len(action.orbits(local_groups[label])) for label in order]
    degree = action.degree
    i3, p3, q3, i5, p5, c3, c2, cinf = counts
    numerator3 = 2 * (degree - i3) + (degree - p3) + 2 * (degree - q3)
    numerator5 = 4 * (degree - i5) + 3 * (degree - p5)
    if numerator3 % 2 or numerator5 % 4:
        raise StrictError("global conductor formula is nonintegral")
    signature = [2 * cinf - degree, degree - cinf]
    if signature[0] < 0 or signature[1] < 0 or signature[0] + 2 * signature[1] != degree:
        raise StrictError("invalid signature input")
    tom140 = local_table(
        action, local_groups["D140"], local_groups["I140"],
        local_groups["P140"], local_groups["Q140"],
    )
    tom206 = local_table(
        action, local_groups["D206"], local_groups["I206"],
        local_groups["P206"], local_groups["Q206"],
    )
    if tom140["degree_total"] != degree or tom206["degree_total"] != degree:
        raise StrictError("local table degree drift")
    if tom140["different_total"] != numerator3 // 2 or tom206["different_total"] != numerator3 // 2:
        raise StrictError("local/global p=3 different mismatch")
    return {
        "degree": degree,
        "orbit_count_order": order,
        "orbit_counts": counts,
        "conductor_exponent_order": ["p3", "p5", "Pi_A", "Pi_B"],
        "conductor_exponents": [numerator3 // 2, numerator5 // 4, degree - c3, degree - c2],
        "signature_r1_r2": signature,
        "discriminant_positive": signature[1] % 2 == 0,
        "tom140": tom140,
        "tom206": tom206,
    }


def build_python_projection(authority: dict[str, Any], arrays: dict[str, Any]) -> tuple[dict[str, Any], Registry]:
    w_gens = one_to_zero(arrays["W27_generators"])
    hp_gens = one_to_zero(arrays["H301_generators"])
    hm_gens = one_to_zero(arrays["H303_generators"])
    W = generated(w_gens)
    Hp = generated(hp_gens)
    Hm = generated(hm_gens)
    if (len(W), len(Hp), len(Hm)) != (51_840, 162, 162):
        raise StrictError("released W/H+/H- orders drifted")
    registry = Registry(W, w_gens)
    w_sha = registry.add(W, w_gens)
    hp_sha = registry.add(Hp, hp_gens)
    hm_sha = registry.add(Hm, hm_gens)
    if w_sha != "f447fdf7677c795b034f567bcc259b6cfbb476d386b19a4a1f0275963eca034e":
        raise StrictError("W complete-set hash drift")
    if hp_sha != "b7f57af7db4e2f6f3942efbb3568d8deb3161bba3a6b3c42360b6042fef28a2c":
        raise StrictError("H+ complete-set hash drift")

    rows_by_lane = {
        "Tpp": double_coset_rows(W, Hp, hp_gens, Hp, hp_gens, "Tpp"),
        "Tpm": double_coset_rows(W, Hp, hp_gens, Hm, hm_gens, "Tpm"),
        "Tmm": double_coset_rows(W, Hm, hm_gens, Hm, hm_gens, "Tmm"),
    }
    if any(len(rows) != 12 for rows in rows_by_lane.values()):
        raise StrictError("tensor double-coset count is not 12/12/12")
    q_types, p_types = classify_rows(rows_by_lane, W, registry)
    for lane, expected in EXPECTED_ROW_TYPES.items():
        observed = [(r["seed"], r["Q_type"], r["P_type"]) for r in rows_by_lane[lane]]
        if observed != expected:
            raise StrictError(f"canonical row/type atlas drift in {lane}")
    serialized_rows = {
        lane: [serialize_tensor_row(row) for row in rows]
        for lane, rows in rows_by_lane.items()
    }
    spectra = {lane: [r["simple_factor_degree"] for r in rows] for lane, rows in serialized_rows.items()}
    dimensions = {lane: sum(values) for lane, values in spectra.items()}
    if set(dimensions.values()) != {102_400}:
        raise StrictError("tensor dimension drift")

    # Enumerate both full conjugacy families and reconstruct characters on all
    # 51,840 canonical ambient elements, not just database class locators.
    hp_conjugate_rows, hp_conjugates, _ = conjugates_by_normalizer(W, Hp, hp_gens)
    hm_conjugate_rows, hm_conjugates, hm_conjugate_gens = conjugates_by_normalizer(W, Hm, hm_gens)
    if len(hp_conjugates) != 160 or len(hm_conjugates) != 160:
        raise StrictError("H+/H- conjugate count drift")
    char_plus = character_from_conjugates(W, Hp, hp_conjugates)
    char_minus = character_from_conjugates(W, Hm, hm_conjugates)
    if char_plus != char_minus:
        raise StrictError("released Gassmann character equality failed")
    square_character = [x * x for x in char_plus]
    if find_conjugator(sorted(W), Hp, Hm, hp_gens) is not None:
        raise StrictError("released H+/H- unexpectedly conjugate")

    # Complete 160-position mixed atlas.  Relative orbits are discovered from
    # H+ conjugation; no order/degree target filter participates.
    q_index = {group: index for index, group in enumerate(hm_conjugates)}
    unseen = set(range(160))
    relative_types_raw: list[dict[str, Any]] = []
    ambient_ordered = sorted(W)
    raw_type_for_index: dict[int, int] = {}
    while unseen:
        seed = min(unseen)
        q = hm_conjugates[seed]
        orbit = {
            q_index[frozenset(conjugate(h, element) for element in q)]
            for h in Hp
        }
        if not orbit <= unseen:
            raise StrictError("mixed relative-position orbits overlap")
        unseen.difference_update(orbit)
        inter = Hp.intersection(q)
        join = generated(tuple(hp_gens) + hm_conjugate_gens[seed])
        q_label, q_witness = class_label_for(inter, q_types, registry, ambient_ordered, "Q")
        p_label, p_witness = class_label_for(join, p_types, registry, ambient_ordered, "P")
        relative_types_raw.append({
            "representative_conjugate_index": seed,
            "raw_conjugate_indices": sorted(orbit),
            "raw_count": len(orbit),
            "Q_type": q_label,
            "P_type": p_label,
            "Q_type_conjugator_one_based": one_based(q_witness),
            "Q_type_conjugator_sha256": sha256_bytes(canonical(one_based(q_witness))),
            "P_type_conjugator_one_based": one_based(p_witness),
            "P_type_conjugator_sha256": sha256_bytes(canonical(one_based(p_witness))),
            "intersection": registry.stats(inter),
            "join": registry.stats(join),
            "compositum_degree": len(W) // len(inter),
            "base_field_degree": len(W) // len(join),
        })
    relative_types_raw.sort(key=lambda r: (r["compositum_degree"], r["base_field_degree"], r["raw_count"], r["representative_conjugate_index"]))
    q_multiplicity = Counter(row["Q_type"] for row in serialized_rows["Tpm"])
    relative_types: list[dict[str, Any]] = []
    for type_index, row in enumerate(relative_types_raw, 1):
        row["relative_position_type"] = type_index
        row["tensor_factor_multiplicity"] = q_multiplicity[row["Q_type"]]
        relative_types.append(row)
        for index in row["raw_conjugate_indices"]:
            raw_type_for_index[index] = type_index
    if len(relative_types) != 8 or sorted(raw_type_for_index) != list(range(160)):
        raise StrictError("mixed 160/8 atlas drift")
    if [r["tensor_factor_multiplicity"] for r in relative_types] != [1,2,1,2,2,2,1,1]:
        raise StrictError("mixed 12-to-8 multiplicity drift")
    raw_positions: list[dict[str, Any]] = []
    for row, group in zip(hm_conjugate_rows, hm_conjugates):
        registry.add(group)
        enriched = dict(row)
        enriched["relative_position_type"] = raw_type_for_index[row["index"]]
        raw_positions.append(enriched)

    # Exact P3 conjugator and the nonconjugate Fourier/mixed P6 class.
    lookup = {(lane, row["seed"]): row for lane, rows in rows_by_lane.items() for row in rows}
    plus_p3 = lookup[("Tpp", 69)]["join"]
    minus_p3 = lookup[("Tmm", 86)]["join"]
    mixed_p6 = lookup[("Tpm", 149)]["join"]
    p3_witness = one_to_zero([P3_WITNESS_ONE_BASED])[0]
    p3_image = frozenset(conjugate(p3_witness, element) for element in minus_p3)
    if p3_image != plus_p3:
        raise StrictError("exact P3 witness failed complete-set equality")
    if find_conjugator(ambient_ordered, plus_p3, mixed_p6, small_generating_set(plus_p3)) is not None:
        raise StrictError("self P3 became conjugate to mixed P6")

    # Degree-640 mixed recovery is an equality of complete embedded groups with
    # released C60 J/N, not merely equality of orders or hashes.
    c60_J = generated(one_to_zero(arrays["J_generators"]))
    c60_N = generated(one_to_zero(arrays["N_generators"]))
    mixed_640 = lookup[("Tpm", 148)]
    if mixed_640["intersection"] != c60_J or mixed_640["join"] != c60_N:
        raise StrictError("mixed degree-640 C60 J/N recovery failed")

    # Raw arithmetic input for all 18 Q and 8 P types.  This is finite-group
    # orbit/tower data only; the arithmetic/resolvent lane must independently
    # consume and validate it before making any arithmetic theorem claim.
    local_groups = {
        "D140": generated(one_to_zero(arrays["branch140_D_generators"])),
        "I140": generated(one_to_zero(arrays["branch140_D_generators"])),
        "P140": generated(one_to_zero(arrays["branch140_P_generators"])),
        "Q140": generated(one_to_zero(arrays["branch140_Q_generators"])),
        "D206": generated(one_to_zero(arrays["branch206_D_generators"])),
        "I206": generated(one_to_zero(arrays["branch206_I_generators"])),
        "P206": generated(one_to_zero(arrays["branch206_P_generators"])),
        "Q206": generated(one_to_zero(arrays["branch206_Q_generators"])),
        "I5": generated(one_to_zero(GLOBAL_LOCAL_ARRAYS["I5_tom147"])),
        "P5": generated(one_to_zero(GLOBAL_LOCAL_ARRAYS["P5_tom23"])),
        "C3": generated(one_to_zero(GLOBAL_LOCAL_ARRAYS["C3_tom6"])),
        "C2": generated(one_to_zero(GLOBAL_LOCAL_ARRAYS["C2_tom2"])),
        "Cinf": generated(one_to_zero(GLOBAL_LOCAL_ARRAYS["Cinf_tom5"])),
    }
    local_groups.update({
        "I3": local_groups["I140"],
        "P3": local_groups["P140"],
        "Q3": local_groups["Q140"],
    })
    expected_local_orders = {
        "D140":18,"I140":18,"P140":9,"Q140":3,
        "D206":36,"I206":18,"P206":9,"Q206":3,
        "I5":20,"P5":5,"C3":3,"C2":2,"Cinf":2,
        "I3":18,"P3":9,"Q3":3,
    }
    if {k:len(v) for k,v in local_groups.items()} != expected_local_orders:
        raise StrictError("local subgroup order contract drift")
    local_group_contract = {
        label: {"group_sha256": registry.add(group), "order": len(group)}
        for label, group in local_groups.items()
    }
    arithmetic_rows: list[dict[str, Any]] = []
    arithmetic_cache: dict[str, dict[str, Any]] = {}
    for prefix, types in (("Q", q_types), ("P", p_types)):
        for index in range(1, len(types) + 1):
            label = f"{prefix}{index}"
            digest = types[label]["representative"]["group_sha256"]
            field = registry.group_by_sha[digest]
            if digest not in arithmetic_cache:
                arithmetic_cache[digest] = arithmetic_input(W, field, local_groups)
            arithmetic_rows.append({
                "type_label": label,
                "field_subgroup_sha256": digest,
                **deepcopy(arithmetic_cache[digest]),
            })

    q_multisets = {
        lane: [row["Q_type"] for row in rows]
        for lane, rows in serialized_rows.items()
    }
    if q_multisets["Tpp"] == q_multisets["Tmm"] or q_multisets["Tpp"] == q_multisets["Tpm"] or q_multisets["Tpm"] == q_multisets["Tmm"]:
        raise StrictError("three Burnside products failed pairwise separation")

    projection = {
        "schema_id": "hcs-c61-python-group-projection-v1",
        "authority_rebound": authority,
        "conventions": {
            "carrier_degree": 27,
            "permutation_arrays": "one_based",
            "composition": "left_after_right",
            "canonical_group_serialization": "lexicographically_sorted_complete_one_based_arrays",
            "promoted_registry_serialization": "canonical_generators_order_and_complete_set_sha256",
            "right_coset_enumeration": "least_unseen_ambient_element",
            "target_degree_or_order_filters_used": False,
        },
        "ambient": {
            "W_group_sha256": w_sha,
            "Hplus_group_sha256": hp_sha,
            "Hminus_group_sha256": hm_sha,
            "W_generators_one_based": arrays["W27_generators"],
            "Hplus_generators_one_based": arrays["H301_generators"],
            "Hminus_generators_one_based": arrays["H303_generators"],
            "orders_W_Hplus_Hminus": [len(W), len(Hp), len(Hm)],
            "W_permutation_count": len(W),
            "W_distinct_labelled_permutation_count": len(set(W)),
            "labelled_W_action_faithful": len(W) == len(set(W)),
        },
        "tensor_atlas": {
            "rows": serialized_rows,
            "row_counts": {lane: len(rows) for lane, rows in serialized_rows.items()},
            "degree_spectra": spectra,
            "dimensions": dimensions,
            "Q_types": q_types,
            "P_types": p_types,
            "Q_type_count": len(q_types),
            "P_type_count": len(p_types),
            "Q_type_multisets": q_multisets,
        },
        "burnside_linearization": {
            "Hplus_conjugate_count": len(hp_conjugates),
            "Hminus_conjugate_count": len(hm_conjugates),
            "Hplus_Hminus_nonconjugate": True,
            "common_character_values_on_canonical_W": char_plus,
            "common_character_sha256": sha256_bytes(canonical(char_plus)),
            "common_tensor_character_values_on_canonical_W": square_character,
            "common_tensor_character_sha256": sha256_bytes(canonical(square_character)),
            "all_three_linearizations_equal": True,
            "all_three_zeta_products_equal_formal_Artin_consequence": True,
            "three_G_sets_pairwise_nonisomorphic": True,
            "three_field_factor_multisets_pairwise_distinct": True,
            "self_self_separator": "two_degree_320_diagonal_Q1_vs_Q16_types",
            "mixed_self_separator": "degree_multiset",
        },
        "mixed_160_12_8": {
            "conjugate_positions": raw_positions,
            "relative_position_types": relative_types,
            "conjugate_position_count": len(raw_positions),
            "double_coset_factor_count": len(serialized_rows["Tpm"]),
            "Q_isomorphism_type_count": len(relative_types),
            "multiplicities": [r["tensor_factor_multiplicity"] for r in relative_types],
        },
        "P3_P6": {
            "plus_self_seed": 69,
            "minus_self_seed": 86,
            "mixed_fourier_seed": 149,
            "plus_self_join_sha256": group_sha(plus_p3),
            "minus_self_embedded_join_sha256": group_sha(minus_p3),
            "mixed_P6_join_sha256": group_sha(mixed_p6),
            "exact_minus_to_plus_conjugator_one_based": P3_WITNESS_ONE_BASED,
            "exact_minus_to_plus_conjugator_sha256": sha256_bytes(canonical(P3_WITNESS_ONE_BASED)),
            "conjugated_minus_complete_set_equals_plus": True,
            "P3_nonconjugate_to_P6": True,
            "three_pairwise_nonconjugate_joins_claimed": False,
            "seed149_join_role": "source_owned_Tplus_bridge_input_for_independent_resolvent_lane",
        },
        "mixed_degree_640_recovery": {
            "mixed_seed": 148,
            "intersection_equals_released_C60_J_complete_set": True,
            "join_equals_released_C60_N_complete_set": True,
            "intersection_sha256": group_sha(c60_J),
            "join_sha256": group_sha(c60_N),
            "factor_degree": 640,
            "base_degree": 160,
        },
        "raw_global_local_inputs": {
            "local_subgroups": local_group_contract,
            "field_type_rows": arithmetic_rows,
            "downstream_authority_status": "INPUT_ONLY_REQUIRES_INDEPENDENT_RESOLVENT_ARITHMETIC_RECONSTRUCTION",
        },
        "subgroup_registry": {key: registry.groups[key] for key in sorted(registry.groups)},
        "status": "PYTHON_RECONSTRUCTION_PASS",
    }
    return projection, registry


def run_gap_checker(checker: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    checker_raw = stable_read(checker, root=checker.parent)
    gap = Path("/usr/bin/gap")
    gap_raw = stable_read(gap)
    if sha256_bytes(gap_raw) != EXPECTED_GAP_SHA256:
        raise StrictError("GAP executable hash drift")
    proc = subprocess.run(
        [str(gap), "-q", str(checker)], check=False, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, timeout=600,
        env={**os.environ, "LC_ALL": "C", "GAP_COLORS": "false"},
    )
    if proc.returncode != 0:
        raise StrictError(f"GAP checker failed ({proc.returncode}): {proc.stderr.decode(errors='replace')[:2000]}")
    if proc.stderr:
        raise StrictError(f"GAP checker emitted stderr: {proc.stderr.decode(errors='replace')[:2000]}")
    projection = strict_json(proc.stdout, "GAP projection")
    backend = {
        "gap_executable": str(gap),
        "gap_executable_sha256": EXPECTED_GAP_SHA256,
        "checker_source_sha256": sha256_bytes(checker_raw),
        "checker_source_size_bytes": len(checker_raw),
        "projection_sha256": sha256_bytes(canonical(projection)),
        "projection_size_bytes": len(canonical(projection)) + 1,
    }
    return projection, backend


def exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != keys:
        got = set(value) if type(value) is dict else type(value).__name__
        raise StrictError(f"{label} keys/type drift: {got} != {keys}")
    return value


def strict_int(value: Any, label: str, *, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise StrictError(f"invalid integer {label}")
    return value


def strict_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        raise StrictError(f"invalid Boolean {label}")
    return value


def walk_no_float(value: Any, label: str = "root") -> None:
    if type(value) is float:
        raise StrictError(f"float forbidden at {label}")
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise StrictError(f"non-string key at {label}")
            walk_no_float(item, f"{label}.{key}")
    elif type(value) is list:
        for index, item in enumerate(value):
            walk_no_float(item, f"{label}[{index}]")
    elif value is not None and type(value) not in (str, int, bool):
        raise StrictError(f"unsupported leaf at {label}: {type(value).__name__}")


def cross_check_gap(python: dict[str, Any], gap: dict[str, Any]) -> dict[str, Any]:
    exact_keys(gap, {
        "ambient","burnside","local_subgroups","mixed","p3_p6","rows","schema_id",
        "software","status","target_degree_or_order_filters_used","type_counts",
    }, "GAP projection")
    if gap["schema_id"] != CHECKER_SCHEMA_ID or gap["status"] != "PASS":
        raise StrictError("GAP schema/status drift")
    if gap["target_degree_or_order_filters_used"] is not False:
        raise StrictError("GAP target filter flag drift")
    if gap["type_counts"] != {"P": 8, "Q": 18}:
        raise StrictError("GAP Q/P count drift")
    expected_ambient = {
        "W_permutation_count": 51_840,
        "W_distinct_labelled_permutation_count": 51_840,
        "labelled_W_action_faithful": True,
    }
    if gap["ambient"] != expected_ambient:
        raise StrictError("GAP labelled ambient faithfulness/count drift")
    for key, value in expected_ambient.items():
        if python["ambient"][key] != value:
            raise StrictError("Python/GAP labelled ambient faithfulness disagreement")
    row_fields = {
        "base_degree","core_intersection_order","core_join_order",
        "intersection_automorphism_order","intersection_normalizer_order",
        "intersection_order","join_automorphism_order","join_normalizer_order",
        "join_order","lane","orbit_size","p_type","q_type",
        "representative_one_based","seed","simple_degree",
    }
    checked_rows = 0
    for lane in ("Tpp", "Tpm", "Tmm"):
        py_rows = python["tensor_atlas"]["rows"][lane]
        gap_rows = gap["rows"][lane]
        if len(py_rows) != 12 or len(gap_rows) != 12:
            raise StrictError("cross-lane row count drift")
        for py, ga in zip(py_rows, gap_rows):
            exact_keys(ga, row_fields, f"GAP {lane} row")
            expected = {
                "base_degree": py["base_field_degree"],
                "core_intersection_order": py["intersection"]["core_order"],
                "core_join_order": py["join"]["core_order"],
                "intersection_automorphism_order": py["intersection"]["automorphism_order"],
                "intersection_normalizer_order": py["intersection"]["normalizer_order"],
                "intersection_order": py["intersection"]["order"],
                "join_automorphism_order": py["join"]["automorphism_order"],
                "join_normalizer_order": py["join"]["normalizer_order"],
                "join_order": py["join"]["order"],
                "lane": lane,
                "orbit_size": py["orbit_size"],
                "p_type": int(py["P_type"][1:]),
                "q_type": int(py["Q_type"][1:]),
                "representative_one_based": py["representative_one_based"],
                "seed": py["seed"],
                "simple_degree": py["simple_factor_degree"],
            }
            if ga != expected:
                raise StrictError(f"Python/GAP row disagreement: {lane}/{py['seed']}")
            checked_rows += 1
    burnside = gap["burnside"]
    exact_keys(burnside, {
        "Hplus_Hminus_nonconjugate","all_three_linearizations_equal",
        "common_character_values_on_25_classes","common_tensor_character_values_on_25_classes",
    }, "GAP burnside")
    expected_character = [320,0,0,32,8,20,0,0,0,0,0,0,0,2,0,0,16,0,0,0,0,4,0,0,0]
    if burnside["common_character_values_on_25_classes"] != expected_character:
        raise StrictError("GAP 25-class character drift")
    if burnside["common_tensor_character_values_on_25_classes"] != [x*x for x in expected_character]:
        raise StrictError("GAP tensor character product drift")
    if burnside["Hplus_Hminus_nonconjugate"] is not True or burnside["all_three_linearizations_equal"] is not True:
        raise StrictError("GAP Burnside flags drift")
    if gap["p3_p6"] != {
        "P3_nonconjugate_to_P6": True,
        "exact_witness_one_based": P3_WITNESS_ONE_BASED,
        "witness_complete_set_equality": True,
    }:
        raise StrictError("GAP P3/P6 projection drift")
    mixed = gap["mixed"]
    exact_keys(mixed, {
        "conjugate_count","conjugator_arrays_one_based","relative_position_rows","relative_type_count",
    }, "GAP mixed")
    py_conjugators = [row["conjugator_one_based"] for row in python["mixed_160_12_8"]["conjugate_positions"]]
    if mixed["conjugator_arrays_one_based"] != py_conjugators:
        raise StrictError("Python/GAP canonical 160 conjugators disagree")
    if mixed["conjugate_count"] != 160 or mixed["relative_type_count"] != 8:
        raise StrictError("GAP mixed 160/8 count drift")
    for py, ga in zip(python["mixed_160_12_8"]["relative_position_types"], mixed["relative_position_rows"]):
        expected = {
            "base_degree": py["base_field_degree"],
            "intersection_order": py["intersection"]["order"],
            "join_order": py["join"]["order"],
            "p_type": int(py["P_type"][1:]),
            "q_type": int(py["Q_type"][1:]),
            "raw_count": py["raw_count"],
            "representative_conjugate_index": py["representative_conjugate_index"],
            "simple_degree": py["compositum_degree"],
        }
        if ga != expected:
            raise StrictError("Python/GAP relative-position row disagreement")
    local_by_label = {row["label"]: row for row in gap["local_subgroups"]}
    expected_tom = {"D140":140,"P140":72,"Q140":7,"D206":206,"I206":140,"P206":72,"Q206":7,"I5":147,"P5":23,"C3":6,"C2":2,"Cinf":5}
    if set(local_by_label) != set(expected_tom):
        raise StrictError("GAP local subgroup label drift")
    registry = python["subgroup_registry"]
    local_contract = python["raw_global_local_inputs"]["local_subgroups"]
    for label, locator in expected_tom.items():
        row = local_by_label[label]
        if row["tom_locator"] != locator:
            raise StrictError(f"GAP ToM locator drift for {label}")
        group = generated(one_to_zero(row["generators_one_based"]))
        py_label = label
        digest = group_sha(group)
        if digest != local_contract[py_label]["group_sha256"] or digest not in registry:
            raise StrictError(f"Python/GAP local embedded group disagreement for {label}")
    return {
        "complete_tensor_rows_deep_equal": True,
        "tensor_rows_checked": checked_rows,
        "unified_Q_P_grouping_equal": True,
        "mixed_160_conjugators_deep_equal": True,
        "mixed_relative_rows_deep_equal": True,
        "P3_witness_and_P3_not_P6_equal": True,
        "TomLib_local_embedded_groups_equal": True,
        "Burnside_character_products_equal": True,
        "labelled_W_faithfulness_and_counts_equal": True,
    }


def build_document(checker: Path) -> dict[str, Any]:
    authority, arrays = bind_authority()
    if authority["formal_input"]["authority_status"] != "INSTALLED_TARGET_LOCK_HASHES_RECOMPUTED":
        raise StrictError("installed target-lock tuple is not bound")
    python_projection, _ = build_python_projection(authority, arrays)
    # Avoid duplicating the large authority block in the component projection.
    source_contract = python_projection.pop("authority_rebound")
    gap_projection, gap_backend = run_gap_checker(checker)
    cross = cross_check_gap(python_projection, gap_projection)
    source_raw = stable_read(Path(__file__), root=Path(__file__).parent)
    document = {
        "schema_id": SCHEMA_ID,
        "semantic_firewall": FIREWALL,
        "source_contract": source_contract,
        "conventions": python_projection["conventions"],
        "python_projection": python_projection,
        "gap_projection": gap_projection,
        "cross_checks": cross,
        "backend_contract": {
            "python": {
                "implementation": "stdlib_only_no_imported_C60_or_pilot_module",
                "optimized_python_rejected": True,
                "producer_source_sha256": sha256_bytes(source_raw),
                "producer_source_size_bytes": len(source_raw),
            },
            "gap": gap_backend,
            "producer_checker_shared_math_allowed": False,
            "shared_surface": "canonical_JSON_and_source_owned_permutation_literals_only",
            "promoted_evidence_size_ceiling_bytes": PROMOTED_EVIDENCE_SIZE_CEILING_BYTES,
        },
        "component_hashes": {
            "python_projection_sha256": sha256_bytes(canonical(python_projection)),
            "gap_projection_sha256": sha256_bytes(canonical(gap_projection)),
            "subgroup_registry_sha256": sha256_bytes(canonical(python_projection["subgroup_registry"])),
            "all_36_tensor_rows_sha256": sha256_bytes(canonical(python_projection["tensor_atlas"]["rows"])),
            "mixed_160_position_sha256": sha256_bytes(canonical(python_projection["mixed_160_12_8"])),
            "raw_global_local_input_sha256": sha256_bytes(canonical(python_projection["raw_global_local_inputs"])),
        },
        "independence_contract": {
            "python_reconstructs_all_groups_without_importing_released_code": True,
            "gap_tomlib_reconstructs_independently": True,
            "pilots_or_tmp_runtime_authority": False,
            "no_target_degree_or_order_filters": True,
            "arithmetic_resolvent_lane_must_duplicate_literals_and_reconstruct": True,
        },
        "scope_nonclaims": dict(FALSE_SCOPE_LEAVES),
        "nonresults": {
            "evaluated_product_form_resolvents": "NOT_IN_GROUP_COMPONENT",
            "Fourier_carrier_Tplus_equality": "SEED149_GROUP_INPUT_ONLY_FOR_INDEPENDENT_RESOLVENT_LANE",
            "global_local_arithmetic_theorem": "RAW_GROUP_INPUTS_ONLY",
            "paper": "PENDING",
            "release": "NOT_RELEASED",
        },
        "lifecycle": {
            "component": "GROUP_MACHINE_PASS",
            "project": "IMPLEMENTATION_IN_PROGRESS",
            "paper": "PAPER_PENDING",
            "release": "NOT_RELEASED",
            "promotion_authorized": False,
        },
        "status": PROJECT_STATUS,
    }
    validate_fast(document)
    return document


def validate_local_table_document(table: Any, label: str) -> None:
    exact_keys(table, {"uncollected_rows","collected_rows","degree_total","different_total","factor_count"}, label)
    raw = table["uncollected_rows"]
    collected = table["collected_rows"]
    if type(raw) is not list or type(collected) is not list:
        raise StrictError(f"{label} row list type drift")
    counts: Counter[tuple[int,int,int,int]] = Counter()
    for index, row in enumerate(raw):
        exact_keys(row, {"orbit_seed","n","e","f","d"}, f"{label}.raw[{index}]")
        seed = strict_int(row["orbit_seed"], f"{label}.seed", minimum=0)
        n = strict_int(row["n"], f"{label}.n", minimum=1)
        e = strict_int(row["e"], f"{label}.e", minimum=1)
        f = strict_int(row["f"], f"{label}.f", minimum=1)
        d = strict_int(row["d"], f"{label}.d", minimum=0)
        if n != e*f or (index and seed <= raw[index-1]["orbit_seed"]):
            raise StrictError(f"{label} invalid n=ef or seed ordering")
        counts[(n,e,f,d)] += 1
    expected_collected = [
        {"n":n,"e":e,"f":f,"d":d,"multiplicity":counts[(n,e,f,d)]}
        for n,e,f,d in sorted(counts)
    ]
    if collected != expected_collected:
        raise StrictError(f"{label} collected rows drift")
    degree = sum(row["n"] for row in raw)
    different = sum(row["f"]*row["d"] for row in raw)
    if table["degree_total"] != degree or table["different_total"] != different or table["factor_count"] != len(raw):
        raise StrictError(f"{label} totals drift")


def validate_source_contract(source: Any) -> None:
    exact_keys(source, {
        "repository","released_files","c60_manifest_verification","c60_payload_sha256",
        "c60_source_contract_sha256","c60_frozen_arrays_sha256",
        "formal_input","pilot_runtime_inputs",
    }, "source contract")
    if source["repository"] != {"head":P60,"origin_main":P60,"tree":P60_TREE,"sole_parent":P60_PARENT}:
        raise StrictError("source repository tuple drift")
    if set(source["released_files"]) != set(EXPECTED_FILES):
        raise StrictError("source released-file inventory drift")
    for label, (relative, digest) in EXPECTED_FILES.items():
        row = source["released_files"][label]
        exact_keys(row, {"relative_path","sha256","size_bytes","source"}, f"source file {label}")
        if row["relative_path"] != relative.as_posix() or row["sha256"] != digest or row["source"] != f"immutable_git_blob_at_{P60}":
            raise StrictError(f"source file binding drift: {label}")
        strict_int(row["size_bytes"], f"source file size {label}", minimum=1)
    if source["c60_payload_sha256"] != EXPECTED_C60_PAYLOAD_SHA256 or source["c60_source_contract_sha256"] != EXPECTED_C60_SOURCE_CONTRACT_SHA256 or source["c60_frozen_arrays_sha256"] != EXPECTED_FROZEN_ARRAYS_SHA256:
        raise StrictError("source C60 subobject digest drift")
    formal = source["formal_input"]
    exact_keys(formal, {
        "formal_13_root_sha256","formal_route_sha256","formal_batch_sha256",
        "formal_exact15_sha256","formal_root_count","formal_exact15_count",
        "formal_exact15_size_bytes","runtime_input_root",
        "later_code_results_inventory_owned_by_release_runner","authority_status",
        "all_installed_hashes_recomputed",
    }, "formal target-lock input")
    expected_formal = {
        "formal_13_root_sha256": FORMAL_13_ROOT_SHA256,
        "formal_route_sha256": FORMAL_ROUTE_SHA256,
        "formal_batch_sha256": FORMAL_BATCH_SHA256,
        "formal_exact15_sha256": FORMAL_EXACT15_SHA256,
    }
    for key, value in expected_formal.items():
        if formal.get(key) != value:
            raise StrictError(f"formal source digest drift: {key}")
    if formal.get("authority_status") != "INSTALLED_TARGET_LOCK_HASHES_RECOMPUTED" or formal.get("all_installed_hashes_recomputed") is not True:
        raise StrictError("installed target-lock status drift")
    if formal.get("formal_root_count") != 13 or formal.get("formal_exact15_count") != 15 or strict_int(formal.get("formal_exact15_size_bytes"), "formal exact15 size", minimum=1) < 1:
        raise StrictError("formal target-lock inventory drift")
    if formal.get("runtime_input_root") != str(REPO / "henon_dynamics") or formal.get("later_code_results_inventory_owned_by_release_runner") is not True:
        raise StrictError("formal runtime/release-runner ownership drift")
    if source["pilot_runtime_inputs"] != []:
        raise StrictError("pilot runtime authority is forbidden")


def validate_fast(document: Any) -> None:
    walk_no_float(document)
    exact_keys(document, {
        "schema_id","semantic_firewall","source_contract","conventions",
        "python_projection","gap_projection","cross_checks","backend_contract",
        "component_hashes","independence_contract","scope_nonclaims","nonresults",
        "lifecycle","status",
    }, "evidence")
    if document["schema_id"] != SCHEMA_ID or document["semantic_firewall"] != FIREWALL or document["status"] != PROJECT_STATUS:
        raise StrictError("evidence identity/firewall/status drift")
    validate_source_contract(document["source_contract"])
    if document["scope_nonclaims"] != FALSE_SCOPE_LEAVES or len(document["scope_nonclaims"]) != 30:
        raise StrictError("30-leaf firewall drift")
    if any(value is not False for value in document["scope_nonclaims"].values()):
        raise StrictError("scope nonclaim leaf became true/non-Boolean")
    if document["lifecycle"] != {
        "component":"GROUP_MACHINE_PASS","project":"IMPLEMENTATION_IN_PROGRESS",
        "paper":"PAPER_PENDING","release":"NOT_RELEASED","promotion_authorized":False,
    }:
        raise StrictError("lifecycle drift")
    py = document["python_projection"]
    exact_keys(py, {
        "schema_id","conventions","ambient","tensor_atlas","burnside_linearization",
        "mixed_160_12_8","P3_P6","mixed_degree_640_recovery",
        "raw_global_local_inputs","subgroup_registry","status",
    }, "Python projection")
    if py["schema_id"] != "hcs-c61-python-group-projection-v1" or py["status"] != "PYTHON_RECONSTRUCTION_PASS":
        raise StrictError("Python projection schema/status drift")
    expected_conventions = {
        "carrier_degree":27,"permutation_arrays":"one_based","composition":"left_after_right",
        "canonical_group_serialization":"lexicographically_sorted_complete_one_based_arrays",
        "promoted_registry_serialization":"canonical_generators_order_and_complete_set_sha256",
        "right_coset_enumeration":"least_unseen_ambient_element","target_degree_or_order_filters_used":False,
    }
    if py["conventions"] != expected_conventions or document["conventions"] != expected_conventions:
        raise StrictError("convention drift")
    hashes = document["component_hashes"]
    exact_keys(hashes, {
        "python_projection_sha256","gap_projection_sha256","subgroup_registry_sha256",
        "all_36_tensor_rows_sha256","mixed_160_position_sha256","raw_global_local_input_sha256",
    }, "component hashes")
    observed_hashes = {
        "python_projection_sha256":sha256_bytes(canonical(py)),
        "gap_projection_sha256":sha256_bytes(canonical(document["gap_projection"])),
        "subgroup_registry_sha256":sha256_bytes(canonical(py["subgroup_registry"])),
        "all_36_tensor_rows_sha256":sha256_bytes(canonical(py["tensor_atlas"]["rows"])),
        "mixed_160_position_sha256":sha256_bytes(canonical(py["mixed_160_12_8"])),
        "raw_global_local_input_sha256":sha256_bytes(canonical(py["raw_global_local_inputs"])),
    }
    if hashes != observed_hashes:
        raise StrictError("component commitment hash drift")

    # Cheap fail-closed checks precede complete-set reconstruction.  This keeps
    # hostile testing linear in the one immutable deep reconstruction while
    # ensuring every mutation is still rejected by this public validator.
    atlas_pre = py["tensor_atlas"]
    if atlas_pre["row_counts"] != {"Tpp":12,"Tpm":12,"Tmm":12} or atlas_pre["Q_type_count"] != 18 or atlas_pre["P_type_count"] != 8:
        raise StrictError("preflight atlas count drift")
    for lane in ("Tpp","Tpm","Tmm"):
        if strict_int(atlas_pre["dimensions"][lane],f"{lane} dimension",minimum=1) != 102_400:
            raise StrictError("preflight tensor dimension drift")
        rows_pre = atlas_pre["rows"][lane]
        if [(row["seed"],row["Q_type"],row["P_type"]) for row in rows_pre] != EXPECTED_ROW_TYPES[lane]:
            raise StrictError("preflight row/type sequence drift")
        for row in rows_pre:
            if row["representative_sha256"] != sha256_bytes(canonical(row["representative_one_based"])):
                raise StrictError("preflight representative hash drift")
    mixed_pre = py["mixed_160_12_8"]
    if mixed_pre["conjugate_position_count"] != 160 or mixed_pre["double_coset_factor_count"] != 12 or mixed_pre["Q_isomorphism_type_count"] != 8 or mixed_pre["multiplicities"] != [1,2,1,2,2,2,1,1]:
        raise StrictError("preflight mixed 160/12/8 drift")
    p3_pre = py["P3_P6"]
    if p3_pre["exact_minus_to_plus_conjugator_one_based"] != P3_WITNESS_ONE_BASED or p3_pre["P3_nonconjugate_to_P6"] is not True:
        raise StrictError("preflight P3/P6 drift")
    burnside_pre = py["burnside_linearization"]
    if burnside_pre["common_character_sha256"] != sha256_bytes(canonical(burnside_pre["common_character_values_on_canonical_W"])):
        raise StrictError("preflight character commitment drift")
    if document["gap_projection"].get("type_counts") != {"P":8,"Q":18}:
        raise StrictError("preflight GAP type-count drift")

    registry_doc = py["subgroup_registry"]
    if type(registry_doc) is not dict or not registry_doc:
        raise StrictError("empty/non-dict subgroup registry")
    registry: dict[str, frozenset[Permutation]] = {}
    for digest, entry in registry_doc.items():
        if type(digest) is not str or len(digest) != 64:
            raise StrictError("invalid registry key")
        exact_keys(entry, {"sha256","order","generators_one_based"}, f"registry {digest}")
        if entry["sha256"] != digest:
            raise StrictError("registry key/self hash mismatch")
        gens = one_to_zero(entry["generators_one_based"])
        group = generated(gens)
        if strict_int(entry["order"], "registry order", minimum=1) != len(group) or group_sha(group) != digest:
            raise StrictError("registry generator/order/complete-set hash drift")
        registry[digest] = group

    ambient = py["ambient"]
    exact_keys(ambient, {
        "W_group_sha256","Hplus_group_sha256","Hminus_group_sha256",
        "W_generators_one_based","Hplus_generators_one_based","Hminus_generators_one_based",
        "orders_W_Hplus_Hminus","W_permutation_count",
        "W_distinct_labelled_permutation_count","labelled_W_action_faithful",
    }, "ambient")
    W = registry[ambient["W_group_sha256"]]
    Hp = registry[ambient["Hplus_group_sha256"]]
    Hm = registry[ambient["Hminus_group_sha256"]]
    if [len(W),len(Hp),len(Hm)] != [51840,162,162] or ambient["orders_W_Hplus_Hminus"] != [51840,162,162]:
        raise StrictError("ambient order drift")
    if ambient["W_permutation_count"] != len(W) or ambient["W_distinct_labelled_permutation_count"] != len(set(W)) or ambient["labelled_W_action_faithful"] is not True:
        raise StrictError("labelled ambient faithfulness/count drift")
    hp_gens = one_to_zero(ambient["Hplus_generators_one_based"])
    hm_gens = one_to_zero(ambient["Hminus_generators_one_based"])
    if generated(hp_gens) != Hp or generated(hm_gens) != Hm:
        raise StrictError("ambient H generator drift")
    right_reps = {"Tpp":canonical_right_cosets(W,Hp)[0],"Tpm":canonical_right_cosets(W,Hm)[0],"Tmm":canonical_right_cosets(W,Hm)[0]}
    q_type_groups = {
        label: registry[row["representative"]["group_sha256"]]
        for label,row in py["tensor_atlas"]["Q_types"].items()
    }
    p_type_groups = {
        label: registry[row["representative"]["group_sha256"]]
        for label,row in py["tensor_atlas"]["P_types"].items()
    }
    if set(q_type_groups) != {f"Q{i}" for i in range(1,19)} or set(p_type_groups) != {f"P{i}" for i in range(1,9)}:
        raise StrictError("Q/P type-label inventory drift")
    row_keys = {
        "lane","seed","representative_one_based","representative_sha256","right_coset_orbit",
        "orbit_size","Q_type","P_type","Q_type_conjugator_one_based","Q_type_conjugator_sha256",
        "P_type_conjugator_one_based","P_type_conjugator_sha256","intersection","join",
        "simple_factor_degree","base_field_degree",
    }
    rows_doc = py["tensor_atlas"]["rows"]
    for lane in ("Tpp","Tpm","Tmm"):
        rows = rows_doc[lane]
        expected = EXPECTED_ROW_TYPES[lane]
        if [(r["seed"],r["Q_type"],r["P_type"]) for r in rows] != expected:
            raise StrictError(f"frozen row/type sequence drift in {lane}")
        left,left_gens = (Hp,hp_gens) if lane != "Tmm" else (Hm,hm_gens)
        right,right_gens = (Hp,hp_gens) if lane == "Tpp" else (Hm,hm_gens)
        for row in rows:
            exact_keys(row,row_keys,f"{lane} row")
            seed = strict_int(row["seed"],f"{lane} seed",minimum=0)
            rep = one_to_zero([row["representative_one_based"]])[0]
            if seed >= len(right_reps[lane]) or rep != right_reps[lane][seed] or row["representative_sha256"] != sha256_bytes(canonical(row["representative_one_based"])):
                raise StrictError(f"canonical representative/seed drift in {lane}/{seed}")
            q = frozenset(conjugate(rep,h) for h in right)
            qgens = tuple(conjugate(rep,h) for h in right_gens)
            inter = left.intersection(q)
            join = generated(tuple(left_gens)+qgens)
            if row["intersection"]["group_sha256"] != group_sha(inter) or row["join"]["group_sha256"] != group_sha(join):
                raise StrictError(f"embedded I/J complete-set drift in {lane}/{seed}")
            if row["orbit_size"]*len(inter) != len(left) or row["simple_factor_degree"]*len(inter) != len(W) or row["base_field_degree"]*len(join) != len(W):
                raise StrictError(f"row degree/orbit identity drift in {lane}/{seed}")
            qw = one_to_zero([row["Q_type_conjugator_one_based"]])[0]
            pw = one_to_zero([row["P_type_conjugator_one_based"]])[0]
            if row["Q_type_conjugator_sha256"] != sha256_bytes(canonical(row["Q_type_conjugator_one_based"])) or row["P_type_conjugator_sha256"] != sha256_bytes(canonical(row["P_type_conjugator_one_based"])):
                raise StrictError("type conjugator hash drift")
            if frozenset(conjugate(qw,h) for h in inter) != q_type_groups[row["Q_type"]] or frozenset(conjugate(pw,h) for h in join) != p_type_groups[row["P_type"]]:
                raise StrictError("type conjugator complete-set equality failed")
    atlas = py["tensor_atlas"]
    if atlas["row_counts"] != {"Tpp":12,"Tpm":12,"Tmm":12} or atlas["Q_type_count"] != 18 or atlas["P_type_count"] != 8:
        raise StrictError("atlas counts drift")
    if any(sum(atlas["degree_spectra"][lane]) != 102400 or atlas["dimensions"][lane] != 102400 for lane in ("Tpp","Tpm","Tmm")):
        raise StrictError("atlas tensor dimensions drift")

    burnside = py["burnside_linearization"]
    values = burnside["common_character_values_on_canonical_W"]
    square = burnside["common_tensor_character_values_on_canonical_W"]
    if type(values) is not list or len(values) != 51840 or square != [x*x for x in values]:
        raise StrictError("full Burnside character vector drift")
    if burnside["common_character_sha256"] != sha256_bytes(canonical(values)) or burnside["common_tensor_character_sha256"] != sha256_bytes(canonical(square)):
        raise StrictError("Burnside character hash drift")
    for key in ("all_three_linearizations_equal","all_three_zeta_products_equal_formal_Artin_consequence","three_G_sets_pairwise_nonisomorphic","three_field_factor_multisets_pairwise_distinct"):
        if burnside[key] is not True:
            raise StrictError(f"Burnside theorem flag drift: {key}")

    mixed = py["mixed_160_12_8"]
    if mixed["conjugate_position_count"] != 160 or mixed["double_coset_factor_count"] != 12 or mixed["Q_isomorphism_type_count"] != 8 or mixed["multiplicities"] != [1,2,1,2,2,2,1,1]:
        raise StrictError("mixed 160/12/8 count drift")
    if len(mixed["conjugate_positions"]) != 160 or len(mixed["relative_position_types"]) != 8 or sum(r["raw_count"] for r in mixed["relative_position_types"]) != 160:
        raise StrictError("mixed raw population drift")
    p3 = py["P3_P6"]
    if p3["exact_minus_to_plus_conjugator_one_based"] != P3_WITNESS_ONE_BASED or p3["conjugated_minus_complete_set_equals_plus"] is not True or p3["P3_nonconjugate_to_P6"] is not True or p3["three_pairwise_nonconjugate_joins_claimed"] is not False:
        raise StrictError("P3/P6 semantic drift")
    if py["mixed_degree_640_recovery"] != {
        "mixed_seed":148,"intersection_equals_released_C60_J_complete_set":True,
        "join_equals_released_C60_N_complete_set":True,
        "intersection_sha256":"80f5ac65a18777d49696ef6984295ab079f0cc22e9d6f0f714206ab982f264c2",
        "join_sha256":"8fd5fa5d8dce47de3abde3c22a1009fc14d4783fca365d2690f206145400e7b0",
        "factor_degree":640,"base_degree":160,
    }:
        raise StrictError("mixed degree-640 recovery drift")

    raw_inputs = py["raw_global_local_inputs"]
    if raw_inputs["downstream_authority_status"] != "INPUT_ONLY_REQUIRES_INDEPENDENT_RESOLVENT_ARITHMETIC_RECONSTRUCTION" or len(raw_inputs["field_type_rows"]) != 26:
        raise StrictError("raw input inventory/status drift")
    local_contract = raw_inputs["local_subgroups"]
    expected_local_orders = {
        "D140":18,"I140":18,"P140":9,"Q140":3,
        "D206":36,"I206":18,"P206":9,"Q206":3,
        "I5":20,"P5":5,"C3":3,"C2":2,"Cinf":2,
        "I3":18,"P3":9,"Q3":3,
    }
    if set(local_contract) != set(expected_local_orders):
        raise StrictError("raw local subgroup inventory drift")
    local_groups: dict[str,frozenset[Permutation]] = {}
    for label, expected_order in expected_local_orders.items():
        entry = local_contract[label]
        exact_keys(entry,{"group_sha256","order"},f"raw local subgroup {label}")
        digest = entry["group_sha256"]
        if digest not in registry or entry["order"] != expected_order or len(registry[digest]) != expected_order:
            raise StrictError(f"raw local subgroup binding drift: {label}")
        local_groups[label] = registry[digest]
    if local_contract["D140"]["group_sha256"] == local_contract["D206"]["group_sha256"]:
        raise StrictError("retained D3 branches collapsed")
    if [row["type_label"] for row in raw_inputs["field_type_rows"]] != [f"Q{i}" for i in range(1,19)]+[f"P{i}" for i in range(1,9)]:
        raise StrictError("raw field-type order drift")
    arithmetic_cache: dict[str,dict[str,Any]] = {}
    for row in raw_inputs["field_type_rows"]:
        exact_keys(row,{
            "type_label","field_subgroup_sha256","degree","orbit_count_order",
            "orbit_counts","conductor_exponent_order","conductor_exponents",
            "signature_r1_r2","discriminant_positive","tom140","tom206",
        },f"raw field type {row['type_label']}")
        field_digest = row["field_subgroup_sha256"]
        if field_digest not in registry:
            raise StrictError("raw field subgroup missing from registry")
        validate_local_table_document(row["tom140"],f"{row['type_label']}.tom140")
        validate_local_table_document(row["tom206"],f"{row['type_label']}.tom206")
        if row["tom140"]["different_total"] != row["tom206"]["different_total"] or row["tom140"]["degree_total"] != row["degree"] or row["tom206"]["degree_total"] != row["degree"]:
            raise StrictError("two retained D3 branch identity drift")
        if row["conductor_exponents"][0] != row["tom140"]["different_total"]:
            raise StrictError("raw global/local p3 bridge drift")
        if field_digest not in arithmetic_cache:
            arithmetic_cache[field_digest] = arithmetic_input(W,registry[field_digest],local_groups)
        stored_arithmetic = {key:value for key,value in row.items() if key not in {"type_label","field_subgroup_sha256"}}
        if stored_arithmetic != arithmetic_cache[field_digest]:
            raise StrictError(f"raw arithmetic reconstruction drift: {row['type_label']}")
    cross = cross_check_gap(py,document["gap_projection"])
    if document["cross_checks"] != cross:
        raise StrictError("stored cross-check projection drift")
    backend = document["backend_contract"]
    if backend["producer_checker_shared_math_allowed"] is not False or backend["python"]["optimized_python_rejected"] is not True or backend["promoted_evidence_size_ceiling_bytes"] != PROMOTED_EVIDENCE_SIZE_CEILING_BYTES:
        raise StrictError("backend independence drift")
    if backend["python"]["producer_source_sha256"] != sha256_bytes(stable_read(Path(__file__),root=Path(__file__).parent)):
        raise StrictError("Python producer source hash drift")
    checker_path = Path(__file__).with_name("c61_checker_group.g")
    if backend["gap"]["checker_source_sha256"] != sha256_bytes(stable_read(checker_path,root=checker_path.parent)):
        raise StrictError("GAP checker source hash drift")
    independence = document["independence_contract"]
    if independence != {
        "python_reconstructs_all_groups_without_importing_released_code":True,
        "gap_tomlib_reconstructs_independently":True,
        "pilots_or_tmp_runtime_authority":False,
        "no_target_degree_or_order_filters":True,
        "arithmetic_resolvent_lane_must_duplicate_literals_and_reconstruct":True,
    }:
        raise StrictError("independence contract drift")


def refresh_component_hashes(document: dict[str, Any]) -> None:
    py = document["python_projection"]
    document["component_hashes"] = {
        "python_projection_sha256":sha256_bytes(canonical(py)),
        "gap_projection_sha256":sha256_bytes(canonical(document["gap_projection"])),
        "subgroup_registry_sha256":sha256_bytes(canonical(py["subgroup_registry"])),
        "all_36_tensor_rows_sha256":sha256_bytes(canonical(py["tensor_atlas"]["rows"])),
        "mixed_160_position_sha256":sha256_bytes(canonical(py["mixed_160_12_8"])),
        "raw_global_local_input_sha256":sha256_bytes(canonical(py["raw_global_local_inputs"])),
    }


def parent_at(root: Any, path: Sequence[Any]) -> tuple[Any, Any]:
    node = root
    for key in path[:-1]:
        node = node[key]
    return node, path[-1]


def mutation_suite(document: dict[str, Any]) -> dict[str, Any]:
    passed: list[str] = []

    def trial(label: str, path: Sequence[Any], replacement: Any, *, refresh: bool = False) -> None:
        parent, key = parent_at(document,path)
        old = parent[key]
        parent[key] = replacement
        if refresh:
            refresh_component_hashes(document)
        try:
            validate_fast(document)
        except StrictError:
            passed.append(label)
        else:
            raise StrictError(f"hostile mutation survived: {label}")
        finally:
            parent[key] = old
            if refresh:
                refresh_component_hashes(document)

    # Scalar/type/authority/firewall/convention mutations.
    trial("status_scalar",["status"],"RELEASE_FROZEN")
    trial("firewall_literal",["semantic_firewall"],"BAD_EULER_ALLOWED")
    trial("scope_leaf_true",["scope_nonclaims","global_root_number_claimed"],True)
    trial("integer_slot_boolean",["python_projection","tensor_atlas","dimensions","Tpp"],True,refresh=True)
    trial("target_filter_enabled",["python_projection","conventions","target_degree_or_order_filters_used"],True,refresh=True)
    trial("source_P60_self_consistent_rebound",["source_contract","repository","head"],"0"*40)
    trial("formal_exact15_rebound",["source_contract","formal_input","formal_exact15_sha256"],"2"*64)
    # Row, grouping, subgroup, branch, character, and 160/12/8 mutations.
    first = document["python_projection"]["tensor_atlas"]["rows"]["Tpp"][0]
    second = document["python_projection"]["tensor_atlas"]["rows"]["Tpp"][1]
    trial("canonical_seed_self_consistent",["python_projection","tensor_atlas","rows","Tpp",0,"seed"],second["seed"],refresh=True)
    trial("Q_type_grouping",["python_projection","tensor_atlas","rows","Tpp",0,"Q_type"],"Q16",refresh=True)
    trial("representative_hash",["python_projection","tensor_atlas","rows","Tpm",0,"representative_sha256"],"3"*64,refresh=True)
    registry = document["python_projection"]["subgroup_registry"]
    some_digest = first["intersection"]["group_sha256"]
    trial("subgroup_order_self_consistent",["python_projection","subgroup_registry",some_digest,"order"],163,refresh=True)
    c2_digest = document["python_projection"]["raw_global_local_inputs"]["local_subgroups"]["C2"]["group_sha256"]
    trial(
        "compact_registry_generator_self_consistent",
        ["python_projection","subgroup_registry",c2_digest,"generators_one_based",0],
        list(range(1,28)),refresh=True,
    )
    trial("P3_witness",["python_projection","P3_P6","exact_minus_to_plus_conjugator_one_based",0],24,refresh=True)
    trial("mixed_160_count",["python_projection","mixed_160_12_8","conjugate_position_count"],159,refresh=True)
    trial("full_character_entry",["python_projection","burnside_linearization","common_character_values_on_canonical_W",0],319,refresh=True)
    # Swapping the two retained branches remains internally plausible at the
    # scalar level, but must fail the branch-population identity.
    field0 = document["python_projection"]["raw_global_local_inputs"]["field_type_rows"][0]
    old140, old206 = field0["tom140"], field0["tom206"]
    field0["tom140"], field0["tom206"] = old206, old140
    refresh_component_hashes(document)
    try:
        validate_fast(document)
    except StrictError:
        passed.append("self_consistent_D3_branch_swap")
    else:
        raise StrictError("hostile mutation survived: self_consistent_D3_branch_swap")
    finally:
        field0["tom140"], field0["tom206"] = old140, old206
        refresh_component_hashes(document)
    trial("gap_Q_type_count",["gap_projection","type_counts","Q"],17,refresh=True)

    # Structural JSON parser mutations.
    parser_cases = {
        "duplicate_JSON_key":b'{"x":1,"x":2}',
        "float_JSON_leaf":b'{"x":1.5}',
        "NaN_JSON_leaf":b'{"x":NaN}',
        "non_UTF8_JSON":b'{"x":"\xff"}',
    }
    for label,raw in parser_cases.items():
        try:
            strict_json(raw,label)
        except StrictError:
            passed.append(label)
        else:
            raise StrictError(f"hostile parser mutation survived: {label}")

    with tempfile.TemporaryDirectory(prefix="c61-group-hostile-") as temp_name:
        temp = Path(temp_name)
        real = temp/"real.json"
        real.write_bytes(b"{}")
        link = temp/"link.json"
        link.symlink_to(real)
        try:
            stable_read(link,root=temp)
        except StrictError:
            passed.append("symlink_rejection")
        else:
            raise StrictError("symlink mutation survived")
        try:
            stable_read(real,root=REPO)
        except StrictError:
            passed.append("path_escape_rejection")
        else:
            raise StrictError("path escape mutation survived")
        try:
            stable_read(real,root=temp,limit=1)
        except StrictError:
            passed.append("oversized_input_rejection")
        else:
            raise StrictError("oversized input mutation survived")
        def touch_after_read(path: Path) -> None:
            old = path.stat().st_mtime_ns
            os.utime(path,ns=(old+1,old+1))
        try:
            stable_read(real,root=temp,_after_read_hook=touch_after_read)
        except StrictError:
            passed.append("stale_snapshot_rejection")
        else:
            raise StrictError("stale snapshot mutation survived")

    optimized_code = (
        "import importlib.util;"
        f"s=importlib.util.spec_from_file_location('c61opt',{str(Path(__file__))!r});"
        "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);m.bind_authority()"
    )
    optimized = subprocess.run(
        [sys.executable,"-B","-O","-c",optimized_code],stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1","LC_ALL":"C"},timeout=30,
    )
    if optimized.returncode == 0:
        raise StrictError("optimized-Python hostile run survived")
    passed.append("optimized_python_rejection")
    validate_fast(document)
    return {"mutation_count":len(passed),"mutations":passed,"all_rejected":True}


def atomic_write(path: Path, raw: bytes) -> None:
    parent = path.parent.resolve(strict=True)
    if path.exists() and path.is_symlink():
        raise StrictError(f"refusing symlink output: {path}")
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.",dir=parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd,"wb") as stream:
            os.fchmod(stream.fileno(),0o644)
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary,path)
        installed = path.stat()
        if stat.S_IMODE(installed.st_mode) != 0o644 or installed.st_nlink != 1:
            raise StrictError(f"installed output mode/link drift: {path}")
    finally:
        if temporary.exists():
            temporary.unlink()


def make_handoff(document: dict[str, Any], evidence_raw: bytes) -> dict[str, Any]:
    py = document["python_projection"]
    referenced: set[str] = {
        py["ambient"]["W_group_sha256"],py["ambient"]["Hplus_group_sha256"],
        py["ambient"]["Hminus_group_sha256"],
    }
    for rows in py["tensor_atlas"]["rows"].values():
        for row in rows:
            referenced.add(row["intersection"]["group_sha256"])
            referenced.add(row["join"]["group_sha256"])
            referenced.add(row["intersection"]["normalizer_sha256"])
            referenced.add(row["intersection"]["core_sha256"])
            referenced.add(row["join"]["normalizer_sha256"])
            referenced.add(row["join"]["core_sha256"])
    for row in py["raw_global_local_inputs"]["local_subgroups"].values():
        referenced.add(row["group_sha256"])
    registry = py["subgroup_registry"]
    expanded_registry: dict[str,dict[str,Any]] = {}
    for digest in sorted(referenced):
        entry = registry[digest]
        group = generated(one_to_zero(entry["generators_one_based"]))
        if len(group) != entry["order"] or group_sha(group) != digest:
            raise StrictError("cannot expand compact registry for handoff")
        expanded_registry[digest] = {
            **entry,
            "complete_element_arrays_one_based": canonical_group_arrays(group),
        }
    handoff = {
        "schema_id":"hcs-c61-nonpromoted-group-handoff-v1",
        "status":"NONPROMOTED_INTERLANE_HANDOFF_NOT_RUNTIME_AUTHORITY",
        "semantic_firewall":FIREWALL,
        "source_evidence_sha256":sha256_bytes(evidence_raw),
        "source_component_hashes":document["component_hashes"],
        "ambient":py["ambient"],
        "all_36_tensor_rows":py["tensor_atlas"]["rows"],
        "Q_types":py["tensor_atlas"]["Q_types"],
        "P_types":py["tensor_atlas"]["P_types"],
        "durable_subgroup_registry":expanded_registry,
        "mixed_160_12_8":py["mixed_160_12_8"],
        "mixed_seed149_Tplus_bridge_input":{
            "row":next(row for row in py["tensor_atlas"]["rows"]["Tpm"] if row["seed"]==149),
            "group_component_claim":"exact embedded seed149 join only",
            "resolver_obligation":"independently reconstruct Fourier Tplus and prove complete-set equality",
        },
        "P3_P6":py["P3_P6"],
        "mixed_degree_640_recovery":py["mixed_degree_640_recovery"],
        "raw_global_local_inputs":py["raw_global_local_inputs"],
        "consumer_contract":{
            "copy_source_owned_literals_if_needed":True,
            "runtime_dependency_on_handoff_forbidden":True,
            "independent_reconstruction_required":True,
            "pilot_inputs_forbidden":True,
        },
    }
    return handoff


def write_manifest(project_root: Path, output: Path) -> dict[str, Any]:
    root = project_root.resolve(strict=True)
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.resolve() != output.resolve() and "__pycache__" not in p.parts and p.suffix not in {".pyc",".pyo"}
    )
    lines: list[str] = []
    previous = ""
    for path in files:
        if path.is_symlink():
            raise StrictError(f"manifest symlink rejected: {path}")
        relative = path.relative_to(root).as_posix()
        if relative <= previous:
            raise StrictError("manifest paths not strictly sorted")
        lines.append(f"{sha256_bytes(stable_read(path,root=root))}  {relative}\n")
        previous = relative
    raw = "".join(lines).encode("ascii")
    atomic_write(output,raw)
    return {"entry_count":len(lines),"sha256":sha256_bytes(raw),"size_bytes":len(raw)}


def self_test(
    checker: Path, output: Path, report: Path, handoff_path: Path,
    manifest_path: Path, external_stage_audit: dict[str,Any] | None = None,
) -> dict[str, Any]:
    import time
    started = time.monotonic_ns()
    first = build_document(checker)
    first_done = time.monotonic_ns()
    first_raw = canonical(first)+b"\n"
    if len(first_raw) > PROMOTED_EVIDENCE_SIZE_CEILING_BYTES:
        raise StrictError("promoted group evidence exceeds size ceiling")
    second = build_document(checker)
    second_done = time.monotonic_ns()
    second_raw = canonical(second)+b"\n"
    if len(second_raw) > PROMOTED_EVIDENCE_SIZE_CEILING_BYTES:
        raise StrictError("second promoted group evidence exceeds size ceiling")
    if first_raw != second_raw:
        raise StrictError("two-build deterministic replay mismatch")
    parsed = strict_json(first_raw,"self-test evidence")
    validate_fast(parsed)
    mutations = mutation_suite(parsed)
    atomic_write(output,first_raw)
    handoff = make_handoff(parsed,first_raw)
    handoff_raw = canonical(handoff)+b"\n"
    atomic_write(handoff_path,handoff_raw)
    cache_entries = sorted(
        str(p) for p in output.parents[1].rglob("*")
        if p.name=="__pycache__" or p.suffix in {".pyc",".pyo"}
    )
    if cache_entries:
        raise StrictError(f"stage-local Python cache found: {cache_entries}")
    report_doc = {
        "schema_id":"hcs-c61-group-hostile-test-report-v1",
        "status":"PASS",
        "semantic_firewall":FIREWALL,
        "external_stage_authority_audit":external_stage_audit if external_stage_audit is not None else {
            "status":"NOT_RUN_BY_RUNTIME_HELPER",
        },
        "deterministic_two_build_replay":True,
        "first_evidence_sha256":sha256_bytes(first_raw),
        "second_evidence_sha256":sha256_bytes(second_raw),
        "first_build_milliseconds":(first_done-started)//1_000_000,
        "second_build_milliseconds":(second_done-first_done)//1_000_000,
        "mutation_suite":mutations,
        "strict_reparse_and_semantic_validation":True,
        "promoted_evidence_size_bytes":len(first_raw),
        "promoted_evidence_size_ceiling_bytes":PROMOTED_EVIDENCE_SIZE_CEILING_BYTES,
        "handoff_sha256":sha256_bytes(handoff_raw),
        "handoff_size_bytes":len(handoff_raw),
        "stage_local_python_cache_entries":cache_entries,
        "staged_nonrelease":True,
    }
    report_raw = canonical(report_doc)+b"\n"
    atomic_write(report,report_raw)
    manifest = write_manifest(output.parents[1],manifest_path)
    return {
        "evidence":str(output),"evidence_sha256":sha256_bytes(first_raw),"evidence_size_bytes":len(first_raw),
        "handoff":str(handoff_path),"handoff_sha256":sha256_bytes(handoff_raw),"handoff_size_bytes":len(handoff_raw),
        "report":str(report),"report_sha256":sha256_bytes(report_raw),"manifest":manifest,
        "mutations":mutations["mutation_count"],"status":"PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command",choices=["build","validate","self-test","handoff","manifest"])
    parser.add_argument("--checker",type=Path,default=Path(__file__).with_name("c61_checker_group.g"))
    parser.add_argument("--evidence",type=Path)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--report",type=Path)
    parser.add_argument("--handoff",type=Path)
    parser.add_argument("--manifest",type=Path)
    parser.add_argument("--project-root",type=Path,default=Path(__file__).parents[1])
    args = parser.parse_args()
    if not __debug__:
        raise StrictError("optimized Python is forbidden")
    if args.command=="build":
        if args.output is None: parser.error("build requires --output")
        document=build_document(args.checker); raw=canonical(document)+b"\n"; atomic_write(args.output,raw)
        result={"output":str(args.output),"sha256":sha256_bytes(raw),"size_bytes":len(raw)}
    elif args.command=="validate":
        if args.evidence is None: parser.error("validate requires --evidence")
        raw=stable_read(args.evidence,root=args.project_root); document=strict_json(raw,"evidence"); validate_fast(document)
        result={"evidence":str(args.evidence),"sha256":sha256_bytes(raw),"status":"PASS"}
    elif args.command=="self-test":
        if args.output is None or args.report is None or args.manifest is None or args.handoff is None:
            parser.error("self-test requires --output --report --handoff --manifest")
        result=self_test(args.checker,args.output,args.report,args.handoff,args.manifest)
    elif args.command=="handoff":
        if args.evidence is None or args.handoff is None: parser.error("handoff requires --evidence --handoff")
        raw=stable_read(args.evidence,root=args.project_root); document=strict_json(raw,"evidence"); validate_fast(document)
        handoff=make_handoff(document,raw); handoff_raw=canonical(handoff)+b"\n"; atomic_write(args.handoff,handoff_raw)
        result={"handoff":str(args.handoff),"sha256":sha256_bytes(handoff_raw),"size_bytes":len(handoff_raw)}
    else:
        if args.manifest is None: parser.error("manifest requires --manifest")
        result=write_manifest(args.project_root,args.manifest)
    print(json.dumps(result,sort_keys=True,separators=(",",":")))


if __name__=="__main__":
    try:
        main()
    except StrictError as exc:
        print(f"C61_GROUP_ERROR: {exc}",file=sys.stderr)
        raise SystemExit(1)
