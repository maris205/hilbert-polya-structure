# Scout-and-kill ledger: twelve literal combinatorial systems

**Counting rule:** one literal update is one system, independently of the
number of ranks enumerated.  **External state:** `HOLD_EXTERNAL`.

| ID | carrier and exact simultaneous update | exact small-case signal | prospective theorem axes | auditable decision |
|---|---|---|---|---|
| `C01 / PDD` | Words `w in [n]^n`; `(Pw)_i` is the number of distinct symbols in the strict prefix `w_0...w_(i-1)`. | All words through `n=7`.  At `n=7`: 823,543 states, first image 32, unique fixed word, sharp depth 6; exact tail histogram `1,35279,88200,164640,216090,201684,117649`. | Closed iterates; all-time binary-path images; every-time target-local product fibres; pointwise clock and depth CDF. | **`KEEP_GREEN_OWNER_THIN`.** Full theorem spike closed.  Restricted-growth vocabulary is subtracted; no literal iterative owner appeared in the bounded search. |
| `C02 / RCS` | Subsets `A={a_0<...<a_(k-1)} subset [0,n-1]`; `R(A)=supp{a_j-j}`. | Every subset through `n=18`.  At `n=18`: 262,144 states, first image 6,765=`F_20`, 19 fixed states, sharp depth 17, unique deepest `{0,17}`. | Exact gap evolution at every time; maximum-gap point clock; all-time image inequality; all-time target-fibre generating function; basin and depth enumeration. | **`KEEP_GREEN_OWNER_THIN`.** Full theorem spike closed.  Stars-and-bars/stretching is zero credit; no inspected source states the iterated support map. |
| `C03 / DSR` | Permutations `pi in S_n`; stably rank the integers `pi_i-i`, breaking ties by position. | Exhaustive through `S_9`: 362,880 states; at `n=9`, image 43,296, exactly 256 fixed points, all observed periods 1, maximum tail 4, fibre range 1--207. | Fixed-point composition bijection is proved; possible convergence clock and diagonal-inequality fibre determinant remain open. | **`RESERVE_AMBER_NOT_PROMOTABLE`.** The convergence theorem and inverse axis are not closed; displacement/rank literature is adjacent. |
| `C04 / BDS` | Set partitions of `[n]`; regroup elements by equal numerical distance `i-min(B(i))` from their old block minimum. | Every partition through `n=10` (115,975 states).  At `n=10`: image 8,432, no fixed point, all eventual periods 2, maximum tail 4, with one state at depth 4. | Possible eventual-transpose normal form, depth thresholds, and target interlacing fibres. | **`KILL_NO_GENERAL_CLOCK_OR_INVERSE`.** The period-two anomaly is exact only in the tested box; it sits dangerously near the directly owned occurrence-rank tableau map from the prior lane. |
| `C05 / CAD` | Permutations; stably rank the cyclic differences `pi_(i+1)-pi_i`. | Through `S_8`; at `n=8`, image 13,696, no fixed points, tail 32, and periods 14 and 16.  Earlier ranks have unrelated periods `2,5,{6,8},9,{6,10,12},{5,13,28}`. | Functional graph and difference-order fibres. | **`KILL_IRREGULAR_NO_PARAMETER_SPINE`.** Large periods are not a theorem signal when their rank dependence fragments immediately. |
| `C06 / CGS` | Subsets of `Z/nZ`; replace a nonempty subset by the support of its cyclic gap lengths modulo `n`, and fix the empty set. | Every subset through `n=14`; final box has image 80, three fixed states, tail 4, and periods 1, 3, 6.  Prime and composite ranks exhibit incompatible period sets. | Gap-composition quotient, image enumeration, temporal arithmetic. | **`KILL_ARITHMETICALLY_IRREGULAR_QUOTIENT`.** The map forgets cyclic placement at epoch one and supplies no uniform second axis. |
| `C07 / IHM` | Set partitions; join all old blocks whose integer hull intervals overlap, taking connected components of that overlap graph. | Every partition through `n=9`; it is idempotent, image/fixed count `2^(n-1)=256`; one-block fibres are the atomic-partition numbers `1,1,2,6,22,92,426,2146,11624`. | Interval-partition image and product fibres over atomic set partitions. | **`KILL_STATIC_CLOSURE`.** Both the clock and inverse are the same interval-overlap closure/species decomposition. |
| `C08 / FPT` | Compositions of `N`; at the leftmost descent `a_i>a_(i+1)`, transfer one unit from `a_i` to `a_(i+1)`. | All `2^(N-1)` compositions through `N=14`; final box has 135 fixed points, maximum tail 30, and only fixed recurrence.  The weighted position sum rises exactly one at every move. | Sharp potential height, nondecreasing endpoints, local inverse grammar. | **`KILL_LOAD_BALANCING_OWNER_DENSE`.** A leftmost chip transfer supplies no independent inverse and lies in occupied sorting/chip-firing territory. |
| `C09 / FCR` | Compositions; rotate the part list left by its current first part modulo the number of parts. | Through `N=12`; 2,048 states, image 1,478, 78 fixed, tail 5, and periods 1 through 10 in the last box. | Decomposition by cyclic part words and weighted pointer maps. | **`KILL_ARBITRARY_WEIGHTED_CIRCLE`.** On each rotation class this is merely the pointer endomap `j -> j+a_j`; no class-uniform theorem survives. |
| `C10 / MEP` | Simple labelled graphs; retain exactly old edges incident with at least one old maximum-degree vertex. | Every graph through six vertices; at `n=6`, 32,768 states and 6,401 image/fixed graphs, maximum fibre 768.  The map is idempotent in every checked state. | Fixed graphs and inverse degree-realisation counts. | **`KILL_SELF_SELECTED_PROJECTION`.** Idempotence follows immediately because old maximum-degree vertices lose no edge; inverse degree coupling does not close. |
| `C11 / DTR` | Simple labelled graphs; regenerate `uv` iff `deg_G(u)+deg_G(v)>=n`. | Every graph through six vertices; final box has image 1,974, 944 fixed graphs, and maximum tail 3; all tested recurrence is fixed. | Threshold fixed graphs, convergence, degree-sequence fibres. | **`KILL_OWNER_DENSE_NO_INVERSE`.** Degree-threshold graph transforms are a mature silhouette, and target recovery is a coupled graphical-sequence problem. |
| `C12 / HLC` | Labelled posets; compute each vertex's longest-chain height and replace the order by the complete weak order of those height layers. | Every labelled poset through `n=5` (4,231 states); idempotent; image 541, the ordered Bell number, and maximum fibre 49. | Ordered-partition image and height-profile source counts. | **`KILL_STATIC_RANK_PROFILE`.** The image and clock are merely the height stratification; the hard source count has no independent temporal content. |

## Funnel

```text
12 literal finite systems
  2 theorem-complete recommendations (PDD, RCS)
  1 numerical reserve with a proved fixed locus but open clock/inverse (DSR)
  3 irregular/no-spine kills (CAD, CGS, FCR)
  4 static/closure/projection kills (IHM, MEP, HLC, BDS after gate)
  2 owner-dense/no-inverse kills (FPT, DTR)
```

The breadth denominator is twelve, not twelve validated subclasses and not
twelve novelty claims.

