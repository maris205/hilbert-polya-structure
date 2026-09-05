# LFAS all-parameter proof audit

All coordinates are zero-based and `r,s>=2`. Tail means first entry into the periodic part of the full finite functional graph, not first repeated step.

## Literal selector and invariant pivot

For an incomparable row pair, let its symmetric-difference word list the unequal columns in order, with signs according to the containing row. An alternating rectangle chooses opposite signs. The lexicographically first one pairs the first sign with the first later opposite sign. This is exactly the author's `min D`, `min E` rule; the displayed coordinate order matters.

If `i` is the first row participating in any incomparable pair, every row `h<i` is comparable with both rows of the selected pair. Because those two rows are incomparable, `A_h` must lie below their intersection or above their union; any mixed position would order the pair. Their interchange preserves intersection and union. Thus all earlier rows remain comparable to every row. The two changed rows remain incomparable, so pivot `i` persists and the least partner can only stay or decrease. The same argument works when reversing a candidate target rectangle, which is essential to the inverse theorem.

## Periodic criterion and the two-visits bound

The current rectangle remains alternating after switching. Therefore the entire selector is nonincreasing. Equal successive selectors give an immediate involutive return; a strictly smaller selector excludes the preceding state from any periodic orbit. Hence periods are only one or two, and a switched state cannot reach a fixed point.

For one fixed partner, switching exchanges the first sign and the first opposite sign of its difference word. If the first two signs were already opposite, the column selector is unchanged. Otherwise the second differing position retains the old first sign and is now opposite to the switched first sign, so the next column selector is the first two differing columns. Thus, while no earlier partner appears, the pair either already yields a two-cycle or reaches its final two-cycle column pair after one switch. Within the selector states from time zero through first recurrence, a partner can occur at most twice. If a partner occurred a third time there, the preceding two equal column selectors with the same pair would already prove recurrence one step earlier. Since partners never return, `tau+1<=2p`.

The recurrent iff criterion is exact: first two difference signs must be opposite, and the changed pivot must remain comparable with every intervening row. Earlier pivots are handled by the invariant-pivot lemma, the current partner remains available, and no later pair can precede it. This handles both necessity and sufficiency, not just a sufficient local return test.

## Wide sharpness and limits

For the proposed supports, at the start of partner `k`, the pivot is `{k+1}`. Every earlier partner contains it, whereas row `k` omits it and has least exclusive element zero. The first switch makes the pivot `{0}`; the next uses columns `0,k` and makes it `{k}`. Meanwhile row `k` becomes `{0,k+1,...,r}`. Row `k-1` is now the first earlier row missing the pivot and induction continues. At partner one the second listed selector is recurrent. There are `2r-2` selector states through this recurrence, hence exactly `2r-3` transient steps. Trailing zero columns do not change any selector, establishing equality for every `s>=r+1`.

At `r=2,s>=3` the same witness has tail one. At `2x2`, the only alternating pair of matrices forms a two-cycle and all other states hold, so maximum tail is zero. This is consistent with the bound, whose sharpness is claimed only in the wide regime. No transpose argument is used: independently found image sizes 3292 and 3290 for `3x4` and `4x3` refute any naive scheduler conjugacy by transposition.

## Complete inverse and distinctness

Fix target rows `P,Q` at candidate pair `(i,k)`. Reversing opposite exclusive columns flips their signs in the difference word. For those columns to be the first opposite pair in the reconstructed source, one must be the target's first differing column and the other must lie in the initial run of opposite signs immediately following it, before the next same sign. This is precisely the author's `ell<b_k` condition. Common columns are irrelevant and no discarded column can qualify.

There can be no earlier pivot in the reconstructed source by the intersection/union argument above. Having no earlier partner is exactly comparability of the changed pivot with every row `i<h<k`. Thus the target conditions give all and only scheduled source rectangles without running a selector on each source candidate. Distinct rectangles change distinct four-cell sets, so there are no duplicate source states. For a fixed target, a switch-source is impossible because the switched rectangle would still be alternating in the target; only its self-source remains.

## Extremum and all equality cases

Each of at most `r-i-1` partner rows supplies at most `s-1` opposite columns. The stated complementary star targets realize every choice: reversing a chosen column makes the pivot a singleton contained in each earlier partner (or its complement case). Hence the product bound is attained.

If the product exceeds one, a maximum target cannot be fixed. Equality forces `i=0`, all partner terms present, and each initial opposite run to use all remaining `s-1` columns. There is then one first-sign column at zero, no common columns, and all other columns have the opposite sign. Consequently every partner is the same complement of row zero, and row zero is either `{0}` or its complement. This proves exactly two targets. When the product is one, `r=s=2`, the whole map is bijective: 14 self-loops and one two-cycle, giving all 16 equality targets.

Conclusion: all four numbered author theorems are valid on their stated domains. No finite-data inference is used to extend the unproved narrow/square conjecture.
