# Research Question

## Source-stage identity

- Candidate: henon_quartic_trace_fibers_v1
- Safe title: **Low-Period Trace Fibers of Quartic Generalized Hénon Maps**
- Literature freeze date: 2026-08-17
- Lifecycle: **SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**
- Authorization: exactly the ten source-design documents in this package
- Exit threshold: novelty at least \(6.5\), standalone size at least \(6.0\), and proof confidence at least \(9.0\)

This file fixes the problem, theorem scope, and nonclaim boundary. It is not
a source lock, an independent review, a paper plan, a manuscript, an
experiment, or a result.

## Problem anchor

For a monic centered polynomial \(p\in\mathbb C[x]\) of degree \(d\ge2\)
and \(a\in\mathbb C^\ast\), put

\[
f_{a,p}(x,y)=(a y+p(x),x).
\]

This is the single-factor monic-centered generalized Hénon normal form. Its
Jacobian is

\[
J(f_{a,p})=-a.
\]

For each \(n\), let \(\operatorname{Trace}_n(f)\) be the formal-period-\(n\)
trace multiset in the sense of Cantat--Dujardin: it records
\(\operatorname{tr}(D_zf^n)\) on the formal periodic zero-cycle, with
scheme-theoretic multiplicities. Define

\[
\mathfrak T_{\le P}(f)
=
\bigl(\operatorname{Trace}_1(f),\ldots,\operatorname{Trace}_P(f)\bigr).
\]

The bottom-line question is:

> On the single-factor normalized quartic space \(\mathcal H^1_4\), can
> pure formal trace data, without supplying the Jacobian, have an explicit
> sharp cutoff; and can the exact non-quasi-finite locus of
> \(\mathfrak T_{\le2}\) be classified?

## Normalized space and finite quotient

Write

\[
\mathcal H^1_d
=
\{(a,p):a\in\mathbb C^\ast,\ p\text{ monic centered of degree }d\}.
\]

For \(\zeta^{d-1}=1\), simultaneous diagonal scaling gives

\[
(x,y)\mapsto(\zeta x,\zeta y),
\qquad
(a,p)\mapsto
\bigl(a,\zeta^{-1}p(\zeta x)\bigr).
\]

This residual \(\mu_{d-1}\)-action preserves every trace multiset. The
finite normalized conjugacy quotient is

\[
\mathcal M^1_d=\mathcal H^1_d/\mu_{d-1}.
\]

No claim is made for a composition of several Hénon factors or for all
loxodromic polynomial automorphisms.

## Unified three-theorem package

The package is intentionally unified. The period-three cutoff by itself was
judged too small.

### Theorem A: pure fixed traces finitely enumerate the Jacobian

This part is algebraic and is stated separately over any algebraically closed
field \(k\) of characteristic zero.

Put

\[
s=1-a=1+J(f_{a,p}),
\qquad
q(x)=p(x)-s x,
\qquad
A_q=k[x]/(q).
\]

The fixed-point equation is \(q(x)=0\). Let

\[
C_f(T)
=
\det\!\left(T-M_{p'}\mid A_q\right),
\]

the characteristic polynomial determined by
\(\operatorname{Trace}_1(f)\). Then

\[
\boxed{C_f'(s)=0.}
\]

Consequently a prescribed formal fixed trace multiset leaves at most
\(d-1\) possible values of \(s\), hence at most \(d-1\) possible
Jacobians. In degree four the correct number is at most \(3\), never \(7\).

This is a pure-trace statement: \(J\) is an output candidate, not an input.

### Theorem B: exact period-\(\le2\) exceptional locus in degree four

This and the remaining theorem are scoped over \(\mathbb C\). Define

\[
E
=
\left\{
(a,p)\in\mathcal H^1_4:
a=1,\quad p(x)=(x^2-L)^2,\quad L\in\mathbb C
\right\}.
\]

Then the non-quasi-finite locus of

\[
\mathfrak T_{\le2}:\mathcal H^1_4\longrightarrow
\operatorname{Sym}^4(\mathbb C)\times
\operatorname{Sym}^{12}(\mathbb C)
\]

is exactly \(E\). Its lower-period fiber is

\[
\boxed{
\operatorname{Trace}_1=0^{\times4},
\qquad
\operatorname{Trace}_2=2^{\times12}.
}
\]

The residual action is \(L\mapsto\zeta L\) for
\(\zeta\in\mu_3\), so

\[
\boxed{E/\mu_3\simeq\mathbb A^1_{L^3}.}
\]

The proof must cover all quartic root partitions

\[
[1111],\ [31],\ [211],\ [22],\ [4]
\]

and all their closure relations. Sugiyama is used only on \([1111]\), where
the associated one-variable polynomial \(h(x)=x+p(x)\) has no multiple
fixed point. The strata \([31]\) and \([211]\) are handled explicitly;
\([22]\) and \([4]\) are precisely \(E\).

### Theorem C: sharp pure-trace cutoff three

The formal trace map

\[
\mathfrak T_{\le3}:\mathcal H^1_4\longrightarrow
\prod_{n=1}^3\operatorname{Sym}^{p_n}(\mathbb C)
\]

is quasi-finite. It descends to a quasi-finite map on
\(\mathcal M^1_4\). In contrast, \(\mathfrak T_{\le2}\) is not quasi-finite
on either space because \(E\), respectively \(E/\mu_3\), is
positive-dimensional.

Thus, for formal pure trace data on the single-factor quartic normalized
space,

\[
\boxed{P_{\mathcal H^1}(4)=3.}
\]

On \(E\), the separating invariant is already the second power sum of the
formal period-three trace multiset:

\[
\boxed{
S^{(3)}_2(L)
=
-1296000-1572864L^3
=
-384(3375+4096L^3).
}
\]

Equality of the full period-three multiset implies equality of this moment.
The moment is used only to separate \(E\); it is not asserted to classify all
quartic maps by itself.

## Why Theorem A must precede Cantat--Dujardin

Cantat--Dujardin Theorem 4.2 takes the Jacobian as part of its input and
applies when \(J\ne-1\), equivalently \(a\ne1\). It cannot by itself prove a
pure-trace theorem. The logical order is:

1. use \(\operatorname{Trace}_1\) and \(C_f'(s)=0\) to enumerate at most
   three quartic Jacobians;
2. for each candidate with \(a\ne1\), apply Cantat--Dujardin Theorem 4.2 to
   get a finite period-\(\le2\) fiber;
3. handle the remaining \(a=1\) slice by the five root partitions;
4. use the explicit period-three moment only on the exceptional curve.

## Formal-period convention

All multiplicities are scheme-theoretic. In particular:

- a nilpotent trace function has one formal eigenvalue with local-algebra
  multiplicity; it is not replaced by a reduced support value;
- at \(a=1\), the full \(f^2\)-fixed algebra is
  \(\mathbb C[x,y]/(p(x),p(y))\), and formal period two is obtained by
  subtracting the embedded formal fixed cycle;
- formal period three is the \(f^3\)-fixed cycle minus the fixed cycle;
- on \(E\), the local length of the \(f^3\)-fixed scheme at each fixed root
  equals the fixed-scheme length, and the remaining formal period-three
  cycle has pointwise length \(60\);
- the pointwise second moment is divided by \(3\), only after formal
  subtraction, to obtain the cyclewise value
  \[
  -432000-524288L^3.
  \]

## Publication relationship to Paper 12

Paper 15 is a unified strengthening that absorbs the theorem and proof of
Paper 12 into a larger global quartic trace-fiber theorem. Paper 12 remains
the provenance and local development artifact for the exceptional-curve
period-three calculation.

The two projects must not be submitted as parallel overlapping papers. Any
future publication path must choose the unified Paper 15 treatment or
otherwise withdraw the overlapping Paper 12 claim.

## Frozen anti-claims

This package does not claim:

- that the Jacobian is supplied to the trace map;
- injectivity, global uniqueness, or generic degree one;
- an exact degree, branch divisor, or fiber cardinality for the trace map;
- a result for degree-four compositions or all loxodromic automorphisms;
- a theorem over arbitrary algebraically closed characteristic-zero fields
  for Parts B or C;
- a positive-characteristic analogue;
- that reduced periodic points can replace formal periodic cycles;
- novelty of Cantat--Dujardin's exceptional family or general rigidity;
- novelty of residue identities, Sugiyama's theorem, Huguin's theorem,
  Morton-type fixed-point identities, or formal dynatomic methods;
- novelty of Paper 12's classification of \(E\) or its period-three ledger;
- \(P(d)=3\) for every degree;
- any effective all-degree cutoff;
- universal nonvanishing of a family of coefficients \(D_m\);
- that one period-three power sum separates all of \(\mathcal H^1_4\);
- an algorithm, computation, symbolic check, scan, or experiment;
- absolute priority or absence of unpublished work.

## Current disposition

The naked cutoff statement received **STOP** on standalone size. The unified
three-theorem package received a conditional **GO to source design only**.
Independent adversarial scores were:

- novelty: \(6.6\)--\(6.9\);
- standalone size: \(6.0\)--\(6.3\);
- proof confidence: \(9.2\)--\(9.5\).

The final synthesis was:

- novelty: \(6.9\);
- standalone size: \(7.4\);
- proof confidence: \(8.7\), lowered for transcription and theorem-scope
  risk.

Accordingly, this package has not passed its proof threshold. A fresh
reviewer must certify proof confidence at least \(9.0\), replay the formal
period ledgers, and verify every cited theorem's exact scope before any
source lock or later stage is possible.
