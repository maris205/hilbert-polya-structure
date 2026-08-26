# Compilation report / 编译报告

## Final result / 最终结果

- Engine: LuaLaTeX.
- Frozen environment: `SOURCE_DATE_EPOCH=1787673600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Final PDF: `paper/main.pdf`.
- Pages: 3.
- File size: 230,358 bytes.
- SHA-256: `5d236849a52afa5d54d7f9d6423020754bf9d0565bd4b8fb7215a4eb0f886e24`.
- Determinism: two final rebuilds produced the same SHA-256.
- `paper/main_round2.pdf` is byte-identical to `paper/main.pdf`.

最终 PDF 共 3 页；冻结环境下双次重建哈希一致，round 2 与 final 逐字节相同。

## Content snapshots / 内容快照

| Snapshot | SHA-256 | Material change |
|---|---|---|
| `main_round0_original.pdf` | `537f99ad425951d06819dc974839518cbd2fd276162f3c1879b344b107f2dde2` | Baseline theorem narrative. |
| `main_round1.pdf` | `15265c8841c4e441f92dff716c1c3f9f5ade9b2bd26672ce08aaaa7dc368ff70` | Full exceptional set, iid return coding, ownership and clock boundary. |
| `main_round2.pdf` | `5d236849a52afa5d54d7f9d6423020754bf9d0565bd4b8fb7215a4eb0f886e24` | Wold theorem, operator boundary, Route-A table, integrity language. |

The snapshots are content-distinct; no score or acceptance probability is attached.

三个快照内容不同；不附加虚构评分或接受概率。

## Final log audit / 最终日志审计

- LaTeX errors: 0.
- Warnings: 0.
- Undefined references: 0.
- Undefined citations: 0.
- Missing characters: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- `[VERIFY]`, `??`, and `[?]` markers in extracted PDF text: 0.

The round-0 CJK/Latin fallback warning was detected and fixed in round 1 by explicit language switching. It is absent from the final build.

基线中的 CJK/Latin 字体切换警告已在第一轮修复，最终日志无残留。

## Fonts and visual audit / 字体与视觉审计

`pdffonts` reports `emb=yes` for every font. All three pages were rendered at 130 dpi and inspected at original image detail. The title, bilingual abstract, equations, Route-A table, references, margins, and page numbers are visible without clipping, overlap, broken glyphs, or blank content.

全部字体嵌入；三页均已渲染检查，标题、双语摘要、公式、表格、参考文献、边距和页码均无裁切、重叠、坏字形或空白内容。

## Release boundary / 发布边界

The PDF is an exact source-side theory note. Compilation success does not certify global novelty, external peer approval, or Route-A acceptance.

编译成功只证明工件构建闭合，不代表全球新颖性、外部评审通过或 Route-A 接受。
