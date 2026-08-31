#!/usr/bin/env python3
"""Run the fresh dual-lane Stage-4.5 originality WebSearch census for P28.

This script writes only a versioned audit sidecar.  It does not edit the
manuscript, bibliography, canonical results, receipts, or PDF.  A paragraph is
counted as successfully searched only when both its quoted exact-search lane
and its unquoted supplementary lane return HTTP 200 and at least one auditable
top-result summary.  Access failures are retained as limitations and are never
converted into ORIGINAL grades.
"""

from __future__ import annotations

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


NOTES = Path(__file__).resolve().parent
OUTPUT = NOTES / "stage4_5_round2_originality_search_raw.json"
DRAFT = NOTES / "stage4_prime_revision_round1.tex"
EXPECTED_DRAFT_SHA256 = (
    "126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e"
)
ENGINE = "Bing WebSearch"
ENGINE_URL = "https://www.bing.com/search?q="
USER_AGENT = "Mozilla/5.0 (P28 Stage-4.5 originality integrity audit)"


# Model-mediated paragraph census/sample frozen for the exact draft hash.
# Every fragment is 8--12 consecutive words after the documented de-TeX and
# punctuation normalization.  The five Stage-4/4-prime materially changed or
# newly inserted paragraph surfaces are all represented.
SAMPLES: tuple[tuple[str, str, str, bool], ...] = (
    ("B0013", "Introduction", "an exact determination from a polygonal presentation has two parts", False),
    ("B0015", "Introduction", "The global lower bound is established by a finite exact enumeration", False),
    ("B0017", "Introduction", "The enumeration is of canonical group elements and performs no quotient", False),
    ("B0016", "Introduction", "all group elements are reduced to canonical polynomial matrix states", False),
    ("B0025", "The source-locked genus-two octagon", "It binds four kinds of input that should not be conflated", False),
    ("B0027", "The source-locked genus-two octagon", "There are also two deliberately separate evidentiary layers", False),
    ("B0031", "The source-locked genus-two octagon", "the title can be verified without a decimal trace test", False),
    ("B0035", "Related exact-computation setting and claim boundary", "Algorithms for exact or certified work with Fuchsian groups have", False),
    ("B0037", "Related exact-computation setting and claim boundary", "The present scope is deliberately narrower than a surface-to-surface comparison", False),
    ("B0125", "Related exact-computation setting and claim boundary", "The present interface can be written as the typed map", True),
    ("B0041", "Exact polynomial normal forms", "After every multiplication the implementation cancels a common factor", False),
    ("B0043", "Exact polynomial normal forms", "Clearing powers turns equality of corresponding entries into polynomial identities", False),
    ("B0047", "Exact polynomial normal forms", "It is useful to make the state update more explicit", False),
    ("B0048", "Exact polynomial normal forms", "Three invariants are checked after each conceptual stage", True),
    ("B0127", "Exact polynomial normal forms", "The exact provenance pointer for these bounded assertions is", True),
    ("B0050", "Exact polynomial normal forms", "The representation is exact but not claimed to be an optimal normal", False),
    ("B0052", "Exact polynomial normal forms", "The same representation makes the prerequisite identities failure-closed", False),
    ("B0058", "Exact polynomial normal forms", "The alternating Taylor series gives rational lower and upper bounds", False),
    ("B0060", "From a length cutoff to a finite tile ball", "The search must contain at least one representative of every short", False),
    ("B0063", "From a length cutoff to a finite tile ball", "List in order the tiles whose interiors the segment crosses", False),
    ("B0068", "From a length cutoff to a finite tile ball", "A closed hyperbolic ball is compact so it contains only finitely", False),
    ("B0069", "From a length cutoff to a finite tile ball", "The wording identity-connected component is essential to the theorem", False),
    ("B0071", "From a length cutoff to a finite tile ball", "their freely reduced word lengths can grow without bound", False),
    ("B0072", "From a length cutoff to a finite tile ball", "The proof supplies exactly that theorem in two stages", False),
    ("B0073", "From a length cutoff to a finite tile ball", "Nor is the integer guard tuned to the observed state cloud", False),
    ("B0074", "From a length cutoff to a finite tile ball", "Every generator edge from every included state is classified", False),
    ("B0081", "The exact systole", "The exact finite execution described in this section exhausts the component", False),
    ("B0086", "The exact systole", "This distinction prevents the most tempting overinterpretation of the certificate", False),
    ("B0089", "Implementation and replayable certificate", "Every proof-decision branch in the implementation uses Python standard-library integer", False),
    ("B0091", "Implementation and replayable certificate", "Every potentially theorem-changing predicate is failure-closed at execution time", False),
    ("B0093", "Implementation and replayable certificate", "The evidence status is numerically certified by exhaustive finite execution", False),
    ("B0095", "Implementation and replayable certificate", "The shortest-discovery-depth histogram includes the identity and all states", False),
    ("B0096", "Implementation and replayable certificate", "Deterministic serialization makes accidental changes visible through exact digests", False),
    ("B0097", "Implementation and replayable certificate", "requires byte-identical trees and records the core-artifact hash", False),
    ("B0099", "Implementation and replayable certificate", "A successful replay has more obligations than reproducing the headline number", True),
    ("B0100", "Implementation and replayable certificate", "Semantic checks are performed before digest checks in the replay", False),
    ("B0101", "Implementation and replayable certificate", "artifact is compact rather than a dump of every large polynomial tuple", False),
    ("B0104", "Adversarial checks and Route-A interpretation", "a bounded word search could miss a short conjugate represented", False),
    ("B0105", "Adversarial checks and Route-A interpretation", "If the finite component contained many shortest elements that fact would not", False),
    ("B0106", "Adversarial checks and Route-A interpretation", "the result should be read as a control-side infrastructure theorem", False),
    ("B0126", "Adversarial checks and Route-A interpretation", "These labels name successive evidence obligations not levels of merit", True),
    ("B0109", "Limitations", "The theorem concerns one fixed parameter and no neighborhood theorem", False),
    ("B0112", "Limitations", "control-surface theorem not evidence of a magnetic universality mechanism", False),
    ("B0115", "Conclusion", "The central methodological outcome is the separation of geometry exact algebra", False),
)


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def fetch(fragment: str, lane: str) -> dict[str, Any]:
    if lane == "quoted_exact":
        query = f'"{fragment}"'
    elif lane == "unquoted_supplementary":
        query = f"{fragment} hyperbolic systole exact certificate"
    else:
        raise ValueError(lane)
    search_url = ENGINE_URL + quote(query)
    captured_at = now()
    try:
        request = Request(search_url, headers={"User-Agent": USER_AGENT})
        with urlopen(request, timeout=30) as response:
            raw = response.read()
            status = response.status
            final_url = response.geturl()
        soup = BeautifulSoup(raw, "html.parser")
        top_results: list[dict[str, str]] = []
        for item in soup.select("li.b_algo")[:3]:
            anchor = item.select_one("h2 a")
            snippet = item.select_one(".b_caption p")
            if anchor is None:
                continue
            top_results.append(
                {
                    "title": anchor.get_text(" ", strip=True)[:240],
                    "url": str(anchor.get("href") or ""),
                    "snippet": (
                        snippet.get_text(" ", strip=True)[:500]
                        if snippet is not None
                        else ""
                    ),
                }
            )
        searchable = " ".join(
            f"{row['title']} {row['snippet']}" for row in top_results
        ).casefold()
        exact_in_summary = fragment.casefold() in searchable
        success = status == 200 and bool(top_results)
        return {
            "lane": lane,
            "query": query,
            "engine": ENGINE,
            "captured_at": captured_at,
            "http_status": status,
            "transport_status": "success" if success else "SEARCH_ACCESS_LIMITATION",
            "requested_search_url": search_url,
            "final_search_url": final_url,
            "response_utf8_bytes": len(raw),
            "result_count_reviewed": len(top_results),
            "top_result_summary": top_results,
            "exact_fragment_in_returned_summary": exact_in_summary,
        }
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        return {
            "lane": lane,
            "query": query,
            "engine": ENGINE,
            "captured_at": captured_at,
            "http_status": getattr(error, "code", None),
            "transport_status": "SEARCH_ACCESS_LIMITATION",
            "requested_search_url": search_url,
            "final_search_url": None,
            "response_utf8_bytes": 0,
            "result_count_reviewed": 0,
            "top_result_summary": [],
            "exact_fragment_in_returned_summary": None,
            "error": f"{type(error).__name__}: {error}",
        }


def main() -> int:
    draft_raw = DRAFT.read_bytes()
    digest = hashlib.sha256(draft_raw).hexdigest()
    if digest != EXPECTED_DRAFT_SHA256:
        raise RuntimeError("draft hash changed; originality sampling is invalid")
    for block_id, _, fragment, _ in SAMPLES:
        count = len(fragment.split())
        if not 8 <= count <= 12:
            raise RuntimeError(f"{block_id}: fragment has {count} words")

    task_rows: list[tuple[int, str]] = []
    for index in range(len(SAMPLES)):
        task_rows.extend(((index, "quoted_exact"), (index, "unquoted_supplementary")))
    lane_results: dict[tuple[int, str], dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(fetch, SAMPLES[index][2], lane): (index, lane)
            for index, lane in task_rows
        }
        for future in as_completed(futures):
            index, lane = futures[future]
            lane_results[(index, lane)] = future.result()

    samples: list[dict[str, Any]] = []
    for index, (block_id, section, fragment, changed) in enumerate(SAMPLES):
        lanes = [
            lane_results[(index, "quoted_exact")],
            lane_results[(index, "unquoted_supplementary")],
        ]
        successful = all(row["transport_status"] == "success" for row in lanes)
        exact_hit = any(
            row["exact_fragment_in_returned_summary"] is True for row in lanes
        )
        if not successful:
            grade = "SEARCH_ACCESS_LIMITATION"
        elif exact_hit:
            grade = "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
        elif block_id == "B0068":
            grade = "COMMON_KNOWLEDGE"
        else:
            grade = "ORIGINAL"
        samples.append(
            {
                "sample_id": f"P28-S45R2-D1-{index + 1:02d}",
                "block_id": block_id,
                "section": section,
                "stage4_or_stage4_prime_changed_surface": changed,
                "normalized_fragment": fragment,
                "word_count": len(fragment.split()),
                "dual_lane_success": successful,
                "provisional_grade_from_returned_top_results": grade,
                "searches": lanes,
            }
        )

    successful_count = sum(row["dual_lane_success"] for row in samples)
    changed_rows = [
        row for row in samples if row["stage4_or_stage4_prime_changed_surface"]
    ]
    changed_successful = sum(row["dual_lane_success"] for row in changed_rows)
    output = {
        "schema": "p28-stage4.5-round2-originality-websearch-raw/1.0",
        "audit_scope": "fresh dual-lane public-Web originality search",
        "generated_at": now(),
        "draft_path": "notes/stage4_prime_revision_round1.tex",
        "draft_sha256": digest,
        "paragraph_denominator": 77,
        "sample_total": len(samples),
        "successful_search_count": successful_count,
        "sampling_rate": successful_count / 77,
        "changed_total": len(changed_rows),
        "changed_successful": changed_successful,
        "changed_coverage_rate": (
            changed_successful / len(changed_rows) if changed_rows else 0.0
        ),
        "counting_rule": (
            "A paragraph counts only when both quoted_exact and "
            "unquoted_supplementary lanes returned HTTP 200 and at least one "
            "auditable top-result summary. SEARCH_ACCESS_LIMITATION never "
            "counts and never implies ORIGINAL."
        ),
        "samples": samples,
    }
    OUTPUT.write_text(
        json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "sample_total": len(samples),
                "successful_search_count": successful_count,
                "sampling_rate": output["sampling_rate"],
                "changed_total": len(changed_rows),
                "changed_successful": changed_successful,
                "potential_match_rows": sum(
                    row["provisional_grade_from_returned_top_results"]
                    == "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
                    for row in samples
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
