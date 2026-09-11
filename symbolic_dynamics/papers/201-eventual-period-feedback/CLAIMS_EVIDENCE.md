# P201 claims–evidence register

Status: proved internal contract; Round0 author checks passed; independent manuscript Review A/B pending; OWNER_AMBER / HOLD_EXTERNAL.

| ID | Exact domain and claim | Proof in main.tex | Verification / subtraction |
|---|---|---|---|
| C201.1 | Every n≥1: total numerical period operator; rank packing r(f)≥Q(r(Pf)) | Lemma 2.1 | Every source n≤7; generic cycle finding and generic rank descent are background |
| C201.2 | Zero is the only recurrent state; exact core-extension relation, including zero-core exception | Proposition 2.2, Lemma 2.3 | Full finite functional graphs and explicit padding controls |
| C201.3 | Height≥h≥2 forces rank≥N_h; exact all-size/all-rank maxima with rank-one boundary | Theorem 3.1 | Every rank maximum n≤7 and witnesses through n=26796; sequence itself is known |
| C201.4 | At n=N_h, all deepest states have exactly the stated recursive cycle-block structure; D_h factorial recursion | Theorem 4.1 | Complete equality iff and census at n=2,3,6; proof, not construction alone |
| C201.5 | All targets: block-product fibres, empty-fibre criterion, constrained multinomial first-image count | Theorem 5.1 | Actual fibres every source n≤7; every target including absent n≤6; static a_d and forest formulas classical |
| C201.6 | Unique largest fibre is zero, of size (n+1)^(n−1), including n=1 | Theorem 5.2 | Full maximizing-target sets n≤7; strict connected comparison and excluded cross-block forest proof |

The standalone paper-local [verifier](code/verify.py) and [canonical transcript](code/CANONICAL.txt) give **3,366,093 assertions**. The n=7 full box has 823,543 states, 1,085 first-image targets, maximum height four, and a unique largest fibre 262,144. Its critical height witnesses at sizes 2,3,6,21,231,26796 have heights 2,...,7.

Two fresh canonical runs are in qa_round0/attempt1/verifier1.stdout and verifier2.stdout. Source uses a functional-graph peeling update; independent orbit tracing covers all inputs n≤6 and the first 256 at n=7. Do not say both implementations exhaust n=7. Critical equality is tested at sizes 2,3,6, not by enumerating every permutation at sizes 21 or larger.

Provenance: [accepted proof](../../docs/papers197_201_sequence/scouting/fifth_fresh_20260905/period_feedback_reentry/THEOREM_CONTRACT_AND_PROOF.md), [independent Stage1 gate](../../docs/papers197_201_sequence/reviews/period_feedback_stage1_20260905/GATE_REPORT.md), [gate proof audit](../../docs/papers197_201_sequence/reviews/period_feedback_stage1_20260905/PROOF_AUDIT.md), [central freeze](../../docs/papers197_201_sequence/FIVE_SEAT_FREEZE.md). The independent Stage1 count 5,885,458 is not this paper's author-verifier count and is not manuscript Review A or B.

Excluded claims: novel threshold sequence; novel static SET/CYC or forest counts; scalar rank evolution equality; closed individual height; all-size deepest-state enumeration beyond critical sizes; all-time inverse; blanket exemption from historical lane bans; external novelty or complete owner clearance.

