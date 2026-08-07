# HCS-C18 computation package

This directory contains the producer and independent verifier for the frozen
HCS-C18 modular open-trace obstruction.

The package checks three distinct layers.

1. For every `q <= 2000`, it directly enumerates
   `phi(q)`, `s_q = #{x mod q: x^2 = -1}`, and
   `n_q = (phi(q) + s_q)/2`. The numerical Dirichlet ledger checks

   ```text
   Z_sc(s) = T0^(-2s)/2 * [
       zeta(2s-1)/zeta(2s)
       + zeta(2s)L(2s,chi_-4)/zeta(4s)
   ]
   ```

   with `T0 = 1` as an analytic coefficient normalization, not as a positive
   geometric cusp cutoff. The recorded residue is

   ```text
   Res_(s=1) Z_sc(s) = 1/(4*zeta(2)) = 3/(2*pi^2).
   ```

2. Exact rational-endpoint arithmetic distinguishes two sections. A primitive
   homogeneous section has automorphy factor in `{+1,-1}`, hence absolute
   factor one. The affine rational section has

   ```text
   abs(c*x+d) = den(g*x)/den(x),
   ```

   so its logarithm is an endpoint coboundary. Three exact witnesses also show
   that multiplication of chosen representatives does not descend to a
   representative-independent product on `P\SL2(Z)/P`.

3. For squarefree levels `2, 6, 30, 210`, the code constructs

   ```text
   Phi_N(s) = Lambda(2s-1)/Lambda(2s) * tensor_(p|N) M_p(s),
   M_p(s) = 1/(p^(2s)-1) *
            [[p-1, p^s-p^(1-s)], [p^s-p^(1-s), p-1]].
   ```

   A fixed divisor-cube Walsh basis diagonalizes every `Phi_N(s)`. The package
   verifies the channel formulas, determinant, functional equation, physical-
   line unitarity, zero commutators at different spectral parameters, and
   invariance of a frozen bare scattering product under every spectral-
   parameter reordering. Three physical-line and two off-line parameters are
   checked. The spectral parameter is not interpreted as dynamical time.

## Projector-resolved scope boundary

The bare scattering product is permutation-invariant because all matrices
have the same Walsh eigenbasis. This conditional product no-go does **not**
cover endpoint-resolved paths.
At level `Gamma_0(6)`, the package also evaluates

```text
tr(P_a Phi(s1) P_b Phi(s2) P_c Phi(s3)),
```

where `P_a` is the rank-one projector onto cusp `a`. Inserting these projectors
leaves the commutative scattering algebra: the frozen parameter-to-edge
reassignment and the frozen path change both give nonzero amplitude
differences. The result is only a positive assignment/path-sensitivity gate.
It is not intrinsic chronology, a determinant, a trace formula, or a
Hilbert--Pólya construction.

## Reproduction

From `henon_dynamics/modular_open_trace_obstruction` run:

```bash
python code/open_trace.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
python -m unittest discover -s code -p 'test_*.py' -v
python code/release_manifest.py --verify
```

The checker does not import `open_trace.py`. It recomputes at 110 decimal
digits, uses prime factorization instead of residue enumeration for the exact
arithmetic ledger, and uses Hurwitz zeta instead of the producer's Dirichlet-L
routine. JSON schemas, duplicate keys, CSV headers, every mathematical row,
and projector amplitudes are checked. The tests include schema, arithmetic,
and projector-amplitude tampering.

## Result artifacts

- `arithmetic_counts.csv`: 2,000 exact arithmetic rows;
- `open_series.csv`: 12 convergence checks with elementary tail bounds;
- `endpoint_ledger.csv`: 30 exact section-cocycle rows;
- `exact_certificates.json`: residue, endpoint, double-coset, and formula locks;
- `scattering_checks.json`: four squarefree levels and projector paths;
- `summary.json`: compact scientific ruling;
- `independent_check.json`: independent verification report.
- `release_manifest.json`: repository-level SHA-256 consistency ledger.

Neither implementation reads a prime table, a Riemann-zero table, or a fitted
scale.
