# Independent paper-plan review R1

## Verdict and finding census

**Verdict: PASS.** I find the repaired Paper 26 plan mathematically faithful,
page-feasible, citation-bounded, anonymous, source-universe exact, and
authority-safe. The final finding census is:

- blocker: 0;
- major mathematical, planning, or lifecycle finding: 0;
- minor mathematical, evidentiary, citation, page, metadata, or inventory
  finding: 0;
- wording or authority ambiguity: 0.

I was not a candidate reviewer, source-design author or reviewer, source-lock
author or reviewer, plan author, or plan repair author. I had not previously
listed or read this project. I authored none of the fourteen objects under
review. My only filesystem write is this review, after every check below had
passed.

The reviewed candidate identifier is
`planar_newton_envelope_bidirectional_degree_v1`. Its exact title is:

**Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector
Rigidity and Bidirectional Degree Growth**

## Opening authority and stable external records

I read the current Batch 06 lifecycle records and independently checked the
controlling Paper 26 transition. Their opening identities were:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `d5115df4bdf664d9918d654258265c124379ccafc19f732cb57f01d6f3431d5c` | 383399 | 5404 |
| `BATCH_06_IDEA_REPORT.md` | `4adf70c012f1aae7f07c71be747478749e5fc83f1ca68a56852662fee00c2788` | 517518 | 9471 |

The current gate permits a newly fresh zero-finding reviewer to create only
this file. It does not permit an edit to the plan or a predecessor, a source
file, citation search, compilation, build, release, or a successor transition.

I also read both immutable candidate reviews through EOF and reproduced their
identities and unique terminals:

| Record | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| `BATCH_06_PAPER26_CANDIDATE_REVIEW_R1.md` | `cc81cc410d9122bdaf6ebf8b20e57bce3cbe4fcaed17c3cc0ed5f596d9844dbe` | 29824 | 611 | `PAPER26_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER26_CANDIDATE_REVIEW_R2.md` | `164273106733f611c0d35a60cb693d5ffbf8cf1300ffb658a00abb555fbda2e1` | 26605 | 1112 | `PAPER26_CANDIDATE_GATE_PASS_R2` |

The source-design PASS is
`974bcfea08dff87d359993839452eb271d2cf0edbbe2fb811abc17051aece92e`,
17823 bytes / 449 LF, with terminal `PAPER26_SOURCE_DESIGN_PASS`. The source
lock is
`226b90ec7367b73cbd481a67a08a38e5a471c0a9d9ac571e6905292587b59839`,
11556 bytes / one LF, schema `paper26.source_lock.v1`, and logical terminal
`PAPER26_SOURCE_LOCK_AUTHOR_STOP`. The independent source-lock PASS is
`c12ea09940a775b97dc7e459b6284858bf076f56b2e13a15b09d95ffe6214e0e`,
20397 bytes / 440 LF, with terminal `PAPER26_SOURCE_LOCK_PASS`. I read these
records and the proof, claims, proposal, citation, and novelty inputs rather
than treating their PASS labels as a substitute for this review.

## Exact predecessor and repaired-plan audit

Before the plan was added, L13 contained thirteen regular files in three child
directories. Independent Node and Ruby implementations sorted raw UTF-8
relative paths and framed each entry as

`u64be(path length) || path || u64be(content length) || content`.

They independently reproduced:

| L13 quantity | Value |
|---|---:|
| regular files | 13 |
| content bytes | 184090 |
| content LF | 4055 |
| path bytes | 396 |
| framing bytes | 208 |
| framed bytes | 184694 |
| framed SHA-256 | `65cbcf05261745bae6b22c7e156af17cbf4870a04fa1153a719de20bc01ddb6f` |

The current plan is `paper/PAPER_PLAN.md`, SHA-256
`8f788b1416ec9887a894c103bf0374896f4c4eff50e9fc7ac7124eb67c43ca15`,
56308 bytes / 834 LF, regular mode 0644 with link count one. It is valid UTF-8,
has no BOM, CR, or NUL, has exactly one terminal LF, and ends uniquely with
`PAPER26_PAPER_PLAN_REPAIR_AUTHOR_STOP_R1`. The superseded terminal does not
occur in the live plan.

The complete opening L14 tree was exactly fourteen regular files in four
mode-0755 child directories, with zero symlinks and zero other nodes. Every
regular file was mode 0644/link one and passed UTF-8, BOM, CR, NUL, and terminal
LF checks. Independent Node and Ruby reconstruction gave:

| L14 quantity | Value |
|---|---:|
| regular files | 14 |
| child directories | 4 |
| content bytes | 240398 |
| content LF | 4889 |
| path bytes | 415 |
| framing bytes | 224 |
| framed bytes | 241037 |
| framed SHA-256 | `8d15e1092c34fc003822313e96552f7efa145a2a9c02d0c7e480f2cdc6edb5c6` |

The plan-review path and future `paper/main.tex`,
`paper/math_commands.tex`, and `paper/references.bib` were absent at prewrite.
No figure, asset, data, code, bibliography, auxiliary source, or hidden node
was present.

## Exact five-line R1 repair reconstruction

I treated the repair provenance as unproved. Each current phrase below occurs
exactly once. In memory only, I reversed these five whole-line substitutions:

1. `Author, Creator, Producer, Subject, and Keywords must all be empty` to
   `Author, Subject, and Keywords must be empty`;
2. `Give five contribution bullets` to `Give four contribution bullets`;
3. `empty PDF fields for Author, Creator, Producer, Subject, and Keywords` to
   `empty identity-bearing PDF fields`;
4. `PDF Author, Creator, Producer, Subject, and Keywords are all empty` to
   `PDF Author, Subject, and Keywords are empty`;
5. `PAPER26_PAPER_PLAN_REPAIR_AUTHOR_STOP_R1` to
   `PAPER26_PAPER_PLAN_AUTHOR_STOP`.

Both independent implementations reconstructed exactly 56216 bytes / 834 LF,
SHA-256
`da00b1521760278865839bc750ce2189bcb9f62a90b0f05df23b5d0da562c556`.
The reverse diff contains no sixth changed phrase. The live repair therefore
changes only the frozen contribution count, the three explicit metadata
contracts, and the terminal. It changes no theorem, page, citation, table,
source path, anti-claim, or permission.

## Independent page arithmetic and proof-mass audit

I summed every subsection independently:

| Body component | Subsection sum | Declared pages | Result |
|---|---:|---:|---|
| Front matter and Abstract | 0.10 + 0.65 | 0.75 | exact |
| Section 1 | 0.45 + 0.45 + 0.70 + 0.65 | 2.25 | exact |
| Section 2 | 0.45 + 0.35 + 0.30 + 0.40 | 1.50 | exact |
| Section 3 | 0.30 + 0.35 + 0.75 + 0.40 + 0.65 + 0.55 | 3.00 | exact |
| Section 4 | 0.45 + 0.35 + 0.40 + 0.75 + 0.85 + 0.45 + 0.55 + 0.45 | 4.25 | exact |
| Section 5 | 0.45 + 0.45 + 0.65 + 0.55 + 0.35 + 0.55 + 0.40 + 0.35 | 3.75 | exact |
| Section 6 | 0.45 + 0.85 + 0.30 + 0.55 + 0.75 + 0.40 + 0.20 | 3.50 | exact |
| Section 7 | 0.45 + 0.55 + 0.55 + 0.65 + 0.45 + 0.65 + 0.50 + 0.20 | 4.00 | exact |
| Section 8 | 0.65 + 0.90 + 0.40 + 0.30 + 0.25 | 2.50 | exact |
| Section 9 | 0.35 + 0.15 | 0.50 | exact |

The total is

\[
0.75+2.25+1.50+3.00+4.25+3.75+3.50+4.00+2.50+0.50=26.00.
\]

Sections 4--7 total

\[
4.25+3.75+3.50+4.00=15.50.
\]

Thus the center target is inside the required 22--30 content-page range,
with references excluded. The proof mass is credible: the full-face argument
receives 3.00 pages; exact bidirectional transport 4.25; contraction 3.75;
selector and spectrum 3.50; and separate scalar recurrences 4.00. The plan has
no appendix, theorem-critical external delegation, filler, forced break,
display inflation, margin/font/spacing device, or empirical section. Its
under- and over-length controls preserve the theorem-critical blocks.

## Main theorem and dependency-order audit

The formal theorem contract contains every locked hypothesis:

1. a characteristic-zero base field;
2. finite, nonempty, collected support
   `E subset Z_{>=2}^2`;
3. arbitrary nonzero collected coefficients, without positivity or a common
   sign;
4. a separated momentum Hamiltonian with nonzero `alpha,beta` and derivative
   exponents `e,f>=2`;
5. the fixed phase order `F=T after S` and reversed subtraction order for the
   inverse;
6. ordinary total degree in all four initial coordinates; and
7. the ordinary forward and inverse seed `(1,1)^T`.

Its statement and section order are genuinely forward-dependent:

1. symmetric Hessian blocks establish symplecticity and literal inverses;
2. the full exposed-face Hessian certificate isolates the minimal-first-
   coordinate self-pair, including arbitrary multi-point ties;
3. the characteristic-zero Jacobian criterion, injective substitution,
   nonzero scalars/signs, and separated powers propagate leading-form
   independence;
4. all forward and inverse carries establish exact transports and visible
   ordinary degrees;
5. positive homogeneity and the ordinary seed establish the shifted bridge and
   only its vector/rate consequences;
6. exact forward transport yields the projective formulas, branch derivative,
   positive logarithmic gap, endpoint decay, finite-support uniform constant,
   and wall patching;
7. the contraction yields one ray, no nontrivial numerical periodic orbit,
   and the complete interior/wall selector classification;
8. the positive interior matrix or common primitive wall ray gives the
   quadratic-at-most/integer spectral dichotomy; and
9. only after state and selector stabilization does Cayley--Hamilton yield the
   forward and separately proved inverse scalar recurrence upper bounds.

The Main Theorem is stated after the full-face proposition. No plan section
uses a fixture, monodromy, or later spectral conclusion to justify an earlier
cancellation or contraction step.

## Cancellation, transport, bridge, and contraction audit

The Section 3 plan explicitly uses the whole face polynomial and separately
records why the coefficient

\[
c_{x_0,y_0}^2x_0y_0(1-x_0-y_0)
\]

is isolated and nonzero. It covers one-point and multi-point ties and never
substitutes coefficient positivity or genericity for the proof.

Section 4 retains both lower carry inequalities and the stronger
cross-coordinate upper-phase inequalities

\[
2A_1-A_2=H-2u_1+u_2\ge3u_2>0,
\qquad
2A_2-A_1=H+u_1-2u_2\ge3u_1>0.
\]

It then gives distinct forward and inverse half-step inductions, including
`T^{-1}` first, subtraction signs, fresh versus carried blocks, leading-pair
survival, and position versus momentum visibility. The resulting exact states
and maximum formulas occur before the bridge.

The bridge preserves the constant `c_star=H(1)-1`, diagonal `B`, ordinary
seed, and one-step shift. Its two-sided norm comparison proves equality of
first dynamical degrees. The plan states at the theorem, proposition,
corollary, transition, recurrence opening, and scope boundary that this bridge
does not give termwise scalar equality and is not an inverse scalar-recurrence
proof.

Section 5 includes every step required to upgrade a chamberwise inequality to
a global theorem: the exact `Phi`, `phi`, and inverse `psi`; negative branch
derivative; logarithmic derivative; strictly positive quadratic gap; endpoint
limits; one maximum over finite support; interval splitting at walls; and the
scaled conjugacy `L(s)=kappa*s`. It says explicitly that inverse chamber
selection uses `kappa*s`, not the unscaled inverse state ratio.

## Selector, spectrum, and separate recurrence audit

Section 6 separates the fixed wall trajectory from strict trajectories. It
records side swapping, convergence, adjacent-chamber alternation, injective
no-delayed-landing, the full tied face on the wall, and the two extreme
adjacent exponents at a multiple tie. It repeatedly distinguishes a selector
word from a numerical two-cycle.

The interior tail uses the positive integral matrix
`C_xi=B*A_xi`. The wall proof chooses a primitive positive integral direction,
shows both adjacent matrices have the same ray and multiplier, proves that the
multiplier is a positive integer, and distinguishes the one-step multiplier
from the square two-step Perron root. This yields exactly an interior degree at
most two and a wall integer, not a dimension-free result.

Section 7 does not borrow the inverse scalar law from the bridge. It defines

\[
D_\xi=A_\xi B=B^{-1}C_\xi B
\]

from the literal inverse state and applies it only when `kappa*s_n` selects the
corresponding chamber. It separately treats:

- forward interior visibility and the `r_star=1` fixed seed;
- forward fixed-wall and strict-wall tails;
- inverse interior `s_star!=1` visibility and the `s_star=1` fixed seed;
- inverse fixed-wall geometry with `kappa*s_star=r_star` on the Newton wall;
- the fact that a strict ordinary inverse wall orbit has `s_star!=1`; and
- both actual-time-order products
  `M_+=C_+C_-`, `M_-=C_-C_+`,
  `N_+=D_+D_-`, and `N_-=D_-D_+`.

It records the exact similarities in expanded notation as
`N_+=B^{-1}M_+B` and `N_-=B^{-1}M_-B`, common trace `tau`, common determinant
`Delta`, parity-wise visible-coordinate stabilization, and the eventual law

\[
d_{n+4}^{\pm}=\tau d_{n+2}^{\pm}-\Delta d_n^{\pm}
\]

for all sufficiently large admissible indices. The plus/minus superscript
denotes forward/inverse scalar degree, while plus/minus subscripts on the
matrices denote selector parity; the notation order keeps these uses
distinguishable. All recurrence orders are upper bounds, and the fixed-ray
case is geometric.

## Fixture and scope-boundary audit

The two fixtures are placed only after the general proofs. The first records

\[
C=\begin{pmatrix}3&6\\4&2\end{pmatrix},\qquad
\chi_C(t)=t^2-5t-18,
\qquad \lambda_1=(5+\sqrt{97})/2,
\]

and the exact bridge vectors `(9,6)`, `(7,8)`, and `(63,48)`.

The second records the support `(2,8),(4,5),(5,3)`, diagonal `(24,11)`, walls
`3/2` and `2`, exact ratios `24/11`, `1548/781`, and `51294/25619`, the
middle/high interval images, primitive wall direction `(2,1)^T`, multiplier
132, monodromy trace 17648, determinant 3902976, and eigenvalues
`17424=132^2` and 224. It labels these as exact hand calculations, not
numerical or CAS evidence.

The plan places every locked boundary near the theorem step it limits and
again in Section 8: axes, exponent one, zero or uncollected coefficients,
mixed `W`, positive characteristic, dimension at least three, changed phase or
seed, numerical cycles, termwise forward/inverse equality, scalar transfer
from the bridge, recurrence minimality, higher dynamical degrees, entropy,
compactification, integrability, point-orbit arithmetic, genericity, support
optimality, classification, nonconjugacy, and global priority are all denied.

## Narrative, contribution, figure, and table audit

The title, one-sentence contribution, What/Why/So What, Abstract sequence,
Introduction, formal theorem, and technical order tell one consistent story.
The repaired Section 1.4 now requests exactly five contribution bullets, which
match the five frozen contribution items and their order:

1. full-face cancellation;
2. exact bidirectional carries and bridge;
3. global wall-patched contraction;
4. selector and spectral rigidity; and
5. separately proved scalar recurrence consequences.

Recurrences, monodromy, and fixtures remain consequences rather than the
headline. Sections 4--7 retain the locked 15.5-page center, so neither the
Paper 24 parity mechanism nor the Paper 25 matrix recurrence becomes the
article's opening or largest novelty claim.

The manuscript contract contains exactly zero figures and assets. Its sole
table is a qualitative hand-typeset structural table in Section 6.7 with
exactly three columns--Mechanism, Consequence, and Boundary--and exactly five
data rows. The plan expressly bars a second table, page-budget table, claims
table, fixture table, literature table, notation table, figure directory,
raster/vector asset, data file, plot, or generated visual.

## Citation, novelty, and collision audit

Every eligible planning slot appears in the frozen citation ledger with the
same authors, title, and persistent identifier: Bellon--Viallet, Dang--Favre,
the two Fordy--Hone records, Ishibashi--Kano, Janeczko--Jelonek,
Berger--Turaev, and Blanc--van Santen. Their use is contextual only. The plan
requires primary-record rechecking before bibliography admission and places no
research citation inside a theorem-critical proof.

The incomplete Koch--Lomelí record associated with arXiv:1304.3377 is
explicitly barred from the manuscript and `references.bib`. Standard theorem
citations may not be invented from memory. If full metadata and claim-level
fit are not verified, bibliography authoring must stop.

Global novelty remains unresolved. The plan contains no global firstness,
uniqueness, exhaustiveness, or priority claim. It also preserves the exact
local subtraction:

- Paper 24 owns its special two-term wall criterion, forced selector
  alternation, two-step monodromy/parity mechanics, and interleaved recurrence
  framing;
- Paper 25 owns support-rank bounds, stationary sharp constructions, unbounded
  higher-dimensional Perron degree, and scalar minimality.

Paper 26 retains only the combined arbitrary finite planar support,
full-tied-face cancellation, global contraction, selector/no-cycle
classification, exact inverse transport, and quadratic-at-most/integer
spectral conclusion under its narrower hypotheses.

## Anonymity, metadata, source trio, and authority audit

The global rule requires the exact PDF Title and empty PDF Author, Creator,
Producer, Subject, and Keywords. The future `main.tex` contract and the source
author checklist repeat all five empty fields. The visible author is
`Anonymous`; the visible date is empty. Affiliation, acknowledgment, grant,
identity link, local path, review identity, hash, gate, and project datum are
barred from comments, rendered text, bookmarks, metadata, attachments, and
bibliography.

The possible future source universe is exactly:

1. `paper/main.tex`;
2. `paper/math_commands.tex`;
3. `paper/references.bib`.

The roles of all three are closed and nonoverlapping. Section files, style
files, figures, data, code, notebooks, scripts, generated tables, auxiliary
sources, alternate bibliography databases, external inputs, and hidden source
are excluded. None of the three source files exists at this review's prewrite.

The source-author checklist and seventeen kill criteria cover theorem order,
every carry and recurrence branch, citation admission, collision subtraction,
page/asset restrictions, anonymity, metadata, and no-drift conditions. The
plan explicitly grants no source authoring, bibliography verification,
computation, compilation, build, PDF, release, submission, external effect, or
successor gate.

## Final review conclusion

The repaired plan is an exact, proof-first organization of the locked theorem.
Its page arithmetic, proof dependencies, inverse recurrence separation,
fixtures, citations, novelty boundary, local collision subtraction, metadata,
zero-figure/one-table design, source trio, and kill conditions are complete and
mutually consistent. The plan is ready for parent consumption as a plan PASS,
but this review does not itself authorize manuscript source or any later
action.

PAPER26_PAPER_PLAN_PASS
