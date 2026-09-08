# C422 paper plan: a uniform finite-field Painlevé period bound

Date: 2026-09-08 UTC. Status: `MANUSCRIPT_DRAFTING_AUTHORIZED`.
This is the detailed implementation plan for the C422 contract in the
coordinator's [approved batch plan](../../BATCH_PLAN.md). The coordinator
read the complete [independent outline review](../../REVIEW_OUTLINE.md)
(PASS, zero mandatory corrections) and explicitly authorized the C422
body and first baseline PDF. This per-paper elaboration is not represented
as a separately reviewed outline. The global approval is for the unchanged
contract and proof placement recorded in that batch plan.

Working title: **A uniform orbit bound for discrete Painlevé I over finite
fields**.

One-sentence contribution: We prove the Joshi–Roffelsen upper bound for
every ordinary orbit of their resolved finite-field discrete Painlevé I
system by using a boundary-lattice and minimal-pole argument to prove that
every finite invariant fibre is geometrically integral of arithmetic
genus one.

Format: English, anonymous, standalone mathematical article, 11 pt.
No conference template, submission destination, hard maximum, minimum
page count, or artificial length target is imposed. This is a proof-only
paper: no empirical section, experiment, census, or decorative figure is
needed. Eight main sections are planned; all argument-specific proofs
will be typeset in the article itself. No proof is to be replaced by a
reference to a local Markdown file.

## 1. Unchanged contract and claim boundary

Let (k=\mathbb F_q), let (s,t_0\in k^*), and let

\[
r=\operatorname{ord}_{k^*}(s),\qquad t\in t_0\langle s\rangle.
\]

The state is (\gamma=(j,x,y,t,s)), where

\[
(j,x,y)\in
\bigl(\{0\}\times(k^*)^2\bigr)
\sqcup\bigsqcup_{j=1}^{4}\bigl(\{j\}\times\{0\}\times k\bigr).
\]

Every native step updates (t'=st) and (s'=s). The seven branches,
including every zero coordinate on the exceptional lines, must be given
explicitly in Section 2. The least **native** period is (\ell); the
least period of the fixed-phase (r)-step return is exactly (\ell/r).

Main theorem to state in the introduction and prove in Section 7:

> Every allowed state is periodic, and its least native period satisfies
> (r\mid\ell) and (\ell/r\le q+1+2\sqrt q), for every finite field
> and every allowed parameter, including characteristics two and three.

The theorem concerns distinct ordinary states. It is not a statement
about fixed-scheme lengths or the number of Frobenius-fixed points of an
unrelated scheme. No prime-field, torus-only, autonomous, smooth-fibre,
generic-parameter, or bounded-order restriction is permitted.

Stronger intermediate theorem: on the explicitly resolved smooth rational
surface (S_{t,s}), the source integral defines a morphism

\[
f_t:S_{t,s}\longrightarrow\mathbb P^1,
\qquad f_t^{-1}(\infty)=rD,
\]

where (D=-K_{S_{t,s}}) is the reduced eight-component boundary cycle.
Every finite **geometric** fibre is an integral, reduced Cartier curve
of arithmetic genus one and is contained in (U_{t,s}=S_{t,s}\setminus D).
This does not assert that the geometric generic fibre is smooth.

Excluded claims: the bin-distribution conjecture; an explicit
singular-value discriminant; generic smoothness in all characteristics;
a spectral-fibre/dynamical-fibre identification; a translation
classification; target Euler factors, root numbers, automorphy,
zero matching, or a Hilbert–Pólya realization. No assertion of global
priority is made.

## 2. Claims–evidence matrix and ownership

The rows are linked parts of one theorem, not separate paper claims.

| Claim | Complete existing evidence | Required manuscript location | Ownership and status |
| --- | --- | --- | --- |
| C1. Every ordinary native orbit obeys (r\mid\ell) and (\ell/r\le q+1+2\sqrt q) | P7 proof Sections 2.1, 5.2, 7–8; nonauthor review Sections 2, 5–6 | Theorem in Section 1; full proof in Sections 2 and 7 | The bound is the source's Conjecture 1.2.A; complete proof admitted in P7 |
| C2. Every finite geometric invariant fibre is integral, reduced and of arithmetic genus one | P7 proof Sections 3–6; nonauthor review Sections 3–5 | Geometric theorem preview in Section 1; proof in Sections 3–6 | The all-finite-fibre argument is the central residual after source ownership is deducted |
| C3. A nonconstant regular function on (U) has pole divisor (mD), and (r\mid m); the source integral realizes (m=r) | P7 proof Lemmas 3.1–4.1 and Section 5; nonauthor review Sections 3–5 | Complete boundary, lattice, face-polynomial and extension proofs in Sections 3–5 | Classical tools; explicit all-characteristic derivation for this surface. The matrix integral and its (-t^r x^{-r}) leading term are source-owned |

The source's map, seven-branch resolution, invariant, leading-term
calculation, proposed upper bound and autonomous discussion remain
credited to Joshi–Roffelsen. Carstea–Takenawa supplies earlier ownership
of roots-of-unity Halphen pencils, not a theorem to be automatically
specialized from a complex period map to every characteristic. The paper
must explain why an invariant alone is insufficient: it does not by
itself control every singular, reducible or multiple fibre.

The full reviewed argument and citation/access receipts are mapped in
[SOURCES_AND_EVIDENCE.md](SOURCES_AND_EVIDENCE.md). The original author
files retain their historical review-pending sentences; the actual
current P7 status is the subsequent PASS review and coordinator admission.

## 3. Planned article structure

### Abstract, unnumbered

Plan a compact, self-contained mathematical abstract, approximately
150–200 words as a readability guide, not a hard requirement.

- Open with the all-finite-field period theorem and define (r) and
  (\ell) before displaying the bound.
- Explain the obstacle: Hasse cannot be applied to arbitrary special
  fibres solely from the existence of a rational integral.
- State the method: integral boundary lattice, uniform pole divisor,
  minimal-pole divisibility, and every finite fibre integral of arithmetic
  genus one.
- State that singular fibres and characteristics two and three are
  included, and that the seven-branch resolved state space is retained.
- Do not claim the distribution conjecture, generic smoothness, the
  explicit discriminant, or an elliptic translation description.

This is an abstract plan; the global outline gate now authorizes drafting.

### Section 1. Introduction and main results

Planned file: `sections/01_introduction.tex`.

Opening problem: bound a complete native orbit when the nonautonomous
phase has finite multiplicative order. Define the relation between the
field-size symbol (q) and the iterative parameter (s), since the
traditional name “q-Painlevé” otherwise invites ambiguity.

State the full orbit theorem early, referring to the explicit branch
table in Section 2. State the stronger all-finite-fibre theorem using
the surface constructed in Section 3. Give a short proof roadmap:
boundary orthogonality and pole divisibility force an integral fibre;
normalization or Hasse bounds its rational points; the original clock
converts this into the orbit bound.

Positioning will be a focused subsection, not a mandatory full-page
literature survey. It will compare the source invariant and conjecture,
classical roots-of-unity Halphen geometry, and this proof's
all-characteristic/all-finite-fibre conclusion. Cite the accessed v2
numbering explicitly while giving verified published bibliographic
information. Do not infer a proof from stronger metadata-abstract
language. No “first ever” claim or worldwide search certificate.

Required citations: Joshi–Roffelsen; Carstea–Takenawa. A compact ownership
table is useful here; no hero image is planned.

### Section 2. The resolved states and the native clock

Planned file: `sections/02_states.tex`.

Give the precise finite state set, phase union and all seven native
branches:

| Input condition | New ((j',x',y')), always with (t'=st) |
| --- | --- |
| (j=0, sx\ne y) | ((0,st/(sx-y),sx/y)) |
| (j=0, sx=y) | ((1,0,t/x)) |
| (j=1) | ((2,0,st(1-sy))) |
| (j=2) | ((3,0,sy)) |
| (j=3) | ((4,0,s(sy-t)/t)) |
| (j=4, y\ne0) | ((0,-s^2t/y,1)) |
| (j=4, y=0) | ((1,0,0)) |

Prove bijectivity using **all seven inverse-state cases** from P7
Section 2.1, with target phase (T) and previous phase (T/s).
Explicitly verify the inverse to the (L_4) branch, whose source line
coordinate is (T(W+s)/s^3), and the zero-to-zero exceptional branch.
The finite state set is consequently a permutation system, not a
preperiodic system with possible tails.

Define the ordinary native period and reserve the proof of the exact
(\ell/r) return-period conversion for Section 7, after the invariant
has been extended at every state. Cite source Definitions 2.1–2.2 and
Algorithm 1; do not count the state encoding as a new construction.

### Section 3. The compactification and its boundary lattice

Planned file: `sections/03_surface.tex`.

Construct (S_{t,s}) by all eight blowups, including the infinitely
near centres. Distinguish total exceptional classes (E_i) from their
strict transforms. Give the blowup-centre table, the free Picard basis
(H_x,H_y,E_1,\ldots,E_8), and its integral intersection form.

List each actual boundary component (D_i) with its class, verify the
eight-cycle intersections, and compute

\[
D=\sum D_i=2H_x+2H_y-\sum E_i=-K_S,
\qquad D^2=DD_i=0.
\]

Identify (U=S\setminus D) exactly as the torus plus the four affine
lines (E_1,E_3,E_6,E_8) minus their boundary points. Display every
accessible chart. Intermediate exceptional components belong to (D),
not to extra ordinary states.

Typeset the **five forward extension formulas** of P7 Section 2.1:
the missing torus divisor and inputs (L_1,L_2,L_3,L_4). Check that all
denominators specialize to units at line points. Show explicitly that
the last formula is regular at (v=0), and that the (L_2) formula
uses the correct numerator and cubic denominator. No division by two
or three occurs.

Then prove the boundary-orthogonality lemma in full: write
(Z=aH_x+bH_y-\sum m_iE_i), give all eight linear equations, solve
them with two integers (u,v), and calculate

\[
Z^2=-8(u-v)^2,\qquad p_a(Z)=1-4(u-v)^2\ge0.
\]

Deduce (u=v=d>0) and (Z\sim dD). Emphasize that this is **linear**
equivalence in a free integral Picard group, and that intersection
numbers remain integers in characteristics two and three. This is not
just a numerical class calculation.

### Section 4. Uniform poles and the minimal-pole obstruction

Planned file: `sections/04_poles.tex`.

First prove the uniform-pole lemma for every nonconstant
(g\in\Gamma(U,\mathcal O_U)). Work over the algebraic closure when
choosing a constant avoiding finitely many boundary residues. Show that
nonnegative intersections sum to zero and the eight-cycle Laplacian
forces (\operatorname{div}_\infty(g)=mD), (m>0). Prove that zero
and pole divisors are disjoint; this gives a genuine morphism to
(\mathbb P^1), with no unresolved base points, and finite fibres
disjoint from the whole boundary.

Next prove (s^m=1). List all eight primitive toric valuation vectors
and the exponent polygon

\[
m\Delta=\operatorname{conv}\{(-m,0),(0,m),(m,0),(m,-m)\}.
\]

Explain why equal-valuation monomials cannot cancel as an entire
Laurent character polynomial. Define the four endpoint coefficients
(A,B,C,E), and prove (B\ne0) using the unique exponent with
(y)-degree (m).

Prove the smooth-boundary blowup multiplicity implication in a local
ring, not by derivatives or factorials. Include the four face-root
conditions and derive, without skipping the endpoint comparison,

\[
C=(-1)^mE,\quad A=(-t)^mB,\quad
A=(-t)^mE,\quad C=(-s)^mB.
\]

Since (tB\ne0), conclude (E=B\ne0), (s^m=1), and (r\mid m).
The proof must remain valid even if (m) is divisible by the field
characteristic. No complex period-map theorem is used as a substitute.

### Section 5. The source invariant and its exact polar divisor

Planned file: `sections/05_integral.tex`.

State the source's proved invariant theorem, with explicit attribution.
Display the three matrices (A_0,A_1,A_2) at gauge (w=1) and the
trace formula

\[
I_{r,t}=\operatorname{Tr}\bigl(A(s^{r-1})\cdots A(s)A(1)\bigr)
-(t^r+1),\qquad I_{r,st}\circ F_t=I_{r,t}.
\]

Explain the source's algebraic cyclic-trace/Lax mechanism briefly;
the invariant theorem is an explicit external input, not a claim to
have invented or independently reproved all of the source's Lax theory.

Give the complete reduction argument: (p\nmid r), the separability
of (X^r-1), the resulting cyclotomic specialization, and clearing
only powers of (x,y,t,s,sx-y) in the rational identity. There are no
integer denominators whose reduction might fail.

Prove extension to (U): the generic points of (L_4,L_3,L_2,L_1)
reach a torus in one, two, three, four forward steps, respectively;
use the Section 3 morphisms and invariance to exclude divisorial poles;
normality excludes a remaining isolated pole at a special line point.
Extend invariance itself by equality of regular functions on a dense
open subset. Every line coordinate, including zero, is thereby covered.

Reproduce and **credit the source's** idempotent-matrix computation of
the leading term (-t^r x^{-r}\ne0). Combine its exact order on
(D_5) with the Section 4 uniform-pole lemma to get the complete
polar divisor (rD) and the projective morphism (f_t).

### Section 6. Every finite fibre is integral and reduced

Planned file: `sections/06_fibres.tex`.

Fix **any** (c\in\bar k), not a generic value, and write its fibre
divisor as (C_c=\sum n_jZ_j\sim rD), disjoint from (D).
The Section 3 lemma gives (Z_j\sim d_jD), (d_j>0).
Explain that linear equivalence produces a rational function with
divisor (Z_j-d_jD); it is nonconstant and regular on (U), so the
Section 4 obstruction gives (r\mid d_j). Now write out

\[
\sum_jn_jd_j=r.
\]

Every summand is a positive multiple of (r); hence there is exactly
one component, with multiplicity one. Supply the scheme-theoretic
last step: the fibre is Cartier on a smooth surface, hence has no
embedded associated points; generic multiplicity one therefore implies
reducedness everywhere. Apply adjunction to obtain (p_a(C_c)=1).

Conclude the geometric theorem and explain exactly which feared cases
have been ruled out: reducible finite fibres, multiple finite fibres,
and their possible component permutations. A classification of Kodaira
types, a fibration section, smooth generic fibre, or quasi-elliptic
exclusion is not needed.

### Section 7. Rational points and the original least period

Planned file: `sections/07_periods.tex`.

Let a finite fibre over (k) contain an ordinary state. If the curve
is smooth, that point gives an elliptic curve, and the all-finite-field
Hasse theorem gives (\#C(k)\le q+1+2\sqrt q).

If it is singular, give the normalization exact sequence and derive

\[
1=g(\widetilde C)+\sum_Q\delta_Q.
\]

Explain perfect-field smoothness of the normalization and positivity
of each geometric singular contribution. There is exactly one
geometric singular point, and the normalization has genus zero.
If the normalization has a rational point, genus-zero Riemann–Roch
identifies it with (\mathbb P^1); otherwise its rational-point set
is empty. Every smooth rational point lifts uniquely. Therefore

\[
\#C(k)\le \#\widetilde C(k)+1\le q+2
\le q+1+2\sqrt q.
\]

Do not assume a split node, a cusp classification, a smooth rational
orbit point, or characteristic greater than three. Cite Sutherland's
Theorem 7.3 and the checked Stacks normalization/delta tags.

Finally finish the ordinary-clock proof: the phase makes (r\mid\ell);
the (r)-step fixed-phase map preserves the extended finite-valued
integral and has least period exactly (\ell/r). These are distinct
ordinary rational points of one finite fibre. Apply the appropriate
point bound. This proof must be present in full, not dismissed as an
unspecified “standard period reduction.”

### Section 8. Scope and conclusion

Planned file: `sections/08_conclusion.tex`.

Restate the exact all-state upper bound and the role of the
all-finite-fibre theorem. Briefly distinguish the proved upper-bound
part from the distribution conjecture and explicit discriminant, which
remain outside this result. State that no generic-smoothness theorem or
spectral identification was assumed. No speculative target-arithmetic
claims, experimental claims, or additional paper-sized contributions.

Bibliography follows the conclusion; no appendix is required by the
current proof plan.

## 4. Tables and figures

| Planned item | Purpose | Evidence source | Placement |
| --- | --- | --- | --- |
| Compact ownership comparison | Distinguish source invariant/Halphen context from the all-finite-fibre proof | P7 source/admission receipts and verified primary versions | Section 1 |
| Seven native branches | Make the exact dynamical object and all exceptional cases visible | Original P7 contract and source Algorithm 1 | Section 2 |
| Seven inverse-state cases | Prove that every state is periodic rather than merely eventually periodic | P7 proof Section 2.1 | Section 2 |
| Eight blowup centres | Resolve infinitely near centres and total-class conventions | P7 proof Section 2 | Section 3 |
| Four face-root conditions | Show the repeated endpoint comparisons giving (s^m=1) | P7 proof Lemma 4.1 | Section 4 |

No data plots or raster images are planned. The tables expose exact
case splits or repeated mappings; they are mathematical content, not
numerical evidence. A separate boundary-cycle picture would repeat the
explicit cyclic intersection statement, so it is omitted unless the
outline reviewer identifies a concrete readability benefit. All five
tables must fit legibly at 11 pt without shrinking an entire page.

## 5. Citation and evidence preparation

Planned bibliography keys and roles:

- `JoshiRoffelsen2026`: published article metadata, with the actual v2
  text/version explicitly identified for theorem and conjecture numbers;
  Sections 1–3 and 5.
- `CarsteaTakenawa2012`: published metadata plus accessed v2 for the
  roots-of-unity/Halphen context; Section 1 only unless needed to explain
  the period-map distinction in Section 4.
- `Sutherland2021`: the checked arbitrary-finite-field Hasse theorem;
  Section 7.
- `stacks-project`: tag-specific citations for normalization,
  delta invariants and genus comparison; Section 7.

The exact verified bibliographic fields, access limitations, source
ownership, proof-component map and immutable input digests are in
[SOURCES_AND_EVIDENCE.md](SOURCES_AND_EVIDENCE.md). No citation is to
be invented from memory or added merely to reach a reference quota.
Only the original proof's standard algebraic-geometric dependencies
are used; any newly requested precise reference will receive a targeted
check before entering a bibliography.

## 6. Review status, risk register and subsequent gates

Existing P7 mathematical review: PASS, no remaining mandatory correction.
Existing coordinator substantive/source decision: ADMIT ONE COMPLETE
SOURCE-SYSTEM CONTRACT. These concern the research proof, not a future
manuscript's completeness, readability or compilation.

Independent global outline review: **PASS, zero mandatory corrections**,
with coordinator closure recorded in the linked batch plan. The complete
review and approved plan were read before drafting. The review covered the
batch's C422 contract and architecture, not a line-by-line review of this
later detailed per-paper plan. No manuscript review has yet occurred.

Specific outline/manuscript risks to test:

1. A source-owned leading-term calculation must not be relabelled as
   new; the entire source invariant and chart construction stay credited.
2. A proof of generic irreducibility cannot replace Section 6's
   argument for each finite geometric fibre.
3. Section 3 must retain linear equivalence and the integral Picard
   lattice, because Section 6 needs an actual rational function for
   each component.
4. Special line points must be covered by morphisms and normality,
   not by naive substitution in a Laurent expression.
5. The local face-root argument and specialization must not divide by
   the characteristic; integer intersection identities remain integral.
6. Singular fibres must be counted via normalization, without assuming
   a smooth rational orbit point.
7. The native and return clocks must remain distinct until the final
   exact least-period argument.
8. The journal bibliographic entry must not silently change the
   accessed arXiv conjecture numbering.

Subsequent authorized sequence, contingent on coordinator handoff:

- Global independent outline approval is complete, with no mandatory edits.
- Read/use the applicable `paper-writing` and drafting instructions;
  write the complete anonymous article within this paper directory.
- Compile only after body authorization; obtain **two actual manuscript
  review rounds**, implement genuine findings and record affected rechecks.
- Use the explicitly disclosed current-team nonauthor fallback; do not
  claim an unavailable GPT-5.4 MCP or human external review occurred.
- Leave formal Route-A evaluation, global adjudication, final deterministic
  rebuild requirements, release ownership and Git operations with the
  coordinator unless separately assigned.

Skill receipt: `paper-plan` and its required writing-principles reference
were fully read and used for a single mathematical story, claim–evidence
mapping and explicit front-matter scope. The repository batch skill and
workflow retain the five-contract and independent-review gates. The
coordinator's explicit standalone-math/no-page-limit contract overrides
the planning skill's ML venue, hard page budget and obligatory hero-figure
defaults. After the coordinator closed the global gate, the complete
body and first baseline PDF were produced under the separate drafting
authorization. See [BUILD_REPORT.md](BUILD_REPORT.md) for actual output,
commands and remaining manuscript-review gates. No mathematical run,
external model, formal evaluator or Git mutation occurred.
