# Fresh07 independent candidate gate 01

Reviewer: /root/round211_functional_surgery_residual.
Author: /root/round211_fresh_residual_scout. Date: 2026-09-09 UTC.

## Decision

**EXACT_REPAIR_REQUIRED.** There is one current MINOR documentary finding,
F07-SOURCE-01, and no identified mathematical or executable discrepancy.
After that exact source-label erratum is accepted, the supported disposition
is **GO_NARROW**, not KILL. No admission, paper number, manuscript-review
acceptance, global novelty certificate or external release is issued here.

The independent mathematical and residual-value assessment supports this
bounded theorem conjunction: complete fixed-point recurrence and terminal
map with sharp full-carrier height; evaluated all-target one-step inverse
by independent integer intervals; fixed-target specialization and exact
largest-fibre growth exponent. It does not support an exact finite-mass
maximum/maximizer classification or an all-time inverse theorem.

The original author packet remains immutable, pinned by
[AUTHOR_INPUT_PINS.sha256](AUTHOR_INPUT_PINS.sha256), including manifest
499d60b8c427e188c62cf9548907070030ca17e4d3c5b0fbe25dd6a39a735414.
A separate accepted text-only amendment can close the single finding;
neither scientific source nor a new pilot is needed for that correction.

## Independence and chronology

This reviewer made no contribution to the submitted fresh07 proof or pilot.
The author announced the final seal before content intake; earlier discovery
was filename-only. The complete submitted proof, source, original pilot
native, collision notes and declared read limits were received, then reviewed.
This is a noncontributor candidate gate, not either manuscript-review round.

The author executed one pilot at n=3,4,5 and N=0,...,6: 756 states in
21 carriers. Its original exit-zero native result is retained in the pinned
author PILOT_NATIVE.json, with 61,482 ASCII output bytes and 779 LF records.
The separate author PILOT_ACTUAL.txt is deliberately that output plus one
extra LF, not a byte-identical raw canonical. The reviewer parsed all 756
archived rows and checked unique state names, successor/depth/terminal
metadata and indegrees against the archived edges without evaluating F.

Sections 4–5 of the final author proof were completed after that pilot.
Its executable has no comparison-word interval implementation or tests for
the fixed-target product or growth exponent. Printed indegrees do not change
this fact. The new reviewer run below is separate evidence; it does not
retroactively make the original pilot an inverse-formula test.

## Literal and temporal audit

The full carrier is labelled nonnegative cyclic integer vectors of length
n>=1 and mass N>=0. The old-state current is q_i=min(a_i,a_(i+1)), and
F(a)_i=a_i-q_i+q_(i-1). Labels, zero coordinates, uniform states and small
lengths are not quotiented or discarded. For n=1,2 the map is the identity.

An independent useful representation is
F(a)_i=max(a_i-a_(i+1),0)+min(a_(i-1),a_i).
It proves nonnegativity; the current form telescopes mass. Translating every
coordinate by the same c translates F by c. At a zero coordinate both
summands are zero, so after subtracting the minimum the minimum remains zero.

Cut at a residual zero. On a positive run the cumulative prefix mass S_j
satisfies S_j'=S_j-q_j; the run endpoint has zero outgoing current.
If a positive site has a positive predecessor, its inflow is positive and
it cannot disappear in that step. Thus only the first positive site can
vanish; original zero separators prevent inter-run transport or merging.
Before a run becomes a singleton, its original right endpoint gains at
least one unit each round. This integer quantity is bounded by the original
run mass M, so the run must terminate there, holding exactly M. The bound
is M minus its initially positive endpoint mass. This reconstructs the
terminal map and excludes every strict cycle without using the inverse.

For n=3 a normalized nonfixed run has two entries (A,B) and total M.
The endpoint obeys B_t=min(2^t B,M), hence exact depth is the least t with
2^t B>=M. Taking B=1 and residual mass N gives the sharp height
ceil(log_2 N), including N=1 where it is zero. At N=0 it is zero.
For n>=4 the bound is N-1. At N>=3 the fixed-label witness
(N-2,1,1,0,...,0) has successive triples
(N-2-t,1,1+t) for 0<=t<=N-2, and needs one additional round after the
leading coordinate becomes zero. N=2 uses (1,1,0,...,0); N=1 is fixed.
No pointwise closed clock for all n>=4 has been smuggled into this result.

## Independent inverse audit

For a target y, introduce nonnegative integer edge currents q and reconstruct
a_i=y_i-q_(i-1)+q_i. The equations q_i=min(a_i,a_(i+1)) are equivalent to

    u_i=y_i-q_(i-1)>=0,
    v_i=y_(i+1)+q_(i+1)-2q_i>=0,
    u_i*v_i=0.

Indeed u_i=a_i-q_i and v_i=a_(i+1)-q_i. These inequalities imply
a_i>=q_i>=0 and the complementarity gives the minimum equality.
They also imply q_i<=y_(i+1). Conversely every source gives its unique
current vector. This independently derived integer-complementarity
description is only a checking reference; generic flux feasibility receives
zero research-axis credit.

Eliminating these constraints with the author's unique weak-ascent/strict-
descent word gives its four local linear equations. Ties go only to ascent.
The all-descent cycle is impossible; an all-ascent cyclic word is uniform.
In every mixed word, valleys fix their own coordinate. Strict descent
interiors are forced backwards by division by two, with integrality and
strictness checked. A one-edge ascent fixes its peak. A longer ascent
fixes all but prepeak t and peak S-t, leaving exactly

    y_(p-1) <= t <= min(floor((y_p+A_(p+1))/2), y_p-1).

Here the last y_p-1 subtracts the integer one, not a subscript. The
ascending target equality and weak-order tests are necessary, including
the r=2 boundary. The lower bound, weak peak inequality and strict outgoing
peak inequality are precisely all remaining constraints.

Distinct valley-to-valley blocks share only already forced valley values,
not free variables. Their independent intervals reconstruct every source
coordinate. Every local equation is satisfied and telescoping gives mass N
automatically; an extra global mass predicate is unnecessary. Unique words
and distinct prepeak values prevent overcounting. This verifies necessity,
sufficiency, empty intervals, divisibility rejection and cyclic wraparound.
The resulting sum has O(n 2^n) arithmetic work, not a bit-cost independent
of N or a polynomial-in-n claim.

For a nonuniform fixed target, every residual source run ends at an isolated
target spike and has length at most two, because at most its first positive
site can disappear per round. An optional head needs two preceding target
zeros; otherwise it would have a positive predecessor and survive.
Thus a spike of residual mass p with at least two preceding zeros contributes
floor(p/2)+1 possibilities, independently. Uniform targets have one source
by invariant minimum and mass. The fixed-target product follows.

For n>=3 and k=floor(n/3), each free interval consumes at least two ascent edges and
one following descent edge, so there are at most k factors. Each nonempty
factor has at most N+1 values, giving the stated uniform upper bound.
Place k positive spikes two zeros apart and distribute mass 2q to each,
where q=floor(N/(2k)), adding the remainder to one spike. At N>=2k the
fixed-target product gives at least (q+1)^k>=(N/(2k))^k. This proves the
Theta_n(N^k) exponent in all parameters, independently of finite checks.

## One independent finite check

[VERIFICATION_CONTRACT.md](VERIFICATION_CONTRACT.md) and [verify.py](verify.py)
were frozen before the sole reviewer scientific command. Source SHA256:
ca3338ba3f6507127690759fac7a89e862e98e87f11ea8d4326209b4a1225ce0.

The fixed box n=1,...,6, N=0,...,4 contains 461 states in 30 full carriers.
Stars-and-bars positions, the surplus update, Kahn graph peeling and
complementarity current enumeration are separately implemented. The chamber
formula is independently recoded, with no author-source import or replay.
All target source sets, not only counts, agree in all three representations.
Every temporal and fixed-product assertion passes, including 205 fixed
targets and the first degree-two n=6 family. Executed branch counters include
18 admitted words with at least two free intervals, plus short/long ascents,
dyadic parity rejection and empty intervals.

[VERIFICATION_NATIVE.json](VERIFICATION_NATIVE.json) retains the actual
exit-zero command return. [VERIFICATION_ACTUAL.txt](VERIFICATION_ACTUAL.txt)
is byte-equal to its 29,987-byte output; SHA256
6f4a542c63207896d01b41618f0e138beafa01e008bd433ebc86fc3489b3b567.
All 461 target certificates and 30 carrier summaries are retained.
No failure, automatic rerun, enlarged box or numerical asymptotic proof.

## Residual value, source boundary and finding

[SOURCE_CHECK.md](SOURCE_CHECK.md) identifies the actual primary reads and
historical subtraction. Conservation, zero barriers, flux feasibility,
ordered linear chambers, dyadic arithmetic and product counting themselves
receive no credit. What remains is this literal's full-carrier sharp clock
plus its exact independent-interval source atlas and matching degree
packing/witness. The inverse is not merely an unevaluated generic decoder,
a scalar time law recast as a census, a permutation-root formula, a retraction
or a changed-size version of the old merging scout. The result is a modest,
bounded short-note prospect; venue quality and global originality are not
certified by this candidate gate.

**F07-SOURCE-01 — MINOR, OPEN.** Author SOURCE_AND_COLLISION.md lines 57–58
calls P211 finite-field kernel/image projection feedback. The pinned P211
setup actually defines all nondecreasing selfmaps of the finite chain [n],
with endpoint/ceiling retractions. The literal distinction from fresh07
remains true, but the field label is false. Required repair: a new pinned
erratum identifying the exact old statement and replacing finite-field by
finite-chain order-preserving kernel/image projection feedback, with no
change to any old sealed file or mathematical/pilot dependency. Acceptance
is text-only and needs no scientific rerun.

Finding census: FATAL 0, MAJOR 0, MINOR 1 open. Exact repair is proportionate;
untested post-pilot deductions are not thereby false and do not justify KILL.
The root owns admission and any central lifecycle update. HOLD_EXTERNAL.
