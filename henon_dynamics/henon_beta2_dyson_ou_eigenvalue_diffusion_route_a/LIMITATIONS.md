# Limitations

- The determinant and Slater construction uses beta two. General beta
  diffusions require a different generalized-Hermite theory and are outside
  this package.
- The theorem starts in the open chamber. It proves nonattainment of the
  collision boundary but does not construct an entrance law from that
  boundary.
- Completeness is for the eigenvalue/radial process, not for every
  non-class-function mode of matrix OU.
- The finite receipt reaches $N=16$ for level multiplicities, $N=8$ for
  explicit partition labels, and $N=4$ for high-precision kernels. Those
  cutoffs test code only; the proofs have no such cutoff.
- Generic GUE statistics do not supply arithmetic relevance. The Route-A
  arithmetic, orbit, determinant, and target-analytic gates remain closed.
