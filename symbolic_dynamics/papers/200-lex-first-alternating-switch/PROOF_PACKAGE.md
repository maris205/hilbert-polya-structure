# P200 proof dependency and attack points

All proofs are in main.tex and quantify over all stated r,s>=2.

1. An alternating pair is exactly two incomparable supports. The least
   columns are min of their two exclusive sets, sorted.
2. A row comparable with two incomparable supports is below their
   intersection or above their union. Both are switch-invariant. This
   protects all earlier first pivots while keeping the current pair
   incomparable, so the partner cannot increase.
3. The flipped rectangle stays alternating. Hence selectors never
   increase. Selector equality is exactly a two-cycle, and a decrease
   excludes recurrence. First-two-difference types and intervening
   row comparability characterize equality completely.
4. With a partner unchanged, at most one preliminary switch is needed
   before the first two differences become its column selector.
   A third visit before first recurrence is impossible. Counting
   selector states, including the terminal recurrent one, gives
   tau+1<=2p and thus tau<=2r−3.
5. The wide witness has pivot {k+1}, then {0}, then {k} at partner k.
   After its two switches row k becomes {0,k+1,...,r}; partner k−1
   is exactly next. The last listed selector is recurrent and all
   preceding transitions strictly decrease. Thus the exact tail is
   2r−3, without using transposition.
6. Reverse-switch exclusive minima satisfy equation (8). Their
   equivalent first-difference/prefix condition and earlier-partner
   containment are necessary and sufficient. Earlier pivot rows stay
   protected by the same intersection/union argument. Distinct
   rectangles flip different entries.
7. At most r−i−1 partners times at most s−1 opposite columns gives
   the maximum. Equality forces i=0, all columns differing and
   singleton same-type difference {0}, hence exactly two targets.
   The separate 2x2 map is bijective on all16 states.

No empirical fit is used. The fixed lonesum class, margin invariants,
classical 2-switch and generic lexicographic scheduling receive zero
contribution credit. Narrow/square sharpness is not deduced; the earlier
false transpose-style reasoning remains withdrawn in its scout history.
