#!/usr/bin/env python3
"""Fresh P33 Stage 4.5 Round-2 originality transport collector.

This script is intentionally draft-bound and does not read the archived
ATTEMPT1_INVALID artifacts.  A query counts as executed only when Bing returns
HTTP 200, a non-empty body, and at least one parseable ``li.b_algo`` result
card.  It records transport/search evidence only; originality grades remain a
separate semantic audit.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


REPO = Path(__file__).resolve().parents[3]
PAPER = REPO / "papers/33-bolza-control-matched-census"
NOTES = PAPER / "notes"
DRAFT = NOTES / "stage4_prime_revision_round2.tex"
PATCHES = [
    NOTES / "stage4_revision_patch_round1.json",
    NOTES / "stage4_prime_revision_patch_round6_exact_confirmation.json",
]
OUTPUT = NOTES / "stage4_5_round2_originality_search_raw.json"

EXPECTED_DRAFT_SHA256 = "40ff6a91c311e7bdd01d6a37bfdd3bd351073311d7781bd4074f0975362e60ce"
AUTHORITY_LOCK_SHA256 = "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0"
AUTHORITY_RECEIPT_SHA256 = "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60"

# Closed body-paragraph population for the Mode-2 denominator.  Structural
# headings, tables/list containers, preamble, bibliography and declarations
# are excluded.  The two changed declaration blocks are nevertheless searched
# below as a conservative top-up beyond the body denominator.
BODY_BLOCK_IDS = """
B0007 B0010 B0014 B0015 B0017 B0018 B0019 B0020 B0022 B0025 B0026
B0027 B0029 B0030 B0032 B0033 B0034 B0036 B0037 B0127 B0040 B0041
B0043 B0044 B0045 B0047 B0050 B0051 B0052 B0053 B0055 B0057 B0058
B0059 B0061 B0062 B0128 B0064 B0066 B0067 B0069 B0070 B0071 B0072
B0073 B0074 B0077 B0079 B0081 B0082 B0084 B0087 B0088 B0090 B0091
B0093 B0095 B0098 B0100 B0102 B0103 B0105 B0106 B0107 B0108 B0109
B0110 B0112 B0113 B0115 B0116 B0117
""".split()

MANUAL_QUERIES = {
    "B0010": "本研究探討 兩個來源鎖定 緊緻虧格二雙曲曲面 精確憑證架構 原始閉測地線 所有權判定 動力學子型 單位速率 共同截斷值",
    "B0070": "Package B fixes owner semantics across producer boundary canonical digest full-group conjugacy",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_blocks(raw: str) -> dict[str, str]:
    pattern = re.compile(r"<!--block:(B[0-9]{4,})-->\n(.*?)(?=\n<!--block:|\Z)", re.S)
    blocks = {m.group(1): m.group(2).rstrip("\n") for m in pattern.finditer(raw)}
    if len(blocks) != 128:
        raise RuntimeError(f"expected 128 blocks, found {len(blocks)}")
    return blocks


def strip_tex(text: str) -> str:
    text = re.sub(r"(?m)^%.*$", " ", text)
    text = text.replace("~", " ")
    text = re.sub(r"\\hspace\{0pt\}", "", text)
    text = re.sub(r"\\(?:citep|citet)\{[^}]*\}", " ", text)
    text = re.sub(r"\\(?:path|url|texttt|textbf|emph)\{([^{}]*)\}", r" \1 ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("\\(", " ").replace("\\)", " ")
    text = text.replace("\\[", " ").replace("\\]", " ")
    text = re.sub(r"[{}$&]", " ", text)
    text = re.sub(r"\\[_%#]", " ", text)
    text = re.sub(r"\\", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def characteristic_sentence(block_id: str, block: str) -> str:
    clean = strip_tex(block)
    if block_id == "B0010":
        return clean
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if len(s.split()) >= 8]
    if not sentences:
        return clean

    def score(sentence: str) -> tuple[int, int]:
        tokens = sentence.split()
        proper = sum(1 for t in tokens[1:] if re.match(r"[A-Z][A-Za-z0-9_-]+", t))
        numeric = len(re.findall(r"\d|SHA-256|P33-|Route|Bolza|Nazarenko|fixture|validator", sentence))
        specificity = proper + 2 * numeric
        return specificity, min(len(tokens), 40)

    return max(sentences, key=score)


def exact_fragment(block_id: str, sentence: str) -> str:
    if block_id in MANUAL_QUERIES:
        tokens = MANUAL_QUERIES[block_id].split()
        if not 8 <= len(tokens) <= 12:
            raise RuntimeError("manual query must contain 8-12 whitespace tokens")
        return " ".join(tokens)
    tokens = [t.strip(".,;:!?()[]{}\"'`") for t in sentence.split()]
    tokens = [t for t in tokens if t]
    if len(tokens) < 8:
        raise RuntimeError(f"{block_id}: fewer than eight query tokens")
    window = min(12, len(tokens))
    # Prefer a window containing a proper noun, digit, or project identifier.
    best = tokens[:window]
    best_score = -1
    for i in range(0, len(tokens) - window + 1):
        candidate = tokens[i : i + window]
        joined = " ".join(candidate)
        score = len(re.findall(r"\d|[A-Z][A-Za-z]+|P33|Bolza|Route|SHA", joined))
        if score > best_score:
            best = candidate
            best_score = score
    return " ".join(best)


def unquoted_query(fragment: str) -> str:
    tokens = fragment.split()
    informative = [t for t in tokens if len(t) >= 4 or re.search(r"\d", t)]
    return " ".join((informative or tokens)[:10])


def parse_cards(html: bytes) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    cards: list[dict[str, str]] = []
    for li in soup.select("li.b_algo"):
        anchor = li.select_one("h2 a")
        if anchor is None or not anchor.get("href"):
            continue
        caption = li.select_one(".b_caption p")
        cards.append(
            {
                "title": anchor.get_text(" ", strip=True),
                "url": str(anchor.get("href")),
                "snippet": caption.get_text(" ", strip=True) if caption else "",
            }
        )
        if len(cards) == 10:
            break
    return cards


def search(session: requests.Session, query: str) -> dict:
    params = {
        "q": query,
        "setlang": "en-US",
        "cc": "US",
        "mkt": "en-US",
        "count": "10",
        "responseFilter": "Webpages",
    }
    url = "https://www.bing.com/search?" + urlencode(params)
    attempts: list[dict] = []
    for attempt in range(1, 4):
        started = time.monotonic()
        try:
            response = session.get(url, timeout=20)
            body = response.content
            cards = parse_cards(body) if response.status_code == 200 and body else []
            row = {
                "attempt": attempt,
                "http_status": response.status_code,
                "response_bytes": len(body),
                "response_sha256": sha256_bytes(body),
                "parseable_result_cards": len(cards),
                "elapsed_ms": round((time.monotonic() - started) * 1000),
            }
            attempts.append(row)
            if response.status_code == 200 and len(body) > 0 and cards:
                return {
                    "query": query,
                    "request_url": url,
                    "status": "EXECUTED_WITH_PARSEABLE_CARDS",
                    "attempts": attempts,
                    "result_cards": cards,
                }
        except requests.RequestException as exc:
            attempts.append(
                {
                    "attempt": attempt,
                    "transport_error": f"{type(exc).__name__}: {exc}",
                    "elapsed_ms": round((time.monotonic() - started) * 1000),
                }
            )
        time.sleep(1.0 * attempt)
    return {
        "query": query,
        "request_url": url,
        "status": "NOT_EXECUTED_NO_PARSEABLE_RESULT_CARDS",
        "attempts": attempts,
        "result_cards": [],
    }


def main() -> None:
    draft_bytes = DRAFT.read_bytes()
    if sha256_bytes(draft_bytes) != EXPECTED_DRAFT_SHA256:
        raise RuntimeError("draft SHA-256 mismatch")
    blocks = parse_blocks(draft_bytes.decode("utf-8"))

    changed_ops: list[dict] = []
    for patch_path in PATCHES:
        patch = json.loads(patch_path.read_text(encoding="utf-8"))
        for op in patch["ops"]:
            changed_ops.append(
                {
                    "revision_round": patch["revision_round"],
                    "block_id": op["block_id"],
                    "roadmap_item_ids": op["roadmap_item_ids"],
                }
            )
    changed_ids = list(dict.fromkeys(row["block_id"] for row in changed_ops))
    changed_body_ids = [block_id for block_id in changed_ids if block_id in BODY_BLOCK_IDS]
    extra_changed_ids = [block_id for block_id in changed_ids if block_id not in BODY_BLOCK_IDS]
    if len(changed_ops) != 50 or len(changed_ids) != 40:
        raise RuntimeError("expected 50 ops and 40 unique changed blocks")
    if len(BODY_BLOCK_IDS) != 72 or len(changed_body_ids) != 38:
        raise RuntimeError("unexpected originality denominator or changed-body count")

    selected = changed_body_ids + extra_changed_ids
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )

    started_at = utc_now()
    paragraph_rows = []
    for index, block_id in enumerate(selected, start=1):
        sentence = characteristic_sentence(block_id, blocks[block_id])
        if block_id not in MANUAL_QUERIES:
            usable = [t.strip(".,;:!?()[]{}\"'`") for t in sentence.split()]
            if len([t for t in usable if t]) < 8:
                sentence = strip_tex(blocks[block_id])
        fragment = exact_fragment(block_id, sentence)
        exact = search(session, f'"{fragment}"')
        supplement = search(session, unquoted_query(fragment))
        paragraph_rows.append(
            {
                "sample_index": index,
                "block_id": block_id,
                "in_body_denominator": block_id in BODY_BLOCK_IDS,
                "changed_in_rounds": sorted(
                    {row["revision_round"] for row in changed_ops if row["block_id"] == block_id}
                ),
                "characteristic_sentence": sentence,
                "exact_fragment": fragment,
                "exact_query": exact,
                "unquoted_query": supplement,
            }
        )
        print(
            f"{index:02d}/{len(selected)} {block_id} "
            f"exact={exact['status']} unquoted={supplement['status']}",
            flush=True,
        )

    author_queries = []
    for query in [
        '"Liang Wang" "Huazhong University of Science and Technology" primitive geodesic',
        '"wangliang.f@gmail.com" publication',
    ]:
        author_queries.append(search(session, query))

    completed_at = utc_now()
    all_queries = [
        query
        for row in paragraph_rows
        for query in (row["exact_query"], row["unquoted_query"])
    ] + author_queries
    executed = sum(q["status"] == "EXECUTED_WITH_PARSEABLE_CARDS" for q in all_queries)
    artifact = {
        "schema_version": "p33-stage4.5-round2-originality-search-raw/1.0",
        "paper_id": "P33",
        "mode": "MODE_2_FINAL_CHECK",
        "started_at_utc": started_at,
        "completed_at_utc": completed_at,
        "authority": {
            "input_lock_sha256": AUTHORITY_LOCK_SHA256,
            "authorization_receipt_sha256": AUTHORITY_RECEIPT_SHA256,
            "explicit_track_pass_received": True,
        },
        "draft": {
            "path": "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round2.tex",
            "sha256": EXPECTED_DRAFT_SHA256,
            "bytes": len(draft_bytes),
        },
        "attempt_boundary": {
            "archived_attempt": "ATTEMPT1_INVALID",
            "archived_attempt_reused": False,
        },
        "population": {
            "body_paragraphs": len(BODY_BLOCK_IDS),
            "changed_body_paragraphs": len(changed_body_ids),
            "changed_nonbody_prose_topups": len(extra_changed_ids),
            "sampled_body_paragraphs": len(changed_body_ids),
            "sampled_body_rate": len(changed_body_ids) / len(BODY_BLOCK_IDS),
            "changed_body_coverage_rate": 1.0,
            "sampled_total_rows": len(selected),
            "revision_rounds": 2,
            "revision_ops": len(changed_ops),
        },
        "search_contract": {
            "engine": "Bing public Web search HTML",
            "success_rule": "HTTP 200 AND non-empty body AND at least one parsed li.b_algo card",
            "http_200_empty_body_counts_as_success": False,
            "http_202_or_429_counts_as_success": False,
            "quoted_fragment_word_range": "8-12",
            "result_card_cap_per_query": 10,
            "heuristic_only": True,
            "professional_plagiarism_detector": False,
        },
        "paragraph_rows": paragraph_rows,
        "author_identity_queries": author_queries,
        "transport_summary": {
            "queries_total": len(all_queries),
            "queries_executed_with_parseable_cards": executed,
            "queries_not_executed": len(all_queries) - executed,
        },
    }
    OUTPUT.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
