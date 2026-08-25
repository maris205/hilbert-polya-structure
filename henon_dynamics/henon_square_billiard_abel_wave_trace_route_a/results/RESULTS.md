# C157 results

## Exact trace theorem

For `Re(s)>0`,

```text
W_D(s)=s/(2*pi)*sum_(m in Z^2)(s^2+4|m|^2)^(-3/2)
       -1/4-1/(exp(pi*s)-1).
```

The principal branch is holomorphic on the right half-plane and both sides
converge absolutely and locally uniformly.  The nonaxis part is exactly

```text
2s/pi * sum_(a,b>=1,gcd=1) sum_(r>=1)
          (s^2+r^2*(2sqrt(a^2+b^2))^2)^(-3/2).
```

This is a source-derived clean-family length/repetition bridge.

## Exact shell ledger

Through squared norm 500:

- 98 primitive shells;
- 239 ordered positive primitive directions;
- 161 occupied nonaxis dual shells;
- 373 ordered positive nonaxis vectors.

Squared norm 65 is the first fourfold ordered primitive collision, with
directions `(1,8),(4,7),(7,4),(8,1)` and 16 sign lifts.

## Numerical and boundary receipts

At `s=0.9+0.4i` and `s=1.3+0.7i`, the primal/accelerated-dual differences are
`5.18e-13` and `3.92e-12`; the rigorous analytic dual truncation bounds are
`2.89e-12` and `2.19e-11`.  The 55-decimal centers are deterministic
sentinels, not interval-arithmetic values, and the checker uses a `1e-34`
serialization/rounding comparison margin.
The Abel boundary separately retains the Weyl zero mode, axis branches,
interior clean-family branches, and boundary-subtraction simple poles.

## Route-A verdict

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  The natural
self-adjoint operator is `sqrt(Delta_D)`, but no isolated stability determinant
or target trace identity is constructed.
