# Rowland's prime-producing gcd recurrence is endogenous but cannot return on its faithful state

**Paper ID:** 090-rowland-gcd-recurrence-nonreturn  
**Record ID:** ASFS-SCOUT-20260914-61  
**Date / status:** 2026-09-14; A0 CONTROL / NEGATIVE A1 SCREEN  
**Route state:** No formal ASFS Route-A coordinate; Route B NOT INVOKED.

## Frozen recurrence

Start with (a(1)=7) and define

\[
a(n)=a(n-1)+\gcd(n,a(n-1)),\qquad n\ge2.
\]

The faithful autonomous realization is

\[
T(n,a)=(n+1,a+\gcd(n+1,a)).
\]

Rowland proves that (a(n)-a(n-1)) is always either (1) or prime. The
prime production is therefore a property of one fixed gcd rule, not an
externally supplied prime schedule.

| Item | Owner | Status |
| --- | --- | --- |
| Arithmetic mechanism | gcd in (T) | internal |
| Symbolic lineage | arithmetic observable -> fixed recurrence | direct control |
| Full state/action | (S,T), including (n) | frozen |
| Closed orbits | none on (S) | exact |
| Geometry/roof/operator | none | NOT SUPPLIED |

## Nonreturn proof

For every (k>0), the first coordinate of (T^k(n,a)) is (n+k). Hence

\[
T^k(n,a)\ne(n,a).
\]

The complete arithmetic-generating state has no periodic point. Reducing,
erasing, or resetting the index produces a new object and cannot inherit the
original prime-increment theorem as an orbit ledger.

## Gate assessment and decision

| Gate | Evidence | Status |
| --- | --- | --- |
| A0 | fixed internal gcd rule produces increments (1) or prime | arithmetic positive control |
| A1 | exact increasing index excludes all positive-period states | scoped FAIL |
| A2 | no orbit ledger, roof, or analytic owner | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop/fork.** Endogenous prime production alone does not
supply recurrent arithmetic. Future search must avoid an unbounded progress
coordinate or prove an ownership-preserving return mechanism for it.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Rowland source record](evidence/README.md)
- [054 prime-time nonrecurrence boundary](../054-prime-time-observation-nonrecurrence/paper.md)
