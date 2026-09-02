# Hostile audit

## Mathematical attacks addressed

- The hopping orientation is fixed before choosing `q`; entrywise conjugation was checked in both directions.
- The finite PBC spectrum is described as points on an ellipse, never as the entire continuum.
- OBC is covered for `N>=2`; oriented-ring PBC is stated for `N>=3`, while `N=2` is isolated because `C=C^{-1}`.
- The condition-number equality is tied to the canonical sine gauge `R=DS`; arbitrary eigenvector rescaling is not hidden.
- Ordinary right-amplitude localization is separated from the canonical biorthogonal density `S_{jm}^2`.
- The one-sided OBC face is one Jordan block, whereas the zero corner has an `N`-dimensional eigenspace.
- Resolvent and propagator norm statements are upper bounds, not equalities.
- The one-sided OBC/PBC split is not promoted to a topological invariant.

## Artifact attacks addressed

The mutation suite repairs semantic payload hashes while changing formulas, exact types, list lengths, duplicate case identities, PBC traces, Jordan ranks, collision owners, boundaries, and scope flags.  It separately attacks duplicate keys, nonfinite JSON, top-level types, YAML duplicates, anchors, aliases, merges, booleans, extra keys, and verdicts.  Stale evidence and stale YAML hash controls are included.  The checker imports no producer code and refuses optimized execution.

## Scope result

No surviving attack may turn a finite determinant into an Euler factor, a finite spectrum into target zeros, skin bias into disorder localization or topology, or a diagonal similarity into a Hilbert--Polya construction.  Route A remains rejected under `NO_BAD_EULER_OR_ROOT_NUMBER`.
