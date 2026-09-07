# P210 claims/evidence matrix

Controlling ceiling: ../../docs/papers204_208_sequence/P210_ROOT_ADMISSION.md and FINAL_THEOREM_CONTRACTS.md §P210. All statements below are deductive for N≥1; finite author checks cover exactly N=1..12.

| Claim | Deductive manuscript evidence | Verifier evidence | Credit |
|---|---|---|---|
| Fixed points are exactly strict descents; every orbit fixes | §2 positivity/strict length descent | Every state, edge, depth, endpoint, fixed list | Background only |
| A deleted round-t cut has old left mass ≥t, and for t≥2 its right block was born at t−1 | Lemma leftmass, preceding surviving cut and integrality induction | Every orbit's deleted cuts with absolute intervals and right birth time | Temporal axis |
| Every round-t new block has mass ≥1+t(t+1)/2 | Lemma birthmass, first two disjoint parents | Every orbit's new-block interval, mass and birth record | Temporal axis |
| Maximum depth H(N); all-surplus descending-prefix witness | Theorem clock, full witness orbit induction | Every depth/max and every h≥1,r≥0 with 1+T_h+r≤12 | Temporal axis |
| Unique refinement segmentation and endpoint partition fibre formula | Lemma refinement and Proposition fibres, full proofs | All target source sets, partition coefficients, suffix endpoint DP and counts, including zero fibres | Support; ZERO independent credit |
| Three-branch scan characterizes the full image; thresholds are attained suffix minima | Theorem image and constructive proof | Every target, every suffix, actual first-part sets and minima; constructive feasible preimage | Structural axis |
| Explicit image ↔ nonempty triangular-part composition bijection, mass preserved | Theorem coding, complete parsing and inverse proof | Every image encoding and inverse, every independent triangular object's inverse and re-encoding | Same structural axis |
| Image series Theta/(1−Theta), known recurrence | Corollary series, positive-weight composition argument | Actual image counts equal independent triangular enumeration and known recurrence | Consequence of same axis, known count/technique |

The implementation uses cut-bitmask composition enumeration, accumulated sums with OLD adjacent comparisons, interval endpoints for births, and right-to-left endpoint-partition DP. It imports no pilot, candidate-gate, old-paper or reviewer code. The candidate assessor instead used persistent cell-set component unions, recursive composition generation and left-to-right transfer. Representation independence is implementation independence, not independent manuscript review. Direct coding follows the admitted proof and is not claimed to be a newly independent proof.

Complete canonical output stores all 4,095 states and edges, exact orbit/depth/fixed information, all 4,095 target fibres and explicit source lists, threshold rows for every suffix, all birth records, all in-box witnesses and both image/triangular coding directions. The parameters are fixed in verify.py and mirrored in PARAMETERS.json; no data file or input canonical is read by the verifier.

Lifecycle evidence is reported separately in AUTHOR_REPLAY.md and AUTHOR_BUILD.md after actual execution. Root's later physical freezes, manuscript A/B and terminal acceptance are not author evidence and remain unfulfilled at this handoff.
