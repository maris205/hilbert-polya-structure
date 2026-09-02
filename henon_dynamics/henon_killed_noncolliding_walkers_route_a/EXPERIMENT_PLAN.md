# Claim-driven experiment plan

## Analytic claims

- Prove the sine diagonalization and determinant transition kernel.
- Prove the Slater family is a complete orthonormal basis, including
  degenerate energy sums.
- Sum the kernel to obtain the survival function, differentiate for the
  density, and integrate for every positive integer moment.
- Isolate the consecutive-mode ground state, prove its determinant positive,
  and derive the QSD/Yaglom and leading asymptotic coefficients.
- Conjugate by the ground state to prove conservative Doob rates, reversibility
  with `h^2`, and the gap; branch explicitly at `k=L`.

## Finite regression

Enumerate every `1<=k<=L<=8`.  Independently reconstruct the integer
subgenerator, direct eigenvalues and matrix exponentials.  Compare them with
all analytic energies, every Slater vector, determinant kernels, Q-process
detailed balance, and three times on up to three representative states per
case.  A separate SymPy lane compares exact characteristic polynomials for
`L<=5` and exact phase-type moments.

## Adversarial boundary

Mutate metadata, bool/float integer aliases, state coordinates, dimensions,
killing degrees, spectrum, ground positivity, full-occupancy gap, survival
probes, route tuple, flags, canonical JSON, strict YAML, and stale self-hashes.
The primary checker must explicitly reject optimized Python.
