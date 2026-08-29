# Hostile audit

The mutation suite changes Hamiltonian/Lax theorem strings, initial Jacobi
data, finite states, norming weights, characteristic-boundary labels, source
and evaluator locks, route tuple, scope flags, citations, counts, and endpoint
status.  It repairs the payload hash for semantic edits before invoking the
checker.  Every one of 22 mutations is rejected.

The audit also checks the main overclaim risks: positive Jacobi simplicity is
not extended to \(a_j=0\); finite \(T=8\) sorting errors are not called limits;
the physical open-chain leaf is not mislabeled a compact torus; a finite
characteristic polynomial is not promoted to a target determinant; and no
arithmetic or Hilbert--Polya claim is emitted.
