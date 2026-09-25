# `Spec Z` as an arithmetic laminated-flow external control: endogenous prime packets without a classical suspension

**Paper ID:** `022-deninger-alf-specz`  
**Candidate ID:** `ALF-20260913-DEN01`  
**Date / status:** `2026-09-13; BROADENED-CARRIER EXTERNAL CONTROL`  
**Audit state:** `T0 ESTABLISHED; T1 ESTABLISHED; T2 PACKET/REPETITION ESTABLISHED, TRACE WEIGHT OPEN; T3 OPEN; ASFS Route A/B NOT APPLICABLE / NOT INVOKED`

## Abstract

Under the authorized laminated/noncommutative/groupoid expansion, this paper
freezes Deninger's constructed arithmetic flow for `Spec Z` as a high-value
external control. The object is an infinite-dimensional, generalized foliated
flow rather than a symplectic map suspension. Its closed-point packet theorem gives an endogenous relation
`(p) -> Gamma_(p)` with every circle in the packet of length `log p`. This
closes the broadened track's T0, T1, and packet/repetition part of T2 audits.
The trace-weight part of T2 remains deliberately open: the prime owner is a
compact packet, not canonically one isolated primitive orbit, and the
appropriate packet index is unresolved in the source. The prior-work
sieve-symbolic lineage has a common prime source but no dynamical coding into
this carrier; it is therefore not promoted to either the main classical ASFS
line or the broadened main line.

## 1. Frozen same-object ledger

Take `X_0=Spec Z`, `K=Qbar`, and `G=Gal(Qbar/Q)`. Deninger's rational-Witt
construction first supplies an unrestricted quotient, but the source says it
has too many periodic orbits. Freeze instead its source-defined admissible
locus, denoted here by

```text
X_Den = X_(0,E_in) subset check(X_0)(C) x_(Q_{>0}) R_{>0},
```

The continuous action is

```text
phi^t([P,u]) = [P,u exp(t)].
```

where `E_in` requires the character on a residue field to be injective on its
roots of unity. These definitions, the arithmetic scheme, and the action
belong to the same source construction. The source describes `X_Den` as
infinite dimensional and equipped with a generalized codimension-one
foliation. Thus it is not silently called a smooth symplectic manifold, and
there is no `F`, roof, or mapping torus in this candidate.

## 2. T1: endogenous prime clock

The closed points of `Spec Z` are `(p)` for rational primes. Deninger's packet
theorem identifies the complete periodic set as a pairwise-disjoint union of
compact packets `Gamma_x0`, one for each closed point, whose periodic circles
have length `log N(x_0)`. Hence

```text
(p)  ->  Gamma_(p),       length(Gamma_(p) circle) = log p.
```

This is an internal source mechanism: no list of prime times, von Mangoldt
weight, or prime-dependent roof was inserted into the action. Each periodic
orbit lies in one uniquely determined packet.

## 3. T2: packet convention and exact limitation

For `(p)`, every orbit in `Gamma_(p)` is a circle
`R_{>0}/p^Z`. A traversal repeated `r` times has time `r log p`. This provides
a precise local repetition convention, and the packet classification plus
repetition part of T2 is established. It does **not** turn the entire packet
into a single isolated primitive orbit: the packet is fibred over a compact
group, and the source explicitly raises the problem of a Fuller-type index for
these packets. No packet weight, Euler factor, or determinant is inferred.

## 4. Relation to the prior-work symbolic lineage

The exact sieve/primorial recursion recorded in 019 generates the same rational
primes that index the closed points `(p)`. This is a source-level reconciliation
only. No semiconjugacy, Markov coding, return map, or deformation from the
sieve word into `X_Den` is currently defined. Accordingly:

```text
prime sieve / symbolic recursion -> rational prime labels -> closed points (p)
                                                   -> Deninger packets
```

is a documented arithmetic identification, while the requested *dynamical*
lineage arrow is `OPEN`. This card is therefore an `EXTERNAL CONTROL`, not an
admitted broadened main candidate, and receives no classical-ASFS admission or
Route credit.

## 5. T3 and next decision

The construction's packeted periodic data make a naive Ruelle product
ill-defined without a specified packet index/weight. The source leaves this as
a question, together with cohomological issues. Therefore T3 is `OPEN`.

**Decision:** `advance within the broadened ALF track to a packet-index/trace
audit; stop before any classical symplectic or Route language.` A later bridge
to the main lineage requires an actual coding/deformation theorem, not merely
the shared set of rational primes.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and source lock](evidence/README.md)
- [Exact sieve source control](../019-primorial-gap-recursion-control/paper.md)
