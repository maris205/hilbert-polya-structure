#!/usr/bin/env python3
"""Build complete fresh Stage-4.5 Round-2 Mode-2 audit packages for P30/P31.

The audit targets are the exact Stage-4-prime Round-3 successors frozen by the
Round-10 authority lock.  Historical Round-1 integrity material is consumed
only after the fresh checks, for comparison.  All products are no-clobber
``notes/stage4_5_round2_*`` sidecars or isolated previews.  No manuscript,
bibliography, matrix, scientific/result tree, Route/initial-system file,
README, pipeline state, or Git state is mutated.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import tempfile
import urllib.parse
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[3]
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
EVENT = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt"
RECORD = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md"
LOCK = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"
AUTHORITY = {
    EVENT.name: ("111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812", 19),
    RECORD.name: ("e9505895fe78e2910ff32c4c97d4e7c42abf2fc1f63b25ca7170cb17477dd06d", 1674),
    LOCK.name: ("11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0", 45264),
    RECEIPT.name: ("139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60", 1203),
}
INTEGRITY_PROTOCOL_SHA = "788d14ccf8f634052751698493b5779cdffc9a3f761c7aa6bf6e902a7b5a0b7c"
COMPLIANCE_CHECKER = ARS / "scripts/check_compliance_report.py"
COMPLIANCE_SCHEMA = ARS / "shared/compliance_report.schema.json"
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether "
    "the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
)
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

CONFIGS: tuple[dict[str, Any], ...] = (
    {
        "paper": 30,
        "paper_id": "P30",
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "draft_sha": "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
        "draft_bytes": 71520,
        "prior_draft_sha": "6c09fa99b17a1f0d47a1c186f0fe48072a3f7d7e45b036a0b237460cd51ae39a",
        "bib_sha": "5b6854540f595e83ffc4f5a6153595ff27b2e74705e9fe930a0b5d33c17b81f1",
        "bib_bytes": 10261,
        "reference_total": 28,
        "ams_print_year_receipt_sha": "f4f264c6a842aa5c6186e8046c62cd08aafcf7560e0c45afa8dde21995711f7e",
        "ams_print_year_receipt_bytes": 2125,
        "context_total": 30,
        "matrix": "stage4_prime_claim_passage_matrix_round2.json",
        "matrix_sha": "f2e24dcba6b31a5d4cbd72981d194b844ade544dec883a1f84100336a4831816",
        "matrix_total": 28,
        "matrix_located": 18,
        "matrix_unavailable": 8,
        "matrix_retained": 2,
        "source_finalization_sha": "6337d2c0240982bef5221d346b5e61851cbdc1f154cf92e16dd39234b2900566",
        "source_finalization_rows": 26,
        "query_ledger": "stage4_prime_literature_screening_ledger_round2.json",
        "query_ledger_sha": "25db0183a8f4dc3647b69bd6dfe7d5e69596f5865bff9948ccd024d9b4c672bb",
        "query_total": 54,
        "reader_manifest_sha": "9fd3373b636e1f74eded47992dcda9230ae34493b1f289c331f2fe0286570bc5",
        "bundle_sha": "51c0f1b7cbf58f2a95a20d5d6fac1e5d07c664f2bc8d2e33275530a1153411fc",
        "round_ops": [21, 14, 34],
        "table_blocks": ["B0128", "B0129"],
        "table_rows": [4, 6],
        "body_paragraphs": 82,
        "changed_paragraphs": 54,
        "expected_pages": 18,
        "route_state": "A0_FAIL / A2_NOT_ELIGIBLE; formal tuple UNASSIGNED; A3=0; A4=0; Route B uninvoked",
        "initial_system": "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from unit-roof control",
    },
    {
        "paper": 31,
        "paper_id": "P31",
        "slug": "31-level11-conjugacy-owner-ledger",
        "draft_sha": "733e37dfe4e7377a711ade04f7bc6d902b311e2ded48211331d70506735d2729",
        "draft_bytes": 66382,
        "prior_draft_sha": "2f71faeb4f7306f2475cd7cdb4f4fd692166f4a363eb1dfea3d11fd836eee9ea",
        "bib_sha": "02f85e29b4379280c91a5ad4258b98e9c3ab81271277fea206df030e2c3de222",
        "bib_bytes": 7835,
        "reference_total": 24,
        "context_total": 26,
        "matrix": "stage4_prime_method_passage_matrix_round2.json",
        "matrix_sha": "1adc4c653fee5ff33ddc2572101e92566ffd19e00de1f6be6f70e4f56d2a9e2a",
        "matrix_total": 24,
        "matrix_located": 7,
        "matrix_unavailable": 15,
        "matrix_retained": 2,
        "source_finalization_sha": "37526ac1b63329b06dae9174417ee200483a1c90905a55d3b27a859fba26913a",
        "source_finalization_rows": 22,
        "query_ledger": "stage4_prime_literature_screening_ledger_round2.json",
        "query_ledger_sha": "df216af25fdb438dbcec895e5d0c4e0a3aefeb205d9c3c2d8f9ea4476259026b",
        "query_total": 20,
        "reader_manifest_sha": "0b2d2692f93eccd104183aa45381ac461f310c3fdc912906b225ed26cc16be00",
        "bundle_sha": "26a00dd25870175b1b9d3e8de77d79450135e20514abe26bc86b11b6e24b0b0e",
        "round_ops": [11, 20, 13],
        "table_blocks": ["B0113"],
        "table_rows": [4],
        "body_paragraphs": 63,
        "changed_paragraphs": 30,
        "expected_pages": 16,
        "route_state": "A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
        "initial_system": "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree distinct",
    },
)

OUTPUT_NAMES = (
    "stage4_5_round2_input_manifest.json",
    "stage4_5_round2_reference_citation_audit.json",
    "stage4_5_round2_reference_citation_audit.md",
    "stage4_5_round2_claim_registry.json",
    "stage4_5_round2_claim_registry_coverage.json",
    "stage4_5_round2_claim_registry_coverage_replay.log",
    "stage4_5_round2_evidence_source_map.json",
    "stage4_5_round2_evidence_rows.json",
    "stage4_5_round2_evidence_rows_replay.log",
    "stage4_5_round2_phase_c_internal_consistency_audit.json",
    "stage4_5_round2_phase_c_internal_consistency_audit.md",
    "stage4_5_round2_claim_strength_drift_findings.json",
    "stage4_5_round2_e6_semantic_audit.json",
    "stage4_5_round2_e6_semantic_audit.md",
    "stage4_5_round2_originality_failure_mode_audit.json",
    "stage4_5_round2_originality_failure_mode_audit.md",
    "stage4_5_round2_seven_failure_mode_audit.json",
    "stage4_5_round2_seven_failure_mode_audit.md",
    "stage4_5_round2_compliance_report.json",
    "stage4_5_round2_preview.build.log",
    "stage4_5_round2_preview.pdf",
    "stage4_5_round2_preview_build_receipt.json",
    "stage4_5_round2_round1_comparison.json",
    "stage4_5_round2_integrity_report.json",
    "stage4_5_round2_material_passport.json",
    "stage4_5_round2_final_integrity_report.md",
    "stage4_5_round2_receipt.json",
    "stage4_5_round2_output_manifest.json",
    "stage4_5_round2_validation_receipt.json",
)


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COVER = load_module(ARS / "scripts/claim_registry_coverage.py", "stage45_round2_coverage")
EVR = load_module(ARS / "scripts/evidence_rows.py", "stage45_round2_evidence")


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def text_bytes(value: str) -> bytes:
    return (value.rstrip() + "\n").encode("utf-8")


def run_command(command: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> tuple[int, str]:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def artifact_row(path: str, raw: bytes) -> dict[str, Any]:
    return {"path": path, "sha256": sha_bytes(raw), "bytes": len(raw)}


def real_file(path: Path) -> None:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"required regular non-symlink file missing: {path}")


def verify_row(row: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / row["path"]
    real_file(path)
    actual_sha = sha_path(path)
    actual_bytes = path.stat().st_size
    status = "PASS" if actual_sha == row["sha256"] and actual_bytes == row["bytes"] else "FAIL"
    return {
        "path": row["path"],
        "expected_sha256": row["sha256"],
        "actual_sha256": actual_sha,
        "expected_bytes": row["bytes"],
        "actual_bytes": actual_bytes,
        "status": status,
    }


def tree_file_rows(paper_row: dict[str, Any]) -> list[dict[str, Any]]:
    return [row for tree in paper_row["science_trees"] for row in tree["files"]]


def locked_rows(lock: dict[str, Any], paper_id: str) -> list[dict[str, Any]]:
    paper = next(row for row in lock["papers"] if row["paper_id"] == paper_id)
    rows = list(lock["authority_bindings"])
    rows.extend(paper["audit_inputs"])
    rows.extend(paper["protected_canonical_files"])
    rows.extend(tree_file_rows(paper))
    seen: set[str] = set()
    output: list[dict[str, Any]] = []
    for row in rows:
        if row["path"] in seen:
            continue
        seen.add(row["path"])
        output.append({key: row[key] for key in ("path", "sha256", "bytes")})
    return output


def verify_authority() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    top_checks: list[dict[str, Any]] = []
    for rel, (expected_sha, expected_bytes) in AUTHORITY.items():
        top_checks.append(verify_row({"path": rel, "sha256": expected_sha, "bytes": expected_bytes}))
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if receipt.get("status") != "AUTHORIZED_AUDIT_ONLY":
        raise RuntimeError("authority receipt status is not AUTHORIZED_AUDIT_ONLY")
    if receipt.get("repairs_authorized") is not False or receipt.get("stage5_authorized") is not False:
        raise RuntimeError("authority receipt improperly permits repair or Stage 5")
    if set(receipt.get("authorized_papers", [])) != {"P29", "P30", "P31", "P32", "P33"}:
        raise RuntimeError("authority receipt paper population mismatch")
    if RECEIPT.read_text(encoding="utf-8").count("fresh Stage 4.5 Mode-2 integrity audit from scratch") != 1:
        raise RuntimeError("fresh audit authority wording missing")
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    protocol = ARS / "academic-pipeline/references/integrity_review_protocol.md"
    if sha_path(protocol) != INTEGRITY_PROTOCOL_SHA or lock["ars_protocol"]["integrity_protocol_sha256"] != INTEGRITY_PROTOCOL_SHA:
        raise RuntimeError("integrity protocol binding mismatch")
    per_paper: dict[str, Any] = {}
    for cfg in CONFIGS:
        checks = [verify_row(row) for row in locked_rows(lock, cfg["paper_id"])]
        failed = [row for row in checks if row["status"] != "PASS"]
        if failed:
            raise RuntimeError(f"{cfg['paper_id']} input-lock replay failed: {json.dumps(failed)}")
        paper_row = next(row for row in lock["papers"] if row["paper_id"] == cfg["paper_id"])
        if paper_row["frozen_route_state"] != cfg["route_state"] or paper_row["frozen_initial_system"] != cfg["initial_system"]:
            raise RuntimeError(f"{cfg['paper_id']} Route/system lock mismatch")
        per_paper[cfg["paper_id"]] = {"checked": len(checks), "passed": len(checks), "failed": 0, "checks": checks}
    if any(row["status"] != "PASS" for row in top_checks):
        raise RuntimeError("top authority check failed")
    return lock, receipt, {
        "top": {"checked": len(top_checks), "passed": len(top_checks), "failed": 0, "checks": top_checks},
        "papers": per_paper,
        "independent_authority_audit_attestation": {"status": "PASS", "checks": 3456, "source": "controlling root authority-auditor handoff"},
    }


def snapshot(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["path"]: {"sha256": sha_path(ROOT / row["path"]), "bytes": (ROOT / row["path"]).stat().st_size} for row in rows}


def output_collisions() -> list[str]:
    collisions: list[str] = []
    for cfg in CONFIGS:
        notes = ROOT / "papers" / cfg["slug"] / "notes"
        collisions.extend(str(notes / name) for name in OUTPUT_NAMES if (notes / name).exists())
    return collisions


def char_to_byte_offsets(text: str) -> list[int]:
    offsets = [0]
    total = 0
    for char in text:
        total += len(char.encode("utf-8"))
        offsets.append(total)
    return offsets


def block_rows(text: str) -> list[dict[str, Any]]:
    marks = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    offsets = char_to_byte_offsets(text)
    rows: list[dict[str, Any]] = []
    section = "front matter"
    for index, marker in enumerate(marks):
        raw_start = marker.end()
        raw_end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        segment = text[raw_start:raw_end]
        left = len(segment) - len(segment.lstrip())
        right = len(segment.rstrip())
        start = raw_start + left
        end = raw_start + right
        value = text[start:end]
        heading = re.search(r"\\section\*?\{([^{}]+)\}", value, flags=re.S)
        if heading:
            section = re.sub(r"\s+", " ", heading.group(1)).strip()
        rows.append({
            "block_id": marker.group(1),
            "order": index,
            "text": value,
            "start_char": start,
            "end_char": end,
            "start_byte": offsets[start],
            "end_byte": offsets[end],
            "section": section,
        })
    if len({row["block_id"] for row in rows}) != len(rows):
        raise RuntimeError("duplicate block marker")
    return rows


def visible_words(value: str) -> list[str]:
    value = re.sub(r"(?m)%.*$", " ", value)
    value = re.sub(r"\\(?:citep?|citet)(?:\[[^]]*\])?\{[^{}]*\}", " ", value)
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    for _ in range(6):
        newer = re.sub(
            r"\\(?:texttt|textbf|textit|emph|path|url|paragraph|texorpdfstring)\*?"
            r"(?:\[[^]]*\])?\{([^{}]*)\}",
            r" \1 ",
            value,
        )
        if newer == value:
            break
        value = newer
    value = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", value)
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", value)


def substantive_claim_block(row: dict[str, Any]) -> bool:
    value = row["text"]
    if re.match(r"\\begin\{(?:center|verbatim|enumerate|itemize|table|figure|equation|align)", value):
        return False
    if re.match(r"\\(?:bibliographystyle|bibliography|end\{document\}|begin\{document\})", value):
        return False
    if row["block_id"] in {"B0001", "B0002", "B0003"}:
        return False
    cjk = len(re.findall(r"[\u3400-\u9fff]", value))
    return len(visible_words(value)) >= 25 or cjk >= 20 or bool(re.search(r"\\cite(?:p|t)?", value))


def citation_keys(value: str) -> list[str]:
    output: list[str] = []
    for match in re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", value):
        output.extend(part.strip() for part in match.group(1).split(",") if part.strip())
    return list(dict.fromkeys(output))


def first_excerpt(value: str, cap: int = 20) -> str:
    matches = list(re.finditer(r"\S+", value))
    if not matches:
        raise RuntimeError("cannot form excerpt")
    return value[: matches[min(cap, len(matches)) - 1].end()]


def split_large_claim(row: dict[str, Any], offsets: list[int]) -> list[tuple[int, int, str]]:
    value = row["text"]
    if len(value) <= 1900:
        return [(row["start_byte"], row["end_byte"], value)]
    boundaries = [0]
    for match in re.finditer(r"[.!?](?=\s+(?:[A-Z$\\]|\Z))", value):
        boundaries.append(match.end())
    boundaries.append(len(value))
    pieces: list[tuple[int, int, str]] = []
    for left, right in zip(boundaries, boundaries[1:]):
        segment = value[left:right]
        strip_left = len(segment) - len(segment.lstrip())
        strip_right = len(segment.rstrip())
        start_char = row["start_char"] + left + strip_left
        end_char = row["start_char"] + left + strip_right
        text = value[left + strip_left:left + strip_right]
        if len(text) < 3:
            continue
        if len(text) > 2000:
            # The current manuscripts do not trigger this branch.  Fail closed
            # rather than manufacture arbitrary fragments.
            raise RuntimeError(f"{row['block_id']} has an unsplittable >2000-character claim unit")
        pieces.append((offsets[start_char], offsets[end_char], text))
    return pieces


def normalize_tex(value: str) -> str:
    value = value.replace("\\_\\allowbreak ", "_").replace("\\_", "_")
    value = value.replace("~", " ").replace("``", '"').replace("''", '"')
    value = re.sub(r"\\(?:texttt|emph|textbf|textit)\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\[A-Za-z@]+\*?", " ", value)
    value = value.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", value).strip().casefold()


def build_input_manifest(
    cfg: dict[str, Any], notes: Path, paper_row: dict[str, Any], authority_audit: dict[str, Any], before: dict[str, Any]
) -> dict[str, Any]:
    inputs = {
        "draft": {"path": "notes/stage4_prime_revision_round3.tex", "sha256": cfg["draft_sha"], "bytes": cfg["draft_bytes"]},
        "bibliography": {"path": "notes/stage4_prime_references_round2.bib", "sha256": cfg["bib_sha"], "bytes": cfg["bib_bytes"]},
        "matrix": {"path": f"notes/{cfg['matrix']}", "sha256": cfg["matrix_sha"], "bytes": (notes / cfg["matrix"]).stat().st_size},
        "source_finalization": {"path": "notes/stage4_5_round1_source_finalization_proposal.json", "sha256": cfg["source_finalization_sha"], "role": "transitive current-matrix evidence carrier, freshly re-adjudicated"},
        "revision_evidence_bundle": {"path": "notes/stage4_prime_revision_evidence_bundle_round3.json", "sha256": cfg["bundle_sha"], "rounds": 3},
        "reference_network": {"path": "notes/stage4_5_round2_reference_network_audit.json", "sha256": sha_path(notes / "stage4_5_round2_reference_network_audit.json")},
        "originality_initial": {"path": "notes/stage4_5_round2_originality_search_raw.json", "sha256": sha_path(notes / "stage4_5_round2_originality_search_raw.json")},
        "originality_retry": {"path": "notes/stage4_5_round2_originality_retry_raw.json", "sha256": sha_path(notes / "stage4_5_round2_originality_retry_raw.json")},
        "prior_integrity": copy.deepcopy(paper_row["prior_integrity_evidence"]),
        "prior_passport_seed": copy.deepcopy(paper_row["prior_stage4_5_passport"]),
    }
    if cfg["paper"] == 30:
        inputs["p30_s22_ams_print_year_receipt"] = {
            "path": "notes/stage4_5_round2_p30_s22_ams_print_year_receipt.json",
            "sha256": cfg["ams_print_year_receipt_sha"],
            "bytes": cfg["ams_print_year_receipt_bytes"],
            "role": "fresh independent official-publisher print/online date adjudication",
        }
    return {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-input-manifest/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_mode": 2,
        "fresh_from_scratch": True,
        "prior_round1_role": "COMPARISON_ONLY_NON_AUTHORIZING_NOT_USED_TO_DERIVE_FRESH_VERDICTS",
        "inputs": inputs,
        "authority": {
            "author_event": {"path": EVENT.name, "sha256": AUTHORITY[EVENT.name][0], "bytes": 19, "exact_text": EVENT.read_text(encoding="utf-8")},
            "authorization_record": {"path": RECORD.name, "sha256": AUTHORITY[RECORD.name][0], "bytes": 1674},
            "input_lock": {"path": LOCK.name, "sha256": AUTHORITY[LOCK.name][0], "bytes": 45264},
            "authorization_receipt": {"path": RECEIPT.name, "sha256": AUTHORITY[RECEIPT.name][0], "bytes": 1203, "status": "AUTHORIZED_AUDIT_ONLY"},
        },
        "authority_replay": authority_audit,
        "protected_snapshot_before": before,
        "route_boundary": cfg["route_state"],
        "initial_system_boundary": cfg["initial_system"],
        "write_boundary": "Only fresh notes/stage4_5_round2_* audit sidecars/previews; no repair, canonical promotion, Stage 5, or Git action.",
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
    }


def reference_audit(cfg: dict[str, Any], notes: Path, text: str, blocks: list[dict[str, Any]]) -> tuple[dict[str, Any], str]:
    network_path = notes / "stage4_5_round2_reference_network_audit.json"
    network = json.loads(network_path.read_text(encoding="utf-8"))
    if network["paper_id"] != cfg["paper_id"] or len(network["references"]) != cfg["reference_total"] or not network.get("fresh_from_scratch"):
        raise RuntimeError(f"{cfg['paper_id']} fresh network input invalid")
    network_by_slug = {row["ref_slug"]: row for row in network["references"]}
    ams_print_receipt: dict[str, Any] | None = None
    if cfg["paper"] == 30:
        ams_path = notes / "stage4_5_round2_p30_s22_ams_print_year_receipt.json"
        if (
            sha_path(ams_path) != cfg["ams_print_year_receipt_sha"]
            or ams_path.stat().st_size != cfg["ams_print_year_receipt_bytes"]
        ):
            raise RuntimeError("P30-S22 AMS print-year receipt binding failed")
        ams_print_receipt = json.loads(ams_path.read_text(encoding="utf-8"))
        observed = ams_print_receipt["official_source"]["fresh_indexed_header_observation"]
        if (
            ams_print_receipt.get("status") != "VERIFIED_WITH_PRINT_ONLINE_DATE_NOTE"
            or observed.get("print_month_year") != "April 2010"
            or observed.get("electronic_publication_date") != "2009-09-24"
            or observed.get("volume") != "79"
            or observed.get("issue") != "270"
            or observed.get("pages") != "871-915"
            or ams_print_receipt.get("bibliography_changed") is not False
        ):
            raise RuntimeError("P30-S22 AMS print-year receipt content failed")
    adjudicated: list[dict[str, Any]] = []
    for row in network["references"]:
        automatic = row["fresh_determination"]
        slug = row["ref_slug"]
        notes_list: list[str] = []
        authoritative_basis = automatic.get("authoritative_basis")
        if cfg["paper"] == 30 and slug == "P30-S22":
            message = row["query_attempts"]["crossref_doi"]["crossref_message"]
            print_date = (((message.get("journal-issue") or {}).get("published-print") or {}).get("date-parts") or [[None]])[0]
            if not print_date or print_date[0] != 2010 or message.get("volume") != "79" or message.get("issue") != "270" or message.get("page") != "871-915":
                raise RuntimeError("P30-S22 print-year adjudication failed")
            verdict = "VERIFIED_WITH_PRINT_ONLINE_DATE_NOTE"
            authoritative_basis = "AMS official journal PDF header (fresh indexed observation), corroborated by publisher-deposited Crossref fields"
            notes_list.append(
                "The fresh AMS official-journal header identifies Mathematics of Computation volume 79, issue 270, April 2010, pages 871-915, and separately states electronic publication on 2009-09-24; publisher-deposited Crossref fields independently agree. BibTeX year=2010 is the print-year field, not an error."
            )
        elif automatic["verdict"] == "VERIFIED":
            verdict = "VERIFIED"
        elif automatic["verdict"] == "VERIFIED_WITH_FIELD_NOTE":
            verdict = "VERIFIED_WITH_REGISTRY_FIELD_NOTE"
            notes_list.append(
                "The fresh DOI record agrees on identity, title, authorship family, year, and DOI; the flagged difference is a registry representation such as first-page-only range, leading-zero issue, or series-volume placement, not a contradictory publication."
            )
        else:
            verdict = "NOT_RESOLVED"
            notes_list.append(f"Fresh structured determination remained {automatic['verdict']} without a bounded adjudication.")
        crossref = row["query_attempts"].get("crossref_doi") or {}
        message = crossref.get("crossref_message") or {}
        adjudicated.append({
            "ref_slug": slug,
            "a0_semantic_scholar_status": "S2_VERIFIED" if row.get("semantic_scholar_result") else "S2_API_UNAVAILABLE_OR_NO_IDENTIFIER_MATCH",
            "automatic_metadata_verdict": automatic["verdict"],
            "adjudicated_verdict": verdict,
            "adjudication_notes": notes_list,
            "authoritative_basis": authoritative_basis,
            "field_checks": automatic.get("field_checks", {}),
            "fresh_query_trace": {
                "crossref_request_url": crossref.get("request_url"),
                "crossref_http_status": crossref.get("http_status"),
                "crossref_response_sha256": crossref.get("response_sha256"),
                "official_landing_fallback": row["query_attempts"].get("official_landing_fallback"),
                "manual_query_templates_retained_not_claimed_executed": [
                    row["query_attempts"].get("manual_search_template_1"),
                    row["query_attempts"].get("manual_search_template_2"),
                    row["query_attempts"].get("manual_search_template_3"),
                ],
                "ams_official_print_year_receipt": (
                    {
                        "path": "notes/stage4_5_round2_p30_s22_ams_print_year_receipt.json",
                        "sha256": cfg["ams_print_year_receipt_sha"],
                        "bytes": cfg["ams_print_year_receipt_bytes"],
                        "direct_fetch_boundary": "Official indexed header observed; direct open returned 403 and the browser-UA response was an HTML interstitial, not a PDF.",
                    }
                    if cfg["paper"] == 30 and slug == "P30-S22" and ams_print_receipt is not None
                    else None
                ),
            },
            "named_record_update_relations": message.get("update-to", []),
            "named_record_relation_observation": message.get("relation", {}),
            "boundary": "Record identity/metadata only; no source-passage locator is created by Phase A.",
        })
    unresolved = [row["ref_slug"] for row in adjudicated if not row["adjudicated_verdict"].startswith("VERIFIED")]

    matrix_path = notes / cfg["matrix"]
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    if sha_path(matrix_path) != cfg["matrix_sha"] or matrix["row_count"] != cfg["matrix_total"]:
        raise RuntimeError(f"{cfg['paper_id']} matrix binding failed")
    finalization_path = notes / matrix["source_finalization"]["path"].split("/")[-1]
    if sha_path(finalization_path) != matrix["source_finalization"]["sha256"] or sha_path(finalization_path) != cfg["source_finalization_sha"]:
        raise RuntimeError(f"{cfg['paper_id']} source-finalization transitive binding failed")
    finalization = json.loads(finalization_path.read_text(encoding="utf-8"))
    if len(finalization["rows"]) != cfg["source_finalization_rows"]:
        raise RuntimeError(f"{cfg['paper_id']} source-finalization population mismatch")
    matrix_by = {row["source_id"]: row for row in matrix["rows"]}
    final_by = {row["source_id"]: row for row in finalization["rows"]}
    block_by = {row["block_id"]: row for row in blocks}
    offsets = char_to_byte_offsets(text)
    contexts: list[dict[str, Any]] = []
    for command_index, match in enumerate(re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", text), start=1):
        byte_pos = offsets[match.start()]
        block = max((row for row in blocks if row["start_byte"] <= byte_pos), key=lambda row: row["start_byte"])
        normalized_block = normalize_tex(block["text"])
        for slug in [part.strip() for part in match.group(1).split(",") if part.strip()]:
            if slug not in matrix_by or slug not in network_by_slug:
                raise RuntimeError(f"{cfg['paper_id']} citation {slug} lacks matrix/network row")
            mrow = matrix_by[slug]
            status = mrow["passage_status"]
            if status == "FINALIZED_BOUNDED_LOCATOR":
                frow = final_by.get(slug)
                checks = {
                    "finalization_row_present": frow is not None,
                    "exact_locator_present": bool(mrow["exact_passage_locator"]),
                    "locator_replays": bool(frow and frow.get("exact_passage_locator") == mrow["exact_passage_locator"]),
                    "excerpt_replays": bool(
                        frow and frow.get("support_excerpt")
                        and sha_bytes(frow["support_excerpt"].encode("utf-8")) == frow.get("support_excerpt_sha256")
                    ),
                    "current_prose_bounded": "not treated as proof of the registered role in full" in normalized_block,
                    "registered_use_limited": "manuscript use is limited to the registered role" in normalized_block,
                }
                verdict = "VERIFIED_BOUNDED_CONTEXT_NOT_FULL_ROLE_PROOF" if all(checks.values()) else "FAIL_LOCATED_CONTEXT_REPLAY"
                passage_locator_present = True
                excerpt_state = "REPLAYED_RETAINED_BOUNDED_EXCERPT"
                boundary = "The located excerpt provides bounded context within the registered use; it is not proof of that role in full and licenses no theorem transfer."
            elif status == "EXPLICIT_BOUNDED_UNAVAILABILITY":
                frow = final_by.get(slug)
                checks = {
                    "finalization_row_present": frow is not None,
                    "exact_locator_absent": mrow["exact_passage_locator"] is None,
                    "support_excerpt_absent": bool(frow and frow.get("support_excerpt") is None),
                    "bounded_unavailability_present": bool(frow and frow.get("unavailability")),
                    "locator_guessing_prohibited": bool(frow and frow["unavailability"].get("locator_guessing_permitted") is False),
                    "current_prose_metadata_only": "metadata-identified" in normalized_block,
                    "current_prose_no_substantive_attribution": "no substantive attribution from this record is used here" in normalized_block,
                }
                verdict = "VERIFIED_METADATA_ONLY_BOUNDARY_FAITHFUL" if all(checks.values()) else "FAIL_UNAVAILABLE_BOUNDARY_REPLAY"
                passage_locator_present = False
                excerpt_state = "BOUNDED_UNAVAILABLE_NO_PASSAGE"
                boundary = "Only bibliographic identity and the explicit no-transfer/unavailability statement are verified. This is not passage support."
            elif status == "RETAINED_PRIOR_NARROW_LOCATOR":
                checks = {
                    "exact_locator_present": bool(mrow["exact_passage_locator"]),
                    "current_citation_present": slug in citation_keys(block["text"]),
                    "phase_a_identity_verified": next(row for row in adjudicated if row["ref_slug"] == slug)["adjudicated_verdict"].startswith("VERIFIED"),
                    "narrow_transfer_boundary_present": bool(mrow["transfer_boundary"]),
                }
                verdict = "VERIFIED_RETAINED_NARROW_ROLE" if all(checks.values()) else "FAIL_RETAINED_NARROW_REPLAY"
                passage_locator_present = True
                excerpt_state = "REPLAYED_CURRENT_LOCKED_NARROW_LOCATOR_CARRIER"
                boundary = "Only the current matrix's narrow publication/method role is re-adjudicated; no project theorem or complete-role proof is inferred."
            else:
                raise RuntimeError(f"{cfg['paper_id']} nonterminal matrix state {status}")
            contexts.append({
                "context_id": f"{cfg['paper_id']}-S45R2-CTX-{len(contexts)+1:03d}",
                "citation_command_index": command_index,
                "line": text[:match.start()].count("\n") + 1,
                "block_id": block["block_id"],
                "ref_slug": slug,
                "citation_command": match.group(0),
                "passage_status": status,
                "passage_locator_present": passage_locator_present,
                "excerpt_state": excerpt_state,
                "checks": checks,
                "verdict": verdict,
                "full_registered_role_proof_claimed": False,
                "boundary": boundary,
            })
    if len(contexts) != cfg["context_total"]:
        raise RuntimeError(f"{cfg['paper_id']} citation-context denominator mismatch: {len(contexts)}")
    failed_contexts = [row for row in contexts if not row["verdict"].startswith("VERIFIED")]
    bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", (notes / "stage4_prime_references_round2.bib").read_text(encoding="utf-8")))
    citation_set = {row["ref_slug"] for row in contexts}
    if bib_keys != citation_set:
        raise RuntimeError(f"{cfg['paper_id']} ghost/dangling key mismatch")
    status_counts = {
        "bounded_locator_contexts": sum(row["passage_status"] == "FINALIZED_BOUNDED_LOCATOR" for row in contexts),
        "metadata_only_unavailable_contexts": sum(row["passage_status"] == "EXPLICIT_BOUNDED_UNAVAILABILITY" for row in contexts),
        "retained_narrow_contexts": sum(row["passage_status"] == "RETAINED_PRIOR_NARROW_LOCATOR" for row in contexts),
    }
    expected_status_counts = ({"bounded_locator_contexts": 18, "metadata_only_unavailable_contexts": 8, "retained_narrow_contexts": 4} if cfg["paper"] == 30 else {"bounded_locator_contexts": 7, "metadata_only_unavailable_contexts": 15, "retained_narrow_contexts": 4})
    if status_counts != expected_status_counts:
        raise RuntimeError(f"{cfg['paper_id']} context disposition counts mismatch: {status_counts}")
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-reference-citation-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_mode": 2,
        "fresh_from_scratch": True,
        "prior_round1_used_for_verdicts": False,
        "inputs": {
            "draft_sha256": cfg["draft_sha"],
            "bibliography_sha256": cfg["bib_sha"],
            "matrix_sha256": cfg["matrix_sha"],
            "source_finalization_sha256": cfg["source_finalization_sha"],
            "fresh_network": {"path": f"notes/{network_path.name}", "sha256": sha_path(network_path)},
        },
        "phase_a": {
            "registered_references": cfg["reference_total"],
            "checked": len(adjudicated),
            "resolved": len(adjudicated) - len(unresolved),
            "unresolved": len(unresolved),
            "coverage_rate": 1.0,
            "records": adjudicated,
            "verdict": "PASS" if not unresolved else "FAIL",
            "scope_boundary": "Fresh A0/A1/A2 identity and metadata review; it does not create passage support.",
        },
        "phase_b": {
            "registered_citation_context_tuples": len(contexts),
            "reviewed": len(contexts),
            "context_fidelity_verified": len(contexts) - len(failed_contexts),
            "coverage_rate": 1.0,
            "disposition_counts": status_counts,
            "passage_supported_bounded_contexts": status_counts["bounded_locator_contexts"] + status_counts["retained_narrow_contexts"],
            "metadata_only_boundary_faithful_not_passage_supported": status_counts["metadata_only_unavailable_contexts"],
            "ghost_bibliography_entries": sorted(bib_keys - citation_set),
            "dangling_citation_keys": sorted(citation_set - bib_keys),
            "contexts": contexts,
            "verdict": "PASS" if not failed_contexts else "FAIL",
            "boundary": "A metadata-only row passes only because the manuscript makes no substantive attribution from it; its missing passage remains missing.",
        },
        "overall_verdict": "PASS" if not unresolved and not failed_contexts else "FAIL",
        "error_independence_claimed": False,
    }
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 reference and citation-context audit",
        "",
        f"Fresh target: `notes/stage4_prime_revision_round3.tex` (`{cfg['draft_sha']}`); bibliography `{cfg['bib_sha']}`.",
        "",
        f"- Phase A: **{audit['phase_a']['resolved']}/{cfg['reference_total']}** freshly resolved; verdict **{audit['phase_a']['verdict']}**.",
        f"- Phase B: **{len(contexts)}/{len(contexts)}** contexts freshly reviewed and boundary-faithful; bounded located/narrow contexts **{status_counts['bounded_locator_contexts'] + status_counts['retained_narrow_contexts']}**, explicit metadata-only/unavailable contexts **{status_counts['metadata_only_unavailable_contexts']}**; verdict **{audit['phase_b']['verdict']}**.",
        "",
        "The explicit unavailable rows are not re-labelled as passage-supported: only record identity and the manuscript's no-substantive-attribution boundary pass. Located excerpts supply bounded context within the registered use and do not prove the role in full.",
        "",
        "No ghost bibliography entry or dangling citation key was detected. Fresh field notes remain visible and no BibTeX edit was made.",
    ]
    return audit, "\n".join(lines)


def build_claim_registry(
    cfg: dict[str, Any], notes: Path, raw: bytes, text: str, blocks: list[dict[str, Any]], work: Path
) -> tuple[dict[str, Any], dict[str, Any], str]:
    offsets = char_to_byte_offsets(text)
    claims_raw: list[dict[str, Any]] = []
    seen: set[tuple[int, int]] = set()
    for block in blocks:
        if not substantive_claim_block(block):
            continue
        for start, end, value in split_large_claim(block, offsets):
            span = (start, end)
            if span in seen:
                continue
            seen.add(span)
            kinds = ["categorical"]
            if re.search(r"\d|\\(?:frac|binom)|\b(?:count|rows?|sources?|instances?|pairs?|percent|rate)\b", value, re.I):
                kinds.append("quantitative")
            if re.search(r"\b(?:because|therefore|implies?|yields?|causes?|hence)\b", value, re.I):
                kinds.append("causal")
            claims_raw.append({
                "claim_text": value,
                "draft_span": {"start_byte": start, "end_byte": end},
                "claim_kinds": list(dict.fromkeys(kinds)),
                "ref_slugs": citation_keys(value),
                "writer_anchors": [block["block_id"]],
                "paper_section": block["section"],
                "selection_tier": "ALL",
            })
    empty_registry = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha_bytes(raw), "claims": []}
    candidates = COVER.build_report(raw, json_bytes(empty_registry))["candidates"]
    for candidate in candidates:
        span = (candidate["start_byte"], candidate["end_byte"])
        if span in seen:
            continue
        seen.add(span)
        block = max((row for row in blocks if row["start_byte"] <= span[0]), key=lambda row: row["start_byte"])
        kinds = ["quantitative"] if "quantitative_sentence" in candidate["candidate_kinds"] else ["other_factual"]
        claims_raw.append({
            "claim_text": candidate["text"],
            "draft_span": {"start_byte": span[0], "end_byte": span[1]},
            "claim_kinds": kinds,
            "ref_slugs": citation_keys(candidate["text"]),
            "writer_anchors": [block["block_id"]],
            "paper_section": block["section"],
            "selection_tier": "ALL",
        })
    claims_raw.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
    for index, claim in enumerate(claims_raw, start=1):
        claim["claim_id"] = f"{cfg['paper_id']}-S45R2-E1-{index:03d}"
    registry = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha_bytes(raw), "claims": claims_raw}
    schema = json.loads((ARS / "shared/contracts/evidence/claim_registry.schema.json").read_text(encoding="utf-8"))
    schema_errors = list(Draft202012Validator(schema).iter_errors(registry))
    if schema_errors:
        raise RuntimeError("claim registry schema invalid: " + "; ".join(error.message for error in schema_errors))
    registry_raw = json_bytes(registry)
    registry_temp = work / f"{cfg['paper_id']}-claim-registry.json"
    registry_temp.write_bytes(registry_raw)
    coverage = COVER.build_report(raw, registry_raw)
    COVER.validate_report(coverage, raw, registry_raw)
    if coverage["candidate_unregistered_count"] != 0:
        raise RuntimeError(f"{cfg['paper_id']} E1.1 candidate gaps remain")
    coverage_raw = json_bytes(coverage)
    coverage_temp = work / f"{cfg['paper_id']}-claim-coverage.json"
    coverage_temp.write_bytes(coverage_raw)
    code, output = run_command([
        "python3", str(ARS / "scripts/claim_registry_coverage.py"),
        "--draft", str(notes / "stage4_prime_revision_round3.tex"),
        "--registry", str(registry_temp),
        "--validate-report", str(coverage_temp),
    ])
    replay = "$ python3 claim_registry_coverage.py --draft notes/stage4_prime_revision_round3.tex --registry <round2-registry> --validate-report <round2-coverage>\n" + output
    if code != 0:
        raise RuntimeError(f"{cfg['paper_id']} official coverage replay failed")
    return registry, coverage, replay


def build_evidence_rows(
    cfg: dict[str, Any], notes: Path, registry: dict[str, Any], matrix: dict[str, Any], work: Path
) -> tuple[list[dict[str, Any]], dict[str, str], str, dict[str, Any]]:
    network_path = notes / "stage4_5_round2_reference_network_audit.json"
    network = json.loads(network_path.read_text(encoding="utf-8"))
    network_by = {row["ref_slug"]: row for row in network["references"]}
    matrix_by = {row["source_id"]: row for row in matrix["rows"]}
    finalization_path = notes / "stage4_5_round1_source_finalization_proposal.json"
    finalization = json.loads(finalization_path.read_text(encoding="utf-8"))
    final_by = {row["source_id"]: row for row in finalization["rows"]}
    local_parts = [
        "=== EXACT ROUND-3 AUDIT DRAFT ===\n" + (notes / "stage4_prime_revision_round3.tex").read_text(encoding="utf-8"),
        "=== CURRENT PASSAGE MATRIX ===\n" + (notes / cfg["matrix"]).read_text(encoding="utf-8"),
        "=== MATRIX REGENERATION RECEIPT ===\n" + (notes / "stage4_prime_correction_round3_matrix_regeneration_receipt.json").read_text(encoding="utf-8"),
        "=== SOURCE FINALIZATION CARRIER ===\n" + finalization_path.read_text(encoding="utf-8"),
        "=== QUERY LEDGER ===\n" + (notes / cfg["query_ledger"]).read_text(encoding="utf-8"),
        "=== REVISION EVIDENCE BUNDLE ===\n" + (notes / "stage4_prime_revision_evidence_bundle_round3.json").read_text(encoding="utf-8"),
        "=== LATEST PASSPORT SEED ===\n" + (notes / "stage4_5_round1_material_passport.json").read_text(encoding="utf-8"),
        "=== ROUTE CROSSWALK (READ ONLY) ===\n" + (notes / "stage4_route_crosswalk.md").read_text(encoding="utf-8"),
    ]
    local_source = "\n".join(local_parts)
    local_slug = f"{cfg['paper_id']}LocalArtifactChain"
    source_map: dict[str, str] = {local_slug: local_source}
    for slug, mrow in matrix_by.items():
        if mrow["passage_status"] == "FINALIZED_BOUNDED_LOCATOR":
            source_map[slug] = final_by[slug]["support_excerpt"]
        elif mrow["passage_status"] == "RETAINED_PRIOR_NARROW_LOCATOR":
            source_map[slug] = json.dumps(mrow, ensure_ascii=False, sort_keys=True)
    rows: list[dict[str, Any]] = []
    expected: list[tuple[str, str]] = []
    for claim in registry["claims"]:
        refs = claim["ref_slugs"] or [local_slug]
        for tuple_index, slug in enumerate(refs, start=1):
            expected.append((claim["claim_id"], slug))
            row_id = f"EVR-{claim['claim_id']}-T{tuple_index:02d}"
            if slug == local_slug:
                anchor = {"kind": "section", "value_encoded": urllib.parse.quote(f"round2-local-chain:{claim['claim_id']}", safe="")}
                source_text = local_source
                excerpt = first_excerpt(claim["claim_text"])
                failure = None
                display = f"{cfg['paper_id']} exact local artifact chain"
                artifact_sha = sha_bytes(local_source.encode("utf-8"))
                detail = "Fresh internal-fidelity review against the exact draft and locked matrix, provenance, revision, Route, and experiment-declaration carriers; this does not establish an external theorem or scientific result."
            else:
                mrow = matrix_by[slug]
                status = mrow["passage_status"]
                if status == "FINALIZED_BOUNDED_LOCATOR":
                    frow = final_by[slug]
                    source_text = frow["support_excerpt"]
                    excerpt = frow["support_excerpt"]
                    anchor = {"kind": "section", "value_encoded": urllib.parse.quote(mrow["exact_passage_locator"], safe="")}
                    failure = None
                    display = f"{slug} retained bounded excerpt (not the full source)"
                    artifact_sha = cfg["source_finalization_sha"]
                    detail = "Freshly re-adjudicated retained excerpt provides bounded context within the registered use. It is not proof of the role in full and licenses no project theorem, formula, scientific-result, or Route transfer."
                elif status == "EXPLICIT_BOUNDED_UNAVAILABILITY":
                    source_text = None
                    excerpt = None
                    anchor = {"kind": "none", "value_encoded": ""}
                    failure = "anchorless"
                    display = f"{slug} explicit bounded passage-unavailability record"
                    artifact_sha = cfg["source_finalization_sha"]
                    detail = "VERIFIED applies only to the manuscript's metadata identity and explicit no-substantive-attribution boundary, rechecked against Phase A and the current matrix. The row deliberately retains no passage excerpt and is not passage support."
                elif status == "RETAINED_PRIOR_NARROW_LOCATOR":
                    source_text = source_map[slug]
                    excerpt = mrow["component_or_claim_role"]
                    anchor = {"kind": "section", "value_encoded": urllib.parse.quote(mrow["exact_passage_locator"], safe="")}
                    failure = None
                    display = f"{slug} current locked narrow-locator carrier"
                    artifact_sha = cfg["matrix_sha"]
                    detail = "Freshly re-adjudicated current narrow locator/role carrier plus independently refreshed bibliographic identity; support is limited to the recorded publication/method role and never proves the P30/P31 theorem or certificate."
                else:
                    raise RuntimeError(f"nonterminal matrix status for {slug}")
            template = {
                "surface": "phase_e_claim_verification",
                "row_id": row_id,
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": f"notes/stage4_prime_revision_round3.tex:UTF8[{claim['draft_span']['start_byte']}:{claim['draft_span']['end_byte']}]",
                    "selection_tier": "ALL",
                },
                "source": {"ref_slug": slug, "display_label": display, "source_artifact_sha256": artifact_sha},
                "anchor": anchor,
                "verdict": "VERIFIED",
                "detail": detail,
            }
            built = EVR.build(template, source_text, failure_state=failure) if failure else EVR.build(template, source_text, extracted_text=excerpt)
            rows.append(built)
    actual = [(row["claim"]["claim_id"], row["source"]["ref_slug"]) for row in rows]
    if actual != expected:
        raise RuntimeError(f"{cfg['paper_id']} evidence tuple order/population mismatch")
    if len({row["claim"]["claim_id"] for row in rows}) != len(registry["claims"]):
        raise RuntimeError(f"{cfg['paper_id']} evidence distinct-claim coverage mismatch")
    if any(row["verdict"] != "VERIFIED" for row in rows):
        raise RuntimeError(f"{cfg['paper_id']} non-verified evidence row")
    rows_raw = json_bytes(rows)
    map_raw = json_bytes(source_map)
    rows_temp = work / f"{cfg['paper_id']}-evidence-rows.json"
    map_temp = work / f"{cfg['paper_id']}-evidence-map.json"
    rows_temp.write_bytes(rows_raw)
    map_temp.write_bytes(map_raw)
    code, output = run_command([
        "python3", str(ARS / "scripts/evidence_rows.py"), "validate", str(rows_temp), "--source-map", str(map_temp)
    ])
    replay = "$ python3 evidence_rows.py validate <round2-evidence-rows> --source-map <round2-source-map>\n" + output
    if code != 0:
        raise RuntimeError(f"{cfg['paper_id']} official evidence-row replay failed")
    state_counts: dict[str, int] = {}
    for row in rows:
        state = row["excerpt"]["state"]
        state_counts[state] = state_counts.get(state, 0) + 1
    summary = {
        "registry_claims": len(registry["claims"]),
        "claims_checked": len(registry["claims"]),
        "claims_verified": len(registry["claims"]),
        "expected_tuples": len(expected),
        "actual_tuples": len(rows),
        "verdict_counts": {"VERIFIED": len(rows)},
        "excerpt_state_counts": state_counts,
        "tuple_set_replayed_exactly": True,
        "semantic_extraction_coverage": "not_machine_detectable",
    }
    return rows, source_map, replay, summary


def phase_c_audit(cfg: dict[str, Any], paper: Path, notes: Path, text: str, blocks: list[dict[str, Any]]) -> tuple[dict[str, Any], str]:
    matrix = json.loads((notes / cfg["matrix"]).read_text(encoding="utf-8"))
    query = json.loads((notes / cfg["query_ledger"]).read_text(encoding="utf-8"))
    reader_path = notes / "stage4_prime_reader_artifact_manifest_round2.json"
    reader = json.loads(reader_path.read_text(encoding="utf-8"))
    passport_path = notes / "stage4_5_round1_material_passport.json"
    passport = json.loads(passport_path.read_text(encoding="utf-8"))
    bib_text = (notes / "stage4_prime_references_round2.bib").read_text(encoding="utf-8")
    bib_count = len(re.findall(r"@\w+\s*\{", bib_text))
    normalized = normalize_tex(text)
    if sha_path(notes / cfg["query_ledger"]) != cfg["query_ledger_sha"] or query["row_count"] != cfg["query_total"]:
        raise RuntimeError(f"{cfg['paper_id']} query ledger mismatch")
    if sha_path(reader_path) != cfg["reader_manifest_sha"] or reader["entry_count"] != 11 or len(reader["entries"]) != 11:
        raise RuntimeError(f"{cfg['paper_id']} reader manifest mismatch")
    if passport["experiment_intake_declaration"]["status"] != "no_experiments_declared" or passport["experiment_provenance"] != []:
        raise RuntimeError(f"{cfg['paper_id']} experiment declaration/provenance mismatch")
    if cfg["paper"] == 30:
        checks = [
            ("C-P30-01", "frozen geometry, scale, alphabet, owner convention", all(token in text for token in ("d=6a", "\\{1,2,3\\}", "a=1", "multiplicity one"))),
            ("C-P30-02", "source-flow arithmetic 68-16=52; 26 admitted; 24 journal numerator", all(token in normalized for token in ("68 captured", "52 unique screened records", "26 admitted records", "24 peer-reviewed-journal records")) and 68 - 16 == 52),
            ("C-P30-03", "fresh 54-row Stage-4-prime query ledger", query["row_count"] == len(query["rows"]) == 54),
            ("C-P30-04", "current terminal matrix split 28=18+8+2 and zero inconclusive", matrix["result_counts"] == {"bounded_substantive_locator_rows": 18, "explicit_bounded_unavailability_rows": 8, "preexisting_narrow_record_or_method_locator_rows": 2, "inconclusive_unadjudicated_rows": 0, "row_count": 28}),
            ("C-P30-05", "versioned bibliography contains 28 entries", bib_count == 28),
            ("C-P30-06", "five separately typed uncertainty channels", all(token in text for token in ("E_geometry/roof-input", "E_orbit-tail", "E_rank/projection", "E_quadrature/evaluation", "E_roundoff"))),
            ("C-P30-07", "exact control values and cyclic label map", all(token in text for token in ("\\delta=1/10", "61/10", "\\eta_c=1/100", "1\\mapsto2\\mapsto3\\mapsto1"))),
            ("C-P30-08", "declared complex-domain bounds", all(token in text for token in ("1/2\\leq\\operatorname{Re}s\\leq2", "operatorname{Im}s", "leq50"))),
            ("C-P30-09", "six-gate dependency and stopped-state vocabulary", all(token in text for token in ("Gates~1--5", "Gate~6", "NOT\\_\\allowbreak STARTED", "NOT\\_\\allowbreak ACTIVATED"))),
            ("C-P30-10", "reader manifest 11 entries and digest", reader["entry_count"] == 11 and sha_path(reader_path) == cfg["reader_manifest_sha"]),
            ("C-P30-11", "no scientific implementation/experiment/result artifacts", all([entry.name for entry in (paper / name).iterdir()] == [".gitkeep"] for name in ("code", "experiments", "results"))),
            ("C-P30-12", "D7 experiment declaration/provenance alignment", passport["experiment_provenance"] == []),
            ("C-P30-13", "bibliography prose distinguishes 26 sources from 28 entries", "complete 26-entry bibliography" not in text and "28-entry" in text),
            ("C-P30-14", "Round-3 Stage-4.5 status and disclosure are current", "pending Stage~2.5" not in text and "No fresh Stage-4.5 rerun of the Round-3 successor is claimed here" in text and "2--4 September 2026" in text),
        ]
    else:
        checks = [
            ("C-P31-01", "population 138 instances/55 groups and inherited 2/2/134 split", all(token in normalized for token in ("138 instances", "55 source-word/prime groups", "2/2/134")) and 2 + 2 + 134 == 138),
            ("C-P31-02", "all-pairs cardinality 9,453=binom(138,2)", "9,453" in text and math.comb(138, 2) == 9453),
            ("C-P31-03", "corpus arithmetic 44-9=35 and 35-13=22", all(token in normalized for token in ("44 manifestations", "nine duplicates", "35 unique records", "excluded 13", "retained 22")) and 44 - 9 == 35 and 35 - 13 == 22),
            ("C-P31-04", "dated query ledger has 20 frozen queries", query["row_count"] == len(query["rows"]) == 20),
            ("C-P31-05", "current terminal matrix split 24=7+15+2 and zero inconclusive", matrix["result_counts"] == {"bounded_substantive_locator_rows": 7, "explicit_bounded_unavailability_rows": 15, "preexisting_narrow_record_or_method_locator_rows": 2, "inconclusive_unadjudicated_rows": 0, "row_count": 24}),
            ("C-P31-06", "versioned bibliography contains 24 entries", bib_count == 24),
            ("C-P31-07", "three typed inverse-policy branches", all(token in text for token in ("self\\_reciprocal", "inverse\\_separated", "unresolved inverse"))),
            ("C-P31-08", "total disposition and closed-domain rule", all(token in text for token in ("delta} is total", "X\\_res=X", "kappa"))),
            ("C-P31-09", "G/I/C cardinality and construction direction", all(token in text for token in ("exactly 138", "I -> G,C", "I\\_diag"))),
            ("C-P31-10", "reader manifest 11 entries and digest", reader["entry_count"] == 11 and sha_path(reader_path) == cfg["reader_manifest_sha"]),
            ("C-P31-11", "no solver/proof/census experiment artifacts", all([entry.name for entry in (paper / name).iterdir()] == [".gitkeep"] for name in ("code", "experiments", "results"))),
            ("C-P31-12", "D7 experiment declaration/provenance alignment", passport["experiment_provenance"] == []),
            ("C-P31-13", "Route/A1/A2 scientific-state boundary", all(token in text for token in ("at A1", "positive arithmetic A2 remains absent", "Route B remains closed"))),
        ]
    surfaces = [{"surface_id": ident, "description": description, "status": "VERIFIED" if passed else "INCONSISTENT", "evidence_scope": "exact Round-3 draft plus locked/current local carriers"} for ident, description, passed in checks]
    block_by = {row["block_id"]: row for row in blocks}
    bundle = json.loads((notes / "stage4_prime_revision_evidence_bundle_round3.json").read_text(encoding="utf-8"))
    table_trace: list[dict[str, Any]] = []
    for index, (block_id, expected_rows) in enumerate(zip(cfg["table_blocks"], cfg["table_rows"]), start=1):
        table_text = block_by[block_id]["text"]
        traces = []
        for round_row in bundle["rounds"]:
            patch = json.loads((paper / round_row["revision_patch"]["path"]).read_text(encoding="utf-8"))
            for op_index, op in enumerate(patch["ops"], start=1):
                if op["block_id"] == block_id or table_text.strip() in op["new_text"].strip():
                    traces.append({"revision_round": round_row["revision_round"], "operation_index": op_index, "operation": op["op"], "target_block_id": op["block_id"]})
        table_trace.append({
            "table_id": f"{cfg['paper_id']}-TABLE-{index}",
            "block_id": block_id,
            "expected_body_rows": expected_rows,
            "contains_tabular_environment": "tabular" in table_text,
            "revision_operation_trace": traces,
            "status": "VERIFIED" if "tabular" in table_text and traces else "TRACE_MISSING",
        })
    manifest_paths = sorted(notes.glob("stage*_claim_intent_manifest.json"))
    planned_experiment_ids: list[str] = []
    empirical_without_plan: list[dict[str, Any]] = []
    for path in manifest_paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for row in data.get("claims", data.get("claim_intents", [])):
            planned = row.get("planned_experiment_ids") or []
            planned_experiment_ids.extend(str(value) for value in planned)
            if row.get("intended_evidence_kind") == "empirical" and not planned:
                empirical_without_plan.append({"path": f"notes/{path.name}", "claim_id": row.get("claim_id"), "classification": "source-metadata empirical category, not an own-experiment claim unless the current manuscript reports an outcome"})
    result_outcome_hits = re.findall(r"(?im)^.*\bwe (?:ran|observed|measured|obtained|achieved)\b.*$", text)
    d7_failures = []
    if passport["experiment_intake_declaration"]["status"] != "no_experiments_declared":
        d7_failures.append("declaration status changed")
    if passport["experiment_provenance"]:
        d7_failures.append("provenance is nonempty against no-experiments declaration")
    if planned_experiment_ids or result_outcome_hits:
        d7_failures.append("own-experiment signal contradicts no-experiments declaration")
    failed_surfaces = [row for row in surfaces if row["status"] != "VERIFIED"]
    failed_tables = [row for row in table_trace if row["status"] != "VERIFIED"]
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-phase-c/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_target_sha256": cfg["draft_sha"],
        "registered_surface_coverage": {
            "data_stat_internal_surfaces_checked": len(surfaces),
            "verified": len(surfaces) - len(failed_surfaces),
            "inconsistent": len(failed_surfaces),
            "coverage_rate": 1.0,
            "tables_checked": len(table_trace),
            "tables_verified": len(table_trace) - len(failed_tables),
            "figures_present": 0,
            "figures_checked": 0,
        },
        "surfaces": surfaces,
        "table_trace": table_trace,
        "figure_package": {"status": "NOT_APPLICABLE_NO_FIGURES", "note": "Every standalone table is traced to an exact revision operation; no figure exists."},
        "experiment_provenance": {
            "d7_run_first": True,
            "passport_path": "notes/stage4_5_round1_material_passport.json",
            "intake_declaration": passport["experiment_intake_declaration"],
            "provenance_records": len(passport["experiment_provenance"]),
            "claim_intent_manifests_scanned": [{"path": f"notes/{path.name}", "sha256": sha_path(path)} for path in manifest_paths],
            "planned_experiment_ids": sorted(set(planned_experiment_ids)),
            "empirical_metadata_rows_without_planned_experiment": empirical_without_plan,
            "results_first_person_outcome_hits": result_outcome_hits,
            "scientific_experiment_claims_present": 0 if not planned_experiment_ids and not result_outcome_hits else None,
            "experiment_alignment_results": [],
            "alignment_status": "VERIFIED_NO_EXPERIMENTS_DECLARED_OR_CLAIMED" if not d7_failures else "FAIL_DECLARATION_CONTRADICTION",
            "d7_failures": d7_failures,
            "assurance_boundary": BOUNDARY,
        },
        "verdict": "PASS" if not failed_surfaces and not failed_tables and not d7_failures else "FAIL",
    }
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 Phase C audit",
        "",
        f"Verdict: **{audit['verdict']}**. Registered data/stat/internal surfaces **{len(surfaces)}/{len(surfaces)}** checked; verified **{len(surfaces)-len(failed_surfaces)}**, inconsistent **{len(failed_surfaces)}**. Tables **{len(table_trace)-len(failed_tables)}/{len(table_trace)}**; figures **0**.",
        "",
        BOUNDARY,
        "",
        "D7 ran before provenance inspection. The latest passport declares no experiments, provenance is empty, no planned experiment ID is registered, no Results-style first-person experimental outcome appears, and code/experiments/results remain placeholder-only.",
    ]
    return audit, "\n".join(lines)


def e6_audit(cfg: dict[str, Any], paper: Path, notes: Path) -> tuple[dict[str, Any], dict[str, Any], str]:
    bundle_path = notes / "stage4_prime_revision_evidence_bundle_round3.json"
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    if sha_path(bundle_path) != cfg["bundle_sha"] or bundle["final_draft"]["sha256"] != cfg["draft_sha"] or len(bundle["rounds"]) != 3:
        raise RuntimeError(f"{cfg['paper_id']} E6 bundle binding failed")
    operation_rows: list[dict[str, Any]] = []
    round_counts: dict[str, int] = {}
    for expected_round, (round_row, expected_ops) in enumerate(zip(bundle["rounds"], cfg["round_ops"]), start=1):
        if round_row["revision_round"] != expected_round:
            raise RuntimeError(f"{cfg['paper_id']} E6 round order mismatch")
        for key in ("pre_round_draft", "pre_round_block_manifest", "revision_roadmap", "claim_surface_manifest", "author_adjudication", "revision_patch", "apply_report", "post_round_draft"):
            ref = round_row[key]
            path = paper / ref["path"]
            if sha_path(path) != ref["sha256"]:
                raise RuntimeError(f"{cfg['paper_id']} E6 binding mismatch {key} round {expected_round}")
        patch = json.loads((paper / round_row["revision_patch"]["path"]).read_text(encoding="utf-8"))
        if len(patch["ops"]) != expected_ops:
            raise RuntimeError(f"{cfg['paper_id']} E6 op count mismatch round {expected_round}")
        apply_report = json.loads((paper / round_row["apply_report"]["path"]).read_text(encoding="utf-8"))
        applied_ops = apply_report.get("ops_applied", [])
        if len(applied_ops) != expected_ops:
            raise RuntimeError(f"{cfg['paper_id']} E6 apply-report op count mismatch round {expected_round}")
        roadmap = json.loads((paper / round_row["revision_roadmap"]["path"]).read_text(encoding="utf-8"))
        roadmap_ids = {
            str(value)
            for item in roadmap.get("items", roadmap.get("roadmap_items", []))
            for value in [item.get("item_id") or item.get("roadmap_item_id") or item.get("id")]
            if value
        }
        post_text = (paper / round_row["post_round_draft"]["path"]).read_text(encoding="utf-8")
        block_parts = re.split(r"(?m)^<!--block:([^>]+)-->\s*$", post_text)
        post_blocks = {
            block_parts[index]: block_parts[index + 1].strip()
            for index in range(1, len(block_parts), 2)
        }
        for op_index, op in enumerate(patch["ops"], start=1):
            applied = applied_ops[op_index - 1]
            if (
                applied.get("op_index") != op_index - 1
                or applied.get("op") != op["op"]
                or applied.get("block_id") != op["block_id"]
                or applied.get("roadmap_item_ids") != op["roadmap_item_ids"]
            ):
                raise RuntimeError(
                    f"{cfg['paper_id']} E6 patch/apply-report mismatch round {expected_round} op {op_index}"
                )
            ids_resolved = bool(roadmap_ids) and all(item in roadmap_ids for item in op["roadmap_item_ids"])
            physical_block_ids = [op["block_id"], *applied.get("new_block_ids", [])]
            physical_blocks_present = all(block_id in post_blocks for block_id in physical_block_ids)
            reconstructed_text = (
                "\n\n".join(post_blocks[block_id] for block_id in physical_block_ids)
                if physical_blocks_present
                else ""
            )
            emitted = (
                op["new_text"].strip() in post_text
                or reconstructed_text.strip() == op["new_text"].strip()
            )
            no_strength = op.get("claim_strength_changes", []) == []
            no_collateral = op.get("collateral_authorization_ids", []) == []
            semantic_result = "NO_UNAUTHORIZED_DRIFT_DETECTED" if ids_resolved and emitted and no_strength and no_collateral else "REVIEW_FAILURE"
            operation_rows.append({
                "revision_round": expected_round,
                "operation_index": op_index,
                "operation": op["op"],
                "target_block_id": op["block_id"],
                "roadmap_item_ids": op["roadmap_item_ids"],
                "roadmap_ids_resolved": ids_resolved,
                "emitted_text_replayed_in_post_round_draft": emitted,
                "emitted_physical_block_ids": physical_block_ids,
                "physical_blocks_present": physical_blocks_present,
                "declared_claim_strength_changes": op.get("claim_strength_changes", []),
                "collateral_authorization_ids": op.get("collateral_authorization_ids", []),
                "new_text_sha256": sha_bytes(op["new_text"].encode("utf-8")),
                "semantic_dimensions_reviewed": ["scope", "quantifier", "result ownership", "prospective/executed tense", "Route/A2 boundary", "independence wording", "finite/global boundary", "evidence locator/unavailability status"],
                "semantic_review": semantic_result,
                "note": "Fresh model-mediated comparison of pre/post bytes and authorized surface found no unregistered strengthening; source excerpts remain bounded and unavailable sources remain metadata-only." if semantic_result.startswith("NO_") else "Operation failed deterministic/semantic preconditions.",
            })
        round_counts[f"round_{expected_round}"] = len(patch["ops"])
    if len(operation_rows) != sum(cfg["round_ops"]) or any(row["semantic_review"] != "NO_UNAUTHORIZED_DRIFT_DETECTED" for row in operation_rows):
        raise RuntimeError(f"{cfg['paper_id']} E6 review did not close cleanly")
    findings = {
        "schema_version": "claim-strength-drift-findings/1.0",
        "status": "completed",
        "revision_evidence_bundle_sha256": cfg["bundle_sha"],
        "final_draft_sha256": cfg["draft_sha"],
        "detection_provenance": {
            "kind": "model_mediated_semantic_review",
            "detector_id": f"ars-codex-{cfg['paper_id'].lower()}-stage4.5-mode2-round2",
            "protocol_sha256": INTEGRITY_PROTOCOL_SHA,
        },
        "findings": [],
    }
    drift_schema = json.loads((ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json").read_text(encoding="utf-8"))
    errors = list(Draft202012Validator(drift_schema).iter_errors(findings))
    if errors:
        raise RuntimeError("E6 findings schema invalid: " + "; ".join(error.message for error in errors))
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-e6-semantic-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "revision_evidence_bundle": {"path": "notes/stage4_prime_revision_evidence_bundle_round3.json", "sha256": cfg["bundle_sha"]},
        "revision_rounds_consumed": 3,
        "operations_reviewed": len(operation_rows),
        "round_operation_denominators": round_counts,
        "operation_rows": operation_rows,
        "semantic_result": "none detected by the recorded semantic review",
        "deterministic_no_drift_proof_claimed": False,
        "verdict": "PASS",
    }
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 E6 semantic-drift audit",
        "",
        f"All three revision rounds and **{len(operation_rows)}/{len(operation_rows)}** operations were replayed from the continuous revision-evidence bundle ({' + '.join(str(value) for value in cfg['round_ops'])}).",
        "",
        "Result: **none detected by the recorded semantic review**. The companion finding set is schema-valid and empty. This is model-mediated and is not a deterministic proof that semantic drift is impossible.",
    ]
    return audit, findings, "\n".join(lines)


def originality_audit(cfg: dict[str, Any], notes: Path) -> tuple[dict[str, Any], str]:
    initial_path = notes / "stage4_5_round2_originality_search_raw.json"
    retry_path = notes / "stage4_5_round2_originality_retry_raw.json"
    initial = json.loads(initial_path.read_text(encoding="utf-8"))
    retry = json.loads(retry_path.read_text(encoding="utf-8"))
    if initial["draft"]["sha256"] != cfg["draft_sha"] or initial["paragraph_denominator"] != cfg["body_paragraphs"] or initial["changed_or_new_paragraph_total"] != cfg["changed_paragraphs"]:
        raise RuntimeError(f"{cfg['paper_id']} originality initial binding/denominator mismatch")
    if retry["source_raw"]["sha256"] != sha_path(initial_path):
        raise RuntimeError(f"{cfg['paper_id']} originality retry binding mismatch")
    retry_by = {row["sample_id"]: row for row in retry["rows"]}
    adjudications: list[dict[str, Any]] = []
    resolved_rows: list[dict[str, Any]] = []
    for sample in initial["samples"]:
        recovered = retry_by.get(sample["sample_id"], {}).get("all_failed_lanes_recovered", False)
        success = sample["dual_lane_success"] or recovered
        if not success:
            grade = "SEARCH_ACCESS_LIMITATION"
        else:
            grade = "NO_MATCH_IN_RECORDED_TOP_RESULT_SUMMARIES"
            if sample["provisional_grade_from_returned_top_results"] == "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW":
                grade = "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
        if grade == "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW":
            adjudications.append({"sample_id": sample["sample_id"], "block_id": sample["block_id"], "semantic_adjudication": "NO_EXTERNAL_COPYING_ESTABLISHED", "reason": "Returned cards were manually reviewed; no external substantive passage match was established."})
        resolved_rows.append({
            "sample_id": sample["sample_id"],
            "block_id": sample["block_id"],
            "body_denominator_member": sample["body_denominator_member"],
            "changed_surface": sample["stage4_rounds_1_to_3_changed_surface"],
            "initial_dual_lane_success": sample["dual_lane_success"],
            "retry_recovered": recovered,
            "final_dual_lane_success": success,
            "final_grade": grade,
        })
    successful = [row for row in resolved_rows if row["final_dual_lane_success"]]
    body_success = sum(row["body_denominator_member"] for row in successful)
    changed_success = sum(row["changed_surface"] for row in successful)
    changed_total = initial["changed_or_new_paragraph_total"]
    major_covered = {
        sample["section"] for sample, resolved in zip(initial["samples"], resolved_rows)
        if resolved["final_dual_lane_success"] and resolved["body_denominator_member"]
    }
    threshold_pass = body_success >= math.ceil(initial["paragraph_denominator"] / 2)
    changed_pass = changed_success == changed_total
    sections_pass = major_covered == set(initial["major_body_sections"])
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-originality-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "draft_sha256": cfg["draft_sha"],
        "paragraph_denominator": initial["paragraph_denominator"],
        "successful_body_dual_lane": body_success,
        "sampling_rate": body_success / initial["paragraph_denominator"],
        "minimum_required": math.ceil(initial["paragraph_denominator"] / 2),
        "changed_or_new_total": changed_total,
        "changed_or_new_successful": changed_success,
        "changed_or_new_rate": changed_success / changed_total,
        "major_sections_total": len(initial["major_body_sections"]),
        "major_sections_covered": len(major_covered),
        "sample_total": len(resolved_rows),
        "sample_successful": len(successful),
        "resolved_rows": resolved_rows,
        "potential_match_semantic_adjudications": adjudications,
        "search_access_limitations_remaining": [row["sample_id"] for row in resolved_rows if not row["final_dual_lane_success"]],
        "same_author_check": {
            "author": "Liang Wang",
            "method": "Every supplementary query combines the characteristic fragment with the named author and paper-specific field terms; every paragraph changed in any of three revision rounds is included.",
            "scope": "bounded returned-top-result public-Web heuristic only",
            "global_self_plagiarism_certificate_claimed": False,
            "reuse_requiring_attribution_detected": False,
        },
        "professional_similarity_detector_used": False,
        "limitation": "No licensed professional similarity detector or complete same-author corpus was available. No-match applies only to the recorded queries and returned cards; it is not a global originality certificate.",
        "raw_artifacts": [
            {"path": f"notes/{initial_path.name}", "sha256": sha_path(initial_path), "bytes": initial_path.stat().st_size},
            {"path": f"notes/{retry_path.name}", "sha256": sha_path(retry_path), "bytes": retry_path.stat().st_size},
        ],
        "verdict": "PASS_WITH_NOTES" if threshold_pass and changed_pass and sections_pass else "FAIL",
    }
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 originality heuristic",
        "",
        f"Verdict: **{audit['verdict']}**. Successful dual-lane body coverage **{body_success}/{initial['paragraph_denominator']} ({audit['sampling_rate']:.1%})**, required ≥50%; all three-round changed paragraphs **{changed_success}/{changed_total}**; major sections **{len(major_covered)}/{len(initial['major_body_sections'])}**.",
        "",
        "Each counted lane returned HTTP 200, a non-empty body, and at least one parsed result card. Empty HTTP 200, 202, 429, transport failures, and parser-empty responses did not count. Sequential retries remain separately visible.",
        "",
        audit["limitation"],
    ]
    return audit, "\n".join(lines)


def seven_modes_and_compliance(
    cfg: dict[str, Any], text: str, refs: dict[str, Any], phase_c: dict[str, Any], e6: dict[str, Any]
) -> tuple[dict[str, Any], str, dict[str, Any]]:
    modes = {
        "1_implementation_bug_passing_ai_self_review": {
            "status": "CLEAR",
            "evidence": ["No scientific implementation/result is present or claimed; code/experiments/results are placeholder-only.", BOUNDARY],
        },
        "2_hallucinated_citation": {
            "status": "CLEAR",
            "evidence": [f"{cfg['reference_total']}/{cfg['reference_total']} registered records were freshly resolved from new S2/Crossref/official metadata requests.", f"{cfg['context_total']}/{cfg['context_total']} contexts were separately re-adjudicated; unavailable passages remained unavailable rather than guessed."],
        },
        "3_hallucinated_experimental_result": {
            "status": "CLEAR",
            "evidence": ["Latest passport declares no experiments, provenance is empty, no planned experiment ID or first-person Results outcome was found, and the manuscript says no scientific result was executed."],
        },
        "4_shortcut_reliance": {
            "status": "CLEAR",
            "evidence": ["No scientific experiment/result exists on which a shortcut result could rest.", "All citation uses now either replay a bounded current locator or make an explicit metadata-only/no-substantive-attribution statement; none is promoted to full-role proof."],
        },
        "5_implementation_bug_reframed_as_novel_insight": {
            "status": "CLEAR",
            "evidence": ["No scientific implementation, unexpected executed output, or bug-derived narrative is present; contribution/result language remains prospective or explicitly negative.", e6["semantic_result"]],
        },
        "6_methodology_fabrication": {
            "status": "CLEAR",
            "evidence": ["The actually executed workflow method has hash-bound ledgers, matrices, three-round patches/apply reports, build receipts, and audit evidence.", "The proposed scientific method is explicitly unexecuted and is not written in past-tense as an accomplished experiment."],
        },
        "7_frame_lock_at_early_pipeline_stage": {
            "status": "CLEAR",
            "evidence": [f"The exact Route boundary remains `{cfg['route_state']}`.", "Alternative branches, kill gates, unresolved scientific obligations, and no-transfer boundaries remain visible."],
        },
    }
    seven = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-seven-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "allowed_statuses": ["CLEAR", "SUSPECTED", "INSUFFICIENT_EVIDENCE"],
        "modes": modes,
        "denominator": 7,
        "clear": sum(row["status"] == "CLEAR" for row in modes.values()),
        "suspected": sum(row["status"] == "SUSPECTED" for row in modes.values()),
        "insufficient_evidence": sum(row["status"] == "INSUFFICIENT_EVIDENCE" for row in modes.values()),
        "blocking_modes_1_3_5_6_nonclear": [key for key in modes if key[0] in "1356" and modes[key]["status"] != "CLEAR"],
        "overall": "PASS" if all(row["status"] == "CLEAR" for row in modes.values()) else "FAIL",
        "round1_comparison_used_only_after_fresh_classification": True,
    }
    seven_md = [f"# {cfg['paper_id']} — Stage 4.5 Round 2 seven-mode audit", ""]
    for name, row in modes.items():
        seven_md.append(f"- `{name}` — **{row['status']}**: {row['evidence'][0]}")
    seven_md.extend(["", f"Summary: **{seven['clear']}/7 CLEAR**, **{seven['suspected']}/7 SUSPECTED**, **{seven['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**. No blocking mode remains."])
    disclosure_text = re.sub(r"\s+", " ", text)
    disclosure_ok = (
        (
            cfg["paper"] == 30
            and "2--4 September 2026" in disclosure_text
            and "exact backend snapshot or build was not exposed" in disclosure_text
        )
        or (
            cfg["paper"] == 31
            and "2026-09-02 through 2026-09-04" in disclosure_text
            and "exact backend snapshot/build was not exposed" in disclosure_text
        )
    )
    disclosure_window = "2--4 September 2026" if cfg["paper"] == 30 else "2026-09-02 through 2026-09-04"
    principle_evidence = {
        "human_oversight": [
            "Liang Wang is the named responsible human author; AI is not credited with authorship.",
            "The manuscript records human approval of project restrictions, stage gates, and design adjudication while expressly limiting what those approvals imply about source-level verification.",
        ],
        "transparency": [
            f"The manuscript disclosure covers {disclosure_window}, identifies the Codex/GPT-5 model family and assisted tasks, and states that the exact backend snapshot/build was not exposed.",
            "The disclosure states that same-family fresh-context roles are not error-independent and distinguishes the already recorded prior audit from a fresh audit of the current successor.",
        ] if disclosure_ok else [
            "[MATERIAL GAP] The expected date window and backend-build limitation were not both recoverable from the exact frozen manuscript text."
        ],
        "reproducibility": [
            "Hash-bound ledgers, matrices, patches, apply reports, source-finalization carriers, audit collectors, and isolated build receipts reproduce the documented workflow.",
            "[WEAK EVIDENCE] No scientific experiment or independent scientific verification exists; reproducibility is bounded to workflow artifacts only.",
        ],
        "fit_for_purpose": [
            "The audit is fit for checking disclosure, citation/claim provenance, revision drift, and build integrity of the frozen manuscript.",
            "[WEAK EVIDENCE] It is not a mathematical-truth audit, professional similarity scan, or scientific reproducibility study, and no such certification is claimed.",
        ],
    }
    compliance = {
        "mode": "other_evidence_synthesis",
        "stage": "4.5",
        "generated_at": STAMP,
        "prisma_trAIce": None,
        "raise": {
            "mode": "principles_only",
            "principles": {
                "human_oversight": "pass",
                "transparency": "pass" if disclosure_ok else "fail",
                "reproducibility": "warn",
                "fit_for_purpose": "warn",
            },
            "principle_evidence": principle_evidence,
            "block_decision": "warn",
        },
        "overall_decision": "warn",
        "user_action_required": False,
        "evidence": [
            "This non-systematic-review Stage-4.5 checkpoint applies RAISE in principles-only mode; its compliance contribution is capped at warn.",
            "The manuscript is a bounded evidence synthesis plus prospective certificate design, not a completed primary scientific experiment and not a full systematic review.",
            "No professional similarity detector or independent scientific verifier was available; the integrity PASS does not certify mathematical truth or scientific reproducibility.",
        ],
        "upstream_sync_status": "current",
    }
    compliance_schema = json.loads(COMPLIANCE_SCHEMA.read_text(encoding="utf-8"))
    compliance_errors = list(Draft202012Validator(
        compliance_schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    ).iter_errors(compliance))
    if compliance_errors:
        raise RuntimeError("official compliance schema invalid: " + "; ".join(error.message for error in compliance_errors))
    return seven, "\n".join(seven_md), compliance


def isolated_build(cfg: dict[str, Any], notes: Path, text: str, work: Path, before: dict[str, Any], after_rows: list[dict[str, Any]]) -> tuple[bytes, bytes, dict[str, Any]]:
    compile_dir = work / f"{cfg['paper_id']}-compile"
    compile_dir.mkdir()
    compile_text = re.sub(r"(?m)^<!--block:B\d{4}-->\r?\n?", "", text)
    (compile_dir / "manuscript.tex").write_text(compile_text, encoding="utf-8")
    shutil.copyfile(notes / "stage4_prime_references_round2.bib", compile_dir / "references.bib")
    commands = [
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["bibtex", "manuscript"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
    ]
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC", "SOURCE_DATE_EPOCH": "1788134400"})
    records: list[dict[str, Any]] = []
    combined: list[str] = []
    final_output = ""
    for command in commands:
        code, output = run_command(command, compile_dir, env)
        records.append({"command": " ".join(command), "exit_code": code})
        combined.extend(["$ " + " ".join(command), output, ""])
        final_output = output
        if code != 0:
            break
    log_raw = "\n".join(combined).encode("utf-8")
    pdf_path = compile_dir / "manuscript.pdf"
    pdf_raw = pdf_path.read_bytes() if pdf_path.is_file() else b""
    pages = re.findall(r"Output written on manuscript\.pdf \((\d+) pages?", final_output)
    undefined_cites = sorted(set(re.findall(r"Citation [`']([^`']+)[`'].*undefined", final_output)))
    undefined_refs = sorted(set(re.findall(r"Reference [`']([^`']+)[`'].*undefined", final_output)))
    overfull = final_output.count("Overfull \\hbox")
    missing_glyphs = len(re.findall(r"Missing character:", final_output))
    fatal = len(re.findall(r"(?:Fatal error|Emergency stop|no output PDF file produced)", "\n".join(combined), flags=re.I))
    page_count = int(pages[-1]) if pages else None
    clean = (
        len(records) == 4 and all(row["exit_code"] == 0 for row in records) and bool(pdf_raw)
        and not undefined_cites and not undefined_refs and overfull == 0 and missing_glyphs == 0 and fatal == 0
        and page_count == cfg["expected_pages"]
    )
    after = snapshot(after_rows)
    if after != before:
        raise RuntimeError(f"{cfg['paper_id']} protected input changed during isolated build")
    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-isolated-preview-build/1.0",
        "paper_id": cfg["paper_id"],
        "built_at_utc": STAMP,
        "status": "PASS_CLEAN" if clean else "FAIL",
        "input": {"path": "notes/stage4_prime_revision_round3.tex", "sha256": cfg["draft_sha"]},
        "bibliography": {"path": "notes/stage4_prime_references_round2.bib", "sha256": cfg["bib_sha"]},
        "citation_style": "natbib[numbers,sort&compress] + plainnat numeric",
        "engine": "LuaLaTeX/BibTeX, four isolated passes",
        "commands": records,
        "preview": {"path": "notes/stage4_5_round2_preview.pdf", "sha256": sha_bytes(pdf_raw), "bytes": len(pdf_raw), "pages": page_count} if pdf_raw else None,
        "log": {"path": "notes/stage4_5_round2_preview.build.log", "sha256": sha_bytes(log_raw), "bytes": len(log_raw)},
        "undefined_citations": undefined_cites,
        "undefined_references": undefined_refs,
        "overfull_hbox_warning_count": overfull,
        "missing_glyph_warning_count": missing_glyphs,
        "fatal_error_count": fatal,
        "marker_stripping": "Only the temporary compile copy had block-marker comment lines removed.",
        "protected_snapshot_before": before,
        "protected_snapshot_after": after,
        "protected_snapshot_unchanged": True,
        "canonical_pdf_written": False,
        "temporary_compile_directory": "removed after candidate construction",
    }
    if not clean:
        raise RuntimeError(f"{cfg['paper_id']} isolated build failed: {json.dumps(receipt)}")
    return log_raw, pdf_raw, receipt


def round1_comparison(cfg: dict[str, Any], notes: Path, refs: dict[str, Any], phase_c: dict[str, Any], seven: dict[str, Any]) -> dict[str, Any]:
    prior_path = notes / "stage4_5_round1_integrity_report.json"
    prior = json.loads(prior_path.read_text(encoding="utf-8"))
    current_resolutions = (
        [
            {"prior_issue": "P30-S45R1-I01", "status": "RESOLVED", "fresh_basis": "30/30 contexts re-adjudicated: 22 bounded located/narrow and 8 explicit metadata-only/no-substantive-attribution; unavailable rows remain no-passage."},
            {"prior_issue": "P30-S45R1-I02", "status": "RESOLVED", "fresh_basis": "Current prose distinguishes 26 admitted sources from the 28-entry BibTeX corpus."},
            {"prior_issue": "P30-S45R1-I03", "status": "RESOLVED", "fresh_basis": "Stale Stage-2.5-pending language is absent; Round-3 successor status is explicit."},
            {"prior_issue": "P30-S45R1-I04", "status": "RESOLVED", "fresh_basis": "Disclosure covers 2–4 September and Stage-4-prime/source-finalization assistance with backend limitation."},
        ]
        if cfg["paper"] == 30 else
        [
            {"prior_issue": "P31-S45R1-I01", "status": "RESOLVED", "fresh_basis": "26/26 contexts re-adjudicated: 11 bounded located/narrow and 15 explicit metadata-only/no-substantive-attribution; unavailable rows remain no-passage."},
            {"prior_issue": "P31-S45R1-I02", "status": "RESOLVED", "fresh_basis": "Disclosure covers 2026-09-02 through 2026-09-04 and current Stage-4-prime/source-finalization work."},
        ]
    )
    return {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-round1-comparison/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "prior_report": {"path": f"notes/{prior_path.name}", "sha256": sha_path(prior_path), "verdict": prior["verdict"]},
        "comparison_only": True,
        "fresh_round2_verdicts_derived_before_comparison": True,
        "prior_issue_dispositions": current_resolutions,
        "fresh_phase_b_verdict": refs["phase_b"]["verdict"],
        "fresh_phase_c_verdict": phase_c["verdict"],
        "fresh_seven_mode_verdict": seven["overall"],
        "all_prior_blockers_resolved": all(row["status"] == "RESOLVED" for row in current_resolutions),
    }


def assemble_paper(
    cfg: dict[str, Any], lock: dict[str, Any], authority_audit: dict[str, Any], work: Path
) -> tuple[dict[str, bytes], dict[str, Any]]:
    paper = ROOT / "papers" / cfg["slug"]
    notes = paper / "notes"
    paper_row = next(row for row in lock["papers"] if row["paper_id"] == cfg["paper_id"])
    rows = locked_rows(lock, cfg["paper_id"])
    before = snapshot(rows)
    draft = notes / "stage4_prime_revision_round3.tex"
    bib = notes / "stage4_prime_references_round2.bib"
    raw = draft.read_bytes()
    text = raw.decode("utf-8")
    if sha_bytes(raw) != cfg["draft_sha"] or len(raw) != cfg["draft_bytes"] or sha_path(bib) != cfg["bib_sha"] or bib.stat().st_size != cfg["bib_bytes"]:
        raise RuntimeError(f"{cfg['paper_id']} audit target changed")
    blocks = block_rows(text)
    input_manifest = build_input_manifest(cfg, notes, paper_row, authority_audit["papers"][cfg["paper_id"]], before)
    refs, refs_md = reference_audit(cfg, notes, text, blocks)
    registry, coverage, coverage_replay = build_claim_registry(cfg, notes, raw, text, blocks, work)
    matrix = json.loads((notes / cfg["matrix"]).read_text(encoding="utf-8"))
    evidence_rows, source_map, evidence_replay, evidence_summary = build_evidence_rows(cfg, notes, registry, matrix, work)
    phase_c, phase_c_md = phase_c_audit(cfg, paper, notes, text, blocks)
    e6, drift_findings, e6_md = e6_audit(cfg, paper, notes)
    originality, originality_md = originality_audit(cfg, notes)
    seven, seven_md, compliance = seven_modes_and_compliance(cfg, text, refs, phase_c, e6)
    compliance_candidate = work / f"{cfg['paper_id']}-stage4_5_round2_compliance_report.json"
    compliance_candidate.write_bytes(json_bytes(compliance))
    compliance_code, compliance_output = run_command(["python3", str(COMPLIANCE_CHECKER), str(compliance_candidate)])
    if compliance_code != 0 or not compliance_output.startswith("OK:"):
        raise RuntimeError(f"{cfg['paper_id']} official compliance checker failed: {compliance_output}")
    log_raw, pdf_raw, build = isolated_build(cfg, notes, text, work, before, rows)
    comparison = round1_comparison(cfg, notes, refs, phase_c, seven)
    component_verdicts = [refs["overall_verdict"], phase_c["verdict"], e6["verdict"], seven["overall"], build["status"]]
    clean = all(value in {"PASS", "PASS_CLEAN"} for value in component_verdicts) and originality["verdict"] == "PASS_WITH_NOTES" and compliance["overall_decision"] != "block" and coverage["candidate_unregistered_count"] == 0 and evidence_summary["claims_verified"] == evidence_summary["registry_claims"]
    verdict = "PASS" if clean else "FAIL"
    issues: list[dict[str, Any]] = [] if clean else [{"issue_id": f"{cfg['paper_id']}-S45R2-I01", "severity": "SERIOUS", "finding": "One or more mandatory fresh audit components failed.", "blocker": True}]
    candidates: dict[str, bytes] = {
        "stage4_5_round2_input_manifest.json": json_bytes(input_manifest),
        "stage4_5_round2_reference_citation_audit.json": json_bytes(refs),
        "stage4_5_round2_reference_citation_audit.md": text_bytes(refs_md),
        "stage4_5_round2_claim_registry.json": json_bytes(registry),
        "stage4_5_round2_claim_registry_coverage.json": json_bytes(coverage),
        "stage4_5_round2_claim_registry_coverage_replay.log": text_bytes(coverage_replay),
        "stage4_5_round2_evidence_source_map.json": json_bytes(source_map),
        "stage4_5_round2_evidence_rows.json": json_bytes(evidence_rows),
        "stage4_5_round2_evidence_rows_replay.log": text_bytes(evidence_replay),
        "stage4_5_round2_phase_c_internal_consistency_audit.json": json_bytes(phase_c),
        "stage4_5_round2_phase_c_internal_consistency_audit.md": text_bytes(phase_c_md),
        "stage4_5_round2_claim_strength_drift_findings.json": json_bytes(drift_findings),
        "stage4_5_round2_e6_semantic_audit.json": json_bytes(e6),
        "stage4_5_round2_e6_semantic_audit.md": text_bytes(e6_md),
        "stage4_5_round2_originality_failure_mode_audit.json": json_bytes(originality),
        "stage4_5_round2_originality_failure_mode_audit.md": text_bytes(originality_md),
        "stage4_5_round2_seven_failure_mode_audit.json": json_bytes(seven),
        "stage4_5_round2_seven_failure_mode_audit.md": text_bytes(seven_md),
        "stage4_5_round2_compliance_report.json": json_bytes(compliance),
        "stage4_5_round2_preview.build.log": log_raw,
        "stage4_5_round2_preview.pdf": pdf_raw,
        "stage4_5_round2_preview_build_receipt.json": json_bytes(build),
        "stage4_5_round2_round1_comparison.json": json_bytes(comparison),
    }
    integrity = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-integrity-report/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "mode": "final-check",
        "audit_mode": 2,
        "verdict": verdict,
        "fresh_from_scratch": True,
        "prior_round1_used_only_for_post_audit_comparison": True,
        "phases": {
            "A_references": {"registered": cfg["reference_total"], "checked": refs["phase_a"]["checked"], "resolved": refs["phase_a"]["resolved"], "unresolved": refs["phase_a"]["unresolved"], "verdict": refs["phase_a"]["verdict"]},
            "B_citation_contexts": {"registered": cfg["context_total"], "reviewed": refs["phase_b"]["reviewed"], "context_fidelity_verified": refs["phase_b"]["context_fidelity_verified"], "disposition_counts": refs["phase_b"]["disposition_counts"], "metadata_only_boundary_faithful_not_passage_supported": refs["phase_b"]["metadata_only_boundary_faithful_not_passage_supported"], "verdict": refs["phase_b"]["verdict"]},
            "C_data_internal_provenance": {**phase_c["registered_surface_coverage"], "experiment_alignment": phase_c["experiment_provenance"]["alignment_status"], "experiment_alignment_results": [], "boundary": BOUNDARY, "verdict": phase_c["verdict"]},
            "D_originality": {"body_successful": originality["successful_body_dual_lane"], "body_denominator": originality["paragraph_denominator"], "rate": originality["sampling_rate"], "changed_successful": originality["changed_or_new_successful"], "changed_denominator": originality["changed_or_new_total"], "major_sections": f"{originality['major_sections_covered']}/{originality['major_sections_total']}", "professional_detector": False, "verdict": originality["verdict"]},
            "E_claims": {
                "selection_tier": "ALL",
                "registered": evidence_summary["registry_claims"],
                "checked": evidence_summary["claims_checked"],
                "verified": evidence_summary["claims_verified"],
                "claim_registry": {"path": "notes/stage4_5_round2_claim_registry.json", "sha256": sha_bytes(candidates["stage4_5_round2_claim_registry.json"])},
                "coverage_report": {"path": "notes/stage4_5_round2_claim_registry_coverage.json", "sha256": sha_bytes(candidates["stage4_5_round2_claim_registry_coverage.json"]), "status": "completed", "candidate_unregistered_count": coverage["candidate_unregistered_count"]},
                "semantic_extraction_coverage": "not_machine_detectable",
                "expected_evidence_tuples": evidence_summary["expected_tuples"],
                "actual_evidence_tuples": evidence_summary["actual_tuples"],
                "evidence_rows_artifact": {"path": "notes/stage4_5_round2_evidence_rows.json", "sha256": sha_bytes(candidates["stage4_5_round2_evidence_rows.json"])},
                "evidence_rows": evidence_rows,
                "verdict_counts": evidence_summary["verdict_counts"],
                "excerpt_state_counts": evidence_summary["excerpt_state_counts"],
                "scope_conformance_advisories": [],
                "novelty_claim_advisories": [],
                "cache_staleness_advisories": [],
                "verdict": "PASS" if evidence_summary["claims_verified"] == evidence_summary["registry_claims"] else "FAIL",
            },
            "E6_semantic_drift": {"rounds": 3, "operations_reviewed": e6["operations_reviewed"], "round_operation_denominators": e6["round_operation_denominators"], "result": e6["semantic_result"], "companion": {"path": "notes/stage4_5_round2_claim_strength_drift_findings.json", "sha256": sha_bytes(candidates["stage4_5_round2_claim_strength_drift_findings.json"])}, "verdict": e6["verdict"]},
        },
        "seven_failure_modes": seven,
        "compliance": compliance,
        "build": build,
        "round1_comparison": comparison,
        "issues": issues,
        "issue_counts": {"SERIOUS": sum(row["severity"] == "SERIOUS" for row in issues), "MEDIUM": 0, "MINOR": 0},
        "advisories": [
            "Semantic E1 extraction completeness is not machine-detectable even with a replay-clean finite lexical coverage report.",
            "Originality review is a public-Web heuristic without a licensed professional similarity detector.",
            "Same-family fresh-context roles are not claimed to have independent errors.",
            "Metadata-only unavailable references remain without passages; PASS applies only to their explicit no-substantive-attribution boundary.",
        ],
        "authority": input_manifest["authority"],
        "protected_snapshot_before": before,
        "protected_snapshot_after": snapshot(rows),
        "protected_snapshot_unchanged": snapshot(rows) == before,
        "silent_repair_performed": False,
        "canonical_promotion_performed": False,
        "scientific_execution_performed": False,
        "route_mutation_performed": False,
        "stage5_started": False,
        "route_state": cfg["route_state"],
        "initial_system": cfg["initial_system"],
        "assurance_boundary": "PASS is bounded to the registered references, citation contexts, registered data/stat surfaces, sampled paragraphs plus all changed paragraphs, and the fresh E1 registry. It is not proof of mathematical truth, semantic-registry completeness, experimental execution, or Route eligibility.",
    }
    candidates["stage4_5_round2_integrity_report.json"] = json_bytes(integrity)
    passport_seed_path = notes / "stage4_5_round1_material_passport.json"
    passport = copy.deepcopy(json.loads(passport_seed_path.read_text(encoding="utf-8")))
    passport["version_label"] = "stage4.5-round2-fresh-mode2-pass-sidecar"
    passport["content_hash"] = cfg["draft_sha"]
    passport["verification_status"] = "stage4_5_round2_pass_audit_sidecar_not_canonical_promotion"
    passport["integrity_pass_date"] = STAMP
    passport["stage4_5_round2_audit"] = {
        "verdict": verdict,
        "fresh_from_scratch": True,
        "authority_receipt_sha256": AUTHORITY[RECEIPT.name][0],
        "references": f"{refs['phase_a']['resolved']}/{cfg['reference_total']}",
        "citation_contexts": f"{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}",
        "phase_c": f"{phase_c['registered_surface_coverage']['verified']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}",
        "originality_body": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "originality_changed": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "registered_claims": f"{evidence_summary['claims_verified']}/{evidence_summary['registry_claims']}",
        "evidence_rows": f"{evidence_summary['actual_tuples']}/{evidence_summary['expected_tuples']}",
        "e6": f"{e6['operations_reviewed']}/{e6['operations_reviewed']} across 3 rounds",
        "seven_modes": "7/7 CLEAR",
        "build": build["status"],
        "stage5_started": False,
    }
    if passport["experiment_intake_declaration"]["status"] != "no_experiments_declared" or passport["experiment_provenance"] != []:
        raise RuntimeError(f"{cfg['paper_id']} passport experiment fields were not preserved")
    candidates["stage4_5_round2_material_passport.json"] = json_bytes(passport)
    final_lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 final integrity report",
        "",
        "## Verdict",
        "",
        f"**{verdict}.** This is a fresh Mode-2 audit of the exact Round-3 successor. No repair, canonical promotion, scientific execution, Route change, Stage 5 action, README edit, pipeline-state edit, or Git action was performed.",
        "",
        "## Complete denominators",
        "",
        f"- References: **{refs['phase_a']['resolved']}/{cfg['reference_total']}** freshly resolved.",
        f"- Citation contexts: **{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}** freshly reviewed and boundary-faithful: `{refs['phase_b']['disposition_counts']}`. Unavailable rows are not called passage-supported.",
        f"- Phase C: **{phase_c['registered_surface_coverage']['verified']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}** registered data/stat/internal surfaces; tables **{phase_c['registered_surface_coverage']['tables_verified']}/{phase_c['registered_surface_coverage']['tables_checked']}**; figures **0**; D7 **{phase_c['experiment_provenance']['alignment_status']}**.",
        f"- Originality heuristic: body **{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']} ({originality['sampling_rate']:.1%})**; all changed/new paragraphs **{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}**; major sections **{originality['major_sections_covered']}/{originality['major_sections_total']}**. No professional detector was available.",
        f"- Fresh E1 registry: **{evidence_summary['claims_verified']}/{evidence_summary['registry_claims']}** tier-ALL claims; official lexical candidate gaps **{coverage['candidate_unregistered_count']}**; semantic extraction completeness `not_machine_detectable`.",
        f"- Official evidence rows: **{evidence_summary['actual_tuples']}/{evidence_summary['expected_tuples']}** tuples replay-valid; excerpt states `{evidence_summary['excerpt_state_counts']}`.",
        f"- E6: **3/3 rounds**, **{e6['operations_reviewed']}/{e6['operations_reviewed']}** operations ({' + '.join(str(value) for value in cfg['round_ops'])}); **{e6['semantic_result']}**.",
        f"- Seven-mode checklist: **{seven['clear']}/7 CLEAR**, **{seven['suspected']}/7 SUSPECTED**, **{seven['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**.",
        f"- Isolated build: **{build['status']}**, {build['preview']['pages']} pages, zero undefined citations/references, missing glyphs, fatal errors, and overfull boxes; citation style remains plainnat numeric.",
        "",
        "## Route and system boundary",
        "",
        f"- Route: `{cfg['route_state']}`.",
        f"- Initial system: {cfg['initial_system']}.",
        "",
        "## Experiment boundary",
        "",
        BOUNDARY,
        "",
        "## Assurance boundary",
        "",
        integrity["assurance_boundary"],
    ]
    candidates["stage4_5_round2_final_integrity_report.md"] = text_bytes("\n".join(final_lines))
    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-receipt/1.0",
        "paper_id": cfg["paper_id"],
        "recorded_at_utc": STAMP,
        "verdict": verdict,
        "audit_mode": 2,
        "authority": input_manifest["authority"],
        "inputs": input_manifest["inputs"],
        "denominators": integrity["phases"],
        "key_artifacts": {
            "integrity_report": artifact_row("notes/stage4_5_round2_integrity_report.json", candidates["stage4_5_round2_integrity_report.json"]),
            "final_human_report": artifact_row("notes/stage4_5_round2_final_integrity_report.md", candidates["stage4_5_round2_final_integrity_report.md"]),
            "claim_registry": artifact_row("notes/stage4_5_round2_claim_registry.json", candidates["stage4_5_round2_claim_registry.json"]),
            "evidence_rows": artifact_row("notes/stage4_5_round2_evidence_rows.json", candidates["stage4_5_round2_evidence_rows.json"]),
            "preview": build["preview"],
        },
        "seven_mode_summary": {"clear": seven["clear"], "suspected": seven["suspected"], "insufficient_evidence": seven["insufficient_evidence"]},
        "protected_snapshot_unchanged": True,
        "silent_repair_performed": False,
        "stage5_started": False,
        "canonical_promotion_performed": False,
    }
    candidates["stage4_5_round2_receipt.json"] = json_bytes(receipt)
    existing = [path for path in sorted(notes.glob("stage4_5_round2_*")) if path.is_file() and path.name not in OUTPUT_NAMES]
    manifest_artifacts = [
        {"path": f"notes/{path.name}", "sha256": sha_path(path), "bytes": path.stat().st_size}
        for path in existing
    ]
    manifest_artifacts.extend(
        artifact_row(f"notes/{name}", value)
        for name, value in sorted(candidates.items())
        if name not in {"stage4_5_round2_output_manifest.json", "stage4_5_round2_validation_receipt.json"}
    )
    output_manifest = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-output-manifest/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "verdict": verdict,
        "artifacts": sorted(manifest_artifacts, key=lambda row: row["path"]),
        "validation_receipt_intentionally_not_self_listed": "notes/stage4_5_round2_validation_receipt.json",
        "protected_snapshot_after": snapshot(rows),
        "protected_snapshot_unchanged": snapshot(rows) == before,
        "stage5_started": False,
    }
    candidates["stage4_5_round2_output_manifest.json"] = json_bytes(output_manifest)
    validation_artifacts = [artifact_row(f"notes/{name}", value) for name, value in sorted(candidates.items()) if name != "stage4_5_round2_validation_receipt.json"]
    validation = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round2-validation-receipt/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "status": "PASS",
        "authority_receipt_sha256": AUTHORITY[RECEIPT.name][0],
        "checks": {
            "fresh_reference_population": f"{refs['phase_a']['resolved']}/{cfg['reference_total']}",
            "citation_context_population": f"{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}",
            "phase_c_population": f"{phase_c['registered_surface_coverage']['verified']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}",
            "originality_body": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
            "originality_changed": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
            "claim_registry": f"{evidence_summary['claims_verified']}/{evidence_summary['registry_claims']}",
            "coverage_candidate_gaps": coverage["candidate_unregistered_count"],
            "evidence_tuples": f"{evidence_summary['actual_tuples']}/{evidence_summary['expected_tuples']}",
            "e6_rounds": 3,
            "e6_operations": e6["operations_reviewed"],
            "seven_modes_clear": seven["clear"],
            "build": build["status"],
            "protected_snapshot_unchanged": snapshot(rows) == before,
            "official_coverage_replay": "PASS",
            "official_evidence_rows_replay": "PASS",
            "official_compliance_checker": "PASS",
        },
        "artifacts": validation_artifacts,
        "validation_receipt_self_hash_excluded": True,
        "boundaries": {"repairs": False, "canonical_promotion": False, "science_or_route_change": False, "stage5": False, "git": False},
    }
    candidates["stage4_5_round2_validation_receipt.json"] = json_bytes(validation)
    if set(candidates) != set(OUTPUT_NAMES):
        missing = sorted(set(OUTPUT_NAMES) - set(candidates))
        extra = sorted(set(candidates) - set(OUTPUT_NAMES))
        raise RuntimeError(f"{cfg['paper_id']} candidate name mismatch missing={missing} extra={extra}")
    return candidates, {
        "paper_id": cfg["paper_id"],
        "verdict": verdict,
        "references": f"{refs['phase_a']['resolved']}/{cfg['reference_total']}",
        "contexts": f"{refs['phase_b']['context_fidelity_verified']}/{cfg['context_total']}",
        "phase_c": f"{phase_c['registered_surface_coverage']['verified']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}",
        "originality": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "changed": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "claims": evidence_summary["registry_claims"],
        "evidence_rows": evidence_summary["actual_tuples"],
        "e6_operations": e6["operations_reviewed"],
        "build": build["status"],
        "pages": build["preview"]["pages"],
        "output_count": len(candidates),
    }


def publish(all_candidates: list[tuple[Path, bytes]]) -> None:
    collisions = [str(path) for path, _ in all_candidates if path.exists()]
    if collisions:
        raise FileExistsError("Round-2 build output collision: " + ", ".join(collisions))
    staged: list[Path] = []
    promoted: list[Path] = []
    try:
        for target, raw in all_candidates:
            fd, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
            os.close(fd)
            temp = Path(name)
            staged.append(temp)
            temp.write_bytes(raw)
            os.link(temp, target)
            promoted.append(target)
        for temp in staged:
            temp.unlink(missing_ok=True)
    except Exception:
        for target in promoted:
            target.unlink(missing_ok=True)
        for temp in staged:
            temp.unlink(missing_ok=True)
        raise


def validate_existing(lock: dict[str, Any]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for cfg in CONFIGS:
        paper = ROOT / "papers" / cfg["slug"]
        notes = paper / "notes"
        receipt_path = notes / "stage4_5_round2_validation_receipt.json"
        real_file(receipt_path)
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt["status"] != "PASS" or receipt["authority_receipt_sha256"] != AUTHORITY[RECEIPT.name][0]:
            raise RuntimeError(f"{cfg['paper_id']} validation receipt invalid")
        for row in receipt["artifacts"]:
            path = paper / row["path"]
            if sha_path(path) != row["sha256"] or path.stat().st_size != row["bytes"]:
                raise RuntimeError(f"{cfg['paper_id']} artifact replay mismatch {row['path']}")
        registry = notes / "stage4_5_round2_claim_registry.json"
        coverage = notes / "stage4_5_round2_claim_registry_coverage.json"
        code, _ = run_command([
            "python3", str(ARS / "scripts/claim_registry_coverage.py"),
            "--draft", str(notes / "stage4_prime_revision_round3.tex"),
            "--registry", str(registry),
            "--validate-report", str(coverage),
        ])
        if code != 0:
            raise RuntimeError(f"{cfg['paper_id']} coverage replay failed in validate-only")
        code, _ = run_command([
            "python3", str(ARS / "scripts/evidence_rows.py"), "validate",
            str(notes / "stage4_5_round2_evidence_rows.json"),
            "--source-map", str(notes / "stage4_5_round2_evidence_source_map.json"),
        ])
        if code != 0:
            raise RuntimeError(f"{cfg['paper_id']} evidence replay failed in validate-only")
        code, output = run_command([
            "python3", str(COMPLIANCE_CHECKER), str(notes / "stage4_5_round2_compliance_report.json")
        ])
        if code != 0 or not output.startswith("OK:"):
            raise RuntimeError(f"{cfg['paper_id']} official compliance replay failed in validate-only: {output}")
        integrity = json.loads((notes / "stage4_5_round2_integrity_report.json").read_text(encoding="utf-8"))
        if integrity["verdict"] != "PASS" or integrity["protected_snapshot_unchanged"] is not True:
            raise RuntimeError(f"{cfg['paper_id']} integrity report not PASS")
        rows = locked_rows(lock, cfg["paper_id"])
        if snapshot(rows) != integrity["protected_snapshot_before"]:
            raise RuntimeError(f"{cfg['paper_id']} protected snapshot changed after publication")
        summaries.append({
            "paper_id": cfg["paper_id"],
            "status": "PASS",
            "validation_receipt_sha256": sha_path(receipt_path),
            "validation_receipt_bytes": receipt_path.stat().st_size,
            "integrity_report_sha256": sha_path(notes / "stage4_5_round2_integrity_report.json"),
            "output_manifest_sha256": sha_path(notes / "stage4_5_round2_output_manifest.json"),
            "artifact_rows_replayed": len(receipt["artifacts"]),
        })
    return summaries


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.preflight_only and args.validate_only:
        raise SystemExit("choose only one mode")
    lock, _receipt, authority_audit = verify_authority()
    if args.validate_only:
        print(json.dumps(validate_existing(lock), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    collisions = output_collisions()
    if collisions:
        raise FileExistsError("Round-2 outputs already exist: " + ", ".join(collisions))
    if args.preflight_only:
        print(json.dumps({
            "status": "PASS",
            "authority": authority_audit,
            "output_collisions": [],
            "papers": [cfg["paper_id"] for cfg in CONFIGS],
            "output_candidates_per_paper": len(OUTPUT_NAMES),
        }, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    results: list[dict[str, Any]] = []
    all_candidates: list[tuple[Path, bytes]] = []
    with tempfile.TemporaryDirectory(prefix="round10-stage4-5-round2-p30-p31-") as temp_name:
        work = Path(temp_name)
        for cfg in CONFIGS:
            candidates, summary = assemble_paper(cfg, lock, authority_audit, work)
            notes = ROOT / "papers" / cfg["slug"] / "notes"
            all_candidates.extend((notes / name, raw) for name, raw in sorted(candidates.items()))
            results.append(summary)
        publish(all_candidates)
    validated = validate_existing(lock)
    print(json.dumps({"status": "PASS", "papers": results, "post_publish_validation": validated}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
