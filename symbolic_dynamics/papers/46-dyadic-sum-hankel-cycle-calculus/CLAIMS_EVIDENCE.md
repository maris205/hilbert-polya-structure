# P46 claims--evidence matrix

Status: `CANONICAL STATE-A BOUND / INFINITE CLAIMS REMAIN PROOF-OWNED`.

This file separates mathematical proof, finite implementation replay, and
governance evidence. It is bound to the State-A result ledger SHA-256
`fa22dde6ec3a9cbd473528ebb619863ac7beb0d1c9cc807394541501153add37`
and writer summary SHA-256
`c86887d3e7e9602cfebaec3e0b03e534d243af576166115fd7825f130a8ec774`.

## Claim matrix

| ID | Exact claim | Analytic owner | Canonical State-A evidence observed | Status / forbidden inference |
|---|---|---|---|---|
| C1 | The coefficient array defines a bounded compact operator `H_s` iff `Re(s)>0`; for `Re(s)<=0` there is no bounded operator with these coefficients | `PROOF_PACKAGE.md`, Steps 1--4, read with the writer's explicit bounded-realization correction: finite-compression phase identity, Schur row estimate, norm approximation by finite compressions, row-one `ell^2` obstruction | proof-contract fields replayed with PASS; row-one obstruction true, finite-grid-as-proof false, zero theorem failures | The infinite theorem remains manuscript-proof-owned. Finite singular values cannot establish the endpoint, and no unbounded realization is claimed. |
| C2 | `H_s in S_2` iff `Re(s)>1/2` | exact anti-diagonal square sum; central-half lower bound; harmonic identity at `sigma=1`; split estimate above one | endpoint diagnostics remain `FINITE_EXACT_DIAGNOSTIC` with an empty theorem-verdict array; proof-contract fields replayed with PASS | The infinite theorem remains manuscript-proof-owned. Partial sums remain diagnostics only. |
| C3 | `H_s in S_1` iff `Re(s)>1` | entrywise absolute summability for sufficiency; disjoint `Q_j=4^j` trace-dual matching for necessity including `sigma=1` | strict-wall and matching-obstruction proof-contract fields replayed with PASS; F06 rejected by C and P | The infinite theorem remains manuscript-proof-owned. No numerical trace-norm extrapolation is allowed. |
| C4 | Every edge preserves `v_2`; for `Re(s)>0`, the resulting bounded operator satisfies `H_s ~= direct_sum 2^(-ks)A_s` by basis reordering | support lemma and scaled weight calculation in `PROOF_PACKAGE.md`, Step 8, with the bounded-operator domain supplied explicitly | cutoffs `8,16,32,64`, zero valuation mismatch, strict cross-lane equality, and expected audit fields replayed with PASS | Exact finite replay checks implementation but does not prove the infinite direct sum. No closed unbounded-operator equivalence is claimed for `Re(s)<=0`. |
| C5 | For `Re(s)>1/2`, `r>=2`, `Tr(H_s^r)=Tr(A_s^r)/(1-2^(-rs))`; the entire `det_2` block product is locally uniform, while its logarithmic trace series is only near zero with branch fixed at zero.  For `Re(s)>1`, the ordinary determinant has its own locally uniform block product and `det_2(I-zH_s)=det(I-zH_s)exp(zTr(H_s))`. | Hilbert--Schmidt membership, valuation direct sum, trace-ideal products, and a self-contained combined-eigenvalue canonical-product proof; standard determinant definitions only are external | 36 finite trace cases agree with scale-dependent truncations; proof keeps the infinite identity separately typed; determinant/type audits pass | The infinite identities remain manuscript-proof-owned. None of the trace, power, or determinant identities is inferred from `H_s=U_tH_Re(s)U_t`. |
| C6 | Ordered dyadic cyclic systems have the complete odd/even solution classification | recurrence and closing equation in `PROOF_PACKAGE.md`, Step 10; positivity and odd-block parity applied after algebraic closure | 335,922 ordered tuples; direct-walk and algebraic lanes agree; frozen witnesses match; zero cycle mismatches | Exact implementation replay matched. Solver does not itself quotient rotations or identify primitives. |
| C7 | Canonical implementation replay is independent and mutation-closed | not a mathematical theorem | evaluator hashes distinct; no local imports/shared expanded fixtures/intermediates; 62 instances/25 families/162 invocations/0 survivors; 13 physical clones/0 accepted; integrity 16/16 | Establishes reproducibility only, not novelty or an infinite theorem. |
| C8 | Literature search found no exact combined package, without proving priority | frozen bounded search and ownership subtraction | priority false, Fournier--Wagner novelty credit zero, ownership preserved, search disposition exact | Never write “first,” “novel,” or “unique.” |

## Mandatory canonical extraction map

The writer-side extractor read only these hash-verified paths:

- `outputs/results/evaluator_m.json`
- `outputs/results/evaluator_c.json`
- `outputs/results/exact_comparison.json`
- `outputs/audits/proof_audit.json`
- `outputs/audits/source_audit.json`
- `outputs/audits/type_audit.json`
- `outputs/audits/independence_audit.json`
- `outputs/audits/integrity_audit.json`
- `outputs/audits/external_auditor_mutations.json`
- `outputs/tests/mutation_results.json`
- `outputs/audits/route_primary.json`
- `outputs/audits/route_independent.json`
- `outputs/RESULT_LEDGER.json`
- `outputs/reports/EXPERIMENT_REPORT.md`

The extractor rejects duplicate JSON keys, noncanonical serialization,
any failed status, any path outside the canonical output namespace, and any
ledger/hash mismatch. It must emit a candidate-local immutable summary; the
paper and tables must never read authority files during compilation.

## Canonical finite values

Canonical State A contains four complete support cutoffs, 335,922 ordered
dyadic label tuples, 36 exact trace cases, and zero support, cycle, or trace
mismatches. The comparison records strict recursive type-and-value equality.
These numbers may be reported only as finite implementation replay.

## Failure gates

Freeze is forbidden if any of the following occurs:

- an endpoint certificate is represented as being inferred from a finite
  grid;
- the finite trace identity is written as a geometric factor;
- an ordinary determinant is mentioned on `1/2<Re(s)<=1`;
- the bounded-operator direct sum is asserted on `Re(s)<=0` without a
  separately defined closed unbounded realization and domain;
- `H_s` is called Hermitian/self-adjoint for nonreal `s`;
- the left--right phase factorization is used to transfer spectra, powers,
  traces, or determinants rather than only singular-value properties;
- the near-zero logarithmic determinant expansion is represented as a
  globally valid logarithm of the entire product;
- an edge-label tuple is called a primitive temporal orbit;
- canonical State-A provenance is mixed with State-B provenance;
- search absence becomes a priority claim;
- any canonical mismatch, theorem failure, mutation survivor, or audit
  failure is nonzero.
