# Bounded mathematical review — ASFS-20260915-DRC01

**Date:** 2026-09-15  
**Candidate status reviewed:** STOP — POSITIVE DERIVATIVE ROOF HAS FINITE-TIME ESCAPE.  
**Review outcome:** No mathematical blocker found in the stated P0 stop.

## Scope and provenance

This review checks the frozen [candidate card](../candidate-card.md),
the full [paper](../paper.md), and its claim ledger and summary. The map in
[147](../../147-saturated-drift-cotangent-sieve/candidate-card.md) was read
only to verify the displayed base-map comparison. Its unit-roof
completeness and analytic results are not premises for this new clock.

The reviewer is a separately dispatched model agent in the same research
session and model family. It communicated the direct bound and an
alternative endpoint argument to the author, then checked the author's
descended-observable proof. This is not blind review, external peer review
or evidence of independent error processes. Calibration: NOT_CALIBRATED.
No venue criteria, literature novelty or publication readiness were assessed.
ARS was used only for scoped evidence, claim boundaries and the
reviewer-only write constraint; no full publication panel was invoked.

## Verified claims

| Criterion | Evidence anchor | Finding | Scope |
| --- | --- | --- | --- |
| Exact clock identity | Paper equation (2); frozen card | MEETS: the roof is log of this map's configuration derivative | Different from 147's unit roof |
| Full allowed counterexample | Paper section 4, equation (5) | MEETS: n=2 has one empty block and every q_0>0 grows at least linearly | All initial momenta are retained |
| Entire infinite roof sum | Paper equation (6) | MEETS: an exact geometric majorant is summable | No finite truncation supports the conclusion |
| No endpoint in the actual quotient | Paper equations (7)--(8) | MEETS: the interpolated observable descends continuously and diverges | No global identification of raw q is assumed |
| Scope of the stop | Paper sections 5--7; claim ledger | MEETS: full-state completeness fails at P0 | No A1, A2 or Route credit is inferred |

The decisive arithmetic-free reduction is correct. Since b(2,1)=0,
q_{j+1}=q_j+(1/2)tanh q_j. With c=(1/2)tanh q_0>0, positivity
and monotonicity imply q_j>=q_0+cj. Both inequalities

\[
\log(1+x)\le x\quad(x\ge0),\qquad
\operatorname{sech}^2q\le4e^{-2q}\quad(q\ge0)
\]

have the directions needed for the upper bound. Therefore every term is
positive and the full sum satisfies

\[
0<S=\sum_{j\ge0}\tau(z_j)
\le\frac{2e^{-2q_0}}{1-e^{-2c}}<\infty.
\]

The momentum recurrence cannot invalidate this trajectory: every finite
iterate is globally defined and momentum enters neither its configuration
recurrence nor its roof.

## Endpoint check

The paper's function

\[
\mathcal Q(z,t)
=q+\frac{t}{\tau(z)}(f_{n,k}(q)-q)
\]

is continuous on the prequotient. Its values agree on every glued pair:
at the upper endpoint it is f_{n,k}(q), equal to the configuration
coordinate of Fz at the next lower endpoint. The quotient property thus
gives a continuous real-valued function on the actual frozen space.
On the escaping trajectory's j-th segment it lies between q_j and q_{j+1}.
As elapsed time tends to S, this forces Q to tend to positive infinity.
No point of the quotient has an infinite Q value, excluding a continuous
extension to time S.

An independent topological check reaches the same conclusion. The map
[z,t] -> [z,t/tau(z)] is a homeomorphism from the variable-roof quotient
to the unit mapping torus, as a space rather than a time-preserving flow
conjugacy. The zero section is consequently a closed embedded copy of M.
If the crossing points [F^j z,0] converged in the quotient, their limit
would lie in that section and F^j z would converge in M. Their diverging
configuration coordinates rule this out. This corroborates, but is not
needed in addition to, the paper's shorter Q argument.

## Coverage and nonclaims

No mathematical weakness was found in the checked base geometry, roof
inequalities, quotient argument or scoped stop. The complete central-cycle
classification, trace constructions, analytic continuation and target clock
were intentionally not assessed: the full-state completeness counterexample
already closes this screen negatively.

There is one nonmathematical locator inconsistency: section 5 refers to
“Proposition 1” while section 4 titles its unique result simply
“Proposition.” Numbering that heading would make the reference exact;
it does not affect any proof or gate conclusion.

**Author adjudication — ADDRESSED (2026-09-15):** section 5 now refers to
“the escape proposition.” The reviewer checked that exact updated wording.
The original observation above is retained as review history; no mathematical
input, proof or conclusion changed.

**Portfolio conclusion:** stop this derivative-roof candidate. A roof floor,
carrier restriction or compactification would be a new object. The
same-object ledger remains intact, formal Route coordinates are UNASSIGNED,
and Route B is NOT INVOKED.
