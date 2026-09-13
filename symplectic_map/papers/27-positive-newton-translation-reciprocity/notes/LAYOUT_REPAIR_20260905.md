# Paper27 layout-only source revision

Status: DRAFT_PENDING_INDEPENDENT_SOURCE_EQUIVALENCE_REVIEW

Purpose: repair the actual overfull and custom-metadata failures recorded in LOCAL_BUILD_20260905_RESULT.md as the next bounded paper-compile correction. This is ordinary typesetting repair toward the existing paper goal, not a new mathematical scope, discarded review concern, or lower acceptance threshold.

Preserved original: `paper/main.tex`, SHA256 `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`.
Separate proposed source: `paper-layout-20260905/main.tex`, SHA256 `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`.
Auxiliary notation and bibliography remain the exact original `paper/math_commands.tex` and `paper/references.bib`; no source file or frozen lock is overwritten.

Exact change classes:

1. Add `\pdfsuppressptexinfo=1` after the document class. This suppresses the compiler Fullbanner metadata only; no PDF postprocessing or metadata stripping of an existing PDF occurs. The primitive's bit-1 meaning is documented by the [pdfTeX 1.40.17 release note](https://miktex.org/kb/pdftex-5900) and [TUG pdfTeX discussion](https://tug.org/pipermail/pdftex/2022-January/009271.html).
2. Split the displayed definitions of T_V/T_W and d_V/d_W into two gathered lines; symbols, sets, values and punctuation remain unchanged, apart from spacing commands and line breaks.
3. In the one target/reflected-target longtable, convert the twelve cell-local aligned environments to gathered environments, remove only their internal alignment tabs, and place the six `(b_1v',b_2v')` labels above their unchanged numeric values. Preserve all table-level `&` column separators, ID rows, captions, widths, data, carries and other content.

No font-size reduction, margin/spacing compression, padding, changed theorem quantifier, changed arithmetic, changed citation, or removed proof content is permitted. Original source/publication locks continue to certify their original hash; they are not silently rebound. The layout copy needs a separate, hash-bound equivalence/formatting review and then renewed actual build acceptance. Full proof/novelty/release claims are not inferred from a typesetting comparison.

The first derived draft briefly removed table-level alignment tabs; the author detected this in the immediate diff and corrected it before freezing the hash above or any review/build. No such draft was compiled. Review the actual final diff, not this statement alone.

No build has used this layout copy. Any approved build will have separately fixed new paths and a hash-bound prebuild decision; no old failed directory is retried or reused. This is correction attempt 2 of at most 3 in the bounded compilation workflow.
