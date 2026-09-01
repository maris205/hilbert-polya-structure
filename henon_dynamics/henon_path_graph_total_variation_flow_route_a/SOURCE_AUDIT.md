# Source audit

## Registered references

1. Haim Brezis, *Operateurs maximaux monotones et semi-groupes de
   contractions dans les espaces de Hilbert*, North-Holland Mathematics
   Studies 5, 1973, MR0348562.  The AMS bibliographic record confirms the
   author, title, series, publisher, year, and Mathematical Reviews identifier:
   <https://mathscinet.ams.org/mathscinet-getitem?mr=0348562>.
2. Leonid I. Rudin, Stanley Osher, and Emad Fatemi, “Nonlinear total variation
   based noise removal algorithms,” *Physica D* **60** (1992), 259--268.
   DOI: <https://doi.org/10.1016/0167-2789(92)90242-F>.  The official Elsevier
   page confirms title, authors, volume, page range, date, and DOI.
3. Clemens Kirisits, Otmar Scherzer, and Eric Setterqvist, “Invariant
   phi-Minimal Sets and Total Variation Denoising on Graphs,” *SIAM Journal on
   Imaging Sciences* **12**(4) (2019), 1643--1668.  DOI:
   <https://doi.org/10.1137/19M124126X>.  The official SIAM record confirms the
   complete metadata and explicitly frames full flow/ROF equivalence as a
   one-dimensional fact that does not extend to general graphs without extra
   conditions.
4. Jose M. Mazon, Marcos Solera, and Julian Toledo, “The Total Variation Flow
   in Metric Random Walk Spaces,” *Calculus of Variations and Partial
   Differential Equations* **59** (2020), article 29.  DOI:
   <https://doi.org/10.1007/s00526-019-1684-z>.  The article proves general
   existence/uniqueness and finite-time arrival at the mean for finite weighted
   connected graphs; this package supplies its own sharper path event proof.
5. Gabriele Steidl, Joachim Weickert, Thomas Brox, Pavel Mrázek, and Martin
   Welk, “On the Equivalence of Soft Wavelet Shrinkage, Total Variation
   Diffusion, Total Variation Regularization, and SIDEs,” *SIAM Journal on
   Numerical Analysis* **42**(2) (2004), 686--713.  DOI:
   <https://doi.org/10.1137/S0036142903422429>.  The official SIAM abstract
   explicitly proves identity of space-discrete one-dimensional TV diffusion
   and TV regularization.  The present package therefore claims no priority
   for the flow--ROF equivalence itself.
6. Holger Hoefling, “A Path Algorithm for the Fused Lasso Signal
   Approximator,” *Journal of Computational and Graphical Statistics*
   **19**(4) (2010), 984--1006.  DOI:
   <https://doi.org/10.1198/jcgs.2010.09208>.  This is direct path-algorithm
   and monotone-fusion precedent; no novelty credit is assigned here to fusion
   after collision.
7. Jerome Friedman, Trevor Hastie, Holger Hoefling, and Robert Tibshirani,
   “Pathwise Coordinate Optimization,” *Annals of Applied Statistics* **1**
   (2007), 302--332.  DOI: <https://doi.org/10.1214/07-AOAS131>.  It supplies
   broader fused-lasso algorithmic context, not a proof dependency.

The first four core records are locked in executable evidence.  All seven are
hash-bound by the release manifest; Steidl et al. and Hoefling are also cited
in the manuscript at the precise prior-art boundary.  They provide provenance
and context, not a novelty guarantee.  Every displayed formula in the package
is nevertheless proved under the frozen incidence and Euclidean conventions.

## Retained source-local residual

The equivalence theorem, the general phenomenon of monotone fusion, and
fused-lasso path algorithms are prior work and receive zero novelty credit.
What remains useful here is a compact, convention-complete certificate that
puts the explicit plateau flux and velocity, joint chained/disjoint
collisions, the `n-1` event bound, a finite-consensus estimate, and the
averaged-subgradient KKT proof into one path theorem with independent exact
reconstruction and hostile semantic testing.  This is an internal theorem
closure and reproducibility result, not a literature-level originality claim.

## Source and originality boundary

The manuscript paraphrases the literature and derives its theorem directly.
No long quotation is retained.  Search-based phrase screening cannot cover
inaccessible or non-indexed literature and is not presented as a plagiarism
certificate.

Source commit: `51fb3d46f96b854314811c1ad62d3103cd5d54e5`;
evaluator v0.2.0 SHA:
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
epoch: `1788220800`; scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
