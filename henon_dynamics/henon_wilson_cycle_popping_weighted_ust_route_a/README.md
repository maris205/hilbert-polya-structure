# HCS-C338 / HEN-O322 — Wilson cycle-popping and weighted USTs

This package closes one theorem-scale source problem: on a finite connected
loopless conductance multigraph, infinite-stack cycle-popping is abelian and
almost surely terminating, its canonical order is Wilson's loop-erased random
walk algorithm, its unoriented output has the weighted spanning-tree law, and
every finite edge-inclusion event is the corresponding transfer-current
determinant.

The proof joins four steps that are often presented separately: the local
diamond/strip argument for arbitrary legal pop orders; a last-exit Green-function
calculation for Wilson paths; a telescoping derivation of the weighted tree law
and matrix-tree normalization; and a conductance-perturbation determinant proof
of all transfer-current minors.  Singleton graphs, graphs already equal to a
tree, distinctly labelled parallel edges, and root changes are explicit.

The finite evidence is deliberately stronger than a few examples: it covers all
772 connected labelled simple graphs through five vertices, all 8,136 graph-tree
pairs, all 55,895 edge-subset events, 24 positive-integer weighted multigraphs,
and 12,754 depth-two stack tables over every rooted connected simple graph
through four vertices.  It is an implementation and convention receipt, not the
proof.

Run the complete gate from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_release_manifest.py
```

The Route-A verdict is `ROUTE_A_REJECTED`: there is no arithmetic source or
prime-orbit ledger.  The tree partition polynomial and transfer-current
determinants are source combinatorial objects, never target Euler factors,
target zeta data, or a Hilbert--Pólya construction.  Route B is disabled under
`NO_BAD_EULER_OR_ROOT_NUMBER`.
