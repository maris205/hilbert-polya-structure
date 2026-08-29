# Source and scope audit — HCS-C225

## Authority and provenance

- Baseline source commit: `489672bd36abd3a4f6da92d1446a0af575917959`.
- Route-A evaluator: `flow_systems/skills/route-a-evaluator.md`, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Fixed build epoch: `1787875200` (2026-08-29 release convention).
- No target-prime, target-zero, Euler-factor, root-number, automorphy, or
  Route-B data enter the producer, checker, symbolic audit, or manuscript.

## Literature ledger

1. Karlin and McGregor, “The differential equations of birth-and-death
   processes, and the Stieltjes moment problem,” *Transactions of the AMS* 85
   (1957), 489–546. DOI: `10.1090/S0002-9947-1957-0091566-1`. Used only for the
   classical birth–death spectral representation context.
2. Sven-Erik Ekström, Carlo Garoni, Adam Jozefiak and Jesse Perla,
   “Eigenvalues and eigenvectors of tau matrices with applications to Markov
   processes and economics,” *Linear Algebra and its Applications* 627 (2021),
   41–71. DOI: `10.1016/j.laa.2021.06.005`. Used only for related finite
   Markov-matrix spectral context.
3. Herman Callaert and Julian Keilson, “On exponential ergodicity and spectral
   structure for birth-death processes, II,” *Stochastic Processes and their
   Applications* 1(3) (1973), 217–235. DOI:
   `10.1016/0304-4149(73)90001-X`. Used for recurrence/ergodicity boundary
   vocabulary.

The formulas in this package are re-derived from the finite generator and
checked independently; no priority claim is made.

## Adversarial scope controls

The frozen object is a continuous-time queue semigroup.  Finite characteristic
polynomials are explicitly not infinite Fredholm determinants.  The Jacobi
similarity is labelled a formal finite-dimensional hint, not a target operator.
The infinite-capacity section states only stationary/gap/mass-escape limits and
explicitly declines an unproved continuous-spectrum assertion.
