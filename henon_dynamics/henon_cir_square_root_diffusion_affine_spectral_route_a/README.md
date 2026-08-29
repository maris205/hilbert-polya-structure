# HCS-C229 — CIR affine boundary and Laguerre semigroup

This Route-A round changes dynamical subtype to a positive-state stochastic
diffusion.  The Cox--Ingersoll--Ross (CIR) process is solved for every
`kappa, theta, sigma >= 0`: the Feller face `2*kappa*theta = sigma^2`, the
regular/reflection side, and every zero-rate degeneration are kept separate.
On the interior face the affine transform identifies a noncentral-χ² kernel,
the invariant Gamma law, the complete Laguerre eigenbasis, and an exact gap
and mixing inequality.

The package is intentionally honest about the Route-A boundary.  A Markov
semigroup is not a primitive-orbit zeta or a Hilbert--Pólya operator, so the
strict tuple is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and
Route B is not invoked.

Artifacts:

- theorem and proof boundary: `THEOREM_PACKAGE.md`;
- source and claim audit: `SOURCE_AUDIT.md`;
- canonical evidence: `results/c229_cir_evidence.json`;
- independent checker, symbolic reconstruction, replay and hostile tests: `code/`;
- three-round compiled paper: `paper/main.pdf`;
- evaluator record: `evaluations/route_a/HCS-C229/2026-08-29.yaml`;
- self-excluded closure: `C229_RELEASE_MANIFEST.json`.

The exact evidence and PDF hashes are recorded in the manifest.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
