# Source and ownership audit

## Primary-source lock

1. Eberhard Hopf, *The partial differential equation \(u_t+u u_x=\mu u_{xx}\)*,
   Communications on Pure and Applied Mathematics **3** (1950), 201--230,
   [doi:10.1002/cpa.3160030302](https://doi.org/10.1002/cpa.3160030302).
2. Julian D. Cole, *On a quasi-linear parabolic equation occurring in
   aerodynamics*, Quarterly of Applied Mathematics **9** (1951), 225--236,
   [JSTOR 43633894](https://www.jstor.org/stable/43633894).

The nonlinear-to-linear substitution is therefore called the classical Hopf--Cole
or Cole--Hopf transformation. This package claims neither discovery nor priority
for that transformation, global viscous-Burgers solvability, or its standard
Fourier consequences. The deliverable is a normalized, all-parameter theorem
assembly with an executable regression certificate and a negative Route-A audit.

## Convention verification

The frozen PDE is \(u_t+u u_x=\nu u_{xx}\). With \(v=u-m\), \(y=x-mt\), and
\(v=-2\nu(\log q)_y\), direct differentiation gives \(q_t=\nu q_{yy}\). Returning
to fixed \(x\), \(w(x,t)=q(x-mt,t)\) obeys

\[
w_t=\nu w_{xx}-m w_x,
\qquad u=m-2\nu(\log w)_x.
\]

Thus the drift sign, Galilean sign, and spectral imaginary part used throughout the
package are mutually consistent. Multiplication \(w\mapsto c w\), \(c>0\), does
not change \(u\), which is why the correct linear state is a positive projective
cone rather than a vector space with an arbitrary normalization.

## Evidence boundary

The proof uses Sobolev composition, the periodic primitive, positivity of the heat
kernel, and Fourier spectral gaps. The 24 exact trigonometric cases exercise signs,
gaps, drift phases, semigroup composition, and the rationalized PDE numerator. They
are finite regression sentinels, not evidence for all functions by enumeration.

## Scope firewall

Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Forbidden and absent: target prime/zero tables, arithmetic local data, Euler factors,
root numbers, automorphy, target divisors or functional equations, a prime clock,
and any Hilbert--Pólya operator. The projective heat lift is a classical source-PDE
linearization and only an `A4_FORMAL_HINT`; it carries no arithmetic semantics.
