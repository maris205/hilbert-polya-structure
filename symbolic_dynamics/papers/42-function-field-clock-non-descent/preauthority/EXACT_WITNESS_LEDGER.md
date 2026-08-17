# Exact witness ledger

## Frozen field sizes

| `q` | `N_q(1)` | `N_q(2)` | primitive length-two witness | forced same-clock label | rational prime? |
|---:|---:|---:|---|---:|---|
| 2 | 2 | 1 | `[01]` | 4 | no |
| 3 | 3 | 3 | `[01]` | 9 | no |
| 5 | 5 | 10 | `[01]` | 25 | no |

The formulas used are

\[
 N_q(1)=q,
 \qquad
 N_q(2)=\frac{q^2-q}{2}.
\]

No finite census is used to infer an infinite theorem. The table records
minimal exact witnesses to the proved statements.

## Independent failure channels

| Channel | Required fields | Minimal witness | Result |
|---|---|---|---|
| clock/support | total map, rational-prime support, exact clock | `[01]` | forced label `q^2` is composite |
| marker/multiplicity | marker, weight, one factor per prime | all length-one classes | `q` source factors collide at target `p=q` |
| analytic determinant | common `s,z` normalization | first `z` coefficient | `q^(1-s)` differs from `P(s)` |

## Positive controls

1. **Function-field prime-polynomial control.** The degree counts `N_q(n)`
   agree exactly with monic irreducible-polynomial counts; norm `q^n`, clock
   `n log q`, and repetitions are correct for that type.
2. **Single-factor control.** Selecting one length-one source orbit gives the
   single rational factor `(1-zq^(-s))^(-1)`. This is locally correct but is a
   non-total projection and does not produce all rational primes.
3. **Target-operator control.** The diagonal operator on `ell^2(P)` owns the
   marked rational Euler product on `Re(s)>1`. The theorem does not claim the
   target product lacks an operator; it claims `SD-C01` does not own that
   operator.
4. **Repetition-weight control.** Under the norm label `q^n`, source weight
   repetitions correctly become `(q^n)^(-rs)`. The failure remains primitive
   rational-prime support and marker, not exponent algebra.

## Mutation attacks for independent DA

- Treat `q^2` as a prime: must be rejected.
- Treat `01` as imprimitive: must be rejected.
- Collapse the `q` length-one factors to one without a projection flag: must
  be rejected.
- Specialize `z=1` before marker comparison: must be rejected as a loss of the
  free-marker witness.
- Import the diagonal rational-prime operator as source-owned: must be
  rejected by the ownership firewall.
- Reverse the verdict to A1/A2 failure because rational-prime descent fails:
  must be rejected; A1/A2 remain positive for the source's own function-field
  species.
