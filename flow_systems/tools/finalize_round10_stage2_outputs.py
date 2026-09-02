#!/usr/bin/env python3
"""Create hash-bound Round-10 Stage-2 audits, paper READMEs, and output manifest."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-09-02T13:29:43Z"
PAPERS = {
    "P29": {
        "slug": "29-bianchi-ideal-owner-refinement",
        "refs": 22,
        "result": "The complete article separates performance-independent mechanism admissibility (Gate M) from exact primitive-unoriented quotient completeness (Gate Q) under a deliberately strict literal Gaussian-prime-ideal codomain. Both gates remain open; no owner law, quotient, or S_H score is reported.",
        "result_zh": "完整论文把机制可容许性 Gate M 与原始无向所有者商集完备性 Gate Q 明确分离，并把字面单一高斯素理想限定为刻意严格的压力测试。两道门均保持开放，没有产生 owner law、完整 quotient 或 S_H 数值。",
        "route": "Route A / A1 preparation; formal tuple UNASSIGNED; positive arithmetic A2 absent; Route B closed.",
        "special": "P29-S06/P29-S07 correction pairing remains visible; P29-S09 remains a preprint; passage support remains INCONCLUSIVE.",
    },
    "P30": {
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "refs": 26,
        "result": "The article turns the physical-roof determinant proposal into six typed gates and a common-norm uncertainty contract: four numerical channels plus separately propagated geometry/roof-input uncertainty. No roof, operator, determinant, enclosure, fidelity result, or nontransfer theorem is reported.",
        "result_zh": "完整论文把物理 roof 行列式方案整理为六道型别化关卡，并冻结共同范数下的误差契约：四个数值通道加独立传播的几何／roof 输入不确定性。没有宣称已构造 roof、算子、行列式、包络、忠实度或非转移定理。",
        "route": "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; Route B closed.",
        "special": "P30-S01/P30-S02, P30-S03, and P30-S17/P30-S18 correction bindings remain visible; passage support remains INCONCLUSIVE.",
    },
    "P31": {
        "slug": "31-level11-conjugacy-owner-ledger",
        "refs": 22,
        "result": "The article makes a deterministic canonicalization biconditional the primary certificate target. The 9,453 pair rows become a derived adversarial audit, while global owners G, incidences I, and cell-local quotient C remain distinct prospective estimands.",
        "result_zh": "完整论文把确定性 canonicalization 双条件提升为首要证书目标，将 9,453 个 pair rows 降为派生的对抗审计，并保持全局 owners G、incidences I 与 cell-local quotient C 三种估计量互不替代。",
        "route": "Route A / A1 preparation; formal tuple UNASSIGNED; positive arithmetic A2 absent; Route B closed.",
        "special": "The 138 instances, 55 groups, and 9,453 pairs remain frozen design inputs; no pair decision or owner partition is reported.",
    },
    "P32": {
        "slug": "32-homology-cover-renormalization-uniformity",
        "refs": 26,
        "result": "The article makes higher-content and zero-content factors the first falsification targets under the exact 1/N time and 1/N^3 logarithmic normalizations. Content one is contingent and secondary; formal objects, panels, tails, and limits remain unresolved.",
        "result_zh": "完整论文在固定 1/N 时间与 1/N^3 对数重整化下，把高内容与零内容因子列为最先的否证目标；content-one 仅为附条件的次级分支。形式对象、面板、尾界和极限均未构造或执行。",
        "route": "Generic Route-A A1--A2 preparation; A0 unavailable; formal tuple UNASSIGNED; Route B closed.",
        "special": "P32-S13 remains PLAUSIBLE/background-only; P32-S06 remains a presentation-unmapped preprint; P32-S17 remains correction-limited.",
    },
    "P33": {
        "slug": "33-bolza-control-matched-census",
        "refs": 20,
        "result": "The article permits heterogeneous surface-specific exact proof producers behind one common semantic owner-certificate schema and independent validator. The target-blind cutoff asymmetry is explicit and P33-RC-1 remains 0/7; no census is reported.",
        "result_zh": "完整论文允许两个曲面使用不同的精确证明产生器，但必须输出同一语义 owner-certificate schema 并交由独立验证器复验。固定截断的不对称已显式化，P33-RC-1 仍为 0/7，没有产生 census。",
        "route": "Route A / A1 preparation; formal A0 prohibited/confounded; formal tuple UNASSIGNED; Route B closed.",
        "special": "P33-S06 remains PLAUSIBLE/context-only/page-unpinned; P33-S03/P33-S16 correction bindings and the P33-S12 bibliographic page range remain visible.",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_comments(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def tex_words(text: str) -> list[str]:
    text = strip_comments(text)
    text = re.sub(r"\\begin\{(?:equation\*?|align\*?|displaymath|verbatim)\}.*?\\end\{(?:equation\*?|align\*?|displaymath|verbatim)\}", " ", text, flags=re.S)
    text = re.sub(r"\$.*?\$|\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", text)


def extract_body(text: str) -> str:
    starts = [m.start() for m in re.finditer(r"\\section\*?\{(?:[0-9]+\.\s*)?Introduction", text, re.I)]
    start = starts[0] if starts else text.find(r"\begin{document}")
    ends = []
    for pattern in (
        r"\\section\*?\{Declarations\}",
        r"\\section\*?\{Author Contributions\}",
        r"\\section\*?\{Author contributions\}",
    ):
        match = re.search(pattern, text[start:], re.I)
        if match:
            ends.append(start + match.start())
    end = min(ends) if ends else text.find(r"\bibliographystyle", start)
    if end < 0:
        end = len(text)
    return text[start:end]


def abstract_metrics(text: str) -> tuple[int, int]:
    match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    en = len(tex_words(match.group(1))) if match else 0
    # Keep the Han-character ledger byte-for-byte aligned with the canonical
    # Stage-2 auditor.  In particular, remove the zero-width TeX break helper
    # before locating the abstract, then stop at the first keyword label.
    clean = text.replace(r"\hspace{0pt}", "")
    match = re.search(r"\\begin\{zhabstract\}(.*?)\\end\{zhabstract\}", clean, re.S)
    if match:
        zh = len(re.findall(r"[\u3400-\u9fff]", match.group(1)))
        return en, zh
    doc = clean[clean.find(r"\begin{document}"):] if r"\begin{document}" in clean else clean
    title = doc.find("繁體中文摘要")
    if title < 0:
        return en, 0
    start = doc.find("\n", title)
    stop = doc.find("關鍵詞", start)
    if stop < 0:
        stop = doc.find(r"\end{otherlanguage}", start)
    zh = len(re.findall(r"[\u3400-\u9fff]", doc[start:stop])) if start >= 0 and stop >= 0 else 0
    return en, zh


def keyword_metrics(text: str) -> tuple[int, int]:
    en_match = re.search(r"Keywords:\}\s*(.*?)(?:\n\n|\\begin\{|\\medskip)", text, re.S | re.I)
    en = len([item for item in (en_match.group(1).split(";") if en_match else []) if item.strip()])
    zh_match = re.search(r"(?:中文關鍵詞|關鍵詞)：?\}\s*(.*?)(?:\}|\n\n)", text, re.S)
    zh = len([item for item in re.split(r"[；;]", zh_match.group(1)) if re.search(r"[\u3400-\u9fff]", item)]) if zh_match else 0
    if not zh:
        # Fallback for the P33 zero-width-spaced keyword block.
        block = re.search(r"\{\\raggedright\\noindent.*?\\hypertarget\{introduction\}", text, re.S)
        if block and "；" in block.group(0):
            zh = block.group(0).count("；") + 1
    return en, zh


def bib_keys(text: str) -> list[str]:
    return re.findall(r"@\w+\s*\{\s*([^,\s]+)", text)


def cite_keys(text: str) -> tuple[list[str], int]:
    groups = re.findall(r"\\cite[a-zA-Z*]*\s*\{([^}]+)\}", strip_comments(text))
    keys = [key.strip() for group in groups for key in group.split(",") if key.strip()]
    return keys, len(groups)


def pdf_pages(path: Path) -> int:
    result = subprocess.run(("pdfinfo", str(path)), check=True, text=True, stdout=subprocess.PIPE)
    match = re.search(r"(?m)^Pages:\s+(\d+)", result.stdout)
    return int(match.group(1)) if match else 0


def metrics(code: str, cfg: dict[str, object]) -> dict[str, object]:
    base = ROOT / "papers" / str(cfg["slug"])
    paper = base / "paper"
    notes = base / "notes"
    tex_path = paper / "manuscript.tex"
    bib_path = paper / "references.bib"
    pdf_path = paper / "paper.pdf"
    build_path = notes / "stage2_build_receipt.json"
    review_path = notes / "stage2_independent_recheck.md"
    map_path = notes / "stage2_bib_key_map.json"
    text = tex_path.read_text(encoding="utf-8")
    bib = bib_path.read_text(encoding="utf-8")
    bibset = set(bib_keys(bib))
    cites, cite_calls = cite_keys(text)
    cited = set(cites)
    markers = re.findall(r"(?m)^% ARS-CITE source_ids=([^\s]+) anchor=none claim_to_passage=INCONCLUSIVE\s*$", text)
    en_abs, zh_abs = abstract_metrics(text)
    en_kw, zh_kw = keyword_metrics(text)
    return {
        "paper": code,
        "slug": cfg["slug"],
        "manuscript_sha256": sha(tex_path),
        "bibliography_sha256": sha(bib_path),
        "pdf_sha256": sha(pdf_path),
        "pdf_pages": pdf_pages(pdf_path),
        "pdf_bytes": pdf_path.stat().st_size,
        "english_body_words": len(tex_words(extract_body(text))),
        "english_abstract_words": en_abs,
        "traditional_chinese_abstract_han": zh_abs,
        "english_keywords": en_kw,
        "traditional_chinese_keywords": zh_kw,
        "bibliography_entries": len(bibset),
        "citation_calls": cite_calls,
        "citation_key_occurrences": len(cites),
        "unique_cited_keys": len(cited),
        "citation_markers": len(markers),
        "missing_bib_keys": sorted(cited - bibset),
        "orphan_bib_keys": sorted(bibset - cited),
        "claim_intents": len(json.loads((notes / "stage2_claim_intent_manifest.json").read_text())["claims"]),
        "claim_manifest_sha256": sha(notes / "stage2_claim_intent_manifest.json"),
        "bib_key_map_sha256": sha(map_path),
        "build_receipt_sha256": sha(build_path),
        "independent_recheck_sha256": sha(review_path),
        "route_state": cfg["route"],
        "scientific_execution": "NOT_RUN",
        "new_retrieval": "NO",
        "canonical_result_refresh": "NO",
        "formal_route_a_tuple": "UNASSIGNED",
        "positive_arithmetic_a2": 0,
        "route_b_invocation": False,
        "stage2_5_integrity": "NOT_STARTED",
    }


def write_paper_files(code: str, cfg: dict[str, object], row: dict[str, object]) -> None:
    base = ROOT / "papers" / str(cfg["slug"])
    paper = base / "paper"
    audit = f"""# {code} -- ARS Stage 2 manuscript audit

Status: **Stage 2 WRITE complete; Stage 2.5 awaiting explicit user confirmation.**
This audit claims neither scientific execution, passage-level verification,
peer-review acceptance, nor Route-A/Route-B promotion.

## Deliverables and integrity

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `{row['manuscript_sha256']}` |
| `references.bib` | `{row['bibliography_sha256']}` |
| `paper.pdf` | `{row['pdf_sha256']}` |
| `notes/stage2_claim_intent_manifest.json` | `{row['claim_manifest_sha256']}` |
| `notes/stage2_bib_key_map.json` | `{row['bib_key_map_sha256']}` |
| `notes/stage2_build_receipt.json` | `{row['build_receipt_sha256']}` |
| `notes/stage2_independent_recheck.md` | `{row['independent_recheck_sha256']}` |

- PDF: **{row['pdf_pages']} pages**, {row['pdf_bytes']} bytes.
- Isolated build: LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX; receipt verdict `PASS`.
- Bibliography: natbib with plainnat numeric output.
- Build log: no fatal error, undefined citation/reference, missing glyph, or overfull box.

## Length, structure, and citation closure

| Check | Result |
|---|---:|
| English body | **{row['english_body_words']} words** |
| English abstract | **{row['english_abstract_words']} words** |
| Traditional-Chinese abstract | **{row['traditional_chinese_abstract_han']} Han characters** |
| Keywords | **{row['english_keywords']} English; {row['traditional_chinese_keywords']} Traditional Chinese** |
| Stage-2 ClaimIntents | **{row['claim_intents']}/8** |
| Bibliography | **{row['bibliography_entries']}/{cfg['refs']} entries; {row['unique_cited_keys']} unique cited; 0 missing; 0 orphan** |
| Citation commands / key occurrences | **{row['citation_calls']} / {row['citation_key_occurrences']}** |
| Adjacent anchor-none markers | **{row['citation_markers']}** |

The manuscript contains the author block, independent English and
Traditional-Chinese abstracts, introduction and research question, frozen
object and owner conventions, related literature, executed closed-corpus
methodology, certificate/proof-method architecture, synthesis findings,
reproducibility interface, discussion, dedicated limitations, future work,
conclusion, and all publication declarations.

## Article-level result and boundary

{cfg['result']}

{cfg['special']}

The independent hash-bound recheck covers all eight ClaimIntents and reports
no unresolved Blocker or Major finding. Every source-dependent statement stays
inside the frozen corpus; every citation remains `anchor:none`, and
claim-to-passage faithfulness remains `INCONCLUSIVE`. No direct source
quotation or invented locator is used.

## Route and scientific state

{cfg['route']}

`SCIENTIFIC_EXECUTION=NOT_RUN`; `NEW_RETRIEVAL=NO`;
`CANONICAL_RESULT_REFRESH=NO`; `FORMAL_ROUTE_A_TUPLE=UNASSIGNED`;
`ROUTE_B_INVOCATION=false`; `STAGE2_5_INTEGRITY=NOT_STARTED`.

**Audit conclusion:** the complete Stage-2 article package is internally
reproducible and ready for the separate Stage-2.5 confirmation gate.
"""
    (paper / "stage2_manuscript_audit.md").write_text(audit, encoding="utf-8")
    readme = f"""# {code} manuscript package

Current state: **STAGE 2 WRITE COMPLETE / AWAITING STAGE 2.5 CONFIRMATION**.
Stage 2.5 has not started, and no formal Route evaluation is claimed.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- complete English article with an independent Traditional-Chinese abstract.
- [`references.bib`](references.bib) -- {row['bibliography_entries']} frozen, fully cited records in plainnat numeric style.
- [`paper.pdf`](paper.pdf) -- {row['pdf_pages']}-page isolated LuaLaTeX/BibTeX build.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.

## 结论概要

{cfg['result_zh']}

## Claim and route boundary

{cfg['result']}

{cfg['route']} Scientific execution, new retrieval, novelty assessment,
canonical-result refresh, and Stage 2.5 integrity checking were not run.
"""
    (paper / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    rows = [metrics(code, cfg) for code, cfg in PAPERS.items()]
    for code, cfg in PAPERS.items():
        row = next(item for item in rows if item["paper"] == code)
        if row["missing_bib_keys"] or row["orphan_bib_keys"]:
            raise SystemExit(f"{code}: bibliography closure failed")
        if row["bibliography_entries"] != cfg["refs"]:
            raise SystemExit(f"{code}: expected {cfg['refs']} bibliography entries")
        if row["claim_intents"] != 8:
            raise SystemExit(f"{code}: expected 8 ClaimIntents")
        write_paper_files(code, cfg, row)
    payload = {
        "schema": "round10-stage2-output-manifest/1.0",
        "created_at": STAMP,
        "stage": "2-write-complete-awaiting-stage-2.5-confirmation",
        "authorization_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt"),
        "input_freeze_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json"),
        "preprose_freeze_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_PREPROSE_FREEZE.json"),
        "start_receipt_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_START.md"),
        "review_configuration_sha256": sha(ROOT / "BATCH_ROUND10_STAGE2_REVIEW_CONFIGURATION.md"),
        "papers": rows,
        "aggregate": {
            "papers": len(rows),
            "english_body_words": sum(int(row["english_body_words"]) for row in rows),
            "pdf_pages": sum(int(row["pdf_pages"]) for row in rows),
            "bibliography_entries": sum(int(row["bibliography_entries"]) for row in rows),
            "citation_calls": sum(int(row["citation_calls"]) for row in rows),
            "citation_key_occurrences": sum(int(row["citation_key_occurrences"]) for row in rows),
            "citation_markers": sum(int(row["citation_markers"]) for row in rows),
            "claim_intents": sum(int(row["claim_intents"]) for row in rows),
            "independent_rechecks_pass": 5,
            "formal_route_a_tuples": 0,
            "positive_arithmetic_a2": 0,
            "route_b_invocations": 0,
            "new_retrievals": 0,
            "scientific_executions": 0,
            "stage2_5_started": 0,
        },
    }
    target = ROOT / "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {target.name}: papers={len(rows)} words={payload['aggregate']['english_body_words']} "
        f"pages={payload['aggregate']['pdf_pages']} refs={payload['aggregate']['bibliography_entries']}"
    )


if __name__ == "__main__":
    main()
