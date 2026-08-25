# HCS-C158: full-cycle secular scaling for the open Walsh gate

C158 studies the exact `k`-tick return of the frozen C148/C153 gate.  The
full-cycle operator is

```text
C_k=B_k^k=A^(tensor k).
```

If `lambda_+` and `lambda_-` are the two nonzero one-site eigenvalues, labeled
by decreasing modulus, then

```text
det(I-zC_k)=product_(j=0)^k
  (1-z lambda_+^j lambda_-^(k-j))^binom(k,j).
```

The exact degree is `2^k`, and the zero generalized eigenspace has dimension
`3^k-2^k`.  Weighting surviving eigenvalues by algebraic multiplicity turns
`k^(-1)log|rho|` into an affine binomial variable.  Its mean is exactly
`-log(3)/4`, its variance is `sigma^2/k`, it obeys an explicit Hoeffding
bound, converges weakly to a point mass, and has a Gaussian central limit.

The package includes exact field coefficients, binomial and concentration
receipts, literal small-`k` Kronecker determinant checks, independent checker
and SymPy paths, replay, semantic mutations, two genuine internal review
rounds, deterministic PDFs, and a self-excluded manifest.  It claims no phase
limit, self-adjoint limit, secular-zero convention transfer, target divisor,
or Route B.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.
