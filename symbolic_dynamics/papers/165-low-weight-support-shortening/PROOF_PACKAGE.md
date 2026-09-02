# P165 proof package

## Status

`PROVABLE AS STATED / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Claim and assumptions

Fix a prime power `q`, `n>=0`, and labelled subspaces of `F_q^n`.  For a
nonzero code `C`, let `d(C)` be its minimum Hamming weight, let `U(C)` be the
union of supports of all nonzero words of weight strictly less than
`2d(C)`, and let `T(C)` be the subcode zero on `U(C)`.  Put `T(0)=0`.

The package proves exactly the temporal, nonzero-target image, lower-bound,
and simultaneous-extremizer statements in Theorem 1 of `main.tex`.  It does
not prove or assert a complete fibre enumeration.

## Dependency map

1. Proper descent and distance doubling use the literal purge definition.
2. Pairwise-disjoint purge sets plus doubling give the support budget.
3. The budget gives termination and the upper height bound; dyadic lines give
   equality.
4. Iterated doubling and the budget give necessity of the image conditions.
5. A direct sum with dyadic full-support lines gives sufficiency.
6. Equality in the dimension/support budgets forces one pure line at each
   stage, giving classification and counting.

## Detailed proof

Let `C_i=T^i(C)`.  While `C_i` is nonzero, write `d_i=d(C_i)` and
`U_i=U(C_i)`.

### Step 1: properness and distance doubling

A minimum word of `C_i` has weight `d_i<2d_i`, so its support contributes to
`U_i` and it is absent from `C_(i+1)`.  Thus the inclusion is proper.  If a
nonzero survivor had weight below `2d_i`, it would belong to the low-word
set, but it is zero on the union of that set's supports.  This is impossible.
Therefore `d_(i+1)>=2d_i` whenever the successor is nonzero.

### Step 2: purge budget

Every later code is zero on every earlier `U_i`; hence the purge sets are
pairwise disjoint.  A minimum word at time `i` has `d_i` coordinates inside
`U_i`, and Step 1 gives `d_i>=2^i d_0>=2^i`.  Therefore
`|U_i|>=d_i>=2^i`.

### Step 3: clock and sharpness

Depth `r` requires nonzero stages `0,...,r-1`, so disjointness yields
`n>=sum_(i<r)2^i=2^r-1`.  Hence `r<=floor(log2(n+1))` and every orbit reaches
zero.  The direct sum of full-support lines on disjoint blocks of sizes
`1,2,...,2^(r-1)` loses exactly one block per step, attaining the bound for
`r=floor(log2(n+1))`.  For `n=0`, `r=0` and the construction is empty.

### Step 4: all-time image necessity

If `T^t(C)=D!=0`, every intermediate state is nonzero.  Thus
`d(D)>=2^t d(C)>=2^t`.  All `U_i` are zero coordinates of `D`, so
`z(D)>=sum_(i<t)|U_i|>=2^t-1`.

### Step 5: all-time image sufficiency

Assume `d(D)>=2^t` and `z(D)>=2^t-1`.  Choose disjoint target-zero blocks
`B_i` of size `2^i`, full-support lines `M_i` on them, and set
`C=D direct_sum M_0 direct_sum ... direct_sum M_(t-1)`.  At stage `i`, the
distance is `2^i`.  Exactly the nonzero words in `M_i` have weight below
`2^(i+1)`: later lines and target words meet the threshold, while disjoint
supports forbid cancellation.  Hence `U_i=B_i`, and after `t` steps the code
is `D`.

### Step 6: universal inverse lower bounds

Every step before the nonzero target has codimension at least one, giving
`dim(C)-dim(D)>=t`.  The disjoint purge sets are contained in
`Supp(C)\Supp(D)`, giving at least `sum_(i<t)2^i=2^t-1` new supported sites.

### Step 7: equality classification

If both totals are equalities, every codimension is one and every inequality
`|U_i|>=d_i>=2^i` is equality.  Let `w_i` be a minimum word of `C_i`.  Its
support is contained in `U_i` and both have size `2^i`, so
`supp(w_i)=U_i`.  In particular, `w_i` is a pure word on the purge block;
it is not merely a coset lift that could cancel against later coordinates.
Restriction to `U_i` has kernel `C_(i+1)` and one-dimensional image, whence
`C_i=C_(i+1) direct_sum span(w_i)`.  Descending induction produces exactly
the dyadic direct-sum form.

### Step 8: count

The ordered labelled block count is
`z(D)!/((z(D)-s_t)! product_(i<t)(2^i)!)`.  A block of size `m` has
`(q-1)^(m-1)` full-support lines.  Multiplication gives the exponent
`sum_(i<t)(2^i-1)=s_t-t`.

## Boundary verification

- `t=0`: no blocks, one source `D`, and both lower bounds are zero.
- `D=0`: it is always reachable, but the complete fibre is
  `{C:tau(C)<=t}`.  The block formula applies only to simultaneous minimizers
  in the exact-depth-`t` shell.
- `n=0`: only zero exists and the height is zero.
- Full-support nonzero `D`: no positive-time source because `z(D)=0`.
- `2^t-1>n`: no nonzero time-`t` target.
- The threshold is `<2d`, not `<=2d`.
- All linear-algebra steps work over every finite field, including nonprime
  prime powers.

## Ownership boundary and open risk

The one-step hitting-set shortening principle receives zero contribution
credit.  The remaining risk is direct ownership of the autonomous iteration,
the exact target criterion, or the extremal layer.  The bounded non-hit in
`SOURCE_VERIFICATION.md` is not novelty evidence.
