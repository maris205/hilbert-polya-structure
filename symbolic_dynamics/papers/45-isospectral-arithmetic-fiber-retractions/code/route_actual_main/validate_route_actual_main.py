#!/usr/bin/env python3
"""Strict JSON-first validator for the actual Paper 45 Route-A v0.2 record."""

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


CONTRACT_REL = Path("code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json")
CONTRACT_SHA256 = "2aabfd7410a94125f7b0c740962ad1bcf95febead39d08c9ab616fb5e2359d69"
SCIENCE_SOURCE_COMMIT = "68369da38e651604cbee65df498846b863572448"
CANDIDATE = "P45-ALLH-RETRACTIONS"
P45_PREFIX = "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"]
H1_CODE_PATHS = [
    "code/route_actual_contract/ROUTE_ACTUAL_CONTRACT.json",
    "code/route_actual_contract/ROUTE_ACTUAL_TEMPLATE.json",
    "code/route_actual_contract/render_route_actual.py",
    "code/route_actual_independent/validate_route_actual_independent.py",
    "code/route_actual_main/validate_route_actual_main.py",
    "code/tests/run_route_actual_tests.py",
]
TOP_KEYS = {
    "a0", "a1", "a2", "a3", "a4", "adversarial_controls",
    "artifact_path_base", "blocking_conditions", "candidate_id", "claim_boundary",
    "evaluation_date", "next_smallest_test", "overall_verdict", "round2_clues",
    "route_b_invocation_allowed", "skill", "skill_version", "source_commit", "source_lock",
}
BLOCK_KEYS = {
    "a0": {"arithmetic_controls", "artifacts", "evidence_status", "strongest_evidence", "strongest_failure", "verdict"},
    "a1": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
    "a2": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
    "a3": {"analytic_structure", "artifacts", "evidence_status", "strongest_evidence", "strongest_failure", "verdict", "weil_compression"},
    "a4": {"artifacts", "evidence_status", "metrics", "strongest_evidence", "strongest_failure", "verdict"},
}
SOURCE_LOCK_KEYS = {
    "allowed_data", "arithmetic_origin", "clock", "cutoff", "determinant_convention",
    "forbidden_data", "normalization", "object", "precision",
}
EVIDENCE_LABELS = {
    "PROVED", "CONDITIONAL_THEOREM", "NUMERICALLY_CERTIFIED", "NUMERICAL_OBSERVATION",
    "HEURISTIC", "MODELING_CHOICE", "FITTED_PARAMETER", "OPEN", "REFUTED",
    "NOT_TESTABLE", "STOP_SCOPED",
}
HASHES = {
    "code/contracts/INTEGRATION_CONTRACT.json": "32edd4caf36a388758a76af8e8b160543f7c5f08aabe72f2f2c9da601487957b",
    "inputs/preauthority/EXPERIMENT_CONTRACT.json": "6ff3776a29b1211762b929782b556d0cae71a60ec97b102863059fc5bf302fbe",
    "inputs/preauthority/LITERATURE_NOVELTY_AUDIT.md": "070151a7526b74f6b7eae7e4a4cff1a0e8411d0114801c91bfb766570575bd75",
    "inputs/preauthority/OBJECT_MARKER_OPERATOR_CONTRACT.md": "117e509bfd2adf2233e0c8a04289eb66801140791ed06deb3948ee9ccce606f9",
    "inputs/preauthority/PROOF_PACKAGE.md": "964d7bd6ccc37cd95dff28b2b82a3903e25eb337afcde11310f299a75e40acd8",
    "inputs/preauthority/ROUTE_EXPECTATION.yaml": "d02ce9f054567aa6d0c8e099797920ea9d29bbcebc062c4874b11baaab6b9c01",
    "inputs/preauthority/SOURCE_LOCK.md": "061f43593b85e1458860a0c9ea902350891674cadb41001f52789ad42c24f4cf",
    "results/SHA256SUMS.txt": "2fae66ff866b63e7119fce7b86c928f589570572728cae942d758f4e599ad734",
    "results/comparator_x.json": "6a8404c802342e9ea37fc311ecb23492f2503fa7137258a46b416aafaaee12c5",
    "results/evaluation_report.json": "4c5efa633213cd6f056b550c562dbf9929b3a7145aae33149b482ecd3fec0b5b",
    "results/evaluator_a.json": "ba3f374f1e65e3598c7d4e769144514e911f5be268ae36afc90000df5a5154da",
    "results/evaluator_b.json": "ac8226e8d9a726ebf78e753d66b19e200ba382a5ecdc926ff79a262c7c81a675",
    "results/integrity_audit.json": "fef14966637e160367f545e7c6ee9f53399c6f3de3f6a01b74614ac3bff94c9b",
    "results/mutation_outcomes.json": "8042263d0ddd43b3b2c8c27737c10a053b422e1dfbf9667f292a4b5bba4f147b",
    "results/proof_auditor_p.json": "1a62f35af5b7147599d23139231f17443c14970612ac115387a484b84b60ce4d",
}
TRUSTED_GIT = Path("/usr/bin/git")
TRUSTED_GIT_SHA256 = "fd7c9389e200d626b46551835e5233bbde49a6a2326f9ebb85c70ed235861001"


class DuplicateKey(ValueError):
    pass


def strict_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKey(key)
        value[key] = item
    return value


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_json_bytes(raw: bytes):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=strict_pairs)


def strict_json(path: Path):
    return strict_json_bytes(path.read_bytes())


def canonical_json(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode("utf-8")


def under(root: Path, relative: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", relative) or relative.startswith("/"):
        raise ValueError("unsafe path")
    candidate = root.joinpath(*relative.split("/"))
    if ".." in Path(relative).parts or candidate.is_symlink() or not candidate.is_file():
        raise ValueError("nonregular evidence path")
    return candidate


def require(condition: bool, label: str) -> None:
    if not condition:
        raise ValueError(label)


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
    require(not TRUSTED_GIT.is_symlink() and stat.S_ISREG(git_metadata.st_mode), "trusted Git regular")
    require(stat.S_IMODE(git_metadata.st_mode) == 0o755, "trusted Git mode")
    require(digest(TRUSTED_GIT) == TRUSTED_GIT_SHA256, "trusted Git digest")
    require(not repository.is_symlink() and stat.S_ISDIR(repository_metadata.st_mode), "repository regular directory")
    require(repository.resolve(strict=True) == repository, "repository canonical path")
    require(not dot_git.is_symlink() and stat.S_ISDIR(dot_git_metadata.st_mode), "repository .git directory")


def git(repository: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(TRUSTED_GIT), "--no-replace-objects", "--literal-pathspecs",
         "-C", str(repository), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=git_environment(),
    )


def verify_h1_blobs(root: Path, repository: Path, commit: str, relatives: list[str]) -> dict:
    probe = git(repository, ["cat-file", "-t", commit])
    require(probe.returncode == 0 and probe.stdout == b"commit\n" and not probe.stderr,
            "expected H1 commit unreadable")
    repository_paths = [P45_PREFIX + "/" + relative for relative in relatives]
    listing = git(repository, ["ls-tree", "-z", "--full-tree", commit, "--", *repository_paths])
    require(listing.returncode == 0 and not listing.stderr and listing.stdout.endswith(b"\0"),
            "H1 tree lookup")
    entries = {}
    for row in listing.stdout.rstrip(b"\0").split(b"\0"):
        match = re.fullmatch(rb"100644 blob ([0-9a-f]{40})\t([^\0]+)", row)
        require(match is not None, "H1 exact 100644 blob entry")
        path = match.group(2).decode("ascii")
        require(path not in entries, "duplicate H1 tree entry")
        entries[path] = match.group(1).decode("ascii")
    require(set(entries) == set(repository_paths) and len(entries) == len(relatives),
            "H1 tree path closure")
    result = {}
    for relative in relatives:
        local = under(root, relative)
        repo_path = P45_PREFIX + "/" + relative
        oid = entries[repo_path]
        blob_run = git(repository, ["cat-file", "blob", oid])
        require(blob_run.returncode == 0 and not blob_run.stderr, "H1 blob lookup")
        require(blob_run.stdout == local.read_bytes(), "H1 blob byte mismatch")
        result[relative] = {"git_blob": oid, "sha256": digest(local)}
    return result


def require_science_ancestor(repository: Path, commit: str) -> None:
    ancestry = git(repository, ["merge-base", "--is-ancestor", SCIENCE_SOURCE_COMMIT, commit])
    require(ancestry.returncode == 0 and not ancestry.stdout and not ancestry.stderr,
            "science source is not ancestor of renderer H1")


def validate(root: Path, canonical_skill: Path, repository: Path, expected_renderer_commit: str) -> dict:
    require(re.fullmatch(r"[0-9a-f]{40}", expected_renderer_commit) is not None, "renderer commit syntax")
    require(expected_renderer_commit != SCIENCE_SOURCE_COMMIT, "renderer commit distinct from science source")
    require(canonical_skill.is_file() and not canonical_skill.is_symlink(), "canonical skill regular")
    validate_git_boundary(repository)

    contract_path = root / CONTRACT_REL
    contract_raw = contract_path.read_bytes()
    contract = strict_json_bytes(contract_raw)
    require(digest(contract_path) == CONTRACT_SHA256, "render contract digest")
    require(contract_raw == canonical_json(contract), "render contract canonical bytes")
    require(contract["schema"] == "paper45.route-a-v0.2-render-contract.v1", "render contract schema")
    require(contract["candidate_id"] == CANDIDATE, "render contract identity")
    require(contract["science_source_commit"] == SCIENCE_SOURCE_COMMIT, "render contract science source")
    require(contract["expected_tuple"] == TUPLE, "render contract tuple")
    require(contract["overall_verdict"] == "ROUTE_A_REJECTED", "render contract overall")
    require(contract["route_b_invocation_allowed"] is False, "render contract route B")
    require(contract["evidence_sha256"] == HASHES, "render contract evidence set")
    require(contract["h1_static_code_paths"] == H1_CODE_PATHS, "H1 static code path set")
    require(contract["trusted_git"] == {
        "path": TRUSTED_GIT.as_posix(),
        "required_global_options": ["--no-replace-objects", "--literal-pathspecs"],
        "sha256": TRUSTED_GIT_SHA256,
    }, "trusted Git contract")
    require(digest(canonical_skill) == contract["canonical_skill"]["sha256"], "canonical skill digest")
    require(contract["canonical_skill"] == {
        "path": "skills/route-a-evaluator.md",
        "sha256": "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a",
        "version": "0.2.0",
    }, "canonical skill contract")
    require(digest(under(root, contract["renderer_path"])) == contract["renderer_sha256"], "renderer digest")

    template_path = under(root, contract["template_path"])
    template_raw = template_path.read_bytes()
    template = strict_json_bytes(template_raw)
    require(digest(template_path) == contract["template_sha256"], "template digest")
    require(template_raw == canonical_json(template), "template canonical bytes")
    require(len(template) == 19 and len(template["source_lock"]) == 9, "canonical Route schema shape")

    require_science_ancestor(repository, expected_renderer_commit)
    h1_blobs = verify_h1_blobs(root, repository, expected_renderer_commit, H1_CODE_PATHS)
    h1_blob_map_sha256 = hashlib.sha256(
        json.dumps(h1_blobs, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()

    record_path = under(root, contract["record_path"])
    raw = record_path.read_bytes()
    record = strict_json_bytes(raw)
    require(raw == canonical_json(record), "record canonical bytes")
    require(record == template, "record differs from committed template")

    require(type(record) is dict and set(record) == TOP_KEYS, "record top keys")
    require(record["skill"] == "route-a-evaluator" and record["skill_version"] == "0.2.0", "skill version")
    require(record["candidate_id"] == CANDIDATE, "candidate identity")
    require(record["candidate_id"] != "SD-C47", "guessed canonical identity")
    require(record["source_commit"] == SCIENCE_SOURCE_COMMIT, "science source commit")
    require(record["artifact_path_base"] == "papers/45-isospectral-arithmetic-fiber-retractions", "artifact base")
    require(record["evaluation_date"] == "2026-08-19", "date")
    require(record["overall_verdict"] == "ROUTE_A_REJECTED", "overall")
    require(record["route_b_invocation_allowed"] is False, "route B")
    require(type(record["round2_clues"]) is list and not record["round2_clues"], "round2")
    require(type(record["blocking_conditions"]) is list and len(record["blocking_conditions"]) == 6, "blockers")
    require(type(record["source_lock"]) is dict and set(record["source_lock"]) == SOURCE_LOCK_KEYS, "source lock keys")
    require(record["source_lock"]["clock"] == "not_applicable_no_dynamical_primitive_clock", "clock")
    require("GO_EVALUATED" not in record["overall_verdict"], "external disposition retyped")

    for number, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        block = record[key]
        require(type(block) is dict and set(block) == BLOCK_KEYS[key], key + " keys")
        require(block["verdict"] == TUPLE[number], key + " verdict")
        require(block["evidence_status"] in EVIDENCE_LABELS, key + " evidence label")
        require(type(block["artifacts"]) is list and block["artifacts"], key + " artifacts")
        for artifact in block["artifacts"]:
            require(type(artifact) is dict and set(artifact) == {"path", "sha256"}, "artifact shape")
            evidence = under(root, artifact["path"])
            require(HASHES.get(artifact["path"]) == artifact["sha256"] == digest(evidence), "artifact digest")

    for relative, expected in HASHES.items():
        require(digest(under(root, relative)) == expected, "frozen evidence drift")

    integration = strict_json(root / "code/contracts/INTEGRATION_CONTRACT.json")
    require(integration["candidate_id"] == CANDIDATE, "integration identity")
    require(integration["experiment_contract_sha256"] == HASHES["inputs/preauthority/EXPERIMENT_CONTRACT.json"], "experiment binding")
    require(integration["route_expectation_sha256"] == HASHES["inputs/preauthority/ROUTE_EXPECTATION.yaml"], "expectation binding")
    require(integration["evaluator_a"]["finite_record_count"] == 21 and integration["evaluator_b"]["finite_record_count"] == 21, "finite contract")
    require(integration["evaluator_b"]["infinite_record_count"] == 15 and integration["proof_auditor"]["per_case_count"] == 15, "infinite contract")
    require(integration["mutation_count"] == 75 and integration["mutation_consumer_outcome_count"] == 168, "mutation contract")

    expectation = yaml.safe_load((root / "inputs/preauthority/ROUTE_EXPECTATION.yaml").read_text(encoding="utf-8"))
    require(expectation["skill_version"] == "0.2.0", "expectation version")
    require(expectation["expected_route_tuple"] == TUPLE, "expectation tuple")
    require(expectation["overall_expectation"] == "ROUTE_A_REJECTED_NOT_EVALUATED", "historical expectation state")
    require(expectation["route_b_invocation_allowed"] is False, "expectation route B")

    report = strict_json(root / "results/evaluation_report.json")
    require(report["c1"] == report["c2"] == "PASS", "science gates")
    require(report["external_disposition"] == "GO_EVALUATED", "external disposition")
    require(report["mutation_survivors"] == 0 and report["infinite_coverage"]["verdict"] == "PASS", "science closure")
    require(report["infinite_coverage"]["b_infinite_count"] == report["infinite_coverage"]["p_audit_count"] == 15, "infinite coverage")
    require(report["infinite_coverage"]["b_p_owner_hash_closure"] is True, "owner hash closure")

    comparator = strict_json(root / "results/comparator_x.json")
    require(comparator["verdict"] == "PASS" and comparator["exact_mismatch_count"] == 0 and comparator["interval_mismatch_count"] == 0, "comparator")
    evaluator_a = strict_json(root / "results/evaluator_a.json")
    evaluator_b = strict_json(root / "results/evaluator_b.json")
    require(len(evaluator_a["finite_records"]) == 21 and len(evaluator_a["infinite_records"]) == 0, "evaluator A")
    require(len(evaluator_b["finite_records"]) == 21 and len(evaluator_b["infinite_records"]) == 15, "evaluator B")
    proof = strict_json(root / "results/proof_auditor_p.json")
    require(proof["verdict"] == "PASS" and proof["findings"] == [] and len(proof["audited_case_ids"]) == 15, "proof audit")
    mutations = strict_json(root / "results/mutation_outcomes.json")["outcomes"]
    require(len(mutations) == 168 and len({row["mutation_id"] for row in mutations}) == 75, "mutation cardinality")
    require(all(row["outcome"] == "REJECT" and row["exit_code"] == 2 for row in mutations), "mutation survivors")

    bundle = hashlib.sha256("".join(HASHES[key] for key in sorted(HASHES)).encode("ascii")).hexdigest()
    return {
        "candidate_id": CANDIDATE,
        "checks": 48,
        "code_commit": expected_renderer_commit,
        "evidence_bundle_sha256": bundle,
        "h1_blob_map_sha256": h1_blob_map_sha256,
        "h1_static_blob_count": len(h1_blobs),
        "record_sha256": hashlib.sha256(raw).hexdigest(),
        "route_b_invocation_allowed": False,
        "schema": "paper45.route-a-v0.2-main-validation.v2",
        "science_ancestor_check": "PASS",
        "science_source_commit": SCIENCE_SOURCE_COMMIT,
        "status": "PASS",
        "trusted_git_path": TRUSTED_GIT.as_posix(),
        "trusted_git_sha256": TRUSTED_GIT_SHA256,
        "tuple": TUPLE,
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
        receipt = {
            "code": "ROUTE_ACTUAL_MAIN_REJECT",
            "exception_type": type(error).__name__,
            "schema": "paper45.route-a-v0.2-main-validation.v2",
            "status": "REJECT",
        }
        print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
        return 2
    print(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
