# Paper 24 Stage-5 finalization report

Project: `24-bianchi-holonomy-flow`  
Stage: `5 — FINALIZE`  
Mode: format-only  
Date: `2026-09-01 UTC`  
Verdict: **PASS — final paper complete; FULL checkpoint issued; Stage 6 pending**

## Authority and frozen inputs

The scholar's exact response is `确认`. It confirms the 15-page proof and
authorizes final PDF construction, read-only package verification, and this
FULL Stage-5 checkpoint. It is recorded in
`stage5_content_confirmation_20260901.md`, SHA-256
`4fe098b00b87b020e57a31e93b441ff1534500c13d8b3f33c4e4419fc4adf852`.

The three frozen input hashes were rechecked before compilation and remain:

| Input | SHA-256 |
|---|---|
| `stage5_finalization/manuscript.tex` | `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e` |
| `stage5_finalization/references.bib` | `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87` |
| `stage5_finalization/content_proof.pdf` | `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea` |

No locked byte was modified. The citation profile remains
`natbib[numbers,sort&compress] + plainnat`.

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
| Final PDF SHA-256 | `8d690aa887c9aed27e1070b6bc840de333ff2d2de9f81a79945a034401025eeb` |
| Pages / page size | 15 / A4 |
| Final/proof `pdftotext -layout` SHA-256 | `f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931` / exact match |
| Fatal / undefined cite-ref / overfull / missing glyph | 0 / 0 / 0 / 0 |
| Underfull boxes | 0 |
| BibTeX warning diagnostics | 0 |
| Citation commands / unique keys / BibTeX entries | 9 / 7 / 7 |
| Missing / orphan / duplicate bibliography keys | 0 / 0 / 0 |
| ARS markers / formatter hard-refusal tokens | 0 / 0 |
| Visual review | 15/15 pages; no observed clipping, overlap, missing page, or illegible table |

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
`2bdb2b3833011c57df17ee27c808a9cda0661ca5174c553ec219e605d23100f6`.
The report fingerprint is
`f4aa2e5407a3b43aee5fe9900b514395112bba1a8a118d7791245eda390512c3`.

- A1–A7: `not_applicable` — no anonymized variant or declared double-blind profile.
- B1–B5: `not_checked` — no venue profile; limits were not guessed.
- C1/C2: `pass` — best-effort 7/7 two-way citation/reference closure.
- Counts: pass 2, not_applicable 7, not_checked 5, fail 0, warn 0.

Every non-passing advisory row is transcribed into the nonempty
`Submission Package Advisories` section of `provenance_summary.md`. The
post-transcription command with `--check-freshness --policy advisory` returned
the exact stdout `report fresh (policy=advisory)`. Neither live nor freshness
stdout contained `TERMINAL-BLOCK`, `VERIFICATION-INCOMPLETE`, or
`STALE-REPORT`. Exit code 3 reflects the five honest NOT-CHECKED venue rows,
not a terminal result.

## Scientific and roadmap result

Formatting preserves the paper's significant result: the normalized trace
identity is universal over commutative principal-congruence rings, stopping it
as a Gaussian-specific owner mechanism; the signed first jet improves the
frozen loxodromic descriptor count from 144 to 508 and lowers the largest
bucket from 208 to 84 but leaves 10,468 joint collision rows and no singleton.

The paper remains early Route-A A0–A1. The typed proxy tuple is unchanged as
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and the
complete Bianchi flow stays `UNASSIGNED`. Positive arithmetic A2 remains
`0/5`; Route-B invocations remain `0/5`; the batch's 19 model instances are
not independent samples. The Route-A and Route-B evaluator hashes remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## Advisory and action boundary

#660 remains `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
SNAPSHOT_NOT_PROVIDED`; #672 remains
`ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`. Both are nonblocking but
neither is clean. No venue profile was supplied, so this result is not a
venue-readiness or submission certificate. No canonical `paper/` or
`results/` file, scientific value, declaration, route tuple, subtype, or flow
restriction changed. No submission, public release, external upload/contact,
corresponding-author designation, Git action, or Stage-6 transition occurred.
