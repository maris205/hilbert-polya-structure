# C185 theorem package

## 1. Frozen family

Fix `n>=2`, strictly ordered real numbers

\[
\lambda_1<\cdots<\lambda_n,
\qquad
\nu_1<\cdots<\nu_n,
\]

and put `Lambda=diag(lambda_1,...,lambda_n)` and
`N=diag(nu_1,...,nu_n)`.  The phase space is the compact orthogonal orbit

\[
\mathcal O_\Lambda=\{Q\Lambda Q^{\mathsf T}:Q\in O(n)\}.
\]

On this orbit consider

\[
\dot H=[H,[H,N]]. \tag{1}
\]

The simple-spectrum and strict-target hypotheses are part of the theorem.
Repeated spectra are treated separately in Section 7.

## 2. All-size theorem

**Theorem C185.**  Equation (1) has the following properties for every frozen
family above.

1. Every solution exists for all real time and remains in
   `mathcal O_Lambda`; in particular, the full spectrum of `H(t)` is constant.
2. For `F(H)=Tr(HN)`,

   \[
   \frac{d}{dt}F(H(t))=\lVert[H,N]\rVert_F^2. \tag{2}
   \]

   Equality holds exactly at an equilibrium.
3. The equilibria are exactly

   \[
   D_\pi=\operatorname{diag}
   (\lambda_{\pi(1)},\ldots,\lambda_{\pi(n)}),
   \qquad \pi\in S_n,
   \]

   hence there are `n!` of them.
4. At `D_pi`, each symmetric off-diagonal pair mode `X_ij=X_ji`
   evolves to first order with rate

   \[
   \rho_{ij}(\pi)=
   (\lambda_{\pi(i)}-\lambda_{\pi(j)})(\nu_j-\nu_i),
   \qquad i<j. \tag{3}
   \]

   No rate vanishes.  The ascent flow has `inv(pi)` unstable modes and
   `binom(n,2)-inv(pi)` stable modes.  Equivalently, the ordinary Morse index
   of the sorting energy `-F` is `inv(pi)`.
5. Every trajectory converges to one permutation equilibrium.  Outside the
   finite union of stable manifolds of the nonsorted equilibria, the limit is

   \[
   D_{\mathrm{sort}}=\operatorname{diag}
   (\lambda_1,\ldots,\lambda_n).
   \]

   Thus the sorting basin is open and has full orbit volume.
6. There is no nonconstant recurrent trajectory and therefore no nonconstant
   periodic orbit.

## 3. Proof of global existence and isospectrality

Set `K(H)=[H,N]`.  Since `H` and `N` are symmetric, `K(H)` is skew-symmetric,
and (1) has Lax form

\[
\dot H=[H,K(H)].
\]

Let `Q` solve `dot Q=-K(H)Q`, with a consistent left/right convention chosen
so that `H=Q Lambda Q^T`.  The skew generator keeps `Q` orthogonal, and direct
differentiation recovers (1).  Hence the orbit and every spectral trace
`Tr(H^r)` are invariant.  A smooth vector field on the compact orbit is
complete, proving global existence.

The sign convention for `Q` is immaterial to the spectral conclusion; the
matrix equation itself is the frozen authority.

## 4. Proof of the Lyapunov identity and equilibria

Write `K=[H,N]`.  Cyclicity of trace gives

\[
\begin{aligned}
\frac{d}{dt}\operatorname{Tr}(HN)
 &=\operatorname{Tr}([H,K]N)\\
 &=\operatorname{Tr}(K[N,H])
 =-\operatorname{Tr}(K^2)
 =\lVert K\rVert_F^2.
\end{aligned}
\]

For a skew matrix, `-Tr(K^2)=||K||_F^2`, proving (2).  At an equilibrium the
left side vanishes, so `[H,N]=0`.  Conversely, commutation makes the vector
field zero.  Because `N` has distinct diagonal entries, every commuting
symmetric `H` is diagonal.  The simple orbit spectrum then forces its diagonal
to be a permutation of the `lambda_i`, proving the exact `n!` count.

## 5. Pair linearization and inversion index

At `D=D_pi`, write `H=D+epsilon X`.  Since `[D,N]=0`, the coefficient of
`epsilon` in the vector field is

\[
L_DX=[D,[X,N]].
\]

Every tangent vector has arbitrary symmetric off-diagonal entries and zero
diagonal entries.  Entrywise,

\[
(L_DX)_{ij}=(D_{ii}-D_{jj})(\nu_j-\nu_i)X_{ij},
\]

which is (3).  For `i<j`, the second factor is positive.  The rate is positive
exactly when `pi(i)>pi(j)`, so positive modes are in bijection with inversions.
The flow is gradient ascent for `F`; consequently the negative Hessian
directions of `-F` are exactly those positive modes.  This proves the stated
Morse index without invoking any cell-closure theorem.

The rearrangement inequality gives a unique maximum of `F` at the increasing
alignment and a unique minimum at the reversed alignment.  Formula (3) makes
the maximum the only asymptotically stable equilibrium.

## 6. Convergence and recurrence obstruction

The bounded monotone function `F(H(t))` has a limit.  LaSalle's invariance
principle places every omega-limit set inside `[H,N]=0`.  That set contains
only the `n!` equilibria.  An omega-limit set of a precompact continuous orbit
is connected, so it consists of one equilibrium; hence every trajectory
converges.

All equilibria are hyperbolic by (3).  The stable manifold theorem gives each
nonsorted equilibrium a stable manifold of dimension strictly smaller than
`binom(n,2)`.  Their finite union has orbit volume zero.  Every remaining
initial point converges to the unique stable sorted equilibrium.  This is the
generic convergence claim; no Bruhat or Schubert closure description is used.

For a nonconstant trajectory, (2) is strictly positive at every time.  A
recurrent return to the initial point would force `F` to return to its initial
value, contradicting strict monotonicity.  Periodicity is a special case.

## 7. Repeated-spectrum boundary

If the source spectrum repeats, distinct permutations may represent the same
diagonal point.  Formula (3) can then vanish for an equal-eigenvalue pair, but
that pair is a stabilizer/non-tangent direction on the lower-dimensional
orbit, not a genuine tangent zero mode.  If `N` repeats, rotations inside a
repeated `N`-eigenspace commute with `N`, producing genuine tangent zero modes
and continuous equilibrium families.  The evidence includes exact `3x3`
sentinels for both effects.

These degeneracies form a separate repeated-spectrum boundary; the
target-degenerate component exhibits the Morse--Bott phenomenon.  The package
does not claim its full classification and does not claim any Bruhat/Schubert
cell-closure theorem.  Global existence, isospectrality, and the nonnegative
identity (2) persist, but the `n!`, hyperbolicity, and inversion-index statements
belong only to the frozen simple/strict theorem.

## 8. Exact finite validation

For `2<=n<=7`, the producer uses source spectrum `1,...,n` and target diagonal
`1^2,...,n^2`.  It enumerates all 5,912 permutations and all 118,004 pair modes.
For six independent rational orthogonal samples it verifies spectral traces,
skew/symmetric types, and (2) using exact fractions.  The checker imports no
producer code.  SymPy reconstructs the symbolic `3x3` Lyapunov and
linearization identities and independently traverses the finite ledger.

These rows are regression evidence, not the proof of the theorem.

## 9. Route-A result

- **A0_FAIL.**  Arbitrary real source and target spectra have no intrinsic
  rational-prime or prime-power origin, carrier, or logarithmic clock.
- **A1_FAIL.**  There is no nonconstant periodic orbit, much less a primitive
  orbit carrying an A0 arithmetic payload.
- **A2_FAIL.**  Local tangent characteristic polynomials are not a global
  source-owned dynamical determinant, and no target divisor is compared.
- **A3_FAIL.**  No target functional equation, counting law, continuation, or
  Weil compression is present.
- **A4_FORMAL_HINT.**  The state-dependent skew Lax generator produces
  orthogonal conjugation along a trajectory, but it is not a fixed linear
  quantum operator with the same clock.

The overall verdict is `ROUTE_A_REJECTED`; Route B is false.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## 10. Nonclaims

No novelty is claimed for the Brockett flow.  No full repeated-spectrum or
Bruhat/Schubert theorem, arithmetic local structure, Euler factor, root number,
automorphy, target divisor, Weil compression, Hilbert--Polya operator, Route-B
authorization, external peer review, or acceptance score is asserted.
