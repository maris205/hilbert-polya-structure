# P26 Stage 5 finalization package

The scholar confirmed this package's exact content proof on 2026-09-01 UTC.
The final PDF has therefore been generated under the authorized format-only
scope. The package verifier report and its freshness result, rather than this
README alone, control the Stage-5 completion record.

## Locked content

- `manuscript.tex`: accepted Stage-4.5 text with only 125 standalone ARS block
  transport-marker lines removed; SHA-256
  `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3`.
- `references.bib`: accepted bibliography, byte-identical; SHA-256
  `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f`.
- `content_proof.pdf`: scholar-confirmed 16-page proof, byte-identical to the
  accepted Stage-4.5 preview; SHA-256
  `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da`.

These three files are immutable Stage-5 inputs. The citation profile remains
numeric `natbib[numbers,sort&compress]` with `plainnat`.

## Final PDF

`paper.pdf` was compiled twice in completely independent temporary directories
with `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC` using
LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX. The two PDF byte streams are identical.

- SHA-256:
  `2e7b0deb7e9bda399d155f514d6f3fdcc89e5d463082456817da91bfca0792c5`.
- Extent: 16 A4 pages.
- `pdftotext -layout` SHA-256:
  `67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444`,
  exactly equal to the confirmed proof.
- Final log: no fatal error, undefined citation/reference, overfull box,
  missing glyph, or cross-reference rerun request; BibTeX warnings are zero.
- Fonts: 18/18 font programs are embedded. The text, CJK, italic, and
  monospace fonts carry Unicode maps. Thirteen unchanged Computer Modern
  Type-1 mathematical subsets report `uni=no` in `pdffonts`, exactly as in the
  confirmed proof; full-page Unicode text extraction nevertheless reproduces
  the proof hash above. This technical font-map limitation is disclosed rather
  than called clean.
- Visual inspection: all 16 pages were rendered and inspected; no clipping,
  overlap, missing glyph, abnormal blank page, or page-number defect was seen.

## Scientific result and Route boundary

The paper's significant result remains its exact finite newform-period
taxonomy: 138 registered Hecke cycle-owner instances split as 2 full
complex-period kernels, 2 real-projection-only kernels, and 134 true
nonkernels. Both primary scalar laws fail 51 of 55 registered groups, while
the declared control fails 55 of 55. This is a finite owner-level
non-implication result, not a global primitive-owner census or determinant.

The project remains at the early Route-A A0--A1 / A1--A2 frontier. P26 retains
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and
`ROUTE_A_EXPLORATORY`; the batch positive-arithmetic A2 count remains `0/5`,
and Route B invocations remain `0/5`. Route-A and Route-B evaluator hashes
remain respectively
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## Package boundary

- `provenance_summary.md` carries the nonblocking advisory record.
- `submission_verification_report.json` is the deterministic ARS package
  verifier output under advisory policy.
- The canonical `paper/**` and `results/**` trees are not part of this
  formatting package and remain unchanged.

The existing `#660` state `not_checked/SNAPSHOT_NOT_PROVIDED` and `#672` state
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE` are nonblocking but not clean.
No venue profile was supplied. Nothing in this package claims venue readiness,
submission, acceptance, or public release. Stage 6 remains pending after the
paper-local Stage-5 FULL completion checkpoint.
