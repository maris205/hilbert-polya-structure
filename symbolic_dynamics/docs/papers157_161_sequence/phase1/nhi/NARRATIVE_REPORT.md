# Narrative report — Newton–Hensel finite atlas

## One-sentence result

For the owned idempotent-lifting polynomial `F(x)=3x^2-2x^3` modulo `2^n`,
the residual finite dynamics admits an exact parity-resolved clock and a
complete, nonuniform every-target inverse atlas controlled by normalized odd
units modulo `8`.

## Contribution after subtraction

The map and its quadratic error improvement are not contributions: Burban and
Drozd use the same polynomial to lift approximate idempotents.  The temporal
valuation doubling is correspondingly cheap.  What remains paper-scale is the
finite inverse problem.  After writing an even source as `x=2^v u`, the output
is `2^(2v) h_v(u)` with

```text
h_v(u)=u^2(3-2^(v+1)u).
```

The image unit is `7 mod 8` at the first valuation stratum and `3 mod 8`
later.  A two-branch bit-lifting argument proves four reduced preimages for
every admissible unit when the quotient modulus is at least eight, with
separate one- and two-bit boundary laws.  Restoring discarded high bits gives
the nonuniform target fibre formula and closed image size.

## Two theorem axes

- Forward time forgets the unit and doubles only the selected endpoint-error
  valuation, yielding every pointwise time and every shell.
- Backward time must retain the normalized unit, distinguish `v=1` from
  `v>=2`, and count a genuinely nonconstant fibre spectrum.

Neither axis is a cosmetic restatement of the other.  The manuscript should
lead with the owner and present the temporal theorem as context for the inverse
atlas, not as invention of a Newton map.

## Evidence state

The proof package is closed, including quotient sizes one and two.  The exact
control checks every state and every target through modulus `2^17`, plus six
valuation strata and quotient moduli through eleven bits: 2,563,880
assertions.  The canonical transcript SHA-256 is
`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

## Remaining risks

- numerical-analysis or ring-theoretic terminology may conceal a direct
  inverse-atlas owner;
- the exact cubic Taylor identity must not be described asymptotically;
- the `N=1,2` branches must remain printed;
- no odd-prime or general-ring extension may be implied.
