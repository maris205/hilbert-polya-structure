# Source and scope audit

* Frozen source commit: `0ebc633706bc34b8b915a44749423486fd4cd243`.
* Evaluator authority: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
* Model: unit magnetization sphere in a constant field; parameters are
  nonnegative damping `alpha` and precession `omega`.  The normalized
  Landau--Lifshitz/Gilbert convention absorbs the usual `(1+alpha^2)` factor
  into `omega`/the time unit.
* Allowed data: the displayed vector field, exact ODE identities, rational
  regression probes, and independent symbolic/numeric checks.
* Sealed/forbidden data: target primes or zeros, arithmetic local data, Euler
  factors, root numbers, automorphy, target divisors, and Hilbert--Pólya
  operators.

The alpha=0 periodic face is a continuum of latitude circles; positive
damping is heteroclinic pole flow, and omega=0 is identity.  These are not
merged into an orbit product.  The owner is distinct from Allen--Cahn/Fisher
fronts, NLS solitons, harmonic strobes, Euler tops, Kepler conics, and metric
graph scattering.

The source citation is locked to Lakshmanan, *Philosophical Transactions of
the Royal Society A* 369(1939), 1280--1300 (2011), DOI
`10.1098/rsta.2010.0319`; both stale- and repaired-hash citation mutations
are rejected.  Boundary rows are checked semantically field-by-field (186
independent assertions; 37/37 hostile rejections).
