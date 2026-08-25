# C156 results

## All-iterate structure

- Odd `n`: `G_n=(Z/L_n Z)^2`, exponent `h_n=L_n`.
- Even `n`: `G_n=Z/F_n Z x Z/(5F_n)Z`, exponent `h_n=5F_n`.
- Every central rotation satisfies `h_n rho_n=0` in `Q/Z`.
- Distinct group-theoretic primary components are orthogonal, and the global
  zero count is the product of their exact zero counts.

## Exact cutoff ledger

There are 23 primary components through `n=14`, containing 314,151 enumerated
elements and 906 distinct rotation cells.  The all-cross-component audit checks
191,597 orthogonality pairs.  The fixed-circle counts are

```text
n   : 1  2  3  4  5   6  7   8  9    10  11   12   13    14
C_n : 1  1  4  1  21  4  57  1  148  105 397  144  1041  57
```

At `n=12`, the primary zero counts are `16*9*1=144`; at `n=14`, they are
`1*1*57=57`.  The observed denominator lcm equals `h_n` for every
`2<=n<=14`, but this finite sharpness is not asserted for all iterates.

## Route-A verdict

`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  Clean fixed circles and a
singular isolated-stability denominator remain.  The primary projectors are
finite zero filters, not arithmetic local factors or operator trace formulas.
