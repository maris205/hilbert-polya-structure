# C196 hostile audit

This is internal artifact-bound auditing, not external peer review or an
independent error process.

The suite recomputes the canonical payload hash after 135 semantic attacks.
It covers identity and provenance, every source/attribution/theorem/boundary
field, the complete Route-A tuple, all scope flags, both source records,
every nonclaim, all aggregates, initial data, traces, pencil positions and
velocities, force residuals, scattering velocities/intercepts, inverse-position reconstruction,
both asymptotic ends, and order reversal.  One stale hash is also rejected.
Five of the repaired-hash attacks inject unknown keys at the top,
finite-regression, case, pencil-row, and scattering levels; exact key-set
checks reject every one.

High-risk rejected attacks include reversing
`ig/(lambda_b-lambda_a)`, changing `Tr L^2=2H` or the `2g^2` force, treating
a sampled gap as an all-time proof, swapping incoming/outgoing ranks,
detaching an intercept from its spectral line, claiming finite regression
proves all `N`, manufacturing a periodic zeta, promoting natural quantization
to a target spectrum, claiming classical novelty, or enabling Route B.

The independent Jacobi/projector checker and SymPy path strengthen
implementation confidence without becoming a new proof, novelty certificate,
or external review.
