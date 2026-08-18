#!/usr/bin/env python3
"""Hostile mutation suite for the fresh Paper-44 Route-A v0.2 contract."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Callable


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       indent=2, separators=(",", ": ")) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate source card")
        result[key] = value
    return result


def load_exact(path: Path) -> tuple[dict[str, Any], bytes]:
    if not path.is_absolute() or path.is_symlink():
        raise ValueError("unsafe route")
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value):
        raise ValueError("noncanonical source route")
    return value, raw


def invoke(script: Path, paper: Path, route: Path, skill: Path, repo: Path,
           code_commit: str, cwd: Path, hostile: Path) -> tuple[int, dict[str, Any] | None, bytes]:
    command = [
        sys.executable, "-I", "-B", str(script),
        "--paper-root", str(paper), "--route", str(route), "--skill", str(skill),
        "--repo-root", str(repo), "--code-commit", code_commit,
    ]
    environment = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile), "PYTHONDONTWRITEBYTECODE": "1",
        "LC_ALL": "C", "LANG": "C", "TZ": "UTC",
    }
    process = subprocess.run(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    parsed: dict[str, Any] | None = None
    try:
        value = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
        if type(value) is dict and process.stdout == canonical(value):
            parsed = value
    except Exception:
        pass
    return process.returncode, parsed, process.stderr


SCIENCE_COMMIT = "b0e41ac3d6bd30618421d1b76122c3e9e04d070b"
GIT = "/usr/bin/git"
CODE_PATHS = [
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/render_route_v0_2.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/validate_route_v0_2.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/route/audit_route_v0_2_independent.py",
    "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/code/tests/run_route_v0_2_mutations.py",
]


def git(repo: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [GIT, "--no-replace-objects", "-C", str(repo), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "LC_ALL": "C", "LANG": "C"},
    )


def verify_commit_fixture(repo: Path, paper: Path, descendant: str, unrelated: str) -> None:
    for value in (descendant, unrelated):
        if len(value) != 40 or any(character not in "0123456789abcdef" for character in value) \
                or value == "0" * 40:
            raise ValueError("invalid commit fixture")
    positive = git(repo, ["merge-base", "--is-ancestor", SCIENCE_COMMIT, descendant])
    negative = git(repo, ["merge-base", "--is-ancestor", SCIENCE_COMMIT, unrelated])
    if positive.returncode != 0 or positive.stdout or positive.stderr \
            or negative.returncode != 1 or negative.stdout or negative.stderr:
        raise ValueError("ancestry fixture contract")
    parents = git(repo, ["rev-list", "--parents", "-n", "1", unrelated])
    if parents.returncode != 0 or parents.stderr \
            or parents.stdout.decode("ascii").strip().split() != [unrelated]:
        raise ValueError("unrelated fixture is not an orphan root commit")
    listing = git(repo, ["ls-tree", "-r", unrelated])
    entries: list[tuple[str, str]] = []
    try:
        for line in listing.stdout.decode("ascii").splitlines():
            metadata, path = line.split("\t", 1)
            mode, kind, object_id = metadata.split(" ")
            if mode != "100644" or kind != "blob" or len(object_id) != 40 \
                    or any(character not in "0123456789abcdef" for character in object_id):
                raise ValueError("bad tree entry")
            entries.append((object_id, path))
    except Exception as error:
        raise ValueError("unrelated fixture tree parse") from error
    if listing.returncode != 0 or listing.stderr \
            or [path for _, path in entries] != sorted(CODE_PATHS):
        raise ValueError("unrelated fixture must contain exactly four code blobs")
    paper_prefix = "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/"
    for repository_path in CODE_PATHS:
        relative = repository_path.removeprefix(paper_prefix)
        if PurePosixPath(relative).is_absolute() or ".." in PurePosixPath(relative).parts:
            raise ValueError("unsafe code fixture path")
        blob = git(repo, ["show", unrelated + ":" + repository_path])
        if blob.returncode != 0 or blob.stderr or blob.stdout != (paper / relative).read_bytes():
            raise ValueError("unrelated fixture code blob mismatch")


def invoke_renderer(script: Path, paper: Path, skill: Path, repo: Path,
                    code_commit: str, cwd: Path, hostile: Path) -> tuple[int, bytes, bytes]:
    command = [
        sys.executable, "-I", "-B", str(script),
        "--paper-root", str(paper), "--skill", str(skill),
        "--source-commit", SCIENCE_COMMIT, "--repo-root", str(repo),
        "--code-commit", code_commit,
    ]
    environment = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile), "PYTHONDONTWRITEBYTECODE": "1",
        "LC_ALL": "C", "LANG": "C", "TZ": "UTC",
    }
    process = subprocess.run(command, cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    return process.returncode, process.stdout, process.stderr


REJECT_OBJECTS = {
    "primary": {
        "payload": {"code": "ROUTE_V0_2_CONTRACT_REJECT"},
        "schema": "paper44-route-v0.2-primary-audit-v1",
        "status": "REJECT",
    },
    "independent": {
        "payload": {"code": "ROUTE_V0_2_INDEPENDENT_REJECT"},
        "schema": "paper44-route-v0.2-independent-audit-v1",
        "status": "REJECT",
    },
}


def expected_pass(label: str, code_commit: str, route_sha256: str) -> dict[str, Any]:
    checks = {
        "primary": {
            "canonical_skill_v0_2_exact": True,
            "canonical_whole_object_reconstructed": True,
            "frozen_expectation_inputs_exact": True,
            "historical_v0_3_chronology_preserved": True,
            "science_h1_is_ancestor_of_code_h1_prime": True,
            "h1_prime_code_commit_binds_all_evaluation_code": True,
            "required_artifact_set_hash_kind_mode_exact": True,
            "stale_preauthority_blocker_removed_only": True,
            "route_b_lock_derived_from_actual_record": True,
        },
        "independent": {
            "yaml_ast_duplicate_rejection": True,
            "canonical_json_yaml_byte_form": True,
            "section8_exact_recursive_schema": True,
            "independent_component_digest_locks": True,
            "tuple_overall_route_b_consistency": True,
            "science_h1_to_code_h1_prime_no_artifact_drift": True,
            "code_h1_prime_binds_four_executables": True,
            "derived_h2_prime_objects_absent_from_h1_prime": True,
        },
    }[label]
    schema = {
        "primary": "paper44-route-v0.2-primary-audit-v1",
        "independent": "paper44-route-v0.2-independent-audit-v1",
    }[label]
    return {
        "payload": {
            "checks": checks,
            "checks_passed": len(checks),
            "checks_total": len(checks),
            "code_commit": code_commit,
            "route_sha256": route_sha256,
            "source_commit": SCIENCE_COMMIT,
        },
        "schema": schema,
        "status": "PASS",
    }


def exact_rejection(label: str, returncode: int, result: dict[str, Any] | None,
                    stderr: bytes) -> bool:
    return returncode == 2 and not stderr and result == REJECT_OBJECTS[label]


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--paper-root", required=True)
    parser.add_argument("--route", required=True)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--unrelated-code-commit", required=True)
    parser.add_argument("--scratch", required=True)
    args = parser.parse_args()
    paper, route, skill, repo = map(Path, (
        args.paper_root, args.route, args.skill, args.repo_root))
    scratch = Path(args.scratch)
    if not scratch.is_absolute() or scratch.is_symlink() or scratch.exists():
        raise ValueError("scratch must be an absent absolute path")
    scratch.mkdir(mode=0o755)
    cases = scratch / "cases"; cases.mkdir(mode=0o755)
    cwd = scratch / "hostile_cwd"; cwd.mkdir(mode=0o755)
    hostile = scratch / "hostile_modules"; hostile.mkdir(mode=0o755)
    for name in ("json.py", "yaml.py", "sitecustomize.py"):
        (hostile / name).write_text("raise RuntimeError('hostile import shadow')\n", encoding="ascii")
        (hostile / name).chmod(0o644)
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(hostile)}
    naive = subprocess.run([sys.executable, "-c", "import json"], cwd=cwd, env=environment,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    isolated = subprocess.run([sys.executable, "-I", "-B", "-c", "import json; import yaml"],
                              cwd=cwd, env=environment, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
    if naive.returncode == 0 or isolated.returncode != 0:
        raise ValueError("hostile import control did not discriminate")

    source, source_raw = load_exact(route)
    verify_commit_fixture(repo, paper, args.code_commit, args.unrelated_code_commit)
    renderer = paper / "code/route/render_route_v0_2.py"
    primary = paper / "code/route/validate_route_v0_2.py"
    independent = paper / "code/route/audit_route_v0_2_independent.py"
    for script in (renderer, primary, independent):
        if script.is_symlink() or not script.is_file() or stat.S_IMODE(os.lstat(script).st_mode) != 0o644:
            raise ValueError("consumer physical contract")
    control_path = cases / "CONTROL.json"
    control_path.write_bytes(source_raw); control_path.chmod(0o644)
    consumer_invocations = 0
    rc, stdout, stderr = invoke_renderer(
        renderer, paper, skill, repo, args.code_commit, cwd, hostile)
    consumer_invocations += 1
    if rc != 0 or stderr or stdout != source_raw:
        raise ValueError("renderer positive control failed")
    for script in (primary, independent):
        label = "primary" if script == primary else "independent"
        rc, result, stderr = invoke(script, paper, control_path, skill, repo,
                                    args.code_commit, cwd, hostile)
        consumer_invocations += 1
        if rc != 0 or stderr or result != expected_pass(label, args.code_commit, sha(source_raw)):
            raise ValueError("positive control failed")

    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []
    def add(name: str, action: Callable[[dict[str, Any]], None]) -> None:
        mutations.append((name, action))
    add("skill_version_v03", lambda x: x.__setitem__("skill_version", "0.3.0"))
    add("candidate_changed", lambda x: x.__setitem__("candidate_id", "SD-C45"))
    add("forbidden_code_commit_extension", lambda x: x.__setitem__("code_commit", "1" * 40))
    add("source_commit_changed", lambda x: x.__setitem__("source_commit", "2" * 40))
    add("evaluation_date_changed", lambda x: x.__setitem__("evaluation_date", "2026-08-18"))
    add("source_clock_missing", lambda x: x["source_lock"].__delitem__("clock"))
    add("source_unknown_key", lambda x: x["source_lock"].__setitem__("extra", 0))
    add("a0_promoted", lambda x: x["a0"].__setitem__("verdict", "A0_ANALYTIC_ARITHMETIC_ORIGIN"))
    add("a1_primitive_forged", lambda x: x["a1"]["metrics"].__setitem__("periodic_orbit_ledger", True))
    add("a2_determinant_forged", lambda x: x["a2"]["metrics"].__setitem__("determinant_defined", True))
    add("a3_scope_widened", lambda x: x["a3"]["analytic_structure"].__setitem__(
        "unit_circle_natural_boundary", "all_q_all_A"))
    add("a4_route_b_ready", lambda x: x["a4"]["metrics"].__setitem__("route_b_readiness", True))
    add("overall_promoted", lambda x: x.__setitem__("overall_verdict", "ROUTE_A_ANALYTIC_CANDIDATE"))
    add("route_b_unlocked", lambda x: x.__setitem__("route_b_invocation_allowed", True))
    add("stale_blocker_reintroduced", lambda x: x["blocking_conditions"].append(
        "evaluator_independence_remains_unexecuted"))
    add("round2_clue_injected", lambda x: x["round2_clues"].append("new_unfrozen_family"))
    add("artifact_path_traversal", lambda x: x["a0"]["artifacts"].__setitem__(0, "../SOURCE_LOCK.md"))
    add("artifact_removed", lambda x: x["a4"]["artifacts"].pop())
    add("bool_int_confusion", lambda x: x.__setitem__("route_b_invocation_allowed", 0))
    add("unknown_top_key", lambda x: x.__setitem__("schema", "invented"))

    records: list[dict[str, Any]] = []
    survivors: list[str] = []
    for index, (name, action) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        action(changed)
        path = cases / f"M{index:02d}_{name}.json"
        path.write_bytes(canonical(changed)); path.chmod(0o644)
        outcomes = {}
        for label, script in (("primary", primary), ("independent", independent)):
            rc, result, stderr = invoke(script, paper, path, skill, repo,
                                        args.code_commit, cwd, hostile)
            consumer_invocations += 1
            accepted = exact_rejection(label, rc, result, stderr)
            outcomes[label] = {"accepted_rejection": accepted, "exit_code": rc,
                               "output_sha256": sha(canonical(result)) if result is not None else None}
            if not accepted:
                survivors.append(name + ":" + label)
        records.append({"case_id": name, "mutated_sha256": sha(path.read_bytes()),
                        "outcomes": outcomes})

    special_raw = {
        "duplicate_top_member": b'{"a0":{},' + source_raw[1:],
        "noncanonical_whitespace": source_raw[:-1] + b" \n",
        "invalid_utf8": source_raw[:-2] + b"\xff}\n",
    }
    for name, raw in special_raw.items():
        path = cases / (name + ".json")
        path.write_bytes(raw); path.chmod(0o644)
        outcomes = {}
        for label, script in (("primary", primary), ("independent", independent)):
            rc, result, stderr = invoke(script, paper, path, skill, repo,
                                        args.code_commit, cwd, hostile)
            consumer_invocations += 1
            accepted = exact_rejection(label, rc, result, stderr)
            outcomes[label] = {"accepted_rejection": accepted, "exit_code": rc,
                               "output_sha256": sha(canonical(result)) if result is not None else None}
            if not accepted:
                survivors.append(name + ":" + label)
        records.append({"case_id": name, "mutated_sha256": sha(raw), "outcomes": outcomes})

    symlink = cases / "route_symlink.json"
    symlink.symlink_to(control_path)
    outcomes = {}
    for label, script in (("primary", primary), ("independent", independent)):
        rc, result, stderr = invoke(script, paper, symlink, skill, repo,
                                    args.code_commit, cwd, hostile)
        consumer_invocations += 1
        accepted = exact_rejection(label, rc, result, stderr)
        outcomes[label] = {"accepted_rejection": accepted, "exit_code": rc,
                           "output_sha256": sha(canonical(result)) if result is not None else None}
        if not accepted:
            survivors.append("route_symlink:" + label)
    records.append({"case_id": "route_symlink", "mutated_sha256": None, "outcomes": outcomes})

    unrelated_outcomes: dict[str, Any] = {}
    rc, stdout, stderr = invoke_renderer(
        renderer, paper, skill, repo, args.unrelated_code_commit, cwd, hostile)
    consumer_invocations += 1
    try:
        error_terminal = stderr.decode("utf-8").splitlines()[-1]
    except Exception:
        error_terminal = "NON_UTF8_OR_EMPTY_STDERR"
    accepted = rc == 1 and not stdout \
        and error_terminal == "ValueError: code commit is not descended from frozen science H1"
    unrelated_outcomes["renderer"] = {
        "accepted_rejection": accepted, "exit_code": rc,
        "error_terminal": error_terminal, "stdout_sha256": sha(stdout),
    }
    if not accepted:
        survivors.append("unrelated_code_root:renderer")
    for label, script in (("primary", primary), ("independent", independent)):
        rc, result, stderr = invoke(script, paper, control_path, skill, repo,
                                    args.unrelated_code_commit, cwd, hostile)
        consumer_invocations += 1
        accepted = exact_rejection(label, rc, result, stderr)
        unrelated_outcomes[label] = {
            "accepted_rejection": accepted, "exit_code": rc,
            "output_sha256": sha(canonical(result)) if result is not None else None,
        }
        if not accepted:
            survivors.append("unrelated_code_root:" + label)
    records.append({
        "case_id": "unrelated_code_root",
        "fixture": {
            "code_blob_count": 4,
            "code_tree_entry_count": 4,
            "commit": args.unrelated_code_commit,
            "is_root_commit": True,
            "science_h1_is_ancestor": False,
        },
        "mutated_sha256": None,
        "outcomes": unrelated_outcomes,
    })

    if len(records) != 25 or consumer_invocations != 54:
        raise ValueError("mutation accounting drift")

    result = {
        "payload": {
            "code_commit": args.code_commit,
            "consumer_invocation_count": consumer_invocations,
            "hostile_import_control": "NAIVE_FAIL_ISOLATED_PASS",
            "mutation_case_count": len(records),
            "positive_control_count": 3,
            "rejection_invocation_count": 51,
            "records": records,
            "route_sha256": sha(source_raw),
            "survivor_count": len(survivors),
            "survivors": survivors,
            "unrelated_code_commit": args.unrelated_code_commit,
        },
        "schema": "paper44-route-v0.2-mutation-results-v2",
        "status": "PASS" if not survivors else "FAIL",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0 if not survivors else 1


if __name__ == "__main__":
    raise SystemExit(main())
