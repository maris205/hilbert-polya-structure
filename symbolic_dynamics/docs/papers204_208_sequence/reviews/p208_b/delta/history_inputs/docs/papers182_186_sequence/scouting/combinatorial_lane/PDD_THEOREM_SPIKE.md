# `PDD`: prefix-diversity delay theorem spike

**Status:** `FROZEN_INTERNAL_CANDIDATE / HOLD_EXTERNAL`  
**Carrier:** `W_n=[n]^n`, with positions and letters numbered `0,...,n-1`

## Literal map

For `w=(w_0,...,w_(n-1))`, define

```text
(P w)_i = |{w_0,...,w_(i-1)}|,
```

where the empty prefix gives `(Pw)_0=0`.  The output lies in `[n]^n`, so this
is a literal finite self-map without totalisation.

## Theorem package

Put `d=P(w)` and `r=t-1`.  For every `t>=1`,

```text
(P^t w)_i = i                     if i<r,
             r+d_(i-r)             if i>=r.                 (1)
```

Consequently, for `1<=t<=n-1`:

1. `im(P^t)` is exactly the set of words `y` satisfying
   `y_i=i` for `0<=i<=t` and `y_i-y_(i-1) in {0,1}` thereafter.  Hence
   `|im(P^t)|=2^(n-t-1)`.
2. The identity word `e=(0,1,...,n-1)` is the unique recurrent state and
   unique fixed point; `P^(n-1)` is constant with value `e`.
3. If `rho(w)` is the length of the longest all-distinct prefix of `w`, then

   ```text
   tau(w)=0                         if w=e,
          max(1,n-rho(w))           otherwise.               (2)
   ```

   Thus the sharp global height is `n-1` for `n>=2`.
4. For `1<=t<=n-1`, the exact depth CDF is

   ```text
   #{w:tau(w)<=t} = (n)_(n-t) n^t.                           (3)
   ```

5. Every nonempty time-`t` fibre has a target-local product.  Recover the
   visible prefix of `d` from a target `y` by

   ```text
   d_j = y_(j+t-1)-(t-1),       0<=j<=n-t.
   ```

   Start with `k=1`.  For `j=1,...,n-t-1`, put
   `epsilon_j=d_(j+1)-d_j`; multiply by `n-k` and increment `k` when
   `epsilon_j=1`, and multiply by `k` when `epsilon_j=0`.  Including the
   first and invisible letters gives

   ```text
   |(P^t)^-1(y)| = n^(t+1)
                    product_(epsilon_j=1)(n-k_j)
                    product_(epsilon_j=0) k_j,                (4)
   ```

   where `k_j=1+sum_(h<j)epsilon_h`.  Targets outside the image have fibre
   zero.

## Proof

The first image satisfies `d_0=0`, `d_1=1`, and
`d_i-d_(i-1) in {0,1}` for `i>=2`: the difference records whether
`w_(i-1)` is new.  Conversely every such binary-rise path is realized by
choosing a fresh letter at rises and an old letter at flats; the last source
letter is invisible.

If `d` is such a path, its prefix through position `i-1` contains every
integer from `0` through `d_(i-1)`.  Therefore

```text
(Pd)_0=0,                 (Pd)_i=d_(i-1)+1  (i>=1).
```

Induction gives (1), and (1) immediately gives the image description and
constant time `n-1`.  It also shows `P^t(w)=e` precisely when the first
`n-t` source letters are distinct.  Taking the least admissible `t`, with
the exceptional already-fixed word separated, proves (2).  There are
`(n)_(n-t)` injective prefixes of length `n-t` and `n^t` arbitrary suffixes,
which proves (3).

Finally, the target exposes exactly the novelty decisions for source
positions `1,...,n-t-1`.  The first source letter has `n` choices.  With `k`
letters already seen, a rise has `n-k` choices and a flat has `k`; the final
`t` source positions are invisible and contribute `n^t`.  This is (4), and
also proves fibre-mass conservation without using the forward enumeration.

## Exact control

[`verify_combinatorial_lane.py`](verify_combinatorial_lane.py) checks (1)--(4)
target by target for all `n^n` states through `n=7`.  The PDD block alone
makes **8,682,903 assertions**.  At `n=7` the exact depth histogram is

```text
0:1, 1:35279, 2:88200, 3:164640, 4:216090, 5:201684, 6:117649.
```

## Residual and kill switch

Restricted-growth words, first-occurrence patterns, falling factorials, and
prefix statistics are zero-credit background.  The retained residual is the
literal iteration together with (1)--(4).  A source stating that conjunction,
or an internal proof transfer that supplies it by routine renaming, kills or
subtracts the candidate.  The present search is bounded and grants no
external release status.

