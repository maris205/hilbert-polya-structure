# Source and novelty audit

Search date: 2026-08-13.

## Frozen local sources

The dynamical base is the source-locked manuscript

`henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.

The immediate mathematical input is C35,
`henon_dynamics/adelic_henon_theta_route/`, which proves the adelic H6
unitary, the infinite dilation orbit, and the Poisson boundary-defect
identity. C36 does not re-claim those theorems.

## Imported analysis

Imported standard facts are:

1. Mellin transformation, analytic continuation by contour deformation,
   and Mellin convolution principles. A stable online locator is NIST DLMF,
   Section 2.5, <https://dlmf.nist.gov/2.5>.
2. Generalized hypergeometric notation and analytic continuation. See NIST
   DLMF, Chapter 16, <https://dlmf.nist.gov/16>.
3. Rouch\'e's theorem and elementary compactness facts for multiplication
   operators.
4. Certified midpoint-radius complex arithmetic as implemented by Arb;
   Fredrik Johansson, “Arb: efficient arbitrary-precision midpoint-radius
   interval arithmetic,” *IEEE Transactions on Computers* 66 (2017),
   1281--1292, DOI 10.1109/TC.2017.2690633.

The DLMF locators were checked against version 1.2.7. The published
Connes--Consani scaling reference was checked against *Journal of Operator
Theory* 85 (2021), 259--278, DOI 10.7900/jot.2019oct30.2265.

The release uses `python-flint==0.9.0` as the Python interface to Arb. The
software performs enclosure arithmetic; it does not supply the mathematical
Rouch\'e argument or the rotated-contour majorant.

## Bounded novelty search

The search covered combinations of:

- cubic oscillatory Mellin transforms and Airy-type integrals;
- H\'enon generating functions with Mellin or scattering transforms;
- reciprocal matrix Mellin symbols and critical-line unitarity;
- Poisson boundary anomalies for polynomial chirps;
- zeta scattering factors modified by cubic phases.

Classical cubic Mellin integrals, Airy analysis, gamma/hypergeometric
continuation, and scattering reciprocity are prior art separately. No source
was located that derives this exact two-sign H6 boundary matrix, identifies
the zeta-relevant parity channel, and certifies that its natural reciprocal
and critical-line-unitary scattering factor has an off-critical strip
divisor.

This is a search-bounded novelty statement, not an exhaustive priority
claim.

## New contribution

The new contribution is the combined theorem:

- the C35 infinite scaling orbit admits an exact two-sign Mellin reduction;
- the forced parity scattering symbol has exact reciprocity and
  critical-line unitarity;
- its even channel has one certified simple zero in an explicit rational
  disc inside the strip and off the line;
- the mirror and odd factors are certified nonzero on the relevant discs;
- the natural linear parent is certified nonzero there;
- the completed Riemann \(\xi\) function is certified nonzero there without
  consulting a zero table;
- therefore the unrenormalized H6 scattering divisor is incompatible with
  an exact Riemann-divisor realization.

The reusable conceptual obstruction is that functional-equation symmetry
and critical-line unitarity alone do not control the divisor.

## Explicitly not claimed

- a proof or disproof of RH;
- a global census of the zeros of \(A\) or \(B\);
- an ordinary Fredholm or Birman--Krein determinant;
- a constructed scaling-site H\'enon scattering operator;
- a theorem that every polynomial H\'enon deformation fails;
- novelty for Mellin transforms, hypergeometric continuation, or
  Rouch\'e's theorem themselves.
