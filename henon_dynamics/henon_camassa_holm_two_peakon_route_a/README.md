# HCS-C278 — Camassa–Holm two-peakon atlas

This package proves one complete theorem for the ordered two-peakon invariant
manifold of the Camassa–Holm equation.  It derives the distributional ODE,
reduces it by two conserved quantities, closes both the same-sign scattering
and opposite-sign collision chambers, and defines an explicit
`alpha`-dissipative collision ledger.  Single-peak, zero-momentum, zero-field,
and coincident-state boundaries are retained.  The strict chamber theorem is
stated for `p_1p_2!=0`; the equality face is handled separately rather than
being silently forced into one of the two chambers.

The strongest statement is **PROVABLE AS STATED** under the frozen two-peakon
and collision-extension conventions.  It is not a uniqueness theorem for all
weak Camassa–Holm solutions.

## Release surface

- theorem and scope: `THEOREM_PACKAGE.md`
- exact evidence: `results/c278_camassa_holm_evidence.json`
- independent validation: `code/`
- Route-A evaluation: `evaluations/route_a/HCS-C278/2026-09-01.yaml`
- retained manuscript and three revisions: `paper/`
- content-addressed closure: `C278_RELEASE_MANIFEST.json`

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route B is not authorized.
