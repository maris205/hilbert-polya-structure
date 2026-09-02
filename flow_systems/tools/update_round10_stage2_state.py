#!/usr/bin/env python3
"""Update Round-10 paper/root README and pipeline-state surfaces after Stage 2."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINALIZER = ROOT / "tools" / "finalize_round10_stage2_outputs.py"
spec = importlib.util.spec_from_file_location("round10_finalizer", FINALIZER)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
PAPERS = module.PAPERS

NAMES = {
    "P29": "Bianchi ideal-owner refinement",
    "P30": "three-disk physical-roof determinant",
    "P31": "level-11 conjugacy owner ledger",
    "P32": "homology-cover renormalization uniformity",
    "P33": "Bolza/control certificate census",
}
SYSTEMS = {
    "P29": "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic arclength; primitive loxodromic inversion-paired owner; literal nonzero Gaussian prime ideal",
    "P30": "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from unit-roof control",
    "P31": "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers repetitions; Hecke degree distinct",
    "P32": "pure genus-two homology-cover tower H_N; all-content oriented primitive owners; exact 1/N time and 1/N^3 logarithmic normalization",
    "P33": "Bolza b=1/2 even subtype plus source-locked control; unit-speed physical base-geodesic time; inverse-paired owner; target-blind Lambda=21/10",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest_path = ROOT / "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows = {row["paper"]: row for row in manifest["papers"]}
    manifest_sha = sha(manifest_path)

    for code, cfg in PAPERS.items():
        base = ROOT / "papers" / cfg["slug"]
        row = rows[code]
        readme = f"""# Paper {code[1:]} -- {NAMES[code]}

## Current status

**ARS STAGE 2 WRITE COMPLETE / AWAITING EXPLICIT STAGE 2.5 CONFIRMATION.**
The complete manuscript, closed bibliography, compiled PDF, build receipt, and
independent recheck are present. Stage 2.5 has not started. No scientific
execution, new retrieval, novelty assessment, canonical-result refresh,
formal Route-A tuple, or Route-B invocation occurred during writing.

## Stage-2 paper package

- [complete manuscript](paper/manuscript.tex)
- [compiled PDF](paper/paper.pdf) -- {row['pdf_pages']} pages
- [closed bibliography](paper/references.bib) -- {row['bibliography_entries']} frozen records, all cited
- [manuscript audit](paper/stage2_manuscript_audit.md)
- [ClaimIntent manifest](notes/stage2_claim_intent_manifest.json) -- 8/8 inherited claims
- [independent recheck](notes/stage2_independent_recheck.md) -- PASS
- [isolated build receipt](notes/stage2_build_receipt.json) -- PASS

## 结论概要

{cfg['result_zh']}

The article-level result is methodological: {cfg['result']}

## Frozen dynamical system and route position

{SYSTEMS[code]}.

{cfg['route']} `SCIENTIFIC_EXECUTION=NOT_RUN`,
`FORMAL_ROUTE_A_TUPLE=UNASSIGNED`, `ROUTE_B_INVOCATION=false`, and
`STAGE2_5_INTEGRITY=NOT_STARTED`.

## Traceability

- Stage-1 handoff: `BATCH_ROUND10_STAGE1_HANDOFF_TO_STAGE2.md`
- Stage-2 input freeze: `BATCH_ROUND10_STAGE2_INPUT_FREEZE.json`
- Stage-2 output manifest SHA-256: `{manifest_sha}`
- Pipeline state: [notes/pipeline_state.md](notes/pipeline_state.md)

All detailed Stage-1 research, source, review, and revision artifacts remain
frozen in `notes/`; they were not replaced by this current-status summary.
"""
        (base / "README.md").write_text(readme, encoding="utf-8")

        state = f"""# {code} pipeline state

Date: **2026-09-02 UTC**

Current controlling state: **STAGE 2 WRITE COMPLETE / AWAITING EXPLICIT USER CONFIRMATION FOR STAGE 2.5**.

| Item | Status |
|---|---|
| Pipeline global state | `awaiting_confirmation` |
| ARS Stage 1 | `COMPLETE`; Phase-6 checkpoint and Stage-2 handoff frozen |
| ARS Stage 2 WRITE | `COMPLETE` |
| Stage-2 authorization | `CONFIRMED`; `BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt` |
| Stage-2 pre-prose registration | `COMPLETE`; 8/8 ClaimIntents, one-to-one same-or-narrower lineage |
| Manuscript | `COMPLETE`; {row['english_body_words']} audited English body words; SHA-256 `{row['manuscript_sha256']}` |
| Bibliography | `COMPLETE`; {row['bibliography_entries']} entries, all cited, no missing/orphan; SHA-256 `{row['bibliography_sha256']}` |
| PDF | `COMPLETE`; {row['pdf_pages']} pages, {row['pdf_bytes']} bytes; SHA-256 `{row['pdf_sha256']}` |
| Build receipt | `PASS`; `notes/stage2_build_receipt.json` |
| Independent recheck | `PASS`; 8/8 ClaimIntents; no unresolved Blocker, Major, or Minor; `notes/stage2_independent_recheck.md` |
| Explicit paper progress | {cfg['result']} |
| Frozen dynamical system | {SYSTEMS[code]} |
| New retrieval / scientific execution | `NO` / `NOT_RUN` |
| Canonical scientific-result refresh | `NO` |
| Novelty assessment | `NOT_RUN` |
| Formal Route-A tuple | `UNASSIGNED`; formal tuples `0`; positive arithmetic A2 `0` |
| Route position | {cfg['route']} |
| Route B | `CLOSED`; evaluation `NOT_RUN`; invocation `false` |
| Stage 2.5 integrity | `NOT_STARTED`; explicit user confirmation required |
| Next state | `AWAITING_EXPLICIT_USER_CONFIRMATION_FOR_STAGE_2_5` |
| Stage-2 output manifest | SHA-256 `{manifest_sha}` |

Stage-2 completion certifies a complete, buildable, closed-corpus article
package and its claim boundary. It does not certify theorem correctness,
passage-level support, novelty, scientific implementation, or route promotion.
"""
        (base / "notes" / "pipeline_state.md").write_text(state, encoding="utf-8")

    root_path = ROOT / "README.md"
    root = root_path.read_text(encoding="utf-8")
    new_row = (
        "| `29--33` — 五个同源但不同检验面的连续时间子型 | **Round 10 / Stage 2 WRITE 完成；等待 Stage 2.5 确认** | "
        "五篇完整论文共 66 页、23,182 个审计正文词、116 条冻结文献；40/40 ClaimIntents、5/5 独立复核、430/430 draft 审计及 543/543 full 审计通过。"
        "每篇都有明确的证书方法进展，但科学执行、正式 Route tuple 与 Route B 均为 0/5。见"
        "[Stage-2 output manifest](BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json)与"
        "[P29--P33 批次检查点](BATCH_ROUND10_STAGE2_CHECKPOINT.md)。 |"
    )
    root, count = re.subn(r"(?m)^\| `29--33` .*?$", new_row, root, count=1)
    if count != 1:
        raise SystemExit("could not replace root Round-10 index row")

    table_rows = []
    for code, cfg in PAPERS.items():
        row = rows[code]
        table_rows.append(
            f"| [{code}](papers/{cfg['slug']}/README.md) | {row['english_body_words']} | {row['pdf_pages']} | {row['bibliography_entries']} | {cfg['result_zh']} | {cfg['route']} |"
        )
    summary = f"""## Papers 29--33 Round 10 当前概要

Round 10 已完成 ARS **Stage 2 WRITE**，当前严格停在
**STAGE_2_WRITE_COMPLETE / AWAITING_EXPLICIT_USER_CONFIRMATION_FOR_STAGE_2_5**。
五篇完整、可编译的论文共 **23,182 个审计英文正文词、66 个 PDF 页面、116 条
冻结文献、114 个 citation commands 与 144 个 citation-key occurrences**。
40/40 Stage-2 ClaimIntents 全部一对一继承 Stage 1 且不增强；5/5 独立交叉复核
均为 PASS，当前无未决 Blocker、Major 或 Minor。Stage-2 deterministic draft
audit 为 **430/430 PASS**，包含五次 fresh isolated rebuild 的 full audit 为
**543/543 PASS**；五份 canonical PDF 均由隔离的
LuaLaTeX--BibTeX--LuaLaTeX--LuaLaTeX 构建链生成，终轮无 undefined
citations/references、missing glyph、overfull 或 underfull box。

| Paper | 正文词 | 页数 | 文献 | 本轮明确落地进展 | 路线图 A 对应 |
|---|---:|---:|---:|---|---|
{chr(10).join(table_rows)}

### 路线图与动力学限定

本轮仍在 **路线图 A 的 A0/A1 基础与 A2 前置证书层**，没有把写作完整性当作
科学晋级。五个冻结连续时间子型、clock、owner、normalization 和 cutoff 均保持
不变；本轮新增的是五篇完整论文，不是五次新科学实验。formal Route-A tuples
保持 `0/5`，正向算术 A2 保持 `0/5`，Route-B invocations 保持 `0/5`，
`SCIENTIFIC_EXECUTION=NOT_RUN` 为 `5/5`。

### 引用与完整性边界

116 条文献全部闭合且均被引用；所有 114 个 citation groups 都有相邻
`anchor=none / claim_to_passage=INCONCLUSIVE` 标记，没有伪造 locator 或直接来源
引文。P32-S13 与 P33-S06 的 `PLAUSIBLE` 特殊边界、全部 correction bindings、
作者信息、无资助、无利益冲突和 AI-assistance disclosure 均保留。Stage 2.5
尚未运行，因此 passage-level integrity、source finalization 与 formal claim
registration 均未被宣称。

下一步只需用户回复“确认”，即可进入 **Stage 2.5 pre-review integrity**；该确认
仍不授权新科学计算、canonical-result refresh、Route-A tuple 赋值或 Route B。
见 [Stage-2 output manifest](BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json)、
[Stage-2 checkpoint](BATCH_ROUND10_STAGE2_CHECKPOINT.md)与
[Stage-2.5 handoff](BATCH_ROUND10_STAGE2_HANDOFF_TO_STAGE2_5.md)。
"""
    root, count = re.subn(
        r"## Papers 29--33 Round 10 当前概要\n.*?(?=\n## Papers 24--28 最新结论)",
        summary.rstrip(),
        root,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("could not replace root Round-10 summary")
    root_path.write_text(root, encoding="utf-8")
    print(f"updated five paper README/state pairs and root README; output_manifest_sha256={manifest_sha}")


if __name__ == "__main__":
    main()
