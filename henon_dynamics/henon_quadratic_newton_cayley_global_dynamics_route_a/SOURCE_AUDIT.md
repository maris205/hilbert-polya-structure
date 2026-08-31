# HCS-C257 source and citation audit

## Locks

- Source commit: `b89544f1f7b1043f4158dfdf9db77787b332f146`
- Evaluation date: `2026-08-31`
- Fixed epoch: `1788048000`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route-A evaluator v0.2.0 SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`

## Verified references

1. A. Cayley, “Desiderata and Suggestions: No. 3. The Newton-Fourier
   Imaginary Problem,” *American Journal of Mathematics* 2(1) (1879), p. 97.
   JSTOR metadata gives DOI `10.2307/2369201`.
2. M. Artin and B. Mazur, “On Periodic Points,” *Annals of Mathematics*
   81(1) (1965), 82–99.  The archival stable identifier is
   `https://www.jstor.org/stable/1970384`.

The references support historical context and the zeta definition.  Every
formula used in the theorem is derived in the package.  No external novelty,
priority, or peer-review claim is made.

## Workspace collision audit

- C141: $z^2-6$ inverse branches and a Hardy Ruelle operator.
- C177: the all-degree expanding-circle Wold/mixing theorem.
- C257: quadratic Newton root-finding on the full sphere, root basins and
  errors, complete preperiodic tails, multipliers, sphere zeta, and boundary
  Cauchy law.

The overlap is the elementary squaring factor; the owner contracts and main
theorems are different.  This is workspace bookkeeping only.
