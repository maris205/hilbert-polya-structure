# Independent completed-output diagnostic review

Decision: **PASS for bounded content and warning quality only.** This is not a builder-completion PASS, successful validation decision, or release authorization. The existing validator-failed status is unchanged.

Reviewed on 2026-09-05 using the `paper-compile` skill's applicable read-only post-compilation checks. Inspection was confined to the actual `build/layout-20260905-r0/main.pdf`, `main.log`, `main.tex`, `main.aux`, and `main.bbl`. No compilation, PDF modification, network access, or old/future-build inspection was performed. The previously established source-equivalence PASS is not broadened into a proof re-review.

## Artifact binding

- PDF: `build/layout-20260905-r0/main.pdf`
  - SHA-256: `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4`
- Actual build source: `build/layout-20260905-r0/main.tex`
  - SHA-256: `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`

`pdfinfo` reports 29 pages, 336,871 bytes, unencrypted PDF 1.5, letter-size pages, and `Custom Metadata: no`. Main-body/conclusion content ends on page 27; references occupy pages 28–29.

## Reference suffix and content checks

The complete extracted text of pages 28–29 was inspected against the complete `main.bbl`. The sole References heading begins on page 28. The suffix contains exactly the bibliography entries numbered `[1]` through `[20]` in order: entries 1–12 on page 28 and 13–20 on page 29, followed only by the final page number. `main.bbl` contains exactly 20 `\bibitem` entries; `main.aux` contains the corresponding 20 key-to-number bindings, agreeing with that order. No theorem, proof, appendix, or resumed body content occurs after References. The source ends with `\clearpage`, the reference-page diagnostic, bibliography commands, and `\end{document}`.

Across the PDF, the statement-heading census agrees with source environments: four theorems, eight lemmas, two propositions, and thirteen `Proof.` starts. Genuine headings were distinguished from line-leading in-text references to Lemmas 4.3 and 3.3. The section/subsection sequence continues through Section 8, and the complete final conclusion paragraphs appear before References. This establishes output continuity and statement/proof presence, not a new verification of the mathematical arguments or a character-perfect comparison of all rendered mathematics.

The repaired degree-set/cardinality display is present on page 13 with all four definitions. All six fixture IDs appear in each of Tables 1–3 in the expected order. Table 1 is on page 22, Table 2 on page 23, and Table 3 spans pages 24–25: `P1, P2, P3, Q1` precede `Q2, Q3`, with the continued column header present. Inspection of layout-preserving extraction retains ID/column associations and the split score-label/equality lines. An additional presence check found all 84 source numeric-tuple occurrences and all 18 scalar-carry occurrences from these three tables in their PDF text; the check is presence-based and is not claimed as an independent arithmetic recomputation or multiset proof. The seed determinant discussion and the displayed path remain after the target table.

The entire page-26 boundary table was inspected in both layout and raw text order. All seven labels, corresponding witnesses, and consequences are complete and ordered:

1. Characteristic zero.
2. Positive coordinates.
3. Coordinate lower bound and strictness.
4. Complete row family.
5. First carry.
6. Literal reflected label.
7. Positive-support cancellation control.

Layout-mode extraction interleaves text from adjacent columns. Raw extraction preserves the cell order, with actual physical wraps including `Positive coor- dinates`, `Literal re- flected label`, and `Positive- support can- cellation control`. These wraps are presentational, not missing labels. A fixed, exact wrapping alias is appropriate for this PDF; broad deletion of arbitrary hyphens or relaxation of the seven-label census is unnecessary.

## Disposition of all 18 underfull warnings

All are `Underfull \hbox` reports. The following accounting lists every occurrence; repeated badness values at one source location represent separate reported lines. Source line numbers refer to the actual hash-bound build source.

| Source lines | Badness values | Page and affected content | Diagnostic disposition |
|---|---|---|---|
| 153–165 | 1253 | Page 4, literature paragraph: Newton-polyhedron and tropical techniques | Loose justified spacing; full passage and citations remain present. |
| 1609 | 10000 | Page 26, “Characteristic zero” label | Short line in narrow label cell; both words present. |
| 1610–1612 | 7504 | Page 26, characteristic-p witness | Spaced prose/formula line; full zero-gradient example and characteristic-2 specialization present. |
| 1613–1614 | 6078 | Page 26, “establish fresh survival” consequence | Hyphenated “sur-vival”; complete sentence retained. |
| 1615 | 4859 | Page 26, “Positive coordinates” label | “coor-dinates” wraps; no label loss. |
| 1620 | 10000, 10000 | Page 26, “Coordinate lower bound and strictness” label | Two short justified lines; complete label retained. |
| 1623–1624 | 10000, 10000, 1546 | Page 26, selector-uniqueness/fresh-old consequence | Three loose narrow-cell lines; complete independent-failure assertion retained. |
| 1625 | 2521 | Page 26, “Complete row family” label | Short label line; both lines retained. |
| 1637 | 10000 | Page 26, “Literal reflected label” | “re-flected” wraps; complete label retained. |
| 1638–1639 | 2042 | Page 26, `(57,48,57) != (83,74,83)` witness | Both tuples and rendered not-equal relation present, with (6.5)–(6.7) references. |
| 1640–1641 | 3439 | Page 26, reflected-reciprocity consequence | Loose first line; full first-phase-failure sentence retained. |
| 1642 | 10000, 10000, 10000 | Page 26, positive-support cancellation-control label | Three short/wrapped label lines; full label retained across four lines. |
| 1646–1647 | 2005 | Page 26, zero/unit-support cancellation consequence | “sup-port” wrap; full actual fresh-term-cancellation assertion retained. |

Count: one warning on page 4 plus seventeen on page 26, totaling eighteen. None concerns the repaired target table. The warnings remain disclosed; they have not been suppressed or reclassified as successful build completion. For this bounded content review they are acceptable whitespace/hyphenation defects, with no missing affected text observed.

## Missing-text and geometry checks; limits

The actual final `main.log` contains no overfull report, missing-character report, undefined-reference/citation report, multiply-defined-label report, or LaTeX/package warning matched by the diagnostic scan. The complete extracted PDF text contains no `??`, `[?]`, `[VERIFY]`, or Unicode replacement-character marker. `pdffonts` lists 22 fonts, all embedded, subsetted, and with Unicode mapping. A read-only PyMuPDF scan found all 14,344 extracted text spans inside their physical page rectangles.

These observations support complete recoverable text, retained mathematical fixture values, and the benign disposition of the specific underfull reports. Page-bound geometry alone does not prove the absence of every internal overlap or clipping path, and PDF extraction cannot replace full visual inspection of every glyph. This report deliberately leaves rendered-image review to the separate visual inspection and does not certify pixel-perfect layout, mathematical correctness, bibliography factual correctness, publication readiness, or builder acceptance. It does not alter or independently overturn the reported `BIB_LOG` validator failure; diagnosis or correction of that validator belongs to the parent task.
