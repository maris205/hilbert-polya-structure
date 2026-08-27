# C198 results

The all-parameter proof reduces every positive-rate closed SIR system to
`x'=-xy`, `y'=y(x-1)` and closes its complete phase portrait.  The executable
ledger contains 24 positive-infection cases across nine subcritical, three
threshold and twelve supercritical starts, both real final-size intersections,
and four physical parameter scalings.

The producer evaluates 48 Lambert branch values at high precision.  The
independent checker uses no Lambert implementation: Decimal logarithms and
monotone bisection recover both roots.  SymPy separately proves seven structural
identities and tests every branch equation.  Replay is byte exact; twelve
repaired-hash semantic attacks and one stale-hash attack are rejected.

The result is mathematical and data-free, not medical advice.  Strict Route A:

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```
