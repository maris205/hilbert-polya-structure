# P26 Stage 5 finalization report

Audit date: **2026-09-01 UTC**  
Stage result: **COMPLETE — FULL CHECKPOINT; STAGE 6 PENDING**

## Scholar confirmation and scope

The scholar's exact response was:

> 确认

It was recorded on 2026-09-01 UTC and answers the immediately preceding
content-proof confirmation request for this paper and Paper 27. It accepts
`stage5_finalization/content_proof.pdf` and authorizes creation of the final
PDF, the package audit, and a Stage-5 FULL completion checkpoint. The authority
is format-only: no scientific text, declaration, bibliography, citation style,
initial dynamical subtype, Route tuple, canonical `paper/**` file, or
`results/**` artifact may change. The current numeric
`natbib[numbers,sort&compress]` plus `plainnat` profile is retained.

The locked inputs were verified before and after finalization:

- `stage5_finalization/manuscript.tex` —
  `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3`;
- `stage5_finalization/references.bib` —
  `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f`;
- `stage5_finalization/content_proof.pdf` —
  `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da`.

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
  `2e7b0deb7e9bda399d155f514d6f3fdcc89e5d463082456817da91bfca0792c5`;
- size: 276,015 bytes; PDF 1.5; 16 A4 pages;
- `pdftotext -layout` SHA-256:
  `67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444`,
  exactly equal to the confirmed proof's layout-text hash.

Build A's three LuaLaTeX stdout files, BibTeX stdout, and final
`paper.aux/.bbl/.blg/.log` are versioned in
`notes/stage5_build_artifacts/`. The final log has zero fatal errors, undefined
citations, undefined references, overfull boxes, missing glyphs, or unresolved
cross-reference rerun requests. BibTeX has zero warnings and emits all seven
entries. The eight citation contexts resolve to seven unique cited keys, with
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

All 16 pages were rendered and visually inspected. Titles, Chinese and English
abstracts, equations, tables, declarations, references, and page numbering
show no clipping, overlap, missing glyph, anomalous blank page, or pagination
defect.

## Submission-package verifier

After `stage5_finalization/README.md` was completed, ARS 0.1.26's official
`scripts/verify_submission_package.py` ran with `--policy advisory`.
The report fingerprint is
`9afec90ea35c77542a14678b442d552a4b5bfac24ac64bdbc9358d565a19776c`;
the input fingerprint is
`0ab10a6e4242f1dc7e304bb8f998e6953e5ddf03a31950d7c74f8d581a9d52fa`.
Its 14 rows comprise seven `not_applicable` blind-review checks, five
`not_checked` venue-limit checks, and two passing best-effort reference checks.
There is no `fail` or `warn`. C1 verifies all 7 cited keys exist in the package
bibliography; C2 verifies all 7 entries are cited.

The five B1--B5 rows are each `not_checked` because no venue profile was
declared. They are transcribed individually under the nonempty
`Submission Package Advisories` section of `provenance_summary.md`. The
freshness replay emits the official line `report fresh (policy=advisory)`.
Neither the live nor freshness stdout has a line-prefixed `TERMINAL-BLOCK`,
`VERIFICATION-INCOMPLETE`, or `STALE-REPORT` token. The raw exit code `3`
reflects advisory `not_checked` rows and is not a terminal decision under the
ARS protocol.

## Scientific result, Route state, and frozen trees

The paper's significant unchanged result is the exact finite taxonomy for the
registered level-11 Hecke-output multiset: 138 instances split into two full
complex kernels, two real-projection-only kernels, and 134 true nonkernels.
At the 55-group level, each primary law fails in 51/55 groups and the
`a_p^2-p` control fails in 55/55. These are finite-multiset statements, not a
global primitive-Euler theorem.

The project remains at the early Route-A A0--A1 / A1--A2 frontier. The tuple
stays
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with
`ROUTE_A_EXPLORATORY`; batch positive-arithmetic A2 remains `0/5`, and Route B
invocations remain `0/5`. The evaluator SHA-256 values remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

The canonical `paper/**` tree remains
`71e7fb6184cfa7ee958745b81f078fdba8f7c930140a1f4bc4cafd1f520d943f`,
and `results/**` remains
`67e503425d253f2907cc85ecdedf6843c00ab84c048de34dd2c6cc722b409713`.
The existing `#660` carrier remains
`not_checked/SNAPSHOT_NOT_PROVIDED`; `#672` remains
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`. Both are nonblocking but
non-clean and are not reinterpreted here.

This completion establishes a paper-local Stage-5 FULL checkpoint only. It
does not claim venue readiness, submission, acceptance, or public release.
Stage 6 is pending and has not been entered automatically.
