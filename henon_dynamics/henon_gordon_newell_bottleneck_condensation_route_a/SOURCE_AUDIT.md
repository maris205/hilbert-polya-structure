# Source, ownership, and collision audit

## Frozen repository source

- Candidate: `HCS-C285`
- Source commit: `3878fa5282ca89f75700b3ef9d623f54dcb7bcf9`
- Evaluation date: `2026-09-02`
- Fixed epoch: `1788307200`
- Evaluator: `route-a-evaluator` v0.2.0, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`

## Verified authoritative sources

1. William J. Gordon and Gordon F. Newell, “Closed Queuing Systems with
   Exponential Servers,” *Operations Research* **15**(2), 254–265 (1967),
   DOI [`10.1287/opre.15.2.254`](https://doi.org/10.1287/opre.15.2.254).
   The INFORMS publisher record gives both authors, the 1 April 1967 online
   publication date, volume/issue/pages, and an abstract explicitly covering
   fixed-population interconnected exponential-service stages, equilibrium
   joint distributions, and regulation by the slowest effective stage or
   stages. This is the classical product-form and bottleneck owner.

2. F. P. Kelly, *Reversibility and Stochastic Networks*, Wiley, Chichester,
   1979; reprinted 1987 and 1994; Cambridge University Press reissue, 2011,
   ISBN `978-1-107-40115-0`. Kelly’s University of Cambridge page makes the
   1979 edition available with copyright permission and lists chapters on
   Markov reversibility, migration processes, and queueing networks. This is
   used for reversal vocabulary and lineage.

3. Frank Kelly and Elena Yudovina, *Stochastic Networks*, Cambridge
   University Press, 2014, book DOI
   [`10.1017/CBO9781139565363`](https://doi.org/10.1017/CBO9781139565363),
   online ISBN `9781139565363`, hardback ISBN `9781107035775`, paperback ISBN
   `9781107691704`. The publisher lists Chapter 2, “Queueing networks,” pages
   22–48. This is a modern authoritative framing source.

No BibTeX or metadata was generated from memory. The first and third records
were checked against publisher pages; Kelly’s edition history and authorized
online text were checked against his Cambridge Statistical Laboratory page
and Cambridge frontmatter.

## Ownership boundary

The manuscript states prominently that Gordon–Newell product form and the
classical bottleneck principle are not new claims. The source-local theorem
package contributes no novelty assertion about those results. Its deliverable
is a self-contained synthesis that simultaneously freezes nonreversible
routing, all occupancy derivatives, event flows, exact reversal, tied
Dirichlet condensation, singular faces, and an independently reconstructible
certificate.

## Full-registry collision scan

The candidate registry and obstruction registry were searched through
HCS-C283 for `queue`, `routing`, `Markov`, `product form`, `condensation`,
`Dirichlet`, `network`, and nearby stochastic mechanisms. No Gordon–Newell or
closed many-station routed canonical owner was returned. The nearest entries
are materially different:

- **C225**: a single finite-capacity M/M/1/K birth–death chain, whose theorem
  is spectral diagonalization and mixing. It has no conserved population
  distributed over a routed network and no bottleneck thermodynamic limit.
- **C263**: a reinforced multicolor Pólya urn, with Dirichlet–multinomial and
  de Finetti laws. Its Dirichlet variable is a reinforcement mixing law, not
  the macroscopic allocation of a tied canonical bottleneck set.
- **C220**: open boundary-driven TASEP with a noncommutative matrix Ansatz,
  not a Gordon–Newell monomial product measure.
- **C246**: a one-dimensional AIMD PDMP and perpetuity/renewal owner.
- **C282**: a killed compound-Poisson risk process and first-passage owner.
- **C181**: deterministic rotor-router dynamics on a directed graph; directed
  routing is shared vocabulary, but neither exponential service, traffic
  equations, canonical occupancy, nor stochastic time reversal is shared.
- **C183/C171**: finite Markov spectral packages (random transpositions and
  Ehrenfest), not queueing-network product-form/condensation packages.

This is not a split, continuation, or near-duplicate of C225, C263, C220,
C246, C282, or C181.

## Claim/source separation

- Source-owned: classical Gordon–Newell equilibrium lineage, standard CTMC
  reversal vocabulary, and general queueing-network context.
- Proved in the paper: every displayed formula and boundary statement for the
  frozen owner, including the elementary complete-homogeneous asymptotic and
  tied conditional-composition proof.
- Finite evidence only: 9 selected networks, 177 exact states, moment cells,
  finite `N<=32` condensation cells, and hostile software checks.
- Not claimed: literature originality, multiclass/product-form generality,
  zero-service or reducible extensions, target arithmetic, Euler factors,
  root numbers, target zeros, or a Hilbert–Pólya operator.
