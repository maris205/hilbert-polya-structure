# Paper 27 — ARS Stage 2 manuscript audit

Audit date: **2026-08-28**
Manuscript: **Renormalization Obstructions in Congruence and Homology Towers of Geodesic Flows**
Stage verdict: **ARS Stage 2 draft complete; Stage 2.5 awaits explicit user confirmation.** This audit does not claim Stage 2.5 approval, reviewer acceptance, Route-A A2 passage, or Route-B authorization.

## 1. Frozen identity and claim boundary

- Author: Liang Wang.
- Affiliation: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China.
- Email: `wangliang.f@gmail.com`.
- Original candidate: coordinatewise geodesic flow on a descending normal residual tower with a common physical arclength clock.
- Separate calibrator: `P27-HOMOLOGY-RENORMALIZED-GEODESIC-PANEL`, using pure genus-two homology covers, a declared `1/N` clock, and a declared `1/N^3` logarithmic multiplicity normalization.
- Paper-level negative result: the residual inverse-limit flow has no periodic point; each fixed owner's quotient orders and physical lifted periods escape, and its Euler factor becomes 1 in every fixed coefficient prefix.
- Paper-level positive calibration: for a primitive content-one owner, homology covers have degree `N^4`, deck order `N`, `N^3` primitive components, and period `N ell(g)`; only simultaneous clock and multiplicity normalization recovers the base factor.
- Explicit exclusions retained: the homology tower is nonresidual; the identity is fixed-finite-panel and generic; there is no prime owner map, no global primitive spectrum/determinant, no target fitting, no Riemann-zero data, no analytic continuation/functional equation, and no operator lift.
- Original candidate Route-A tuple: `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.
- Calibrator tuple: `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)`, also `ROUTE_A_REJECTED`.

The manuscript is consistent with `BATCH_ROUND9_MANUSCRIPT_FREEZE.md` and `skills/route-a-evaluator.md`. It does not treat the positive calibrator as a rescue of the residual inverse-limit owner.

## 2. Deliverable and structure check

| Check | Result |
|---|---|
| `manuscript.tex` | Present; complete English paper with mathematical proofs and declarations |
| `references.bib` | Present; 5 auditable entries |
| `paper.pdf` | Present; 12 pages |
| English abstract | 234 words; within the required 150–300 range |
| Traditional Chinese abstract | 389 Han characters; independent summary within the required 300–500-character range |
| Keywords | 6 English and 6 Traditional Chinese keywords |
| English body | 4,593 source-aware English tokens from Introduction through Conclusion; conservative `detex` visible-text count 4,052 words |
| Research questions | Owner-preserving no-go and separately declared renormalized rescue stated in the Introduction |
| Definitions/background | Period owner, quotient order, residual tower, coefficientwise owner variable, homology calibrator, and renormalization quadrants |
| Related work | Dedicated prior-work and bounded-positioning section |
| Main results | 1 definition, 1 lemma, 2 propositions, and 4 theorems with complete proofs |
| Computation/certificate | Three artifact families kept separate; exact integers, binomial coefficients, source locks, deterministic two-tree verification |
| Adversarial/Route-A discussion | Dedicated section plus internal four-quadrant and nonarithmetic proves-too-much controls |
| Limitations/conclusion | Dedicated sections; fixed-panel, nonnormal-chain, and limit/product restrictions explicit |
| Declarations | Data/Code, Ethics, CRediT contributions, Conflict of Interest, Funding, and AI disclosure all present |

Counting method: comments and citation commands were excluded; visible English alphanumeric/hyphenated tokens were counted between `\section{Introduction}` and `\section*{Data and Code Availability}`. The second count is the same region passed through `detex | wc -w`. Han characters were counted only in the independent Traditional Chinese abstract.

## 3. Claim-support and proof audit

The central statements have complete internal proofs:

1. residual-tower aperiodicity and quotient-order divergence follow from coherence, normality, residual intersection, and divisibility of quotient orders;
2. the projective-sign issue for `Gamma(3n!)` is resolved explicitly rather than assumed;
3. the cocompact control separates residuality/common clock from cusp and congruence features;
4. fixed-prefix factor escape follows from the increasing first supported degree in the owner variable;
5. the homology-cover degree, order, lift count, lift period, and lift primitivity are derived from `H_1(Sigma;Z)=Z^4`, content one, deck translation, and cyclic centralizers;
6. the four quadrants and the uniqueness of `1/N` and `1/N^3` within scalar clock/exponent renormalizations are proved exactly for all `N`;
7. finite ledgers are presented as reproducible illustrations/certificates and never as empirical proofs of the infinite theorems.

The manuscript distinguishes whole-loop closing diagnostics from primitive minimal periods for the three cusped rows whose full conjugacy-primitivity remains unproved.

## 4. Citation integrity audit

All five bibliography records were checked against a primary paper or authoritative preprint/metadata page on 2026-08-28.

| Key | Existence/metadata check | Manuscript claim supported | Local locator |
|---|---|---|---|
| `martinez2016` | DOI [10.3934/jmd.2016.10.113](https://doi.org/10.3934/jmd.2016.10.113) | leafwise geodesic/horocycle framework and explicit aperiodic/universal-solenoid examples | Section 2.2 and Examples 4, 6 |
| `penner2008` | DOI [10.1007/s10711-007-9226-9](https://doi.org/10.1007/s10711-007-9226-9) | punctured-solenoid construction through finite modular covers and disk leaves | Introduction and Definition 2.1 |
| `alcalde2026` | DOI [10.4171/GGD/967](https://doi.org/10.4171/GGD/967) | finite-type hyperbolic solenoidal surfaces and leafwise flow/tower terminology | Definitions 4, 5, and 7 |
| `hurder2019` | DOI [10.1090/tran/7339](https://doi.org/10.1090/tran/7339) | relation between group-chain intersection and leaf fundamental group in compact weak solenoids | Definition 5.5 |
| `nica2013` | Primary exposition [arXiv:1306.2385](https://arxiv.org/abs/1306.2385) | Malcev residual-finiteness theorem for finitely generated linear groups | p. 1 |

Integrity results:

- citation occurrences: 5;
- unique cited keys: 5;
- bibliography entries: 5;
- missing bibliography keys: 0;
- uncited/orphan bibliography entries: 0;
- citations without an optional locator: 0;
- citations without an adjacent `% Source locator:` audit comment: 0;
- fabricated or unverified DOI records found: 0.

Electronic verification of existence and claim support is complete. It is not represented as `USER_ATTESTED_READ`; the manuscript remains at the Stage 2.5 confirmation gate.

## 5. Reproducibility and regression audit

Commands were run with `PYTHONDONTWRITEBYTECODE=1`.

1. From `code/`: `python3 -m unittest discover -v`
   Result: **58/58 tests passed**. This is the complete historical Paper 27 test discovery across the available Round 2 and Round 4–8 modules.
2. From the paper root: `bash experiments/reproduce_round8.sh` with no refresh flag
   Result: **12/12 Round-8 tests passed**, 96 quadrant rows, 1,248 coefficient rows, core SHA-256 `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`, and checked-in artifacts `VERIFIED`.
3. Cache check after testing: no `__pycache__/` directory and no `.pyc` file under the Paper 27 tree.

The verify-default run did not refresh or rewrite research artifacts.

## 6. Typesetting audit

Build sequence from `paper/`:

```text
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

- engine/style: LuaLaTeX + BibTeX, `natbib`, `plainnat`, numeric citations;
- result: successful, 12-page PDF, PDF 1.5;
- LaTeX errors: 0;
- undefined citations/references: 0;
- BibTeX warnings: 0;
- overfull boxes: 0;
- overfull and underfull boxes in the final post-review log: 0;
- English and Traditional Chinese first-page rendering visually inspected;
- the generated, Git-ignored `paper/paper.log` was checked after the final build; `paper/paper.pdf` is the publication artifact.

## 7. Final file hashes

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` |
| `references.bib` | `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981` |
| `paper.pdf` | `540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a` |

PDF size: **243,701 bytes**.

Independent read-only scientific review found **0 Blocker and 0 Major**
issues. Its only Minor was a cosmetic underfull bibliography line. A scoped
ragged-right bibliography removed that warning without changing content. The
post-patch final log, 58/58 historical tests, 12/12 Round-8 replay, and root
structural audit are clean.

## 8. Residual limitations and Stage 2.5 handoff

The no-period theorem is restricted to normal residual towers with a common clock. The three cusped finite rows do not claim full conjugacy-primitivity. The positive homology-cover identity is fixed-panel, nonresidual, generic, and does not justify an infinite product/tower-limit interchange. A growing-panel convergence theorem, an arithmetic owner mechanism, a global determinant, and all A3–A4 obligations remain absent. The present manuscript is a complete, auditable Stage 2 draft for the frozen comparative result, but **Stage 2.5 has not been passed** and awaits explicit user confirmation.
