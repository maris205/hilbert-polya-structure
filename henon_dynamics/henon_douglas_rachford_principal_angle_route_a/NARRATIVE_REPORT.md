# Narrative report

The relaxed Douglas--Rachford method looks like an algorithm with many tuning
choices, but for two linear subspaces it is one completely soluble dynamical
system.  Principal angles are the correct coordinates.  Two intersection
spaces are fixed, two mismatch spaces carry the scalar `1-lambda`, and every
remaining plane is a rotation-contraction whose modulus is known exactly.

This gives a genuine one-paper step.  The same calculation identifies the
whole convergence interval `0<lambda<2`, the sharp operator-norm rate, the
unique uniformly best relaxation `lambda=1`, the shadow limit, the two endpoint
systems, divergence outside the closed interval, every power trace, and the
finite determinant.  It also prevents two common errors: treating
`lambda=2` as convergent, or omitting `U-perp intersection V-perp` from the
fixed space.

The exact evidence deliberately uses rational Pythagorean angles, so all
matrix entries remain fractions.  That grid is broad enough to kill sign,
normalization, trace and endpoint errors but is not presented as proof.  The
all-subspace proof comes from the canonical projection decomposition.

For Route A the result is decisive and negative.  The orthogonal endpoint is
natural, but natural unitarity by itself is not arithmetic relevance.  The
subspaces provide neither rational primes nor a logarithmic clock, and the
finite matrix determinant is an algorithmic determinant rather than a target
dynamical Zeta function.  The correct research output is therefore both a
complete dynamics theorem and a strict rejection of this family as a primary
Hilbert--Pólya dynamics candidate.
