# Source and collision audit

## Locks

- Source commit:
  `51fb3d46f96b854314811c1ad62d3103cd5d54e5`.
- Route-A evaluator version `0.2.0`, SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Fixed epoch: `1788220800`.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

No batch document, registry, root README, target table, zero table, Euler
factor, root number, or Route-B artifact was edited or used as mathematical
input.

## Verified literature metadata and exact roles

1. Richard S. Hamilton, “Three-manifolds with positive Ricci curvature,”
   *Journal of Differential Geometry* **17** (1982), 255–306,
   DOI `10.4310/jdg/1214436922`.  The Project Euclid record verifies title,
   author, journal, volume, year, pages, and the original Ricci-flow setting.
   We cite it only for the source equation and historical lineage.
2. Bennett Chow and Dan Knopf, *The Ricci Flow: An Introduction*,
   Mathematical Surveys and Monographs **110**, American Mathematical
   Society, 2004, 325 pages, DOI `10.1090/surv/110`, MR2061425.  The official
   AMS record lists special geometries, limit solutions, singularities, and
   Type-I singularities.  We cite it for standard conventions and background,
   not for an outsourced product theorem.

Every displayed product formula, normalization identity, endpoint integral,
and blowup limit is proved inside this package.  The release claims an exact
source-local synthesis, not invention of Ricci flow, product curvature, or
singularity terminology.

## Internal collision scan

At the frozen pre-release tree, the read-only command

```bash
rg -n -i 'ricci flow|ricci-flow|product of (round )?spheres|product[- ]sphere|homogeneous ricci|geometric evolution' \
  henon_dynamics/docs/candidate_registry.md \
  henon_dynamics/docs/obstruction_registry.md \
  <all prior package README/SOURCE_AUDIT/THEOREM_PACKAGE files>
```

returned no prior owner.  The registry SHA-256 was
`7090dcf027e6ea7b9df5030eaba082897ecfd10deb47b67b4471443ab9fa38da`;
the obstruction-registry SHA-256 was
`e384d1f99b565cb7a3fe6963234615cd414ac7762ba31bfe15f68956731b6692`.

Mechanism-level comparisons were then made explicitly:

- C185 is a Brockett double-bracket flow on an isospectral matrix orbit.  Its
  state is a matrix and its theorem is sorting by a Lyapunov function; it has
  no evolving metric, curvature collapse, or normalized geometric time.
- C270 is a static sub-Riemannian geodesic/cut-locus theorem on the Heisenberg
  group, not a geometric evolution equation.
- C277 is a Caputo Dirichlet heat family on a function space, and C283 is a
  conductor-shell p-adic Markov heat semigroup.  HCS-C281 instead evolves the
  Riemannian metric nonlinearly and contains no heat trace, spectral zeta,
  determinant, or Schatten theorem.
- C133 is a metric-graph unitary-scattering owner.  It was the reason a
  proposed Kirchhoff-star replacement was killed before construction.  The
  present owner has neither graph scattering nor a unitary propagator.
- The retired C281 dimer/RSA directory is untouched.  Random greedy adsorption
  and its jammed combinatorics play no role here.

Thus the retained mechanism—exact homogeneous Ricci evolution, tied geometric
collapse, and volume-normalized singular time—is absent from C1–C280 and is
not a split of C283.

## Claim firewall

- No priority claim beyond this all-parameter packaged synthesis.
- No stability claim for perturbations away from the product family.
- No surgery, quotient, orbifold, or general homogeneous-space theorem.
- No heat-semigroup, zeta, determinant, Schatten, Euler-product, or target-zero
  conclusion.
- No Route-B authorization.
