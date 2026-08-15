# Exact authority experiment report — SD-C37

## Outcome

The source/evaluator-separated exact audit passes as a reproducible negative
benchmark. Fresh A, fresh B, and cache-free cold start C produced the same 23
scientific artifacts byte for byte. The scientific aggregate is
`94df5a68ef2a3a9a05bedddea2b6f210e437622a3d77cb1f9ec4aff351a55fed`,
and all 84 exact tests pass, including five deliberate mutation-sensitivity
tests.

This is not a positive dynamical determinant. The strict Route-A tuple is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

The overall verdict is `ROUTE_A_REJECTED`; Route B remains false.

## Authority reconciliation of the `/tmp` bridge

The `/tmp/paper35_exact_prototype/` package supplied the neutral algorithms,
independent reconstruction pattern, correction ledger, and finite parameter
ranges. Authority outputs were recomputed rather than copied. Two frozen
scaffold conventions supersede prototype diagnostics:

- the authority height is `h_r(b,k)=b+r^k`, with U increment `r^k` and V
  increment `(r-1)r^k`;
- the primary two-generator operator is unweighted `A_+=S+T`, so every U/V
  relation witness has weight one.

The prototype bridge record, its exact hashes, and these corrections are in
`results/prototype_bridge.json`.

## Exact raw-data table

| Block | Evidence class | Population | Exact value | Failures |
|---|---|---:|---:|---:|
| authority height windows | exact finite ledger plus independent DAG check | 520 edges | 520 strict exact increments | 0 |
| symmetric backtracks | exact edgewise construction | 520 words | 520 Hashimoto exclusions | 0 |
| admissible-word census | exhaustive for frozen bases and lengths | 699,040 words | 126,553 admissible; 88 primitive cyclic-NB closed | 0 |
| affine relation witnesses | exact symbolic witnesses | 8 | 8 primitive words of length `r+3` | 0 |
| commutation and arbitrary-monoid controls | exact generic controls | 8 | all retain reduced relation cycles | 0 |
| operator certificates | exact finite witness families | 4 operator blocks | all disjoint, uniformly nonzero | 0 |
| finite quotients | exhaustive for `q=1,...,12` | 48 rows | 48 relation closures and 48 `U_q^q` cycles | 0 |
| diagonal trace/determinant firewall | exact rational coefficients | 2 fixtures | 2 coefficient identities | 0 |
| evaluator-only prime-Fock marker | exact occupation control | 8 prime labels | product and enumeration agree through degree 6 | 0 |
| signed/matrix/groupoid boundary | exact scoped controls | 3 classes | boundary gate passes | 0 |

These are deterministic exact counts, not stochastic samples. Means, standard
deviations, confidence intervals, and best-seed selection are inapplicable.

## Key findings

1. **Observation:** all 520 positive edges satisfy the source-locked authority
   height increment, and every induced window passes an independent Kahn DAG
   audit. **Interpretation:** the positive right-Cayley source is acyclic; this
   does not extend to every action representation, as the retained Cuntz-zero
   loop shows. **Implication:** the unprojected positive source owns no nonzero
   primitive periodic ledger. **Next step:** do not add a terminal projector or
   identity loop; any new recurrence object must be source-locked separately.

2. **Observation:** formal symmetrization creates 520 primitive length-two
   immediate backtracks, all removed by Hashimoto semantics. **Interpretation:**
   nonbacktracking solves the universal inverse-edge artifact only.
   **Implication:** it cannot by itself supply arithmetic selectivity.
   **Next step:** any successor must classify all surviving relation words,
   including the cyclic join.

3. **Observation:** for `r=2,3,4,5` at two bases, every
   `V U V^{-1} U^{-r}` witness is admissible, primitive, cyclically
   nonbacktracking, and length `r+3`; generic commutators and mutated
   one-relator monoids behave the same way. **Interpretation:** these cycles
   encode presentation geometry, not a prime selector. **Implication:** A1
   fails despite the structural arithmetic origin at A0. **Next step:** Paper
   36 may test only a chainwise, source-natural relation cancellation that
   fails matched generic presentations.

4. **Observation:** all 48 finite quotients preserve the affine relation and
   also contain `U_q^q`; fourteen small-modulus rows have non-simple relation
   polygons, including `(r,q)=(2,2)`. **Interpretation:** quotient closure and
   quotient-ledger faithfulness are different claims. **Implication:** no
   quotient determinant descends silently to the infinite positive graph.
   **Next step:** require an explicit original-step marker map and an operator
   descent theorem before using a quotient.

5. **Observation:** for both diagonal fixtures,
   `[z^m](-log det(I-zD_beta))=Tr(D_beta^m)/m`; the partition trace is the
   linear coefficient, while `det(I-D_beta)=0` because the `n=1` eigenvalue is
   one. **Interpretation:** a Gibbs trace, determinant germ, reciprocal
   determinant, and specialization are related but distinct operator objects.
   **Implication:** the Bost--Connes partition function is not automatically
   the primitive determinant of this graph. **Next step:** prove a same-whole-
   operator trace-log identity before comparing divisors.

6. **Observation:** the evaluator-only prime-Fock product agrees with an
   independent occupation enumeration through particle degree six, and its
   `z=1` finite Euler specialization is exact. **Interpretation:** this control
   deliberately preloads a prime-indexed one-particle basis and uses `z` for
   occupation, not generator steps. **Implication:** it is a marker firewall,
   not prime emergence from the affine source. **Next step:** keep prime labels
   out of candidate-source generation.

7. **Observation:** signed weights cancel odd but not even power sums; a
   nonzero nilpotent matrix has determinant factor one; `diag(1,-1)` cancels
   its first trace but not its second. **Interpretation:** coefficient
   cancellation is weaker than literal primitive-word deletion. **Implication:**
   signed, matrix, supertrace, and groupoid approaches remain open only as new
   same-object programs. **Next step:** require source-natural all-orders
   cancellation and preserve the original marker and operator domain.

## Reproducibility, schema, and provenance

- source artifacts are hashed before evaluation and unchanged afterward;
- the independent evaluator imports neither source module;
- A/B/C scientific artifacts are byte-identical;
- the metadata seal checks that the 23 published science hashes remain fixed;
- strict Route-A v0.2 enums, target/root `not_applicable; ...` strings, and
  `route_b_invocation_allowed: false` are machine-audited;
- all three provenance fields remain the paired token
  `PENDING_FIRST_ARTIFACT_COMMIT` under the acyclic two-stage policy;
- final inventory, UTF-8/LF/exact-one-EOF, trailing whitespace, control bytes,
  symlinks, caches, idempotence, and SHA checks are recorded under `results/`.

No Git, mirror, manifest, manuscript, figure, PDF, or root README mutation is
part of this integration.

## Suggested next experiment

Paper 36 has one minimum obligation: exhibit a source-natural chainwise
cancellation, or a quotient/induction with an explicit original-step marker
map, that kills backtracks and every affine/commutation relation cycle, retains
a nonzero arithmetic sector on the same whole operator, and fails generic
matched presentations. Otherwise this exact negative benchmark remains the
controlling result.
