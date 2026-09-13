# Independent Manuscript Review R1

## Verdict

PASS. I found no required findings and no cosmetic findings. The Round-0
manuscript package is internally consistent with the publication lock, the
passed source review, the deterministic build receipt, and the rendered PDF.
The manuscript is mathematically coherent, scope-disciplined, anonymous, and
submission-ready within the locked proof-first envelope.

## Independence, fence, and method

I am a fresh Round-1 reviewer. I authored none of the Paper18 governance,
plan, proof, source, build, or prior review artifacts. Before writing this
file I read, to EOF, the required review/compile/workflow skill instructions,
the publication governance pair, the exact U_R0 project universe, and the
current Batch-05 control files for readiness context.

This audit was read-only except for the sole authorized write to this path. I
did not modify `paper/main.tex`, `paper/references.bib`, the PDF, the receipt,
or any governance artifact. I performed no compilation, no web access, no
scientific execution, and no project write before this file.

## Exact Round-0 identities bound in this review

| Path | SHA-256 | Bytes | LF/lines |
|---|---|---:|---:|
| `paper/main_round0.pdf` | `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b` | 425,791 | 2,220 |
| `paper/BUILD_RECEIPT_R0.json` | `b7f95533f81f9aa2c316eef2f20be4f0ad6af8fa8c1ac19745eff95d6d5cd0ad` | 207,381 | 1 |
| `paper/main.tex` | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` | 69,588 | 1,602 |
| `paper/references.bib` | `51bb41341009caa22d9433440475761608e1d4af2343a974cfbd74447070ea21` | 1,577 | 54 |
| `notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md` | `5ca232f888fc62d8fbd7d87f26f4dd31562af09c7191e7a8829f1d6ea97762cc` | 23,257 | 215 |
| `experiments/publication_lock.json` | `052ba1d2ed94055feaa7af53aa667019ec81481621d86fbe5775fd73eaf6d542` | 60,277 | 1 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `6802b5fb83657cff2a1b65c1e4c9f8bdc6f726df9d713a84ace09adcc87951a6` | 44,779 | 932 |

I independently revalidated that `experiments/publication_lock.json`,
`experiments/source_lock.json`, and `paper/BUILD_RECEIPT_R0.json` are strict
canonical JSON: UTF-8, LF-only, one terminal LF, duplicate-key rejection,
nonfinite rejection, recursively sorted keys, compact separators, and correct
self-exclusion.

## Exact prewrite U_R0 inventory and later-path absences

Immediately before this write, the live Paper18 project was exactly U_R0:
23 regular files, 4 child directories (`experiments`, `notes`, `paper`,
`refine-logs`), 0 symlinks, and 0 other entry types.

The exact regular-file path set was:

```text
experiments/EXPERIMENT_PLAN.md
experiments/EXPERIMENT_TRACKER.md
experiments/publication_lock.json
experiments/source_lock.json
notes/CITATION_VERIFICATION.md
notes/CLAIMS_EVIDENCE_MATRIX.md
notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md
notes/INDEPENDENT_PAPER_PLAN_REVIEW.md
notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md
notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md
notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md
notes/NOVELTY_ASSESSMENT.md
notes/PROOF_PACKAGE.md
notes/PUBLICATION_STAGE_SCOPE.md
notes/RESEARCH_QUESTION.md
paper/BUILD_RECEIPT_R0.json
paper/PAPER_PLAN.md
paper/main.tex
paper/main_round0.pdf
paper/references.bib
refine-logs/FINAL_PROPOSAL.md
refine-logs/INITIAL_PROPOSAL.md
refine-logs/REVIEW_SUMMARY.md
```

The later paths remained absent before this write, including
`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`,
`paper/SOURCE_REVISION_RECEIPT_R1.json`, `paper/BUILD_RECEIPT_R1.json`,
`paper/main_round1.pdf`, and `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`.

## Conjunctive audit summary

### 1. Governance, receipt, and deterministic-build integrity

- The publication lock, publication scope, source lock, source review, source
  files, Round-0 PDF, and Round-0 receipt match the bound identities above.
- The receipt is strict canonical JSON and binds the exact two-root build
  protocol, eight-command transcript equality, byte-identical A=B outputs,
  font-table equality, and explicit cleanup.
- The receipt’s authoritative validator status is `VALIDATOR_V8_PASS`; the
  receipt records a byte-identical PDF, BBL, final log, per-command
  transcripts, combined transcript, and font table across the two fresh `/tmp`
  roots.
- The receipt’s cleanup ledger is structurally consistent with the locked
  nonrecursive unlink-and-rmdir policy, and the Round-0 roots named in the
  receipt are presently absent.
- The current Batch-05 controls remain consistent with Paper18 being the live
  batch paper and with the R1 manuscript-review stage being the next allowed
  internal step.

### 2. Source structure, article contract, and bibliography

- `paper/main.tex` uses the exact locked class line
  `\\documentclass[11pt]{article}`, exact blank `\\author{}` and `\\date{}`,
  and the exact locked title at source line 62.
- The manuscript is monolithic and pdfTeX-compatible. There are no external
  section files, no figure files, no graphics includes, and no hidden source
  tree.
- The abstract at source lines 69--71 is result-first, anonymous,
  citation-free, history-free, and within the locked word window.
- The source contains exactly eight numbered main sections in the locked order
  (source lines 73, 188, 368, 507, 933, 1052, 1296, 1428), exactly one
  appendix introduced at line 1514, and a forced `\\clearpage` before the
  bibliography at line 1598.
- There is exactly one manuscript table environment, the proof-dependency
  table at source lines 620--643, and zero figure environments,
  `\\includegraphics` commands, raster/vector assets, or numerical-result
  tables.
- The citation key set in `paper/main.tex` exactly equals the seven-entry key
  set in `paper/references.bib`:
  `BH26, CD26, FM89, GT24, Gor13, Hug24, StacksProject`.
- The bibliography has exactly seven entries, all cited, with no wildcard
  `\\nocite`, no duplicate keys, and no uncited record.

### 3. Mathematical correctness, scope guards, and proof coverage

- The source states the full locked setup: `d>=2`, `r=d-1`, arbitrary positive
  period vector, repeated numerical periods allowed, labelled cycles, exact
  periods, pairwise disjointness, and simplicity.
- The five theorem parts at source lines 529--618 match the locked theorem:
  selected scalar component, coordinate map, reducible-fiber-safe fixed-`b`
  specialization, completed local form, and simple-boundary Fitting
  restriction.
- The theorem does not overclaim on irreducibility, prescribed nonzero fiber,
  all-component dominance, injectivity, reducedness, transversality, or
  closed-point intersection multiplicity.
- All twelve proof bridges appear in the main text and align with the theorem:
  finite-free loop algebra, Jacobian criterion, cyclic quotient, scalar
  identification, Gorbovickis input, component separation, block
  differential, fixed-`b` spreading, formal completion, differential/Fitting
  base change, Cartier-or-empty multiplicity control, and residual
  `\\mu_{d-1}` symmetry.
- The finite-free lemma and Appendix A correctly include the `n=1` and `n=2`
  coincident-index relations and repeatedly block the forbidden inference that
  rank `d^n` counts exact cycles or proves irreducibility.
- The degree-two guard is correctly preserved: the proof uses Gorbovickis
  Theorem 1.6 and Lemma 2.1, not the later degree-at-least-three corollary.
- The determinant/eigenvalue guard is correct:
  `det(DH_{b,p}^{n_i})=(-b)^{n_i}` supports only the unordered eigenvalue pair
  once the determinant is known.
- The exact A1--A20 anti-claim ledger appears intact at source lines
  1473--1492 and is not contradicted elsewhere in the paper.

### 4. PDF content, layout, metadata, fonts, and security

- `paper/main_round0.pdf` is a 23-page letter PDF. Independent text extraction
  shows 22 nonempty content pages followed by exactly 1 nonempty final
  references page.
- Every page is nonempty. The page-by-page extraction showed continuous public
  mathematical or bibliographic content on all pages 1--23.
- Visual spot-check rendering of representative pages 1, 9, 22, and 23 showed
  clean layout: title/abstract page, proof-table page, appendix-ending page,
  and final references page all render normally with no clipping or blank-page
  anomaly.
- PDF metadata are anonymous and compliant: title exact, author blank, subject
  blank, keywords blank, creator blank, creation/modification dates absent,
  producer `pdfTeX-1.40.22`, encryption off.
- `pdffonts` reports 22 fonts; every font is embedded, subset, and Unicode
  mapped.
- `pdfimages -list` reports zero image XObjects. `pdfdetach -list` reports zero
  embedded files. `pdfsig` reports zero signatures.
- Independent PDF inspection found only ordinary internal GoTo navigation links
  and one bibliographic URI link to the Stacks Project on the references page.
  I found no forbidden AcroForm, XFA, JavaScript, JS, Launch, RichMedia,
  FileAttachment, embedded-file, external-file-action, signature, image-XObject,
  or trailer-ID token.

### 5. Public-text hygiene

- Source grep found no TODO/FIXME/XXX/VERIFY markers, no draft placeholders,
  and no leaked governance or internal-operation text in the two public source
  files.
- The manuscript is anonymous and free of author identity, grant,
  acknowledgment, repository identity, submission ID, internal paper number,
  prompt text, or hidden workflow narrative.
- The comparison section remains a bounded scope comparison through 2026-08-17,
  not an absolute-priority claim.

## Findings

No required findings.

No cosmetic findings.

## Disposition

The manuscript satisfies the Round-1 review contract on its current Round-0
artifacts. This review authorizes no source change by itself, no release, no
submission, no identity disclosure, and no external effect. It records only
that the current Round-0 package passes the independent R1 manuscript audit.

MANUSCRIPT_R1_PASS
