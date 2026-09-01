# P140 claims--evidence ledger

Status: `ROUND1 / REVIEW_A_REPAIRED / GO_INTERNAL / HOLD_EXTERNAL`.

| ID | Exact claim | Formal support | Executable support | Owner subtraction / boundary | Status |
|---|---|---|---|---|---|
| `P140-C1` | A two-run word `0^a1^b` remains two-run, with three successor types and the stated multiplicities. | Proposition 2.1 and proof in `main.tex`. | Direct state recurrences and literal word updates are compared on bounded grids. | The majority gate is background; the shrinking closure is process-specific. | Proved; exact controls pass. |
| `P140-C2` | `P(1)=(b-1)/(n-2)`, `P(0)=(a-1)/(n-2)`, with terminal history counts `(b-1)(n-4)!!` and `(a-1)(n-4)!!`. | Theorem 2.2 and proof. | All two-run pairs through `n=201`; literal dynamic checks through `n=15`; all-word history denominators through `n=15`. | Every history means a sequence of current window positions. | Proved; exact controls pass. |
| `P140-C3` | The marked cross-history polynomials obey the displayed recurrence and symmetry; their support and linear coefficient are exact. | Theorem 3.1 and Corollary 3.2. | Polynomial recurrence through `n=101`, literal marked word histories through `n=13`, including coefficient/support checks. | Generic generating-function marking is elementary and receives zero credit. | Proved; exact controls pass. |
| `P140-C4` | The holding-time vector is independent of the complete embedded window-choice history; at `n=1` both vectors are empty and `tau_1=0` almost surely. | Theorem 4.1, boundary sentence, and exponential-race/strong-Markov proof. | Every binary word through `n=11` satisfies the exact joint Laplace factorization at `s=3`, including the length-one empty history. | Equal-rate races and memorylessness are standard; zero credit. | Proved; Round-A boundary repaired. |
| `P140-C5` | For `n=2m+1>=3`, `exp(-2 tau_n)` is `Beta(1/2,m)`; along `m -> infinity`, `m exp(-2 tau_n)` tends to `Gamma(1/2,1)`. The Laplace and moment formulas extend to `n=1` by empty products/sums. | Corollary 4.2, its preceding boundary paragraph, and Theorem 4.3. | Exact product transforms for odd `n<=201` and integer `s=1,...,10`; the limiting step is analytic, not simulated. | `Beta(1/2,0)` is not asserted. Beta--Gamma identities and convergence are standard machinery. | Proved; Round-A scope defect closed. |
| `P140-E1` | The local verifier uses exact rational arithmetic only, without sampling, floating point, network, or third-party packages. | `code/verify.py` source contract. | Canonical stdout is byte-replayed; assertion and grid counts are frozen. | Finite computation is falsification evidence, not proof or novelty evidence. | Pass. |

## Kill conditions retained

Reposition or kill the note if a direct source is found for the literal
random adjacent-triple contraction together with the two-run endpoint,
cross-history, and continuous clock package. Sources owning majority as an
operation or majority dynamics on fixed carriers subtract motivation but do
not by themselves print this theorem package. External status stays on hold.
