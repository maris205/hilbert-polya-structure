# P26 Round-2 reproduction

From the P26 directory, run:

```bash
./experiments/reproduce.sh
```

The script fixes locale, timezone, Python hash seed, and bytecode behavior;
runs all 7 unit tests; generates two isolated result trees; requires a recursive
byte-for-byte diff and identical stdout; copies the first tree to `results/`;
and writes `reproducibility_receipt.json`.

The canonical run completed in approximately 18.7 seconds in the recorded
environment.  Both result-tree hashes are:

```text
e635ee051ea25d543eb4f3fd72bce5ae4da95d64ee2ca9f90b2f5f81ba8a2da5
```

The experiment numerically recomputes q-cutoff, quadrature, basepoint shift,
orientation reversal, and direct `M^2` repetition checks.  The repetition
branch has its own 2048-versus-4096 q-cutoff and 256-versus-512 quadrature
comparisons.  The reported residuals are binary64 observations, not rigorous
error bounds.

The registered negative controls are a deterministic bounded PSL2Z-invariant
`j`-based observable matched by finite-ledger RMS, a cyclic shift of periods,
and the full 125-row simpler-parent length ledger.  They do not make the
Hecke/Euler hypothesis testable without an exact source-derived recurrence.
