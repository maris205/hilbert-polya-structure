# P142 claims--evidence ledger

Status: `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`.  The P142 entry of
`FINAL_THEOREM_CONTRACTS.md` is an absolute claim ceiling.  Exact enumeration
is falsification evidence and never the proof of an all-parameter statement.

| ID | Exact claim | Formal support | Executable support | Ownership / limitation | Status |
|---|---|---|---|---|---|
| `P142-C1` | For odd prime `p`, `F_(p,e)(p^a)=p^min(2a,e-a)`. | Lemma 2.1, by factoring the smaller power and checking the equal-valuation unit. | Literal gcd equality at every state in 508 boxes. | Valuation algebra is zero credit.  The statement excludes `p=2` for a necessary reason. | Proved; exact controls pass. |
| `P142-C1B` | If `p=2` and `e=3a`, the literal output valuation is `2a+1`; `(e,a)=(3,1)` is the smallest failure of the odd-prime rule. | Remark 2.2 and direct factor `2^(2a)(1+1)`. | Every binary state for `2<=e<=48`; sixteen equal-valuation cases. | Boundary statement only; no characteristic-two replacement theorem is claimed. | Proved; exact controls pass. |
| `P142-C2` | The recurrent set is `{0} union [L,U]`; it consists of `A` fixed states and `(R-A)/2` strict two-cycles, yielding the parity law for `Fix(T_e^k)`. | Theorem 3.1, using the invariant band and entry proof. | Complete functional graphs and iterates `1<=k<=12` in all odd-prime boxes. | Finite-map and Artin--Mazur bookkeeping are zero credit. | Proved; exact controls pass. |
| `P142-C3` | The complete four-case entry-time formula holds; `M_e=1+ceil(log_2 L)`, uniquely at `e-1` for `e>=4` and uniquely at `e` for `e=2,3`. | Theorem 4.1 and its dyadic-threshold/uniqueness proof. | Every bounded state and exact deepest set. | Ceiling-log algebra and the real map silhouette are zero credit. | Proved and sharp; controls pass. |
| `P142-C4` | With the displayed `c_j`, the temporal polynomial is `R+z+(1+z) sum c_j z^j`. | Theorem 4.2, by exact dyadic intervals and reflected partners. | Complete depth histograms for all 508 odd-prime boxes. | Formal generating-function packaging is zero credit. | Proved; exact controls pass. |
| `P142-C5` | `im(T_e)=[0,U]`; the fibre over every target is the displayed set union of the reflection and even doubling preimages, empty beyond `U`. | Theorem 5.1, solving both branches with their inequalities. | All 33,528 target cells across the odd-prime sweep; all branch coincidences checked as sets. | General inverse-branch language is zero credit. | Proved; exact controls pass. |
| `P142-E1` | The paper-local audit is deterministic exact arithmetic with no sampling, floating point, external CAS, network, or third-party package. | `verify_p142.py` source contract. | Frozen `verification_output.txt`; 319,074 assertions and byte replay. | Computation cannot establish novelty, ownership, or the all-parameter theorem. | Pass. |

## Zero-credit inputs

- elementary `p`-adic valuation of a sum with unequal valuations;
- general piecewise-monotone interval dynamics and kneading theory;
- real piecewise-linear/tent-map geometry;
- finite/discretized tent-map constructions and cycle statistics;
- generic finite functional-graph, cycle, fixed-iterate, and zeta identities;
- ceiling-log arithmetic and formal generating-function bookkeeping.

## Scope sentinels

- The prime is odd and fixed, and `e>=2`.
- The carrier is exactly the divisor chain `{p^a:0<=a<=e}`.
- The update is the literal integer gcd, not an independently proposed real
  interval map.
- Entry time means first entrance into the recurrent set.
- The temporal polynomial counts all `e+1` exponent states by entry time.
- Fibres are sets; the two candidates are counted once when `3b=2e`.
- The `p=2` calculation is a negative boundary, not a second dynamical atlas.
- A bounded direct-owner non-hit is not novelty, priority, or clearance.
- If the arithmetic lift is judged cosmetic, the paper must be killed rather
  than broadened.
- External posting, specialist contact, submission, and release remain
  unauthorized.
