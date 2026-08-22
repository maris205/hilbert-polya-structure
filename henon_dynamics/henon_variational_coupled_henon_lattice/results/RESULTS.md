# Results (C106)

## Exact orbit ledger

| object | period | monodromy trace | determinant | `det(I-zM)` coefficients (low degree first) |
|---|---:|---:|---:|---|
| origin fixed point | 1 | (27/2) | 1 | (1,-27/2,95/2,-27/2,1) |
| synchronous fixed point | 1 | (-13/2) | 1 | (1,13/2,25/2,13/2,1) |
| synchronous 2-cycle | 2 | (-47/4) | 1 | (1,47/4,141/4,47/4,1) |

The period-two states are `(3,3;6,6)` and `(6,6;3,3)`. The cycle closes exactly and is not a fixed point.

## Coupling control

For the same synchronous period-two states with \(\kappa=0\), the coefficients are
\[
1,14,51,14,1.
\]
The coupled-minus-uncoupled trace difference is \(9/4\); the \(z^2\) coefficient difference is \(-63/4\). These are finite-dimensional control statistics, not a zeta or Fredholm claim.

## Gate summary

* exact rational producer: PASS;
* independent checker: PASS;
* SymPy cross-check: PASS;
* canonical replay: PASS;
* hostile mutations: 11/11 rejected;
* A1: `A1_WEAK` (partial low-period certification only);
* A2: `A2_FAIL` (operator owner open).
