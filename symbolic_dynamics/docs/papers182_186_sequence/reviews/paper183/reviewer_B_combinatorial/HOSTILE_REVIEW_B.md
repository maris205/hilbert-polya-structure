# Hostile Review B — P183, random incoming-copy symmetrization

**Reviewer lane:** combinatorial; process-separated from the author and Review A  
**Reviewed object:** immutable Round 1  
**Review date:** 2026-09-03  
**Decision:** `ACCEPT_ROUND1_FOR_COORDINATOR_GATE`  
**External lifecycle:** `HOLD_EXTERNAL`

## Bottom line

The frozen P183 Round-1 package survives Review B with **zero Critical, zero
Major, and zero Minor findings**.  I found no counterexample or logical gap in
the conflict-deletion lemma, recurrent-state classification, all-time
independent-set absorption CDF, every-source/every-target endpoint kernel, or
the two one-step inverse censuses.  No paper-directory file was edited and no
repair is requested.

This is process-separated evidence, not a claim that reviewer and author
errors are independent.  The processes share the theorem specification,
standard combinatorial identities, Python implementation environment, and
frozen inputs.  Review B nevertheless changes both the state model and the
algorithms used to pressure the claims.

## Exact Round-1 binding

| Object | SHA-256 | Result |
|---|---|---|
| `main.tex` | `9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678` | exact required binding |
| `main_round1.pdf` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | exact required binding |
| `main.pdf` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | byte-identical |
| `main_round0_original.pdf` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | byte-identical |
| `references.bib` | `5b5f0fe2b7e78176d097ab2e919d35954adffff824528b999847be791038912d` | frozen and resolved |
| author verifier | `a7c56aa48783eae09e44a7df39f34109a891d33ac6a11e9b86e4fd22cdfdd472` | bound, not executed by Review B |
| author canonical | `f21652d061f409a0833be4900d6cbafee6a034b3121a03750984073893c2dea1` | bound and parsed |

The 19-row author manifest validates and is non-self-referential.  The Round-1
PDF is a byte-identical promotion of the author baseline; therefore the
author-side control documents' Round-0 labels do not describe a contradictory
content version.  Review B binds `main_round1.pdf` directly because that later
receipt is intentionally not part of the earlier author manifest.  The PDF is
four pages, 377,864 bytes, unencrypted, and its extracted text carries the
same theorem quantifiers, 47,033-author-assertion receipt, disclosures, and
`HOLD_EXTERNAL` status as the source.

Terminal re-signing note: the original `main.tex`, Round-1 PDF, and
mathematical attack are unchanged; this re-signing only rebinds the terminal
19-row paper manifest.  Its four added lifecycle rows (`IMPROVEMENT_LOG.md`,
`FINAL_QA.md`, `main_round1.pdf`, and `main_round2.pdf`) remain hard-fail
checks but are excluded from the original scientific assertion census.

## Representation and algorithm separation

| Process | State representation | Temporal/inverse method |
|---|---|---|
| author | one global ordered-arc bit integer | literal word enumeration and forward action accumulation |
| Review A | one four-state coordinate per unordered vertex pair | direct history enumeration and support/permutation regrouping |
| **Review B** | immutable relation: a `frozenset` of present directed arcs | weighted Markov dynamic programming, inclusion-exclusion support weights, closed-SCC recurrence, and target-star inverse construction |

Review B does not import or invoke either earlier verifier.  It enumerates the
relation carrier directly by subsets of the ordered-arc set.  Its time-
\(t\) kernel is propagated by the Markov recurrence on weighted endpoints;
the prescribed-support count is separately calculated as

\[
\sum_{j=0}^{r}(-1)^{r-j}\binom rj j^t,
\]

then divided by \(r!\) for a fixed first-occurrence order and checked against
\(\left\{\begin{smallmatrix}t\\r\end{smallmatrix}\right\}\).  It finds
recurrent Markov classes through a complete strongly-connected-component
decomposition and identifies closed components.  One-step predecessor
families are generated from each target by freeing a candidate action
vertex's outgoing star, rather than accumulated only from forward images.

## Hostile theorem audit

### 1. Literal action, deletion, idempotence, and noncommutation

On an unordered pair \(\{u,v\}\), choosing \(v\) leaves \(u\to v\) intact
and replaces \(v\to u\) by that same bit.  Thus every conflict incident with
\(v\) is deleted and every pair not incident with \(v\) is untouched.  This
proves the displayed exact conflict-star subtraction, and a second
application at \(v\) reads two equal bits and changes nothing.

For a conflicting pair the old bits differ.  Choosing \(u\) first retains the
old arc entering \(u\), whereas choosing \(v\) first retains the other bit;
therefore the two compositions differ on that pair even if additional pairs
are present.  Review B checks deletion and idempotence for all 16,585
state/action pairs through \(n=4\), and noncommutation for every conflicting
pair in every enumerated state.

**Result:** survives pointwise.

### 2. Recurrent states

The conflict set decreases by deleting a selected vertex star and can never
increase.  A symmetric state is fixed by every action.  From a nonsymmetric
state, choosing an endpoint of any conflict has positive probability and
moves to a strictly smaller conflict set, from which return is impossible.
This rules out both recurrence of the state and any hidden nonsymmetric
closed class.

As a separate graph calculation, Review B constructs the full Markov support
digraph and finds all closed SCCs.  The closed-SCC union is exactly the set of
symmetric relations, every closed SCC is a singleton, and its size is
\(2^{\binom n2}\) in every box.

**Result:** survives.

### 3. All-time absorption CDF

After a history, a conflict survives exactly when neither endpoint has ever
appeared.  Hence the residual conflicts are exactly those induced by the
missing set \(M(W)\), and absorption by time \(t\) is equivalent to \(M(W)\)
being independent in the initial conflict graph.

For a fixed missing set, the used alphabet is prescribed and has size
\(r=n-|M|\).  Inclusion-exclusion gives the number of onto words as
\(r!\left\{\begin{smallmatrix}t\\r\end{smallmatrix}\right\}\), with no extra choice of labels because the used labels were
already fixed.  Distinct missing sets partition all histories, so the
manuscript's numerator is exact.  At \(t=0\), only the empty support has
weight one; it absorbs precisely an already symmetric source.  For a
symmetric source every missing set is independent and the support classes sum
to all \(n^t\) histories.

Review B compares the CDF with weighted Markov propagation for every state
through \(n=4\) and every \(0\le t\le n+2\), checks normalization and CDF
monotonicity, and covers 22,391,680 units of history mass without enumerating
individual words.

**Result:** the formula, its all-\(t\) proof, and boundary conventions survive.

### 4. Every-source/every-target endpoint kernel

For an initial conflict \(\{u,v\}\), the first endpoint appearing in the
history resolves the pair.  If that endpoint is \(e\) and the other is \(o\),
the surviving common value is the old incoming bit \(A_{oe}\).  Equality then
persists, so later occurrences—including repeats—cannot affect that pair.
Thus only the support and its first-occurrence order matter, with unselected
endpoints correctly assigned infinite rank.

For a fixed support and fixed first-occurrence order, ordering the occurrence
blocks by their least time positions removes the usual \(r!\) factor, leaving
exactly \(\left\{\begin{smallmatrix}t\\r\end{smallmatrix}\right\}\) histories.  The support/order classes are disjoint and
complete, including the unique empty order at \(t=0\).

Review B verifies that its relation-level endpoint equals direct successive
actions for every partial permutation, checks the claimed residual conflict
graph, and compares the complete target multiplicity `Counter` against
weighted Markov propagation for all 29,080 source/time rows.  Counter equality
checks zero as well as nonzero target entries; this is not merely a support or
normalization test.

**Result:** survives for every stated source, target, and time.

### 5. Labelled-action and distinct-source fibres

If \(C_vA=B\), every pair incident with \(v\) is symmetric in \(B\); hence
\(v\) must be isolated in the conflict graph of \(B\).  Conversely, for an
isolated \(v\), every source arc not leaving \(v\) is forced and precisely the
\(n-1\) overwritten outgoing bits are free.  This gives \(2^{n-1}\) sources
per admissible labelled action and \(k(B)2^{n-1}\) labelled pairs.

Two distinct admissible-star families intersect only at \(B\): membership in
the \(w\)-family fixes every arc leaving \(v\), including \(v\to w\), and the
\(v\)-family symmetrically fixes every arc leaving \(w\); all remaining arcs
were fixed in either family already.  Consequently their union has
\(1+k(B)(2^{n-1}-1)\) states when \(k(B)>0\), and is empty for \(k(B)=0\).

The verifier constructs and compares each action-labelled family and its full
union for all 4,165 targets.  The sharp maxima are also attained at symmetric
targets: \(n2^{n-1}\) labelled pairs and
\(1+n(2^{n-1}-1)\) distinct sources.

**Result:** both notions of fibre remain correctly separated and survive.

## Quantifier and boundary table

| Scope | Attack | Outcome |
|---|---|---|
| labelled loopless binary digraphs, \(n\ge1\) | direct relation carriers for \(n=1,2,3,4\); proof is pair-local | pass |
| uniform independent vertex choice | history counts become probabilities only after division by \(n^t\); integer kernel itself needs no uniformity | pass |
| every integer \(t\ge0\) | support/order bijection has no finite-horizon step; exact pressure through \(n+2\) | pass |
| \(n=1\) | unique empty relation, one action, one fixed state, unit labelled/distinct fibre | pass |
| \(t=0\) | empty support/order and \(Stir00=1\) give identity kernel and correct CDF | pass |
| symmetric source | every history fixes it and independent-set sum totals \(n^t\) | pass |
| target with no isolated conflict vertex | no admissible action; both inverse counts are zero | pass |

The finite census is falsification pressure.  The universal quantifiers are
carried by the pairwise update and support/order proofs, not inferred from the
four boxes.

## Artifact, source, and owner wording audit

- `main.tex`, Round-1 PDF, `PROOF_PACKAGE.md`, `CLAIMS_EVIDENCE.md`, README,
  build receipt, self-QA, author canonical, and author manifest agree on the
  rule, quantifiers, theorem scope, boundary cases, 47,033 author assertions,
  and `HOLD_EXTERNAL`.
- Every bibliography entry is cited, every citation key resolves, and the
  three DOI/arXiv records match the local metadata and assigned background
  scope.  Brown concerns left-regular-band semigroup walks
  ([primary preprint](https://arxiv.org/abs/math/0006145)); Yin--Zhu concerns
  reciprocity ensembles ([publisher record](https://www.sciencedirect.com/science/article/pii/S0378437115010353));
  and Cirkovic--Wang--Resnick concerns growing preferential attachment with
  probabilistic reciprocal-edge creation
  ([publisher record](https://academic.oup.com/comnet/article/doi/10.1093/comnet/cnad031/7260367)).
  None is cited as an owner of the literal fixed-carrier incoming-copy map.
- The contribution subtraction assigns generic reciprocity, semigroup-walk,
  coupon-support, Stirling, and independent-set ingredients zero credit.  The
  comparison with P179 explicitly distinguishes noncommuting first-occurrence
  order from a commuting support-only endpoint.
- The external search is labelled bounded.  The manuscript expressly denies
  that a non-hit proves novelty, priority, completeness, or freedom to
  operate, and promises withdrawal if a literal/equivalent owner appears.

**Result:** no source, owner-language, or artifact inconsistency found.

## Exact Review-B receipt

```text
boxes=4
all_targets=4165
action_transitions=16585
kernel_rows=29080
virtual_history_mass=22391680
exact_assertions=1274441
review_transition_digest=bbf2f935a455b2a3e92f49f4b9df24058a2cdeee17fd8703926cc6697c851cbd
```

## Findings ledger

### Critical findings (0)

None.

### Major findings (0)

None.

### Minor findings (0)

None.

## Residual risks, not findings

1. Exhaustion stops at \(n=4\) and time \(n+2\); it does not replace the
   all-parameter proof.
2. Process separation and representation diversity reduce some shared failure
   modes but do not make errors independent.
3. The exact-owner search remains bounded.  Correctness acceptance therefore
   does not change `OWNER_AMBER` or `HOLD_EXTERNAL`.

## Reproduction

From the repository root:

```bash
python3 docs/papers182_186_sequence/reviews/paper183/reviewer_B_combinatorial/verify_review_b.py
```

Acceptance requires exit code zero and stdout byte-identical to
`CANONICAL.txt`.  Two fresh processes satisfied this condition before sealing.
