# Local wheel cycles and global sieve recursion cannot belong to one closed orbit

**Paper ID:** `020-wheel-event-dichotomy`  
**Record ID:** `ASFS-SCOUT-20260913-17`  
**Date / status:** `2026-09-13; METHODOLOGICAL THEOREM / PRE-P0 STOP RULE`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Architecture

Let a state have a stage label `L` and a local cyclic wheel coordinate. An event
set `E` marks the local boundary at which the exact gap-cycle rule updates the
stage. Assume every event visit satisfies `L(Fx)>L(x)`; away from `E`, the map
may rotate the local wheel arbitrarily.

## Dichotomy

Let `gamma` be a periodic orbit.

- If `gamma` meets `E`, then its stage label strictly increases at least once
  over one period and never decreases. It cannot return to its initial state.
- If `gamma` avoids `E`, its stage never changes. It may be a local wheel cycle,
  but it does not execute the sieve recursion or generate the next prime from
  the current gap cycle.

This proves the dichotomy. It is a refinement of the monotone-clock theorem
[018](../018-monotone-sieve-clock-obstruction/paper.md) tailored to the natural
primorial-wheel architecture of [019](../019-primorial-gap-recursion-control/paper.md).

## Gate consequence

The first branch cannot supply A1. The second can supply only the finite-wheel
orbit already controlled in record 017; its arithmetic data are fixed externally
and it cannot earn A0 from an update rule it never uses. A candidate must thus
provide a different recurrent arithmetic state, not merely add local wheel
rotation to the advancing sieve state.

## Evidence index

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Monotone-clock theorem](../018-monotone-sieve-clock-obstruction/paper.md)
- [Primorial recursion control](../019-primorial-gap-recursion-control/paper.md)
