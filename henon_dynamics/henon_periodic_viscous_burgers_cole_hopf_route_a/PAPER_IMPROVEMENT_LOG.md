# Paper improvement log

The two reviews below are internal adversarial reviews performed for this package.
They are not external peer review, not an acceptance score, and not evidence of
novelty.

## Round 0 to round 1: theorem-completeness review

**Finding.** The initial manuscript established the global Hopf--Cole formula but
did not yet make the requested phase-portrait increment explicit. It also stated a
decay rate without isolating the next linear mode from the quadratic logarithmic
correction, and listed eigenvalues without the generator domain.

**Implemented changes.**

- Added the definition of forward recurrence and proved that convergence to the mean
  excludes every nonconstant recurrent or periodic point.
- Added the first and next active absolute modes, the remainder exponent
  \(\min(2\nu\kappa_r^2,\nu\kappa_{r_2}^2)\), the nonzero leading pair, and the exact
  logarithmic decay limit.
- Added the complexified \(H^s\) generator domain \(H^{s+2}\), compact-resolvent
  completeness, the missing \(k=0\) direction on the fixed-mean leaf, and the real
  conjugate-block interpretation.

## Round 1 to round 2: hostile boundary and reproducibility review

**Finding.** The revised draft risked calling pure heat the fixed-coordinate
autonomous conjugate, did not sufficiently distinguish finite oracle rows from the
all-function proof, and needed an explicit classical-ownership and Route-A boundary.

**Implemented changes.**

- Distinguished \(K_t=e^{t(\nu\partial_x^2-m\partial_x)}\) in fixed \(x\) from pure
  heat in \(y=x-mt\), and checked the drift and spectral signs together.
- Clarified that exact rational \((\rho,\zeta)\) rows probe the universal commuting
  heat/translation multiplier and need not lie on the physical one-parameter curve.
- Added exact oracle counts and identified the checker as producer-independent while
  saying explicitly that finite trigonometric rows are regression only.
- Added Hopf and Cole primary-source ownership, removed any possible priority reading,
  and stated every forbidden arithmetic/non-source claim.
- Added the exact frozen route tuple, rejected overall status, and false Route-B flag.
- The all-page visual audit found two references orphaned on an otherwise empty
  second page. Repaginated the final-only certificate section and added a compact
  six-row audit table, producing two coherent, unclipped pages without log warnings.

## Release disposition

Round 0, round 1, and round 2 are preserved as content-distinct PDFs. The final PDF
is byte-identical to round 2 and is subject to the fixed-epoch double-build, font,
log, text, page-render, and manifest audits recorded in the release reports.
