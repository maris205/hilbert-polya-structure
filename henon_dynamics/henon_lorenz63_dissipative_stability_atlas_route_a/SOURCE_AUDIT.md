# Source and collision audit

## Ownership

Edward Lorenz introduced the three-mode system in *Deterministic Nonperiodic
Flow*, **Journal of the Atmospheric Sciences** 20 (1963), 130–141, DOI
`10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2`.  The present package claims no
priority for the classical equations, equilibria or bifurcation phenomena.

Pade, Rauh and Tsarouhas, *Analytical investigation of the Hopf bifurcation in
the Lorenz model*, **Physics Letters A** 115 (1986), 93–96, DOI
`10.1016/0375-9601(86)90031-9`, is recorded for nonlinear Hopf background.
That nonlinear direction is explicitly not asserted here.  Tucker,
*A Rigorous ODE Solver and Smale's 14th Problem*, **Foundations of
Computational Mathematics** 2 (2002), 53–117, DOI
`10.1007/s002080010018`, and Guckenheimer–Williams, *Structural stability of
Lorenz attractors*, **Publications Mathématiques de l'IHÉS** 50 (1979),
59–72, DOI `10.1007/BF02684769`, delimit rigorous classical-parameter and
geometric-attractor context.  Neither is used to extrapolate an all-parameter
chaos theorem.

## Claim-to-source boundary

- The model and classical context are externally owned.
- Equations (2)–(9) in `THEOREM_PACKAGE.md` are re-derived exactly in the
  released artifact chain.
- The package proves only an equilibrium/local-stability atlas.  It does not
  classify periodic orbits, strange attractors, crises or every invariant
  measure.
- DOI strings, titles and author attribution are frozen in the evidence and
  independently checked.

## Repository collision check

No C1–C223 package owns Lorenz-63.  The only textual “Lorenz” collision was an
author surname in unrelated work.  Nearby nonlinear ODE packages treat
Lotka–Volterra, Rayleigh cavity collapse and oscillator models; none has the
shifted Lorenz absorbing ellipsoid, wing Routh–Hurwitz surface or zero-rate
equilibrium families.  This package is therefore a new local dynamical
subtype, not a relabelled continuation of one earlier article.

## Scope firewall

No target zero or prime tables, local arithmetic, Euler factors, root
numbers, automorphy, target divisor, target functional equation or
Hilbert–Pólya construction enter the source or proof.  Route B remains false.
