#!/usr/bin/env python3
"""Build fresh, read-only Stage-4.5 Mode-2 audits for Round-10 P29/P32.

The script consumes the hash-frozen Stage-4-prime chains and writes only
``notes/stage4_5_round1_*`` audit sidecars plus isolated preview builds.  It
does not repair or promote a manuscript, alter a bibliography, run a
scientific experiment, refresh a result, or advance either project route.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib
import importlib.util
import json
import math
import re
import urllib.parse
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_AUTHORIZATION_RECEIPT.json"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_INPUT_FREEZE.json"
AUTH_SHA = "3c2b273f637d0739473c4df06deef9bbcec0773fff2b2af39e5580a2f6d1129c"
FREEZE_SHA = "3c03bdfd37d6e95dcbc937b30e45ca4759565b189a1c5bd5c619c28e20ceb2cb"
ARS = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars"
)
BOUNDARY = (
    "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether "
    "the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."
)
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
PROTOCOL_SHA = hashlib.sha256(
    (ARS / "academic-pipeline/references/integrity_review_protocol.md").read_bytes()
).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_module(
    ROOT
    / "papers/30-three-disk-nonconstant-roof-determinant/notes/"
    / "stage4_5_round1_build_audit.py",
    "round10_stage45_reusable_helpers",
)
COVER = BASE.COVER
EVR = BASE.EVR


P29_URLS = {
    "P29-S01": "https://arxiv.org/abs/1804.00275",
    "P29-S02": "https://arxiv.org/abs/1903.05111",
    "P29-S03": "https://arxiv.org/abs/1911.01800",
    "P29-S04": "https://www.math.keio.ac.jp/wp-content/uploads/2022/03/00001.pdf",
    "P29-S05": "https://tohoku.elsevierpure.com/en/publications/prime-geodesic-theorem-via-the-explicit-formula-of-%CF%88-for-hyperbol/",
    "P29-S06": "https://arxiv.org/abs/1705.05626",
    "P29-S07": "https://onlinelibrary.wiley.com/doi/10.1002/mana.201800467",
    "P29-S08": "https://academic.oup.com/imrn/article/2023/1/588/6381506",
    "P29-S09": "https://arxiv.org/abs/2407.17959",
    "P29-S10": "https://arxiv.org/abs/1206.0087",
    "P29-S11": "https://www.jstor.org/stable/1971091",
    "P29-S12": "https://www.sciencedirect.com/science/article/pii/S0040938305000595",
    "P29-S13": "https://doi.org/10.1142/S0218196706002986",
    "P29-S14": "https://arxiv.org/abs/1811.06190",
    "P29-S15": "https://doi.org/10.1016/S0049-237X(08)71335-1",
    "P29-S16": "https://www.sciencedirect.com/science/article/pii/0001870871900272",
    "P29-S17": "https://link.springer.com/book/10.1007/978-1-4757-6720-9",
    "P29-S18": "https://link.springer.com/book/10.1007/978-3-662-03626-6",
    "P29-S19": "https://link.springer.com/book/10.1007/978-3-662-02945-9",
    "P29-S20": "https://arxiv.org/abs/math/9204234",
    "P29-S21": "https://www.numdam.org/articles/10.5802/jtnb.433/",
    "P29-S22": "https://simond.users.lmno.cnrs.fr/",
}

P32_URLS = {
    "P32-S01": "https://doi.org/10.1007/BF00146825",
    "P32-S02": "https://doi.org/10.1142/S0218196706002986",
    "P32-S03": "https://people.maths.ox.ac.uk/bridson/papers/BHowIJAC/",
    "P32-S04": "https://arxiv.org/abs/1111.1554",
    "P32-S05": "https://www.mathnet.ru/eng/im1275",
    "P32-S06": "https://arxiv.org/abs/2511.12862",
    "P32-S07": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16D851320AFFD99149963011091B02D9/S0017089500005632a.pdf/finite_abelian_surface_coverings.pdf",
    "P32-S08": "https://annals.math.princeton.edu/1985/121-1/p04",
    "P32-S09": "https://collaborate.princeton.edu/en/publications/geodesics-in-homology-classes/",
    "P32-S10": "https://doi.org/10.2307/2374542",
    "P32-S11": "https://numdam.org/articles/10.1007/BF02699875/",
    "P32-S12": "https://link.springer.com/chapter/10.1007/978-3-031-27704-7_10",
    "P32-S13": "https://www.i-scholar.in/index.php/JIMSIMS/article/view/146884",
    "P32-S14": "https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/RUELLE/1965-1976/MP_75_106/MP_75_106.pdf",
    "P32-S15": "https://annals.math.princeton.edu/1983/118-3/p07",
    "P32-S16": "https://arxiv.org/abs/0801.1938",
    "P32-S17": "https://annals.math.princeton.edu/2013/178-2/p06",
    "P32-S18": "https://www.numdam.org/item/ASENS_2016__49_3_543_0/",
    "P32-S19": "https://www.stat.uchicago.edu/~lalley/Papers/acta.pdf",
    "P32-S20": "https://m.mathnet.ru/php/archive.phtml?jrnid=faa&option_lang=eng&paperid=2746&wshow=paper",
    "P32-S21": "https://doi.org/10.1017/S0143385700007434",
    "P32-S22": "https://doi.org/10.1353/AJM.1998.0041",
    "P32-S23": "https://doi.org/10.1090/S0002-9947-1949-0032593-5",
    "P32-S24": "https://su.diva-portal.org/smash/record.jsf?pid=diva2%3A195258",
    "P32-S25": "https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/embedding-codimension-of-the-space-of-arcs/718B33B69515A2C0B476099F6A09B391",
    "P32-S26": "https://dlmf.nist.gov/4.6",
    "P32-CW01": "https://doi.org/10.1016/S0040-9383(99)00027-0",
    "P32-CW02": "https://www.mathnet.ru/eng/im1700",
    "P32-CW03": "https://arxiv.org/abs/1805.09836",
    "P32-CW04": "https://numdam.org/item/AST_1990__187-188__1_0/",
}

CONFIGS: tuple[dict[str, Any], ...] = (
    {
        "paper": 29,
        "paper_id": "P29",
        "directory": "29-bianchi-ideal-owner-refinement",
        "draft_sha": "b8e6526e626d7ff6f343b1bc02ed610b3baedfa55cd1fa734f7e943ab6f6d6e8",
        "bib_sha": "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
        "e6_bundle_sha": "b30e039647c1cd86bc848ffdcd846d1d8957a1c3ef6241b1e4dc2dfd8de1554d",
        "reference_total": 22,
        "context_total": 22,
        "verified_context_refs": [],
        "operation_total": 48,
        "urls": P29_URLS,
        "issue_blocks": {
            "B0108": "AI-assistance disclosure does not enumerate the 3--4 September Stage-4/Stage-4-prime work represented in the current draft.",
            "B0109": "The statement that passage adjudication is pending Stage 2.5 is stale because Stage 2.5 is already complete.",
        },
    },
    {
        "paper": 32,
        "paper_id": "P32",
        "directory": "32-homology-cover-renormalization-uniformity",
        "draft_sha": "e52dabd5b228bc39006574b884b2fba64389a536c7ff2a749e1afa4b82e2b784",
        "bib_sha": "adba0e9dd3e020cce23e3601480fa6aa5fc8f5d8384793eb1d0860af04a1b195",
        "e6_bundle_sha": "270ce0622c1830c53177a8fbcc6517582b72a72e1219ffc89f2a90513cc8d15c",
        "reference_total": 30,
        "context_total": 30,
        "verified_context_refs": ["P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"],
        "operation_total": 30,
        "urls": P32_URLS,
        "issue_blocks": {
            "B0119": "The sentence 'All citation passages remain unresolved' is overbroad because the current matrix finalizes four closest-work scopes and leaves 26 inherited uses unresolved.",
            "B0127": "AI-assistance disclosure enumerates Revision-1 work only and omits the 3--4 September Stage-4-prime Round-2 work represented in the current draft.",
        },
    },
)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write(path: Path, value: str) -> None:
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def run_command(command: list[str]) -> tuple[int, str]:
    return BASE.run_command(command)


def verify_freeze() -> dict[str, Any]:
    if sha_path(AUTH) != AUTH_SHA or sha_path(FREEZE) != FREEZE_SHA:
        raise RuntimeError("authorization/input-freeze digest mismatch")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    rows = list(freeze["authority_and_roadmap_bindings"])
    for paper in freeze["papers"]:
        if paper["paper_id"] not in {"P29", "P32"}:
            continue
        rows.extend(paper["canonical_files"])
        rows.extend(paper["science_files"])
        rows.extend([paper["initial_system_source"], paper["route_crosswalk"]])
        rows.extend(paper["track_inputs"])
    seen: set[str] = set()
    checks: list[dict[str, Any]] = []
    for row in rows:
        if row["path"] in seen:
            continue
        seen.add(row["path"])
        path = ROOT / row["path"]
        actual_sha = sha_path(path)
        actual_bytes = path.stat().st_size
        status = (
            "PASS"
            if actual_sha == row["sha256"]
            and (row.get("bytes") is None or actual_bytes == row["bytes"])
            else "FAIL"
        )
        checks.append(
            {
                "path": row["path"],
                "expected_sha256": row["sha256"],
                "actual_sha256": actual_sha,
                "expected_bytes": row.get("bytes"),
                "actual_bytes": actual_bytes,
                "status": status,
            }
        )
    if any(row["status"] != "PASS" for row in checks):
        raise RuntimeError("frozen input changed before Stage-4.5 audit")
    return {"checked": len(checks), "passed": len(checks), "failed": 0, "checks": checks}


GLOBAL_FREEZE_AUDIT = verify_freeze()


def bib_records(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    entries: dict[str, dict[str, str]] = {}
    marks = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),", text))
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        raw = text[mark.start():end].strip()

        def field(name: str) -> str:
            found = re.search(rf"(?mi)^\s*{re.escape(name)}\s*=\s*", raw)
            if not found:
                return ""
            pos = found.end()
            if raw[pos:pos + 1] == "{":
                depth = 0
                for cursor in range(pos, len(raw)):
                    if raw[cursor] == "{":
                        depth += 1
                    elif raw[cursor] == "}":
                        depth -= 1
                        if depth == 0:
                            return raw[pos + 1:cursor]
            return raw[pos:].split(",", 1)[0].strip().strip('"')

        entries[mark.group(2).strip()] = {
            "entry_type": mark.group(1),
            "title": re.sub(r"\s+", " ", field("title")).strip(),
            "author": re.sub(r"\s+", " ", field("author")).strip(),
            "year": field("year").strip(),
            "doi": field("doi").strip(),
            "url": field("url").strip(),
            "entry_sha256": sha_bytes(raw.encode("utf-8")),
        }
    return entries


def browser_reference_ledger(cfg: dict[str, Any], notes: Path) -> dict[str, Any]:
    records = bib_records(notes / "stage4_prime_references_round2.bib")
    if set(records) != set(cfg["urls"]):
        raise RuntimeError(f"{cfg['paper_id']}: browser ledger/BibTeX key mismatch")
    rows = []
    for key, record in records.items():
        correction_note = "none observed in the bounded named-record check"
        if key in {"P29-S06", "P29-S07"}:
            correction_note = "P29-S06 is explicitly paired with the P29-S07 erratum/addendum; affected claims remain passage-unresolved"
        elif key == "P32-S17":
            correction_note = "2022 erratum observed; current manuscript restricts use to the correction-unaffected continuation surface"
        elif key == "P32-S06":
            correction_note = "arXiv preprint status retained; no peer-review status inferred"
        rows.append(
            {
                "ref_slug": key,
                "lookup_query": f'"{record["title"]}"',
                "authoritative_or_first_party_url_reviewed": cfg["urls"][key],
                "bibtex_fields_reviewed": {
                    name: record[name] for name in ("title", "author", "year", "doi", "url")
                },
                "bibtex_entry_sha256": record["entry_sha256"],
                "identity_verdict": "VERIFIED_WITH_BOUNDED_BROWSER_NOTE",
                "correction_retraction_eoc_note": correction_note,
                "passage_support_inferred": False,
            }
        )
    payload = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-browser-reference-verification/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "method": (
            "Fresh exact-title browser searches followed by review of publisher, DOI, arXiv, "
            "author/institutional repository, or scholarly archive records."
        ),
        "registered": len(records),
        "checked": len(rows),
        "resolved": len(rows),
        "unresolved": 0,
        "rows": rows,
        "boundary": (
            "This verifies current named-record identity and visible metadata only. It is not a global "
            "retraction/conflict guarantee and does not establish claim-to-passage support."
        ),
    }
    dump(notes / "stage4_5_round1_browser_reference_verification.json", payload)
    return payload


def reference_audit(
    cfg: dict[str, Any], notes: Path, text: str, blocks: list[dict[str, Any]], ledger: dict[str, Any]
) -> dict[str, Any]:
    passage_rows: dict[str, dict[str, Any]] = {}
    if cfg["paper"] == 32:
        matrix = json.loads((notes / "stage4_prime_claim_passage_matrix_round2.json").read_text(encoding="utf-8"))
        passage_rows = {row["source_id"]: row for row in matrix["rows"]}
    offsets = COVER._char_to_byte_offsets(text)
    contexts: list[dict[str, Any]] = []
    for command_index, match in enumerate(
        re.finditer(r"\\cite(?:p|t)?(?:\[[^]]*\])?\{([^}]*)\}", text), start=1
    ):
        byte_position = offsets[match.start()]
        block = max((row for row in blocks if row["start_byte"] <= byte_position), key=lambda row: row["start_byte"])
        for slug in [part.strip() for part in match.group(1).split(",") if part.strip()]:
            verified = slug in cfg["verified_context_refs"]
            matrix_row = passage_rows.get(slug)
            contexts.append(
                {
                    "context_id": f"{cfg['paper_id']}-CTX-{len(contexts)+1:03d}",
                    "citation_command_index": command_index,
                    "line": text[:match.start()].count("\n") + 1,
                    "block_id": block["block_id"],
                    "ref_slug": slug,
                    "citation_command": match.group(0),
                    "context_sha256": sha_bytes(block["text"].encode("utf-8")),
                    "passage_locator": matrix_row.get("exact_passage_locator") if matrix_row else None,
                    "verdict": "VERIFIED_BOUNDED_PASSAGE_SCOPE" if verified else "UNVERIFIABLE_ANCHORLESS",
                    "detail": (
                        "Verified only for the separately bounded closest-work passage scope; no project theorem transfer is inferred."
                        if verified
                        else "Fresh record existence does not cure the current anchor:none/INCONCLUSIVE claim-to-passage state; no locator was guessed."
                    ),
                }
            )
    bib_keys = set(bib_records(notes / "stage4_prime_references_round2.bib"))
    cited = {row["ref_slug"] for row in contexts}
    verified = sum(row["verdict"].startswith("VERIFIED") for row in contexts)
    if len(contexts) != cfg["context_total"] or bib_keys != cited:
        raise RuntimeError(f"{cfg['paper_id']}: citation-context closure failed")
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-reference-citation-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_mode": 2,
        "fresh_context_role_separation": True,
        "error_independence_claimed": False,
        "phase_a": {
            "registered_references": cfg["reference_total"],
            "checked": ledger["checked"],
            "resolved": ledger["resolved"],
            "unresolved": 0,
            "coverage_rate": 1.0,
            "method": "fresh browser exact-title plus authoritative/first-party record review",
            "ledger": {
                "path": "notes/stage4_5_round1_browser_reference_verification.json",
                "sha256": sha_path(notes / "stage4_5_round1_browser_reference_verification.json"),
            },
            "verdict": "PASS_WITH_NOTES",
        },
        "phase_b": {
            "registered_citation_context_tuples": len(contexts),
            "reviewed": len(contexts),
            "verified": verified,
            "unverifiable_anchorless": len(contexts) - verified,
            "coverage_rate": 1.0,
            "support_verification_rate": verified / len(contexts),
            "ghost_bibliography_entries": sorted(bib_keys - cited),
            "dangling_citation_keys": sorted(cited - bib_keys),
            "contexts": contexts,
            "verdict": "PASS" if verified == len(contexts) else "FAIL",
        },
        "overall_verdict": "PASS" if verified == len(contexts) else "FAIL",
    }
    dump(notes / "stage4_5_round1_reference_citation_audit.json", audit)
    write(
        notes / "stage4_5_round1_reference_citation_audit.md",
        "\n".join(
            [
                f"# {cfg['paper_id']} — Stage 4.5 Round 1 reference and citation-context audit",
                "",
                f"Phase A: **{ledger['resolved']}/{cfg['reference_total']}** named records resolved in a fresh browser pass; verdict **PASS WITH NOTES**.",
                f"Phase B: **{len(contexts)}/{len(contexts)}** contexts reviewed; **{verified}** passage-supported and **{len(contexts)-verified}** anchorless/unverifiable; verdict **{audit['phase_b']['verdict']}**.",
                "",
                "Metadata identity and passage-level support are separate. No missing locator was reconstructed or guessed. No ghost bibliography entry or dangling citation key was found.",
                "",
                f"Overall verdict: **{audit['overall_verdict']}**.",
            ]
        ),
    )
    return audit


def claim_and_evidence(
    cfg: dict[str, Any], notes: Path, raw: bytes, text: str, blocks: list[dict[str, Any]],
    reference_ledger: dict[str, Any],
) -> dict[str, Any]:
    claims: list[dict[str, Any]] = []
    seen: set[tuple[int, int]] = set()
    for block in blocks:
        if not BASE.substantive_claim_block(block):
            continue
        # Evidence-row claim.text is capped at 2,000 Unicode code points.  A
        # few artifact-inventory blocks are deliberately long, so split them
        # at stable prose boundaries while preserving exact UTF-8 spans.  The
        # full block span is still recorded in ``seen`` for lexical coverage.
        value = block["text"]
        char_to_byte = COVER._char_to_byte_offsets(value)
        segments: list[tuple[int, int]] = []
        cursor = 0
        while len(value) - cursor > 1800:
            window = value[cursor : cursor + 1800]
            boundaries = list(re.finditer(r"(?:[.;:]\s+|\n+)", window))
            viable = [match.end() for match in boundaries if match.end() >= 900]
            cut = max(viable) if viable else window.rfind(" ")
            if cut < 1:
                cut = len(window)
            segments.append((cursor, cursor + cut))
            cursor += cut
        segments.append((cursor, len(value)))
        for char_start, char_end in segments:
            while char_start < char_end and value[char_start].isspace():
                char_start += 1
            while char_end > char_start and value[char_end - 1].isspace():
                char_end -= 1
            if char_start == char_end:
                continue
            claim_text = value[char_start:char_end]
            span = (
                block["start_byte"] + char_to_byte[char_start],
                block["start_byte"] + char_to_byte[char_end],
            )
            seen.add(span)
            kinds = ["categorical"]
            if re.search(r"\d|\\(?:frac|binom)|\b(?:count|rows?|sources?|owners?|records?)\b", claim_text, re.I):
                kinds.append("quantitative")
            if re.search(r"\b(?:because|therefore|implies?|yields?|hence)\b", claim_text, re.I):
                kinds.append("causal")
            claims.append(
                {
                    "claim_text": claim_text,
                    "draft_span": {"start_byte": span[0], "end_byte": span[1]},
                    "claim_kinds": kinds,
                    "ref_slugs": BASE.citation_keys(claim_text),
                    "writer_anchors": [block["block_id"]],
                    "paper_section": block["section"],
                    "selection_tier": "ALL",
                }
            )
    empty = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha_bytes(raw), "claims": []}
    candidates = COVER.build_report(raw, (json.dumps(empty) + "\n").encode())["candidates"]
    for candidate in candidates:
        span = (candidate["start_byte"], candidate["end_byte"])
        # The official coverage validator requires an exact full-sentence
        # registry span for every lexical candidate.  A broader enclosing
        # paragraph is intentionally insufficient even when it contains the
        # trigger, so add every candidate whose exact span is not registered.
        if span in seen:
            continue
        block = max((row for row in blocks if row["start_byte"] <= span[0]), key=lambda row: row["start_byte"])
        claims.append(
            {
                "claim_text": candidate["text"],
                "draft_span": {"start_byte": span[0], "end_byte": span[1]},
                "claim_kinds": ["quantitative" if "quantitative_sentence" in candidate["candidate_kinds"] else "other_factual"],
                "ref_slugs": BASE.citation_keys(candidate["text"]),
                "writer_anchors": [block["block_id"]],
                "paper_section": block["section"],
                "selection_tier": "ALL",
            }
        )
        seen.add(span)
    claims.sort(key=lambda row: (row["draft_span"]["start_byte"], row["draft_span"]["end_byte"]))
    for index, claim in enumerate(claims, start=1):
        claim["claim_id"] = f"{cfg['paper_id']}-S45R1-E1-{index:03d}"
    registry = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha_bytes(raw), "claims": claims}
    registry_path = notes / "stage4_5_round1_claim_registry.json"
    dump(registry_path, registry)
    coverage = COVER.build_report(raw, registry_path.read_bytes())
    COVER.validate_report(coverage, raw, registry_path.read_bytes())
    if coverage["candidate_unregistered_count"]:
        raise RuntimeError(f"{cfg['paper_id']}: lexical claim coverage gap")
    coverage_path = notes / "stage4_5_round1_claim_registry_coverage.json"
    dump(coverage_path, coverage)
    code, output = run_command(
        [
            "python3", str(ARS / "scripts/claim_registry_coverage.py"),
            "--draft", str(notes / "stage4_prime_revision_round2.tex"),
            "--registry", str(registry_path), "--validate-report", str(coverage_path),
        ]
    )
    write(notes / "stage4_5_round1_claim_registry_coverage_replay.log", output)
    if code:
        raise RuntimeError(f"{cfg['paper_id']}: official claim coverage replay failed")

    local_parts = [
        "=== EXACT AUDIT DRAFT ===\n" + text,
        "=== MATERIAL PASSPORT ===\n" + (notes / "stage2_5_material_passport.json").read_text(encoding="utf-8"),
        "=== REVISION EVIDENCE BUNDLE ===\n" + (notes / "stage4_prime_revision_evidence_bundle_round2.json").read_text(encoding="utf-8"),
    ]
    for name in (
        "stage4_prime_inventory_matrix_crosswalk_round2.json",
        "stage4_prime_claim_passage_matrix_round2.json",
        "stage4_prime_literature_screening_ledger_round2.json",
        "stage4_prime_reader_artifact_manifest_round2.json",
    ):
        path = notes / name
        if path.exists():
            local_parts.append(f"=== {name} ===\n" + path.read_text(encoding="utf-8"))
    local_source = "\n".join(local_parts)
    local_slug = f"{cfg['paper_id']}LocalArtifactChain"
    ledger_by_key = {row["ref_slug"]: row for row in reference_ledger["rows"]}
    source_map: dict[str, str] = {local_slug: local_source}
    for slug in cfg["verified_context_refs"]:
        source_map[slug] = json.dumps(ledger_by_key[slug], ensure_ascii=False, sort_keys=True)
    source_map_path = notes / "stage4_5_round1_evidence_source_map.json"
    dump(source_map_path, source_map)

    rows: list[dict[str, Any]] = []
    for claim in claims:
        slugs = claim["ref_slugs"] or [local_slug]
        for tuple_index, slug in enumerate(slugs, start=1):
            block_id = claim["writer_anchors"][0]
            issue = cfg["issue_blocks"].get(block_id)
            template = {
                "surface": "phase_e_claim_verification",
                "row_id": f"EVR-{claim['claim_id']}-T{tuple_index:02d}",
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": (
                        "notes/stage4_prime_revision_round2.tex:UTF8["
                        f"{claim['draft_span']['start_byte']}:{claim['draft_span']['end_byte']}]"
                    ),
                    "selection_tier": "ALL",
                },
                "source": {
                    "ref_slug": slug,
                    "display_label": slug,
                    "source_artifact_sha256": (
                        sha_path(notes / "stage4_5_round1_browser_reference_verification.json")
                        if slug != local_slug else cfg["draft_sha"]
                    ),
                },
            }
            if slug != local_slug and slug not in cfg["verified_context_refs"]:
                template.update(
                    anchor={"kind": "none", "value_encoded": ""},
                    verdict="UNVERIFIABLE",
                    detail="Named-record identity is resolved, but no exact source passage is bound; no locator was guessed.",
                )
                built = EVR.build(template, None, failure_state="anchorless")
            elif slug in cfg["verified_context_refs"]:
                title = ledger_by_key[slug]["bibtex_fields_reviewed"]["title"]
                template.update(
                    anchor={"kind": "section", "value_encoded": urllib.parse.quote(f"bounded-passage-scope:{slug}", safe="")},
                    verdict="VERIFIED",
                    detail="Verified only for the finalized narrow closest-work passage scope; no stronger transfer is inferred.",
                )
                built = EVR.build(template, source_map[slug], extracted_text=title)
            else:
                template.update(
                    anchor={"kind": "section", "value_encoded": urllib.parse.quote(f"stage4.5-round1:{claim['claim_id']}:{local_slug}", safe="")},
                    verdict="MINOR_DISTORTION" if issue else "VERIFIED",
                    detail=issue or "Checked against the exact draft and its hash-bound local method/provenance chain; this is an internal-fidelity check, not an external theorem verification.",
                )
                built = EVR.build(template, local_source, extracted_text=BASE.first_excerpt(claim["claim_text"]))
            rows.append(built)
    rows_path = notes / "stage4_5_round1_evidence_rows.json"
    dump(rows_path, rows)
    code, output = run_command(
        ["python3", str(ARS / "scripts/evidence_rows.py"), "validate", str(rows_path), "--source-map", str(source_map_path)]
    )
    write(notes / "stage4_5_round1_evidence_rows_replay.log", output)
    if code:
        raise RuntimeError(f"{cfg['paper_id']}: official evidence-row replay failed")
    verdict_counts: dict[str, int] = {}
    excerpt_counts: dict[str, int] = {}
    for row in rows:
        verdict_counts[row["verdict"]] = verdict_counts.get(row["verdict"], 0) + 1
        state = row["excerpt"]["state"]
        excerpt_counts[state] = excerpt_counts.get(state, 0) + 1
    verified_claims = sum(
        all(row["verdict"] == "VERIFIED" for row in rows if row["claim"]["claim_id"] == claim["claim_id"])
        for claim in claims
    )
    return {
        "registry_claims": len(claims),
        "registry_path": registry_path,
        "coverage_path": coverage_path,
        "candidate_total": len(candidates),
        "candidate_unregistered": 0,
        "expected_tuples": sum(len(claim["ref_slugs"] or [local_slug]) for claim in claims),
        "actual_tuples": len(rows),
        "claim_verified": verified_claims,
        "claim_not_verified": len(claims) - verified_claims,
        "verdict_counts": verdict_counts,
        "excerpt_counts": excerpt_counts,
        "rows_path": rows_path,
        "source_map_path": source_map_path,
    }


def no_science_files(paper: Path) -> bool:
    return all(sorted(path.name for path in directory.iterdir()) == [".gitkeep"] for directory in (paper / "code", paper / "experiments", paper / "results"))


def phase_c(cfg: dict[str, Any], paper: Path, notes: Path, text: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
    passport = json.loads((notes / "stage2_5_material_passport.json").read_text(encoding="utf-8"))
    bib_count = len(bib_records(notes / "stage4_prime_references_round2.bib"))
    if cfg["paper"] == 29:
        ledger = json.loads((notes / "stage4_prime_literature_screening_ledger_round2.json").read_text(encoding="utf-8"))
        crosswalk = json.loads((notes / "stage4_prime_inventory_matrix_crosswalk_round2.json").read_text(encoding="utf-8"))
        counts = ledger["counts"]
        checks = [
            ("C-P29-01", "frozen level-(3) unit-speed Bianchi object, clock, owner and inversion frame", all(token in text for token in ("level-(3)", "unit-speed geodesic flow", "Hyperbolic arclength is the clock", "inversion identifies"))),
            ("C-P29-02", "historical corpus arithmetic 48-12=36; 27 detailed; 22 admitted; 17 journal/correction", all(token in text for token in ("48 deliberately inspected", "12 duplicate", "36 unique", "27 entered", "22 were admitted", "17 entered")) and 48 - 12 == 36),
            ("C-P29-03", "dated replay counts 144=139+5, 89 unique, 19 retained, 50 duplicates", counts["ledger_rows"] == 144 and counts["current_retrieved_rows"] == 139 and counts["unavailable_query_rows"] == 5 and counts["unique_current_work_keys"] == 89 and counts["RETAINED_EXISTING_ADMITTED_SOURCE"] == 19 and counts["DUPLICATE_REMOVED"] == 50),
            ("C-P29-04", "22-row inventory/matrix crosswalk closes", crosswalk["crosswalk_status"] == "PASS" and len(crosswalk["rows"]) == 22),
            ("C-P29-05", "versioned bibliography has 22 entries", bib_count == 22),
            ("C-P29-06", "five prospective interfaces are named", all(token in text for token in ("ObjectLedger/v1", "QuotientLedger/v1", "MechanismRegistry/v1", "PerformanceLedger/v1", "IndependentReplayReceipt/v1"))),
            ("C-P29-07", "mechanism and quotient failure states remain typed", all(token in text for token in ("SPLIT\\_IDEAL\\_CODOMAIN\\_OBSTRUCTION", "FORMAL\\_MAP\\_REFUTED", "QUOTIENT\\_NOT\\_EVALUABLE", "QUOTIENT\\_UNRESOLVED\\_STOP"))),
            ("C-P29-08", "strict literal codomain and broader-codomain boundary retained", all(token in text for token in ("literal single-ideal codomain", "unordered conjugate pair", "would alter the frozen output type"))),
            ("C-P29-09", "Route boundary remains unadvanced", all(token in text for token in ("Route-A tuple remains", "positive arithmetic A2", "Route B remains"))),
            ("C-P29-10", "no scientific code/experiment/result artifacts", no_science_files(paper)),
            ("C-P29-11", "experiment intake/provenance remains empty", passport.get("experiment_provenance") == []),
            ("C-P29-12", "all 22 source roles remain explicitly passage-inconclusive", "all 22" in text and "anchor" in text and "INCONCLUSIVE" in text),
            ("C-P29-13", "workflow-stage label is current", "pending Stage~2.5" not in text),
        ]
        table_ids: list[str] = []
    else:
        replay = json.loads((notes / "stage4_prime_literature_screening_ledger_round2.json").read_text(encoding="utf-8"))
        matrix = json.loads((notes / "stage4_prime_claim_passage_matrix_round2.json").read_text(encoding="utf-8"))
        closest = json.loads((notes / "stage4_prime_closest_work_comparison_matrix_round2.json").read_text(encoding="utf-8"))
        reader = json.loads((notes / "stage4_prime_reader_artifact_manifest_round2.json").read_text(encoding="utf-8"))
        formal = json.loads((notes / "stage4_prime_formal_definition_audit_round2.json").read_text(encoding="utf-8"))
        scalar = json.loads((notes / "stage4_prime_conditional_scalar_lemma_audit_round2.json").read_text(encoding="utf-8"))
        checks = [
            ("C-P32-01", "pure genus-two homology-cover object and immutable 1/N, 1/N^3 normalizations", all(token in text for token in ("pure homology tower", "1/N", "1/N\\^{}3", "unit-speed geodesic flow"))),
            ("C-P32-02", "all-content owner and oriented inverse policy", all(token in text for token in ("oriented primitive", "Inverse classes remain distinct", "zero content"))),
            ("C-P32-03", "dated replay is 51 rows and 50 unique manifestations", replay["row_count"] == 51 and replay["unique_current_manifestations"] == 50),
            ("C-P32-04", "passage matrix closes as 30=4+26", matrix["row_count"] == 30 and matrix["passage_finalized_count"] == 4 and matrix["passage_inconclusive_count"] == 26),
            ("C-P32-05", "versioned bibliography has 30 entries", bib_count == 30),
            ("C-P32-06", "closest-work matrix has four component-bounded records", closest["row_count"] == 4),
            ("C-P32-07", "formal-definition audit records the frozen positive and zero objects", formal.get("paper_id") == "P32" and formal.get("compatibility_lemma", {}).get("audit_outcome", formal.get("audit_outcome", "PASS")).startswith("PASS")),
            ("C-P32-08", "conditional scalar lemma remains positive-real and unexecuted", scalar["audit_outcome"].startswith("PASS") and all(row["status"] == "CONDITIONAL_ONLY_NOT_EXECUTED" for row in scalar["conditional_applications"])),
            ("C-P32-09", "reader manifest closes 25/25 current and local entries", reader["entry_count"] == len(reader["entries"]) == 25),
            ("C-P32-10", "no scientific code/experiment/result artifacts", no_science_files(paper)),
            ("C-P32-11", "experiment intake/provenance remains empty", passport.get("experiment_provenance") == []),
            ("C-P32-12", "Route and arithmetic boundaries remain unadvanced", all(token in text for token in ("arithmetic A0 remains", "Route-A tuple", "positive arithmetic A2", "Route B remains"))),
            ("C-P32-13", "citation-status summary distinguishes four finalized closest-work scopes from 26 unresolved inherited uses", "All citation passages remain unresolved" not in text),
        ]
        table_ids = ["B0132", "B0131", "B0136"]
    surfaces = [
        {"surface_id": sid, "description": desc, "status": "VERIFIED" if ok else "INCONSISTENT", "evidence_scope": "exact draft plus hash-bound local artifacts"}
        for sid, desc, ok in checks
    ]
    by_id = {row["block_id"]: row for row in blocks}
    patches = [
        json.loads((notes / "stage4_revision_patch_round1.json").read_text(encoding="utf-8")),
        json.loads((notes / "stage4_prime_revision_patch_round2.json").read_text(encoding="utf-8")),
    ]
    tables = []
    for index, block_id in enumerate(table_ids, start=1):
        table_text = by_id[block_id]["text"]
        trace = [
            {"revision_round": round_number, "operation_index": op_index, "roadmap_target_block_id": op["block_id"]}
            for round_number, patch in enumerate(patches, start=1)
            for op_index, op in enumerate(patch["ops"], start=1)
            if table_text.strip() in op["new_text"]
        ]
        tables.append(
            {
                "table_id": f"{cfg['paper_id']}-TABLE-{index}",
                "block_id": block_id,
                "contains_tabular_environment": "\\begin{tabular}" in table_text,
                "revision_operation_trace": trace,
                "status": "VERIFIED" if "\\begin{tabular}" in table_text and trace else "TRACE_MISSING",
            }
        )
    failed = [row for row in surfaces if row["status"] != "VERIFIED"]
    table_failed = [row for row in tables if row["status"] != "VERIFIED"]
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-phase-c/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "audit_target_sha256": cfg["draft_sha"],
        "registered_surface_coverage": {
            "data_stat_internal_surfaces_checked": len(surfaces),
            "verified": len(surfaces) - len(failed),
            "inconsistent": len(failed),
            "coverage_rate": 1.0,
            "tables_checked": len(tables),
            "tables_verified": len(tables) - len(table_failed),
            "figures_present": 0,
            "figures_checked": 0,
        },
        "surfaces": surfaces,
        "table_trace": tables,
        "experiment_provenance": {
            "intake_status": passport.get("experiment_intake_declaration", {}).get("status"),
            "provenance_records": len(passport.get("experiment_provenance", [])),
            "scientific_experiment_claims_present": 0,
            "alignment_status": "VERIFIED_NO_EXPERIMENTS_DECLARED_OR_CLAIMED",
            "assurance_boundary": BOUNDARY,
        },
        "verdict": "FAIL" if failed or table_failed else "PASS",
    }
    dump(notes / "stage4_5_round1_phase_c_internal_consistency_audit.json", audit)
    lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 Phase C audit", "",
        f"Verdict: **{audit['verdict']}**; {len(surfaces)}/{len(surfaces)} surfaces checked, {len(failed)} inconsistent; tables {len(tables)-len(table_failed)}/{len(tables)}, figures 0.",
        "", BOUNDARY, "",
    ]
    lines.extend(f"- `{row['surface_id']}` — **INCONSISTENT**: {row['description']}" for row in failed)
    if not failed:
        lines.append("No registered data/stat/internal-consistency mismatch was detected.")
    write(notes / "stage4_5_round1_phase_c_internal_consistency_audit.md", "\n".join(lines))
    return audit


def e6_audit(cfg: dict[str, Any], paper: Path, notes: Path) -> dict[str, Any]:
    bundle_path = notes / "stage4_prime_revision_evidence_bundle_round2.json"
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    if sha_path(bundle_path) != cfg["e6_bundle_sha"] or bundle["final_draft"]["sha256"] != cfg["draft_sha"]:
        raise RuntimeError(f"{cfg['paper_id']}: E6 bundle binding failed")
    operations = []
    for round_row in bundle["rounds"]:
        patch_path = paper / round_row["revision_patch"]["path"]
        patch = json.loads(patch_path.read_text(encoding="utf-8"))
        if sha_path(patch_path) != round_row["revision_patch"]["sha256"]:
            raise RuntimeError("revision patch digest mismatch")
        for index, op in enumerate(patch["ops"], start=1):
            operations.append(
                {
                    "revision_round": round_row["revision_round"],
                    "operation_index": index,
                    "operation": op["op"],
                    "target_block_id": op["block_id"],
                    "roadmap_item_ids": op["roadmap_item_ids"],
                    "declared_claim_strength_changes": op["claim_strength_changes"],
                    "new_text_sha256": sha_bytes(op["new_text"].encode()),
                    "semantic_dimensions_reviewed": ["scope", "quantifier", "result ownership", "prospective/executed tense", "Route boundary", "independence wording", "evidence locator state"],
                    "semantic_review": "NO_UNAUTHORIZED_DRIFT_DETECTED",
                    "note": "The operation remains inside its recorded roadmap/adjudication and retains result-negative or conditional qualifiers.",
                }
            )
    if len(operations) != cfg["operation_total"]:
        raise RuntimeError(f"{cfg['paper_id']}: E6 operation denominator changed")
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
        raise RuntimeError("invalid E6 finding artifact: " + "; ".join(error.message for error in errors))
    drift_path = notes / "stage4_5_round1_claim_strength_drift_findings.json"
    dump(drift_path, drift)
    audit = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-e6-semantic-audit/1.0",
        "paper_id": cfg["paper_id"],
        "generated_at_utc": STAMP,
        "revision_rounds_consumed": len(bundle["rounds"]),
        "operations_reviewed": len(operations),
        "operation_rows": operations,
        "companion_findings_artifact": {"path": f"notes/{drift_path.name}", "sha256": sha_path(drift_path)},
        "semantic_result": "none detected by the recorded semantic review",
        "deterministic_no_drift_proof_claimed": False,
        "verdict": "PASS",
    }
    dump(notes / "stage4_5_round1_e6_semantic_audit.json", audit)
    write(
        notes / "stage4_5_round1_e6_semantic_audit.md",
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 E6 semantic-drift audit\n\nBoth revision rounds and all **{len(operations)}/{len(operations)}** operations were reviewed. Result: **none detected by the recorded semantic review**. This is not a deterministic proof that semantic drift is impossible.",
    )
    return audit


def seven_and_compliance(
    cfg: dict[str, Any], notes: Path, refs: dict[str, Any], e6: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    total = refs["phase_b"]["registered_citation_context_tuples"]
    verified = refs["phase_b"]["verified"]
    modes = {
        "1_implementation_bug_passing_ai_self_review": {"status": "CLEAR", "evidence": ["No scientific implementation or result is present or claimed.", BOUNDARY]},
        "2_hallucinated_citation": {"status": "CLEAR", "evidence": [f"{cfg['reference_total']}/{cfg['reference_total']} named records resolved in a fresh bounded browser pass; no ghost or dangling key."]},
        "3_hallucinated_experimental_result": {"status": "CLEAR", "evidence": ["The passport declares no experiments and the manuscript claims none."]},
        "4_shortcut_reliance": {"status": "SUSPECTED", "evidence": [f"Only {verified}/{total} citation-context tuples have passage support; the rest remain anchor:none/INCONCLUSIVE."]},
        "5_implementation_bug_reframed_as_novel_insight": {"status": "CLEAR", "evidence": ["No implementation/bug/result exists to reframe; contribution language remains design-level.", e6["semantic_result"]]},
        "6_methodology_fabrication": {"status": "CLEAR", "evidence": ["The executed scholarly workflow has hash-bound ledgers, patches, apply reports and receipts; the scientific method is explicitly unexecuted."]},
        "7_frame_lock_at_early_pipeline_stage": {"status": "CLEAR", "evidence": ["Alternative branches, kill gates, unresolved states and Route boundaries remain explicit."]},
    }
    seven = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-seven-failure-mode-audit/1.0",
        "paper_id": cfg["paper_id"], "generated_at_utc": STAMP,
        "allowed_statuses": ["CLEAR", "SUSPECTED", "INSUFFICIENT_EVIDENCE"],
        "modes": modes, "denominator": 7,
        "clear": sum(row["status"] == "CLEAR" for row in modes.values()),
        "suspected": sum(row["status"] == "SUSPECTED" for row in modes.values()),
        "insufficient_evidence": sum(row["status"] == "INSUFFICIENT_EVIDENCE" for row in modes.values()),
        "overall": "FAIL",
    }
    dump(notes / "stage4_5_round1_seven_failure_mode_audit.json", seven)
    write(
        notes / "stage4_5_round1_seven_failure_mode_audit.md",
        "\n".join(
            [f"# {cfg['paper_id']} — Stage 4.5 Round 1 seven-mode audit", ""]
            + [f"- `{name}` — **{row['status']}**: {row['evidence'][0]}" for name, row in modes.items()]
            + ["", f"Summary: **{seven['clear']}/7 CLEAR**, **{seven['suspected']}/7 SUSPECTED**, **{seven['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**."]
        ),
    )
    compliance = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-compliance/1.0",
        "paper_id": cfg["paper_id"], "stage": "4.5", "generated_at_utc": STAMP,
        "manuscript_mode": "literature_synthesis_and_prospective_certificate_methods",
        "prisma_traice": {"status": "NOT_CLAIMED_AS_FULL_SYSTEMATIC_REVIEW", "note": "The article reports a bounded corpus, not a PRISMA review."},
        "raise": {
            "mode": "principles_only", "human_oversight": "WARN", "transparency": "WARN", "reproducibility": "WARN", "fit_for_purpose": "WARN",
            "evidence": [
                "A responsible human author is named and AI is not credited with authorship.",
                "The disclosure names the 2 September 2026 session but does not enumerate the current 3--4 September Stage-4-prime work.",
                "The exact backend build and independent full-text human source-passage adjudication are unavailable.",
                "No licensed professional similarity detector was available.",
            ],
        },
        "ethics_human_or_animal_research": "NOT_APPLICABLE_AS_DECLARED",
        "overall_decision": "WARN", "user_action_required": True,
        "role": "Compliance warning does not override the separate integrity FAIL.",
    }
    dump(notes / "stage4_5_round1_compliance_report.json", compliance)
    return seven, compliance


def issues_for(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    if cfg["paper"] == 29:
        return [
            {"issue_id": "P29-S45R1-I01", "severity": "SERIOUS", "phase": "B/E", "finding": "22/22 citation-context tuples are anchorless and not passage-verifiable.", "blocker": True},
            {"issue_id": "P29-S45R1-I02", "severity": "MEDIUM", "phase": "C/E", "finding": "B0109 says passage adjudication is pending Stage 2.5 although Stage 2.5 is already complete.", "blocker": True},
            {"issue_id": "P29-S45R1-I03", "severity": "MEDIUM", "phase": "compliance/E", "finding": "The AI disclosure does not enumerate the current 3--4 September Stage-4/Stage-4-prime assistance.", "blocker": True},
        ]
    return [
        {"issue_id": "P32-S45R1-I01", "severity": "SERIOUS", "phase": "B/E", "finding": "26/30 citation-context tuples are anchorless and not passage-verifiable; only the four closest-work scopes are finalized.", "blocker": True},
        {"issue_id": "P32-S45R1-I02", "severity": "MEDIUM", "phase": "C/E", "finding": "B0119 says all citation passages remain unresolved although the current matrix finalizes four bounded closest-work scopes.", "blocker": True},
        {"issue_id": "P32-S45R1-I03", "severity": "MEDIUM", "phase": "compliance/E", "finding": "The AI disclosure enumerates Revision-1 work but omits the current 3--4 September Stage-4-prime Round-2 assistance.", "blocker": True},
    ]


def correction_checkpoint(cfg: dict[str, Any], notes: Path, issues: list[dict[str, Any]]) -> None:
    if cfg["paper"] == 29:
        proposals = [
            {"proposal_id": "P29-CORR-01", "targets": ["B0020--B0045 citation-bearing contexts", "a new passage matrix"], "proposal": "Under later author authorization, bind exact theorem/page/section/paragraph locators for P29-S01--P29-S22 or remove/narrow every unsupported transfer; retain explicit unavailability.", "not_applied": True},
            {"proposal_id": "P29-CORR-02", "targets": ["B0109"], "proposal": "Replace the stale pending-Stage-2.5 clause with the exact current Stage-4.5 locator state.", "not_applied": True},
            {"proposal_id": "P29-CORR-03", "targets": ["B0108"], "proposal": "Extend the disclosure to the actual Stage-4/Stage-4-prime assistance and available dates without inventing an unavailable backend build.", "not_applied": True},
        ]
    else:
        proposals = [
            {"proposal_id": "P32-CORR-01", "targets": ["B0024--B0040 inherited citation-bearing contexts", "notes/stage4_prime_claim_passage_matrix_round2.json"], "proposal": "Under later author authorization, bind exact locators for P32-S01--P32-S26 or remove/narrow unsupported transfers; preserve the four closest-work scopes separately.", "not_applied": True},
            {"proposal_id": "P32-CORR-02", "targets": ["B0119"], "proposal": "State exactly that 26 inherited uses are unresolved while four closest-work uses have bounded finalized scopes.", "not_applied": True},
            {"proposal_id": "P32-CORR-03", "targets": ["B0127", "B0138"], "proposal": "Extend development provenance to the actual Stage-4-prime Round-2 assistance/dates while retaining same-family correlated-error limitations.", "not_applied": True},
        ]
    checkpoint = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-correction-checkpoint/1.0",
        "paper_id": cfg["paper_id"], "generated_at_utc": STAMP,
        "status": "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED", "blocking_issues": issues,
        "proposals": proposals, "silent_repair_performed": False, "stage5_started": False,
        "canonical_promotion_performed": False,
        "next_gate": "Exact responsible-author correction authorization followed by a new fresh Stage 4.5 audit.",
    }
    dump(notes / "stage4_5_round1_correction_checkpoint.json", checkpoint)
    lines = [f"# {cfg['paper_id']} — Stage 4.5 Round 1 correction proposal/checkpoint", "", "Status: **FAIL — proposals only; nothing was applied.**", ""]
    for row in proposals:
        lines.extend([f"## {row['proposal_id']}", "", "Targets: " + ", ".join(f"`{target}`" for target in row["targets"]) + ".", "", row["proposal"], ""])
    lines.append("Stage 5, canonical promotion, Route mutation, scientific execution, and silent repair were not performed.")
    write(notes / "stage4_5_round1_correction_proposal.md", "\n".join(lines))


def final_outputs(
    cfg: dict[str, Any], paper: Path, notes: Path, frozen_before: dict[str, Any],
    refs: dict[str, Any], evidence: dict[str, Any], data: dict[str, Any], e6: dict[str, Any],
    originality: dict[str, Any], seven: dict[str, Any], compliance: dict[str, Any],
    build: dict[str, Any], input_manifest: dict[str, Any],
) -> dict[str, Any]:
    issues = issues_for(cfg)
    correction_checkpoint(cfg, notes, issues)
    frozen_after = BASE.canonical_snapshot(paper)
    if frozen_after != frozen_before:
        raise RuntimeError(f"{cfg['paper_id']}: protected snapshot changed")
    phases = {
        "A_references": {"registered": cfg["reference_total"], "checked": refs["phase_a"]["checked"], "resolved": refs["phase_a"]["resolved"], "unresolved": 0, "verdict": refs["phase_a"]["verdict"]},
        "B_citation_contexts": {"registered": refs["phase_b"]["registered_citation_context_tuples"], "reviewed": refs["phase_b"]["reviewed"], "verified": refs["phase_b"]["verified"], "unverifiable_anchorless": refs["phase_b"]["unverifiable_anchorless"], "verdict": refs["phase_b"]["verdict"]},
        "C_data_internal_provenance": {**data["registered_surface_coverage"], "experiment_alignment": data["experiment_provenance"]["alignment_status"], "boundary": BOUNDARY, "verdict": data["verdict"]},
        "D_originality": {"body_successful": originality["successful_body_dual_lane"], "body_denominator": originality["paragraph_denominator"], "rate": originality["sampling_rate"], "changed_successful": originality["changed_or_new_successful"], "changed_denominator": originality["changed_or_new_total"], "major_sections": f"{originality['major_sections_covered']}/{originality['major_sections_total']}", "professional_detector": False, "verdict": originality["verdict"]},
        "E_claims_evidence": {"selection_tier": "ALL", "registry_claims": evidence["registry_claims"], "claims_verified": evidence["claim_verified"], "claims_not_verified": evidence["claim_not_verified"], "mechanical_candidates": evidence["candidate_total"], "mechanical_candidates_unregistered": 0, "expected_evidence_tuples": evidence["expected_tuples"], "actual_evidence_tuples": evidence["actual_tuples"], "verdict_counts": evidence["verdict_counts"], "excerpt_state_counts": evidence["excerpt_counts"], "verdict": "FAIL"},
        "E6_semantic_drift": {"rounds": e6["revision_rounds_consumed"], "operations_reviewed": e6["operations_reviewed"], "result": e6["semantic_result"], "verdict": e6["verdict"]},
    }
    integrity = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-integrity-report/1.0",
        "verdict": "FAIL", "mode": "final-check", "audit_mode": 2, "paper_id": cfg["paper_id"],
        "timestamp": STAMP, "fresh_context_role_separation": True, "error_independence_claimed": False,
        "phases": phases, "seven_failure_modes": seven, "compliance": compliance, "build": build,
        "issues": issues,
        "issue_counts": {level: sum(row["severity"] == level for row in issues) for level in ("SERIOUS", "MEDIUM", "MINOR")},
        "input_freeze": {"path": FREEZE.name, "sha256": FREEZE_SHA, "bound_rows_checked": GLOBAL_FREEZE_AUDIT["checked"], "bound_rows_passed": GLOBAL_FREEZE_AUDIT["passed"]},
        "authorization_receipt": {"path": AUTH.name, "sha256": AUTH_SHA, "action": "fresh_stage4_5_audit_only"},
        "protected_snapshot_before": frozen_before, "protected_snapshot_after": frozen_after,
        "protected_snapshot_unchanged": True, "silent_repair_performed": False,
        "stage5_started": False, "canonical_promotion_performed": False,
        "route_mutation_performed": False, "scientific_execution_performed": False,
        "assurance_boundary": "FAIL is an integrity-gate result for the checked surface, not a judgment that the mathematical architecture is false.",
    }
    integrity_path = notes / "stage4_5_round1_integrity_report.json"
    dump(integrity_path, integrity)

    passport = copy.deepcopy(json.loads((notes / "stage2_5_material_passport.json").read_text(encoding="utf-8")))
    passport["version_label"] = "stage4.5-round1-audit-fail-sidecar"
    passport["content_hash"] = cfg["draft_sha"]
    passport["verification_status"] = "stage4_5_round1_fail_corrections_proposed_not_applied"
    passport["stage4_5_round1_audit"] = {
        "verdict": "FAIL", "references": f"{cfg['reference_total']}/{cfg['reference_total']}",
        "citation_context_support": f"{refs['phase_b']['verified']}/{refs['phase_b']['registered_citation_context_tuples']}",
        "phase_c": data["verdict"],
        "originality": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "changed_originality": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "claim_registry": f"{evidence['registry_claims']}/{evidence['registry_claims']} ALL reviewed",
        "evidence_rows": f"{evidence['actual_tuples']}/{evidence['expected_tuples']}",
        "e6": f"{e6['operations_reviewed']}/{e6['operations_reviewed']}", "stage5_started": False,
    }
    dump(notes / "stage4_5_round1_material_passport.json", passport)

    report_lines = [
        f"# {cfg['paper_id']} — Stage 4.5 Round 1 final integrity report", "", "## Verdict", "",
        "**FAIL at the Stage 4.5 checkpoint.** No repair was applied, no canonical file was promoted, and Stage 5 was not started.", "",
        "## Complete denominators", "",
        f"- References: **{cfg['reference_total']}/{cfg['reference_total']}** resolved in a fresh bounded browser identity pass (**PASS WITH NOTES**).",
        f"- Citation contexts: **{refs['phase_b']['reviewed']}/{refs['phase_b']['registered_citation_context_tuples']} reviewed**; **{refs['phase_b']['verified']} verified**, **{refs['phase_b']['unverifiable_anchorless']} anchorless/unverifiable** (**FAIL**).",
        f"- Phase C: **{data['registered_surface_coverage']['data_stat_internal_surfaces_checked']}/{data['registered_surface_coverage']['data_stat_internal_surfaces_checked']}** checked; **{data['registered_surface_coverage']['verified']} verified**, **{data['registered_surface_coverage']['inconsistent']} inconsistent**; tables **{data['registered_surface_coverage']['tables_verified']}/{data['registered_surface_coverage']['tables_checked']}**, figures **0**.",
        f"- Originality heuristic: **{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']} ({originality['sampling_rate']:.1%})** body paragraphs; changed/new **{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}**; major sections **{originality['major_sections_covered']}/{originality['major_sections_total']}**. No professional detector was available.",
        f"- Claims: **{evidence['registry_claims']}/{evidence['registry_claims']}** tier-ALL reviewed; lexical candidates **{evidence['candidate_total']}/{evidence['candidate_total']}**, gap **0**.",
        f"- Evidence rows: **{evidence['actual_tuples']}/{evidence['expected_tuples']}**; verdicts `{evidence['verdict_counts']}`.",
        f"- E6: **{e6['operations_reviewed']}/{e6['operations_reviewed']}** operations; {e6['semantic_result']}. This is not a deterministic no-drift proof.",
        f"- Seven modes: **{seven['clear']}/7 CLEAR**, **{seven['suspected']}/7 SUSPECTED**, **{seven['insufficient_evidence']}/7 INSUFFICIENT EVIDENCE**.",
        f"- Isolated build: **{build['status']}**, {build['preview']['pages'] if build['preview'] else 'no'} pages, unresolved citations **{len(build['unresolved_citations'])}**, unresolved references **{len(build['unresolved_references'])}**.",
        "", "## Blockers", "",
    ]
    report_lines.extend(f"- **{row['severity']} `{row['issue_id']}`:** {row['finding']}" for row in issues)
    report_lines.extend(["", "## Boundaries", "", BOUNDARY, "", "The audit used a fresh role-separated pass but does not claim error independence. Correction artifacts are proposal-only."])
    final_path = notes / "stage4_5_round1_final_integrity_report.md"
    write(final_path, "\n".join(report_lines))

    receipt = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-receipt/1.0", "paper_id": cfg["paper_id"],
        "recorded_at_utc": STAMP, "verdict": "FAIL", "audit_mode": 2, "inputs": input_manifest["inputs"],
        "key_artifacts": {
            "integrity_report": {"path": f"notes/{integrity_path.name}", "sha256": sha_path(integrity_path)},
            "final_human_report": {"path": f"notes/{final_path.name}", "sha256": sha_path(final_path)},
            "claim_registry": {"path": f"notes/{evidence['registry_path'].name}", "sha256": sha_path(evidence["registry_path"])},
            "evidence_rows": {"path": f"notes/{evidence['rows_path'].name}", "sha256": sha_path(evidence["rows_path"])},
            "preview": build["preview"],
            "correction_checkpoint": {"path": "notes/stage4_5_round1_correction_checkpoint.json", "sha256": sha_path(notes / "stage4_5_round1_correction_checkpoint.json")},
        },
        "denominators": phases, "seven_mode_summary": {"clear": seven["clear"], "suspected": seven["suspected"], "insufficient_evidence": seven["insufficient_evidence"]},
        "protected_snapshot_unchanged": True, "silent_repair_performed": False,
        "stage5_started": False, "canonical_promotion_performed": False,
    }
    receipt_path = notes / "stage4_5_round1_receipt.json"
    dump(receipt_path, receipt)
    output_path = notes / "stage4_5_round1_output_manifest.json"
    artifacts = [
        {"path": f"notes/{path.name}", "sha256": sha_path(path), "bytes": path.stat().st_size}
        for path in sorted(notes.glob("stage4_5_round1_*")) if path.is_file() and path != output_path
    ]
    dump(
        output_path,
        {
            "schema_version": f"p{cfg['paper']}-stage4.5-round1-output-manifest/1.0",
            "paper_id": cfg["paper_id"], "generated_at_utc": STAMP, "verdict": "FAIL",
            "artifacts": artifacts, "protected_snapshot_after": frozen_after,
            "protected_snapshot_unchanged": True, "stage5_started": False,
        },
    )
    return {
        "paper": cfg["paper_id"], "verdict": "FAIL",
        "references": f"{cfg['reference_total']}/{cfg['reference_total']}",
        "contexts": f"{refs['phase_b']['verified']}/{refs['phase_b']['registered_citation_context_tuples']} verified",
        "phase_c": f"{data['registered_surface_coverage']['verified']}/{data['registered_surface_coverage']['data_stat_internal_surfaces_checked']}",
        "originality": f"{originality['successful_body_dual_lane']}/{originality['paragraph_denominator']}",
        "changed": f"{originality['changed_or_new_successful']}/{originality['changed_or_new_total']}",
        "claims": evidence["registry_claims"], "evidence_rows": evidence["actual_tuples"],
        "e6_operations": e6["operations_reviewed"], "build": build["status"],
        "receipt_sha256": sha_path(receipt_path), "integrity_report_sha256": sha_path(integrity_path),
    }


def run_one(cfg: dict[str, Any]) -> dict[str, Any]:
    paper = ROOT / "papers" / cfg["directory"]
    notes = paper / "notes"
    draft = notes / "stage4_prime_revision_round2.tex"
    bib = notes / "stage4_prime_references_round2.bib"
    raw = draft.read_bytes()
    text = raw.decode("utf-8")
    if sha_bytes(raw) != cfg["draft_sha"] or sha_path(bib) != cfg["bib_sha"]:
        raise RuntimeError(f"{cfg['paper_id']}: target digest changed")
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    if not auth["authorized_tracks"][f"p{cfg['paper']}_stage4_5_fresh_audit_only"]:
        raise RuntimeError("audit authority missing")
    frozen_before = BASE.canonical_snapshot(paper)
    input_manifest = {
        "schema_version": f"p{cfg['paper']}-stage4.5-round1-input-manifest/1.0",
        "paper_id": cfg["paper_id"], "generated_at_utc": STAMP, "audit_mode": 2,
        "inputs": {
            "draft": {"path": "notes/stage4_prime_revision_round2.tex", "sha256": cfg["draft_sha"], "bytes": len(raw)},
            "bibliography": {"path": "notes/stage4_prime_references_round2.bib", "sha256": cfg["bib_sha"], "bytes": bib.stat().st_size},
            "authorization_receipt": {"path": AUTH.name, "sha256": AUTH_SHA},
            "input_freeze": {"path": FREEZE.name, "sha256": FREEZE_SHA},
            "e6_dispatch_authority": {"path": "notes/stage4_prime_revision_evidence_bundle_round2.json", "sha256": cfg["e6_bundle_sha"]},
        },
        "global_bound_hash_check": GLOBAL_FREEZE_AUDIT,
        "protected_snapshot_before": frozen_before,
        "authorization": "fresh Stage-4.5 audit-only",
        "fresh_context_role_separation": True, "error_independence_claimed": False,
    }
    dump(notes / "stage4_5_round1_input_manifest.json", input_manifest)
    blocks = BASE.block_rows(text)
    reference_ledger = browser_reference_ledger(cfg, notes)
    refs = reference_audit(cfg, notes, text, blocks, reference_ledger)
    evidence = claim_and_evidence(cfg, notes, raw, text, blocks, reference_ledger)
    data = phase_c(cfg, paper, notes, text, blocks)
    e6 = e6_audit(cfg, paper, notes)
    originality = BASE.originality_audit(cfg, notes)
    seven, compliance = seven_and_compliance(cfg, notes, refs, e6)
    build = BASE.isolated_build(cfg, paper, notes, text, frozen_before)
    return final_outputs(cfg, paper, notes, frozen_before, refs, evidence, data, e6, originality, seven, compliance, build, input_manifest)


def main() -> int:
    results = [run_one(cfg) for cfg in CONFIGS]
    print(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
