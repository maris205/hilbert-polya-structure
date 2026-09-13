# Paper 28 refinement review summary

## Disposition

The candidate reached an unconditional dual formal PASS only after four
append-only versions.  The mathematical headline survived, while each failed
review narrowed a literal quantifier, recurrence index, side-information
claim, or empty-set convention.  No correction was justified by empirical
evidence.

## Version-by-version issue ledger

| Version | Adversarial finding | Exact resolution | Headline effect |
|---|---|---|---|
| V1 | Automatic strict carry was stated without excluding \(r=1\). | Require \(r\ge2\); retain the explicit dimension-one cancellation counterexample.  The realization has \(r=\ell+1\ge4\). | none |
| V1 | \(0<m_0\le u_0\) was presented as necessary. | Replace it by the exact coordinatewise gate \(0<m_0<A_{\alpha_{a_0}}u_0\); keep \(m_0\le u_0\) only as sufficient. | broader and exact chamber |
| V1 | Literal label recovery lacked an information boundary. | Marked monodromy recovers support vectors; literal labels require the labelled support dictionary; unmarked data give only a cyclic class. | decoder narrowed to identifiable data |
| V1 | Closest weighted-degree literature was incomplete. | Add Blanc--van Santen and Meunier, and position weighted chambers/permutation matrices as prior ingredients. | novelty wording narrowed |
| V2 | Complete-state scalar recurrence was claimed from \(n=0\) for every admissible momentum seed. | Separate position maximum \(q_n\) from complete-state maximum \(d_n\); start the latter at \(n\ge1\), with an exact iff for \(n=0\). | scalar boundary corrected |
| V3 | Moving spike congruence was said for every coordinate. | Define moving \(y_n^{(i)}\) and fixed-star \(y_n^{(\star)}\) separately. | none |
| V3 | A phase subsequence reused an earlier vector symbol. | Introduce \(z_m^{(i,s)}\) explicitly. | none |
| V3 | Both selector sides were assigned a finite gap even for singleton alphabets. | State gap \(g\) only against an existing competitor; singleton uniqueness is vacuous and its normal cone is the full space. | restores all primitive pair words |

## Final independently reviewed scores

| Gate | Formal R1 | Formal R2 | Required |
|---|---:|---:|---:|
| Blocker | 0 | 0 | 0 |
| Major | 0 | 0 | 0 |
| Minor | 0 | 0 | 0 |
| Ambiguity | 0 | 0 | 0 |
| Bounded-search novelty | 8.1 | 8.0 | at least 7.5 |
| Standalone value | 8.2 | 8.1 | at least 7.5 |
| Proof confidence | 9.6 | 9.6 | at least 9.0 |
| Anonymous content pages | 25.5 | 26.0 | 22--30 |

Both final reviewers were fresh and mutually blind.  Their candidate PASS
does not substitute for the pending source-design review.

## Final claim hierarchy

The public theorem should be presented in this order:

1. general equal-total strict selector iff by a rational normal-fan
   intersection;
2. explicit incidence realization for every rooted primitive pair word;
3. strict actual polynomial-degree lifting in the exact momentum chamber;
4. exact ordered prefix products and period monodromy;
5. carry-free marked recovery of the rooted support-vector word;
6. least selector and quotient periods; and
7. precisely indexed annihilating recurrences and failure boundaries.

The arbitrary-word construction is the center.  Symplectic shears,
weighted-degree chambers, max-plus matrices, periodic products, and
base-expansion ideas are ingredients and should not be advertised as novel in
isolation.

## Source-design checks still pending

A new reviewer must verify that the ten frozen files:

- use one map per word consistently;
- distinguish \(r\) coordinate pairs from ambient dimension \(2r\);
- preserve the exact first-carry inequality and all recurrence start indices;
- handle singleton supports without a fictitious gap;
- state the decoder inputs and outputs without information leakage;
- bind every literature claim to a primary or official record;
- provide a complete proof dependency DAG and counterexample register; and
- fit a proof-first 22--30 page anonymous article without governance prose.

Any nonzero finding requires `FAIL_WRITE_NOTHING`; it cannot be waived by the
candidate reviews.

## Anonymous-publication boundary

The eventual manuscript must contain the mathematics, bounded literature
method, counterexamples, and limitations, but none of the batch number,
ledger events, paths, hashes, reviewer identities, governance chronology, or
internal scores.  No upload, submission, release, or identity disclosure is
authorized by this source-design record.

BATCH07_PAPER28_REVIEW_SUMMARY_FROZEN
