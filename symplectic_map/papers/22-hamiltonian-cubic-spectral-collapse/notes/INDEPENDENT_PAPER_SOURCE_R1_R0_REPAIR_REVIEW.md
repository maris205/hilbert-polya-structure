# Paper 22 — Independent Repaired-Source Review R1 of the R0 Hyperref Repair

## Reviewer identity, scope, independence, and skill used

Review date: 2026-08-24 UTC.

I am a fresh independent repaired-source reviewer for Paper 22. I did not
author `paper/main.tex`, `paper/math_commands.tex`, `paper/references.bib`,
`notes/BUILD_R0_BLOCKER.md`, `notes/R0_HYPERREF_SOURCE_REPAIR.md`, or the
historical review `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`. I did not
contact any earlier agent or reviewer.

I read the full applicable research-review skill at
`/root/.codex/skills/skills-codex/research-review/SKILL.md` and used it only
as a local, non-delegated review protocol because the frozen repaired-source
authorization controlled this turn more strictly than the generic skill loop.

Per the frozen protocol, I performed no browsing, no compilation, no TeX or
BibTeX run, no CAS, no symbolic package use, no scientific experiment, no
source edit, no batch-ledger edit, and no filesystem modification except this
single review artifact.

## Opening root gate and project state

At reviewer opening, the live root authorization gate was exactly
`PAPER22_REPAIRED_SOURCE_DUAL_REVIEW_OPEN` in `BATCH_06_STATUS.md`.

The opening root bindings matched the frozen prompt exactly:

| Path | SHA-256 |
|---|---|
| `BATCH_06_STATUS.md` | `5857b0989d805f91e38d50c61fb0e8b1c0822b11364fa1460a5fa9d4ae5a8443` |
| `BATCH_06_IDEA_REPORT.md` | `dbc590e08ef66f8f1741282d67b76a85d193f37025f3e704d24c81336ad4e09a` |

I independently recomputed the pre-review Paper 22 project inventory before
writing:

- regular files: `25`
- child directories: `4`
- symlinks: `0`

The four child directories were exactly `experiments`, `notes`, `paper`, and
`refine-logs`. The authorized review path
`notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` did not exist at
opening.

## Bound repaired-source, old-source, blocker, and receipt identities

### Repaired source trio

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69241 | 1921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1928 | 55 |

### Old main, historical blocker, historical old-source review, and repair receipt

| Path | SHA-256 | Bytes | LF | Terminal line |
|---|---|---:|---:|---|
| `/tmp/paper22-r0-A.PIwA2V/main.tex` | `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e` | 69218 | 1921 | — |
| `notes/BUILD_R0_BLOCKER.md` | `5242052c625add4ba084d5542faae221e6b1a1cb6d81b773b9295d968afbc7fd` | 5873 | 145 | `R0_BLOCKED` |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `d38343539db88d1eeda555c464657e408df6ab58aa6ad7a811cd262f53038750` | 17056 | 424 | `PAPER_SOURCE_R1_PASS` |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `0587269d6e5fcd4461a4749b6846d459c096d698dd460d2f4abf291463934ed5` | 7553 | 189 | `SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED` |

I treated the historical blocker and old-source review as immutable evidence
only. I did not transfer PASS status from the old-source review to the repaired
bytes.

## Stable project evidence inspected and rebound

I read and rebound the following stable project evidence needed for the
repaired-source decision:

- `experiments/source_lock.json`
  - SHA-256 `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88`
  - 32258 bytes, 1 LF
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
  - SHA-256 `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f`
  - 16605 bytes, 521 LF
  - terminal `SOURCE_LOCK_PASS`
- `paper/PAPER_PLAN.md`
  - SHA-256 `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224`
  - 34692 bytes, 952 LF
- `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`
  - SHA-256 `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c`
  - 10683 bytes, 248 LF
  - terminal `PAPER_PLAN_PASS`
- `notes/PUBLICATION_STAGE_SCOPE.md`
  - SHA-256 `49b17a22be1a774f5befbce67f54d1770d8277bd179a4a7ec728e4f55a59eeeb`
  - 21397 bytes, 561 LF
- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`
  - SHA-256 `65bfe3d7e24c6f9f4ec6a826f2d29a387c0105e208f4990226a4d22242f24512`
  - 16536 bytes, 388 LF
  - terminal `PUBLICATION_STAGE_PASS`
- `experiments/publication_lock.json`
  - SHA-256 `3d7eb3c7ef143a17c1ccdb82ece985a05c916b78c1ebe0591bca8af3c05ce6cd`
  - 34222 bytes, 1 LF
- `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`
  - SHA-256 `21a35057011098de88b03518cbb4e24a27ee1cb998303e526fcd128188c99fa8`
  - 17031 bytes, 350 LF
  - terminal `PUBLICATION_LOCK_PASS`
- `notes/CITATION_VERIFICATION.md`
  - SHA-256 `d2b89b3313d54e612c3aa6e1e0a454c034d312268fd431217638417d90afa2bc`
  - 4916 bytes, 65 LF
- `notes/CLAIMS_EVIDENCE_MATRIX.md`
  - SHA-256 `b1184e0dffd4ccd633e9ced15c227e5bad3e9074627fd7442bd78896c1f48416`
  - 6915 bytes, 94 LF
- `notes/NOVELTY_ASSESSMENT.md`
  - SHA-256 `dbd33f68af27f0ba57982e5bb6f2dde8d01099188e2d240e0319199ee52b2699`
  - 7486 bytes, 140 LF
- `notes/PROOF_PACKAGE.md`
  - SHA-256 `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846`
  - 23639 bytes, 951 LF
- `notes/RESEARCH_QUESTION.md`
  - SHA-256 `fc2269c6abe58b077b1c0b33bf07f93661f59a2ca72733330b9d67c38cb63175`
  - 5266 bytes, 138 LF

These files agreed on the same frozen theorem scope: arbitrary
characteristic-zero field `K`, integer range `r>=4`, `g>=2r+1`, phase order
`F=T∘S`, exact complete-step matrix `C=BA`, strict visibility only for `n>=1`,
tied initial case `n=0`, cubic-annihilator-only language, seed/selected-face
sharpness at `g=2r`, formal `r=3` consistency only, and the four-nonzero-
coefficient fixed-support extension.

## One-line diff proof and unchanged-companion proof

I independently compared the repaired `paper/main.tex` against the frozen old
main at `/tmp/paper22-r0-A.PIwA2V/main.tex`. The unified diff contains exactly
one hunk and exactly one semantic line replacement:

```diff
-\subsection{The \(g=2r\) seed/selected-face boundary}
+\subsection{The \texorpdfstring{\(g=2r\)}{g=2r} seed/selected-face boundary}
```

I also verified all of the following source-side facts independently:

1. the target old heading occurred exactly once;
2. the repaired heading occurs exactly once, at line 1754;
3. no other line in `paper/main.tex` differs from the old main;
4. `paper/math_commands.tex` remained exactly
   `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c`; and
5. `paper/references.bib` remained exactly
   `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d`.

Thus the repaired public-source package differs from the frozen pre-repair
package only by the single authorized heading repair in `paper/main.tex`.

## Independent mathematical replay on the repaired source

The repair does not alter any theorem text or proof line, but I still replayed
the theorem-critical chain against the repaired bytes rather than inheriting
the historical PASS.

### 1. Family, gradients, inverses, and symplecticity

The manuscript states exactly the fixed family

- `V_{r,g}(q)=prod_i q_i^2+q_1^g`,
- `W_{r,g}(p)=prod_i p_i^2+p_r^g`,
- `S(q,p)=(q,p+∇V_{r,g}(q))`,
- `T(q,p)=(q+∇W_{r,g}(p),p)`,
- `F_{r,g}=T∘S`.

With `h=g-1` and `m=r-2`, the derivative ledger in §2 is correct:

- `∂V/∂q_1 = 2 q_1 prod_{j=2}^r q_j^2 + g q_1^{g-1}`,
- `∂V/∂q_i = 2 q_i prod_{j!=i} q_j^2` for `2<=i<=r`,
- `∂W/∂p_i = 2 p_i prod_{j!=i} p_j^2` for `1<=i<r`,
- `∂W/∂p_r = 2 p_r prod_{j=1}^{r-1} p_j^2 + g p_r^{g-1}`.

The subtraction inverses

- `S^{-1}(q,p)=(q,p-∇V_{r,g}(q))`,
- `T^{-1}(q,p)=(q-∇W_{r,g}(p),p)`

are exact. The block Jacobians

- `J_S=[[I,0],[H_V,I]]`,
- `J_T=[[I,H_W],[0,I]]`

preserve `ω=sum_i dq_i∧dp_i` because both Hessians are symmetric, so the
symplectic proof remains correct and unchanged.

### 2. Exact support rows, selectors, and complete-step matrix

For a positive degree vector `u`, the mixed row score is

`u_i + 2 sum_{j!=i} u_j = 2 sum_j u_j - u_i`,

so the mixed matrix is exactly `M=2 11^T-I_r`. The only competitive rows are
the first `V` row and the last `W` row. Therefore:

- `A` is `M` with row `1` replaced by `h e_1^T`,
- `B` is `M` with row `r` replaced by `h e_r^T`,
- the complete-step matrix is `C=BA`, never `AB`.

The normalized variables are used exactly as locked:

- `x_i=u_i/u_1` only for `2<=i<=r`,
- `sigma=sum_{i=2}^r x_i`,
- `x_1` is excluded.

The first selector margin is

`h u_1 - (u_1 + 2 sum_{i=2}^r u_i) = u_1(h-1-2 sigma)`.

For `v=Au`, the intermediate normalization is

- `v_1/u_1 = h`,
- `v_i/u_1 = 2 + 2 sigma - x_i` for `2<=i<=r`.

The second selector is correctly applied to `v=Au`, not directly to `u`. Its
pure-minus-mixed margin is

`Delta_T/u_1 = (2h-4m)sigma - (h+1)x_r - 4m - 2`.

Using `x_r<=sigma-m`, this reduces to

`Delta_T/u_1 >= (h-4m-1)sigma + m(h-3) - 2`.

I independently checked both sign cases:

- if `h-4m-1<0`, then
  `Delta_T/u_1 > ((h+1)(h-2m-3))/2 > 0`;
- if `h-4m-1>=0`, then
  `Delta_T/u_1 >= (2m+1)(h-2m-3) > 0`.

Both are strict because `h>=2m+4`, so `h-2m-3>=1`. The least-parameter edge
case `h=2m+4` therefore remains valid.

I also recomputed `C=BA` row by row and confirmed the exact ledger:

- first row:
  `C_11=h+4m+4`, `C_1j=4m+2` for `2<=j<=r`;
- middle rows `2<=i<r`:
  `C_i1=2h+4m+2`,
  `C_ij=4m+delta_ij` for `2<=j<=r`;
- last row:
  `C_rj=2h` for `1<=j<r`, `C_rr=h`.

### 3. Seed, cone invariance, carried coordinates, and leading forms

The seed and cone are still exactly the frozen ones:

- `K_{r,g}={u>0 : x_i>=1 for 2<=i<=r and sigma<(h-1)/2}`,
- `sigma(1)=r-1=m+1<(h-1)/2`,
- the theorem range is `r>=4`, `g>=2r+1`, hence `m>=2`, `h>=2m+4`.

For the cone walls, I independently checked:

- every middle lower wall:
  `((Cu)_i-(Cu)_1)/u_1 = (h-1-2 sigma) + (x_i-1) > 0`;
- the last lower wall:
  `L_1 = h-4m-4 + (2h-4m-2)sigma - h x_r`,
  giving the strict bounds
  `((h+2)(h-2m-3))/2` and `2(m+1)(h-2m-3)` in the two sign cases;
- the height wall:
  `H_2=(h-1)(Cu)_1 - 2 sum_{i=2}^r (Cu)_i`,
  with
  `H_2/u_1 >= (h-2m-3)(h+4m^2+4m+2) > 0`.

At the least parameter `h=2m+4`, every decisive factor `h-2m-3` equals `1`,
so there is no hidden threshold equality.

For the carried-coordinate induction, the exact positivity facts remain
correct:

- `C-I_r > 0` entrywise,
- `A 1 > 1`,
- every row of `A` is nonnegative and nonzero.

Hence

- `Au_n > Au_{n-1} = v_n`,
- `BAu_n - u_n = (C-I_r)u_n > 0`,

which gives the actual half-step recurrence

- `v_{n+1}=Au_n`,
- `u_{n+1}=Cu_n`.

The noncancellation argument is still correctly located in the polynomial
domain:

- `LH(fg)=LH(f)LH(g) != 0`,
- if `deg f > deg g`, then `LH(f+g)=LH(f)`.

The manuscript does not replace this with a positivity-of-coefficients
shortcut, so the fixed-support arbitrary-nonzero-coefficient corollary remains
logically supported.

### 4. Strict visibility for `n>=1`, tied `n=0`, and exact degree

The visibility split is still stated with the correct edge case:

- strict last-coordinate visibility only for `n>=1`,
- tied initial case at `n=0`,
- exact degree identity for all `n>=0`.

I independently checked the matrix comparison `C-A>0` entrywise:

- first row difference:
  `(4m+4,4m+2,...,4m+2)`;
- middle row difference:
  first entry `2h+4m`, entries `4m-2+2 delta_ij` for `j>=2`;
- last row difference:
  `2h-2` before the last position and `h-1` at the last position.

For the last row versus the remaining `q` rows:

- `(Cu)_r>(Cu)_1` is exactly the reused last-lower-wall comparison;
- for `2<=i<r`,
  `L_i=((Cu)_r-(Cu)_i)/u_1 = (2h-4m)sigma - h x_r - x_i - 4m - 2`,
  equivalently
  `L_i=(2h-4m)s + (h-4m)x_r - x_i - 4m - 2`
  with `s=sum_{j=2}^{r-1}x_j`.

I verified both sign cases again:

- if `h-4m<0`, then
  `L_i > ((h+2)(h-2m-3))/2 > 0`;
- if `h-4m>=0`, then
  `L_i >= (2m+1)(h-2m-3) > 0`.

Therefore the repaired source still proves:

- `deg(F_{r,g}^n)=e_r^T C^n 1` for `n>=0`,
- strict last-coordinate visibility only for `n>=1`,
- `lambda_1(F_{r,g})=rho(C)` as an algebraic-degree statement only.

### 5. Unit space, quotient, cubic factor, exact multiplicity, and recurrence

The invariant splitting is unchanged and internally consistent:

- `U={z : z_1=z_r=0 and sum_{i=2}^{r-1} z_i = 0}`,
- `dim U = r-3`,
- `A|_U = B|_U = -I_U`,
- `C|_U = I_U`.

The equal-middle complement is still
`E={(a,b,...,b,c)^T}` in the exact convention
`(a,b,c) -> (a,b,...,b,c)` with `m` equal middle coordinates.

I recomputed the restricted matrices:

- `A_E = [[h,0,0],[2,2m-1,2],[2,2m,1]]`,
- `B_E = [[1,2m,2],[2,2m-1,2],[0,0,h]]`,
- `Q=B_E A_E = [[h+4m+4,2m(2m+1),2(2m+1)],[2h+4m+2,4m^2+1,4m],[2h,2mh,h]]`.

The quotient invariants remain exact:

- `tr Q = 2h+4m^2+4m+5`,
- principal-minor sum
  `= h^2 - 8h m(m+1) + 2h + 4`,
- `det Q = h^2(2m+1)^2`.

So the characteristic factor remains

`P_{m,h}(t)=t^3-(2h+4m^2+4m+5)t^2+(h^2-8hm(m+1)+2h+4)t-h^2(2m+1)^2`,

and

`chi_C(t)=(t-1)^(r-3) P_{m,h}(t)`.

I independently recomputed

`P_{m,h}(1) = -4m(m+1)(h+1)^2 != 0`,

so the source still supports the exact claim that the eigenvalue `1` has both
algebraic and geometric multiplicity exactly `r-3`, with no quotient unit
eigenvalue and no hidden unit Jordan block.

The scalar recurrence is still correctly bounded as a cubic annihilator only:

- `d_n=e_r^T C^n 1`,
- `d_{n+3}=T_0 d_{n+2} - S_0 d_{n+1} + D_0 d_n`,
- `T_0=2h+4m^2+4m+5`,
- `S_0=h^2-8hm(m+1)+2h+4`,
- `D_0=h^2(2m+1)^2`,
- `d_0=1`,
- `d_1=h(2m+3)`.

The repaired source does not overclaim universal minimality, universal
irreducibility, or algebraic degree exactly three for every Perron root.

### 6. Boundary audit, `r=3` formal consistency, and fixed-support coefficients

The §8 boundary remains correctly bounded:

- at the ordinary seed, first pure-minus-mixed score difference
  `=(g-1)-(1+2(r-1)) = g-2r`;
- at `g=2r`, the first selector ties and
  `sigma(1)=r-1=(g-2)/2` lies on the open cone-height boundary;
- at `g=2r+1`, the score gap is `1` and the height slack is `1/2`.

The repaired source still states this only as a seed/selected-face sharpness
claim, not as a global failure theorem or an optimality theorem for every
possible selector region.

The formal low-mode reduction is still correctly bounded as consistency only:

- `Q_{1,g-1}=[[g+7,6,6],[2g+4,5,4],[2(g-1),2(g-1),g-1]]`,
- `P_{1,g-1}(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2`.

This is explicitly outside the public theorem range `r>=4`; it is not
promoted to a new `r=3` theorem.

The four-coefficient corollary also remains correctly bounded:

- potentials
  `alpha prod q_i^2 + beta q_1^g`,
  `gamma prod p_i^2 + delta p_r^g`,
  with `alpha,beta,gamma,delta in K^times`;
- derivative scalars
  `2 alpha`, `g beta`, `2 gamma`, `g delta` stay nonzero in characteristic
  zero;
- no zero coefficient, extra monomial, changed support, altered word, or
  positive-characteristic specialization is smuggled in.

## Citation, structure, metadata, static LaTeX, and hygiene audit

### Citation and bibliography closure

The repaired source cites exactly four `\citep` commands, all in the
Introduction, and exactly six distinct keys:

- `BlancVanSanten2021`
- `ShaoSun2025`
- `Deserti2016`
- `DangFavre2021`
- `Rangarajan2002`
- `FujiokaKogawaLiShudo2023`

`paper/references.bib` contains exactly those six entries and no seventh.
There are no missing cited keys and no uncited bibliography entries. The
citation contexts remain bounded positioning only: broader affine-triangular
context, higher-dimensional degree-growth context, general spectral context,
and neighboring polynomial symplectic/coupled-Hénon context. No citation is
used as proof of a selector, cone, carry, visibility, quotient, multiplicity,
cubic, or threshold claim.

### Public identity and metadata

I confirmed the exact public identity contract directly in the repaired source:

- title exactly
  `Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number`;
- visible author exactly `Anonymous`;
- `\date{}` exactly empty;
- `\hypersetup{...}` binds the same full title as `pdftitle`,
  binds `pdfauthor={}`, and leaves `pdfcreator` and `pdfproducer` empty.

I found no author footnote, affiliation, address, email, ORCID,
acknowledgment, funding statement, grant number, local path, project number,
review token, hash, dashboard, gate history, agent identity, model identity,
submission venue, release language, or external-effect authorization in the
public source trio.

### Static source counts and closure

I independently recomputed the repaired source structure and hygiene:

- exactly `1` abstract environment;
- exactly `8` numbered `\section{...}` headings;
- exactly `28` `\subsection{...}` headings;
- exactly `3` `table` environments;
- exactly `0` `figure` environments;
- exactly `0` `\includegraphics` commands;
- exactly `0` `\appendix` commands;
- exactly `1` external `\input{...}` dependency, namely `math_commands`;
- exactly `0` `\include{...}` commands;
- exactly `0` `\write18` commands;
- exactly `121` labels, all unique;
- exactly `98` `\eqref`/`\ref` cross-references, with no missing target;
- exactly `6` bibliography entries;
- exactly `0` comments in all three source files;
- exactly `0` forbidden markers among `TODO`, `FIXME`, `XXX`, `TBD`,
  `VERIFY`, `placeholder`, and `??`;
- balanced theorem/proof environments, balanced braces, UTF-8 throughout,
  LF-only endings, no BOM, no CR, no NUL, and one terminal LF in each file.

The theorem/proof environment counts also remained internally balanced:

- theorems `6`,
- lemmas `2`,
- propositions `5`,
- corollaries `2`,
- definitions `1`,
- proofs `12`.

### Word/page plausibility without compilation

Without compiling, I checked visible source mass using `detex` from the paper
directory. The repaired `main.tex` yields a visible word count of `6621`,
which is consistent with the locked 26.5-page proof-first target and the
authorized 22–30 substantive-page band. This is a plausibility check only; I
did not run TeX, BibTeX, or produce a PDF.

## Repair-specific hyperref audit

The prior blocker identified exactly one prohibited hyperref PDF-string
warning arising from the old heading at source line 1754:

`\subsection{The \(g=2r\) seed/selected-face boundary}`.

I verified all repair-specific source facts:

1. `\usepackage{hyperref}` is loaded before any sectioning command; in the
   repaired file it appears at line 14.
2. The repaired heading is
   `\subsection{The \texorpdfstring{\(g=2r\)}{g=2r} seed/selected-face boundary}`.
3. The first argument preserves the visible typeset heading exactly as math:
   `\(g=2r\)`.
4. The second argument supplies the plain bookmark/PDF-string text exactly:
   `g=2r`.
5. The old blocker complained specifically about a PDF-string token removal
   caused by raw math in that heading; the repair therefore targets the exact
   source cause rather than changing downstream metadata or prose.
6. A full scan of all `\section` and `\subsection` lines shows that this is
   now the only heading containing math markup, and it is the only such
   heading wrapped in `\texorpdfstring`.
7. Because the repair changes only heading markup, it does not alter any
   theorem statement, proof line, label, reference, citation, or metadata
   field other than the bookmark-safe plain string for this subsection title.

Within a source-only review scope, this is the complete exact repair for the
recorded hyperref warning. It preserves visible typesetting, provides a safe
plain bookmark string, and introduces no syntax drift, no metadata leak, and
no additional source-side risk that I could detect.

## Build-output absence and no-compilation confirmation

I did not compile. I also confirmed that all nine success-only build outputs
remain absent:

- `paper/BUILD_METADATA_R0.json`
- `paper/BUILD_RECEIPT_R0.json`
- `paper/main.aux`
- `paper/main.bbl`
- `paper/main.blg`
- `paper/main.log`
- `paper/main.out`
- `paper/main.pdf`
- `paper/main_round0.pdf`

This review therefore introduces no new build artifact and does not rely on a
fresh TeX log.

## Permission boundary, post-write verification, and verdict

This artifact authorizes nothing except repaired-source eligibility for a fresh
independent R2 review. It does not authorize compilation, build review,
publication, release, upload, transport, messaging, identity disclosure,
Paper 23 work, or any external effect.

After creating this file, I rechecked the project structure expectations:

- post-write regular files: `26`
- post-write child directories: `4`
- post-write symlinks: `0`

The only created path is this review file:

- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md`

All earlier project files remained byte-identical to the pre-write snapshot,
including the repaired source trio, the blocker, the repair receipt, the lock
files, the review chain, and the paper plan. The root ledgers also remained at
their opening hashes:

- `BATCH_06_STATUS.md`
  - `5857b0989d805f91e38d50c61fb0e8b1c0822b11364fa1460a5fa9d4ae5a8443`
- `BATCH_06_IDEA_REPORT.md`
  - `dbc590e08ef66f8f1741282d67b76a85d193f37025f3e704d24c81336ad4e09a`

Verdict: every required repaired-source audit passed. The one-line
`\texorpdfstring` repair is exact, mathematically inert, structurally frozen,
metadata-safe, citation-safe, and source-complete for the recorded warning.

PAPER_SOURCE_R1_R0_REPAIR_PASS
