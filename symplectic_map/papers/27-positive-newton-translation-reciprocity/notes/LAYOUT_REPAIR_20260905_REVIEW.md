# Independent layout-source equivalence review

Decision: **PASS** — source/typesetting equivalence only, bound to the exact hashes below.

Reviewed on 2026-09-05. The complete actual unified diff, both source files, and `notes/LAYOUT_REPAIR_20260905.md` were inspected. The note's narrative was not used as a substitute for checking the sources.

- Preserved original: `paper/main.tex`
  - SHA-256: `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`
- Reviewed layout copy: `paper-layout-20260905/main.tex`
  - SHA-256: `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`

## Exact checks

A read-only Perl check reconstructed the entire proposed source from the original with the following finite transformations and then required byte-for-byte equality with the proposed source:

1. Insert exactly one `\pdfsuppressptexinfo=1` line immediately after `\documentclass[11pt]{article}`. No other preamble or metadata-related source change occurs.
2. Replace exactly the displayed `T_V`, `T_W`, `d_V`, `d_W` definitions with the inspected two-line `gathered` version. Only the environment wrapper, one line break, whitespace, and `\quad`/`\qquad` placement change.
3. Within the body of the single target/reflected-target table, replace exactly twelve cell-local `aligned` environments with `gathered`, remove exactly 54 cell-internal alignment tabs, and insert exactly six line breaks between the `(b_1v',b_2v')` labels and their equals signs. No transformation is applied to table-level alignment tabs.

The entire-source reconstruction passed. This rejects changes anywhere outside the explicitly inspected regions, rather than globally discarding alignment tokens or whitespace.

An additional comparison tokenized the changed mathematical material as TeX control words, control symbols, and individual non-whitespace characters. After removing only the allowed layout tokens within their respective changed regions, the definition display and each of the twelve corresponding table cells had identical ordered token streams. In particular, numbers, signs, indices, primes, punctuation, carries, and mathematical control sequences are unchanged.

The table was separately checked structurally. Replacing each complete cell-local environment by a placeholder leaves byte-identical original and revised body skeletons: six rows in the order `P1, P2, P3, Q1, Q2, Q3`, two table-level `&` separators per data row (12 total), and six outer row terminators. Both table header occurrences, their column separators, caption, label, three column specifications and widths, footer, and inter-row spacing commands are unchanged. Thus the draft column-separator bug described in the author's note is absent from this hash-bound copy.

Outside these finite layout changes, all prose, logical content, theorem/proof source, references/citation commands, and dependency declarations are byte-identical. The original source's SHA-256 matches the supplied frozen hash; this review did not modify either source, auxiliary notation/bibliography, or any lock.

## Scope and limitations

This is a source-equivalence decision, not a new proof review, numerical recomputation, novelty assessment, or release decision. No compilation was run and no build/evidence file contents were read. The new metadata assignment is the only metadata-related source difference; actual emitted metadata, engine compatibility, visual readability, page layout, and zero-overfull acceptance still require a separate actual build and inspection. No successful runtime fit or publication readiness is inferred from this PASS.
