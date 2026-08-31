# Frobenius-shear proof spike

## Verdict

The exact finite checks support the proposed closed census for

```text
T(f)=f+f^p  on  I_N=x F_p[x]/(x^N).
```

The verifier covers `p=2,3,5`, 23 values of `(p,N)`, and 145,716 explicit
assertions.  It checks bijectivity, the full orbit period of every state, all
fixed counts through twice the predicted order, and agreement between the
orbit census and the fixed-stratum differences.

## Proof route isolated by the computation

Write `F(f)=f^p`, so `T=1+F`.  For `t=p^r m`, `p` not dividing `m`, the
freshman's dream gives

```text
(1+F)^t-1 = F^(p^r) U(F),   U(0)=m.
```

Nilpotence of `F` makes `U(F)` invertible.  Hence the fixed space is precisely
`ker(F^(p^r))`.  A coefficient survives `F^s` exactly when its exponent `i`
satisfies `i p^s<N`, which proves

```text
|Fix(T^t)| = p^((N-1)-floor((N-1)/p^(p^r))).
```

Möbius subtraction along the chain `1,p,p^2,...` gives exact-period points;
division by the period gives cycles.  The least `p^R` with `p^(p^R)>=N` is the
order of `T`.

For `F_q`, `q=p^a`, coefficient Frobenius is still a bijection, so the same
kernel argument replaces the outer base `p` by `q`.  This extension is a
deduction from the proof, not part of the finite enumeration.

## Boundary

This calculation does not establish novelty.  General finite-linear-system
and additive-polynomial dynamics remain zero-credit owner theory.  The result
stays a conditional batch finalist and `HOLD_EXTERNAL` until the owner and
value gates are complete.
