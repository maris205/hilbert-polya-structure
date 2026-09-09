# Independent review of the full integral Fricke return atlas

2026-09-08 UTC. Reviewer: the nonauthor arithmetic-lane agent. The
coordinator authored the mathematical package; this reviewer did not
edit it. This report concerns only the original NG2-F question continued
as R3-NG-F, not NG2-V, the arithmetic GM3 question, or another stream.

## 1. Verdict and exact gate

**Mathematics: PASS, original complete question closed.**

**Required mathematical corrections: 0. Required source corrections: 0.**

**Substantive-increment verdict: PASS for one complete research contract,
after the deductions in Section 5.** This is not merely `CLOSED_AUX`.
The surviving contribution is the all-coefficient, all-level exhaustion
by periodic integer lines and an explicitly bounded residual core, not
the general Fricke object, coefficient independence, a new time unit,
fibrewise finiteness, or finite-graph bookkeeping.

**Source/priority scope: bounded primary-source audit passed; worldwide
priority is not certified.** No conflicting full fixed-word atlas was
identified in the sources actually examined. That is not a proof of its
absence from every other paper.

I recommend that the coordinator may count this as **one** independently
reviewed completed original-question contract, subject to the project's
remaining administrative/admission gates. It is not two contracts for
the line theorem and its zeta corollary, nor a newly invented question in
addition to the retained NG2-F question. No C number, paper, formal
evaluation, top-venue acceptance, registry write, or Git integration is
created by this review.

## 2. Frozen inputs and actual review scope

The four author files were read completely at their actual paths under
`continuation_round3/nonlinear_geometry/`. Their SHA-256 values checked
before writing this report were:

| File | SHA-256 |
| --- | --- |
| `FROZEN_QUESTIONS.md` | `955d728c6801f10016d120b77d2bad47c7ebf923039be5eec1b42a94a8953669` |
| `PROOF_PACKAGE.md` | `4672ce2e12a3e6584cb2bc4df815ea9c4110806d2d96d05a0506cdf79ed10b9c` |
| `SOURCE_AUDIT.md` | `e1e7f6ce47027eec07069e53eac99506de249e8a4726409daac5227a3ab7f0f8` |
| `SCOUT_REPORT.md` | `916eae98c9dc09a49d93d3ec91fe247746b76afb6197ea06796e1fe7d41572c9` |

The proof is 272 lines. Its formulas and all steps in Sections 2--7
were independently recomputed by hand, including the threshold constants,
phase conversions, line preimages, residual termination, and ordinary
counts. The coordinator's summary was not used as a substitute for this
reading. The dated route update changes the proof strategy, not the
object or its quantifiers.

For the local deduction, I also read the complete second-round
`nonlinear_geometry/FROZEN_QUESTIONS.md` (97 lines),
`PROOF_AND_GAPS.md` (171 lines), and `SOURCE_AUDIT.md` (108 lines), and
the complete C421 predecessor
`research_c419_c423/continuation_round2/integral_return/IR1_PROOF.md`
(260 lines). The predecessor's old programs/certificates were not rerun;
its existing certified core is treated as already owned, not newly
certified by this review. I do not claim a fresh whole-library audit.

The research-review skill's claim/evidence and actionable-correction
discipline was applied through this assigned nonauthor team review.
No legacy external-review API, external manuscript upload, or additional
model session was opened. There is no invented external thread ID or
claim of multiple external review rounds.

## 3. Mathematical checks

### 3.1. Original domain, invariant, and native clock

The object remains every ordered integer triple `(A,B,C)`, all of
`Z^3`, and every integral invariant level, with no positivity, smoothness,
nonzero-coordinate, or generic-parameter assumption. The three Vieta
involutions and their polynomial inverses act on this entire lattice.
Singular affine points are ordinary points in this argument; no lifted
exceptional divisor or point at infinity replaces them.

One native tick is exactly `T = s_z s_y s_x`, rightmost first. On phase
zero, the auxiliary `F^3` is exactly this map. A native periodic orbit
gives a two-sided periodic scalar word, and its native triples partition
the scalar positions into blocks of three. Consequently the scalar
maximum `M` is the maximum native-orbit coordinate height; this equality
does not overlook a larger intermediate factor-update coordinate.
No reversal symmetry of the ordered forcing triple is assumed.

### 3.2. Entry at a true global maximum

At a position with `|x_j| = M`, the recurrence at indices `j-2` and
`j-1` gives `M |x_(j-1)| <= 2M+H` and
`M |x_(j+1)| <= 2M+H`. For `M > H+2`, integrality bounds the two
neighbors by two. A neighbor of absolute value two forces the next
outer coordinate to have magnitude at least `2M-2-H > M`.
The reverse-direction formula supplies the same exclusion on the
other side. Thus both neighbors lie in `{-1,0,1}`.

This use of a genuine global maximum is justified by periodicity, not
by an unsupported escape hypothesis. It yields one of the 27 labelled
state lines with middle parameter of absolute value exactly `M`.

### 3.3. Exact edges and all omitted-edge cases

For `v = +/-1`, direct substitution gives
`F^2(i;u,t,v) = (i+2;v,vt+b,vb+a_(i+1))`, with `b=a_i-u`.
For `v=0`, the scalar continuation is
`b, t', b t'+a_(i+2), t'(b t'+a_(i+2))-b+a_i`, where
`t'=-t+a_(i+1)`. These are the stated identities, for every integer
parameter, not asymptotic formulas. The listed intermediate triples
are affine and contain a coordinate of slope `+1` or `-1`.

I checked the entire propagation argument at
`B_0=H+1`, `R=100B_0`, and `0 <= j <= 27`:

- An absent Type I edge gives a coordinate at least
  `2M-57B_0 > M` in absolute value.
- In the zero case, `|b| >= 2` gives at least
  `2M-56B_0-H > M`.
- If `|b|=1`, the next quadratic expression is at least
  `(M-28B_0)(M-29B_0)-B_0 > M`. Both factors are positive;
  `M > 100B_0 >= 100` suffices for the final inequality.
- Once `b=0`, `|a_(i+2)| >= 2` similarly contradicts the maximum.

These exhaust the omitted-edge possibilities. Each actual edge changes
the large parameter by an affine isometry with translation at most
`B_0`, so induction supplies the required 27 successive transitions.
It does not silently reapply the maximum-neighbor lemma to a nonmaximal
middle coordinate. The 28 visited states force a repeated state and,
because the graph is deterministic, entry into a directed cycle.

### 3.4. Cycle returns, whole lines, and preperiodic graph tails

The phase sum forces `3 | ell_C`. A retained cycle induces either the
identity or a reflection of the integer parameter. Thus its entire
state lines and every intermediate image consist of ordinary periodic
points. The affine maps are bijections on the integers, not just
injections on a restricted range.

The possible graph tail before a cycle is not an unproved extra family.
The union of all intermediate lines of retained cycles is exactly
`F`-invariant. Since `F` itself is bijective, its inverse image is also
this union. Any point that reaches that union was already in it.
This supplies the essential backward step in the exhaustion theorem.
A hypothetical nonzero-translation cycle has no periodic parameter;
the proof's exclusion of it is valid (and is redundant by Section 7
below).

Distinct directed cycles have disjoint state sets. Their total number
of phase-zero intermediate positions is
`sum_C ell_C/3 <= sum_C |C| <= 27`. Also `ell_C <= 81`, so the
native return times are `ell_C/3` or `2 ell_C/3`, at most 54.
The proof correctly says return time, not automatically least period.
Coincident geometric lines can only reduce the line count.

### 3.5. Complete residual rule, not an unperformed census claim

Every periodic orbit outside the retained union has maximum at most
`R`; hence every native point of that orbit lies in `Q_R`. Conversely
every directed cycle of the exact partial map on `Q_R` is an ordinary
native periodic orbit. This is a proved exhaustive decomposition.

The finite rule terminates after exit or a repeat within `N_R+1`
visited vertices. Injectivity of `T` implies that a first repeated
vertex of a nonexiting seed path is its initial vertex: otherwise two
different predecessors would have the same image. No empirical time
cutoff is being used.

The frozen question expressly accepts proved exhaustive residual rules.
It does not require a sharp closed period table for every coefficient
triple. Therefore the parameterwise graph construction satisfies the
contract without an actual execution of its potentially large core.
Core size or computational expense is not itself a novelty argument.

### 3.6. Integral parametrization, least periods, coexistence

A coordinate of slope `+1` or `-1` makes every displayed parametrization
primitive: it gives all integer points of its rational affine line.
Coincident lines therefore coincide on integers, while distinct lines
meet at most once. Their coincidences and integral intersections are
decidable by linear equations, and line points can be removed from the
finite-core output without losing or duplicating a point.

On a line with certified return `r`, least period divides `r`. For
each divisor `d`, the three polynomials in `T^d P(t)-P(t)` determine
exactly its period-dividing-`d` parameters. If they are not identically
zero, their common integer roots are a finite effectively computable
set. The rational-root rule after removing a zero root is sufficient.
Taking the smallest qualifying divisor gives the generic period and
all finite exceptions. This is a complete least-period and coexistence
procedure, not a generic-period assertion that ignores exceptional
parameters or line intersections.

### 3.7. Every level and ordinary counts

Direct substitution verifies `K_(i+1) o F_i = K_i`. On a state line,
`K_i(u,t,v)` is the displayed monic quadratic in `t`. Transport through
the affine identities preserves its quadratic nature and leading
coefficient. Each line consequently meets a fixed level in at most two
points. The bound `54+N_R` for the number of periodic integer points on
any one level follows before de-duplication, and all these points and
their least periods are effective.

The finite cycle-product expression is therefore a legitimate ordinary
fibre zeta. Its exponents count primitive native cycles, and its fixed
point counts have the usual `sum_(d|n) d c_d` form. The proof expressly
does not manufacture an ordinary all-lattice zeta when fixed iterates
contain infinitely many integer points. No multiplicities, weights,
Euler factors at target primes, or root numbers enter the result.

## 4. Independent primary-source checks and limits

**Shin, Character varieties on a four-holed sphere, v3 (1 June 2026).**
I read the complete browser-visible HTML text, including Theorems
1.1--1.3, Sections 2--3, the low-coordinate calculations, Lemmas 2.2--2.3
and their visible proofs, and Remark 3.1. Embedded graph figures were
not separately analyzed. Theorems 1.2--1.3 concern group-orbit equivalence;
Remark 3.1 removes the boundary-trace parameter relations. Thus independent
`A,B,C,D` is already in source scope. The low-coordinate and height-graph
mechanisms must also be deducted. The displayed results do not themselves
state this exact fixed-word, level-uniform line/core classification.
That last comparison is an inference from the checked statements, not
an assertion about all unexamined literature.
[Primary v3](https://arxiv.org/html/2308.16614v3).

For sign clarity, the integral bijection `(x,y,z) -> (-x,y,z)` carries
our convention to the source convention with
`(alpha_1,alpha_2,alpha_3,beta)=(-A,B,C,D)`, preserving the ordered
three-factor word. The author's alternative sign change in the
second-round Cantat comparison is also valid; neither grants novelty.

**Cantat, Bers and Hénon, Painlevé and Schroedinger, v2
(5 December 2007).** I checked the coefficient/involution setup,
boundary smoothness, the involution matrices, full Proposition 2.2,
Section 3.1 including Theorem 3.1, Proposition 3.2 and Corollary 3.3
with their proofs, and Corollary 3.4. Their fixed-fibre escape
neighborhoods give the already-owned compact-containment/lattice
finiteness deduction. Boundary smoothness includes affine-singular
fibres. No effective radius independent of `D` or integer line/core
atlas is imported. Corollary 3.4 causes no conflict: the present lines
cross levels and are not invariant curves inside one fixed fibre.
[Primary v2](https://arxiv.org/pdf/0711.1727v2).

**Vishkautsan, Residual periodicity on the Markoff surface, v2
(8 July 2015).** The abstract, Sections 1.1--1.2 including Theorems A
and B, and the displayed two-reflection linear-fibre calculation in
Section 3 were inspected. This is a two-reflection, unforced-surface
local/global residual-periodicity problem, not the present three-factor
integer exhaustion. It is not a dependency of the proof.
[Primary v2](https://arxiv.org/pdf/1504.07099v2).

**Abboud, Rigidity of periodic points for loxodromic automorphisms of
affine surfaces, v3 (23 April 2025).** I inspected the abstract and
introduction, including Theorems A--C and the algebraic-torus exception.
The stated comparison/rigidity of periodic sets is not this effective
integer atlas. No estimate is imported from the later Northcott or
canonical-height proofs, which were not reviewed here.
[Primary v3](https://arxiv.org/html/2406.11510v3).

**Planat--Chester--Irwin, Dynamics of Fricke--Painlevé VI Surfaces
(2 January 2024).** The publisher PDF metadata, abstract and
introduction were inspected. Its stated emphasis is selected algebraic
Painlevé solutions and their applications. This is an introductory-scope
screen only; I did not infer the absence of every potentially relevant
theorem from unread later sections.
[Publisher PDF](https://mdpi-res.com/d_attachment/dynamics/dynamics-04-00001/article_deploy/dynamics-04-00001.pdf?version=1704184938).

The fresh Roberts--Baake 1994 trace-map lead was checked against an
author/institution publication listing and a primary PDF search extract.
The direct PDF open returned an internal retrieval error. Its full body
was not read and it supplies no affirmative step of this review; the
search engine's recent relative age was not mistaken for its publication
date. Secondary finite-orbit, K3 and modular-function hits were not
adopted as proof sources. No denied access was bypassed.

The actual fresh search strings in this nonauthor review were:

```text
"Fricke" "integral periodic" automorphism
"Markoff" "periodic points" "three" involutions integers
"Vieta" "periodic" "integer" "lines"  [recency: 180 days]
"trace map" "integer" "periodic orbits" Fricke
"Markoff" "integral" "bounded orbits" automorphism
"Fricke" "periodic points" "classification" integers
"Fricke" "integer" "periodic" lines automorphisms  [recency: 180 days]
"Roberts" "Baake" 1994 "trace maps" periodic integer
```

These eight queries were issued in three search-bearing calls, followed
by primary opens/finds. They are separate from the author's six queries.
All newly inspected primary bodies were remote HTML/PDF; no local PDF
page-anchor or new local structure-preflight certification is claimed.
Unseen proofs, indexing, retraction and conflict-of-interest checks,
and exhaustive bibliography coverage remain unassessed.

## 5. Substantive-increment decision after deductions

The following are not independent contributions of this contract:

- The Fricke invariant and Vieta involutions, parameter independence,
  the plus/minus sign convention, or replacing one clock by another.
- The exact equal-forcing slice: for `A=B=C=a`, the native map is
  `F_a^3`. C421 already owns that scalar system's all-parameter
  classification, exceptional families and sharp certified core.
- Second-round fixed-factor equations, the axis family, the distinction
  from finite full-group orbits, and Cantat-based fibrewise finiteness.
- Source-owned low-coordinate mutation identities and general height
  graphs; routine affine-cycle tests, finite graph searches, polynomial
  gcd algorithms, and ordinary cycle-zeta bookkeeping.

After those deductions, Sections 2--5 prove a genuinely additional
global implication for the retained full question: every periodic orbit
whose height exceeds `100(1+max(|A|,|B|,|C|))` belongs to an explicitly
constructed finite union of whole periodic integer lines. The proof
works across all levels simultaneously, controls every ordered forcing
triple, and supplies the exact invariant complement where a complete
finite residual rule applies. C421's homogeneous difference mechanism
does not supply this implication when forcing phases differ; Shin's
whole-group statement and Cantat's fixed-fibre compactness are not
substituted for its proof.

The material step is not merely changing coefficients or appending a
finite search to known finiteness. It is the uniform global-maximum
entry, forced finite-state propagation, and bijective-tail exhaustion
that separate every unbounded periodic channel from a bounded residual
set. Their combination closes the original all-input contract with
least-period and coexistence rules. I therefore judge the surviving
increment sufficient for **one substantial mathematical contract**, not
just an auxiliary proposition or a source corollary.

This is a research-substance judgment based on checked mathematics and
bounded ownership comparisons, not a guarantee of acceptance at a
specified venue. Neither sharp constants nor a new experimental census
is required for closure of this particular frozen contract. The line
and period bounds must not be advertised as optimal, and the generic
procedure must not be advertised as a table already computed.

## 6. Required corrections and evidence-to-claim matrix

Required corrections: **none**. There is no missing finite computation
whose output is necessary for the theorem as stated. Estimated required
additional mathematical-program/GPU work for this review gate: **zero**.

| Proposed claim | Review disposition |
| --- | --- |
| Complete original all-`(A,B,C)`, all-level, full-lattice periodic atlas by line parametrizations and exhaustive residual rules | Allowed, by the frozen proof. |
| At most 27 whole periodic integer lines, native return times at most 54, residual radius `100(H+1)` | Allowed; nonsharp bounds. |
| Exact least periods and ordinary fibre counts are effectively determined | Allowed; effective algorithm, not a performed census. |
| Fixed-fibre finiteness, independent coefficients, the equal-forcing slice, or routine zeta bookkeeping is new | Not allowed; already deducted. |
| Sharp universal period table, all core computations already executed, or an ordinary zeta on an infinite all-lattice fixed-point set | Not established or expressly excluded. |
| Worldwide priority, top-venue acceptance, or an independently reviewed second contract | Not established. |

## 7. Optional simplification only

The invariant gives a harmless simplification of the cycle test. On a
state line write `q(t)=t^2-Lt+C_0`, where `L=uv+a_(i+1)`.
Every graph cycle returns to the same phase and satisfies the identity
`q(epsilon t+beta)=q(t)`. Comparing the linear coefficients shows
`beta=0` when `epsilon=1`, and `beta=L` when `epsilon=-1`.
Thus every actual graph cycle is automatically retained; the rejected
nonzero-translation branch is empty for this invariant-preserving graph.

This observation was independently noticed during the monic-invariant
check; the coordinator subsequently sent the same optional observation.
It does not repair a gap, change a quantified claim, or invalidate the
proof's exact test. No amendment of the frozen proof, extra program,
or new review round is requested for it.

## 8. Execution and scope receipt

Mathematical program executions by this reviewer for NG2-F: **zero**.
Finite-core/line-graph enumerations: **zero**. Numerical or symbolic
diagnostics, old certification reruns, LaTeX builds, formal evaluations,
external manuscript uploads, and Git mutations: **zero**.

Actual local actions were read-only file discovery/reading, line counts,
hash checks, and writing this report with `apply_patch`. Initial lookup
of a nonexistent singular `FROZEN_CONTRACT.md` was corrected using the
actual `FROZEN_QUESTIONS.md` path; the then-absent review directory was
also a locator result, not a missing mathematical input. No author
payload or shared status file was changed by this reviewer.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. This report closes
the assigned independent review, not the unrelated outstanding questions.
