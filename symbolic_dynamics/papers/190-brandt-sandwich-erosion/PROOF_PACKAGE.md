# Proof package — P190 Round 0

## Claim

For every `n,m>=1`, the cyclic Brandt map `T(x)_i=x_i x_(i+1)x_i` has the
stated all-time good-run normal form, exact fixed and tail classification,
every-target matrix/gap fibre formula, all-zero spectrum, image criterion, and
fibre-mass identity.

## Status

`PROVABLE AS STATED`

## Assumptions

- `B_n={0} union [n]^2` with matrix-unit multiplication.
- Indices on words of length `m` are read modulo `m`.
- `n,m` are positive integers; no generic case silently excludes `n=1` or
  `m=1,2`.
- Matrices act on column vectors, and `M_y(u,v)=1[u v u=y]`; thus rows are
  current source letters and columns are next source letters.

## Notation

- `u*=(b,a)` for `u=(a,b)` and `0*=0`.
- `g_i=1[x_i!=0 and x_(i+1)=x_i*]`.
- `L(x)` is the longest cyclic run of good edges for a non-all-good word.
- `M_y` is the local output matrix and `A=M_0`.
- `r=n^2` and `q=r+1=|B_n|`.

## Proof strategy

Induct directly on time for the temporal axis.  For the inverse axis, expand
a matrix trace as a cyclic source path, then use the rank-one support of every
nonzero output matrix to pin anchors.  Diagonalize the remaining zero-output
matrix through the inversion permutation on matrix units.

## Dependency map

1. Local multiplication gives `u v u=u` iff `u!=0` and `v=u*`.
2. The local filter plus induction proves the all-time normal form.
3. Time one classifies fixed words.
4. The disappearance time of the longest good run gives every tail and the
   parity obstruction gives the sharp maximum.
5. Cyclic trace expansion gives every labelled fibre.
6. Nonzero output matrices pin adjacent source letters and give the gap
   product.
7. The inversion eigenspaces of `A` give its characteristic factors and the
   zero-target recurrence.
8. Positivity patterns of `A^h` give the image criterion.
9. Summing all output matrices gives the all-ones matrix and mass conservation.

## Proof

### Step 1: local filter

If `u=0`, then `u v u=0`.  For `u=(a,b)` and `v=(c,d)`, the first product is
nonzero exactly when `b=c`, and multiplying it by `u` is then nonzero exactly
when `d=a`.  These two conditions say `v=(b,a)=u*`, and the output is `u`.

### Step 2: all-time normal form

At time zero the coordinate is `x_i`, matching the empty good-edge product.
Assume the formula at time `t`.  The next local output at `i` is nonzero only
if the time-`t` values at `i` and `i+1` survive and are inverses.  By the
induction hypothesis, survival requires the good edges from `i` through
`i+t-1` and from `i+1` through `i+t`; their union is the block from `i`
through `i+t`.  The first edge already states the needed inverse relation.
The output then remains `x_i`.  This proves the formula at `t+1`.

### Step 3: fixed points

If a fixed word has one nonzero letter, the local filter forces its successor
to be its inverse.  Repeating around the cycle makes every letter nonzero and
alternating.  Odd length forces the initial unit to equal its inverse, giving
`n` diagonal choices; even length permits all `n^2` units.  The all-zero word
adds one fixed point.

### Step 4: pointwise and sharp tails

For a nonfixed word, the normal form says a coordinate survives time `t`
exactly when a length-`t` cyclic good run starts there.  A longest run of
length `L` therefore leaves a nonzero coordinate at time `L`, while time
`L+1` is all zero.  The tail is exactly `L+1`.

When `n>=2` and `m` is odd, alternate an off-diagonal unit along `m-1` good
edges; only the closing edge is bad, so `L=m-1`.  When `m` is even, exactly
one bad edge is impossible: traversing the other odd number of inverse steps
forces the omitted edge to be good.  Two adjacent bad edges are realized by
alternating an off-diagonal unit for `m-2` edges and repeating it once, so
`L=m-2`.  For `n=1`, good edges are precisely adjacent pairs of the unique
nonzero idempotent.  A mixed word has maximum good-run length `m-2`, realized
by one zero and `m-1` nonzero letters; `m=1` has only fixed words.

### Step 5: every-target trace

Expand `tr(M_(y_0)...M_(y_(m-1)))`.  Each summand is indexed by a cyclic
sequence `u_0,...,u_(m-1)` and equals one exactly when
`u_i u_(i+1)u_i=y_i` at every site.  Such cyclic sequences are exactly the
source words in the labelled fibre of `y`.  The row/column direction is fixed
by `M_y(u_i,u_(i+1))`.

### Step 6: nonzero anchors

For nonzero `y`, `M_y` has its unique one at `(y,y*)`.  Hence every nonzero
target site pins the adjacent source pair to `(y,y*)`.  Between consecutive
nonzero anchors, each zero target contributes one factor `A`; multiplying the
corresponding matrix entries over all cyclic gaps gives the stated product.

### Step 7: zero-target spectrum

Let `P` invert the `r` nonzero matrix units.  On the unit-coordinate subspace
of coefficient sum zero, `A=-P`.  Inversion has `n` fixed units and
`(r-n)/2` transposed pairs, so its `+1` and `-1` multiplicities are
`(r+n)/2` and `(r-n)/2`.  Removing the all-unit sum leaves eigenvalue `-1`
for `A` with multiplicity `(r+n)/2-1`; eigenvalue `+1` has multiplicity
`(r-n)/2`.

On the complementary span of `e_0` and the all-unit vector `w`,
`A e_0=e_0+w` and `A w=r e_0+(r-1)w`.  The representing matrix has trace `r`
and determinant `-1`, hence characteristic polynomial `z^2-rz-1`.  The power
sum of its roots has initial values `2,r` and recurrence
`s_m=r s_(m-1)+s_(m-2)`.  Adding all eigenvalue powers gives the claimed
trace of `A^m`.

### Step 8: image criterion

The gap product is positive precisely according to entries of `A^h`.  For
`h=0`, the identity matrix requires the next anchor to be the inverse of the
previous one.  For `h=1`, the entry from `y*` to `z` vanishes exactly when
`z=y`.  For every `h>=2`, a length-`h` path can go from any letter to zero,
remain at zero, and then go to any letter, so every entry is positive.  The
all-zero target is hit by the all-zero source.

### Step 9: mass conservation

Every ordered source-letter pair has exactly one output, so `sum_y M_y=J_q`.
Summing the trace formula over all targets yields `tr(J_q^m)=q^m`, because
`J_q^m=q^(m-1)J_q` for `m>=1`.

Therefore every claim follows. ∎

## Corrections or Missing Assumptions

None.  The `n=1` sharp-tail formula is necessarily separate from `n>=2`
because no off-diagonal matrix unit exists.

## Open Risks

- External ownership of the literal update and theorem conjunction has only a
  bounded search, so `OWNER_AMBER / HOLD_EXTERNAL` remains mandatory.
- Generic run erosion, Brandt identities, sandwich terminology, and de Bruijn
  matrices are background, not contribution claims.

