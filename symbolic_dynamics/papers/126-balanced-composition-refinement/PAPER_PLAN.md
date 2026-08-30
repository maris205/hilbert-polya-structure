# Paper plan — P126

## Problem anchor

For synchronous balanced halving on integer compositions, determine the
temporal information strictly beyond stabilization: the complete equality
kernel of every iterate, every target fibre, and every iterated image.

## Frozen theorem contract

1. Exact pointwise depth and sharp global depth.
2. For `K=2^t`, the canonical form that replaces every part at most `K` by
   ones is the complete kernel invariant of `Phi^t`.
3. The canonical image words form a suffix code, giving an explicit
   right-to-left decoder.
4. Every nonempty `t`-fibre is a product of `K`-restricted composition counts
   over canonical one-runs; the maximum is `R_K(n)` at `1^n`.
5. The same `R_K(n)` counts states of depth at most `t`.
6. The `t`-image is in weight-preserving bijection with compositions whose
   parts are `1` or exceed `K`, with OGF
   `(1-x)/(1-2x+x^2-x^(K+1))` and an exact Garden census.

## Proof architecture

- Codeword induction supplies length, terminal marker, and clock facts.
- The terminal marker proves suffix decodability and hence injectivity on
  canonical forms.
- Normal-form preimages decompose independently over maximal one-runs.
- Canonical forms then enumerate the image tower by an ordinary sequence
  construction.

## Claim ceiling

The residual is the conjunction of the literal dynamics with the complete
all-iterate kernel/fibre/image package.  Restricted-composition recurrences,
the no-part-2 sequence, generic suffix-code facts, balanced splitting, and
substitution/fragmentation frameworks are background.  External status is
`HOLD_EXTERNAL`.

The internal package silhouette is also zero-credit: P094 already occupies
morphism/recognizability language, P108 clock--Fibonacci--fibre geometry,
P113 integer-sum absorption and product-fibre transport, P115 the
all-iterate image/fibre/log-threshold package, P122 target-local fibre DP and
Garden enumeration, P123 refinement, and P125 pointwise fibres/image layers.
Only the present map's exact all-iterate kernel, one-run fibre product, and
temporal image bijection remain inside the contract.
