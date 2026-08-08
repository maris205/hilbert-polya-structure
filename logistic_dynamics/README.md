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
| [`exact_uc_polar_nuclear_fredholm`](projects/exact_uc_polar_nuclear_fredholm/README.md) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; Riemann target `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` / `GO_WITH_LIMITATIONS` | Complete modular LaTeX manuscript and compiled PDF |
| [`legacy_annular_residual_001`](projects/legacy_annular_residual_001/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `NOT_TESTABLE` | Not opened; no new theorem edge |
| [`polar_partition_trace`](projects/polar_partition_trace/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | Historical prerequisite | Incorporated into the LOG-0001 theorem chain |
| [`polar_boundary_trace`](projects/polar_boundary_trace/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | Historical local theorem | Incorporated into the LOG-0001 manuscript |

The current smallest target-free task is an intrinsic growth-order bound or
high-imaginary-height divisor-count regime for `D_pol(s)`. Target-zero
comparison and Route B remain closed.

## Provenance

- HP-Dynamics LOG-0001 research commit: `e3358c3a90ec67c2f1cf8b883107ad0fcf3cc64a`
- Previous HP-Dynamics integration checkpoint: `223ba99`
- Legacy prime-dynamics source checkpoint: `2d01633de0bcf0ecd1310291e2547cff417e13a0` (RH-371)
- Canonical transport: SSH remote `git@github.com:maris205/hilbert-polya-structure.git`

This README is updated whenever a stage changes state or a new paper
subproject is opened.
