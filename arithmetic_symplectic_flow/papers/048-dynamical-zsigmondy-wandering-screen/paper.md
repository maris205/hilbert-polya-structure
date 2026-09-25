# Dynamical Zsigmondy prime production is a wandering-orbit, not an A1, mechanism

**Paper ID:** `048-dynamical-zsigmondy-wandering-screen`  
**Record ID:** `ASFS-SCOUT-20260914-36`  
**Date / status:** `2026-09-14; EXTERNAL CONTROL — PRIMITIVE PRIME DIVISORS ON A WANDERING ORBIT; A1 SCOPED FAIL`  
**Route state:** `No classical candidate; Route A not evaluated; Route B NOT INVOKED`

## Abstract

The dynamical Zsigmondy theorem gives a rigorous instance in which a single
rational self-map produces new prime divisors internally along iteration. Its
essential hypothesis, however, is that the chosen point is wandering. Hence
the exact same orbit carrying the prime-divisor events cannot be a periodic
orbit, and it supplies neither primitive closed orbits nor their repetitions.
This is retained as an external negative control: it makes the arithmetic
versus recurrence conflict precise without pretending to be a prime-symbolic
or symplectic candidate.

## 1. Object and ownership ledger

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Carrier | `P^1(Q)` with one rational map `phi` and point `alpha` | source-screen only |
| Map | degree `d>=2`, `phi(0)=0`, not of polynomial type at `0` | cited theorem hypotheses |
| Arithmetic source | reduced numerators `A_n` of `phi^n(alpha)` | same object |
| Prime event | a prime divisor of `A_n` absent from every earlier `A_i` | same object |
| Orbit convention | `alpha` has infinite forward orbit | same object; nonperiodic |
| Symplectic map / roof / suspension | none | absent |
| Coding / zeta / determinant / operator | none | absent |

The source itself is an arithmetic-dynamics theorem, not an arithmetic
suspension. No geometric carrier is imported to manufacture recurrence.

## 2. Question and claim boundary

**Question.** Can internally generated primitive prime divisors along a single
iteration furnish the prime side of an A1 primitive closed-orbit ledger?

**Strongest supported claim.** No, for the theorem's selected orbit: its
wandering hypothesis is logically incompatible with periodic closure. The
accumulating set of primes first seen by time `n` also records irreversible
history along that orbit.

**Nonclaims.** This does not rule out periodic points elsewhere in a given
rational map, does not rule out another arithmetic recurrence construction,
and makes no Route-A, Route-B, trace, zeta, Hamiltonian, or Riemann-zero claim.

## 3. Input and method

Use Ingram--Silverman's Theorem 1: if `phi` and `alpha` satisfy the ledger
hypotheses, then the Zsigmondy set of the numerator sequence is finite, or
equivalently all sufficiently large `A_n` have a primitive prime divisor.
The only deduction made here is structural. A periodic orbit has finite
forward orbit, whereas this `alpha` has infinite forward orbit by hypothesis.
Moreover a prime first observed at step `n` stays in the historical set of
observed prime events, so that augmented event-history carrier is strictly
forward-growing at every sufficiently large event.

## 4. Results and controls

This produces a useful A0-style arithmetic control in the weak sense that the
prime divisors arise from a single iterated map rather than an inserted prime
list. It fails the required lineage before P0: it begins with a generic
rational arithmetic map, skipping the prior-work symbolic admissibility and
the documented sequential/Logistic/Hénon deformation arrows. Independently,
the orbit selected by the theorem fails A1 because it is wandering. Adding a
natural extension, a compactification, or a symplectic lift would be a new
object and could not inherit the theorem's orbit credit.

This is deliberately distinguished from 047: the SOPFR map had a complete
fixed-point ledger but no nontrivial repetitions; the present mechanism has
infinitely many newly appearing primes but no periodic carrier. Together they
show two separate partial successes, neither a main-candidate admission.

## 5. Gate assessment

| Gate | Evidence for this exact screen | Status | Limitation |
| --- | --- | --- | --- |
| A0 | arithmetic iteration and prime-divisor event are same-object | external positive control only | no prior-work lineage, no frozen ASFS tuple |
| A1 | selected `alpha` is wandering | scoped FAIL | no closed orbit or repetitions on the event-carrying orbit |
| A2 | no zeta/determinant/transfer owner | `NOT EVALUATED` | absent |
| Route B | no formal Route-A readiness | `NOT INVOKED` | prohibited by scope |

## 6. Decision

**Stop this screen; fork.** Future breadth search must require recurrence and
an endogenous prime-symbolic admissibility mechanism *before* a conservative
or symplectic realization is tested. Do not repair this control by recording
the prime-event history as an auxiliary clock: that only makes its one-way
character explicit.

## Reproducibility / evidence index

The exact theorem statement and assumptions are linked in
[evidence](evidence/README.md). This is a source-theorem audit with no local
computation or generated numerical output.

