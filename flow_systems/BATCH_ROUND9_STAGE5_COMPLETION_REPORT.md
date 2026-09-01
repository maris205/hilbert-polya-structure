# Round 9 Papers 24--28 — Stage 5 FULL completion report

Date: **2026-09-01 UTC**  
Pipeline state: **Stage 5 complete; FULL checkpoint delivered; Stage 6 pending and not entered**  
Batch verdict: **PASS WITH DISCLOSED NONBLOCKING FORMAT/PACKAGE ADVISORIES**  
Final papers: **5/5 emitted**

## Scholar confirmation and scope

The scholar's exact in-stage content response was:

> 确认

It confirms all five retained `content_proof.pdf` artifacts and authorizes the
reproducible final LaTeX builds, package verification, and this Stage-5 FULL
checkpoint.  It does not authorize a scientific-content edit, citation-style
change, canonical-tree promotion, Route advancement, submission, venue-
readiness claim, public release beyond the separately requested repository
synchronization, or external contact.

Stage 5 remained format-only.  All five locked `manuscript.tex`,
`references.bib`, and `content_proof.pdf` files retained their pre-confirmation
SHA-256 values.  The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.  Pandoc/DOCX
derivatives remain withheld because the recorded preflight demonstrated
material loss of mathematics, theorem/cross-reference structure, citation
rendering, bibliography linkage, or literal artifact paths.

## Final paper deliverables and explicit results

| Paper | Final PDF | Pages | PDF SHA-256 | Explicit scientific result carried by the completed paper | Route correspondence |
|---|---|---:|---|---|---|
| [P24](papers/24-bianchi-holonomy-flow/README.md) | [PDF](papers/24-bianchi-holonomy-flow/stage5_finalization/paper.pdf) | 15 | `8d690aa887c9aed27e1070b6bc840de333ff2d2de9f81a79945a034401025eeb` | The ring-general principal-congruence trace identity and first-jet laws survive as exact theorems.  On the frozen loxodromic matrix profile the joint descriptor lowers the largest collision bucket from 208 to 84, but yields zero singleton owners; this is a quantified negative-specificity result, not an orbit-owner solution. | Proxy remains `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; full flow unassigned. |
| [P25](papers/25-three-disk-scattering-flow/README.md) | [PDF](papers/25-three-disk-scattering-flow/stage5_finalization/paper.pdf) | 13 | `5968230a947956744c41d542a833e8cc165a0610980bb8bcdb3fed31c4f0198f` | The exact roof-nontransfer theorem and the 2,241-row validation-only estimand give a clear negative transfer result: the physical three-disk flow is not credited with the unit-roof symbolic determinant. | Unit-roof calibrator remains the nonarithmetic tuple `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`; physical flow unassigned. |
| [P26](papers/26-level11-newform-time-change/README.md) | [PDF](papers/26-level11-newform-time-change/stage5_finalization/paper.pdf) | 16 | `2e7b0deb7e9bda399d155f514d6f3fdcc89e5d463082456817da91bfca0792c5` | The exact 138-instance/55-group owner taxonomy, paired negative controls, and zero both-controls-pass residue establish the paper's scoped nonfactorization result without promoting the finite multiset to a global primitive Euler owner. | Remains early Route-A exploratory evidence with A2 failed. |
| [P27](papers/27-congruence-inverse-limit-no-go/README.md) | [PDF](papers/27-congruence-inverse-limit-no-go/stage5_finalization/paper.pdf) | 13 | `6b82701f253ab452b4c6be1c7f27dd6ff24267f5609317743492889834b40684` | The residual inverse-limit renormalization no-go/fixed-owner escape theorem and the separate homology-cover four-quadrant calibration are both explicit negative candidate results; the non-residual `Q11` control is not conflated with the residual theorem. | Both candidates retain their frozen rejected tuples; no positive arithmetic A2. |
| [P28](papers/28-bolza-magnetic-flow/README.md) | [PDF](papers/28-bolza-magnetic-flow/stage5_finalization/paper.pdf) | 14 | `be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9` | Exact nonarithmeticity, a finite word-to-length completeness certificate, and the exact systole chain form a substantive positive control.  Magnetic/arithmetic transfer and a matched Bolza/control A2 comparison remain unclaimed. | Full tuple remains unassigned; control infrastructure only. |

The five papers total **71 A4 pages**, **45 LaTeX citation-command
instances**, **33 unique citation keys**, and **33 BibTeX entries**.  Missing,
orphan, and duplicate keys are all zero.

## Reproducible final builds and content identity

Every finalizer used two completely independent temporary directories and the
same reproducibility envelope:

```text
SOURCE_DATE_EPOCH=1788220800
FORCE_SOURCE_DATE=1
TZ=UTC
LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX
LuaTeX wrapper: \pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}
```

The paired builds for each paper were byte-identical and one member of each
pair became `stage5_finalization/paper.pdf`.  The independent batch auditor
then ran a second pair of fresh builds for every paper.  All ten audit builds
matched the five promoted PDFs byte-for-byte.  Across the finalizer and
auditor, **20 independent build outputs** were therefore checked under the
same fixed envelope.

For every paper, the final PDF and scholar-confirmed proof have identical
`pdftotext -layout` bytes:

| Paper | Final/proof text SHA-256 |
|---|---|
| P24 | `f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931` |
| P25 | `60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185` |
| P26 | `67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444` |
| P27 | `5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b` |
| P28 | `2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff` |

All final and independent logs have zero fatal errors, undefined citations,
undefined references, overfull boxes, missing-character diagnostics, or
BibTeX warnings.  Paper 25 retains ten underfull Chinese-abstract lines as
nonblocking layout information.

## Render and font inspection

All **71/71 pages** were rendered into temporary all-page contact sheets and
visually inspected.  No clipping, overlap, unexpected blank page, broken
equation/table, unreadable Chinese text, truncated reference, or page-number
defect was observed.

All font programs are embedded: P24 `17/17`, P25 `17/17`, P26 `18/18`, P27
`18/18`, and P28 `17/17`.  Each paper has five CID text/CJK fonts with explicit
ToUnicode maps.  The remaining legacy Computer Modern Type-1 math subsets
report `uni=no`, exactly as in the accepted proofs.  This is a disclosed
accessibility limitation: no claim of complete per-font ToUnicode coverage is
made.  It is not a finalization regression, and full Unicode text extraction
is byte-identical to the proofs.

## Submission-package terminal gate

The official ARS verifier ran separately on all five finalization packages
under the explicitly resolved `advisory` policy, followed by a freshness
replay.  Each 14-row report has the same status distribution:

- A1--A7: 7 `not_applicable` rows; no anonymized variant or declared
  double-blind profile;
- B1--B5: 5 `not_checked` rows; no venue profile was declared, so limits were
  not guessed;
- C1--C2: 2 `pass` rows; LaTeX citation keys and BibTeX entries close in both
  directions;
- `warn=0`, `fail=0`;
- freshness output: `report fresh (policy=advisory)`;
- no `TERMINAL-BLOCK`, `VERIFICATION-INCOMPLETE`, or `STALE-REPORT` token.

Across the batch this is 10 pass, 35 not-applicable, and 25 honestly
not-checked rows.  Every B1--B5 row is transcribed into the nonempty
`Submission Package Advisories` section of the corresponding
`provenance_summary.md`.  Exit code 3 is the verifier's nonterminal advisory
result for incomplete venue checks; the ARS contract makes stdout tokens, not
raw exit codes, authoritative.

These are complete general-paper packages.  They are **not** venue-compliance,
journal-fit, acceptance, or submission-readiness certificates.

## Independent validation

The new read-only batch validator
[`tools/audit_round9_stage5_completion.rb`](tools/audit_round9_stage5_completion.rb),
SHA-256
`5407ba355557237f0764a66443643c284ee6d5b6e33106b3d728042e1f89b94b`,
passes **444/444** checks.  Its machine receipt is
[`BATCH_ROUND9_STAGE5_COMPLETION_RECEIPT.json`](BATCH_ROUND9_STAGE5_COMPLETION_RECEIPT.json),
SHA-256
`53ad11010b8a9fa5064644c0ce9fea22666370b6d9f89ab623a5cf70f7b73018`.

The validator independently checks locked source/proof hashes, exact content
confirmation, citation closure, page/text/font properties, final logs, two new
builds per paper, promoted-PDF byte identity, package-report roster and
freshness, advisory transcription, per-paper manifests, FULL checkpoints,
pipeline states, canonical/result trees, and Route locks.  The previous fresh
Stage-4.5 audit was also replayed and remains **397/397 PASS** with 487 claims
and 522 source-bound evidence rows.

The first validator execution reported 437/444 only because two newly written
string predicates were narrower than the authoritative text (`FRESH` versus
the official lowercase `report fresh`, and `scientific content` versus the
equivalent P24/P25 phrase `manuscript science`).  The predicates were corrected
without changing any paper artifact, and the complete build-and-audit suite
was rerun from scratch to obtain the recorded 444/444 PASS.  This 437/444
sentence is an operator execution-history note; only the final 444/444 receipt
is retained as machine-bound evidence.

## Roadmap correspondence and frozen dynamical scope

The two governing roadmap files remain byte-locked:

- [`skills/route-a-evaluator.md`](skills/route-a-evaluator.md), SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- [`skills/route-b-evaluator.md`](skills/route-b-evaluator.md), SHA-256
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Stage-5 completion is a paper-production milestone, not a Route coordinate.
The five projects remain in Route A's early A0--A1 / A1--A2 evidence and
control layer.  Positive arithmetic A2 is **0/5** and Route-B invocation is
**0/5**.  Paper 25's exact A2 determinant belongs only to its nonarithmetic
unit-roof symbolic calibrator and does not count as a positive arithmetic A2
result.  Gates A--E receive no new credit.

The initial dynamical restrictions remain unchanged:

1. the cusped Bianchi hyperbolic 3-flow proxy;
2. the no-eclipse physical three-disk flow, with a separate unit-roof symbolic
   calibrator;
3. the positive Level-11 newform time change;
4. the residual inverse-limit and homology-cover geodesic candidates; and
5. the nonarithmetic genus-two geodesic control / magnetic precursor.

The twelve frozen geometric/physical instances plus seven `q`-symbol
calibrators remain **19 bookkeeping model instances**, not 19 statistically
independent samples.

## Required advisory and authority boundaries

- #660 remains `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
  SNAPSHOT_NOT_PROVIDED`; it is not a clean-draft certificate.
- #672 remains `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; no carrier was
  fabricated, and it is not an agreement or clean result.
- B1--B5 remain untested until a scholar declares a venue profile.
- Partial per-font ToUnicode coverage is disclosed above.
- Pandoc/DOCX conversion remains materially lossy and unpromoted.
- Canonical `paper/` and `results/` trees remain exactly at their Stage-4.5
  hashes; final deliverables live in `stage5_finalization/`.
- No submission, journal contact, corresponding-author designation, external
  upload, venue-readiness claim, or Route advancement was performed.

The Stage-5 Collaboration Depth window contains only two scholar turns.  Under
the ARS short-stage guard, every dimension is recorded as
`insufficient_evidence`, without numerical scores or a Zone label.  This is
advisory only and cannot block progression.

## FULL checkpoint and next legal action

Stage 5 is complete for all five papers.  Each paper directory contains the
final PDF, locked LaTeX/BibTeX sources, retained content proof, build logs,
content-confirmation receipt, finalization report, final manifest, package
verifier report, provenance/advisory summary, pipeline-state update, and FULL
completion checkpoint.

Stage 6 (`PROCESS SUMMARY`) is optional and has **not** been entered.  The
scholar may confirm Stage 6, or explicitly skip it and terminate each pipeline
as completed with Stage 6 marked `skipped`.

```text
Pipeline: [v]RES -> [v]WRT -> [v]INT -> [v]REV -> [v]REVISE -> [v]RE-REV -> [v]F-INT -> [v]FIN -> [ ]SUMMARY
```
