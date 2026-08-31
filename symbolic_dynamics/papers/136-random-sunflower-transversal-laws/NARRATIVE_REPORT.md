# Narrative report: P136 round 1

## Outcome

The surviving SF1 signal has been converted into a deliberately small
probability manuscript: **Recorded-Transversal Laws on Rate-Weighted Sunflower
Forests**. The note proves a complete endpoint-and-choice-count atlas for one sharply
specified carrier and makes no process-level novelty claim.

Current status: `ANONYMOUS_ROUND1 / REVIEW_A_REPAIRED / HOLD_EXTERNAL`.

## What the system does

A sunflower has a nonempty core and disjoint nonempty petals. Each edge is the
union of the core with one petal and has a fixed positive rate. Among the
unhit edges, the process selects one proportionally to its rate, chooses one
of its vertices uniformly, records that vertex, and deletes every edge it
hits. A petal vertex removes one edge; a core vertex stops the component. The
endpoint is the entire recorded set, including petal vertices that would be
discarded by a later minimalization step. No such reduction is performed.

## The mathematical progress

For a prescribed proper set `A` of petals recorded before the first core
choice, conditioning on the terminal core time gives

```text
product_(i in A) r_i
* sum_(j not in A) q_j lambda_j
* integral exp(-Lambda(complement A)t)
           product_(i in A)(1-exp(-lambda_i t)) dt.
```

Inclusion--exclusion evaluates the integral exactly. The all-petal endpoint is
a separate atom. Conditional uniformity then divides each aggregate mass by
the exact number of compatible core and petal vertices, resolving the law to
actual vertex sets even when rates are unequal.

At unit rates, the clock order is uniform. The tail `Pr(T>t)` is the average
of the products of the petal probabilities over all `t`-subsets, hence an
elementary symmetric polynomial divided by a binomial coefficient. The
maximal atom is handled carefully: it contains both the all-petal event and a
final core choice after `m-1` petal choices. Differencing tails gives the full
PGF; standard tail sums give the mean, second moment, and variance.

For vertex-disjoint sunflower components, independent local marked clock
families produce independent stopped endpoints and discrete selection counts.
Global sorting is exactly the rate-proportional scheduler. Therefore endpoint
laws tensorize, selection counts add, and their PGFs multiply. This is not a
wall-clock statement: continuous elapsed absorption time is outside the paper,
and under the exponential embedding the forest completion time is the maximum
of the component stopping times.

## Owner boundary

The direct owner subtraction is central, not a footnote. Bar-Yehuda's
Algorithmica paper, Section 5.1/Theorem 6, directly owns the hypergraph Pitt
covering process. Pitt owns its graph ancestor. Erdős--Rado own the sunflower
carrier, and the transversal literature owns the surrounding extremal and
approximation framing. Plackett and Gnedin own the size-biased/exponential
ordering machinery and disjoint-restriction dissociation. All of these receive
zero contribution credit, as do the standard integral, symmetric-polynomial,
tail-sum, and product-PGF tools.

The only surviving residual is the complete conjunction of weighted aggregate
endpoint, actual-vertex refinement, unit-rate choice-count atlas, and marked
forest consequence on this carrier. A bounded direct-package non-hit is
reported only as a non-hit; it is not a novelty certificate.

## Executable evidence

The paper-local verifier independently enumerates the finite process with
`fractions.Fraction`. It checks:

- 4092 unit-rate aggregate inputs with `c in {1,2,3}`,
  `m in {1,...,5}`, and `p_i in {1,...,4}`;
- 1638 weighted aggregate inputs with `c in {1,2}`, `m in {1,2,3}`,
  and `p_i,lambda_i in {1,2,3}`;
- 78 separately vertex-resolved unit-rate inputs with `c in {1,2}`,
  `m in {1,2,3}`, and `p_i in {1,2,3}`;
- three unit-rate and one unequal-rate two-component forest controls.

The program checks terminal normalization and positivity, every aggregate or
resolved mass, the full discrete step-count law, the top atom, both tail-sum
moments, forest endpoint products, and forest step-count convolutions. The frozen byte replay and
exact assertion count are recorded in `CONTROL_RESULTS.md` after execution.

## Limits and next gate

Finite controls do not exhaust weighted vertex-resolved endpoints or arbitrary
forests. Those statements depend on the written all-parameter proofs. The note
does not claim a new random greedy algorithm, approximation ratio,
exponential-race technique, finite ranking formula, general independence
theorem, or law for continuous completion time. Review A repairs the
count-versus-time terminology; Review B remains intentionally unwritten.
