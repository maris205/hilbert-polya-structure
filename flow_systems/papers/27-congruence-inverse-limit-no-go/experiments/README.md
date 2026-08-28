# P27 experiment status

## Round 8

Run `bash experiments/reproduce_round8.sh`.  Twelve tests and two isolated
builds must pass byte-for-byte before the checked-in outputs are verified.  The
replay contains 96 quadrant rows and 1,248 exact coefficient rows; core
SHA-256 is
`a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`.
The new-owner, nonresidual-tower, finite-panel, Route, and target-data
boundaries are all machine-checked.

## Round 7

Run `bash experiments/reproduce_round7.sh`.  Twelve tests and two isolated
builds must pass byte-for-byte before the checked-in outputs are verified.
The replay contains 48 locked owner/level rows and 54 fixed-prefix diagnostics;
core SHA-256 is
`551e92315c46dcbb4d01bd84688bb77eca8fcd4a6c2eaec202fe04f621275845`.
The default is read-only verification and `--refresh` is explicit.  Finite
rows certify coefficient support only; the all-level theorem is proved in the
Round-7 note.

## Round 6

Run `bash experiments/reproduce_round6.sh`.  It runs eleven tests, makes two
isolated three-file builds, requires byte identity, installs the claim/source
matrix, summary, and manifest, and writes
`round6_reproducibility_receipt.json`.  The artifact-tree SHA-256 is
`53b8b332c09f771f97ad45a1504491a7e542d014a9d6ce677d3dc86851efeb5a`.

The matrix contains 13 rows, including nine external rows across five
authoritative records (four research articles and one theorem exposition).
All nine are web-verified with exact URLs, locators, and access date
`2026-08-28`; all retain
`HUMAN_CONFIRMATION_PENDING`, and none is `USER_ATTESTED_READ`.  The replay
also freezes short owner-audit `GO`, standalone novelty `NO_GO`, and
same-owner A2 `NO_GO`.

## Round 5

Run `bash experiments/reproduce_round5.sh`.  It checks the three frozen
primitive-homology owners at all eight factorial levels, the exact modular
homology order formula, forward divisibility, owner/Route firewalls, and two
byte-identical builds.  Ten tests pass and the combined artifact SHA-256 is
`f8b04a5bbc323bf2161cfe675b40c9b9dc16f2c67a12082dad29794396ade4ea`.

The generated 24 rows certify homology lower bounds through `8!=40320`.  They
do not enumerate the canonical residual cores or compute the full quotient
orders; the cocompact residual-tower and minimal-period conclusions are proved
in the accompanying theorem note.

## Round 4

Run `bash experiments/reproduce_round4.sh`.  It checks the 24-row frozen input,
all 21 order-divisibility transitions, the exact three order sequences, period
ratios, owner firewalls, and two byte-identical builds.  Eight tests pass and
the combined output SHA-256 is
`2fcf33ed6c458339ac808d7b7007a240b7a588b0093249a90a35559f1ef2aa22`.

The finite rows illustrate the proved group-theoretic closing-time escape
theorem for whole traversals of a selected `g`-loop; they are not used to infer
asymptotic divergence, primitive minimal periods, or inverse-limit periodic-
orbit credit.

## Round 2

Round-2 finite-level diagnostics are complete.  Run:

```bash
bash experiments/reproduce.sh
```

The entry point performs two complete generations, verifies each manifest,
runs five unit tests, and demands byte identity for the CSV, metrics JSON,
experiment receipt, and manifest.  Current receipt:

```text
ROWS=24
ELEMENTS=3
LEVELS=8/8
ORDER_CROSSCHECKS=24/24
UNIT_TESTS=5/5
TWO_RUN_BYTE_IDENTITY=4/4
STATUS=PASS
```

See `round2_reproducibility_receipt.md` for hashes and the owner boundary.  The
cocompact-tower structural control is now closed by Round 5; the
trivial-product control remains `[OPEN]` and is not needed for the landed
cocompact theorem.
