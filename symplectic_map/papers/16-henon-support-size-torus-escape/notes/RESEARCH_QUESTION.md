# Research Question

## Source-stage identity

- Candidate: `henon_support_size_torus_escape_v1`
- Safe title: **Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps**
- Literature freeze date: 2026-08-17
- Lifecycle: **SOURCE_DESIGN_AUTHOR_COMPLETE / PENDING INDEPENDENT SOURCE REVIEW / NO CODE / NO RESULTS / NO MANUSCRIPT**
- Authorized content: mathematical source design only
- Required next gate: fresh proof-and-citation review, followed by a source lock if and only if that review passes

This document fixes the problem anchor, exact theorem package, assumptions, and
nonclaim boundary. It is not a source lock, experiment, result log, manuscript,
submission authorization, or priority claim.

## Problem anchor

Let (K) be a field of characteristic zero. Fix distinct positive exponents

\[
1\le e_1<\cdots<e_s=d
\]

and nonzero coefficients

\[
a,c,b_1,\ldots,b_s\in K^\ast.
\]

Put

\[
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\qquad
H(x,y)=(P(x)+ay,x).
\]

The coefficient (a\ne0) makes (H) a generalized Hénon automorphism, with

\[
H^{-1}(X,Y)=\left(Y,\frac{X-P(Y)}a\right).
\]

Let \(\Gamma\le K^\ast\) be a multiplicative subgroup of finite rank (r);
finite generation is not assumed. For (m\ge0), define

\[
T_m(H,\Gamma)
=
\{Q\in\Gamma^2:H^i(Q)\in\Gamma^2\text{ for }0\le i\le m\}.
\]

Thus (T_m) records (m) transitions and (m+1) states. The bottom-line
question is:

> How does the number of nonconstant monomials in (P) change the shortest
> coefficient-uniform finite window for finite-rank torus survival?

The must-solve bottleneck is not the nondegenerate unit equation. It is the
complete treatment of its vanishing proper subsums without assuming that any
coefficient belongs to \(\Gamma\).

## Quantitative constants

For integers (q\ge2) and (R\ge0), define

\[
\mathcal A(q,R)
=(8q)^{4q^4(q+R+1)}.
\]

This is the Amoroso--Viada bound for nondegenerate solutions of a (q)-term
linear equation in a finite-rank subgroup. Its use over an arbitrary
characteristic-zero field is by base extension to the algebraic closure; the
original solution set injects and the group rank does not increase.

Define

\[
\mathcal S_q(d,r)
=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\qquad 2\le q\le s+1,
\]

and

\[
\mathcal S_\ast(s,d,r)
=\max_{2\le q\le s+1}\mathcal S_q(d,r).
\]

For a nonempty subset (J\subseteq[s]=\{1,\ldots,s\}), write

\[
e_{\max J}=\max_{j\in J}e_j,
\qquad
e_{\min J}=\min_{j\in J}e_j.
\]

The component/root budget is defined by the two explicit subset sums

\[
\boxed{
\begin{aligned}
\mathcal M(\mathbf e)
={}&2(2^s-1)\\
&+\sum_{\substack{J\subseteq[s]\\ |J|\ge2}}
  (e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
\end{aligned}}
\]

Two checks, neither of which replaces the defining subset sums, are

\[
\mathcal M(\mathbf e)
=2^{s+1}-2+\sum_{k=1}^s(2^k-2^{s-k})e_k
\]

and

\[
\mathcal M(\mathbf e)
\le
2(2^s-1)+d(2^{s+1}-s-2).
\]

## PC1: genuinely sparse two-transition finiteness

The dominant claim is the following.

> **Theorem PC1.** Assume (s\ge2). For every characteristic-zero field
> (K), every displayed choice of nonzero coefficients, and every finite-rank
> subgroup \(\Gamma\le K^\ast\) of rank (r),
> \[
> \boxed{
> \#T_2(H,\Gamma)
> \le
> d\,\mathcal A(s+2,3r)
> +\mathcal M(\mathbf e)\,\mathcal S_\ast(s,d,r).
> }
> \]

The first term counts initial states for which the first local equation is
nondegenerate. The second term covers every vanishing-proper-subsum type,
including simultaneous zero subsums, by a union bound. No coefficient is
adjoined to the variable group.

## PC2: the two-transition threshold is sharp

The supporting sharpness claim is uniform in the prescribed support.

> **Theorem PC2.** For every (s\ge2) and every prescribed sequence
> (1\le e_1<\cdots<e_s), there are rational nonzero coefficients and a
> rank-one subgroup \(\Gamma\le\mathbb Q^\ast\) for which (T_1(H,\Gamma))
> is infinite.

Take

\[
a=1,
\qquad b_1=\cdots=b_s=1,
\qquad c=-s,
\qquad \Gamma=\langle2\rangle.
\]

Then (P(1)=0), and for (n\ge0),

\[
Q_n=(1,2^n),
\qquad
H(Q_n)=(2^n,1).
\]

All these states lie in \(\Gamma^2\), and the (Q_n) are distinct. Thus the
shortest universally finite window in the support-size-(s\ge2) class is
exactly two transitions.

Over a characteristic-zero field containing all roots of unity, the same
construction with \(\Gamma=\mu_\infty\) shows that rank zero can already have
infinite (T_1). The headline uses the rational rank-one example because it
has the cleanest arithmetic scope.

## PC3: absorbed support-one theorem

When \(s=1\) and \(d\ge2\), write

\[
P(X)=c+bX^d,
\qquad
H(x,y)=(b x^d+ay+c,x).
\]

The support-one result is fully absorbed as the comparison half of the
support-size theorem package.

> **Theorem PC3.** If \(s=1\) and \(d\ge2\), then
> \[
> \#T_4(H,\Gamma)
> \le
> 4d\,\mathcal A(3,3r)+81d^2.
> \]
> For every (d\ge2), there are a number field, nonzero coefficients, and a
> rank-one subgroup for which (T_3(H,\Gamma)) is infinite.

The sharpness family is

\[
b=1,
\qquad a=-1,
\qquad c^{d-1}=-1,
\qquad
K=\mathbb Q(c),
\qquad
\Gamma=\langle2,c,-1\rangle,
\]

with

\[
Q_t=(t,t^d),
\qquad t=2^n,
\]

and scalar orbit segment, in the order \(x_{-1},x_0,\ldots,x_3\),

\[
t^d,\ t,\ c,\ -t,\ (-t)^d.
\]

The earlier local support-one project is retained solely as provenance. Its
terminal review hash is
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`,
and its final PDF hash is
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.
PC3 is reproduced and proved in this source package. The earlier project must
not be externally submitted in parallel with a Paper16 manuscript; any later
publication plan must treat Paper16 as the absorbing work and disclose the
provenance appropriately.

## Structural contrast

The theorem package establishes a support-size jump:

| Number of nonconstant monomials | Universally finite window | Sharp shorter failure |
|---:|---:|---:|
| (s=1) | (T_4) | (T_3) can be infinite |
| (s\ge2) | (T_2) | (T_1) can be infinite |

The extra monomial does not make the unit equation easier. It makes every
apparently free graph branch carry a genuinely multi-term sparse polynomial,
which finite-rank unit equations then bound.

## Assumption stress tests

### The nonzero constant is essential

If (c=0), the two-transition theorem is false. For

\[
P(X)=X^d+X,
\qquad a=-1,
\]

and every (t\in\Gamma),

\[
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t).
\]

Thus an infinite \(\Gamma\) gives infinite (T_2).

### The Hénon coefficient is essential

If (a=0), the second coordinate is forgotten and an arbitrary initial
second coordinate may survive. For example, choose a genuinely sparse
(P) with (P(1)=1). Then

\[
(1,t)\longmapsto(1,1)\longmapsto(1,1)
\]

for every (t\in\Gamma). Hence (a\ne0) is not cosmetic.

### Distinct-support convention

The integer (s) is the actual number of nonzero positive-degree monomials
after collecting equal powers and deleting zero coefficients. The theorem is
not stated for a syntactic presentation with repeated exponents.

## Complete nonclaims

This project does not claim:

- a positive-characteristic analogue;
- a theorem with (c=0), (a=0), or a zero (b_j);
- that support size is invariant under affine conjugacy;
- that the displayed constants are optimal;
- an effective enumeration algorithm for (T_2) or (T_4);
- a height bound for surviving points;
- a classification of rational or integral periodic points;
- a classification of all zero-constant free chains;
- a theorem for arbitrary rational maps or arbitrary polynomial automorphisms;
- finite generation of every finite-rank subgroup;
- coefficient membership in \(\Gamma\);
- closure of \(\Gamma\) under addition;
- a computational, numerical, prime, modulus, or parameter-scan result;
- a global priority claim over unpublished or unindexed work;
- authorization to create a manuscript, run an experiment, or submit either
  the absorbed predecessor or this project.

## Source-stage decision

The mathematical source design is **AUTHOR COMPLETE**. PC1 is the dominant
claim, PC2 is its minimal sharpness statement, and PC3 is an absorbed
comparison theorem rather than a parallel contribution. The next permitted
action is an independent source review. No scientific run is required or
authorized.
