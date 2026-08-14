# Experiment Plan

## Objective

Test whether P49's surviving trace-field packets admit a lossless collective
assembly, and whether forgetting to rational primes preserves their intrinsic
cyclotomic clocks.

## Frozen object

- Map: `H6(q,p)=(1-6q^2-p,q)`.
- Signed multiplier branches: primitive periods 1, 3, and 4 from HCS-P49.
- Trace fields: `Q(sqrt(7))`, `Q(sqrt(5))`, and `Q`.
- Cyclotomic indices: `3 <= n <= 20`.
- Packet element: `beta_(gamma,n)=lambda^(-phi(n)/2) Phi_n(lambda)`.
- No fitted parameters, prime lookup, or zero lookup.

## Claims and falsifiers

| ID | Claim or mutation | Acceptance test |
|---|---|---|
| C1 | every half packet is an algebraic integer in the stated trace field | exact integral-basis coordinates |
| C2 | prime-ideal valuations push forward to the rational norm factorization | compare every prime exponent in all 54 rows |
| C3 | if the residue characteristic does not divide `n`, the multiplier residue order is exactly `n` | finite-field power test against every proper divisor |
| C4 | the rational-prime pushforward is noninjective | compute free-kernel rank atom count minus prime count |
| C5 | orbit, index, and prime-ideal tags are independently necessary | lock the `p=109`, `p=29`, and split-prime controls |
| M1 | replace the signed period-three branch by its positive modulus | require the index-three norm to change |
| M2 | promote bad-characteristic rows to exact-order rows | require `p | n` rows to remain uncertified |
| M3 | identify atoms only by rational prime | require strict loss of cardinality and a positive kernel rank |
| M4 | call the finite ledger an all-orbit trace | reject through the claim-boundary schema |

## Reproducibility

The code hash-locks four HCS-P49 artifacts.  The output is a canonical JSON
certificate and a generated LaTeX table.  The finite pilot is exact; no
floating-point computation is used.
