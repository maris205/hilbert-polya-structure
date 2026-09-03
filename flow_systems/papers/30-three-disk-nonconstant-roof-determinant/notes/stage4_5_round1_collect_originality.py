#!/usr/bin/env python3
"""Fresh read-only Stage-4.5 originality census/search for Papers 30 and 31.

Only versioned ``stage4_5_round1_*`` audit sidecars are written.  A sampled
paragraph counts only when both the quoted-exact and supplementary lanes
return an auditable search-result summary.  Search/access failure is retained
as a limitation and is never converted into an originality finding.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[3]
CONFIGS = (
    {
        "paper_id": 30,
        "directory": "30-three-disk-nonconstant-roof-determinant",
        "draft_sha256": "6c09fa99b17a1f0d47a1c186f0fe48072a3f7d7e45b036a0b237460cd51ae39a",
        "body_start": "B0009",
        "body_end_exclusive": "B0119",
        "field_terms": "three disk physical roof transfer determinant",
    },
    {
        "paper_id": 31,
        "directory": "31-level11-conjugacy-owner-ledger",
        "draft_sha256": "2f71faeb4f7306f2475cd7cdb4f4fd692166f4a363eb1dfea3d11fd836eee9ea",
        "body_start": "B0011",
        "body_end_exclusive": "B0100",
        "field_terms": "Gamma0 11 canonical conjugacy owner certificate",
    },
)
UA = "Mozilla/5.0 (Round-10 Stage-4.5 originality integrity audit)"


def stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blocks(text: str) -> list[dict[str, Any]]:
    marks = list(re.finditer(r"(?m)^<!--block:(B\d{4})-->\s*$", text))
    output: list[dict[str, Any]] = []
    current_section = "front matter"
    for index, marker in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        block_text = text[marker.end() : end].strip()
        heading = re.search(r"\\section\*?\{([^{}]+)\}", block_text, flags=re.S)
        if heading:
            current_section = re.sub(r"\s+", " ", heading.group(1)).strip()
        output.append(
            {
                "block_id": marker.group(1),
                "text": block_text,
                "order": index,
                "section": current_section,
            }
        )
    return output


def visible_words(raw: str) -> list[str]:
    value = re.sub(r"(?m)%.*$", " ", raw)
    value = re.sub(r"\\(?:citep?|citet)(?:\[[^]]*\])?\{[^{}]*\}", " ", value)
    for _ in range(5):
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
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = value.replace("Livšic", "Livsic").replace("Gamma_0", "Gamma0")
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", value)


def is_paragraph(raw: str) -> bool:
    if re.match(
        r"\\begin\{(?:center|verbatim|enumerate|itemize|table|figure|equation|align)",
        raw,
    ):
        return False
    return len(visible_words(raw)) >= 25


def changed_blocks(notes: Path, current: list[dict[str, Any]]) -> tuple[set[str], list[dict[str, Any]]]:
    changed: set[str] = set()
    operations: list[dict[str, Any]] = []
    current_by_text = {row["text"].replace("\r\n", "\n").strip(): row["block_id"] for row in current}
    for round_number, name in (
        (1, "stage4_revision_patch_round1.json"),
        (2, "stage4_prime_revision_patch_round2.json"),
    ):
        payload = json.loads((notes / name).read_text(encoding="utf-8"))
        for op_index, op in enumerate(payload["ops"], start=1):
            kind = op["op"]
            if kind == "replace_block":
                current_id = op["block_id"]
            elif kind in {"insert_after", "insert_before"}:
                current_id = current_by_text.get(op["new_text"].replace("\r\n", "\n").strip())
            else:
                current_id = None
            if current_id:
                changed.add(current_id)
            operations.append(
                {
                    "revision_round": round_number,
                    "operation_index": op_index,
                    "operation": kind,
                    "roadmap_target_block_id": op["block_id"],
                    "current_block_id": current_id,
                    "current_paragraph_surface": bool(
                        current_id and is_paragraph(next(row["text"] for row in current if row["block_id"] == current_id))
                    ),
                }
            )
    return changed, operations


def parse_bing(raw: bytes) -> list[dict[str, str]]:
    soup = BeautifulSoup(raw, "html.parser")
    result: list[dict[str, str]] = []
    for item in soup.select("li.b_algo")[:3]:
        anchor = item.select_one("h2 a")
        if anchor is None:
            continue
        snippet = item.select_one(".b_caption p")
        result.append(
            {
                "title": anchor.get_text(" ", strip=True)[:240],
                "url": str(anchor.get("href") or ""),
                "snippet": snippet.get_text(" ", strip=True)[:500] if snippet else "",
            }
        )
    return result


def parse_duckduckgo(raw: bytes) -> list[dict[str, str]]:
    soup = BeautifulSoup(raw, "html.parser")
    result: list[dict[str, str]] = []
    for item in soup.select(".result")[:3]:
        anchor = item.select_one("a.result__a")
        if anchor is None:
            continue
        snippet = item.select_one(".result__snippet")
        result.append(
            {
                "title": anchor.get_text(" ", strip=True)[:240],
                "url": str(anchor.get("href") or ""),
                "snippet": snippet.get_text(" ", strip=True)[:500] if snippet else "",
            }
        )
    return result


def parse_google(raw: bytes) -> list[dict[str, str]]:
    soup = BeautifulSoup(raw, "html.parser")
    result: list[dict[str, str]] = []
    for heading in soup.select("h3"):
        anchor = heading.find_parent("a")
        if anchor is None:
            continue
        container = anchor.find_parent("div")
        summary = container.get_text(" ", strip=True) if container else ""
        result.append(
            {
                "title": heading.get_text(" ", strip=True)[:240],
                "url": str(anchor.get("href") or ""),
                "snippet": summary[:500],
            }
        )
        if len(result) == 3:
            break
    return result


def one_attempt(query: str, engine: str) -> dict[str, Any]:
    if engine == "Bing WebSearch":
        request_url = "https://www.bing.com/search?q=" + quote(query)
        parser = parse_bing
    elif engine == "DuckDuckGo HTML Search":
        request_url = "https://html.duckduckgo.com/html/?q=" + quote(query)
        parser = parse_duckduckgo
    else:
        request_url = "https://www.google.com/search?hl=en&num=5&q=" + quote(query)
        parser = parse_google
    requested_at = stamp()
    try:
        request = Request(request_url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.8"})
        with urlopen(request, timeout=35) as response:
            raw = response.read()
            status = response.status
            final_url = response.geturl()
        results = parser(raw)
        return {
            "engine": engine,
            "query": query,
            "requested_at": requested_at,
            "request_url": request_url,
            "final_url": final_url,
            "http_status": status,
            "response_bytes": len(raw),
            "response_sha256": sha(raw),
            "result_count_reviewed": len(results),
            "top_result_summary": results,
            "transport_status": "success" if status == 200 and results else "SEARCH_ACCESS_LIMITATION",
        }
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        return {
            "engine": engine,
            "query": query,
            "requested_at": requested_at,
            "request_url": request_url,
            "final_url": None,
            "http_status": getattr(error, "code", None),
            "response_bytes": 0,
            "response_sha256": None,
            "result_count_reviewed": 0,
            "top_result_summary": [],
            "transport_status": "SEARCH_ACCESS_LIMITATION",
            "error": f"{type(error).__name__}: {error}",
        }


def search_lane(fragment: str, field_terms: str, lane: str) -> dict[str, Any]:
    if lane == "quoted_exact":
        query = f'"{fragment}"'
    else:
        query = f'{fragment} "Liang Wang" {field_terms}'
    attempts = [one_attempt(query, "Bing WebSearch")]
    if attempts[-1]["transport_status"] != "success":
        attempts.append(one_attempt(query, "DuckDuckGo HTML Search"))
    if all(row["transport_status"] != "success" for row in attempts):
        attempts.append(one_attempt(query, "Google Web Search"))
    successful = next((row for row in attempts if row["transport_status"] == "success"), None)
    summaries = successful["top_result_summary"] if successful else []
    searchable = " ".join(f"{row['title']} {row['snippet']}" for row in summaries).casefold()
    return {
        "lane": lane,
        "query": query,
        "status": "success" if successful else "SEARCH_ACCESS_LIMITATION",
        "successful_engine": successful["engine"] if successful else None,
        "exact_fragment_in_returned_summary": fragment.casefold() in searchable if successful else None,
        "attempts": attempts,
    }


def run_paper(config: dict[str, Any]) -> dict[str, Any]:
    notes = ROOT / "papers" / config["directory"] / "notes"
    draft = notes / "stage4_prime_revision_round2.tex"
    raw = draft.read_bytes()
    if sha(raw) != config["draft_sha256"]:
        raise RuntimeError(f"P{config['paper_id']}: draft hash changed")
    text = raw.decode("utf-8")
    current = blocks(text)
    by_id = {row["block_id"]: row for row in current}
    body_start_order = by_id[config["body_start"]]["order"]
    body_end_order = by_id[config["body_end_exclusive"]]["order"]
    body = [
        row for row in current
        if body_start_order <= row["order"] < body_end_order and is_paragraph(row["text"])
    ]
    changed, revision_operations = changed_blocks(notes, current)
    changed_paragraphs = [row for row in current if row["block_id"] in changed and is_paragraph(row["text"])]

    # Systematic deterministic half-census, topped up with every changed/new
    # paragraph regardless of whether it lies in the body denominator.
    selected_ids = {row["block_id"] for index, row in enumerate(body) if index % 2 == 0}
    selected_ids.update(row["block_id"] for row in changed_paragraphs)
    for section in dict.fromkeys(row["section"] for row in body):
        selected_ids.add(next(row["block_id"] for row in body if row["section"] == section))
    minimum = math.ceil(len(body) / 2)
    for row in body:
        if len(selected_ids & {item["block_id"] for item in body}) >= minimum:
            break
        selected_ids.add(row["block_id"])
    selected = [row for row in current if row["block_id"] in selected_ids]

    samples: list[dict[str, Any]] = []
    for index, row in enumerate(selected, start=1):
        words = visible_words(row["text"])
        if len(words) < 8:
            raise RuntimeError(f"P{config['paper_id']} {row['block_id']}: insufficient visible words")
        # Start after boilerplate when possible, while retaining an exact
        # contiguous normalized 10-word sequence for reproducible searches.
        offset = min(4, max(0, len(words) // 6))
        fragment = " ".join(words[offset : offset + 10])
        if len(fragment.split()) < 8:
            fragment = " ".join(words[:10])
        samples.append(
            {
                "sample_id": f"P{config['paper_id']}-S45R1-D1-{index:03d}",
                "block_id": row["block_id"],
                "section": row["section"],
                "body_denominator_member": row in body,
                "stage4_or_stage4_prime_changed_surface": row["block_id"] in changed,
                "normalized_fragment": fragment,
                "word_count": len(fragment.split()),
            }
        )

    tasks: list[tuple[int, str]] = [
        (index, lane)
        for index in range(len(samples))
        for lane in ("quoted_exact", "unquoted_supplementary")
    ]
    results: dict[tuple[int, str], dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {
            executor.submit(
                search_lane,
                samples[index]["normalized_fragment"],
                config["field_terms"],
                lane,
            ): (index, lane)
            for index, lane in tasks
        }
        for future in as_completed(futures):
            results[futures[future]] = future.result()

    for index, sample in enumerate(samples):
        lanes = [results[(index, "quoted_exact")], results[(index, "unquoted_supplementary")]]
        sample["searches"] = lanes
        sample["dual_lane_success"] = all(row["status"] == "success" for row in lanes)
        sample["provisional_grade_from_returned_top_results"] = (
            "SEARCH_ACCESS_LIMITATION"
            if not sample["dual_lane_success"]
            else "POTENTIAL_MATCH_REQUIRES_SEMANTIC_REVIEW"
            if any(row["exact_fragment_in_returned_summary"] is True for row in lanes)
            else "NO_MATCH_IN_RECORDED_TOP_RESULT_SUMMARIES"
        )

    body_ids = {row["block_id"] for row in body}
    changed_ids = {row["block_id"] for row in changed_paragraphs}
    body_success = sum(row["dual_lane_success"] and row["block_id"] in body_ids for row in samples)
    changed_success = sum(row["dual_lane_success"] and row["block_id"] in changed_ids for row in samples)
    output = {
        "schema_version": f"p{config['paper_id']}-stage4.5-round1-originality-websearch-raw/1.0",
        "paper_id": config["paper_id"],
        "generated_at_utc": stamp(),
        "audit_scope": "fresh dual-lane public-Web paragraph originality heuristic plus changed/new-paragraph census",
        "draft": {
            "path": "notes/stage4_prime_revision_round2.tex",
            "sha256": sha(raw),
            "bytes": len(raw),
        },
        "paragraph_census_rule": (
            "Blocks in the body interval with at least 25 de-TeXed visible words; section/subsection/"
            "hypertarget-only blocks and center, verbatim, list, table, figure, equation, and align environments excluded."
        ),
        "paragraph_denominator": len(body),
        "body_paragraph_ids": [row["block_id"] for row in body],
        "sample_total": len(samples),
        "body_sample_total": sum(row["block_id"] in body_ids for row in samples),
        "major_body_sections": list(dict.fromkeys(row["section"] for row in body)),
        "major_body_sections_covered": list(
            dict.fromkeys(row["section"] for row in samples if row["block_id"] in body_ids)
        ),
        "successful_body_dual_lane_count": body_success,
        "successful_body_sampling_rate": body_success / len(body),
        "changed_or_new_paragraph_total": len(changed_paragraphs),
        "changed_or_new_paragraph_successful": changed_success,
        "changed_or_new_paragraph_coverage_rate": changed_success / len(changed_paragraphs),
        "revision_operation_census": revision_operations,
        "counting_rule": (
            "A paragraph counts only when both quoted_exact and unquoted_supplementary lanes return HTTP 200 "
            "and at least one auditable top-result summary through the recorded primary/fallback attempts. "
            "SEARCH_ACCESS_LIMITATION never counts and never implies originality."
        ),
        "professional_similarity_detector_used": False,
        "self_plagiarism_scope": (
            "The supplementary lane adds the named author and field terms to every sampled passage, and every changed/new passage is searched; "
            "this is a bounded public-Web heuristic, not a global same-author corpus comparison."
        ),
        "samples": samples,
    }
    out = notes / "stage4_5_round1_originality_search_raw.json"
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "paper": config["paper_id"],
        "output": str(out),
        "body": len(body),
        "body_success": body_success,
        "changed": len(changed_paragraphs),
        "changed_success": changed_success,
        "samples": len(samples),
    }


def main() -> int:
    print(json.dumps([run_paper(config) for config in CONFIGS], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
