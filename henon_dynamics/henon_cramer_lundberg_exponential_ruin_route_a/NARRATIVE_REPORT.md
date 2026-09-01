# Narrative report

Let `tau` be first strict ruin and `D` the deficit.  Conditioning over the
first compound-Poisson jump yields an inhomogeneous renewal equation: claims
smaller than the current reserve restart the same transform, while larger
claims cause ruin and contribute the deficit penalty.  For exponential claims,
both terms are exponentials.  The probabilistically selected bounded solution
is

`Phi_{q,s}(u)=(beta-r_q)/(beta+s) exp(-r_q u)`,

where

`r_q=(c beta-nu-q+sqrt((c beta-nu-q)^2+4c beta q))/(2c)`.

For positive claim intensity, the factor `beta/(beta+s)` proves—rather than
merely suggests—that the deficit is exponential and independent of ruin time
conditional on ruin.  At zero discount in the profitable chamber, the local
equation is closed by a convolution state into a two-dimensional linear
system.  Its characteristic modes exhaust the solution space; `J(0)=0` and
the chamber boundary fix the coefficient.  At zero discount in the profitable
chamber, the local equation also admits a constant bounded solution; the probability boundary
`Phi(u)->0`, obtained from the negative-drift strong law, selects
`beta-nu/c`.  The root is zero at or beyond critical loading.  Hence ruin is
defective in the first chamber and certain in the other two.  With no claims,
ruin is impossible and conditional laws are undefined.

Differentiation gives a finite conditional mean on both strict sides of the
wall, but the critical root behaves like `sqrt(beta q/c)`, making the mean
infinite.  In the profitable chamber, the same adjustment root makes the
claims-minus-premium exponential a martingale and identifies its all-time
supremum as an atom at zero plus an exponential tail.

The exact source theorem is large, but Route A fails sharply: the explicitly
killed PDMP/Markov semigroup has no intrinsic deterministic, enumerable
primitive-periodic-orbit owner.
