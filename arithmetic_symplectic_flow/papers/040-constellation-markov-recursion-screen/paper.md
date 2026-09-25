# Exact constellation-population recursions remain stage-driven, not orbit-bearing

**Paper ID:** `040-constellation-markov-recursion-screen`  
**Record ID:** `ASFS-SCOUT-20260914-29`  
**Date / status:** `2026-09-14; PRE-P0 STOP — STAGE-DRIVEN POPULATION RECURSION, NOT A RECURRENT ORBIT CARRIER`  
**Route state:** `No classical candidate; Route A not evaluated; Route B NOT INVOKED`

## Abstract

Holt's primorial-wheel analysis supplies exact Markov-chain recursions for
populations of admissible gap constellations. This is closer to a
finite-dimensional state update than the full wheel word and is therefore a
distinct breadth candidate. The update nevertheless uses the next sieve stage:
`v_(k+1)=M(p_(k+1))v_k`. Keeping the stage produces a strictly increasing
coordinate; discarding it changes the update owner. Thus no single autonomous
map, positive roof, primitive closed-orbit convention, or same-object zeta is
defined. The screen stops before P0 while retaining the result as an A0
symbolic-statistical control.

## 1. Required lineage

```text
prime/composite sieve observable
  -> primorial gap-cycle admissibility (019)
  -> exact constellation populations across sieve stages
  -> Markov population recursion (this screen).
```

The cited construction follows the actual primorial recursion and studies a
fixed admissible constellation `s` via counts of its driving terms. For a
specified initial stage and permitted lengths, its population vector evolves
by a stage-dependent transition matrix. This is not a free choice of a Markov
matrix: the stage is part of the arithmetic construction.

## 2. Decisive recurrence audit

The faithful operational state is `(v,k)`, with

`(v,k) -> (M(p_(k+1))v,k+1)`.

The source's wheel recursion can internally identify the next sieve prime at a
finite stage, so this is an endogenous sieve relation in the limited A0 sense.
But the `k` coordinate is bounded below and increases at every full update.
If a state returned after `r>0` steps, its second coordinate would obey
`k=k+r`, a contradiction. Hence the faithful stage carrier has no periodic
point.

Omitting `k` does not repair this: it makes the next matrix ambiguous, because
the same population vector is not an instruction for which sieve prime should
act next. Treating a normalized limiting vector as a fixed point similarly
forgets the chronology and supplies neither an orbit length nor a repetition
law. This is exactly the distinction between a statistical recursion and a
closed-orbit dynamical object.

## 3. Same-object ledger

| Item | Owner | Status |
| --- | --- | --- |
| Arithmetic source | primorial sieve/constellation update | retained as source control |
| State transition | stage-indexed `M(p_(k+1))` | defined, nonautonomous |
| Symplectic `(M,omega)` and map `F` | none | absent |
| Roof and suspension | none | absent |
| Primitive orbit/repetition | stage state cannot return | scoped fail |
| Operator/zeta | no same-object flow | absent |

No Hénon map is post-selected to reproduce these vectors, because that would
make the arithmetic language external to the map (the failure already isolated
in 012 and 013). No finite-wheel packet or 032 zeta is transferred.

## 4. Controls and decision

| Control | Result |
| --- | --- |
| Retain stage `k` | strict advance; no closed state |
| Drop stage `k` | update law is not defined by the retained state |
| Normalize population vector | statistic may converge but gives no primitive orbit/roof |
| Add a cyclic local wheel coordinate | 020's event dichotomy still prohibits return across updates |

| Gate | Evidence | Status |
| --- | --- | --- |
| A0 | endogenous finite-stage symbolic recursion is a positive control | `NOT EVALUATED AS A CANDIDATE` |
| A1 | no recurrent same-object carrier | `scoped FAIL` |
| A2 | no roofed carrier, operator, or zeta | `NOT EVALUATED` |
| Route B | no Route-A candidate | `NOT INVOKED` |

**Portfolio position: stop/fork.** Stop the population-recursion carrier.
Future work may use its exact constellation statistic only if a new frozen
object supplies an autonomous conservative map that derives the same update
law and characterizes its full primitive-orbit ledger; otherwise it remains a
lineage-positive but non-orbit-bearing control.
