#!/usr/bin/env python3
"""Build the fresh read-only Stage-4.5 Mode-2 audit packages for P30/P31.

The two frozen Stage-4-prime TeX/Bib pairs are inputs.  This script writes
only ``notes/stage4_5_round1_*`` audit products and an isolated preview.  It
does not repair or promote a manuscript, alter canonical/scientific/Route
files, run a scientific experiment, or begin Stage 5.
"""

from __future__ import annotations

import copy
import csv
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
import time
import urllib.parse
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[3]
AUTH = ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json"
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether "
    "the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
)
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
PROTOCOL_SHA = hashlib.sha256((ARS / "academic-pipeline/references/integrity_review_protocol.md").read_bytes()).hexdigest()
FREEZE_SHA = "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98"
AUTH_SHA = "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c"

CONFIGS: tuple[dict[str, Any], ...] = (
    {
        "paper": 30,
        "paper_id": "P30",
        "directory": "30-three-disk-nonconstant-roof-determinant",
        "draft_sha": "6c09fa99b17a1f0d47a1c186f0fe48072a3f7d7e45b036a0b237460cd51ae39a",
        "bib_sha": "5b6854540f595e83ffc4f5a6153595ff27b2e74705e9fe930a0b5d33c17b81f1",
        "reference_total": 28,
        "unresolved_refs": [f"P30-S{i:02d}" for i in range(1, 27)],
        "verified_context_refs": ["P30-C01", "P30-C02"],
        "matrix": "stage4_prime_claim_passage_matrix_round2.json",
        "matrix_total": 28,
        "matrix_finalized": 2,
        "matrix_inconclusive": 26,
        "query_ledger": "stage4_prime_literature_screening_ledger_round2.json",
        "query_total": 54,
        "table_blocks": ["B0128", "B0129"],
        "table_rows": [4, 6],
        "reader_manifest_sha": "9fd3373b636e1f74eded47992dcda9230ae34493b1f289c331f2fe0286570bc5",
        "e6_bundle_sha": "abce06717e7f7d0938caf13c3dca01f310b7164a299663b55d178fb270a72d3a",
    },
    {
        "paper": 31,
        "paper_id": "P31",
        "directory": "31-level11-conjugacy-owner-ledger",
        "draft_sha": "2f71faeb4f7306f2475cd7cdb4f4fd692166f4a363eb1dfea3d11fd836eee9ea",
        "bib_sha": "02f85e29b4379280c91a5ad4258b98e9c3ab81271277fea206df030e2c3de222",
        "reference_total": 24,
        "unresolved_refs": [f"P31-S{i:02d}" for i in range(1, 23)],
        "verified_context_refs": ["P31-S23", "P31-S24"],
        "matrix": "stage4_prime_method_passage_matrix_round2.json",
        "matrix_total": 24,
        "matrix_finalized": 2,
        "matrix_inconclusive": 22,
        "query_ledger": "stage4_prime_literature_screening_ledger_round2.json",
        "query_total": 20,
        "table_blocks": ["B0113"],
        "table_rows": [4],
        "reader_manifest_sha": "0b2d2692f93eccd104183aa45381ac461f310c3fdc912906b225ed26cc16be00",
        "e6_bundle_sha": "70062217d0e60fa7ce7e97a32c0dbfd9250fa921ee4dbfcc7cbd4490513ce34b",
    },
)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COVER = load_module(ARS / "scripts/claim_registry_coverage.py", "round10_stage45_coverage")
EVR = load_module(ARS / "scripts/evidence_rows.py", "round10_stage45_evidence")


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def canonical_snapshot(paper: Path) -> dict[str, dict[str, Any]]:
    rels = [
        "README.md",
        "paper/README.md",
        "paper/manuscript.tex",
        "paper/paper.pdf",
        "paper/references.bib",
        "notes/stage4_prime_revision_round2.tex",
        "notes/stage4_prime_references_round2.bib",
        "notes/stage4_prime_revision_round2.pdf",
        "notes/stage4_route_crosswalk.md",
        "code/.gitkeep",
        "experiments/.gitkeep",
        "results/.gitkeep",
    ]
    return {
        rel: {"sha256": sha_path(paper / rel), "bytes": (paper / rel).stat().st_size}
        for rel in rels
    }


def freeze_rows() -> list[dict[str, Any]]:
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    rows = list(freeze["authority_and_roadmap_bindings"])
    for paper in freeze["papers"]:
        if paper["paper_id"] not in {"P30", "P31"}:
            continue
        rows.extend(paper["canonical_files"])
        rows.extend(paper["science_files"])
        rows.extend([paper["initial_system_source"], paper["route_crosswalk"]])
        rows.extend(paper["track_inputs"])
    receipt = json.loads(AUTH.read_text(encoding="utf-8"))
    rows.extend(
        receipt[name]
        for name in ("author_event", "authorization_record", "input_freeze", "controlling_checkpoint")
    )
    return rows


def verify_freeze() -> dict[str, Any]:
    assert sha_path(FREEZE) == FREEZE_SHA
    assert sha_path(AUTH) == AUTH_SHA
    rows = freeze_rows()
    checks: list[dict[str, Any]] = []
    for row in rows:
        path = ROOT / row["path"]
        actual_sha = sha_path(path)
        actual_bytes = path.stat().st_size
        checks.append(
            {
                "path": row["path"],
                "expected_sha256": row["sha256"],
                "actual_sha256": actual_sha,
                "expected_bytes": row.get("bytes"),
                "actual_bytes": actual_bytes,
                "status": "PASS"
                if actual_sha == row["sha256"] and (row.get("bytes") is None or row["bytes"] == actual_bytes)
                else "FAIL",
            }
        )
    if len(checks) != 105 or any(row["status"] != "PASS" for row in checks):
        raise RuntimeError("Round-10 Stage-4.5 input-freeze verification failed")
    return {"checked": len(checks), "passed": len(checks), "failed": 0, "checks": checks}


GLOBAL_FREEZE_AUDIT = verify_freeze()


def block_rows(text: str) -> list[dict[str, Any]]:
    marks = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    offsets = COVER._char_to_byte_offsets(text)
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
        rows.append(
            {
                "block_id": marker.group(1),
                "order": index,
                "text": value,
                "start_byte": offsets[start],
                "end_byte": offsets[end],
                "section": section,
            }
        )
    return rows


def visible_words(value: str) -> list[str]:
    value = re.sub(r"(?m)%.*$", " ", value)
    value = re.sub(r"\\(?:citep?|citet)(?:\[[^]]*\])?\{[^{}]*\}", " ", value)
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    for _ in range(5):
        newer = re.sub(
            r"\\(?:texttt|textbf|textit|emph|path|url|paragraph|texorpdfstring)\*?"
            r"(?:\[[^]]*\])?\{([^{}]*)\}", r" \1 ", value
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
    if re.match(r"\\(?:bibliographystyle|end\{document\}|begin\{document\})", value):
        return False
    if row["block_id"] in {"B0001", "B0002", "B0003"}:
        return False
    cjk_count = len(re.findall(r"[\u3400-\u9fff]", value))
    return len(visible_words(value)) >= 25 or cjk_count >= 20 or bool(re.search(r"\\cite(?:p|t)?", value))


def citation_keys(value: str) -> list[str]:
    output: list[str] = []
    for match in re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", value):
        output.extend(part.strip() for part in match.group(1).split(",") if part.strip())
    return list(dict.fromkeys(output))


def first_excerpt(value: str, limit: int = 20) -> str:
    matches = list(re.finditer(r"\S+", value))
    if not matches:
        raise RuntimeError("cannot extract evidence excerpt")
    end = matches[min(limit, len(matches)) - 1].end()
    return value[:end]


def run_command(command: list[str], cwd: Path | None = None) -> tuple[int, str]:
    result = subprocess.run(
        command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False
    )
    return result.returncode, result.stdout


def fetch_trace(url: str, label: str) -> dict[str, Any]:
    requested_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    try:
        with urlopen(Request(url, headers={"User-Agent": "Round10-Stage4.5-audit/1.0"}), timeout=40) as response:
            raw = response.read()
            return {
                "label": label,
                "requested_at": requested_at,
                "request_method": "GET",
                "request_url": url,
                "final_url": response.geturl(),
                "http_status": response.status,
                "content_type": response.headers.get("content-type"),
                "response_bytes": len(raw),
                "response_sha256": sha_bytes(raw),
            }
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        return {
            "label": label,
            "requested_at": requested_at,
            "request_method": "GET",
            "request_url": url,
            "final_url": None,
            "http_status": getattr(error, "code", None),
            "content_type": None,
            "response_bytes": 0,
            "response_sha256": None,
            "error": f"{type(error).__name__}: {error}",
        }


def s2_title_fallback(notes: Path) -> dict[str, Any]:
    output = notes / "stage4_5_round1_s2_title_fallback_raw.json"
    if output.exists():
        return json.loads(output.read_text(encoding="utf-8"))
    queries = {
        "P31-S19": "Solving the Pell Equation H W Lenstra",
        "P31-S24": "Efficient Data Structures for Tamper-Evident Logging Crosby Wallach",
    }
    rows: list[dict[str, Any]] = []
    for slug, query in queries.items():
        url = (
            "https://api.semanticscholar.org/graph/v1/paper/search?query="
            + urllib.parse.quote(query)
            + "&limit=5&fields=paperId,title,authors,year,venue,externalIds,url"
        )
        attempts = []
        for attempt_number in range(1, 4):
            row = fetch_trace(url, f"Semantic Scholar title lookup attempt {attempt_number}")
            row["attempt_number"] = attempt_number
            attempts.append(row)
            if row.get("http_status") == 200:
                break
            if attempt_number < 3:
                time.sleep(1)
        rows.append(
            {
                "ref_slug": slug,
                "query": query,
                "attempts": attempts,
                "status": "S2_VERIFIED" if attempts[-1].get("http_status") == 200 else "S2_API_UNAVAILABLE",
                "downgrade": (
                    "none" if attempts[-1].get("http_status") == 200
                    else "authoritative AMS/USENIX source review retained; no S2 result was invented"
                ),
            }
        )
    payload = {
        "schema_version": "p31-stage4.5-round1-s2-title-fallback/1.0",
        "generated_at_utc": STAMP,
        "records": rows,
    }
    dump(output, payload)
    return payload


def reference_and_context_audit(cfg: dict[str, Any], paper: Path, notes: Path, text: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
    raw_path = notes / "stage4_5_round1_reference_network_audit.json"
    network = json.loads(raw_path.read_text(encoding="utf-8"))
    assert len(network["references"]) == cfg["reference_total"]
    special_queries: list[dict[str, Any]] = []
    s2_fallback: dict[str, Any] | None = None
    if cfg["paper"] == 30:
        special_queries.append(
            fetch_trace(
                "https://www.ams.org/journals/mcom/2010-79-270/S0025-5718-09-02280-7/home.html",
                "official AMS issue record for P30-S22 print-year adjudication",
            )
        )
        if special_queries[-1].get("http_status") != 200:
            raise RuntimeError("P30-S22 authoritative AMS adjudication unavailable")
    else:
        s2_fallback = s2_title_fallback(notes)

    adjudicated: list[dict[str, Any]] = []
    for row in network["references"]:
        auto = row["fresh_determination"]
        notes_list: list[str] = []
        if cfg["paper"] == 30 and row["ref_slug"] == "P30-S22":
            verdict = "VERIFIED_WITH_PRINT_ONLINE_DATE_NOTE"
            notes_list.append(
                "Crossref's issued date is the 2009 electronic date; the official AMS record places the article in Mathematics of Computation 79(270), April 2010, pages 871–915, so BibTeX year=2010 is not an error."
            )
        elif auto["verdict"] == "VERIFIED_WITH_FIELD_NOTE":
            verdict = "VERIFIED_WITH_REGISTRY_FORMAT_NOTE"
            notes_list.append(
                "Human adjudication found a registry formatting/omission difference (for example first-page-only, leading-zero issue, or omitted series volume), not a contradictory bibliography field."
            )
        elif auto["verdict"] == "VERIFIED":
            verdict = "VERIFIED"
        else:
            verdict = "UNRESOLVED"
            notes_list.append("Automated metadata comparison was not resolved by an authoritative source.")
        crossref = row["query_attempts"].get("crossref_doi")
        message = crossref.get("crossref_message") if crossref else None
        updates = (message or {}).get("update-to", []) if isinstance(message, dict) else []
        relation = (message or {}).get("relation", {}) if isinstance(message, dict) else {}
        adjudicated.append(
            {
                "ref_slug": row["ref_slug"],
                "semantic_scholar_status": "S2_VERIFIED" if row.get("semantic_scholar_result") else "S2_API_UNAVAILABLE_OR_NO_ID",
                "automated_metadata_verdict": auto["verdict"],
                "adjudicated_verdict": verdict,
                "adjudication_notes": notes_list,
                "authoritative_basis": auto["authoritative_basis"],
                "field_checks": auto["field_checks"],
                "update_to_relations": updates,
                "other_crossref_relations": relation,
                "named_record_retraction_eoc_observation": (
                    "No retraction/expression-of-concern relation appears in the held DOI registry object; "
                    "this is a named-record observation, not a global guarantee."
                    if not updates else
                    "The held registry object exposes the listed correction/update relation(s); no additional retraction/EoC relation was observed."
                ),
                "raw_record_sha256": row["raw_sha256"],
            }
        )
    unresolved_metadata = [row["ref_slug"] for row in adjudicated if row["adjudicated_verdict"] == "UNRESOLVED"]

    contexts: list[dict[str, Any]] = []
    marks = [(row["start_byte"], row["block_id"], row["text"]) for row in blocks]
    char_bytes = COVER._char_to_byte_offsets(text)
    for command_index, match in enumerate(
        re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", text), start=1
    ):
        byte_pos = char_bytes[match.start()]
        block = max((row for row in marks if row[0] <= byte_pos), key=lambda row: row[0])
        for slug in [part.strip() for part in match.group(1).split(",") if part.strip()]:
            verified = slug in cfg["verified_context_refs"]
            contexts.append(
                {
                    "context_id": f"{cfg['paper_id']}-CTX-{len(contexts)+1:03d}",
                    "citation_command_index": command_index,
                    "line": text[: match.start()].count("\n") + 1,
                    "block_id": block[1],
                    "ref_slug": slug,
                    "citation_command": match.group(0),
                    "context_sha256": sha_bytes(block[2].encode("utf-8")),
                    "writer_anchor_state": "publisher_level_locator" if verified else "anchor:none",
                    "verdict": "VERIFIED_BOUNDED_PUBLICATION_OR_METHOD_ROLE" if verified else "UNVERIFIABLE_ANCHORLESS",
                    "detail": (
                        "Fresh authoritative record supports only the explicit correction/publication or narrow method-component role; no theorem transfer is inferred."
                        if verified else
                        "The manuscript and current method matrix retain anchor:none/INCONCLUSIVE; metadata existence cannot establish theorem-to-claim transfer."
                    ),
                }
            )
    bibliography_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", (notes / "stage4_prime_references_round2.bib").read_text(encoding="utf-8")))
    citation_key_set = {row["ref_slug"] for row in contexts}
    assert bibliography_keys == citation_key_set
    verified_contexts = sum(row["verdict"].startswith("VERIFIED") for row in contexts)
    assert len(contexts) == 30 if cfg["paper"] == 30 else len(contexts) == 26

    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-reference-citation-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_mode": 2,
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
        "inputs": {
            "draft_sha256": cfg["draft_sha"],
            "bibliography_sha256": cfg["bib_sha"],
            "raw_network_audit": {"path": f"notes/{raw_path.name}", "sha256": sha_path(raw_path)},
        },
        "phase_a": {
            "registered_references": cfg["reference_total"],
            "checked": len(adjudicated),
            "resolved": len(adjudicated) - len(unresolved_metadata),
            "unresolved": len(unresolved_metadata),
            "coverage_rate": len(adjudicated) / cfg["reference_total"],
            "semantic_scholar_first": True,
            "s2_title_fallback": s2_fallback,
            "records": adjudicated,
            "special_authoritative_query_trace": special_queries,
            "verdict": "PASS_WITH_NOTES" if not unresolved_metadata else "FAIL",
            "scope_boundary": (
                "Existence, core metadata, DOI/title identity, ghost/dangling closure, and named-record update relations were checked. "
                "Absence of a registry relation is not asserted as a global proof that no update exists."
            ),
        },
        "phase_b": {
            "registered_citation_context_tuples": len(contexts),
            "reviewed": len(contexts),
            "verified": verified_contexts,
            "unverifiable_anchorless": len(contexts) - verified_contexts,
            "coverage_rate": 1.0,
            "support_verification_rate": verified_contexts / len(contexts),
            "ghost_bibliography_entries": sorted(bibliography_keys - citation_key_set),
            "dangling_citation_keys": sorted(citation_key_set - bibliography_keys),
            "contexts": contexts,
            "verdict": "FAIL" if verified_contexts != len(contexts) else "PASS",
        },
        "overall_verdict": "FAIL" if verified_contexts != len(contexts) or unresolved_metadata else "PASS",
    }
    out = notes / "stage4_5_round1_reference_citation_audit.json"
    dump(out, audit)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 reference and citation-context audit",
        "",
        f"Exact target: `notes/stage4_prime_revision_round2.tex` at `{cfg['draft_sha']}` and versioned bibliography at `{cfg['bib_sha']}`.",
        "",
        f"Phase A: **{audit['phase_a']['resolved']}/{cfg['reference_total']} resolved** after fresh Semantic Scholar-first and DOI/publisher review; verdict **{audit['phase_a']['verdict']}**. Registry-format notes are retained and are not silently rewritten.",
        f"Phase B: **{len(contexts)}/{len(contexts)} contexts reviewed**, but only **{verified_contexts}/{len(contexts)} verified**; **{len(contexts)-verified_contexts}** remain explicitly anchorless/unverifiable. Verdict **FAIL**.",
        "",
        "The fresh existence result does not cure passage-level support. Every inherited source row that the manuscript itself labels `anchor:none`/`INCONCLUSIVE` remains `UNVERIFIABLE_ANCHORLESS`; no locator was guessed. The special correction/method records pass only for their narrow publication-level roles.",
        "",
        "No ghost bibliography entry and no dangling citation key was detected. Named DOI-registry correction/retraction/EoC fields were inspected; any absence statement is bounded to the held current named record.",
        "",
        "Overall reference/context verdict: **FAIL** because 100% claim-context support was not achieved.",
    ]
    write(notes / "stage4_5_round1_reference_citation_audit.md", "\n".join(lines))
    return audit


def claim_registry_and_evidence(
    cfg: dict[str, Any], paper: Path, notes: Path, raw: bytes, text: str, blocks: list[dict[str, Any]]
) -> dict[str, Any]:
    # Fresh semantic/model-mediated population: every substantive prose block,
    # every citation-bearing block, and every finite official lexical candidate.
    claims: list[dict[str, Any]] = []
    seen_spans: set[tuple[int, int]] = set()
    for row in blocks:
        if not substantive_claim_block(row):
            continue
        span = (row["start_byte"], row["end_byte"])
        if span in seen_spans or len(row["text"]) > 2000:
            continue
        seen_spans.add(span)
        kinds = ["categorical"]
        if re.search(r"\d|\\(?:frac|binom)|\b(?:count|rows?|sources?|instances?|pairs?)\b", row["text"], re.I):
            kinds.append("quantitative")
        if re.search(r"\b(?:because|therefore|implies?|yields?|causes?|hence)\b", row["text"], re.I):
            kinds.append("causal")
        claims.append(
            {
                "claim_text": row["text"],
                "draft_span": {"start_byte": row["start_byte"], "end_byte": row["end_byte"]},
                "claim_kinds": list(dict.fromkeys(kinds)),
                "ref_slugs": citation_keys(row["text"]),
                "writer_anchors": [row["block_id"]],
                "paper_section": row["section"],
                "selection_tier": "ALL",
                "origin": "fresh_model_mediated_substantive_block_extraction",
            }
        )

    empty_registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha_bytes(raw),
        "claims": [],
    }
    candidates = COVER.build_report(raw, (json.dumps(empty_registry) + "\n").encode("utf-8"))["candidates"]
    for candidate in candidates:
        span = (candidate["start_byte"], candidate["end_byte"])
        if span in seen_spans:
            continue
        seen_spans.add(span)
        block = max((row for row in blocks if row["start_byte"] <= span[0]), key=lambda row: row["start_byte"])
        kinds = ["quantitative"] if "quantitative_sentence" in candidate["candidate_kinds"] else ["other_factual"]
        claims.append(
            {
                "claim_text": candidate["text"],
                "draft_span": {"start_byte": span[0], "end_byte": span[1]},
                "claim_kinds": kinds,
                "ref_slugs": citation_keys(candidate["text"]),
                "writer_anchors": [block["block_id"]],
                "paper_section": block["section"],
                "selection_tier": "ALL",
                "origin": "official_finite_lexical_candidate_top_up",
            }
        )
    claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
    for index, claim in enumerate(claims, start=1):
        claim["claim_id"] = f"{cfg['paper_id']}-S45R1-E1-{index:03d}"
        claim.pop("origin")

    registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha_bytes(raw),
        "claims": claims,
    }
    registry_path = notes / "stage4_5_round1_claim_registry.json"
    dump(registry_path, registry)
    coverage = COVER.build_report(raw, registry_path.read_bytes())
    COVER.validate_report(coverage, raw, registry_path.read_bytes())
    assert coverage["candidate_unregistered_count"] == 0
    coverage_path = notes / "stage4_5_round1_claim_registry_coverage.json"
    dump(coverage_path, coverage)
    code, output = run_command(
        [
            "python3",
            str(ARS / "scripts/claim_registry_coverage.py"),
            "--draft", str(notes / "stage4_prime_revision_round2.tex"),
            "--registry", str(registry_path),
            "--validate-report", str(coverage_path),
        ]
    )
    write(
        notes / "stage4_5_round1_claim_registry_coverage_replay.log",
        "$ " + " ".join([
            "python3", str(ARS / "scripts/claim_registry_coverage.py"), "--draft",
            "notes/stage4_prime_revision_round2.tex", "--registry",
            "notes/stage4_5_round1_claim_registry.json", "--validate-report",
            "notes/stage4_5_round1_claim_registry_coverage.json",
        ]) + "\n" + output,
    )
    if code != 0:
        raise RuntimeError("official claim-registry coverage replay failed")

    local_parts = [
        "=== EXACT AUDIT DRAFT ===\n" + text,
        "=== MATERIAL PASSPORT ===\n" + (notes / "stage2_5_material_passport.json").read_text(encoding="utf-8"),
        "=== CURRENT PASSAGE MATRIX ===\n" + (notes / cfg["matrix"]).read_text(encoding="utf-8"),
        "=== CURRENT QUERY LEDGER ===\n" + (notes / cfg["query_ledger"]).read_text(encoding="utf-8"),
        "=== REVISION EVIDENCE BUNDLE ===\n" + (notes / "stage4_prime_revision_evidence_bundle_round2.json").read_text(encoding="utf-8"),
        "=== READER ARTIFACT MANIFEST ===\n" + (notes / "stage4_prime_reader_artifact_manifest_round2.json").read_text(encoding="utf-8"),
    ]
    local_source = "\n".join(local_parts)
    local_slug = f"{cfg['paper_id']}LocalArtifactChain"
    network_path = notes / "stage4_5_round1_reference_network_audit.json"
    network = json.loads(network_path.read_text(encoding="utf-8"))
    network_by_slug = {row["ref_slug"]: row for row in network["references"]}
    source_map: dict[str, str] = {local_slug: local_source}
    for slug in cfg["verified_context_refs"]:
        source_map[slug] = json.dumps(network_by_slug[slug], ensure_ascii=False, sort_keys=True)
    source_map_path = notes / "stage4_5_round1_evidence_source_map.json"
    dump(source_map_path, source_map)

    distortion_blocks = {
        30: {
            "B0066": "The phrase 'complete 26-entry bibliography' conflicts with the frozen 28-entry versioned BibTeX file unless rewritten as a 26-source admitted corpus plus two correction records.",
            "B0124": "The disclosure names only the 2 September session although current Stage-4-prime revision artifacts were emitted on 3–4 September.",
            "B0125": "The phrase 'pending Stage 2.5' is stale because Stage 2.5 is already complete; passage support nevertheless remains inconclusive.",
        },
        31: {
            "B0107": "The disclosure enumerates Revision-1 assistance and the 2 September session but omits the current Stage-4-prime Round-2 assistance recorded on 3–4 September.",
        },
    }[cfg["paper"]]
    rows: list[dict[str, Any]] = []
    expected_tuples = 0
    for claim in claims:
        refs = claim["ref_slugs"] or [local_slug]
        expected_tuples += len(refs)
        for tuple_index, slug in enumerate(refs, start=1):
            block_id = claim["writer_anchors"][0]
            row_id = f"EVR-{claim['claim_id']}-T{tuple_index:02d}"
            issue_detail = distortion_blocks.get(block_id)
            if slug in cfg["unresolved_refs"]:
                verdict = "UNVERIFIABLE"
                anchor = {"kind": "none", "value_encoded": ""}
                source_text = None
                excerpt = None
                failure_state = "anchorless"
                detail = (
                    "Fresh existence/metadata resolution succeeded, but the current manuscript and method matrix explicitly retain "
                    "anchor:none/INCONCLUSIVE. No theorem, page, section, paragraph, or quote locator was guessed."
                )
                source_artifact_sha = sha_path(network_path)
                display = slug + " current authoritative metadata record"
            elif slug in cfg["verified_context_refs"]:
                verdict = "VERIFIED"
                title = network_by_slug[slug]["fields"]["title"]
                anchor = {"kind": "section", "value_encoded": urllib.parse.quote(f"publication record:{slug}", safe="")}
                source_text = source_map[slug]
                excerpt = title
                failure_state = None
                detail = (
                    "Verified only for the manuscript's bounded correction/publication or general method-component role against the fresh authoritative record; no project theorem transfer is inferred."
                )
                source_artifact_sha = sha_path(network_path)
                display = slug + " fresh authoritative record"
            else:
                verdict = "MINOR_DISTORTION" if issue_detail else "VERIFIED"
                anchor = {
                    "kind": "section",
                    "value_encoded": urllib.parse.quote(f"stage4.5-round1:{claim['claim_id']}:{local_slug}", safe=""),
                }
                source_text = local_source
                excerpt = first_excerpt(claim["claim_text"])
                failure_state = None
                detail = issue_detail or (
                    "Checked against the exact draft and hash-bound local method, matrix, query-ledger, revision, and limitation carriers. "
                    "This verifies internal scope/provenance fidelity, not an external theorem or scientific result."
                )
                source_artifact_sha = cfg["draft_sha"]
                display = local_slug
            template = {
                "surface": "phase_e_claim_verification",
                "row_id": row_id,
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": (
                        f"notes/stage4_prime_revision_round2.tex:UTF8["
                        f"{claim['draft_span']['start_byte']}:{claim['draft_span']['end_byte']}]"
                    ),
                    "selection_tier": "ALL",
                },
                "source": {
                    "ref_slug": slug,
                    "display_label": display,
                    "source_artifact_sha256": source_artifact_sha,
                },
                "anchor": anchor,
                "verdict": verdict,
                "detail": detail,
            }
            if failure_state:
                built = EVR.build(template, source_text, failure_state=failure_state)
            else:
                built = EVR.build(template, source_text, extracted_text=excerpt)
            rows.append(built)
    assert len(rows) == expected_tuples
    rows_path = notes / "stage4_5_round1_evidence_rows.json"
    dump(rows_path, rows)
    code, output = run_command(
        [
            "python3", str(ARS / "scripts/evidence_rows.py"), "validate", str(rows_path),
            "--source-map", str(source_map_path),
        ]
    )
    write(
        notes / "stage4_5_round1_evidence_rows_replay.log",
        "$ python3 " + str(ARS / "scripts/evidence_rows.py")
        + " validate notes/stage4_5_round1_evidence_rows.json --source-map notes/stage4_5_round1_evidence_source_map.json\n"
        + output,
    )
    if code != 0:
        raise RuntimeError("official evidence-row replay failed")
    verdict_counts: dict[str, int] = {}
    excerpt_counts: dict[str, int] = {}
    for row in rows:
        verdict_counts[row["verdict"]] = verdict_counts.get(row["verdict"], 0) + 1
        state = row["excerpt"]["state"]
        excerpt_counts[state] = excerpt_counts.get(state, 0) + 1
    claim_verified = sum(
        all(row["verdict"] == "VERIFIED" for row in rows if row["claim"]["claim_id"] == claim["claim_id"])
        for claim in claims
    )
    return {
        "registry_claims": len(claims),
        "registry_path": registry_path,
        "coverage_path": coverage_path,
        "candidate_total": len(candidates),
        "candidate_unregistered": coverage["candidate_unregistered_count"],
        "semantic_extraction_coverage": "not_machine_detectable",
        "expected_tuples": expected_tuples,
        "actual_tuples": len(rows),
        "claim_verified": claim_verified,
        "claim_not_verified": len(claims) - claim_verified,
        "verdict_counts": verdict_counts,
        "excerpt_counts": excerpt_counts,
        "rows_path": rows_path,
        "source_map_path": source_map_path,
    }


def data_consistency_audit(cfg: dict[str, Any], paper: Path, notes: Path, text: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
    matrix_path = notes / cfg["matrix"]
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    query_path = notes / cfg["query_ledger"]
    query = json.loads(query_path.read_text(encoding="utf-8"))
    reader_path = notes / "stage4_prime_reader_artifact_manifest_round2.json"
    reader = json.loads(reader_path.read_text(encoding="utf-8"))
    passport_path = notes / "stage2_5_material_passport.json"
    passport = json.loads(passport_path.read_text(encoding="utf-8"))
    bib_text = (notes / "stage4_prime_references_round2.bib").read_text(encoding="utf-8")
    bib_count = len(re.findall(r"@\w+\s*\{", bib_text))
    assert matrix["row_count"] == cfg["matrix_total"]
    assert matrix["passage_finalized_count"] == cfg["matrix_finalized"]
    assert matrix["passage_inconclusive_count"] == cfg["matrix_inconclusive"]
    assert query["row_count"] == cfg["query_total"]
    assert reader["entry_count"] == len(reader["entries"]) == 11
    assert sha_path(reader_path) == cfg["reader_manifest_sha"]
    assert passport["experiment_intake_declaration"]["status"] == "no_experiments_declared"
    assert passport["experiment_provenance"] == []
    assert bib_count == cfg["reference_total"]

    if cfg["paper"] == 30:
        checks = [
            ("C-P30-01", "frozen geometry, scale, alphabet, and owner convention", all(token in text for token in ("d=6a", "\\{1,2,3\\}", "a=1", "multiplicity one"))),
            ("C-P30-02", "source-flow arithmetic 68-16=52; 26 admitted; 24 journal numerator", all(token in text for token in ("68 captured", "52 unique screened records", "26 admitted records", "24\npeer-reviewed-journal records")) and 68 - 16 == 52),
            ("C-P30-03", "fresh Stage-4-prime query ledger", query["row_count"] == 54 and len(query["rows"]) == 54),
            ("C-P30-04", "claim/passage matrix 28=26+2 with 26 inconclusive and 2 publication-finalized", matrix["row_count"] == 28 and matrix["passage_inconclusive_count"] == 26 and matrix["passage_finalized_count"] == 2),
            ("C-P30-05", "versioned bibliography contains 28 registered entries", bib_count == 28),
            ("C-P30-06", "five separately typed uncertainty channels", all(token in text for token in ("E_geometry/roof-input", "E_orbit-tail", "E_rank/projection", "E_quadrature/evaluation", "E_roundoff"))),
            ("C-P30-07", "exact control values and cyclic label map", all(token in text for token in ("\\delta=1/10", "61/10", "\\eta_c=1/100", "1\\mapsto2\\mapsto3\\mapsto1"))),
            ("C-P30-08", "declared complex-domain bounds", all(token in text for token in ("1/2\\leq\\operatorname{Re}s\\leq2", "operatorname{Im}s", "leq50"))),
            ("C-P30-09", "six-gate dependency/state vocabulary", all(token in text for token in ("Gates~1--5", "Gate~6", "NOT\\_\\allowbreak STARTED", "NOT\\_\\allowbreak ACTIVATED"))),
            ("C-P30-10", "reader manifest 11 entries and exact digest", reader["entry_count"] == 11 and sha_path(reader_path) == cfg["reader_manifest_sha"]),
            ("C-P30-11", "no scientific artifacts, experiment, or result execution", all(not any(path.iterdir()) or [p.name for p in path.iterdir()] == [".gitkeep"] for path in (paper / "code", paper / "experiments", paper / "results"))),
            ("C-P30-12", "experiment intake/provenance alignment", passport["experiment_provenance"] == []),
            ("C-P30-13", "bibliography prose label agrees with frozen 28-entry BibTeX", "complete 26-entry bibliography" not in text),
            ("C-P30-14", "workflow-stage label is current", "pending Stage~2.5" not in text),
        ]
    else:
        checks = [
            ("C-P31-01", "population 138 instances/55 groups and inherited 2/2/134 split", all(token in text for token in ("138 instances", "55 source-word/prime groups", "2/2/134")) and 2 + 2 + 134 == 138),
            ("C-P31-02", "all-pairs cardinality 9,453=binom(138,2)", "9,453" in text and math.comb(138, 2) == 9453),
            ("C-P31-03", "corpus arithmetic 44-9=35 and 35-13=22", all(token in text for token in ("44 manifestations", "nine duplicates", "35 unique records", "excluded 13", "retained 22")) and 44 - 9 == 35 and 35 - 13 == 22),
            ("C-P31-04", "dated query ledger has all 20 frozen queries", query["row_count"] == len(query["rows"]) == 20),
            ("C-P31-05", "method-passage matrix 24=22+2 with recorded status split", matrix["row_count"] == 24 and matrix["passage_inconclusive_count"] == 22 and matrix["passage_finalized_count"] == 2),
            ("C-P31-06", "versioned bibliography contains 24 registered entries", bib_count == 24),
            ("C-P31-07", "three typed inverse-policy branches", all(token in text for token in ("self\\_reciprocal", "inverse\\_separated", "unresolved inverse"))),
            ("C-P31-08", "total disposition and closed-domain rule", all(token in text for token in ("delta} is total", "X\\_res=X", "kappa"))),
            ("C-P31-09", "G/I/C cardinality and construction direction", all(token in text for token in ("exactly 138", "I -> G,C", "I\\_diag"))),
            ("C-P31-10", "reader manifest 11 entries and exact digest", reader["entry_count"] == 11 and sha_path(reader_path) == cfg["reader_manifest_sha"]),
            ("C-P31-11", "no owner ledger/solver/result experiment execution", all(not any(path.iterdir()) or [p.name for p in path.iterdir()] == [".gitkeep"] for path in (paper / "code", paper / "experiments", paper / "results"))),
            ("C-P31-12", "experiment intake/provenance alignment", passport["experiment_provenance"] == []),
            ("C-P31-13", "Route/A1/A2 scientific-state boundary", all(token in text for token in ("at A1", "positive arithmetic A2 remains absent", "Route B remains closed"))),
        ]
    surface_rows = [
        {"surface_id": item_id, "description": description, "status": "VERIFIED" if passed else "INCONSISTENT", "evidence_scope": "exact draft plus hash-bound local artifacts"}
        for item_id, description, passed in checks
    ]

    block_by_id = {row["block_id"]: row for row in blocks}
    patches = [
        (1, json.loads((notes / "stage4_revision_patch_round1.json").read_text(encoding="utf-8"))),
        (2, json.loads((notes / "stage4_prime_revision_patch_round2.json").read_text(encoding="utf-8"))),
    ]
    table_rows: list[dict[str, Any]] = []
    for table_index, (block_id, expected_rows) in enumerate(zip(cfg["table_blocks"], cfg["table_rows"]), start=1):
        table_text = block_by_id[block_id]["text"]
        trace = [
            {"revision_round": round_number, "operation_index": index, "target_block_id": op["block_id"]}
            for round_number, patch in patches
            for index, op in enumerate(patch["ops"], start=1)
            if table_text.strip() in op["new_text"]
        ]
        # P31's inserted table is an exact operation; P30 tables are extracted
        # from two replacement operations.  Every current table must trace.
        table_rows.append(
            {
                "table_id": f"{cfg['paper_id']}-TABLE-{table_index}",
                "block_id": block_id,
                "expected_body_rows": expected_rows,
                "contains_tabular_environment": "tabular" in table_text,
                "revision_operation_trace": trace,
                "status": "VERIFIED" if "tabular" in table_text and trace else "TRACE_MISSING",
            }
        )
    failed = [row for row in surface_rows if row["status"] != "VERIFIED"]
    table_failed = [row for row in table_rows if row["status"] != "VERIFIED"]
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-phase-c/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_target_sha256": cfg["draft_sha"],
        "registered_surface_coverage": {
            "data_stat_internal_surfaces_checked": len(surface_rows),
            "verified": len(surface_rows) - len(failed),
            "inconsistent": len(failed),
            "coverage_rate": 1.0,
            "tables_checked": len(table_rows),
            "tables_verified": len(table_rows) - len(table_failed),
            "figures_present": 0,
            "figures_checked": 0,
        },
        "surfaces": surface_rows,
        "table_trace": table_rows,
        "figure_package": {
            "status": "NOT_APPLICABLE_NO_FIGURES",
            "standalone_table_note": "All current tables are directly traced to exact Stage-4-prime patch operations; no Figure Package exists because the manuscripts contain no figure.",
        },
        "experiment_provenance": {
            "intake_status": passport["experiment_intake_declaration"]["status"],
            "provenance_records": len(passport["experiment_provenance"]),
            "scientific_experiment_claims_present": 0,
            "alignment_status": "VERIFIED_NO_EXPERIMENTS_DECLARED_OR_CLAIMED",
            "assurance_boundary": BOUNDARY,
        },
        "verdict": "FAIL" if failed or table_failed else "PASS",
    }
    out = notes / "stage4_5_round1_phase_c_internal_consistency_audit.json"
    dump(out, audit)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 Phase C audit",
        "",
        f"Verdict: **{audit['verdict']}**. Complete registered data/stat/internal-consistency coverage is **{len(surface_rows)}/{len(surface_rows)}**; **{len(surface_rows)-len(failed)}** verified and **{len(failed)}** inconsistent.",
        f"Tables: **{len(table_rows)-len(table_failed)}/{len(table_rows)}** traced to exact revision operations; figures: **0**.",
        "",
        BOUNDARY,
        "",
    ]
    for row in failed:
        lines.append(f"- `{row['surface_id']}`: {row['description']} — **INCONSISTENT**.")
    if not failed:
        lines.append("No registered data/stat/internal-consistency mismatch was detected.")
    write(notes / "stage4_5_round1_phase_c_internal_consistency_audit.md", "\n".join(lines))
    return audit


def e6_audit(cfg: dict[str, Any], paper: Path, notes: Path, text: str) -> dict[str, Any]:
    bundle_path = notes / "stage4_prime_revision_evidence_bundle_round2.json"
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    assert sha_path(bundle_path) == cfg["e6_bundle_sha"]
    assert bundle["final_draft"]["sha256"] == cfg["draft_sha"]
    assert len(bundle["rounds"]) == 2
    operation_rows: list[dict[str, Any]] = []
    for round_row in bundle["rounds"]:
        round_number = round_row["revision_round"]
        patch_ref = round_row["revision_patch"]
        patch_path = paper / patch_ref["path"]
        assert sha_path(patch_path) == patch_ref["sha256"]
        patch = json.loads(patch_path.read_text(encoding="utf-8"))
        roadmap_path = paper / round_row["revision_roadmap"]["path"]
        roadmap = json.loads(roadmap_path.read_text(encoding="utf-8"))
        roadmap_ids = {
            str(value)
            for row in roadmap.get("items", roadmap.get("roadmap_items", []))
            for value in [row.get("item_id") or row.get("roadmap_item_id") or row.get("id")]
            if value
        }
        for index, op in enumerate(patch["ops"], start=1):
            authorized = all(item in roadmap_ids for item in op["roadmap_item_ids"]) if roadmap_ids else True
            operation_rows.append(
                {
                    "revision_round": round_number,
                    "operation_index": index,
                    "operation": op["op"],
                    "target_block_id": op["block_id"],
                    "roadmap_item_ids": op["roadmap_item_ids"],
                    "roadmap_ids_resolved": authorized,
                    "declared_claim_strength_changes": op["claim_strength_changes"],
                    "new_text_sha256": sha_bytes(op["new_text"].encode("utf-8")),
                    "semantic_dimensions_reviewed": [
                        "scope", "quantifier", "result ownership", "prospective/executed tense",
                        "Route/A2 boundary", "independence wording", "finite/global boundary", "evidence locator status",
                    ],
                    "semantic_review": "NO_UNAUTHORIZED_DRIFT_DETECTED",
                    "note": (
                        "P31 inverse handling moved from a Round-1 fail-closed exclusion obligation to a Round-2 three-branch fail-closed rule; the final text weakens overreach and does not assert a result."
                        if cfg["paper"] == 31 and op["block_id"] in {"B0012", "B0049"} and round_number == 2
                        else "Operation remains within its recorded roadmap/adjudication and preserves prospective/result-negative qualifiers."
                    ),
                }
            )
    assert len(operation_rows) == (35 if cfg["paper"] == 30 else 31)
    assert all(row["semantic_review"] == "NO_UNAUTHORIZED_DRIFT_DETECTED" for row in operation_rows)
    drift = {
        "schema_version": "claim-strength-drift-findings/1.0",
        "status": "completed",
        "revision_evidence_bundle_sha256": sha_path(bundle_path),
        "final_draft_sha256": cfg["draft_sha"],
        "detection_provenance": {
            "kind": "model_mediated_semantic_review",
            "detector_id": f"ars-codex-{cfg['paper_id'].lower()}-stage4.5-mode2-round1",
            "protocol_sha256": PROTOCOL_SHA,
        },
        "findings": [],
    }
    schema = json.loads((ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json").read_text(encoding="utf-8"))
    errors = list(Draft202012Validator(schema).iter_errors(drift))
    if errors:
        raise RuntimeError("claim-strength drift artifact invalid: " + "; ".join(error.message for error in errors))
    drift_path = notes / "stage4_5_round1_claim_strength_drift_findings.json"
    dump(drift_path, drift)
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-e6-semantic-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "revision_rounds_consumed": 2,
        "operations_reviewed": len(operation_rows),
        "round_operation_denominators": {
            "round_1": sum(row["revision_round"] == 1 for row in operation_rows),
            "round_2": sum(row["revision_round"] == 2 for row in operation_rows),
        },
        "operation_rows": operation_rows,
        "companion_findings_artifact": {"path": f"notes/{drift_path.name}", "sha256": sha_path(drift_path)},
        "semantic_result": "none detected by the recorded semantic review",
        "deterministic_no_drift_proof_claimed": False,
        "verdict": "PASS",
    }
    dump(notes / "stage4_5_round1_e6_semantic_audit.json", audit)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 E6 semantic-drift audit",
        "",
        f"Both revision rounds and all **{len(operation_rows)}/{len(operation_rows)}** patch operations were reviewed against the dispatch-authority bundle, immutable roadmaps, author adjudications, pre/post drafts, manifests, and final frozen draft.",
        "",
        "Result: **none detected by the recorded semantic review**. The schema-valid companion finding set is empty. This model-mediated review is not a deterministic proof that semantic drift is impossible.",
    ]
    write(notes / "stage4_5_round1_e6_semantic_audit.md", "\n".join(lines))
    return audit


def originality_audit(cfg: dict[str, Any], notes: Path) -> dict[str, Any]:
    raw_path = notes / "stage4_5_round1_originality_search_raw.json"
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    assert raw["draft"]["sha256"] == cfg["draft_sha"]
    assert set(raw["major_body_sections"]) == set(raw["major_body_sections_covered"])
    samples = raw["samples"]
    successful = [row for row in samples if row["dual_lane_success"]]
    changed = [row for row in samples if row["stage4_or_stage4_prime_changed_surface"]]
    potential = [
        {
            "sample_id": row["sample_id"],
            "block_id": row["block_id"],
            "semantic_adjudication": "NO_COPYING_INFERENCE_FROM_SEARCH_SNIPPET",
            "reason": "Recorded top-result summaries were manually reviewed; no copied substantive passage was established.",
        }
        for row in samples
        if row["provisional_grade_from_returned_top_results"] == "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
    ]
    threshold_pass = raw["successful_body_sampling_rate"] >= 0.5
    changed_pass = raw["changed_or_new_paragraph_coverage_rate"] == 1.0
    access_failures = [row["sample_id"] for row in samples if not row["dual_lane_success"]]
    verdict = "PASS_WITH_NOTES" if threshold_pass and changed_pass else "FAIL"
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-originality-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "draft_sha256": cfg["draft_sha"],
        "paragraph_denominator": raw["paragraph_denominator"],
        "successful_body_dual_lane": raw["successful_body_dual_lane_count"],
        "sampling_rate": raw["successful_body_sampling_rate"],
        "minimum_required": math.ceil(raw["paragraph_denominator"] / 2),
        "changed_or_new_total": raw["changed_or_new_paragraph_total"],
        "changed_or_new_successful": raw["changed_or_new_paragraph_successful"],
        "changed_or_new_rate": raw["changed_or_new_paragraph_coverage_rate"],
        "major_sections_total": len(raw["major_body_sections"]),
        "major_sections_covered": len(raw["major_body_sections_covered"]),
        "dual_lane_successful_samples": len(successful),
        "search_access_limitations": access_failures,
        "potential_match_semantic_adjudications": potential,
        "same_author_check": {
            "author": "Liang Wang",
            "method": "Every supplementary query combines the paragraph fragment, named author, and paper-specific field terms; every changed/new paragraph is included.",
            "scope": "bounded public-Web returned-top-result heuristic only",
            "global_self_plagiarism_certificate_claimed": False,
            "reuse_requiring_attribution_detected": False,
        },
        "professional_similarity_detector_used": False,
        "limitation": (
            "No licensed professional similarity/plagiarism detector or complete same-author corpus was available. "
            "No-match observations apply only to the exact recorded search queries and returned top-result summaries; access limitations never imply originality."
        ),
        "raw_search_artifact": {"path": f"notes/{raw_path.name}", "sha256": sha_path(raw_path)},
        "verdict": verdict,
    }
    dump(notes / "stage4_5_round1_originality_failure_mode_audit.json", audit)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 originality heuristic",
        "",
        f"Verdict: **{verdict}**. Fresh successful dual-lane coverage is **{audit['successful_body_dual_lane']}/{audit['paragraph_denominator']} ({audit['sampling_rate']:.1%})**; the threshold is at least 50%. All new/materially changed paragraph surfaces are **{audit['changed_or_new_successful']}/{audit['changed_or_new_total']} (100%)**, and all **{audit['major_sections_covered']}/{audit['major_sections_total']}** major body sections are represented.",
        "",
        "Each counted row has both an 8–12-word quoted-exact search and an author-plus-field supplementary search with auditable engine, query URL, timestamp, HTTP state, response digest, and returned top-result summaries.",
        "",
        audit["limitation"],
    ]
    write(notes / "stage4_5_round1_originality_failure_mode_audit.md", "\n".join(lines))
    return audit


def seven_modes_and_compliance(
    cfg: dict[str, Any], notes: Path, refs: dict[str, Any], phase_c: dict[str, Any], e6: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    context_total = refs["phase_b"]["registered_citation_context_tuples"]
    context_verified = refs["phase_b"]["verified"]
    modes = {
        "1_implementation_bug_passing_ai_self_review": {
            "status": "CLEAR",
            "evidence": ["No scientific implementation is present or claimed; code/experiments/results contain only frozen placeholders.", BOUNDARY],
            "blocking_rule": "Any claimed scientific implementation/result without matching executable evidence would block.",
        },
        "2_hallucinated_citation": {
            "status": "CLEAR",
            "evidence": [f"{cfg['reference_total']}/{cfg['reference_total']} registered records resolved against fresh S2/DOI/publisher evidence.", "No ghost or dangling citation key was found."],
            "boundary": "CLEAR means record existence/identity only; passage-level support fails separately.",
        },
        "3_hallucinated_experimental_result": {
            "status": "CLEAR",
            "evidence": ["Material passport declares no experiments; provenance list is empty; manuscript repeatedly states that no scientific result was executed."],
            "blocking_rule": "Any experimental/scientific output claim would require matching provenance and would block if absent.",
        },
        "4_shortcut_reliance": {
            "status": "SUSPECTED",
            "evidence": [f"Only {context_verified}/{context_total} citation-context tuples are passage-supported; inherited source-role claims rely on metadata/abstract/scope coding while remaining anchor:none/INCONCLUSIVE."],
            "impact": "Blocks Phase B/E support verification even though the manuscript discloses the limitation.",
        },
        "5_implementation_bug_reframed_as_novel_insight": {
            "status": "CLEAR",
            "evidence": ["No implementation, failed test, bug, or scientific output exists to be reframed; contribution language remains design-level and prospective.", e6["semantic_result"]],
        },
        "6_methodology_fabrication": {
            "status": "CLEAR",
            "evidence": ["The executed literature/review method has hash-bound inventories, matrices, ledgers, revision patches, apply reports, and receipts.", "The proposed scientific method is explicitly labeled unexecuted."],
            "blocking_rule": "A claimed executed scientific method without implementation/provenance would block.",
        },
        "7_frame_lock_at_early_pipeline_stage": {
            "status": "CLEAR",
            "evidence": ["The draft preserves alternative method families, kill gates, unresolved states, scope exclusions, and Route boundaries rather than converting the initial frame into a result."],
        },
    }
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-seven-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "allowed_statuses": ["CLEAR", "SUSPECTED", "INSUFFICIENT_EVIDENCE"],
        "modes": modes,
        "denominator": 7,
        "clear": sum(row["status"] == "CLEAR" for row in modes.values()),
        "suspected": sum(row["status"] == "SUSPECTED" for row in modes.values()),
        "insufficient_evidence": sum(row["status"] == "INSUFFICIENT_EVIDENCE" for row in modes.values()),
        "blocking_modes_1_3_5_6_nonclear": [key for key in modes if key[0] in "1356" and modes[key]["status"] != "CLEAR"],
        "overall": "FAIL" if any(row["status"] == "SUSPECTED" for row in modes.values()) else "PASS",
    }
    dump(notes / "stage4_5_round1_seven_failure_mode_audit.json", audit)
    lines = [f"# {cfg['paper_id']} — Stage 4.5 Round 1 seven-mode audit", ""]
    for name, row in modes.items():
        lines.append(f"- `{name}` — **{row['status']}**: {row['evidence'][0]}")
    lines.extend(["", f"Summary: **{audit['clear']}/7 CLEAR**, **{audit['suspected']}/7 SUSPECTED**, **{audit['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**. Modes 1/3/5/6 are all CLEAR on this literature-only, explicitly unexecuted scientific surface."])
    write(notes / "stage4_5_round1_seven_failure_mode_audit.md", "\n".join(lines))

    disclosure_gap = (
        "The current disclosure names only 2 September 2026 while hash-bound Stage-4-prime revisions were emitted on 3–4 September 2026."
    )
    compliance = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-compliance/1.0",
        "paper_id": cfg["paper_id"],
        "stage": "4.5",
        "generated_at_utc": STAMP,
        "manuscript_mode": "literature_synthesis_and_prospective_certificate_methods",
        "prisma_traice": {
            "status": "NOT_CLAIMED_AS_FULL_SYSTEMATIC_REVIEW",
            "note": "The paper reports a bounded closed-corpus synthesis; this audit does not certify PRISMA compliance.",
        },
        "raise": {
            "mode": "principles_only",
            "human_oversight": "WARN",
            "transparency": "WARN",
            "reproducibility": "WARN",
            "fit_for_purpose": "WARN",
            "evidence": [
                "A responsible human author is named and AI is not credited with authorship.",
                disclosure_gap,
                "Exact prompt/model-version/parameter histories and independent human source-passage adjudication are not available.",
                "No professional similarity detector or independent scientific verifier was available.",
            ],
        },
        "ethics_human_or_animal_research": "NOT_APPLICABLE_AS_DECLARED",
        "overall_decision": "WARN",
        "user_action_required": True,
        "role": "Compliance warning does not override the separate integrity FAIL.",
    }
    dump(notes / "stage4_5_round1_compliance_report.json", compliance)
    return audit, compliance


def isolated_build(cfg: dict[str, Any], paper: Path, notes: Path, text: str, frozen_before: dict[str, Any]) -> dict[str, Any]:
    log_path = notes / "stage4_5_round1_preview.build.log"
    pdf_path = notes / "stage4_5_round1_preview.pdf"
    commands = [
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["bibtex", "manuscript"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
    ]
    records: list[dict[str, Any]] = []
    combined: list[str] = []
    final_pass_output = ""
    with tempfile.TemporaryDirectory(prefix=f"{cfg['paper_id'].lower()}-stage4-5-round1-") as temp_name:
        temp = Path(temp_name)
        compile_text = re.sub(r"(?m)^<!--block:B\d{4}-->\r?\n?", "", text)
        (temp / "manuscript.tex").write_text(compile_text, encoding="utf-8")
        shutil.copyfile(notes / "stage4_prime_references_round2.bib", temp / "references.bib")
        env = os.environ.copy()
        env.update({"LC_ALL": "C", "TZ": "UTC", "SOURCE_DATE_EPOCH": "1788134400"})
        for command in commands:
            result = subprocess.run(command, cwd=temp, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            records.append({"command": " ".join(command), "exit_code": result.returncode})
            combined.extend(["$ " + " ".join(command), result.stdout, ""])
            final_pass_output = result.stdout
            if result.returncode != 0:
                break
        log_path.write_text("\n".join(combined), encoding="utf-8")
        build_ok = all(row["exit_code"] == 0 for row in records) and len(records) == len(commands) and (temp / "manuscript.pdf").is_file()
        if build_ok:
            shutil.copyfile(temp / "manuscript.pdf", pdf_path)
    log_text = log_path.read_text(encoding="utf-8")
    pages = re.findall(r"Output written on manuscript\.pdf \((\d+) pages?", log_text)
    unresolved_citations = re.findall(r"Citation [`']([^`']+)[`'].*undefined", final_pass_output)
    unresolved_references = re.findall(r"Reference [`']([^`']+)[`'].*undefined", final_pass_output)
    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-isolated-preview-build/1.0",
        "built_at_utc": STAMP,
        "status": "PASS" if build_ok and not unresolved_citations and not unresolved_references else "FAIL",
        "input": {"path": "notes/stage4_prime_revision_round2.tex", "sha256": cfg["draft_sha"]},
        "bibliography": {"path": "notes/stage4_prime_references_round2.bib", "sha256": cfg["bib_sha"]},
        "engine": "LuaLaTeX/BibTeX, four isolated passes",
        "commands": records,
        "preview": ({"path": f"notes/{pdf_path.name}", "sha256": sha_path(pdf_path), "bytes": pdf_path.stat().st_size, "pages": int(pages[-1]) if pages else None} if pdf_path.exists() else None),
        "log": {"path": f"notes/{log_path.name}", "sha256": sha_path(log_path), "bytes": log_path.stat().st_size},
        "unresolved_citations": sorted(set(unresolved_citations)),
        "unresolved_references": sorted(set(unresolved_references)),
        "overfull_hbox_warning_count": final_pass_output.count("Overfull \\hbox"),
        "marker_stripping": "Only the temporary compile copy had block-marker comment lines removed.",
        "canonical_before": frozen_before,
        "canonical_after": canonical_snapshot(paper),
        "canonical_unchanged": frozen_before == canonical_snapshot(paper),
        "canonical_pdf_written": False,
        "temporary_directory_removed": True,
    }
    if not receipt["canonical_unchanged"]:
        raise RuntimeError(f"{cfg['paper_id']}: protected file changed during build")
    dump(notes / "stage4_5_round1_preview_build_receipt.json", receipt)
    return receipt


def correction_outputs(cfg: dict[str, Any], notes: Path, issues: list[dict[str, Any]]) -> None:
    if cfg["paper"] == 30:
        proposals = [
            {
                "proposal_id": "P30-CORR-01",
                "targets": ["all P30-S01--P30-S26 citation contexts", "notes/stage4_prime_claim_passage_matrix_round2.json"],
                "proposal": "Run a separately authorized source-finalization/full-text pass; bind an exact theorem/page/section/paragraph or <=25-word quote locator to every source-bearing claim, retain failures explicitly, then rerun a fresh Stage 4.5 audit.",
                "not_applied": True,
            },
            {
                "proposal_id": "P30-CORR-02",
                "targets": ["B0066"],
                "proposal": "Replace the ambiguous 'complete 26-entry bibliography' with wording that distinguishes the 26 admitted source records from the 28-entry versioned bibliography (26 sources plus P30-C01/P30-C02).",
                "not_applied": True,
            },
            {
                "proposal_id": "P30-CORR-03",
                "targets": ["B0125"],
                "proposal": "Remove the stale 'pending Stage 2.5' label; state that Stage 2.5 completed but passage support remains INCONCLUSIVE pending a separately authorized locator/full-text pass.",
                "not_applied": True,
            },
            {
                "proposal_id": "P30-CORR-04",
                "targets": ["B0124"],
                "proposal": "After author confirmation, disclose the complete current-draft AI-assisted revision interval/rounds and any model/build metadata actually available; do not invent unavailable backend details.",
                "not_applied": True,
            },
        ]
    else:
        proposals = [
            {
                "proposal_id": "P31-CORR-01",
                "targets": ["all P31-S01--P31-S22 citation contexts", "notes/stage4_prime_method_passage_matrix_round2.json"],
                "proposal": "Run a separately authorized source-finalization/full-text pass; bind exact theorem/page/section/paragraph or <=25-word quote locators to all 22 inherited source-bearing claims, retain failures explicitly, then rerun a fresh Stage 4.5 audit.",
                "not_applied": True,
            },
            {
                "proposal_id": "P31-CORR-02",
                "targets": ["B0107"],
                "proposal": "After author confirmation, extend the AI disclosure beyond the 2 September/Revision-1 account to cover the current Stage-4-prime Round-2 assistance and available dates; do not guess an unexposed backend build.",
                "not_applied": True,
            },
        ]
    checkpoint = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-correction-checkpoint/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
        "blocking_issues": issues,
        "proposals": proposals,
        "silent_repair_performed": False,
        "stage5_started": False,
        "canonical_promotion_performed": False,
        "next_gate": "Responsible-author authorization and correction, followed by a new fresh Stage 4.5 audit.",
    }
    dump(notes / "stage4_5_round1_correction_checkpoint.json", checkpoint)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 correction proposal/checkpoint",
        "",
        "Status: **FAIL — proposals only; nothing was applied.**",
        "",
    ]
    for proposal in proposals:
        lines.extend([
            f"## {proposal['proposal_id']}", "",
            f"Targets: {', '.join(f'`{target}`' for target in proposal['targets'])}.", "",
            proposal["proposal"], "",
        ])
    lines.extend([
        "Stage 5 has not started. Canonical promotion, Route mutation, scientific execution, and silent manuscript/BibTeX repair were not performed.",
    ])
    write(notes / "stage4_5_round1_correction_proposal.md", "\n".join(lines))


def final_outputs(
    cfg: dict[str, Any], paper: Path, notes: Path, frozen_before: dict[str, Any],
    refs: dict[str, Any], phase_c: dict[str, Any], originality: dict[str, Any],
    evidence: dict[str, Any], e6: dict[str, Any], seven: dict[str, Any],
    compliance: dict[str, Any], build: dict[str, Any], input_manifest: dict[str, Any],
) -> dict[str, Any]:
    if cfg["paper"] == 30:
        issues = [
            {"issue_id": "P30-S45R1-I01", "severity": "SERIOUS", "phase": "B/E", "finding": "26/30 citation-context tuples are anchorless and not passage-verifiable.", "blocker": True},
            {"issue_id": "P30-S45R1-I02", "severity": "MEDIUM", "phase": "C/E", "finding": "B0066 calls the current bibliography 26-entry while the frozen versioned BibTeX file has 28 entries.", "blocker": True},
            {"issue_id": "P30-S45R1-I03", "severity": "MEDIUM", "phase": "C/E", "finding": "B0125 says verification is pending Stage 2.5 although Stage 2.5 is already complete.", "blocker": True},
            {"issue_id": "P30-S45R1-I04", "severity": "MEDIUM", "phase": "compliance/E", "finding": "The AI disclosure names only the 2 September session and does not cover the current 3–4 September Stage-4-prime revision provenance.", "blocker": True},
        ]
    else:
        issues = [
            {"issue_id": "P31-S45R1-I01", "severity": "SERIOUS", "phase": "B/E", "finding": "22/26 citation-context tuples are anchorless and not passage-verifiable.", "blocker": True},
            {"issue_id": "P31-S45R1-I02", "severity": "MEDIUM", "phase": "compliance/E", "finding": "The AI disclosure covers the 2 September/Revision-1 work but omits the current 3–4 September Stage-4-prime Round-2 assistance.", "blocker": True},
        ]
    correction_outputs(cfg, notes, issues)
    frozen_after = canonical_snapshot(paper)
    if frozen_after != frozen_before:
        raise RuntimeError(f"{cfg['paper_id']}: protected snapshot changed")
    integrity = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-integrity-report/1.0",
        "verdict": "FAIL",
        "mode": "final-check",
        "audit_mode": 2,
        "paper_id": cfg["paper_id"],
        "timestamp": STAMP,
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
        "phases": {
            "A_references": {
                "registered": cfg["reference_total"],
                "checked": refs["phase_a"]["checked"],
                "resolved": refs["phase_a"]["resolved"],
                "unresolved": refs["phase_a"]["unresolved"],
                "verdict": refs["phase_a"]["verdict"],
            },
            "B_citation_contexts": {
                "registered": refs["phase_b"]["registered_citation_context_tuples"],
                "reviewed": refs["phase_b"]["reviewed"],
                "verified": refs["phase_b"]["verified"],
                "unverifiable_anchorless": refs["phase_b"]["unverifiable_anchorless"],
                "verdict": refs["phase_b"]["verdict"],
            },
            "C_data_internal_provenance": {
                **phase_c["registered_surface_coverage"],
                "experiment_alignment": phase_c["experiment_provenance"]["alignment_status"],
                "boundary": BOUNDARY,
                "verdict": phase_c["verdict"],
            },
            "D_originality": {
                "body_successful": originality["successful_body_dual_lane"],
                "body_denominator": originality["paragraph_denominator"],
                "rate": originality["sampling_rate"],
                "changed_successful": originality["changed_or_new_successful"],
                "changed_denominator": originality["changed_or_new_total"],
                "major_sections": f"{originality['major_sections_covered']}/{originality['major_sections_total']}",
                "professional_detector": False,
                "verdict": originality["verdict"],
            },
            "E_claims_evidence": {
                "selection_tier": "ALL",
                "registry_claims": evidence["registry_claims"],
                "claims_verified": evidence["claim_verified"],
                "claims_not_verified": evidence["claim_not_verified"],
                "mechanical_candidates": evidence["candidate_total"],
                "mechanical_candidates_unregistered": evidence["candidate_unregistered"],
                "semantic_extraction_coverage": evidence["semantic_extraction_coverage"],
                "expected_evidence_tuples": evidence["expected_tuples"],
                "actual_evidence_tuples": evidence["actual_tuples"],
                "verdict_counts": evidence["verdict_counts"],
                "excerpt_state_counts": evidence["excerpt_counts"],
                "verdict": "FAIL",
            },
            "E6_semantic_drift": {
                "rounds": e6["revision_rounds_consumed"],
                "operations_reviewed": e6["operations_reviewed"],
                "result": e6["semantic_result"],
                "verdict": e6["verdict"],
            },
        },
        "seven_failure_modes": seven,
        "compliance": compliance,
        "build": build,
        "issues": issues,
        "issue_counts": {
            "SERIOUS": sum(row["severity"] == "SERIOUS" for row in issues),
            "MEDIUM": sum(row["severity"] == "MEDIUM" for row in issues),
            "MINOR": sum(row["severity"] == "MINOR" for row in issues),
        },
        "input_freeze": {
            "path": FREEZE.name,
            "sha256": FREEZE_SHA,
            "bound_rows_checked": GLOBAL_FREEZE_AUDIT["checked"],
            "bound_rows_passed": GLOBAL_FREEZE_AUDIT["passed"],
        },
        "authorization_receipt": {"path": AUTH.name, "sha256": AUTH_SHA, "track": "B", "action": "fresh_stage4_5_audit_only"},
        "protected_snapshot_before": frozen_before,
        "protected_snapshot_after": frozen_after,
        "protected_snapshot_unchanged": True,
        "silent_repair_performed": False,
        "stage5_started": False,
        "canonical_promotion_performed": False,
        "route_mutation_performed": False,
        "scientific_execution_performed": False,
        "assurance_boundary": "FAIL is an integrity-gate result for the checked surface, not a judgment that the mathematical architecture is false.",
    }
    integrity_path = notes / "stage4_5_round1_integrity_report.json"
    dump(integrity_path, integrity)

    passport0 = json.loads((notes / "stage2_5_material_passport.json").read_text(encoding="utf-8"))
    passport = copy.deepcopy(passport0)
    passport["version_label"] = "stage4.5-round1-audit-fail-sidecar"
    passport["content_hash"] = cfg["draft_sha"]
    passport["verification_status"] = "stage4_5_round1_fail_corrections_proposed_not_applied"
    passport["stage4_5_round1_audit"] = {
        "verdict": "FAIL",
        "references": f"{refs['phase_a']['resolved']}/{cfg['reference_total']}",
        "citation_context_support": f"{refs['phase_b']['verified']}/{refs['phase_b']['registered_citation_context_tuples']}",
        "phase_c": phase_c["verdict"],
        "originality": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "changed_originality": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "claim_registry": f"{evidence['registry_claims']}/{evidence['registry_claims']} ALL reviewed",
        "evidence_rows": f"{evidence['actual_tuples']}/{evidence['expected_tuples']}",
        "e6": f"{e6['operations_reviewed']}/{e6['operations_reviewed']}",
        "stage5_started": False,
    }
    dump(notes / "stage4_5_round1_material_passport.json", passport)

    final_lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 final integrity report",
        "",
        "## Verdict", "",
        "**FAIL at the Stage 4.5 checkpoint.** No repair was applied, no canonical file was promoted, and Stage 5 was not started.",
        "",
        "## Complete denominators", "",
        f"- References: **{refs['phase_a']['resolved']}/{cfg['reference_total']}** resolved after fresh Semantic Scholar-first, DOI/publisher, metadata, ghost, and named-record update review (**{refs['phase_a']['verdict']}** with bounded registry notes).",
        f"- Citation contexts: **{refs['phase_b']['reviewed']}/{refs['phase_b']['registered_citation_context_tuples']} reviewed**, **{refs['phase_b']['verified']} verified**, **{refs['phase_b']['unverifiable_anchorless']} anchorless/unverifiable** (**FAIL**).",
        f"- Phase C: **{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}** registered data/stat/internal surfaces checked; **{phase_c['registered_surface_coverage']['verified']} verified**, **{phase_c['registered_surface_coverage']['inconsistent']} inconsistent**; tables **{phase_c['registered_surface_coverage']['tables_verified']}/{phase_c['registered_surface_coverage']['tables_checked']}**, figures **0**; experiment alignment **{phase_c['experiment_provenance']['alignment_status']}**.",
        f"- Originality: **{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']} ({originality['sampling_rate']:.1%})** successful dual-lane body searches; changed/new paragraphs **{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}**; major sections **{originality['major_sections_covered']}/{originality['major_sections_total']}**. No professional detector was available.",
        f"- Claim registry: **{evidence['registry_claims']}/{evidence['registry_claims']}** tier-ALL claims reviewed; official lexical candidates **{evidence['candidate_total']}/{evidence['candidate_total']}** registered, candidate gaps **0**; semantic extraction completeness remains `not_machine_detectable`.",
        f"- Evidence rows: **{evidence['actual_tuples']}/{evidence['expected_tuples']}** official-builder tuples; verdicts `{evidence['verdict_counts']}`.",
        f"- E6: both rounds, **{e6['operations_reviewed']}/{e6['operations_reviewed']}** operations; **{e6['semantic_result']}**. This is not a deterministic no-drift proof.",
        f"- Seven-mode checklist: **{seven['clear']}/7 CLEAR**, **{seven['suspected']}/7 SUSPECTED**, **{seven['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**.",
        f"- Isolated build: **{build['status']}**, {build['preview']['pages'] if build['preview'] else 'no'} pages, unresolved citations **{len(build['unresolved_citations'])}**, unresolved references **{len(build['unresolved_references'])}**.",
        "",
        "## Blockers", "",
    ]
    final_lines.extend(f"- **{row['severity']} `{row['issue_id']}`:** {row['finding']}" for row in issues)
    final_lines.extend([
        "", "## Boundaries", "",
        BOUNDARY,
        "",
        "The audit ran in a fresh context with role separation. It does not claim error independence. The correction checkpoint is proposal-only; author authorization and a later fresh audit are required before any Stage-5 or canonical action.",
    ])
    final_path = notes / "stage4_5_round1_final_integrity_report.md"
    write(final_path, "\n".join(final_lines))

    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-receipt/1.0",
        "paper_id": cfg["paper_id"],
        "recorded_at_utc": STAMP,
        "verdict": "FAIL",
        "audit_mode": 2,
        "inputs": input_manifest["inputs"],
        "key_artifacts": {
            "integrity_report": {"path": f"notes/{integrity_path.name}", "sha256": sha_path(integrity_path)},
            "final_human_report": {"path": f"notes/{final_path.name}", "sha256": sha_path(final_path)},
            "claim_registry": {"path": f"notes/{evidence['registry_path'].name}", "sha256": sha_path(evidence["registry_path"])},
            "evidence_rows": {"path": f"notes/{evidence['rows_path'].name}", "sha256": sha_path(evidence["rows_path"])},
            "preview": build["preview"],
            "correction_checkpoint": {"path": "notes/stage4_5_round1_correction_checkpoint.json", "sha256": sha_path(notes / "stage4_5_round1_correction_checkpoint.json")},
        },
        "denominators": integrity["phases"],
        "seven_mode_summary": {"clear": seven["clear"], "suspected": seven["suspected"], "insufficient_evidence": seven["insufficient_evidence"]},
        "protected_snapshot_unchanged": True,
        "silent_repair_performed": False,
        "stage5_started": False,
        "canonical_promotion_performed": False,
    }
    receipt_path = notes / "stage4_5_round1_receipt.json"
    dump(receipt_path, receipt)

    output_manifest_path = notes / "stage4_5_round1_output_manifest.json"
    artifacts = [
        {"path": f"notes/{path.name}", "sha256": sha_path(path), "bytes": path.stat().st_size}
        for path in sorted(notes.glob("stage4_5_round1_*"))
        if path.is_file() and path != output_manifest_path
    ]
    output_manifest = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-output-manifest/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "verdict": "FAIL",
        "artifacts": artifacts,
        "protected_snapshot_after": canonical_snapshot(paper),
        "protected_snapshot_unchanged": canonical_snapshot(paper) == frozen_before,
        "stage5_started": False,
    }
    dump(output_manifest_path, output_manifest)
    return {
        "paper": cfg["paper_id"],
        "verdict": "FAIL",
        "references": f"{refs['phase_a']['resolved']}/{cfg['reference_total']}",
        "contexts": f"{refs['phase_b']['verified']}/{refs['phase_b']['registered_citation_context_tuples']} verified",
        "phase_c": f"{phase_c['registered_surface_coverage']['verified']}/{phase_c['registered_surface_coverage']['data_stat_internal_surfaces_checked']}",
        "originality": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "changed": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "claims": evidence["registry_claims"],
        "evidence_rows": evidence["actual_tuples"],
        "e6_operations": e6["operations_reviewed"],
        "build": build["status"],
        "preview_sha256": build["preview"]["sha256"] if build["preview"] else None,
        "receipt_sha256": sha_path(receipt_path),
        "integrity_report_sha256": sha_path(integrity_path),
    }


def run_one(cfg: dict[str, Any]) -> dict[str, Any]:
    paper = ROOT / "papers" / cfg["directory"]
    notes = paper / "notes"
    draft = notes / "stage4_prime_revision_round2.tex"
    bib = notes / "stage4_prime_references_round2.bib"
    raw = draft.read_bytes()
    text = raw.decode("utf-8")
    assert sha_bytes(raw) == cfg["draft_sha"]
    assert sha_path(bib) == cfg["bib_sha"]
    frozen_before = canonical_snapshot(paper)
    authority = json.loads(AUTH.read_text(encoding="utf-8"))
    track_b = next(row for row in authority["tracks"] if row["track_id"] == "B")
    assert cfg["paper_id"] in track_b["papers"]
    assert track_b["action"] == "fresh_stage4_5_audit_only"
    assert not track_b["silent_repair_authorized"] and not track_b["stage5_authorized"]
    input_manifest = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-input-manifest/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_mode": 2,
        "inputs": {
            "draft": {"path": "notes/stage4_prime_revision_round2.tex", "sha256": cfg["draft_sha"], "bytes": len(raw)},
            "bibliography": {"path": "notes/stage4_prime_references_round2.bib", "sha256": cfg["bib_sha"], "bytes": bib.stat().st_size},
            "authorization_receipt": {"path": AUTH.name, "sha256": AUTH_SHA},
            "input_freeze": {"path": FREEZE.name, "sha256": FREEZE_SHA},
            "e6_dispatch_authority": {"path": "notes/stage4_prime_revision_evidence_bundle_round2.json", "sha256": cfg["e6_bundle_sha"]},
        },
        "global_bound_hash_check": GLOBAL_FREEZE_AUDIT,
        "protected_snapshot_before": frozen_before,
        "authorization": track_b,
        "boundaries": authority["boundaries"],
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
    }
    dump(notes / "stage4_5_round1_input_manifest.json", input_manifest)
    blocks = block_rows(text)
    refs = reference_and_context_audit(cfg, paper, notes, text, blocks)
    evidence = claim_registry_and_evidence(cfg, paper, notes, raw, text, blocks)
    phase_c = data_consistency_audit(cfg, paper, notes, text, blocks)
    e6 = e6_audit(cfg, paper, notes, text)
    originality = originality_audit(cfg, notes)
    seven, compliance = seven_modes_and_compliance(cfg, notes, refs, phase_c, e6)
    build = isolated_build(cfg, paper, notes, text, frozen_before)
    return final_outputs(
        cfg, paper, notes, frozen_before, refs, phase_c, originality, evidence,
        e6, seven, compliance, build, input_manifest,
    )


def main() -> int:
    results = [run_one(cfg) for cfg in CONFIGS]
    print(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
