# Control results

Final hostile-audit execution (2026-08-28 UTC):

```bash
python3 code/verify_catalan_renewal.py
```

Result:

```text
PASS: 1,369 exact assertions
boundary fixed counts c=1: [1, 3, 10, 35, 126, 462, 1716, 6435]
boundary fixed counts c=2: [2, 8, 32, 128, 512, 2048, 8192, 32768]
classification: c=1 transient; c=2 null recurrent; c>=3 positive recurrent
```

The script checks the formal renewal coefficients and both boundary laws
through order 40, together with exact rational root and mean-return formulas
for `3<=c<=50`.
