# Final Proposal: Low-Period Trace Fibers of Quartic Generalized Hénon Maps

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## One-sentence thesis

On the single-factor monic-centered quartic generalized Hénon space, pure
formal fixed traces first restrict the unknown Jacobian to three candidates,
periods one and two have exactly one positive-dimensional fiber, and a
period-three trace moment removes that fiber; hence the sharp quasi-finite
pure-trace cutoff is three.

## Problem anchor

Let

\[
f_{a,p}(x,y)=(a y+p(x),x),
\]

where \(a\in\mathbb C^\ast\) and \(p\) is monic centered. Let
\(\operatorname{Trace}_n(f)\) be the formal-period-\(n\) multiset of
\(\operatorname{tr}(D_zf^n)\), with intersection multiplicities, and put

\[
\mathfrak T_{\le P}
=
(\operatorname{Trace}_1,\ldots,\operatorname{Trace}_P).
\]

The goal is to determine the smallest \(P\) for which this pure trace map is
quasi-finite on \(\mathcal H^1_4\), without supplying the Jacobian, and to
classify the exact failure locus at the preceding period.

## Exact normalized scope

\[
\mathcal H^1_d
=
\{(a,p):a\in\mathbb C^\ast,\ p\text{ monic centered of degree }d\}.
\]

The residual diagonal group \(\mu_{d-1}\) acts by

\[
(a,p(x))
\longmapsto
\bigl(a,\zeta^{-1}p(\zeta x)\bigr),
\qquad
\zeta^{d-1}=1.
\]

The finite quotient is

\[
\mathcal M^1_d=\mathcal H^1_d/\mu_{d-1}.
\]

The proposal concerns only this single-factor space. It is not a theorem
about degree-\(d\) compositions or arbitrary loxodromic automorphisms.

## Unified main theorem

### Part A. Pure fixed traces enumerate the Jacobian

This lemma is valid over any algebraically closed field of characteristic
zero. Put

\[
s=1-a=1+J(f),
\qquad
q=p-sx,
\]

and let

\[
C_f(T)
=
\det\!\left(T-M_{p'}\mid k[x]/(q)\right).
\]

The formal fixed trace multiset determines \(C_f\), and

\[
\boxed{C_f'(s)=0.}
\]

Since \(C_f'\) has degree \(d-1\), fixed traces leave at most \(d-1\)
possible values of the Jacobian. For \(d=4\), the bound is at most \(3\).

The Jacobian is derived from pure trace data; it is not an input.

### Part B. Exact period-\(\le2\) exceptional locus

Over \(\mathbb C\), define

\[
E
=
\{(a,p)\in\mathcal H^1_4:
a=1,\ p=(x^2-L)^2,\ L\in\mathbb C\}.
\]

Then \(E\) is exactly the non-quasi-finite locus of
\(\mathfrak T_{\le2}\). Its common formal trace data is

\[
\boxed{
\operatorname{Trace}_1=0^{\times4},
\qquad
\operatorname{Trace}_2=2^{\times12}.
}
\]

The residual action sends \(L\mapsto\zeta L\), so

\[
\boxed{
E/\mu_3\simeq\mathbb A^1_{L^3}.
}
\]

### Part C. Sharp cutoff

Over \(\mathbb C\),

\[
\mathfrak T_{\le3}
\]

is quasi-finite on \(\mathcal H^1_4\) and on
\(\mathcal M^1_4\), while \(\mathfrak T_{\le2}\) is not. Therefore

\[
\boxed{
P_{\mathcal H^1}(4)=3.
}
\]

On the exceptional curve, the second power sum of the formal period-three
trace multiset is

\[
\boxed{
S_2^{(3)}(L)
=
-1296000-1572864L^3.
}
\]

It is an affine coordinate in \(L^3\), up to a nonzero scaling and
translation.

## Proof architecture

### 1. Fixed algebra and residue identity

The fixed equation is

\[
q(x)=p(x)-(1-a)x=0.
\]

Since \(p'=q'+s\), there are two cases.

If \(q\) is squarefree with roots \(\alpha_i\),

\[
\frac{C_f'(s)}{C_f(s)}
=
-\sum_i\frac1{q'(\alpha_i)}
=0.
\]

The last equality follows by taking the \(x^{d-1}\)-coefficient in the
Lagrange interpolation formula for \(1\).

If \(q\) has a root of multiplicity \(m\ge2\), then \(q'\) is nilpotent in
that local factor. Multiplication by \(p'=s+q'\) has the sole local
eigenvalue \(s\), so

\[
(T-s)^m\mid C_f(T),
\]

and again \(C_f'(s)=0\).

### 2. Every \(a\ne1\) candidate is finite

Pure fixed traces first enumerate at most three quartic values of \(a\).
For each candidate \(a\ne1\), Cantat--Dujardin Theorem 4.2 applies with its
required fixed Jacobian and gives a finite period-\(\le2\) fiber.

No form of Theorem 4.2 is invoked before this enumeration.

### 3. Period two on \(a=1\)

For \(a=1\),

\[
\operatorname{Fix}(f^2)
\quad\text{has algebra}\quad
\mathbb C[x,y]/(p(x),p(y)).
\]

On it,

\[
\operatorname{tr}(Df^2)
=
2+p'(x)p'(y).
\]

Thus the full length-\(16\) formal multiset is determined by the length-\(4\)
fixed multiset. Subtracting the embedded fixed cycle leaves the
length-\(12\) formal period-two multiset. Hence period two adds no new
fiber geometry on this slice.

### 4. Five quartic partitions

The \(a=1\) fixed-trace map is closed by:

- \([1111]\): apply Sugiyama only here. For \(h=x+p\), all four fixed
  multipliers are \(1+p'(\alpha)\ne1\), so the tuple lies in \(V_4\).
- \([31]\):
  \[
  p=(x-r)^3(x+3r),\qquad
  \operatorname{Trace}_1=\{0,0,0,-64r^3\}.
  \]
- \([211]\): with roots \(r,r,r+u,r+v\) and
  \(4r+u+v=0\),
  \[
  A=u^2(u-v),\qquad
  B=-v^2(u-v),\qquad
  \frac BA=-\left(\frac vu\right)^2.
  \]
  The ratio gives finitely many \(v/u\), then \(A=u^3(1-v/u)\) gives
  finitely many \(u\).
- \([22]\) and \([4]\):
  \[
  p=(x^2-L)^2,
  \]
  precisely \(E\).

The boundaries \(u=0\), \(v=0\), \(u=v\), and \(u=v=0\) land in the listed
lower partitions, so no closure case is omitted.

### 5. Formal period-three calculation

On \(E\), introduce

\[
F_i=(x_i^2-L)^2+\varepsilon(x_{i-1}-x_{i+1})
\]

and

\[
t_\varepsilon
=
q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2),
\qquad
q_i=4x_i(x_i^2-L).
\]

The quotient is monic free of rank \(64\). The same
\(t_\varepsilon\) is the complete-intersection Jacobian and, at
\(\varepsilon=1\), \(\operatorname{tr}(Df^3)\). Therefore

\[
\operatorname{Tr}(M_{t_\varepsilon^2})
=
\operatorname{Res}(t_\varepsilon^3).
\]

Weights first allow four terms. The separated double-root algebra removes
\(L^9\); the full Puiseux cluster analysis removes
\(L^6\varepsilon^2\). Thus

\[
S_2(L,\varepsilon)
=
C_2\varepsilon^6+D_2L^3\varepsilon^4.
\]

Two exact slope ledgers give

\[
D_2=-1572864.
\]

The normal-form recurrence ledger gives

\[
C_2=-1296000.
\]

On the fixed algebra \(q^2=0\), so the fixed contribution to the second
moment vanishes.

### 6. Formal lengths and quotient normalization

At a root \(\alpha\) of multiplicity \(r=2\) or \(4\), formal elimination
shows that the \(f^3\)-fixed local equation has order exactly \(r\). Hence
the fixed support contributes no residual formal period-three length after
subtraction.

The pointwise formal period-three length is

\[
64-4=60.
\]

Every remaining orbit has three points, so the cyclewise moment is

\[
-432000-524288L^3.
\]

Normalized conjugacy on \(E\) is \(L^3\), exactly matching the residual
\(\mu_3\)-quotient.

### 7. Quasi-finiteness

Every lower-period fiber outside \(E\) is finite. The exceptional lower
fiber is exactly \(E\), and equality of full period-three trace multisets
implies equality of their second moments, hence equality of \(L^3\).
Therefore every geometric period-\(\le3\) fiber is finite.

The trace map is of finite type, so finite geometric fibers imply
quasi-finiteness. The same argument descends through the finite quotient.

## Contribution hierarchy

1. **Dominant unified result:** exact lower failure locus plus sharp global
   quartic cutoff.
2. **Necessary bridge:** pure fixed traces enumerate the unknown Jacobian.
3. **Absorbed proof component:** the exceptional-curve period-three ledger
   originating in Paper 12.

The bridge and absorbed calculation are not parallel paper claims; both are
necessary parts of the dominant theorem.

## Literature boundary

- Cantat--Dujardin already provide the exceptional family, lower-period
  blindness, general trace rigidity, and an unspecified finite cutoff.
- Cantat--Dujardin Theorem 4.2 is used only over \(\mathbb C\), with fixed
  Jacobian, and only for \(a\ne1\).
- Sugiyama is used only on the simple-root stratum \(V_4\).
- Friedland--Milnor provide the normal-form framework.
- Multidimensional residue and formal-cycle methods are established prior
  art.
- The bounded search found no indexed direct statement of the unified
  package. This is not a priority claim.

## Publication relationship

Paper 15 is a unified strengthening that absorbs Paper 12's central theorem
and proof. Paper 12 remains provenance. The two must not be submitted as
parallel overlapping papers.

## Complete nonclaims

The proposal does not claim:

- injectivity or global uniqueness;
- an exact map degree or branch divisor;
- all-degree \(P(d)=3\);
- an effective cutoff in every degree;
- degree-four composition or arbitrary-loxodromic scope;
- Parts B--C over arbitrary characteristic-zero fields;
- positive characteristic;
- reduced-period replacement of formal cycles;
- novelty of the exceptional family or classical methods;
- novelty of the absorbed Paper 12 calculation;
- that one period-three moment separates every quartic map;
- a computation, experiment, scan, or numerical result;
- absolute priority.

## Required next gate

A fresh independent reviewer must:

- certify proof confidence at least \(9.0\);
- replay \(C_f'(s)=0\);
- verify Cantat--Dujardin and Sugiyama scopes from primary text;
- rederive all five root partitions and boundary cases;
- replay the two slope ledgers, constant ledger, and local-length argument;
- verify formal versus reduced conventions and the finite quotient.

Until that gate passes, this proposal remains an author-side source design.
