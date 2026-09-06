# Replacement cross-class breadth scout — P162--P166

**Date:** 2026-09-02 UTC  
**Route:** replacement breadth across five carrier classes  
**External state:** `HOLD_EXTERNAL`  
**Paper assignment:** none

## Outcome first

This lane exact-tested **20 new literal systems**, four each from nonlinear
arrays, finite posets/lattices, maps on functions/relations, rank-changing
combinatorial objects, and state-dependent Markov kernels.  The independent
deterministic verifier made **914,408 assertions** and froze a canonical
transcript.

The survivor pool is **empty**.  This is a value/owner conclusion, not a
failure to find correct formulas:

- `RCE` produced the strongest early array anomaly: tails `1,2,3,4` through
  square order four and only periods one and two.  Its exact factor is a pair
  of mutually iterated histograms, however, so inventory-loop theory owns the
  temporal engine.  The remaining binary-margin realization problem is not a
  second dynamical theorem.
- `OIH` produced a clean all-size fence theorem: a sharp linear clock and an
  odd/even fixed-versus-two-cycle dichotomy.  Cold derivation shows that its
  minimal-element coordinates are *exactly radius-one binary dilation*.
  Thus the whole temporal theorem lies in the elementary morphology engine
  already excluded alongside `X05`, with passive maximum bits.  It is killed
  rather than renamed.
- `CRG` has genuine adaptive depth (`3` by total weight 14) and is not the
  literal `R11` adjacent-GCD smoother.  But only termination, its adjacent-
  coprime fixed locus, and a refinement recursion survived.  Those do not
  form two independent all-parameter axes after P147/P121/R11 subtraction.
- The stochastic systems either square to Bernoulli--Laplace, expose only a
  label-dependent rank clock, already have nonabsorbing recurrent classes at
  order three, or randomize a closure frontier without an all-parameter law.

There are therefore **0 GREEN, 0 AMBER, and 20 KILL** decisions.  No weak row
is kept to fill the five-paper quota, and none receives a paper number.

## Collision firewall applied before counting

The full P1--P161 occupancy summaries and current kill ledgers were read before
the pool was frozen.  In particular:

- equal-size block merging was excluded because it is exactly killed `ESA`
  and lies behind the parallel-Glaisher/Latapy gate;
- fence pseudocomplement was excluded because it is exactly killed `LT1`;
- cyclic adjacent-GCD smoothing was excluded because it is exactly killed
  `R11`, whose binary shadow is exactly killed `X05` erosion;
- `RFW`, `CNG`, and `AA01/USP` remain killed by the current hostile gate;
  `BQC` remains low amber in its existing lane and was not recycled;
- generic direct images, LDU/Gaussian-elimination rewrites, finite-linear
  functional graphs, totalized rational maps, group power maps, closure/
  pruning, and renamed classical Markov chains receive no contribution credit.

The 20 rows below are not exact repeats in the internal ledgers.  Some have an
exact *factor* or proof engine that is occupied; those reductions are the
reason for killing them.

## Exact executable contract

[`verify_scout.py`](verify_scout.py) is self-contained.  It imports no author,
paper, or prior-scout code and uses no seed, sampling, floating point,
third-party package, timestamp, or network access.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py > /tmp/replacement_crossclass.out
cmp -s CANONICAL.txt /tmp/replacement_crossclass.out
```

[`CANONICAL.txt`](CANONICAL.txt) is the frozen stdout.  Finite enumeration is
counterexample pressure only; the all-parameter deductions stated below come
from the literal rules.

## Twenty-system decision ledger

| ID | carrier and literal update | exact signal / first theorem axis | independent-axis attack | collision or failure | decision |
|---|---|---|---|---|---|
| `A01 RMN` | `m x n` binary arrays; complement each row whose weight is above `n/2` | one-step retraction; per-row image `sum_(j<=n/2) C(n,j)` | fibres are 2 below the middle layer and 1 on an even middle layer | coordinate normalization only | **`KILL_THIN_RETRACTION`** |
| `A02 SBH` | replace a binary matrix by the complete rectangle on its nonzero rows and columns | idempotent; image `1+(2^m-1)(2^n-1)` | a target `R x C` has the no-zero-margin inclusion--exclusion fibre | generic support closure/direct image | **`KILL_CLOSURE`** |
| `A03 RCE` | `A'_(ij)=1` iff row degree `r_i(A)` equals column degree `c_j(A)` | full orders 1--4 give `(image,fixed,max tail,max period)` = `(1,1,1,1),(4,1,2,1),(41,10,3,2),(1100,17,4,2)` | every inverse is a sum of binary-matrix margin counts | exact mutual-inventory factor; residual is static margins | **`KILL_DIRECT_TEMPORAL_ENGINE`** |
| `A04 CCC` | for a `q`-ary rectangle, delete top row/left column when the top-left entry is nonzero, otherwise bottom row/right column | clock is exactly `min(h,w)` | every nonempty one-step target has an explicit two-branch fibre | content gate on P160 rectangular-corner stripping | **`KILL_INTERNAL_P160`** |
| `L01 LMC` | Boolean lattice; `s -> (s meet (a join b)) join (a meet b)` | idempotent median clamp onto interval `[a meet b,a join b]` | image `2^d`, uniform fibre `2^(n-d)`, `d=|a xor b|` | coordinate lattice polynomial | **`KILL_THIN_LATTICE`** |
| `L02 LCP` | pairs in a Boolean lattice; `(x,y)->(x meet y,x join y)` | one-step lattice comparator; image `3^n` | target `(u,v)`, `u<=v`, has fibre `2^|v-u|` | classical meet/join sorting | **`KILL_THIN_LATTICE`** |
| `L03 OIH` | fence ideal `I`; generate the ideal by all `x` for which `|down(x) cap I|` is odd | sharp clock and complete fixed/2-cycle census | recurrent ideal is resolved by maximum bits | minimal bits are exactly elementary binary dilation, in the excluded `X05` morphology engine | **`KILL_ELEMENTARY_DILATION`** |
| `L04 MSD` | Boolean-lattice pairs; `(x,y)->(x meet y,x xor y)` | all orbits are fixed after at most two steps | image `3^n`, fixed set `2^n`, target fibre `2^|v|` | product of one four-state truth table | **`KILL_PRODUCT_TRUTH_TABLE`** |
| `F01 KRR` | endofunction; replace each value by the least index in its fibre | idempotent; image is the `B_n` canonical kernel partitions | a `k`-block target has `(n)_k` sources | one-step kernel quotient beside P143 | **`KILL_QUOTIENT`** |
| `F02 REM` | binary relation; relate two labels iff their source rows are identical | idempotent; image is all equivalence relations | a `k`-class target has `(2^n)_k` sources | equality-kernel direct image | **`KILL_QUOTIENT`** |
| `F03 FSQ` | full transformation monoid; `f -> f composed with f` | exact pointwise preperiod and period from tree height and cycle lcm | fixed counts have an explicit functional-digraph sum | directly surrounded by full-transformation powers/roots; generic power ban | **`KILL_DIRECT_POWER_OWNER`** |
| `F04 RSC` | binary relation; `R -> R cap R^T` | idempotent; image is all symmetric relations | target fibre is `3^a`, `a` absent unordered off-diagonal pairs | meet-with-involution, beside P102/P127 | **`KILL_INTERNAL_LATTICE_MEET`** |
| `C01 CRG` | composition; merge every maximal run whose adjacent entries have `gcd>1` | total weight is fixed, length strictly falls, fixed iff adjacent entries are coprime | one-step sources admit only a coupled segmentation/refinement recursion | no independent theorem after P147/P121/R11 warning | **`KILL_BELOW_VALUE_FLOOR`** |
| `C02 DQC` | directed relation; quotient vertices by equal current outdegree using existential edges | rank never grows and every orbit fixes in at most the old rank | order-four image/fixed counts are `423/256`; no target atlas emerged | direct quotient/BQC engine | **`KILL_DIRECT_IMAGE`** |
| `C03 TWC` | binary matrix; retain the sorted list of distinct columns | one-step rank contraction | an `r`-column target has `r! S(w,r)` ordered sources | duplicate deletion/setification beside P143 | **`KILL_CANONICALIZATION`** |
| `C04 SEQ` | rooted unordered tree; merge sibling roots having equal current subtree size, simultaneously at every parent | maximum tails through orders 1--10 are `0,0,1,1,2,3,3,4,5,6` | fixed trees have recursively distinct sibling-subtree sizes | recursive lift of killed equal-size merger plus P148 tree quotient | **`KILL_INTERNAL_ENGINE_LIFT`** |
| `M01 CPS` | nonempty subset; choose a uniform member `i` and send `S` to `S^c union {i}` | size alternates deterministically `k <-> n-k+1` | the exact two-step target kernel is computable | square is lazy Bernoulli--Laplace/Johnson exchange; P145 nearby | **`KILL_DIRECT_MARKOV_OWNER`** |
| `M02 FLM` | endofunction; choose a uniformly maximal-load fibre, move its least-index member to the least empty value | image size rises exactly one; clock `n-|im f|` | terminal support first branches but has size only two through order five | label-dependent tie breaking; no all-size terminal law | **`KILL_THEOREM_THIN`** |
| `M03 DRC` | square binary array; choose a uniform index with unequal row/column degree and complement that row | exact rational kernel; 512 order-three states scanned | order three already has closed SCCs of size six | no absorption or stable all-parameter invariant | **`KILL_UNSTABLE_MARKOV`** |
| `M04 OPG` | fence ideal; choose uniformly an outside element with odd principal-ideal intersection and adjoin its downset | monotone and finite; terminal laws exact by DAG recursion | terminal support grows `1,1,1,1,2,2,3,3,4` through fence order nine | randomized frontier closure behind `OIH`; no closed second axis | **`KILL_STOCHASTIC_CLOSURE`** |

## Cold derivations of the strongest false starts

### `RCE`: a bipartite lift of mutual inventory

Let

```text
r_i = sum_j A_ij,          c_j = sum_i A_ij,
a_v = #{i:r_i=v},          b_v = #{j:c_j=v}.
```

The update is literally

```text
T(A)_ij = [r_i=c_j].
```

Consequently its new margins are

```text
r'_i=b_(r_i),              c'_j=a_(c_j).
```

After the first step, all further temporal information therefore lives in a
pair of mutually describing histograms.  This explains the short tails and
two-cycles without treating the order-four enumeration as an all-size proof.
It also creates the fatal subtraction: iterated inventories and mutually
descriptive frequency vectors are established objects.  Recovering a source
from prescribed `(r,c)` is the static enumeration of binary matrices with
those margins.  No inspected formula joined that static count to a new second
dynamical axis.

The bounded search found no source for the exact displayed matrix lift.  That
non-hit is not used as positive evidence.  The frozen claim ceiling is only:

> `RCE` factors after one step through a two-population inventory map, and its
> checked square orders have periods at most two.

It must not be promoted without an all-size temporal theorem that survives
inventory subtraction and a separate explicit target-resolved result.

### `OIH`: the attractive fence formula is elementary dilation

Write the alternating fence as minima `e_0,...,e_k` with maxima `o_i`
covering consecutive minima.  The ideal condition says `o_i=1` only when
`e_i=e_(i+1)=1`.  If `s_i` is the parity of the old ideal inside the
principal ideal of `o_i`, then

```text
s_i = o_i xor e_i xor e_(i+1),
e'_i = e_i OR s_(i-1) OR s_i.
```

Using the ideal condition, the second line simplifies pointwise to

```text
e'_i = e_(i-1) OR e_i OR e_(i+1),
```

with the obvious boundary convention.  Hence nonempty minimum support expands
one edge per step.  Its pointwise depth is the covering radius of the initial
support in the path of minima.

For `n=2k+1`, after all minima are present the `k` maximum bits are arbitrary
and fixed.  Including the empty ideal gives `2^k+1` fixed points and maximum
depth `k`.  For `n=2k`, the dangling last maximum toggles; there is one fixed
empty ideal and `2^(k-1)` two-cycles, with maximum depth `k-1`.  These are
all-parameter theorems, but their temporal engine is exactly elementary
binary dilation.  `OIH` is therefore a useful negative control, not a reserve.

### `CRG`: distinct from `R11`, still below threshold

For a composition `a=(a_1,...,a_l)`, join positions `i,i+1` when
`gcd(a_i,a_(i+1))>1` and replace each connected run by its sum.  Every
nonfixed update strictly decreases `l`, total weight is preserved, and the
fixed locus is precisely

```text
gcd(a_i,a_(i+1))=1 for every i.
```

Thus the clock is at most `l-1`.  Adaptive recomputation is real: maximum
depths by total weight 1 through 16 are

```text
0,0,0,1,1,1,1,2,2,2,2,2,2,3,3,3.
```

This is not `R11`: for example `(2,3,4)` is fixed here, whereas cyclic
adjacent-GCD smoothing changes every coordinate and preserves length.  The
distinction prevents an *exact-map* kill.  It does not supply paper mass.
The proposed inverse axis merely enumerates segmentations of each target part
whose internal adjacent gcds exceed one while adjacent segment boundaries are
coprime; boundary choices are coupled.  No closed target theorem or sharp
all-weight clock emerged, and the vocabulary is already saturated by P147
run consolidation, P121 coalescence, and R11.  `CRG` is killed now; its small
depths are not a silent reserve.

## Two exact but owner-thin formulas

For `CCC`, let a source have shape `h x w` and a nonempty target `B` have shape
`(h-1) x (w-1)`.  Its one-step fibre is

```text
(q-1) q^(h+w-2) + [B_00=0] q^(h+w-1).
```

The first summand pads the deleted top/left border with a nonzero corner; the
second pads the bottom/right border while retaining a zero target corner.  If
the target shape is empty, every one of the `q^(hw)` sources maps to the sink.
This correctness does not overcome the exact P160 clock/mechanism collision.

For `FSQ`, let `H(f)` be the maximum in-tree height of a functional digraph and
`L(f)` the lcm of its cycle lengths.  Put `a=v_2(L)` and `L_o=L/2^a`.  Since

```text
T^t(f)=f^(2^t),
```

the preperiod and period under `T` are

```text
max(ceil(log_2 H),a),       ord_(L_o)(2),
```

where the order is one for `L_o=1`.  Moreover `T^t(f)=f` exactly when every
vertex is on or directly attached to a cycle whose length divides `2^t-1`.
If `p_c(d)` counts permutations of `c` labels with all cycle lengths dividing
`d`, the fixed count is

```text
sum_(c=1)^n C(n,c) p_c(2^t-1) c^(n-c).
```

The verifier confirms these formulas for every endofunction through order
five.  They are nevertheless standard power/functional-digraph consequences,
and transformation powers and roots have direct owners.

## State-dependent Markov attacks

The Markov rows were required to be literal state-dependent kernels, not
ordinary gambler's ruin, coupon collection, random deletion, linear extension,
standard Glauber, or a fixed-slot reversible walk in disguise.

- For `CPS`, two steps from a `k`-subset stay put with probability
  `1/(n-k+1)` and replace a specified `i in S` by specified `j notin S` with
  probability `1/[k(n-k+1)]`.  This is exactly lazy Johnson exchange, so the
  lift is killed.
- For `FLM`, every move creates one new image value.  The clock is consequently
  deterministic, but the least-index/least-empty conventions dominate the
  terminal and no label-invariant target law appeared.
- For `DRC`, the exact closed-SCC signatures `(n,total SCC,closed SCC,max closed
  size,absorbing)` are `(1,2,2,1,2)`, `(2,16,8,1,8)`, and
  `(3,192,112,6,80)`.  The order-three closed classes of size six destroy the hoped-for
  absorption silhouette.
- For `OPG`, exact rational DAG recursion gives multiple terminals from fence
  order five onward, but neither support nor weights stabilized into an
  all-parameter law.  Randomizing an owned frontier/closure mechanism is not a
  contribution.

## Breadth disposition

```text
literal systems exact-tested                    20
nonlinear arrays                                 4
finite posets/lattices                           4
maps on functions/relations                      4
rank-changing combinatorial objects              4
state-dependent Markov kernels                   4
direct temporal/power/Markov owner kills         3
exact internal proof-engine collisions           5
thin/closure/unstable/below-value kills          12
GREEN / AMBER / KILL                         0 / 0 / 20
paper-sized owner-thin survivors                  0
external state                        HOLD_EXTERNAL
```

The full bounded owner record is in
[`OWNER_SEARCH_LOG.md`](OWNER_SEARCH_LOG.md).  A later lane must change both
the literal update and the controlling proof engine; a new carrier name,
parameter, stochastic scheduler, quotient drawing, or closure section does
not reopen any killed row here.
