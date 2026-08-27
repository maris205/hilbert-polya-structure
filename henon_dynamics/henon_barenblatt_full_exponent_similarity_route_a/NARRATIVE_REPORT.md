# Narrative report

Mass preservation forces the first-kind exponent `alpha=1/(m+1)`.  Inserting
`u=t^{-alpha}F(x t^{-alpha})` and integrating the profile equation under the
declared zero-flux condition reduces the nonlinear PDE to a first-order
identity.  For `m>1` it integrates to a positive-part quadratic raised to
`1/(m-1)`; for `0<m<1` the sign reverses and produces a positive quadratic
raised to `-1/(1-m)`.  At `m=1` the correct limiting equation is logarithmic,
and the normalized Gaussian must be written separately.

The solution concept is part of the theorem: `F^m` is locally absolutely
continuous and the integrated law holds almost everywhere, with uniqueness
up to almost-everywhere equality.  On each positivity component the primitive
is forced.  Endpoint continuity leaves exactly one symmetric component in
the porous branch and no finite endpoint in the heat or fast branch, closing
the possible zero-set loophole without classifying arbitrary Cauchy data.

The mass normalization is exact, not numerical: one Beta integral fixes the
constant `C` uniquely in each nonlinear regime.  The same substitution with
`|xi|^r` gives every absolute moment.  In fast diffusion, the tail is
`|xi|^{-2/(1-m)}`, so the exact condition is
`r<(1+m)/(1-m)`; equality gives logarithmic divergence.  Taking `r=2`
isolates `m=1/3`, a boundary that is easy to lose in a three-regime summary.

For porous medium, the pressure is quadratic on the compact support and the
free boundary is explicit.  Logarithmic time and mass-preserving spatial
rescaling turn every Barenblatt profile into a stationary state.  The
nonlinear energy `integral(v^m/(m-1)+alpha*xi^2*v/2)` and the heat branch
`integral(v log(v)-v+xi^2*v/4)` have the displayed chemical potential as
their first variation.  Their dissipation identity is reported only for
sufficiently regular positive solutions with each energy term finite and
enough boundary decay.  In the fast regime,
the Barenblatt second-moment/free-energy class used here begins strictly above
`m=1/3`.

The numeric ledger uses 100 working decimal digits and serializes 82
significant digits.  It states these roles separately rather than calling the
stored strings 100-digit data.

The exact ledger confirms all frozen conventions but cannot replace the
continuous proof.  The model supplies no prime owner, isolated periodic-orbit
ledger, target determinant, or unitary same-clock lift.  All Route-A gates
fail, and Route B is not invoked.
