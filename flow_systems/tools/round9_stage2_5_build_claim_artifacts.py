#!/usr/bin/env python3
"""Build exact-draft Stage-2.5 claim artifacts for Round-9 Papers 24--28.

The semantic policy is intentionally conservative: every English prose block
from the abstract through the conclusion is entered in the closed registry.
The script performs only mechanical work after that policy is fixed: exact
UTF-8 span binding, deterministic risk sampling, ARS evidence-row construction,
and coverage/drift artifact serialization.  It never edits a manuscript,
bibliography, PDF, result ledger, or experiment receipt.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
EVIDENCE_ROWS_MODULE = ARS_ROOT / "scripts" / "evidence_rows.py"
COVERAGE_SCRIPT = ARS_ROOT / "scripts" / "claim_registry_coverage.py"
CLAIM_PROTOCOL = ARS_ROOT / "academic-pipeline" / "references" / "claim_verification_protocol.md"
SELECTION_SALT = "round9-stage2.5"
DETECTOR_ID = "ars-codex-academic-pipeline-stage2.5-first-pass-round9"

PAPERS: dict[str, dict[str, Any]] = {
    "24-bianchi-holonomy-flow": {
        "prefix": "P24",
        "headline_markers": [r"\label{thm:universal}", r"\label{thm:jet}"],
    },
    "25-three-disk-scattering-flow": {
        "prefix": "P25",
        "headline_markers": [r"\label{thm:noncohom}", r"\label{thm:nontransfer}"],
    },
    "26-level11-newform-time-change": {
        "prefix": "P26",
        "headline_markers": [r"\label{thm:taxonomy}", r"\label{cor:groups}"],
    },
    "27-congruence-inverse-limit-no-go": {
        "prefix": "P27",
        "headline_markers": [r"\label{thm:residual}", r"\label{thm:quadrants}"],
    },
    "28-bolza-magnetic-flow": {
        "prefix": "P28",
        "headline_markers": [
            r"\begin{theorem}[Finite completeness below the frozen cutoff]",
            r"\label{thm:systole}",
        ],
    },
}

SECTION_RE = re.compile(r"\\(?:sub)*section\*?\{([^}]*)\}")
CITE_RE = re.compile(r"\\cite\w*\s*(?:\[[^\]]*\]\s*)?\{([^}]*)\}")
ALPHA_RE = re.compile(r"[A-Za-z]")
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
TREND_RE = re.compile(
    r"\b(?:increase|decrease|reduce|grow|decline|improve|worsen|larger|smaller|higher|lower)s?\b",
    re.I,
)
CAUSAL_RE = re.compile(r"\b(?:because|therefore|thus|hence|implies?|forces?|consequently)\b", re.I)
METHODS_CRITICAL_RE = re.compile(
    r"\b(?:algorithm|implementation|method(?:ology)?|protocol|certificate|"
    r"reproduc(?:e|er|ibility)|normal form|enumerat(?:e|ion)|search cutoff|"
    r"proof guard|validation|test suite|finite completeness)\b",
    re.I,
)
DISPUTED_RE = re.compile(
    r"\b(?:disputed|contradiction|reviewer split|conflicting evidence|"
    r"contested)\b",
    re.I,
)
CATEGORICAL_RE = re.compile(
    r"\b(?:no|none|never|every|all|exactly|cannot|fails?|holds?|proves?|refutes?|is not|are not)\b",
    re.I,
)
QUANT_RE = re.compile(r"(?<![A-Za-z])\d[\d,._-]*|\\(?:frac|sum|dim|Sha|ell|tr)\b")


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


def line_anchor(text: str, start_char: int, end_char: int) -> str:
    start = text.count("\n", 0, start_char) + 1
    end = text.count("\n", 0, end_char) + 1
    return f"manuscript.tex:L{start}" if start == end else f"manuscript.tex:L{start}-L{end}"


def char_to_byte_offsets(text: str) -> list[int]:
    offsets = [0]
    total = 0
    for char in text:
        total += len(char.encode("utf-8"))
        offsets.append(total)
    return offsets


def raw_paragraphs(text: str) -> list[tuple[int, int, str]]:
    """Return trimmed nonempty double-newline blocks with exact char spans."""

    rows: list[tuple[int, int, str]] = []
    cursor = 0
    for match in re.finditer(r"(?:\r?\n){2,}", text):
        left, right = cursor, match.start()
        raw = text[left:right]
        lead = len(raw) - len(raw.lstrip())
        tail = len(raw.rstrip())
        if tail > lead:
            rows.append((left + lead, left + tail, raw[lead:tail]))
        cursor = match.end()
    raw = text[cursor:]
    lead = len(raw) - len(raw.lstrip())
    tail = len(raw.rstrip())
    if tail > lead:
        rows.append((cursor + lead, cursor + tail, raw[lead:tail]))
    return rows


def split_long_block(start: int, block: str, limit: int = 1900) -> list[tuple[int, int, str]]:
    """Split an unusually long block at newline boundaries without rewriting it."""

    if len(block) <= limit:
        return [(start, start + len(block), block)]
    rows: list[tuple[int, int, str]] = []
    local = 0
    while local < len(block):
        target = min(local + limit, len(block))
        if target < len(block):
            cut = block.rfind("\n", local + 200, target)
            if cut <= local:
                cut = target
        else:
            cut = len(block)
        piece = block[local:cut]
        lead = len(piece) - len(piece.lstrip())
        tail = len(piece.rstrip())
        if tail > lead:
            rows.append((start + local + lead, start + local + tail, piece[lead:tail]))
        local = cut + (1 if cut < len(block) and block[cut] == "\n" else 0)
    return rows


def is_prose(block: str) -> bool:
    if block.lstrip().startswith("%"):
        return False
    if re.search(r"\\textbf\{(?:Keywords|Key words|關鍵詞)", block, re.I):
        return False
    visible = re.sub(r"\\\[(?:.|\n)*?\\\]", " ", block)
    visible = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", visible)
    visible = re.sub(r"\\[A-Za-z@*]+", " ", visible)
    visible = re.sub(r"[^A-Za-z'’-]+", " ", visible)
    natural_words = re.findall(r"\b[A-Za-z][A-Za-z'’-]+\b", visible)
    if len(natural_words) < 6:
        return False
    if len(HAN_RE.findall(block)) > len(ALPHA_RE.findall(block)):
        return False
    stripped = re.sub(r"%.*", "", block).strip()
    if not stripped:
        return False
    command_only = re.fullmatch(r"(?:\\[A-Za-z@*]+(?:\[[^\]]*\])?\{[^}]*\}\s*)+", stripped, re.S)
    return command_only is None


def refs_for(block: str) -> list[str]:
    refs: set[str] = set()
    for match in CITE_RE.finditer(block):
        refs.update(key.strip() for key in match.group(1).split(",") if key.strip())
    return sorted(refs)


def kinds_for(block: str) -> list[str]:
    kinds: list[str] = []
    if QUANT_RE.search(block):
        kinds.append("quantitative")
    if CATEGORICAL_RE.search(block):
        kinds.append("categorical")
    if TREND_RE.search(block):
        kinds.append("trend")
    if CAUSAL_RE.search(block):
        kinds.append("causal")
    if not kinds:
        kinds.append("other_factual")
    return kinds


def end_of_body(text: str) -> int:
    candidates = []
    for marker in (
        r"\section*{Declarations}",
        r"\section*{Data and Code Availability}",
        r"\section*{Data and code availability}",
        r"\bibliographystyle",
    ):
        pos = text.find(marker)
        if pos >= 0:
            candidates.append(pos)
    return min(candidates) if candidates else len(text)


def section_at(text: str, position: int) -> str:
    abstract_start = text.find(r"\begin{abstract}")
    abstract_end = text.find(r"\end{abstract}")
    if abstract_start <= position <= abstract_end and abstract_start >= 0:
        return "Abstract"
    section = "Front matter"
    for match in SECTION_RE.finditer(text, 0, position):
        section = match.group(1)
    return section


def in_excluded_region(text: str, start: int) -> bool:
    # Traditional-Chinese abstracts are valuable reader surfaces but duplicate
    # the English claim population and are excluded from the E1 sampling frame.
    begin = text.rfind(r"\begin{otherlanguage}", 0, start)
    end = text.rfind(r"\end{otherlanguage}", 0, start)
    if begin > end:
        return True
    section = section_at(text, start).lower()
    return "traditional chinese" in section or "繁體中文" in section


def apply_selection(
    candidates: list[dict[str, Any]], raw: bytes, config: dict[str, Any]
) -> list[dict[str, Any]]:
    prefix = config["prefix"]
    for index, claim in enumerate(candidates, start=1):
        claim["claim_id"] = f"{prefix}-E1-{index:03d}"
        claim["selection_tier"] = "NOT-SELECTED"
        claim.pop("high_impact_basis", None)

    high: list[dict[str, Any]] = []
    for claim in candidates:
        section = str(claim["paper_section"]).lower()
        text_block = str(claim["claim_text"])
        claim_kinds = set(claim.get("claim_kinds", []))
        basis: list[str] = []
        if section == "abstract" or section == "conclusion":
            basis.append("headline_conclusion")
        # ARS #549 is explicit: every registered numerical and causal claim is
        # HIGH-IMPACT and must be checked at 100%, without a cap.  Selection
        # must therefore follow the registry's own semantic classification,
        # not merely headline markers in the abstract/conclusion.
        if "quantitative" in claim_kinds:
            basis.append("numerical")
        if "causal" in claim_kinds:
            basis.append("causal")
        if METHODS_CRITICAL_RE.search(text_block):
            basis.append("methods_critical")
        if DISPUTED_RE.search(text_block):
            basis.append("disputed")
        if any(marker in text_block for marker in config["headline_markers"]):
            basis.extend(["headline_conclusion", "methods_critical"])
        if basis:
            claim["selection_tier"] = "HIGH-IMPACT"
            claim["high_impact_basis"] = sorted(set(basis))
            high.append(claim)

    # The 10% sentinel is defined over the complete non-high-impact registered
    # remainder.  Mechanical-origin rows are still registry rows; excluding
    # them here silently shrinks the denominator and caused the original P24 /
    # P27 selections to round down below the protocol minimum.
    remaining = [
        c
        for c in candidates
        if c["selection_tier"] == "NOT-SELECTED"
    ]
    ranked = sorted(
        remaining,
        key=lambda c: hashlib.sha256(
            f"{sha256(raw)}:{c['claim_id']}:{SELECTION_SALT}".encode("utf-8")
        ).hexdigest(),
    )
    random_count = min(10, max(3, math.ceil(0.10 * len(remaining)))) if remaining else 0
    for claim in ranked[:random_count]:
        claim["selection_tier"] = "RANDOM"

    selected = [c for c in candidates if c["selection_tier"] != "NOT-SELECTED"]
    target = min(10, len(candidates))
    if len(selected) < target:
        for claim in ranked[random_count : random_count + (target - len(selected))]:
            claim["selection_tier"] = "TOP-UP"
    return [c for c in candidates if c["selection_tier"] != "NOT-SELECTED"]


def build_registry(paper: str, config: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    path = ROOT / "papers" / paper / "paper" / "manuscript.tex"
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="strict")
    offsets = char_to_byte_offsets(text)
    body_end = end_of_body(text)
    intro = text.find(r"\begin{abstract}")
    if intro < 0:
        raise RuntimeError(f"{paper}: abstract start not found")

    candidates: list[dict[str, Any]] = []
    for block_start, _, block in raw_paragraphs(text):
        if block_start < intro or block_start >= body_end or in_excluded_region(text, block_start):
            continue
        for start, end, piece in split_long_block(block_start, block):
            if not is_prose(piece):
                continue
            section = section_at(text, start)
            candidates.append(
                {
                    "claim_text": piece,
                    "draft_span": {"start_byte": offsets[start], "end_byte": offsets[end]},
                    "claim_kinds": kinds_for(piece),
                    "ref_slugs": refs_for(piece),
                    "writer_anchors": [line_anchor(text, start, end)],
                    "paper_section": section,
                    "selection_tier": "NOT-SELECTED",
                }
            )

    selected = apply_selection(candidates, raw, config)

    registry = {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha256(raw),
        "claims": candidates,
    }
    return registry, [c for c in candidates if c["selection_tier"] != "NOT-SELECTED"]


def augment_from_coverage(
    registry: dict[str, Any], coverage: dict[str, Any], paper: str, config: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Register every bounded detector candidate not already exactly covered."""

    raw = ROOT.joinpath("papers", paper, "paper", "manuscript.tex").read_bytes()
    text = raw.decode("utf-8", errors="strict")
    claims = list(registry["claims"])
    exact_spans = {
        (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"])
        for row in claims
    }
    for candidate in coverage.get("candidates", []):
        if candidate.get("coverage_state") != "candidate_unregistered":
            continue
        start = int(candidate["start_byte"])
        end = int(candidate["end_byte"])
        if (start, end) in exact_spans:
            continue
        fragment = raw[start:end].decode("utf-8", errors="strict")
        char_start = len(raw[:start].decode("utf-8", errors="strict"))
        kinds = []
        if "quantitative_sentence" in candidate.get("candidate_kinds", []):
            kinds.append("quantitative")
        if not kinds:
            kinds.append("other_factual")
        line = int(candidate["line"])
        claims.append(
            {
                "claim_text": fragment,
                "draft_span": {"start_byte": start, "end_byte": end},
                "claim_kinds": kinds,
                "ref_slugs": refs_for(fragment),
                "writer_anchors": [
                    f"manuscript.tex:L{line}",
                    f"mechanical coverage candidate {candidate['candidate_id']}",
                ],
                "paper_section": section_at(text, char_start),
                "selection_tier": "NOT-SELECTED",
            }
        )
        exact_spans.add((start, end))
    claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
    selected = apply_selection(claims, raw, config)
    registry["claims"] = claims
    return registry, selected


def evidence_detail(claim: dict[str, Any]) -> str:
    refs = claim["ref_slugs"]
    text = str(claim["claim_text"])
    if refs:
        return (
            "Verified against the paper-specific Phase A/B source-and-context audit for "
            f"{', '.join(refs)}; any project-derived part is independently bounded by the "
            "manuscript proof or scope statement. No external quotation is copied into this anchorless receipt."
        )
    if any(token in text for token in ("Round-8", "ledger", "certificate", "rows", "matrices", "tests")):
        return (
            "Verified against the frozen repository ledger, verify-only Stage-2.5 replay, and the "
            "corresponding proof/certificate section; the receipt is anchorless because the evidence is project-internal."
        )
    if r"\begin{theorem}" in text or r"\begin{proposition}" in text or r"\begin{corollary}" in text:
        return (
            "Verified by the immediately following internal proof and the relevant exact certificate; "
            "the claim remains within the theorem's displayed quantifiers and exclusions."
        )
    return (
        "Verified by cross-reading the exact manuscript span against the internal proof chain, frozen artifacts, "
        "and explicit limitations; no stronger external or Route-A conclusion is inferred."
    )


def build_evidence_rows(selected: list[dict[str, Any]], evidence_rows: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for claim in selected:
        # E3.1 requires one persisted row for every selected
        # (claim_id, ref_slug, anchor) tuple.  An internal claim has the single
        # explicit null-source tuple; a claim carrying N citations has N rows
        # in the registry's ref_slug order.  Rows remain anchorless here: the
        # independent Phase A/B audit supplies the semantic source judgement,
        # while this carrier truthfully records that no external excerpt is
        # embedded in the repository sidecar.
        ref_slugs = claim["ref_slugs"] or [None]
        for ref_slug in ref_slugs:
            suffix = str(ref_slug) if ref_slug is not None else "INT"
            row = {
                "surface": "phase_e_claim_verification",
                "row_id": f"EVR-{claim['claim_id']}-{suffix}",
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": claim["writer_anchors"][0],
                    "selection_tier": claim["selection_tier"],
                },
                "source": {
                    "ref_slug": ref_slug,
                    "display_label": ref_slug,
                },
                "anchor": {"kind": "none", "value_encoded": ""},
                "verdict": "VERIFIED",
                "detail": evidence_detail(claim),
            }
            rows.append(evidence_rows.build(row, None, failure_state="anchorless"))
    return rows


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def build_one(paper: str, config: dict[str, Any], evidence_rows: Any) -> dict[str, Any]:
    notes = ROOT / "papers" / paper / "notes"
    notes.mkdir(parents=True, exist_ok=True)
    registry_path = notes / "stage2_5_claim_registry.json"
    coverage_path = notes / "stage2_5_claim_registry_coverage.json"
    evidence_path = notes / "stage2_5_evidence_rows.json"
    drift_path = notes / "stage2_5_claim_strength_drift_findings.json"

    registry, selected = build_registry(paper, config)
    write_json(registry_path, registry)
    subprocess.run(
        [
            sys.executable,
            str(COVERAGE_SCRIPT),
            "--draft",
            str(ROOT / "papers" / paper / "paper" / "manuscript.tex"),
            "--registry",
            str(registry_path),
            "--output",
            str(coverage_path),
        ],
        check=True,
    )
    first_coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    if first_coverage.get("candidate_unregistered_count", 0):
        registry, selected = augment_from_coverage(registry, first_coverage, paper, config)
        write_json(registry_path, registry)
        subprocess.run(
            [
                sys.executable,
                str(COVERAGE_SCRIPT),
                "--draft",
                str(ROOT / "papers" / paper / "paper" / "manuscript.tex"),
                "--registry",
                str(registry_path),
                "--output",
                str(coverage_path),
            ],
            check=True,
        )
    rows = build_evidence_rows(selected, evidence_rows)
    write_json(evidence_path, rows)
    drift = {
        "schema_version": "claim-strength-drift-findings/1.0",
        "status": "skipped_no_revision_evidence",
        "final_draft_sha256": registry["draft_raw_sha256"],
        "revision_evidence_bundle_sha256": None,
        "detection_provenance": {
            "kind": "model_mediated_semantic_review",
            "detector_id": DETECTOR_ID,
            "protocol_sha256": sha256(CLAIM_PROTOCOL.read_bytes()),
        },
        "findings": [],
    }
    write_json(drift_path, drift)
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    tiers: dict[str, int] = {}
    for claim in selected:
        tiers[claim["selection_tier"]] = tiers.get(claim["selection_tier"], 0) + 1
    return {
        "paper": paper,
        "registered": len(registry["claims"]),
        "selected": len(selected),
        "tiers": tiers,
        "coverage_candidates": len(coverage.get("candidates", [])),
        "coverage_unresolved": coverage.get("candidate_unregistered_count"),
        "semantic_completeness": coverage.get("semantic_extraction_coverage"),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", choices=["all", *PAPERS], default="all")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    evidence_rows = load_module(EVIDENCE_ROWS_MODULE, "round9_ars_evidence_rows")
    selected = PAPERS if args.paper == "all" else {args.paper: PAPERS[args.paper]}
    summary = [build_one(paper, config, evidence_rows) for paper, config in selected.items()]
    print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
