# MCT final author replay receipt

Date: 2026-09-05 UTC; both fresh processes completed before 07:26 UTC.
Status: **AUTHOR_FINITE_CHECKS_PASS / NO_INDEPENDENT_REVIEW / HOLD_EXTERNAL**.

## Frozen code and command

Run from `/root/autodl-tmp/symbolic_dynamics`:

```sh
python -B docs/papers197_201_sequence/scouting/monochromatic_triangle_20260905/probe.py
```

Code SHA-256:
`1e40d08722268ab476a8687d1f0204a5dd3f5b2dc6c7046eb0d887c63d36b937`.
The code was unchanged between the following two fresh operating-system
processes. Exploratory earlier runs with fewer assertions are not counted
as these final replays.

## Replay 1

Fresh process started in tool receipt `d7fd89`, session 34606; final stdout
and exit code 0 arrived in receipt `a4de00`. It enumerated n=0,…,6 complete
carriers and printed `TOTAL_ASSERTIONS=374812`, followed by
`PASS_BOUNDED_ONLY / NO_ALL_N_SHARP_CLAIM`.

## Replay 2

Different fresh process started in receipt `b43a5d`, session 29270; final
stdout and exit code 0 arrived in receipt `b66578`. It printed the same
374,812 assertions and finite-check PASS footer. It was not a copied run
or a read of the first process's saved transcript.

## Byte comparison and canonical transcript

The orchestration layer retained both actual complete stdout strings and
compared them directly: `run1.output === run2.output` returned true.
They are **byte-identical** ASCII output. `CANONICAL.txt` preserves that
stdout, including its final newline, with SHA-256
`ed9ad60c5dc168b930f3512a8fe101ed9dba90b45c281bc9ff43638a92c24f18`.

## Scope and independent representations inside the author code

The complete boxes contain 33,868 labelled graphs. Pair-bit masks encode
the carrier; a dense symmetric adjacency-matrix control independently
checks the literal selector. Direct visited-state orbit paths determine
entrance times and periods. Actual predecessor sets are compared both
with a reversed-triangle/earlier-selector parser and with the target-only
D/C local-colour conditions. Zero fibres and fixed self-fibres are included.
The code also checks the local recurrent iff, Johnson pair intersections,
target-only star/four-face equality certificates, all finite maximizers,
the no-return/anchor trace structure, and the explicit sharp witnesses
through n=6. No complete box above n=6 is run.

The total assertion count is verification workload, not a count of proved
theorems or distinct systems. The all-n proof rests on the separately pinned
mathematical documents, not this finite transcript. Two runs demonstrate
determinism/reproducibility; neither is an independent researcher review.
