# Results

## Source-unitary structure

For both frozen arrangements:

- `U_w=S C_w` is a real 10-by-10 orthogonal matrix;
- `det(U_w)=1`;
- `Theta_w=C_w K` is involutive and reverses `U_w`;
- `P_w=|U_w|^2` is doubly stochastic with the same one-step clock;
- the signed primitive product is absolutely convergent for `|z|<5/7`.

## Arrangement result

The words `00011` and `00101` share population `(3,2)` but are not
dihedrally equivalent.  Their degree-ten determinants differ by

```text
(196/4225)z^2(z-1)^2(z+1)^2(z^2+1).
```

The population-average coin has orthogonality defect
`-(24/1625)I`, so averaging is not a unitary replacement.

## Validation

- independent checker: 62 assertions;
- SymPy: 39 exact checks;
- traces: 12 per arrangement;
- path ledger: clocks 1--10 per arrangement;
- mutations: 30/30 rejected;
- canonical replay: pass.

Strict verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`;
Route B false.
