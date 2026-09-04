# Narrative report: HCS-C363

For assertion-specific classical solutions with the stated mass, moment,
strict-positivity, energy, dissipation, decay, and cutoff hypotheses, mass and
barycenter are conserved
and

\[
\mathcal F[\rho]=\int\rho\log\rho-\frac12\int\rho c
\]

dissipates as `- integral rho |grad(log rho-c)|^2`.  Under the mass-preserving
dilation `rho_lambda(x)=lambda^2 rho(lambda x)`,

\[
\mathcal F[\rho_\lambda]-\mathcal F[\rho]
=2M\left(1-\frac{M}{8\pi}\right)\log\lambda.
\]

The same factor appears in the finite-moment virial law

\[
I'=4M\left(1-\frac{M}{8\pi}\right).
\]

If `M>8 pi`, a classical finite-moment solution cannot persist beyond
`2 pi I(0)/(M(M-8 pi))`.  This is a forced loss of the stated classical
regime, not a complete theorem about the post-concentration weak solution.

At critical mass, translations and dilations of

\[
\rho_{\lambda,a}(x)=\frac{8\lambda^2}
 {(\lambda^2+|x-a|^2)^2}
\]

are stationary.  They have mass `8 pi` but infinite second moment, so they do
not satisfy the virial theorem's finite-moment hypothesis.  In radial form,
`n=m/(2 pi)` obeys `n_t=n_rr-n_r/r+n n_r/r`; the critical family is its exact
stationary solution.

This is a theorem-scale PDE package, not a numerical blow-up simulation.  The
finite ledger only audits exact coefficients, profiles, and parser behavior.
All Route-A checkpoints fail because no arithmetic source, prime clock,
target determinant, target analytic bridge, or target-zero operator appears.
