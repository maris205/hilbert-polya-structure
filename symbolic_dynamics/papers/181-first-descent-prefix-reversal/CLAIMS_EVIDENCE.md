# Claims and evidence — P181

**Status:** `ROUND2_DUAL_REVIEW_ACCEPTED / OWNER_AMBER / HOLD_EXTERNAL`

| ID | Exact claim | All-parameter proof route | Author-side paper-local attack |
|---|---|---|---|
| C1 | the image is exactly the `n!/2` permutations beginning with an ascent | every nonfixed output begins with the reversed descent pair; `rho_2` supplies every inverse; first-position swap halves `S_n` | compare the complete literal image with the ascent set through `S_9` |
| C2 | recurrent states are the identity plus `n!/3` position-two peaks, paired into `n!/6` two-cycles | peaks trigger `rho_3` and remain peaks; every other nonidentity image state maps to a peak | compute every orbit coordinate and every peak partner through `S_9` |
| C3 | tail populations are `n!/3+1`, `n!/2`, `n!/6-1`, with no depth above two | noncore image states have run length one and are in bijection under `rho_2` with depth-two sources; subtract remaining states | compare the tail of every permutation and the literal depth-two pair map |
| C4 | `F^(-1)(tau)={rho_k(tau):2<=k<=r(tau)+1}`, plus the fixed identity when `tau=id` | reverse the source first-descent inequalities; involutivity of `rho_k`; distinct first entries for distinct `k` | compare full predecessor sets—not merely sizes—for every target through `S_9` |
| C5 | for `n>=4`, maximum fibre is `n-1`, at exactly the `n-1` targets with `tau_2=n` and decreasing positions `2,...,n` | maximize the run, force `n` into position two, choose `tau_1`, force the rest | compare maximum, complete maximizing set, and count through `S_9` |
| B1 | `n=1` has the sole fixed arrow `1->1`, singleton image/core, depth zero, and fibre one | direct calculation | complete `S_1` box |
| B2 | `n=2` has arrows `12->12`, `21->12`, and unique fibre two at the identity | direct calculation | complete `S_2` box |
| B3 | `n=3` has one fixed point, one two-cycle, three depth-one states, and three maximum fibres of size two | direct six-arrow atlas | complete `S_3` box |

The verifier makes 6,273,070 integer assertions and its 19-line canonical
transcript is byte-reproducible.  It makes no infinite-family, novelty,
priority, or release claim.

Two process-separated hostile reviewers accepted this complete claim package
with zero open findings.  Their distinct exact controls make 17,364,060 and
377,591 assertions, respectively; these controls are falsification pressure,
not substitutes for the all-parameter proofs or evidence of ownership.

## Zero-credit boundary

No separation credit is assigned to the prefix-reversal operation, pancake
sorting or its graph/distance, longest-increasing-prefix selection, elementary
descent and peak counts, or generic finite functional-graph bookkeeping.
P122's permutation reversal and target-local inverse vocabulary are also
subtracted.  Project Euler First Sort owns the different follower-to-front
update, while the FAR scout is a value-complement conjugate and earns no new
credit.  The retained conjunction remains owner-thin.
