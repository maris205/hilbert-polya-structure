# Hypergraph incidence gate

This directory records the complete pressure test of H03/OCF, the deterministic
map on labelled $3$-uniform hypergraphs

$$
x\longmapsto W_{2,3}^{\mathsf T}W_{2,3}x.
$$

The mathematical signal closes exactly: odd $n$ gives an idempotent of rank
$\binom{n-1}{2}$; even $n$ gives a square-zero map of rank
$\binom{n-2}{2}$; the complete functional graph, all-time fibres, and the
cycle/cut/bicycle boundary reconstruction follow.

The candidate does **not** survive allocation.  Peeters (2002) directly owns
the Johnson-matrix minimal-polynomial and rank core after
$L=I+A(J(n,3))$, and the remaining uniform boundary-lift refinement loses the
portfolio comparison to the current odd-degree Seidel-switch feedback.

```text
FINAL_DISPOSITION=KILL_DIRECT_OWNER_AND_INTERNAL_SILHOUETTE
EXTERNAL_STATE=HOLD_EXTERNAL
PAPER_NUMBER=NONE
```

Artifacts:

- `DERIVATION_PACKAGE.md`: invariant-first formula derivation.
- `PROOF_PACKAGE.md`: all-$n$ cycle/cut/bicycle proof and complete dynamics.
- `OWNER_AND_COLLISION_GATE.md`: primary-owner subtraction and P1--P171 gate.
- `verify_hypergraph_incidence.py`: deterministic exact verifier.
- `CANONICAL.txt`: canonical verifier transcript.
- `CONTROL_RESULTS.md`: coverage and replay instructions.
- `MANIFEST.sha256`: artifact checksums.

