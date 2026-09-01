# Source audit

## Primary source

- Erik Sparre Andersen, “On the fluctuations of sums of random variables,”
  *Mathematica Scandinavica* **1** (1953), 263–285.
- DOI: <https://doi.org/10.7146/math.scand.a-10385>
- Official journal record: <https://www.mscand.dk/article/view/10385>

The journal record supplies the author, title, volume, year, page range, and
DOI used in the paper and evidence payload.  The package cites this work for
the classical fluctuation/permutation theorem and makes no literature-priority
claim.

## Claim discipline

The package proves a carefully frozen specialization: iid real increments,
continuous law, and symmetry about zero.  It does not claim the most general
exchangeable form of the original theory.  Continuity is used twice: every
finite partial sum is nonzero almost surely, and the maximum over
`S_0,...,S_n` is unique almost surely.

The finite sign/permutation controls use deterministic superincreasing
magnitudes.  They audit the combinatorics and conventions but are not offered
as evidence that finitely many distributions imply a universal theorem.

## Source and evaluator locks

- source commit: `9cb7483e97ef82fdc06d45ecb3043f183ce22391`
- evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0
- evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- fixed epoch: `1788134400`
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
