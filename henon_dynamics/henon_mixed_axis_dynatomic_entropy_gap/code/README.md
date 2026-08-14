# Code

`c60_dynatomic_gap.py` constructs the odd mixed-axis closure sequence,
divides out every lower formal period, factors the primitive quotients through
period 15, checks squarefreeness and locks the P58 period-nine polynomial.

`independent_check.py` imports no primary research code. It rebuilds the
recurrence, exact quotient chain, coefficient hashes and degree sequence.

Run all checks with:

```bash
bash code/run_c60.sh
```

The period-15 exact factorization is the slow step and may take several
minutes. No floating-point root decision enters the certificate.
