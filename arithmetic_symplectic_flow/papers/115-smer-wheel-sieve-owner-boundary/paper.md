# Periodic SMER scheduling does not turn a finite wheel sieve into a recurrent prime action

**Paper ID:** `115-smer-wheel-sieve-owner-boundary`  
**Record ID:** `ASFS-SCOUT-20260914-82`  
**Date / status:** `2026-09-14; PRE-P0 STOP — PERIODIC SCHEDULER AND FINITE PRIME-SIEVE OUTPUT HAVE DISTINCT OWNERS`  
**Route state:** `No formal ASFS Route-A coordinate; Route B NOT INVOKED`

## 1. Frozen source construction

The screened source combines two finite objects. SMER evolves orientations of a finite multigraph: eligible nodes reverse prescribed numbers of arcs, and the finite orientation state has periodic behaviour. Separately, a wheel sieve is executed for a fixed bound \(n\), returning primes in \([2,n]\).

The procedure explicitly carries a first-\(k\)-prime set \(\mathcal P\), a next-prime variable, wheel residue intervals, and cutoff-dependent storage. Thus its exact object is a finite distributed computation with an internal scheduler, not one action that starts with no prime-side data and indefinitely generates a recurrent prime-symbolic state.

| Owner | Source supplies | Boundary |
| --- | --- | --- |
| SMER period | repeated multigraph orientations | scheduler state only |
| wheel selection | residues after initial wheel factors | supplied finite arithmetic configuration |
| prime output | sieve result in \([2,n]\) | finite computation output |
| prime packet/repetition | none for the all-prime action | absent |
| geometric/analytic owner | none | absent |

## 2. Same-object audit

A repeated SMER orientation says that the resource scheduler has returned to a previous finite orientation. It does not mean that the wheel has enlarged, that a new sieving prime has been internally selected, or that the output prime set has returned under an autonomous all-scale action. Conversely, the sieve side uses a fixed cutoff and initialized arithmetic data. Changing \(n\), the wheel, the initial prime set, or the multigraph makes a different finite instance before any orientation begins to cycle.

Therefore a SMER period cannot be relabelled as a primitive prime packet. A disjoint collection of finite instances would be a new carrier requiring its own action, recurrence, symbolic lineage, and geometry; it cannot inherit the individual scheduler cycles.

## 3. Gate assessment and decision

| Gate | Evidence for this exact screen | Status |
| --- | --- | --- |
| A0 | finite wheel/prime initialization and cutoff precede the scheduler | scoped FAIL |
| A1 | real finite SMER orientation periods, but no same-action all-prime packet | scoped owner FAIL |
| A2 | no roof, transfer operator, or determinant | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.** This is a positive control for the narrow statement that sieve-adjacent distributed scheduling can be periodic. It still fails the central ownership test. Future candidates must not use a finite scheduler's period to repair a separately initialized or bounded sieve, and must independently supply the prime-symbolic-to-Hénon/conservative lineage.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source record](evidence/README.md)
- [099 reversible-sieve computation boundary](../099-reversible-sieve-computation-boundary/paper.md)
- [017 finite-wheel Hénon control](../017-finite-wheel-henon-control/paper.md)
- [108 source-action frontier](../108-source-action-frontier-cycle-11/paper.md)
