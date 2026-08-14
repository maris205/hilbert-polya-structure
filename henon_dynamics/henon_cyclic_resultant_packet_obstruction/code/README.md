# Code

`c49_cyclic_packets.py` builds the exact signed H6 cyclic-resultant ledger,
checks the cyclotomic divisor product, and verifies the square-norm theorem
through index 12 for primitive periods 1, 3, and 4.

`test_c49.py` supplies adversarial controls for the period-three sign, the
sharp `n>2` range, the reciprocal-unit hypothesis, the false one-scalar
power law, and the scalar/ideal claim boundary.

`generate_table.py` reads the JSON certificate and generates the LaTeX table
used in the paper.  Run everything with:

```bash
bash code/run_c49.sh
```
