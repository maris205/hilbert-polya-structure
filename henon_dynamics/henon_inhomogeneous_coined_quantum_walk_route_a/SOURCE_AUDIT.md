# Source audit

## Source lock

- Space: `C^5 tensor C^2`, basis ordered by site then coin sign.
- Graph: the five-cycle.
- Coins:
  `C0=(1/5)[[3,4],[4,-3]]` and
  `C1=(1/13)[[5,12],[12,-5]]`.
- Arrangements: `00011` and `00101`.
- Evolution: coin first, then the flip-flop shift, `U_w=S C_w`.
- Clock: one application of `U_w`.
- Determinant: `D_w(z)=det(I_10-zU_w)`.
- Precision: exact rational arithmetic.

## Evidence discipline

Signed and complex amplitudes belong to the object.  The release never
replaces them by absolute values.  Absolute values appear only in the
convergence majorant for the raw primitive product.

No external paper or novelty result is asserted.  The earlier quantum-graph
and metaplectic packages are used only for repository-level de-duplication:
C143 is a spatially inhomogeneous discrete coined walk, not a metric graph
propagator or a finite torus quantization.

## Exclusions

There is no target zero table, target divisor, prime table, arithmetic local
factor, Euler factor, root number, automorphy input, Hilbert--Polya operator,
or Route-B invocation.
