# Theorem package

## Frozen spaces

The adjoint wave has data `(u0,u1) in H_0^1(0,L) x L^2(0,L)` and energy

`E=1/2 int_0^L (|u_t|^2+c^2|u_x|^2) dx`.

Its observation is `u_x(L,.)`.  HUM duality gives an `L^2(0,T)` Dirichlet
control at `x=L` for the transposition state space
`L^2(0,L) x H^{-1}(0,L)`, with `x=0` fixed.

## Main theorem — PROVABLE AS STATED

For every `L,c>0`:

1. The least positive time at which the free Dirichlet wave group is the
   identity on its full energy space is `T*=2L/c`.
2. At exactly that time,

   `int_0^T* |u_x(t,L)|^2 dt = 4E(0)/c^3`.

3. Consequently, one-end observability and the dual exact controllability
   hold for every `T>=T*`, including equality.
4. If `T<T*`, there is a nonzero smooth energy solution with
   `u_x(L,t)=0` on `[0,T]`; hence observability and exact controllability fail.

There is no Dirichlet zero mode.  Endpoint reversal, `L,c` scaling, the
critical equality, and `T=0` are explicit.  The theorem does not concern
finite-difference/Galerkin controls, damping, internal control, or variable
coefficients.

## Proof spine

Write every energy solution as
`u(x,t)=F(x+ct)-F(-x+ct)` with `F` `2L`-periodic.  Then
`u_x(L,t)=2F'(L+ct)` and
`E=c^2 int_0^(2L)|F'|^2`.  One traversal gives the exact identity.  If
`cT<2L`, choose a nonzero smooth periodic mean-zero `F'` supported in the
complement of the observed arc `[L,L+cT]`; this gives the strict failure.
Fourier phases `exp(±in pi c t/L)` give the least common revival.  For the
control-adjoint observation `O_T z=c^2 u_x(L,.)`, the critical equality is a
norm identity onto the closed observation range; it does not assert that
`O_T` is onto all of `L^2(0,T)`.  The coercive HUM Gramian `O_T^* O_T`, after
Riesz identification, gives the stated dual control theorem.

Finite modal and arc cells audit constants and endpoint conventions but do
not prove the infinite-dimensional theorem.

## Route-A ceiling

The free wave group has non-isolated periodic families and a natural
Dirichlet-Laplacian quantization, giving only `A1_WEAK` and
`A4_NATURAL_QUANTIZATION`.  There is no rational-prime primitive owner,
target determinant, target divisor, or arithmetic same-clock bridge.
