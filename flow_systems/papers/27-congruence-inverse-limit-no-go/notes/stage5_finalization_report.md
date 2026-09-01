# P27 Stage 5 finalization report

Audit date: **2026-09-01 UTC**  
Stage result: **COMPLETE — FULL CHECKPOINT; STAGE 6 PENDING**

## Scholar confirmation and scope

The scholar's exact response was:

> 确认

It was recorded on 2026-09-01 UTC and answers the immediately preceding
content-proof confirmation request for Papers 26 and 27. It accepts
`stage5_finalization/content_proof.pdf` and authorizes creation of the final
PDF, the package audit, and a Stage-5 FULL completion checkpoint. The authority
is format-only: no scientific text, declaration, bibliography, citation style,
initial dynamical subtype, Route tuple, canonical `paper/**` file, or
`results/**` artifact may change. The current numeric
`natbib[numbers,sort&compress]` plus `plainnat` profile is retained.

The locked inputs were verified before and after finalization:

- `stage5_finalization/manuscript.tex` —
  `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48`;
- `stage5_finalization/references.bib` —
  `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981`;
- `stage5_finalization/content_proof.pdf` —
  `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208`.

## Deterministic final build

Two completely independent `mktemp` directories were populated only from the
three locked package inputs. Both builds used
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, followed
this exact sequence, and returned `0,0,0,0`:

1. `lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'`
2. `bibtex paper`
3. the same LuaLaTeX command
4. the same LuaLaTeX command

The two `paper.pdf` byte streams were identical. One Build-A copy was retained
as `stage5_finalization/paper.pdf`:

- SHA-256:
  `6b82701f253ab452b4c6be1c7f27dd6ff24267f5609317743492889834b40684`;
- size: 256,723 bytes; PDF 1.5; 13 A4 pages;
- `pdftotext -layout` SHA-256:
  `5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b`,
  exactly equal to the confirmed proof's layout-text hash.

Build A's three LuaLaTeX stdout files, BibTeX stdout, and final
`paper.aux/.bbl/.blg/.log` are versioned in
`notes/stage5_build_artifacts/`. The final log has zero fatal errors, undefined
citations, undefined references, overfull boxes, missing glyphs, or unresolved
cross-reference rerun requests. BibTeX has zero warnings and emits all five
entries. The five citation contexts resolve to five unique cited keys, with
zero missing keys and zero uncited bibliography entries. All seven required
declaration headings and the author/affiliation/email line remain present.

Pandoc remains a documented lossy path: it drops the rendered numeric
citations and bibliography and reports mathematical conversion losses, so the
locked LaTeX is authoritative.

## Font and visual checks

`pdffonts` reports 18/18 embedded font programs. Five text, CJK, italic, and
monospace rows have Unicode maps. Thirteen unchanged Computer Modern Type-1
math subsets report `uni=no`, exactly as in the accepted proof. This is a
technical limitation, not a claim that every subset has ToUnicode; full-page
Unicode text extraction nevertheless matches the confirmed proof exactly.

All 13 pages were rendered and visually inspected. Titles, Chinese and English
abstracts, equations, tables, declarations, references, and page numbering
show no clipping, overlap, missing glyph, anomalous blank page, or pagination
defect.

## Submission-package verifier

After `stage5_finalization/README.md` was completed, ARS 0.1.26's official
`scripts/verify_submission_package.py` ran with `--policy advisory`.
The report fingerprint is
`ecb22e933dcf49cb9a33b01997e635e53245a18114e8e3159c0c7f66c316bf7c`;
the input fingerprint is
`0ab10a6e4242f1dc7e304bb8f998e6953e5ddf03a31950d7c74f8d581a9d52fa`.
Its 14 rows comprise seven `not_applicable` blind-review checks, five
`not_checked` venue-limit checks, and two passing best-effort reference checks.
There is no `fail` or `warn`. C1 verifies all 5 cited keys exist in the package
bibliography; C2 verifies all 5 entries are cited.

The five B1--B5 rows are each `not_checked` because no venue profile was
declared. They are transcribed individually under the nonempty
`Submission Package Advisories` section of `provenance_summary.md`. The
freshness replay emits the official line `report fresh (policy=advisory)`.
Neither the live nor freshness stdout has a line-prefixed `TERMINAL-BLOCK`,
`VERIFICATION-INCOMPLETE`, or `STALE-REPORT` token. The raw exit code `3`
reflects advisory `not_checked` rows and is not a terminal decision under the
ARS protocol.

## Scientific result, Route state, and frozen trees

The paper's significant unchanged result is the owner-level no-go theorem for
the frozen residual congruence inverse-limit flow: the total space has no
periodic points, and every fixed finite same-owner panel escapes every bounded
physical-time and coefficient window. The separately registered nonresidual
homology-cover calibrator recovers the fixed-panel factor only with simultaneous
`1/N` clock rescaling and `1/N^3` logarithmic normalization; it neither creates
periodic points in the residual object nor transfers Route credit to it.

The project remains at the early Route-A A0--A1 / A1--A2 frontier. The
residual tuple stays
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the
separate calibrator tuple stays
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)`; both remain
`ROUTE_A_REJECTED`. Batch positive-arithmetic A2 remains `0/5`, and Route B
invocations remain `0/5`. The evaluator SHA-256 values remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

The canonical `paper/**` tree remains
`c95656aee2c1ba49bf4646f80e6c203047fcb832ed76371ae931a898991594a1`,
and `results/**` remains
`5009c710cf06ef5147ccc392ee09c604b9a5b846b433eacbfc57650957d65761`.
The existing `#660` carrier remains
`not_checked/SNAPSHOT_NOT_PROVIDED`; `#672` remains
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`. Both are nonblocking but
non-clean and are not reinterpreted here.

This completion establishes a paper-local Stage-5 FULL checkpoint only. It
does not claim venue readiness, submission, acceptance, or public release.
Stage 6 is pending and has not been entered automatically.
