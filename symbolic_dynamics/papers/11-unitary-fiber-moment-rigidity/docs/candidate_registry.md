# Candidate Registry

## SD-C13 — finite positive unitary fibers

- Family: **Symbolic Dynamics**, exclusively.
- Atoms: tensor-indecomposable full shifts \(F_p\), internally generated and
  entropy ordered.
- Base grammar: one primitive loop at each atom.
- Fiber: one frozen finite-dimensional unitary \(U_p\).
- Ledger: \(p^{-rs}\tau_p(U_p^r)\), with faithful normalized matrix trace.
- Determinant: ordinary finite-cutoff determinant and all-order tracial
  logarithm on the honest trace-class half-plane.
- Data firewall: no Riemann zeros, target roots, fitting, or changed fibers.

### Exact accomplishment

The positive moment problem is rigid:

\[
\tau(U)=1\Longrightarrow U=I.
\]

Ordinary traces \(\operatorname{Tr}(U^r)=1\) for every repetition force
\(d=1,U=1\). Hence a nontrivial positive state-visible fiber cannot preserve
the exact prime/repetition ledger.

Nonfaithful sectors do not control their hidden ordinary determinant.
Matched graded sectors cancel the hidden determinant motion. Roots-of-unity
fibers leak at a finite repetition. Matched composite and random clocks show
the same Bloch response.

### Route status

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    GO_POSITIVE_MOMENT_RIGIDITY
    STOP_BLOCH_ESCAPE
    STOP_SCOPED / PROVES_TOO_MUCH
    route_b_invocation_allowed: false

The canonical YAML remains provisional with WORKTREE_PENDING_FINAL_COMMIT
until the root agent performs the two-stage freeze.
