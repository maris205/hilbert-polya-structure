# Root-coordinator theorem spikes

These are promotion candidates, not frozen paper contracts.

## RC01 — cyclic divisor-quotient dynamics

Let `N=prod_p p^{a_p}`, `m>=2`, and

```text
Q_N(x)_i = x_i/gcd(x_i,x_{i+1})              (indices modulo m).
```

Under each valuation, `Q_N` is the positive cyclic difference
`D(e)_i=(e_i-e_{i+1})_+`.  The proposed temporal theorem is that every orbit
is fixed by time `max_p a_p` for `m>=3` (by time one for `m=2`), with sharpness
witnessed primewise; recurrence is exactly the fixed locus.  A valuation word
is fixed precisely when its positive support is independent in `C_m`, so the
fixed-state census is

```text
prod_{p|N} I(C_m,a_p),
```

where positive heights give vertex weight `a_p`.  Independently, for every
labelled target `y`, the one-step fibre factors over primes and is the trace of
a product of explicit `(a_p+1)`-square `0/1` transfer matrices indexed by the
target valuations.

Proof route: after one step, every surviving height-`h` coordinate is either
strictly below `h` or is an isolated frozen `h`-peak bordered by zeros; delete
the frozen peaks and induct on `h`.  Matrix trace is a cyclic local-constraint
sum.  Boundary obligations: `N=1`, `m=1`, `m=2`, prime powers, repeated
maxima, and zero targets.  P97, P128, P142, P158, P162, P184, and P186 share
generic arithmetic/support vocabulary but not this literal update plus
positive-difference clock and fibre matrices.

## RC03 — self-cardinality truncation

For `A subseteq [n]`, put `T(A)=A intersect [|A|]`.  With
`r_A(k)=|A intersect [k]|`, set `k_0=|A|` and
`k_{t+1}=r_A(k_t)`.  The proposed closed iterate is

```text
T^t(A)=A intersect [k_{t-1}]  (t>=1).
```

The endpoint is `[rho(A)]`, where `rho(A)` is the length of the initial
segment contained in `A`; all recurrence is fixed.  The maximum tail is
`n-1` for `n>=2`, uniquely attained by `{2,...,n}`.  The terminal fibre of
`[r]` has size `2^{n-r-1}` for `r<n` and size one for `r=n`.

For a labelled target `B`, `b=|B|`, `M=max(B)` with `M=0` for the empty set,
the independent inverse theorem is

```text
|T^{-1}(B)| = sum_{k=max(b,M)}^{floor((n+b)/2)} binom(n-k,k-b).
```

This also characterizes the exact first image.  Proof route: source size `k`
forces all non-target source points into `{k+1,...,n}`; temporal claims reduce
to the monotone rank iteration.  Boundary obligations: `n=0,1`, empty/full
targets, initial segments, and the unique deepest state.  P165, P185, and P186
must be subtracted at literal-update and sufficient-statistic level rather
than by carrier name alone.

## RC05 — left-stabilizer subset dynamics — historical collision, killed

For a finite group `G` and `A subseteq G`, define

```text
S(A)={g in G:gA=A}.
```

Then `S(A)` is a subgroup and `S(H)=H` for every subgroup `H`, so `S^2=S`,
the image equals the fixed locus, and both equal the subgroup lattice.  For
every `H<=G`, the labelled target fibre is proposed as

```text
|S^{-1}(H)| = sum_{K>=H} mu_G(H,K) 2^{[G:K]},
```

with the empty set included in the `G` fibre.  The formula follows by
Möbius inversion because an `H`-invariant subset is a union of left
`H`-cosets.  Further specializations to cyclic groups recover exact minimal
period counts and therefore receive zero credit where classical.

This spike is retained only as negative evidence.  The identical literal map
was A13 in the P172–P176 algebra scout and was killed there as a shallow static
stabilizer invariant with the same divisor-Möbius/necklace inverse axis.  A
nonabelian example does not supply a new proof engine.  RC05 therefore cannot
be promoted in this batch.
