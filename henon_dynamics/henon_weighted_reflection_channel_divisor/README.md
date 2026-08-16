# HCS-P75: Weighted reflection-channel divisor

P70's one-parameter orbit product has a canonical two-fugacity lift.  Put
`w=qz`, so that an orbit monomial becomes

    z^n q^(S_n chi) = z^(n-S_n chi) w^(S_n chi).

Then the logarithm of the lifted product has the exact channel expansion

    log Z_sharp(z,w) = sum_(m>=1) c_m 2w^m/(1-z^(2m)-w^(2m)),
    c_m = (1/m) product_(p|m, p odd) (1-p).

The coefficients are the same nonzero Möbius--repetition coefficients as in
P72.  In the bidisk, the denominator-zero sets

    H_m : z^(2m)+w^(2m)=1

are smooth and form a locally finite effective divisor.  The channel series
converges normally on the complement.  On the positive-weight fiber
`w=qz`, its `m`th channel has the `2m` roots

    alpha_(m,l)(q)=(1+q^(2m))^(-1/(2m)) exp(pi i l/m).

Every such root has an explicit nonzero logarithmic principal part.  P75
does not claim that the limiting roots form a natural boundary; that is a
separate P76 question.

**Status:** weighted regrouping, bidisk continuation, divisor geometry, and
fixed-positive-`q` principal parts PROVED; Lind comparison for `q!=1`, an
operator model, arithmetic semantics, and a natural-boundary theorem are not
claimed.  Reproduce with `bash code/run_c75.sh` and see `paper/paper.pdf`.
