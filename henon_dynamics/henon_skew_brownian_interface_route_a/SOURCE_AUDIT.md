# Source and collision audit

## Primary sources

- J. M. Harrison and L. A. Shepp, “On Skew Brownian Motion,” *Annals of
  Probability* **9** (1981), 309–313,
  [doi:10.1214/aop/1176994472](https://doi.org/10.1214/aop/1176994472).
  This supports the exact symmetric-local-time SDE threshold, strong
  uniqueness, and independent excursion-sign construction.
- T. Appuhamillage, V. Bokil, E. Thomann, E. Waymire, and B. Wood,
  “Occupation and local times for skew Brownian motion with applications to
  dispersion across an interface,” *Annals of Applied Probability* **21**
  (2011), 183–214,
  [doi:10.1214/10-AAP691](https://doi.org/10.1214/10-AAP691).  This is used as
  provenance for interface occupation/local-time questions.
- T. Appuhamillage, V. Bokil, E. Thomann, E. Waymire, and B. Wood,
  “Corrections: Occupation and local times for skew Brownian motion with
  applications to dispersion across an interface,” *Annals of Applied
  Probability* **21** (2011), 2050–2051,
  [doi:10.1214/11-AAP775](https://doi.org/10.1214/11-AAP775).  This corrects a
  drift-parameter restriction and the zero-drift trivariate-density display.
- The same authors, “Second errata to ‘Occupation and local times for skew
  Brownian motion with applications to dispersion across an interface,’”
  *Annals of Applied Probability* **34** (2024), 5842–5844,
  [doi:10.1214/24-AAP2106](https://doi.org/10.1214/24-AAP2106).  This corrects
  the multivariate-density Laplace transform after identifying a failed
  symmetry argument that the first correction did not cover.

HCS-C266 freezes zero drift and imports none of those corrected multivariate
formulas.  Its occupation density is instead derived from an independent
stable-$1/2$ ratio, and every displayed formula used by the certificate is
proved locally and regression-checked.

Metadata, page ranges, correction scope, and DOI resolution were checked on
2026-08-31 against IMS/Project Euclid records.  The paper makes no
literature-priority claim.

## Internal collision audit

- C200 owns a compact Jacobi/Wright--Fisher diffusion with beta equilibrium;
  C266 owns a local-time interface on the line, with no finite invariant law.
- C214 owns Brownian stochastic resetting and first passage; C266 has no
  reset clock and closes an interface semigroup and speed measure.
- C229 owns CIR square-root diffusion; C237 owns hypoelliptic Kramers
  diffusion.  Neither has a skew local-time matching condition.
- C226 is a deterministic Stefan free boundary, not a stochastic point
  interface.

HCS-C266 is therefore a distinct workspace owner.  HEN-O250 records the
noncompact recurrent/primitive-orbit obstruction.

## Claim boundary

No drifted skew Brownian motion, unequal two-sided diffusivity, sticky
interface, statistical calibration, or physical-material inference is
claimed.  Numerical quadrature is a regression oracle, never the proof.
Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
