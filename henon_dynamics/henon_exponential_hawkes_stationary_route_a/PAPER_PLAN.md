# Paper plan

## Title

*Affine Transforms, Three Covariances, and Borel Clusters of an Exponential
Hawkes Process*

## Claims–evidence map

| claim | proof | executable evidence |
|---|---|---|
| joint affine transform | backward generator | generic SymPy coefficient check |
| stationary Laplace law | cluster existence + stationary generator | exact transform-series controls |
| all moments | triangular generator recurrence | 3,520 exact cells |
| intensity covariance | conditional mean | independent second-moment reconstruction |
| counting covariance and spectrum | complete point covariance + Fourier inversion | rational spectrum decomposition |
| window variance | square-integral of covariance measure | 3,200 Maclaurin cells |
| Borel clusters | Galton--Watson Lagrange inversion | 160 rooted-tree rows |
| Route-A rejection | source-owner audit | evaluator and hostile mutations |

## Revision ladder

- Round 0: owner, affine transform, stationary Laplace law, all moments.
- Round 1: add the full three-covariance separation, Bartlett convention, and
  window variance.
- Round 2: add Borel genealogy, parameter boundary atlas, executable evidence,
  collision audit, and strict Route-A conclusion.

No figure is needed: exact displayed equations and one object-separation table
are more informative than a decorative plot.
