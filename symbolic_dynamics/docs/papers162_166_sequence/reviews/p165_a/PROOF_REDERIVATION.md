# Independent proof re-derivation for P165

## Claim

Let `q` be a prime power and let the state space be the labelled linear
subspaces of `F_q^n`.  For a nonzero code `C`, put

```text
d(C) = min{wt(c): 0 != c in C},
L(C) = {c in C: 0 < wt(c) < 2d(C)},
U(C) = union_{c in L(C)} supp(c),
T(C) = {c in C: c|_{U(C)}=0},
```

with `T(0)=0`.  Writing `s_t=2^t-1`, the manuscript claims:

1. every nonzero step is a strict subcode step, a nonzero survivor has
   minimum distance at least twice the old distance, zero is the unique
   recurrent state, and the maximum absorption time is
   `floor(log_2(n+1))`;
2. for `D != 0`, `D` belongs to `im(T^t)` exactly when
   `d(D)>=2^t` and `z(D)>=s_t`;
3. every source of such a target adds at least `t` dimensions and at least
   `s_t` support coordinates; simultaneous equality occurs exactly by
   adjoining full-support lines on pairwise disjoint labelled blocks of
   sizes `1,2,4,...,2^(t-1)`, and the number of sources is

   ```text
   z(D)! / ((z(D)-s_t)! product_{i=0}^{t-1}(2^i)!)
       * (q-1)^(s_t-t).
   ```

The boundary assertions concern `D=0`, `t=0`, `n=0`, full-support targets,
the post-cap time range, and the necessity of the strict cutoff.

## Status

**PROVED AS STATED.**  Independent re-derivation found no missing hypothesis
and no false boundary.  The direct one-step low-weight shortening mechanism
is treated as owned background and receives zero contribution credit; that
ownership issue does not affect the validity of the residual theorems.

## Assumptions

- `q` is a prime power, so `F_q` is a field.
- Coordinates are labelled and are retained after shortening; deleted
  coordinates are padded by zero.
- Minimum distance is used only for nonzero codes.
- Support means the union of supports of all codewords.
- Sources are subspaces, not generator matrices or equivalence classes.
- The cutoff in `L(C)` is strictly `<2d(C)`.

No primality assumption on `q`, binary-only argument, efficient
minimum-distance oracle, or full-fibre enumeration is used.

## Notation

For a fixed source `C`, write

```text
C_i = T^i(C),  d_i=d(C_i),  U_i=U(C_i)
```

as long as `C_i` is nonzero.  Let `rho_i:C_i -> F_q^{U_i}` be coordinate
restriction.  Then `C_{i+1}=ker(rho_i)`.  Let `Supp(C)` be full code support,
`z(C)=n-|Supp(C)|`, and `tau(C)=min{t:T^t(C)=0}`.

## Proof Strategy

The key observation is not an abstract finite-map argument but an exact
restriction-kernel budget.  A minimum word is always purged, so every
nonzero step loses dimension.  A surviving word below twice the old
distance would simultaneously be supported inside the purge union and
zero on that union, which is impossible.  Successive purge supports are
therefore disjoint and have geometrically growing sizes.

That budget gives the sharp clock and the necessity of the image criterion.
For sufficiency, one adjoins disjoint full-support lines with dyadic support
sizes.  Equality in both inverse bounds forces equality in every inequality
of the budget, so each quotient is precisely one of those lines.  The
count then separates into an ordered block count and a full-support line
count.

## Dependency Map

```text
restriction-kernel lemma
  |-- strict descent
  |-- distance doubling
  `-- disjoint purge supports
          |-- geometric support budget
          |     |-- sharp height upper bound
          |     |-- target image necessity
          |     `-- inverse support lower bound
          |-- dyadic block construction
          |     |-- sharp height witness
          |     `-- target image sufficiency
          `-- equality in every budget inequality
                |-- full-support line decomposition
                `-- exact labelled source count
```

The boundary results are direct specializations of this chain, except for
the weak-cutoff sentinel, which uses the first two dyadic blocks.

## Proof

### 1. Strict descent and distance doubling

Let `C_i != 0`.  Choose a minimum word `w_i`.  Since
`0<wt(w_i)=d_i<2d_i`, its support lies in `U_i`, while a survivor is zero on
`U_i`.  Thus `w_i` does not survive and
`C_{i+1}=ker(rho_i)` is a proper subspace of `C_i`.

Now suppose `C_{i+1} != 0` and take `0 != v in C_{i+1}`.  If
`wt(v)<2d_i`, then `v in L(C_i)`, hence `supp(v) subset U_i`.  But membership
in `C_{i+1}` says that `v` is zero on `U_i`, a contradiction.  Therefore

```text
d_{i+1} >= 2d_i.
```

Every later code is contained in `C_{i+1}` and is zero on `U_i`; hence every
later purge support is disjoint from `U_i`.  Also the minimum word has
support of size `d_i` inside `U_i`.  Inductively,

```text
|U_i| >= d_i >= 2^i d_0 >= 2^i.
```

### 2. Unique recurrence and sharp height

If `tau(C)=r`, then `C_0,...,C_{r-1}` are nonzero, so disjointness and the
last display give

```text
n >= sum_{i=0}^{r-1}|U_i| >= sum_{i=0}^{r-1}2^i = 2^r-1.
```

Thus `r<=floor(log_2(n+1))`.  Strict containment at every nonzero state
excludes every nonzero periodic orbit, so zero is the unique recurrent
state.

For sharpness, let `r=floor(log_2(n+1))`, choose disjoint coordinate blocks
`B_i` of sizes `2^i`, and let `M_i` be any full-support line on `B_i`.
Take `C=M_0 direct-sum ... direct-sum M_{r-1}`.  Disjoint supports make
weights additive.  At stage `i`, the only nonzero words of weight strictly
below `2^(i+1)` are the nonzero words in `M_i`; later lines have weight at
least `2^(i+1)`.  Thus the blocks disappear in order and `tau(C)=r`.  For
`r=0` the empty direct sum is zero.

### 3. Every-time nonzero images

Suppose `T^t(C)=D != 0`.  Every intermediate state is nonzero.  Repeated
doubling yields `d(D)>=2^t d(C)>=2^t`.  The disjoint sets
`U_0,...,U_{t-1}` are all zero coordinates of `D`, so

```text
z(D) >= sum_i |U_i| >= 2^t-1.
```

This proves necessity.

Conversely assume `d(D)>=2^t` and `z(D)>=2^t-1`.  In zero coordinates of
`D`, choose disjoint blocks `B_i` with `|B_i|=2^i`, and choose a
full-support line `M_i` on each block.  Put

```text
C = D direct-sum M_0 direct-sum ... direct-sum M_{t-1}.
```

At stage `i` the current code is
`D direct-sum M_i direct-sum ... direct-sum M_{t-1}` and has distance
`2^i`.  A later line has weight at least `2^(i+1)`, a nonzero target word
has weight at least `2^t`, and disjoint-support components cannot cancel.
Consequently the words below the strict threshold `2^(i+1)` are exactly
the nonzero words of `M_i`.  The next shortening removes precisely `M_i`,
and after `t` steps the state is `D`.

### 4. The two inverse lower bounds

For `T^t(C)=D != 0`, each of the `t` inclusions
`C_i supersetneq C_{i+1}` has positive codimension.  Therefore
`dim(C)-dim(D)>=t`.  Moreover, every `U_i` is contained in `Supp(C)` and is
zero for all of `D`; disjointness and the budget imply

```text
|Supp(C) setminus Supp(D)| >= sum_i |U_i| >= 2^t-1.
```

### 5. Necessity of the dyadic equality structure

Assume equality in both bounds.  The codimension sum equals `t`, so every
transition has codimension one.  The support difference has size
`s_t`, contains the disjoint union of the `U_i`, and
`|U_i|>=d_i>=2^i`; equality of the total forces, term by term,

```text
|U_i|=d_i=2^i.
```

Choose a minimum word `w_i in C_i`.  Its support is contained in `U_i` and
both have size `2^i`, so `supp(w_i)=U_i`.  Since
`C_{i+1}=ker(rho_i)` has codimension one and `w_i` is not in the kernel,

```text
C_i = C_{i+1} direct-sum span(w_i).
```

The line `span(w_i)` is full-support on the dyadic purge block `U_i`.
Iterating this decomposition down to `C_t=D` gives exactly the stated
source form.  The construction in the preceding subsection proves the
converse.

### 6. Exact count for every prime power

The dynamic purge supports make the ordered blocks intrinsic to a source,
so the parameterization has no hidden overcount.  From `z=z(D)` labelled
zero coordinates, the number of ordered disjoint blocks of sizes
`2^0,...,2^(t-1)` is

```text
z! / ((z-s_t)! product_i (2^i)!).
```

On a labelled block of size `m`, there are `(q-1)^m` full-support vectors,
and each one-dimensional subspace has exactly `q-1` nonzero
representatives.  Hence there are `(q-1)^(m-1)` full-support lines.  The
product over all blocks is `(q-1)^(s_t-t)`, proving the formula for every
prime power, including nonprime `q`.

### 7. Boundary cases

- `n=0`: the only subspace is zero and the height is zero.
- `t=0`, `D!=0`: the image criterion is tautological; the simultaneous
  extremal source is uniquely `D`, and the empty-product count is one.
- `D=0`: the full fibre is exactly `{C:tau(C)<=t}`.  For exact depth
  `t>=1`, the same stepwise proof with terminal code zero gives minimum
  dimension `t`, minimum support `s_t`, the same block classification, and
  the displayed count with `z(D)` replaced by `n`.
- Full-support `D!=0`: `z(D)=0`, so no positive-time preimage exists.
- If `s_t>n`, the positive part of `im(T^t)` is empty, while zero remains.
- Strict cutoff: on disjoint blocks of sizes one and two, the strict map
  removes only the first line at time one; replacing `<2d` by `<=2d`
  removes the second block too.  Thus the strict convention is essential.

## Corrections or Missing Assumptions

None.  No executable source repair is required after this review.

## Open Risks

- The bounded owner search cannot establish novelty.  A direct source for
  the literal autonomous map, the every-time image equivalence, or the
  simultaneous extremal inverse count would reopen the ownership gate.
- The residual is deliberately narrower than a complete fibre theorem.
  The manuscript correctly states that it counts only the simultaneous
  minimum-dimension/minimum-support layer.
- Evaluating the map requires minimum-distance information, which is
  computationally hard in general; no algorithmic efficiency is claimed.
- The artifact must remain `HOLD_EXTERNAL` until the full review sequence
  and central lifecycle gates close.
