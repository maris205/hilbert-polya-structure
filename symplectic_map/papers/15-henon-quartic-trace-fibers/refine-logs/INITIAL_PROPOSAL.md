# Initial Proposal

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Problem anchor

On the single-factor monic-centered generalized Hénon normal form

\[
f_{a,p}(x,y)=(a y+p(x),x),
\]

determine whether pure formal trace data, without supplying the Jacobian, has
an explicit sharp cutoff in degree four, and classify the exact
period-\(\le2\) non-quasi-finite locus.

This anchor is immutable. It excludes degree-four compositions, all
loxodromic maps, reduced-only periodic data, and any hidden fixed-Jacobian
input.

## Historical starting point

The first candidate was the short assertion

\[
P_{\mathcal H^1}(4)=3.
\]

Its intended lower bound came from the Cantat--Dujardin family

\[
f_L(x,y)=\left(y+(x^2-L)^2,x\right),
\]

whose period-one and period-two trace multisets are constant. Its intended
upper bound came from the already-developed formal period-three moment

\[
-1296000-1572864L^3.
\]

## Why the naked proposal stopped

The naked cutoff was mathematically suggestive but not yet a standalone
paper:

1. It proved period three only on one known curve, not on all of
   \(\mathcal H^1_4\).
2. It did not explain why every other period-\(\le2\) fiber was finite.
3. It risked applying Cantat--Dujardin Theorem 4.2 as though the Jacobian
   were supplied, contradicting the pure-trace problem.
4. It did not classify the full \(a=1\) boundary.
5. It would duplicate Paper 12's local calculation without a sufficiently
   larger theorem.

The independent size verdict was therefore **STOP**.

## First repair: remove the hidden Jacobian

Let

\[
s=1-a,
\qquad
q=p-sx,
\qquad
C_f(T)=
\det\!\left(T-M_{p'}\mid k[x]/(q)\right).
\]

The fixed trace multiset determines \(C_f\). The key proposed bridge became

\[
C_f'(s)=0.
\]

Since \(C_f'\) has degree \(d-1\), fixed traces leave at most \(d-1\)
Jacobians. In degree four, at most three candidates remain. This is the
correct bound; the discarded value seven was a transcription error from an
unrelated elimination count.

Only after this finite enumeration may Cantat--Dujardin Theorem 4.2 be
applied to candidates \(a\ne1\).

## Second repair: close the \(a=1\) slice

When \(a=1\), period-two formal trace data is determined by fixed trace
data. The quartic root partitions are

\[
[1111],\ [31],\ [211],\ [22],\ [4].
\]

The refined route assigned one exact method to each:

- \([1111]\): Sugiyama only on \(V_4\), because all fixed multipliers of
  \(h=x+p\) differ from \(1\);
- \([31]\):
  \[
  p=(x-r)^3(x+3r),\qquad
  \operatorname{Trace}_1=\{0,0,0,-64r^3\};
  \]
- \([211]\): with centered roots \(r,r,r+u,r+v\),
  \[
  A=u^2(u-v),\qquad
  B=-v^2(u-v),\qquad
  \frac BA=-\left(\frac vu\right)^2;
  \]
- \([22]\) and \([4]\):
  \[
  p=(x^2-L)^2,
  \]
  exactly the exceptional curve \(E\).

No singular-stratum extension of Sugiyama is used.

## Third repair: unify Paper 12 rather than duplicate it

The local period-three calculation from Paper 12 is not treated as an
external theorem. Its formal subtraction, two exact slope ledgers, constant
ledger, local fixed-branch lengths, residual \(\mu_3\), and
pointwise/cyclewise normalization are reproduced in the new proof.

The publication relationship is fixed:

- Paper 15 is the unified strengthening;
- Paper 12 is provenance;
- the overlapping central results must not be submitted as parallel papers.

## Strengthened proposal selected

The only viable proposal became:

1. fixed traces leave at most \(d-1\) Jacobians;
2. the exact non-quasi-finite locus of
   \(\mathfrak T_{\le2}\) on \(\mathcal H^1_4\) is
   \[
   E=\{a=1,\ p=(x^2-L)^2\};
   \]
3. \(\mathfrak T_{\le3}\) is quasi-finite globally and on the finite
   quotient, while period two is not.

This is one dependency chain, not three unrelated contributions.

## Scope repairs

The overall theorem is over \(\mathbb C\). The fixed-algebra identity alone
is stated over an algebraically closed characteristic-zero field.

No faithful-flat or base-change descent is supplied for
Cantat--Dujardin Theorem 4.2 or Sugiyama, so no broader field statement is
allowed for the global quartic theorem.

## Initial anti-claims

The refined proposal does not claim:

- injectivity;
- exact fiber cardinality or degree;
- a branch divisor;
- a result for compositions;
- positive characteristic;
- \(P(d)=3\) for all \(d\);
- an effective cutoff in every degree;
- novelty of the exceptional family or classical methods;
- that one moment separates all quartic maps;
- computational evidence;
- absolute priority.

## Refinement decision

**CONDITIONAL GO TO SOURCE DESIGN ONLY.**

The strengthened package may be documented, but not source-locked or
advanced. The final synthesis proof score is \(8.7/10\), below the required
\(9.0\). A fresh reviewer must close that gap.
