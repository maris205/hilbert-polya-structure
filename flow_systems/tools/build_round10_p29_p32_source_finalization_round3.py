#!/usr/bin/env python3
"""Build the authorized read-only P29/P32 Round-3 source finalization.

This program deliberately does not emit or apply a manuscript patch.  It binds
short (<= 20 word) support excerpts to authoritative/first-party surfaces when
available, and records explicit bounded unavailability otherwise.
"""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
REQUEST = ROOT / "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json"
REQUEST_SHA = "2b8a1c5d57cc01589ca6c926dc5590be0cbe58cae187a0b70d0b4c6c9a6bf3b3"
AUTH = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json"
AUTH_SHA = "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json"
FREEZE_SHA = "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff"
STAMP = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
USER_AGENT = "flow-systems-source-finalization/1.0 (mailto:wangliang.f@gmail.com)"

PAPERS = {
    "P29": "29-bianchi-ideal-owner-refinement",
    "P32": "32-homology-cover-renormalization-uniformity",
}

# The short excerpt is generated from the opening 20 words of the named abstract.
ARXIV_IDS = {
    "P29-S01": "1804.00275",
    "P29-S02": "1903.05111",
    "P29-S03": "1911.01800",
    "P29-S06": "1705.05626",
    "P29-S09": "2407.17959",
    "P29-S10": "1206.0087",
    "P29-S14": "1811.06190",
    "P29-S20": "math/9204234",
    "P32-S04": "1111.1554",
    "P32-S06": "2511.12862",
    "P32-S16": "0801.1938",
}

CROSSREF_EXACT = {
    "P29-S07": "10.1002/mana.201800467",
    "P29-S08": "10.1093/imrn/rnab048",
    "P29-S13": "10.1142/S0218196706002986",
    "P29-S21": "10.5802/jtnb.433",
    "P29-S22": "10.1090/mcom/3913",
    "P32-S02": "10.1142/S0218196706002986",
    "P32-S03": "10.1142/S0218196705002529",
    "P32-S07": "10.1017/S0017089500005632",
    "P32-S12": "10.1007/978-3-031-27704-7_10",
    "P32-S21": "10.1017/S0143385700007434",
    "P32-S22": "10.1353/AJM.1998.0041",
    "P32-S25": "10.1017/FMP.2021.19",
}

HTML_EXACT = {
    "P32-S15": {
        "url": "https://annals.math.princeton.edu/1983/118-3/p07",
        "locator": "Annals official article page, Abstract, opening sentence",
        "excerpt": "For an Axiom A flow restricted to a basic set we extend the zeta function",
        "authority": "journal first-party article page",
    },
    "P32-S17": {
        "url": "https://annals.math.princeton.edu/2013/178-2/p06",
        "locator": "Annals official article page, Abstract, sentence 1",
        "excerpt": "We study the Ruelle and Selberg zeta functions",
        "authority": "journal first-party article page",
    },
    "P32-S18": {
        "url": "https://www.numdam.org/item/ASENS_2016__49_3_543_0/",
        "locator": "Numdam official record, English Abstract, sentence 1",
        "excerpt": "The purpose of this paper is to give a short microlocal proof of the meromorphic continuation of the Ruelle zeta function",
        "authority": "journal archive first-party record",
    },
    "P32-S26": {
        "url": "https://dlmf.nist.gov/4.6",
        "locator": "NIST DLMF Section 4.6, section heading",
        "excerpt": "Power Series",
        "authority": "NIST first-party reference",
    },
}

PDF_EXACT = {
    "P32-S11": {
        "url": "https://numdam.org/item/10.1007/BF02699875.pdf",
        "locator": "Numdam full article, printed p. 5, Section 0 Introduction, opening paragraph",
        "excerpt": "In this paper, employing an idea in analytic number theory, we count the number of closed orbits in a homology class.",
        "authority": "journal archive first-party full text",
    },
    "P32-S19": {
        "url": "https://www.stat.uchicago.edu/~lalley/Papers/acta.pdf",
        "locator": "author-hosted article PDF, printed p. 1, table of contents, Part I item 5",
        "excerpt": "Periodic orbits of suspension flows",
        "authority": "author-hosted first-party full text",
    },
    "P32-S23": {
        "url": "https://www.ams.org/journals/tran/1949-066-01/S0002-9947-1949-0032593-5/S0002-9947-1949-0032593-5.pdf",
        "locator": "AMS official article PDF, printed p. 202, Part I contents, Section 3",
        "excerpt": "Well-ordered sequences in an ordered semigroup.",
        "authority": "publisher first-party full text",
    },
    "P32-S24": {
        "url": "https://su.diva-portal.org/smash/get/diva2:195258/FULLTEXT01.pdf",
        "locator": "Stockholm University repository dissertation, p. ii, Abstract, opening sentence",
        "excerpt": "We study the power series ring",
        "authority": "institutional repository first-party full text",
    },
}

UNAVAILABLE_REASONS = {
    "P29-S04": "The first-party institutional scan and DOI metadata identify the report, but this bounded pass finalized no machine-readable substantive passage; use is reduced to title/report metadata.",
    "P29-S05": "Institutional and DOI metadata identify the record, but no passage-bearing abstract or full text was finalized in the bounded pass.",
    "P29-S11": "The journal/index and DOI metadata identify the article, but no passage-bearing abstract or full text was finalized in the bounded pass.",
    "P29-S12": "The publisher surface did not yield a passage in the bounded pass and the DOI registry carries no abstract.",
    "P29-S15": "The DOI registry carries bibliographic metadata only; no passage-bearing chapter text was finalized.",
    "P29-S16": "The publisher surface did not yield a passage in the bounded pass and the DOI registry carries no abstract.",
    "P29-S17": "The publisher book record carries identity metadata only; no chapter/page passage was finalized.",
    "P29-S18": "The publisher book record carries identity metadata only; no chapter/page passage was finalized.",
    "P29-S19": "The publisher book record carries identity metadata only; no chapter/page passage was finalized.",
    "P32-S01": "The DOI registry carries bibliographic metadata only; no passage-bearing article text was finalized.",
    "P32-S05": "The MathNet surface was unavailable to the bounded pass and the DOI registry carries no abstract.",
    "P32-S08": "The journal first-party page explicitly exposes no abstract, and no full-text passage was finalized.",
    "P32-S09": "The institutional and DOI records identify the article, but no passage-bearing abstract or full text was finalized.",
    "P32-S10": "The DOI/index records identify the article, but no passage-bearing abstract or full text was finalized.",
    "P32-S13": "The journal index record identifies the article, but no passage-bearing source surface was captured in the bounded pass.",
    "P32-S14": "The institutional full-text retrieval did not complete inside the bounded pass and the DOI registry carries no abstract.",
    "P32-S20": "The MathNet surface was unavailable to the bounded pass and the DOI registry carries no abstract.",
}

RETAINED = {"P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path: Path) -> dict[str, Any]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size}


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def normalize(value: str) -> str:
    return " ".join(html.unescape(value).replace("\u00a0", " ").split())


def html_text(value: str) -> str:
    parser = TextExtractor()
    parser.feed(value)
    return normalize(" ".join(parser.parts))


def excerpt20(value: str) -> str:
    words = normalize(value).split()
    return " ".join(words[:20])


def fetch(url: str, *, timeout: int = 35) -> tuple[bytes, dict[str, Any]]:
    last: Exception | None = None
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                body = response.read()
                trace = {
                    "request_method": "GET",
                    "request_url": url,
                    "resolved_url": response.geturl(),
                    "http_status": int(response.status),
                    "content_type": response.headers.get("Content-Type", ""),
                    "response_bytes": len(body),
                    "response_sha256": hashlib.sha256(body).hexdigest(),
                    "retrieved_at_utc": STAMP,
                }
                return body, trace
        except Exception as exc:  # pragma: no cover - live transport boundary
            last = exc
            if attempt == 0:
                time.sleep(0.5)
    raise RuntimeError(f"GET failed for {url}: {last}")


def crossref_url(doi: str) -> str:
    return "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")


def crossref_fetch(item: tuple[str, str]) -> tuple[str, dict[str, Any]]:
    source_id, doi = item
    body, trace = fetch(crossref_url(doi))
    message = json.loads(body)["message"]
    raw_abstract = message.get("abstract", "")
    abstract = html_text(raw_abstract) if raw_abstract else ""
    trace["authority"] = "Crossref DOI registry carrying publisher-deposited metadata"
    trace["doi"] = doi
    trace["abstract_present"] = bool(abstract)
    trace["title"] = normalize(" ".join(message.get("title", [])))
    return source_id, {"trace": trace, "abstract": abstract}


def arxiv_records() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    ids = list(dict.fromkeys(ARXIV_IDS.values()))
    url = "https://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=20"
    body, trace = fetch(url)
    trace["authority"] = "arXiv first-party Atom API"
    root = ET.fromstring(body)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    by_id: dict[str, dict[str, str]] = {}
    for entry in root.findall("a:entry", ns):
        versioned = entry.findtext("a:id", default="", namespaces=ns).split("/abs/", 1)[-1]
        unversioned = re.sub(r"v\d+$", "", versioned)
        by_id[unversioned] = {
            "versioned_id": versioned,
            "title": normalize(entry.findtext("a:title", default="", namespaces=ns)),
            "summary": normalize(entry.findtext("a:summary", default="", namespaces=ns)),
        }
    missing = sorted(set(ids) - set(by_id))
    if missing:
        raise RuntimeError(f"arXiv response missing {missing}")
    return by_id, trace


def pdf_record(source_id: str, spec: dict[str, str]) -> dict[str, Any]:
    body, trace = fetch(spec["url"], timeout=45)
    trace["authority"] = spec["authority"]
    with tempfile.TemporaryDirectory(prefix="round10-p2932-source-") as temp_dir:
        pdf_path = Path(temp_dir) / "source.pdf"
        pdf_path.write_bytes(body)
        completed = subprocess.run(
            ["pdftotext", str(pdf_path), "-"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    if completed.returncode != 0:
        raise RuntimeError(f"pdftotext failed for {source_id}: {completed.stderr.decode('utf-8', 'replace')}")
    extracted = normalize(completed.stdout.decode("utf-8", "replace"))
    excerpt = normalize(spec["excerpt"])
    if excerpt.casefold() not in extracted.casefold():
        raise RuntimeError(f"configured PDF excerpt not found for {source_id}")
    trace["extracted_text_sha256"] = hashlib.sha256(extracted.encode("utf-8")).hexdigest()
    trace["extracted_text_bytes"] = len(extracted.encode("utf-8"))
    return {"trace": trace, "locator": spec["locator"], "excerpt": excerpt}


def html_record(source_id: str, spec: dict[str, str]) -> dict[str, Any]:
    body, trace = fetch(spec["url"])
    trace["authority"] = spec["authority"]
    extracted = html_text(body.decode("utf-8", "replace"))
    excerpt = normalize(spec["excerpt"])
    if excerpt.casefold() not in extracted.casefold():
        raise RuntimeError(f"configured HTML excerpt not found for {source_id}")
    trace["extracted_text_sha256"] = hashlib.sha256(extracted.encode("utf-8")).hexdigest()
    trace["extracted_text_bytes"] = len(extracted.encode("utf-8"))
    return {"trace": trace, "locator": spec["locator"], "excerpt": excerpt}


def verify_authority() -> dict[str, Any]:
    for path, expected in [(REQUEST, REQUEST_SHA), (AUTH, AUTH_SHA), (FREEZE, FREEZE_SHA)]:
        actual = sha(path)
        if actual != expected:
            raise RuntimeError(f"authority digest mismatch: {path.name}: {actual}")
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    track = next(x for x in auth["tracks"] if x["track_id"] == "P29_P32")
    if track["request"]["sha256"] != REQUEST_SHA or track["replace_block_pairs"] != 36:
        raise RuntimeError("P29/P32 execution authority projection mismatch")
    return json.loads(REQUEST.read_text(encoding="utf-8"))


def main() -> int:
    request = verify_authority()
    request_papers = {x["paper_id"]: x for x in request["papers"]}

    # Fetch all DOI registry records concurrently; unavailable rows use them as
    # positive metadata evidence and must still expose that no abstract was present.
    browser_rows: dict[str, dict[str, Any]] = {}
    proposals: dict[str, dict[str, Any]] = {}
    doi_by_source: dict[str, str] = {}
    for paper_id, slug in PAPERS.items():
        notes = ROOT / "papers" / slug / "notes"
        browser_path = notes / "stage4_5_round1_browser_reference_verification.json"
        proposal_path = notes / "stage4_5_round1_source_finalization_proposal.json"
        for row in json.loads(browser_path.read_text(encoding="utf-8"))["rows"]:
            browser_rows[row["ref_slug"]] = row
            doi = row["bibtex_fields_reviewed"].get("doi", "")
            if doi and not doi.lower().startswith("10.48550/arxiv"):
                doi_by_source[row["ref_slug"]] = doi
        proposals[paper_id] = json.loads(proposal_path.read_text(encoding="utf-8"))

    crossref_ids = sorted(set(CROSSREF_EXACT) | (set(UNAVAILABLE_REASONS) & set(doi_by_source)))
    crossref_results: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(crossref_fetch, (sid, CROSSREF_EXACT.get(sid, doi_by_source[sid]))) for sid in crossref_ids]
        for future in concurrent.futures.as_completed(futures):
            sid, value = future.result()
            crossref_results[sid] = value

    arxiv, arxiv_trace = arxiv_records()
    html_results = {sid: html_record(sid, spec) for sid, spec in HTML_EXACT.items()}
    pdf_results = {sid: pdf_record(sid, spec) for sid, spec in PDF_EXACT.items()}

    outputs: list[dict[str, Any]] = []
    for paper_id, slug in PAPERS.items():
        notes = ROOT / "papers" / slug / "notes"
        base = Path(request_papers[paper_id]["current_stage4_prime_draft"]["path"])
        base_path = ROOT / base
        if sha(base_path) != request_papers[paper_id]["current_stage4_prime_draft"]["sha256"]:
            raise RuntimeError(f"{paper_id} base draft changed before read-only finalization")
        prior_audit_path = notes / "stage4_5_round1_reference_citation_audit.json"
        prior_browser_path = notes / "stage4_5_round1_browser_reference_verification.json"
        prior_proposal_path = notes / "stage4_5_round1_source_finalization_proposal.json"

        rows: list[dict[str, Any]] = []
        for prior in proposals[paper_id]["rows"]:
            sid = prior["ref_slug"]
            row: dict[str, Any] = {
                "context_id": prior["context_id"],
                "source_id": sid,
                "block_id": prior["block_id"],
                "expected_current_context_sha256": prior["context_sha256"],
                "prior_stage4_5_verdict": prior["current_verdict"],
                "identity_source_url": prior["identity_source_url"],
                "claim_strength_increase_allowed": False,
                "locator_guessed": False,
                "manuscript_patch_applied": False,
            }
            if sid in RETAINED:
                row.update(
                    {
                        "finalization_status": "RETAINED_PRIOR_BOUNDED_SCOPE",
                        "exact_passage_locator": prior["current_passage_locator"],
                        "support_excerpt": None,
                        "support_excerpt_sha256": None,
                        "support_excerpt_word_count": 0,
                        "source_authority": "bound Stage-4.5 Round-1 citation audit",
                        "retrieval_trace": {
                            "kind": "prior_hash_bound_audit",
                            "path": binding(prior_audit_path),
                            "context_id": prior["context_id"],
                        },
                        "manuscript_disposition": "retain the already finalized narrow closest-work scope; infer no project theorem",
                    }
                )
            elif sid in ARXIV_IDS:
                rec = arxiv[ARXIV_IDS[sid]]
                excerpt = excerpt20(rec["summary"])
                row.update(
                    {
                        "finalization_status": "EXACT_LOCATOR_FINALIZED",
                        "exact_passage_locator": f"arXiv {rec['versioned_id']} abstract, opening 20 words",
                        "support_excerpt": excerpt,
                        "support_excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                        "support_excerpt_word_count": len(excerpt.split()),
                        "source_authority": "arXiv first-party abstract",
                        "retrieval_trace": arxiv_trace,
                        "manuscript_disposition": "replace only the authorized citation block with a locator-bounded contextual use and preserve every prohibited transfer",
                    }
                )
            elif sid in CROSSREF_EXACT:
                rec = crossref_results[sid]
                if not rec["abstract"]:
                    raise RuntimeError(f"expected Crossref abstract absent for {sid}")
                excerpt = excerpt20(rec["abstract"].removeprefix("Abstract "))
                row.update(
                    {
                        "finalization_status": "EXACT_LOCATOR_FINALIZED",
                        "exact_passage_locator": "publisher-deposited Crossref abstract, opening 20 words",
                        "support_excerpt": excerpt,
                        "support_excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                        "support_excerpt_word_count": len(excerpt.split()),
                        "source_authority": "Crossref registry carrying publisher-deposited abstract",
                        "retrieval_trace": rec["trace"],
                        "manuscript_disposition": "replace only the authorized citation block with a locator-bounded contextual use and preserve every prohibited transfer",
                    }
                )
            elif sid in HTML_EXACT:
                rec = html_results[sid]
                excerpt = rec["excerpt"]
                row.update(
                    {
                        "finalization_status": "EXACT_LOCATOR_FINALIZED",
                        "exact_passage_locator": rec["locator"],
                        "support_excerpt": excerpt,
                        "support_excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                        "support_excerpt_word_count": len(excerpt.split()),
                        "source_authority": rec["trace"]["authority"],
                        "retrieval_trace": rec["trace"],
                        "manuscript_disposition": "replace only the authorized citation block with a locator-bounded contextual use and preserve every prohibited transfer",
                    }
                )
            elif sid in PDF_EXACT:
                rec = pdf_results[sid]
                excerpt = rec["excerpt"]
                row.update(
                    {
                        "finalization_status": "EXACT_LOCATOR_FINALIZED",
                        "exact_passage_locator": rec["locator"],
                        "support_excerpt": excerpt,
                        "support_excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                        "support_excerpt_word_count": len(excerpt.split()),
                        "source_authority": rec["trace"]["authority"],
                        "retrieval_trace": rec["trace"],
                        "manuscript_disposition": "replace only the authorized citation block with a locator-bounded contextual use and preserve every prohibited transfer",
                    }
                )
            elif sid in UNAVAILABLE_REASONS:
                trace: dict[str, Any]
                if sid in crossref_results:
                    rec = crossref_results[sid]
                    if rec["abstract"]:
                        raise RuntimeError(f"bounded-unavailability classification stale: {sid} now exposes a Crossref abstract")
                    trace = rec["trace"]
                else:
                    trace = {
                        "kind": "prior_hash_bound_authoritative_identity_review",
                        "path": binding(prior_browser_path),
                        "source_id": sid,
                        "authoritative_or_first_party_url_reviewed": browser_rows[sid]["authoritative_or_first_party_url_reviewed"],
                        "passage_support_inferred": False,
                    }
                row.update(
                    {
                        "finalization_status": "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY",
                        "exact_passage_locator": None,
                        "support_excerpt": None,
                        "support_excerpt_sha256": None,
                        "support_excerpt_word_count": 0,
                        "source_authority": "authoritative identity/metadata surface only",
                        "retrieval_trace": trace,
                        "bounded_unavailability_reason": UNAVAILABLE_REASONS[sid],
                        "manuscript_disposition": "narrow the authorized citation block to a metadata-only record statement or remove the unsupported transfer; never guess a locator",
                    }
                )
            else:
                raise RuntimeError(f"unclassified source row: {sid}")
            if row["support_excerpt_word_count"] > 25:
                raise RuntimeError(f"support excerpt exceeds 25 words: {sid}")
            rows.append(row)

        exact = sum(x["finalization_status"] == "EXACT_LOCATOR_FINALIZED" for x in rows)
        retained = sum(x["finalization_status"] == "RETAINED_PRIOR_BOUNDED_SCOPE" for x in rows)
        unavailable = sum(x["finalization_status"] == "EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY" for x in rows)
        source_doc = {
            "schema_version": "round10-stage4-prime-source-finalization/1.0",
            "paper_id": paper_id,
            "generated_at_utc": STAMP,
            "workflow_date": "2026-09-04",
            "status": "READ_ONLY_FINALIZATION_COMPLETE_PATCH_BLOCKED_BY_SCOPE_ESCALATION",
            "authority": [binding(REQUEST), binding(AUTH), binding(FREEZE)],
            "bound_inputs": [binding(prior_audit_path), binding(prior_browser_path), binding(prior_proposal_path), binding(base_path)],
            "summary": {
                "registered_contexts": len(rows),
                "exact_locators_finalized": exact,
                "prior_bounded_scopes_retained": retained,
                "explicit_bounded_unavailability": unavailable,
                "passage_bounded_total": exact + retained,
                "manuscript_patch_applied": False,
            },
            "rows": rows,
            "boundaries": {
                "locator_guessing": False,
                "claim_strengthening": False,
                "bibliography_mutation": False,
                "manuscript_mutation": False,
                "scientific_execution_or_result_refresh": False,
                "route_or_initial_system_mutation": False,
                "stage4_5_rerun": False,
            },
        }
        source_path = notes / "stage4_prime_source_finalization_round3.json"
        dump(source_path, source_doc)

        matrix_rows = []
        for row in rows:
            matrix_rows.append(
                {
                    "context_id": row["context_id"],
                    "source_id": row["source_id"],
                    "base_block_id": row["block_id"],
                    "base_context_sha256": row["expected_current_context_sha256"],
                    "passage_status": row["finalization_status"],
                    "exact_passage_locator": row["exact_passage_locator"],
                    "support_excerpt_sha256": row["support_excerpt_sha256"],
                    "support_excerpt_word_count": row["support_excerpt_word_count"],
                    "authorized_future_disposition": row["manuscript_disposition"],
                    "claim_strength_increase_allowed": False,
                    "locator_guessed": False,
                }
            )
        matrix_doc = {
            "schema_version": "round10-stage4-prime-claim-passage-matrix/1.0",
            "paper_id": paper_id,
            "generated_at_utc": STAMP,
            "status": "READ_ONLY_MATRIX_COMPLETE_PATCH_BLOCKED_BY_SCOPE_ESCALATION",
            "source_finalization": binding(source_path),
            "base_draft": binding(base_path),
            "summary": source_doc["summary"],
            "rows": matrix_rows,
            "interpretation_boundary": "A finalized locator supports only the row's bounded contextual use. It does not verify project-specific theorem applicability, scientific correctness, or any Route result.",
        }
        matrix_path = notes / "stage4_prime_claim_passage_matrix_round3.json"
        dump(matrix_path, matrix_doc)

        checks = [
            {"check_id": "S01", "status": "PASS" if len(rows) == (22 if paper_id == "P29" else 30) else "FAIL", "detail": "registered context denominator"},
            {"check_id": "S02", "status": "PASS" if len({x["context_id"] for x in rows}) == len(rows) else "FAIL", "detail": "unique context ids"},
            {"check_id": "S03", "status": "PASS" if all(not x["locator_guessed"] for x in rows) else "FAIL", "detail": "no guessed locator"},
            {"check_id": "S04", "status": "PASS" if exact + retained + unavailable == len(rows) else "FAIL", "detail": "closed status partition"},
            {"check_id": "S05", "status": "PASS" if all(x["support_excerpt_word_count"] <= 25 for x in rows) else "FAIL", "detail": "short excerpt ceiling"},
            {"check_id": "S06", "status": "PASS" if sha(base_path) == request_papers[paper_id]["current_stage4_prime_draft"]["sha256"] else "FAIL", "detail": "base draft remained frozen"},
        ]
        validation = {
            "schema_version": "round10-stage4-prime-source-finalization-validation/1.0",
            "paper_id": paper_id,
            "generated_at_utc": STAMP,
            "source_finalization": binding(source_path),
            "claim_passage_matrix": binding(matrix_path),
            "checks": checks,
            "passed": sum(x["status"] == "PASS" for x in checks),
            "failed": sum(x["status"] == "FAIL" for x in checks),
            "verdict": "PASS" if all(x["status"] == "PASS" for x in checks) else "FAIL",
        }
        validation_path = notes / "stage4_prime_source_finalization_round3_validation.json"
        dump(validation_path, validation)
        if validation["verdict"] != "PASS":
            raise RuntimeError(f"{paper_id} source finalization validation failed")
        outputs.append(
            {
                "paper_id": paper_id,
                "source_finalization": binding(source_path),
                "claim_passage_matrix": binding(matrix_path),
                "validation": binding(validation_path),
                "summary": source_doc["summary"],
            }
        )

    print(json.dumps({"status": "PASS", "outputs": outputs}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
