# Proof package

## Claim

For `N>=2`, let `sigma_N` be normalized surface measure on `S^{N-1}(sqrt(N))`.  If `R_ij(theta)` rotates coordinates `i,j`, define

`Q_N f = binom(N,2)^(-1) sum_{i<j} (2pi)^(-1) int_{-pi}^{pi} f(R_ij(theta)v) dtheta`

and `L_N=N(I-Q_N)`.  Then `Q_N` is a self-adjoint positive Markov contraction.  On constants-perpendicular `L2(sigma_N)`,

`gap(L_N)=Delta_N=(N+2)/[2(N-1)]`.

For `N>=3` the slow eigenspace is one-dimensional, spanned by

`F_N(v)=sum_i v_i^4-3N^2/(N+2)`.

At `N=2`, `Q_2` is projection onto constants and every mean-zero function has eigenvalue `2` under `L_2`; the quartic is one such function.  Consequently

`||exp(-tL_N)f||_2 <= exp(-Delta_N t)||f||_2`

for every mean-zero `f`, sharply.  The same theorem holds on `S^{N-1}(sqrt(E))` for every `E>0`, with slow mode `sum_i v_i^4-3E^2/(N+2)` (equivalently, per-coordinate fourth-moment center `3E^2/[N(N+2)]`).  At `E=0` the state space is a single point, so no nonzero mean-zero sector and no positive spectral-gap problem remain.

## Status

PROVABLE AS STATED, with the `N=2` multiplicity and `E=0` degeneracy split explicitly.

## Normalization lock

- Pair selection is uniform over unordered pairs.
- Angle measure is exactly `dtheta/(2pi)`.
- `L_N=N(I-Q_N)` is the positive generator; the master semigroup is `exp(-tL_N)`.
- Energy is `E=N` in the main statement.  It does not change the gap for `E>0`.

## Dependency map

1. Haar invariance makes every pair average an orthogonal projection, hence `Q_N` a positive self-adjoint Markov contraction.
2. Slicing the sphere at one coordinate expresses the `N`-particle quadratic form as an average of `(N-1)`-particle forms.
3. Coordinate projections `P_j` reduce the slicing error to the spectral radius `mu_N` of their average `P`.
4. A one-coordinate conditional operator `K_N` has a complete orthogonal-polynomial spectrum.  Its leading coefficients give `kappa_N=3/(N^2-1)` and the most negative eigenvalue `-1/(N-1)`.
5. The factorization `P=TT*/N` transfers its complete nonzero spectrum to the block Gram operator `T*T/N`; the trivial/standard index branches convert the spectrum of `K_N` into `mu_N`, yielding `Delta_N >= (1-kappa_N)Delta_{N-1}`.
6. The two-particle base and a telescoping product give the exact lower bound.
7. Direct angular averaging makes the centered quartic an eigenfunction at the lower-bound value, proving equality and sharp decay.

## Proof

### 1. Operator structure

For each pair, angular averaging over its circle action is the orthogonal projection onto the functions invariant under that rotation.  Denote it by `Q_ij`.  Thus `Q_N` is the average of positive self-adjoint contractions `Q_ij`, preserves constants and positivity, and is a contraction.  Constants are its only common fixed functions because coordinate-plane rotations generate `SO(N)`, which acts transitively on the positive-radius sphere.

Let

`lambda_N=sup{<f,Q_N f>: ||f||_2=1, <f,1>=0}`,

so `Delta_N=N(1-lambda_N)`.

### 2. The slicing inequality

Let `P_j f=E[f|v_j]` and `P=N^{-1}sum_j P_j`.  Fixing `v_j=y` leaves an `(N-1)`-coordinate sphere.  Each pair appears in exactly `N-2` of the `N` slices, and

`(1/N)(N-2)/binom(N-1,2)=1/binom(N,2)`.

Therefore

`<f,Q_N f>=(1/N)sum_j int <f_{j,y},Q_{N-1}f_{j,y}> dnu_N(y)`.

Center each slice by its scalar mean `P_j f(y)`.  Applying `lambda_{N-1}` to the centered part and using `Q_{N-1}1=1` gives

`<f,Q_N f> <= lambda_{N-1}||f||^2+(1-lambda_{N-1})<f,Pf>`.

If `mu_N` is the supremum of `<f,Pf>` over unit mean-zero `f`, then

`lambda_N <= lambda_{N-1}+(1-lambda_{N-1})mu_N`.  (1)

### 3. Exact coordinate correlation

On one-coordinate functions define `K_N` by

`(K_N g)(x)=E[g(v_2)|v_1=x]`.

At radius `sqrt(N)`, conditional spherical moments give

`K_N(x^{2r}) = c_{r,N}(N-x^2)^r`,

where

`c_{r,N}=(2r-1)!!/[(N-1)(N+1)...(N+2r-3)]`,

and `K_N` kills odd functions.  The even polynomial spaces are invariant.  Since `K_N` is self-adjoint and polynomials are dense for the compact one-coordinate marginal, it has a complete orthogonal-polynomial eigenbasis with

`alpha_0=1`, `alpha_(2r)=(-1)^r c_{r,N}`, and odd eigenvalues zero.

The ratio `|alpha_(2r+2)/alpha_(2r)|=(2r+1)/(N+2r-1)<1` for `N>=3`.  Hence on constants-perpendicular functions the largest eigenvalue is

`kappa_N=alpha_4=3/(N^2-1)`,

and the smallest is `alpha_2=-1/(N-1)`.

We transfer this one-coordinate spectrum without assuming that `P` has only point spectrum.  Put `H_0=L^2_0(nu_N)` and define the bounded operator

`T:H_0^N -> L^2_0(sigma_N)`, `T(h_1,...,h_N)=sum_j h_j(v_j)`.

Its adjoint is `T*f=(P_1f,...,P_Nf)`, hence `P=TT*/N`.  The standard polar-decomposition identity gives equality of the nonzero spectra (with eigenspace multiplicities) of `TT*/N` and `T*T/N`; explicitly, an eigenvector of either side is carried to the other by `T*` or `T`.  More generally the resolvent identity for `z != 0`,

`(TT*-z)^(-1)=-z^(-1)I+z^(-1)T(T*T-z)^(-1)T*`,

excludes missing continuous or approximate spectrum.

The block matrix of `T*T/N` has diagonal `I/N` and every off-diagonal block `K_N/N`.  For a `K_N` eigenfunction with eigenvalue `alpha`, the coordinate-index space splits orthogonally as the trivial line `span{(1,...,1)}` and the standard subspace `sum_j a_j=0`.  The corresponding eigenvalues are

`[1+(N-1)alpha]/N` and `[1-alpha]/N`,

respectively.  The complete polynomial spectral resolution of `K_N` makes these blocks a complete resolution of `T*T/N`; its branch eigenvalues tend only to `1/N` (which is already the infinite-multiplicity odd block), so no continuous or approximate branch can lie above their supremum.  Any extra spectral point of `P` is only `0` from `ker T*`.

On `H_0`, the symmetric branch is maximized by `alpha=kappa_N`, while the standard branch is maximized by `alpha=alpha_2`.  Thus the largest mean-zero spectral value of `P` is

`mu_N=max{[1+(N-1)kappa_N]/N, [1- alpha_2]/N}`

`=[1+(N-1)kappa_N]/N=(N+4)/[N(N+1)]`,

The competing standard value is `1/(N-1)`, strictly smaller for `N>2`; simplicity of `alpha_4` and of the trivial index line proves the asserted one-dimensionality.

### 4. Gap induction and exact closure

Substitute `mu_N` into (1).  Since `Delta_N=N(1-lambda_N)`,

`Delta_N >= [N/(N-1)](1-mu_N)Delta_(N-1)`

`=(1-kappa_N)Delta_(N-1)`

`=[(N-2)(N+2)/((N-1)(N+1))]Delta_(N-1)`.  (2)

For `N=2`, the only pair is averaged over the whole circle, so `Q_2` is projection onto constants, `lambda_2=0`, and `Delta_2=2`.  Iterating (2),

`Delta_N >= 2 prod_{j=3}^N [(j-2)(j+2)/((j-1)(j+1))]`

`=2 (N+2)/[4(N-1)]=(N+2)/[2(N-1)]`.  (3)

Now use the uniform angular identities

`average[(u cos theta+v sin theta)^4+(-u sin theta+v cos theta)^4]`

`=(3/4)(u^2+v^2)^2`

and `E_sigma[v_i^4]=3N/(N+2)`.  Summing over unordered pairs yields

`Q_N F_N=[1-(N+2)/(2N(N-1))]F_N`.

Therefore `L_N F_N=(N+2)F_N/[2(N-1)]`, which meets (3), proving equality.  For `N>=3`, equality through the induction forces equality in the `P` variational step, whose top eigenspace was shown one-dimensional; hence the slow eigenspace is exactly the span of `F_N`.  At `N=2`, the base projection has the explicitly stated larger multiplicity.

### 5. Semigroup and energy boundaries

The spectral theorem for the nonnegative self-adjoint `L_N` gives the displayed `L2` decay on constants-perpendicular functions.  The quartic mode makes it sharp (`N=2` has equality for every mean-zero function).  Scaling `v -> sqrt(E/N)v` unitarily conjugates every positive-energy walk and leaves the gap unchanged.  At `E=0`, the sphere collapses to one point; the mean-zero Hilbert space is `{0}`, so the positive-energy gap statement is not assigned a fictitious value there.

## Evidence boundary and nonclaims

Finite polynomial matrices do not prove the infinite-dimensional lower bound; they audit its algebra.  No full spectrum, entropy-production rate, nonlinear Boltzmann convergence theorem, nonuniform angular law, momentum-conserving three-dimensional model, or literature priority is asserted.

## Route-A boundary

The tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`.  The natural self-adjoint collision generator supplies only the formal lift hint; it is not a unitary/scattering/Hamiltonian quantization and carries no arithmetic orbit bridge.  Route B is locked.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
