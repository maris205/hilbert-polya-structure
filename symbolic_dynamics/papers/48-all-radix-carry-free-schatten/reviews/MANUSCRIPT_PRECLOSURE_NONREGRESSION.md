# Paper 48 Pre-closure Repair: Nonregression and Recheck Anchors

Date: 2026-08-18 UTC.

Status: writer-side nonregression PASS; controlling state is
HOLD_FOR_INDEPENDENT_WRITER_AUDIT.

This is a writer-side audit, not an independent referee verdict.  It does
not transfer the earlier round-2 ACCEPT decision to the repaired artifact and
does not claim CLEAN.  It is now an input to, not a substitute for, the
independent writer audit.

## Artifact identity

- Repaired PDF: `paper/CarryFreeRadixOperators.pdf`
- SHA-256:
  `5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573`
- Withdrawn predecessor:
  `daaf6435625c6f1206f3e1faaec090619f2bc2750be5e1b4ca2cf748c0063867`
- Format: 16 A4 pages, fixed epoch 1787011200.
- Fresh lanes A and B, the named PDF, and the in-place PDF are
  byte-identical at the repaired SHA-256.

## Exact source anchors

- Glyph maps: `paper/main.tex`, lines 3--8.
- Fixed loop-set delimiters: `paper/sections/06_traces_determinants_periods.tex`,
  lines 8--16.
- Frozen one-sided shift and periodic-word convention:
  `paper/sections/06_traces_determinants_periods.tex`, lines 167--179.
- Least-period statement and proof:
  `paper/sections/06_traces_determinants_periods.tex`, lines 181--205.
- Lucas volume 6: `references.bib`, lines 12--20, and
  `evidence/SOURCE_VERIFICATION.md`, lines 20--27.
- Fixed binary-figure matrix delimiters:
  `figures/tikz/pinching_comparison.tex`, lines 50--57.

All explicit `\left`, `\right`, `\bigl`, and `\bigr` sizing commands that
generated the original illegal extension glyphs were removed from manuscript
and figure source.  Remaining matrix delimiters retain their visual function
and now receive correct Unicode component mappings.

## PDF anchors for visual/text recheck

- Page 1: abstract and finite digit matrix; fixed semantic delimiters.
- Page 2: explicit digit spectrum, equation (3).
- Page 4: digit definitions and equations (5)--(6).
- Page 6: shell norms and two-ratio estimate, equations (10) and (14).
- Page 7: the two geometric-series displays; Unicode minimum page.
- Page 9: binary pinching figure and equation (20).
- Page 10: loop digit set, equation (21), with braces and floor glyphs.
- Page 11: Section 6.4, explicitly the one-sided shift on
  \(\mathbb N_0\) and \(\mathbb N^{\mathbb N_0}\).
- Page 13: Appendix A trigonometric boundary equation.
- Page 14: Appendix B digit tuples and Appendix C direct-sum norm.
- Page 16: Lucas bibliography entry displays volume `6:49--54`.

## Mechanical evidence

- Poppler `-nopgbrk` default/layout/raw: illegal XML C0 = 0, DEL = 0,
  C1 = 0, U+FFFD = 0 in each mode.
- PyMuPDF page text: the same four counts are all zero.
- Private Use Area code points: zero in Poppler and PyMuPDF text.
- Raw Poppler bbox XHTML: zero illegal XML bytes and direct XML parse PASS;
  no cleaning or sanitization step was applied.
- Unicode non-whitespace page counts use actual code points and
  `not char.isspace()`: minimum page 7, exactly 1,180.
- Final LaTeX/BibTeX logs: no warning, error, unresolved citation/reference,
  overfull box, or underfull box.
- Citations: 9 cited keys, 9 bibliography items, no missing or uncited item,
  and no `??` placeholder.
- Fonts: 33 reported rows; every row is embedded, subset, and has ToUnicode.
- Visual inspection: all 16 fresh rendered pages checked without clipping,
  overlap, missing glyph, or unexpected reflow.

The exact structured result is retained as `evidence/PDF_QA.json`.  Raw
extractions, two fresh build roots, and page renders remain candidate-only
development evidence and are deliberately excluded from the minimal overlay.

## Claim-level nonregression checklist

- Main theorem quantifiers and strict Schatten surface are unchanged.
- The universal wall, active/hidden digit wall, and equality rejection are
  unchanged.
- Binary paired-shell compression still covers the full relevant
  nonmembership range and not merely equality.
- Phase removal remains the two-sided unitary equivalence
  \(B_{b,s}=U_tB_{b,\sigma}U_t\), not a unitary conjugation.
- Zero deletion, trace-class domain, trace-power limiting argument, and the
  local-vs-entire determinant distinction are unchanged.
- The restored one-sided shift matches the frozen SOURCE_LOCK.  Periodic
  points are explicitly right-infinite repetitions of cyclic words, so the
  existing least-period witnesses apply without enlarging the source.
- The Lucas change is bibliographic metadata only and does not alter its
  historical-comparator ownership role.
- Finite lanes, interval checks, mutations, and adversarial replays remain
  validation controls only; no machine PASS is described as an infinite
  proof or certificate.
- No priority, exhaustive-search, completed-function, target-divisor,
  rational-prime, or free-UFD claim was introduced.

## Requested independent disposition

The independent writer auditor should verify the repaired PDF hash, the
page/source anchors above, all four extraction families, and this
nonregression checklist.  The live protected manifest has now been injected
and independently replayed, retiring `WAIT_PROTECTED_AUTHORITY`; nevertheless
the writer makes no independent-review or CLEAN claim.  Closure remains
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT` until a separate auditor accepts the exact
self-excluding overlay.
