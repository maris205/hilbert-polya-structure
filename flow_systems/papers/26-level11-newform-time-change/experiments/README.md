# P26 reproduction

## Round 4

Run:

```bash
./experiments/reproduce_round4.sh
```

It runs 8 unit tests, generates two isolated six-file artifact trees, requires
a recursive byte-for-byte match and identical generator stdout, installs the
canonical Round-4 artifacts, and writes
`round4_reproducibility_receipt.json`. The canonical tree SHA-256 is:

```text
4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e
```

The exact surfaces contain 385 branch gluings, 320 eta-product coefficient
relations, and 138 closed-cycle owner/primitivity certificates. The numerical
surface contains 55 direct complex period-sum rows at q cutoffs 1536/1024 and
Simpson panels 256/128. Numerical residuals remain observations rather than
rigorous error bounds. The receipt preserves the Stage-1/A0--A1 boundary,
formal-tuple `UNASSIGNED` state, A2 `NOT_RUN`, and Route-B prohibition.

## Round 3

Run:

```bash
./experiments/reproduce_round3.sh
```

It runs 5 unit tests, generates two isolated artifact trees, requires a
recursive byte-for-byte match, installs the four canonical Round-3 artifacts,
and writes `round3_reproducibility_receipt.json`.  The canonical tree SHA-256
is:

```text
a3e71f86124ec8ae58f3971002fd3e0f11a0f06ccf3851e1f4ed4fad25d03841
```

## Round 2

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
