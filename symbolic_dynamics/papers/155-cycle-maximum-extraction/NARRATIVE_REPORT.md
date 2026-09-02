# P155 narrative report

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Why this map is worth isolating

The update forgets all cyclic order but remembers two ordered endpoint
systems: support minima choose the order of output coordinates, while support
maxima choose the target values.  This makes the map strongly lossy but leaves
enough geometry for an exact inverse theory.

The first signal is target-dependent rather than merely rank-dependent.  A
cycle support can collapse to one coordinate only if its target value is a
right-to-left minimum.  Therefore the target itself specifies its singleton
capacity, yielding the exact minimum source rank

```text
mu(sigma)=2|sigma|-rlmin(sigma).
```

The matching upper construction is not a counting argument.  It is a
deterministic endpoint scheduler with opener, closer, and simultaneous events.
Every right-to-left minimum can be synchronized at once, and no other target
position can be.  Splitting simultaneous events and inserting interior labels
turns the minimum construction into a right section at every larger rank.

The second axis retains information that the image theorem discards.  A
source first chooses an ordered set partition of `[n]` whose maxima have
standardization `sigma`.  It then independently chooses a cyclic order on
each block.  This gives the exact every-target weight
`prod_i(|B_i|-1)!`.  Thus existence is controlled by endpoint scheduling,
whereas multiplicity is controlled by labelled cycle species.

Forward dynamics closes honestly but modestly: equal source and target rank
means every cycle was a singleton, so only identities recur.  The finite tail
profile suggests a sharper clock, but the needed all-parameter lower bound is
open and is confined to the manuscript's Limitations paragraph.

## Ownership subtraction

The paper assigns zero contribution credit to block minima/maxima,
opener/closer configurations, cycles ordered by their minima, prescribed
cycle maxima, and `(b-1)!` cyclic-order counts.  The residual is only the
literal map's exact image/section/fibre conjunction and its recurrent
classification.  The primary-source audit is bounded and cannot establish
novelty or priority.

## Computational role

The verifier independently constructs literal permutations, endpoint dynamic
programs, greedy sections, and restricted-growth-word support sums.  Its
16,473,121 exact assertions are deliberately stronger than a few illustrative
examples but remain falsification pressure rather than proof.

Independent Hostile Review B rederived the complete owner-subtracted
narrative and returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`.
It requested no manuscript change, so Round 2 preserves the accepted Round-1
manuscript byte for byte under `HOLD_EXTERNAL`.
