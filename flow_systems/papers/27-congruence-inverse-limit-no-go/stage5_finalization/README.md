# P27 Stage 5 finalization package

The scholar confirmed this package's exact content proof on 2026-09-01 UTC.
The final PDF has therefore been generated under the authorized format-only
scope. The package verifier report and its freshness result, rather than this
README alone, control the Stage-5 completion record.

## Locked content

- `manuscript.tex`: accepted Stage-4.5 text with only 110 standalone ARS block
  transport-marker lines removed; SHA-256
  `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48`.
- `references.bib`: accepted bibliography, byte-identical; SHA-256
  `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981`.
- `content_proof.pdf`: scholar-confirmed 13-page proof, byte-identical to the
  accepted Stage-4.5 preview; SHA-256
  `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208`.

These three files are immutable Stage-5 inputs. The citation profile remains
numeric `natbib[numbers,sort&compress]` with `plainnat`.

## Final PDF

`paper.pdf` was compiled twice in completely independent temporary directories
with `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC` using
LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX. The two PDF byte streams are identical.

- SHA-256:
  `6b82701f253ab452b4c6be1c7f27dd6ff24267f5609317743492889834b40684`.
- Extent: 13 A4 pages.
- `pdftotext -layout` SHA-256:
  `5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b`,
  exactly equal to the confirmed proof.
- Final log: no fatal error, undefined citation/reference, overfull box,
  missing glyph, or cross-reference rerun request; BibTeX warnings are zero.
- Fonts: 18/18 font programs are embedded. The text, CJK, italic, and
  monospace fonts carry Unicode maps. Thirteen unchanged Computer Modern
  Type-1 mathematical subsets report `uni=no` in `pdffonts`, exactly as in the
  confirmed proof; full-page Unicode text extraction nevertheless reproduces
  the proof hash above. This technical font-map limitation is disclosed rather
  than called clean.
- Visual inspection: all 13 pages were rendered and inspected; no clipping,
  overlap, missing glyph, abnormal blank page, or page-number defect was seen.

## Scientific result and Route boundary

The paper's significant result remains the owner-level no-go theorem for the
frozen residual congruence inverse-limit flow: it has no periodic points, and
every fixed finite same-owner panel escapes every bounded physical-time or
coefficient window. A separately registered nonresidual homology-cover
calibrator recovers each fixed finite-panel factor only under simultaneous
`1/N` clock rescaling and `1/N^3` logarithmic normalization. The calibrator
does not restore periodic points or transfer Route credit to the residual
object.

The project remains at the early Route-A A0--A1 / A1--A2 frontier. The
residual tuple stays
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and the
separate homology-calibrator tuple stays
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)`; both remain
`ROUTE_A_REJECTED`. The batch positive-arithmetic A2 count remains `0/5`, and
Route B invocations remain `0/5`. Route-A and Route-B evaluator hashes remain
respectively
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
