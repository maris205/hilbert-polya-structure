# P24 experiment status — Rounds 2–6

The exact word-ball enumeration and target-free holonomy shuffle completed.
The core output is reproduced byte for byte under the hash recorded in
`round2_receipt.json`; exact checks and claim boundaries are in
`round2_validation.md`.

Executed control:

- keep every sampled complex-length real part and observed repetition field;
- permute holonomy angles by a fixed SHA-256 ordering derived only from row IDs;
- record orientation reversal separately;
- never inspect prime ideals, rational primes, or Riemann zeros.

Observed phase/length score:

```text
original = 0.003173818350680037
shuffle  = 0.02247064819754699
```

This is `[NUMERICAL_OBSERVATION]`; it does not favor the observed angles over
the shuffle and does not create an arithmetic owner.  At the Round-2
checkpoint, both the independent Kleinian ledger and scalar/chiral trace
comparison were `[OPEN]`.  Round 3 below closes the former construction only;
the scalar/chiral comparison and arithmetic verdict remain `[OPEN]`.
Arithmetic label controls remain prohibited until a canonical orbit owner
exists.

## Round 3

The classical-Schottky control construction is now complete.  Exact
Gaussian-rational checks plus the classical ping-pong theorem prove the
rank-4 free, discrete, convex-cocompact control group.  The deterministic
ledger and intrinsic shuffle were reproduced under the combined SHA-256 in
`round3_receipt.json`; commands and claim boundaries are recorded in
`round3_validation.md`.

The phrase “matched control” is restricted to rank 4, oriented alphabet 8, and
word cutoff 5.  This is an infinite-volume non-lattice, not a finite-volume
matched manifold.  The construction is `[PROVED]`, the numerical ledger is
`[NUMERICALLY_CERTIFIED]`, and the intrinsic phase/length scores are
`[NUMERICAL_OBSERVATION]`.  The cross-system arithmetic verdict remains
`[OPEN]`; formal Route-A tuple is `UNASSIGNED`, A2--A4 are `NOT_EVALUATED`, and
Route B is not run or invocable.

## Round 4

The finite-volume non-arithmetic control is complete at the Stage-1 research
level.  `reproduce_round4.sh` runs 9 unit tests, generates two independent
temporary artifact trees, requires byte identity, and verifies the checked-in
tree.  The core artifact hash is
`54dc289c26ef8466405576c29d819d2ccc0464d57c78386e1a021464d78f6875`.

The source theorem chain and local computation have deliberately separate
statuses.  The former proves that `5_2=m015` is finite-volume, one-cusped and
non-arithmetic.  The latter supplies 18 numerical complex-length groups / 31
primitive classes and a 9-class independent prefix crosscheck.  It is not
interval verified because SageMath is unavailable.  The same-enumeration
Bianchi/control comparison remains `[OPEN]`; no score, tuple, A2+ layer, or
Route-B evaluation is produced.

## Round 5

The same-enumeration comparison has now been executed at the **marked-word
algorithm** level.  The input contract and phase statistic were frozen before
result execution under SHA-256
`210cff78b8af54847baae1c7ef21572dd697d70004f50723f6b1bac4e19a85b7`.
`reproduce_round5.sh` runs 10 tests, builds two independent temporary output
trees, requires byte identity, and verifies the checked-in artifacts.

The core-output SHA-256 is
`b1d323ba04b6f0a0ead32516bc11f6bdf8610847d070ffe54c1b4b7ca0778892`.
The Round-5 receipt schema 1.1 also binds the generator, ten-test suite, and
reproduction script by SHA-256, so the archived result identifies its exact
implementation version as well as its freeze contract and core artifacts.
The two censuses contain 2,074 and 51 marked owners; the phase statistic uses
1,932 and 39 primitive loxodromic rows.  Its absolute permutation-standardized
contrast is `0.935490232934`.

This closes the Round-4 word-ball-versus-metric-cutoff type mismatch, but not
the scientific kill gate: the alphabets have sizes 8 and 4 and the underlying
presentations differ.  The comparison is descriptive and marking-dependent.
Prime/zero target data remain prohibited; Route tuple, A2+, and Route B remain
unassigned/not run.

## Round 6

`reproduce_round6.sh` runs 11 tests, builds two independent artifact trees,
requires byte identity, and verifies the checked-in tree.  Core SHA-256 is
`f5d31071c7174d84322c352b9028e334bf30e89a2368a751fbe58f6ab83ed660`.
The decision is `STOP_SCOPED_CURRENT_PHASE_STATISTIC_AS_MARKING_SENSITIVE`.
Only the marked-word proxy receives a formal tuple; the full flow is still
unassigned and Route B remains closed.
