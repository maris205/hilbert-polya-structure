# Refinement Report

## Initial direction

The initial Route A idea asked for an energy-localized relative wave trace
with explicit period/action control, but it did not specify a tractable
energy regime, an orbit, or how to control radial orbit families.

## Final direction

The refined project uses the unique equilibrium and exact Hessian of the
one-step \(a=1.02\) well.  It turns a broad global-wave-trace problem into a
single-orbit eigenvalue-only theorem near \(E=2\pi\).

## What became simpler

- Compact regular energy shells are automatic.
- The fast normal-mode nonresonance is automatic.
- The limiting period and stability determinant are exact.
- The time interval \([0.60,0.75]\) is prospectively fixed by the Hessian,
  not by a spectral peak.
- The radial reference can be removed by nonstationary phase rather than a
  clean-family amplitude calculation.
- A complete-shell blow-up reduces the global warped orbit census to a
  Poincaré-map uniqueness theorem.

## What became stronger

- Period and action now have a non-fitted first nonlinear coefficient.
- The numerical run tests action and monodromy, not only a magnitude peak.
- The independent checker re-solves the orbit without project imports.
- The fixed-energy and high-energy limits are explicitly separated.
- A4.12 now validates one primitive branch through the complete target band,
  and A4.13 proves its strict transverse gap by exact Hamiltonian reduction
  plus directed interval arithmetic.

## What remains genuinely hard

- an absolute Conley--Zehnder lift if a convention beyond the trace-relevant
  CRR index modulo four is later required;
- validated exclusion of the local root complement and the remaining global
  warped returns, plus the independent event-projected \(D\Pi\) and
  Taylor-identity cross-check; A4.11a--A4.11b close the radial and short-time
  components, while A4.12--A4.13 close the fast local branch and its
  \(D>3\) gap through \(\delta=0.010201\);
- the fixed-operator high-energy hard-wall/Hénon-metric calculus;
- any endogenous prime-power mechanism.

## Research contribution after refinement

The result is no longer pitched as a new general trace formula.  It is a
model-specific analytic bridge demonstrating that a clock-preserving Hénon
warp can generate an isolated, eigenvalue-only semiclassical periodic
contribution with explicit normal-form data while the equimeasurable radial
reference is absent from the same time window.  A4.8 supplies the required
whole-shell uniqueness and A4.9 removes the observable.  A4.10 and R401-SC
now also fix and numerically recover the full complex coefficient, while the
arithmetic P gate remains untouched.  The subsequent A4.12--A4.13
certificates materially strengthen the quantitative theorem-domain program:
one primitive local branch now covers the full parameter band and has a
uniform validated transverse determinant above \(3\).  They do not replace
the still-open complement/global cover or the independent determinant
identity gate.
