# C161 source and pivot audit

## Frozen source

The released source is the odd cyclic rotation `R_q(x)=x+1` on `Z/qZ` with
the source observable `phi_(a,b)(x)=a x^2+b x`.  The iterate clock is the
literal Birkhoff length `n`; no rescaling or fitted parameter is used.

## Hard-gate decision

The first candidate was the C156 Heisenberg central-rotation module.  Algebra
suggested simple local factors, but discriminant calculations did not prove
uniform quotient coordinates, removal of the affine term, or the required
2-adic and 5-adic equivalences.  Those draft factors were therefore rejected,
not reported as a finding, and their generated release artifacts were removed.

The authorized pivot passes the hard gate: its complete Birkhoff amplitude is
evaluated for every odd `q` and every `a,b,n`, and its prime-modulus zero level
has an exact discriminant law.  Exhaustive finite checks are sentinels only;
the proof is the gcd reduction, completion of the square, and odd Gauss lemma.

## Evidence boundary

No external dataset or citation is used.  The words prime and Jacobi refer only
to finite source rings, not to arithmetic local data or an Euler product.  No
target zero/prime table, target divisor/counting law, Euler factor, root number,
automorphy, Hilbert--Polya operator, or Route B input enters the package.
