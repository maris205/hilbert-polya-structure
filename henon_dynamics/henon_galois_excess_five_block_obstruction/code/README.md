# Code

`c57_five_block_obstruction.py` builds the primary exact certificate.  It
derives the reflection-reduced period-six and period-seven closing
polynomials, trace resultants, root isolators, Galois excesses, the exact
integer separation and both width-six minors.

`independent_check.py` reconstructs the same objects without importing the
primary module.  `test_c57.py` locks the public schema and claim boundary.

Run the complete finite audit with:

```bash
bash code/run_c57.sh
```

The scripts use exact SymPy arithmetic for identities and Sturm counts.
High-precision roots are diagnostics only; the obstruction sign is certified
by an integer product comparison.
