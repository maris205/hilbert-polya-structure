# Deterministic evidence plan

The finite computation is a regression audit of the analytic theorem, never a
replacement for it.

## Frozen inputs

- Candidate: `HCS-C274`
- Source commit: `418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02`
- Evaluation date: `2026-09-01`
- Fixed epoch: `1788220800`
- Evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`

## Producer grid

Generate 48 high-precision canonical `6 x 6` matrices spanning stable,
critical, unstable, zero-field, zero-axial, free, and both field-sign cases.
For each row record determinant, symplectic defect, energy defect, and an
independent-time semigroup defect.  Separately generate 24 stable-mode rows,
13 strobe rows, 7 active-mode minimal-period rows, and 9 boundary rows.

The receipt must contain 2,743 numeric cells when recounted from an explicit
field schema.  The payload hash excludes only its own hash field.

## Independent validation

The checker must not import the producer.  It independently reconstructs the
Hamilton matrix and flow, checks all receipt identities at 90-digit precision,
recounts every row and numeric cell, and validates the frozen regime, period,
strobe, Route-A, source, and nonclaim contracts.

The symbolic checker independently derives the Hamilton equations, the
rotating-frame reduction, the generator's Hamiltonian identity, characteristic
polynomial, signed action cancellation, critical/free limits, and field-sign
conjugacy.

## Replay and hostile audit

1. Replay the producer into a fresh temporary directory and demand exact byte
   equality with the committed receipt.
2. Apply single-fault mutations to metadata, matrices, mode actions, periods,
   strobe dimensions, boundary classifications, Route-A fields, and scope
   flags.
3. Repair each mutated receipt's internal payload hash.
4. Require the independent checker to reject every repaired-hash mutation.

## Paper/build gate

Compile three substantively different revision rounds.  For every round,
perform two independent fresh LuaLaTeX builds with two passes per build under
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Require
byte-identical paired outputs, warning-free settled logs, embedded subset fonts,
three distinct round hashes, and `main.pdf == main_round2.pdf`.

## Release gate

The self-excluded release manifest must close exactly 27 payload files and 28
physical files, rerun the full code chain, verify frozen textual claims in the
PDF, and reproduce the final PDF twice from fresh directories.
