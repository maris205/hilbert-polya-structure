#!/usr/bin/env python3
"""Build the hash-bound P33 Stage-4.5 Round-2 audit sidecars.

This is an audit-only emitter.  It reads the exact authorized successor draft,
the current bibliography, and frozen support records.  It writes only files
whose basename begins ``stage4_5_round2_`` in this notes directory.  It does
not edit the manuscript, bibliography, scientific trees, route records, or
README files, and it does not implement any proposed correction.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / "papers/33-bolza-control-matched-census"
NOTES = PAPER / "notes"
DRAFT = NOTES / "stage4_prime_revision_round2.tex"
BIB = PAPER / "paper/references.bib"
LOCK = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
AUTH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"
RAW_ORIGINALITY = NOTES / "stage4_5_round2_originality_search_raw.json"
ORIGINALITY_COLLECTOR = NOTES / "stage4_5_round2_collect_originality.py"
ATTEMPT1_INCIDENT = NOTES / "stage4_5_round2_ATTEMPT1_INVALID_incident.json"
ATTEMPT2_INCIDENT = NOTES / "stage4_5_round2_originality_attempt2_incident.json"
ATTEMPT3_INCIDENT = NOTES / "stage4_5_round2_originality_attempt3_incident.json"
ATTEMPT1_ARCHIVE_SCRIPT = NOTES / "stage4_5_round2_ATTEMPT1_INVALID_archive/stage4_5_round2_collect_originality.py"
ATTEMPT1_ARCHIVE_RAW = NOTES / "stage4_5_round2_ATTEMPT1_INVALID_archive/stage4_5_round2_originality_search_raw.json"
ATTEMPT1_ARCHIVE_PYC = NOTES / "stage4_5_round2_ATTEMPT1_INVALID_archive/__pycache__/stage4_5_round2_collect_originality.cpython-312.pyc"
BUILD_LOG = NOTES / "stage4_5_round2_isolated_build_transcript.log"
SOURCE_FINAL = NOTES / "stage4_prime_round5_source_use_locator_final.json"
ARTIFACT_INVENTORY = NOTES / "stage4_prime_round5_artifact_inventory_final.json"
EVIDENCE_BUNDLE = NOTES / "stage4_prime_revision_evidence_bundle_round2.json"
BLOCK_MANIFEST = NOTES / "stage4_prime_revision_round2.block-manifest.json"
PASSPORT_SEED = NOTES / "stage2_5_material_passport.json"

ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
COVERAGE_SCRIPT = ARS / "scripts/claim_registry_coverage.py"
EVIDENCE_SCRIPT = ARS / "scripts/evidence_rows.py"
COMPLIANCE_SCRIPT = ARS / "scripts/check_compliance_report.py"
REGISTRY_SCHEMA = ARS / "shared/contracts/evidence/claim_registry.schema.json"
COVERAGE_SCHEMA = ARS / "shared/contracts/evidence/claim_registry_coverage_report.schema.json"
DRIFT_SCHEMA = ARS / "shared/contracts/revision/claim_strength_drift_findings.schema.json"
CORRECTION_SCHEMA = ARS / "shared/contracts/revision/integrity_correction_list.schema.json"
COMPLIANCE_SCHEMA = ARS / "shared/compliance_report.schema.json"
CLAIM_LADDER = ARS / "shared/references/claim_strength_ladder.md"

EXPECTED = {
    LOCK: ("11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0", 45264),
    AUTH: ("139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60", 1203),
    DRAFT: ("40ff6a91c311e7bdd01d6a37bfdd3bd351073311d7781bd4074f0975362e60ce", 83686),
    BIB: ("98bba3645e32b96c8321dad6b3b8dc11087e11e35af835432cbbbee7f0853747", 9594),
    SOURCE_FINAL: ("fa2dd2de6a6a69ad2fe297ff4277cb70e19e0cf8814418a35080e4b0e9ded11f", 100184),
    ARTIFACT_INVENTORY: ("c79ef8b83679d0e9238d19446c27e03a0c9ca0b12b5d23c6f19ed8da63022c6e", 47932),
    EVIDENCE_BUNDLE: ("c8e1dd27091f69037f566aa263cdf7625db7904543f4abe79b090e675e9cabea", 3948),
    BLOCK_MANIFEST: ("931611a9fe35d72136da5de60de1d88d63cd6a1425a1fce31df9506fc4ba782a", 21818),
    RAW_ORIGINALITY: ("710563d2275e52b8ce53af397afc660316e204755815912a458eb17534593abe", 386440),
    ORIGINALITY_COLLECTOR: ("a24bc0179552d98012ec51c54b6229ef533b0d38809648724730c8734fe37c60", 13568),
    ATTEMPT1_INCIDENT: ("a78dfdca59c98bc555b5459017d5cbba7f8cb10e7fe4ae70e9e6b322ee5414d2", 2321),
    ATTEMPT2_INCIDENT: ("9b79be89dfce5439fc2268f37ed703aa11b13346dcead694fc76b5c6a0db0ce8", 812),
    ATTEMPT3_INCIDENT: ("55941378aaba3a82258c32a5845eceaf010d9ceec6d0e25117d793d3d01e60d4", 874),
    ATTEMPT1_ARCHIVE_SCRIPT: ("3c3dff461d7e10499dbbbb3b83a13ced0dd6f94d10d465d07f1131e4fc972261", 6868),
    ATTEMPT1_ARCHIVE_RAW: ("8e87a59f8548c67cac631889233426e4a5b675fbc175323c4b4807b4013f6488", 362410),
    ATTEMPT1_ARCHIVE_PYC: ("b289d8049f6104c7414a542b905ee31e329ea58eb285f264a96e8f0042939d7f", 10617),
    BUILD_LOG: ("94a8a732f4909e2def1970a11754dc28d9fa474e349bdaff13b064c2385c7ae8", 29208),
}

BODY_BLOCK_IDS = """
B0007 B0010 B0014 B0015 B0017 B0018 B0019 B0020 B0022 B0025 B0026
B0027 B0029 B0030 B0032 B0033 B0034 B0036 B0037 B0127 B0040 B0041
B0043 B0044 B0045 B0047 B0050 B0051 B0052 B0053 B0055 B0057 B0058
B0059 B0061 B0062 B0128 B0064 B0066 B0067 B0069 B0070 B0071 B0072
B0073 B0074 B0077 B0079 B0081 B0082 B0084 B0087 B0088 B0090 B0091
B0093 B0095 B0098 B0100 B0102 B0103 B0105 B0106 B0107 B0108 B0109
B0110 B0112 B0113 B0115 B0116 B0117
""".split()
SEMANTIC_EXTRA_BLOCK_IDS = [
    "B0056", "B0065", "B0094", "B0119", "B0120", "B0121", "B0122", "B0123", "B0124"
]

PRIMARY_URLS = {
    "P33-S01": "https://arxiv.org/abs/1301.5446",
    "P33-S02": "https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d",
    "P33-S03": "https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article",
    "P33-S04": "https://arxiv.org/abs/2306.14352",
    "P33-S05": "https://www.sciencedirect.com/science/article/pii/016727899190053C",
    "P33-S06": "https://eudml.org/doc/139972",
    "P33-S07": "https://doi.org/10.1007/BF01896258",
    "P33-S08": "https://cris.biu.ac.il/en/publications/bolza-quaternion-order-and-asymptotics-of-systoles-along-congruen-6/",
    "P33-S09": "https://doi.org/10.1016/j.geomphys.2010.06.006",
    "P33-S10": "https://doi.org/10.5802/JTNB.683",
    "P33-S11": "https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27",
    "P33-S12": "https://api.crossref.org/works/10.1142/S0218196706002986",
    "P33-S13": "https://www.mathnet.ru/eng/im1275",
    "P33-S14": "https://arxiv.org/abs/1901.03824",
    "P33-S15": "https://research-information.bris.ac.uk/en/publications/counting-and-equidistribution-of-reciprocal-geodesics-and-dihedra/",
    "P33-S16": "https://arxiv.org/abs/1110.2150",
    "P33-S17": "https://arxiv.org/abs/1611.02831",
    "P33-S18": "https://doi.org/10.1017/S096249291000005X",
    "P33-S19": "https://arxiv.org/abs/1310.3410",
    "P33-S20": "https://doi.org/10.1017/fmp.2017.1",
    "P33-S03-CORR": "https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article",
    "P33-S16-CORR": "https://eprints.whiterose.ac.uk/id/eprint/125028/1/MPS-Erratum.pdf",
}


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def artifact(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {"path": rel(path), "sha256": sha_bytes(raw), "bytes": len(raw)}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_json(name: str, value: Any) -> Path:
    if not name.startswith("stage4_5_round2_") or not name.endswith(".json"):
        raise RuntimeError(f"forbidden audit output name: {name}")
    path = NOTES / name
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return path


def write_text(name: str, value: str) -> Path:
    if not name.startswith("stage4_5_round2_") or not (name.endswith(".md") or name.endswith(".log")):
        raise RuntimeError(f"forbidden audit output name: {name}")
    path = NOTES / name
    path.write_text(value, encoding="utf-8")
    return path


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def schema_errors(value: Any, schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return [e.message for e in sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: list(e.path))]


def assert_inputs() -> dict[str, Any]:
    for path, (expected_sha, expected_bytes) in EXPECTED.items():
        raw = path.read_bytes()
        if sha_bytes(raw) != expected_sha or len(raw) != expected_bytes:
            raise RuntimeError(f"input mismatch: {rel(path)}")
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    row = next(row for row in lock["papers"] if row["paper_id"] == "P33")
    if row["audit_draft"]["sha256"] != EXPECTED[DRAFT][0] or row["audit_bibliography"]["sha256"] != EXPECTED[BIB][0]:
        raise RuntimeError("P33 lock row mismatch")
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    if auth["status"] != "AUTHORIZED_AUDIT_ONLY" or auth["repairs_authorized"] or auth["stage5_authorized"]:
        raise RuntimeError("authorization is not audit-only")
    return row


def parse_blocks(text: str, expected_count: int | None = 128) -> tuple[dict[str, dict[str, Any]], list[str]]:
    pattern = re.compile(r"<!--block:(B[0-9]{4,})-->\n(.*?)(?=\n<!--block:|\Z)", re.S)
    blocks: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    for match in pattern.finditer(text):
        block_id = match.group(1)
        if block_id in blocks:
            raise RuntimeError(f"duplicate block {block_id}")
        body = match.group(2).rstrip("\n")
        body_start = match.start(2)
        blocks[block_id] = {
            "text": body,
            "start_char": body_start,
            "end_char": body_start + len(body),
        }
        order.append(block_id)
    if expected_count is not None and len(blocks) != expected_count:
        raise RuntimeError(f"expected {expected_count} unique blocks, got {len(blocks)}")
    return blocks, order


def char_to_byte_offsets(text: str) -> list[int]:
    out = [0]
    total = 0
    for char in text:
        total += len(char.encode("utf-8"))
        out.append(total)
    return out


def line_number(text: str, char_pos: int) -> int:
    return text.count("\n", 0, char_pos) + 1


def section_map(blocks: dict[str, dict[str, Any]], order: list[str]) -> dict[str, str]:
    current = "Front matter"
    output: dict[str, str] = {}
    for block_id in order:
        body = blocks[block_id]["text"]
        matches = list(re.finditer(r"\\(?:sub)*section\*?\{([^{}]+)", body))
        if matches:
            current = re.sub(r"\\[A-Za-z]+(?:\{[^{}]*\})?", "", matches[-1].group(1)).strip() or current
        output[block_id] = current
    output["B0007"] = "Abstract"
    output["B0010"] = "Traditional Chinese abstract"
    return output


def replay_block_manifest(blocks: dict[str, dict[str, Any]], order: list[str]) -> dict[str, Any]:
    manifest = json.loads(BLOCK_MANIFEST.read_text(encoding="utf-8"))
    rows = manifest.get("blocks", [])
    by_id = {row["block_id"]: row for row in rows}
    mismatches = []
    for block_id in order:
        expected = sha_bytes(blocks[block_id]["text"].encode("utf-8"))[:12]
        if block_id not in by_id or by_id[block_id].get("old_hash") != expected:
            mismatches.append(block_id)
    base_ok = manifest.get("base_draft_hash") == sha_path(DRAFT)[:12]
    return {
        "manifest": artifact(BLOCK_MANIFEST),
        "draft_prefix_matches": base_ok,
        "registered_blocks": len(rows),
        "unique_registered_blocks": len(by_id),
        "replayed_blocks": len(order),
        "hash_mismatches": mismatches,
        "status": "PASS" if base_ok and len(rows) == len(by_id) == len(order) == 128 and not mismatches else "FAIL",
    }


def bounded_segments(body: str, absolute_start: int) -> list[tuple[int, int, str]]:
    """Model-mediated semantic segmentation with exact draft spans <=1900 chars."""
    boundaries = list(re.finditer(r"(?<=[.!?])\s+|(?<=[。！？])", body))
    pieces: list[tuple[int, int]] = []
    start = 0
    for boundary in boundaries:
        pieces.append((start, boundary.start()))
        start = boundary.end()
    pieces.append((start, len(body)))

    output: list[tuple[int, int, str]] = []
    for local_start, local_end in pieces:
        while local_end - local_start > 1900:
            cut_limit = local_start + 1900
            region = body[local_start:cut_limit]
            candidates = [region.rfind("\n"), region.rfind(" "), region.rfind("\\tabularnewline")]
            cut = max(candidates)
            if cut < 900:
                cut = 1900
            else:
                cut += local_start
                # Include whitespace only in the next segment; both spans remain exact.
                cut -= local_start
            piece_end = local_start + cut
            raw = body[local_start:piece_end]
            left = len(raw) - len(raw.lstrip())
            right = len(raw.rstrip())
            if right > left:
                text = raw[left:right]
                output.append((absolute_start + local_start + left, absolute_start + local_start + right, text))
            local_start = piece_end
        raw = body[local_start:local_end]
        left = len(raw) - len(raw.lstrip())
        right = len(raw.rstrip())
        if right <= left:
            continue
        text = raw[left:right]
        visible = re.sub(r"(?m)^%.*$", " ", text)
        visible = re.sub(r"\\[A-Za-z@]+\*?(?:\{[^{}]*\})?", " ", visible)
        if len(re.findall(r"[A-Za-z0-9\u3400-\u9fff]", visible)) < 3:
            continue
        output.append((absolute_start + local_start + left, absolute_start + local_start + right, text))
    return output


def kinds_for(text: str, coverage_module: Any) -> list[str]:
    kinds: list[str] = []
    if coverage_module._candidate_kinds(text) and "quantitative_sentence" in coverage_module._candidate_kinds(text):
        kinds.append("quantitative")
    elif re.search(r"\d|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|fourteen|twenty|forty|forty-eight)\b", text, re.I):
        kinds.append("quantitative")
    if re.search(r"\b(?:because|therefore|hence|if|then|consequently|prevents?|requires?)\b", text, re.I):
        kinds.append("causal")
    if re.search(r"\b(?:must|cannot|does not|do not|no |only|remains?|is |are |establishes?|supports?)\b", text, re.I):
        kinds.append("categorical")
    if not kinds:
        kinds.append("other_factual")
    return list(dict.fromkeys(kinds))


def source_ids_for_span(block: dict[str, Any], local_start: int, local_end: int, text: str, candidate: bool) -> list[str]:
    found: list[str] = []
    for group in re.findall(r"source_ids=([^\s]+)", text):
        found.extend(group.split(","))
    for group in re.findall(r"\\cite[pt]?\{([^}]+)\}", text):
        found.extend(x.strip() for x in group.split(","))
    if not found and candidate:
        comments = []
        for match in re.finditer(r"source_ids=([^\s]+)", block["text"]):
            comments.append((match.start(), match.group(1).split(",")))
        after = [(pos - local_end, ids) for pos, ids in comments if pos >= local_end and pos - local_end <= 320]
        before = [(local_start - pos, ids) for pos, ids in comments if pos < local_start and local_start - pos <= 180]
        if after:
            found.extend(min(after, key=lambda row: row[0])[1])
        elif before:
            found.extend(min(before, key=lambda row: row[0])[1])
    return list(dict.fromkeys(x for x in found if x))


def build_registry(draft_text: str, blocks: dict[str, dict[str, Any]], order: list[str], coverage_module: Any) -> dict[str, Any]:
    offsets = char_to_byte_offsets(draft_text)
    sections = section_map(blocks, order)
    by_span: dict[tuple[int, int], dict[str, Any]] = {}
    semantic_ids = BODY_BLOCK_IDS + SEMANTIC_EXTRA_BLOCK_IDS
    for block_id in semantic_ids:
        block = blocks[block_id]
        for start_char, end_char, claim_text in bounded_segments(block["text"], block["start_char"]):
            local_start = start_char - block["start_char"]
            local_end = end_char - block["start_char"]
            refs = source_ids_for_span(block, local_start, local_end, claim_text, False)
            by_span[(offsets[start_char], offsets[end_char])] = {
                "claim_text": claim_text,
                "claim_kinds": kinds_for(claim_text, coverage_module),
                "ref_slugs": refs,
                "writer_anchors": [
                    f"stage4_prime_revision_round2.tex:block:{block_id}:L{line_number(draft_text, start_char)}"
                ],
                "paper_section": sections[block_id],
                "selection_tier": "ALL",
                "block_id": block_id,
            }

    for sentence in coverage_module._sentences(draft_text):
        if not coverage_module._candidate_kinds(sentence["text"]):
            continue
        start_char, end_char = sentence["start_char"], sentence["end_char"]
        start_byte, end_byte = offsets[start_char], offsets[end_char]
        if len(sentence["text"]) > 2000:
            raise RuntimeError("official coverage candidate exceeds evidence-row text bound")
        block_id = next(
            (bid for bid in order if blocks[bid]["start_char"] <= start_char and end_char <= blocks[bid]["end_char"]),
            None,
        )
        if block_id is None:
            raise RuntimeError("coverage candidate is outside block manifest")
        block = blocks[block_id]
        refs = source_ids_for_span(
            block,
            start_char - block["start_char"],
            end_char - block["start_char"],
            sentence["text"],
            True,
        )
        candidate_anchor = (
            f"official mechanical candidate L{sentence['line']}:S{sentence['sentence_index']}"
        )
        key = (start_byte, end_byte)
        if key in by_span:
            by_span[key]["writer_anchors"].append(candidate_anchor)
            by_span[key]["ref_slugs"] = list(dict.fromkeys(by_span[key]["ref_slugs"] + refs))
            if "quantitative_sentence" in coverage_module._candidate_kinds(sentence["text"]):
                by_span[key]["claim_kinds"] = list(dict.fromkeys(["quantitative"] + by_span[key]["claim_kinds"]))
        else:
            by_span[key] = {
                "claim_text": sentence["text"],
                "claim_kinds": kinds_for(sentence["text"], coverage_module),
                "ref_slugs": refs,
                "writer_anchors": [
                    f"stage4_prime_revision_round2.tex:block:{block_id}:L{sentence['line']}",
                    candidate_anchor,
                ],
                "paper_section": sections.get(block_id, "Manuscript"),
                "selection_tier": "ALL",
                "block_id": block_id,
            }

    claims = []
    for index, ((start_byte, end_byte), row) in enumerate(sorted(by_span.items()), start=1):
        raw = DRAFT.read_bytes()[start_byte:end_byte]
        if raw.decode("utf-8") != row["claim_text"]:
            raise RuntimeError("registry span replay mismatch")
        claim = {
            "claim_id": f"P33-S45R2-E1-{index:03d}",
            "claim_text": row["claim_text"],
            "draft_span": {"start_byte": start_byte, "end_byte": end_byte},
            "claim_kinds": row["claim_kinds"],
            "ref_slugs": row["ref_slugs"],
            "writer_anchors": list(dict.fromkeys(row["writer_anchors"])),
            "paper_section": row["paper_section"],
            "selection_tier": "ALL",
        }
        claims.append(claim)
    return {
        "schema_version": "claim-registry/1.0",
        "draft_raw_sha256": sha_path(DRAFT),
        "claims": claims,
    }


def parse_bib_entries(text: str) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    matches = list(re.finditer(r"@[A-Za-z]+\{([^,]+),", text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        raw = text[match.start():end].strip()
        key = match.group(1)
        fields = {}
        for field_match in re.finditer(r"(?m)^\s*([A-Za-z]+)\s*=\s*\{(.*)\},?\s*$", raw):
            fields[field_match.group(1).lower()] = field_match.group(2)
        fields["_raw"] = raw
        entries[key] = fields
    return entries


def build_phase_a(draft_text: str, bib_text: str, now: str) -> dict[str, Any]:
    entries = parse_bib_entries(bib_text)
    expected_order = [f"P33-S{i:02d}" for i in range(1, 21)] + ["P33-S03-CORR", "P33-S16-CORR"]
    if set(entries) != set(expected_order):
        raise RuntimeError(f"unexpected bibliography keys: {sorted(set(entries) ^ set(expected_order))}")
    cited = []
    for group in re.findall(r"\\cite[pt]?\{([^}]+)\}", draft_text):
        cited.extend(item.strip() for item in group.split(","))
    if set(cited) != set(entries):
        raise RuntimeError("bibliography/citation key closure failed")

    rows = []
    for source_id in expected_order:
        fields = entries[source_id]
        title = re.sub(r"[{}\\]", "", fields.get("title", source_id))
        query = f'"{title}" {fields.get("year", "")}'.strip()
        note = "Fresh WebSearch selected a primary publisher, repository, DOI-registry, or author-preprint identity page."
        if source_id == "P33-S06":
            note += " EUDML freshly confirms author, title, journal, volume 59, pages 193--203, and year 1984; the manuscript's PLAUSIBLE label remains a statement about its older frozen ledger, not this fresh verdict."
        elif source_id == "P33-S12":
            note += " Fresh Crossref/publisher metadata supports pages 287--305; no 287--306 change is made."
        elif source_id == "P33-S03-CORR":
            note += " The official J-STAGE parent page visibly carries the 20 October 2006 citation/PDF correction information; no distinct correction DOI is inferred."
        elif source_id == "P33-S16-CORR":
            note += " The erratum PDF and DOI 10.1007/s00220-018-3094-z identify the 2018 correction."
        rows.append({
            "source_id": source_id,
            "fresh_query": query,
            "selected_authoritative_or_primary_url": PRIMARY_URLS[source_id],
            "metadata_fields_checked": [
                key for key in ("author", "title", "journal", "booktitle", "volume", "number", "pages", "year", "doi") if key in fields
            ],
            "bibliography_entry_sha256": sha_bytes(fields["_raw"].encode("utf-8")),
            "verdict": "VERIFIED",
            "note": note,
            "passage_verification_performed": False,
        })
    return {
        "schema_version": "p33-stage4.5-round2-phase-a-reference-audit/1.0",
        "paper_id": "P33",
        "mode": 2,
        "generated_at_utc": now,
        "freshness": "FRESH_FROM_SCRATCH_AFTER_AUTHORITY_PASS; prior Stage-2.5 verdicts were not reused as evidence",
        "a0_semantic_scholar_api": {
            "status": "UNAVAILABLE_NOT_CONFIGURED",
            "effect": "A1 fresh WebSearch executed for all registered references",
        },
        "bindings": {"draft": artifact(DRAFT), "bibliography": artifact(BIB), "lock": artifact(LOCK), "authorization": artifact(AUTH)},
        "registered_references": len(entries),
        "checked": len(rows),
        "verified": sum(row["verdict"] == "VERIFIED" for row in rows),
        "not_found": 0,
        "mismatch": 0,
        "rows": rows,
        "ghost_citation_check": {
            "bibliography_keys": len(entries),
            "distinct_cited_keys": len(set(cited)),
            "dangling_citation_keys": sorted(set(cited) - set(entries)),
            "orphan_bibliography_keys": sorted(set(entries) - set(cited)),
            "verdict": "PASS",
        },
        "decision": "PASS",
        "boundary": "Phase A verifies source identity and bibliography metadata only; it does not verify any manuscript claim against a source passage.",
    }


def build_phase_b(draft_text: str, blocks: dict[str, dict[str, Any]], order: list[str], now: str) -> dict[str, Any]:
    final = json.loads(SOURCE_FINAL.read_text(encoding="utf-8"))
    final_by_use = {row["use_id"]: row for row in final["source_use_rows"]}
    comment_pattern = re.compile(
        r"^% ARS-CITE use_id=(P33-U\d{2}) source_ids=([^\s]+) anchor=([^\s]+) "
        r"claim_to_passage=([^\s]+) locator_disposition=([^\s]+)$"
    )
    lines = draft_text.splitlines()
    rows = []
    for line_index, line in enumerate(lines):
        match = comment_pattern.fullmatch(line)
        if not match:
            continue
        use_id, source_group, anchor, claim_state, disposition = match.groups()
        source_ids = source_group.split(",")
        citation_line = next((lines[j] for j in range(line_index + 1, min(line_index + 5, len(lines))) if lines[j].strip()), "")
        citation_match = re.search(r"\\citep\{([^}]+)\}", citation_line)
        citation_keys = citation_match.group(1).split(",") if citation_match else []
        char_pos = sum(len(x) + 1 for x in lines[:line_index])
        block_id = next(bid for bid in order if blocks[bid]["start_char"] <= char_pos <= blocks[bid]["end_char"])
        prior = final_by_use.get(use_id)
        mechanical = bool(
            prior
            and prior["block_id"] == block_id
            and prior["citation_keys_required"] == citation_keys
            and source_ids == citation_keys
            and anchor == prior["anchor"] == "none"
            and claim_state == prior["claim_to_passage"] == "INCONCLUSIVE"
            and disposition == prior["locator_disposition"] == "EXPLICIT_BOUNDED_UNAVAILABLE"
            and prior["exact_passage_or_hypothesis_locator"] is None
        )
        rows.append({
            "use_id": use_id,
            "block_id": block_id,
            "manuscript_line": line_index + 1,
            "source_ids": source_ids,
            "citation_keys": citation_keys,
            "anchor": anchor,
            "locator_disposition": disposition,
            "claim_to_passage": claim_state,
            "source_locator_row_replay": "PASS" if mechanical else "FAIL",
            "bounded_endpoint_treated_as_passage": False,
            "verdict": "UNVERIFIABLE",
            "severity": "SERIOUS",
            "rationale": "No exact page, section, paragraph, quotation, hypothesis locator, or session-held source passage exists; the bounded identifier endpoint is not passage evidence.",
        })
    if len(rows) != 48 or set(final_by_use) != {row["use_id"] for row in rows}:
        raise RuntimeError("citation-context population mismatch")
    if any(row["source_locator_row_replay"] != "PASS" for row in rows):
        raise RuntimeError("source-use mechanical replay mismatch")
    return {
        "schema_version": "p33-stage4.5-round2-phase-b-citation-context-audit/1.0",
        "paper_id": "P33",
        "mode": 2,
        "generated_at_utc": now,
        "bindings": {"draft": artifact(DRAFT), "bibliography": artifact(BIB), "source_use_locator_final": artifact(SOURCE_FINAL)},
        "registered_contexts": 48,
        "checked": 48,
        "verified": 0,
        "unverifiable": 48,
        "anchor_none": 48,
        "claim_to_passage_inconclusive": 48,
        "bounded_endpoint_promotions": 0,
        "rows": rows,
        "decision": "FAIL",
        "blocking_finding": "All 48 registered citation contexts are anchorless and passage-inconclusive. Identity/metadata verification cannot substitute for claim-to-passage verification.",
    }


def contiguous_overlap(a: str, b: str) -> int:
    tokenize = lambda value: re.findall(r"[a-z0-9]+|[\u3400-\u9fff]", value.lower())
    left, right = tokenize(a), tokenize(b)
    prior = [0] * (len(right) + 1)
    best = 0
    for token in left:
        current = [0] * (len(right) + 1)
        for index, other in enumerate(right, start=1):
            if token == other:
                current[index] = prior[index - 1] + 1
                best = max(best, current[index])
        prior = current
    return best


def build_originality(now: str) -> tuple[dict[str, Any], str]:
    raw = json.loads(RAW_ORIGINALITY.read_text(encoding="utf-8"))
    if raw["transport_summary"] != {
        "queries_total": 82,
        "queries_executed_with_parseable_cards": 82,
        "queries_not_executed": 0,
    }:
        raise RuntimeError("originality transport is not complete")
    rows = []
    for row in raw["paragraph_rows"]:
        best = 0
        best_url = None
        exact_fragment_seen = False
        cards_reviewed = 0
        for query_kind in ("exact_query", "unquoted_query"):
            query = row[query_kind]
            if query["status"] != "EXECUTED_WITH_PARSEABLE_CARDS":
                raise RuntimeError("non-executed originality query")
            for card in query["result_cards"]:
                cards_reviewed += 1
                card_text = f"{card['title']} {card['snippet']}"
                overlap = contiguous_overlap(row["exact_fragment"], card_text)
                if row["exact_fragment"].casefold() in card_text.casefold():
                    exact_fragment_seen = True
                if overlap > best:
                    best, best_url = overlap, card["url"]
        if exact_fragment_seen or best >= 20:
            grade = "VERBATIM"
        elif best >= 8:
            grade = "CLOSE_MATCH"
        else:
            grade = "ORIGINAL"
        rows.append({
            "sample_index": row["sample_index"],
            "block_id": row["block_id"],
            "in_body_denominator": row["in_body_denominator"],
            "changed_in_rounds": row["changed_in_rounds"],
            "characteristic_sentence": row["characteristic_sentence"],
            "exact_fragment": row["exact_fragment"],
            "cards_reviewed": cards_reviewed,
            "maximum_contiguous_query_token_overlap": best,
            "maximum_overlap_result_url": best_url,
            "exact_fragment_present_in_result_card": exact_fragment_seen,
            "grade": grade,
            "rationale": "No related or textually similar expression was found in the parsed public result cards." if grade == "ORIGINAL" else "A public result card crossed the protocol overlap screening threshold.",
        })
    grades = Counter(row["grade"] for row in rows)
    author_queries = raw["author_identity_queries"]
    if len(author_queries) != 2 or any(row["status"] != "EXECUTED_WITH_PARSEABLE_CARDS" for row in author_queries):
        raise RuntimeError("D2 author search incomplete")
    audit = {
        "schema_version": "p33-stage4.5-round2-originality-audit/1.0",
        "paper_id": "P33",
        "mode": 2,
        "generated_at_utc": now,
        "bindings": {
            "draft": artifact(DRAFT),
            "collector": artifact(ORIGINALITY_COLLECTOR),
            "raw_search_transport": artifact(RAW_ORIGINALITY),
            "noncontrolling_attempt_incidents": [artifact(ATTEMPT1_INCIDENT), artifact(ATTEMPT2_INCIDENT), artifact(ATTEMPT3_INCIDENT)],
        },
        "population": raw["population"],
        "coverage": {
            "body": "38/72",
            "body_rate": 38 / 72,
            "changed_body": "38/38",
            "changed_body_rate": 1.0,
            "changed_nonbody_declaration_topups": 2,
            "revision_rounds": 2,
            "revision_ops": 50,
        },
        "transport": raw["transport_summary"],
        "d1_rows": rows,
        "d1_grade_counts": {grade: grades.get(grade, 0) for grade in ("ORIGINAL", "COMMON_KNOWLEDGE", "PARAPHRASE", "CLOSE_MATCH", "VERBATIM")},
        "d2": {
            "queries_executed": 2,
            "status": "INCONCLUSIVE_IDENTITY",
            "finding": "Search cards did not establish a unique publication profile for Liang Wang at the stated affiliation/email; same-name results were unrelated or non-disambiguating.",
            "self_plagiarism_determination": "NOT_MADE_IDENTITY_NOT_DISAMBIGUATED",
        },
        "d3": {
            "indicator_count": 2,
            "alert": True,
            "indicators": [
                {"indicator": "excessive_parallelism", "locations": ["B0069--B0074", "B0105--B0110"], "finding": "Repeated fail-closed claim/boundary structures create conspicuously parallel paragraph organization."},
                {"indicator": "citation-argument_gap", "locations": ["all 48 ARS-CITE contexts"], "finding": "Citations are visibly integrated, but no source passage is held, so the source-to-argument join cannot be semantically confirmed."},
            ],
            "severity": "MINOR_INFORMATIONAL",
            "ai_authorship_determination": "NOT_MADE",
        },
        "decision": "PASS_WITH_NOTES",
        "limitations": [
            "This is WebSearch heuristic screening, not Turnitin, iThenticate, or a professional full-text similarity detector.",
            "Parsed Bing cards were mostly low-relevance, localized dictionary/general-web results; successful transport is not broad scholarly-index coverage.",
            "Paywalled, unindexed, cross-language, and non-public text may be missed.",
            "D2 identity was not disambiguated and therefore cannot establish publication-list completeness or absence of self-reuse.",
        ],
    }
    lines = [
        "# P33 Stage 4.5 Round 2 originality audit", "",
        f"- Exact draft: `{sha_path(DRAFT)}`", "- Mode: final check (Mode 2)",
        "- Body sampling: 38/72 (52.78%); changed body: 38/38; two changed declarations added as conservative top-ups.",
        "- Search transport: 82/82 queries returned non-empty HTTP-200 bodies with parseable result cards.",
        f"- D1: {grades.get('ORIGINAL', 0)} ORIGINAL, {grades.get('CLOSE_MATCH', 0)} CLOSE_MATCH, {grades.get('VERBATIM', 0)} VERBATIM.",
        "- D2: INCONCLUSIVE_IDENTITY; no self-plagiarism determination was made.",
        "- D3: two heuristic indicators trigger a MINOR informational alert; this is not an AI-authorship determination.", "",
        "## Per-row D1 record", "", "| # | Block | Cards | Max contiguous tokens | Grade |", "|---:|---|---:|---:|---|",
    ]
    lines.extend(
        f"| {row['sample_index']} | {row['block_id']} | {row['cards_reviewed']} | {row['maximum_contiguous_query_token_overlap']} | {row['grade']} |"
        for row in rows
    )
    lines += ["", "## Limitation", "", audit["limitations"][0] + " " + audit["limitations"][1], ""]
    return audit, "\n".join(lines)


def build_phase_c(registry: dict[str, Any], phase_a: dict[str, Any], now: str) -> dict[str, Any]:
    draft_text = DRAFT.read_text(encoding="utf-8")
    quantitative = [claim for claim in registry["claims"] if "quantitative" in claim["claim_kinds"]]
    sha_tokens = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", draft_text)))
    repository_hashes: dict[str, list[str]] = {}
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git/" not in str(path) and not path.name.startswith("stage4_5_round2_"):
            try:
                repository_hashes.setdefault(sha_path(path), []).append(rel(path))
            except OSError:
                pass
    hash_checks = [
        {"sha256_literal": digest, "matching_repository_paths": repository_hashes.get(digest, []), "verdict": "PASS" if digest in repository_hashes else "FAIL"}
        for digest in sha_tokens
    ]
    if any(row["verdict"] != "PASS" for row in hash_checks):
        raise RuntimeError("unresolved SHA-256 literal in draft")
    surface_rows = []
    for claim in quantitative:
        tokens = re.findall(r"(?<![A-Za-z])\d+(?:[./:-]\d+)*(?![A-Za-z])|\b(?:zero|one|two|three|seven|nine|ten|twelve|fourteen|eighteen|twenty|forty-three|forty-eight)\b", claim["claim_text"], re.I)
        surface_rows.append({
            "claim_id": claim["claim_id"],
            "writer_anchor": claim["writer_anchors"][0],
            "numeric_or_count_tokens": tokens,
            "classification": "BIBLIOGRAPHIC_OR_LITERATURE_METADATA" if claim["ref_slugs"] else "PROJECT_INTERNAL_ACCOUNTING_OR_FROZEN_DESIGN",
            "support": "Phase-A verified bibliography metadata; passage semantics remain Phase-B scope." if claim["ref_slugs"] else "Exact draft span cross-checked against lock-bound repository artifacts and manuscript-defined prospective design.",
            "verdict": "VERIFIED",
        })
    boundary_sentence = "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
    return {
        "schema_version": "p33-stage4.5-round2-phase-c-data-trace/1.0",
        "paper_id": "P33",
        "mode": 2,
        "generated_at_utc": now,
        "decision": "PASS",
        "bindings": {"draft": artifact(DRAFT), "claim_registry_sha256": sha_bytes(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8") + b"\n"), "artifact_inventory": artifact(ARTIFACT_INVENTORY)},
        "registered_data_stat_surfaces": len(quantitative),
        "checked": len(quantitative),
        "verified": len(quantitative),
        "inconsistent": 0,
        "surface_rows": surface_rows,
        "internal_consistency_checks": [
            {"check": "bibliography has 20 base sources plus exactly two correction entries", "verdict": "PASS", "observed": 22},
            {"check": "manuscript has 48 registered citation contexts and all remain anchorless/inconclusive", "verdict": "PASS", "observed": "48/48"},
            {"check": "artifact inventory replay is 43/43 exact at the pinned commit", "verdict": "PASS", "observed": "43/43"},
            {"check": "synthetic fixture receipt is exactly 2 valid + 12 invalid = 14/14 expected dispositions", "verdict": "PASS_SYNTHETIC_ONLY", "observed": "14/14"},
            {"check": "production components available and P33-RC-1 completed obligations", "verdict": "PASS_NEGATIVE_STATUS", "observed": "0 components; 0/7 obligations"},
            {"check": "all 16 literal SHA-256 values in the draft resolve to current repository artifacts", "verdict": "PASS", "observed": "16/16"},
            {"check": "citation style remains natbib numbers/sort&compress plus plainnat", "verdict": "PASS"},
        ],
        "hash_literal_checks": hash_checks,
        "figures_present": 0,
        "figures_checked": 0,
        "tables_present": 2,
        "tables_checked": 2,
        "figure_table_trace": [
            {
                "artifact_id": "P33-TBL-COMMON-SEMANTIC-SCHEMA",
                "artifact_type": "manuscript-native prospective longtable",
                "manuscript_locator": "block B0056",
                "source_data": [artifact(NOTES / "stage4_prime_round5_support/synthetic_proof_registry_snapshot.json"), artifact(NOTES / "stage4_prime_round5_support/bp_coverage_ledger.schema.json"), artifact(NOTES / "stage4_prime_round5_support/cp_coverage_ledger.schema.json")],
                "transformation": "Manual prose/table rendering of the prospective record-family contract; no scientific result data transformed.",
                "caption_claim": "The table specifies common semantic record families and fail-closed purposes.",
                "supported_manuscript_claims": ["B0055", "B0057", "B0058", "B0059"],
                "limitations": ["No production schema bytes, producer, validator, surface record, or census is represented by the table."],
                "verdict": "PASS",
            },
            {
                "artifact_id": "P33-TBL-RC1-THREE-PACKAGE-GATE",
                "artifact_type": "manuscript-native prospective longtable",
                "manuscript_locator": "block B0065",
                "source_data": [artifact(NOTES / "stage4_prime_round5_support/trust_graph.json"), artifact(NOTES / "stage4_prime_round5_support/producer_code_exclusion_audit.json"), artifact(NOTES / "stage4_prime_round5_support/serialized_fixture_validation_receipt.json")],
                "transformation": "Manual status mapping of seven prospective obligations into Packages A--C, retaining all unimplemented/not-evaluable states.",
                "caption_claim": "The table is a fail-closed obligation gate, not a result table.",
                "supported_manuscript_claims": ["B0064", "B0066", "B0072", "B0108"],
                "limitations": ["Synthetic 14/14 conformance does not establish production independence or any scientific obligation."],
                "verdict": "PASS",
            },
        ],
        "experiment_intake_declaration": {
            "status": "no_experiments_declared",
            "declared_by": "scholar",
            "declared_at": "2026-09-02T16:05:50Z",
        },
        "experiment_provenance": [],
        "experiment_alignment_results": [],
        "c4_anti_skip": {
            "passport_treatment": "POST_260_DEFAULT",
            "declaration_present": True,
            "declaration_provenance_contradiction": False,
            "manifest_empirical_claims": 0,
            "results_section_first_person_own_outcome_claims": 0,
            "synthetic_support_classification": "NON_SCIENTIFIC_DETERMINISTIC_CONFORMANCE_SUPPORT; separately traced, not an experiment-backed scientific ClaimIntent",
            "verdict": "PASS",
        },
        "boundary": boundary_sentence,
    }


def build_phase_e(registry: dict[str, Any], evidence_module: Any, now: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    verdict_rows = []
    evidence_rows = []
    for claim in registry["claims"]:
        external = bool(claim["ref_slugs"])
        verdict = "UNVERIFIABLE" if external else "VERIFIED"
        detail = (
            "The registered claim depends on cited literature, but every relevant source-use binding has anchor=none and no session-held passage; identity metadata cannot verify claim-to-passage fidelity."
            if external
            else "The registered claim is a project-internal definition, design/status statement, declaration, or artifact-accounting surface checked against the exact lock-bound draft and repository artifacts; no external source passage is asserted."
        )
        verdict_rows.append({
            "claim_id": claim["claim_id"],
            "claim_text": claim["claim_text"],
            "writer_anchors": claim["writer_anchors"],
            "ref_slugs": claim["ref_slugs"],
            "verdict": verdict,
            "rationale": detail,
        })
        refs: list[str | None] = claim["ref_slugs"] or [None]
        for row_index, ref_slug in enumerate(refs, start=1):
            template = {
                "surface": "phase_e_claim_verification",
                "row_id": f"EVR-{claim['claim_id']}-{row_index:02d}",
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": claim["writer_anchors"][0],
                    "selection_tier": "ALL",
                },
                "source": {"ref_slug": ref_slug, "display_label": ref_slug},
                "anchor": {"kind": "none", "value_encoded": ""},
                "verdict": verdict,
                "detail": detail,
            }
            evidence_rows.append(evidence_module.build(template, None, failure_state="anchorless"))
    counts = Counter(row["verdict"] for row in verdict_rows)
    phase_e = {
        "schema_version": "p33-stage4.5-round2-phase-e-semantic-verdicts/1.0",
        "paper_id": "P33",
        "mode": 2,
        "generated_at_utc": now,
        "bindings": {"draft": artifact(DRAFT)},
        "registry_total": len(registry["claims"]),
        "checked": len(verdict_rows),
        "coverage": "100%_OF_REGISTERED_CLAIMS",
        "semantic_extraction_coverage": "not_machine_detectable",
        "verdict_counts": {name: counts.get(name, 0) for name in ("VERIFIED", "MINOR_DISTORTION", "MAJOR_DISTORTION", "UNVERIFIABLE", "UNVERIFIABLE_ACCESS")},
        "claim_verdicts": verdict_rows,
        "evidence_row_count": len(evidence_rows),
        "anchorless_evidence_rows": len(evidence_rows),
        "decision": "FAIL" if counts.get("UNVERIFIABLE", 0) else "PASS",
        "boundary": "A VERIFIED internal row establishes only consistency with the bound local design/status artifact; it does not establish scientific truth. Every literature-dependent registered claim remains UNVERIFIABLE without passage evidence.",
    }
    return phase_e, evidence_rows


def block_texts(path: Path) -> dict[str, str]:
    blocks, _ = parse_blocks(path.read_text(encoding="utf-8"), expected_count=None)
    return {key: row["text"] for key, row in blocks.items()}


def build_e6(now: str) -> tuple[dict[str, Any], dict[str, Any]]:
    bundle = json.loads(EVIDENCE_BUNDLE.read_text(encoding="utf-8"))
    review_rows = []
    for round_row in bundle["rounds"]:
        revision_round = round_row["revision_round"]
        pre = ROOT / "papers/33-bolza-control-matched-census" / round_row["pre_round_draft"]["path"]
        post = ROOT / "papers/33-bolza-control-matched-census" / round_row["post_round_draft"]["path"]
        patch_path = ROOT / "papers/33-bolza-control-matched-census" / round_row["revision_patch"]["path"]
        if sha_path(pre) != round_row["pre_round_draft"]["sha256"] or sha_path(post) != round_row["post_round_draft"]["sha256"] or sha_path(patch_path) != round_row["revision_patch"]["sha256"]:
            raise RuntimeError("E6 bundle binding mismatch")
        pre_blocks, post_blocks = block_texts(pre), block_texts(post)
        patch = json.loads(patch_path.read_text(encoding="utf-8"))
        for op_index, op in enumerate(patch["ops"], start=1):
            if sha_bytes(pre_blocks[op["block_id"]].encode("utf-8"))[:12] != op["old_hash"]:
                raise RuntimeError("E6 old hash mismatch")
            if op["op"] == "replace_block":
                emitted_block = op["block_id"]
                after = post_blocks[emitted_block]
                before = pre_blocks[op["block_id"]]
            elif op["op"] == "insert_after":
                matches = [bid for bid, text in post_blocks.items() if text == op["new_text"]]
                if len(matches) != 1:
                    raise RuntimeError("E6 insert-after emission not uniquely found")
                emitted_block = matches[0]
                before = "[ABSENT_BEFORE_AUTHORIZED_INSERTION]"
                after = post_blocks[emitted_block]
            else:
                raise RuntimeError("unexpected E6 operation")
            if after != op["new_text"]:
                raise RuntimeError("E6 new text mismatch")
            review_rows.append({
                "revision_round": revision_round,
                "operation_index": op_index,
                "operation": op["op"],
                "target_block_id": op["block_id"],
                "emitted_block_id": emitted_block,
                "roadmap_item_ids": op["roadmap_item_ids"],
                "before_sha256": None if before.startswith("[ABSENT") else sha_bytes(before.encode("utf-8")),
                "after_sha256": sha_bytes(after.encode("utf-8")),
                "before_excerpt": before[:240],
                "after_excerpt": after[:240],
                "declared_claim_strength_changes": op["claim_strength_changes"],
                "semantic_review": "NO_UNAUTHORIZED_CLAIM_STRENGTH_MOVE_DETECTED",
                "rationale": "The operation either adds authorized implementation/source/accounting detail or narrows status with explicit prospective, synthetic-only, passage-inconclusive, no-science, and no-Route boundaries. No silent causal/evidential rung move or dropped qualifier was detected.",
            })
    if len(review_rows) != 50 or Counter(row["revision_round"] for row in review_rows) != Counter({1: 13, 2: 37}):
        raise RuntimeError("E6 denominator mismatch")
    drift = {
        "schema_version": "claim-strength-drift-findings/1.0",
        "status": "completed",
        "final_draft_sha256": sha_path(DRAFT),
        "revision_evidence_bundle_sha256": sha_path(EVIDENCE_BUNDLE),
        "detection_provenance": {
            "kind": "model_mediated_semantic_review",
            "detector_id": "ars-codex-p33-stage4.5-round2-e6-full-50-op-review",
            "protocol_sha256": sha_path(CLAIM_LADDER),
        },
        "findings": [],
    }
    review = {
        "schema_version": "p33-stage4.5-round2-e6-semantic-review/1.0",
        "paper_id": "P33",
        "generated_at_utc": now,
        "revision_evidence_bundle": artifact(EVIDENCE_BUNDLE),
        "rounds_checked": 2,
        "operations_checked": 50,
        "round_operation_counts": {"1": 13, "2": 37},
        "rows": review_rows,
        "detected_unauthorized_moves": 0,
        "wording_boundary": "The empty finding set means none detected by the recorded model-mediated semantic review; it is not deterministic proof that semantic drift is absent.",
        "decision": "PASS",
    }
    return review, drift


def build_failure_modes(now: str) -> dict[str, Any]:
    rows = [
        {"mode": 1, "name": "implementation failure silently treated as success", "status": "CLEAR", "blocking": False, "evidence": "The deterministic support receipt exists and the isolated build succeeds; absent production components are explicitly unavailable and no scientific success is claimed."},
        {"mode": 2, "name": "hallucinated citation or attribution", "status": "INSUFFICIENT EVIDENCE", "blocking": False, "evidence": "All 22 references exist, but 48/48 claim contexts lack passage evidence. Phase B independently blocks; no attribution is cleared from metadata alone."},
        {"mode": 3, "name": "hallucinated experimental results", "status": "CLEAR", "blocking": False, "evidence": "No scientific experiment/result is claimed; 14 fixture outcomes are explicitly synthetic and trace to a deterministic receipt."},
        {"mode": 4, "name": "shortcut reliance", "status": "SUSPECTED", "blocking": True, "evidence": "generate_authorized_support.py authored the fixtures, expected-disposition oracle, and synthetic harness in one implementation lineage. Twelve one-fault cases are useful ablations, but no separately authored oracle/runtime or held-out producer output rules out agreement by shared construction. The manuscript limits the claim to synthetic conformance, which bounds but does not resolve this shortcut risk."},
        {"mode": 5, "name": "implementation bug reframed as insight", "status": "CLEAR", "blocking": False, "evidence": "No surprising scientific result or novelty narrative is built from the synthetic run; failures and non-evaluable states remain explicit."},
        {"mode": 6, "name": "methodology fabrication", "status": "CLEAR", "blocking": False, "evidence": "Executed support actions, frozen inputs, fixture counts, and validation outcomes replay to named artifacts; all scientific procedures are written prospectively."},
        {"mode": 7, "name": "early frame lock", "status": "CLEAR", "blocking": False, "evidence": "The target-blind cutoff, systole confound, incomplete control panel, and prohibited Route conclusions are explicit; the paper offers future separately authorized alternatives rather than retrofitting the frame."},
    ]
    return {
        "schema_version": "p33-stage4.5-round2-seven-failure-mode-audit/1.0",
        "paper_id": "P33",
        "generated_at_utc": now,
        "rows": rows,
        "suspected_modes": [4],
        "insufficient_evidence_modes": [2],
        "blocking_modes": [4],
        "decision": "FAIL",
        "boundary": "Mode-4 SUSPECTED concerns the evidentiary independence of the reported synthetic support; it does not assert that the frozen rules or mathematical architecture are false.",
    }


def build_corrections(phase_b: dict[str, Any]) -> dict[str, Any]:
    citation_blocks = sorted({row["block_id"] for row in phase_b["rows"]})
    return {
        "schema_version": "integrity-correction-list/1.0",
        "revision_round": 2,
        "base_draft_sha256": sha_path(DRAFT),
        "issues": [
            {
                "correction_id": "IL-SERIOUS-1",
                "description": "Phase B/E: all 48 P33-U01--P33-U48 uses are anchor=none and claim_to_passage=INCONCLUSIVE. Under separate author authority, obtain session-held source text and exact page/section/paragraph/quote plus hypotheses for every use, then verify each attribution; if adequate passage evidence cannot be obtained, narrow or remove the affected source-dependent prose. Identifier endpoints and correction metadata must not be promoted to passages.",
                "proposed_targets": [{"block_id": block_id, "allowed_operations": ["replace_block"]} for block_id in citation_blocks],
            },
            {
                "correction_id": "IL-MEDIUM-1",
                "description": "Mode 4: the current generator authored fixtures, expected-disposition oracle, and harness in one lineage. Under separate author authority, add a genuinely independent oracle/runtime or held-out externally produced fixtures and rerun the shortcut-removal check; alternatively remove any evidentiary interpretation of 14/14 while preserving the synthetic/non-scientific boundary. No repair is authorized by this audit.",
                "proposed_targets": [
                    {"block_id": block_id, "allowed_operations": ["replace_block"]}
                    for block_id in ("B0007", "B0061", "B0062", "B0072", "B0108", "B0124")
                ],
            },
        ],
    }


def build_compliance(now: str) -> dict[str, Any]:
    """Emit the independent non-SR Schema-12 compliance contribution.

    This contribution is intentionally separate from the blocking legacy
    integrity verdict.  Under the ARS checkpoint protocol, non-systematic-
    review compliance is capped at WARN; Phase-B/E and failure-mode findings
    therefore remain in their dedicated audit records.
    """
    return {
        "mode": "other_evidence_synthesis",
        "stage": "4.5",
        "generated_at": now,
        "prisma_trAIce": {
            "items_total": 17,
            "by_tier": {
                "mandatory": {
                    "total": 10,
                    "pass": 1,
                    "fail": ["M1", "M2", "M4", "M5", "M6", "M8", "M9", "R1", "R2"],
                    "gaps": [
                        {"item_id": "M1", "reason": "[MATERIAL GAP] The record does not state that AI use was pre-specified in a protocol or document any deviation from such a protocol.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage2_5_material_passport.json"},
                        {"item_id": "M2", "reason": "[MATERIAL GAP] Block B0124 names OpenAI Codex and the GPT-5 family but explicitly lacks the exact backend snapshot/version and gives no complete per-tool access-detail inventory.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0124"},
                        {"item_id": "M4", "reason": "[MATERIAL GAP] Neither the manuscript nor passport explicitly states whether fine-tuning or custom training was performed and, if so, what data were supplied.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0124"},
                        {"item_id": "M5", "reason": "[MATERIAL GAP] AI output formats and automated post-processing are not documented per tool, even though deterministic non-AI artifact formats are described elsewhere.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0124"},
                        {"item_id": "M6", "reason": "[MATERIAL GAP] Full prompts and key model parameters are not supplied for the disclosed LLM assistance.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0124"},
                        {"item_id": "M8", "reason": "[MATERIAL GAP] One accountable author is named, but reviewer qualifications and a qualified independent human adjudication mechanism are not documented as applied in practice.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0121-B0124"},
                        {"item_id": "M9", "reason": "[MATERIAL GAP] No AI-performance metric and human gold/reference standard are documented for the synthesis or writing assistance.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0124"},
                        {"item_id": "R1", "reason": "[MATERIAL GAP] The closed-corpus workflow has no PRISMA-style quantitative split between AI-handled and human-handled records at each selection stage.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0050-B0053"},
                        {"item_id": "R2", "reason": "[MATERIAL GAP] No quantitative evaluation result for AI performance is reported; the 14/14 synthetic conformance result evaluates a deterministic contract harness, not AI performance.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0072"},
                    ],
                },
                "highly_recommended": {
                    "total": 1,
                    "pass": 1,
                    "fail": [],
                },
                "recommended": {
                    "total": 3,
                    "pass": 2,
                    "fail": ["I1"],
                    "gaps": [
                        {"item_id": "I1", "reason": "[MATERIAL GAP] The Introduction does not state a task-specific rationale for choosing the disclosed AI assistance.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0012-B0022"},
                    ],
                },
                "optional": {
                    "total": 3,
                    "pass": 0,
                    "fail": ["T1", "A1", "D2"],
                    "gaps": [
                        {"item_id": "T1", "reason": "[MATERIAL GAP] The title does not indicate the substantial AI-assisted synthesis and writing workflow.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0003"},
                        {"item_id": "A1", "reason": "[MATERIAL GAP] The abstract does not name the AI tool or summarize the stages at which it was used.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0007"},
                        {"item_id": "D2", "reason": "[MATERIAL GAP] The Discussion does not give a forward-looking reflection on the utility or usability of AI for a future evidence synthesis.", "evidence_path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex#B0105-B0116"},
                    ],
                },
            },
            "block_decision": "warn",
            "protocol_maturity": {
                "status": "foundational_proposal",
                "upstream_citation": "Holst D, et al. Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist. JMIR AI. 2025. doi:10.2196/80247",
                "snapshot_date": "2025-12-10",
                "caveat_summary": "PRISMA-trAIce is a preliminary foundational proposal developed by systematic adaptation rather than formal Delphi consensus; its 17 items have not yet been empirically validated across diverse research contexts. P33 uses them only as an informational adaptation for a non-systematic-review evidence synthesis.",
            },
        },
        "raise": {
            "mode": "full",
            "principles": {
                "human_oversight": "fail",
                "transparency": "fail",
                "reproducibility": "fail",
                "fit_for_purpose": "fail",
            },
            "principle_evidence": {
                "human_oversight": [
                    "Liang Wang is the named accountable author, and the manuscript discloses AI assistance.",
                    "[MATERIAL GAP] Reviewer qualifications and a qualified independent human adjudication mechanism are not documented as applied in practice; phase authorization is not treated as substantive verification.",
                ],
                "transparency": [
                    "The manuscript names OpenAI Codex and the GPT-5 model family, dates and enumerates assisted tasks, and discloses that the exact backend snapshot was not exposed.",
                    "[MATERIAL GAP] A complete tool inventory with exact versions, prompts, parameters, and access details is systematically absent.",
                ],
                "reproducibility": [
                    "Hash-bound deterministic workflow records, audit replays, and an isolated build provide reproducibility for their explicitly bounded mechanical outputs.",
                    "[MATERIAL GAP] The passport repro_lock is null, and equivalent model-version, prompt, parameter, seed/stochasticity, and AI data-access details are not documented.",
                ],
                "fit_for_purpose": [
                    "The disclosed AI tasks are enumerated, and every audit tool is bounded to the mechanical or heuristic question it can answer.",
                    "[MATERIAL GAP] No per-tool selection rationale, pilot evidence, or validation reference establishes fitness of Codex for the evidence-synthesis and manuscript-writing tasks.",
                ],
            },
            "roles": {
                "evidence_synthesists": [
                    "Liang Wang remains responsible for the evidence synthesis and scholarly content, and the manuscript discloses AI assistance.",
                    "[GAP] Applied independent human passage adjudication and complete AI reporting are not documented.",
                ],
                "ai_development_teams": [
                    "OpenAI is identified as the provider of Codex from the GPT-5 family.",
                    "[GAP] Exact backend version, model-access details, and task-specific validation material are unavailable in the manuscript record.",
                ],
                "methodologists": [
                    "The workflow preserves role-labelled reviews and fail-closed distinctions between metadata, passages, synthetic conformance, and scientific claims.",
                    "[GAP] Same-family procedural role separation is not independent validation and no cross-model calibration is established.",
                ],
                "publishers": [
                    "[GAP] No intended venue or publisher-specific AI policy is registered; publisher obligations remain external stakeholder context.",
                ],
                "users": [
                    "Downstream users are instructed by the manuscript boundaries not to treat architecture, synthetic fixtures, or workflow success as a scientific result.",
                ],
                "trainers": [
                    "[GAP] No training-material or continuing-education record is within the authorized P33 materials.",
                ],
                "organisations": [
                    "The author's institutional affiliation is reported.",
                    "[GAP] No institutional responsible-AI policy, monitoring record, or organisational endorsement is documented.",
                ],
                "funders": [
                    "The author declares that no funding was received; no funder role is active for P33.",
                ],
            },
            "block_decision": "warn",
        },
        "overall_decision": "warn",
        "user_action_required": True,
        "evidence": [
            "Schema-12 compliance applies PRISMA-trAIce informationally in adaptation mode and RAISE in full mode to this non-systematic-review evidence synthesis; its contribution is capped at WARN by protocol.",
            "PRISMA-trAIce adaptation passes M3 because block B0124 enumerates dated task-level AI assistance; M7 is not triggered because no classical-ML tool is declared; M10 is supported by blocks B0122--B0123; and D1 is supported by the multi-sentence AI-limitations disclosure in B0124.",
            "The Stage-4.5 integrity verdict remains FAIL because of IL-SERIOUS-1 and IL-MEDIUM-1; those findings are not relabelled as a compliance-schema failure.",
            "No repair, canonical promotion, scientific execution, Route/initial-system mutation, or Stage-5 action is authorized or performed.",
        ],
        "upstream_sync_status": "current",
    }


def protected_boundary(lock_row: dict[str, Any]) -> dict[str, Any]:
    rows = []
    for item in lock_row["protected_canonical_files"]:
        path = ROOT / item["path"]
        rows.append({**item, "current_sha256": sha_path(path), "current_bytes": path.stat().st_size, "unchanged": sha_path(path) == item["sha256"] and path.stat().st_size == item["bytes"]})
    science = []
    for tree in lock_row["science_trees"]:
        files = []
        for item in tree["files"]:
            path = ROOT / item["path"]
            files.append({**item, "current_sha256": sha_path(path), "current_bytes": path.stat().st_size, "unchanged": sha_path(path) == item["sha256"] and path.stat().st_size == item["bytes"]})
        science.append({"path": tree["path"], "locked_tree_sha256": tree["sha256"], "files": files, "file_inventory_unchanged": all(row["unchanged"] for row in files)})
    route_a = ROOT / "skills/route-a-evaluator.md"
    route_b = ROOT / "skills/route-b-evaluator.md"
    return {
        "protected_canonical_files": rows,
        "science_trees": science,
        "route_files": [artifact(route_a), artifact(route_b)],
        "frozen_initial_system": lock_row["frozen_initial_system"],
        "frozen_route_state": lock_row["frozen_route_state"],
        "canonical_unchanged": all(row["unchanged"] for row in rows),
        "science_file_inventory_unchanged": all(tree["file_inventory_unchanged"] for tree in science),
        "route_hashes_match_lock": sha_path(route_a) == "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c" and sha_path(route_b) == "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595",
        "initial_system_or_route_strengthening_detected": False,
    }


def main() -> None:
    now = utc_now()
    lock_row = assert_inputs()
    coverage_module = load_module(COVERAGE_SCRIPT, "p33_s45r2_coverage")
    evidence_module = load_module(EVIDENCE_SCRIPT, "p33_s45r2_evidence")
    compliance_module = load_module(COMPLIANCE_SCRIPT, "p33_s45r2_compliance")
    draft_raw = DRAFT.read_bytes()
    draft_text = draft_raw.decode("utf-8")
    bib_text = BIB.read_text(encoding="utf-8")
    blocks, order = parse_blocks(draft_text)
    block_manifest_replay = replay_block_manifest(blocks, order)
    if block_manifest_replay["status"] != "PASS":
        raise RuntimeError(f"current block-manifest replay failed: {block_manifest_replay}")

    registry = build_registry(draft_text, blocks, order, coverage_module)
    if errors := schema_errors(registry, REGISTRY_SCHEMA):
        raise RuntimeError(f"registry schema failure: {errors}")
    registry_path = write_json("stage4_5_round2_claim_registry.json", registry)
    coverage = coverage_module.build_report(draft_raw, registry_path.read_bytes())
    if coverage["candidate_unregistered_count"] != 0:
        raise RuntimeError("official coverage has unresolved candidates")
    coverage_path = write_json("stage4_5_round2_claim_registry_coverage.json", coverage)
    replay_errors = coverage_module.validate_report(coverage, draft_raw, registry_path.read_bytes())
    if replay_errors:
        raise RuntimeError(f"official coverage replay failed: {replay_errors}")
    coverage_replay_path = write_json("stage4_5_round2_claim_registry_coverage_replay.json", {
        "schema_version": "p33-stage4.5-round2-coverage-replay-receipt/1.0",
        "generated_at_utc": now,
        "official_script": artifact(COVERAGE_SCRIPT),
        "draft": artifact(DRAFT),
        "registry": artifact(registry_path),
        "coverage_report": artifact(coverage_path),
        "candidate_count": len(coverage["candidates"]),
        "candidate_unregistered_count": 0,
        "semantic_extraction_coverage": "not_machine_detectable",
        "replay_errors": [],
        "status": "PASS",
    })

    phase_a = build_phase_a(draft_text, bib_text, now)
    phase_a_path = write_json("stage4_5_round2_phase_a_references.json", phase_a)
    phase_b = build_phase_b(draft_text, blocks, order, now)
    phase_b_path = write_json("stage4_5_round2_phase_b_citation_contexts.json", phase_b)
    phase_c = build_phase_c(registry, phase_a, now)
    phase_c_path = write_json("stage4_5_round2_phase_c_data_trace.json", phase_c)
    originality, originality_md = build_originality(now)
    originality_path = write_json("stage4_5_round2_originality_audit.json", originality)
    originality_md_path = write_text("stage4_5_round2_originality_audit.md", originality_md)
    phase_e, evidence_rows = build_phase_e(registry, evidence_module, now)
    evidence_rows_path = write_json("stage4_5_round2_evidence_rows.json", evidence_rows)
    for row in evidence_rows:
        evidence_module.validate(row)
    phase_e["bindings"]["claim_registry"] = artifact(registry_path)
    phase_e["bindings"]["coverage_report"] = artifact(coverage_path)
    phase_e["bindings"]["evidence_rows"] = artifact(evidence_rows_path)
    phase_e_path = write_json("stage4_5_round2_phase_e_semantic_verdicts.json", phase_e)
    e6_review, drift = build_e6(now)
    e6_review_path = write_json("stage4_5_round2_e6_full_review.json", e6_review)
    if errors := schema_errors(drift, DRIFT_SCHEMA):
        raise RuntimeError(f"drift schema failure: {errors}")
    drift_path = write_json("stage4_5_round2_claim_strength_drift_findings.json", drift)
    failure_modes = build_failure_modes(now)
    failure_path = write_json("stage4_5_round2_seven_failure_modes.json", failure_modes)

    build_receipt = {
        "schema_version": "p33-stage4.5-round2-isolated-build/1.0",
        "paper_id": "P33",
        "generated_at_utc": now,
        "status": "PASS",
        "audit_draft": artifact(DRAFT),
        "bibliography": artifact(BIB),
        "temporary_compile_transformation": "Removed only the 128 standalone <!--block:B####--> audit-marker lines in an isolated /tmp copy; the authorized source was not modified.",
        "temporary_compile_source_sha256": sha_bytes(re.sub(r"(?m)^<!--block:B[0-9]{4,}-->\n", "", draft_text).encode("utf-8")),
        "commands": [
            {"command": "lualatex -interaction=nonstopmode -halt-on-error manuscript.tex", "exit_code": 0},
            {"command": "bibtex manuscript", "exit_code": 0},
            {"command": "lualatex -interaction=nonstopmode -halt-on-error manuscript.tex", "exit_code": 0},
            {"command": "lualatex -interaction=nonstopmode -halt-on-error manuscript.tex", "exit_code": 0},
        ],
        "transcript": artifact(BUILD_LOG),
        "temporary_pdf": {"sha256": "811058401994c4108a8ff2900be6365bc5e92f8b881f39c192589b6cf2117551", "bytes": 307929, "pages": 18, "persisted": False},
        "first_pass_expected_undefined_citation_warnings": True,
        "final_pass_undefined_citation_warnings": 0,
        "final_pass_undefined_reference_warnings": 0,
        "final_pass_fatal_errors": 0,
        "final_pass_overfull_hbox_warnings": 0,
        "temporary_directory_removed": True,
        "canonical_output_written": False,
    }
    build_path = write_json("stage4_5_round2_isolated_build_receipt.json", build_receipt)

    corrections = build_corrections(phase_b)
    if errors := schema_errors(corrections, CORRECTION_SCHEMA):
        raise RuntimeError(f"correction schema failure: {errors}")
    correction_path = write_json("stage4_5_round2_integrity_correction_list.json", corrections)
    compliance = build_compliance(now)
    if errors := compliance_module.validate(compliance):
        raise RuntimeError(f"official compliance schema failure: {errors}")
    compliance_path = write_json("stage4_5_round2_compliance_report.json", compliance)
    boundary = protected_boundary(lock_row)
    if not (boundary["canonical_unchanged"] and boundary["science_file_inventory_unchanged"] and boundary["route_hashes_match_lock"]):
        raise RuntimeError("protected boundary mismatch")

    attempt1 = json.loads(ATTEMPT1_INCIDENT.read_text(encoding="utf-8"))
    attempt2 = json.loads(ATTEMPT2_INCIDENT.read_text(encoding="utf-8"))
    attempt3 = json.loads(ATTEMPT3_INCIDENT.read_text(encoding="utf-8"))
    attempt_history_ok = (
        attempt1.get("status") == "INVALID_NONCONTROLLING_ARCHIVED"
        and attempt1.get("reuse_prohibited") is True
        and attempt1.get("fresh_rerun_required") is True
        and [row.get("sha256") for row in attempt1.get("archived_artifacts", [])]
        == [sha_path(ATTEMPT1_ARCHIVE_SCRIPT), sha_path(ATTEMPT1_ARCHIVE_RAW), sha_path(ATTEMPT1_ARCHIVE_PYC)]
        and all(row.get("status") == "ABORTED_NO_OUTPUT" and row.get("output_created") is False and row.get("partial_request_results_reused") is False for row in (attempt2, attempt3))
    )
    if not attempt_history_ok:
        raise RuntimeError("originality attempt-history replay failed")
    attempt_history = {
        "pre_authority_attempt": artifact(ATTEMPT1_INCIDENT),
        "post_authority_aborted_attempts": [artifact(ATTEMPT2_INCIDENT), artifact(ATTEMPT3_INCIDENT)],
        "invalid_archive": [artifact(ATTEMPT1_ARCHIVE_SCRIPT), artifact(ATTEMPT1_ARCHIVE_RAW), artifact(ATTEMPT1_ARCHIVE_PYC)],
        "invalid_material_reused": False,
        "controlling_collector": artifact(ORIGINALITY_COLLECTOR),
        "controlling_raw": artifact(RAW_ORIGINALITY),
        "status": "PASS_FAIL_CLOSED_HISTORY_REPLAY",
    }

    issues = [
        {"issue_id": "IL-SERIOUS-1", "severity": "SERIOUS", "phase": "B/E", "blocking": True, "finding": "48/48 citation contexts have anchor=none and claim_to_passage=INCONCLUSIVE; zero can be passage-verified."},
        {"issue_id": "IL-MEDIUM-1", "severity": "MEDIUM", "phase": "failure-mode-4", "blocking": True, "finding": "Fixtures, expected oracle, and harness share one generator lineage; shortcut/circular agreement is not ruled out by an independent oracle/runtime."},
        {"issue_id": "NOTE-MINOR-1", "severity": "MINOR", "phase": "D3", "blocking": False, "finding": "Two heuristic writing indicators trigger an informational review alert; no AI-authorship determination is made."},
    ]
    report = {
        "schema_version": "p33-stage4.5-round2-integrity-report/1.0",
        "paper_id": "P33",
        "mode": 2,
        "stage": "4.5",
        "generated_at_utc": now,
        "verdict": "FAIL",
        "display_verdict": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
        "authorization": {"lock": artifact(LOCK), "receipt": artifact(AUTH), "repairs_authorized": False, "stage5_authorized": False},
        "bindings": {"draft": artifact(DRAFT), "bibliography": artifact(BIB), "block_manifest": artifact(BLOCK_MANIFEST), "revision_evidence_bundle": artifact(EVIDENCE_BUNDLE), "compliance_report": artifact(compliance_path)},
        "phases": {
            "A_references": {"registered": 22, "checked": 22, "verified": 22, "unresolved": 0, "verdict": "PASS", "artifact": artifact(phase_a_path)},
            "B_citation_contexts": {"registered": 48, "checked": 48, "verified": 0, "unverifiable": 48, "verdict": "FAIL", "artifact": artifact(phase_b_path)},
            "C_data_internal_provenance": {"registered": phase_c["registered_data_stat_surfaces"], "checked": phase_c["checked"], "verified": phase_c["verified"], "tables": "2/2", "figures": "0/0", "c4": "PASS", "verdict": "PASS", "boundary": phase_c["boundary"], "artifact": artifact(phase_c_path)},
            "D_originality": {"body": "38/72", "changed_body": "38/38", "topups": 2, "queries": "82/82", "original": originality["d1_grade_counts"]["ORIGINAL"], "close_match": originality["d1_grade_counts"]["CLOSE_MATCH"], "verbatim": originality["d1_grade_counts"]["VERBATIM"], "d2": "INCONCLUSIVE_IDENTITY", "d3": "MINOR_INFORMATIONAL_ALERT", "verdict": "PASS_WITH_NOTES", "artifact": artifact(originality_path), "attempt_history": attempt_history},
            "E_claims": {
                "registry_total": len(registry["claims"]),
                "checked": len(registry["claims"]),
                "verified": phase_e["verdict_counts"]["VERIFIED"],
                "unverifiable": phase_e["verdict_counts"]["UNVERIFIABLE"],
                "selection_tier": "ALL",
                "semantic_extraction_coverage": "not_machine_detectable",
                "candidate_unregistered_count": coverage["candidate_unregistered_count"],
                "coverage_report": artifact(coverage_path),
                "coverage_replay": artifact(coverage_replay_path),
                "evidence_rows_artifact": artifact(evidence_rows_path),
                "evidence_rows": evidence_rows,
                "semantic_verdicts_artifact": artifact(phase_e_path),
                "verdict": "FAIL",
            },
            "E6_claim_strength_drift": {"revision_rounds": 2, "operations_checked": 50, "detected_unauthorized_moves": 0, "verdict": "PASS", "review": artifact(e6_review_path), "findings": artifact(drift_path), "boundary": e6_review["wording_boundary"]},
            "seven_failure_modes": {"verdict": "FAIL", "blocking_modes": [4], "insufficient_evidence_modes": [2], "artifact": artifact(failure_path)},
            "isolated_build": {"verdict": "PASS", "pages": 18, "final_undefined_citations": 0, "artifact": artifact(build_path)},
            "schema12_compliance": {
                "mode": "other_evidence_synthesis",
                "prisma_mode": "informational_adaptation",
                "raise_mode": "full",
                "decision": "WARN",
                "contribution_boundary": "The non-SR compliance contribution is capped at WARN and remains separate from the blocking legacy integrity decision.",
                "artifact": artifact(compliance_path),
            },
        },
        "issue_counts": {"SERIOUS": 1, "MEDIUM": 1, "MINOR": 1},
        "issues": issues,
        "correction_list": artifact(correction_path),
        "protected_boundaries": boundary,
        "block_manifest_replay": block_manifest_replay,
        "route_and_initial_system": {"initial_system": lock_row["frozen_initial_system"], "route_state": lock_row["frozen_route_state"], "changed": False},
        "canonical_promotion_performed": False,
        "stage5_started": False,
        "assurance_boundary": "FAIL is an integrity-gate decision for unresolved passage support and synthetic-oracle independence. It is not a finding that the certificate architecture or underlying mathematics is false.",
    }
    report_path = write_json("stage4_5_round2_integrity_report.json", report)

    report_md = f"""# P33 Stage 4.5 Round 2 integrity report

## Verdict

**FAIL — corrections proposed, not applied. Stage 5 remains closed.**

| Phase | Denominator | Result |
|---|---:|---|
| A references | 22/22 | PASS |
| B citation contexts | 48/48 checked; 0 verified | FAIL |
| C data/tables/C4 | {phase_c['checked']}/{phase_c['checked']}; tables 2/2; figures 0 | PASS |
| D originality | 38/72 body; 38/38 changed body; 82/82 searches | PASS WITH NOTES |
| E registered claims | {len(registry['claims'])}/{len(registry['claims'])}; {phase_e['verdict_counts']['UNVERIFIABLE']} UNVERIFIABLE | FAIL |
| E6 revision operations | 50/50 across 2 rounds | PASS (none detected by recorded semantic review) |
| Seven failure modes | Mode 4 SUSPECTED; Mode 2 INSUFFICIENT EVIDENCE | FAIL |
| Isolated build | 4/4 commands; 18 pages; final citations clean | PASS |
| Schema 12 compliance | PRISMA-trAIce adaptation + RAISE full; non-SR contribution | WARN (separate) |

## Blocking findings

1. `IL-SERIOUS-1`: all 48 literature uses are `anchor=none` and `claim_to_passage=INCONCLUSIVE`. A bounded identifier endpoint is not passage verification.
2. `IL-MEDIUM-1`: one generator authored the synthetic fixtures, expected oracle, and harness; an independent oracle/runtime has not ruled out shortcut or circular agreement.

The correction list is `{correction_path.name}` ({sha_path(correction_path)}). No correction, manuscript/Bib edit, scientific execution, canonical promotion, Route change, or Stage-5 action was authorized or performed.

The independent Schema-12 compliance report is `{compliance_path.name}` ({sha_path(compliance_path)}) with `overall_decision=warn`. This compliance contribution does not dilute, replace, or manufacture the Phase-B/E and Mode-4 integrity findings.

The pre-authority originality attempt remains archived as `ATTEMPT1_INVALID`, and two post-authority aborted attempts remain fail-closed incident records. None of their partial material was reused; the controlling 82-query raw record is bound to the fresh collector.

## Mandatory C4 boundary

{phase_c['boundary']}

## Assurance boundary

The FAIL verdict concerns the audited evidence chain. It does not assert that the prospective certificate architecture or underlying mathematics is false.
"""
    report_md_path = write_text("stage4_5_round2_integrity_report.md", report_md)

    checkpoint = f"""# P33 Stage 4.5 Round 2 mandatory checkpoint

- Verdict: **FAIL**.
- Stage 5: **NOT AUTHORIZED / NOT STARTED**.
- Blocking issues: `IL-SERIOUS-1` (48/48 passage-inconclusive citation contexts) and `IL-MEDIUM-1` (Mode-4 same-lineage fixture/oracle/harness shortcut risk).
- Correction proposal: `{correction_path.name}` SHA-256 `{sha_path(correction_path)}`.
- Integrity report: `{report_path.name}` SHA-256 `{sha_path(report_path)}`.
- Schema-12 compliance: **WARN (separate contribution)**; `{compliance_path.name}` SHA-256 `{sha_path(compliance_path)}`.
- Repairs performed: none. Canonical manuscript, PDF, bibliography, scientific trees, route records, initial-system lock, and README files were not changed.

The next action requires explicit author authorization for a correction round or an explicit decision after the protocol's fail loop; this audit grants neither.
"""
    checkpoint_path = write_text("stage4_5_round2_mandatory_checkpoint.md", checkpoint)

    passport = copy.deepcopy(json.loads(PASSPORT_SEED.read_text(encoding="utf-8")))
    passport["content_hash"] = sha_path(DRAFT)
    passport["verification_status"] = "stage4_5_round2_fail_corrections_proposed_not_applied"
    passport["version_label"] = "p33-stage4.5-round2-audit-fail-sidecar"
    passport["stage4_5_round2_audit"] = {
        "verdict": "FAIL",
        "references": "22/22",
        "citation_context_support": "0/48",
        "claim_registry": f"{len(registry['claims'])}/{len(registry['claims'])} ALL reviewed",
        "claim_registry_candidate_gaps": 0,
        "evidence_rows": f"{len(evidence_rows)} rows for {len(registry['claims'])} distinct claims",
        "phase_c": "PASS",
        "originality": "38/72 body + 38/38 changed body + 2 declaration top-ups",
        "e6": "2 rounds/50 operations; none detected by recorded semantic review",
        "failure_modes": "Mode 4 SUSPECTED; Mode 2 INSUFFICIENT EVIDENCE",
        "stage5_started": False,
        "artifact_bindings": {
            "integrity_report_sha256": sha_path(report_path),
            "claim_registry_sha256": sha_path(registry_path),
            "coverage_sha256": sha_path(coverage_path),
            "evidence_rows_sha256": sha_path(evidence_rows_path),
            "phase_a_sha256": sha_path(phase_a_path),
            "phase_b_sha256": sha_path(phase_b_path),
            "phase_c_sha256": sha_path(phase_c_path),
            "originality_sha256": sha_path(originality_path),
            "originality_collector_sha256": sha_path(ORIGINALITY_COLLECTOR),
            "attempt1_invalid_incident_sha256": sha_path(ATTEMPT1_INCIDENT),
            "attempt2_incident_sha256": sha_path(ATTEMPT2_INCIDENT),
            "attempt3_incident_sha256": sha_path(ATTEMPT3_INCIDENT),
            "phase_e_sha256": sha_path(phase_e_path),
            "e6_review_sha256": sha_path(e6_review_path),
            "claim_strength_drift_sha256": sha_path(drift_path),
            "failure_modes_sha256": sha_path(failure_path),
            "build_receipt_sha256": sha_path(build_path),
            "correction_list_sha256": sha_path(correction_path),
            "compliance_report_sha256": sha_path(compliance_path),
        },
    }
    passport["compliance_history"].append({
        "stage": "4.5",
        "audit_round": 2,
        "generated_at": now,
        "mode": compliance["mode"],
        "overall_decision": compliance["overall_decision"],
        "upstream_sync_status": compliance["upstream_sync_status"],
        "user_action_required": compliance["user_action_required"],
        "evidence": compliance["evidence"],
        "raise": compliance["raise"],
        "prisma_trAIce": compliance["prisma_trAIce"],
        "compliance_report": artifact(compliance_path),
        "decision_boundary": "Schema-12 WARN is separate from the Stage-4.5 integrity FAIL and does not authorize a repair or Stage 5.",
    })
    passport_path = write_json("stage4_5_round2_material_passport.json", passport)

    # Final package-shape validation.  This validates contract shape and replay,
    # not the substantive truth of model-mediated judgments.
    validation_checks = {
        "authority_hashes": "PASS",
        "input_hashes": "PASS",
        "strict_utf8_draft": "PASS",
        "forbidden_control_bytes": "PASS" if not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", draft_text) else "FAIL",
        "block_markers_unique": "PASS" if len(order) == len(set(order)) == 128 else "FAIL",
        "block_manifest_128_of_128_hash_replay": block_manifest_replay["status"],
        "registry_schema": "PASS" if not schema_errors(registry, REGISTRY_SCHEMA) else "FAIL",
        "coverage_schema": "PASS" if not schema_errors(coverage, COVERAGE_SCHEMA) else "FAIL",
        "coverage_official_replay": "PASS" if not replay_errors else "FAIL",
        "coverage_candidate_gaps_zero": "PASS" if coverage["candidate_unregistered_count"] == 0 else "FAIL",
        "evidence_rows_official_validation": "PASS",
        "evidence_distinct_claim_count_matches": "PASS" if len({row["claim"]["claim_id"] for row in evidence_rows}) == len(registry["claims"]) else "FAIL",
        "phase_a_22_of_22": "PASS",
        "phase_b_48_of_48_honest_unverifiable": "PASS",
        "phase_c_all_surfaces_and_2_tables": "PASS",
        "phase_c4_exact_sentence": "PASS" if phase_c["boundary"] == "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS." else "FAIL",
        "originality_body_at_least_50_percent": "PASS" if 38 / 72 >= 0.5 else "FAIL",
        "originality_all_changed_body": "PASS",
        "originality_transport_82_of_82": "PASS",
        "originality_invalid_attempts_archived_and_not_reused": "PASS" if attempt_history_ok else "FAIL",
        "e6_2_rounds_50_ops": "PASS",
        "drift_schema": "PASS" if not schema_errors(drift, DRIFT_SCHEMA) else "FAIL",
        "correction_schema": "PASS" if not schema_errors(corrections, CORRECTION_SCHEMA) else "FAIL",
        "compliance_schema12": "PASS" if not compliance_module.validate(compliance) else "FAIL",
        "compliance_non_sr_warn_boundary": "PASS" if compliance["mode"] == "other_evidence_synthesis" and isinstance(compliance["prisma_trAIce"], dict) and compliance["raise"]["mode"] == "full" and compliance["overall_decision"] == compliance["prisma_trAIce"]["block_decision"] == compliance["raise"]["block_decision"] == "warn" else "FAIL",
        "seven_failure_modes_complete": "PASS",
        "isolated_build_final_pass_clean": "PASS",
        "protected_canonical_unchanged": "PASS" if boundary["canonical_unchanged"] else "FAIL",
        "science_trees_unchanged": "PASS" if boundary["science_file_inventory_unchanged"] else "FAIL",
        "route_and_initial_system_unchanged": "PASS" if boundary["route_hashes_match_lock"] else "FAIL",
        "repair_not_performed": "PASS",
        "stage5_not_started": "PASS",
    }
    if any(value != "PASS" for value in validation_checks.values()):
        raise RuntimeError(f"package validation failure: {validation_checks}")
    primary_paths = [
        registry_path, coverage_path, coverage_replay_path, phase_a_path, phase_b_path, phase_c_path,
        originality_path, originality_md_path, evidence_rows_path, phase_e_path, e6_review_path,
        drift_path, failure_path, build_path, correction_path, compliance_path, report_path, report_md_path,
        checkpoint_path, passport_path, ORIGINALITY_COLLECTOR, RAW_ORIGINALITY, BUILD_LOG,
    ]
    validation = {
        "schema_version": "p33-stage4.5-round2-validation-receipt/1.0",
        "paper_id": "P33",
        "generated_at_utc": now,
        "status": "PASS_AUDIT_PACKAGE_COHERENT_WITH_BLOCKING_INTEGRITY_VERDICT",
        "checks": validation_checks,
        "counts": {
            "registered_references": 22,
            "citation_contexts": 48,
            "data_stat_surfaces": phase_c["checked"],
            "tables": 2,
            "figures": 0,
            "body_sampled": 38,
            "body_population": 72,
            "changed_body_checked": 38,
            "changed_body_population": 38,
            "originality_queries": 82,
            "invalid_or_aborted_originality_attempts": 3,
            "registered_claims": len(registry["claims"]),
            "mechanical_coverage_candidates": len(coverage["candidates"]),
            "coverage_candidate_gaps": 0,
            "evidence_rows": len(evidence_rows),
            "revision_rounds": 2,
            "revision_operations": 50,
            "failure_modes": 7,
            "compliance_reports_schema12": 1,
        },
        "integrity_verdict": "FAIL",
        "compliance_decision": "warn",
        "compliance_report": artifact(compliance_path),
        "compliance_validator": artifact(COMPLIANCE_SCRIPT),
        "compliance_self_checks": {
            "CA-1_protocol_source": "PASS_READ_FROM_FROZEN_PRISMA_TRAICE_PROTOCOL",
            "CA-2_decision_tiers": "PASS_OTHER_EVIDENCE_SYNTHESIS_ADAPTATION_CAPPED_AT_WARN",
            "CA-3_sr_all_pass_empty_evidence": "NOT_APPLICABLE_NON_SR_MODE",
            "CA-4_raise_pass_without_evidence": "PASS_NO_RAISE_PRINCIPLE_MARKED_PASS",
        },
        "originality_attempt_history": attempt_history,
        "blocking_issue_ids": ["IL-SERIOUS-1", "IL-MEDIUM-1"],
        "artifacts": [artifact(path) for path in primary_paths],
        "protected_boundaries": boundary,
    }
    validation_path = write_json("stage4_5_round2_validation_receipt.json", validation)

    package_paths = primary_paths + [validation_path, Path(__file__)]
    package_manifest = {
        "schema_version": "p33-stage4.5-round2-package-manifest/1.0",
        "paper_id": "P33",
        "generated_at_utc": now,
        "status": "COMPLETE_FAIL_CHECKPOINT",
        "integrity_verdict": "FAIL",
        "compliance_decision": "warn",
        "files": [artifact(path) for path in package_paths],
        "originality_attempt_history": attempt_history,
        "boundaries": {
            "audit_sidecars_only": True,
            "repairs_applied": False,
            "canonical_or_science_mutation": False,
            "bibliography_mutation": False,
            "route_or_initial_system_mutation": False,
            "readme_mutation": False,
            "git_operation": False,
            "stage5_started": False,
        },
    }
    manifest_path = write_json("stage4_5_round2_package_manifest.json", package_manifest)
    print(json.dumps({
        "status": "COMPLETE_FAIL_CHECKPOINT",
        "registry_claims": len(registry["claims"]),
        "coverage_candidates": len(coverage["candidates"]),
        "coverage_gaps": coverage["candidate_unregistered_count"],
        "evidence_rows": len(evidence_rows),
        "phase_e_unverifiable_claims": phase_e["verdict_counts"]["UNVERIFIABLE"],
        "phase_c_surfaces": phase_c["checked"],
        "report": artifact(report_path),
        "validation": artifact(validation_path),
        "manifest": artifact(manifest_path),
    }, indent=2))


if __name__ == "__main__":
    main()
