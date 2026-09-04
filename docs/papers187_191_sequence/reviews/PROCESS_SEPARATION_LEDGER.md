# Review-process separation ledger — P187–P191

## Excluded provisional material

Before the authorized fresh Review-B processes closed, one earlier process
pre-created same-timestamp placeholder files in the batch `p187_b`, `p188_b`,
`p189_b`, `p190_b`, and `p191_b` directories and wrote premature paper-local
claims that Review B and terminal QA were complete.  Those claims were not
accepted: the process did not perform the assigned P189 review, the manifests
were malformed or incomplete, and no terminal cold-build population existed.

The placeholders and their assertion counts are excluded from every aggregate
in this batch. P189's competing directory was renamed
`p189_b_preliminary_superseded/` once the authoritative paper-local Review B
closed. A later byte-identical convenience copy of the authoritative P189
package was renamed `p189_b_duplicate_mirror_excluded/`; it contributes zero
additional review or assertion count. The separate Git mirror's checkpoint commit
`a5c9e41e8d07006916148bb581ad8748bad7a9d9` preserves the pre-terminal state;
its placeholder claims are not authoritative evidence. The settled working
result does not silently count provisional material as a review.

## Authoritative review routing

| paper | formal Review A | authorized fresh Review B |
|---:|---|---|
| P187 | `docs/papers187_191_sequence/reviews/p187_a/` | `docs/papers187_191_sequence/reviews/p187_b/` |
| P188 | `docs/papers187_191_sequence/reviews/p188_a/` | `docs/papers187_191_sequence/reviews/p188_b/` |
| P189 | `papers/189-transpose-row-compression/reviews/round1/reviewer_a/` | `papers/189-transpose-row-compression/reviews/round2/reviewer_b/` |
| P190 | `docs/papers187_191_sequence/reviews/p190_a/` | `docs/papers187_191_sequence/reviews/p190_b/` |
| P191 | `papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/` | `docs/papers187_191_sequence/reviews/p191_b/` |

P191's `p191_a_preliminary_superseded/` directory is an auxiliary early audit,
not a formal third review. `P191_PRELIMINARY_A_SUPERSEDED.md` records why its
accepted-ledger rebound does not promote it to a formal review.

## Acceptance rule

A Review-B result enters the batch only after the authorized fresh process
supplies a reviewer-owned implementation, canonical transcript, exact input
pins, proof/source/artifact records, accepted delta record, two fresh replay
receipts, and a passing non-self-referential manifest.  The root process then
replays the canonical independently.  Until all five meet that rule, Round 2
and terminal QA remain pending.  Every state remains
`OWNER_AMBER / HOLD_EXTERNAL`.
