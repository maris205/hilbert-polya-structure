# Results — HCS-C136

## Headline theorem

For all odd coprime `M,N>1`, all units `c mod L` with `L=MN`, and

`c_M=(c mod M)*N^(-1) mod M`,

`c_N=(c mod N)*M^(-1) mod N`,

the canonical residue-basis unitary satisfies exact tensor identities for
`F`, `C`, `W`, and `U`.  There is no projective scalar.  In addition,
`Theta_[r,c]=F_[r,c] K_r` obeys

`Theta^2=I`, `Theta U Theta^(-1)=U^(-1)`, and
`Theta W(q,p) Theta^(-1)=W(p,q)`,

and factors exactly under canonical CRT using the explicitly defined
conjugate-linear product map.  For every fixed ordered finite pairwise-coprime
odd factor list, the induced character on factor `r_j` is

`c_j=(c mod r_j)*(L/r_j)^(-1) mod r_j`,

independent of binary split schedule and parenthesization under canonical
tensor associators.  No factor-permutation coherence is claimed.

## Exact certificate

| receipt | cases |
|---|---:|
| pair Fourier kernels | 13,520 |
| pair chirp diagonals | 306 |
| pair unitary kernels | 13,520 |
| pair Weyl basis actions | 658,314 |
| CRT conjugation bases | 306 |
| antiunitary CRT kernels | 27,040 |
| triple unitary kernels | 381,672 |
| antiunitary involution kernels | 2,404 |
| antiunitary reversal kernels | 2,404 |
| antiunitary Weyl swaps | 31,928 |
| total enumerated | 1,131,414 |
| four-factor bracket comparisons | 6 |

The independent SymPy/congruence path adds 96,449 exact checks.  The mutation
suite rejects 83 repaired-hash semantic changes and one stale-hash change.

## Negative result

The direct standard-character tensor is false under canonical CRT.  At
`(M,N)=(3,5)`, the global Fourier exponent at `x=y=1` is `1 mod 15`; the
naive standard tensor exponent is `8`; the correct inverse-scaled exponent is
`1`.  A kernel-ratio proof shows that no scalar repairs the standard unitary
tensor for any nontrivial coprime odd pair.

## Boundary

The result does not classify intertwiners back to standard local characters.
It covers neither noncoprime factors nor even levels under the frozen half-phase
convention, and it does not compare reordered factor lists.  It makes no target
divisor, semiclassical trace, arithmetic local
factor, root-number, automorphy, or Hilbert--Polya claim.

Strict result:

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,

`ROUTE_A_EXPLORATORY`, Route B unauthorized.
