# Complete-graph relaxed randomized-gossip theorem

Let `N>=2`, let `0<=eta<=1`, and start from deterministic `x_0 in R^N`.
At every discrete time choose one unordered pair `{i,j}` uniformly and
independently, and set

\[
x_{t+1}=W_{ij}x_t,\qquad
W_{ij}=I-\eta d_{ij}d_{ij}^{\mathsf T},\qquad d_{ij}=e_i-e_j.
\]

Put `P=I-J/N`, `y_t=Px_t`, and
`mu=1-2 eta/(N-1)`.  Then the mean is preserved pathwise and

\[
\mathbb E y_t=\mu^t y_0.
\]

For a centered symmetric matrix `A=PAP`, define

\[
\Pi_0A={\operatorname{tr}A\over N-1}P.
\]

For `N>2`, put `R=A-Pi_0 A`,
`u=N diag(R)/(N-2)`,

\[
\Pi_1A=P\operatorname{diag}(u)P,\qquad
\Pi_2A=A-\Pi_0A-\Pi_1A.
\]

These are pairwise orthogonal projectors onto invariant spaces of dimensions
`1`, `N-1`, and `N(N-3)/2`.  For `N=3`, `Pi_2=0`; for `N=2`, only the
scalar block occurs.  The second-moment transfer acts on the three blocks by

\[
\lambda_0=1-{4\eta(1-\eta)\over N-1},
\]
\[
\lambda_1=1-{4\eta-2\eta^2\over N-1},\qquad
\lambda_2=1-{4\eta\over N-1}+{4\eta^2\over N(N-1)}.
\]

The three spaces are invariant orthogonal blocks for every declared `eta`.
For `eta>0`, all eigenvalues attached to present nonzero blocks are distinct:

\[
\lambda_0-\lambda_1={2\eta^2\over N-1}>0,
\qquad
\lambda_1-\lambda_2={2\eta^2(N-2)\over N(N-1)}>0,
\]

with the second comparison used only when the third block is present.  Hence
each present block is then the full eigenspace for its displayed eigenvalue.
At `eta=0`, however, the transfer is the identity: all present invariant
blocks merge into the eigenvalue-one eigenspace, whose total multiplicity is
`N(N-1)/2`.

Consequently, for `A_0=y_0 y_0^T`,

\[
M_t:=\mathbb E[y_ty_t^{\mathsf T}]
=\sum_{r=0}^2\lambda_r^t\Pi_rA_0,
\]

with absent low-dimensional blocks omitted, and the statistical covariance is

\[
\operatorname{Cov}(x_t)=M_t-\mu^{2t}y_0y_0^{\mathsf T}.
\]

The exact sharp energy law is

\[
\mathbb E\|y_t\|^2=\lambda_0^t\|y_0\|^2.
\]

For `0<eta<1`, `epsilon>0`, and nonzero `y_0`, this gives

\[
\Pr\{\|y_t\|\ge\varepsilon\|y_0\|\}
\le\lambda_0^t/\varepsilon^2
\]

The consensus-line case `y_0=0` is fixed pathwise and is excluded only from
this normalized tail event.  Almost-sure convergence to the initial average
holds for every initial vector.  At `eta=0` the map and second-moment transfer
are the identity, with the merged multiplicity just stated.  At `eta=1` every
update is a transposition, disagreement energy
is constant, and non-consensus data do not define a consensus algorithm.  For
`N=2`, the sole difference is multiplied by `1-2 eta`; at `eta=1/2` consensus
occurs in one step.  `N=1` is a separately defined static process.

The theorem is analytic for every declared parameter.  The finite exact grid
is a regression certificate, not its proof.
