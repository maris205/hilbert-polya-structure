# Theorem package

Freeze, for t>0,

    u_t = u_xx,       0 < x < s(t),
    u(0,t) = 1,       u(s(t),t) = 0,
    beta s'(t) = -u_x(s(t)^-,t),       s(0)=0,
    beta=Ste^{-1}>0.

## Neumann root and profile

With eta=x/(2 sqrt(t)), set

    s(t)=2 lambda sqrt(t),
    u(x,t)=1-erf(eta)/erf(lambda).

The interface condition is equivalent to

    F(lambda) = sqrt(pi)*lambda*exp(lambda^2)*erf(lambda) = Ste.

Since

    F'(lambda)=sqrt(pi)*exp(lambda^2)*erf(lambda)*(1+2 lambda^2)+2 lambda > 0,

and F(0)=0, F(lambda) tends to infinity, every positive Ste has exactly one
positive root. This is uniqueness of the similarity root/profile only, not
global uniqueness for arbitrary Stefan initial data.

## Two endpoint regimes

Writing z=Ste, formal reversion at z=0 gives

    lambda^2 = z/2 - z^2/6 + 7 z^3/90 - 79 z^4/1890
                 + 689 z^5/28350 + O(z^6),

or

    lambda = sqrt(z/2)*(1-z/6+23 z^2/360-157 z^3/5040+O(z^4)).

For lambda>0, 0<erfc(lambda)<exp(-lambda^2)/(sqrt(pi)*lambda). Hence
Ste < sqrt(pi)*lambda*exp(lambda^2) < Ste+1; monotonic inversion gives,
for Ste>1,

    W(2 Ste^2/pi)/2 < lambda^2 < W(2 (Ste+1)^2/pi)/2,

and therefore lambda^2 is asymptotic to W(2 Ste^2/pi)/2.

## Flux and energy ledger

The wall and interface fluxes are

    J_wall = -u_x(0,t)        = 1/(sqrt(pi*t)*erf(lambda)),
    J_interface = -u_x(s^-,t) = exp(-lambda^2) J_wall.

Integrating the heat equation over the moving interval gives the exact
identity

    Integral_0^t J_wall(tau) d tau
      = Integral_0^{s(t)} u(x,t) dx + beta*s(t).

The two terms on the right are respectively

    S(t)=2 sqrt(t)*(1-exp(-lambda^2))/(sqrt(pi)*erf(lambda)),
    L(t)=beta*s(t)=2 exp(-lambda^2) sqrt(t)/(sqrt(pi)*erf(lambda)),

so their sum is 2 sqrt(t)/(sqrt(pi)*erf(lambda)), exactly the wall input.

## Singular faces and Route-A boundary

beta tends to infinity (Ste tends to zero) sends lambda to zero; beta tends
to zero from above sends lambda to infinity with the Lambert-W growth. Zero
superheat makes the normalized temperature scale undefined, zero dimensional
diffusivity kappa=0 collapses the similarity length, and L=0 (Ste=infinity) requires a separate
zero-latent rescaling. None is called a finite-lambda classical extension.

This source-native theorem has no primitive periodic-orbit owner, arithmetic
clock, target divisor, or self-adjoint operator. The source heat clock is not
target continuation/divisor/counting law and is not an A3 analytic match. The
recorded tuple is
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT), hence
ROUTE_A_REJECTED; Route B remains locked false under
NO_BAD_EULER_OR_ROOT_NUMBER.
