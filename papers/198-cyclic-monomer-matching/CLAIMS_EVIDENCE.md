# P198 claims–evidence register

Status: proved internal contract, Round0 author checks passed, independent manuscript reviews pending, OWNER_AMBER / HOLD_EXTERNAL.

| ID | Exact claim and domain | Full proof in main.tex | Bounded evidence / credit boundary |
|---|---|---|---|
| C198.1 | The specified rule is a self-map on all matchings of every odd simple cycle n≥3 | Lemma 2.1 | Full closure checks; classical alternating-path fact |
| C198.2 | Pointwise tail m−|M|, one n-cycle, unique deepest empty state, no fixed point | Theorem 3.1 | Indegree-peeling full functional graphs; clock/rotor not independent novelty |
| C198.3 | All target fibres T_floor(u/2)+1_maximum, with an exact interval predecessor bijection | Theorem 4.1 | Actual indegree and independent endpoint-set predecessor equality for every target, including empty fibres |
| C198.4 | Unique maximal fibre at monomer n−1, size 1+T_m | Corollary 4.2 | Exact set of maximizing targets, not just value |
| C198.5 | First-image count F_(n−1)+F_(n−3)+2 | Corollary 5.1 | Every exact image; consequence of atlas and classical path counts |
| C198.6 | Every depth coefficient n/(n−r) binom(n−r,r) | Corollary 3.2 | Every coefficient; classical static enumeration, zero independent credit |

The paper-local code and canonical output are [code/verify.py](code/verify.py) and [code/CANONICAL.txt](code/CANONICAL.txt). Box: all matchings for each odd 3≤n≤21; **237,845 assertions**. At n=21: 24,476 states, 9,351 image states, 21 recurrent states, maximum tail 10, unique maximum fibre 56. Two fresh replay files are retained in qa_round0/attempt1/. No claim is established merely by these checks.

Provenance: [CMM_THEOREM_CONTRACT.md](../../docs/papers197_201_sequence/scouting/graph_matching_lane/CMM_THEOREM_CONTRACT.md); independent [stage1_hostile_gate_algebra.md](../../docs/papers197_201_sequence/reviews/stage1_hostile_gate_algebra.md); [FIVE_SEAT_FREEZE.md](../../docs/papers197_201_sequence/FIVE_SEAT_FREEZE.md). The whole graph/matching scout's 2,508,857 assertions are not this paper's count. Stage1 admission is not a Round0 manuscript Review A or B.

Exclusions: no standard augmentation innovation; no novel static matching formula; no arbitrary-graph guarantee; no all-time inverse atlas; no external novelty, priority, or source-complete ownership claim. P51–P56 missing manuscripts remain a historical limitation.

