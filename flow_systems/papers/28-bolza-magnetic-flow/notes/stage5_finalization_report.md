# Paper 28 Stage-5 finalization report

Project: `28-bolza-magnetic-flow`  
Stage: `5 — FINALIZE`  
Mode: `academic-paper / format-convert`, LaTeX authoritative  
Date: `2026-09-01`  
Verdict: **PASS WITH DISCLOSED FONT-ACCESSIBILITY ADVISORY — FULL checkpoint complete; Stage 6 pending**

## 1. Scholar decision and immutable inputs

The scholar supplied the exact in-stage content response:

> 确认

The decision is recorded in
`stage5_content_confirmation_20260901.md`, SHA-256
`6f54576b8a45dcd65c3cfabe3f07bb841a7343f8fd19eb9f135f19b1cdd437e6`.
It accepts the Stage-4.5 content proof and authorizes the final PDF, package
audit, and Stage-5 FULL checkpoint.  It does not authorize a content change,
submission, release, external contact, Git action, venue-readiness claim, or
Route advancement.

| Locked artifact | SHA-256 | Stage-5 result |
|---|---|---|
| `stage5_finalization/manuscript.tex` | `14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22` | unchanged |
| `stage5_finalization/references.bib` | `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e` | unchanged |
| `stage5_finalization/content_proof.pdf` | `253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382` | unchanged; 14 pages |
| `stage5_finalization/paper.pdf` | `be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9` | final reproducible output |

The accepted batch lock remains
`BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json`, SHA-256
`bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30`.
The canonical `paper/` tree remains
`4497bac80e9e8e4d5f7e3dfa2ce666fbccbee352a8ea86c026329ef3416af4ca`,
and the canonical `results/` tree remains
`6a4910923b08c92c738462ef6be60e8ed77c9d3fd4bf373bcc56e6bc1cd97fc7`.

## 2. Reproducible compilation

The three locked finalization inputs were copied into two completely
independent `mktemp` directories.  Each directory ran the exact four-command
sequence LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX with:

```text
SOURCE_DATE_EPOCH=1788220800
FORCE_SOURCE_DATE=1
TZ=UTC
lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
bibtex paper
lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
```

Both outputs have SHA-256
`be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9`
and are byte-identical.  Their final `.log` files are also byte-identical at
SHA-256
`7e48c8ac2bdbffe52e1977fc818e4aa5538b8eb3373702e59b54f5a390ccb3e2`,
and their BibTeX `.blg` files are byte-identical at
`c636a1f0bf09160111f49ccab4eeeeac66011c91f779c30679312d394d1d9511`.
Only the first run's PDF was copied to the final package.

The final file is 323,657 bytes, PDF 1.5, and 14 A4 pages at
`595.276 x 841.89 pt`.  The final log contains zero fatal errors, undefined
citations, undefined references, overfull boxes, and missing-character/glyph
diagnostics.  BibTeX ends with `warning$ -- 0`.

## 3. Content, citation, and declaration checks

The final PDF and accepted proof have identical `pdftotext -layout` streams,
each SHA-256
`2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff`.
Thus the final rendered text is byte-equivalent to the scholar-confirmed proof
under the recorded extractor.

- Citation profile:
  `natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.
- Citation commands / citation-key occurrences: 9 / 9.
- Unique citation keys / BibTeX entries: 6 / 6.
- Missing / orphan / duplicate keys: 0 / 0 / 0.
- ARS HTML markers: 0.
- Formatter refusal tokens: 0.
- `TODO`, `TBD`, `FIXME`, author-confirmation, or material-gap placeholders:
  0.
- Required declaration/content gate: the byte-locked preflight's 16/16 result
  remains valid because the source and bibliography hashes are unchanged.

The Stage-4.5 Round-2 integrity result remains `PASS`: references 6/6,
citation contexts 9/9, registered claims 95/95, and expected/actual evidence
tuples 104/104.

## 4. Fonts and visual rendering

All 17 font programs are embedded and subsetted.  Five text/CJK fonts carry
explicit ToUnicode maps.  Twelve legacy Computer Modern Type-1 math fonts
report `uni=no`; the accepted content proof has exactly the same 5/17 versus
12/17 profile.  This is recorded as a bounded accessibility advisory and is
not misreported as complete per-font ToUnicode coverage.  The successful
Unicode `pdftotext` equivalence establishes that final extraction did not
regress from the accepted proof.

A temporary `pdfpages` 2x2 contact document represented all 14 pages on four
landscape A4 sheets.  `pdftoppm` rendered every sheet, and each was inspected
at original image detail.  No clipping, overlap, unexpected blank page,
broken equation/table, unreadable Traditional Chinese, or truncated reference
was observed.  The two unused quadrants on the fourth contact sheet are the
expected remainder of a 14-page document, not manuscript blank pages.

## 5. Submission-package verifier

The official ARS verifier ran against `stage5_finalization/` under the
explicitly resolved `advisory` policy.  The report is
`stage5_finalization/submission_verification_report.json`, SHA-256
`13311a088bb0f2083c82f4dd01676ccf5d910bc88c725a567f7b59f539ad67ab`,
with package fingerprint
`27fa855909de6309c11203cc40842b2077ee31aaaa5496b7e4194be4c6a367a4`.

- A1--A7: 7 `not_applicable`; no anonymized variant and no declared
  double-blind profile.
- B1--B5: 5 `not_checked`; no venue profile, so limits were not guessed.
- C1--C2: 2 `pass`; all 6 cited keys and all 6 BibTeX entries close under the
  explicitly labelled best-effort extractor.
- `fail`: 0; `warn`: 0.
- Freshness stdout: `report fresh (policy=advisory)`.
- Terminal stdout tokens: none (`TERMINAL-BLOCK`,
  `VERIFICATION-INCOMPLETE`, and `STALE-REPORT` absent).

Exit code 3 reflects the five venue `not_checked` rows; it is not treated as a
terminal signal because the ARS contract makes stdout tokens authoritative.
All B1--B5 rows are transcribed in the mandatory nonempty
`Submission Package Advisories` section of `provenance_summary.md`.

This audit does not establish venue compliance, venue fit, submission
readiness, or release authority.

## 6. Scientific progress and Route correspondence

The significant landed result is a positive control chain:

1. exact nonarithmeticity for the frozen genus-two octagon;
2. a finite completeness certificate below the target-blind cutoff; and
3. the exact systole with a primitive equality witness.

This closes a substantive Route-A control-side prerequisite.  It does not
claim the later magnetic/arithmetic transfer, perform a matched
Bolza/control census, run A2, or invoke Route B.  P28 therefore remains in the
early Route-A control-infrastructure layer, with the formal full tuple
unassigned.  Across the batch, positive-arithmetic A2 remains `0/5` and
Route-B invocations remain `0/5`.  The 19 recorded model instances are not
independent statistical samples.

The governing Route files retain their locked hashes:

- `skills/route-a-evaluator.md`:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md`:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Stage-5 integrity and formatting PASS do not promote either Route.

## 7. Non-clean advisories and authority boundary

- #660 remains `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
  SNAPSHOT_NOT_PROVIDED`; it is not a clean certificate.
- #672 remains
  `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; it is neither agreement nor a
  clean result.
- B1--B5 remain `not_checked` until a venue profile is declared.
- Twelve legacy math fonts lack explicit ToUnicode maps in both final and
  accepted proof; complete per-font ToUnicode coverage is not claimed.
- Pandoc is withheld because the unchanged preflight demonstrates material
  loss of bibliography, artifact-path, theorem, and cross-reference structure.

No scientific/declaration/bibliography/Route/subtype/canonical-source/result
change, submission, public release, external upload, author contact,
corresponding-author designation, venue-readiness claim, or Git operation was
performed.  Stage 5 is complete.  Stage 6 remains optional and pending.

