# Internal proof and artifact QA — P149

**Mode:** author-side self-QA, not an external or hostile review  
**Status:** ROUND-2 INTERNAL REVIEW ACCEPTED  
**External status:** `HOLD_EXTERNAL`

## Frozen-contract audit

| Contract item | Result | Location |
|---|---|---|
| literal finite carrier `S_{<=N}` and endpoint-zero convention | PASS | opening definition |
| one-step packing for every source | PASS | equation (2) |
| explicit high/valley/decreasing-tail section | PASS | equation (3), Lemma 1 |
| both inclusions for every iterate image | PASS | Theorem 2 |
| right section at every feasible rank | PASS | minimal odd-length chain in Theorem 2 |
| factorial image cardinality | PASS | disjoint-rank corollary in Theorem 2 |
| pointwise upper clock and sharp every-`n` witness | PASS | Theorem 3 and equation (8) |
| singleton unique recurrent state | PASS | strict rank descent |
| complete comparison-word/poset fibre | PASS | Theorem 4 |
| exact-boundary, one-sided, and ordinary-pinnacle owners separated; fibre secondary | REPAIRED after Review-B Major | introduction, post-Theorem-4 boundary, source ledger |

## Proof stress tests

- The global maximum makes the extracted word nonempty.
- Endpoint peaks are handled separately from interior `UD` peaks.
- In the section, valleys use `1,...,m-1`, highs use the top `m` values, and
  the decreasing tail uses exactly the remaining values.
- When the tail is empty, the last high is a peak against boundary zero; when
  nonempty, every tail entry has a larger left neighbour.
- `m<=ceil(n/2^k)` is converted to the exact integer condition
  `n>=2^k m-(2^k-1)`.
- Large `k` is covered: any inner `L_{1,1}` is the identity.
- The recursive deepest witness saturates the packing bound at every
  intermediate rank.
- Base peak positions are maximal in the adjacent-comparison poset, so adding
  the target peak chain is acyclic.
- The cases `m>ceil(n/2)` and `n=m=1` are explicit in the fibre theorem.

## Round-0 snapshot and changes

- Round-0 PDF: 4 pages.
- SHA-256:
  `2cbd557258087f59dc5a378a379137b137d85a0d767a20da6f919bb47d0e8dcd`.
- Self-QA added the fixed-carrier convention `n<=N`.
- Self-QA made the pointwise clock inequality explicit in the theorem.
- Self-QA recorded the `L_{1,1}` large-iterate boundary.  No claim was
  broadened.

## Artifact QA

- Verifier canonical replay: PASS, 1,228,181 assertions.
- Bibliography: nine cited primary sources with stable journal/DOI metadata;
  Ji's exact convention, Fu's one-sided convention, the padding bridge,
  fixed-set neighbours, and run-sorting equidistribution are explicitly
  zero-credit.
- Required declarations: Data Availability, Ethics Statement, Author
  Contributions, Conflict of Interest, Funding, and Limitations all present.
- Anonymous author block and blank PDF author metadata are present.
- `HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md` are preserved.  Review B
  found no theorem defect but exposed the Fu convention mismatch; Ji 2025 now
  supplies the directly inspected exact static owner.  Carlitz--Scoville is
  not assigned priority without direct access to the original text.

## Residual risks

The direct-owner search is bounded.  The comparison-poset fibre uses standard
technology and is intentionally secondary.  Neither finite computation nor a
search non-hit establishes novelty, priority, or release clearance.

## Final adjudication

The Review-B source-role Major and stale-build Minor are closed.  A source-wide
scan finds no active statement assigning Fu the exact two-zero convention.
The directly inspected Ji Definition 2.1 supplies the static exact-convention
owner, while Carlitz--Scoville receives no priority wording without direct
original-text access.  The final verifier replay is byte-identical, two
source-only builds reproduce the canonical PDF, and all four pages pass visual
inspection.  Internal result is `GO_INTERNAL`; external status remains
`HOLD_EXTERNAL`.
