# Research Question

## Source-design status

This document fixes the mathematical question and the admissible theorem
package for **Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences:
Constant Anchors and the Exact Zero-Constant Boundary**.

The source design uses the following instruction sets:

- `proof-writer` for theorem normalization, character-lattice proofs, sharpness,
  and gap audits;
- `research-lit` for the bounded primary-source search and theorem-level scope
  comparisons;
- `novelty-check` for collision tests and portfolio penalties;
- `research-review` for adversarial GO/STOP criteria; and
- `writing-principles` for a single anchor-loss narrative rather than two
  adjacent notes.

The package is author-complete but still requires a separately authorized,
independent source review. It does not authorize a manuscript, computation,
experiment, source lock, build, or submission.

## The unified question

For a sparse shift-like polynomial automorphism, how many independent torus
directions can survive a prescribed finite recurrence window, and what exactly
happens when the nonzero constant term that anchors the character partition is
deleted?

The answer has two logically linked parts.

1. With a nonzero constant and at least two actual nonconstant monomials, each
   new recurrence equation removes one torus direction, in every dimension and
   for every shift type.
2. When the constant is zero, the planar case has an exact support phase: the
   only nonlinear two-step survivor is the binomial support `{1,d}` on the
   unique coefficient locus `a=-beta^2`, and that survivor closes at the third
   equation.

The common engine is the same group-algebra principle. A nonzero constant
creates an immovable trivial character. With at least two distinct powers of a
nontrivial middle character, two endpoint terms cannot prevent a singleton.
Deleting the constant leaves exactly enough room for a four-term pair
partition; the exceptional low/high alternation is Part B.

## Exact conventions

### Fields and tori

Geometry is taken over an algebraically closed field `Omega` of characteristic
zero. Arithmetic corollaries start with an arbitrary characteristic-zero field
`K`, an algebraic closure `Omega`, and a subgroup `Gamma <= K*` of finite rank:

`rank(Gamma/Gamma_tor) < infinity`.

Finite generation is not assumed. In particular, `Gamma_tor` may be infinite
and may contain all roots of unity.

A torus coset means `xi H`, where `H` is a connected algebraic subtorus of an
ambient multiplicative torus. If a possibly disconnected diagonalizable
subgroup is used instead, the statement applies component by component to its
identity component and hence gives the same dimension bound.

### The type-nu map and scalar orientation

Fix integers

`k >= 2`, `1 <= nu <= k-1`.

Let `a in K*` and `P in K[X]`. The type-`nu` shift-like automorphism is

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_{k-nu+1})+a z_1)`.

Its inverse is

`S^{-1}(w_1,...,w_k)=(a^{-1}(w_k-P(w_{k-nu})),w_1,...,w_{k-1})`.

Use zero-based scalar coordinates. If

`S^n(x_0,...,x_{k-1})=(x_n,...,x_{n+k-1})`,

then

`x_{n+k}=P(x_{n+k-nu})+a x_n`.                                      (R)

This orientation is fixed throughout. In particular, the one-step monomial
example in Part B is `(x_0,x_1,x_2)=(t^e,t,2t^e)`, not
`(t,t^e,2t^e)`.

### Survivor varieties and arithmetic windows

For every `m >= 0`, define

`V_m(S) <= (G_m)^(k+m)`

as the closed subvariety with coordinates `x_0,...,x_{k+m-1}` cut out by

`x_{n+k}=P(x_{n+k-nu})+a x_n`, `0 <= n <= m-1`.                      (V)

The symbol `<=` here denotes containment, not a subgroup assertion. Set

`V_0=(G_m)^k`.

For `Gamma <= K*`, define the `m`-transition survivor window by

`T_m(S,Gamma)={z in Gamma^k : S^j(z) in Gamma^k for 0 <= j <= m}`.

Projection to the first `k` coordinates gives a bijection

`V_m(S)(Gamma) = V_m(S) intersect Gamma^(k+m)  -->  T_m(S,Gamma)`.

Thus `m` counts recurrence equations or transitions, while the states run from
time zero through time `m`.

## Part A: anchored torus-coset decay

Write the polynomial in collected form

`P(X)=c+sum_{j=1}^s b_j X^(e_j)`,

where

`0<e_1<...<e_s`, `a,c,b_1,...,b_s != 0`, and `s>=2`.

The support is actual collected support: repeated exponents are combined and
zero resulting coefficients are deleted before `s` is counted.

### Theorem A

For every `0 <= m <= k` and every connected torus coset

`xi H subset V_m(S)_Omega`,

one has

`dim H <= k-m`.                                                       (A1)

The result is uniform in `nu`; it has no `gcd(k,nu)` hypothesis.

If `a=1` and `P(1)=0`, then equality is attained for every `0<=m<=k` by an
explicit saturated subtorus `H_m subset V_m` of dimension `k-m`. For every
prescribed exponent support this condition is realized, for example, by
`b_j=1` and `c=-s`.

Consequently, for every arbitrary finite-rank `Gamma <= K*`,

`T_k(S,Gamma)` is finite, hence so is `T_m` for every `m>=k`.           (A2)

The threshold is sharp in the coefficient-uniform sense: for every `k,nu` and
every prescribed support, the equality construction with `Gamma=<2>` gives
infinitely many points in `T_{k-1}`. The unique free zero-based initial index is

`q=k-1-nu`,

equivalently the one-based state coordinate `z_{k-nu}`.

### Exact equality model

For `0<=m<=k`, put

`R_m={n-nu mod k : 0<=n<m} subset {0,...,k-1}`.

The residues are distinct because the interval of `n` values has length at
most `k`; this is a translation modulo `k`, not iteration by `-nu`.

Define `H_m` by

- `x_r=1` for `r in R_m` among the initial coordinates;
- `x_{k+n}=x_n` for `0<=n<m`; and
- all other initial coordinates free.

Then `H_m` is a connected saturated subtorus isomorphic to
`(G_m)^(k-m)`, and every recurrence in (V) reads

`x_n=P(1)+x_n`.

At `m=k-1`, let the free coordinate `x_q=t`, set every other initial
coordinate to `1`, and copy future coordinates as above. Taking `t=2^N`
gives the rank-one infinite family in `T_{k-1}`.

## Part B: exact zero-constant planar phase

Part B fixes

`k=2`, `nu=1`, `c=0`,

so that

`S(x_0,x_1)=(x_1,P(x_1)+a x_0)`

and

`x_{n+2}=P(x_{n+1})+a x_n`.                                         (R0)

Write

`P(X)=sum_{e in E} b_e X^e`,

where `empty != E subset Z_{>=1}` is finite and every displayed `b_e` is
nonzero. Let `V_m^0` denote the corresponding variety in
`(G_m)^(m+2)`.

### Theorem B: geometric phase diagram

1. **Linear support.** If `E={1}` and `P(X)=beta X`, then for every `m`
   the variety `V_m^0` contains a one-dimensional torus coset. For any
   nonzero root `r` of `r^2=beta r+a`, it is

   `{(t,rt,...,r^(m+1)t):t in G_m}`.                                 (B1)

   Therefore no finite geometric window exists in the linear phase.

2. **Unique nonlinear two-step exception.** Let `d>=2`. If

   `P(X)=beta X+delta X^d`,

   then `V_2^0` contains a positive-dimensional connected torus coset if and
   only if

   `a=-beta^2`.                                                       (B2)

   On that locus the unique such coset is

   `C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d):t in G_m}`.    (B3)

   For all coefficients, including the resonant locus, `V_3^0` contains no
   positive-dimensional torus coset.

3. **Every other nonlinear support.** If `E` is nonlinear and is neither
   `{1}` nor `{1,d}`, then `V_2^0` contains no positive-dimensional torus
   coset. This includes every monomial `{e}` with `e>=2`, every binomial
   `{p,q}` with `2<=p<q`, and every support of size at least three.            (B4)

### Theorem B: arithmetic consequences and sharp examples

Laurent's torus theorem gives, for every characteristic-zero `K` and every
arbitrary finite-rank `Gamma <= K*`:

- `T_2(S,Gamma)` is finite for every nonlinear support except a potentially
  resonant `{1,d}` support;
- on the resonant `{1,d}` locus, `T_3(S,Gamma)` is finite; and
- no assertion of infinitude for a fixed `Gamma` follows merely from the
  geometric existence of `C_d`.

The resonance is arithmetically realizable: with

`beta=delta=1`, `a=-1`, `Gamma=<2>`,

the points

`(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d)`, `t=2^N`,

give infinitely many members of `T_2`.

Every other nonlinear support can have an infinite one-step window:

- for a monomial, take `P=X^e`, `a=1`, and the correctly oriented tuple
  `(x_0,x_1,x_2)=(t^e,t,2t^e)` with `t=2^N` and `Gamma=<2>`;
- for any prescribed support of size at least two, choose nonzero rational
  coefficients with `P(1)=0`, take `a=1`, and use
  `(x_0,x_1,x_2)=(t,1,t)`.

Thus Part B is an exact geometric phase diagram plus compatible arithmetic
sharpness, not a claim that every geometric coset has infinitely many points
over every finite-rank group.

## Laurent input and the finite-rank bridge

The only indispensable external proof theorem is the torus case of Michel
Laurent's 1984 Mordell--Lang theorem. In the form needed here: if `X` is a
closed subvariety of a complex torus and `Delta` is the division group of a
finitely generated subgroup, then `X intersect Delta` is a finite union of
intersections with torus cosets contained in `X`. Therefore the absence of a
positive-dimensional torus coset implies finiteness.

The arbitrary-field and infinite-torsion scope is not assumed silently. Given
finite-rank `Gamma`, choose finitely many representatives whose classes form a
`Q`-basis of `Gamma tensor Q`, and let `Gamma_0` be the subgroup they generate.
For every `gamma in Gamma`, some positive power of `gamma` lies in `Gamma_0`;
hence

`Gamma subset Gamma_0^div`.

This includes arbitrary torsion because each torsion element already lies in
the division group of the identity. Let `L` be the field generated over `Q` by
the finitely many map coefficients and generators of `Gamma_0`. Then `L` is a
finitely generated characteristic-zero field and embeds in `C`; all elements
of `Gamma` are algebraic over `L`. Embedding an algebraic closure of `L` into
`C` reduces the required intersection to Laurent's complex theorem. The result
is qualitative: no cardinality bound or effective enumeration is extracted.

## Exact relation to Paper16

Paper16 is the terminal project

`papers/16-henon-support-size-torus-escape`.

It proves, for the planar generalized Henon map with `c!=0`:

- an explicit finite cardinality bound at `T_2` for actual support `s>=2`,
  with `T_1` sharp; and
- the fully absorbed support-one theorem with an explicit `T_4` bound and
  `T_3` sharpness.

Paper17 neither absorbs nor improves those quantitative planar statements. Its
`k=2` anchored endpoint is only a weaker qualitative shadow of Paper16. The
new contribution is the all-`k`, all-`nu`, all-window torus-coset dimension law
and the exact `c=0` planar boundary. Paper16 remains a separate, closed
predecessor and must not be repackaged here. Paper14's support-one result is
already fully absorbed by Paper16; Paper17 neither revives Paper14 nor claims a
second absorption.

## Credible article size and unity gate

The intended article has **about 22 substantive content pages**, with no
appendix padding and references excluded from the count:

| Content block | Pages |
|---|---:|
| Introduction and anchor-loss question | 1.75 |
| Shift-like setup, survivor varieties, and Laurent bridge | 2.25 |
| Common group-algebra/character framework | 2.00 |
| Part A dimension theorem and independence proof | 4.00 |
| Part A equality and arithmetic sharpness | 2.00 |
| Part B local partition calculus | 3.50 |
| Part B phase theorem, resonance, and closure | 4.00 |
| Paper16 boundary, examples, and scope audit | 1.50 |
| Related work and limitations | 1.00 |
| **Total substantive content** | **22.00** |

This budget is justified by distinct proof obligations, not repeated examples.
Both parts use the same survivor varieties, character restrictions, singleton
principle, and Laurent corollary. Part B is the exact failure mode of the
constant-anchor step in Part A, so the article is unified rather than a
two-result miscellany.

## Fifteen locked anti-claims

The project must stop any statement that does one of the following:

1. says that `T_m` itself is positive-dimensional rather than identifying a
   torus coset in `V_m`;
2. says resonance makes `T_2(S,Gamma)` infinite for every `Gamma`;
3. says `a=1` and `P(1)=0` are necessary for equality in Theorem A;
4. inserts a `gcd(k,nu)` hypothesis or conclusion;
5. replaces the killed set by an iterated orbit under `j -> j-nu` rather than
   the translation `{n-nu mod k}`;
6. says nonlinear monomials have no finite window in the `c=0` phase;
7. claims an effective cardinality bound or algorithm from Laurent;
8. markets the standard character-partition lemma by itself as the novelty;
9. extends the theorem to positive characteristic, `a=0`, rational/Laurent
   maps, or arbitrary polynomial automorphisms;
10. treats actual support as invariant under affine conjugacy;
11. replaces finite rank by finite generation or assumes bounded torsion;
12. claims to improve Paper16's explicit planar cardinality bounds;
13. turns a bounded search into a global priority claim;
14. claims a classification of all equality or maximal cosets in Part A; or
15. claims height bounds, periodic-point classifications, or effective
   enumeration.

## Source-stage decision

The theorem package is internally coherent, has a complete author proof in
`PROOF_PACKAGE.md`, survives the Paper16 portfolio penalty, and supports the
22-page target without padding.

**SOURCE-DESIGN DECISION: GO TO INDEPENDENT SOURCE REVIEW ONLY.**
