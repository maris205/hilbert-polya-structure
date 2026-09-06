# P166 Round-7 exact scout

**Verdict:** `KILL_ALL`  
**Exact replay:** `verify_scout.py` / `CANONICAL.txt`  
**Assertions:** 123,632  
**External state:** `HOLD_EXTERNAL`

The six systems below were enumerated only after searching the current
P162--P166 scouting tree for literal repeats.  The acceptance threshold was a
sharp all-parameter temporal theorem plus a logically independent target,
image, recurrent, extremal, or recovery theorem after owner subtraction.
Small-box regularity alone was not promoted.

## 1. `DCF`: double-conjugation feedback

For a finite group `G`, set

```text
D_G(x,y)=(xyx^{-1},yxy^{-1}).                         (1)
```

On an abelian group this is exactly `(x,y)->(y,x)`, so every point has period
one or two and every fibre is a singleton.  Nonabelian boxes do not preserve
that silhouette:

| `G` | states | image | max tail | max period | max fibre |
|---|---:|---:|---:|---:|---:|
| `C3` | 9 | 9 | 0 | 2 | 1 |
| `S3` | 36 | 30 | 1 | 2 | 3 |
| `D4` | 64 | 64 | 0 | 2 | 1 |
| `A4` | 144 | 120 | 1 | 6 | 4 |
| `S4` | 576 | 360 | 1 | 6 | 5 |

The changing image and periods are not evidence for a theorem over arbitrary
finite groups.  A theorem would require classifying a two-variable group word
map, while inverse counts are word-equation counts with no target-local
factorization.  Conjugation racks, matched-pair/Yang--Baxter maps, and group
word maps are established owner neighborhoods; HUR and RTCD already consume
nearby action packages internally.  `KILL_NO_ALL_GROUP_SPINE`.

## 2. `RPF`: ring-pair feedback

On `(Z/mZ)^2`, define

```text
R_m(x,y)=(x+xy,y+xy).                                  (2)
```

The difference `d=x-y` is invariant.  If `(u,v)` is a target and
`d=u-v`, every source is uniquely `(x,x-d)`, where

```text
x^2+(1-d)x-u = 0 (mod m).                              (3)
```

Thus (3) is a complete every-target one-step fibre formula.  It also explains
the prime-field image size `m(m+1)/2`: each invariant line is a quadratic
map with the usual two-to-one/critical-value split.  For composite `m`, the
largest fibres become the corresponding quadratic-congruence root counts.

The temporal side does not close.  On the invariant line `x-y=d`, (2) is
exactly

```text
x -> x^2+(1-d)x (mod m),                               (4)
```

so an all-parameter orbit theorem would classify a full family of quadratic
polynomial functional graphs.  The exact boxes already change from only
fixed recurrence (`m=2,3,4`) to periods two (`m=5,7,8,9`) and periods three
and four (`m=11,13`); maximum tails range from one through six.  Equation
(3) is one axis, not two.  `KILL_QUADRATIC_FAMILY_NO_CLOCK`.

## 3. `IHI`: incidence--Hadamard inverse

Let `U_n(F_2)` be the unitriangular incidence algebra of the chain `[n]`.  For
`U=I+N`, define

```text
H(U)=U circ U^{-1},                                    (5)
```

where `circ` is entrywise multiplication.  Since
`U^{-1}=I+N+...+N^{n-1}`, a strict entry `(i,j)` survives precisely when it
was present and the number of directed `i`--`j` paths in `N` is odd.
Consequently (5) never creates an entry and has no nontrivial recurrent
cycles.

There is a genuine triangular temporal observation.  For interval length
`ell=j-i`, the survival decision is the old bit times a Boolean expression in
strictly shorter intervals.  Induction on `ell` therefore stabilizes every
entry by time at most `ell-1`, and the whole matrix by time `n-2`.  The exact
boxes attain `n-2` for every `3<=n<=6`.

The second axis fails decisively:

| `n` | states | image | fixed/recurrent | max first fibre |
|---:|---:|---:|---:|---:|
| 3 | 8 | 7 | 7 | 2 |
| 4 | 64 | 42 | 41 | 6 |
| 5 | 1,024 | 427 | 393 | 26 |
| 6 | 32,768 | 7,373 | 6,082 | 164 |

The target-predecessor condition is a coupled parity system over all paths;
no interval product, target statistic, or closed fixed census emerged.
Moreover, both `A circ A^{-1}` and incidence-algebra inversion are standard
inputs.  A monotone `n-2` deletion clock without a closed inverse or extremal
axis is below threshold.  `KILL_NO_SECOND_AXIS`.

## 4. `AST`: asymmetric sandwich transformations

Let `T_n` be the full transformation monoid on `[n]`.  On `T_n^2`, set

```text
S(a,b)=(aba,ab),                                       (6)
```

with multiplication given by composition.  Both output ranks are at most
`min(rank(a),rank(b))`, but stabilization of ranks does not stabilize the
pair.  Exhaustion gives:

| `n` | states | image | max tail | recurrent | periods | max fibre |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 1 | 1 | 0 | 1 | 1 | 1 |
| 2 | 16 | 6 | 1 | 6 | 1,3 | 6 |
| 3 | 729 | 135 | 3 | 87 | 1,3,4 | 87 |

The signal branches before an all-`n` conjecture is credible, and target
fibres are simultaneous transformation-word equations.  The exact word was
not found in the bounded search, but changing the asymmetric sandwich word
does not escape the generic full-transformation-semigroup engine or the
same-batch `NL07/NL08` sandwich-map kill.  `KILL_WORD_MAP_NO_SPINE`.

## 5. `LHF`: leftmost horizontal domino flip

A tiling of `2 x n` has a unique Fibonacci-word encoding by tokens
`V` (one vertical domino, width one) and `H` (a stacked pair of horizontal
dominoes, width two).  Define `F` by flipping the leftmost `H` block into
`VV`; hold the all-vertical tiling.

If the source contains `k` horizontal blocks, then

```text
F^t replaces its first min(t,k) H tokens by VV,
depth(source)=k,
global height=floor(n/2).                              (7)
```

The unique recurrent state is `V^n`, and `H^{floor(n/2)}` (with a final `V`
when needed) is sharp.

There is also a complete target atlas.  Let `Y` be a target and `t>=0`.
If `Y` contains an `H`, let `L(Y)` be the number of leading `V` tokens before
its first `H`.  Then

```text
|{X:F^t(X)=Y}| = binom(L(Y)-t,t) if L(Y)>=2t,
                  0                    otherwise.      (8)
```

Indeed the source prefix is a width-`L(Y)` Fibonacci tiling with exactly `t`
horizontal blocks.  If `Y=V^n`, then

```text
|{X:F^t(X)=V^n}|
   = sum_{0<=j<=min(t,floor(n/2))} binom(n-j,j).        (9)
```

Equations (7)--(9) include `t=0`, `n=0,1`, and post-cap times.  They were
checked for every target, every relevant time, and all `0<=n<=16`.

This is the strongest raw result and still a kill.  The Fibonacci encoding
removes all tiling geometry: the operation simply selects and erases the
leftmost `H` coordinate at each time.  The same leftmost-selector temporal
and inverse engine is permanently occupied by P144/P149 and the selector
kill ledger; the classical local domino flip supplies no independent axis.
`KILL_INTERNAL_SELECTOR_TRANSFER`.

## 6. `MGC`: matroid greedy-circuit deletion

Let `M` be a matroid on a totally ordered ground set `E`.  For a dependent
subset `A`, choose the lexicographically first circuit `C subset A` and delete
`max C`; fix independent subsets.  Call the resulting map `K_M`.

Deleting an element of a contained circuit preserves rank and lowers size by
one.  Therefore

```text
depth(A)=|A|-r_M(A),
max depth=|E|-r_M(E),                                  (10)
```

and the recurrent set is exactly the independence complex.  The verifier
checks (10) on the triangle, a square with a diagonal, the graphic matroid of
`K4`, and the Fano matroid.

This is not a fresh dynamics package.  Its terminal state is the ordered
greedy basis of the restriction `M|A`; grouping sources by terminal basis is
the classical Boolean-interval/activity decomposition behind the Tutte
polynomial.  The scheduler changes the path, not the nullity clock or the
owned inverse partition.  Internal `GBD`, `MA1`, and `GG05` already reject
matroid greedy/minor dynamics.  `KILL_DIRECT_GREEDY_ENGINE`.

## 7. Exact-control scope and conclusion

`verify_scout.py` independently constructs permutation groups, finite
quadratic congruences, binary unitriangular inverses, full transformation
monoids, every Fibonacci tiling, and four represented binary matroids.  It
checks 123,632 statements and freezes complete transition SHA-256 signatures.
Two fresh executions are byte-identical.

The only candidate with two closed raw axes is `LHF`, whose entire proof
transfers through a forbidden leftmost selector.  `IHI` has the only unusual
unsubtracted early signal but lacks a second theorem axis.  No owner-thin
candidate remains:

```text
ROUND7 KILL_ALL
HOLD_EXTERNAL
```

