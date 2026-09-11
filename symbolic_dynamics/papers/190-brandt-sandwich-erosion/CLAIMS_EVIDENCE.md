# Claims-to-evidence ledger — P190 Round 0

| claim | deductive location | exact author-side pressure |
|---|---|---|
| local Brandt filter and all-time good-run normal form | Lemma 2.1 and Theorem 2.2; Proof Package Steps 1–2 | every state and times `0..m+1` in 26 boxes |
| fixed-state odd/even formula | Corollary 2.3; Proof Package Step 3 | every state in all boxes |
| pointwise tail and sharp maximum, including `n=1` | Theorem 2.4; Proof Package Step 4 | every orbit; `n=1`, `m=1..10` |
| `m=1,2` fibre and tail boundaries | Remark 2.5 and Section 3 | explicit target-by-target assertions for `n=1..5` |
| every-target trace with correct row/column direction | Theorem 3.1; Proof Package Step 5 | cyclic-path DP versus literal source fibres for every target; dense products in small boxes |
| nonzero-anchor gap product and exact image criterion | Theorems 3.2 and 3.4; Proof Package Steps 6 and 8 | every target in all 26 boxes |
| all-zero recurrence and spectrum, including `+/-1` multiplicities | Theorem 3.3; Proof Package Step 7 | integer eigenspace basis checks for `n=1..5`; trace comparison in every box |
| mass conservation | Corollary 3.5; Proof Package Step 9 | exact sum over every target in every box |

The proofs establish the all-parameter claims.  `code/verify_p190.py` is an
author-side regression control derived independently from the literal update;
it is not process-separated review, proof, novelty evidence, or ownership
clearance.  Two fresh runs must match `code/CANONICAL.txt` byte for byte before
the Round-0 freeze.

