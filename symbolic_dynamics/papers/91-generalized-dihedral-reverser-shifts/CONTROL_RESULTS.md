# Control results — P91

Final registered exact execution (2026-08-28 UTC):

```bash
python3 code/verify_reverser_shift.py
```

Output:

```text
PASS: 12,175 exact assertions
20 finite-abelian presentations: conjugation rule, invariant decomposition, canonical collapse, rank, and mixing verified
period traces k<=10 and all small characteristic/zeta polynomials verified
same-parameter collapses include Z/9 vs (Z/3)^2 and Z/2 x Z/8 vs Z/4 x Z/4
```

The direct group implementation and the closed canonical graph are separate
code paths. Integer traces, rational row reduction, and symbolic polynomial
checks provide three further cross-checks.

Coverage added during the hostile audit:

- basis-level checks of the internal zero spaces, the `(c-1)`-dimensional
  `t`-eigenspace, and the three-class quotient action;
- the extra presentation `Z/2 x Z/8`, giving a second nonisomorphic
  same-parameter collapse against `Z/4 x Z/4` at `(N,t)=(16,4)`;
- explicit endpoint coverage for the trivial group and elementary
  two-groups, including the all-ones rank, traces, and zeta determinant.

All comparisons are exact. SymPy is used only for exact characteristic and
determinant-polynomial identities on the stated small matrices; no numerical
eigenvalue tolerance or random sampling occurs. The original package
reported 10,682 assertions; the final total is 12,175.
