# Theorem package

## Frozen realization

For `alpha in R`, let `H_alpha` be associated with

`q_alpha[psi]=int_R |psi'|^2 dx + alpha |psi(0)|^2`, `Dom(q)=H^1(R)`.

Equivalently, `H_alpha psi=-psi''` off zero on functions in
`H^2(R\{0})` which are continuous at zero and satisfy
`psi'(0+)-psi'(0-)=alpha psi(0)`.

## Main theorem — PROVABLE AS STATED

1. The form is closed and lower bounded, and defines the above self-adjoint
   operator.
2. For `kappa>0` and `2 kappa+alpha !=0`,

   `R_alpha(-kappa^2;x,y)=[exp(-kappa|x-y|)-alpha exp(-kappa(|x|+|y|))/(2kappa+alpha)]/(2kappa)`.

3. The essential spectrum is `[0,infinity)` and is purely absolutely
   continuous; the singular-continuous spectrum is empty.  If `alpha<0`
   there is exactly one normalized bound state
   `sqrt(-alpha/2) exp(alpha|x|/2)` at `-alpha^2/4`; if `alpha>=0` there is
   none.  The pole `2kappa+alpha=0` is the bound state, not a regular
   resolvent cell.
4. At momentum `k>0`,
   `r=alpha/(2ik-alpha)`, `t=2ik/(2ik-alpha)`.  The odd channel is free and
   the even channel is `(2ik+alpha)/(2ik-alpha)`; flux is unitary.
5. For `t>0`, with `a=|x|+|y|`,

   `K_alpha=K_0(t,x-y)-(alpha/4) exp(alpha a/2+alpha^2 t/4)
   erfc(a/(2 sqrt(t))+alpha sqrt(t)/2)`.

   Its diagonal defect is integrable and

   `Tr_rel exp(-tH_alpha)=0.5[exp(alpha^2 t/4)
   erfc(alpha sqrt(t)/2)-1]`.

The formulas include `alpha=0`, attractive and repulsive coupling, the
zero-energy scattering limit, high energy, and large heat time.  They do not
cover delta-prime interactions, several centers, time-dependent coupling, or
nonlinear dynamics.

## Proof spine

The trace theorem on `H^1(R)` makes the point evaluation infinitesimally form
bounded.  Integration by parts yields continuity plus the derivative jump.
Solving the free Green equation and one scalar interface equation gives the
rank-one resolvent.  Its sole upper-half-plane pole gives the bound state.
The odd sine and even Robin generalized Fourier transforms, equivalently
Stone's formula applied to the explicit half-line resolvents, give Lebesgue
spectral densities on `(0,infinity)`.  Their denominators have no positive
real zero, the threshold solution is not square integrable, and the only
off-continuum singularity is the attractive pole; hence there is no
singular-continuous spectrum.  Matching an incoming plane wave proves the
scattering formulas.  The identity

`L_t->s[exp(alpha*a/2+alpha^2*t/4)
erfc(a/(2sqrt(t))+alpha*sqrt(t)/2)]
=2exp(-a*sqrt(s))/(sqrt(s)*(2sqrt(s)+alpha))`

for `Re sqrt(s)>max(0,-alpha/2)` inverts the resolvent correction.  One
elementary integration by parts gives the relative trace.

The evidence is a regression certificate, not a substitute for these
arbitrary-real-parameter arguments.

## Route-A ceiling

There is a natural self-adjoint Hamiltonian, so only `A4_NATURAL_QUANTIZATION`
is retained.  There are no intrinsic rational-prime primitives, prime-power
repetitions, target determinant, target divisor, or same-clock arithmetic
bridge.  The other four axes fail and Route B is disabled.
