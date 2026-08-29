# Stage 2 report — Papers 97–101

Status: **five theorem-bearing manuscripts and PDFs generated**.
External release: **HOLD**.

## Artifact census

| Paper | Pages | Concrete landed advance | Deterministic control |
|---:|---:|---|---|
| P97 | 5 | recurrent classification, all fixed counts/zeta, exact worst depth on every size layer, extremizers, temporal census, and first-anomaly recovery | 91,509 exact assertions; 10,403 literal states and 17,139 ordered sumset pairs |
| P98 | 4 | affine normal form, repeated-root fixed dimension in every characteristic, exact shift order, all cycles/zeta, and recovery | 152,266 exact polynomial, rank, affine, and full-state assertions over prime and nonprime fields |
| P99 | 4 | HNF cycle decomposition, every fixed count and zeta, prime-power staircase, and index recovery | 93,912 exact assertions over 11,973 canonical HNF states |
| P100 | 5 | digit-sum absorption, exact depth polynomial and coefficients, moments/limits, periodic blindness, and profile rigidity | 46,319,420 exact orbit, convolution, inclusion–exclusion, and rational-moment assertions |
| P101 | 5 | clamp/constant normal form, distribution-free synchronization law, geometric decomposition, endpoint laws, and exact uniform mean diameter | 6,948,361 exact word, rank-gap, law, convolution, and endpoint assertions |

The packet contains **23 pages** and **53,605,468 exact assertions**. The
canonical PDFs total **1,546,730 bytes**. Final digests and uniform
mechanical checks are recorded in `FINAL_QA_REPORT.md` and
`CANONICAL_PDF_MANIFEST.sha256`.

## Paper packages

- [`papers/97-sumset-squaring-dynamics/`](../../papers/97-sumset-squaring-dynamics/)
- [`papers/98-equal-block-sum-torsion-shifts/`](../../papers/98-equal-block-sum-torsion-shifts/)
- [`papers/99-unipotent-shear-sublattice-dynamics/`](../../papers/99-unipotent-shear-sublattice-dynamics/)
- [`papers/100-least-valuation-digit-erasure/`](../../papers/100-least-valuation-digit-erasure/)
- [`papers/101-random-cap-floor-synchronization/`](../../papers/101-random-cap-floor-synchronization/)

Each package contains an anonymous `amsart` manuscript, cited-only
bibliography, canonical PDF, runnable deterministic verifier with stored
output, build instructions, claim/evidence mapping, hostile-review ledger,
final QA, and checksums. No target venue is named and no figure was needed:
the evidence-bearing objects are exact formulas, proofs, and compact tables.

## Claim discipline

- P97 credits Cauchy–Davenport, Vosper, iterated-sumset, and generic zeta
  machinery; the residual claim is the complete special-map package.
- P98 credits algebraic actions, companion networks, finite-field repeated
  roots, and generic finite-system zeta theory.
- P99 credits HNF, finite-index subgroup enumeration, subgroup zeta, and
  Hecke background.
- P100 expressly subtracts Wegner's binary bit-clearing endpoint, classical
  digit-sum laws, iid lattice limits, and generic zeta facts.
- P101 credits iterated random functions, monotone synchronization,
  contraction semigroups, and order-statistic machinery.

The bounded source audit establishes citation and scope hygiene, not
worldwide novelty. Specialist priority clearance remains external-only.
