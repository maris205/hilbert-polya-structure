# Narrative report

The decisive structural step is to split the clock at criticality. The
off-critical coordinate `delta=exp(-(lambda-mu)t)` turns the one-ancestor PGF
into an exact M\"obius map whose semigroup law is multiplication. At
`lambda=mu`, the apparently singular formulas are replaced by
`tau=lambda*t`, and composition becomes addition. This closes the entire
nonnegative rate quadrant, including the zero-rate identity.

The second key step is genealogical rather than merely algebraic. Each of the
`z` initial ancestors is extinct or alive at time `t`; the number alive is
binomial. Only after conditioning on that number does the population become a
negative-binomial sum of positive geometric family sizes. The hostile review
also sharpened the wording: the family is not **uniformly** one
negative-binomial law, although special parameter values can collapse the
mixture. That exception is retained explicitly.

The same representation makes all three large-time regimes transparent.
Subcritical and critical survival is asymptotically owned by one ancestral
line.  In the subcritical case the limiting geometric PGF also obeys the
exact conditional-semigroup invariance identity, which proves that it is
quasi-stationary rather than merely a conditional limit.  The critical case
yields Yaglom exponential scaling. Supercritical rescaling leaves each ancestor either zero or
exponential, so `z` ancestors produce the exact atom/binomial/gamma mixture.
Pure birth, pure death, zero population and undefined conditioning clauses are
closed rather than divided away.

This is a theorem-scale stochastic-process advance inside the project, but a
strict Route-A rejection. The PGF is a source-local expectation, not a
dynamical zeta; stochastic genealogical events are not deterministic
primitive periodic orbits; and no target analytic or operator structure is
present.
