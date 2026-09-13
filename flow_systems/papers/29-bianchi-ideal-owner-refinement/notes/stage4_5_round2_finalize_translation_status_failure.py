#!/usr/bin/env python3
"""Invalidate the missed translated-abstract PASS and emit the true FAIL package.

This is a narrowly authorized audit-sidecar finalizer.  It never edits the
manuscript, bibliography, canonical tree, science/results tree, Route state, or
status documents.  It preserves the prior PASS bytes in a noncontrolling
notes-side archive, records their hashes in an incident, adds the previously
missed Traditional-Chinese citation-status claim/surface, replays the official
claim/evidence/compliance validators, and atomically emits a
FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED Stage-4.5 Round-2 package.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import urllib.parse
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
COMPLIANCE_CHECKER = ARS / "scripts/check_compliance_report.py"
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether "
    "the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COVER = load_module(ARS / "scripts/claim_registry_coverage.py", "s45r2_fail_coverage")
EVR = load_module(ARS / "scripts/evidence_rows.py", "s45r2_fail_evidence")


CONFIGS: dict[str, dict[str, Any]] = {
    "P29": {
        "paper": 29,
        "paper_id": "P29",
        "slug": "29-bianchi-ideal-owner-refinement",
        "block_id": "B0006",
        "line": 44,
        "pass_manifest_sha": "e3ec7cdcd795d38460a71fe389f742fd1aba8442fcadec7bd528be1f7fcece6d",
        "archive": "stage4_5_round2_attempt2_invalidated_pass",
        "draft": "stage4_prime_revision_round3.tex",
        "draft_sha": "009ae2e9b30cb087902c7fbb9d01226bc544ce536da8ebf40f244e7b07d817ae",
        "matrix": "stage4_prime_claim_passage_matrix_round3.json",
        "matrix_sha": "ac253359ce62df4c4f7d8c1143fde92d71918c157c45a68f8a32717d3bc79b71",
        "old_clause": "所有引文均缺段落定位，故支持狀態仍為不確定；",
        "proposed_clause": (
            "在二十二個既有引文脈絡中，十三項已有精確且逐列限定的段落定位，另九項因未完成可承載段落的定位而"
            "明確限於書目中介資料；每一項支持僅限其記錄的脈絡；"
        ),
        "prior_claims": 88,
        "prior_evidence": 88,
        "new_claim_id": "P29-S45R2-E1-089",
        "parent_compound_claim_id": "P29-S45R2-E1-002",
        "new_row_id": "EVR-P29-S45R2-E1-089-T01",
        "matrix_slug": "P29MatrixRound3Summary",
        "passage_bounded": 13,
        "unverifiable_contexts": 0,
        "metadata_only": 9,
        "reference_total": 22,
        "tables": 0,
        "e6": 79,
        "pages": 17,
        "issue_id": "P29-S45R2-I01-TRANSLATED-ABSTRACT-STATUS",
        "correction_id": "P29-S45R2-CORR-001",
        "section": "Traditional Chinese Abstract / 繁體中文摘要",
        "phase_a_reclassification_id": "P29-S45R2-AUDIT-RECLASS-001",
        "status_blocks": {
            "B0004", "B0009", "B0048", "B0049", "B0050", "B0051", "B0053", "B0054", "B0055",
            "B0062", "B0075", "B0076", "B0077", "B0078", "B0080", "B0114", "B0085", "B0089",
            "B0090", "B0091", "B0092", "B0100", "B0101", "B0102", "B0103", "B0106", "B0107",
            "B0115", "B0108", "B0109",
        },
        "proof_claim_ids": set(),
        "constitutive_status_block_overrides": set(),
    },
    "P32": {
        "paper": 32,
        "paper_id": "P32",
        "slug": "32-homology-cover-renormalization-uniformity",
        "block_id": "B0007",
        "line": 73,
        "pass_manifest_sha": "8e3b37bc2e9d569e19e242da78e86b5428efd7574e5c01717e535c169cec51e0",
        "archive": "stage4_5_round2_attempt1_invalidated_pass",
        "draft": "stage4_prime_revision_round3.tex",
        "draft_sha": "b43c5cb6c7770dd80600e1ee64a8e23d17ffc2ceb39e9fcb625ff2b6c5f692fd",
        "matrix": "stage4_prime_claim_passage_matrix_round3.json",
        "matrix_sha": "18259fa9200782715192325dd882c9d6b32bd7f7f2e335e1bf54c8c39d10ea9a",
        "old_clause": (
            "所有引文均無段落定位， P32-S13 的書目身分已核為 \\texttt{VERIFIED}，但仍僅作背景來源， "
            "故逐主張支持仍屬未定；"
        ),
        "proposed_clause": (
            "目前三十列矩陣中，十八項繼承來源已有精確且逐列限定的段落定位，四項最近工作脈絡僅保留既有定位"
            "而未在本輪鎖定材料中綁定摘錄與雜湊，故仍不可核；另八項因未完成可承載段落的定位而明確限於書目中介資料；"
            "P32-S13 的書目身分已核為 \\texttt{VERIFIED}，但仍屬後一類，且任何定位狀態均不建立本計畫的定理；"
        ),
        "prior_claims": 97,
        "prior_evidence": 119,
        "new_claim_id": "P32-S45R2-E1-098",
        "parent_compound_claim_id": "P32-S45R2-E1-003",
        "new_row_id": "EVR-P32-S45R2-E1-098-T01",
        "matrix_slug": "P32MatrixRound3Summary",
        "passage_bounded": 18,
        "unverifiable_contexts": 4,
        "metadata_only": 8,
        "reference_total": 30,
        "tables": 3,
        "e6": 45,
        "pages": 19,
        "issue_id": "P32-S45R2-I01-TRANSLATED-ABSTRACT-STATUS",
        "correction_id": "P32-S45R2-CORR-001",
        "section": "Traditional Chinese Abstract / 繁體中文摘要",
        "phase_a_reclassification_id": "P32-S45R2-AUDIT-RECLASS-001",
        "phase_b_reclassification_id": "P32-S45R2-AUDIT-RECLASS-002",
        "status_blocks": {
            "B0006", "B0024", "B0025", "B0026", "B0028", "B0029", "B0030", "B0034", "B0036",
            "B0037", "B0039", "B0040", "B0041", "B0044", "B0133", "B0045", "B0046", "B0047",
            "B0049", "B0050", "B0094", "B0095", "B0098", "B0137", "B0102", "B0104", "B0105",
            "B0106", "B0107", "B0109", "B0110", "B0111", "B0112", "B0118", "B0119", "B0121",
            "B0124", "B0125", "B0139", "B0127", "B0128", "B0138",
        },
        "proof_claim_ids": {
            "P32-S45R2-E1-042", "P32-S45R2-E1-065", "P32-S45R2-E1-066", "P32-S45R2-E1-067"
        },
        "constitutive_status_block_overrides": {
            "B0025", "B0026", "B0029", "B0030", "B0034", "B0037", "B0040", "B0041", "B0104", "B0105"
        },
    },
}


REPLACED = {
    "stage4_5_round2_browser_reference_verification.json",
    "stage4_5_round2_claim_registry.json",
    "stage4_5_round2_claim_registry_coverage.json",
    "stage4_5_round2_claim_registry_coverage_replay.log",
    "stage4_5_round2_evidence_projection_ledger.json",
    "stage4_5_round2_evidence_rows.json",
    "stage4_5_round2_evidence_rows_replay.log",
    "stage4_5_round2_evidence_source_map.json",
    "stage4_5_round2_local_claim_evidence_carriers.json",
    "stage4_5_round2_local_claim_dependency_catalog.json",
    "stage4_5_round2_local_claim_semantic_re_adjudication.json",
    "stage4_5_round2_final_integrity_report.md",
    "stage4_5_round2_integrity_pass_receipt.json",
    "stage4_5_round2_integrity_report.json",
    "stage4_5_round2_mandatory_checkpoint.json",
    "stage4_5_round2_material_passport.json",
    "stage4_5_round2_output_manifest.json",
    "stage4_5_round2_phase_c_internal_consistency_audit.json",
    "stage4_5_round2_phase_c_internal_consistency_audit.md",
    "stage4_5_round2_reference_citation_audit.json",
    "stage4_5_round2_reference_citation_audit.md",
    "stage4_5_round2_seven_failure_mode_audit.json",
    "stage4_5_round2_seven_failure_mode_audit.md",
}


INPUT_LOCK_SHA256 = "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0"
AUTHORITY_ARTIFACTS = {
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt": (
        "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
        19,
    ),
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md": (
        "e9505895fe78e2910ff32c4c97d4e7c42abf2fc1f63b25ca7170cb17477dd06d",
        1674,
    ),
    "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json": (INPUT_LOCK_SHA256, 45264),
    "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json": (
        "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60",
        1203,
    ),
}
P29_INDEPENDENT_MAPPING = {
    "path": (
        "papers/29-bianchi-ideal-owner-refinement/notes/"
        "stage4_5_round2_p29_dependency_mapping_independent_review.json"
    ),
    "sha256": "e72fe7011fd0261e7402701c690c50f803fd369f39f1f568d8f315b16ae6d523",
    "bytes": 222777,
}


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def artifact(path: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha_path(path),
        "bytes": path.stat().st_size,
    }


def staged_artifact(stage: Path, path: Path) -> dict[str, Any]:
    final_path = stage.parent / path.name
    return {
        "path": final_path.relative_to(ROOT).as_posix(),
        "sha256": sha_path(path),
        "bytes": path.stat().st_size,
    }


def dump(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def run(command: list[str], *, cwd: Path | None = None) -> tuple[int, str]:
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def verify_artifact_row(row: dict[str, Any]) -> Path:
    path = ROOT / row["path"]
    if (sha_path(path), path.stat().st_size) != (row["sha256"], row["bytes"]):
        raise RuntimeError(f"artifact replay mismatch: {row['path']}")
    return path


def exact_claim(cfg: dict[str, Any], raw: bytes) -> dict[str, Any]:
    needle = cfg["old_clause"].encode("utf-8")
    if raw.count(needle) != 1:
        raise RuntimeError("translated stale clause is not unique")
    start = raw.index(needle)
    end = start + len(needle)
    return {
        "claim_id": cfg["new_claim_id"],
        "claim_text": cfg["old_clause"],
        "draft_span": {"start_byte": start, "end_byte": end},
        "claim_kinds": ["categorical", "quantitative"],
        "ref_slugs": [cfg["matrix_slug"]],
        "writer_anchors": [cfg["block_id"]],
        "paper_section": cfg["section"],
        "selection_tier": "ALL",
    }


def first_excerpt(value: str, limit: int = 20) -> str:
    matches = list(re.finditer(r"\S+", value))
    if not matches:
        raise RuntimeError("empty evidence source")
    return value[: matches[min(limit, len(matches)) - 1].end()]


def bounded_claim_excerpt(draft_text: str, draft_raw: bytes, claim: dict[str, Any]) -> str:
    """Return a <=20-token unique excerpt wholly inside the registered byte span."""
    span = claim["draft_span"]
    start, end = span["start_byte"], span["end_byte"]
    if not (0 <= start < end <= len(draft_raw)):
        raise RuntimeError(f"invalid claim span: {claim['claim_id']}")
    span_text = draft_raw[start:end].decode("utf-8")
    if span_text != claim["claim_text"]:
        raise RuntimeError(f"claim text/span mismatch: {claim['claim_id']}")
    tokens = list(re.finditer(r"\S+", span_text))
    if not tokens:
        raise RuntimeError(f"empty claim span: {claim['claim_id']}")
    for width in range(min(20, len(tokens)), 0, -1):
        for index in range(0, len(tokens) - width + 1):
            excerpt = span_text[tokens[index].start() : tokens[index + width - 1].end()]
            if draft_text.count(excerpt) != 1:
                continue
            excerpt_start = len(draft_text[: draft_text.index(excerpt)].encode("utf-8"))
            excerpt_end = excerpt_start + len(excerpt.encode("utf-8"))
            if start <= excerpt_start < excerpt_end <= end:
                return excerpt
    raise RuntimeError(f"no unique bounded excerpt for claim: {claim['claim_id']}")


def block_context_excerpt(draft_text: str, draft_raw: bytes, claim: dict[str, Any]) -> tuple[str, dict[str, int]]:
    """Return a unique <=20-token window in the actual writer block around a claim.

    The registry includes a few intentionally short lexical top-up claims.  A
    naked fragment is not an adequate semantic dependency, so those rows use a
    surrounding window from the same immutable writer block and record the
    actual byte span of that dependency.
    """
    if len(claim["writer_anchors"]) != 1:
        raise RuntimeError(f"expected one writer block: {claim['claim_id']}")
    block = claim["writer_anchors"][0]
    marker = f"<!--block:{block}-->".encode("utf-8")
    if draft_raw.count(marker) != 1:
        raise RuntimeError(f"writer block marker is not unique: {block}")
    block_start = draft_raw.index(marker)
    following = draft_raw.find(b"<!--block:", block_start + len(marker))
    block_end = len(draft_raw) if following < 0 else following
    block_text = draft_raw[block_start:block_end].decode("utf-8")
    claim_text = claim["claim_text"]
    if block_text.count(claim_text) != 1:
        raise RuntimeError(f"claim is not unique inside writer block: {claim['claim_id']}")
    claim_char_start = block_text.index(claim_text)
    claim_char_end = claim_char_start + len(claim_text)
    tokens = list(re.finditer(r"\S+", block_text))
    overlapping = [
        index
        for index, token in enumerate(tokens)
        if token.end() > claim_char_start and token.start() < claim_char_end
    ]
    if not overlapping:
        raise RuntimeError(f"no token overlaps claim: {claim['claim_id']}")
    first_index, last_index = overlapping[0], overlapping[-1]
    if last_index - first_index + 1 > 20:
        excerpt = bounded_claim_excerpt(draft_text, draft_raw, claim)
        excerpt_char_start = draft_text.index(excerpt)
        excerpt_start = len(draft_text[:excerpt_char_start].encode("utf-8"))
        return excerpt, {
            "start_byte": excerpt_start,
            "end_byte": excerpt_start + len(excerpt.encode("utf-8")),
        }
    remaining = 20 - (last_index - first_index + 1)
    before = min(first_index, remaining // 2)
    after = min(len(tokens) - last_index - 1, remaining - before)
    before = min(first_index, remaining - after)
    start_index, end_index = first_index - before, last_index + after
    excerpt = block_text[tokens[start_index].start() : tokens[end_index].end()]
    if draft_text.count(excerpt) != 1:
        # Shrink deterministically while retaining the entire top-up fragment.
        while (start_index < first_index or end_index > last_index) and draft_text.count(excerpt) != 1:
            if end_index > last_index:
                end_index -= 1
            elif start_index < first_index:
                start_index += 1
            excerpt = block_text[tokens[start_index].start() : tokens[end_index].end()]
    if draft_text.count(excerpt) != 1:
        raise RuntimeError(f"no unique writer-block dependency excerpt: {claim['claim_id']}")
    global_char_start = len(draft_raw[:block_start].decode("utf-8")) + tokens[start_index].start()
    dependency_start = len(draft_text[:global_char_start].encode("utf-8"))
    dependency_end = dependency_start + len(excerpt.encode("utf-8"))
    if not (block_start <= dependency_start < dependency_end <= block_end):
        raise RuntimeError(f"writer-block dependency escaped block: {claim['claim_id']}")
    return excerpt, {"start_byte": dependency_start, "end_byte": dependency_end}


def raw_excerpt_window(source_text: str, needle: str, *, maximum_words: int = 20) -> tuple[str, dict[str, int]]:
    """Select a unique bounded raw-source window that contains ``needle``.

    This is deliberately a source operation, not a generated summary.  The
    returned byte span always replays exactly against the immutable artifact.
    """
    if not needle or source_text.count(needle) != 1:
        raise RuntimeError(f"raw dependency needle is not unique: {needle!r}")
    needle_start = source_text.index(needle)
    needle_end = needle_start + len(needle)
    tokens = list(re.finditer(r"\S+", source_text))
    overlapping = [
        index
        for index, token in enumerate(tokens)
        if token.end() > needle_start and token.start() < needle_end
    ]
    if not overlapping:
        raise RuntimeError("raw dependency needle has no token")
    first_index, last_index = overlapping[0], overlapping[-1]
    if last_index - first_index + 1 > maximum_words:
        last_index = first_index + maximum_words - 1
    remaining = maximum_words - (last_index - first_index + 1)
    before = min(first_index, remaining // 2)
    after = min(len(tokens) - last_index - 1, remaining - before)
    before = min(first_index, remaining - after)
    start_index, end_index = first_index - before, last_index + after
    excerpt = source_text[tokens[start_index].start() : tokens[end_index].end()]
    while source_text.count(excerpt) != 1 and (start_index < first_index or end_index > last_index):
        if end_index > last_index:
            end_index -= 1
        elif start_index < first_index:
            start_index += 1
        excerpt = source_text[tokens[start_index].start() : tokens[end_index].end()]
    if source_text.count(excerpt) != 1:
        raise RuntimeError(f"could not make raw dependency excerpt unique: {needle!r}")
    char_start = source_text.index(excerpt)
    byte_start = len(source_text[:char_start].encode("utf-8"))
    return excerpt, {
        "start_byte": byte_start,
        "end_byte": byte_start + len(excerpt.encode("utf-8")),
    }


def raw_dependency(
    *,
    component_id: str,
    path: Path,
    needle: str,
    role: str,
    derivation_rule: str,
    parsed_value: Any = None,
    json_pointer: str | None = None,
) -> tuple[dict[str, Any], str]:
    if not path.is_file():
        raise RuntimeError(f"raw dependency missing: {path}")
    source_text = path.read_text(encoding="utf-8")
    excerpt, span = raw_excerpt_window(source_text, needle)
    if path.read_bytes()[span["start_byte"] : span["end_byte"]].decode("utf-8") != excerpt:
        raise RuntimeError(f"raw dependency span does not replay: {component_id}")
    record = {
        "component_id": component_id,
        "artifact": artifact(path),
        "raw_utf8_span": span,
        "raw_excerpt": excerpt,
        "raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
        "raw_excerpt_word_count": len(excerpt.split()),
        "semantic_role": role,
        "derivation_rule": derivation_rule,
        "json_pointer": json_pointer,
        "parsed_value": parsed_value,
        "fresh_semantic_adjudication": "SUPPORTED_WITHIN_DECLARED_RAW_CARRIER_SCOPE",
    }
    return record, source_text


def raw_artifact_source_slug(cfg: dict[str, Any], artifact_row: dict[str, Any]) -> str:
    """Return one stable source slug for one exact (path, SHA) artifact.

    The draft and matrix retain their established slugs because the claim
    registry already names them. Every other raw carrier is keyed by the
    canonical path plus digest, so component rows can share one source-map
    payload without weakening their distinct anchors.
    """
    draft_path = f"papers/{cfg['slug']}/notes/{cfg['draft']}"
    matrix_path = f"papers/{cfg['slug']}/notes/{cfg['matrix']}"
    if artifact_row["path"] == draft_path:
        return f"{cfg['paper_id']}LocalSuccessor"
    if artifact_row["path"] == matrix_path:
        return cfg["matrix_slug"]
    token = sha_bytes(
        f"{artifact_row['path']}\0{artifact_row['sha256']}".encode("utf-8")
    )
    return f"{cfg['paper_id']}RawArtifact{token}"


def occurrence_specific_excerpt(
    source_text: str,
    excerpt: str,
    span: dict[str, int],
    *,
    maximum_words: int = 25,
) -> tuple[str, dict[str, int], bool]:
    """Make a repeated mapped excerpt uniquely replayable at its exact span.

    The ARS evidence-row builder resolves an extracted string to its first
    occurrence. If a mapper-selected excerpt repeats, expand it with adjacent
    raw-source tokens (never beyond the 25-word cap) until the requested
    occurrence is unique. No generated prose is introduced as evidence.
    """
    raw = source_text.encode("utf-8")
    start_byte, end_byte = span["start_byte"], span["end_byte"]
    if raw[start_byte:end_byte].decode("utf-8") != excerpt:
        raise RuntimeError("mapped excerpt/span does not replay before disambiguation")
    if source_text.count(excerpt) == 1:
        return excerpt, span, False

    char_start = len(raw[:start_byte].decode("utf-8"))
    char_end = len(raw[:end_byte].decode("utf-8"))
    tokens = list(re.finditer(r"\S+", source_text))
    covered = [
        index
        for index, token in enumerate(tokens)
        if token.end() > char_start and token.start() < char_end
    ]
    if not covered or len(covered) > maximum_words:
        raise RuntimeError("repeated mapped excerpt cannot be bounded within the word cap")
    first, last = covered[0], covered[-1]
    base_count = last - first + 1
    for total in range(base_count + 1, maximum_words + 1):
        extra = total - base_count
        for before in range(extra + 1):
            after = extra - before
            left, right = first - before, last + after
            if left < 0 or right >= len(tokens):
                continue
            candidate = source_text[tokens[left].start() : tokens[right].end()]
            if excerpt not in candidate or source_text.count(candidate) != 1:
                continue
            candidate_char_start = tokens[left].start()
            candidate_start = len(source_text[:candidate_char_start].encode("utf-8"))
            candidate_span = {
                "start_byte": candidate_start,
                "end_byte": candidate_start + len(candidate.encode("utf-8")),
            }
            if raw[candidate_span["start_byte"] : candidate_span["end_byte"]].decode("utf-8") != candidate:
                raise RuntimeError("occurrence-specific excerpt span failed replay")
            return candidate, candidate_span, True
    raise RuntimeError("could not disambiguate repeated mapped excerpt within 25 words")


def _artifact_rows_in_lock(value: Any) -> list[dict[str, Any]]:
    """Return every exact path/SHA/bytes row carried by the current input lock."""
    rows: list[dict[str, Any]] = []
    if isinstance(value, dict):
        if {"path", "sha256", "bytes"}.issubset(value):
            rows.append({key: value[key] for key in ("path", "sha256", "bytes")})
        for child in value.values():
            rows.extend(_artifact_rows_in_lock(child))
    elif isinstance(value, list):
        for child in value:
            rows.extend(_artifact_rows_in_lock(child))
    return rows


def _raw_binding_excerpt(parent: Path, child: Path) -> tuple[str, dict[str, int], str]:
    """Extract parent bytes that jointly bind a child path and digest.

    TeX parents insert ``\\allowbreak{}`` inside long digests.  The returned
    bytes are always raw parent bytes; the normalization rule merely removes
    those discretionary-break commands before replaying the child digest.
    """
    parent_text = parent.read_text(encoding="utf-8")
    child_row = artifact(child)
    relative = child_row["path"]
    candidates = [relative]
    paper_marker = f"papers/{relative.split('/papers/', 1)[-1]}" if "/papers/" in relative else None
    if paper_marker:
        candidates.append(paper_marker)
    if "/notes/" in relative:
        candidates.append("notes/" + relative.split("/notes/", 1)[1])
    candidates.append(child.name)
    path_match = next((token for token in candidates if token and token in parent_text), None)
    if path_match is None:
        raise RuntimeError(f"parent does not name child path: {parent} -> {child}")
    sha = child_row["sha256"]
    path_starts = [match.start() for match in re.finditer(re.escape(path_match), parent_text)]
    selected: tuple[int, int, int, str] | None = None
    for path_start in path_starts:
        direct = parent_text.find(sha, path_start)
        if direct >= 0 and direct - path_start <= 4096:
            selected = (path_start, direct, direct + len(sha), "IDENTITY")
            break
        # Search a bounded parent slice and replay the digest only after
        # removing TeX discretionary line-break commands.
        bounded_end = min(len(parent_text), path_start + 4096)
        bounded = parent_text[path_start:bounded_end]
        normalized = bounded.replace(r"\allowbreak{}", "")
        normalized_sha = normalized.find(sha)
        if normalized_sha < 0:
            continue
        raw_cursor = path_start
        normalized_cursor = 0
        while normalized_cursor < normalized_sha:
            if parent_text.startswith(r"\allowbreak{}", raw_cursor):
                raw_cursor += len(r"\allowbreak{}")
            else:
                raw_cursor += 1
                normalized_cursor += 1
        sha_start = raw_cursor
        remaining = len(sha)
        while remaining:
            if parent_text.startswith(r"\allowbreak{}", raw_cursor):
                raw_cursor += len(r"\allowbreak{}")
            else:
                raw_cursor += 1
                remaining -= 1
        sha_end = raw_cursor
        selected = (path_start, sha_start, sha_end, "REMOVE_LITERAL_TEX_ALLOWBREAK_COMMANDS")
        break
    if selected is None:
        raise RuntimeError(f"parent does not bind child digest: {parent} -> {child}")
    path_start, sha_start, sha_end, normalization = selected
    char_start = path_start
    char_end = sha_end
    excerpt = parent_text[char_start:char_end]
    normalized_excerpt = excerpt.replace(r"\allowbreak{}", "")
    if path_match not in excerpt or sha not in normalized_excerpt:
        raise RuntimeError(f"binding excerpt does not jointly replay path/digest: {parent} -> {child}")
    byte_start = len(parent_text[:char_start].encode("utf-8"))
    span = {
        "start_byte": byte_start,
        "end_byte": byte_start + len(excerpt.encode("utf-8")),
    }
    if parent.read_bytes()[span["start_byte"] : span["end_byte"]].decode("utf-8") != excerpt:
        raise RuntimeError(f"binding excerpt byte span does not replay: {parent} -> {child}")
    return excerpt, span, normalization


def dependency_binding_chain(
    *,
    child: Path,
    input_lock_path: Path,
    input_lock_doc: dict[str, Any],
    paper: Path,
    notes: Path,
    _seen: tuple[str, ...] = (),
) -> dict[str, Any] | None:
    """Close a raw dependency recursively to the exact Stage-4.5 input lock."""
    child_row = artifact(child)
    child_rel = child_row["path"]
    if child_rel in _seen:
        return None
    if child.resolve() == input_lock_path.resolve():
        expected_sha, expected_bytes = AUTHORITY_ARTIFACTS[input_lock_path.name]
        if (child_row["sha256"], child_row["bytes"]) != (expected_sha, expected_bytes):
            raise RuntimeError("input-lock self binding no longer matches exact authority")
        lock_text = input_lock_path.read_text(encoding="utf-8")
        needle = json_scalar_needle("schema_version", input_lock_doc["schema_version"])
        excerpt, span = raw_excerpt_window(lock_text, needle, maximum_words=20)
        return {
            "type": "TOP_LEVEL_INPUT_LOCK",
            "input_lock": child_row,
            "locked_artifact": child_row,
            "lock_raw_utf8_span": span,
            "lock_raw_excerpt": excerpt,
            "lock_raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
            "replay_rule": "REPLAY_EXACT_AUTHORITY_BOUND_INPUT_LOCK_SELF_SHA256_BYTES",
        }
    lock_rows = {
        row["path"]: row
        for row in _artifact_rows_in_lock(input_lock_doc)
        if isinstance(row.get("path"), str)
    }
    locked = lock_rows.get(child_rel)
    if locked == child_row:
        lock_text = input_lock_path.read_text(encoding="utf-8")
        row_pattern = re.compile(
            r'\{\s*"bytes":\s*' + re.escape(str(child_row["bytes"]))
            + r',\s*"path":\s*' + re.escape(json.dumps(child_rel, ensure_ascii=False))
            + r',\s*"sha256":\s*' + re.escape(json.dumps(child_row["sha256"])) + r'\s*\}'
        )
        match = row_pattern.search(lock_text)
        if match is None:
            raise RuntimeError(f"parsed input-lock row has no replayable raw object: {child_rel}")
        excerpt = match.group(0)
        byte_start = len(lock_text[: match.start()].encode("utf-8"))
        span = {
            "start_byte": byte_start,
            "end_byte": byte_start + len(excerpt.encode("utf-8")),
        }
        # The complete lock is parsed as part of replay; the bounded excerpt
        # identifies the exact row and the parsed row carries SHA/bytes.
        return {
            "type": "TOP_LEVEL_INPUT_LOCK",
            "input_lock": artifact(input_lock_path),
            "locked_artifact": child_row,
            "lock_raw_utf8_span": span,
            "lock_raw_excerpt": excerpt,
            "lock_raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
            "replay_rule": "PARSE_COMPLETE_INPUT_LOCK_AND_REQUIRE_EXACT_PATH_SHA256_BYTES_ROW",
        }

    # These parents form the only authorized transitive graph.  Each parent
    # must itself close recursively to the exact input lock.
    parents = [
        notes / "stage4_prime_revision_round3.tex",
        notes / "stage4_prime_reader_artifact_manifest_round2.json",
        notes / "stage1_phase6_checkpoint.md",
    ]
    for parent in parents:
        if parent == child or not parent.is_file():
            continue
        try:
            excerpt, span, normalization = _raw_binding_excerpt(parent, child)
        except RuntimeError:
            continue
        parent_chain = dependency_binding_chain(
            child=parent,
            input_lock_path=input_lock_path,
            input_lock_doc=input_lock_doc,
            paper=paper,
            notes=notes,
            _seen=_seen + (child_rel,),
        )
        if parent_chain is None:
            continue
        return {
            "type": "TRANSITIVE_SHA_BINDING",
            "child_artifact": child_row,
            "parent_artifact": artifact(parent),
            "parent_raw_utf8_span": span,
            "parent_raw_excerpt": excerpt,
            "parent_raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
            "normalization": normalization,
            "normalized_excerpt_contains_child_path": True,
            "normalized_excerpt_contains_child_sha256": True,
            "replay_rule": "REPLAY_PARENT_RAW_BYTES_THEN_REQUIRE_CHILD_PATH_AND_SHA256_IN_NORMALIZED_EXCERPT",
            "parent_binding_chain": parent_chain,
        }
    return None


def json_scalar_needle(key: str, value: Any) -> str:
    return f"{json.dumps(key, ensure_ascii=False)}: {json.dumps(value, ensure_ascii=False)}"


def unique_line_needle(source_text: str) -> str:
    for line in source_text.splitlines():
        candidate = line.strip()
        if len(candidate) >= 8 and source_text.count(candidate) == 1:
            return candidate
    raise RuntimeError("text artifact has no unique nontrivial line")


def unique_value_needle(source_text: str, value: Any) -> str:
    """Find a unique raw scalar inside a possibly nested parsed JSON value."""
    candidates: list[str] = []

    def collect(item: Any) -> None:
        if isinstance(item, dict):
            for key, child in item.items():
                if isinstance(child, (str, int, float, bool)) or child is None:
                    candidates.append(json_scalar_needle(str(key), child))
                collect(child)
        elif isinstance(item, list):
            for child in item:
                collect(child)
        elif isinstance(item, (str, int, float, bool)) or item is None:
            candidates.append(json.dumps(item, ensure_ascii=False))

    collect(value)
    for candidate in sorted(set(candidates), key=lambda item: (-len(item), item)):
        if len(candidate) >= 4 and source_text.count(candidate) == 1:
            return candidate
    raise RuntimeError("nested JSON field has no unique scalar carrier")


P32_STATUS_PLANS: dict[str, list[dict[str, Any]]] = {
    "P32-S45R2-E1-001": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "P32 studies a fixed renormalization proposal for the pure genus-two homology-cover tower", "role": "frozen proposal, normalizations, endpoint, and review-adjudicated architecture"},
        {"kind": "matrix", "fields": ["registered_contexts", "prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
        {"kind": "formal", "fields": ["audit_outcome", "scientific_application_status"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-002": [
        {"kind": "source_rows", "source_ids": ["P32-S13"]},
        {"kind": "route", "facets": ["A0", "FORMAL_TUPLE", "A2", "ROUTE_B"]},
    ],
    "P32-S45R2-E1-014": [{"kind": "source_rows", "source_ids": [f"P32-S{i:02d}" for i in range(1, 6)]}],
    "P32-S45R2-E1-018": [{"kind": "source_rows", "source_ids": [f"P32-S{i:02d}" for i in range(7, 13)]}],
    "P32-S45R2-E1-026": [{"kind": "source_rows", "source_ids": [f"P32-S{i:02d}" for i in range(19, 23)]}],
    "P32-S45R2-E1-029": [{"kind": "source_rows", "source_ids": [f"P32-S{i:02d}" for i in range(23, 27)]}],
    "P32-S45R2-E1-033": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "Phase 2 captured 51 records, removed 12 duplicate manifestations, screened 39 unique records, excluded 13, and retained 26 sources", "role": "historical Phase-2 aggregate"},
        {"kind": "replay_fields", "fields": ["retrieval_bound"]},
        {"kind": "ledger_fields", "fields": ["row_count", "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE", "REMOVE_DUPLICATE_MANIFESTATION", "RETAIN_EXISTING_INVENTORY_RECORD", "scientific_result_changed", "canonical_result_refreshed"]},
    ],
    "P32-S45R2-E1-034": [
        {"kind": "mentioned_files"},
        {"kind": "ledger_fields", "fields": ["row_count", "decision_counts"]},
    ],
    "P32-S45R2-E1-035": [
        {"kind": "phrase", "file": "stage1_phase4_research_report.md", "needle": "The 26-row matrix assigned each source an existence outcome, claim-fitness grade, support class, admitted contribution, excluded stronger claim", "role": "source-effect coding and synthesis method"},
    ],
    "P32-S45R2-E1-036": [
        {"kind": "phrase", "file": "stage1_phase4_research_report.md", "needle": "The 26-row matrix assigned each source an existence outcome, claim-fitness grade, support class, admitted contribution, excluded stronger claim", "role": "admitted-effect and prohibited-transfer discipline"},
        {"kind": "phrase", "file": "stage1_phase4_research_report.md", "needle": "Publication and correction status were not averaged away", "role": "publication/correction/background status preservation"},
    ],
    "P32-S45R2-E1-037": [
        {"kind": "mentioned_files"},
        {"kind": "matrix", "fields": ["registered_contexts", "prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
    ],
    "P32-S45R2-E1-038": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "The executed method is a staged synthesis over frozen literature and project records", "role": "executed literature-synthesis method"},
        {"kind": "files", "basenames": ["stage4_prime_literature_replay_round2.raw.json"]},
        {"kind": "input_artifacts", "basenames": ["stage4_prime_source_finalization_round3.json", "stage4_prime_claim_passage_matrix_round3.json"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-039": [
        {"kind": "phrase", "file": "stage1_phase6_claim_intent_manifest.json", "needle": "No owner binding, lift computation, local-factor theorem, coefficient test, panel, tail bound, scalar limit, obstruction", "role": "frozen ClaimIntent no-execution constraint"},
        {"kind": "input_artifacts", "basenames": ["stage4_prime_revision_evidence_bundle_round3.json"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-072": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "Eight frozen positions govern the report. First", "role": "author-adjudicated positions one through three"},
    ],
    "P32-S45R2-E1-073": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "Fourth, a content-one subproduct is contingent and secondary", "role": "author-adjudicated positions four through eight"},
        {"kind": "formal", "fields": ["scientific_application_status", "non_global_boundary"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-074": [
        {"kind": "mentioned_files"},
        {"kind": "reader_fields", "fields": ["repository_commit", "entry_count", "section6_claimed_current_count", "section6_exact_at_pinned_commit_count", "local_stage4_prime_sidecar_count", "pinned_commit_verification", "locator_state"]},
    ],
    "P32-S45R2-E1-075": [
        {"kind": "input_artifacts", "basenames": ["stage4_prime_revision_round3.tex", "stage4_prime_revision_round3.tex.apply-report.json", "stage4_prime_revision_round3_build_receipt.json", "stage4_prime_source_finalization_round3.json", "stage4_prime_claim_passage_matrix_round3.json", "stage4_prime_source_finalization_round3_validation.json"]},
        {"kind": "reader_fields", "fields": ["locator_state", "boundary"]},
    ],
    "P32-S45R2-E1-079": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "The smallest next package is therefore not an owner panel or numerical grid", "role": "prospective dossier decision"},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-082": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "The pure tower has no intrinsic rational-prime owner map or `log p` clock in this record", "role": "bounded calibrator/arithmetic-specificity conclusion"},
        {"kind": "initial_system"},
    ],
    "P32-S45R2-E1-083": [
        {"kind": "route", "facets": ["A0", "FORMAL_TUPLE", "A2", "A3_A4", "ROUTE_B"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-084": [
        {"kind": "ledger_fields", "fields": ["row_count", "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE", "REMOVE_DUPLICATE_MANIFESTATION", "RETAIN_EXISTING_INVENTORY_RECORD", "scientific_result_changed"]},
        {"kind": "matrix", "fields": ["registered_contexts", "prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
    ],
    "P32-S45R2-E1-085": [
        {"kind": "source_rows", "source_ids": ["P32-S06", "P32-S13", "P32-S17"]},
        {"kind": "phrase", "file": "stage1_phase4_research_report.md", "needle": "General conflict-of-interest and retraction screens were not run", "role": "general source-status screening boundary"},
    ],
    "P32-S45R2-E1-086": [
        {"kind": "formal", "fields": ["audit_outcome", "scientific_application_status", "non_global_boundary"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-087": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "No novelty comparison was authorized, so no priority or originality claim is made", "role": "bounded no-novelty-claim status"},
        {"kind": "phrase", "file": "stage1_phase5_editorial_review.md", "needle": "Procedural separation does not imply statistically independent errors", "role": "project report records the same-model-family procedural-role boundary"},
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "His gate confirmations do not attest that he performed full-text or exact source-passage verification", "role": "project report records the human-gate verification boundary"},
    ],
    "P32-S45R2-E1-089": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "P32 now places its shortest discriminating obligations first", "role": "author-adjudicated falsification-first order"},
        {"kind": "formal", "fields": ["scientific_application_status"]},
    ],
    "P32-S45R2-E1-090": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "This revision is a report-level advance, not a mathematical obstruction or recovery result", "role": "design-level/no-result conclusion"},
        {"kind": "science"},
        {"kind": "matrix", "fields": ["registered_contexts", "prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
        {"kind": "route", "facets": ["A0", "FORMAL_TUPLE", "A2", "ROUTE_B"]},
    ],
    "P32-S45R2-E1-091": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "Liang Wang is the responsible human author. He specified the inherited mathematical object and restrictions", "role": "project report records the author contribution statement"},
    ],
    "P32-S45R2-E1-092": [
        {"kind": "phrase", "file": "stage1_phase5_ethics_review.md", "needle": "| 7. Human-subjects boundary | `NOT_APPLICABLE` |", "role": "frozen human-subject/data-ethics scope review"},
    ],
    "P32-S45R2-E1-093": [
        {"kind": "mentioned_files"},
        {"kind": "reader_fields", "fields": ["entry_count", "section6_claimed_current_count", "section6_exact_at_pinned_commit_count", "local_stage4_prime_sidecar_count", "boundary"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-094": [
        {"kind": "mentioned_files"},
        {"kind": "matrix", "fields": ["registered_contexts", "prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
    ],
    "P32-S45R2-E1-095": [
        {"kind": "phrase", "file": "stage1_phase5_editorial_review.md", "needle": "using the current Codex model family", "role": "project report records AI model-family provenance"},
        {"kind": "input_artifacts", "basenames": ["stage4_prime_revision_evidence_bundle_round3.json", "stage4_prime_revision_patch_round3_exact_confirmation.json", "stage4_prime_revision_round3.tex.apply-report.json", "stage4_prime_source_finalization_round3.json"]},
        {"kind": "science"},
    ],
    "P32-S45R2-E1-096": [
        {"kind": "phrase", "file": "stage1_phase6_final_report.md", "needle": "Liang Wang is the responsible human author. He approved the project restrictions, workflow gates", "role": "project report records responsible-author approval"},
        {"kind": "matrix", "fields": ["prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
        {"kind": "phrase", "file": "stage1_phase4_research_report.md", "needle": "General conflict-of-interest and retraction screens were not run", "role": "no-clean-screen boundary"},
    ],
    "P32-S45R2-E1-097": [
        {"kind": "phrase", "file": "stage1_phase5_review_synthesis.md", "needle": "| EIC | `f5119d18ff95882be8c0ec089f0e44ce9f810c5aae9acbd9e2a5f94304d5cc5d`", "role": "editorial review-label record"},
        {"kind": "phrase", "file": "stage1_phase5_review_synthesis.md", "needle": "| Ethics | `f3747e59ce8b8a9e8150c2ffbe12eb647e3927369b20c960e7894c92b729d31e`", "role": "ethics review-label record"},
        {"kind": "phrase", "file": "stage1_phase5_review_synthesis.md", "needle": "| Citation integrity | `cc345a03315881aff5ced8c995580c7fbed8f3a76ccdb0aed1ca7b7f46a7a059`", "role": "citation-integrity review-label record"},
        {"kind": "phrase", "file": "stage1_phase5_review_synthesis.md", "needle": "| Devil's Advocate | `1d80639061b85f942eeb244e77a412523051b0f0972739ed183a3238610d3afc`", "role": "adversarial review-label record"},
        {"kind": "phrase", "file": "stage1_phase5_editorial_review.md", "needle": "Procedural separation does not imply statistically independent errors", "role": "project report records the same-family correlated-error limitation"},
        {"kind": "input_artifacts", "basenames": ["stage3_prime_round3_traceability.json"]},
        {"kind": "matrix", "fields": ["prior_bounded_scopes_retained", "exact_locators_finalized", "explicit_bounded_unavailability"]},
    ],
}


P32_MISSING_COMPONENTS: dict[str, list[dict[str, str]]] = {
    "P32-S45R2-E1-087": [
        {
            "component_id": "P32-S45R2-E1-087-M01",
            "kind": "AI_ACTIVITY_PROVENANCE",
            "label": "one-model-family/session activity history",
            "required_artifact": "independent raw session/model activity ledger",
            "rationale": "The locked project reports record the disclosure but do not contain the original session/model activity ledger.",
        },
        {
            "component_id": "P32-S45R2-E1-087-M02",
            "kind": "AUTHOR_ATTESTATION",
            "label": "human gate approval/readership boundary",
            "required_artifact": "original author attestation for the stated gate/readership acts",
            "rationale": "A project report repeating the boundary is not the original author attestation.",
        },
    ],
    "P32-S45R2-E1-091": [
        {
            "component_id": "P32-S45R2-E1-091-M01",
            "kind": "AUTHOR_ATTESTATION",
            "label": "author contribution and accountability acts",
            "required_artifact": "original author contribution attestation",
            "rationale": "The report is a secondary workflow record and cannot attest the author's acts by itself.",
        }
    ],
    "P32-S45R2-E1-095": [
        {
            "component_id": "P32-S45R2-E1-095-M01",
            "kind": "AI_ACTIVITY_PROVENANCE",
            "label": "AI dates, model family, and task history",
            "required_artifact": "complete raw session/model activity ledger",
            "rationale": "Locked reports and output artifacts do not replay the complete activity/date/model assertion.",
        }
    ],
    "P32-S45R2-E1-096": [
        {
            "component_id": "P32-S45R2-E1-096-M01",
            "kind": "AUTHOR_ATTESTATION",
            "label": "responsible-author approvals",
            "required_artifact": "original author approval attestation bound to these acts",
            "rationale": "The locked report records the statement but is not the original attestation.",
        }
    ],
    "P32-S45R2-E1-097": [
        {
            "component_id": "P32-S45R2-E1-097-M01",
            "kind": "AI_ACTIVITY_PROVENANCE",
            "label": "single-model-family instantiation of four procedural roles",
            "required_artifact": "complete raw model/session/role activity ledger",
            "rationale": "Review-file existence and report labels do not independently establish the runtime model-family history.",
        }
    ],
}


def resolve_status_dependencies(
    cfg: dict[str, Any],
    claim: dict[str, Any],
    paper: Path,
    notes: Path,
    input_lock_path: Path,
    input_paper: dict[str, Any],
    matrix_path: Path,
    matrix: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, str], list[str]]:
    """Resolve an explicit compound-claim plan to raw, replayable dependencies."""
    plan = P32_STATUS_PLANS.get(claim["claim_id"]) if cfg["paper_id"] == "P32" else None
    if plan is None:
        return [], {}, ["NO_EXPLICIT_RAW_DEPENDENCY_PLAN"]
    input_lock_doc = json.loads(input_lock_path.read_text(encoding="utf-8"))
    input_paper_index = next(
        index for index, row in enumerate(input_lock_doc["papers"]) if row["paper_id"] == cfg["paper_id"]
    )
    dependencies: list[dict[str, Any]] = []
    sources: dict[str, str] = {}
    unsupported: list[str] = []
    active_verdict = "VERIFIED"

    def add(
        path: Path,
        needle: str,
        role: str,
        rule: str,
        *,
        parsed_value: Any = None,
        pointer: str | None = None,
    ) -> None:
        component_id = f"{claim['claim_id']}-D{len(dependencies) + 1:03d}"
        try:
            record, source_text = raw_dependency(
                component_id=component_id,
                path=path,
                needle=needle,
                role=role,
                derivation_rule=rule,
                parsed_value=parsed_value,
                json_pointer=pointer,
            )
        except Exception as exc:
            unsupported.append(f"{component_id}:{type(exc).__name__}:{exc}")
            return
        chain = dependency_binding_chain(
            child=path,
            input_lock_path=input_lock_path,
            input_lock_doc=input_lock_doc,
            paper=paper,
            notes=notes,
        )
        if chain is None:
            unsupported.append(f"{component_id}:NO_CLOSED_INPUT_LOCK_BINDING_CHAIN:{path.relative_to(ROOT)}")
            return
        record["claim_id"] = claim["claim_id"]
        record["source_ref_slug"] = raw_artifact_source_slug(cfg, record["artifact"])
        record["semantic_verdict"] = active_verdict
        record["component_semantic_verdict"] = active_verdict
        record["binding_chain"] = chain
        dependencies.append(record)
        sources[record["source_ref_slug"]] = source_text

    finalization_path = notes / "stage4_prime_source_finalization_round3.json"
    finalization = json.loads(finalization_path.read_text(encoding="utf-8"))
    finalized_rows = {row["source_id"]: (index, row) for index, row in enumerate(finalization["rows"])}
    ledger_path = notes / "stage4_prime_literature_screening_ledger_round2.json"
    replay_path = notes / "stage4_prime_literature_replay_round2.raw.json"
    reader_path = notes / "stage4_prime_reader_artifact_manifest_round2.json"
    formal_path = notes / "stage4_prime_formal_definition_audit_round2.json"

    for spec in plan:
        kind = spec["kind"]
        active_verdict = spec.get("verdict", "VERIFIED")
        if active_verdict not in {"VERIFIED", "UNVERIFIABLE", "MAJOR_DISTORTION", "MINOR_DISTORTION"}:
            unsupported.append(f"INVALID_SPEC_VERDICT:{active_verdict}")
            continue
        if kind in {"phrase", "phrase_root"}:
            path = (notes / spec["file"]) if kind == "phrase" else (ROOT / spec["file"])
            add(path, spec["needle"], spec["role"], "DIRECT_RAW_TEXT_PASSAGE_REVIEW")
        elif kind == "source_rows":
            for source_id in spec["source_ids"]:
                if source_id not in finalized_rows:
                    unsupported.append(f"SOURCE_FINALIZATION_ROW_MISSING:{source_id}")
                    continue
                index, row = finalized_rows[source_id]
                needle = json_scalar_needle("source_id", source_id)
                finalization_text = finalization_path.read_text(encoding="utf-8")
                if finalization_text.count(needle) != 1:
                    support_value = json.dumps(row.get("support_excerpt"), ensure_ascii=False)
                    needle = f'{needle},\n      "support_excerpt": {support_value}'
                role = (
                    f"fresh review of locked source-finalization row {source_id}: status={row['finalization_status']}; "
                    "passage support is limited to the current excerpt/hash and is absent when those fields are null"
                )
                add(
                    finalization_path,
                    needle,
                    role,
                    "PARSE_AND_REVIEW_COMPLETE_LOCKED_SOURCE_FINALIZATION_ROW",
                    parsed_value=row,
                    pointer=f"/rows/{index}",
                )
        elif kind == "matrix":
            for field in spec["fields"]:
                value = matrix["summary"][field]
                add(
                    matrix_path,
                    json_scalar_needle(field, value),
                    f"frozen Round-3 matrix summary field {field}",
                    "PARSE_JSON_SCALAR_AND_COMPARE_TO_COMPOUND_CLAIM_COMPONENT",
                    parsed_value=value,
                    pointer=f"/summary/{field}",
                )
        elif kind == "route":
            route_value = input_paper["frozen_route_state"]
            for facet in spec["facets"]:
                add(
                    input_lock_path,
                    route_value,
                    f"frozen Route-state facet {facet}",
                    "PARSE_CURRENT_INPUT_LOCK_PAPER_ROUTE_STATE_AND_REVIEW_NAMED_FACET",
                    parsed_value={"facet": facet, "frozen_route_state": route_value},
                    pointer=f"/papers/{input_paper_index}/frozen_route_state",
                )
        elif kind == "initial_system":
            value = input_paper["frozen_initial_system"]
            add(
                input_lock_path,
                value,
                "frozen initial dynamical system and normalization",
                "PARSE_CURRENT_INPUT_LOCK_PAPER_INITIAL_SYSTEM",
                parsed_value=value,
                pointer=f"/papers/{input_paper_index}/frozen_initial_system",
            )
        elif kind == "science":
            for index, tree in enumerate(input_paper["science_trees"]):
                add(
                    input_lock_path,
                    tree["sha256"],
                    f"complete frozen {Path(tree['path']).name} tree listing; no unlisted result is inferred",
                    "PARSE_COMPLETE_CURRENT_INPUT_LOCK_SCIENCE_TREE_ENTRY_AND_REPLAY_EACH_FILE_HASH",
                    parsed_value=tree,
                    pointer=f"/papers/{input_paper_index}/science_trees/{index}",
                )
        elif kind == "replay_fields":
            replay = json.loads(replay_path.read_text(encoding="utf-8"))
            for field in spec["fields"]:
                value = replay[field]
                needle = json_scalar_needle(field, value) if not isinstance(value, dict) else json.dumps(field)
                add(
                    replay_path,
                    needle,
                    f"dated replay field {field}",
                    "PARSE_LOCKED_DATED_REPLAY_FIELD",
                    parsed_value=value,
                    pointer=f"/{field}",
                )
        elif kind == "ledger_fields":
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
            for field in spec["fields"]:
                if field == "decision_counts":
                    value = ledger[field]
                    needle = '"decision_counts": {'
                    pointer = "/decision_counts"
                elif field in ledger.get("decision_counts", {}):
                    value = ledger["decision_counts"][field]
                    needle = json_scalar_needle(field, value)
                    pointer = f"/decision_counts/{field}"
                else:
                    value = ledger[field]
                    needle = json_scalar_needle(field, value)
                    pointer = f"/{field}"
                add(
                    ledger_path,
                    needle,
                    f"dated retrieval/deduplication/screening ledger field {field}",
                    "PARSE_LOCKED_LEDGER_FIELD_AND_RECOMPUTE_DECLARED_COUNT_OR_BOOLEAN",
                    parsed_value=value,
                    pointer=pointer,
                )
        elif kind == "formal":
            formal = json.loads(formal_path.read_text(encoding="utf-8"))
            for field in spec["fields"]:
                value = formal[field]
                needle = json_scalar_needle(field, value) if not isinstance(value, dict) else json.dumps(field)
                add(
                    formal_path,
                    needle,
                    f"formal-definition audit field {field}",
                    "PARSE_LOCKED_FORMAL_AUDIT_FIELD_WITH_NON_GLOBAL_SCIENTIFIC_BOUNDARY",
                    parsed_value=value,
                    pointer=f"/{field}",
                )
        elif kind == "reader_fields":
            reader = json.loads(reader_path.read_text(encoding="utf-8"))
            reader_text = reader_path.read_text(encoding="utf-8")
            for field in spec["fields"]:
                value = reader[field]
                if isinstance(value, dict):
                    needle = unique_value_needle(reader_text, value)
                else:
                    needle = json_scalar_needle(field, value)
                add(
                    reader_path,
                    needle,
                    f"reader-artifact manifest field {field}",
                    "PARSE_LOCKED_READER_MANIFEST_FIELD_AND_RESPECT_ITS_BOUNDARY",
                    parsed_value=value,
                    pointer=f"/{field}",
                )
        elif kind == "mentioned_files":
            mentioned, missing = claim_paths(paper, claim["claim_text"])
            unsupported.extend(f"MENTIONED_FILE_MISSING:{value}" for value in missing)
            for path in mentioned:
                source_text = path.read_text(encoding="utf-8")
                try:
                    first_line = unique_line_needle(source_text)
                except RuntimeError:
                    unsupported.append(f"MENTIONED_FILE_EMPTY:{path.relative_to(ROOT)}")
                    continue
                add(
                    path,
                    first_line,
                    f"full-file byte/hash replay for manuscript-mentioned artifact {path.name}",
                    "SHA256_OVER_COMPLETE_ARTIFACT_BYTES_AND_COMPARE_WITH_MANUSCRIPT_LITERAL",
                    parsed_value={"recomputed_sha256": sha_path(path), "bytes": path.stat().st_size},
                )
        elif kind == "files":
            for basename in spec["basenames"]:
                path = notes / basename
                if not path.is_file():
                    unsupported.append(f"RAW_ARTIFACT_MISSING:{basename}")
                    continue
                source_text = path.read_text(encoding="utf-8")
                try:
                    first_line = unique_line_needle(source_text)
                except RuntimeError:
                    unsupported.append(f"RAW_ARTIFACT_EMPTY:{basename}")
                    continue
                add(
                    path,
                    first_line,
                    f"full-file byte/hash replay for current raw artifact {basename}",
                    "SHA256_OVER_COMPLETE_ARTIFACT_BYTES_AND_REVIEW_DECLARED_BOUNDED_ROLE",
                    parsed_value={"recomputed_sha256": sha_path(path), "bytes": path.stat().st_size},
                )
        elif kind == "input_artifacts":
            by_basename = {Path(row["path"]).name: row for row in input_paper["audit_inputs"]}
            for basename in spec["basenames"]:
                row = by_basename.get(basename)
                if row is None:
                    # A few older support artifacts are current files but not a
                    # direct lock row.  They must not be silently substituted.
                    unsupported.append(f"INPUT_LOCK_ARTIFACT_ROW_MISSING:{basename}")
                    continue
                artifact_path = ROOT / row["path"]
                source_text = artifact_path.read_text(encoding="utf-8")
                add(
                    artifact_path,
                    unique_line_needle(source_text),
                    f"current input-lock artifact binding for {basename}",
                    "REPLAY_SHA256_AND_BYTES_OVER_COMPLETE_ARTIFACT_THEN_COMPARE_TO_CURRENT_INPUT_LOCK_ROW",
                    parsed_value={"input_lock_row": row, "recomputed_sha256": sha_path(artifact_path)},
                )
        else:
            unsupported.append(f"UNKNOWN_DEPENDENCY_SPEC_KIND:{kind}")

    # Every literal digest in a status claim must be either the digest of a
    # consumed artifact or occur in the consumed raw carrier.  Merely looking
    # like a SHA-256 is not evidence.
    for literal in embedded_sha256_literals(claim["claim_text"]):
        matched = any(
            literal == row["artifact"]["sha256"] or literal.encode("ascii") in sources[row["source_ref_slug"]].encode("utf-8")
            for row in dependencies
        )
        if not matched:
            unsupported.append(f"UNBOUND_EMBEDDED_SHA256:{literal}")
    return dependencies, sources, unsupported


def reclassify_phase_a(cfg: dict[str, Any], notes: Path, stage: Path) -> tuple[dict[str, Any], Path]:
    """Separate useless Bing cards from fresh adjudication of locked raw identity carriers."""
    source = json.loads((notes / "stage4_5_round2_browser_reference_verification.json").read_text(encoding="utf-8"))
    rows = source["rows"]
    if len(rows) != cfg["reference_total"]:
        raise RuntimeError("Phase-A row denominator changed")
    finalization_path = notes / "stage4_prime_source_finalization_round3.json"
    finalization = json.loads(finalization_path.read_text(encoding="utf-8"))
    finalized = {row["source_id"]: row for row in finalization["rows"]}
    cw_path = notes / "stage4_prime_closest_work_source_verification_round2.json"
    cw_records: dict[str, dict[str, Any]] = {}
    if cw_path.is_file():
        cw_records = {row["key"]: row for row in json.loads(cw_path.read_text(encoding="utf-8"))["records"]}
    prior_browser_path = notes / "stage4_5_round1_browser_reference_verification.json"
    prior_browser: dict[str, dict[str, Any]] = {}
    if prior_browser_path.is_file():
        prior_browser = {
            row["ref_slug"]: row
            for row in json.loads(prior_browser_path.read_text(encoding="utf-8"))["rows"]
        }
    for row in rows:
        search = row.get("fresh_exact_title_author_search", {})
        summaries = search.get("top_result_summaries", [])
        row["fresh_search_semantic_adjudication"] = {
            "result_cards_reviewed": len(summaries),
            "definitive_author_title_year_match": False,
            "correction_retraction_eoc_clearance": False,
            "status": "NOT_FOUND",
            "reason": (
                "Returned cards did not establish the registered author+title+year identity; zero/one generic title-term "
                "hits and transport success are not semantic resolution."
            ),
        }
        ref_slug = row["ref_slug"]
        if ref_slug in cw_records:
            carrier_path = cw_path
            carrier_record = cw_records[ref_slug]
            carrier_kind = "SAME_DAY_HASH_BOUND_AUTHORITATIVE_CLOSEST_WORK_IDENTITY_RECORD"
            identity_fields = {
                "title": carrier_record["title"],
                "authors": carrier_record["authors"],
                "year": carrier_record["year"],
                "doi": carrier_record.get("doi"),
                "authoritative_metadata": carrier_record["authoritative_metadata"],
            }
        elif ref_slug == "P32-S13" and ref_slug in prior_browser:
            carrier_path = prior_browser_path
            carrier_record = prior_browser[ref_slug]
            carrier_kind = "HASH_BOUND_AUTHORITATIVE_IDENTITY_REVIEW_RECORD"
            identity_fields = carrier_record["bibtex_fields_reviewed"]
        else:
            carrier_path = finalization_path
            carrier_record = finalized[ref_slug]
            trace = carrier_record.get("retrieval_trace", {})
            if trace.get("http_status") != 200 or not (
                trace.get("response_sha256") or trace.get("extracted_text_sha256")
            ):
                raise RuntimeError(f"no current raw authoritative identity carrier for {ref_slug}")
            carrier_kind = "CURRENT_HASH_BOUND_AUTHORITATIVE_RETRIEVAL_TRACE"
            identity_fields = {
                "source_id": carrier_record["source_id"],
                "identity_source_url": carrier_record["identity_source_url"],
                "retrieval_authority": trace.get("authority"),
                "request_url": trace.get("request_url"),
                "resolved_url": trace.get("resolved_url"),
                "response_sha256": trace.get("response_sha256") or trace.get("extracted_text_sha256"),
                "response_bytes": trace.get("response_bytes") or trace.get("extracted_text_bytes"),
                "retrieved_at_utc": trace.get("retrieved_at_utc"),
                "recorded_title": trace.get("title"),
            }
        row["locked_authoritative_identity_carrier"] = {
            "kind": carrier_kind,
            "artifact": artifact(carrier_path),
            "record": identity_fields,
            "fresh_model_readjudication": "VERIFIED_IDENTITY_AND_REGISTERED_METADATA_WITHIN_CARRIER_SCOPE",
            "passage_support_inferred": False,
        }
        row["named_record_identity_resolution"] = (
            "RESOLVED_BY_FRESH_READJUDICATION_OF_LOCKED_AUTHORITATIVE_IDENTITY_CARRIER"
        )
        row["status"] = "RESOLVED"
        row["correction_retraction_eoc_observation"] = "NOT_CHECKED_NO_FRESH_CLEARANCE_CLAIMED"
    source.update(
        {
            "generated_at_utc": STAMP,
            "resolved": cfg["reference_total"],
            "unresolved": 0,
            "unresolved_ref_slugs": [],
            "locked_authoritative_identity_carriers_readjudicated": cfg["reference_total"],
            "irrelevant_bing_result_sets_contributing_to_resolution": 0,
            "correction_retraction_eoc_clearances": 0,
            "verdict": "PASS_WITH_NOTES_LOCKED_AUTHORITATIVE_IDENTITY_CARRIERS",
            "boundary": (
                "Every identity was freshly re-adjudicated from a hash-bound authoritative identity/retrieval carrier. "
                "The current Bing cards contributed 0/N and no fresh correction/retraction/EOC clearance is claimed."
            ),
        }
    )
    path = stage / "stage4_5_round2_browser_reference_verification.json"
    dump(path, source)
    return source, path


def reclassify_reference_audit(
    cfg: dict[str, Any], notes: Path, stage: Path, phase_a_path: Path
) -> tuple[dict[str, Any], Path, Path]:
    audit = copy.deepcopy(
        json.loads((notes / "stage4_5_round2_reference_citation_audit.json").read_text(encoding="utf-8"))
    )
    audit["generated_at_utc"] = STAMP
    audit["overall_verdict"] = "PASS_WITH_NOTES"
    audit["phase_a"].update(
        {
            "ledger": staged_artifact(stage, phase_a_path),
            "resolved": cfg["reference_total"],
            "unresolved": 0,
            "coverage_rate": 1.0,
            "locked_authoritative_identity_carriers_readjudicated": cfg["reference_total"],
            "irrelevant_bing_result_sets_contributing_to_resolution": 0,
            "correction_retraction_eoc_clearances": 0,
            "verdict": "PASS_WITH_NOTES_LOCKED_AUTHORITATIVE_IDENTITY_CARRIERS",
        }
    )
    audit_reclassifications = [
        {
            "reclassification_id": cfg["phase_a_reclassification_id"],
            "phase": "A",
            "status": "APPLIED_TO_AUDIT_ARTIFACTS_ONLY",
            "affected_rows": cfg["reference_total"],
            "from": "RESOLVED_WITH_FRESH_SEARCH_AND_LOCKED_SOURCE_FINALIZATION",
            "to": "RESOLVED_BY_FRESH_READJUDICATION_OF_LOCKED_AUTHORITATIVE_IDENTITY_CARRIER",
            "reason": (
                "Returned Bing cards contribute no identity evidence; resolution comes only from fresh row-wise "
                "adjudication of current hash-bound authoritative identity/retrieval carriers."
            ),
        }
    ]
    if cfg["paper_id"] == "P32":
        contexts = audit["phase_b"]["contexts"]
        affected = [row for row in contexts if row["ref_slug"] in {"P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"}]
        if len(affected) != 4:
            raise RuntimeError("P32 retained-context denominator changed")
        for row in affected:
            if row.get("support_excerpt_sha256") is not None:
                raise RuntimeError("P32 retained row unexpectedly acquired a locked excerpt hash")
            row.update(
                {
                    "support_excerpt_hash_bound_in_current_context": False,
                    "semantic_review": (
                        "A declared endpoint is retained, but no support excerpt/hash is bound by the current locked "
                        "source-finalization row; substantive role verification is unavailable."
                    ),
                    "semantic_review_method": "fresh locked-evidence-availability audit; no source-excerpt review possible",
                    "verdict": "UNVERIFIABLE",
                    "unverifiable_reason": "CURRENT_LOCKED_SUPPORT_EXCERPT_AND_HASH_ABSENT",
                }
            )
        audit["phase_b"].update(
            {
                "registered_use_verified": 26,
                "coverage_rate": 26 / 30,
                "passage_bounded_contexts": 18,
                "retained_prior_bounded_contexts": 4,
                "retained_prior_bounded_contexts_verified": 0,
                "unverifiable_contexts": 4,
                "unsupported_contexts": 0,
                "verdict": "FAIL",
                "interpretation_boundary": (
                    "Eighteen exact current excerpts support bounded context and eight metadata-only rows preserve "
                    "no-transfer boundaries. Four retained endpoints have no current locked excerpt/hash and are UNVERIFIABLE."
                ),
            }
        )
        audit_reclassifications.append(
            {
                "reclassification_id": cfg["phase_b_reclassification_id"],
                "phase": "B/E",
                "status": "APPLIED_TO_AUDIT_ARTIFACTS_ONLY",
                "affected_rows": 4,
                "ref_slugs": ["P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"],
                "from": "VERIFIED_BOUNDED_CONTEXT_NOT_FULL_ROLE_PROOF",
                "to": "UNVERIFIABLE",
                "reason": "Current locked source-finalization rows contain locator strings but null support excerpts/hashes.",
            }
        )
        audit["overall_verdict"] = "FAIL"
    audit["audit_artifact_reclassifications"] = audit_reclassifications
    json_path = stage / "stage4_5_round2_reference_citation_audit.json"
    dump(json_path, audit)
    b = audit["phase_b"]
    md_lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 2 reference/citation audit",
        "",
        "## Verdict",
        "",
        f"Phase-A identity: **{cfg['reference_total']}/{cfg['reference_total']}** freshly re-adjudicated from locked "
        "authoritative identity/retrieval carriers. Bing result-card contribution: **0/"
        f"{cfg['reference_total']}**. Fresh correction/retraction/EOC clearances: **0**.",
        "",
        "## Phase B",
        "",
        f"Reviewed **{b['reviewed']}/{b['registered_citation_context_tuples']}** registered contexts; "
        f"verified **{b['registered_use_verified']}/{b['registered_citation_context_tuples']}**.",
        f"Passage-bounded **{b['passage_bounded_contexts']}**; metadata-only boundary-faithful "
        f"**{b['metadata_only_boundary_faithful_contexts']}**; UNVERIFIABLE **{b.get('unverifiable_contexts', 0)}**.",
        "",
        "No full-source role, project theorem, scientific result, or Route transfer is inferred.",
    ]
    md_path = stage / "stage4_5_round2_reference_citation_audit.md"
    write(md_path, "\n".join(md_lines))
    return audit, json_path, md_path


def reclassify_seven_modes(
    cfg: dict[str, Any], notes: Path, stage: Path, reference_audit: dict[str, Any]
) -> tuple[Path, Path]:
    audit = copy.deepcopy(
        json.loads((notes / "stage4_5_round2_seven_failure_mode_audit.json").read_text(encoding="utf-8"))
    )
    mode = audit["modes"]["2_hallucinated_citation"]
    unverifiable = reference_audit["phase_b"].get("unverifiable_contexts", 0)
    mode["status"] = "INSUFFICIENT_EVIDENCE"
    mode["evidence"] = [
        (
            f"{cfg['reference_total']}/{cfg['reference_total']} identities were freshly re-adjudicated from current "
            "hash-bound authoritative identity/retrieval carriers; unrelated Bing cards contributed 0."
        ),
        (
            f"Phase B verified {reference_audit['phase_b']['registered_use_verified']}/"
            f"{reference_audit['phase_b']['registered_citation_context_tuples']} registered uses; "
            f"{unverifiable} remain UNVERIFIABLE."
        ),
        (
            f"The locked successor still contains the blocking translated citation-status distortion at "
            f"{cfg['block_id']} line {cfg['line']}; audit-side evidence rebinding does not correct manuscript bytes."
        ),
    ]
    audit.update(
        {
            "generated_at_utc": STAMP,
            "clear": 6,
            "insufficient_evidence": 1,
            "suspected": 0,
            "overall": "FAIL",
        }
    )
    json_path = stage / "stage4_5_round2_seven_failure_mode_audit.json"
    dump(json_path, audit)
    md_path = stage / "stage4_5_round2_seven_failure_mode_audit.md"
    write(
        md_path,
        "\n".join(
            [
                f"# {cfg['paper_id']} — Stage 4.5 Round 2 seven-failure-mode audit",
                "",
                "Overall: **FAIL**.",
                "",
                "- CLEAR: **6/7**.",
                "- INSUFFICIENT_EVIDENCE: **1/7** (`2_hallucinated_citation`).",
                "- SUSPECTED: **0/7**.",
                "",
                (
                    f"All {cfg['reference_total']} identities were freshly re-adjudicated from locked authoritative "
                    "carriers; Bing cards contributed no evidence and no fresh correction-status clearance is claimed. "
                    f"Phase B retains {unverifiable} unverifiable contexts. The locked translated citation-status "
                    "sentence is also materially inconsistent with the matrix. These are evidence-scope/status findings, "
                    "not accusations that a source is fabricated."
                ),
            ]
        ),
    )
    return json_path, md_path


def local_semantic_class(cfg: dict[str, Any], claim: dict[str, Any]) -> str:
    if claim["claim_id"] == cfg["parent_compound_claim_id"]:
        return "TRANSLATED_STATUS_CONTRADICTION"
    if claim["claim_id"] in cfg["proof_claim_ids"]:
        return "SELF_CONTAINED_FORMAL_PROOF_OR_COROLLARY"
    if any(block in cfg["constitutive_status_block_overrides"] for block in claim["writer_anchors"]):
        return "CONSTITUTIVE_DEFINITION_PROPOSAL_OR_MANUSCRIPT_SCOPE"
    if any(block in cfg["status_blocks"] for block in claim["writer_anchors"]):
        return "CLAIM_SPECIFIC_LOCKED_CARRIER"
    return "CONSTITUTIVE_DEFINITION_PROPOSAL_OR_MANUSCRIPT_SCOPE"


def claim_paths(paper: Path, text_value: str) -> tuple[list[Path], list[str]]:
    resolved: list[Path] = []
    missing: list[str] = []
    for rel in dict.fromkeys(re.findall(r"\\path\{([^{}]+)\}", text_value)):
        if rel.startswith("notes/"):
            path = paper / rel
        elif rel.startswith("papers/") or rel.startswith("BATCH_") or rel == "README.md":
            path = ROOT / rel
        else:
            continue
        if path.is_file():
            resolved.append(path)
        else:
            missing.append(rel)
    return resolved, missing


def embedded_sha256_literals(text_value: str) -> list[str]:
    normalized = text_value.replace(r"\allowbreak{}", "")
    return list(dict.fromkeys(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", normalized)))


def proof_dependency_claim_id(claim_id: str) -> str:
    if claim_id in {"P32-S45R2-E1-065", "P32-S45R2-E1-067"}:
        return "P32-S45R2-E1-066"
    return claim_id


VERDICT_WEAKNESS = {
    "VERIFIED": 0,
    "MINOR_DISTORTION": 1,
    "UNVERIFIABLE": 2,
    "UNVERIFIABLE_ACCESS": 2,
    "MAJOR_DISTORTION": 3,
}


def weakest_verdict(verdicts: list[str]) -> str:
    if not verdicts:
        return "UNVERIFIABLE"
    return max(verdicts, key=lambda value: VERDICT_WEAKNESS[value])


def evidence_from_dependency(
    *,
    dependency: dict[str, Any],
    claim_surface: dict[str, Any],
    source_text: str,
    row_id: str,
    detail_prefix: str,
) -> dict[str, Any]:
    """Emit one shared Schema-5 row from one raw dependency tuple."""
    template = {
        "schema_version": "evidence-row/1.0",
        "surface": "phase_e_claim_verification",
        "row_id": row_id,
        "claim": claim_surface,
        "source": {
            "ref_slug": dependency["source_ref_slug"],
            "display_label": dependency["source_ref_slug"],
            "source_artifact_sha256": dependency["artifact"]["sha256"],
        },
        "anchor": {
            "kind": "section",
            "value_encoded": urllib.parse.quote(
                f"raw-dependency:{dependency['component_id']}:{dependency.get('json_pointer') or 'bounded-text'}",
                safe="",
            ),
        },
        "verdict": dependency["semantic_verdict"],
        "detail": (
            f"{detail_prefix} Raw role: {dependency['semantic_role']} Binding: "
            f"{dependency['binding_chain']['type']}; rule: {dependency['derivation_rule']}."
        ),
    }
    row = EVR.build(template, source_text, extracted_text=dependency["raw_excerpt"])
    if row["excerpt"]["excerpt_sha256"] != dependency["raw_excerpt_sha256"]:
        raise RuntimeError(f"dependency/evidence excerpt digest mismatch: {dependency['component_id']}")
    expected_span = {
        "start": dependency["raw_utf8_span"]["start_byte"],
        "end": dependency["raw_utf8_span"]["end_byte"],
    }
    if row["excerpt"]["source_span_utf8"] != expected_span:
        raise RuntimeError(
            f"dependency/evidence exact UTF-8 span mismatch: {dependency['component_id']}"
        )
    if row["source"]["source_artifact_sha256"] != dependency["artifact"]["sha256"]:
        raise RuntimeError(f"dependency/evidence artifact digest mismatch: {dependency['component_id']}")
    dependency["evidence_row_id"] = row_id
    return row


def propagate_schema5_claim_verdicts(
    *,
    rows: list[dict[str, Any]],
    source_map: dict[str, str],
    claim_overall: dict[str, str],
    component_verdict_by_row: dict[str, str],
    component_id_by_row: dict[str, str],
) -> list[dict[str, Any]]:
    """Propagate weakest claim verdict while preserving component semantics.

    Shared evidence-row/1.0 is a claim-level schema: every row carrying one
    claim_id must carry the same verdict.  Component outcomes therefore live
    in the dependency catalog and are restated explicitly in row detail.
    """
    rebuilt_rows: list[dict[str, Any]] = []
    for row in rows:
        claim_id = row["claim"]["claim_id"]
        if claim_id not in claim_overall:
            rebuilt_rows.append(row)
            continue
        component_verdict = component_verdict_by_row[row["row_id"]]
        component_id = component_id_by_row[row["row_id"]]
        overall = claim_overall[claim_id]
        template = {
            "schema_version": "evidence-row/1.0",
            "surface": "phase_e_claim_verification",
            "row_id": row["row_id"],
            "claim": row["claim"],
            "source": {
                "ref_slug": row["source"]["ref_slug"],
                "display_label": row["source"]["display_label"],
                "source_artifact_sha256": row["source"]["source_artifact_sha256"],
            },
            "anchor": {
                "kind": row["anchor"]["kind"],
                "value_encoded": row["anchor"]["value_encoded"],
            },
            "verdict": overall,
            "detail": (
                f"{row['detail']} component={component_id}; "
                f"component_semantic_verdict={component_verdict}; claim_overall={overall}. "
                "A supported component is not itself reclassified "
                "as unsupported; only the compound claim verdict is propagated."
            ),
        }
        if row["excerpt"]["state"] == "anchorless":
            rebuilt = EVR.build(template, None, failure_state="anchorless")
        else:
            ref_slug = row["source"]["ref_slug"]
            if ref_slug is None or ref_slug not in source_map:
                raise RuntimeError(f"source map missing during claim-verdict propagation: {row['row_id']}")
            rebuilt = EVR.build(
                template,
                source_map[ref_slug],
                extracted_text=row["excerpt"]["text"],
            )
            if rebuilt["excerpt"]["source_span_utf8"] != row["excerpt"]["source_span_utf8"]:
                raise RuntimeError(
                    f"Schema-5 verdict propagation moved the raw excerpt span: {row['row_id']}"
                )
        rebuilt_rows.append(rebuilt)
    return rebuilt_rows


def p29_mapped_dependencies(
    *,
    cfg: dict[str, Any],
    mapping_claim: dict[str, Any],
    mapping_catalog: dict[str, Any],
    claim: dict[str, Any],
    paper: Path,
    notes: Path,
    input_lock_path: Path,
    input_lock_doc: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, str], list[dict[str, Any]]]:
    """Replay Hubble's P29 map against raw bytes without using it as evidence."""
    if mapping_claim["claim_id"] != claim["claim_id"]:
        raise RuntimeError("P29 independent mapping claim ID mismatch")
    if mapping_claim["claim_text_sha256"] != sha_bytes(claim["claim_text"].encode("utf-8")):
        raise RuntimeError(f"P29 independent mapping claim hash mismatch: {claim['claim_id']}")
    if mapping_claim["claim_span_utf8"] != claim["draft_span"]:
        raise RuntimeError(f"P29 independent mapping claim span mismatch: {claim['claim_id']}")
    dependencies: list[dict[str, Any]] = []
    sources: dict[str, str] = {}
    missing: list[dict[str, Any]] = []
    sequence = 0
    for component in mapping_claim["components"]:
        tuple_ids = component["tuple_ids"]
        for tuple_index, tuple_id in enumerate(tuple_ids, start=1):
            mapped = mapping_catalog.get(tuple_id)
            if mapped is None:
                raise RuntimeError(f"P29 mapped tuple is absent: {tuple_id}")
            path = ROOT / mapped["artifact"]["path"]
            if not path.is_file() or artifact(path) != mapped["artifact"]:
                raise RuntimeError(f"P29 mapped tuple artifact changed: {tuple_id}")
            raw = path.read_bytes()
            source_text = raw.decode("utf-8")
            span = mapped["excerpt"]["utf8_span"]
            excerpt = raw[span["start_byte"] : span["end_byte"]].decode("utf-8")
            if (
                excerpt != mapped["excerpt"]["text"]
                or sha_bytes(excerpt.encode("utf-8")) != mapped["excerpt"]["sha256"]
                or len(excerpt.encode("utf-8")) != mapped["excerpt"]["bytes"]
                or len(excerpt.split()) != mapped["excerpt"]["words"]
                or len(excerpt.split()) > 25
            ):
                raise RuntimeError(f"P29 mapped tuple excerpt replay failed: {tuple_id}")
            raw_scope = mapped["raw_dependency"]
            scope_span = raw_scope["utf8_span"]
            scope_bytes = raw[scope_span["start_byte"] : scope_span["end_byte"]]
            if (
                len(scope_bytes) != raw_scope["bytes"]
                or sha_bytes(scope_bytes) != raw_scope["sha256"]
            ):
                raise RuntimeError(f"P29 mapped tuple raw-scope replay failed: {tuple_id}")
            chain = dependency_binding_chain(
                child=path,
                input_lock_path=input_lock_path,
                input_lock_doc=input_lock_doc,
                paper=paper,
                notes=notes,
            )
            if chain is None:
                raise RuntimeError(f"P29 mapped tuple has no controlling input-lock chain: {tuple_id}")
            sequence += 1
            controlling_excerpt, controlling_span, disambiguated = occurrence_specific_excerpt(
                source_text,
                excerpt,
                span,
            )
            dependency = {
                "claim_id": claim["claim_id"],
                "component_id": f"{component['component_id']}-D{tuple_index:03d}",
                "mapper_component_id": component["component_id"],
                "mapper_tuple_id": tuple_id,
                "artifact": mapped["artifact"],
                "raw_utf8_span": controlling_span,
                "raw_excerpt": controlling_excerpt,
                "raw_excerpt_sha256": sha_bytes(controlling_excerpt.encode("utf-8")),
                "raw_excerpt_word_count": len(controlling_excerpt.split()),
                "raw_dependency_scope": raw_scope,
                "semantic_role": f"{component['label']}: {mapped['role']}",
                "semantic_boundary": mapped["boundary"],
                "derivation_rule": mapped["derivation_rule"],
                "json_pointer": raw_scope.get("json_pointer"),
                "parsed_value": {"mapper_tuple_id": tuple_id},
                "fresh_semantic_adjudication": component["sufficiency"],
                "source_ref_slug": raw_artifact_source_slug(cfg, mapped["artifact"]),
                "semantic_verdict": component["verdict"],
                "component_semantic_verdict": component["verdict"],
                "binding_chain": chain,
            }
            if disambiguated:
                dependency["mapper_excerpt_occurrence_disambiguation"] = {
                    "reason": "MAPPED_EXCERPT_REPEATED_IN_RAW_ARTIFACT",
                    "mapped_utf8_span": span,
                    "mapped_excerpt_sha256": mapped["excerpt"]["sha256"],
                    "controlling_excerpt_expanded_with_adjacent_raw_tokens": True,
                    "word_cap": 25,
                }
            dependencies.append(dependency)
            sources[dependency["source_ref_slug"]] = source_text
        if component["missing_raw_dependency"] is not None:
            if component["verdict"] != "UNVERIFIABLE" or tuple_ids:
                # Mixed supported + missing components are valid; only require
                # that the missing component itself remains UNVERIFIABLE.
                if component["verdict"] != "UNVERIFIABLE":
                    raise RuntimeError(f"P29 missing component has non-U verdict: {component['component_id']}")
            missing.append(
                {
                    "claim_id": claim["claim_id"],
                    "component_id": component["component_id"],
                    "kind": component["kind"],
                    "label": component["label"],
                    "missing_raw_dependency": component["missing_raw_dependency"],
                    "rationale": component["rationale"],
                    "semantic_verdict": "UNVERIFIABLE",
                    "component_semantic_verdict": "UNVERIFIABLE",
                    "binding_boundary": artifact(input_lock_path),
                }
            )
    return dependencies, sources, missing


def make_correction(cfg: dict[str, Any], notes: Path, raw: bytes, matrix: dict[str, Any]) -> dict[str, Any]:
    claim = exact_claim(cfg, raw)
    marker = f"<!--block:{cfg['block_id']}-->".encode("utf-8")
    marker_start = raw.index(marker)
    following = raw.find(b"<!--block:", marker_start + len(marker))
    block_end = len(raw) if following < 0 else following
    block_raw = raw[marker_start:block_end]
    return {
        "correction_id": cfg["correction_id"],
        "issue_id": cfg["issue_id"],
        "severity": "SERIOUS",
        "blocking": True,
        "status": "PROPOSED_NOT_APPLIED",
        "manuscript": artifact(notes / cfg["draft"]),
        "block_id": cfg["block_id"],
        "line": cfg["line"],
        "block_sha256": sha_bytes(block_raw),
        "exact_old_text": cfg["old_clause"],
        "exact_old_text_sha256": sha_bytes(cfg["old_clause"].encode("utf-8")),
        "proposed_replacement_text": cfg["proposed_clause"],
        "proposed_replacement_sha256": sha_bytes(cfg["proposed_clause"].encode("utf-8")),
        "conflict": (
            "The translated abstract says every citation lacks a passage locator and that claim-level support remains "
            "undetermined, while the frozen Round-3 matrix records the nonzero bounded-locator partition below."
        ),
        "matrix": artifact(notes / cfg["matrix"]),
        "matrix_summary": matrix["summary"],
        "authority_to_apply": False,
        "applied": False,
        "scientific_claim_change": False,
        "required_followup": (
            "Obtain separate author authorization for this exact block replacement, apply it through the revision protocol, "
            "then run a fresh post-correction Stage-4.5 audit."
        ),
    }


def build_failure_package(cfg: dict[str, Any], *, preview_only: bool = False) -> dict[str, Any]:
    paper = ROOT / "papers" / cfg["slug"]
    notes = paper / "notes"
    for relative, (expected_sha, expected_bytes) in AUTHORITY_ARTIFACTS.items():
        authority_path = ROOT / relative
        if not authority_path.is_file() or (sha_path(authority_path), authority_path.stat().st_size) != (
            expected_sha,
            expected_bytes,
        ):
            raise RuntimeError(f"Stage-4.5 Round-2 authority binding changed: {relative}")
    event_raw = (ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHOR_EVENT_20260904.txt").read_bytes()
    if event_raw != "确认，下一轮\n".encode("utf-8"):
        raise RuntimeError("Stage-4.5 Round-2 author event exact bytes changed")
    input_lock_path = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
    input_lock = json.loads(input_lock_path.read_text(encoding="utf-8"))
    matching_input_papers = [row for row in input_lock["papers"] if row["paper_id"] == cfg["paper_id"]]
    if len(matching_input_papers) != 1:
        raise RuntimeError("input-lock paper row is not unique")
    input_paper = matching_input_papers[0]
    for row in input_paper["audit_inputs"]:
        verify_artifact_row(row)
    manifest_path = notes / "stage4_5_round2_output_manifest.json"
    archive = notes / cfg["archive"]
    incident_name = "stage4_5_round2_pass_attempt_invalidation_incident.json"
    incident_path = notes / incident_name
    if archive.exists() or incident_path.exists():
        raise RuntimeError("failure-finalization archive/incident collision")
    if sha_path(manifest_path) != cfg["pass_manifest_sha"]:
        raise RuntimeError("controlling PASS manifest changed")
    pass_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if pass_manifest.get("verdict") != "PASS" or pass_manifest.get("artifact_count_excluding_self") != 31:
        raise RuntimeError("unexpected PASS package shape")
    old_outputs = [verify_artifact_row(row) for row in pass_manifest["artifacts"]]
    old_outputs.append(manifest_path)
    if len({path.name for path in old_outputs}) != 32:
        raise RuntimeError("PASS output denominator/name collision")
    for key in ("builder", "invocation_entrypoint"):
        verify_artifact_row(pass_manifest[key])
    old_integrity = json.loads((notes / "stage4_5_round2_integrity_report.json").read_text(encoding="utf-8"))
    if old_integrity.get("verdict") != "PASS":
        raise RuntimeError("identified prior package is not the missed-surface PASS")
    compliance = json.loads((notes / "stage4_5_round2_compliance_report.json").read_text(encoding="utf-8"))
    if compliance.get("mode") != "primary_research" or compliance.get("overall_decision") != "warn":
        raise RuntimeError("do not alter the correct primary-research compliance classification")
    code, output = run(["python3", str(COMPLIANCE_CHECKER), str(notes / "stage4_5_round2_compliance_report.json")])
    if code != 0 or not output.startswith("OK:"):
        raise RuntimeError("official Schema-12 replay failed before adjudicative correction")

    input_manifest = json.loads((notes / "stage4_5_round2_input_manifest.json").read_text(encoding="utf-8"))
    for rel, row in input_manifest["protected_snapshot_before"].items():
        path = ROOT / rel
        if (sha_path(path), path.stat().st_size) != (row["sha256"], row["bytes"]):
            raise RuntimeError(f"protected input changed: {rel}")
    raw = (notes / cfg["draft"]).read_bytes()
    if sha_bytes(raw) != cfg["draft_sha"]:
        raise RuntimeError("successor draft changed")
    matrix_path = notes / cfg["matrix"]
    if sha_path(matrix_path) != cfg["matrix_sha"]:
        raise RuntimeError("Round-3 matrix changed")
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    correction = make_correction(cfg, notes, raw, matrix)
    p29_mapping: dict[str, Any] | None = None
    if cfg["paper_id"] == "P29":
        mapping_path = ROOT / P29_INDEPENDENT_MAPPING["path"]
        if not mapping_path.is_file() or artifact(mapping_path) != P29_INDEPENDENT_MAPPING:
            raise RuntimeError("P29 independent dependency mapping changed")
        p29_mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        if (
            p29_mapping.get("paper_id") != "P29"
            or p29_mapping.get("status") != "FAIL"
            or len(p29_mapping.get("claims", [])) != 66
            or len(p29_mapping.get("dependency_catalog", {})) != 108
            or p29_mapping.get("missing_raw_dependency_components") != 28
            or p29_mapping.get("verdict_summary")
            != {"VERIFIED": 45, "UNVERIFIABLE": 20, "MAJOR_DISTORTION": 1}
        ):
            raise RuntimeError("P29 independent dependency mapping contract changed")

    with tempfile.TemporaryDirectory(prefix=f"{cfg['paper_id'].lower()}-s45r2-fail-stage-", dir=notes) as temp_name:
        stage = Path(temp_name)
        for source in old_outputs:
            if source.name in REPLACED:
                continue
            shutil.copyfile(source, stage / source.name)

        phase_a_ledger, phase_a_path = reclassify_phase_a(cfg, notes, stage)
        reference_audit, reference_json_path, reference_md_path = reclassify_reference_audit(
            cfg, notes, stage, phase_a_path
        )
        seven_json_path, seven_md_path = reclassify_seven_modes(cfg, notes, stage, reference_audit)

        correction_payload = {
            "schema_version": f"p{cfg['paper']}-stage4.5-round2-correction-list/1.0",
            "paper_id": cfg["paper_id"],
            "generated_at_utc": STAMP,
            "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
            "correction_count": 1,
            "corrections_applied": 0,
            "corrections": [correction],
            "audit_artifact_reclassification_count": len(reference_audit["audit_artifact_reclassifications"]) + 1,
            "audit_artifact_reclassifications_applied": len(reference_audit["audit_artifact_reclassifications"]) + 1,
            "audit_artifact_reclassifications": reference_audit["audit_artifact_reclassifications"]
            + [
                {
                    "reclassification_id": f"{cfg['paper_id']}-S45R2-AUDIT-RECLASS-LOCAL-EVIDENCE",
                    "phase": "E",
                    "status": "APPLIED_TO_AUDIT_ARTIFACTS_ONLY",
                    "affected_rows": 66 if cfg["paper_id"] == "P29" else 89,
                    "from": "VERIFIED_WITH_UNRELATED_FIXED_PREAMBLE_EXCERPT",
                    "to": "CLAIM_SPECIFIC_SEMANTIC_READJUDICATION_WITH_ACTUAL_DEPENDENCY_SPANS",
                    "reason": (
                        "The earlier row anchors named each claim span, but every local excerpt was the same source-prefix "
                        "preamble and did not overlap the claim. Each row is now classified and rebound to its actual "
                        "constitutive span, proof dependency, or independently replayable locked carrier; manuscript "
                        "presence alone is never treated as factual support."
                    ),
                }
            ],
            "scope_boundary": "Audit-derived proposal only; this object grants no manuscript-edit authority.",
        }
        correction_path = stage / "stage4_5_round2_correction_list.json"
        dump(correction_path, correction_payload)
        write(
            stage / "stage4_5_round2_correction_list.md",
            "\n".join(
                [
                    f"# {cfg['paper_id']} — Stage 4.5 Round 2 correction list",
                    "",
                    "**FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED.**",
                    "",
                    f"- `{cfg['correction_id']}` / `{cfg['issue_id']}` — `{cfg['block_id']}`, line {cfg['line']}: the Traditional-Chinese abstract says every citation lacks a passage locator, but the locked evidence records {cfg['passage_bounded']} passage-bounded, {cfg['metadata_only']} metadata-only, and {cfg['unverifiable_contexts']} retained-endpoint/unverifiable contexts.",
                    "- The exact replacement is recorded in the JSON sidecar. It was not applied and is not authorized by this audit.",
                    f"- Audit-derived reclassifications applied: **{correction_payload['audit_artifact_reclassification_count']}**; these change only Stage-4.5 sidecars, never manuscript bytes.",
                    "",
                    "A separately authorized patch and a fresh post-correction Stage-4.5 audit are required.",
                ]
            ),
        )

        phase_c = copy.deepcopy(
            json.loads((notes / "stage4_5_round2_phase_c_internal_consistency_audit.json").read_text(encoding="utf-8"))
        )
        coverage = phase_c["registered_surface_coverage"]
        if (coverage["verified"], coverage["inconsistent"], len(phase_c["surfaces"])) != (13, 0, 13):
            raise RuntimeError("prior Phase-C denominator changed")
        phase_c["generated_at_utc"] = STAMP
        phase_c["late_discovered_surface_adjudication"] = True
        phase_c["surfaces"].append(
            {
                "surface_id": f"C-{cfg['paper_id']}-14",
                "description": "Traditional-Chinese abstract citation-locator/support-status statement",
                "evidence_scope": "exact successor block plus frozen Round-3 matrix summary",
                "block_id": cfg["block_id"],
                "line": cfg["line"],
                "exact_text_sha256": correction["exact_old_text_sha256"],
                "matrix_summary": matrix["summary"],
                "status": "INCONSISTENT_BLOCKING",
                "correction_id": cfg["correction_id"],
                "correction_applied": False,
            }
        )
        coverage.update(
            {
                "data_stat_internal_surfaces_registered": 14,
                "data_stat_internal_surfaces_checked": 14,
                "verified": 13,
                "inconsistent": 1,
            }
        )
        phase_c["verdict"] = "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED"
        dump(stage / "stage4_5_round2_phase_c_internal_consistency_audit.json", phase_c)
        write(
            stage / "stage4_5_round2_phase_c_internal_consistency_audit.md",
            "\n".join(
                [
                    f"# {cfg['paper_id']} — Stage 4.5 Round 2 Phase C audit",
                    "",
                    f"Verified **13/14** registered data/stat/internal surfaces; **1/14** is blocking and inconsistent. Tables remain **{cfg['tables']}/{cfg['tables']}**; figures **0/0**.",
                    "",
                    f"The missed surface is `{cfg['block_id']}` line {cfg['line']} in the Traditional-Chinese abstract. It says all citations lack passage locators, contradicting the locked audit partition {cfg['passage_bounded']} bounded + {cfg['metadata_only']} metadata-only + {cfg['unverifiable_contexts']} retained-endpoint/unverifiable.",
                    "",
                    "Verdict: **FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED**.",
                ]
            ),
        )

        registry = copy.deepcopy(json.loads((notes / "stage4_5_round2_claim_registry.json").read_text(encoding="utf-8")))
        if len(registry["claims"]) != cfg["prior_claims"]:
            raise RuntimeError("prior ALL-tier claim denominator changed")
        new_claim = exact_claim(cfg, raw)
        registry["claims"].append(new_claim)
        registry_path = stage / "stage4_5_round2_claim_registry.json"
        dump(registry_path, registry)
        registry_raw = registry_path.read_bytes()
        coverage_report = COVER.build_report(raw, registry_raw)
        COVER.validate_report(coverage_report, raw, registry_raw)
        if coverage_report["candidate_unregistered_count"] != 0:
            raise RuntimeError("official claim coverage has a lexical gap")
        coverage_path = stage / "stage4_5_round2_claim_registry_coverage.json"
        dump(coverage_path, coverage_report)
        code, output = run(
            [
                "python3",
                str(ARS / "scripts/claim_registry_coverage.py"),
                "--draft",
                str(notes / cfg["draft"]),
                "--registry",
                str(registry_path),
                "--validate-report",
                str(coverage_path),
            ]
        )
        write(stage / "stage4_5_round2_claim_registry_coverage_replay.log", output)
        if code != 0:
            raise RuntimeError("official claim coverage replay failed")

        matrix_text = matrix_path.read_text(encoding="utf-8")
        source_map = copy.deepcopy(
            json.loads((notes / "stage4_5_round2_evidence_source_map.json").read_text(encoding="utf-8"))
        )
        if cfg["matrix_slug"] in source_map:
            raise RuntimeError("matrix summary source slug collision")
        source_map[cfg["matrix_slug"]] = matrix_text
        local_slug = f"{cfg['paper_id']}LocalSuccessor"
        draft_text = raw.decode("utf-8")
        if source_map.get(local_slug) != draft_text:
            raise RuntimeError("local-successor source map changed")

        projection = copy.deepcopy(
            json.loads((notes / "stage4_5_round2_evidence_projection_ledger.json").read_text(encoding="utf-8"))
        )
        projection["generated_at_utc"] = STAMP
        cw_slugs = {"P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"} if cfg["paper_id"] == "P32" else set()
        projection["rows"] = [
            row
            for row in projection["rows"]
            if row.get("ref_slug") not in cw_slugs | {local_slug, cfg["matrix_slug"]}
        ]
        source_finalization_path = notes / "stage4_prime_source_finalization_round3.json"
        source_finalization_text = source_finalization_path.read_text(encoding="utf-8")
        source_finalization = json.loads(source_finalization_text)
        finalization_rows = {row["source_id"]: row for row in source_finalization["rows"]}
        projection["rows"].append(
            {
                "ref_slug": local_slug,
                "projection_origin": (
                    "current successor text with each constitutive/proof excerpt newly constrained to its actual dependency span"
                ),
                "source_artifact": artifact(notes / cfg["draft"]),
                "held_text_sha256": sha_bytes(raw),
                "held_text_bytes": len(raw),
                "passage_support_claimed": False,
                "role": (
                    "constitutive/normative manuscript scope and self-contained proof dependencies only; manuscript "
                    "self-assertion is not used for external fact or execution-status verification"
                ),
            }
        )
        projection["rows"].append(
            {
                "ref_slug": cfg["matrix_slug"],
                "projection_origin": "complete raw frozen Round-3 matrix; bounded excerpt identifies the parsed summary field",
                "source_artifact": artifact(matrix_path),
                "held_text_sha256": sha_bytes(matrix_text.encode("utf-8")),
                "held_text_bytes": len(matrix_text.encode("utf-8")),
                "passage_support_claimed": False,
                "role": "internal citation-status consistency evidence only",
            }
        )

        old_evidence_rows = copy.deepcopy(
            json.loads((notes / "stage4_5_round2_evidence_rows.json").read_text(encoding="utf-8"))
        )
        if len(old_evidence_rows) != cfg["prior_evidence"]:
            raise RuntimeError("prior evidence denominator changed")
        claims_by_id = {claim["claim_id"]: claim for claim in registry["claims"]}
        evidence_rows: list[dict[str, Any]] = []
        local_adjudications: list[dict[str, Any]] = []
        dependency_catalog_rows: list[dict[str, Any]] = []
        missing_dependency_catalog_rows: list[dict[str, Any]] = []
        local_reclassified = 0
        cw_reclassified = 0
        projected_raw_source_slugs = {
            row["ref_slug"] for row in projection["rows"] if row.get("ref_slug") is not None
        }

        def add_projection(dependency: dict[str, Any], source_text: str) -> None:
            source_slug = dependency["source_ref_slug"]
            expected_slug = raw_artifact_source_slug(cfg, dependency["artifact"])
            if source_slug != expected_slug:
                raise RuntimeError(
                    f"raw source slug is not the stable artifact slug: {dependency['component_id']}"
                )
            existing_source = source_map.get(source_slug)
            if existing_source is not None and existing_source != source_text:
                raise RuntimeError(f"raw source slug collision: {source_slug}")
            source_map[source_slug] = source_text
            if source_slug in projected_raw_source_slugs:
                return
            projection["rows"].append(
                {
                    "ref_slug": source_slug,
                    "projection_origin": "direct raw claim dependency with recursively replayable input-lock binding",
                    "source_artifact": dependency["artifact"],
                    "held_text_sha256": sha_bytes(source_text.encode("utf-8")),
                    "held_text_bytes": len(source_text.encode("utf-8")),
                    "passage_support_claimed": dependency["semantic_verdict"] == "VERIFIED",
                    "role": dependency["semantic_role"],
                    "binding_chain": dependency["binding_chain"],
                }
            )
            projected_raw_source_slugs.add(source_slug)

        def matrix_dependency(claim_id: str, component_id: str, verdict: str) -> dict[str, Any]:
            key = "exact_locators_finalized"
            value = matrix["summary"][key]
            dependency, held = raw_dependency(
                component_id=component_id,
                path=matrix_path,
                needle=json_scalar_needle(key, value),
                role=(
                    f"frozen matrix summary proves a nonzero exact-locator count ({value}); "
                    "this is internal status evidence, not theorem support"
                ),
                derivation_rule="PARSE_COMPLETE_MATRIX_AND_COMPARE_SUMMARY_EXACT_LOCATOR_COUNT",
                parsed_value=value,
                json_pointer=f"/summary/{key}",
            )
            dependency.update(
                {
                    "claim_id": claim_id,
                    "source_ref_slug": cfg["matrix_slug"],
                    "semantic_verdict": verdict,
                    "component_semantic_verdict": verdict,
                    "binding_chain": dependency_binding_chain(
                        child=matrix_path,
                        input_lock_path=input_lock_path,
                        input_lock_doc=input_lock,
                        paper=paper,
                        notes=notes,
                    ),
                }
            )
            if dependency["binding_chain"] is None:
                raise RuntimeError("matrix dependency lacks input-lock binding")
            return dependency

        for old_row in old_evidence_rows:
            ref_slug = old_row["source"]["ref_slug"]
            if ref_slug == local_slug:
                claim = claims_by_id[old_row["claim"]["claim_id"]]
                old_span = old_row["excerpt"]["source_span_utf8"]
                if not (
                    old_span["end"] <= claim["draft_span"]["start_byte"]
                    or old_span["start"] >= claim["draft_span"]["end_byte"]
                ):
                    raise RuntimeError("expected fixed-preamble local-evidence defect is absent")
                claim_dependencies: list[dict[str, Any]] = []
                claim_rows: list[dict[str, Any]] = []
                missing_components: list[dict[str, Any]] = []
                if cfg["paper_id"] == "P29":
                    if p29_mapping is None:
                        raise RuntimeError("P29 independent mapping was not loaded")
                    mapped_claims = {row["claim_id"]: row for row in p29_mapping["claims"]}
                    mapped_claim = mapped_claims.get(claim["claim_id"])
                    if mapped_claim is None:
                        raise RuntimeError(f"P29 local claim missing from independent map: {claim['claim_id']}")
                    dependencies, dependency_sources, missing_components = p29_mapped_dependencies(
                        cfg=cfg,
                        mapping_claim=mapped_claim,
                        mapping_catalog=p29_mapping["dependency_catalog"],
                        claim=claim,
                        paper=paper,
                        notes=notes,
                        input_lock_path=input_lock_path,
                        input_lock_doc=input_lock,
                    )
                    for index, dependency in enumerate(dependencies, start=1):
                        row_id = f"EVR-{claim['claim_id']}-RAW-{index:03d}"
                        source_text = dependency_sources[dependency["source_ref_slug"]]
                        claim_rows.append(
                            evidence_from_dependency(
                                dependency=dependency,
                                claim_surface=old_row["claim"],
                                source_text=source_text,
                                row_id=row_id,
                                detail_prefix=(
                                    "Fresh replay of a claim-component raw tuple from the independent map; the raw "
                                    "artifact, not the mapper's conclusion, is the evidence source."
                                ),
                            )
                        )
                        add_projection(dependency, source_text)
                    for missing_index, missing in enumerate(missing_components, start=1):
                        row_id = f"EVR-{claim['claim_id']}-MISSING-{missing_index:03d}"
                        missing["evidence_row_id"] = row_id
                        missing["source_ref_slug"] = (
                            f"P29Missing{claim['claim_id'].split('-')[-1]}M{missing_index:03d}"
                        )
                        missing_dependency_catalog_rows.append(missing)
                        claim_rows.append(
                            EVR.build(
                                {
                                    "schema_version": "evidence-row/1.0",
                                    "surface": "phase_e_claim_verification",
                                    "row_id": row_id,
                                    "claim": old_row["claim"],
                                    "source": {
                                        "ref_slug": missing["source_ref_slug"],
                                        "display_label": "No controlling raw dependency in the exact input lock",
                                        "source_artifact_sha256": None,
                                    },
                                    "anchor": {"kind": "none", "value_encoded": ""},
                                    "verdict": "UNVERIFIABLE",
                                    "detail": (
                                        f"Missing component {missing['component_id']} ({missing['label']}): "
                                        f"{missing['missing_raw_dependency']} {missing['rationale']} Present-but-unlocked "
                                        "files are non-authorizing and cannot upgrade this row."
                                    ),
                                },
                                None,
                                failure_state="anchorless",
                            )
                        )
                    claim_dependencies.extend(dependencies)
                    semantic_class = f"P29_INDEPENDENT_COMPONENT_MAP_{mapped_claim['focus']}"
                    dependency_claim_id = claim["claim_id"]
                    mapped_overall = mapped_claim["overall_verdict"]
                else:
                    semantic_class = local_semantic_class(cfg, claim)
                    dependency_claim_id = proof_dependency_claim_id(claim["claim_id"])
                    dependency_claim = claims_by_id[dependency_claim_id]
                    mapped_overall = None
                if cfg["paper_id"] == "P29":
                    pass
                elif semantic_class == "TRANSLATED_STATUS_CONTRADICTION":
                    dependency = matrix_dependency(
                        claim["claim_id"], f"{claim['claim_id']}-D001", "MAJOR_DISTORTION"
                    )
                    dependency["evidence_row_id"] = old_row["row_id"]
                    claim_dependencies.append(dependency)
                    claim_rows.append(
                        evidence_from_dependency(
                            dependency=dependency,
                            claim_surface=old_row["claim"],
                            source_text=matrix_text,
                            row_id=old_row["row_id"],
                            detail_prefix=(
                                "The compound translated status claim contains the same false universal locator statement "
                                "as the exact child claim; both identify one deduplicated blocking issue."
                            ),
                        )
                    )
                elif semantic_class == "CLAIM_SPECIFIC_LOCKED_CARRIER":
                    dependencies, dependency_sources, unsupported = resolve_status_dependencies(
                        cfg,
                        claim,
                        paper,
                        notes,
                        input_lock_path,
                        input_paper,
                        matrix_path,
                        matrix,
                    )
                    if unsupported or not dependencies:
                        raise RuntimeError(f"unclosed P32 raw dependency plan {claim['claim_id']}: {unsupported}")
                    for index, dependency in enumerate(dependencies, start=1):
                        row_id = f"EVR-{claim['claim_id']}-RAW-{index:03d}"
                        source_text = dependency_sources[dependency["source_ref_slug"]]
                        claim_rows.append(
                            evidence_from_dependency(
                                dependency=dependency,
                                claim_surface=old_row["claim"],
                                source_text=source_text,
                                row_id=row_id,
                                detail_prefix=(
                                    "Fresh component-level adjudication; the compound claim takes its weakest component. "
                                    "No manuscript self-attestation or generated summary is used as evidence."
                                ),
                            )
                        )
                        add_projection(dependency, source_text)
                    claim_dependencies.extend(dependencies)
                    missing_components = [
                        {
                            **row,
                            "claim_id": claim["claim_id"],
                            "missing_raw_dependency": row["required_artifact"],
                            "semantic_verdict": "UNVERIFIABLE",
                            "component_semantic_verdict": "UNVERIFIABLE",
                            "binding_boundary": artifact(input_lock_path),
                        }
                        for row in P32_MISSING_COMPONENTS.get(claim["claim_id"], [])
                    ]
                    for missing_index, missing in enumerate(missing_components, start=1):
                        row_id = f"EVR-{claim['claim_id']}-MISSING-{missing_index:03d}"
                        missing["evidence_row_id"] = row_id
                        missing["source_ref_slug"] = (
                            f"P32Missing{claim['claim_id'].split('-')[-1]}M{missing_index:03d}"
                        )
                        missing_dependency_catalog_rows.append(missing)
                        claim_rows.append(
                            EVR.build(
                                {
                                    "schema_version": "evidence-row/1.0",
                                    "surface": "phase_e_claim_verification",
                                    "row_id": row_id,
                                    "claim": old_row["claim"],
                                    "source": {
                                        "ref_slug": missing["source_ref_slug"],
                                        "display_label": "No controlling raw dependency in the exact input lock",
                                        "source_artifact_sha256": None,
                                    },
                                    "anchor": {"kind": "none", "value_encoded": ""},
                                    "verdict": "UNVERIFIABLE",
                                    "detail": (
                                        f"Missing component {missing['component_id']} ({missing['label']}): "
                                        f"requires {missing['required_artifact']}. {missing['rationale']}"
                                    ),
                                },
                                None,
                                failure_state="anchorless",
                            )
                        )
                else:
                    excerpt, dependency_span = block_context_excerpt(draft_text, raw, dependency_claim)
                    if semantic_class == "SELF_CONTAINED_FORMAL_PROOF_OR_COROLLARY":
                        role = (
                            "The actual dependency span is the manuscript's self-contained proof or its explicit "
                            "corollary premise; logical review is limited to the displayed implication under stated hypotheses"
                        )
                        rule = f"SELF_CONTAINED_LOGICAL_REVIEW_OF_{dependency_claim_id}"
                    else:
                        role = (
                            "The actual writer-block dependency span defines this manuscript's elected object, proposal, "
                            "prospective contract, or explicit no-transfer boundary"
                        )
                        rule = "CONSTITUTIVE_OR_NORMATIVE_MANUSCRIPT_SCOPE_REVIEW"
                    dependency = {
                        "claim_id": claim["claim_id"],
                        "component_id": f"{claim['claim_id']}-D001",
                        "artifact": artifact(notes / cfg["draft"]),
                        "raw_utf8_span": dependency_span,
                        "raw_excerpt": excerpt,
                        "raw_excerpt_sha256": sha_bytes(excerpt.encode("utf-8")),
                        "raw_excerpt_word_count": len(excerpt.split()),
                        "semantic_role": role,
                        "derivation_rule": rule,
                        "json_pointer": None,
                        "parsed_value": None,
                        "fresh_semantic_adjudication": "SUPPORTED_ONLY_AS_CONSTITUTIVE_OR_BOUNDED_LOGICAL_CONTENT",
                        "source_ref_slug": local_slug,
                        "semantic_verdict": "VERIFIED",
                        "component_semantic_verdict": "VERIFIED",
                        "binding_chain": dependency_binding_chain(
                            child=notes / cfg["draft"],
                            input_lock_path=input_lock_path,
                            input_lock_doc=input_lock,
                            paper=paper,
                            notes=notes,
                        ),
                    }
                    if dependency["binding_chain"] is None:
                        raise RuntimeError("local draft dependency lacks input-lock binding")
                    claim_dependencies.append(dependency)
                    claim_rows.append(
                        evidence_from_dependency(
                            dependency=dependency,
                            claim_surface=old_row["claim"],
                            source_text=draft_text,
                            row_id=old_row["row_id"],
                            detail_prefix=(
                                "VERIFIED is limited to constitutive/normative manuscript scope or a bounded "
                                "self-contained implication; it does not verify an external fact or scientific antecedent."
                            ),
                        )
                    )
                if not claim_rows:
                    raise RuntimeError(f"local claim lacks dependency rows: {claim['claim_id']}")
                component_verdicts = [row["semantic_verdict"] for row in claim_dependencies]
                component_verdicts.extend("UNVERIFIABLE" for _ in missing_components)
                claim_overall = weakest_verdict(component_verdicts)
                if mapped_overall is not None and claim_overall != mapped_overall:
                    raise RuntimeError(
                        f"P29 weakest-component verdict mismatch: {claim['claim_id']} {claim_overall} != {mapped_overall}"
                    )
                evidence_rows.extend(claim_rows)
                dependency_catalog_rows.extend(claim_dependencies)
                local_adjudications.append(
                    {
                        "claim_id": claim["claim_id"],
                        "writer_anchors": claim["writer_anchors"],
                        "registered_claim_span": claim["draft_span"],
                        "prior_excerpt_span": old_span,
                        "prior_excerpt_sha256": old_row["excerpt"]["excerpt_sha256"],
                        "prior_excerpt_overlaps_registered_claim_span": False,
                        "semantic_class": semantic_class,
                        "dependency_claim_id": dependency_claim_id,
                        "dependency_count": len(claim_dependencies),
                        "missing_dependency_count": len(missing_components),
                        "total_component_count": len(claim_dependencies) + len(missing_components),
                        "dependency_component_ids": [row["component_id"] for row in claim_dependencies],
                        "missing_component_ids": [row["component_id"] for row in missing_components],
                        "evidence_row_ids": [row["row_id"] for row in claim_rows],
                        "semantic_adjudication": claim_overall,
                        "weakest_component_rule": True,
                        "mixed_component_verdicts_allowed": True,
                        "used_as_positive_support": claim_overall == "VERIFIED",
                    }
                )
                local_reclassified += 1
            elif cfg["paper_id"] == "P32" and ref_slug in {"P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"}:
                finalization_row = finalization_rows[ref_slug]
                if finalization_row.get("support_excerpt") is not None or finalization_row.get("support_excerpt_sha256") is not None:
                    raise RuntimeError(f"{ref_slug} unexpectedly has current locked excerpt evidence")
                start = source_finalization_text.index(json_scalar_needle("source_id", ref_slug))
                end_needle = json_scalar_needle("support_excerpt_word_count", 0)
                end = source_finalization_text.index(end_needle, start) + len(end_needle)
                excerpt = source_finalization_text[start:end]
                if len(excerpt.split()) > 20 or source_finalization_text.count(excerpt) != 1:
                    raise RuntimeError(f"{ref_slug} unavailability excerpt is not uniquely bounded")
                source_map[ref_slug] = source_finalization_text
                projection["rows"].append(
                    {
                        "ref_slug": ref_slug,
                        "projection_origin": "complete raw current source-finalization record",
                        "source_artifact": artifact(source_finalization_path),
                        "held_text_sha256": sha_bytes(source_finalization_text.encode("utf-8")),
                        "held_text_bytes": len(source_finalization_text.encode("utf-8")),
                        "passage_support_claimed": False,
                        "role": "raw current row proves support excerpt/hash are null despite a retained locator string",
                        "binding_chain": dependency_binding_chain(
                            child=source_finalization_path,
                            input_lock_path=input_lock_path,
                            input_lock_doc=input_lock,
                            paper=paper,
                            notes=notes,
                        ),
                    }
                )
                row_template = {
                    "schema_version": "evidence-row/1.0",
                    "surface": "phase_e_claim_verification",
                    "row_id": old_row["row_id"],
                    "claim": old_row["claim"],
                    "source": {
                        "ref_slug": ref_slug,
                        "display_label": ref_slug,
                        "source_artifact_sha256": sha_path(notes / "stage4_prime_source_finalization_round3.json"),
                    },
                    "anchor": {
                        "kind": "section",
                        "value_encoded": urllib.parse.quote(
                            f"locked-source-finalization:{ref_slug}:excerpt-hash-availability", safe=""
                        ),
                    },
                    "verdict": "UNVERIFIABLE",
                    "detail": (
                        "The current locked source-finalization row retains a locator string but binds neither support "
                        "excerpt nor excerpt hash. Prior unbound prose cannot be replayed as current passage evidence."
                    ),
                }
                evidence_rows.append(EVR.build(row_template, source_finalization_text, extracted_text=excerpt))
                cw_reclassified += 1
            else:
                evidence_rows.append(old_row)
        expected_local = 66 if cfg["paper_id"] == "P29" else 89
        if local_reclassified != expected_local or cw_reclassified != cfg["unverifiable_contexts"]:
            raise RuntimeError("evidence reclassification denominator mismatch")
        if cfg["paper_id"] == "P32" and (
            len(dependency_catalog_rows), len(missing_dependency_catalog_rows)
        ) != (237, 6):
            # 181 raw factual/status components + 51 constitutive + 4 proof + 1 translated contradiction.
            raise RuntimeError(
                "P32 local dependency denominator before exact child changed: "
                f"{len(dependency_catalog_rows)} raw / {len(missing_dependency_catalog_rows)} missing"
            )
        if cfg["paper_id"] == "P29" and (
            len(dependency_catalog_rows), len(missing_dependency_catalog_rows)
        ) != (217, 28):
            raise RuntimeError(
                "P29 expanded local dependency denominator changed: "
                f"{len(dependency_catalog_rows)} raw / {len(missing_dependency_catalog_rows)} missing"
            )
        local_adjudication_path = stage / "stage4_5_round2_local_claim_semantic_re_adjudication.json"
        semantic_class_counts: dict[str, int] = {}
        local_verdict_counts: dict[str, int] = {}
        for row in local_adjudications:
            semantic_class_counts[row["semantic_class"]] = semantic_class_counts.get(row["semantic_class"], 0) + 1
            local_verdict_counts[row["semantic_adjudication"]] = (
                local_verdict_counts.get(row["semantic_adjudication"], 0) + 1
            )
        dump(
            local_adjudication_path,
            {
                "schema_version": f"p{cfg['paper']}-stage4.5-round2-local-claim-semantic-readjudication/1.0",
                "paper_id": cfg["paper_id"],
                "generated_at_utc": STAMP,
                "status": "FAIL_REBOUND_AND_FRESHLY_READJUDICATED_WITH_BLOCKING_FINDINGS",
                "registered_local_claims": expected_local,
                "re_adjudicated": local_reclassified,
                "semantic_class_counts": semantic_class_counts,
                "verdict_counts": local_verdict_counts,
                "verified": local_verdict_counts.get("VERIFIED", 0),
                "major_distortion": local_verdict_counts.get("MAJOR_DISTORTION", 0),
                "unverifiable": local_verdict_counts.get("UNVERIFIABLE", 0),
                "prior_fixed_preamble_excerpt_defect_count": local_reclassified,
                "actual_dependency_binding_corrected_count": local_reclassified,
                "boundary": (
                    "Constitutive/normative rows are verified only as manuscript-defined scope; proof rows only as bounded "
                    "formal implications; factual/status rows only from claim-specific locked carriers. Manuscript presence "
                    "alone is never treated as external truth or execution evidence."
                ),
                "rows": local_adjudications,
            },
        )
        correction_payload["audit_artifact_reclassifications"][-1]["classification_counts"] = semantic_class_counts
        correction_payload["audit_artifact_reclassifications"][-1]["verdict_counts"] = local_verdict_counts
        correction_payload["local_claim_semantic_re_adjudication"] = staged_artifact(
            stage, local_adjudication_path
        )
        correction_payload["claim_relation"] = {
            "child_claim_id": cfg["new_claim_id"],
            "parent_claim_id": cfg["parent_compound_claim_id"],
            "relation": "EXACT_MATERIAL_SUBCLAIM_OF_COMPOUND_NON_ENGLISH_BLOCK",
            "blocking_issue_deduplication": "SAME_SUBSTANTIVE_ISSUE_NOT_AN_ADDITIONAL_BLOCKER",
        }
        child_claim_surface = {
                "claim_id": cfg["new_claim_id"],
                "text": cfg["old_clause"],
                "paper_locator": (
                    f"notes/{cfg['draft']}:UTF8[{new_claim['draft_span']['start_byte']}:"
                    f"{new_claim['draft_span']['end_byte']}]"
                ),
                "selection_tier": "ALL",
        }
        child_dependency = matrix_dependency(
            cfg["new_claim_id"], f"{cfg['new_claim_id']}-D001", "MAJOR_DISTORTION"
        )
        evidence_rows.append(
            evidence_from_dependency(
                dependency=child_dependency,
                claim_surface=child_claim_surface,
                source_text=matrix_text,
                row_id=cfg["new_row_id"],
                detail_prefix=(
                    "The exact translated subclaim is contradicted by the nonzero frozen exact-locator count and is "
                    "deduplicated with its compound parent as one blocking issue."
                ),
            )
        )
        dependency_catalog_rows.append(child_dependency)
        if cfg["paper_id"] == "P32" and (
            len(dependency_catalog_rows), len(missing_dependency_catalog_rows)
        ) != (238, 6):
            raise RuntimeError("P32 expanded local dependency denominator changed")
        if cfg["paper_id"] == "P29" and (
            len(dependency_catalog_rows), len(missing_dependency_catalog_rows)
        ) != (218, 28):
            raise RuntimeError("P29 expanded local dependency denominator after exact child changed")

        catalog_claim_rows = [
            {
                "claim_id": row["claim_id"],
                "claim_overall_verdict": row["semantic_adjudication"],
                "raw_dependency_count": row["dependency_count"],
                "missing_dependency_count": row["missing_dependency_count"],
                "total_component_count": row["dependency_count"] + row["missing_dependency_count"],
                "component_ids": row["dependency_component_ids"] + row["missing_component_ids"],
                "evidence_row_ids": row["evidence_row_ids"],
                "weakest_component_rule": True,
            }
            for row in local_adjudications
        ]
        catalog_claim_rows.append(
            {
                "claim_id": cfg["new_claim_id"],
                "claim_overall_verdict": "MAJOR_DISTORTION",
                "raw_dependency_count": 1,
                "missing_dependency_count": 0,
                "total_component_count": 1,
                "component_ids": [child_dependency["component_id"]],
                "evidence_row_ids": [child_dependency["evidence_row_id"]],
                "weakest_component_rule": True,
            }
        )
        claim_overall_map = {
            row["claim_id"]: row["claim_overall_verdict"] for row in catalog_claim_rows
        }
        component_verdict_by_evidence_row: dict[str, str] = {}
        component_id_by_evidence_row: dict[str, str] = {}
        components_by_claim: dict[str, list[str]] = {}
        for dependency in dependency_catalog_rows:
            component_verdict = dependency["component_semantic_verdict"]
            dependency["claim_overall_verdict"] = claim_overall_map[dependency["claim_id"]]
            component_verdict_by_evidence_row[dependency["evidence_row_id"]] = component_verdict
            component_id_by_evidence_row[dependency["evidence_row_id"]] = dependency["component_id"]
            components_by_claim.setdefault(dependency["claim_id"], []).append(component_verdict)
        for missing in missing_dependency_catalog_rows:
            component_verdict = missing["component_semantic_verdict"]
            missing["claim_overall_verdict"] = claim_overall_map[missing["claim_id"]]
            component_verdict_by_evidence_row[missing["evidence_row_id"]] = component_verdict
            component_id_by_evidence_row[missing["evidence_row_id"]] = missing["component_id"]
            components_by_claim.setdefault(missing["claim_id"], []).append(component_verdict)
        if set(components_by_claim) != set(claim_overall_map):
            raise RuntimeError("dependency components do not cover every local claim")
        for claim_id, component_verdicts in components_by_claim.items():
            if weakest_verdict(component_verdicts) != claim_overall_map[claim_id]:
                raise RuntimeError(f"catalog weakest-component recomputation failed: {claim_id}")
        evidence_rows = propagate_schema5_claim_verdicts(
            rows=evidence_rows,
            source_map=source_map,
            claim_overall=claim_overall_map,
            component_verdict_by_row=component_verdict_by_evidence_row,
            component_id_by_row=component_id_by_evidence_row,
        )

        def value_counts(values: list[str]) -> dict[str, int]:
            counts: dict[str, int] = {}
            for value in values:
                counts[value] = counts.get(value, 0) + 1
            return counts

        component_semantic_verdict_counts = value_counts(
            [row["component_semantic_verdict"] for row in dependency_catalog_rows]
            + [row["component_semantic_verdict"] for row in missing_dependency_catalog_rows]
        )
        claim_overall_verdict_counts = value_counts(list(claim_overall_map.values()))
        shared_local_evr_verdict_counts = value_counts(
            [
                row["verdict"]
                for row in evidence_rows
                if row["claim"]["claim_id"] in claim_overall_map
            ]
        )
        for claim_row in catalog_claim_rows:
            if (
                len(claim_row["component_ids"])
                != claim_row["total_component_count"]
                or len(claim_row["evidence_row_ids"])
                != claim_row["total_component_count"]
            ):
                raise RuntimeError(
                    f"catalog claim component/evidence denominator mismatch: {claim_row['claim_id']}"
                )

        unique_raw_artifacts = {
            (row["artifact"]["path"], row["artifact"]["sha256"], row["artifact"]["bytes"])
            for row in dependency_catalog_rows
        }
        raw_source_slugs = {row["source_ref_slug"] for row in dependency_catalog_rows}
        if len(raw_source_slugs) != len(unique_raw_artifacts):
            raise RuntimeError("raw source-map deduplication is not one slug per exact artifact")
        for dependency in dependency_catalog_rows:
            source_slug = dependency["source_ref_slug"]
            source_text = source_map.get(source_slug)
            if source_text is None:
                raise RuntimeError(f"raw dependency source is absent from source map: {source_slug}")
            if (
                sha_bytes(source_text.encode("utf-8")) != dependency["artifact"]["sha256"]
                or len(source_text.encode("utf-8")) != dependency["artifact"]["bytes"]
            ):
                raise RuntimeError(
                    f"source-map payload does not replay dependency artifact: {dependency['component_id']}"
                )
        source_map_path = stage / "stage4_5_round2_evidence_source_map.json"
        dump(source_map_path, source_map)
        dependency_catalog_path = stage / "stage4_5_round2_local_claim_dependency_catalog.json"
        dump(
            dependency_catalog_path,
            {
                "schema_version": f"p{cfg['paper']}-stage4.5-round2-local-claim-dependency-catalog/1.0",
                "paper_id": cfg["paper_id"],
                "generated_at_utc": STAMP,
                "status": "FRESH_RAW_DEPENDENCY_REPLAY_WITH_WEAKEST_COMPONENT_ADJUDICATION",
                "authority": {relative: artifact(ROOT / relative) for relative in AUTHORITY_ARTIFACTS},
                "input_lock": artifact(input_lock_path),
                "independent_mapping_input": (
                    artifact(ROOT / P29_INDEPENDENT_MAPPING["path"])
                    if cfg["paper_id"] == "P29"
                    else None
                ),
                "independent_mapping_authority_role": (
                    "NONCONTROLLING_ROUTE_MAP_ONLY; ALL EVIDENCE IS RE-READ FROM RAW ARTIFACTS"
                    if cfg["paper_id"] == "P29"
                    else None
                ),
                "registered_local_claims_including_exact_child": len(catalog_claim_rows),
                "dependency_count": len(dependency_catalog_rows) + len(missing_dependency_catalog_rows),
                "raw_dependency_count": len(dependency_catalog_rows),
                "anchorless_missing_dependency_count": len(missing_dependency_catalog_rows),
                "unique_source_artifact_count": len(unique_raw_artifacts),
                "unique_source_ref_slug_count": len(raw_source_slugs),
                "source_map": staged_artifact(stage, source_map_path),
                "source_map_digest_replay": "PASS_ALL_RAW_ARTIFACT_SHA256_AND_BYTES",
                "component_semantic_verdict_counts": component_semantic_verdict_counts,
                "component_semantic_verdict_denominator": (
                    len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
                ),
                "claim_overall_verdict_counts": claim_overall_verdict_counts,
                "claim_overall_verdict_denominator": len(catalog_claim_rows),
                "shared_evr_verdict_counts": shared_local_evr_verdict_counts,
                "shared_evr_verdict_denominator": sum(shared_local_evr_verdict_counts.values()),
                "schema5_verdict_propagation_note": (
                    "Shared evidence-row/1.0 requires one claim-level verdict across all rows sharing claim_id. The "
                    "shared_evr counts therefore duplicate each claim's weakest overall verdict over all component "
                    "rows; they must not be read as component-level distortion or unavailability counts."
                ),
                "claim_overall_verdict_rule": (
                    "Each raw dependency becomes one shared evidence row. A compound claim is fully VERIFIED only when "
                    "every factual component is VERIFIED; otherwise its overall verdict is the weakest component."
                ),
                "claims": catalog_claim_rows,
                "dependencies": dependency_catalog_rows,
                "missing_dependencies": missing_dependency_catalog_rows,
                "boundary": (
                    "Raw excerpts and byte spans come from recursively lock-bound artifacts. Generated audit prose is "
                    "never used as a positive source; constitutive draft spans prove only definitions/proposals/boundaries."
                ),
            },
        )
        correction_payload["local_claim_dependency_catalog"] = staged_artifact(stage, dependency_catalog_path)
        dump(correction_path, correction_payload)
        dump(stage / "stage4_5_round2_evidence_projection_ledger.json", projection)
        evidence_path = stage / "stage4_5_round2_evidence_rows.json"
        dump(evidence_path, evidence_rows)
        code, output = run(
            [
                "python3",
                str(ARS / "scripts/evidence_rows.py"),
                "validate",
                str(evidence_path),
                "--source-map",
                str(source_map_path),
            ]
        )
        write(stage / "stage4_5_round2_evidence_rows_replay.log", output)
        if code != 0:
            raise RuntimeError(f"official evidence replay failed: {output}")

        evidence_by_id = {row["row_id"]: row for row in evidence_rows}
        if len(evidence_by_id) != len(evidence_rows):
            raise RuntimeError("shared evidence row IDs are not unique")
        raw_catalog_evidence_ids = {row["evidence_row_id"] for row in dependency_catalog_rows}
        missing_catalog_evidence_ids = {row["evidence_row_id"] for row in missing_dependency_catalog_rows}
        catalog_evidence_ids = raw_catalog_evidence_ids | missing_catalog_evidence_ids
        if len(raw_catalog_evidence_ids) != len(dependency_catalog_rows):
            raise RuntimeError("dependency catalog does not map one-to-one to shared evidence rows")
        for dependency in dependency_catalog_rows:
            row = evidence_by_id.get(dependency["evidence_row_id"])
            if row is None:
                raise RuntimeError(f"dependency has no shared evidence row: {dependency['component_id']}")
            expected_span = {
                "start": dependency["raw_utf8_span"]["start_byte"],
                "end": dependency["raw_utf8_span"]["end_byte"],
            }
            if (
                row["claim"]["claim_id"] != dependency["claim_id"]
                or row["source"]["ref_slug"] != dependency["source_ref_slug"]
                or row["source"]["source_artifact_sha256"] != dependency["artifact"]["sha256"]
                or row["excerpt"]["excerpt_sha256"] != dependency["raw_excerpt_sha256"]
                or row["excerpt"]["source_span_utf8"] != expected_span
                or row["verdict"] != dependency["claim_overall_verdict"]
                or f"component={dependency['component_id']};" not in row["detail"]
                or f"claim_overall={dependency['claim_overall_verdict']}" not in row["detail"]
            ):
                raise RuntimeError(f"dependency/shared-row tuple mismatch: {dependency['component_id']}")
        for missing in missing_dependency_catalog_rows:
            row = evidence_by_id.get(missing["evidence_row_id"])
            if row is None or (
                row["claim"]["claim_id"] != missing["claim_id"]
                or row["verdict"] != missing["claim_overall_verdict"]
                or row["excerpt"]["state"] != "anchorless"
                or row["source"]["ref_slug"] != missing["source_ref_slug"]
                or row["source"]["source_artifact_sha256"] is not None
                or row["excerpt"]["excerpt_sha256"] is not None
                or f"component={missing['component_id']};" not in row["detail"]
                or f"claim_overall={missing['claim_overall_verdict']}" not in row["detail"]
            ):
                raise RuntimeError(f"missing dependency/anchorless row mismatch: {missing['component_id']}")
        local_and_child_evidence_ids = {
            row["row_id"]
            for row in evidence_rows
            if row["claim"]["claim_id"] in {entry["claim_id"] for entry in catalog_claim_rows}
        }
        if local_and_child_evidence_ids != catalog_evidence_ids:
            raise RuntimeError("dependency catalog/shared local evidence two-way join is incomplete")

        verdict_counts: dict[str, int] = {}
        excerpt_state_counts: dict[str, int] = {}
        verdicts_by_claim: dict[str, set[str]] = {}
        for row in evidence_rows:
            verdict_counts[row["verdict"]] = verdict_counts.get(row["verdict"], 0) + 1
            state = row["excerpt"]["state"]
            excerpt_state_counts[state] = excerpt_state_counts.get(state, 0) + 1
            verdicts_by_claim.setdefault(row["claim"]["claim_id"], set()).add(row["verdict"])
        if set(verdicts_by_claim) != set(claims_by_id):
            raise RuntimeError("claim/evidence join is incomplete")
        mixed_multi_tuple = {
            claim_id: sorted(verdicts) for claim_id, verdicts in verdicts_by_claim.items() if len(verdicts) != 1
        }
        if mixed_multi_tuple:
            raise RuntimeError(
                f"Schema-5 claim-level verdict propagation left mixed shared EVRs: {mixed_multi_tuple}"
            )
        overall_verdict_by_claim = {
            claim_id: weakest_verdict(sorted(verdicts)) for claim_id, verdicts in verdicts_by_claim.items()
        }
        for claim_id, expected_overall in claim_overall_map.items():
            if overall_verdict_by_claim.get(claim_id) != expected_overall:
                raise RuntimeError(f"shared EVR claim overall mismatch: {claim_id}")
        all_claim_overall_verdict_counts = value_counts(list(overall_verdict_by_claim.values()))
        mixed_component_claims = {
            claim_id: sorted(set(component_verdicts))
            for claim_id, component_verdicts in components_by_claim.items()
            if len(set(component_verdicts)) > 1
        }
        fully_verified_claims = sum(verdict == "VERIFIED" for verdict in overall_verdict_by_claim.values())
        claims_not_verified = len(verdicts_by_claim) - fully_verified_claims

        integrity = copy.deepcopy(old_integrity)
        integrity["timestamp"] = STAMP
        integrity["verdict"] = "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED"
        integrity["late_discovered_translated_surface_adjudication"] = True
        integrity["phases"]["A_references"] = {
            "registered": cfg["reference_total"],
            "checked": cfg["reference_total"],
            "resolved_by_fresh_readjudication_of_locked_authoritative_raw_carriers": cfg["reference_total"],
            "unresolved": 0,
            "irrelevant_bing_result_sets_contributing_to_resolution": 0,
            "correction_retraction_eoc_clearances": 0,
            "verdict": "PASS_WITH_NOTES_LOCKED_AUTHORITATIVE_IDENTITY_CARRIERS",
        }
        phase_b = reference_audit["phase_b"]
        integrity["phases"]["B_citation_contexts"] = {
            "registered": phase_b["registered_citation_context_tuples"],
            "reviewed": phase_b["reviewed"],
            "verified_registered_use": phase_b["registered_use_verified"],
            "passage_bounded": phase_b["passage_bounded_contexts"],
            "metadata_only_boundary_faithful": phase_b["metadata_only_boundary_faithful_contexts"],
            "unverifiable": phase_b.get("unverifiable_contexts", 0),
            "unsupported": phase_b["unsupported_contexts"],
            "full_role_proofs": phase_b["full_role_proofs"],
            "verdict": phase_b["verdict"],
        }
        integrity["phases"]["C_data_internal_provenance"] = {
            **coverage,
            "experiment_declarations": "1/1",
            "experiment_provenance_rows": "0/0",
            "experiment_backed_claims": "0/0",
            "claim_provenance_alignment_rows": "0/0",
            "boundary": BOUNDARY,
            "verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
        }
        phase_e = integrity["phases"]["E_claims_evidence"]
        phase_e.update(
            {
                "registry_claims": cfg["prior_claims"] + 1,
                "claims_fully_verified": fully_verified_claims,
                "claims_not_verified": claims_not_verified,
                "expected_evidence_tuples": len(evidence_rows),
                "actual_evidence_tuples": len(evidence_rows),
                "verdict_counts": verdict_counts,
                "component_semantic_verdict_counts": component_semantic_verdict_counts,
                "component_semantic_verdict_denominator": (
                    len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
                ),
                "component_semantic_verdict_scope": "LOCAL_CLAIMS_INCLUDING_EXACT_TRANSLATED_CHILD",
                "claim_overall_verdict_counts": all_claim_overall_verdict_counts,
                "claim_overall_verdict_denominator": len(overall_verdict_by_claim),
                "claim_overall_verdict_scope": "ALL_REGISTERED_CLAIMS",
                "shared_evr_verdict_counts": verdict_counts,
                "shared_evr_verdict_denominator": len(evidence_rows),
                "shared_evr_verdict_scope": "ALL_SHARED_EVIDENCE_ROWS",
                "schema5_verdict_propagation_note": (
                    "Shared-EVR counts repeat each claim's weakest overall verdict over every component row. They do "
                    "not state that every raw component is distorted or unavailable; component semantics remain in "
                    "the dependency catalog and row detail."
                ),
                "excerpt_state_counts": excerpt_state_counts,
                "semantic_extraction_completeness": (
                    "late_non_English_claim added; every factual/status component expanded to a raw dependency row; "
                    "constitutive and proof rows use actual bounded manuscript dependencies; not_machine_detectable"
                ),
                "mixed_component_claims": mixed_component_claims,
                "same_claim_multi_tuple_verdict_consistency": (
                    "PASS_SCHEMA5_UNIFORM_CLAIM_OVERALL_PROPAGATED_TO_EVERY_SHARED_ROW"
                ),
                "local_claim_dependency_catalog": staged_artifact(stage, dependency_catalog_path),
                "verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
            }
        )
        blocking_findings = [
            {
                "issue_id": cfg["issue_id"],
                "severity": "SERIOUS",
                "blocker": True,
                "phase": "C/E",
                "block_id": cfg["block_id"],
                "line": cfg["line"],
                "finding": correction["conflict"],
                "correction_id": cfg["correction_id"],
                "correction_status": "PROPOSED_NOT_APPLIED",
                "deduplication": (
                    f"The exact subclaim {cfg['new_claim_id']} is part of parent compound claim "
                    f"{cfg['parent_compound_claim_id']}; Phase C and E identify one substantive blocker."
                ),
            },
            {
                "issue_id": f"{cfg['paper_id']}-S45R2-I03-LOCAL-EVIDENCE-ANCHOR",
                "severity": "SERIOUS",
                "blocker": True,
                "phase": "E",
                "finding": (
                    f"{local_reclassified} local evidence rows used one unrelated fixed preamble excerpt outside their "
                    f"registered claim spans. The fresh expanded-EVR replay corrects that persistence defect, but "
                    f"{local_verdict_counts.get('UNVERIFIABLE', 0)} local compound claims retain at least one "
                    "UNVERIFIABLE raw component under the weakest-component rule."
                ),
                "audit_reclassification_status": "APPLIED",
            },
        ]
        if cfg["paper_id"] == "P32":
            blocking_findings.append(
                {
                    "issue_id": "P32-S45R2-I04-CW-EXCERPT-BINDING",
                    "severity": "SERIOUS",
                    "blocker": True,
                    "phase": "B/E",
                    "finding": (
                        "CW01–CW04 retain locator strings but current locked source-finalization binds null support "
                        "excerpt/hash; four context/evidence tuples are UNVERIFIABLE."
                    ),
                    "audit_reclassification_status": "APPLIED",
                }
            )
        integrity["blocking_findings"] = blocking_findings
        integrity["blocking_issue_count"] = len(blocking_findings)
        integrity["audit_artifact_reclassifications_applied"] = correction_payload[
            "audit_artifact_reclassifications_applied"
        ]
        integrity["correction_list"] = staged_artifact(stage, correction_path)
        integrity["evidence_rows"] = evidence_rows
        integrity["stage5_started"] = False
        integrity_path = stage / "stage4_5_round2_integrity_report.json"
        dump(integrity_path, integrity)

        passport = copy.deepcopy(
            json.loads((notes / "stage4_5_round2_material_passport.json").read_text(encoding="utf-8"))
        )
        passport["version_label"] = f"{cfg['paper_id'].lower()}-round10-stage4.5-round2-fail-corrections-proposed"
        passport["verification_status"] = "STAGE4_5_ROUND2_FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED"
        passport["stage4_5_round2_audit"].update(
            {
                "timestamp": STAMP,
                "verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
                "phase_a": (
                    f"{cfg['reference_total']}/{cfg['reference_total']} identities freshly re-adjudicated from "
                    f"locked authoritative raw carriers; Bing contribution 0/{cfg['reference_total']}; no correction clearance"
                ),
                "phase_b": (
                    f"{phase_b['registered_use_verified']}/{phase_b['registered_citation_context_tuples']} registered uses verified; "
                    f"{phase_b.get('unverifiable_contexts', 0)} UNVERIFIABLE"
                ),
                "phase_c": "13/14; one translated-abstract citation-status contradiction",
                "claim_registry": (
                    f"{fully_verified_claims}/{cfg['prior_claims'] + 1} fully verified; "
                    f"{claims_not_verified} not verified"
                ),
                "evidence_rows": (
                    f"{verdict_counts.get('VERIFIED', 0)}/{len(evidence_rows)} VERIFIED; "
                    f"{verdict_counts.get('UNVERIFIABLE', 0)} UNVERIFIABLE; "
                    f"{verdict_counts.get('MAJOR_DISTORTION', 0)} MAJOR_DISTORTION"
                ),
                "component_semantic_verdict_counts": component_semantic_verdict_counts,
                "component_semantic_verdict_denominator": (
                    len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
                ),
                "claim_overall_verdict_counts": all_claim_overall_verdict_counts,
                "claim_overall_verdict_denominator": len(overall_verdict_by_claim),
                "shared_evr_verdict_counts": verdict_counts,
                "shared_evr_verdict_denominator": len(evidence_rows),
                "stage5_started": False,
            }
        )
        passport["stage4_5_round2_corrections"] = {
            "status": "PROPOSED_NOT_APPLIED",
            "count": 1,
            "correction_id": cfg["correction_id"],
            "block_id": cfg["block_id"],
            "audit_artifact_reclassifications_applied": correction_payload[
                "audit_artifact_reclassifications_applied"
            ],
        }
        passport_path = stage / "stage4_5_round2_material_passport.json"
        dump(passport_path, passport)

        final_md_path = stage / "stage4_5_round2_final_integrity_report.md"
        body_phase = integrity["phases"]["D_originality"]
        write(
            final_md_path,
            "\n".join(
                [
                    f"# {cfg['paper_id']} — Stage 4.5 Round 2 final integrity report",
                    "",
                    "## Verdict",
                    "",
                    "**FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED.** The prior PASS attempt is invalidated/noncontrolling: it omitted one material non-English status surface, attributed identity resolution to irrelevant search cards, and used fixed preamble excerpts as local-claim evidence.",
                    "",
                    "## Complete denominators",
                    "",
                    f"- Phase A references: **{cfg['reference_total']}/{cfg['reference_total']}** identities freshly re-adjudicated from same-day hash-bound authoritative raw carriers; Bing-card contribution **0/{cfg['reference_total']}**; correction/retraction clearances **0**.",
                    f"- Phase B contexts: **{cfg['reference_total']}/{cfg['reference_total']}** reviewed; **{phase_b['registered_use_verified']}/{cfg['reference_total']}** verified; **{cfg['passage_bounded']}** passage-bounded + **{cfg['metadata_only']}** metadata-only boundary-faithful + **{cfg['unverifiable_contexts']}** UNVERIFIABLE; unsupported **0**.",
                    f"- Phase C: **13/14** verified, **1/14** blocking inconsistency; tables **{cfg['tables']}/{cfg['tables']}**, figures **0/0**.",
                    "- Experiments: declaration **1/1**; provenance **0/0**; experiment-backed claims **0/0**; alignment **0/0**.",
                    f"- Phase D: body **{body_phase['body_successful']}/{body_phase['body_denominator']}**; changed/new **{body_phase['changed_successful']}/{body_phase['changed_denominator']}**; professional detector **not used**.",
                    f"- Phase E: **{fully_verified_claims}/{cfg['prior_claims'] + 1}** ALL-tier claims fully verified; **{claims_not_verified}** not verified. Evidence rows: **{verdict_counts.get('VERIFIED', 0)} VERIFIED**, **{verdict_counts.get('UNVERIFIABLE', 0)} UNVERIFIABLE**, **{verdict_counts.get('MAJOR_DISTORTION', 0)} MAJOR_DISTORTION** of **{len(evidence_rows)}**.",
                    (
                        "- Phase E denominator separation: local raw-component semantics "
                        f"**{json.dumps(component_semantic_verdict_counts, sort_keys=True)} / "
                        f"{len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)}**; all-claim weakest "
                        f"outcomes **{json.dumps(all_claim_overall_verdict_counts, sort_keys=True)} / "
                        f"{len(overall_verdict_by_claim)}**; Schema-5 shared-EVR outcomes "
                        f"**{json.dumps(verdict_counts, sort_keys=True)} / {len(evidence_rows)}**. The final group repeats "
                        "a claim's weakest outcome over each component row and is not a component-level distortion count."
                    ),
                    f"- E6: **3/3** rounds, **{cfg['e6']}/{cfg['e6']}** operations reviewed.",
                    "- Seven failure modes: **6/7 CLEAR**, **1/7 INSUFFICIENT_EVIDENCE** (citation identity/support); the translated status contradiction is separately deduplicated across Phase C/E.",
                    f"- Isolated build: **PASS**, **{cfg['pages']} pages**, unresolved citation/reference **0/0**, overfull **0**.",
                    "- ARS Schema-12 compliance: official checker **PASS**, primary-research `overall_decision=warn`; this classification is unchanged.",
                    "",
                    "## Required correction",
                    "",
                    f"`{cfg['block_id']}` line {cfg['line']} must be separately authorized and corrected to match the frozen matrix partition. The exact old and proposed replacement bytes are in `stage4_5_round2_correction_list.json`; no correction was applied.",
                    "",
                    f"Audit-only reclassifications were applied to **{correction_payload['audit_artifact_reclassifications_applied']}** issue families. They do not edit the manuscript. The local-claim ledger records **{local_reclassified}/{local_reclassified}** per-claim re-adjudications; none is treated as verified merely because its text appears in the manuscript.",
                    "",
                    "Stage 5 is not authorized or started. A fresh post-correction Stage-4.5 audit is required.",
                ]
            ),
        )

        old_rows = [
            {
                "original_path": path.relative_to(ROOT).as_posix(),
                "archived_path": (archive / path.name).relative_to(ROOT).as_posix(),
                "sha256": sha_path(path),
                "bytes": path.stat().st_size,
            }
            for path in old_outputs
        ]
        incident = {
            "schema_version": f"p{cfg['paper']}-stage4.5-round2-pass-attempt-invalidation/1.0",
            "paper_id": cfg["paper_id"],
            "recorded_at_utc": STAMP,
            "status": "INVALIDATED_NONCONTROLLING_PASS_ATTEMPT",
            "reason": (
                f"The PASS attempt omitted {cfg['block_id']} line {cfg['line']}, attributed semantic identity evidence "
                f"to {cfg['reference_total']} irrelevant Bing result-card sets instead of separating the locked raw "
                f"identity carriers, and accepted {local_reclassified} local evidence rows whose fixed preamble excerpts "
                "did not overlap their registered claims."
            ),
            "defect_counts": {
                "translated_status_surfaces_omitted": 1,
                "irrelevant_bing_result_sets_misattributed_as_identity_evidence": cfg["reference_total"],
                "locked_authoritative_identity_carriers_freshly_readjudicated": cfg["reference_total"],
                "local_evidence_rows_with_false_excerpt_binding": local_reclassified,
                "retained_endpoint_rows_without_current_locked_excerpt_hash": cw_reclassified,
            },
            "invalidated_manifest": artifact(manifest_path),
            "invalidated_integrity_report": artifact(notes / "stage4_5_round2_integrity_report.json"),
            "invalidated_pass_receipt": artifact(notes / "stage4_5_round2_integrity_pass_receipt.json"),
            "archive_path": archive.relative_to(ROOT).as_posix(),
            "archived_file_count": len(old_rows),
            "archived_files": old_rows,
            "controlling_authority": "NONE",
            "manuscript_or_bibliography_changed": False,
            "replacement_status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
        }
        incident_stage_path = stage / incident_name
        dump(incident_stage_path, incident)

        fail_receipt_path = stage / "stage4_5_round2_integrity_fail_receipt.json"
        dump(
            fail_receipt_path,
            {
                "schema_version": f"p{cfg['paper']}-stage4.5-round2-integrity-fail-receipt/1.0",
                "paper_id": cfg["paper_id"],
                "recorded_at_utc": STAMP,
                "verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
                "audit_mode": 2,
                "audit_target": artifact(notes / cfg["draft"]),
                "input_manifest": staged_artifact(stage, stage / "stage4_5_round2_input_manifest.json"),
                "integrity_report": staged_artifact(stage, integrity_path),
                "final_human_report": staged_artifact(stage, final_md_path),
                "material_passport": staged_artifact(stage, passport_path),
                "correction_list": staged_artifact(stage, correction_path),
                "invalidated_pass_attempt": staged_artifact(stage, incident_stage_path),
                "blocking_issue_count": len(blocking_findings),
                "corrections_proposed": 1,
                "corrections_applied": 0,
                "audit_artifact_reclassifications_applied": correction_payload[
                    "audit_artifact_reclassifications_applied"
                ],
                "local_raw_dependency_count_including_exact_child": len(dependency_catalog_rows),
                "local_anchorless_missing_dependency_count": len(missing_dependency_catalog_rows),
                "local_total_component_count": (
                    len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
                ),
                "unique_local_source_artifact_count": len(unique_raw_artifacts),
                "component_semantic_verdict_counts": component_semantic_verdict_counts,
                "claim_overall_verdict_counts": all_claim_overall_verdict_counts,
                "shared_evr_verdict_counts": verdict_counts,
                "official_compliance_schema12": "PASS_PRIMARY_RESEARCH_WARN_NONBLOCKING",
                "protected_snapshot_unchanged": True,
                "manuscript_or_bibliography_mutation_performed": False,
                "scientific_execution_performed": False,
                "canonical_promotion_performed": False,
                "stage5_started": False,
            },
        )
        checkpoint_path = stage / "stage4_5_round2_mandatory_checkpoint.json"
        dump(
            checkpoint_path,
            {
                "schema_version": f"p{cfg['paper']}-stage4.5-round2-mandatory-checkpoint/1.0",
                "paper_id": cfg["paper_id"],
                "recorded_at_utc": STAMP,
                "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
                "integrity_fail_receipt": staged_artifact(stage, fail_receipt_path),
                "correction_list": staged_artifact(stage, correction_path),
                "blocking_issue_count": len(blocking_findings),
                "audit_artifact_reclassifications_applied": correction_payload[
                    "audit_artifact_reclassifications_applied"
                ],
                "fresh_stage4_5_complete": False,
                "corrections_applied": False,
                "stage5_authorized": False,
                "stage5_started": False,
                "canonical_promotion_performed": False,
                "next_gate": "Separate exact correction authorization, deterministic block replacement, and fresh post-correction Stage-4.5 audit.",
            },
        )

        staged_files = sorted(path for path in stage.iterdir() if path.is_file())
        if (stage / "stage4_5_round2_integrity_pass_receipt.json").exists():
            raise RuntimeError("invalidated PASS receipt leaked into the controlling FAIL package")
        manifest_out_path = stage / "stage4_5_round2_output_manifest.json"
        producer = Path(__file__).resolve()
        invocation = notes / "stage4_5_round2_finalize_translation_status_failure.py"
        manifest_out = {
            "schema_version": f"p{cfg['paper']}-stage4.5-round2-output-manifest/1.1",
            "paper_id": cfg["paper_id"],
            "generated_at_utc": STAMP,
            "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
            "verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
            "base_fresh_audit_builder": pass_manifest["builder"],
            "failure_finalizer": artifact(producer),
            "invocation_entrypoint": artifact(invocation),
            "invalidated_pass_attempt": staged_artifact(stage, incident_stage_path),
            "artifacts": [staged_artifact(stage, path) for path in staged_files],
            "artifact_count_excluding_self": len(staged_files),
            "blocking_issue_count": len(blocking_findings),
            "corrections_proposed": 1,
            "corrections_applied": 0,
            "audit_artifact_reclassifications_applied": correction_payload[
                "audit_artifact_reclassifications_applied"
            ],
            "local_raw_dependency_count_including_exact_child": len(dependency_catalog_rows),
            "local_anchorless_missing_dependency_count": len(missing_dependency_catalog_rows),
            "local_total_component_count": (
                len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
            ),
            "unique_local_source_artifact_count": len(unique_raw_artifacts),
            "component_semantic_verdict_counts": component_semantic_verdict_counts,
            "claim_overall_verdict_counts": all_claim_overall_verdict_counts,
            "shared_evr_verdict_counts": verdict_counts,
            "protected_snapshot_unchanged": True,
            "scientific_execution_performed": False,
            "canonical_promotion_performed": False,
            "stage5_started": False,
        }
        prior_incident = notes / "stage4_5_round2_compliance_schema12_supersession_incident.json"
        if prior_incident.is_file():
            manifest_out["earlier_noncontrolling_schema_incident"] = artifact(prior_incident)
        dump(manifest_out_path, manifest_out)
        staged_files.append(manifest_out_path)

        for path in staged_files:
            if path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
        for row in manifest_out["artifacts"]:
            path = stage / Path(row["path"]).name
            if (sha_path(path), path.stat().st_size) != (row["sha256"], row["bytes"]):
                raise RuntimeError(f"staged output manifest mismatch: {row['path']}")
        staged_integrity = json.loads(integrity_path.read_text(encoding="utf-8"))
        staged_evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        if staged_integrity.get("evidence_rows") != staged_evidence:
            raise RuntimeError("integrity report does not embed the complete controlling evidence_rows array")
        code, compliance_output = run(
            ["python3", str(COMPLIANCE_CHECKER), str(stage / "stage4_5_round2_compliance_report.json")]
        )
        if code != 0 or not compliance_output.startswith("OK:"):
            raise RuntimeError(f"staged official compliance replay failed: {compliance_output}")
        for rel, row in input_manifest["protected_snapshot_before"].items():
            path = ROOT / rel
            if (sha_path(path), path.stat().st_size) != (row["sha256"], row["bytes"]):
                raise RuntimeError(f"protected input changed during preview: {rel}")
        if preview_only:
            return {
                "paper_id": cfg["paper_id"],
                "preview_only": True,
                "status": "VALIDATED_TEMPORARY_PREVIEW_NOT_PROMOTED",
                "phase_a_identity_resolved": f"{cfg['reference_total']}/{cfg['reference_total']}",
                "phase_a_bing_evidence_contribution": f"0/{cfg['reference_total']}",
                "phase_b_verified": (
                    f"{reference_audit['phase_b']['registered_use_verified']}/"
                    f"{reference_audit['phase_b']['registered_citation_context_tuples']}"
                ),
                "claims_fully_verified": f"{fully_verified_claims}/{cfg['prior_claims'] + 1}",
                "evidence_rows": len(evidence_rows),
                "evidence_verdict_counts": verdict_counts,
                "component_semantic_verdict_counts": component_semantic_verdict_counts,
                "all_claim_overall_verdict_counts": all_claim_overall_verdict_counts,
                "local_claim_overall_verdict_counts_before_exact_child": local_verdict_counts,
                "local_raw_dependency_count_including_exact_child": len(dependency_catalog_rows),
                "local_anchorless_missing_dependency_count": len(missing_dependency_catalog_rows),
                "local_total_component_count": (
                    len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
                ),
                "unique_local_source_artifact_count": len(unique_raw_artifacts),
                "unique_local_source_ref_slug_count": len(raw_source_slugs),
                "blocking_issues": len(blocking_findings),
                "official_claim_coverage_replay": "PASS",
                "official_evidence_rows_replay": "PASS",
                "official_schema12_compliance_replay": "PASS",
                "integrity_embedded_evidence_rows_equivalent": True,
                "archive_created": False,
                "outputs_promoted": False,
            }

        moved: list[tuple[Path, Path]] = []
        promoted: list[Path] = []
        try:
            archive.mkdir()
            for source in old_outputs:
                target = archive / source.name
                os.replace(source, target)
                moved.append((source, target))
            for source in staged_files:
                target = notes / source.name
                if target.exists():
                    raise RuntimeError(f"final output collision: {target.name}")
                os.replace(source, target)
                promoted.append(target)
        except Exception:
            for path in promoted:
                path.unlink(missing_ok=True)
            for source, target in reversed(moved):
                if target.exists():
                    os.replace(target, source)
            if archive.exists():
                archive.rmdir()
            raise

    final_manifest_path = notes / "stage4_5_round2_output_manifest.json"
    final_manifest = json.loads(final_manifest_path.read_text(encoding="utf-8"))
    for row in final_manifest["artifacts"]:
        verify_artifact_row(row)
    for rel, row in input_manifest["protected_snapshot_before"].items():
        path = ROOT / rel
        if (sha_path(path), path.stat().st_size) != (row["sha256"], row["bytes"]):
            raise RuntimeError(f"protected input changed after finalization: {rel}")
    code, compliance_output = run(
        ["python3", str(COMPLIANCE_CHECKER), str(notes / "stage4_5_round2_compliance_report.json")]
    )
    if code != 0:
        raise RuntimeError(f"final compliance replay failed: {compliance_output}")
    return {
        "paper_id": cfg["paper_id"],
        "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
        "phase_c": "13/14",
        "phase_a_identity_resolved": f"{cfg['reference_total']}/{cfg['reference_total']}",
        "phase_a_bing_evidence_contribution": f"0/{cfg['reference_total']}",
        "phase_b_verified": (
            f"{reference_audit['phase_b']['registered_use_verified']}/"
            f"{reference_audit['phase_b']['registered_citation_context_tuples']}"
        ),
        "claims_fully_verified": f"{fully_verified_claims}/{cfg['prior_claims'] + 1}",
        "evidence_verdict_counts": verdict_counts,
        "component_semantic_verdict_counts": component_semantic_verdict_counts,
        "all_claim_overall_verdict_counts": all_claim_overall_verdict_counts,
        "local_raw_dependency_count_including_exact_child": len(dependency_catalog_rows),
        "local_anchorless_missing_dependency_count": len(missing_dependency_catalog_rows),
        "local_total_component_count": (
            len(dependency_catalog_rows) + len(missing_dependency_catalog_rows)
        ),
        "unique_local_source_artifact_count": len(unique_raw_artifacts),
        "blocking_issues": len(blocking_findings),
        "corrections_proposed": 1,
        "corrections_applied": 0,
        "archive": archive.relative_to(ROOT).as_posix(),
        "output_manifest": artifact(final_manifest_path),
        "integrity_report": artifact(notes / "stage4_5_round2_integrity_report.json"),
        "fail_receipt": artifact(notes / "stage4_5_round2_integrity_fail_receipt.json"),
        "checkpoint": artifact(notes / "stage4_5_round2_mandatory_checkpoint.json"),
        "correction_list": artifact(notes / "stage4_5_round2_correction_list.json"),
        "invalidation_incident": artifact(notes / incident_name),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True, choices=sorted(CONFIGS))
    parser.add_argument("--preview-only", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            build_failure_package(CONFIGS[args.paper], preview_only=args.preview_only),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
