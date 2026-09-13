# Research Question

## Source-stage identity

- Candidate: henon_four_step_torus_escape_v1
- Safe title: **Four-Step Escape from Finite-Rank Tori for Monomial Hénon Maps**
- Literature freeze date: 2026-08-16
- Lifecycle: **SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**
- Authorization: source-design documents only
- Required next gate: a genuinely independent proof-and-citation review

This file fixes the exact mathematical question, the strongest currently
supported theorem, and its nonclaim boundary. It is not a source lock, review
record, experiment, result, or manuscript.

## Problem anchor

Let \(K\) be a field of characteristic zero, let \(d\ge 2\), and let
\(a,b,c\in K^\ast\). Consider the monomial Hénon automorphism

\[
H(x,y)=(b x^d+a y+c,x).
\]

Let \(\Gamma\le K^\ast\) be a multiplicative subgroup of finite rank \(r\).
No assumption is made that \(a\), \(b\), \(c\), or \(-1\) belongs to
\(\Gamma\).

For \(m\ge 0\), define the forward \(m\)-step torus-survival set

\[
T_m(H,\Gamma)
=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2
  \text{ for every }0\le j\le m\}.
\]

The research question is:

> Is there a bound for \(T_m(H,\Gamma)\), uniform in \(K,a,b,c\), that
> depends only on \(d\) and \(r\); what is the shortest universally finite
> window; and what periodic-orbit statement follows without confusing one
> torus-valued representative with an orbit contained in the torus?

## Primary theorem

Define

\[
\mathcal E_r
=
\exp\!\bigl(18^9(3r+1)\bigr).
\]

The exact proposed theorem is

\[
\boxed{
\#T_4(H,\Gamma)
\le
4d\,\mathcal E_r+81d^2.
}
\]

Equivalently,

\[
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

The four in \(T_4\) means that

\[
P,H(P),H^2(P),H^3(P),H^4(P)\in\Gamma^2.
\]

If

\[
H^j(P)=(x_j,x_{j-1}),
\]

then a point in \(T_4(H,\Gamma)\) supplies the four local recurrences with
indices \(i=0,1,2,3\):

\[
x_{i+1}=b x_i^d+a x_{i-1}+c.
\]

## Sharpness of the four-step threshold

The proposed threshold statement is:

> For every integer \(d\ge2\), there exist a number field \(K\), nonzero
> coefficients \(a,b,c\in K\), and a rank-one subgroup
> \(\Gamma\le K^\ast\) for which \(T_3(H,\Gamma)\) is infinite.

One exact family is obtained by choosing

\[
b=1,\qquad a=-1,\qquad c^{d-1}=-1,
\]

taking \(K=\mathbb Q(c)\), and putting

\[
\Gamma=\langle 2,c,-1\rangle.
\]

The elements \(c\) and \(-1\) are torsion, whereas \(2\) is not, so
\(\operatorname{rank}\Gamma=1\). For \(t=2^n\), \(n\ge0\), let

\[
P_t=(t,t^d).
\]

Then

\[
\begin{aligned}
H(P_t)&=(c,t),\\
H^2(P_t)&=(-t,c),\\
H^3(P_t)&=((-t)^d,-t),
\end{aligned}
\]

and all displayed coordinates lie in \(\Gamma\). The points \(P_t\) are
distinct, hence

\[
\#T_3(H,\Gamma)=\infty.
\]

Thus the proposed theorem is sharp in window length, not in the numerical
size of either summand in its upper bound.

## Weighted periodic-orbit corollary

For \(n\ge1\), let \(C_n^\Gamma(H)\) denote the number of exact-period-\(n\)
orbits \(\mathcal O\) satisfying

\[
\mathcal O\subseteq\Gamma^2.
\]

Each such orbit contributes exactly \(n\) periodic points, and every one of
those points lies in \(T_4(H,\Gamma)\). The safe periodic consequence is

\[
\boxed{
\sum_{n\ge1} n\,C_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

In particular,

\[
C_n^\Gamma(H)
\le
\frac{4d\exp(18^9(3r+1))+81d^2}{n}.
\]

The hypothesis \(\mathcal O\subseteq\Gamma^2\) is essential. A point
\(P\in\Gamma^2\) need not have \(H(P)\in\Gamma^2\), because \(\Gamma\) is
not additively closed.

## Why coefficient membership is absent

The local recurrence is rewritten as

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}
=1.
\]

The variable triple

\[
(x_{i+1},x_i^d,x_{i-1})
\]

belongs to \(\Gamma^3\), of rank at most \(3r\). The quantities

\[
\frac1c,\qquad -\frac bc,\qquad -\frac ac
\]

are fixed nonzero coefficients in \(K\), exactly as allowed by the
Evertse--Schlickewei--Schmidt theorem. They do not need to lie in
\(\Gamma\), and no coefficient-enlarged group is used.

## Scope

The primary theorem has exactly these quantifiers:

- every characteristic-zero field \(K\);
- every integer \(d\ge2\);
- every \(a,b,c\in K^\ast\);
- every finite-rank subgroup \(\Gamma\le K^\ast\) of rank \(r\);
- all points surviving from time \(0\) through time \(4\).

The bound is uniform in \(K,a,b,c\). Finite rank does not mean finitely
generated; the Evertse--Schlickewei--Schmidt input is used in its finite-rank
form.

## Secondary questions held outside the theorem

The following are possible later refinements, not proved claims of this
package:

1. a coefficient-stratified classification of all infinite \(T_3\) sets;
2. a corresponding \(T_2\)-versus-\(T_3\) hierarchy;
3. an optimal count of realizable four-letter degeneracy words;
4. improvements to the constants \(81d^2\) or
   \(\exp(18^9(3r+1))\);
5. classification of equality or near-equality cases.

Only the explicit rank-one \(T_3\) family above is promoted to a theorem.

## Complete nonclaims

This project does not claim any of the following:

- a bound for all rational periodic points;
- a bound for all integral periodic points;
- a bound for \(\operatorname{Per}(H)\cap\Gamma^2\) when only one point of
  an orbit is known to lie in \(\Gamma^2\);
- a theorem for \(d=1\), positive characteristic, or \(abc=0\);
- a theorem for arbitrary \(H(x,y)=(p(x)+ay,x)\);
- closure of \(\Gamma\) under addition;
- finite generation of every finite-rank \(\Gamma\);
- numerical optimality of \(81d^2\);
- numerical optimality of the ESS constant;
- optimality of the factor \(4d\);
- an effective enumeration algorithm for \(T_4\);
- a height bound for the surviving points;
- a classification of all infinite \(T_2\) or \(T_3\) strata;
- that every degeneracy word is realizable;
- that the explicit \(T_3\) family consists of periodic points;
- a positive-characteristic analogue;
- a computational, numerical, prime, modulus, or parameter-scan result;
- an unconditional global-priority claim over all unpublished work;
- any theorem belonging to the quartic sharp-cutoff candidate reserved for
  Paper 15.

## Paper 15 reserve

The competing quartic sharp-cutoff project is reserved as Paper 15. No
quartic theorem, proof ingredient, score, or evidence is imported into the
present claim package. The two projects must remain separately reviewable.

