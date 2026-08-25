# C157 source audit

## Source lock

The unit square carries its ordinary Dirichlet Laplacian.  Its positive
half-wave frequencies are
`pi*sqrt(j^2+k^2)`, `j,k>=1`, and the trace is defined only for `Re(s)>0`
before taking the Abel boundary `s=epsilon-it`.  The ordered positive direction
convention keeps coordinate swaps distinct.  No parameter is fitted.

## Fourier and multiplicity audit

The Fourier convention is fixed as
`fhat(m)=integral f(x) exp(-2*pi*i*m dot x) dx`.  Under this convention the
radial transform has numerator `2s/pi`.  The full lattice is related to the
positive quadrant by

```text
Theta=1+4/(exp(pi*s)-1)+4W_D.
```

Four sign lifts of each ordered positive nonaxis vector convert the outer
coefficient `s/(2pi)` to `2s/pi`.  Each vector has one gcd decomposition into
primitive direction and repetition, so no collision is silently merged.

## Independence

The producer enumerates lattice boxes directly.  The checker instead solves
each sum-of-two-positive-squares shell.  SymPy differentiates the radial
Laplace--Bessel transform and reconstructs all shells a third way.  The two
numeric paths use different cutoffs and are compared through rigorous analytic
truncation envelopes plus a `1e-34` high-precision serialization/rounding
margin.  Their 55-decimal centers are not interval-arithmetic outputs.

## Firewall

This is the source Dirichlet Abel half-wave trace.  It is not an
isolated-orbit determinant or a target trace identity.  No target/prime/zero
table, arithmetic local/Euler factor, root number, automorphy input,
Hilbert--Polya construction, or Route-B input is used.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
