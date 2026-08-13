# HCS-C44 results

## Theorem result

For every prime \(p>3\) with \(p\equiv1\pmod3\), the paired first Hénon
moment satisfies

\[
\mathbf Q(B_{p,1})=\mathbf Q(\zeta_p)^+,
\qquad
[\mathbf Q(B_{p,1}):\mathbf Q]=(p-1)/2.
\]

The proof is symbolic and all-prime.  It identifies the Galois stabilizer with
the scaling stabilizer of the paired phase histogram and uses two exact
nonzero power moments to prove that this stabilizer is \(\{\pm1\}\).

Therefore no fixed number field can contain all paired moments.  The proposed
fixed-coefficient-field compatible system is refuted before a uniform rank or
conductor question is reached.

## Exact controls

The released ledger contains all 45 primes \(p\equiv1\pmod3\) with
\(p\le499\).  Every row verifies independently:

- the exact order-three element and phase histogram;
- the first and second closed-form power-moment identities, with the declared
  \(p=7\) special case;
- paired histogram stabilizer \(\{1,p-1\}\);
- trace-field degree \((p-1)/2\), reaching 249 at \(p=499\);
- zero-fiber count \(N_p(0)=p-3\);
- rational field trace \(-6\).

At \(p=7\), the exact primitive minimal polynomial is

\[
7X^3+42X^2-168X-232.
\]

Finite controls validate conventions and implementation.  They are not used
as a substitute for the uniform proof.

## Route-A result

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_REJECTED`.  The paired Euler germ and natural local
quantization survive; fixed-field arithmetic promotion does not.  Route B is
not authorized.

## Next gate

The additive Galois trace is universally \(-6\).  HCS-C45 therefore tests the
Galois norm of the complete local determinant and asks whether rational
descent can avoid unbounded local virtual rank and divisor complexity.

