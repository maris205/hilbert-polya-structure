# Proof Package — HCS-C298

## Claim

Let `A=A^T` be a real `n x n` matrix and let `1<=k<=n-1`.  On rank-`k`
orthogonal projections consider

`dot(P)=[P,[P,A]]`.

The flow has a global exact solution for every real time.  Its Plücker
coordinates scale by the sums of eigenvalues.  For simple spectrum every
Schubert cell has an exact coordinate-plane limit and an exponential rate
determined by the actual second nonzero Plücker weight.  All equilibria,
linear modes, and stable/unstable dimensions are explicit.  For repeated
spectrum the equilibrium sets are complete product-Grassmann Morse--Bott
manifolds and every orbit converges to its eigenflag associated graded.
Finally `Tr(AP)` is strictly increasing off equilibria, so nonconstant
recurrent or periodic trajectories do not exist.

## Status

**PROVABLE AS STATED.**  Frozen obstruction record: `HEN-O282`.

## Assumptions and notation

- `P0=P0^T=P0^2` and `rank(P0)=k`.
- `Q0` is any full-column-rank frame for `V0=Ran(P0)`.
- In an orthonormal eigenbasis, `A e_i=lambda_i e_i`.
- For `I={i_1<...<i_k}`, put `lambda_I=sum_(i in I)lambda_i` and let
  `p_I(V)` be the projective Plücker coordinate.
- `B(V)={I:p_I(V)!=0}` is the set of bases of the representable row matroid
  of a frame for `V`.

No hypothesis says that the numbers `lambda_I` are pairwise distinct.

## Proof strategy and dependency map

1. Differentiate the orthogonal projector onto `exp(tA)V0` to obtain the
   equation and global formula.
2. Apply the induced exterior-power action to obtain exact Plücker scaling.
3. For simple spectrum, apply matroid greedy exchange to the actual support;
   then read limits and rates in the Plücker embedding.
4. Linearize graph coordinates at invariant coordinate planes.
5. For repeated spectrum, choose a basis adapted to the eigenflag and take
   its leading components.  Cross-block modes prove Morse--Bott
   nondegeneracy and give dimension formulas.
6. Differentiate `Tr(AP)` to exclude recurrence.

## Proof

### 1. Global quotient solution

Set `Y(t)=exp(tA)Q0`, `G(t)=Y(t)^T Y(t)`, and

`P(t)=Y(t)G(t)^(-1)Y(t)^T`.

The exponential is invertible, so `Y(t)` has rank `k` and `G(t)` is positive
definite for every real `t`.  Hence the formula is global and is exactly the
orthogonal projection onto `exp(tA)V0`.  Since `Y'=AY` and `A=A^T`, direct
differentiation gives

`P'=AP+PA-2PAP=[P,[P,A]]`.

Uniqueness for the smooth finite-dimensional ODE identifies this formula with
the required solution.

### 2. Exterior powers and tie-safe simple-spectrum limits

In an eigenbasis,

`wedge^k(exp(tA)) e_I = exp(t lambda_I)e_I`.

Thus, projectively,

`p_I(t)=exp(t lambda_I)p_I(0)`

up to one common nonzero scale.

Assume now `lambda_1<...<lambda_n`.  Although arbitrary subset sums can tie,
the supported indices `B(V0)` are the bases of a representable matroid.
Greedy selection with the distinct element weights `lambda_i` has a unique
maximum basis `I_+`: if two optimal bases differed, take the largest-weight
element in their symmetric difference and use strong basis exchange to
increase the basis missing that element, a contradiction.  The same argument
gives a unique minimum basis `I_-`.

Let `F_j=span(e_1,...,e_j)`.  The Schubert cell indexed by
`I=(i_1<...<i_k)` is equivalently the locus whose greedy maximum supported
basis is `I`, or

`dim(V cap F_j)=#{a:i_a<=j}`.

Factoring `exp(t lambda_I)` from the Plücker vector proves

`lim_(t to +infinity) P(t)=P_I`.

The opposite-flag statement, or the same argument for `-A`, gives
`lim_(t to -infinity)P(t)=P_(I_-)`.

If `V0` is not already `E_(I_+)`, define only from actual support

`rho_2=max{lambda_J:J in B(V0), J!=I_+}`,
`Delta_+=lambda_(I_+)-rho_2>0`.

The nonzero coordinates of weight `rho_2` give the first surviving transverse
term, so in Plücker/Fubini--Study distance the error is
`Theta(exp(-Delta_+ t))`.  The Plücker embedding and the orthogonal-projector
chart are smoothly locally bi-Lipschitz; consequently

`lim_(t to infinity) -(1/t)log ||P(t)-P_(I_+)||_F = Delta_+`.

The backward rate is obtained from the actual second-smallest supported
weight.  A coordinate equilibrium has zero error and is assigned infinite
gap.  This formulation neither ignores zero coordinates nor assumes distinct
ambient subset sums.

### 3. Equilibria and simple-spectrum linearization

Relative to `Ran(P) plus Ker(P)`, the off-diagonal block of `A` is `B`, while
`[P,[P,A]]` has off-diagonal blocks `B,B^T`.  Therefore equilibrium is
equivalent to `[P,A]=0`, hence to `Ran(P)` being `A`-invariant.

For simple spectrum these are the coordinate planes `E_I`.  A tangent graph
mode sending selected `e_i`, `i in I`, toward unselected `e_j`, `j notin I`,
scales under the exact solution as

`x_(ji)(t)=exp((lambda_j-lambda_i)t)x_(ji)(0)`

to first order.  Thus

`dim W^s(E_I)=#{(i,j):i in I,j notin I,lambda_j<lambda_i}`,

`dim W^u(E_I)=#{(i,j):i in I,j notin I,lambda_j>lambda_i}`.

Writing `I={i_1<...<i_k}`, the first number is
`sum_a(i_a-a)` and the two dimensions sum to `k(n-k)`.

### 4. Repeated spectrum and associated graded

Write the distinct eigenvalues as `mu_1<...<mu_s`, their eigenspaces as
`E_alpha` of dimensions `m_alpha`, and the ascending eigenflag as
`F_alpha=direct_sum_(beta<=alpha)E_beta`.  Put

`G_alpha=pi_alpha(V0 cap F_alpha) subset E_alpha`,

where `pi_alpha` is orthogonal projection to `E_alpha`.  Its dimension is

`k_alpha=dim(V0 cap F_alpha)-dim(V0 cap F_(alpha-1))`.

Choose a basis of `V0` adapted to the filtration `V0 cap F_alpha`.  The top
nonzero component of each newly added basis vector lies in `G_alpha`; those
top components are independent.  After multiplying by `exp(tA)` and removing
irrelevant scalar factors, lower components decay relative to these top
components.  Hence

`lim_(t to infinity) exp(tA)V0 = direct_sum_alpha G_alpha`.

This is the associated-graded subspace.  In exterior-power language it is the
entire nonzero top-weight component of the initial decomposable Plücker vector,
not an arbitrarily chosen coordinate when weights tie.  The descending
eigenflag gives the backward limit.

Every invariant `k`-plane has an occupancy vector
`(k_1,...,k_s)`, `0<=k_alpha<=m_alpha`, `sum k_alpha=k`, and the complete
critical manifold for that vector is

`product_alpha Gr(k_alpha,E_alpha)`.

Its tangent dimension is `sum_alpha k_alpha(m_alpha-k_alpha)`.  Cross-block
graph modes have nonzero rates `mu_beta-mu_alpha`; within-block modes have
zero rate and are precisely tangent to the product.  Therefore each component
is Morse--Bott, with

`d_s=sum_(beta<alpha) k_alpha(m_beta-k_beta)`,

`d_u=sum_(beta>alpha) k_alpha(m_beta-k_beta)`.

Together with the critical-manifold dimension these sum to `k(n-k)`.

### 5. Strict Lyapunov law and recurrence obstruction

For `Phi(P)=Tr(AP)`, cyclicity of trace and `P^2=P` give

`d Phi/dt=Tr(A[P,[P,A]])=||[P,A]||_F^2>=0`.

Equality holds exactly at an invariant projection.  If a nonconstant forward
orbit were recurrent to its initial point, `Phi` would first increase
strictly and then remain above its initial value, contradicting continuity at
the returning subsequence.  Thus no nonconstant recurrent or periodic orbit
exists.  The explicit associated-graded limit is stronger than this
obstruction.

## Collision and scope boundaries

C185 evolves the full state matrix on a fixed isospectral orbit and uses a
separate ordered target.  C298 fixes the symmetric generator and evolves a
rank-`k` subspace; its exact solution is the induced linear action.  The two
state spaces, invariants, equilibrium atlases, and conclusions are distinct.

The tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the overall verdict is
`ROUTE_A_REJECTED`.  Plücker weights are source exponents, continuous time is
not an arithmetic clock, strict Lyapunov behavior removes an A1 periodic-
orbit bridge, and a symmetric matrix is not thereby a Hilbert--Pólya
operator.  Route B is locked.

Finite evidence is regression evidence only.  It cannot replace matroid
exchange, the adapted-flag proof, or the global projector differentiation.

## Open risks

- If `A` ceases to be symmetric, the orthogonal-projector differentiation no
  longer yields this same double-commutator equation.
- For repeated spectrum, selecting one coordinate from a tied top-weight
  block is generally wrong; the associated-graded subspace is the invariant
  statement.
- Rate gaps must be computed from nonzero Plücker support.  Ambient subset
  lists can contain zeros, ties, and irrelevant weights.
