# Results

## Exact theorem outputs

- Multiplier:
  \(L=289+24\sqrt{145}=577.9982698910150\ldots\).
- Uniform correction:
  \(C_L<0.001735\).
- Abel constant:
  \(A_L=3\log L/\pi^2=1.9330777456585248\ldots\).
- Scaled-index limit: Gamma\((2,1)\), density \(xe^{-x}\,dx\).
- Tagged-space verdict: no norm- or weakly-convergent boundary subnet.

## Finite certificate

- exact packet rows: 70;
- HCS-P51 crosscheck rows: 22 recorded, 18 non-null source rows;
- Abel scales: 5;
- Laplace probes per scale: 3;
- dependency locks: 4;
- independent checker mutations rejected: 7;
- unit/adversarial tests: 12/12 normal and 12/12 under `-O`.

At \(\tau=0.0125\), the finite certificate gives
\(\tau^2Z(\tau)/A_L=0.99953857\ldots\) and only
\(0.0273036\ldots\) of the mass remains in the fixed prefix
\(3\le n\le20\).

These rows are finite diagnostics.  The limits are proved independently in
`../PROOF_PACKAGE.md`.
