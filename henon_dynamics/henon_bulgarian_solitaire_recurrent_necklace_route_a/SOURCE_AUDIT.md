# C190 source and ownership audit

## Primary source lock

Jørgen Brandt, “Cycles of partitions,” *Proceedings of the American
Mathematical Society* 85(3), 483--486 (1982), DOI
`10.1090/S0002-9939-1982-0656129-5`.

The AMS DOI, journal record, and Aarhus publication metadata were checked.
Brandt is the primary owner used here for the characterization of cyclic
partitions.  In the package's notation, if
`N=binom(k,2)+r`, `0<=r<k`, a recurrent state is obtained from
`(k-1,k-2,...,0)` by adding a length-`k`, weight-`r` zero-one word.  Rotation
of the word tracks the Bulgarian move.  The package does not claim priority
for this result or reproduce the whole historical proof.

Ethan Akin and Morton Davis, “Bulgarian Solitaire,” *The American
Mathematical Monthly* 92(4), 237--250 (1985), DOI
`10.1080/00029890.1985.11971590`, stable JSTOR DOI `10.2307/2323643`.

The publisher and JSTOR records were checked.  This article supplies the
classical Bulgarian-solitaire treatment and recurrent-set background.

## Convention lock

For `lambda=(lambda_1>=...>=lambda_m>0)`, the package uses

`T(lambda)=sort(m,lambda_1-1,...,lambda_m-1)`,

with zero parts removed.  For a word `w=w_0...w_(k-1)`,

`phi(w)=positive parts of (k-1,...,0)+w`.

The executable identity is `T phi(w)=phi(rho w)`, where
`(rho w)_i=w_(i-1 mod k)`, i.e. right rotation.  Calling it left rotation
without changing the index convention would corrupt the clock and reflection
checks.

## Claim-level ownership

- **Attributed classical theorem:** the recurrent set for every `N` is the
  declared binary-word layer and the dynamics becomes rotation.
- **Package derivation:** the gcd-binomial fixed formula, Möbius least periods
  and cycles, full finite zeta, full Koopman algebraic spectrum, trace law,
  recurrent reflection formulas, and triangular specialization.
- **Executable evidence:** independent word construction, full direct
  partition functional graphs for `N<=40`, a separate SymPy path, byte replay,
  and semantic mutation rejection.
- **Not claimed:** complete transient trees, hitting-time distributions,
  nilpotent Jordan block sizes, a global reversor, theorem priority,
  literature-wide novelty, or external peer review.

The bibliography population is two.  Neither source supplies target zeros,
prime tables, arithmetic local data, Euler factors, root numbers, automorphy,
or a Hilbert--Polya operator.
