# P155 claims–evidence ledger

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.  The freeze contract is
an absolute claim ceiling.  Enumeration never proves an all-parameter claim.

| ID | Exact claim | Deductive support | Exact-control support | Ownership / limitation | Status |
|---|---|---|---|---|---|
| `P155-C1` | `C(pi)` is a permutation of length equal to the number of cycles of `pi`. | One output letter is read from each uniquely determined cycle support. | Literal support extraction for all sources through rank 10. | Disjoint-cycle notation and standardization are zero credit. | Proved; controls pass. |
| `P155-C2` | `sigma in C(S_n)` iff `n >= mu(sigma)=2m-rlmin(sigma)`. | Singleton necessity plus the greedy opener/closer/simultaneous schedule. | 145,684 target/rank cells; independent endpoint DP on 46,233 targets. | Static block endpoints and RTL-min distributions are zero credit. | Proved; controls pass. |
| `P155-C3` | Every admissible source rank has an explicit right section. | Minimum schedule, then split simultaneous events and insert interior coordinates. | 3,161 literal constructed section cells. | Constructive existence only; no iterated-preimage optimum. | Proved; controls pass. |
| `P155-C4` | `|C_n^{-1}(sigma)| = sum_P prod_i(|B_i|-1)!` over the prescribed ordered supports. | Unique support partition; `(b-1)!` independent cyclic orders on a fixed block; reversible reconstruction. | 53,218 target fibre cells through rank 8; 5,295 support terms; totals equal `n!`. | Fixed-support cyclic-order counts and set-partition technology are zero credit. | Proved; controls pass. |
| `P155-C5` | Identities are exactly the fixed/recurrent states; every nonidentity step strictly drops rank. | Output rank equals cycle count; rank equality forces all singleton cycles. | 4,037,913 literal states; one fixed state in every tested rank. | Generic finite-map rank monotonicity is zero credit. | Proved; controls pass. |
| `P155-C6` | Image census is the unsigned-Stirling sum in the manuscript. | Combine the threshold with the classical RTL-min distribution. | Image sizes `1,2,4,8,17,39,96,253,706,2074`. | Stirling/record distribution is explicitly zero credit. | Corollary of C2. |
| `P155-X1` | No power-of-two maximum clock is claimed. | The required all-parameter lower bound is absent. | Transcript prints `power_of_two_clock=NOT_CLAIMED`. | Finite maxima through rank 10 are observations only. | Excluded. |

## Zero-credit inputs

- block minimum/maximum and opener/closer/singleton terminology;
- crossing/nesting distributions at fixed endpoint sets;
- cycles ordered by increasing minima;
- prescribed cycle-maxima sets;
- the elementary `(b-1)!` count on a fixed support;
- unsigned Stirling and right-to-left-minimum distributions;
- generic finite functional-graph bookkeeping.

## Scope sentinels

- `C` is exactly the map defined in `main.tex`; no other cycle selector is
  covered.
- The right section is target- and source-rank resolved.
- Fibre weights count complete labelled permutations, not merely supports.
- No claim about a sharp absorption clock, arbitrary pointwise tail, or
  global iterated-preimage minimality is active.
- A bounded owner-search non-hit is not novelty, priority, or clearance.

## Internal review closure

Hostile Review B independently rederived every active claim, verified both
Review-A repairs, and returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. No claim or manuscript
change was made for Round 2.
