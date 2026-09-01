# Paper 25 Stage-5 finalization report

Project: `25-three-disk-scattering-flow`  
Stage: `5 — FINALIZE`  
Mode: format-only  
Date: `2026-09-01 UTC`  
Verdict: **PASS — final paper complete; FULL checkpoint issued; Stage 6 pending**

## Authority and frozen inputs

The scholar's exact response is `确认`. It confirms the 13-page proof and
authorizes final PDF construction, read-only package verification, and this
FULL Stage-5 checkpoint. It is recorded in
`stage5_content_confirmation_20260901.md`, SHA-256
`54c38fe81429220bc1cd91ec0fc006a8646b0307336df27e276dcd07f923fc31`.

The three frozen input hashes were rechecked before compilation and remain:

| Input | SHA-256 |
|---|---|
| `stage5_finalization/manuscript.tex` | `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1` |
| `stage5_finalization/references.bib` | `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab` |
| `stage5_finalization/content_proof.pdf` | `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65` |

No locked byte was modified. The citation profile remains
`natbib[numbers,sort&compress] + plainnat`. The accepted derived bibliography
was not promoted into canonical `paper/references.bib`.

## Deterministic final build

Two completely independent `mktemp` workspaces used
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`. Each ran
the exact sequence LuaLaTeX → BibTeX → LuaLaTeX → LuaLaTeX, with every
LuaLaTeX call using job name `paper`, `-interaction=nonstopmode`,
`-halt-on-error`, and wrapper
`\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}`.

| Build fact | Result |
|---|---:|
| Independent PDFs | 2/2 byte-identical |
| Final PDF SHA-256 | `5968230a947956744c41d542a833e8cc165a0610980bb8bcdb3fed31c4f0198f` |
| Pages / page size | 13 / A4 |
| Final/proof `pdftotext -layout` SHA-256 | `60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185` / exact match |
| Fatal / undefined cite-ref / overfull / missing glyph | 0 / 0 / 0 / 0 |
| Underfull boxes | 10, all nonblocking Chinese-abstract paragraph diagnostics |
| BibTeX warning diagnostics | 0 |
| Citation commands / unique keys / BibTeX entries | 13 / 8 / 8 |
| Missing / orphan / duplicate bibliography keys | 0 / 0 / 0 |
| ARS markers / formatter hard-refusal tokens | 0 / 0 |
| Visual review | 13/13 pages; no observed clipping, overlap, missing page, or illegible table |

All 17 PDF fonts are embedded. `pdffonts` reports explicit Unicode maps on the
five CID text fonts and no ToUnicode map on 12 legacy Computer Modern Type-1
math subsets. This is recorded honestly rather than called all-font Unicode;
the full proof/final text extraction is byte-identical. Funding, conflict of
interest, contributions, data/code availability, ethics, author identity, and
AI-assisted-research disclosure remain present.

The retained build-A artifacts are `pass1.stdout`, `bib.stdout`,
`pass2.stdout`, `pass3.stdout`, `paper.aux`, `paper.bbl`, `paper.blg`, and
`paper.log` under `notes/stage5_build_artifacts/`. Pandoc/DOCX remains withheld
under the bound preflight lossiness result; no lossy file was promoted.

## Package verifier

The Stage-5 package README was complete before the verifier ran. ARS
`verify_submission_package.py` ran with `--policy advisory` and wrote
`stage5_finalization/submission_verification_report.json`, SHA-256
`e08e6143d23cb1fdefad4a71dbe37da46f4f811ceaac66fd062d28f02e536a44`.
The report fingerprint is
`782aa5e54234d906212175917a0ceec92d8da305d1bb797e734941f1f7d3d967`.

- A1–A7: `not_applicable` — no anonymized variant or declared double-blind profile.
- B1–B5: `not_checked` — no venue profile; limits were not guessed.
- C1/C2: `pass` — best-effort 8/8 two-way citation/reference closure.
- Counts: pass 2, not_applicable 7, not_checked 5, fail 0, warn 0.

Every non-passing advisory row is transcribed into the nonempty
`Submission Package Advisories` section of `provenance_summary.md`. The
post-transcription command with `--check-freshness --policy advisory` returned
the exact stdout `report fresh (policy=advisory)`. Neither live nor freshness
stdout contained `TERMINAL-BLOCK`, `VERIFICATION-INCOMPLETE`, or
`STALE-REPORT`. Exit code 3 reflects the five honest NOT-CHECKED venue rows,
not a terminal result.

## Scientific and roadmap result

Formatting preserves the paper's significant result: symmetric period-two and
period-three owners have exact mean roofs `d-2a` and `d-sqrt(3)a`, whose gap
`(2-sqrt(3))a` proves the physical roof is not cohomologous to a constant and
rules out every global owner- and repetition-preserving scalar substitution
`z=exp(-cs)`. The 2,241-row replay remains implementation validation, not a
second proof.

The paper retains only the early Route-A A1–A2 typed symbolic calibrator with
tuple `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`;
the arithmetic route is rejected and the physical-flow tuple stays
`UNASSIGNED`. Positive arithmetic A2 remains `0/5`; Route-B invocations remain
`0/5`; the batch's 19 model instances are not independent samples. The
Route-A and Route-B evaluator hashes remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## Advisory and action boundary

The Stage-4.5 source audit's linked erratum DOI `10.1063/1.457670` affects Eq.
(5.4) and Appendix typography, not the two current abstract/Sections-II–III
contexts; that bounded assessment remains visible in the provenance summary.
#660 remains `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
SNAPSHOT_NOT_PROVIDED`; #672 remains
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`. Both are nonblocking but
neither is clean. No venue profile was supplied, so this result is not a
venue-readiness or submission certificate. No canonical `paper/` or
`results/` file, canonical bibliography/PDF, scientific value, declaration,
route tuple, subtype, or flow restriction changed. No submission, public
release, external upload/contact, corresponding-author designation, Git
action, or Stage-6 transition occurred.
