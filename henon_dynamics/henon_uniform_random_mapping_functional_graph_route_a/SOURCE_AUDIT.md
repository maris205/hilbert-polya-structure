# Source audit

## Primary sources

1. Bernard Harris, “Probability Distributions Related to Random Mappings,”
   *The Annals of Mathematical Statistics* **31** (1960), 1045–1062.
   DOI: <https://doi.org/10.1214/aoms/1177705677>.
2. Philippe Flajolet and Andrew M. Odlyzko, “Random Mapping Statistics,”
   *Advances in Cryptology — EUROCRYPT ’89*, LNCS 434 (1990), 329–354.
   DOI: <https://doi.org/10.1007/3-540-46885-4_34>.

The official publisher/DOI records were checked on 2026-09-01 for authors,
titles, venues, years, and pagination.  Harris is the primary early source for
random-mapping distributions; Flajolet–Odlyzko is the primary systematic
analytic-combinatorics source used for context on mapping statistics and
asymptotics.  The package presents an original source-locked exposition and
executable audit, not a literature-priority claim.

## Claim discipline

The theorem concerns the uniform distribution on all `n^n` functions.  It is
not asserted for conditioned maps, random permutations, random endofunctions
with nonuniform images, or a single deterministic map.  Finite enumeration is
not used to infer the all-`n` statements.  The asymptotic claim is weak
convergence under the stated square-root scaling, with the joint density
normalized on the nonnegative quadrant.

## Integrity and scope audit

- Fabrication: no; every bibliographic field is tied to the DOI records.
- Overclaim: no; classical ownership and the finite-evidence boundary are
  explicit.
- Method inconsistency: no; independent reconstruction differs from the
  producer traversal.
- Irreproducibility: no; fixed epoch, byte replay, deterministic PDFs, and a
  closed manifest are required.
- Cherry-picking: no; every map through `n=7` and every admissible cell is kept.
- Scope creep: no; arithmetic, automorphic, and operator claims are excluded.

## Source and evaluator locks

- source commit: `418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02`
- evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0
- evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- fixed epoch: `1788220800`
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
