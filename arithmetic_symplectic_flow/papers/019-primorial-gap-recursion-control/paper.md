# Exact primorial gap recursion is an A0 source, not yet an arithmetic symplectic flow

**Paper ID:** `019-primorial-gap-recursion-control`  
**Record ID:** `ASFS-SCOUT-20260913-16`  
**Date / status:** `2026-09-13; A0 SYMBOLIC POSITIVE CONTROL / PRE-P0 SCREEN`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Source mechanism and lineage

The source studies Eratosthenes sieve through the cycle of gaps
`G(p_k#)` among `p_k`-rough numbers and gives a three-step recursion

```text
G(p_k#) -> G(p_(k+1)#).
```

Its first step is intrinsically arithmetic: if `g_1` is the first gap of the
current cycle, then `p_(k+1)=g_1+1`. The next sieve prime is therefore read
from the current symbolic state rather than supplied as a separate table. This
retains the required direct lineage:

```text
prime sieve -> symbolic gap cycles / admissible constellations -> sequential recursion.
```

Unlike 010's smooth density envelope, the arithmetic content is present in the
combinatorial sieve operation itself. It is therefore retained as an A0
*positive control*, not dismissed as generic chaos.

## Why P0 is not admitted

The source recursion changes the primorial stage even though it derives the
next prime internally. It is not a single-valued autonomous map on one fixed
smooth phase space. A faithful state which records `k`, `p_k`, or `p_k#` has a
strictly increasing frontier, so by
[018](../018-monotone-sieve-clock-obstruction/paper.md) it cannot own a periodic
orbit on that carrier. Each finite gap cycle is periodic as a combinatorial
wheel, but promoting it to a flow orbit requires selecting a finite stage and
supplying its factorization; record 017 shows why that repair fails A0.

No phase space `(M,omega)`, symplectic base map `F`, roof, mapping torus,
primitive-orbit/repetition convention, or zeta owner is supplied by this source.
Combining those missing objects from other records would violate the one-object
invariant.

## Decision

This control improves the admission frontier: future candidates should retain
the exact gap-cycle recursion, rather than a density surrogate, while replacing
the monotone stage state with a proven recurrent global arithmetic mechanism.
Until that replacement is constructed in one object, stop before P0.

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source/provenance](evidence/README.md)
- [Monotone-clock theorem](../018-monotone-sieve-clock-obstruction/paper.md)
