# P183 hostile Review A

## Verdict

`PROVABLE AS STATED / ZERO FINDINGS / HOLD_EXTERNAL`

The frozen Round-0 theorem package survives this review.  No paper-directory
file was edited.  This is a process-separated review, not a claim of an
independent error process: the manuscript was authored in the cross-domain
author process identified by the coordinator, whereas this report and control
were produced in `/root/reviewer_a_p183_p184`.

## Frozen input binding

| object | SHA-256 | audit result |
|---|---|---|
| `papers/183-random-incoming-copy-symmetrization/main.tex` | `9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678` | read only |
| `papers/183-random-incoming-copy-symmetrization/main_round0_original.pdf` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | 4 pages; unencrypted; no JavaScript |

The paper-local `SHA256SUMS` verified every listed Round-0 object.  The live
`main.pdf` was byte-identical to `main_round0_original.pdf` at review time.
The abstract's 47,033 author assertions agree with both the manuscript and the
paper-local canonical output.  No undefined citation/reference or overfull-box
diagnostic was found in the frozen build log.

## Reviewer-owned representation and exact control

The reviewer does not import the author verifier.  It represents each
unordered pair `{i,j}` by one of the four local states `(A_ij,A_ji)`, applies a
vertex action locally to those four-state coordinates, and reconstructs a
history independently from its support and first-occurrence order.  This is
materially different from a global ordered-arc bit integer.

The exact replay exhausts:

- every loopless labelled digraph through `n=4`;
- every action at every such state, including conflict deletion and
  idempotence;
- every history of length `0,...,n` from every state through `n=4`;
- every support/permutation endpoint class and its Stirling weight;
- every simple conflict graph through `n=4`, every history through time `n`,
  and the independent-missing-set absorption polynomial;
- all labelled `(source,action)` fibres and all distinct-source unions through
  `n=4`.

It records 1,509,739 successful assertions.  A second replay must match
`CANONICAL.txt` byte for byte.

## Hostile claim audit

### Carrier, local rule, deletion, and recurrence

For pair code `(a,b)=(A_ij,A_ji)`, selecting `i` sends it to `(b,b)` and
selecting `j` sends it to `(a,a)`; selecting any other vertex leaves it alone.
Thus exactly the selected conflict star is deleted, deleted conflicts cannot
return, and each `C_v` is idempotent.  A conflict pair with `a != b` also gives
the claimed noncommutation witness.  A state is fixed by every action exactly
when all pair codes are symmetric, giving precisely `2^(n choose 2)` recurrent
fixed states.  The argument is valid on the finite Markov carrier: a state
with a conflict has a positive-probability transition to a strictly lower,
irreversible conflict set and therefore cannot lie in a closed recurrent
class.

### Absorption CDF

After a history, a conflict survives exactly when both endpoints are missing.
The endpoint is symmetric exactly when the missing set is independent in the
initial conflict graph.  Histories with a fixed used alphabet of size `r` are
surjections counted by `r! S(t,r)`, which produces the manuscript formula with
`r=n-|M|`.  The reviewer compared the formula to direct histories, checked
normalization by `n^t`, and checked CDF monotonicity after placing consecutive
times over a common denominator.  At `t=0`, only the empty support contributes;
at an initially symmetric state, every history contributes.  Both boundaries
agree with the theorem.

### Ordered endpoint kernel

On a conflict `{i,j}`, the first selected endpoint permanently copies its old
incoming bit to both directions.  Later actions cannot change an equal pair.
Ordering the nonempty occurrence blocks by their least time gives a bijection
between histories with a prescribed first-occurrence order and set partitions
of `[t]`, so the exact weight is `S(t,|S|)`, with no missing factorial.  Direct
history endpoints and the support/order construction agreed for every tested
source, target, and time; every kernel row summed to `n^t`.  The `t=0` identity
kernel and `n=1` singleton chain were explicitly reopened.

### Labelled-action and distinct-source fibres

For fixed action vertex `v`, a target is attainable precisely when `v` is
isolated in its conflict graph, and then the `n-1` overwritten outgoing bits
are free.  This gives `k(B)2^(n-1)` labelled pairs.  For distinct admissible
vertices, their source families meet only at `B`: the second family forces the
first vertex's one otherwise exceptional outgoing arc, and conversely.  Hence
the union is `1+k(B)(2^(n-1)-1)` when `k(B)>0`, and empty when `k(B)=0`.
Exhaustion reproduces maximum distinct fibres `1,3,10,29` for `n=1,2,3,4`.

## Wording, citation, owner, and source-control audit

The theorem wording distinguishes integer history multiplicity from the
uniform Markov probability, labelled predecessor/action pairs from distinct
predecessor states, and absorption by time `t` from first-hit mass.  No claim
silently moves from finite controls to the unbounded theorem.

The citation contexts agree with the cited primary records: Brown is used only
for finite-semigroup-walk background; Yin--Zhu for reciprocity statistics in
directed-network ensembles; and Cirkovic--Wang--Resnick for a growing
preferential-attachment reciprocity model.  None is presented as owning the
literal fixed-carrier update.  The records were checked against
[Brown's arXiv record](https://arxiv.org/abs/math/0006145),
[Yin--Zhu's arXiv record](https://arxiv.org/abs/1412.2187), and the
[publisher record for Cirkovic--Wang--Resnick](https://doi.org/10.1093/comnet/cnad031).

The contribution subtraction is appropriately conjunctive.  The text says
that its exact-rule search was bounded, expressly denies that a non-hit is a
novelty certificate, and retains `HOLD_EXTERNAL`; therefore the source screen
cannot be misread as a priority, completeness, or freedom-to-operate result.

## Finding ledger

- Critical: **0**.
- Major: **0**.
- Minor: **0**.

No repair is requested.  A byte-identical Round-1 receipt is acceptable.  Any
content change not required by this review reopens all theorem, source, and
reproducibility gates and must be recorded in the delta acceptance file.

## Replay

From the repository root:

```bash
python3 docs/papers182_186_sequence/reviews/paper183/reviewer_A_rootspawn/verify_review_a_p183.py
```

Acceptance requires exit code zero and stdout exactly equal to
`CANONICAL.txt`.  The review-package `SHA256SUMS` is non-self-referential.
