# Evidence and falsification plan

## Analytic claims

- Derive `det(yI-TT*)` both from a site-level continuant and from the
  Chebyshev secular polynomial, including the `(vw)^M` prefactor.
- Put `x=-cosh(kappa)` and prove that
  `sinh((M+1)kappa)/sinh(M kappa)` is strictly increasing from
  `(M+1)/M` to infinity.
- Substitute the proposed left/right hyperbolic tapers into both block
  eigenvalue equations and recover the positive energy in two equivalent
  forms.
- Treat `w=0`, `v=0`, `(v,w)=(0,0)`, `v=w>0`, and `M=1` directly rather
  than by division through a vanishing hopping.
- Fourier diagonalize the finite ring and distinguish the continuum gap
  `|v-w|` from the sampled gap: `|v-w|` for even `M` and
  `sqrt(v^2+w^2-2vw cos(pi/M))` for odd `M`.
- Derive the propagator from even and odd powers of the chiral block so the
  matrix `sinc` is entire on singular faces.
- Reduce a positive, gapped two-band quench zero to one affine equation in
  `cos(k)` and preserve the finite-grid incidence condition.

## Regression matrix

- Open chains: `M=2,...,12`, five regimes each, every polynomial
  coefficient exact.
- Hyperbolic witnesses: `M=2,...,12` and
  `exp(-kappa) in {1/2,2/3,3/4}`, with exact rational hoppings, energy,
  eigenvectors, norm, and decay receipt.
- Threshold: every `M=2,...,12`, scaled as `(v,w)=(M,M+1)`.
- Rings: `M=2,...,15`, five parameter faces, both explicitly named gap
  conventions, and all 595 sampled momenta.
- Singular faces: all three open-chain faces for `M=2,...,12`.
- Propagation: six faces for `M=2,...,6`, checked by an independent Taylor
  matrix exponential.
- Quench: three cross-phase and three control rows, including
  `cos(k*)=-1/2`, whose finite grid is hit exactly only when `3` divides
  `M` in the audited range.

## Independence and release gates

The checker must not import the producer.  JSON and YAML loaders reject
duplicate keys, aliases, merge keys, nonfinite constants, wrong roots,
extra row fields, and noncanonical rationals.  Every executable lane refuses
optimized Python.  A SymPy lane checks symbolic identities, two isolated
producer runs must match the checked-in evidence byte for byte, and every
repaired-hash mutation must fail, including a globally rescaled OBC row and
an odd-critical zero sampled-gap forgery.  Each of three substantively different
paper rounds is built twice from a fresh directory with a fixed epoch; all
PDFs must be warning-free, rasterizable, distinct across rounds, and contain
only embedded subset fonts.
