# Logistic Dynamics

This directory is the continuously updated entry point for the Logistic-map
branch of the Hilbert–Pólya structure project.

## Research boundary

The program searches for intrinsic dynamical determinants, global analytic
structure, and natural operator lifts. Numerical zero matching is treated as
diagnostic evidence only. Prime tables and Riemann-zero tables may not enter a
candidate definition, and signed or complex cancellation may not be replaced
by unrelated absolute-value estimates.

## Project layout

Each stage lives in its own self-contained directory:

```text
projects/<stage_slug>/
├── README.md
├── source_lock.yaml
├── route_a_evaluation.yaml
├── paper/                 # created only after a genuine result edge
├── src/                   # stage-specific implementation, when needed
├── tests/                 # exact reproduction and regression tests
└── results/               # machine-readable artifacts
```

A stage is promoted to a paper subproject only when it yields a theorem,
certified result, reproducible candidate, strict obstruction, or meaningful
negative result. Audit-only checkpoints retain their project directory but do
not receive a manuscript that would overstate the mathematics.

## Current stages

| Stage | Route-A tuple | Status | Paper |
|---|---|---|---|
| [`legacy_annular_residual_001`](projects/legacy_annular_residual_001/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `NOT_TESTABLE` | Not opened; no new theorem edge |
| [`polar_partition_trace`](projects/polar_partition_trace/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `REVISE` / `NOT_TESTABLE` for analytic trace | Reserved; local endpoint trace theorem still open |

## Provenance

- HP-Dynamics source checkpoint: `1f236c404e3a549dc639cf4d616cc8dfae846c67`
- HP-Dynamics integration commit: `223ba99`
- Legacy prime-dynamics source checkpoint: `2d01633de0bcf0ecd1310291e2547cff417e13a0` (RH-371)
- Canonical transport: SSH remote `git@github.com:maris205/hilbert-polya-structure.git`

This README is updated whenever a stage changes state or a new paper
subproject is opened.
