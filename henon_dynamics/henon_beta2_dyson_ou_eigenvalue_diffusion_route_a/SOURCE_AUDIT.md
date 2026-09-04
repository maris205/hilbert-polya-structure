# Primary-source and collision audit

## Primary-source verification

Publisher/Crossref DOI metadata were fetched on 4 September 2026 with
`Accept: application/x-bibtex`. They confirm the author, title, journal,
volume, issue, pages, and year recorded in `REFERENCES.md` for Dyson,
Karlin--McGregor, Cépa--Lépingle, and Baker--Forrester. NUMDAM's primary
record confirms Grabiner, volume 35(2), pages 177--204, 1999.

Claim ownership is deliberately narrow:

- Dyson owns the matrix-eigenvalue Brownian/Coulomb model lineage.
- Karlin--McGregor and Grabiner own the determinant/reflection lineage for
  noncoinciding paths and Weyl chambers.
- Cépa--Lépingle supplies the standard strong-solution/noncollision context
  for electrostatic repulsion.
- Baker--Forrester supplies generalized-Hermite/Calogero--Sutherland context.
- This package derives the exact $-H/2$ normalization and its combined
  all-$N$ kernel, norm, completeness, trace, and gap theorem explicitly; it
  does not assert historical priority for the individual ingredients.

## Exact registry scan

Command:

```bash
rg -n -i 'Dyson|eigenvalue diffusion' \
  henon_dynamics/README.md \
  henon_dynamics/docs/candidate_registry.md \
  henon_dynamics/docs/obstruction_registry.md \
  henon_dynamics/IDEA_REPORT_C*.md \
  henon_dynamics/BATCH_PLAN_C*.md
```

The only owner-level Dyson--OU hit before C378 is
`IDEA_REPORT_C324_C328.md:239`: it reserves Dyson--OU because a variance
normalization error would contaminate Coulomb drift and the sharp gap. A scan
of top-level package names found no prior Dyson package.

## Nearest-owner exclusions

- `candidate_registry.md:860`, **C196**: deterministic rational
  Calogero--Moser scattering represented by a free Hermitian pencil. C378 is
  a confined stochastic diffusion and has no scattering map.
- `candidate_registry.md:836`, **C200**: scalar Jacobi--Wright--Fisher
  diffusion with shifted-Jacobi spectrum. C378 is an interacting type-$A$
  eigenvalue chamber with a Vandermonde transform.
- `candidate_registry.md:770`, **C237**: hypoelliptic harmonic
  Kramers--Langevin phase-space flow. C378 is elliptic on ordered eigenvalues
  and has reciprocal-gap repulsion.
- `candidate_registry.md:374`, **C306**: killed finite discrete
  nearest-neighbor walkers with a finite Slater spectrum. C378 is continuous,
  conservative after the Doob transform, and has an infinite partition
  spectrum at every fixed $N$.

These distinctions are model-level, not title-level. C378 does not reuse an
existing owner to make a small increment.
