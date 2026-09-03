# Claim–evidence matrix — P173

**Round:** dual-review closed; final reproducibility QA complete  
**Lifecycle:** `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`

| Claim | Uniform proof in `main.tex` | Independent exact pressure |
|---|---|---|
| Every-target ambient fibre | Surjective restriction/quotient map, common lift dimension, injective induced map | Exhausts every binary `T` and every `B <= U` for `n<=3` |
| Dimension quotient is stochastic | Sum over Gaussian target layer | Exact row sums for four `q` values through `n=9` |
| Every-time labelled kernel | Nestedness plus stabilizer transitivity | Full labelled matrix powers for `q=2`, `n<=3`, `t<=4` |
| Algebraic spectrum | Dimension-ordered triangular matrix and exact self-loops | Literal diagonal checks and quotient reconstruction |
| Complementary `J_2` ladder | Strict concavity plus positive adjacent-transition eigenvector obstruction | Exact nullities of `Q-lambda I` and its square for `q=2,3,4,5`, `n<=9` |
| Endpoint Jordan inventory | for `n>=1`, the constant right vector and the full-dimension indicator are independent; for `n=0`, `Q=(1)` | author sentinel checks one `J_1(1)` at `n=0`; Review A checks explicit endpoint eigenvectors and the corrected nullities |
| Proper-state absorption | Finite nested chain with positive strict-loss probability | Positive exact mean recursion and `n=2` boundary |

The verifier is a falsifier, not a proof of the all-parameter theorem or a
novelty test.  External status is `HOLD_EXTERNAL`.

Hostile Review A used an independent RREF/annihilator implementation and
passed 36,390 exact assertions: complete literal boxes over `q=2,n<=3` and
`q=3,n<=2`, plus quotient/Jordan/absorption boxes for eight prime powers
through `n=14`.  It exposed and forced closure of the `n=0` endpoint-block
exception, the visible exponent typo, the uniform/nonuniform owner
attribution, and the paper-local P109/P162/P165/P168 firewall.

Hostile Review B independently passed 9,995,101 projective-incidence
assertions.  Evans Theorem 3.5 and Van Peski Theorem 3.3.4 with
(3.42)–(3.55) are now explicit zero-credit owners of the dimension-chain and
labelled uniform-square-kernel/fixed-target injection architecture.  P172 is
also reciprocally subtracted: fresh maps, nesting, quotient recovery,
triangular/Jordan tactics, and absorption are shared shell.  Thus C1–C3 are
exact statements needed to derive the paper, but their generic kernel and
powering ingredients are not claimed as residual progress.  The retained
axis is the linear injection fibre, the fixed-ambient rectangular schedule
`a -> n-a`, and the complementary-dimension `J_2` ladder it forces; by
contrast P172 retains specified-box set-image occupancy and one terminal
`J_2`, so neither residual transfers to the other.

Both hostile reviews and their read-only delta acceptances are closed with
zero open findings.  The three exact controls replay byte-identically, and
two independent source-only cold builds reproduce the locked Round-2 PDF.
