# Deterministic results

Run `bash ../experiments/reproduce.sh` from this directory, or
`bash papers/6-cohomological-owner/experiments/reproduce.sh` from the project
root.  The controls use exact integer/rational arithmetic and no Riemann-zero
data, fitting, randomness or network input.

The finite tables are software and identity regressions.  The infinite
spectral-type conclusions are proved mathematically in the accompanying proof
audit and are not inferred from a cutoff.

## Generated artifacts

- `degree_trace_ledger.csv`: degree counts and exact cycle/point/cohomology
  agreement through degree 24.
- `cohomological_trace_ledger.csv`: degree-zero and degree-two traces and
  logarithmic zeta coefficients through power 24.
- `koopman_multiplicity_controls.csv`: finite-cutoff witnesses for selected
  rational-scaled Koopman frequencies.
- `frobenius_divisor_lift.csv`: the two Frobenius factors lifted to their
  `s`-plane pole preimage lattices.
- `operator_ownership_certificate.json`: typed operator, Route-A, and limited
  Route-B claim boundary.
- `manifest.sha256.json`: SHA-256 hashes of all five generated artifacts.

At the recorded release run, the manifest file itself has SHA-256
`4a78e430d08134bca09b88b4e5f3adf25b68692212893f6abeaad407d1711c16`.
