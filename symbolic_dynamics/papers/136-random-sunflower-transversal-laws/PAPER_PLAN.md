# P136 paper plan

## Status

`ANONYMOUS_ROUND1 / REVIEW_A_REPAIRED / HOLD_EXTERNAL`

This is a short exact-probability note. It is not a new-algorithm paper and it
is not cleared for external circulation. The independent SF1 gate returned
`REPAIR`; every mandatory textual repair A--F is built into this plan and the
manuscript.

## One-sentence residual

For the owned random-edge/random-vertex covering process restricted to
vertex-disjoint heterogeneous sunflowers with fixed edge rates, derive the
complete recorded-transversal law and, at unit rates, the complete stopping
PGF and first two moments.

## Formal claim spine

1. **P136-C1, weighted aggregate endpoint.** For every proper petal mask,
   condition on the stopping core time and evaluate the resulting
   inclusion--exclusion integral; add the all-petal atom separately.
2. **P136-C2, actual vertices.** Condition on aggregate mark categories and
   resolve the independent uniform core and petal marks, at arbitrary fixed
   positive rates.
3. **P136-C3, uniform choice-count law.** Average the probability that the first
   `t` edges in a uniform order have petal marks, obtaining the elementary-
   symmetric tail. Resolve `T=m` into the disjoint all-petal and final-core
   events.
4. **P136-C4, PGF and moments.** Difference the tails and use the two finite
   tail-sum identities for `T` and `T^2`.
5. **P136-C5, forest factorization.** Project independent marked clock
   families to the vertex-disjoint components; tensor endpoints, add the
   discrete selection counts, and multiply their PGFs. Continuous elapsed
   absorption time is outside the claim; under the exponential embedding the
   forest completion time is the maximum of the component stopping times.

## Owner subtraction, before any novelty language

- Erdős--Rado own the sunflower/Delta-system carrier.
- Pitt owns the graph ancestor. Bar-Yehuda, Section 5.1/Theorem 6, directly
  owns the hypergraph Pitt covering process, including the unweighted uniform
  vertex rule. The algorithm, cover validity, and approximation guarantees
  receive zero credit.
- Plackett and Gnedin own the finite size-biased ranking and positive-rate
  independent-exponential representation. Rate-proportional ordering,
  memorylessness, finite ranking probabilities, and dissociation on disjoint
  restrictions receive zero credit.
- Inclusion--exclusion, beta integration, elementary symmetric polynomials,
  tail-sum moments, and products of independent PGFs receive zero credit.
- The residual is only the complete exact conjunction for this restricted
  carrier. A bounded literature non-hit is not a priority certificate.

## Hypotheses that must remain visible

- `m,c,p_1,...,p_m` are positive integers.
- Every fixed edge rate `lambda_i` is a positive real number.
- Forest components are vertex-disjoint.
- Vertex marks are mutually independent, independent of all clocks, and
  uniform within their selected edge.
- Rates are fixed throughout the process.
- The endpoint is the full recorded vertex set and is not reduced to a
  minimal transversal.

## Paper architecture

1. Position the note and subtract owners.
2. Define the literal process and marked order.
3. Prove the weighted aggregate and actual-vertex endpoint laws.
4. Prove the uniform choice-count law, top atom, PGF, mean, second moment, and
   variance.
5. Prove the marked stopped forest factorization.
6. State the exact-arithmetic controls and their finite scope.
7. Conclude with the deliberately narrow residual.

## Evidence contract

The paper-local verifier is self-contained and deterministic. Its exact finite
grids are: 4092 unit-rate aggregate inputs with `c in {1,2,3}`,
`m in {1,...,5}`, and every `p_i in {1,...,4}`; 1638 weighted aggregate inputs
with `c in {1,2}`, `m in {1,2,3}`, and every
`p_i,lambda_i in {1,2,3}`; 78 unit-rate actual-vertex inputs with
`c in {1,2}`, `m in {1,2,3}`, and every `p_i in {1,2,3}`; and four
two-component controls. It must not be described as exhaustive for real-valued
rates, weighted resolved endpoints, or arbitrary forests. Symbolic proof, not
enumeration, carries the all-parameter claims.

## Round-0 acceptance criteria

- All claims above have complete proofs in `main.tex`.
- `code/verification_output.txt` is a byte-for-byte fresh replay of
  `code/verify.py`.
- Four-stage LaTeX compilation succeeds and preserves both `main.pdf` and
  `main_round0_original.pdf`.
- PDF metadata, embedded fonts, searchable text, page count, and log warnings
  are inspected.
- Status remains `HOLD_EXTERNAL`; hostile-review rounds A/B are intentionally
  absent at this stage.
