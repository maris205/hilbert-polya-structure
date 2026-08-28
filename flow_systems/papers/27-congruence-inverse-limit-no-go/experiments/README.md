# P27 experiment status

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
