# Control results

Command:

```bash
python3 code/verify_weighted_heisenberg.py
```

The script first checks four direct clock--shift blocks over prime fields
containing the required roots of unity.  Two lie on the Fermat locus and two
lie off it; their determinants and nullities agree with the exact block
lemmas.  It then checks ten full quotient convolution matrices.  The full
matrices include `ell=3,5`, characteristics `2,3,5,7,11`, unit and nonunit
weights, and both Fermat-singular and Fermat-nonsingular cases.  Every
observed nullity equals the theorem formula, ending with:

```text
clock-shift determinant and exact nullity: PASS (four direct blocks)
ALL WEIGHTED HEISENBERG CONTROLS PASS
```

The frozen receipt is `code/verification_output.txt`.  These checks are
regression evidence only.

For the official GPT-5.4/xhigh Round-2 freeze, fresh script stdout was compared
line-for-line with that receipt using `diff -u` and matched exactly.
