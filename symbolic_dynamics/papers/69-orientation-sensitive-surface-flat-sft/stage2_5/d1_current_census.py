#!/usr/bin/env python3
"""Reproduce P69's current Phase-D1 paragraph census and selected sample.

A narrative unit is a blank-line-delimited block in ``sections/*.tex`` that
contains at least 20 alphabetic words after comments, sectioning commands,
cross-reference/citation commands, environment wrappers, TeX commands, math
punctuation, and digits are stripped.  This deliberately excludes headings,
display-only blocks, theorem labels without prose, and table-grid fragments.
The rule is local and auditable; it is not a plagiarism detector.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path


STAGE = Path(__file__).resolve().parent
SECTIONS = STAGE.parent / "sections"

QUERIES = [
    ("sections/0_abstract.tex", "Finite moment inversion shows that the two spectra jointly determine"),
    ("sections/1_introduction.tex", "This makes the topology of the corresponding finite covers available"),
    ("sections/1_introduction.tex", "Periodic data already recover a finite-group parameter in a distinct"),
    ("sections/1_introduction.tex", "this bibliographic choice does not alter historical ownership"),
    ("sections/1_introduction.tex", "The inverse step is a finite exponential-moment problem"),
    ("sections/2_background.tex", "This criterion will be important because it is the same"),
    ("sections/2_background.tex", "our chosen modern normalization source, we use Klug's account"),
    ("sections/2_background.tex", "We do not reprove this character calculation, and we make no"),
    ("sections/3_flat_shift.tex", "There are finitely many forbidden patterns on this set"),
    ("sections/3_flat_shift.tex", "Every connection has a unique based gauge transform whose labels"),
    ("sections/3_flat_shift.tex", "The full gauge group can have stabilizers governed by centralizers"),
    ("sections/4_subgroup_counts.tex", "We retain all positive moduli because both parities of the"),
    ("sections/4_subgroup_counts.tex", "This prevents the orientation comparison from being hidden in unrelated"),
    ("sections/5_moment_recovery.tex", "The reduced rational function on the right has simple poles"),
    ("sections/5_moment_recovery.tex", "When the bases are known, moments with nonnegative indices"),
    ("sections/5_moment_recovery.tex", "We use this standard finite-group expression at positive even integers"),
    ("sections/5_moment_recovery.tex", "The orientable moments alone cannot distinguish characters of equal degree"),
    ("sections/6_dihedral_quaternion.tex", "The two-dimensional indicators have opposite signs. This can be checked"),
    ("sections/6_dihedral_quaternion.tex", "separation holds at every odd level, not only at the first one"),
    ("sections/7_scope_controls.tex", "The residual proof sequence in this manuscript begins with the"),
    ("sections/7_scope_controls.tex", "This finite enumeration can detect normalization or parity regressions"),
    ("sections/7_scope_controls.tex", "That negative search is not a priority result"),
    ("sections/8_conclusion.tex", "The flat-connection SFT converts finite-index fixed points into raw flat"),
    ("sections/8_conclusion.tex", "Several boundaries are deliberate. The recovered signature is not a"),
]


def strip_comment(line: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", line)


def narrative_word_count(block: str) -> int:
    text = "\n".join(strip_comment(line) for line in block.splitlines())
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", text)
    text = re.sub(
        r"\\(?:section\*?|subsection\*?|subsubsection\*?|paragraph)\{[^}]*\}",
        " ",
        text,
    )
    text = re.sub(r"\\(?:citep|citet|cite|eqref|ref|cref|label)\{[^}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"[{}$\\_^&~#=+<>\[\]0-9]", " ", text)
    return len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", text))


def blocks(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    result = []
    active: list[str] = []
    start = 0
    for number, line in enumerate(lines + [""], start=1):
        if not line.strip() and active:
            text = "\n".join(active)
            count = narrative_word_count(text)
            if count >= 20:
                result.append(
                    {
                        "start_line": start,
                        "end_line": number - 1,
                        "alphabetic_words_after_normalization": count,
                        "normalized_whitespace": re.sub(r"\s+", " ", text).strip(),
                    }
                )
            active = []
        elif line.strip():
            if not active:
                start = number
            active.append(line)
    return result


def main() -> int:
    census = {}
    block_map = {}
    for path in sorted(SECTIONS.glob("*.tex")):
        relative = f"sections/{path.name}"
        held = blocks(path)
        census[relative] = len(held)
        block_map[relative] = held

    denominator = sum(census.values())
    selected = []
    for index, (relative, query) in enumerate(QUERIES, start=1):
        word_count = len(query.split())
        if not 8 <= word_count <= 12:
            raise RuntimeError(f"D{index:02d}: query has {word_count} words")
        hits = [item for item in block_map[relative] if query in item["normalized_whitespace"]]
        if len(hits) != 1:
            raise RuntimeError(f"D{index:02d}: expected one current narrative-unit hit, got {len(hits)}")
        hit = hits[0]
        selected.append(
            {
                "sample_id": f"D{index:02d}",
                "location": f"{relative}:{hit['start_line']}-{hit['end_line']}",
                "query": query,
                "query_words": word_count,
                "indexed_web_result": "NO_EXACT_MATCH_IN_INDEXED_WEB",
                "search_date": "2026-08-26",
            }
        )

    required = math.ceil(0.30 * denominator)
    represented = sorted({item["location"].split(":", 1)[0] for item in selected})
    expected_sections = sorted(census)
    if len(selected) < required or represented != expected_sections:
        raise RuntimeError("D1 sample floor or all-section coverage failed")

    output = {
        "schema_version": "p69-d1-current-census/1.0",
        "normalization_rule": (
            "Blank-line-delimited blocks with at least 20 alphabetic words after the "
            "documented TeX/comment normalization."
        ),
        "source_files_sha256": {
            relative: hashlib.sha256((STAGE.parent / relative).read_bytes()).hexdigest()
            for relative in expected_sections
        },
        "census_by_file": census,
        "denominator": denominator,
        "minimum_sample_ceiling_30_percent": required,
        "selected_count": len(selected),
        "selected_percent": round(100 * len(selected) / denominator, 4),
        "all_sections_represented": represented == expected_sections,
        "selected": selected,
        "search_boundary": (
            "General indexed-web exact-quote searches only; no proprietary similarity corpus."
        ),
        "verdict": "PASS_WITH_TOOL_LIMITATIONS",
    }
    target = STAGE / "d1_current_census.json"
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"P69 D1 census PASS_WITH_TOOL_LIMITATIONS: {len(selected)}/{denominator} "
        f"({output['selected_percent']:.4f}%), all {len(expected_sections)} section files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
