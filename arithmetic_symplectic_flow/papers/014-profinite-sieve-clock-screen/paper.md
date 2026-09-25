# A profinite sieve clock preserves stage information but cannot provide closed orbits

**Paper ID:** `014-profinite-sieve-clock-screen`  
**Record ID:** `ASFS-SCOUT-20260913-12`  
**Date / status:** `2026-09-13; PRE-P0 NEGATIVE SCREEN`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Abstract

The sequential route in the prior work requires a stage variable.  Record 010
made that evolution autonomous by a real translating clock and immediately lost
periodic points.  This screen tests the natural compact arithmetic replacement:
the profinite stage clock with translation by one.  It avoids a manually chosen
finite cycle, and hence preserves the full sieve-stage lineage, but it has the
same no-return obstruction.  For every positive iterate, translation by that
iterate is not the identity on the profinite integers.  A skew product over it
therefore has no periodic point, and the clock is not a finite-dimensional
smooth symplectic phase-space factor.  No candidate is frozen.

## 1. Retained lineage and proposed construction

```text
recursive Eratosthenes sieve stages
  -> sequential/nonautonomous Logistic-Hénon parameter evolution
  -> autonomous skew-product clock
  -> attempted conservative/symplectic realization.
```

Let `K = lim <- Z/mZ` and consider the clock `C(k)=k+1`.  A fibre update
could formally take the form `(k,z) -> (C(k), H_k(z))`, where `H_k` is the
stage-dependent Hénon-type update.  This is an architectural test only: no
smooth `M`, symplectic form, map `F`, roof, or orbit convention is assigned.

## 2. No-return calculation

Suppose `C^n(k)=k` for some positive integer `n`.  Then `k+n=k` in `K`.
Projecting to `Z/(n+1)Z` gives `n=0 mod (n+1)`, a contradiction.  Thus `C`
has no periodic point.  Any periodic point of a skew product over `C` would
project to one of `C`, so no fibre dynamics can change this conclusion.

This is the same A1 obstruction that appeared for the real translating clock
in record 010, now shown to survive the natural inverse-limit compactification.
It is not a numerical observation and does not depend on a Hénon parameter.

## 3. Why finite cyclic repair is not admitted

Replacing `K` by `Z/NZ` creates periodic clock cycles, but `N` is then a chosen
terminal sieve stage or period.  It cannot encode the full evolving sieve
without an external truncation rule, and the resulting prime labels/periods
are selection data rather than an endogenous infinite mechanism.  It is a new
object, not a repair of this screen or record 010.

## 4. Gate assessment and decision

| Gate | Evidence | Status | Limitation / decision |
| --- | --- | --- | --- |
| P0 | clock is profinite/non-smooth and has no return | not admitted | stop before a symplectic lift |
| A0 | sieve-stage provenance is retained only architecturally | NOT EVALUATED | no frozen single object |
| A1 | no periodic base point for the proposed skew-product clock | scoped FAIL | do not seek fibre orbit computations |
| A2 | no same-object orbit ledger | NOT EVALUATED | unassigned |
| Route B | no Route-A-ready candidate | NOT INVOKED | prohibited |

A future fork must replace monotone stage progression by a genuinely recurrent
internal arithmetic state while proving that the recurrence is not a finite
external wheel.  It gets a fresh P0 card.

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Phase-I prior-work index](../../docs/prior_work/README.md)
