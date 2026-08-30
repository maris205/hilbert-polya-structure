# Claims-to-evidence ledger

| ID | Claim | Proof location | Mechanical evidence | Credit status |
|---|---|---|---|---|
| C1 | Component partitions refine; even components freeze | Main Lemma 1.1 | Literal refinement asserted for every labelled graph through `n=6` | Residual structural input |
| C2 | Exact pointwise depth equals the maximum active split-tree height | Main Theorem 2.2 | Literal orbit depth equals a separately evaluated parity-pruned split depth for every graph through `n=6` | Core contribution |
| C3 | Recurrent iff every nontrivial odd component is co-connected; fixed iff components are singleton or even | Main Corollary 2.3 | Both iff criteria asserted state by state; both literal censuses compared exhaustively in aggregate at each order through `n=6` | Core classification |
| C4 | Every period is 1 or 2 | Main Corollary 2.3 | Exhaustive eventual-period ceiling through `n=6` | Consequence of C1--C3 |
| C5 | Maximum transient depth on `n` vertices is `floor((n-1)/2)` | Main Theorem 3.1 | Exact maxima through `n=6` | Core sharp theorem |
| C6 | `O_t=Q+Odd(exp(C_even+O_{t-1})-1-C_even-O_{t-1})` | Main Theorem 4.1 | EGF coefficients agree with exhaustive depth layers through `n=6` | Core all-depth census |
| C7 | `F_t=exp(C_even+O_t)` and `F_t-F_{t-1}` gives exact depth `t` | Main Theorem 4.1 | Cumulative counts through `n=6` | Core all-depth census |
| C8 | Fixed EGF is `exp(x+C_even)` | Main Proposition 4.2 | Fixed counts through `n=6` | Zero-credit bookkeeping consequence |
| C9 | Two-cycle count is `(r_n-f_n)/2`; zeta is `(1-z)^(-f_n)(1-z^2)^(-(r_n-f_n)/2)` | Main Corollary 5.1 | Recurrent/fixed census through `n=6` | Residual dynamical census consequence |

The paper-local verifier is `code/verify_odd_component_complementation.py`; its canonical output is frozen beside it. It executes 203,244 assertions and does not serve as a proof of the all-order theorems.
