# Claims–evidence ledger — P147

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

| claim | proof object | exact pressure | owner boundary |
|---|---|---|---|
| `A_n` preserves total and strictly shortens every nonfixed state | maximal-run factorization | checked at every enumerated state | elementary, zero credit alone |
| fixed points are adjacent-unequal compositions | run length one iff unchanged | fixed criterion and Carlitz census through `n=18` | Carlitz class/enumeration directly owned |
| `tau(alpha)<=floor(log2 n)` | backwards newly-created-run chain; weight doubles at every dependent round | pointwise bound on all 262,143 states | iterative claim retained |
| maximum clock equals `floor(log2 n)` for every `n` | explicit cascade `C_t` plus safe remainder placement `W_n` | witness constructed and replayed for every `n<=18` | retained |
| `[u^ell]Phi_beta` is the length-`ell` fibre for `beta in Comp(n)` | bijection between source runs and adjacent-unequal positive-divisor choices | every target in each exact-total layer through 18, including empty fibres | retained |
| fixed-class OGF | last-part decomposition | DP census only | classical, explicit zero credit |

The verifier is not proof evidence for unbounded claims.  Its role is to make
literal-map errors, boundary mistakes, false equality witnesses, or omitted
target fibres reproducibly visible.

## Review closure

Review A's proof/interface/source findings (0 Critical / 1 Major / 3 Minor)
were repaired by the formal ancestor selector, exact-total target typing,
explicit extremal witness orbits, and updated closest-source subtraction.
Review B found 0 / 0 / 0 surviving defects after a 2,690,869-assertion cold
replay, an isolated byte-identical build, and inspection of all four pages.
The owner boundary remains strict: only the clock-plus-target-inverse residual
is retained; classical/static/evolutionary neighbours receive zero credit.
