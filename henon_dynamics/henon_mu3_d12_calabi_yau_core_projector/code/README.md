# HCS-C52 exact certificate

Run the complete release verification from this project directory:

\[
\texttt{./code/run\_c52.sh}.
\]

The runner regenerates the certificate in a temporary directory, checks it
with an independently implemented exact engine, runs the isolated
mutation/rollback suite, byte-compares the regenerated artifacts with the
frozen release copies, and verifies the full-project SHA-256 manifest.

## Independent routes

- `c52_producer.py` uses custom arithmetic in
  \(\mathbf Q(\rho)=\mathbf Q[\rho]/(\rho^2+\rho+1)\) and dense exact RREF.
- `c52_checker.py` rebuilds the same finite quotient with SymPy
  `DomainMatrix` over a separately constructed exact number field.
- The checker derives the support permutations from all \(8!\)
  permutations, verifies the complete representation law, and treats the
  two reductions modulo \(211\) only as auxiliary controls.
- `test_c52.py` uses rehashed targeted mutations, strict type attacks, and
  injected promotion failures.  Every semantic mutation must fail its
  named gate without producing an `ERROR`.

## Safe refresh

After an intentional source or documentation change, refresh only with

\[
\texttt{./code/run\_c52.sh --refresh-results --refresh-manifest}.
\]

Results and the manifest are promoted as one rollback-protected group only
after the temporary certificate, independent check, test suite, and
temporary full-project manifest all pass.  `--refresh-results` without
`--refresh-manifest` is rejected.

## Scope

The executable certificate covers the frozen source, the complete
projective monomial group, ordinary middle Chow projector identities, the
exact Cayley-ring character, the rank-\(10/158\) Hodge split, and the
\(\mathbf Q[G_{\rm mon}]\)-only rank-two obstruction.  It does not compute
C53 Frobenius polynomials, construct a correspondence outside the graph
algebra, prove coniveau or automorphy, or test Riemann zeros.
