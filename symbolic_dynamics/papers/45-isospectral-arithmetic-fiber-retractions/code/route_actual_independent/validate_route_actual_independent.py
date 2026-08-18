#!/usr/bin/env python3
"""Independent YAML-node and manifest replay for Paper 45 Route-A v0.2."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
from pathlib import Path

import yaml


CONTRACT_REL = "code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json"
CONTRACT_SHA256 = "2aabfd7410a94125f7b0c740962ad1bcf95febead39d08c9ab616fb5e2359d69"
SCIENCE_SOURCE_COMMIT = "68369da38e651604cbee65df498846b863572448"
P45_PREFIX = "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions"
EXPECTED_TUPLE = ("A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL")
H1_CODE_PATHS = [
    "code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json",
    "code/route_actual_contract/ROUTE_ACTUAL_TEMPLATE.json",
    "code/route_actual_contract/render_route_actual.py",
    "code/route_actual_independent/validate_route_actual_independent.py",
    "code/route_actual_main/validate_route_actual_main.py",
    "code/tests/run_route_actual_tests.py",
]
ROUTE_TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls",
    "artifact_path_base", "blocking_conditions", "candidate_id", "claim_boundary",
    "evaluation_date", "next_smallest_test", "overall_verdict", "round2_clues",
    "route_b_invocation_allowed", "skill", "skill_version", "source_commit", "source_lock",
}
SOURCE_LOCK_KEYS = {
    "allowed_data", "arithmetic_origin", "clock", "cutoff", "determinant_convention",
    "forbidden_data", "normalization", "object", "precision",
}
EXPECTED_RESULT_NAMES = (
    "comparator_x.json", "evaluation_report.json", "evaluator_a.json", "evaluator_b.json",
    "integrity_audit.json", "mutation_outcomes.json", "proof_auditor_p.json",
)
EXPECTED_RESULT_MANIFEST_SHA256 = "2fae66ff866b63e7119fce7b86c928f589570572728cae942d758f4e599ad734"
TRUSTED_GIT = Path("/usr/bin/git")
TRUSTED_GIT_SHA256 = "fd7c9389e200d626b46551835e5233bbde49a6a2326f9ebb85c70ed235861001"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_true(value: bool, label: str) -> None:
    if not value:
        raise ValueError(label)


def reject_duplicate_nodes(node) -> None:
    if isinstance(node, yaml.MappingNode):
        seen = set()
        for key_node, value_node in node.value:
            if not isinstance(key_node, yaml.ScalarNode) or key_node.value in seen:
                raise ValueError("duplicate or nonscalar YAML key")
            seen.add(key_node.value)
            reject_duplicate_nodes(value_node)
    elif isinstance(node, yaml.SequenceNode):
        for child in node.value:
            reject_duplicate_nodes(child)


def read_yaml_without_duplicate_nodes(path: Path):
    raw = path.read_text(encoding="utf-8")
    syntax = yaml.compose(raw, Loader=yaml.BaseLoader)
    reject_duplicate_nodes(syntax)
    return yaml.safe_load(raw)


def read_json(path: Path):
    return json.loads(path.read_bytes())


def canonical_json(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_regular(root: Path, relative: str) -> Path:
    assert_true(re.fullmatch(r"[A-Za-z0-9._/-]+", relative) is not None, "relative path syntax")
    assert_true(not relative.startswith("/") and ".." not in Path(relative).parts, "relative path scope")
    target = root.joinpath(*relative.split("/"))
    assert_true(target.is_file() and not target.is_symlink(), "regular file")
    return target


def git_environment() -> dict[str, str]:
    return {
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_SYSTEM": "/dev/null",
        "GIT_NO_REPLACE_OBJECTS": "1",
        "GIT_OPTIONAL_LOCKS": "0",
        "GIT_TERMINAL_PROMPT": "0",
        "HOME": "/nonexistent-paper45-route-git-home",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": "/usr/bin:/bin",
        "TZ": "UTC",
    }


def validate_git_boundary(repository: Path) -> None:
    git_metadata = os.lstat(TRUSTED_GIT)
    repository_metadata = os.lstat(repository)
    dot_git = repository / ".git"
    dot_git_metadata = os.lstat(dot_git)
    assert_true(not TRUSTED_GIT.is_symlink() and stat.S_ISREG(git_metadata.st_mode), "trusted Git regular")
    assert_true(stat.S_IMODE(git_metadata.st_mode) == 0o755, "trusted Git mode")
    assert_true(digest(TRUSTED_GIT) == TRUSTED_GIT_SHA256, "trusted Git digest")
    assert_true(not repository.is_symlink() and stat.S_ISDIR(repository_metadata.st_mode), "repository regular directory")
    assert_true(repository.resolve(strict=True) == repository, "repository canonical path")
    assert_true(not dot_git.is_symlink() and stat.S_ISDIR(dot_git_metadata.st_mode), "repository .git directory")


def git(repository: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(TRUSTED_GIT), "--no-replace-objects", "--literal-pathspecs",
         "-C", str(repository), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=git_environment(),
    )


def replay_h1_tree(root: Path, repository: Path, commit: str, relatives: list[str]) -> dict:
    probe = git(repository, ["cat-file", "-t", commit])
    assert_true(probe.returncode == 0 and probe.stdout == b"commit\n" and not probe.stderr,
                "H1 commit type")
    repository_paths = [P45_PREFIX + "/" + relative for relative in relatives]
    listing = git(repository, ["ls-tree", "-z", "--full-tree", commit, "--", *repository_paths])
    assert_true(listing.returncode == 0 and not listing.stderr and listing.stdout.endswith(b"\0"),
                "H1 tree lookup")
    entries = {}
    for row in listing.stdout.rstrip(b"\0").split(b"\0"):
        match = re.fullmatch(rb"100644 blob ([0-9a-f]{40})\t([^\0]+)", row)
        assert_true(match is not None, "H1 exact 100644 blob row")
        path = match.group(2).decode("ascii")
        assert_true(path not in entries, "duplicate H1 tree row")
        entries[path] = match.group(1).decode("ascii")
    assert_true(set(entries) == set(repository_paths) and len(entries) == len(relatives),
                "H1 tree path closure")
    result = {}
    for relative in relatives:
        repo_path = P45_PREFIX + "/" + relative
        oid = entries[repo_path]
        blob = git(repository, ["cat-file", "blob", oid])
        local = safe_regular(root, relative)
        assert_true(blob.returncode == 0 and not blob.stderr and blob.stdout == local.read_bytes(),
                    "H1 tree bytes")
        result[relative] = {
            "git_blob": oid,
            "sha256": digest(local),
        }
    return result


def establish_science_ancestry(repository: Path, commit: str) -> None:
    result = git(repository, ["merge-base", "--is-ancestor", SCIENCE_SOURCE_COMMIT, commit])
    assert_true(result.returncode == 0 and not result.stdout and not result.stderr,
                "science source ancestry")


def replay_result_manifest(root: Path) -> dict[str, str]:
    path = root / "results/SHA256SUMS.txt"
    assert_true(digest(path) == EXPECTED_RESULT_MANIFEST_SHA256, "result manifest digest")
    rows = path.read_text(encoding="ascii").splitlines()
    assert_true(len(rows) == len(EXPECTED_RESULT_NAMES), "result manifest row count")
    observed = {}
    for row in rows:
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", row)
        assert_true(match is not None, "result manifest framing")
        expected_hash, name = match.groups()
        assert_true(name not in observed and name in EXPECTED_RESULT_NAMES, "result manifest name")
        target = root / "results" / name
        assert_true(target.is_file() and not target.is_symlink(), "result regular file")
        assert_true(digest(target) == expected_hash, "result row digest")
        observed[name] = expected_hash
    assert_true(tuple(sorted(observed)) == tuple(sorted(EXPECTED_RESULT_NAMES)), "result manifest path set")
    return observed


def validate(root: Path, canonical_skill: Path, repository: Path, expected_renderer_commit: str) -> dict:
    assert_true(re.fullmatch(r"[0-9a-f]{40}", expected_renderer_commit) is not None, "renderer commit syntax")
    assert_true(expected_renderer_commit != SCIENCE_SOURCE_COMMIT, "renderer/science separation")
    assert_true(canonical_skill.is_file() and not canonical_skill.is_symlink(), "canonical skill regular")
    validate_git_boundary(repository)

    contract_path = root / CONTRACT_REL
    assert_true(digest(contract_path) == CONTRACT_SHA256, "contract raw digest")
    contract_raw = contract_path.read_bytes()
    contract = read_json(contract_path)
    assert_true(contract_raw == canonical_json(contract), "contract canonical")
    assert_true(contract["schema"] == "paper45.route-a-v0.2-render-contract.v1", "contract schema")
    assert_true(contract["candidate_id"] == "P45-ALLH-RETRACTIONS", "contract identity")
    assert_true(contract["science_source_commit"] == SCIENCE_SOURCE_COMMIT, "contract science source")
    assert_true(tuple(contract["expected_tuple"]) == EXPECTED_TUPLE, "contract tuple")
    assert_true(contract["overall_verdict"] == "ROUTE_A_REJECTED", "contract overall")
    assert_true(contract["route_b_invocation_allowed"] is False, "contract route B")
    assert_true(contract["h1_static_code_paths"] == H1_CODE_PATHS, "H1 code paths")
    assert_true(contract["trusted_git"] == {
        "path": TRUSTED_GIT.as_posix(),
        "required_global_options": ["--no-replace-objects", "--literal-pathspecs"],
        "sha256": TRUSTED_GIT_SHA256,
    }, "trusted Git contract")
    assert_true(digest(canonical_skill) == contract["canonical_skill"]["sha256"], "canonical skill digest")

    template_path = safe_regular(root, contract["template_path"])
    assert_true(digest(template_path) == contract["template_sha256"], "template digest")
    template = read_json(template_path)
    assert_true(template_path.read_bytes() == canonical_json(template), "template canonical")
    assert_true(set(template) == ROUTE_TOP_KEYS, "canonical Route top-level keys")
    assert_true(set(template["source_lock"]) == SOURCE_LOCK_KEYS, "canonical source-lock keys")
    assert_true(digest(safe_regular(root, contract["renderer_path"])) == contract["renderer_sha256"], "renderer digest")

    establish_science_ancestry(repository, expected_renderer_commit)
    h1_blobs = replay_h1_tree(root, repository, expected_renderer_commit, H1_CODE_PATHS)
    h1_blob_map_sha256 = hashlib.sha256(
        json.dumps(h1_blobs, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()

    record_path = safe_regular(root, contract["record_path"])
    record_raw = record_path.read_bytes()
    record = read_yaml_without_duplicate_nodes(record_path)
    assert_true(record == template and record_raw == canonical_json(template), "exact committed template")

    assert_true(record["skill"] == "route-a-evaluator" and record["skill_version"] == "0.2.0", "skill")
    assert_true(record["candidate_id"] == "P45-ALLH-RETRACTIONS", "actual candidate identity")
    assert_true(record["candidate_id"] != "SD-C47", "unauthorized guessed identity")
    assert_true(record["source_commit"] == SCIENCE_SOURCE_COMMIT, "science source commit")
    actual_tuple = tuple(record[f"a{number}"]["verdict"] for number in range(5))
    assert_true(actual_tuple == EXPECTED_TUPLE, "actual tuple")
    assert_true(record["overall_verdict"] == "ROUTE_A_REJECTED", "overall")
    assert_true(record["route_b_invocation_allowed"] is False, "route B")
    assert_true(record["adversarial_controls"]["verdict"] == "STOP_SCOPED / PROVES_TOO_MUCH", "control disposition")
    assert_true(record["a0"]["evidence_status"] == "PROVED" and record["a1"]["evidence_status"] == "PROVED", "negative rung evidence")
    assert_true(record["a2"]["evidence_status"] == "PROVED", "determinant evidence")
    assert_true(record["a3"]["evidence_status"] == record["a4"]["evidence_status"] == "NOT_TESTABLE", "higher rungs")

    assert_true(len(contract["evidence_sha256"]) == 15, "evidence mapping size")
    assert_true(".paper45-publication-state/ROUTE.json" not in contract["evidence_sha256"], "no mutable publication input")
    for relative, expected_hash in contract["evidence_sha256"].items():
        assert_true(digest(safe_regular(root, relative)) == expected_hash, "contract evidence replay")

    artifact_rows = []
    for key in ("a0", "a1", "a2", "a3", "a4"):
        artifact_rows.extend(record[key]["artifacts"])
    for row in artifact_rows:
        assert_true(set(row) == {"path", "sha256"}, "artifact row shape")
        target = safe_regular(root, row["path"])
        assert_true(digest(target) == row["sha256"] == contract["evidence_sha256"][row["path"]], "artifact replay")

    integration = read_json(root / "code/contracts/INTEGRATION_CONTRACT.json")
    preoutput = read_json(root / "PREOUTPUT_STATUS.json")
    assert_true(integration["candidate_id"] == preoutput["candidate_id"] == record["candidate_id"], "candidate identity closure")
    assert_true(integration["route_expectation_sha256"] == digest(root / "inputs/preauthority/ROUTE_EXPECTATION.yaml"), "expectation hash")
    expectation = read_yaml_without_duplicate_nodes(root / "inputs/preauthority/ROUTE_EXPECTATION.yaml")
    assert_true(expectation["skill_version"] == "0.2.0", "expectation version")
    assert_true(tuple(expectation["expected_route_tuple"]) == actual_tuple, "expected-to-actual tuple")
    assert_true(expectation["overall_expectation"] == "ROUTE_A_REJECTED_NOT_EVALUATED", "historical expectation retained")
    assert_true(expectation["route_b_invocation_allowed"] is False, "historical route B lock")

    manifest = replay_result_manifest(root)
    report = read_json(root / "results/evaluation_report.json")
    assert_true(set(report) == {"c1", "c2", "contract_sha256", "external_disposition", "infinite_coverage", "mutation_survivors", "schema_version"}, "evaluation report keys")
    assert_true(report["c1"] == report["c2"] == "PASS" and report["external_disposition"] == "GO_EVALUATED", "science result")
    assert_true(report["mutation_survivors"] == 0, "science mutation result")
    coverage = report["infinite_coverage"]
    assert_true(coverage["verdict"] == "PASS" and coverage["b_infinite_count"] == coverage["p_audit_count"] == 15, "infinite coverage")
    assert_true(coverage["b_p_id_match"] is True and coverage["b_p_owner_hash_closure"] is True, "proof owner closure")

    evaluator_a = read_json(root / "results/evaluator_a.json")
    evaluator_b = read_json(root / "results/evaluator_b.json")
    assert_true(len(evaluator_a["finite_records"]) == 21 and len(evaluator_a["infinite_records"]) == 0, "A rows")
    assert_true(len(evaluator_b["finite_records"]) == 21 and len(evaluator_b["infinite_records"]) == 15, "B rows")
    proof = read_json(root / "results/proof_auditor_p.json")
    assert_true(proof["verdict"] == "PASS" and proof["findings"] == [], "proof verdict")
    assert_true(len(proof["per_case_audits"]) == 15 and all(row["verdict"] == "PASS" for row in proof["per_case_audits"]), "proof rows")
    assert_true(len(set(proof["audited_case_ids"])) == 15, "proof case IDs")

    comparison = read_json(root / "results/comparator_x.json")
    assert_true(comparison["verdict"] == "PASS", "comparison verdict")
    assert_true(comparison["exact_mismatch_count"] == comparison["interval_mismatch_count"] == 0, "comparison mismatch")

    mutations = read_json(root / "results/mutation_outcomes.json")["outcomes"]
    grouped = {}
    for outcome in mutations:
        grouped.setdefault(outcome["mutation_id"], []).append(outcome)
    assert_true(len(mutations) == 168 and len(grouped) == 75, "mutations")
    assert_true(all(row["outcome"] == "REJECT" and row["exit_code"] == 2 for row in mutations), "mutation rejection")

    integrity = read_json(root / "results/integrity_audit.json")
    assert_true(integrity["verdict"] == "PASS" and integrity["manifest_verified"] is True, "integrity")
    assert_true(integrity["path_policy_verified"] is True and integrity["second_run_zero_replacements"] is True, "transaction closure")
    assert_true(integrity["provenance"]["evaluator_output_seals"]["A"] == manifest["evaluator_a.json"], "A seal")
    assert_true(integrity["provenance"]["evaluator_output_seals"]["B"] == manifest["evaluator_b.json"], "B seal")

    return {
        "candidate_id": record["candidate_id"],
        "checks": 43,
        "code_commit": expected_renderer_commit,
        "h1_blob_map_sha256": h1_blob_map_sha256,
        "h1_static_blob_count": len(h1_blobs),
        "manifest_rows": len(manifest),
        "mutation_instances": len(grouped),
        "mutation_outcomes": len(mutations),
        "record_sha256": hashlib.sha256(record_raw).hexdigest(),
        "route_b_invocation_allowed": False,
        "schema": "paper45.route-a-v0.2-independent-validation.v2",
        "science_ancestor_check": "PASS",
        "science_source_commit": SCIENCE_SOURCE_COMMIT,
        "status": "PASS",
        "trusted_git_path": TRUSTED_GIT.as_posix(),
        "trusted_git_sha256": TRUSTED_GIT_SHA256,
        "tuple": list(actual_tuple),
        "verdict": "ROUTE_A_REJECTED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--canonical-skill", type=Path, required=True)
    parser.add_argument("--git-repo", type=Path, required=True)
    parser.add_argument("--expected-renderer-commit", required=True)
    args = parser.parse_args()
    try:
        receipt = validate(
            args.root.resolve(strict=True),
            args.canonical_skill.resolve(strict=True),
            args.git_repo.resolve(strict=True),
            args.expected_renderer_commit,
        )
    except Exception as error:
        print(json.dumps({
            "code": "ROUTE_ACTUAL_INDEPENDENT_REJECT",
            "exception_type": type(error).__name__,
            "schema": "paper45.route-a-v0.2-independent-validation.v2",
            "status": "REJECT",
        }, sort_keys=True, separators=(",", ":")))
        return 2
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
