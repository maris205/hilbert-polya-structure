# HCS-C259 — tree Kuramoto locking and Morse atlas

This package proves a complete phase-locking theorem for every finite
positively weighted heterogeneous Kuramoto tree.  The unique child-subtree cut
flow gives the exact locking chamber; independent inverse-sine choices give
all branches; a quotient-Hessian congruence gives every Morse index and
saturated nullity.

The released regression enumerates all `18,248` labeled Prüfer trees for
`2 <= N <= 7`.  It is checked by a separate implementation, SymPy derivation,
byte replay and repaired-hash hostile mutation suite.  The finite ledger checks
conventions; the theorem is analytic for every finite tree.

Primary outputs:

- `THEOREM_PACKAGE.md` — full statement and proof.
- `results/c259_kuramoto_evidence.json` — content-addressed exact evidence.
- `paper/main.pdf` — final paper after two substantive revisions.
- `C259_RELEASE_MANIFEST.json` — self-excluded release manifest.

The result does not classify every unlocked running state or cyclic graph.
It has no arithmetic origin or target determinant.  The strict verdict is
`ROUTE_A_REJECTED`, Route B is disabled, and the scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
