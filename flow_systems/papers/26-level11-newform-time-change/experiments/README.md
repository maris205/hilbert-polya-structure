# P26 reproduction

## Round 7

Verify the checked-in artifacts without modifying them:

```bash
./experiments/reproduce_round7.sh
```

Refresh them explicitly with:

```bash
./experiments/reproduce_round7.sh --refresh
```

The script runs 13 tests, generates two isolated four-file exact-homology
trees from the SHA-locked Round-4 cycle and Round-6 moment ledgers, requires
byte identity and matching stdout, and either compares with or refreshes the
canonical outputs and receipt.  The tree SHA-256 is:

```text
bdfa8f5baaeef47f1bfd8482e8b459d2bd0606cdbb9cdcf0c441a8f65829d678
```

The receipt binds the freeze, builder, tests, reproducer, locked inputs, and
all four outputs.  Exact homology is the proof layer; inherited quadrature
values remain cross-checks only.

## Round 6

Run:

```bash
./experiments/reproduce_round6.sh
```

It runs 12 unit tests, generates two isolated five-file Round-6 artifact
trees from the SHA-locked Round-4 ledgers, requires byte identity and matching
generator output, installs the canonical results, and writes
`round6_reproducibility_receipt.json`.  The canonical tree SHA-256 is:

```text
fc553aa18bc4fb54d70ea8f4c0bdbc41efc3c0905b3f2942c49e1f6f8c62f864
```

The registered surfaces contain 552 inverse-pair/repetition rows, 110
quadratic degree-moment rows, and 165 finite Hecke second-variation rows.
The receipt binds the formal tuple
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`, A2 `FAIL/NOT_TESTABLE`, and the Route-B prohibition.
It is explicitly a finite/local log-product audit, not a global determinant
or root-counting campaign.

## Round 5

Run:

```bash
./experiments/reproduce_round5.sh
```

It runs 11 unit tests, generates two isolated five-file Round-5 artifact
trees from the exact Round-4 source ledgers, requires a recursive
byte-for-byte match and identical generator stdout, installs the canonical
artifacts, and writes `round5_reproducibility_receipt.json`.  The canonical
tree SHA-256 is:

```text
7b21a0c25ee269d28b53cd8c0551c8b2a977307641c2d07be78810be2e975731
```

The registered surfaces contain 1,104 orientation/repetition rows, 110
degree-moment rows, and 165 one-sided Hecke-zeta variation rows.  The receipt
binds the two Round-4 input files and preserves Stage 1 / A0--A1, formal tuple
`UNASSIGNED`, A2 `NOT_RUN`, and Route-B prohibition.  Exact orientation
cancellation and the analytic degree-moment theorem are kept separate from
binary64 weighted residuals.

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
relations, and 138 closed-cycle owner-instance/primitivity certificates. The numerical
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
