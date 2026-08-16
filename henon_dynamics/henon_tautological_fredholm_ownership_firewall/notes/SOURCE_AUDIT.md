# Source audit

The frozen mathematical inputs are repository results HCS-P75 and HCS-P76.

- P75 proves the exact weighted channel formula, nonzero coefficients
  `c_m`, and the moving channel divisor.
- P76 proves the punctured fixed-`q` continuation and its limiting boundary
  classification.

P77 locks each dependency's proof package, executable certificate, and PDF.
The trace-ideal identities used for the channel and rank-one constructions
are standard Fredholm determinant facts; the paper cites Simon's monograph.
The H\'enon/full-shift background is cited only for context to the verified
Devaney--Nitecki and Arai sources already used upstream.

The finite cyclic block, its singular values, the singleton noncompactness
argument, and the graded-ledger warning are derived directly here. No Lind
formula at `q!=1`, external arithmetic source, transfer operator, or
self-adjoint spectral theorem is imported or claimed.
