# Narrative report — C229

## Contribution

The paper gives one closed theorem for the square-root diffusion

`dX = kappa(theta-X) dt + sigma sqrt(X) dW`.

The key advance is closure across parameter faces.  In the positive interior,
the Riccati flow yields an exact affine Laplace transform and the usual
noncentral chi-square transition law.  The scale `beta=sigma^2/(2*kappa)` and
shape `alpha=2*kappa*theta/sigma^2` put the generator in Laguerre form.  Thus
the Gamma invariant law, a reversible kernel expansion, and a sharp spectral
gap are all statements about one semigroup, not independent fitted facts.

The boundary atlas is explicit.  The Feller index compares
`2*kappa*theta` and `sigma^2`: equality belongs to the inaccessible/entrance
side; the strict lower side is regular and instantaneously reflecting.  When
the dimension is zero (`theta=0` or `kappa=0` with noise), zero is absorbing
and the transition law has an explicit atom.  Removing noise gives a
deterministic ODE, while removing both mean reversion and noise gives the
constant process.

## Evidence boundary

The JSON certificate contains 8 boundary rows, 7 transform rows, 3 Gamma
rows, 12 Laguerre/kernel rows, 5 gap rows and 3 atom rows.  A checker with 235
assertions, 18 symbolic identities, clean replay and 20 hostile mutations
backs the displayed ledger.  The numerical rows are regression evidence, not
claims of a new CIR discovery.

The stochastic kernel is not identified with a primitive periodic-orbit zeta,
an arithmetic determinant, a target divisor, or a Hilbert--Pólya operator.
