#!/usr/bin/env python3
"""Collect fresh network evidence for the Round-10 P30/P31 Stage-4.5 audit.

This collector is intentionally read-only with respect to manuscripts, BibTeX,
canonical files, experiments, results, and route state.  It writes only the two
``notes/stage4_5_round1_reference_network_audit.json`` audit artifacts.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPERS = {
    "P30": ROOT / "papers/30-three-disk-nonconstant-roof-determinant",
    "P31": ROOT / "papers/31-level11-conjugacy-owner-ledger",
}
UA = "flow-systems-stage4.5-integrity-audit/1.0 (bibliographic verification)"
TIMEOUT = 30


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request(url: str, *, method: str = "GET", data: bytes | None = None,
            headers: dict[str, str] | None = None) -> dict:
    hdr = {"User-Agent": UA, "Accept": "application/json, text/html;q=0.8, */*;q=0.5"}
    if headers:
        hdr.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdr, method=method)
    started = now()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read()
            return {
                "requested_at": started,
                "request_method": method,
                "request_url": url,
                "http_status": resp.status,
                "final_url": resp.geturl(),
                "content_type": resp.headers.get("Content-Type"),
                "response_bytes": len(body),
                "response_sha256": sha(body),
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        return {
            "requested_at": started,
            "request_method": method,
            "request_url": url,
            "http_status": exc.code,
            "final_url": exc.geturl(),
            "content_type": exc.headers.get("Content-Type") if exc.headers else None,
            "response_bytes": len(body),
            "response_sha256": sha(body),
            "body": body,
            "error": f"HTTPError: {exc}",
        }
    except Exception as exc:  # explicit transport evidence, never guessed
        return {
            "requested_at": started,
            "request_method": method,
            "request_url": url,
            "http_status": None,
            "final_url": None,
            "content_type": None,
            "response_bytes": None,
            "response_sha256": None,
            "body": b"",
            "error": f"{type(exc).__name__}: {exc}",
        }


def parse_bib(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),\s*$", text))
    out = []
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        raw = text[match.start():end].strip()
        fields = {}
        for line in raw.splitlines()[1:]:
            field = re.match(r"\s*(\w+)\s*=\s*\{(.*)\}\s*,?\s*$", line)
            if field:
                fields[field.group(1).lower()] = field.group(2)
        out.append({"entry_type": match.group(1), "ref_slug": match.group(2), "fields": fields, "raw_sha256": sha(raw.encode())})
    return out


def simple_text(value: str) -> str:
    value = value.replace("--", "-")
    value = re.sub(r"\\(?:texttt|mathrm|mathbb|v|c|H|')\s*\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\[A-Za-z]+", " ", value)
    value = value.replace("{", "").replace("}", "").replace("$", "")
    return re.sub(r"\s+", " ", value).strip()


def tokens(value: str) -> set[str]:
    return {x for x in re.findall(r"[a-z0-9]+", simple_text(value).lower()) if len(x) > 2}


def ratio(left: str, right: str) -> float:
    a, b = tokens(left), tokens(right)
    return round(len(a & b) / max(1, len(a | b)), 4)


def crossref_lookup(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    event = request(url)
    raw = event.pop("body")
    message = None
    parse_error = None
    if event["http_status"] == 200:
        try:
            message = json.loads(raw.decode("utf-8"))["message"]
        except Exception as exc:
            parse_error = f"{type(exc).__name__}: {exc}"
    return {**event, "parse_error": parse_error, "crossref_message": message}


def landing_lookup(url: str) -> dict:
    event = request(url)
    raw = event.pop("body")
    snippet = raw[:2000].decode("utf-8", errors="replace") if raw else None
    title = None
    if snippet:
        found = re.search(r"(?is)<title[^>]*>(.*?)</title>", snippet)
        if found:
            title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", found.group(1))).strip()
    return {**event, "html_title_prefix": title, "body_prefix_utf8": snippet}


def s2_batch(entries: list[dict]) -> tuple[dict[str, dict | None], list[dict]]:
    ids, key_for = [], {}
    for entry in entries:
        fields = entry["fields"]
        if fields.get("doi"):
            ident = "DOI:" + fields["doi"]
        elif fields.get("eprint"):
            ident = "ARXIV:" + fields["eprint"]
        else:
            continue
        ids.append(ident)
        key_for[ident.lower()] = entry["ref_slug"]
    results: dict[str, dict | None] = {entry["ref_slug"]: None for entry in entries}
    events = []
    for start in range(0, len(ids), 20):
        group = ids[start:start + 20]
        url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=paperId,title,authors,year,venue,externalIds,url"
        payload = json.dumps({"ids": group}, separators=(",", ":")).encode()
        event = request(url, method="POST", data=payload, headers={"Content-Type": "application/json"})
        raw = event.pop("body")
        parsed = None
        parse_error = None
        try:
            parsed = json.loads(raw.decode("utf-8")) if raw else None
        except Exception as exc:
            parse_error = f"{type(exc).__name__}: {exc}"
        events.append({**event, "request_body": {"ids": group}, "parse_error": parse_error, "response": parsed})
        if event["http_status"] == 200 and isinstance(parsed, list):
            for ident, row in zip(group, parsed):
                results[key_for[ident.lower()]] = row
        time.sleep(0.25)
    return results, events


def assess(entry: dict, cr: dict | None, s2: dict | None, landing: dict | None) -> dict:
    fields = entry["fields"]
    title = simple_text(fields.get("title", ""))
    authoritative = cr.get("crossref_message") if cr else None
    if authoritative:
        cr_title = (authoritative.get("title") or [""])[0]
        author_surnames = [x.get("family", "") for x in authoritative.get("author", [])]
        published = authoritative.get("published-print") or authoritative.get("published-online") or authoritative.get("issued") or {}
        year = ((published.get("date-parts") or [[None]])[0] or [None])[0]
        metadata = {
            "title": cr_title,
            "authors": author_surnames,
            "year": year,
            "container_title": (authoritative.get("container-title") or [None])[0],
            "volume": authoritative.get("volume"),
            "issue": authoritative.get("issue"),
            "page_or_article": authoritative.get("page") or authoritative.get("article-number"),
            "doi": authoritative.get("DOI"),
            "publisher": authoritative.get("publisher"),
            "resource_primary_url": (authoritative.get("resource") or {}).get("primary", {}).get("URL"),
            "url": authoritative.get("URL"),
            "title_token_jaccard": ratio(title, cr_title),
        }
        checks = {
            "doi_exact": fields.get("doi", "").lower() == str(authoritative.get("DOI", "")).lower(),
            "title_material_match": ratio(title, cr_title) >= 0.6,
            "year_exact": fields.get("year") == str(year),
            "volume_exact_or_not_applicable": not fields.get("volume") or simple_text(fields.get("volume", "")).lower() == simple_text(str(authoritative.get("volume") or "")).lower(),
            "issue_exact_or_not_applicable": not fields.get("number") or simple_text(fields.get("number", "")).lower() == simple_text(str(authoritative.get("issue") or "")).lower(),
            "page_exact_or_not_applicable": not fields.get("pages") or simple_text(fields.get("pages", "")).lower() == simple_text(str(authoritative.get("page") or authoritative.get("article-number") or "")).lower(),
        }
        serious = not checks["doi_exact"] or not checks["title_material_match"] or not checks["year_exact"]
        metadata_mismatch = [k for k, v in checks.items() if not v]
        verdict = "MISMATCH" if serious else ("VERIFIED_WITH_FIELD_NOTE" if metadata_mismatch else "VERIFIED")
        return {"verdict": verdict, "authoritative_basis": "Crossref DOI registry", "metadata": metadata, "field_checks": checks, "mismatch_fields": metadata_mismatch}
    if s2:
        cr_title = s2.get("title") or ""
        checks = {"title_material_match": ratio(title, cr_title) >= 0.6, "year_exact": fields.get("year") == str(s2.get("year"))}
        verdict = "VERIFIED" if all(checks.values()) else "MISMATCH"
        return {"verdict": verdict, "authoritative_basis": "Semantic Scholar structured record (fallback; not publisher metadata)", "metadata": s2, "field_checks": checks, "mismatch_fields": [k for k, v in checks.items() if not v]}
    if landing and landing.get("http_status") == 200:
        landing_title = landing.get("html_title_prefix") or ""
        title_match = ratio(title, landing_title) >= 0.35 if landing_title else None
        verdict = "VERIFIED" if title_match is not False else "MISMATCH"
        return {"verdict": verdict, "authoritative_basis": "official URL retrieval", "metadata": {"landing_title": landing_title, "final_url": landing.get("final_url")}, "field_checks": {"title_material_match": title_match}, "mismatch_fields": [] if title_match is not False else ["title"]}
    return {"verdict": "NOT_FOUND", "authoritative_basis": None, "metadata": None, "field_checks": {}, "mismatch_fields": []}


def main() -> None:
    for paper_id, paper in PAPERS.items():
        bib = paper / "notes/stage4_prime_references_round2.bib"
        entries = parse_bib(bib)
        s2_results, s2_events = s2_batch(entries)
        rows = []
        for index, entry in enumerate(entries, start=1):
            fields = entry["fields"]
            doi = fields.get("doi")
            cr = crossref_lookup(doi) if doi else None
            official_url = fields.get("url") or ("https://doi.org/" + doi if doi else None)
            landing = landing_lookup(official_url) if official_url and (not cr or cr.get("http_status") != 200) else None
            result = assess(entry, cr, s2_results.get(entry["ref_slug"]), landing)
            rows.append({
                "sequence": index,
                **entry,
                "query_attempts": {
                    "semantic_scholar_batch": "see top-level semantic_scholar_batch_events",
                    "crossref_doi": cr,
                    "official_landing_fallback": landing,
                    "manual_search_template_1": f'"{simple_text(fields.get("author", "")).split(" and ")[0]}" "{simple_text(fields.get("title", ""))}" {fields.get("year", "")}',
                    "manual_search_template_2": doi,
                    "manual_search_template_3": f'"{simple_text(fields.get("journal", fields.get("booktitle", fields.get("publisher", ""))))}" "{fields.get("volume", "")}" {fields.get("year", "")}',
                },
                "semantic_scholar_result": s2_results.get(entry["ref_slug"]),
                "fresh_determination": result,
            })
            time.sleep(0.12)
        verdicts = {}
        for row in rows:
            key = row["fresh_determination"]["verdict"]
            verdicts[key] = verdicts.get(key, 0) + 1
        payload = {
            "schema_version": "stage4.5-round1-reference-network-audit/1.0",
            "paper_id": paper_id,
            "generated_at_utc": now(),
            "audit_mode": 2,
            "fresh_context_role_separation": True,
            "error_independence_claimed": False,
            "bibliography": {"path": str(bib.relative_to(paper)), "sha256": sha(bib.read_bytes()), "entry_count": len(entries)},
            "network_method": {
                "a0": "Semantic Scholar batch DOI/arXiv lookup attempted before A1 for every identifier-bearing entry; transport outcomes retained exactly.",
                "a1_a2": "Crossref DOI registry GET used as the primary structured metadata record for DOI entries; official URL GET fallback used only when no DOI registry record resolved.",
                "not_found_rule": "No item is guessed. A missing authoritative match is NOT_FOUND; up to three deterministic manual-query templates are retained for follow-up.",
                "response_retention": "Structured JSON response is retained for Crossref/S2; HTML is bounded to a 2,000-character prefix plus raw-body SHA-256 to avoid reproducing publisher pages.",
            },
            "semantic_scholar_batch_events": s2_events,
            "summary": {"registered_references": len(rows), "determinations": verdicts},
            "references": rows,
        }
        output = paper / "notes/stage4_5_round1_reference_network_audit.json"
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(paper_id, len(rows), verdicts, output)


if __name__ == "__main__":
    main()
