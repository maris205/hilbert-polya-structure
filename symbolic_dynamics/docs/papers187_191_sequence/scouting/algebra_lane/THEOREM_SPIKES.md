# Algebra-lane theorem spikes — survivors only

These are unnumbered proof contracts, not manuscripts.  “Contract” means a
specific statement to attack next; it does not mean proved, novel, owned, or
externally ready.  Finite controls are not used as proof.

## A01 — nilpotent last-nonzero selector

Let `V` be a positive-dimensional vector space over `F_q`, let `N` be
nilpotent with Jordan block lengths `lambda_1,...,lambda_b`, and define

`h(v)=min{h>=1:N^h v=0}`, `T(0)=0`, and
`T(v)=N^(h(v)-1)v` for `v!=0`.

### All-parameter contract

1. `T(V)=ker N`, `T^2=T`, every recurrent state is fixed, the depth is zero
   on `ker N` and one outside it, and the functional-graph transition matrix
   has characteristic polynomial
   `z^(q^dim(V)-q^b)(z-1)^(q^b)`.
2. Choose bottom vectors `e_i` for the Jordan blocks and write a nonzero
   `y in ker N` as `sum y_i e_i`.  Put
   `L(y)=min{lambda_i:y_i!=0}` and
   `D(h)=sum_i min(h-1,lambda_i)`.  Then

   `|T^{-1}(0)|=1`, and
   `|T^{-1}(y)|=sum_{h=1}^{L(y)} q^{D(h)}`.

   Targets with `L(y)=ell` number
   `q^{b_{>=ell}}-q^{b_{>=ell+1}}`, where
   `b_{>=ell}=#{i:lambda_i>=ell}`.  This gives the complete fibre histogram
   and its extremizers; the largest fibres are the nonzero kernel vectors
   supported only on longest blocks.

### Proof route

Jordan chains are used only as coordinates.  If `h(v)=h`, applying
`N^(h-1)` deletes all levels below `h-1` and sends exactly the active
level-`h-1` coefficients to block bottoms.  Lower coordinates contribute
`D(h)` free parameters.  Summing the disjoint height strata gives the fibre
formula.  Similarity equivariance makes the result basis-independent.

### Boundary and second-axis obligations

- `N=0`: all block lengths are one and `T` is the identity.
- One Jordan block, repeated block lengths, `q=2`, and targets supported in
  blocks of unequal lengths must be proved explicitly.
- Axis 1 is the exact terminal/spectral theorem; Axis 2 is the every-target
  fibre polynomial and extremizer classification.

### P1–P186 mechanism subtraction

This is not P182's map on a subspace lattice: the carrier is the vector set
and the update chooses a state-dependent terminal iterate of one fixed
nilpotent endomorphism.  It has no comparator, polarity, Gram matrix,
adjugate, norm, annihilator, commutator, Möbius action, or Newton–Hensel lift.
Nilpotent Jordan theory and vector height are classical background and receive
zero contribution credit.  Any source stating the literal map or the fibre
formula kills the candidate.

## A02 — conjugacy-class-size power dynamics on dihedral groups

Let `D_{2n}=<r,s:r^n=s^2=1, srs=r^{-1}>`, `n>=3`, and define
`T(g)=g^{|g^{D_{2n}}|}`.  Write `n=2^a m` with `m` odd.

### All-parameter contract

The literal map is

- `T(1)=1` and, for even `n`, `T(r^{n/2})=r^{n/2}`;
- every other rotation satisfies `T(r^k)=r^{2k}`;
- reflections are fixed when `4` does not divide `n`, and all reflections
  map to `1` when `4` divides `n`.

Consequently:

1. If `n` is odd, the map is a permutation.  All `n` reflections are fixed,
   while rotations of exact order `d|n` form
   `phi(d)/ord_d(2)` cycles of length `ord_d(2)` (with `ord_1(2)=1`).
2. If `a>=1`, the recurrent rotations are the `m` rotations in the odd-order
   subgroup together with the exceptional central rotation `r^{n/2}`.
   When `a=1`, all `n` reflections add fixed recurrent points; when `a>=2`,
   every reflection has tail one.  The same divisor/order formula over
   `d|m` gives the noncentral rotational cycles, plus the central singleton.
3. A noncentral rotation whose exponent is not divisible by `m` has tail
   `a-min(a,nu_2(k))`.  A rotation `r^k` with `m|k`, other than `1` and
   `r^{n/2}`, reaches the central fixed point after
   `a-1-nu_2(u)` steps when `u=k/m` is represented in
   `Z/2^a Z`.  These cases yield the exact tail census and sharp depth.
4. The image size is `2n` for odd `n`, `3n/2+1` for `n=2 mod 4`, and
   `n/2` for `4|n`.

### Exact inverse axis

Let `Z={0}` for odd `n` and `Z={0,n/2}` for even `n`.  For every rotation
target `r^j`,

`T^{-1}(r^j)={r^k:k notin Z, 2k=j mod n}`

plus `1` when `j=0`, plus `r^{n/2}` when `n` is even and `j=n/2`, plus all
`n` reflections when `4|n` and `j=0`.  A reflection target has itself as its
unique predecessor when `4` does not divide `n`, and has no predecessor when
`4|n`.  Hence the sharp maximum fibre is `1` for odd `n`, `2` for
`n=2 mod 4`, and `n+1` for `4|n`.

### Proof route and boundaries

Use the exact dihedral conjugacy classes, then solve only doubling congruences
in `Z/nZ`.  Chinese remaindering separates the `2^a` tail clock from the
permutation `x -> 2x` on `Z/mZ`; multiplicative orders give cycle counts.
The cases `n` odd, `n=2 mod 4`, `4|n`, `m=1`, and the exceptional central
rotation are separate proof branches.  Axis 1 is the tail/cycle/image atlas;
Axis 2 is the every-target predecessor set and sharp fibre cap.

### P1–P186 mechanism subtraction

This is not a commutator map, group-algebra norm, fixed power map, co-gcd
translation, or state-selected diagonal feedback.  The exponent is the
current element's conjugacy-class cardinality; on rotations this creates a
central exception to doubling, while reflection behavior changes at `4|n`.
Dihedral conjugacy classes, orbit–stabilizer, ordinary power maps, CRT, and
multiplicative orders receive zero contribution credit.  A direct owner of
the literal class-size-dependent power map or this dihedral atlas kills it.

## Gate state

Both contracts require a fresh symbolic proof audit and broader direct-owner
search before any numbering.  Present status:
`UNNUMBERED / OWNER_AMBER / HOLD_EXTERNAL`.
