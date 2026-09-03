# Source audit

The theorem and normalization were checked against primary sources.

- M. Kac, “Foundations of kinetic theory,” in *Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability*, vol. III (1956), 171–197; UC Berkeley Library record `112857`.  Used for the collision model and master-equation lineage.
- E. A. Carlen, M. C. Carvalho, and M. Loss, “Determination of the spectral gap for Kac's master equation and related stochastic evolution,” *Acta Mathematica* 191 (2003), 1–54, DOI `10.1007/BF02392695`, accessible preprint `arXiv:math-ph/0109003`.  Used for the exact conditional-expectation induction, correlation constant, and sharp quartic mode.

The normalization is locked explicitly.  `Q_N` is the average over the `binom(N,2)` unordered pairs and the probability measure `dtheta/(2pi)`; the positive generator is `L_N=N(I-Q_N)`.  Omitting the factor `N` gives the one-step gap instead and changes every displayed rate by that factor.  The energy `E=N` only fixes the sphere radius; all `E>0` versions are unitarily conjugate by scaling.

No priority claim is made.  The package reproduces the lower-bound induction in full enough detail to audit every constant, while attributing its architecture and theorem to Carlen–Carvalho–Loss.  No source supports an arithmetic, Euler-factor, root-number, automorphy, divisor, functional-equation, zero, or Hilbert–Pólya claim.
