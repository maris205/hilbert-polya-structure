#!/usr/bin/env python3
"""Freeze Round-10 Stage-2.5 originality samples and local overlap candidates.

The script is deterministic and performs no web retrieval. It selects at
least 30 percent of substantive body paragraphs per paper, guarantees every
numbered major section is represented, chooses one distinctive exact-search
fragment per selected paragraph, and exhaustively compares normalized local
scientific bodies at the eight-word threshold. Human/web adjudication is a
separate sidecar step.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = ROOT / "tools" / "round9_stage2_5_build_claim_artifacts.py"
PAPERS = [
    "29-bianchi-ideal-owner-refinement",
    "30-three-disk-nonconstant-roof-determinant",
    "31-level11-conjugacy-owner-ledger",
    "32-homology-cover-renormalization-uniformity",
    "33-bolza-control-matched-census",
]
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’-]*")
COMMAND_RE = re.compile(r"\\[A-Za-z@]+\*?")


def load_base():
    spec = importlib.util.spec_from_file_location("round10_originality_base", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {BASE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strip_tex_words(text: str) -> list[str]:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", text)
    text = re.sub(r"\\(?:cite\w*|label|ref|cref|url|href)\s*(?:\[[^]]*\])?\{[^}]*\}", " ", text)
    text = COMMAND_RE.sub(" ", text)
    text = text.replace("~", " ")
    return [word.lower().replace("’", "'") for word in WORD_RE.findall(text)]


def major_sections(text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    for match in re.finditer(r"\\section(?!\*)\{", text):
        cursor = match.end()
        depth = 1
        while cursor < len(text) and depth:
            if text[cursor] == "{":
                depth += 1
            elif text[cursor] == "}":
                depth -= 1
            cursor += 1
        raw = text[match.end() : cursor - 1]
        title = " ".join(strip_tex_words(raw)) or "unnamed section"
        rows.append((match.start(), title))
    return rows


def major_section_at(sections: list[tuple[int, str]], position: int) -> str:
    current = "front matter"
    for offset, title in sections:
        if offset > position:
            break
        current = title
    return current


def line_anchor(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def scientific_body_end(text: str) -> int:
    markers = (
        r"\section*{Declarations}",
        r"\section*{Author Contributions}",
        r"\section*{Author contributions}",
        r"\section*{Funding}",
        r"\section*{Competing Interests}",
        r"\section*{Data and Code Availability}",
        r"\section*{Data and code availability}",
        r"\section*{Data and Materials Availability}",
        r"\section*{AI Disclosure",
        r"\section*{AI-Assistance",
        r"\bibliographystyle",
    )
    positions = [text.find(marker) for marker in markers if text.find(marker) >= 0]
    return min(positions) if positions else len(text)


def body_rows(base: Any, paper: str) -> tuple[bytes, str, list[dict[str, Any]]]:
    path = ROOT / "papers" / paper / "paper" / "manuscript.tex"
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    sections = major_sections(text)
    if not sections:
        raise RuntimeError(f"{paper}: no numbered section")
    start = sections[0][0]
    end = scientific_body_end(text)
    rows: list[dict[str, Any]] = []
    for begin, finish, block in base.raw_paragraphs(text):
        if begin < start or begin >= end or base.in_excluded_region(text, begin):
            continue
        words = strip_tex_words(block)
        if not base.is_prose(block) or len(words) < 12:
            continue
        rows.append(
            {
                "start_char": begin,
                "end_char": finish,
                "line": line_anchor(text, begin),
                "major_section": major_section_at(sections, begin),
                "raw_text": block,
                "words": words,
            }
        )
    return raw, text, rows


def select_rows(raw: bytes, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    target = math.ceil(0.30 * len(rows))
    by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_section[row["major_section"]].append(row)
    selected: dict[int, dict[str, Any]] = {}
    for section_rows in by_section.values():
        row = min(section_rows, key=lambda item: item["line"])
        selected[row["line"]] = row
    ranked = sorted(
        rows,
        key=lambda row: hashlib.sha256(
            f"{sha256(raw)}:{row['line']}:round10-stage2.5-originality".encode()
        ).hexdigest(),
    )
    for row in ranked:
        if len(selected) >= target:
            break
        selected[row["line"]] = row
    return sorted(selected.values(), key=lambda item: item["line"])


def choose_fragment(words: list[str], document_frequency: Counter[str], docs: int) -> str:
    width = 10 if len(words) < 16 else 12
    best: tuple[float, int, list[str]] | None = None
    for index in range(0, len(words) - width + 1):
        window = words[index : index + width]
        if sum(len(word) >= 5 for word in window) < 4:
            continue
        score = sum(math.log((docs + 1) / (1 + document_frequency[word])) for word in window)
        candidate = (score, -index, window)
        if best is None or candidate > best:
            best = candidate
    if best is None:
        return " ".join(words[:width])
    return " ".join(best[2])


def longest_common_run(a: list[str], b: list[str], floor: int = 8) -> tuple[int, str]:
    if len(a) > len(b):
        a, b = b, a
    positions: dict[str, list[int]] = defaultdict(list)
    for index, word in enumerate(b):
        positions[word].append(index)
    best_len = 0
    best_start = 0
    previous: dict[int, int] = {}
    for i, word in enumerate(a):
        current: dict[int, int] = {}
        for j in positions.get(word, []):
            length = previous.get(j - 1, 0) + 1
            current[j] = length
            if length > best_len:
                best_len = length
                best_start = i - length + 1
        previous = current
    phrase = " ".join(a[best_start : best_start + best_len]) if best_len >= floor else ""
    return best_len, phrase


def existing_paper_body_words(base: Any, path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    sections = major_sections(text)
    if sections:
        start = sections[0][0]
    else:
        abstract_end = text.find(r"\end{abstract}")
        start = abstract_end + len(r"\end{abstract}") if abstract_end >= 0 else 0
    end = scientific_body_end(text)
    words: list[str] = []
    for begin, _, block in base.raw_paragraphs(text):
        if start <= begin < end and base.is_prose(block):
            words.extend(strip_tex_words(block))
    return words


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--paper",
        choices=("all", *PAPERS),
        default="all",
        help="write the sample for one paper only; the batch precommitment is unchanged",
    )
    args = parser.parse_args()
    selected_papers = PAPERS if args.paper == "all" else [args.paper]
    base = load_base()
    corpus: dict[str, tuple[bytes, str, list[dict[str, Any]]]] = {
        paper: body_rows(base, paper) for paper in PAPERS
    }
    all_rows = [row for _, _, rows in corpus.values() for row in rows]
    df: Counter[str] = Counter()
    for row in all_rows:
        df.update(set(row["words"]))

    summary: list[dict[str, Any]] = []
    for paper in selected_papers:
        raw, _, rows = corpus[paper]
        selected = select_rows(raw, rows)
        selected_rows = []
        for ordinal, row in enumerate(selected, start=1):
            selected_rows.append(
                {
                    "sample_id": f"{paper.split('-', 1)[0]}-D1-{ordinal:03d}",
                    "line": row["line"],
                    "major_section": row["major_section"],
                    "paragraph_sha256": sha256(row["raw_text"].encode("utf-8")),
                    "exact_search_fragment": choose_fragment(row["words"], df, len(all_rows)),
                    "search_status": "PENDING_WEBSEARCH",
                    "verdict": "PENDING",
                }
            )
        artifact = {
            "schema": "flow-systems-round10-stage2.5-originality-sample/1.0",
            "paper": paper,
            "manuscript_sha256": sha256(raw),
            "body_boundary": "first numbered section through last numbered section before declarations",
            "paragraph_rule": "double-newline prose blocks with at least 12 alphabetic words; declarations, Chinese duplicate abstract, pure markup, and tables excluded",
            "selection_rule": "every major numbered section represented, then deterministic SHA-256 rank to ceil(30 percent)",
            "body_paragraph_denominator": len(rows),
            "selected_paragraphs": len(selected_rows),
            "sampling_rate": round(len(selected_rows) / len(rows), 6),
            "professional_detector_used": False,
            "samples": selected_rows,
        }
        output = ROOT / "papers" / paper / "notes" / "stage2_5_originality_sample.json"
        output.write_text(json.dumps(artifact, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        summary.append(
            {
                "paper": paper,
                "denominator": len(rows),
                "selected": len(selected_rows),
                "sampling_rate": round(len(selected_rows) / len(rows), 6),
                "major_sections": sorted({row["major_section"] for row in rows}),
                "artifact": str(output.relative_to(ROOT)),
                "artifact_sha256": sha256(output.read_bytes()),
            }
        )

    overlaps = []
    normalized = {paper: [word for row in rows for word in row["words"]] for paper, (_, _, rows) in corpus.items()}
    for left_index, left in enumerate(PAPERS):
        for right in PAPERS[left_index + 1 :]:
            length, phrase = longest_common_run(normalized[left], normalized[right])
            overlaps.append(
                {
                    "left": left,
                    "right": right,
                    "maximum_exact_run_words": length,
                    "candidate_phrase_if_at_least_8": phrase,
                    "human_classification": "PENDING" if length >= 8 else "NO_OVERLAP_AT_THRESHOLD",
                }
            )
    prior_paths = []
    for path in sorted((ROOT / "papers").glob("*/paper/manuscript.tex")):
        try:
            number = int(path.parts[-3].split("-", 1)[0])
        except ValueError:
            continue
        if number < 29:
            prior_paths.append(path)
    prior_words = {str(path.relative_to(ROOT)): existing_paper_body_words(base, path) for path in prior_paths}
    prior_overlaps = []
    for paper in PAPERS:
        for path, words in prior_words.items():
            length, phrase = longest_common_run(normalized[paper], words)
            prior_overlaps.append(
                {
                    "round10_paper": paper,
                    "prior_manuscript": path,
                    "maximum_exact_run_words": length,
                    "candidate_phrase_if_at_least_8": phrase,
                    "human_classification": "PENDING" if length >= 8 else "NO_OVERLAP_AT_THRESHOLD",
                }
            )
    batch = {
        "schema": "flow-systems-round10-stage2.5-originality-precommitment/1.0",
        "papers": summary,
        "aggregate": {
            "paragraph_denominator": sum(row["denominator"] for row in summary),
            "selected": sum(row["selected"] for row in summary),
            "paper_pairs": len(overlaps),
            "prior_manuscripts": len(prior_paths),
            "round10_prior_pairs": len(prior_overlaps),
            "threshold_words": 8,
        },
        "local_pairwise_candidates": overlaps,
        "local_prior_corpus_candidates": prior_overlaps,
        "limitation": "Mechanical selection and local exact overlap only; WebSearch and human classification remain required, and this is not Turnitin or iThenticate.",
    }
    if args.paper == "all":
        output = ROOT / "BATCH_ROUND10_STAGE2_5_ORIGINALITY_PRECOMMITMENT.json"
        output.write_text(json.dumps(batch, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        print(json.dumps(batch["aggregate"], indent=2, sort_keys=True))
    else:
        print(json.dumps({"paper": args.paper, "sample": summary[0]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
