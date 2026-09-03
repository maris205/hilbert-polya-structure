# C333 exact results

The frozen complete-graph relaxed gossip process has the complete all-time
second-moment solution

\[
M_t=\lambda_0^t\Pi_0A_0+\lambda_1^t\Pi_1A_0+
\lambda_2^t\Pi_2A_0,
\]

with absent low-dimensional blocks omitted.  Their dimensions are
`1`, `N-1`, and `N(N-3)/2`, and

\[
\lambda_0=1-\frac{4\eta(1-\eta)}{N-1},\quad
\lambda_1=1-\frac{4\eta-2\eta^2}{N-1},\quad
\lambda_2=1-\frac{4\eta}{N-1}
+\frac{4\eta^2}{N(N-1)}.
\]

These are invariant orthogonal blocks for all `0<=eta<=1`.  For `eta>0`,
the eigenvalues of every present nonzero block are pairwise distinct, so the
blocks are the corresponding full eigenspaces.  At `eta=0`, the transfer is
the identity and the blocks merge into its eigenvalue-one eigenspace of total
multiplicity `N(N-1)/2`.

The exact statistical covariance subtracts the nonzero first moment:

\[
\operatorname{Cov}(x_t)=M_t-
\left(1-\frac{2\eta}{N-1}\right)^{2t}y_0y_0^{\mathsf T}.
\]

For `0<eta<1`, mean-square disagreement contracts at the exact sharp rate
`lambda0` and convergence to the original average is almost sure.  The
normalized tail event is stated only for `epsilon>0` and `y_0!=0`; consensus-
line data are fixed pathwise.  At `eta=1`, updates are transpositions and
disagreement energy is constant.

## Evidence inventory

- 56 spectral rows;
- 6 explicit projector receipts;
- 48 exhaustive-word rows;
- 4,242 exactly enumerated edge words;
- 2,966 audited scalar leaves;
- evidence SHA-256:
  `29a67f77766c1e40385dd4a1aa4719eba3ec5d2cd3f985a3e3ebdd4cf06baf39`.

Finite evidence is a regression receipt, not proof.  No arithmetic or target-
spectral conclusion is drawn.
