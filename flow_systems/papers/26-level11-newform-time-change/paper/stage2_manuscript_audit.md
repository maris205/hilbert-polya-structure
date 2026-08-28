# Paper 26 — ARS Stage 2 manuscript audit

Audit date: **2026-08-28**
Manuscript: **Exact Newform-Period Taxonomy for a Level-11 Time Change of the Modular Geodesic Flow**
Stage verdict: **ARS Stage 2 draft complete; Stage 2.5 awaits explicit user confirmation.** This audit does not claim Stage 2.5 approval, reviewer acceptance, Route-A A2 passage, or Route-B authorization.

## 1. Frozen identity and claim boundary

- Author: Liang Wang.
- Affiliation: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China.
- Email: `wangliang.f@gmail.com`.
- Frozen object: the positive time change of the level-11 modular geodesic flow with infinitesimal clock given by the real part of the unique normalized weight-two level-11 newform differential.
- Frozen finite population: 11 source owners, five primes, 55 source/prime groups, and 138 Hecke permutation-cycle owner instances.
- Paper-level positive result: an exact owner theorem, an all-parameter quadratic degree-moment criterion, and an exhaustive exact rational-homology taxonomy of the frozen population.
- Paper-level negative result: each of the predeclared primary laws `a_p` and `a_p^2` fails exactly 51/55 groups; the control `a_p^2-p` fails 55/55 groups.
- Explicit exclusions retained: no full primitive-conjugacy census, no global dynamical determinant, no analytic continuation or functional equation, no prime-to-orbit target fitting, no Riemann-zero data, no quantum/operator realization, and no Route-B claim.
- Route-A language is unchanged and conservative: `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`.

The manuscript is consistent with `BATCH_ROUND9_MANUSCRIPT_FREEZE.md` and `skills/route-a-evaluator.md`. The exact finite result is not generalized beyond the locked multiset.

## 2. Deliverable and structure check

| Check | Result |
|---|---|
| `manuscript.tex` | Present; complete English paper with mathematical proofs and declarations |
| `references.bib` | Present; 5 auditable entries |
| `paper.pdf` | Present; 12 pages |
| English abstract | 239 words; within the required 150–300 range |
| Traditional Chinese abstract | 359 Han characters; independent summary within the required 300–500-character range |
| Keywords | 6 English and 6 Traditional Chinese keywords |
| English body | 4,729 source-aware English tokens from Introduction through Conclusion; conservative `detex` visible-text count 4,165 words |
| Research question | Explicitly stated in the Introduction |
| Definitions/background | Level-11 form, time change, owner, Hecke branch owner, product conventions, and exact homology model |
| Related work | Dedicated bounded-positioning section |
| Main results | 5 propositions/corollaries and 4 theorems, all with proofs or exact-enumeration proof protocol |
| Computation/certificate | Locked inputs, exact arithmetic hierarchy, deterministic rebuild, tree hash, and fail-closed behavior |
| Adversarial/Route-A discussion | Dedicated section with same-owner and inverse-pair proves-too-much controls |
| Limitations/conclusion | Dedicated sections; finite/global quantifiers separated |
| Declarations | Data/Code, Ethics, CRediT contributions, Conflict of Interest, Funding, and AI disclosure all present |

Counting method: comments and citation commands were excluded; visible English alphanumeric/hyphenated tokens were counted between `\section{Introduction}` and `\section*{Data and Code Availability}`. The second count is the same region passed through `detex | wc -w`. Han characters were counted only in the independent Traditional Chinese abstract.

## 3. Claim-support and proof audit

The manuscript's central claims are supported internally rather than outsourced to citations:

1. period variation, conjugacy invariance, orientation sign, and traversal repetition are proved directly from one-form integration;
2. the Hecke cycle-pushforward identity is proved by pairing the correspondence with the cycle and explicitly rebuilding each branch-cycle owner;
3. the first/second log-product variations and the all-`s` degree-moment criterion are proved by differentiation, power-series coefficient comparison, and Möbius inversion;
4. the exact period coordinate `k=2y+z` is derived from the rational Schreier model and real involution;
5. the 138-instance and 55-group claims are tied to integer/rational reconstruction, frozen population counts, source hashes, and deterministic exact enumeration;
6. the four positive groups are described as compact-homology or real-projection kernels, not as arithmetic validation cases.

No theorem depends on a numerical near-zero test. The maximum inherited floating-point residual is reported only as a cross-check and is explicitly excluded from the proof.

## 4. Citation integrity audit

All five bibliography records were checked against a primary paper or official metadata page on 2026-08-28.

| Key | Existence/metadata check | Manuscript claim supported | Local locator |
|---|---|---|---|
| `lmfdb112aa` | Official [LMFDB newform orbit 11.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/) | level, weight, dimension, rational coefficient field, q-expansion, eta quotient | `Properties and q-expansion` |
| `manin1972` | DOI [10.1070/IM1972v006n01ABEH001867](https://doi.org/10.1070/IM1972v006n01ABEH001867) | modular-symbol and weight-two period setting | pp. 19–25 |
| `merel1991` | DOI [10.5802/aif.1264](https://doi.org/10.5802/aif.1264) | explicit Hecke action on relative homology/modular symbols | Introduction and Sections 1–2 |
| `ruelle1976` | DOI [10.1007/BF01403069](https://doi.org/10.1007/BF01403069) | primitive-periodic-orbit zeta organization | Introduction and flow case |
| `fried1986` | DOI [10.24033/asens.1515](https://doi.org/10.24033/asens.1515) | prime periodic orbits versus iterates in Ruelle/Selberg product bookkeeping | Section 2 |

Integrity results:

- citation occurrences: 5;
- unique cited keys: 5;
- bibliography entries: 5;
- missing bibliography keys: 0;
- uncited/orphan bibliography entries: 0;
- citations without an optional locator: 0;
- citations without an adjacent `% Source locator:` audit comment: 0;
- fabricated or unverified DOI records found: 0.

The Ruelle DOI was checked as `10.1007/BF01403069`; the manuscript does not reproduce the erroneous terminal digits present in an older local note.

## 5. Reproducibility and regression audit

Commands were run with `PYTHONDONTWRITEBYTECODE=1`.

1. From `code/`: `python3 -m unittest discover -v`
   Result: **74/74 tests passed**. This is the complete historical Round 2–8 test discovery for Paper 26.
2. From the paper root: `bash experiments/reproduce_round8.sh` with no refresh flag
   Result: **18/18 Round-8 tests passed**, status `REPRODUCIBLE (verify)`, checked-in artifact tree SHA-256 `cc36c1f952c9ce89050996f4bb4c9905571f9ef09a0d7115be8a985e02a5621d`.
3. Cache check after testing: no `__pycache__/` directory and no `.pyc` file under the Paper 26 tree.

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
- overfull/underfull boxes in final log: 0;
- English and Traditional Chinese first-page rendering visually inspected;
- the generated, Git-ignored `paper/paper.log` was checked after the final build; `paper/paper.pdf` is the publication artifact.

## 7. Final file hashes

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` |
| `references.bib` | `9b061c02006f07f1c93df68d8577d44906122f55db71e6f529f43cf3f6483ed8` |
| `paper.pdf` | `b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa` |

PDF size: **250,485 bytes**.

Independent read-only scientific review found **0 Blocker, 0 Major, and 0
Minor** findings. The reviewer independently reproduced the 138-instance
taxonomy, all 165 group/law verdicts, 74/74 historical tests, and the 18/18
Round-8 verify-only suite. The unified post-review four-pass build and root
structural audit are clean.

## 8. Residual limitations and Stage 2.5 handoff

The smallest remaining finite task is cross-instance `Gamma_0(11)` conjugacy canonicalization. Larger tasks—complete primitive enumeration and a global determinant with analytic control—remain unestablished. The present manuscript is a complete, auditable Stage 2 draft for the frozen theorem and obstruction, but **Stage 2.5 has not been passed**. It awaits explicit user confirmation of content and citations before any review-stage promotion.
