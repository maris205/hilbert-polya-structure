# C196 proof package: the free rational Calogero--Moser flow

## Main theorem and status

Let `N>=2`, `g>0`, `q_1<...<q_N`, and `p in R^N`.  Set

\[
Q_0=\operatorname{diag}(q),\qquad
(L_0)_{jk}=p_j\delta_{jk}+\frac{ig(1-\delta_{jk})}{q_j-q_k},
\]

and let `x_1(t)<...<x_N(t)` be the ordered eigenvalues of
`X(t)=Q_0+tL_0`.  Then:

1. `X(t)` is simple for every real `t`; `L_0` is also simple.
2. `(x,dot x)` is the unique collision-free complete Hamiltonian solution,
   with `ddot x_j=2g^2 sum_(k!=j)(x_j-x_k)^(-3)`.
3. `Tr L(t)^m=Tr L_0^m` for every `m>=1`, and `Tr L^2=2H`.
4. If `lambda_1<...<lambda_N` are the eigenvalues of `L_0`, normalized
   eigenvectors satisfy the gauge `e^*v_a=1`, and
   `a_a=v_a^*Q_0v_a`, then
   \[
   x_j(t)=t\lambda_j+a_j+O(t^{-1}),\quad
   \dot x_j(t)=\lambda_j+O(t^{-2})\quad(t\to+\infty),
   \]
   \[
   x_j(t)=t\lambda_{N+1-j}+a_{N+1-j}+O(|t|^{-1}),\quad
   \dot x_j(t)=\lambda_{N+1-j}+O(t^{-2})\quad(t\to-\infty).
   \]
   Spectral line `m` enters at rank `N+1-m`, exits at rank `m`, and retains
   its intercept.
5. `(q,p) -> (lambda,a)` is a global bijection.  Its inverse forms
   \[
   \widetilde L=\operatorname{diag}(\lambda),\qquad
   \widetilde Q_{aa}=a_a,\qquad
   \widetilde Q_{ab}=\frac{ig}{\lambda_b-\lambda_a}\quad(a\ne b),
   \]
   then diagonalizes `Q_tilde` and fixes the commutator phase gauge.
6. Every trajectory is unbounded in relative configuration, so no bounded
   nonconstant periodic orbit exists.

Status: `PROVABLE AS STATED` on the declared domain.  This is a
source-derived closure of classical Calogero--Moser/Moser structure, not a
priority claim.  Finite `N<=7` regression does not prove the theorem.

## Proof

### Signs, energy, and simplicity

Hermiticity follows by conjugating `ig/(q_j-q_k)`.  Entrywise multiplication
gives

\[
[Q_0,L_0]=ig(J-I),\qquad
\operatorname{Tr}L_0^2=\sum_jp_j^2+2\sum_{j<k}
\frac{g^2}{(q_j-q_k)^2}=2H.
\]

Since `[X(t),L_0]=ig(J-I)`, compress to an eigenspace `E` of `X(t)`.
Scalar action of `X(t)` yields `P_E[X(t),L_0]P_E=0`, hence
`P_EJP_E=P_E`.  If `dim E>=2`, the two sides have ranks at most one and at
least two, respectively: impossible.  The pencil is simple for all real
time.  Compressing the same commutator to an eigenspace of `L_0` proves its
spectrum simple.

### Physical flow, completeness, and integrals

Let `U(t)` diagonalize `X(t)`.  Diagonal compression shows every component of
`U^*e` has modulus one; gauge them all to one.  For
`L_tilde=U^*L_0U`, the off-diagonal commutator is

\[
(x_j-x_k)(L_{\rm tilde})_{jk}=ig.
\]

Simple Hermitian eigenvalue perturbation gives

\[
\dot x_j=(L_{\rm tilde})_{jj},\qquad
\ddot x_j=2\sum_{k\ne j}\frac{|(L_{\rm tilde})_{kj}|^2}{x_j-x_k}
=2g^2\sum_{k\ne j}(x_j-x_k)^{-3}.
\]

At `t=0`, values and derivatives are `q_j,p_j`.  ODE uniqueness identifies
the pencil with the physical flow.  The all-time simple pencil proves no
collisions and global completeness.  Since `L(t)=U^*L_0U`, every trace power
is constant.

### Global atlas and both ends

For an `L_0` eigenvector `v_a`, diagonal compression gives
`|e^*v_a|=1`; fix `e^*v_a=1`.  In the `L_0` basis,

\[
(\lambda_b-\lambda_a)\widetilde Q_{ab}=ig,
\]

which proves the forward formula.  Conversely, the displayed inverse matrix
is Hermitian and satisfies the same commutator.  The rank argument makes it
simple.  Diagonalize and order it; diagonal compression and a phase gauge
make the transformed commutator vector all ones, forcing transformed
`L_jk=ig/(q_j-q_k)` off diagonal and real `p_j` on the diagonal.  The
constructions are inverse.  Bijectivity is claimed; no unproved symplectic
claim is added.

Nondegenerate Hermitian perturbation of `t(L_0+t^(-1)Q_0)` gives the positive
expansion.  Negative `t` reverses eigenvalue order and gives index `N+1-j`.
Since `lambda_N-lambda_1>0`, relative diameter grows linearly in both time
directions, excluding bounded periodic motion.

## Boundaries and Route-A stop

`g=0` permits free crossings; repeated positions are singular; `N=1` is a
trivial free particle.  Confining, trigonometric, hyperbolic, elliptic, spin,
complex, and quantum spectral variants are outside the theorem.  The natural
positive inverse-square Schrödinger form supports
`A4_NATURAL_QUANTIZATION`, but no target spectrum is identified.

There is no intrinsic rational-prime carrier, bounded primitive-cycle ledger,
source zeta, target divisor, functional equation, or Weil compression.  Thus

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_REJECTED`, Route B false.
