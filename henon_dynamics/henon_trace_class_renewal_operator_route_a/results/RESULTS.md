# Results

## Analytic result

For the frozen renewal operator,

```text
||S||_1=1,
||R||_1=1/sqrt(3),
det_F(I-zT)=1-sum_{m>=1}2^{-m(m+1)/2}z^m.
```

The determinant is entire of order zero and has an absolutely convergent
primitive excursion-necklace product on
`|z|<(1+1/sqrt(3))^(-1)`.

## Exact replay

- determinant coefficients: 16;
- trace moments: 12;
- finite section: size 14;
- primitive classes through clock 10: 225;
- independent checker: 110 assertions;
- separate SymPy reconstruction: 56 checks;
- byte replay: pass;
- hostile mutations: 25/25 rejected.

## Negative control

With constant advance weight `1/2`, the formal first-return expression is
`(1-3z/4)/(1-z/4)`, but the natural shift is noncompact.  The control has no
ordinary trace-class Fredholm determinant.

## Verdict

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`, Route B false.
