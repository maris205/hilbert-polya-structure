# Paper plan — P131

## Literal system

For `N>=2`, the carrier is the rational half-level

```text
R_N = { q in Q : 0<q<1, q=[0;a_1,...,a_k] canonically,
        a_i>=1, a_k>=2, sum a_i=N }.
```

Move the first Euclidean quotient to the back.  If this creates a terminal
quotient `1`, apply the canonical identity `[...,b,1]=[...,b+1]` as part of
the update.

## Claim spine

1. Exact entrance time is the position of the last quotient equal to one;
   the sharp maximum is `N-2`.
2. A cyclic run-absorption decoder gives the terminal core, and the eventual
   period is its primitive rotation period.
3. Formal OGFs enumerate every exact-depth layer and sum to `2^(N-2)`.
4. Every one-step fibre has size `0,1,2`; explicit inverse branches give the
   image and Garden counts.
5. Recurrent orbits are restricted weighted necklaces; their by-length
   Burnside count and the divisor fixed count are corollaries.

## Two proof routes

- Quotient-word route: track the last digit `1`, prove the cyclic
  run-absorption normal form, and invert the two update branches.
- Raw rational-path route: reconstruct `[0;a_1,...,a_k]` as the subtractive
  Euclidean word `L^{a_1}R^{a_2}...`; define the normalized full-string map
  `Psi` before taking run lengths; prove `E Phi = Psi E`; then recover the
  marker/core and both inverse strings directly from singleton blocks.

## Mandatory subtraction

Finite-CF uniqueness, the trailing-one identity, digit-sum Euclidean cost,
Stern--Brocot run coding, continuants, composition enumeration, regular
languages, Burnside, and cyclic-composition enumeration receive zero credit.
P117/P122/P126 are explicit internal ceilings.  The residual headline is
only the literal quotient queue together with its terminal decoder, depth
layers, small fibres, and its raw-path engine.  Under `a_k -> a_k-1` the
carrier is literally the composition set of `N-1`; this collision is admitted
rather than renamed away.  External status remains `HOLD`.
