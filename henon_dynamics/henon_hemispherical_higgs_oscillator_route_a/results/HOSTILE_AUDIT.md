# Hostile audit

The hostile suite first accepts the unmodified evidence and evaluator YAML.
For its substantive evidence attacks it then repairs all section digests and
the outer payload digest after mutation, so rejection cannot be attributed to
a stale hash.

## Rejected attacks

- 58 repaired-hash evidence attacks covering identity, obstruction, baseline,
  epoch, evaluator and YAML bindings, classical and quantum domains,
  Hamiltonian normalization, action and frequency contracts, Jacobi spectrum,
  boundary faces, limits, revival necessity and global phase, collision
  ownership, references, scale, rows, tuple, flags, and Route B;
- 1 stale-hash control;
- 2 malformed JSON controls: duplicate key and nonfinite constant;
- 12 YAML controls: duplicate key, merge, non-string key, anchor/alias,
  implicit date, unknown field, type, classical domain, status, artifact,
  tuple, and Route-B changes.
- 2 TeX-spacing mutations: an escaped command changed to literal `quad` or
  `qquad`; four legal controls verify that `\quad`, `\qquad`, `quadratic`, and
  `quadric` are not rejected.

Result: `75/75` hostile mutations killed; all four legal spacing controls
accepted.

## Reviewer attacks closed in theorem and paper

1. The action formula is derived from an explicit turning-root integral and
   Vieta identities; it is not inferred from the finite grid.
2. The classical theorem freezes `omega>0`. The `omega=0` open hemisphere is
   explicitly incomplete and is not called a complete periodic flow.
3. Circular, meridional, and north-equilibrium faces are separated from the
   regular action-angle chamber.
4. The quantum `omega=0` endpoint belongs to the Friedrichs family and is
   identified with the Dirichlet hemisphere, not the full sphere.
5. Multiplicity `N+1` is proved by directly counting admissible parity labels,
   not by importing a conflicting prose statement from arXiv:quant-ph/9803085.
6. Consecutive phase differences prove both necessity and sufficiency of the
   revival criterion; the `k=1` exponent proves the global phase is exactly
   one.
7. Spectral commensurability is not relabeled as arithmetic local data, and no
   target spectral or Route-B conclusion is drawn.
8. The release source gate rejects unescaped TeX spacing commands, and the PDF
   text gate rejects any leaked literal `qquad` token.
