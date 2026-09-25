# A fixed-rule sieve cellular automaton is endogenous but its prime trajectory cannot close

**Paper ID:** `053-realtime-sieve-ca-nonrecurrence`  
**Record ID:** `ASFS-SCOUT-20260914-39`  
**Date / status:** `2026-09-14; A0 SYMBOLIC POSITIVE CONTROL; PRE-P0 STOP — DESIGNATED SIEVE TRAJECTORY IS NONRECURRENT`  
**Route state:** No classical P0 candidate; no formal Route-A coordinate is
evaluated; Route B `NOT INVOKED`.

## 1. Question and lineage

The open branch after one-sided causal rigidity (051) is whether a fixed local
rule can generate prime/composite data without importing a prime directive
sequence. The cited one-dimensional cellular automaton implements the
Eratosthenes sieve with a finite rule table and one standard initial condition:

```text
prime/composite observable -> sieve crossing-out rule -> local symbolic CA update
-> [no supplied Logistic/Henon/conservative lift].
```

This realizes the first two required lineage arrows, but not the
sequential-to-Henon or higher-dimensional symplectic arrows. The narrow
question is whether the trajectory that carries the prime observable can be a
closed-orbit source.

## 2. Frozen source object and ownership

Let `A` denote the reported synchronous CA on the positive-integer half-line.
It has a finite state set, a uniform nearest-neighbour local update, a fixed
left boundary, and initial configuration `x_0` with the boundary cell in its
designated initiating state and every other cell quiescent. Put `x_t=A^t(x_0)`.

The source defines real-time generation so that boundary cell `C1` is in output
state `1` at time `t` exactly when `t` is prime. Write the observation as

`b(x_t)=1_{t is prime}`.

The eight-state implementation uses waves and partitions to perform the
crossing-out procedure; its finite rule table is part of the source object.
Prime information is not a list of prime-indexed operators or an externally
selected subshift. Conversely, `A` is a forward computational update. No
inverse, symplectic form, smooth finite-dimensional phase space, roof,
suspension, transfer operator, or zeta is owned by this object.

## 3. Exact nonrecurrence of the designated arithmetic trajectory

**Lemma.** The prime indicator `u(t)=1_{t is prime}` on positive integers is
not periodic.

**Proof.** Suppose it had positive period `q`. Choose a prime `p>q`.
Periodicity gives `u(p+pq)=u(p)=1`. But `p+pq=p(1+q)` is composite, a
contradiction. ∎

**Proposition.** The designated CA trajectory `(x_t)_{t>=0}` is not periodic.

**Proof.** If `x_{t+q}=x_t` for all `t` and some `q>0`, applying fixed
observation `b` makes `b(x_t)` period-`q`. Section 2 identifies it with the
prime indicator, contradicting the lemma. ∎

This is only a statement about the same trajectory carrying prime output. A CA
may possess unrelated periodic configurations; neither source nor screen
classifies them. They cannot replace `x_t` without breaking same-object
arithmetic ownership.

## 4. Gate audit and controls

| Gate / obligation | Finding | Status |
| --- | --- | --- |
| Prime-symbolic provenance | fixed local sieve rule and fixed seed, no supplied prime list | endogenous symbolic positive control |
| A0 as classical ASFS gate | no finite-dimensional symplectic base map | not admitted / no P0 |
| A1 for arithmetic trajectory | exact nonperiodicity above | scoped FAIL |
| Complete global CA periodic ledger | not supplied or derived | `OPEN`; not needed for scoped stop |
| Roof, primitive convention, repetitions | absent | `NOT EVALUATED` |
| A2 / determinant / operator | absent | `NOT EVALUATED` |
| Route B | no Route-A-ready same object | `NOT INVOKED` |

Controls: unlike 030 and 041, the rule does not take primes as a language or
operator index. Unlike 011, no history-register enlargement is asserted.
Reversibilizing this CA would create a new object requiring independent A0,
A1, and full-periodic-ledger audits.

## 5. Decision

**Portfolio position: stop/fork.** Algorithmic sieve endogeneity is achievable
with a finite uniform symbolic rule, but its prime-carrying history is a
one-way nonrecurrent computation. The next admissible architecture must retain
that intrinsic-rule advantage while independently providing a reversible or
otherwise recurrent same-object carrier. It may not obtain recurrence by
post-selecting unrelated CA cycles, adding a generic reversible simulator, or
borrowing the periodic ledger of 052.

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source and method boundary](evidence/README.md)
- [Prior-work lineage index](../../docs/prior_work/README.md)
