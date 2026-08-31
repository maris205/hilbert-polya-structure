# P136 claims--evidence ledger

Status: `ROUND1 / REVIEW_A_REPAIRED / HOLD_EXTERNAL`.

| ID | Exact claim | Formal support | Executable support | Owner subtraction / boundary | Status |
|---|---|---|---|---|---|
| `P136-C0` | The fixed-rate, independent-mark clock construction realizes the literal rate-proportional edge / uniform-vertex process. | `main.tex`, “Model and marked order.” | Every enumerated dynamic law is compared with a law derived from this representation. | Exponential races, memorylessness, and size-biased order are Plackett/Gnedin background; zero credit. | Proved; owned engine. |
| `P136-C1` | For every proper petal mask `A`, the weighted endpoint mass is the displayed inclusion--exclusion integral/sum; the all-petal mass is `product r_i`. | Theorem 3.1 and its proof. | 1638 weighted aggregate inputs on `c in {1,2}`, `m in {1,2,3}`, and `p_i,lambda_i in {1,2,3}`, plus the unit-rate lane. | The random covering process is Bar-Yehuda/Pitt; only this closed restricted-carrier law remains. Arbitrary positive real rates are proved, not exhaustively enumerated. | Proved; exact controls pass. |
| `P136-C2` | Every precise core-stopped endpoint has mass `pi(A)/(c product p_i)` and every precise all-petal endpoint has mass `product 1/(c+p_i)`. | Corollary 3.2 and its sigma-field conditioning proof. | 78 unit-rate actual-vertex inputs on `c in {1,2}`, `m in {1,2,3}`, and `p_i in {1,2,3}` enumerate marks directly. | Conditional uniform marks are elementary; the refinement is low-value alone and is claimed only as part of the atlas. Weighted resolved endpoints are not claimed as exhaustively checked. | Proved; bounded resolved control. |
| `P136-C3` | At unit rates, the discrete choice count satisfies `Pr(T>t)=e_t(r)/binom(m,t)` and the complete mass/PGF follows. | Theorem 4.1 and Corollary 4.2. | 4092 unit-rate aggregate inputs compare every step-count mass. | Uniform random order and symmetric-polynomial algebra receive zero credit. | Proved; exact controls pass. |
| `P136-C3a` | `T=m` is the disjoint union of the all-petal endpoint and a final core choice, and equals `e_(m-1)(r)/m`. | Equation (4.4) and proof. | Explicit exact identity check for every unit-rate input. | This repair prevents conflating two different terminal events. | Proved; explicit control. |
| `P136-C4` | `E[T]`, `E[T^2]`, and `Var(T)` equal the displayed finite tail sums. | Corollary 4.2 and indicator proof. | Dynamic first and second moments are compared with both tail sums for every unit-rate input. | Tail-sum identities are standard; zero credit. | Proved; explicit controls. |
| `P136-C5` | On a vertex-disjoint forest, the fully marked stopped endpoint law tensorizes, discrete choice counts add, and their PGFs multiply. | Theorem 5.1 and coupling proof. | Three unit-rate and one unequal-rate two-component controls compare all joint endpoint masses and step-count convolutions. | Generic dissociation/independence on disjoint exponential-order restrictions is Gnedin/background. Continuous elapsed time is not analyzed; under the embedding, forest completion time is the maximum of component stopping times, not a sum. Arbitrary forests are not exhaustively enumerated. | Proved; four bounded controls. |
| `P136-E1` | The frozen verifier uses exact rational arithmetic without sampling, floating point, network, or third-party libraries. | `code/verify.py` source contract. | 5812 inputs, 174170 exact assertions, and fresh byte replay with exit code 0. | Computational agreement is falsification evidence, not proof or novelty evidence. | Pass; frozen result recorded in `CONTROL_RESULTS.md`. |

## Kill conditions retained

The note is killed or must be repositioned if a direct source is found that
prints the full package of weighted sunflower-mask law, actual-vertex
refinement, uniform choice-count PGF/moments, and marked forest product. A direct
owner of only the process, exponential order, or independence principle does
not invalidate the formulas, but it removes all credit for those ingredients;
that subtraction has already been made.
