# Exact control results — P107

Canonical command:

```bash
python3 code/verify_annihilator_power.py
```

The script uses only Python's standard library.  It compares two routes:

1. direct prime-exponent iteration with the deviation/depth/CDF formulas;
2. literal divisor ideals `(d)` in `Z/NZ`, updated by
   `gcd(N,(N/d)^r)`, followed by an independent CRT conversion.

The exact assertion count and byte-identical stdout are frozen in
`code/verification_output.txt` after the final run.  Finite enumeration is a
falsification control and does not replace the paper's quantified proof.
