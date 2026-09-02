# Results

## Mathematical result

The package proves one complete full-class theorem: every bounded-at-origin, finite-circulation, \(C^2\) radial forward-self-similar vorticity profile is the signed Lamb--Oseen Gaussian.  It then gives the induced velocity, every positive-radius trajectory, every even radial moment, all finite \(L^p\) norms, exact enstrophy and palinstrophy, the dissipation identity, and the sharp singular/asymptotic boundary atlas over all \(\Gamma\in\mathbb R\), \(\nu>0\), and \(\tau_0\ge0\).

## Finite regression result

- 8 field cases
- 72 pointwise residual/circulation cells
- 72 moment cells (orders 0 through 8 in every field case)
- 48 \(L^p\) cells (powers 1 through 6 in every field case)
- 12 exponential-integral/direct-quadrature trajectory cells
- 9 boundary cells
- 213 audited cells total
- 1195 independent checker assertions
- 31 exact SymPy identities
- 84 of 84 hostile mutations rejected

Evidence payload SHA-256: `a1e673d61021eea58b54d2fdbf3d813ee87d7b84d91fbfcefb528f4e741766b4`

Evidence file SHA-256: `518343c593f63402eabbcb602761d54c56003d27c3e9f3774ee405b5115c74c2`

Final PDF SHA-256: `5b1a4d4dd9480e55ff970b5ae01dac8435c5c9ac4a62ee3c1f740288cd342b61`

## Route-A result

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`; overall `ROUTE_A_REJECTED`.  Route B is locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.
