# HCS-C306 theorem package

## Frozen system

Let `L>=1` and `1<=k<=L`.  Before killing, the ordered state is

`W_{L,k}={1<=x_1<...<x_k<=L}`.

Each labeled particle has independent rate-one left and right clocks.  An
attempt to reach `0` or `L+1`, or an attempt to enter another particle's site,
kills the entire system.  Thus a legal one-coordinate move has off-diagonal
rate one and every diagonal entry is `-2k`.  This is a killed process, not a
reflecting or suppressed-jump exclusion chain.

## Master theorem

Define

`phi_r(j)=sqrt(2/(L+1)) sin(pi r j/(L+1))`,

`epsilon_r=2-2 cos(pi r/(L+1))`, for `1<=r,j<=L`.  For every increasing
`k`-tuple `m=(m_1<...<m_k)`, put

`Phi_m(x)=det[phi_{m_a}(x_b)]` and
`Lambda_m=sum_a epsilon_{m_a}`.

Then:

1. `p_t^(1)(i,j)=sum_r exp(-epsilon_r t) phi_r(i)phi_r(j)` is the
   one-particle Dirichlet kernel.
2. The `binom(L,k)` functions `Phi_m` are a complete orthonormal basis of the
   chamber and `Q_k Phi_m=-Lambda_m Phi_m`.
3. The killed kernel has both exact forms

   `P_t(x,y)=det[p_t^(1)(x_i,y_j)]`

   and

   `P_t(x,y)=sum_m exp(-Lambda_m t)Phi_m(x)Phi_m(y)`.
4. With `A_m=sum_y Phi_m(y)`, the whole absorption law is

   `S_x(t)=sum_m exp(-Lambda_m t)Phi_m(x)A_m`,

   `P_x(tau<=t)=1-S_x(t)`, and

   `f_x(t)=sum_m Lambda_m exp(-Lambda_m t)Phi_m(x)A_m`.

   For every integer `r>=1`,

   `E_x[tau^r]=r! sum_m Phi_m(x)A_m/Lambda_m^r`.
5. Orient the lowest Slater mode by
   `h=(-1)^{k(k-1)/2}Phi_(1,...,k)`.  Then `h>0`, `||h||_2=1`, and
   `Lambda_0=sum_{r=1}^k epsilon_r` is simple.  If `k<L`, the next energy is
   `Lambda_1=sum_{r=1}^{k-1}epsilon_r+epsilon_{k+1}`, so

   `S_x(t)=h(x)A_0 exp(-Lambda_0 t)+O_x(exp(-Lambda_1 t))`

   and the same formula after multiplication by `Lambda_0` holds for the
   leading absorption density.
6. The unique QSD and Yaglom limit are `nu(y)=h(y)/A_0`.  The Doob transform
   has `q^h(x,y)=q(x,y)h(y)/h(x)` off diagonal and
   `q^h(x,x)=q(x,x)+Lambda_0`; it is reversible with normalized invariant law
   `pi^h(x)=h(x)^2`.
7. For `k<L` its relaxation gap is

   `epsilon_{k+1}-epsilon_k = 2(cos(k*pi/(L+1))-cos((k+1)*pi/(L+1)))`.

   For `k=L` the conditioned chain is a singleton and has no nonzero
   relaxation mode.

## Proof chain

The one-particle Dirichlet difference equation is diagonalized by discrete
sine orthogonality.  Antisymmetrized tensor products give the Slater
eigenvectors.  Restriction to the ordered chamber has zero collision boundary;
Cauchy--Binet gives orthonormality, and the dimension count gives completeness.
Expanding the one-particle determinant by Cauchy--Binet proves the spectral
kernel.  The equivalent path-switching proof pairs every trajectory at its
first collision with the path obtained by swapping its two colliding tails.

Ground positivity is explicit.  Writing `theta_b=pi*x_b/(L+1)` and using
`sin(a theta)=sin(theta)U_{a-1}(cos theta)`, the leading coefficients of the
Chebyshev polynomials give

`h(x)=(2/(L+1))^(k/2) 2^(k(k-1)/2) prod_b sin(theta_b)
      prod_{i<j}(cos(theta_i)-cos(theta_j))>0`.

Summation, differentiation, and integration of the finite spectral series
give the absorption statements.  Strict increase of the one-particle
energies identifies the first two many-particle energies.  The chamber graph
is connected, so finite Perron--Frobenius gives a simple positive ground
vector and QSD uniqueness.  Symmetry makes the left and right ground vectors
equal.  Finally `Qh=-Lambda_0 h` proves the Doob row sums vanish, and symmetry
gives detailed balance with `h^2`.

## Boundary closure

- `k=1`: the ordinary killed Dirichlet walk.
- `k=L`: one state; every one of `2L` attempts kills; `tau~Exp(2L)`, `h=1`,
  and the Q-process is the stationary singleton.
- `L=k=1`: `Exp(2)`.
- `t=0`: identity kernel and survival one; the initial absorption density is
  the number of illegal rate-one attempts.
- `t->infinity`: the exact leading terms above; for `k=L` they are identities.

Individual coefficients in the finite absorption sum may have signs, although
the semigroup makes the total survival and density nonnegative.  No
first-passage formula beyond these exact finite sums is claimed.

## Evidence and scope

The finite atlas covers all 36 pairs through `L=8`, 502 states, 502 modes, and
273 survival/density probes.  The independent checker uses direct integer
generators and matrix exponentials.  The SymPy lane exactly matches 15
characteristic polynomials and 114 phase-type moment cells.  These checks are
regression evidence; the proof above owns all parameters.

Route-A tuple:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall rejected, Route B
false.  The formal hint records only finite self-adjointness.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, with every target-arithmetic flag false.
