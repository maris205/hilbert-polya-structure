# P192 process-separated hostile Review B

## Verdict

`PASS / ZERO OPEN FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-1 package survives a new residual-cycle-splitting audit.
Review B is neither the author nor Reviewer A, imports neither implementation,
and made no change under `papers/192-first-collision-hurwitz/`.

## Independent representation

The author generated the carrier as one Hurwitz orbit.  Review A scanned the
Cartesian power of all transpositions and filtered by product.  Review B
instead starts from the residual long cycle and recursively left-multiplies by
a transposition joining two points of the same residual cycle.  Each step
splits one cycle; reaching the identity after `n-1` splits emits one ordered
factorization.  This constructs all `280,392` states for `2<=n<=8` without an
orbit, tree code, or product filter.

A separate content-vector dynamic program counts parking words and adjacent-
unequal arrangements through length nine.  It neither enumerates Pollak
circles nor consumes the factorization graph.

## Hostile attacks

- **`n=2`:** the carrier is exactly `((1,2))`; it is fixed, has tail zero,
  and its self-fibre has size `1=n-1`.
- **Hurwitz orientation:** direct products confirm that the canonical chain
  is `(1 2 ... n)` under rightmost-first composition and its reversal is the
  inverse cycle.  At `n=4`, the frozen orientation has one history `(1,2)`
  and maximum tail two, whereas the inverse-cycle carrier has no such history
  and maximum tail one.
- **Strict clock and sharpness:** every literal history is strictly increasing;
  the stated witness executes `1,...,n-2` and terminates at the chain.
- **Fixed census:** the graph count and independent parking-content DP both
  give `(n-1)^(n-2)`.
- **Every target fibre:** literal incoming source sets equal the self source
  plus exactly the reverse-admissible `H_i^{-1}` sources before the target's
  first collision.  Fibre mass, maximum `n-1`, and unique chain maximizer all
  pass.
- **Owner subtraction:** Campion Loth--Rattan is cited, its conditional
  Hurwitz-string mechanism is zero-credit, and the object-level distinction
  is explicit.
- **Conjecture quarantine:** all 127 history masks through `n=8` and the pinned
  independent `n=9` stream agree with the displayed law, but the law and its
  consequences remain explicitly conjectural and unused by the proved axes.

## Finding census

- Critical: `0`
- Major: `0`
- Minor: `0`

## Exact receipt

```text
states/transitions/targets: 280,392 / 280,392 / 280,392
reviewer assertions: 4,606,117
reviewer digest: 5343319ee0915bf342877ea2511e14201fa9c99c0822804ae914f94550b2ba5f
reviewer canonical SHA-256: a56ac0eb6c8975273b2c9a3153572ac945f4ff7ef89c8619830e784c831261c5
Round-1 PDF SHA-256: e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
replay 1 / replay 2: byte-identical
```

Review B accepts a byte-identical internal Round-2 receipt only.  Direct
ownership remains unresolved under `OWNER_RED_AMBER / HOLD_EXTERNAL`; bounded
search and exact computation establish no novelty, priority, or freedom to
operate.
