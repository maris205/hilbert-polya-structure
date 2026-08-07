# HCS-C18: modular open data and trace closure

This project asks whether the two most natural escapes from the HCS-C17
final-denominator obstruction---retaining boundary endpoints and retaining all
cusp channels---survive an ordinary trace or determinant closure.

The answer is a scoped negative result with two positive controls.

1. The unoriented modular scattering geodesics have a genuine open
   Dirichlet--Laplace series
   \[
   Z_{\rm sc}(s;T_0)=\frac{T_0^{-2s}}2\left[
   \frac{\zeta(2s-1)}{\zeta(2s)}+
   \frac{\zeta(2s)L(2s,\chi_{-4})}{\zeta(4s)}\right].
   \]
   This is not a closed-orbit Selberg zeta.  It is retained as a classical,
   source-derived positive control rather than claimed as a major novelty.
2. On the cusp endpoint action groupoid
   \(\mathrm{PSL}_2(\mathbb Z)\ltimes\mathbb P^1(\mathbb Q)\), every
   section-induced absolute projective automorphy cocycle of the specified
   form is an algebraic/set-theoretic coboundary.  In the affine gauge its
   value from \(\infty\) is \(2\log |c|\), so the scattering denominator is
   endpoint-gauge data rather than an intrinsic loop period.  No continuous
   or bounded transfer-operator conjugacy is claimed.
3. Extending the unit space to \(\mathbb P^1(\mathbb R)\) creates nonzero
   loops with nonzero automorphy period, but those periods are precisely the
   signed hyperbolic translation lengths.  This identifies the period support
   of a diagonal loop trace; it does not by itself construct a Selberg
   determinant.
4. For squarefree \(N\), the complete standard scattering matrix of
   \(\Gamma_0(N)\) is a tensor product of two-channel local blocks.  A fixed
   Walsh--Hadamard basis diagonalizes the family for every spectral parameter.
   A frozen product at distinct spectral parameters is computed before any
   compression; its permutation invariance follows from the source matrices
   themselves, not from an averaged transition approximation.  The spectral
   parameter is not identified with dynamical time.
5. Endpoint projectors inserted between scattering matrices generally restore
   parameter-to-edge assignment and endpoint-path sensitivity.  This is an
   explicit positive scope boundary, but it does not yet establish intrinsic
   chronology or supply a canonical primitive-object law or Fredholm
   determinant.

## Main status

- Candidate: **HCS-C18**.
- Research verdict: **READY AS A SCOPED OBSTRUCTION** after independent
  validation.
- Hilbert--P\'olya verdict: **Route-A rejected object by object** for the
  frozen ordinary endpoint closures and bare squarefree-product model; the
  projector branch remains not testable rather than refuted.
- Novelty boundary: the scattering formulas, Busemann cocycle, fixed-point
  classification, and Atkin--Lehner factorization are classical.  The project
  theorem novelty is low.  The defensible contribution is their exact
  compatibility synthesis and a reproducible trace-closure obstruction.

The result does **not** rule out projector-resolved path amplitudes,
nontrivial matrix cocycles inserted between open arrows, twisted/non-squarefree
scattering, off-diagonal groupoid kernels, or a separately derived
self-adjoint operator.

## Reproduction

```bash
python code/open_trace.py --output results
python code/independent_check.py --results results \
  --output results/independent_check.json
(cd code && python -m unittest -v test_open_trace.py)
python code/release_manifest.py --verify
```

## Directory guide

- `paper/`: article source and compiled PDF.
- `code/`: producer, independent checker, and tests.
- `results/`: exact and high-precision certificates.
- `evaluations/route_a/`: frozen Route-A decision.
- `DERIVATION_PACKAGE.md`: theorem statements and proofs.
- `SOURCE_AUDIT.md`: primary-source and novelty audit through 2026-08-07.
- `EXPERIMENT_PLAN.md`: preregistered claims, controls, and falsifiers.
- `IDEA_REPORT.md`: breadth-first candidate comparison.
- `PAPER_PLAN.md`: claim--evidence map and manuscript structure.
- `AUTO_REVIEW.md`: adversarial findings and their resolutions.
- `REFINEMENT_REPORT.md`: before/after claim boundary.
- `COMPILE_REPORT.md`: final PDF build and visual-check record.
- `REPOSITORY_UPDATE.md`: release provenance and verification commands.
