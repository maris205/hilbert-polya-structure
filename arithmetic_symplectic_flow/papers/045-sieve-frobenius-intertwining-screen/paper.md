# Primorial sieve updates cannot intertwine with fixed-prime Frobenius packet flow

**Paper ID:** `045-sieve-frobenius-intertwining-screen`  
**Record ID:** `ASFS-SCOUT-20260914-33`  
**Date / status:** `2026-09-14; PRE-P0 STOP — PRIME LABEL CHANGES UNDER SIEVE UPDATE BUT IS FLOW-INVARIANT ON FROBENIUS PACKETS`  
**Route state:** `Route A not evaluated; Route B NOT INVOKED`

## Test

The source state at sieve stage `k` reads `L(k)=p_(k+1)` from its primorial gap cycle. Thus `L(k+1)=p_(k+2)` differs from `L(k)`. On the proposed target, the finite-place Frobenius mapping torus above `C_p` is a component labelled by the same prime `p`; its flow never changes this component label.

Suppose an action-preserving coding `h` took stage `k` into the packet `C_(L(k))`. Intertwining the source update with any target flow time would give `h(k+1)` in the same target component as `h(k)`, because the target action preserves `p`. The label requirement instead puts them in `C_(p_(k+2))` and `C_(p_(k+1))`, distinct components. Contradiction.

This does not deny a bare set map from stages to primes. It proves that such a map is not an action-preserving symbolic-to-Frobenius coding. Adding a jump between packet components would define a new groupoid/action and must not borrow the target's packet clock, repetitions, or trace data.

| Gate | Status |
| --- | --- |
| A0 | source retained only; no same-object target action |
| A1 | `scoped FAIL — no action-intertwining orbit carrier` |
| A2 | `NOT EVALUATED` |
| Route B | `NOT INVOKED` |

**Decision: stop/fork.** This closes the direct finite-place Frobenius bridge under the natural component-label requirement. Future work needs a new carrier whose arithmetic transition and periodic packet action move under one law.
