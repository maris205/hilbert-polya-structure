# Narrative report

## Core story

Fix a prime `p`.  For a finite abelian `p`-group `G`, feed its current
generator rank back into the ordinary image/kernel decomposition of
multiplication by a power of `p`:

```text
F(G) = p^d(G) G direct_sum G[p^d(G)].
```

The group classification turns `G` into a partition
`lambda=(a_1,...,a_r)`, where `r=d(G)`.  A cyclic factor of exponent `a<=r`
survives unchanged; a factor with `a>r` splits into exponents `r` and `a-r`.
That reduction is elementary and receives no contribution credit.  The
paper's residual story is what the state-dependent rank feedback forces
globally and inversely.

## Proof spine

1. Multiplication by `p^r` has image exponent `max(a-r,0)` and kernel
   exponent `min(a,r)` on `C_(p^a)`.  The exact sequence gives order
   preservation and the partition rule.
2. If `c` parts exceed the current rank `r`, then the next rank is `r+c`.
   Hence every nonfixed step strictly raises rank.  All recurrent states are
   therefore fixed, exactly when the largest part is at most the length.
3. A fixed partition of length `r`, after subtracting one from each part, is
   a Ferrers diagram in an `r` by `(r-1)` rectangle.  This gives the fixed
   OGF by a Gaussian polynomial.
4. Tag each initial part.  Whenever a residual part splits at time `t`, its
   new part `r_t` is a permanent marker: every later rank is larger.  If
   `c_t` parts split, the final state contains `c_t` disjoint markers of
   weight `r_t`, plus one positive residual per initial tag.  Thus

   ```text
   n >= r_0 + sum_t c_t r_t
     >= r_0(d+1) + binom(d,2).
   ```

   This yields the triangular upper bound.  The cyclic type follows the
   explicit orbit `sort(n-T_t,t,...,1)` and attains it.  If `r_0>=2`, the
   pointwise budget already exceeds the next triangular threshold, proving
   uniqueness of `(n)`.
5. For a target of length `L`, a source rank `r` would have made `c=L-r`
   splits.  Remove `c` target copies of the marker `r`.  Every remaining
   part above `r` is forced to be a split remainder; choose the other
   remainders among multiplicities at most `r`.  A bounded product records
   exactly those choices and the same reconstruction gives the image
   criterion.

## Why the strongest result is not merely classification

The classification of finite abelian `p`-groups and the types of `p^rG` and
`G[p^r]` are fully owned background.  With a fixed `r`, they contain no
dynamics.  The nontrivial mechanism is that `r` is recomputed after every
split.  That feedback makes marker sizes strictly increase, creates the
pointwise triangular budget, and makes the deepest source unique.  The same
state dependence is what forces the rank-indexed sum in the every-target
fibre formula.

## Internal collision boundary

- P126 uses ordered compositions and a synchronous nearly-halving split at
  a fixed threshold.  Its main theorem is an all-iterate kernel/image code.
  P137 uses unordered `p`-group types, subtraction by a changing rank, a
  triangular clock, and one-step target fibres.
- P135 is a multiplicity-threshold orbit-partition map derived from
  permutation centralizers.  It includes mergers and two-cycles.  P137 is
  split-only and all recurrence is fixed.
- P115 is a linear Cartier/Frobenius coefficient operator.  P137 has no
  finite-field coefficient shift, additive-polynomial lane, or rank-nullity
  functional graph.

Sharing partitions, splitting language, or a finite algebraic carrier is not
a theorem collision.

## Evidence and limitations

The dependency-free verifier uses exact Python integers and tuples.  It
checks 18,504,770 assertions: literal cyclic kernels/images, all partition
states through weight 50, 51 fixed-OGF coefficients, and all target fibres
through weight 35.  At weight 50 there are 204,226 states, 106,864 fixed
states, 120,872 image targets, maximum one-step fibre 31, and unique maximum
entry time 9 at `(50)`.

These finite controls can refute formulas but cannot prove the all-weight
theorems or certify ownership.  A bounded source-audit non-hit is not novelty
or priority evidence.  External release remains `HOLD_EXTERNAL`.
