# Source Lock — SD-C23

**Date:** 2026-08-14
**Primary family:** Symbolic Dynamics
**Authority object:** one-sided successor–divisor countable Markov shift and
its endpoint-weighted vertex adjacency
**Target-zero data:** forbidden and unused
**Route-B invocation:** forbidden

## 1. Full-shift semiring skeleton

For an \(n\)-letter alphabet \(A_n\), write

\[
 F_n=A_n^{\mathbb Z}
\]

up to topological conjugacy.  Freeze

\[
 F_m\boxtimes F_n
 :=F_{A_m\times A_n}\cong F_{mn},
\]

\[
 F_m\boxplus F_n
 :=F_{A_m\sqcup A_n}\cong F_{m+n}.
\]

The operation \(\boxplus\) means alphabet-sum followed by the full-shift
functor.  It is not the topological disjoint union of \(F_m\) and \(F_n\).
The frozen intrinsic data are

\[
 h(F_n)=\log n,
 \qquad
 S(F_n)=F_n\boxplus F_1=F_{n+1}.
\]

The skeleton realizes the positive-integer semiring inside one conjugacy
class representative per alphabet size.  No stronger categorical
universality is claimed.

## 2. Frozen edge grammar

The vertex set is

\[
 V=\{2,3,4,\ldots\}.
\]

Freeze

\[
 n\to d
 \quad\Longleftrightarrow\quad
 d\ge2\ \text{and}\ d\mid n+1.
\]

Equivalently, an edge exists when there is a unique exposed integer
\(q\ge1\) satisfying

\[
 S(F_n)=F_{n+1}
 \cong F_d\boxtimes F_q.
\]

The quotient label is

\[
 q(n,d)=\frac{n+1}{d}.
\]

It is allowed for audits and Paper22 filters.  It is not a prime predicate.

## 3. Phase space

The symbolic phase space is the one-sided countable edge shift

\[
 X_G^+
 =
 \{(n_0,n_1,\ldots)\in V^{\mathbb N}:
 n_j\to n_{j+1}\}.
\]

All periodic objects are directed closed words modulo cyclic rotation.
Reflection is not quotiented.  A primitive orbit is a closed rotation class
that is not a positive temporal power of a shorter class.

## 4. Frozen roof and operator

The edge roof is

\[
 \tau(n,d)=h(F_n\boxtimes F_d)
          =\log n+\log d.
\]

On

\[
 \mathcal H=\ell^2(V)
\]

with basis \(e_n\), freeze the column-source weighted adjacency

\[
 L_s e_n
 =
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}e_d.
\]

The object is called a weighted vertex adjacency or graph transfer.  It is
not identified with a Ruelle operator on a Hölder function space.

For a closed orbit

\[
 \gamma=(n_0,\ldots,n_{\ell-1}),
\]

freeze

\[
 N(\gamma)=\prod_{j=0}^{\ell-1}n_j,
\]

\[
 w_s(\gamma)
 =
 \prod_{j=0}^{\ell-1}(n_jn_{j+1})^{-s}
 =
 N(\gamma)^{-2s},
\]

\[
 T_\gamma=2\log N(\gamma).
\]

The factor two is part of the frozen roof and may not be removed after target
comparison.

## 5. Frozen determinant convention

On the proved domain

\[
 \operatorname{Re}s>\frac12,
\]

freeze the whole Fredholm determinant

\[
 D_{\rm SD}(s,z)=\det(I-zL_s).
\]

For sufficiently small \(|z|\),

\[
 -\log D_{\rm SD}(s,z)
 =
 \sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_s^r,
\]

\[
 D_{\rm SD}(s,z)
 =
 \prod_{[\gamma]\ {\rm primitive}}
 \left(
 1-z^{\ell(\gamma)}N(\gamma)^{-2s}
 \right).
\]

The Fredholm determinant is entire in \(z\).  The primitive product is
asserted only in its local absolute-convergence domain, not automatically at
\(z=1\).

## 6. Frozen target comparison

Only after the candidate is frozen may it be compared with

\[
 D_{\mathbb P}(s,z)
 =
 \prod_p(1-zp^{-s}),
 \qquad
 \operatorname{Re}s>1.
\]

No target zero is needed.  The comparison is coefficientwise:

\[
 [z]D_{\rm SD}(s,z)=0,
\]

whereas

\[
 [z]D_{\mathbb P}(s,z)
 =-\sum_pp^{-s}\ne0
\]

for real \(s>1\).

The scalar specialization \(D_{\rm SD}(s,1)\) is not promoted to a target
identity.  An isolated accidental equality at one \(s\) would not repair the
marked ledger.

## 7. Frozen theorem ledger

The manuscript may claim:

1. constructive strong connectivity;
2. path-sense topological mixing;
3. the simple primitive cycles
   \(C_k=(k,\ldots,2k-1)\) for all \(k\ge2\);
4. confinement of every length-\(r\) closed walk to
   \(\{2,\ldots,2r-1\}\);
5. uniqueness, up to rotation, of the extremal walk reaching \(2r-1\);
6. exact finite trace certification at cutoff \(N\ge2r-1\);
7. the necklace recurrence
   \(T_r=\sum_{d\mid r}dP_d\);
8. the sharp theorem
   \(L_s\in\mathcal S_1\) iff \(\operatorname{Re}s>1/2\);
9. trace-norm holomorphy and the same-object Fredholm determinant there;
10. the marked first-trace and composite-square orbit-norm obstructions;
11. persistence of the obstruction on the \(q\in\{1,2\}\) spine.

## 8. Forbidden claims

The manuscript must not claim:

- that the candidate determinant equals \(1/\zeta(s)\);
- that the determinant continues to or across
  \(\operatorname{Re}s=1/2\);
- a functional equation;
- a Gamma factor or completed Riemann divisor;
- the Riemann–von Mangoldt law;
- a Weil Hermitian compression;
- RH;
- a Hilbert–Pólya operator;
- that the literature search proves absolute priority.

## 9. Control lock

The principal graph control is the quotient spine retaining only

\[
 q\in\{1,2\}.
\]

It is strongly connected, mixing, has \(C_k\) for every \(k\ge2\), no loops,
and the same sharp trace-class threshold.  Its control margin is zero for the
properties that cause rejection.

The successor-only \(q=1\) graph is an acyclic negative control.  Positive
weight-inventory substitutions change weights but not the cycle set and must
be described only as weight controls.

## 10. Strict Route-A lock

\[
\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_FAIL},\\
 &\mathrm{A4\_FAIL}).
\end{aligned}
\]

Overall:

\[
\mathrm{ROUTE\_A\_REJECTED}.
\]

Required labels:

\[
\mathrm{STOP\_PRIME\_ORBIT\_LEDGER},
\quad
\mathrm{CYCLE\_FLOOD},
\quad
\mathrm{PRUNING\_PERSISTS},
\quad
\mathrm{PROVES\_TOO\_MUCH},
\quad
\mathrm{STOP\_SCOPED},
\quad
\mathrm{ROUTE\_B\_LOCKED}.
\]

The A2 verdict applies to the same-object determinant.  A3 remains failed
because no part of the target's completed global analytic structure is
reproduced.

## 11. Scope discipline

Symbolic Dynamics is the sole primary family in every section, figure, proof,
and control.  Any geometric, scattering, or self-adjoint carrier appears only
as a ROUND2_CLUE and is not developed.
