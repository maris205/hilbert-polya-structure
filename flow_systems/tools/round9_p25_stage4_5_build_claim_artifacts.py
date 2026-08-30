#!/usr/bin/env python3
"""Build Paper 25 Stage-4.5 exact-draft claim/evidence/E6 artifacts.

The claim-bearing block census, sentence-split decisions, claim-kind
classifications, and E6 op assessments below are model-mediated semantic
decisions frozen for the exact Stage-4 draft hash.  This script performs the
bounded mechanical work after those decisions: exact UTF-8 span binding,
schema validation, replayable coverage construction, source-bound evidence-row
construction, and serialization of the recorded E6 result.

It does not edit the manuscript, bibliography, canonical results, README,
pipeline state, or any experiment artifact.  Mechanical validation cannot
establish semantic extraction completeness, claim truth, or an absence-of-drift
guarantee.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "papers" / "25-three-disk-scattering-flow"
NOTES = PROJECT / "notes"
RESULTS = PROJECT / "results"
EXPERIMENTS = PROJECT / "experiments"

DRAFT = NOTES / "stage4_revision_round1.tex"
EXPECTED_DRAFT_SHA256 = (
    "39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835"
)
REGISTRY_PATH = NOTES / "stage4_5_claim_registry.json"
COVERAGE_PATH = NOTES / "stage4_5_claim_registry_coverage.json"
COVERAGE_ADJUDICATION_PATH = (
    NOTES / "stage4_5_claim_registry_coverage_adjudication.md"
)
EVIDENCE_PATH = NOTES / "stage4_5_evidence_rows.json"
SOURCE_MAP_PATH = NOTES / "stage4_5_evidence_source_map.json"
DRIFT_PATH = NOTES / "stage4_5_claim_strength_drift_findings.json"
E6_AUDIT_PATH = NOTES / "stage4_5_e6_semantic_audit.md"

ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
EVIDENCE_ROWS_MODULE = ARS_ROOT / "scripts" / "evidence_rows.py"
COVERAGE_MODULE = ARS_ROOT / "scripts" / "claim_registry_coverage.py"
REVISION_VALIDATOR = ARS_ROOT / "scripts" / "revision_roadmap.py"
TOKEN_CHECKER = ARS_ROOT / "scripts" / "check_revision_token_conservation.py"
CLAIM_PROTOCOL = (
    ARS_ROOT
    / "academic-pipeline"
    / "references"
    / "claim_verification_protocol.md"
)
CLAIM_STRENGTH_LADDER = (
    ARS_ROOT / "shared" / "references" / "claim_strength_ladder.md"
)
REGISTRY_SCHEMA = (
    ARS_ROOT
    / "shared"
    / "contracts"
    / "evidence"
    / "claim_registry.schema.json"
)
DRIFT_SCHEMA = (
    ARS_ROOT
    / "shared"
    / "contracts"
    / "revision"
    / "claim_strength_drift_findings.schema.json"
)

BUNDLE = NOTES / "stage4_revision_evidence_bundle.json"
PATCH = NOTES / "stage4_revision_patch_round1.json"
BASE_DRAFT = NOTES / "stage3_revision_base.tex"
ROADMAP = NOTES / "stage3_revision_roadmap.json"
TOKEN_REPORT = NOTES / "stage4_token_conservation_round1.json"
EXTERNAL_AUDIT = NOTES / "stage4_5_reference_citation_audit.md"
REFERENCE_SOURCE_SNAPSHOT = NOTES / "stage4_5_reference_source_snapshot.json"

LOCAL_SOURCE_SLUG = "P25LocalArtifactChain"
EXPECTED_BLOCK_COUNT = 116
EXPECTED_REGISTRY_COUNT = 114
EXPECTED_MECHANICAL_CANDIDATES = 5
EXPECTED_EXTERNAL_EVIDENCE_ROWS = 13
EXPECTED_EVIDENCE_SHA256 = (
    "752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146"
)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def write_bytes(path: Path, raw: bytes) -> None:
    path.write_bytes(raw)


def line_anchor(text: str, start_char: int, end_char: int) -> str:
    start = text.count("\n", 0, start_char) + 1
    end = text.count("\n", 0, end_char) + 1
    if start == end:
        return f"notes/stage4_revision_round1.tex:L{start}"
    return f"notes/stage4_revision_round1.tex:L{start}-L{end}"


def char_to_byte_offsets(text: str) -> list[int]:
    offsets = [0]
    total = 0
    for char in text:
        total += len(char.encode("utf-8"))
        offsets.append(total)
    return offsets


@dataclass(frozen=True)
class Block:
    block_id: str
    marker_start: int
    body_start: int
    body_end: int
    text: str


BLOCK_RE = re.compile(r"<!--block:(B[0-9]{4,})-->\n")
CITE_RE = re.compile(r"\\cite\w*\s*(?:\[[^\]]*\]\s*)?\{([^}]*)\}")
SECTION_RE = re.compile(r"\\(?:sub)*section\*?\{([^}]*)\}")
QUANT_RE = re.compile(
    r"(?<![A-Za-z])\d[\d,._/-]*|"
    r"\\(?:frac|sum|dim|tr|det|Lambda|sqrt|overline|mathbb)\b"
)
CATEGORICAL_RE = re.compile(
    r"\b(?:no|none|never|every|all|exact|exactly|cannot|fails?|holds?|"
    r"proves?|refutes?|rules? out|is not|are not|unassigned|only)\b",
    re.I,
)
CAUSAL_RE = re.compile(
    r"\b(?:because|therefore|thus|hence|implies?|forces?|consequently|"
    r"since|so that)\b",
    re.I,
)
TREND_RE = re.compile(
    r"\b(?:increase|decrease|reduce|grow|decline|improve|worsen|"
    r"larger|smaller|higher|lower|stable|persists?)\b",
    re.I,
)


# These 29 blocks were inspected and frozen as manuscript structure rather
# than claim-bearing text.  Every other current block is included, except that
# B0047--B0049 are joined into one proof surface and the sentence-split blocks
# below are registered at a finer granularity.
NONCLAIM_BLOCKS = frozenset(
    {
        "B0001",
        "B0002",
        "B0003",
        "B0005",
        "B0007",
        "B0009",
        "B0017",
        "B0022",
        "B0023",
        "B0027",
        "B0030",
        "B0032",
        "B0036",
        "B0041",
        "B0052",
        "B0062",
        "B0068",
        "B0069",
        "B0072",
        "B0077",
        "B0081",
        "B0084",
        "B0088",
        "B0089",
        "B0092",
        "B0095",
        "B0100",
        "B0107",
        "B0110",
    }
)
JOINED_PROOF_BLOCKS = ("B0047", "B0048", "B0049")
SENTENCE_SPLIT_BLOCKS = frozenset(
    {
        "B0011",
        "B0026",
        "B0029",
        "B0031",
        "B0050",
        "B0051",
        "B0057",
        "B0109",
    }
)


EXTERNAL_EXCERPTS_BY_CLAIM = {
    ("P25-S45-E1-B0011-S01", "Ikawa1988"): (
        "Periodic rays and Poincare maps in exterior-wave decay analysis"
    ),
    ("P25-S45-E1-B0011-S02", "GaspardRice1989Semiclassical"): (
        "Periodic-orbit semiclassical organization of three-disk resonances"
    ),
    ("P25-S45-E1-B0011-S03", "GaspardRice1989Exact"): (
        "Exact scattering uses a multiple-scattering matrix/determinant rather "
        "than the manuscript's symbolic adjacency determinant"
    ),
    ("P25-S45-E1-B0026-S02", "Livsic1972"): (
        "Constant-cohomology implies equal periodic means; manuscript uses only "
        "the necessary telescoping direction"
    ),
    ("P25-S45-E1-B0026-S03", "BowenLanford1970"): (
        "Reciprocal determinant for a finite-type shift"
    ),
    ("P25-S45-E1-B0026-S04", "Ruelle1976"): (
        "Flow-zeta/operator construction retains actual periods and weights"
    ),
    ("P25-S45-E1-B0026-S05", "Wirzba1999"): (
        "Established separation of symbolic, classical, semiclassical, and "
        "exact multiscattering objects"
    ),
    ("P25-S45-E1-B0029-S01", "BowenLanford1970"): (
        "Reciprocal-determinant finite-type shift zeta"
    ),
    ("P25-S45-E1-B0029-S02", "Ruelle1976"): (
        "Flow timing and dynamical weights are not discarded"
    ),
    ("P25-S45-E1-B0031-S03", "GaspardRice1989Exact"): (
        "Three-hard-disk S-matrix resonances use the multiscattering determinant"
    ),
    ("P25-S45-E1-B0031-S04", "Wirzba1999"): (
        "Exact determinant structure and non-interchangeable "
        "semiclassical/cumulant limits"
    ),
    ("P25-S45-E1-B0051-S01", "CvitanovicEckhardt1989"): (
        "Effectiveness of periodic-orbit quantization/cycle methods"
    ),
    ("P25-S45-E1-B0057-S01", "Livsic1972"): (
        "Periodic sums as the standard cohomological obstruction"
    ),
}
EXTERNAL_SOURCE_SLUGS = frozenset(
    slug for _, slug in EXTERNAL_EXCERPTS_BY_CLAIM
)


LOCAL_CHAIN_INPUTS = (
    DRAFT,
    NOTES / "round8_roof_nontransfer_theorem.md",
    RESULTS / "round6_symbolic_owner_counts.csv",
    RESULTS / "round7_q_symbolic_summary.json",
    RESULTS / "round8_exact_roof_witnesses.csv",
    RESULTS / "round8_physical_roof_replay.csv",
    RESULTS / "round8_roof_nontransfer_summary.json",
    EXPERIMENTS / "round8_roof_nontransfer_freeze.json",
    EXPERIMENTS / "round8_validation.md",
    EXPERIMENTS / "stage4_reproducibility_lock.json",
    EXPERIMENTS / "stage4_reproducibility_receipt.json",
    NOTES / "stage4_revision_evidence_bundle.json",
    NOTES / "stage2_5_material_passport.json",
    REFERENCE_SOURCE_SNAPSHOT,
    EXTERNAL_AUDIT,
)


OP_REVIEWS = (
    (
        0,
        "B0013 / REV-001",
        "The categorical noncohomology conclusion is unchanged; cannot be and "
        "is not are the same theorem-level assertion here. The explicit sharp "
        "two-witness bound already appears in the untouched minimax corollary.",
        "Same categorical rung; novelty is narrowed to the two-witness scalar-bridge audit.",
    ),
    (
        1,
        "B0015 / REV-003",
        "The 747, 2,241, and 744 counts are conserved and their role is reduced "
        "to solver, serialization, and rebuild validation.",
        "Downward evidentiary narrowing; no replay row is promoted to theorem evidence.",
    ),
    (
        2,
        "B0018 / REV-002",
        "The four objects are named and typed, while the scalar bridge remains "
        "the only tested bridge and equality among objects is expressly denied.",
        "Clarification at the same rung with an added scope guard.",
    ),
    (
        3,
        "B0026 / REV-001",
        "Established cohomology, symbolic-zeta, flow-zeta, and scattering "
        "frameworks are added with citations; the manuscript expressly disclaims "
        "those general contributions.",
        "Literature-supported addition plus narrowed novelty, not a priority promotion.",
    ),
    (
        4,
        "B0033 / REV-001, REV-002",
        "The former prose distinction becomes a four-row object map. The physical "
        "row constructs no determinant, the semiclassical row claims only a "
        "controlled approximation, and shared labels do not imply equality.",
        "Same categorical distinctions with stronger anti-transfer qualifiers.",
    ),
    (
        5,
        "B0078 / REV-003",
        "The table inputs and 3/744 split are unchanged; a new paragraph limits "
        "them to the declared finite owner population.",
        "Downward evidentiary narrowing.",
    ),
    (
        6,
        "B0079 / REV-003",
        "All table values are byte-conserved and the added sentence denies a "
        "second numerical proof of the exact theorem.",
        "Unchanged quantitative rung with an added limitation.",
    ),
    (
        7,
        "B0082 / REV-004, REV-006",
        "The Stage-4 dependency lock, receipt, read-only command, and 68-file "
        "inventory add reproducibility metadata without changing scientific results.",
        "Administrative/provenance addition outside the scientific strength ladder.",
    ),
    (
        8,
        "B0090 / REV-002",
        "The symbolic typed tuple and Route-A rejection are conserved; the new "
        "object-map reference reinforces that symbolic A1/A2 credit stays local.",
        "Same categorical rung with an explicit nontransfer guard.",
    ),
    (
        9,
        "B0091 / REV-002",
        "The physical tuple remains unassigned and the theorem is explicitly "
        "limited to the owner- and repetition-preserving scalar bridge.",
        "Narrower theorem interpretation; no determinant credit is added.",
    ),
    (
        10,
        "B0102 / REV-003",
        "The finite 2,241-row ledger remains bounded to length twelve and gains "
        "explicit exclusions for asymptotics, an infinite census, and the full trapped set.",
        "Downward evidentiary narrowing.",
    ),
    (
        11,
        "B0105 / REV-001",
        "The open-status wording is made manuscript-scoped, construction and "
        "analytic-continuation absences are listed, and no equality is claimed.",
        "Narrowed field-level scope; same object distinction.",
    ),
    (
        12,
        "B0108 / REV-001, REV-002, REV-003",
        "The exact two-witness theorem is retained, the three-disk increment is "
        "bounded within established frameworks, and the replay is validation only.",
        "Same theorem rung with stronger ownership and replay limitations.",
    ),
    (
        13,
        "B0109 / REV-004, REV-005, REV-006",
        "Scientific and authorship declarations are conserved; only the obsolete "
        "audit pointer is replaced by the current lock, receipt, and read-only command.",
        "Administrative correction outside the scientific strength ladder.",
    ),
)


def parse_blocks(text: str) -> tuple[list[Block], dict[str, Block]]:
    matches = list(BLOCK_RE.finditer(text))
    blocks: list[Block] = []
    for index, match in enumerate(matches):
        raw_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        raw_body = text[match.end() : raw_end]
        leading = len(raw_body) - len(raw_body.lstrip())
        trailing = len(raw_body.rstrip())
        if trailing <= leading:
            raise RuntimeError(f"{match.group(1)} has an empty body")
        start = match.end() + leading
        end = match.end() + trailing
        blocks.append(
            Block(
                block_id=match.group(1),
                marker_start=match.start(),
                body_start=start,
                body_end=end,
                text=text[start:end],
            )
        )
    by_id = {block.block_id: block for block in blocks}
    if len(blocks) != EXPECTED_BLOCK_COUNT or len(by_id) != EXPECTED_BLOCK_COUNT:
        raise RuntimeError(
            f"block census changed: {len(blocks)} total, expected {EXPECTED_BLOCK_COUNT}"
        )
    return blocks, by_id


def refs_for(fragment: str) -> list[str]:
    refs: set[str] = set()
    for match in CITE_RE.finditer(fragment):
        refs.update(key.strip() for key in match.group(1).split(",") if key.strip())
    return sorted(refs)


def kinds_for(fragment: str) -> list[str]:
    kinds: list[str] = []
    if QUANT_RE.search(fragment):
        kinds.append("quantitative")
    if CATEGORICAL_RE.search(fragment):
        kinds.append("categorical")
    if TREND_RE.search(fragment):
        kinds.append("trend")
    if CAUSAL_RE.search(fragment):
        kinds.append("causal")
    if not kinds:
        kinds.append("other_factual")
    return kinds


def section_for(text: str, position: int, block_id: str) -> str:
    if block_id == "B0004":
        return "Title block"
    if block_id == "B0006":
        return "Abstract"
    if block_id == "B0008":
        return "Traditional Chinese Abstract"
    section = "Front matter"
    for match in SECTION_RE.finditer(text, 0, position):
        section = match.group(1)
    return section


def make_claim(
    *,
    claim_id: str,
    fragment: str,
    start_char: int,
    end_char: int,
    block_id: str,
    text: str,
    offsets: list[int],
    extra_anchor: str | None = None,
) -> dict[str, Any]:
    if text[start_char:end_char] != fragment:
        raise RuntimeError(f"{claim_id}: char-span round trip failed")
    raw = text.encode("utf-8")
    start_byte = offsets[start_char]
    end_byte = offsets[end_char]
    if raw[start_byte:end_byte].decode("utf-8") != fragment:
        raise RuntimeError(f"{claim_id}: byte-span round trip failed")
    if len(fragment) > 2000:
        raise RuntimeError(f"{claim_id}: evidence-row text exceeds 2000 characters")
    anchors = [
        line_anchor(text, start_char, end_char),
        f"block:{block_id}",
    ]
    if extra_anchor:
        anchors.append(extra_anchor)
    return {
        "claim_id": claim_id,
        "claim_text": fragment,
        "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
        "claim_kinds": kinds_for(fragment),
        "ref_slugs": [LOCAL_SOURCE_SLUG, *refs_for(fragment)],
        "writer_anchors": anchors,
        "paper_section": section_for(text, start_char, block_id),
        "selection_tier": "ALL",
    }


def build_claims(
    text: str,
    offsets: list[int],
    coverage_module: Any,
) -> tuple[list[dict[str, Any]], list[Block]]:
    blocks, by_id = parse_blocks(text)
    claims: list[dict[str, Any]] = []
    sentence_rows = coverage_module._sentences(text)

    for block in blocks:
        if block.block_id in NONCLAIM_BLOCKS:
            continue
        if block.block_id in JOINED_PROOF_BLOCKS:
            continue
        if block.block_id in SENTENCE_SPLIT_BLOCKS:
            selected_sentences = [
                row
                for row in sentence_rows
                if row["start_char"] >= block.body_start
                and row["end_char"] <= block.body_end
                and not str(row["text"]).lstrip().startswith("%")
                and not re.fullmatch(
                    r"\\(?:sub)*section\*?\{[^}]*\}",
                    str(row["text"]).strip(),
                )
            ]
            if not selected_sentences:
                raise RuntimeError(f"{block.block_id}: sentence split produced no claims")
            for ordinal, row in enumerate(selected_sentences, start=1):
                claims.append(
                    make_claim(
                        claim_id=(
                            f"P25-S45-E1-{block.block_id}-S{ordinal:02d}"
                        ),
                        fragment=str(row["text"]),
                        start_char=int(row["start_char"]),
                        end_char=int(row["end_char"]),
                        block_id=block.block_id,
                        text=text,
                        offsets=offsets,
                        extra_anchor=(
                            f"semantic sentence split; source sentence index "
                            f"{row['sentence_index']}"
                        ),
                    )
                )
            continue
        claims.append(
            make_claim(
                claim_id=f"P25-S45-E1-{block.block_id}",
                fragment=block.text,
                start_char=block.body_start,
                end_char=block.body_end,
                block_id=block.block_id,
                text=text,
                offsets=offsets,
            )
        )

    proof_start = by_id[JOINED_PROOF_BLOCKS[0]].body_start
    proof_end = by_id[JOINED_PROOF_BLOCKS[-1]].body_end
    claims.append(
        make_claim(
            claim_id="P25-S45-E1-B0047-B0049",
            fragment=text[proof_start:proof_end],
            start_char=proof_start,
            end_char=proof_end,
            block_id="B0047-B0049",
            text=text,
            offsets=offsets,
            extra_anchor="joined proof surface across layout-only block splits",
        )
    )
    claims.sort(
        key=lambda row: (
            row["draft_span"]["start_byte"],
            row["draft_span"]["end_byte"],
            row["claim_id"],
        )
    )

    seen_ids: set[str] = set()
    seen_spans: set[tuple[int, int]] = set()
    for claim in claims:
        claim_id = str(claim["claim_id"])
        span = (
            int(claim["draft_span"]["start_byte"]),
            int(claim["draft_span"]["end_byte"]),
        )
        if claim_id in seen_ids or span in seen_spans:
            raise RuntimeError(f"duplicate claim id or exact span at {claim_id}")
        seen_ids.add(claim_id)
        seen_spans.add(span)
    if len(claims) != EXPECTED_REGISTRY_COUNT:
        raise RuntimeError(
            f"claim population changed: {len(claims)}, expected {EXPECTED_REGISTRY_COUNT}"
        )
    return claims, blocks


def build_local_source() -> str:
    chunks: list[str] = []
    for path in LOCAL_CHAIN_INPUTS:
        raw = path.read_bytes()
        content = raw.decode("utf-8", errors="strict")
        relative = path.relative_to(ROOT)
        chunks.append(
            "\n".join(
                [
                    f"===== BEGIN {relative} =====",
                    f"sha256={sha256(raw)}",
                    content,
                    f"===== END {relative} =====",
                ]
            )
        )
    return "\n\n".join(chunks) + "\n"


def bounded_excerpt(fragment: str, word_cap: int = 20) -> str:
    tokens = list(re.finditer(r"\S+", fragment))
    if not tokens:
        raise RuntimeError("cannot excerpt an empty claim")
    last = tokens[min(word_cap, len(tokens)) - 1]
    excerpt = fragment[tokens[0].start() : last.end()]
    if len(excerpt.split()) > 25 or len(excerpt) > 1000:
        raise RuntimeError("local excerpt exceeds ARS evidence-row bounds")
    return excerpt


def evidence_template(
    claim: dict[str, Any],
    ref_slug: str,
    *,
    external: bool,
    audit_sha: str,
) -> dict[str, Any]:
    if external:
        source = {
            "ref_slug": ref_slug,
            "display_label": f"{ref_slug} fresh Stage-4.5 audit carrier",
            "source_artifact_sha256": audit_sha,
        }
        anchor = "Stage4.5 fresh Phase-B citation-context audit"
        detail = (
            f"Source-bound to the current Stage-4.5 fresh Phase-A/B "
            f"citation-context audit entry for {ref_slug}. This replays the "
            "persisted audit carrier and does not copy the primary publication."
        )
    else:
        source = {
            "ref_slug": ref_slug,
            "display_label": "Paper 25 frozen local artifact chain",
        }
        anchor = "Current draft and frozen local artifact chain"
        detail = (
            "The exact current-draft span is present in the persisted local "
            "artifact chain, which also carries the frozen theorem, result, "
            "lock, receipt, bundle, and passport materials. This binds "
            "provenance and does not independently establish semantic truth."
        )
    return {
        "surface": "phase_e_claim_verification",
        "row_id": f"EVR-{claim['claim_id']}-{ref_slug}",
        "claim": {
            "claim_id": claim["claim_id"],
            "text": claim["claim_text"],
            "paper_locator": claim["writer_anchors"][0],
            "selection_tier": "ALL",
        },
        "source": source,
        "anchor": {
            "kind": "section",
            "value_encoded": quote(anchor, safe="-._~"),
        },
        "verdict": "VERIFIED",
        "detail": detail,
    }


def build_evidence_rows(
    claims: list[dict[str, Any]],
    source_map: dict[str, str],
    evidence_rows_module: Any,
) -> list[dict[str, Any]]:
    audit_sha = sha256(EXTERNAL_AUDIT.read_bytes())
    rows: list[dict[str, Any]] = []
    for claim in claims:
        for ref_slug in claim["ref_slugs"]:
            external = ref_slug != LOCAL_SOURCE_SLUG
            excerpt = (
                EXTERNAL_EXCERPTS_BY_CLAIM[
                    (str(claim["claim_id"]), ref_slug)
                ]
                if external
                else bounded_excerpt(str(claim["claim_text"]))
            )
            source_text = source_map[ref_slug]
            if excerpt not in source_text:
                raise RuntimeError(
                    f"{claim['claim_id']}/{ref_slug}: excerpt absent from held source"
                )
            if len(excerpt.split()) > 25:
                raise RuntimeError(
                    f"{claim['claim_id']}/{ref_slug}: excerpt exceeds 25 words"
                )
            template = evidence_template(
                claim,
                ref_slug,
                external=external,
                audit_sha=audit_sha,
            )
            rows.append(
                evidence_rows_module.build(
                    template,
                    source_text,
                    extracted_text=excerpt,
                )
            )
    evidence_rows_module.paginate(rows)
    return rows


def coverage_adjudication(
    *,
    registry_raw: bytes,
    coverage_raw: bytes,
    coverage: dict[str, Any],
    evidence_rows: list[dict[str, Any]],
    source_map_raw: bytes,
) -> str:
    external_rows = sum(
        row["source"]["ref_slug"] != LOCAL_SOURCE_SLUG for row in evidence_rows
    )
    source_bound = sum(
        row["excerpt"]["state"]
        in {"verified_exact_match", "agent_extracted", "unconfirmed_anchor"}
        for row in evidence_rows
    )
    candidate_lines = "\n".join(
        (
            f"| {row['candidate_id']} | {row['line']} | "
            f"{', '.join(row['candidate_kinds'])} | "
            f"{', '.join(row['matched_claim_ids'])} |"
        )
        for row in coverage["candidates"]
    )
    return f"""# Paper 25 Stage 4.5 E1.1 coverage adjudication

Audit date: **2026-08-30 UTC**

This is a draft-bound mechanical and semantic-census sidecar. It is not an
overall Stage-4.5 verdict and does not advance the pipeline.

## Exact bindings and counts

- Current work draft: notes/stage4_revision_round1.tex
- Draft SHA-256: {EXPECTED_DRAFT_SHA256}
- Claim Registry SHA-256: {sha256(registry_raw)}
- Coverage report SHA-256: {sha256(coverage_raw)}
- Evidence-row file: {len(evidence_rows)} rows
- Evidence source-map SHA-256: {sha256(source_map_raw)}
- Registry population: {EXPECTED_REGISTRY_COUNT} rows, all selection_tier=ALL
- Mechanical candidates: {len(coverage['candidates'])}
- Mechanical candidates with exact full-span registry matches:
  {len(coverage['candidates']) - coverage['candidate_unregistered_count']}
- candidate_unregistered_count: {coverage['candidate_unregistered_count']}
- semantic_extraction_coverage:
  {coverage['semantic_extraction_coverage']}

Within the frozen model-mediated population, {EXPECTED_REGISTRY_COUNT} of
{EXPECTED_REGISTRY_COUNT} claims are registered and ALL-selected, and every
registered (claim_id, ref_slug) projection has a persisted evidence row. This
is 100% coverage of the frozen current-draft claim population. It is not a
machine proof that no additional semantic claim could be identified.

## Population census

The exact draft contains {EXPECTED_BLOCK_COUNT} anchored blocks. The semantic
census excludes only 29 inspected structural blocks: LaTeX setup and macros,
begin/end-document plumbing, keywords, heading-only blocks, and the bibliography
invocation. Every other current block from title metadata through English and
Traditional-Chinese abstracts, main text, tables, proofs, conclusion, and
declarations is included.

Seven citation-dense or compound scientific blocks and the declaration block
are split at exact sentence spans. Comment-only SOURCE carrier lines and
heading-only declaration labels are not themselves registered as claims.
B0047--B0049 are one mathematical proof surface because those three markers
are layout splits inside one proof. The five bounded candidates emitted by the
official ARS detector are exact members of this already-frozen population.

## Mechanical candidate replay

| Candidate | Line | Detector class | Exact registry row |
|---|---:|---|---|
{candidate_lines}

The official detector is deliberately conservative: its candidate scope is
limited to citation-bearing sentences with inline machine anchors and selected
quantitative lexical triggers. The semantic block census therefore includes
many claims outside those mechanical classes.

## Evidence projection and source boundary

- Expected evidence tuples: {len(evidence_rows)}
- Persisted evidence rows: {len(evidence_rows)}
- Source-bound excerpt states: {source_bound}
- Anchorless rows: {len(evidence_rows) - source_bound}
- Local artifact-chain rows: {len(evidence_rows) - external_rows}
- Fresh Stage-4.5 external-audit-carrier rows: {external_rows}
- Distinct source-map slugs: {len(EXTERNAL_SOURCE_SLUGS) + 1}

P25LocalArtifactChain persists the exact current draft together with frozen
theorem, symbolic-count, physical replay, witness, lock, receipt, Revision-
Evidence Bundle, Material Passport, fresh reference snapshot, and citation
audit carriers. The eight bibliography slugs map to the exact bytes of the
current Stage-4.5 fresh Phase-A/B citation-context audit, with one short exact
excerpt for each of its 13 checked contexts. Those external rows are
source-bound to the fresh audit carrier; they are not represented as local
copies of the primary publications.
Likewise, a current-draft/local-artifact binding establishes provenance and
replayable bytes, not independent mathematical truth.

## Replay commands

~~~text
PYTHONDONTWRITEBYTECODE=1 python \
  {COVERAGE_MODULE} \
  --draft {DRAFT} \
  --registry {REGISTRY_PATH} \
  --validate-report {COVERAGE_PATH}

PYTHONDONTWRITEBYTECODE=1 python \
  {EVIDENCE_ROWS_MODULE} validate \
  {EVIDENCE_PATH} \
  --source-map {SOURCE_MAP_PATH}
~~~
"""


def e6_audit(
    *,
    bundle_sha: str,
    drift_raw: bytes,
    token_report: dict[str, Any],
) -> str:
    review_lines = "\n".join(
        f"| {op} | {surface} | {assessment} | {movement} |"
        for op, surface, assessment, movement in OP_REVIEWS
    )
    advisories = "\n".join(
        f"- {row}" for row in token_report["advisory_rows"]
    )
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    round_one = bundle["rounds"][0]
    chain_lines = "\n".join(
        [
            (
                f"- Pre-round draft: {round_one['pre_round_draft']['path']} — "
                f"{round_one['pre_round_draft']['sha256']}"
            ),
            (
                f"- Pre-round block manifest: "
                f"{round_one['pre_round_block_manifest']['path']} — "
                f"{round_one['pre_round_block_manifest']['sha256']}"
            ),
            (
                f"- Roadmap: {round_one['revision_roadmap']['path']} — "
                f"{round_one['revision_roadmap']['sha256']}"
            ),
            (
                f"- Claim-surface manifest: "
                f"{round_one['claim_surface_manifest']['path']} — "
                f"{round_one['claim_surface_manifest']['sha256']}"
            ),
            (
                f"- Author adjudication: {round_one['author_adjudication']['path']} — "
                f"{round_one['author_adjudication']['sha256']}"
            ),
            (
                f"- Revision patch: {round_one['revision_patch']['path']} — "
                f"{round_one['revision_patch']['sha256']}"
            ),
            (
                f"- Apply report: {round_one['apply_report']['path']} — "
                f"{round_one['apply_report']['sha256']}"
            ),
            (
                f"- Final draft: {round_one['post_round_draft']['path']} — "
                f"{round_one['post_round_draft']['sha256']}"
            ),
        ]
    )
    return f"""# Paper 25 Stage 4.5 E6 independent semantic audit

## Recorded result

**None detected by the recorded semantic review.**

The schema-valid companion has an empty ordered finding set. This is a
model-mediated review result, not a deterministic no-drift certificate, a
completeness guarantee, an author disposition, or an overall Stage-4.5 verdict.
No Stage-5 transition is authorized by this artifact.

## Detector and protocol binding

| Field | Value |
|---|---|
| Detector kind | model_mediated_semantic_review |
| Detector ID | codex-session-model/p25-stage4.5-e6-independent-20260830 |
| Exact final draft SHA-256 | {EXPECTED_DRAFT_SHA256} |
| Revision-Evidence Bundle SHA-256 | {bundle_sha} |
| Finding-set SHA-256 | {sha256(drift_raw)} |
| Claim-verification protocol SHA-256 | {sha256(CLAIM_PROTOCOL.read_bytes())} |
| Claim-strength ladder SHA-256 | {sha256(CLAIM_STRENGTH_LADDER.read_bytes())} |
| Token checker SHA-256 | {sha256(TOKEN_CHECKER.read_bytes())} |
| Finding schema SHA-256 | {sha256(DRIFT_SCHEMA.read_bytes())} |
| Bundle validator SHA-256 | {sha256(REVISION_VALIDATOR.read_bytes())} |

## Fresh bundle comparison population

The complete Revision-Evidence Bundle was used as the comparison authority:

{chain_lines}

The exact patch has 14 replace_block operations. Its layout re-emission splits
six added continuation paragraphs into B0111--B0116; those are reviewed with
their owning operations rather than treated as untracked revisions. All patch-
level claim_strength_changes and collateral_authorization_ids arrays are empty,
so block-edit permission was not treated as permission for a silent strength
move.

## Operation-by-operation rung and qualifier review

Categorical theorem assertion is used here as the field-relative analogue of
the ladder's top categorical rung. Administrative metadata is reported as
outside that scientific ladder.

| Op | Block / roadmap | Recorded semantic comparison | Rung or qualifier result |
|---:|---|---|---|
{review_lines}

## Token-conservation sibling

The deterministic checker reports conserved=false because four advisory
deltas require semantic attribution; it does not itself classify drift:

{advisories}

The added 2 in op 0 makes the already-proved two-witness lower bound explicit.
The op-3 numbers and citations are source locators, the op-4 decimals are table
column widths, and the op-7 numbers are dependency versions, round ranges, and
the closed inventory count. The recorded review found each delta specifically
authorized by its roadmap item and found no dropped scientific hedge, null
result, limitation, or ownership guard.

## Commands used for the bounded replay

~~~text
PYTHONDONTWRITEBYTECODE=1 python \
  {REVISION_VALIDATOR} validate-bundle \
  {BUNDLE} --root {PROJECT}

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH={ARS_ROOT} python \
  {TOKEN_CHECKER} patch \
  --patch {PATCH} \
  --base {BASE_DRAFT}
~~~

## Boundary

An empty findings array means only that this recorded model-mediated review
did not identify an unauthorized strength movement in the exact bundle-bound
comparison. A later reviewer can supersede it with a new exact finding set.
The mechanical validators establish shape, hashes, replay, and token deltas;
they do not establish semantic correctness.
"""


def main() -> int:
    draft_raw = DRAFT.read_bytes()
    if sha256(draft_raw) != EXPECTED_DRAFT_SHA256:
        raise RuntimeError(
            "current work draft hash changed; refusing to build Stage-4.5 artifacts"
        )
    text = draft_raw.decode("utf-8", errors="strict")
    offsets = char_to_byte_offsets(text)

    evidence_rows_module = load_module(
        EVIDENCE_ROWS_MODULE, "p25_stage45_evidence_rows"
    )
    coverage_module = load_module(
        COVERAGE_MODULE, "p25_stage45_claim_registry_coverage"
    )
    claims, blocks = build_claims(text, offsets, coverage_module)
    registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": EXPECTED_DRAFT_SHA256,
        "claims": claims,
    }
    registry_schema = json.loads(REGISTRY_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(registry_schema).validate(registry)
    registry_raw = json_bytes(registry)

    coverage = coverage_module.build_report(draft_raw, registry_raw)
    if len(coverage["candidates"]) != EXPECTED_MECHANICAL_CANDIDATES:
        raise RuntimeError(
            "mechanical candidate population changed: "
            f"{len(coverage['candidates'])}, expected "
            f"{EXPECTED_MECHANICAL_CANDIDATES}"
        )
    if coverage["candidate_unregistered_count"] != 0:
        raise RuntimeError(
            "frozen claim population does not exactly cover all mechanical candidates"
        )
    if any(
        row["coverage_state"] != "registry_span_matched"
        for row in coverage["candidates"]
    ):
        raise RuntimeError("a mechanical candidate lacks clean exact-span coverage")
    coverage_raw = json_bytes(coverage)

    local_source = build_local_source()
    external_audit_text = EXTERNAL_AUDIT.read_text(encoding="utf-8")
    if len(EXTERNAL_EXCERPTS_BY_CLAIM) != EXPECTED_EXTERNAL_EVIDENCE_ROWS:
        raise RuntimeError("fresh external context excerpt population changed")
    for (_, slug), excerpt in EXTERNAL_EXCERPTS_BY_CLAIM.items():
        if excerpt not in external_audit_text:
            raise RuntimeError(f"{slug}: frozen external audit excerpt not found")
    source_map = {
        LOCAL_SOURCE_SLUG: local_source,
        **{slug: external_audit_text for slug in EXTERNAL_SOURCE_SLUGS},
    }
    source_map_raw = json_bytes(source_map)

    # Evidence rows persist the evaluator-owned extraction timestamp.  That
    # timestamp is an audit event, not a deterministic build product.  Replay
    # therefore validates and reuses the exact frozen row bytes instead of
    # calling build() again (which would mint a new captured_at and silently
    # invalidate every downstream hash pointer).
    if not EVIDENCE_PATH.is_file():
        raise RuntimeError(
            "frozen Stage-4.5 evidence rows are missing; a fresh semantic "
            "extraction event requires a new explicitly versioned artifact"
        )
    evidence_raw = EVIDENCE_PATH.read_bytes()
    if sha256(evidence_raw) != EXPECTED_EVIDENCE_SHA256:
        raise RuntimeError(
            "frozen Stage-4.5 evidence-row bytes changed; refusing to mint "
            "replacement extraction timestamps during replay"
        )
    evidence_rows = json.loads(evidence_raw.decode("utf-8", errors="strict"))
    if json_bytes(evidence_rows) != evidence_raw:
        raise RuntimeError("frozen evidence rows are not canonical JSON bytes")
    expected_rows = sum(len(claim["ref_slugs"]) for claim in claims)
    if len(evidence_rows) != expected_rows:
        raise RuntimeError("evidence tuple projection is incomplete")
    external_rows = sum(
        row["source"]["ref_slug"] != LOCAL_SOURCE_SLUG
        for row in evidence_rows
    )
    if external_rows != EXPECTED_EXTERNAL_EVIDENCE_ROWS:
        raise RuntimeError(
            f"external evidence-row count {external_rows}, expected "
            f"{EXPECTED_EXTERNAL_EVIDENCE_ROWS}"
        )
    for row in evidence_rows:
        slug = row["source"]["ref_slug"]
        evidence_rows_module.validate(row, source_map[slug])
        if row["excerpt"]["state"] not in {
            "verified_exact_match",
            "agent_extracted",
            "unconfirmed_anchor",
        }:
            raise RuntimeError(f"{row['row_id']}: row is not source-bound")
    bundle_sha = sha256(BUNDLE.read_bytes())
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    if bundle["final_draft"]["sha256"] != EXPECTED_DRAFT_SHA256:
        raise RuntimeError("Revision-Evidence Bundle final draft binding is stale")
    drift = {
        "schema_version": "claim-strength-drift-findings/1.0",
        "status": "completed",
        "final_draft_sha256": EXPECTED_DRAFT_SHA256,
        "revision_evidence_bundle_sha256": bundle_sha,
        "detection_provenance": {
            "kind": "model_mediated_semantic_review",
            "detector_id": (
                "codex-session-model/p25-stage4.5-e6-independent-20260830"
            ),
            "protocol_sha256": sha256(CLAIM_PROTOCOL.read_bytes()),
        },
        "findings": [],
    }
    drift_schema = json.loads(DRIFT_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(drift_schema).validate(drift)
    drift_raw = json_bytes(drift)

    token_report = json.loads(TOKEN_REPORT.read_text(encoding="utf-8"))
    if token_report.get("conserved") is not False:
        raise RuntimeError("expected semantic token advisories are absent")
    if len(token_report.get("advisory_rows", [])) != 4:
        raise RuntimeError("token advisory population changed")

    adjudication_text = coverage_adjudication(
        registry_raw=registry_raw,
        coverage_raw=coverage_raw,
        coverage=coverage,
        evidence_rows=evidence_rows,
        source_map_raw=source_map_raw,
    )
    e6_text = e6_audit(
        bundle_sha=bundle_sha,
        drift_raw=drift_raw,
        token_report=token_report,
    )

    # The six deterministic Stage-4.5 sidecars are rebuilt.  The source-bound
    # evidence-row file is deliberately replay-validated but not rewritten.
    write_bytes(REGISTRY_PATH, registry_raw)
    write_bytes(COVERAGE_PATH, coverage_raw)
    write_bytes(
        COVERAGE_ADJUDICATION_PATH, adjudication_text.encode("utf-8")
    )
    write_bytes(SOURCE_MAP_PATH, source_map_raw)
    write_bytes(DRIFT_PATH, drift_raw)
    write_bytes(E6_AUDIT_PATH, e6_text.encode("utf-8"))

    summary = {
        "draft_sha256": EXPECTED_DRAFT_SHA256,
        "block_count": len(blocks),
        "claim_count": len(claims),
        "selection_tier_ALL": len(claims),
        "mechanical_candidate_count": len(coverage["candidates"]),
        "candidate_unregistered_count": coverage[
            "candidate_unregistered_count"
        ],
        "evidence_row_count": len(evidence_rows),
        "external_audit_carrier_rows": external_rows,
        "local_artifact_chain_rows": len(evidence_rows) - external_rows,
        "source_bound_rows": len(evidence_rows),
        "anchorless_rows": 0,
        "e6_findings": 0,
        "outputs": {
            str(path.relative_to(ROOT)): sha256(path.read_bytes())
            for path in (
                REGISTRY_PATH,
                COVERAGE_PATH,
                COVERAGE_ADJUDICATION_PATH,
                EVIDENCE_PATH,
                SOURCE_MAP_PATH,
                DRIFT_PATH,
                E6_AUDIT_PATH,
            )
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
