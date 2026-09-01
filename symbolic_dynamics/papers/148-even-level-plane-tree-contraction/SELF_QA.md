# Internal proof and artifact QA — P148

**Mode:** author-side self-QA, not an external or hostile review  
**Status:** AUTHOR REPAIR AFTER HOSTILE-A CRITICAL OWNER HIT  
**External status:** `HOLD_EXTERNAL`

## Frozen-contract audit

| Contract item | Result | Location |
|---|---|---|
| finite self-map on `PT_{<=N}` distinguished from exact layer `PT_n` | PASS | opening definition and explicit arbitrary-`N` quantifier convention |
| original depths divisible by `2^k`, induced ancestry/order | PASS | Theorem 1 and labelled induction |
| height identity and pointwise clock | PASS | equation (2) |
| sharp every-`n` clock with paths | PASS | equation (3) and proof |
| singleton unique fixed/recurrent state | PASS | strict size descent |
| local fibre factor and reversible construction | PASS | Lemma 2 |
| global fibre series and binomial coefficient | PASS | Theorem 3 |
| exact-size image condition | PASS | Corollary 4 |
| local image specification and algebraic image series | PASS | equations (8)--(11) after QA |
| direct outward-contraction subtraction and `HOLD_EXTERNAL` | REPAIRED; independent review B pending | introduction, Limitations, source ledger |

## Proof stress tests

- `k=0`, height zero, and the singleton are handled explicitly.
- A deepest path contains every depth, so the clock is an equality rather
  than an unsupported bound.
- For a target leaf, the local factor is `1/(1-y)`; for a target internal
  vertex, at least one productive odd child is forced.
- Empty odd leaves occupy `r+1` gaps, including both exterior gaps.
- Multiplication counts each inserted odd vertex exactly once at its retained
  parent.
- The manuscript now exposes the recursive bijection
  `F_U=A_d product_j F_{U_j}`, including coefficientwise finiteness.
- The singleton target has one predecessor at every exact size: a star,
  agreeing with the binomial formula.
- The image condition is obtained from coefficient nonvanishing and is never
  confused with size preservation.

## Round-0 snapshot and changes

- Round-0 PDF: 4 pages.
- SHA-256:
  `b32439d6be070d10bd54ff05a60b9920db176dcaf81c6a6a96fc939dd8db88d2`.
- Self-QA added the explicit convention that all-rank statements are read
  inside a fixed carrier with `n<=N`.
- Self-QA added the closed algebraic branch for `H(z)`; no theorem was
  broadened.

## Artifact QA

- Verifier canonical replay: PASS, 216,905 assertions.
- Bibliography: five cited primary records; the Berkemer journal year/name are
  corrected and the direct outward-contraction owner is printed.
- Required declarations: Data Availability, Ethics Statement, Author
  Contributions, Conflict of Interest, Funding, and Limitations all present.
- Anonymous author block and blank PDF author metadata are present.
- `HOSTILE_REVIEW_A.md` is preserved; it triggered the direct-owner repair.
  Independent review B remains mandatory before internal acceptance.

## Residual risks

The unordered primitive is directly owned; only the ordered
iterate/fibre/image conjunction remains under a bounded non-hit.  Neither the
proof nor finite computation establishes novelty, priority, or release
clearance.
