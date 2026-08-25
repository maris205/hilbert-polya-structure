# C163 results

The unchanged frozen open Walsh gate passes the hard phase gate without a
dynamics pivot.

- Exact obstruction: `2cos(delta)=(sqrt(3)-sqrt(111))/6` has primitive
  irreducible integer polynomial `3x^4-19x^2+27` and monic rational minimal
  polynomial `x^4-(19/3)x^2+9`.  The nonintegral coefficient excludes
  algebraic integrality, so the phase ratio is not a root of unity.
- All-`k` theorem: the phase Fourier coefficient is
  `u_-^(mk)((1+r^m)/2)^k`; every nonzero fixed mode decays exponentially.
- Limit: the surviving phase measure converges weakly to Haar measure.
- Stronger limit: centered `sqrt(k)` log-modulus fluctuation and phase
  converge jointly to `Normal(0,sigma^2) tensor Haar`.
- Dichotomy control: moving the hole makes the phase ratio order four and
  produces convergence to the uniform four-point coset instead of Haar.
- Receipts: 32 register-length rows, 24 exact Chebyshev/Fourier rows, and 32
  moved-hole residue rows.

All claims are source-side.  Route B remains disabled.
