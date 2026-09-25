# Broadened analytic-owner card — ANG-20260915-LKC01

Version 1, frozen 2026-09-15 before the mathematical audit. Initial T0--T3
audit outcomes OPEN. This is a new analytic contract over a fully redefined
localization groupoid, not a modification of 146 or a new classical map.

## Exact carrier and source

For every integer n>=2 form E_n={d>=1: d divides n^k for some k>=0} and
the actual subring A_n=Z[1/n] of Q. The index set I consists of every
distinct such actual subring, with equality of subrings and no selected n
representative. For A in I let U_A={q in Q_{>0}:qA=A}.

Objects are (A,u), u in R. Arrows (A,u,q), q in U_A, go from (A,u) to
(A,u+log q); composition multiplies q. All A and q indices are discrete;
each u line has its ordinary topology. Time phi^t translates u by t on
objects and arrows. No roof is inserted. Every component and every
time-return arrow remains in the carrier.

The source arrow is local divisor admissibility -> power-saturated
denominator admissibility E_n -> actual localization and unit action.
This is an explicit replacement within the prime-symbolic lineage, not
a chronological sieve conjugacy and not a Logistic/Hénon geometric lift.

## Frozen analytic construction

For each A set B_A={f in C^infinity(R;C): f(u+log q)=f(u) for every q in U_A}.
Use the groupoid-basic de Rham complex

\[
\mathcal B^0=\bigoplus_{A\in I}^{\mathrm{alg}} B_A,
\qquad
\mathcal B^1=\bigoplus_{A\in I}^{\mathrm{alg}} B_A\,du,
\qquad d f=f' du.
\]

The differential is the one-coordinate differential/Koszul form
du wedge partial_u. This is not claimed to be the full bar complex of the
groupoid, group cohomology of U_A, or a transverse exterior complex.

The Hilbert completion in each degree is proposed from the SAME rule

\[
\|f\|_A^2=\lim_{R\to\infty}\frac1{2R}
\int_{-R}^{R}|f(u)|^2\,du,
\qquad
\|\eta\|^2=\sum_{A\in I}\|\eta_A\|_A^2.
\]

Existence, definiteness and the component description of this norm must
be proved. The constant form du has norm one relative to the u coordinate.
No support-dependent coefficient multiplies this mean or direct sum.

For epsilon>0 use the uniform real Gaussian

\[
g_\epsilon(v)=(4\pi\epsilon)^{-1/2}e^{-v^2/(4\epsilon)},
\quad (Q_\epsilon f)(u)=\int_\mathbb R g_\epsilon(v)f(u+v)\,dv,
\quad (V_t f)(u)=f(u+t).
\]

The same formulas act on coefficients of 1-forms. The operator under
audit is R_{epsilon,t}=Q_epsilon V_t on both Hilbert degrees. The target
is its ordinary unweighted supertrace Tr(R^0)-Tr(R^1), only if both
ordinary traces are justified, and its possible epsilon-to-zero return
distribution. No subtraction of two undefined infinite traces is allowed.
Finite-component direct sums may be used only as labelled controls.

## Discriminator, controls and stop condition

1. Check the full groupoid/basic complex, norm and action ownership.
2. Compare the degree-0 and degree-1 actions already on a rank-one circle.
3. Check full direct-sum trace class using its constant channels.

Controls: actual repeated localization labels; mixed-support component;
single rank-one circle as positive scalar trace control; finite-component
cutoffs versus full trace; degree-0-only extraction as a changed analytic
observable. At least three are required in the full record.

Stop this contract if its unweighted grading also cancels the prime-circle
returns, or if the precommitted full ordinary supertrace is undefined.
Do not add degree weights, torsion, component damping, quotient traces,
rank-one selection, or a different complex inside this candidate.

| Field | Frozen owner / boundary |
| --- | --- |
| Packets | All time returns up to arrows; least positive return only where it exists |
| Analytic owner | Basic complex and normalized-mean Hilbert completion above |
| Trace normalization | Ordinary traces in each degree; signs +1 and -1 only |
| Time normalization | Original real translation; no prime-log roof insertion |
| Classical map / symplectic form / mapping torus | NOT APPLICABLE |
| Hamiltonian/contact/quantum owner | DEFERRED |
| Formal Route coordinates | UNASSIGNED |
| Route B | NOT INVOKED |

Changing the analytic owner requires a fresh card. The prior object is
[146](../146-localization-scaling-groupoid/paper.md), used for collision
and scope comparison rather than automatic analytic credit.

## Appended audit outcome — version-1 definitions unchanged

**Candidate ID:** ANG-20260915-LKC01  
**Status:** STOP — BASIC GRADING CANCELS PRIME RETURNS; FULL ORDINARY SUPERTRACE UNDEFINED.  
**Decision:** stop this analytic contract.

The [paper](paper.md) proves the full groupoid and return classification,
the uniform-mean completion, and bounded ownership of the specified
smoothed time action. The map J(f)=f du pairs its two degrees unitarily.
Each prime-circle scalar trace has the actual return distribution
L sum_k delta_(kL), L=log p, but its unweighted graded contribution
vanishes for every smoothing parameter. On the complete direct sum,
each degree fixes infinitely many orthonormal constant channels and
is not trace class. The ordinary supertrace stipulated above is
therefore undefined, not a finite cancellation of two ordinary traces.

Finite-component supertraces and the explicitly paired difference
before trace are well-defined and zero. Neither gives prime-only
returns. All mixed components remain in the carrier; the basic
representation, not the carrier, loses some return information.
No different complex or weight was substituted.

T0 and scoped T1 ownership are established; complete T2 returns retain
the nonprimitive mixed components. The specific T3 unweighted filtering
and full ordinary-supertrace proposals stop. All other cohomological,
weighted or relative constructions remain OPEN. The same-object ledger
is INTACT; classical fields NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. See the [claim ledger](claim-ledger.md) and
[evidence index](evidence/README.md).
