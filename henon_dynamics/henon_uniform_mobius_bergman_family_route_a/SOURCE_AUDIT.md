# Source audit

## Frozen object

- Candidate: `HCS-C137`.
- Parameter set: `R*=[3,7/2]×[6,7]` with `a` the first and `b` the second branch parameter.
- Branches: `phi_x(z)=1/(x+z)`.
- Space and normalization: normalized Bergman `A^2(D)`, basis `e_n=sqrt(n+1)z^n`.
- Operator: `L_(a,b)=C_phi_a+C_phi_b`.
- Word clock: one branch composition per letter; matrix convention `M_x=[[0,1],[1,x]]`.

The fixed pair `{3,6}` in C132 motivated the family question, but all C137 formulas and receipts are reconstructed inside this package.  No external target data or web-derived numerical data enter the evidence.

## Allowed evidence

Exact rational disk geometry, analytic nuclear decompositions, rational Möbius matrices, quadratic surds represented by `(trace, determinant, discriminant)`, finite word-ledger hashes, and symbolic identities are allowed.  The nine rational grid points are deterministic sentinels only; the theorem covers every real parameter in `R*`.

## Excluded evidence and claims

Prime and zero tables, fitted target zeros, local arithmetic factors, root numbers, Gamma factors, automorphy assumptions, and Route-B inputs are forbidden.  The package does not identify its Fredholm determinant with an external divisor and does not produce a unitary, scattering, self-adjoint, or Hilbert–Pólya operator.

Active firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
