# Results

## Exact theorem

The two-fugacity lift of P70 satisfies

    log Z_sharp(z,w)
      = sum_(m>=1) c_m 2w^m/(1-z^(2m)-w^(2m)),
    c_m = (1/m) product_(p|m,p odd)(1-p) != 0.

In the bidisk, `H_m={z^(2m)+w^(2m)=1}` is smooth, the hypersurface family is
locally finite, and the series converges normally off its union.

On `w=qz`, `q>0`, channel `m` has roots

    alpha_(m,l)=rho_m(q) exp(pi i l/m),
    rho_m(q)=(1+q^(2m))^(-1/(2m)),

and

    log Z_orb(z,q)
      = c_m*(-1)^l*q^m/[m*sqrt(1+q^(2m))]
        /(1-z/alpha_(m,l)) + holomorphic.

Every displayed coefficient is nonzero.  Dense boundary accumulation is not
part of this result.

## Verification

- 48 exact `q`-polynomial coefficient comparisons in the primary
  certificate.
- 64 independently reconstructed weighted coefficients and 64 nonzero
  channel coefficients.
- 72 fixed-fiber geometry rows: 24 channels at each of `q=1/2,1,2`.
- 24/24 tests across normal and optimized modes.
- 9/9 dependency locks to P69, P70, and P72.
- 38/38 hostile claim mutations rejected.

## Boundary

No weighted Lind source, joint collision classification, operator model,
arithmetic trace, natural boundary, arithmetic advance, or Route-B claim is
made.
