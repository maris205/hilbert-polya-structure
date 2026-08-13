# Integrity pre-review

**Status:** `PRE_REVIEW_PASS`  
**Document date:** 2026-08-14  
**Integrity runtime:** 2026-08-13 UTC container clock  
**Scope:** author-side integrity and evidence-boundary check before an
independent manuscript review; this is not an independent or final review.

The one-day date difference is intentional and transparent: the source lock,
paper plan, and manuscript carry frozen research-document metadata, whereas
runtime records use the actual UTC clock exposed by the container.

## Frozen evidence closure

- The prospective source lock remains byte-identical at SHA-256
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.
- All 35 artifacts in `results/final_result_manifest.json` were rehashed at
  the paper stage without rewriting the official results; 35/35 paths and
  hashes match.
- `results/run_summary.json` remains
  `PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION`: eight registered entries
  pass, controls precede every Hénon static stage, and the candidate gate is
  closed.
- The frozen official JUnit XML records 82 tests, zero failures, and zero
  errors.  Its SHA-256 is
  `c29e6bc5f805f32d9a9620dfad42bfe9474973f430c857531970e0f28782fa62`.
- Candidate parameter substitution, candidate periodic-point computation,
  candidate action computation, external prime-table access, and Riemann-zero
  data access all remain false.  No official result was regenerated during
  paper production.

## Claim/evidence alignment

| Gate | Result |
|---|---|
| Regular finite algebraic evaluation is proved for every finite period | PASS |
| Hermite--Lindemann is applied only to exact logarithms of nontrivial algebraic targets | PASS |
| `beta=0` and the algebraic `beta=1, A=0` exception are explicit | PASS |
| Algebraic scale/average/repetition/real/imaginary/modulus extensions are separated from `log|A|` | PASS |
| General gauge formula retains `chi_n(P_n)-chi_0(P_0)+sum_j C_j` | PASS |
| Algebraic endpoint mismatch is retained rather than silently declared compatible | PASS |
| Symbolic identity-map `G=log(2)` control exposes the transcendental-normalization boundary | PASS |
| Exact Hénon potential and type-1 generating function have opposite sign on the graph | PASS |
| Hénon finite periodic-point algebraicity has an all-period no-infinity proof | PASS |
| Orbit field and extension of places are explicit in the S-integral statement | PASS |
| Only `3*A_G` is claimed S-integral; exact `-1/3` control is present | PASS |
| Static JSON is labeled an implementation audit and never empirical proof of the theorem | PASS |
| Universal symplectic, `log|A|`, multiplier, return, multivalued, closed-nonexact, transcendental, and approximate nonclaims are explicit | PASS |

The machine-readable mapping is in `CLAIM_MANIFEST.json`; the official-run
mapping is in `EXPERIMENT_PASSPORT.json`.  The route decision is exactly
`GO_AS_NARROW_DESIGN_CERTIFICATE`, closing only the frozen normalized
algebraic absolute-action prime-log route.  The publication boundary remains
`MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`.

## Bibliography closure

- Thirteen cited bibliography records were checked against DOI, arXiv, or
  publisher metadata; claim-level safe-use restrictions are documented in
  `../notes/PAPER_CITATION_AUDIT.md`.
- The compiled auxiliary file contains 13 unique citation keys and
  `references.bib` contains exactly those 13 entries: zero missing and zero
  unused entries.
- The 2024 Hénon survey uses its publisher-listed collective author, Julia
  Xénelkis de Hénon.  The Cambridge edition credits Alan Baker as author and
  David Masser for the foreword.
- No citation substitutes for the paper-specific proof, and no
  historical-first claim is made.  There are no `[VERIFY]`, `TODO`, or
  placeholder records.

## Figure integrity

- Three publication figures have PDF and SVG vector masters plus PNG review
  copies.
- Categorical scientific statuses are loaded from the frozen JSON package by
  `figures/frozen_data.py`; the Hénon and gauge formulas are the frozen static
  identities audited by that package.
- The loader rejects a changed source lock, incomplete registry, failure of
  proof/control/isolation checks, controls-order drift, any opened candidate
  gate, or prime/zero access.
- All three PNG renderings were inspected at original resolution, and all 12
  compiled pages were rendered and visually inspected.
- Two consecutive full figure regenerations produced 9/9 identical SHA-256
  hashes.  `FIGURE_PACKAGE.json` records every input, generator, and output
  hash.

## Compilation integrity

Build command:

```bash
paper/build.sh
```

The build fixes `SOURCE_DATE_EPOCH`, runs BibTeX, and performs four
`pdflatex` passes.  Final checks:

| Check | Result |
|---|---|
| PDF pages | 12 total; conclusion ends on page 10 |
| PDF size | letter, 612 × 792 pt |
| LaTeX errors / final warnings | 0 / 0 |
| Overfull / underfull boxes | 0 / 0 |
| Undefined references / citations | 0 / 0 |
| Citation-key closure | 13/13 |
| Fonts embedded and subset | PASS |
| Full-PDF visual inspection | PASS, 12/12 pages |
| Consecutive deterministic builds | identical SHA-256 |
| Manuscript and frozen snapshot hashes | identical |
| Pre-review PDF SHA-256 | `2e8f2cef866f06e219fb0d582aec8ad4a1403b26e61cf8f44549dbc4f8399742` |

## Primary artifact hashes

| Artifact | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `a701aeaa56c921b00b07e2e34b3b61f063f534b92693bbdc09f1dbfa0d66e62c` |
| `paper/manuscript.tex` | `1e4f477c20609e520baa9342a133493fbe031aa659e5517ba1d17763b706b60e` |
| `paper/paper_pre_review.pdf` | `2e8f2cef866f06e219fb0d582aec8ad4a1403b26e61cf8f44549dbc4f8399742` |
| `paper/references.bib` | `c28e546aba7bf3beb6c18f3da40cc0d8c410b2e38e167ac44c5b3624cf5b88a0` |
| `notes/PAPER_CITATION_AUDIT.md` | `cc348ae8c9e793818f0fd2b56cd4f94a17948d6fc31444eccd84279f628671a6` |
| `paper/PAPER_CONFIGURATION.md` | `de5218a57daab9c53bb0d679a63a55ea245b43bfcdff1f2aa9e3dba6bc780e52` |
| `paper/CLAIM_MANIFEST.json` | `9cc2469397615e47640bfa99b016a602b67dd10d2a0dd242067bbe8b33b0c783` |
| `paper/EXPERIMENT_PASSPORT.json` | `f96320eb8fe5b1bd48e9b4b4946f1bb0b8def70c75893c342ca34edb95cb4899` |
| `paper/FIGURE_PACKAGE.json` | `680f846c10b9ce642640b869ea2f3bed82502db874ec6984a731cca44cb8ad1d` |
| `paper/PIPELINE_STATE.json` | `4a5ca3b06d2928642e5e560b74c2e861521def8fe2e72c4bcb0484af883511da` |
| `results/final_result_manifest.json` | `6b3dbfed68dbd058056c35139756d5ccbb4e9f3b9a263ccaddef64bb183326e7` |

## Handoff boundary

The article is ready for an independent manuscript reviewer.  No independent
manuscript review or auto-improvement loop was performed in this production
thread, and no submission-readiness claim is made.  Review-driven repairs,
a clean recompile, and a final post-review integrity check remain pending.
