# Localization units produce exact clocks but not a full primitive-circle ledger

**Paper ID:** 146-localization-scaling-groupoid  
**Candidate ID:** ANG-20260915-LSG01  
**Date:** 2026-09-15  
**Status:** STOP — EXACT LOCALIZATION CLOCKS; FULL PRIMITIVE-PACKET PRODUCT UNSUPPORTED.  
**Route state:** Broadened owner T0--T3 only; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

We audit the frozen groupoid of all actual localizations Z[1/n], n>=2,
with positive multiplication-unit arrows acting by their logarithms on
real coordinate lines. Translation in that same coordinate is the time
action. The denominator language is an explicit power-saturation of local
divisibility symbols, so the arithmetic-to-carrier relation is stated
without importing a prime-indexed flow. Equality of actual localizations
eliminates prime-power label duplicates. The full time-return subgroup
is the integer span of the logarithms of the primes inverted by the
localization. Rank-one components therefore yield one circle of length
log p per prime. Every higher-rank component instead has a dense, proper
return subgroup and no least positive return. Moreover, infinitely many
distinct such components return at any fixed time log p. These exact
full-ledger facts stop the proposed ordinary primitive-packet product.
They do not rule out every groupoid trace or regularization. In particular,
discarding the higher-rank components would be a change of analytic owner,
not an unrecorded simplification of this candidate.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) was frozen before this audit.
For n>=2, set

\[
A_n=\mathbb Z[1/n]\subset\mathbb Q,\qquad
E_n=\{d\ge1:\ d\mid n^j\text{ for some }j\ge0\}.
\tag{1}
\]

Let A range over the distinct actual subrings A_n, not over chosen integer
representatives. Write

\[
U_A=\{q\in\mathbb Q_{>0}:qA=A\}.
\tag{2}
\]

Objects are (A,u), u in R. An arrow (A,u,q) has source (A,u) and
target (A,u+log q), with q in U_A. Subring and unit indices have discrete
topology. The action phi^t sends every u to u+t, on both objects and arrows.

| Item | This candidate's owner | Evidence / boundary |
| --- | --- | --- |
| Carrier | Disjoint union of U_A acting by log translations on R | Countable étale groupoid; generally nonproper |
| Arithmetic input | All integers, divisibility and actual localization equality | No selected prime domain |
| Source relation | Local divisibility symbols to E_n to localization units | Exact replacement; no chronological sieve conjugacy |
| Time | Translation u to u+t | No roof and no manually prescribed prime periods |
| Returns | All times closing up to an arrow in every A component | Complete classification below |
| Primitive convention | Least positive return where one exists | Absent on every higher-rank component |
| Analytic proposal | Full ordinary primitive-packet product | Not justified by the complete ledger |
| Trace, operator, space and measure | OPEN | No implicit packet weighting or regularization |
| Symplectic map and mapping torus | NOT APPLICABLE | Broadened ANG carrier only |
| Future Hamiltonian/contact/quantum owner | DEFERRED | No later-route inference |

The groupoid's point isotropy and the time-action stabilizer up to arrows
are different notions; Proposition 2 makes that distinction explicit.

## 2. Question and claim boundary

Can power-saturated divisor admissibility produce an owned exact
logarithmic return clock without importing the prime circles of an
external arithmetic flow? Yes, on the rank-one part of this full
construction. Does that give a complete ordinary primitive-circle ledger
for the frozen carrier? No: all higher-rank components remain and have
non-discrete return subgroups.

The strongest result is the full exact classification of localization
classes and time returns, together with a scoped obstruction to the
precommitted ordinary full-ledger product. We do not claim a Hausdorff
flow realizing every return subgroup, an Euler product for the full
groupoid, a trace formula, a determinant, or a formal Route result.

## 3. Source lineage, definitions and provenance

The source arrow is

\[
\text{local divisor symbol }1_{\{d\mid n\}}
\ \longrightarrow\
1_{\{d\mid n^j\text{ for some }j\}}
\ \longrightarrow\ A_n\ \longrightarrow\ U_{A_n}.
\tag{3}
\]

This is a precise change from proper-divisor exclusion to multiplicative
denominator admissibility in the [prior-work lineage](../../docs/prior_work/README.md).
It does not preserve the distinction between a prime and its powers:
that loss is intentional and recorded. It also does not preserve the
one-way causal sieve trajectory or supply a conjugacy from that trajectory.
The next section proves exactly what mechanism survives the replacement.

All n enter (1) before a return or rank test. The use of prime supports
below is a proof classification by unique factorization, not input
selection. Logarithms enter as the additive coordinate of the actual
multiplication-unit action, with the same fixed normalization for every
positive rational q. No prime times, prime table, fitted weights,
Riemann-zero data or per-prime choices are used.

The comparison with [029](../029-primorial-index-cocycle-screen/paper.md)
is specific: the present logarithm is tested on actual time-return arrows,
not on nonreturning sieve-stage arrows. Unlike
[024](../024-primorial-scaling-site-bridge/paper.md), no primorial path or
claim about its canonical landing is imported. The packets and clocks of
[022](../022-deninger-alf-specz/paper.md) supply no theorem for this object.

## 4. Exact derivation

### Proposition 1 — Denominator language, units and duplicate labels

Let S(n) be the finite nonempty set of primes dividing n. Then

\[
E_n=\{d\ge1:\text{every prime divisor of }d\text{ belongs to }S(n)\},
\]
\[
A_n=\{a/d:a\in\mathbb Z,\ d\in E_n\},\qquad
U_{A_n}=\left\{\prod_{p\in S(n)}p^{e_p}:e_p\in\mathbb Z\right\}.
\tag{4}
\]

Furthermore, A_n=A_m if and only if S(n)=S(m).

**Proof.** If d divides n^j, every prime dividing d divides n. Conversely,
when the prime divisors of d all divide n, choosing j large enough makes
each exponent in n^j at least the corresponding exponent of d. This
proves the E_n statement and its equality with the denominators permitted
by localization.

A positive rational q satisfies qA=A exactly when q and q^{-1} both
belong to A: necessity follows by applying qA=A and its inverse to 1;
sufficiency follows because A is a ring. In reduced numerator-denominator
form, both membership conditions require all prime factors of numerator
and denominator to belong to S(n). This proves the unit formula.

Finally, 1/p belongs to A_n precisely when p belongs to S(n). Thus
equality of actual localizations forces equality of supports, and the
converse follows from the denominator description. QED.

Consequently n=p,p^2,p^3,... define one actual component, not infinitely
many duplicate circles. The same quotient identifies 6,12,18,... exactly
when their prime supports agree; it does not collapse different supports.

### Proposition 2 — Groupoid ownership and time-return classification

The frozen arrows form an étale topological groupoid. Its isotropy at
every object (A,u) is trivial. Its time-action stabilizer up to arrows is

\[
\Lambda_A
=\{t:\text{there is an arrow }(A,u)\longrightarrow(A,u+t)\}
=\log U_A
=\sum_{p\in S(A)}\mathbb Z\log p.
\tag{5}
\]

This does not depend on u. The coarse component is R/Lambda_A.

**Proof.** Composition and inverse are
(u,q) followed by (u+log q,r) maps to (u,qr), and
(u,q)^{-1}=(u+log q,q^{-1}). The identity has q=1.
On each fixed (A,q) arrow line, source and target are homeomorphisms
onto the object line. Thus source and target are local homeomorphisms.
Continuity of all structure maps follows componentwise. The indices
are countable, and each line has its usual topology.

An arrow has equal source and target exactly when log q=0, hence q=1;
ordinary point isotropy is therefore trivial. Translation by t commutes
with every arrow, so it induces a time action. Closing that time action
up to an arrow means t=log q for a unit q, proving (5) from (4).
Taking all arrow equivalence classes gives R/Lambda_A. QED.

The language “isotropy produces the clock” is permissible only if it
explicitly means the stabilizer of this residual time action, or time
closure up to groupoid arrows. It is false for the ordinary point
isotropy of the displayed étale groupoid.

### Proposition 3 — Circles and dense nonprimitive return components

If S(A)={p}, its coarse component is one oriented circle orbit with least
positive period log p and repetitions r log p, r>=1. If |S(A)|>=2,
Lambda_A is a proper dense subgroup of R and has no least positive
element. The latter coarse component is not T1.

**Proof.** In the rank-one case, (5) is (log p)Z, so the quotient and
repetition statements follow directly from real translation modulo that
discrete lattice. All u in that component belong to the same time orbit;
they are not separately counted primitive circles.

For different primes p and q, log p/log q is irrational. A rational
equality would imply p^a=q^b for positive integers a,b, contrary to unique
factorization. Pigeonholing the fractional parts of
0,alpha,...,N alpha for alpha=log p/log q gives a nonzero integer
combination of log p and log q with absolute value at most log q/N.
Changing its sign if necessary gives arbitrarily small positive elements
of Lambda_A. Integer multiples of a positive element smaller than the
length of a given open interval meet that interval. Hence Lambda_A is
dense. It is countable and therefore is not all of R.

No least positive element can exist. In the quotient topology, the
inverse image of a singleton is a coset of this nonclosed subgroup.
That singleton is not closed, proving failure of T1. QED.

At higher rank every positive return T decomposes as
T=t+(T-t) with both summands positive returns, by taking 0<t<T from the
dense subgroup. There is no primitive positive time from which all
returns are integer repetitions. Every individual return can still be
repeated r times, producing rT; those valid repetitions do not manufacture
a primitive generator.

A continuous R action on a T1 space has closed stabilizers, since the
stabilizer is the inverse image of a closed singleton under an orbit map.
Thus these exact dense proper time stabilizers cannot be retained in a
T1, in particular Hausdorff, ordinary-flow realization. This is not an
obstruction to the nonproper groupoid frozen here.

Nonproperness is also explicit. In a higher-rank component choose
distinct nonzero lambda_j in Lambda_A tending to zero. The source-target
pairs (0,lambda_j), together with (0,0), form a compact subset of R^2.
Its arrow preimage contains arrows with the infinitely many distinct
discrete labels exp(lambda_j), so that preimage is not compact. Hence
the source-target map is not proper.

### Proposition 4 — Infinite distinct return components at one fixed time

For every prime p, time T=log p is a return in infinitely many distinct
localization components, including infinitely many higher-rank ones.

**Proof.** There are infinitely many primes: if a finite list contained
all of them, a prime divisor of their product plus one would be missing.
For each prime q different from p, consider the already present
localization A_{pq}. These are pairwise distinct by Proposition 1.
Multiplication by p is a unit in every A_{pq}, so Proposition 2 gives
the time-log p return in every such component. QED.

This counts distinct components after exact localization equality, not
integer labels and not the continuum of u representatives within one
coarse orbit. Thus neither eliminating prime-power duplicates nor
quotienting circle basepoints removes this infinite return-component
multiplicity.

## 5. Results and the ordinary-product boundary

The exact full return classification is now available. Its rank-one
circle sector alone has one primitive orbit per prime with length log p.
But the frozen card explicitly retained every localization and every
time-return arrow. Higher-rank components have no least positive period
and are not repetitions of these distinct rank-one components.

Consequently the usual recipe “one factor for each primitive circle and
all other returns are its repetitions” does not describe the complete
frozen return ledger. A product restricted to rank-one circles would be
an explicitly sector-restricted object. We do not identify it with the
full candidate's zeta, determinant or trace.

Likewise, an unweighted count assigning one unit to each distinct
time-return component already has infinite count at T=log p. A groupoid
trace, cohomological index, cancellation or regularization could obey
other rules, but no such owner, domain, measure or normalization was
frozen or constructed here. Proposition 4 is not a theorem that every
possible trace fails. The bounded audit stops without pursuing such
alternative analytic definitions.

## 6. Controls and adverse findings

| Control | Exact finding | Meaning |
| --- | --- | --- |
| No localization, A=Z, external comparator | Positive unit group is {1}; no nonzero time return | Log clocks depend on actual allowed denominators |
| Repeated labels p,p^2,p^3 | One actual localization and one rank-one circle | Duplicate labels cannot create packet multiplicity |
| Mixed labels pq, p^2q | Same higher-rank localization | “Composite” is not equivalent to higher rank; prime powers stay rank one |
| Different mixed supports pq,pr | Distinct components, both returning at log p | Full multiplicity survives the natural quotient |
| Rank-one-sector selection | Would discard frozen higher-rank return components | Not a full-ledger simplification or trace proof |
| Hausdorff carrier replacement | Cannot retain dense proper time stabilizers | Would change the geometric/category owner |
| Arbitrary selected denominator families | Can generate selected clock subgroups | PROVES_TOO_MUCH risk: all-integer provenance matters, not a universal naturalness claim |

There is no numerical cutoff or precision claim. Every result concerns
all frozen localizations and all real times through the proofs above.
No empirical randomization, label fitting or target-zero comparison is
needed for these exact distinguishing controls.

## 7. Gate assessment

| Gate | Evidence | Status | Boundary |
| --- | --- | --- | --- |
| T0 | Proposition 2 constructs the exact étale groupoid and action | ESTABLISHED | Nonproper; no classical map or Hausdorff coarse flow claimed |
| T1 | Propositions 1--3 derive units and exact time logarithms from E_n | ESTABLISHED WITH SCOPE | Replaces divisor exclusion by power-saturation; not chronological sieve conjugacy |
| T2 full returns | Propositions 2--4 classify every return subgroup and retain duplicates correctly | ESTABLISHED CLASSIFICATION | Higher-rank components have no primitive positive period |
| T2 ordinary primitive convention | Full returns cannot be organized as primitive-circle repetitions | SCOPED FAIL | Rank-one sector is not the full frozen ledger |
| T3 | No full ordinary product, operator or trace owner supplied | NOT ADVANCED | Infinite unit-count return multiplicity; other traces OPEN |
| Classical A0--A2 | Carrier fields NOT APPLICABLE | NOT EVALUATED | No rebranding of T coordinates |
| Formal Route / B | No evaluation performed | UNASSIGNED / NOT INVOKED | No inherited credit |

## 8. Conclusion and decision

**Portfolio decision: stop/fork.** ANG-20260915-LSG01 gives a genuine
same-object arithmetic logarithm and a complete return classification.
The decisive stop is that the full object has dense higher-rank return
subgroups without primitive positive periods, together with infinitely
many return components at a single prime-log time. Restricting its
circle sector or constructing a weighted analytic quotient would require
an explicit new owner and its own audit, not accumulated credit here.

The same-object ledger remained intact: every localization, unit,
coordinate, time and return used above belongs to the frozen groupoid.
No later branch is created by this paper.

## Reproducibility / evidence index

- [Frozen card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence index](evidence/README.md)
- [Independent derivation and bounded model review](evidence/review.md)

This is a Markdown research note with self-contained exact proofs.
No numerical experiment, external dataset or source-dependent theorem
is asserted. AI agents constructed and reviewed the argument; model
review is not human peer review. The ARS argument discipline was used
to separate proved ownership, negative controls and unresolved analytics,
not to claim publication readiness or a formal research evaluation.
