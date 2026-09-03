#!/usr/bin/env python3
"""Fail-closed final audit for Round 10 / Papers 29--33 / Stage 3 prime.

This audit replays the ARS mechanical checker, verifies every frozen hash chain,
checks the separately persisted semantic-audit evidence, reconciles current
status documentation, and proves that no successor/science/Route mutation has
been created.  It never edits manuscripts or authorizes a successor stage.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN_DECLARED_PROJECT_ROOT = Path("/root/autodl-tmp/flow_systems")
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
CONTRACTS = ARS / "shared/contracts/re_review"
CHECKER = ARS / "scripts/check_re_review_synthesis.py"
PANEL_VALIDATOR = ARS / "scripts/review_panel_provenance.py"
WORKFLOW = ARS / "academic-paper-reviewer/WORKFLOW.md"
PROTOCOL = ARS / "academic-paper-reviewer/references/re_review_mode_protocol.md"
OUTPUT = ROOT / "BATCH_ROUND10_STAGE3_PRIME_FINAL_AUDIT.json"
ROUTE_A = ROOT / "skills/route-a-evaluator.md"
ROUTE_B = ROOT / "skills/route-b-evaluator.md"

# Updated only by a deliberate terminal rebuild.  These constants prevent the
# outcome receipt from authenticating an arbitrary self-consistent replacement
# report or checkpoint.
TERMINAL_HASHES = {
    "batch_report":
        "0343b34e2fcb80477046ac5cd0ea069fe51f6efe162edf18dc32b51ad25d0672",
    "mandatory_checkpoint":
        "c646d67cf1f39b8a8723f501d7c17a12489737080234c37f631d6330b90034ae",
    "outcome_receipt":
        "cfa61eb8504c45250b1658d63193475567a2e8fd0afc1037ef6eda580c196852",
}

BATCH_HASHES = {
    "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json":
        "9628917f81d07288dbb6a255f922c397ca87cf4114df61a07fe600c02cfb97bd",
    "BATCH_ROUND10_STAGE3_PRIME_AUTHOR_EVENT_20260903.txt":
        "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
    "BATCH_ROUND10_STAGE3_PRIME_AUTHORIZATION_RECORD.md":
        "0c3932af8cf8d5e5f8636cfd24491aee6216ec01cdc136b61091cc3433de0d4d",
    "BATCH_ROUND10_STAGE3_PRIME_INPUT_MANIFEST_RECEIPT.json":
        "69ba576eec4cfb9cedd61bceec0d8255807f35c49760c7d3e90d465cbcb88c6a",
    "BATCH_ROUND10_STAGE3_PRIME_PHASE1_VALIDATION.json":
        "729c8cae0f4926d3a4d55f108200abe7103f0b7683cf14166168b8a237ad8d9f",
    "BATCH_ROUND10_STAGE3_PRIME_PHASE2A_VALIDATION.json":
        "9ad14f3f7fcfae944287d2eb48e4d54948d863792c5fb0032b222aa0b260343d",
    "BATCH_ROUND10_STAGE3_PRIME_PHASE2B_INTEGRATION_VALIDATION.json":
        "449f2b9ca4ee6220bc56021c17638ab1f0edbca67ef9d0f40e848b6c4efdd1b3",
}

SEMANTIC_HASHES = {
    "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json":
        "315f49d33677b31d900cd8147bb5d11f4d72f8aa54d0df1a8a79a94497844883",
    "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json":
        "3605a8f846c7e908421680bac91b5a075a750efd60700a677ca41175b667515f",
    "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json":
        "550a765db4851d15dbf8efc1f3bef5a5d82e90ecaee619cdad366c120d7c3ba4",
    "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json":
        "cc59faf29dbbaf85ba67bfb231c797fa37ac2156390cc02280724e781caabadb",
    "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json":
        "43c65150a5edb6afde58c6abde0f0718272918e3dc26326238a6ae41e0187171",
}

PAPERS = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "recorded": (7, 4, 0), "audited": (6, 5, 0),
        "status": "ABORTED", "abort": "phase2a_lint_failed", "rule": "B4",
        "state": "stage3_prime_round1_aborted_awaiting_round2_authorization",
        "trace": "a0f7cf092db710519af0556f4e0dddd85c8f2ddb3c80ec210636aa138c8b72f9",
        "route": "3946edf4f1f2ffc52343f9e9471b81bef590c59bd084ad5db049b6cb89da9445",
        "system": "Frozen system: torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal.",
        "canonical": {
            "paper/manuscript.tex": "5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034",
            "paper/references.bib": "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
            "paper/paper.pdf": "14dd360e0152da9c976c88bfe3ca197449017d49e09ea75279d4099457f1044e",
        },
        "inventory": {
            "baseline_entries": 140,
            "baseline_sha256": "926b2e5e9dbb1a883166e41b5eb3224ee4ba30acb89f59414560fa2ec57a021f",
            "round1_entries": 13,
            "round1_sha256": "87efa3d96aff31ae916ab84a5af4ab122a7d71be13f72022a0e7377bc46026bf",
        },
    },
    "P30": {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "recorded": (4, 5, 0), "audited": (4, 5, 0),
        "status": "ABORTED", "abort": "phase1_lint_failed", "rule": "B4",
        "state": "stage3_prime_round1_aborted_awaiting_round2_authorization",
        "trace": "f12ec18e78bd158e425b41eefcc158e108caea9d19f6566000b33f48d5a3ce94",
        "route": "d1af9901e66450ca88d01419a9fe02d6606bac2f7e7e0999a14a9213bb9ce166",
        "system": "Frozen system: no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control.",
        "canonical": {
            "paper/manuscript.tex": "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
            "paper/references.bib": "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
            "paper/paper.pdf": "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e",
        },
        "inventory": {
            "baseline_entries": 140,
            "baseline_sha256": "a3aa2b956ef7fcb54a8d0b1ab749e35849706f2f7b3e86cb7939b0ad928b6468",
            "round1_entries": 13,
            "round1_sha256": "ff067a708c903e4eb3cef746478d76987f343aca0fdac22fde558ef3b40d1d37",
        },
    },
    "P31": {
        "slug": "31-level11-conjugacy-owner-ledger",
        "recorded": (4, 6, 1), "audited": (3, 7, 1),
        "status": "ABORTED", "abort": "phase1_lint_failed", "rule": "B3",
        "state": "stage3_prime_round1_aborted_awaiting_round2_authorization",
        "trace": "2d1b11aa0cac043b738bb60bbc71b959b7ff93f9c2338e37ff38b3a97a6bee27",
        "route": "e851c2ee493414fe26321740aac277e95cd196372a11bc2618eb089b8ad1eff2",
        "system": "Frozen system: fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct.",
        "canonical": {
            "paper/manuscript.tex": "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
            "paper/references.bib": "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
            "paper/paper.pdf": "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722",
        },
        "inventory": {
            "baseline_entries": 143,
            "baseline_sha256": "5c48cf3388779063f9db3ce3b4311f05abb32e0a08851ec8c382f8f30f06b30e",
            "round1_entries": 13,
            "round1_sha256": "eff8763be9f54dc02fd716f1e480172a9ec311c0232287ed7dbf899f2f49e342",
        },
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "recorded": (6, 5, 1), "audited": (6, 5, 1),
        "status": "ABORTED", "abort": "phase1_lint_failed", "rule": "B3",
        "state": "stage3_prime_round1_aborted_awaiting_round2_authorization",
        "trace": "8357e6a0463a4bfd3ff5b17913725642053c4a2f59681f216349c1bd498983db",
        "route": "570b8d7307913495053c69560ccd04e0d37ab6dbcd99fbe53248b81db296fcda",
        "system": "Frozen system: unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3.",
        "canonical": {
            "paper/manuscript.tex": "4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a",
            "paper/references.bib": "e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9",
            "paper/paper.pdf": "66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93",
        },
        "inventory": {
            "baseline_entries": 139,
            "baseline_sha256": "31ecf6fef631616fc0957d4ae130eeca548f90f18a249317c4327a92286c96c1",
            "round1_entries": 13,
            "round1_sha256": "792590a2e23cb9a42498768c5b65a6baf351c497e47e5d46da4ee25770e5487c",
        },
    },
    "P33": {
        "slug": "33-bolza-control-matched-census",
        "recorded": (6, 7, 0), "audited": (6, 7, 0),
        "status": "ABORTED", "abort": "phase1_lint_failed", "rule": "B4",
        "state": "stage3_prime_round1_aborted_awaiting_round2_authorization",
        "trace": "ef46c682d1444f8c9552b54d09853e5bcc3085da5e90397d5f6b2bb010eb5afa",
        "route": "0434982b38bf658bfd808469671431f089140850ceb2c01875539ef997f942cf",
        "system": "Frozen system: unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule.",
        "canonical": {
            "paper/manuscript.tex": "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
            "paper/references.bib": "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
            "paper/paper.pdf": "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031",
        },
        "inventory": {
            "baseline_entries": 142,
            "baseline_sha256": "c1d3963a624de72f024ac4440a3a38b78daa1ed2fa95f63d26df76a01b3bca1e",
            "round1_entries": 13,
            "round1_sha256": "60558354b3e548e844736e8a5af4d074e3bad5f19e1cd7039481a883a23af264",
        },
    },
}

# These are the only paths added or rewritten by the authorized Stage 3-prime
# Round-1 publication.  The complementary tree is bound to the independently
# checked Stage-4 baseline hashes above.  Exact membership (rather than a
# filename prefix) ensures that an extra, plausibly named output cannot hide
# from the closed inventory.
ROUND1_PAPER_PATHS = {
    "README.md",
    "notes/pipeline_state.md",
    "paper/README.md",
    "notes/stage3_prime_round1_abort_record.json",
    "notes/stage3_prime_round1_checker_receipt.json",
    "notes/stage3_prime_round1_input_manifest.json",
    "notes/stage3_prime_round1_phase1_receipt.md",
    "notes/stage3_prime_round1_phase2a_receipt.md",
    "notes/stage3_prime_round1_phase2b_integration.json",
    "notes/stage3_prime_round1_precommitment.json",
    "notes/stage3_prime_round1_traceability.json",
    "notes/stage3_prime_round1_verdict_record.json",
    "notes/stage3_prime_round1_verification_report.md",
}

EXPECTED_PAPER_TOP_LEVEL = {
    "README.md": "file",
    "code": "directory",
    "experiments": "directory",
    "notes": "directory",
    "paper": "directory",
    "results": "directory",
}


def path_has_no_symlink_components(path: Path) -> bool:
    """Check every lexical component, including the file itself, with lstat."""
    absolute = Path(os.path.abspath(path))
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return False
    return True


def real_regular_file(path: Path) -> bool:
    """Accept only regular, no-symlink files under the project or ARS package."""
    absolute = Path(os.path.abspath(path))
    allowed_roots = (ROOT, ARS.parent)
    if not any(absolute.is_relative_to(base) for base in allowed_roots):
        return False
    return path_has_no_symlink_components(absolute) and absolute.is_file()


def digest(path: Path) -> str:
    if not real_regular_file(path):
        raise ValueError(f"not a real regular allowed file: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> object:
    if not real_regular_file(path):
        raise ValueError(f"not a real regular allowed JSON file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    if not real_regular_file(path):
        raise ValueError(f"not a real regular allowed text file: {path}")
    return path.read_text(encoding="utf-8")


def canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def jcs_digest(value: object) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def atomic_write_json(path: Path, value: object) -> None:
    """Publish JSON without following an existing target symlink or truncating it."""
    target = Path(os.path.abspath(path))
    parent = target.parent
    if parent != ROOT or not parent.is_dir() or not path_has_no_symlink_components(parent):
        raise ValueError(f"unsafe audit-output parent: {parent}")
    if target.is_symlink() or (target.exists() and not target.is_file()):
        raise ValueError(f"unsafe audit-output target: {target}")

    payload = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    descriptor, temporary_name = tempfile.mkstemp(
        dir=parent, prefix=f".{target.name}.", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError(f"audit-output target changed type: {target}")
        os.replace(temporary, target)
        temporary = None
        directory_descriptor = os.open(parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def valid_terminal_binding(binding: object) -> bool:
    if not isinstance(binding, dict) or set(binding) != {"path", "sha256"}:
        return False
    rel = binding.get("path")
    sha = binding.get("sha256")
    if not isinstance(rel, str) or not rel or Path(rel).is_absolute():
        return False
    try:
        candidate = Path(os.path.abspath(ROOT / rel))
        candidate.relative_to(ROOT)
    except ValueError:
        return False
    return (real_regular_file(candidate) and isinstance(sha, str) and
            len(sha) == 64 and
            all(char in "0123456789abcdef" for char in sha))


def manifest_path(paper: Path, entry: dict[str, object]) -> Path:
    ref = str(entry["path_or_passport_ref"])
    if not ref.startswith("path:"):
        raise ValueError(f"unsupported manifest reference: {ref}")
    return paper / ref.removeprefix("path:")


def declared_path(value: str) -> Path:
    """Resolve evidence paths portably and independently of the caller's cwd.

    Persisted semantic evidence was authored in the frozen project checkout and
    may contain that checkout's absolute prefix.  Map only that exact project
    prefix into the checkout containing this audit; keep external ARS paths
    absolute and unchanged.
    """
    path = Path(value)
    if not path.is_absolute():
        return Path(os.path.abspath(ROOT / path))
    absolute = Path(os.path.abspath(path))
    if absolute.is_relative_to(FROZEN_DECLARED_PROJECT_ROOT):
        return ROOT / absolute.relative_to(FROZEN_DECLARED_PROJECT_ROOT)
    return absolute


def declared_hash_entries(value: object):
    """Yield (path, sha256) leaves from nested declared-path hash maps."""
    if not isinstance(value, dict):
        return
    for key, child in value.items():
        if isinstance(child, str):
            yield key, child
        elif isinstance(child, dict):
            yield from declared_hash_entries(child)


def tree_inventory(root: Path) -> list[dict[str, str]]:
    """Return a deterministic path/type/content inventory without following links."""
    rows: list[dict[str, str]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            row = {"path": relative, "type": "symlink"}
        elif path.is_dir():
            row = {"path": relative, "type": "directory"}
        elif path.is_file():
            row = {"path": relative, "type": "file", "sha256": digest(path)}
        else:
            row = {"path": relative, "type": "other"}
        rows.append(row)
    return rows


def main() -> int:
    # Keep the only non-stdlib dependency inside the structured-failure
    # boundary established by the module's __main__ wrapper.
    from jsonschema import Draft202012Validator

    failures: list[str] = []
    checks: list[str] = []

    def check(condition: bool, label: str) -> None:
        if condition:
            checks.append(label)
        else:
            failures.append(label)

    check(ROOT.is_dir() and path_has_no_symlink_components(ROOT),
          "project root is a real no-symlink directory")
    check(ARS.parent.is_dir() and path_has_no_symlink_components(ARS.parent),
          "ARS package root is a real no-symlink directory")

    # Immutable entry authorization and gate-validation receipts.
    for rel, expected in BATCH_HASHES.items():
        path = ROOT / rel
        exists = real_regular_file(path)
        check(exists, f"batch artifact is a real regular file: {rel}")
        if exists:
            check(digest(path) == expected, f"batch artifact frozen hash: {rel}")
    check(digest(ROUTE_A) ==
          "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
          "Route-A evaluator frozen hash")
    check(digest(ROUTE_B) ==
          "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
          "Route-B evaluator frozen hash")

    phase1 = load_json(ROOT / "BATCH_ROUND10_STAGE3_PRIME_PHASE1_VALIDATION.json")
    phase2a = load_json(ROOT / "BATCH_ROUND10_STAGE3_PRIME_PHASE2A_VALIDATION.json")
    phase2b = load_json(ROOT / "BATCH_ROUND10_STAGE3_PRIME_PHASE2B_INTEGRATION_VALIDATION.json")
    input_receipt = load_json(ROOT / "BATCH_ROUND10_STAGE3_PRIME_INPUT_MANIFEST_RECEIPT.json")
    p1_by_id = {row["paper_id"]: row for row in phase1["papers"]}
    p2a_by_id = {row["paper_id"]: row for row in phase2a["papers"]}
    p2b_by_id = {row["paper_id"]: row for row in phase2b["papers"]}
    input_by_id = {row["paper_id"]: row for row in input_receipt["papers"]}
    stage4_completion = load_json(ROOT / "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json")
    check(stage4_completion.get("status") == "PASS" and
          stage4_completion.get("boundaries") == {
              "canonical_manuscripts_changed": False,
              "canonical_bibliographies_changed": False,
              "canonical_pdfs_changed": False,
              "science_trees_changed": False,
              "initial_dynamical_systems_changed": False,
              "formal_route_a_tuples_assigned": 0,
              "positive_arithmetic_a2": 0,
              "route_b_invocations": 0,
              "stage3_prime_started": False,
              "stage4_5_started": False,
              "stage5_started": False,
          }, "upstream Stage-4 frozen boundary")
    stage4_by_id = {row["paper"]: row for row in stage4_completion.get("papers", [])}
    check(set(stage4_by_id) == set(PAPERS) and all(
        stage4_by_id[paper_id].get("route", {}).get("crosswalk_sha256") ==
        spec["route"] and
        stage4_by_id[paper_id].get("route", {}).get("formal_route_a_tuple") ==
        "UNASSIGNED" and
        stage4_by_id[paper_id].get("route", {}).get("positive_arithmetic_a2") == 0 and
        stage4_by_id[paper_id].get("route", {}).get("route_b_invoked") is False
        for paper_id, spec in PAPERS.items()
    ), "upstream Stage-4 per-paper Route bindings")
    check(phase1["totals"] == {
        "papers": 5, "precommitted_items": 56, "validation_checks": 679,
        "schema_validation": "PASS", "phase1_validation": "PASS"
    }, "Phase-1 frozen totals")
    check(phase2a["totals"] == {
        "papers": 5, "verdict_rows": 56, "validation_checks": 380,
        "schema_validation": "PASS", "phase2a_validation": "PASS"
    }, "Phase-2A frozen totals")
    check(phase2b["totals"] == {
        "papers": 5, "response_rows": 56, "validation_checks": 482,
        "adjustments": 0, "verdict_changes": 0,
        "post_letter_observations": 0,
        "phase2b_integration_validation": "PASS"
    }, "Phase-2B frozen totals")

    schemas = {
        "manifest": load_json(CONTRACTS / "input_manifest.schema.json"),
        "precommitment": load_json(CONTRACTS / "precommitment.schema.json"),
        "verdict": load_json(CONTRACTS / "verdict_record.schema.json"),
        "trace": load_json(CONTRACTS / "traceability.schema.json"),
    }

    paper_results: dict[str, object] = {}
    integrity_by_paper: dict[str, dict[str, bool]] = {}
    expected_manifest_keys = {
        "original_manuscript", "revised_manuscript", "revision_roadmap",
        "author_adjudication", "revision_evidence_bundle",
        "editorial_decision_letter", "response_to_reviewers",
        "revision_patches", "apply_reports", "round1_findings",
        "round1_config_cards",
    }
    route_tokens = {
        "FORMAL_ROUTE_A_TUPLE=UNASSIGNED", "POSITIVE_ARITHMETIC_A2=0",
        "STAGE4_ROUTE_PROMOTION=NONE", "ROUTE_B_INVOKED=false",
        "CANONICAL_RESULTS_REFRESHED=false",
    }
    separator = r"[\s_.\-\u2013\u2014]*"
    successor_pattern = re.compile(
        rf"(?:round{separator}2(?!\d)|"
        rf"stage{separator}4{separator}(?:prime|['\u2019\u2032\u02b9])|"
        rf"stage{separator}4{separator}5(?!\d)|"
        rf"stage{separator}5(?!\d)|"
        rf"submission{separator}receipt)",
        re.IGNORECASE,
    )
    round10_context = re.compile(rf"round{separator}10(?!\d)", re.IGNORECASE)

    for paper_id, spec in PAPERS.items():
        paper = ROOT / "papers" / spec["slug"]
        notes = paper / "notes"
        manifest_file = notes / "stage3_prime_round1_input_manifest.json"
        pre_file = notes / "stage3_prime_round1_precommitment.json"
        verdict_file = notes / "stage3_prime_round1_verdict_record.json"
        integration_file = notes / "stage3_prime_round1_phase2b_integration.json"
        trace_file = notes / "stage3_prime_round1_traceability.json"
        checker_receipt_file = notes / "stage3_prime_round1_checker_receipt.json"

        manifest = load_json(manifest_file)
        precommitment = load_json(pre_file)
        verdict = load_json(verdict_file)
        integration = load_json(integration_file)
        trace = load_json(trace_file)
        checker_receipt = load_json(checker_receipt_file)

        for schema_name, value in (
            ("manifest", manifest), ("precommitment", precommitment),
            ("verdict", verdict), ("trace", trace),
        ):
            errors = sorted(
                Draft202012Validator(schemas[schema_name]).iter_errors(value),
                key=lambda error: list(error.path),
            )
            check(not errors, f"{paper_id}: {schema_name} schema")

        check(set(manifest["artifacts"]) == expected_manifest_keys,
              f"{paper_id}: exact eleven manifest surfaces")
        check(manifest["contract_version"] == "1.1",
              f"{paper_id}: manifest contract 1.1")
        check(manifest["cross_model_active"] is False,
              f"{paper_id}: cross-model false")
        check(digest(manifest_file) == input_by_id[paper_id]["manifest_sha256"],
              f"{paper_id}: input receipt manifest binding")
        check(digest(manifest_file) == p1_by_id[paper_id]["manifest_sha256"],
              f"{paper_id}: Phase-1 manifest raw binding")
        check(jcs_digest(manifest) == p1_by_id[paper_id]["manifest_jcs_sha256"],
              f"{paper_id}: Phase-1 manifest JCS binding")
        check(digest(pre_file) == p1_by_id[paper_id]["precommitment_sha256"],
              f"{paper_id}: precommitment raw freeze")
        check(jcs_digest(precommitment) == p1_by_id[paper_id]["precommitment_jcs_sha256"],
              f"{paper_id}: precommitment JCS freeze")
        check(digest(verdict_file) == p2a_by_id[paper_id]["verdict_record_sha256"],
              f"{paper_id}: verdict raw freeze")
        check(jcs_digest(verdict) == p2a_by_id[paper_id]["verdict_record_jcs_sha256"],
              f"{paper_id}: verdict JCS freeze")
        check(digest(integration_file) == p2b_by_id[paper_id]["integration_sha256"],
              f"{paper_id}: Phase-2B raw freeze")
        check(jcs_digest(integration) == p2b_by_id[paper_id]["integration_jcs_sha256"],
              f"{paper_id}: Phase-2B JCS freeze")
        check(digest(trace_file) == spec["trace"],
              f"{paper_id}: traceability frozen hash")

        # Every manifest-carried byte is still exact.
        manifest_files = 0
        for key, entry in manifest["artifacts"].items():
            if "items" in entry:
                for index, child in enumerate(entry["items"]):
                    path = manifest_path(paper, child)
                    exists = real_regular_file(path)
                    check(exists, f"{paper_id}: {key}[{index}] is a real regular file")
                    if exists:
                        check(digest(path) == child["sha256"],
                              f"{paper_id}: {key}[{index}] byte binding")
                    manifest_files += 1
            else:
                path = manifest_path(paper, entry)
                exists = real_regular_file(path)
                check(exists, f"{paper_id}: {key} is a real regular file")
                if exists:
                    check(digest(path) == entry["sha256"],
                          f"{paper_id}: {key} byte binding")
                manifest_files += 1

        # Phase-2B must remain persuasion-separated and adjustment-free.
        verdict_by_id = {row["item_id"]: row for row in verdict["items"]}
        check(not integration["adjustments"], f"{paper_id}: no Phase-2B adjustments")
        check(not integration["post_letter_observations"],
              f"{paper_id}: no post-letter observations")
        check(integration["verdict_record_hash"] == jcs_digest(verdict),
              f"{paper_id}: Phase-2B verdict binding")
        check(all(
            row["phase2a_verdict"] == verdict_by_id[row["item_id"]]["verdict"]
            and row["final_verdict"] == row["phase2a_verdict"]
            for row in integration["rows"]
        ), f"{paper_id}: no silent Phase-2B verdict change")

        recorded = Counter(row["verdict"] for row in verdict["items"])
        check((recorded["FULLY_ADDRESSED"], recorded["PARTIALLY_ADDRESSED"],
               recorded["NOT_ADDRESSED"]) == spec["recorded"],
              f"{paper_id}: recorded verdict count")

        if paper_id == "P33":
            expected_partial_ids = {
                "REV-P33-002", "REV-P33-003", "REV-P33-005",
                "REV-P33-006", "REV-P33-007", "REV-P33-008",
                "REV-P33-013",
            }
            partial_rows = {
                row["item_id"]: row for row in verdict["items"]
                if row["verdict"] == "PARTIALLY_ADDRESSED"
            }
            roadmap_by_id = {row["id"]: row for row in
                             load_json(notes / "stage3_revision_roadmap.json")["items"]}
            trace_by_id = {row["item_id"]: row for row in trace["rows"]}
            integration_by_id = {row["item_id"]: row for row in integration["rows"]}
            check(set(partial_rows) == expected_partial_ids,
                  "P33: exact seven PARTIAL item ids")
            check(all(partial_rows[item_id].get("evidence_anchor") and
                      partial_rows[item_id].get("residual_gap", {}).get("text")
                      for item_id in expected_partial_ids),
                  "P33: every PARTIAL has typed evidence and residual")
            expected_anchor_tokens = {
                "REV-P33-002": {"B0087", "B0123"},
                "REV-P33-003": {"B0107"},
                "REV-P33-005": {"B0061", "B0062", "B0072", "B0128"},
                "REV-P33-006": {"B0057", "B0059", "B0062", "B0128"},
                "REV-P33-007": {"B0051", "B0052", "B0108"},
                "REV-P33-008": {"B0045"},
                "REV-P33-013": {"B0081", "B0007", "B0010", "B0020", "B0100", "B0109"},
            }
            check(all(
                tokens <= set().union(*(
                    {token for token in tokens if token in anchor}
                    for anchor in partial_rows[item_id]["evidence_anchor"]
                ))
                for item_id, tokens in expected_anchor_tokens.items()
            ), "P33: exact frozen anchor tokens")
            expected_classes = {
                "REV-P33-002": ("must_fix", "must_fix"),
                "REV-P33-003": ("should_fix", "should_fix"),
                "REV-P33-005": ("must_fix", "must_fix"),
                "REV-P33-006": ("must_fix", "must_fix"),
                "REV-P33-007": ("must_fix", "must_fix"),
                "REV-P33-008": ("must_fix", "must_fix"),
                "REV-P33-013": ("must_fix", "must_fix"),
            }
            check(all(
                roadmap_by_id[item_id]["obligation_class"] == classes[0] and
                partial_rows[item_id]["residual_gap"]["residual_obligation_class"] == classes[1]
                for item_id, classes in expected_classes.items()
            ), "P33: exact obligation and residual classes")
            check(all(
                trace_by_id[item_id]["status"] == "PARTIALLY_ADDRESSED" and
                trace_by_id[item_id]["final_verdict"] == "PARTIALLY_ADDRESSED" and
                integration_by_id[item_id]["phase2a_verdict"] == "PARTIALLY_ADDRESSED" and
                integration_by_id[item_id]["final_verdict"] == "PARTIALLY_ADDRESSED"
                for item_id in expected_partial_ids
            ), "P33: verdict/integration/trace PARTIAL agreement")
            must_partial_ids = expected_partial_ids - {"REV-P33-003"}
            check(all(trace_by_id[item_id].get("cross_model_status") ==
                      "not_configured" for item_id in must_partial_ids) and
                  "cross_model_status" not in trace_by_id["REV-P33-003"],
                  "P33: must-only cross-model column semantics")
            check(len(must_partial_ids) == 6,
                  "P33: six must-fix PARTIAL rows deterministically trigger B4")

        # Replay the official checker from the exact manifest paths.
        artifacts = manifest["artifacts"]
        command = [
            sys.executable, str(CHECKER),
            "--manifest", str(manifest_file),
            "--precommitment", str(pre_file),
            "--verdict-record", str(verdict_file),
            "--traceability", str(trace_file),
            "--roadmap", str(manifest_path(paper, artifacts["revision_roadmap"])),
            "--author-adjudication", str(manifest_path(paper, artifacts["author_adjudication"])),
            "--revision-evidence-bundle", str(manifest_path(paper, artifacts["revision_evidence_bundle"])),
            "--revision-evidence-root", str(paper),
            "--letter", str(manifest_path(paper, artifacts["editorial_decision_letter"])),
        ]
        for entry in artifacts["apply_reports"]["items"]:
            command.extend(["--apply-report", str(manifest_path(paper, entry))])
        process = subprocess.run(command, cwd=paper, text=True, capture_output=True)
        checker_output = (process.stdout + process.stderr).strip()
        check(process.returncode == 0, f"{paper_id}: official checker exit 0")
        check("apply_chain_witness 'pass'" in checker_output,
              f"{paper_id}: official apply-chain pass")
        check("decision_state 'Major Revision'" in checker_output,
              f"{paper_id}: mechanical Major direction")

        # Outcome receipt, fail-closed status, and exact Judge Record fields.
        check(checker_receipt["mechanical_status"] == "PASS",
              f"{paper_id}: checker receipt mechanical PASS")
        check(checker_receipt["mechanical_decision_rule"] == spec["rule"],
              f"{paper_id}: checker receipt B-rule")
        check(checker_receipt["controlling_status"] == spec["status"],
              f"{paper_id}: controlling outcome")
        check(checker_receipt.get("abort_reason") == spec["abort"],
              f"{paper_id}: abort reason")
        check(checker_receipt["decision_emitted"] is (spec["abort"] is None),
              f"{paper_id}: decision emission boundary")
        check(tuple(checker_receipt["recorded_counts"][name] for name in
                    ("FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "NOT_ADDRESSED"))
              == spec["recorded"], f"{paper_id}: checker recorded counts")
        check(tuple(checker_receipt["audit_supported_counts"][name] for name in
                    ("FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "NOT_ADDRESSED"))
              == spec["audited"], f"{paper_id}: checker audited counts")
        judge = checker_receipt.get("judge_record", {})
        check(set(judge) >= {
            "verification_judge", "round1_panel_provenance",
            "cross_model_pass", "precommitment_hash",
            "prompt_rubric_surfaces", "reviewer_configuration",
            "routing_status", "apply_chain_witness", "evidence_seen",
            "judging_budget_note",
        }, f"{paper_id}: complete Judge Record")
        check(judge.get("cross_model_pass") == "not_configured",
              f"{paper_id}: cross-model status disclosed")
        check(judge.get("reviewer_configuration") == "round1_cards_reused" and
              judge.get("routing_status") == "card_mapped",
              f"{paper_id}: yardstick continuity and routing")
        check(judge.get("apply_chain_witness") == "pass",
              f"{paper_id}: Judge Record apply chain")
        check(judge.get("precommitment_hash") == jcs_digest(precommitment),
              f"{paper_id}: Judge Record precommitment binding")
        check(judge.get("round1_panel_provenance") ==
              load_json(notes / "stage3_review_package.json")["review_panel_provenance"],
              f"{paper_id}: exact Round-1 panel provenance carrier")
        rubric_surfaces = judge.get("prompt_rubric_surfaces", [])
        protocol_surfaces = [row for row in rubric_surfaces
                             if row.get("path") == str(PROTOCOL)]
        check(len(rubric_surfaces) == 7 and len(protocol_surfaces) == 1 and
              protocol_surfaces[0].get("sha256") == digest(PROTOCOL),
              f"{paper_id}: prompt/rubric surface recorded")
        expected_rubric_bindings = {
            str(path): digest(path) for path in (
                WORKFLOW,
                PROTOCOL,
                CONTRACTS / "input_manifest.schema.json",
                CONTRACTS / "precommitment.schema.json",
                CONTRACTS / "verdict_record.schema.json",
                CONTRACTS / "traceability.schema.json",
                CHECKER,
            )
        }
        actual_rubric_bindings = {
            row.get("path"): row.get("sha256") for row in rubric_surfaces
            if isinstance(row, dict)
        }
        check(actual_rubric_bindings == expected_rubric_bindings,
              f"{paper_id}: exact seven prompt/rubric bindings")
        check(protocol_surfaces and protocol_surfaces[0].get("sections") == [
            "Three-Gate Orchestration (#576 Spec B)",
            "Criterion Inheritance",
            "Decision Derivation (verdict -> decision)",
            "Judge Record (#539)",
        ], f"{paper_id}: exact re-review protocol sections")
        evidence_seen = judge.get("evidence_seen", {})
        phase1_seen = evidence_seen.get("phase1", {})
        phase2a_seen = evidence_seen.get("phase2a", {})
        phase2b_seen = evidence_seen.get("phase2b", {})
        check(set(phase1_seen.get("allowed", [])) == {
            "revision roadmap", "editorial decision surface",
            "Round-1 findings/configuration cards", "Phase-0 field analysis",
            "manifest verification binding",
        } and set(phase1_seen.get("withheld", [])) == {
            "manifest body", "original manuscript", "revised manuscript",
            "evidence bundle", "patch/apply reports", "Response to Reviewers",
            "author adjudication",
        }, f"{paper_id}: exact Phase-1 evidence fence")
        check(set(phase2a_seen.get("allowed", [])) == {
            "frozen precommitment", "manifest path/hash bindings",
            "roadmap/decision/findings/cards", "original manuscript",
            "revised manuscript", "patch/apply reports", "evidence bundle",
        } and set(phase2a_seen.get("withheld", [])) == {
            "Response to Reviewers", "author adjudication",
        }, f"{paper_id}: exact Phase-2A evidence fence")
        check(set(phase2b_seen.get("protocol_allowed", [])) == {
            "frozen Phase-2A verdict", "roadmap/manuscript evidence",
            "Response to Reviewers",
        } and set(phase2b_seen.get("withheld", [])) == {
            "author adjudication (checker-only)",
        }, f"{paper_id}: exact Phase-2B evidence fence")
        check("author adjudication (checker-only)" in
              phase2b_seen.get("withheld", []) and
              "Response to Reviewers" in
              phase2b_seen.get("protocol_allowed", []) and
              phase2b_seen.get("call_level_input_receipt", "").startswith("not retained"),
              f"{paper_id}: Phase-2B author-sidecar fencing")
        check(set(evidence_seen.get("untrusted_data_boundary", [])) == {
            "revised manuscript", "Response to Reviewers",
        } and "only to verify" in evidence_seen.get("checker", "") and
              "did not become a judging criterion" in
              evidence_seen.get("checker", "") and
              "withheld outcome reports" in
              evidence_seen.get("post_checker_semantic_audit", ""),
              f"{paper_id}: untrusted-data and post-checker fences")
        verification_judge = judge.get("verification_judge", {})
        check(verification_judge.get("service_model_id") ==
              "unavailable_to_workspace" and
              verification_judge.get("same_family_as_revision_workflow") is True and
              verification_judge.get("independent_error_process_claimed") is False,
              f"{paper_id}: honest verification-judge identity")
        check("Exact realized calls/tokens must not be inferred" in
              judge.get("judging_budget_note", ""),
              f"{paper_id}: honest degraded judging budget")

        panel_validation = subprocess.run(
            [sys.executable, str(PANEL_VALIDATOR), "validate-schema6",
             "--mode", "reviewer_full", "--artifact-root", str(paper),
             str(notes / "stage3_review_package.json")],
            cwd=paper, text=True, capture_output=True,
        )
        check(panel_validation.returncode == 0,
              f"{paper_id}: Round-1 panel provenance replay")
        check(checker_receipt.get("same_family_disclosure") ==
              "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).",
              f"{paper_id}: exact same-family disclosure")
        if spec["abort"]:
            check("Round 2" in checker_receipt.get("next_authorization", ""),
                  f"{paper_id}: next authorization is fresh Round 2")
        else:
            check("prepare a hash-bound Stage 4′" in
                  checker_receipt.get("next_authorization", "") and
                  "manuscript writes require a later exact approval" in
                  checker_receipt.get("next_authorization", ""),
                  f"{paper_id}: Stage-4-prime request-only boundary")

        abort_file = notes / "stage3_prime_round1_abort_record.json"
        if spec["abort"]:
            abort_exists = real_regular_file(abort_file)
            check(abort_exists, f"{paper_id}: abort record is a real regular file")
            if abort_exists:
                abort = load_json(abort_file)
                check(abort["status"] == "aborted" and
                      abort["abort_reason"] == spec["abort"],
                      f"{paper_id}: abort record controls")
                check(abort["no_retry_rule_applied"] is True and
                      abort["frozen_phase_artifacts_preserved"] is True,
                      f"{paper_id}: no-retry preservation")
                retry = abort.get("retry_handling", {})
                if spec["abort"] == "phase1_lint_failed":
                    check(retry.get("detection_timing") ==
                          "post_commit_after_phase2a_and_phase2b" and
                          retry.get("in_place_retry_eligible") is False and
                          "only before Phase 2A" in retry.get("protocol_rule", "") and
                          "fresh authorized Round 2" in retry.get("reason", ""),
                          f"{paper_id}: post-commit Phase-1 retry boundary")
                else:
                    check(retry.get("detection_timing") ==
                          "post_commit_phase2a_semantic_audit" and
                          retry.get("in_place_retry_eligible") is False and
                          "Phase 2A is no-retry" in retry.get("protocol_rule", "") and
                          "fresh authorized Round 2" in retry.get("reason", ""),
                          f"{paper_id}: Phase-2A no-retry boundary")
                check(abort["next_round_requirement"]["explicit_scholar_authorization"] is True,
                      f"{paper_id}: Round-2 authorization required")
        else:
            check(not abort_file.exists(), f"{paper_id}: no spurious abort record")

        # Canonical, scientific-tree, and Route invariants.
        canonical_ok = True
        for rel, expected in spec["canonical"].items():
            matches = real_regular_file(paper / rel) and digest(paper / rel) == expected
            canonical_ok = canonical_ok and matches
            check(matches,
                  f"{paper_id}: canonical frozen {rel}")
        route_file = notes / "stage4_route_crosswalk.md"
        route_text = read_text(route_file)
        route_hash_ok = digest(route_file) == spec["route"]
        route_tokens_ok = all(token in route_text for token in route_tokens)
        system_ok = spec["system"] in route_text
        check(route_hash_ok, f"{paper_id}: Route crosswalk hash")
        check(route_tokens_ok,
              f"{paper_id}: zero-credit Route tokens")
        check(system_ok, f"{paper_id}: exact frozen dynamical-system declaration")
        # Close the entire paper tree, not just familiar science directories.
        # The baseline half was independently reproduced from the frozen Stage-4
        # publication; the second half is an exact, thirteen-path Round-1 set.
        inventory = tree_inventory(paper)
        inventory_by_path = {row["path"]: row for row in inventory}
        baseline_inventory = [
            row for row in inventory if row["path"] not in ROUND1_PAPER_PATHS
        ]
        round1_inventory = [
            row for row in inventory if row["path"] in ROUND1_PAPER_PATHS
        ]
        inventory_spec = spec["inventory"]
        top_level_types = {
            row["path"]: row["type"] for row in inventory
            if "/" not in row["path"]
        }
        paper_root_ok = (
            paper.is_dir() and not paper.is_symlink() and
            (ROOT / "papers").is_dir() and not (ROOT / "papers").is_symlink()
        )
        no_links_or_special_nodes = all(
            row["type"] in {"file", "directory"} for row in inventory
        )
        exact_round1_paths = (
            set(inventory_by_path).intersection(ROUND1_PAPER_PATHS) ==
            ROUND1_PAPER_PATHS and
            len(round1_inventory) == inventory_spec["round1_entries"] and
            all(row["type"] == "file" for row in round1_inventory)
        )
        baseline_inventory_ok = (
            len(baseline_inventory) == inventory_spec["baseline_entries"] and
            jcs_digest(baseline_inventory) == inventory_spec["baseline_sha256"]
        )
        round1_inventory_ok = (
            exact_round1_paths and
            jcs_digest(round1_inventory) == inventory_spec["round1_sha256"]
        )
        inventory_ok = (
            paper_root_ok and no_links_or_special_nodes and
            top_level_types == EXPECTED_PAPER_TOP_LEVEL and
            len(inventory) == (
                inventory_spec["baseline_entries"] +
                inventory_spec["round1_entries"]
            ) and baseline_inventory_ok and round1_inventory_ok
        )
        check(paper_root_ok, f"{paper_id}: paper root is a real in-tree directory")
        check(no_links_or_special_nodes,
              f"{paper_id}: recursive inventory has no symlink/special node")
        check(top_level_types == EXPECTED_PAPER_TOP_LEVEL,
              f"{paper_id}: exact typed paper top-level inventory")
        check(baseline_inventory_ok,
              f"{paper_id}: exact recursive Stage-4 baseline tree")
        check(round1_inventory_ok,
              f"{paper_id}: exact recursive Round-1 publication tree")
        check(inventory_ok, f"{paper_id}: closed recursive paper inventory")

        science_roots = (
            paper / "code", paper / "experiments", paper / "results",
            paper / "paper/figures",
        )
        science_layout_ok = all(
            science_root.is_dir() and not science_root.is_symlink()
            for science_root in science_roots
        )
        science_unchanged = science_layout_ok and inventory_ok
        check(science_unchanged,
              f"{paper_id}: all science roots remain in exact frozen tree")

        # Current status surfaces must agree with the controlling receipt.
        pipeline = read_text(notes / "pipeline_state.md")
        readme = read_text(paper / "README.md")
        package_readme = read_text(paper / "paper/README.md")
        verification_report = read_text(
            notes / "stage3_prime_round1_verification_report.md"
        )
        check(spec["state"] in pipeline, f"{paper_id}: pipeline state synchronized")
        check("stage4_complete_awaiting_scholar_confirmation_before_stage3_prime" not in pipeline,
              f"{paper_id}: old pipeline state absent")
        check("Stage 3′ Round 1" in readme, f"{paper_id}: paper README synchronized")
        check("authoritative current" in package_readme,
              f"{paper_id}: canonical-package README marked historical")
        status_text = "\n".join((pipeline, readme, package_readme))
        status_artifact_paths = (
            notes / "stage3_prime_round1_verification_report.md",
            notes / "stage3_prime_round1_checker_receipt.json",
            notes / "stage3_prime_round1_abort_record.json",
        )
        check(all(digest(path) in status_text for path in status_artifact_paths),
              f"{paper_id}: status docs carry current terminal hashes")
        judge_labels = (
            "**Verification judge**", "**Round-1 panel provenance**",
            "**Blind cross-model pass**", "**Pre-committed criteria**",
            "**Prompt/rubric surfaces**", "**Reviewer configuration**",
            "**Routing**", "**Apply-report chain**",
            "**Evidence seen by the judge**", "**Judging budget**",
        )
        check(all(label in verification_report for label in judge_labels),
              f"{paper_id}: Markdown Judge Record ten lines")
        checklist = ""
        if "## Complete revision-response checklist" in verification_report:
            checklist = verification_report.split(
                "## Complete revision-response checklist", 1)[1].split("\n## ", 1)[0]
        check(checklist.count("\n| REV-") == len(verdict["items"]),
              f"{paper_id}: complete Markdown item checklist")
        check(checker_receipt["same_family_disclosure"] in verification_report,
              f"{paper_id}: Markdown same-family disclosure")
        if spec["abort"]:
            check(f"[RE-REVIEW-ABORT: {spec['abort']}]" in verification_report and
                  "no decision is emitted" in verification_report,
                  f"{paper_id}: Markdown abort controls")
        else:
            check(f"Major Revision ({spec['rule']})" in verification_report and
                  "manuscript write" in verification_report,
                  f"{paper_id}: Markdown decision/request boundary")

        # No unauthorized successor artifacts.
        forbidden = []
        for path in paper.rglob("*"):
            relative = str(path.relative_to(paper))
            if successor_pattern.search(relative):
                forbidden.append(relative)
        check(not forbidden, f"{paper_id}: no successor-stage artifact")

        integrity_by_paper[paper_id] = {
            "canonical": canonical_ok and inventory_ok,
            "science": science_unchanged,
            "route": route_hash_ok and route_tokens_ok and system_ok and inventory_ok,
            "successor": not forbidden and inventory_ok,
        }

        paper_results[paper_id] = {
            "manifest_files": manifest_files,
            "roadmap_items": len(verdict["items"]),
            "recorded_counts": list(spec["recorded"]),
            "audit_supported_counts": list(spec["audited"]),
            "controlling_status": spec["status"],
            "abort_reason": spec["abort"],
            "mechanical_rule": spec["rule"],
            "official_checker": "PASS",
            "canonical_mutations": 0 if canonical_ok and inventory_ok else None,
            "science_artifacts": 0 if science_unchanged else None,
            "route_advancement": (
                "NONE" if route_hash_ok and route_tokens_ok and system_ok and
                inventory_ok else None
            ),
        }

    # Persisted semantic audits and consolidation are required before terminalization.
    semantic_paths = [
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json",
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json",
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json",
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json",
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json",
    ]
    semantic_data: dict[str, object] = {}
    for path in semantic_paths:
        exists = real_regular_file(path)
        check(exists, f"semantic evidence is a real regular file: {path.name}")
        if exists:
            check(digest(path) == SEMANTIC_HASHES[path.name],
                  f"semantic evidence frozen hash: {path.name}")
            try:
                semantic_data[path.name] = load_json(path)
                check(True, f"semantic evidence JSON parses: {path.name}")
            except Exception:
                check(False, f"semantic evidence JSON parses: {path.name}")

    # The primary passes provide full coverage, while the fresh-context
    # tie-break controls every disputed P29--P32 row and all P33 verdicts.
    # A narrower, manuscript/verdict/outcome-blind audit controls only P33's
    # Phase-1 criterion-inheritance gate.  These same-family roles are not
    # represented as independent error processes.
    primary_29_30 = semantic_data.get(
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json", {})
    primary_31_32 = semantic_data.get(
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json", {})
    tie_break = semantic_data.get(
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json", {})
    p33_confirmation = semantic_data.get(
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json", {})
    consolidation = semantic_data.get(
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json", {})

    check(primary_29_30.get("auditor_provenance", {}).get("fresh_context") is True and
          primary_29_30.get("auditor_provenance", {}).get("role_separated") is True and
          primary_29_30.get("auditor_provenance", {}).get("model_family_distinct") is False,
          "P29-P30 primary audit honest same-family fresh-context provenance")
    check(primary_31_32.get("auditor_provenance", {}).get("fresh_context") is True and
          primary_31_32.get("auditor_provenance", {}).get("role_separated") is True and
          primary_31_32.get("auditor_provenance", {}).get("model_family_distinct") is False and
          primary_31_32.get("auditor_provenance", {}).get(
              "independent_error_process_claimed") is False,
          "P31-P32 primary audit honest same-family fresh-context provenance")
    primary_29_30_inputs = list(declared_hash_entries(
        primary_29_30.get("input_raw_sha256", {})))
    primary_31_32_inputs = list(declared_hash_entries({
        "governing": primary_31_32.get("governing_sources_raw_sha256", {}),
        "paper_inputs": primary_31_32.get("input_raw_sha256", {}),
    }))
    check(len(primary_29_30_inputs) == 21 and all(
        real_regular_file(declared_path(path)) and digest(declared_path(path)) == sha
        for path, sha in primary_29_30_inputs
    ), "P29-P30 primary audit 21/21 input hashes replay")
    check(len(primary_31_32_inputs) == 21 and all(
        real_regular_file(declared_path(path)) and digest(declared_path(path)) == sha
        for path, sha in primary_31_32_inputs
    ), "P31-P32 primary audit 21/21 input hashes replay")
    check(tie_break.get("fresh_context") is True and
          tie_break.get("role_separation", {}).get("semantic_role_separated") is True and
          tie_break.get("role_separation", {}).get("family_separated") is False and
          tie_break.get("role_separation", {}).get("independent_error_claimed") is False,
          "tie-break honest same-family fresh-context provenance")
    check(tie_break.get("scope") == {
        "disputed_rows_papers_29_to_32": 11,
        "paper33_registered_rows": 13,
        "total_rows_semantically_audited": 24,
        "scientific_content_only": True,
        "manuscript_or_protocol_mutation": False,
    }, "tie-break exact semantic scope")
    tie_allowed = tie_break.get("allowed_inputs", [])
    check(len(tie_allowed) == 60 and all(
        isinstance(row, dict) and isinstance(row.get("path"), str) and
        isinstance(row.get("sha256"), str) and real_regular_file(declared_path(row["path"])) and
        digest(declared_path(row["path"])) == row["sha256"]
        for row in tie_allowed
    ) and len({row["path"] for row in tie_allowed}) == 60,
        "tie-break 60/60 unique allowed-input hashes replay")

    expected_disputed = {
        (29, "REV-EIC-1"): (
            "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "no_material_extension_or_weakening", False),
        (30, "REV-EIC-W4"): (
            "PARTIALLY_ADDRESSED", "FULLY_ADDRESSED",
            "material_extension", True),
        (30, "REV-R2-W1"): (
            "FULLY_ADDRESSED", "FULLY_ADDRESSED",
            "no_material_extension_or_weakening", False),
        (30, "REV-R3-W1-DA-N1"): (
            "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "material_extension", False),
        (31, "REV-P31-005"): (
            "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "material_extension", False),
        (31, "REV-P31-009"): (
            "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "material_extension_and_weakening", True),
        (31, "REV-P31-010"): (
            "FULLY_ADDRESSED", "FULLY_ADDRESSED",
            "no_material_extension_or_weakening", False),
        (32, "REV-P32-R1-W1"): (
            "FULLY_ADDRESSED", "FULLY_ADDRESSED",
            "no_material_extension_or_weakening", False),
        (32, "REV-P32-R1-W2"): (
            "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "no_material_extension_or_weakening", False),
        (32, "REV-P32-R3-W1"): (
            "PARTIALLY_ADDRESSED", "FULLY_ADDRESSED",
            "material_extension", True),
        (32, "REV-P32-DA-M1"): (
            "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
            "material_extension", False),
    }
    actual_disputed = {
        (row["paper_id"], row["item_id"]): (
            row["recorded_verdict"], row["audited_verdict"],
            row["phase1_criterion_inheritance"]["status"],
            row["phase1_criterion_inheritance"]["decision_relevant"],
        )
        for row in tie_break.get("disputed_rows", [])
    }
    check(actual_disputed == expected_disputed,
          "tie-break exact disputed-row verdict and inheritance map")

    primary_rows: dict[tuple[int, str], dict[str, object]] = {}
    primary_row_keys: list[tuple[int, str]] = []
    for paper_entry in primary_29_30.get("papers", []):
        paper_number = paper_entry.get("paper_id")
        for row in paper_entry.get("row_audits", []):
            key = (paper_number, row["item_id"])
            primary_row_keys.append(key)
            primary_rows[key] = {
                "recorded": row["phase2a"]["recorded_verdict"],
                "audited": row["phase2a"]["audit_supported_verdict"],
                "criterion": row["immutable_criterion"]["text"],
                "obligation": row["obligation_class"],
            }
    for paper_label, paper_entry in primary_31_32.get("papers", {}).items():
        paper_number = int(paper_label.removeprefix("P"))
        for row in paper_entry.get("row_audits", []):
            key = (paper_number, row["item_id"])
            primary_row_keys.append(key)
            primary_rows[key] = {
                "recorded": row["recorded_verdict"],
                "audited": row["audit_supported_verdict"],
                "criterion": row["immutable_criterion"],
                "obligation": row["obligation_class"],
            }

    frozen_rows: dict[tuple[int, str], dict[str, object]] = {}
    for paper_label, spec in PAPERS.items():
        paper_number = int(paper_label.removeprefix("P"))
        notes = ROOT / "papers" / spec["slug"] / "notes"
        verdict_rows = {
            row["item_id"]: row for row in
            load_json(notes / "stage3_prime_round1_verdict_record.json")["items"]
        }
        roadmap_rows = {
            row["id"]: row for row in
            load_json(notes / "stage3_revision_roadmap.json")["items"]
        }
        roadmap_order = {item_id: index for index, item_id in enumerate(
            roadmap_rows, start=1
        )}
        for item_id, verdict_row in verdict_rows.items():
            residual = verdict_row.get("residual_gap")
            frozen_rows[(paper_number, item_id)] = {
                "recorded": verdict_row["verdict"],
                "criterion": roadmap_rows[item_id]["verification_criteria"],
                "obligation": roadmap_rows[item_id]["obligation_class"],
                "severity": roadmap_rows[item_id]["severity"],
                "roadmap_order": roadmap_order[item_id],
                "residual_class": (
                    residual.get("residual_obligation_class")
                    if isinstance(residual, dict) else None
                ),
            }
    expected_primary_keys = {
        key for key in frozen_rows if key[0] in {29, 30, 31, 32}
    }
    check(len(primary_row_keys) == 43 and
          len(set(primary_row_keys)) == len(primary_row_keys) and
          set(primary_rows) == expected_primary_keys and len(primary_rows) == 43,
          "primary semantic audits exact P29-P32 item coverage")
    check(all(
        primary_rows[key]["recorded"] == frozen_rows[key]["recorded"] and
        primary_rows[key]["criterion"] == frozen_rows[key]["criterion"] and
        primary_rows[key]["obligation"] == frozen_rows[key]["obligation"]
        for key in expected_primary_keys
    ), "primary semantic rows bind frozen verdict/criterion/obligation")

    disputed_rows_raw = tie_break.get("disputed_rows", [])
    check(len(disputed_rows_raw) == len(expected_disputed) and
          len(actual_disputed) == len(disputed_rows_raw),
          "tie-break disputed rows are unique and complete")
    check(all(
        (row.get("paper_id"), row.get("item_id")) in frozen_rows and
        row.get("recorded_verdict") == frozen_rows[
            (row.get("paper_id"), row.get("item_id"))]["recorded"] and
        row.get("immutable_roadmap_criterion") == frozen_rows[
            (row.get("paper_id"), row.get("item_id"))]["criterion"] and
        row.get("obligation_class") == frozen_rows[
            (row.get("paper_id"), row.get("item_id"))]["obligation"] and
        row.get("severity") == frozen_rows[
            (row.get("paper_id"), row.get("item_id"))]["severity"] and
        row.get("verdict_changed") is
            (row.get("recorded_verdict") != row.get("audited_verdict"))
        for row in disputed_rows_raw
    ), "tie-break disputed rows bind frozen criterion/obligation/verdict")

    consolidated_disputed_raw = consolidation.get("disputed_rows", [])
    consolidated_disputed = {
        (int(row["paper_id"].removeprefix("P")), row["item_id"]): row
        for row in consolidated_disputed_raw
    }
    check(len(consolidated_disputed_raw) == len(expected_disputed) and
          len(consolidated_disputed) == len(consolidated_disputed_raw) and
          set(consolidated_disputed) == set(expected_disputed),
          "semantic consolidation exact disputed-row set")
    check(all(
        row.get("recorded_verdict") == frozen_rows[key]["recorded"] and
        row.get("primary_audit_supported_verdict") == primary_rows[key]["audited"] and
        row.get("tie_break_audit_supported_verdict") == actual_disputed[key][1] and
        row.get("primary_tie_agree") is
            (primary_rows[key]["audited"] == actual_disputed[key][1]) and
        row.get("consolidated_audit_supported_verdict") == actual_disputed[key][1] and
        row.get("criterion_inheritance_finding") is
            (actual_disputed[key][2] != "no_material_extension_or_weakening")
        for key, row in consolidated_disputed.items()
    ), "primary-to-tie-break-to-consolidation row chain")

    reconstructed: dict[str, Counter[str]] = {}
    for paper_label in PAPERS:
        paper_number = int(paper_label.removeprefix("P"))
        rows = {}
        if paper_number < 33:
            rows = {
                item_id: data["audited"]
                for (number, item_id), data in primary_rows.items()
                if number == paper_number
            }
            for (number, item_id), values in actual_disputed.items():
                if number == paper_number:
                    rows[item_id] = values[1]
        else:
            rows = {
                row["item_id"]: row["audited_verdict"]
                for row in tie_break.get("paper33_all_rows", [])
            }
        reconstructed[paper_label] = Counter(rows.values())
    check(all(
        (
            reconstructed[paper_label]["FULLY_ADDRESSED"],
            reconstructed[paper_label]["PARTIALLY_ADDRESSED"],
            reconstructed[paper_label]["NOT_ADDRESSED"],
        ) == spec["audited"]
        for paper_label, spec in PAPERS.items()
    ), "semantic arbitration independently reconstructs all five counts")

    p33_rows = tie_break.get("paper33_all_rows", [])
    expected_p33_ids = {
        item_id for paper_number, item_id in frozen_rows if paper_number == 33
    }
    p33_by_id = {
        row.get("item_id"): row for row in p33_rows if isinstance(row, dict)
    }
    p33_audited = Counter(row.get("audited_verdict") for row in p33_rows)
    check(len(p33_rows) == 13 and
          len(p33_by_id) == len(p33_rows) and
          set(p33_by_id) == expected_p33_ids ==
          {f"REV-P33-{index:03d}" for index in range(1, 14)} and
          all(row.get("recorded_verdict") == row.get("audited_verdict")
              for row in p33_rows) and
          (p33_audited["FULLY_ADDRESSED"],
           p33_audited["PARTIALLY_ADDRESSED"],
           p33_audited["NOT_ADDRESSED"]) == (6, 7, 0),
          "tie-break complete P33 verdict coverage and counts")
    check(all(
        (33, row.get("item_id")) in frozen_rows and
        row.get("paper_id") == 33 and
        row.get("recorded_verdict") == frozen_rows[
            (33, row.get("item_id"))]["recorded"] and
        row.get("immutable_roadmap_criterion") == frozen_rows[
            (33, row.get("item_id"))]["criterion"] and
        row.get("obligation_class") == frozen_rows[
            (33, row.get("item_id"))]["obligation"] and
        row.get("severity") == frozen_rows[
            (33, row.get("item_id"))]["severity"] and
        row.get("verdict_changed") is False and
        (
            row.get("residual_gap", {}).get("residual_obligation_class")
            if isinstance(row.get("residual_gap"), dict) else None
        ) == frozen_rows[(33, row.get("item_id"))]["residual_class"]
        for row in p33_rows
    ), "tie-break P33 rows bind frozen criterion/obligation/verdict/residual")
    p33_summary = tie_break.get("paper33_summary", {})
    check(p33_summary.get("changed_rows") == [] and
          p33_summary.get("must_fix", {}).get(
              "partial_with_must_fix_residual") == 6 and
          p33_summary.get("should_fix", {}).get("addressed_rate_percent") == 100 and
          p33_summary.get("controlling_B_rule") == "B4" and
          p33_summary.get("decision") == "Major Revision",
          "tie-break P33 mechanical B4 direction")

    confirm_fresh = p33_confirmation.get("fresh_context", {})
    confirm_same_family = p33_confirmation.get("same_family_restriction", {})
    check(confirm_fresh.get("confirmed") is True and
          confirm_fresh.get("manuscript_blind") is True and
          confirm_fresh.get("later_verdict_and_outcome_blind") is True and
          confirm_fresh.get("forbidden_project_surfaces_accessed") is False and
          confirm_same_family.get("cross_model_or_cross_family_pass") is False and
          confirm_same_family.get("independence_claim") == "none",
          "P33 criterion confirmation blind same-family boundary")
    confirm_inputs = p33_confirmation.get("input_inventory", {}).get("allowed", [])
    check(len(confirm_inputs) == 7 and all(
        isinstance(row, dict) and isinstance(row.get("path"), str) and
        isinstance(row.get("sha256"), str) and real_regular_file(declared_path(row["path"])) and
        digest(declared_path(row["path"])) == row["sha256"] and
        row.get("access") == "read_full"
        for row in confirm_inputs
    ) and len({row["path"] for row in confirm_inputs}) == 7,
        "P33 criterion confirmation 7/7 unique input hashes replay")
    expected_p33_drift = {
        "REV-P33-001", "REV-P33-003", "REV-P33-004",
        "REV-P33-006", "REV-P33-007", "REV-P33-009", "REV-P33-012",
    }
    finding_summary = p33_confirmation.get("finding_summary", {})
    check(set(finding_summary.get("drift_affected_item_ids", [])) ==
          expected_p33_drift and
          finding_summary.get("rows_audited") == 13 and
          finding_summary.get("faithful_rows") == 6 and
          finding_summary.get("drift_affected_rows") == 7 and
          finding_summary.get("total_findings") == 8 and
          finding_summary.get("new_standards_formally_declared") == [] and
          finding_summary.get("all_detected_drifts_undeclared") is True,
          "P33 criterion confirmation exact drift set")
    confirm_comparisons = p33_confirmation.get("item_comparisons", [])
    confirm_by_id = {
        row.get("item_id"): row for row in confirm_comparisons
        if isinstance(row, dict)
    }
    check(len(confirm_comparisons) == 13 and
          len(confirm_by_id) == len(confirm_comparisons) and
          set(confirm_by_id) == expected_p33_ids and
          {row.get("item_id") for row in confirm_comparisons
           if not row.get("faithful")} == expected_p33_drift and
          all(row.get("formally_declared_in_new_standards") is False
              for row in confirm_comparisons),
          "P33 criterion confirmation row-level inheritance result")
    check(all(
        (33, row.get("item_id")) in frozen_rows and
        row.get("row") == frozen_rows[
            (33, row.get("item_id"))]["roadmap_order"] and
        row.get("roadmap_exact_criterion") == frozen_rows[
            (33, row.get("item_id"))]["criterion"] and
        row.get("obligation_class") == frozen_rows[
            (33, row.get("item_id"))]["obligation"] and
        row.get("phase1_inherited_criterion_exact_copy") is True and
        row.get("faithful") is (row.get("item_id") not in expected_p33_drift) and
        row.get("phase1_semantic_lint") == (
            "pass" if row.get("item_id") not in expected_p33_drift else "fail"
        )
        for row in confirm_comparisons
    ), "P33 criterion confirmation exact frozen row binding")
    gate = p33_confirmation.get("pipeline_gate_implication", {})
    check(gate.get("phase1_gate") == "FAIL" and
          gate.get("constitutes_phase1_lint_failure") is True and
          gate.get("may_phase2a_consume_this_artifact_as_is") is False and
          gate.get("later_verdict_can_cure_failure") is False and
          gate.get("audit_retry_performed") is False and
          gate.get("repair_or_rewrite_performed") is False,
          "P33 criterion confirmation fail-closed gate")

    expected_source_bindings = [
        {"path": name, "sha256": SEMANTIC_HASHES[name]}
        for name in (
            "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json",
            "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json",
            "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json",
            "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json",
        )
    ]
    check(consolidation.get("source_artifacts") == expected_source_bindings,
          "semantic consolidation exact four source bindings")
    check(consolidation.get("auditor_provenance") == {
        "fresh_context_role_separation": True,
        "human_distinct": False,
        "model_family_distinct": False,
        "provider_distinct": False,
        "independent_error_process_claimed": False,
        "limitation": "All semantic passes used role-separated fresh contexts in the same model family/provider. Correlated-error risk remains.",
    }, "semantic consolidation honest same-family provenance")
    expected_paper_semantics = {
        paper_id: {
            "recorded_counts": [
                Counter(
                    row["recorded"] for (number, _), row in frozen_rows.items()
                    if number == int(paper_id.removeprefix("P"))
                )[verdict]
                for verdict in (
                    "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "NOT_ADDRESSED"
                )
            ],
            "consolidated_audit_supported_counts": [
                reconstructed[paper_id][verdict]
                for verdict in (
                    "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "NOT_ADDRESSED"
                )
            ],
            "controlling_status": "ABORTED",
            "abort_reason": spec["abort"],
            "mechanical_rule": spec["rule"],
        }
        for paper_id, spec in PAPERS.items()
    }
    consolidated_papers_raw = consolidation.get("papers", [])
    consolidated_papers = {row.get("paper_id"): row
                           for row in consolidated_papers_raw}
    check(len(consolidated_papers_raw) == len(PAPERS) and
          len(consolidated_papers) == len(consolidated_papers_raw) and
          set(consolidated_papers) == set(PAPERS),
          "semantic consolidation exact paper set")
    check(all(
        all(consolidated_papers.get(paper_id, {}).get(key) == value
            for key, value in expected.items())
        for paper_id, expected in expected_paper_semantics.items()
    ), "semantic consolidation per-paper counts and controlling gates")
    expected_drift_by_paper = {
        "P29": set(),
        "P30": {"REV-EIC-W4", "REV-R3-W1-DA-N1"},
        "P31": {"REV-P31-005", "REV-P31-009"},
        "P32": {"REV-P32-R3-W1", "REV-P32-DA-M1"},
        "P33": expected_p33_drift,
    }
    expected_overrides_by_paper = {
        "P29": {"REV-EIC-1"},
        "P30": {"REV-EIC-W4", "REV-R3-W1-DA-N1"},
        "P31": {"REV-P31-009"},
        "P32": {"REV-P32-R1-W2", "REV-P32-R3-W1"},
        "P33": set(),
    }
    derived_drift_by_paper = {
        paper_id: {
            item_id for (number, item_id), values in actual_disputed.items()
            if number == int(paper_id.removeprefix("P")) and
            values[2] != "no_material_extension_or_weakening"
        }
        for paper_id in PAPERS if paper_id != "P33"
    }
    derived_drift_by_paper["P33"] = {
        row.get("item_id") for row in confirm_comparisons
        if row.get("faithful") is False
    }
    derived_overrides_by_paper = {
        paper_id: {
            item_id for (number, item_id), row in consolidated_disputed.items()
            if number == int(paper_id.removeprefix("P")) and
            row.get("consolidated_audit_supported_verdict") !=
                frozen_rows[(number, item_id)]["recorded"]
        }
        for paper_id in PAPERS if paper_id != "P33"
    }
    derived_overrides_by_paper["P33"] = {
        row.get("item_id") for row in p33_rows
        if row.get("audited_verdict") !=
        frozen_rows[(33, row.get("item_id"))]["recorded"]
    }
    check(derived_drift_by_paper == expected_drift_by_paper,
          "semantic source rows derive exact criterion-drift map")
    check(derived_overrides_by_paper == expected_overrides_by_paper,
          "semantic source rows derive exact verdict-override map")
    expected_override_kinds = {
        "P29": {"REV-EIC-1": "phase2a_overcredit"},
        "P30": {
            "REV-EIC-W4": "phase2a_undercredit_from_criterion_extension",
            "REV-R3-W1-DA-N1": "phase2a_overcredit",
        },
        "P31": {
            "REV-P31-009": "phase2a_overcredit_from_criterion_weakening",
        },
        "P32": {
            "REV-P32-R1-W2": "phase2a_overcredit",
            "REV-P32-R3-W1": "phase2a_undercredit_from_criterion_extension",
        },
        "P33": {},
    }
    expected_drift_kinds = {
        "P29": {},
        "P30": {
            "REV-EIC-W4": "unrecorded_semantic_extension_decision_relevant",
            "REV-R3-W1-DA-N1": "unrecorded_semantic_extension",
        },
        "P31": {
            "REV-P31-005": "unrecorded_semantic_extension",
            "REV-P31-009":
                "unrecorded_semantic_extension_and_weakening_decision_relevant",
        },
        "P32": {
            "REV-P32-R3-W1": "unrecorded_semantic_extension_decision_relevant",
            "REV-P32-DA-M1": "unrecorded_semantic_extension",
        },
        "P33": {
            "REV-P33-001": "unrecorded_semantic_extension",
            "REV-P33-003": "unrecorded_semantic_weakening",
            "REV-P33-004": "unrecorded_semantic_extension_and_weakening",
            "REV-P33-006": "unrecorded_semantic_extension",
            "REV-P33-007": "unrecorded_semantic_extension",
            "REV-P33-009": "unrecorded_semantic_extension",
            "REV-P33-012": "unrecorded_semantic_extension",
        },
    }
    check(all(
        len(consolidated_papers[paper_id].get(
            "criterion_inheritance_findings", [])) ==
            len(expected_drift_by_paper[paper_id]) and
        {row.get("item_id") for row in consolidated_papers[paper_id].get(
            "criterion_inheritance_findings", [])} == expected_drift_by_paper[paper_id]
        for paper_id in PAPERS
    ), "semantic consolidation exact criterion-drift map")
    check(all(
        len(consolidated_papers[paper_id].get("verdict_discrepancies", [])) ==
            len(expected_overrides_by_paper[paper_id]) and
        {row.get("item_id") for row in consolidated_papers[paper_id].get(
            "verdict_discrepancies", [])} == expected_overrides_by_paper[paper_id]
        for paper_id in PAPERS
    ), "semantic consolidation exact verdict-override map")
    check(all(
        {row.get("item_id"): row.get("kind") for row in
         consolidated_papers[paper_id].get("verdict_discrepancies", [])} ==
        expected_override_kinds[paper_id] and
        all(
            isinstance(row.get("reason"), str) and row["reason"].strip() and
            (int(paper_id.removeprefix("P")), row.get("item_id")) in
                consolidated_disputed and
            row.get("recorded") == frozen_rows[
                (int(paper_id.removeprefix("P")), row.get("item_id"))
            ]["recorded"] and
            row.get("audit_supported") == consolidated_disputed[
                (int(paper_id.removeprefix("P")), row.get("item_id"))
            ].get("consolidated_audit_supported_verdict")
            for row in consolidated_papers[paper_id].get(
                "verdict_discrepancies", [])
        )
        for paper_id in PAPERS
    ), "semantic consolidation row-bound verdict-discrepancy classes")
    check(all(
        {row.get("item_id"): row.get("kind") for row in
         consolidated_papers[paper_id].get("criterion_inheritance_findings", [])} ==
        expected_drift_kinds[paper_id] and
        all(isinstance(row.get("reason"), str) and row["reason"].strip()
            for row in consolidated_papers[paper_id].get(
                "criterion_inheritance_findings", []))
        for paper_id in PAPERS
    ), "semantic consolidation exact criterion-drift classes")
    method = consolidation.get("method", {})
    check(method.get("criterion") ==
          "Each verdict is judged against the immutable exact roadmap criterion; Phase-1 operationalization may not add or weaken an acceptance condition." and
          method.get("arbitration") ==
          "The fresh-context tie-break controls the listed disputed rows; full-coverage primary audits control all other P29-P32 rows; the tie-break supplies full P33 verdict coverage; a separate roadmap-versus-precommitment-only P33 audit confirms the Phase-1 inheritance result." and
          method.get("earliest_gate_rule") ==
          "Any unrecorded Phase-1 criterion extension or weakening aborts at phase1_lint_failed even when the mechanical decision direction is unchanged; frozen artifacts are not rewritten in place.",
          "semantic consolidation exact arbitration method")
    check(consolidation.get("aggregate") == {
        "recorded_counts": [27, 27, 2],
        "consolidated_audit_supported_counts": [25, 29, 2],
        "verdict_discrepancies": 6,
        "false_full_rows": 4,
        "false_partial_rows": 2,
        "criterion_inheritance_affected_rows": 13,
        "complete_papers": 0,
        "aborted_papers": 5,
    }, "semantic consolidation exact aggregate")

    outcome_file = ROOT / "BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json"
    outcome = load_json(outcome_file)
    check(digest(outcome_file) == TERMINAL_HASHES.get("outcome_receipt"),
          "batch outcome receipt frozen hash")
    check(outcome["status"] == "ALL_FIVE_ABORTED_FAIL_CLOSED",
          "batch all-five fail-closed outcome")
    check(outcome["totals"]["complete"] == 0 and
          outcome["totals"]["aborted"] == 5,
          "batch zero-complete five-aborted")
    check(outcome["totals"]["recorded"] == {
        "FULLY_ADDRESSED": 27, "PARTIALLY_ADDRESSED": 27,
        "NOT_ADDRESSED": 2, "MADE_WORSE": 0, "CANNOT_VERIFY": 0,
    }, "batch recorded counts")
    check(outcome["totals"]["audit_supported"] == {
        "FULLY_ADDRESSED": 25, "PARTIALLY_ADDRESSED": 29,
        "NOT_ADDRESSED": 2, "MADE_WORSE": 0, "CANNOT_VERIFY": 0,
    }, "batch audited counts")
    check(outcome["totals"]["verdict_discrepancies"] == 6 and
          outcome["totals"]["false_full_rows"] == 4 and
          outcome["totals"]["false_partial_rows"] == 2 and
          outcome["totals"]["criterion_inheritance_affected_rows"] == 13,
          "batch semantic discrepancy/drift totals")
    check(outcome["mandatory_checkpoint"]["authorization_granted"] is False,
          "successor authorization not granted")
    check(outcome["mandatory_checkpoint"]["round2_authorized"] is False and
          outcome["mandatory_checkpoint"]["stage4_prime_authorization_request_preparation_authorized"] is False,
          "Round-2 and Stage-4-prime preparation not authorized")
    check(outcome["mandatory_checkpoint"]["p29_revision_authorized"] is False,
          "P29 manuscript revision not authorized")
    check(outcome["mandatory_checkpoint"]["p33_revision_authorized"] is False,
          "P33 manuscript revision not authorized")
    check(outcome["route_boundary"] == {
        "formal_route_a_tuples_assigned": 0,
        "positive_arithmetic_a2_results": 0,
        "route_b_invocations": 0,
        "initial_dynamical_systems_changed": 0,
        "canonical_manuscripts_changed": 0,
        "canonical_bibliographies_changed": 0,
        "canonical_pdfs_changed": 0,
        "scientific_result_artifacts_changed": 0,
    }, "batch Route/science boundary")
    check(outcome.get("semantic_audit", {}).get("sources") ==
          expected_source_bindings and
          outcome.get("semantic_audit", {}).get("consolidation") == {
              "path": "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json",
              "sha256": SEMANTIC_HASHES[
                  "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json"],
          } and outcome.get("semantic_audit", {}).get(
              "independent_error_process_claimed") is False and
          outcome.get("semantic_audit", {}).get("cross_model") is False,
          "batch outcome exact semantic authority chain")

    # Terminal bindings close every generated outcome artifact except this audit itself.
    terminal = outcome.get("terminal_artifacts", {})
    check(set(terminal) == {
        "semantic_audits", "semantic_consolidation", "checker_receipts",
        "verification_reports", "abort_records", "batch_report",
        "mandatory_checkpoint",
    }, "terminal binding exact key set")
    check(len(terminal.get("semantic_audits", [])) == 4,
          "terminal semantic-audit binding count")
    check(len(terminal.get("checker_receipts", [])) == 5,
          "terminal checker-receipt binding count")
    check(len(terminal.get("verification_reports", [])) == 5,
          "terminal verification-report binding count")
    check(len(terminal.get("abort_records", [])) == 5,
          "terminal abort-record binding count")
    for label, binding in terminal.items():
        if isinstance(binding, dict) and "path" in binding:
            check(valid_terminal_binding(binding),
                  f"terminal binding shape/scope: {label}")
            path = ROOT / binding["path"]
            exists = real_regular_file(path)
            check(exists, f"terminal binding is a real regular file: {label}")
            if exists:
                check(digest(path) == binding["sha256"],
                      f"terminal binding hash: {label}")
        elif isinstance(binding, list):
            for index, child in enumerate(binding):
                check(valid_terminal_binding(child),
                      f"terminal list shape/scope: {label}[{index}]")
                path = ROOT / child["path"]
                exists = real_regular_file(path)
                check(exists,
                      f"terminal list is a real regular file: {label}[{index}]")
                if exists:
                    check(digest(path) == child["sha256"],
                          f"terminal list hash: {label}[{index}]")
        else:
            check(False, f"terminal binding shape: {label}")

    expected_checker_paths = {
        f"papers/{spec['slug']}/notes/stage3_prime_round1_checker_receipt.json"
        for spec in PAPERS.values()
    }
    expected_report_paths = {
        f"papers/{spec['slug']}/notes/stage3_prime_round1_verification_report.md"
        for spec in PAPERS.values()
    }
    expected_abort_paths = {
        f"papers/{spec['slug']}/notes/stage3_prime_round1_abort_record.json"
        for spec in PAPERS.values()
    }
    expected_semantic_paths = {
        name for name in SEMANTIC_HASHES if name !=
        "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json"
    }
    check({row.get("path") for row in terminal.get("semantic_audits", [])} ==
          expected_semantic_paths and all(
              row.get("sha256") == SEMANTIC_HASHES[row.get("path")]
              for row in terminal.get("semantic_audits", [])
              if row.get("path") in SEMANTIC_HASHES
          ), "terminal exact semantic-audit paths and hashes")
    check(terminal.get("semantic_consolidation") == {
        "path": "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json",
        "sha256": SEMANTIC_HASHES[
            "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json"],
    }, "terminal exact semantic-consolidation binding")
    check({row.get("path") for row in terminal.get("checker_receipts", [])} ==
          expected_checker_paths, "terminal exact checker paths")
    check({row.get("path") for row in terminal.get("verification_reports", [])} ==
          expected_report_paths, "terminal exact verification-report paths")
    check({row.get("path") for row in terminal.get("abort_records", [])} ==
          expected_abort_paths, "terminal exact abort paths")
    check(terminal.get("batch_report", {}).get("path") ==
          "BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md",
          "terminal batch-report path")
    check(terminal.get("batch_report", {}).get("sha256") ==
          TERMINAL_HASHES.get("batch_report"),
          "terminal frozen batch-report hash")
    check(terminal.get("mandatory_checkpoint", {}).get("path") ==
          "BATCH_ROUND10_STAGE3_PRIME_MANDATORY_CHECKPOINT.md",
          "terminal checkpoint path")
    check(terminal.get("mandatory_checkpoint", {}).get("sha256") ==
          TERMINAL_HASHES.get("mandatory_checkpoint"),
          "terminal frozen checkpoint hash")
    all_terminal_paths = []
    for binding in terminal.values():
        if isinstance(binding, list):
            all_terminal_paths.extend(row.get("path") for row in binding)
        elif isinstance(binding, dict):
            all_terminal_paths.append(binding.get("path"))
    check(len(all_terminal_paths) == 22 and
          len(set(all_terminal_paths)) == 22,
          "terminal path uniqueness and total closure count")

    checkpoint_text = read_text(
        ROOT / "BATCH_ROUND10_STAGE3_PRIME_MANDATORY_CHECKPOINT.md"
    )
    check("Reply **“确认”** to authorize exactly these next actions:" in
          checkpoint_text and
          "start fresh Stage 3′ Round-2 records" in checkpoint_text and
          "does **not** authorize manuscript/bibliography edits, Stage 4′ request preparation" in
          checkpoint_text and
          "no decision was emitted" in checkpoint_text,
          "checkpoint exact authorization boundary language")
    check("authorize scoped Stage 4′" not in checkpoint_text and
          "Stage 4′ is authorized" not in checkpoint_text and
          "manuscript writes are authorized" not in checkpoint_text,
          "checkpoint contains no conflicting successor authorization")

    root_readme = read_text(ROOT / "README.md")
    check("P29--P33_ALL_ABORTED_FAIL_CLOSED" in root_readme,
          "root README current outcome")
    check("Stage 3 prime 尚未开始" not in root_readme,
          "root README old current claim absent")
    check("P33_COMPLETE_MAJOR_B4" not in root_readme and
          "P29--P32_ABORTED_FAIL_CLOSED" not in root_readme and
          "审计支持 **22/32/2**" not in root_readme and
          "P33 开始 scoped Stage 4′" not in root_readme,
          "root README has no superseded mixed outcome")
    check(all(value in root_readme for key, value in TERMINAL_HASHES.items()
              if key != "outcome_receipt") and
          TERMINAL_HASHES["outcome_receipt"] in root_readme and
          SEMANTIC_HASHES[
              "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json"
          ] in root_readme,
          "root README carries current terminal batch hashes")

    root_successor_hits = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT).as_posix()
        if (round10_context.search(relative) and
                successor_pattern.search(relative)):
            root_successor_hits.append(relative)
    check(not root_successor_hits,
          "no recursively located Round-10 successor-stage artifact")

    # Historical Stage-3 audit is replayed as an upstream invariant.
    historical = subprocess.run(
        [sys.executable, str(ROOT / "tools/audit_round10_stage3.py")],
        cwd=ROOT, text=True, capture_output=True,
    )
    historical_output = (historical.stdout + historical.stderr).strip()
    try:
        historical_json = json.loads(historical_output)
    except json.JSONDecodeError:
        historical_json = {}
    check(historical.returncode == 0 and historical_json.get("status") == "PASS",
          "upstream Stage-3 full audit replay")
    check(historical_json.get("totals", {}).get("canonical_mutations") == 0,
          "upstream canonical mutation count zero")

    # No evaluation target or top-level successor authorization has appeared.
    evaluation_hits = []
    evaluation_root = ROOT / "evaluations"
    if evaluation_root.exists():
        for path in evaluation_root.rglob("*"):
            if path.is_file():
                if not real_regular_file(path):
                    evaluation_hits.append(str(path.relative_to(ROOT)))
                    continue
                text = path.read_text(encoding="utf-8", errors="ignore")
                if any(token in text for token in ("P29", "P30", "P31", "P32", "P33")):
                    evaluation_hits.append(str(path.relative_to(ROOT)))
    check(not evaluation_hits, "no P29-P33 Route evaluation artifact")

    status_surface_paths = [ROOT / "README.md"]
    for spec in PAPERS.values():
        paper = ROOT / "papers" / spec["slug"]
        status_surface_paths.extend([
            paper / "README.md",
            paper / "paper/README.md",
            paper / "notes/pipeline_state.md",
        ])
    tooling_paths = [
        ROOT / "tools/build_round10_stage3_prime_outcomes.rb",
        ROOT / "tools/audit_round10_stage3_prime_final.py",
        CHECKER,
        PANEL_VALIDATOR,
        WORKFLOW,
        PROTOCOL,
        ROUTE_A,
        ROUTE_B,
        CONTRACTS / "input_manifest.schema.json",
        CONTRACTS / "precommitment.schema.json",
        CONTRACTS / "verdict_record.schema.json",
        CONTRACTS / "traceability.schema.json",
    ]

    canonical_clean = (len(integrity_by_paper) == len(PAPERS) and all(
        row["canonical"] for row in integrity_by_paper.values()))
    science_clean = (len(integrity_by_paper) == len(PAPERS) and all(
        row["science"] for row in integrity_by_paper.values()))
    route_clean = (len(integrity_by_paper) == len(PAPERS) and all(
        row["route"] for row in integrity_by_paper.values()) and
        not evaluation_hits)
    successor_clean = (len(integrity_by_paper) == len(PAPERS) and all(
        row["successor"] for row in integrity_by_paper.values()) and
        not root_successor_hits)

    receipt = {
        "schema_version": "round10-stage3-prime-final-audit/1.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "PASS" if not failures else "FAIL",
        "checks_passed": len(checks),
        "failures": failures,
        "papers": paper_results,
        "outcome_receipt": {
            "path": str(outcome_file.relative_to(ROOT)),
            "sha256": digest(outcome_file),
        },
        "upstream_frozen_artifacts": [
            {"path": rel, "sha256": digest(ROOT / rel)}
            for rel in BATCH_HASHES
        ],
        "semantic_evidence": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for path in semantic_paths if real_regular_file(path)
        ],
        "outcome_terminal_artifacts": outcome.get("terminal_artifacts", {}),
        "status_surfaces": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for path in status_surface_paths
        ],
        "tooling_and_contracts": [
            {
                "path": (str(path.relative_to(ROOT))
                         if path.is_relative_to(ROOT) else str(path)),
                "sha256": digest(path),
            }
            for path in tooling_paths
        ],
        "closure_note": "This receipt cannot contain its own hash. The Git commit that publishes it supplies the external terminal binding.",
        "boundaries": {
            "canonical_mutations": 0 if canonical_clean else None,
            "scientific_result_mutations": 0 if science_clean else None,
            "initial_system_mutations": 0 if route_clean else None,
            "route_advancement": "NONE" if route_clean else None,
            "route_b_invoked": False if route_clean else None,
            "stage3_prime_round2_authorized": False if successor_clean else None,
            "p33_stage4_prime_revision_authorized": False if successor_clean else None,
            "stage4_5_authorized": False if successor_clean else None,
            "stage5_authorized": False if successor_clean else None,
        },
    }
    atomic_write_json(OUTPUT, receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    try:
        exit_code = main()
    except Exception as exc:  # fail closed with a machine-readable receipt
        fatal = {
            "schema_version": "round10-stage3-prime-final-audit/1.0",
            "generated_at": datetime.now(timezone.utc).replace(
                microsecond=0).isoformat().replace("+00:00", "Z"),
            "status": "FAIL",
            "checks_passed": 0,
            "failures": [
                f"fatal audit exception: {type(exc).__name__}: {exc}"
            ],
            "boundaries": {
                "canonical_mutations": None,
                "scientific_result_mutations": None,
                "initial_system_mutations": None,
                "route_advancement": None,
                "route_b_invoked": None,
                "stage3_prime_round2_authorized": None,
                "p33_stage4_prime_revision_authorized": None,
                "stage4_5_authorized": None,
                "stage5_authorized": None,
            },
            "closure_note": "Audit stopped fail-closed before a complete terminal proof could be emitted.",
        }
        try:
            atomic_write_json(OUTPUT, fatal)
        except Exception as persistence_exc:
            fatal["failures"].append(
                "fatal receipt persistence failed without following the target: "
                f"{type(persistence_exc).__name__}: {persistence_exc}"
            )
        print(json.dumps(fatal, indent=2, ensure_ascii=False))
        exit_code = 1
    raise SystemExit(exit_code)
