# Code

`c50_tagged_packets.py` reconstructs the inversion-fixed half-cyclotomic
elements for the signed primitive H6 periods 1, 3, and 4.  For indices
`3..20` it factors their principal ideals in the exact trace fields
`Q(sqrt(7))`, `Q(sqrt(5))`, and `Q`.

Each atom records:

- orbit and signed branch;
- cyclotomic index;
- trace-field prime ideal;
- rational prime;
- ramification index and residue degree;
- ideal valuation;
- whether the multiplier-field residue order is certified to equal the
  cyclotomic index.

The implementation uses exact integer arithmetic, quadratic integral bases,
Hensel lifting for split-prime valuations, and finite-field polynomial
remainders for the order checks.  It reads no prime table or Riemann-zero
table.  Rational factorization is performed only on source-generated exact
norms.

Run the complete certificate with:

```bash
bash code/run_c50.sh
```

The script uses `python -B`, so it does not create `__pycache__` artifacts.
