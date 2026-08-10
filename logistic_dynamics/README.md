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
├── artifacts/             # machine-readable certificates
└── results/               # formal stage result
```

A stage is promoted to a paper subproject only when it yields a theorem,
certified result, reproducible candidate, strict obstruction, or meaningful
negative result. Audit-only checkpoints retain their project directory but do
not receive a manuscript that would overstate the mathematics.

## Current stages

| Stage | Route-A tuple | Status | Paper |
|---|---|---|---|
| [`exact_uc_polar_lower_growth`](projects/exact_uc_polar_lower_growth/README.md) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; Riemann target `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` / `GO_WITH_LIMITATIONS` | Cancellation-safe derivative lower bound, explicit linear maximum-modulus lower bound, and transcendental-entire manuscript; compiled PDF |
| [`exact_uc_polar_conformal_ratio`](projects/exact_uc_polar_conformal_ratio/README.md) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; Riemann target `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` / `GO_WITH_LIMITATIONS` | Explicit conformal-ratio and numerical-growth-constant manuscript; compiled PDF |
| [`exact_uc_polar_growth_order`](projects/exact_uc_polar_growth_order/README.md) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; Riemann target `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` / `GO_WITH_LIMITATIONS` | Order-at-most-two and zero-free-half-plane manuscript; compiled PDF |
| [`exact_uc_polar_nuclear_fredholm`](projects/exact_uc_polar_nuclear_fredholm/README.md) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; Riemann target `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` / `GO_WITH_LIMITATIONS` | Complete modular LaTeX manuscript and compiled PDF |
| [`legacy_annular_residual_001`](projects/legacy_annular_residual_001/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `NOT_TESTABLE` | Not opened; no new theorem edge |
| [`polar_partition_trace`](projects/polar_partition_trace/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | Historical prerequisite | Incorporated into the LOG-0001 theorem chain |
| [`polar_boundary_trace`](projects/polar_boundary_trace/README.md) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | Historical local theorem | Incorporated into the LOG-0001 manuscript |
| [`coprime_0001_countable_trace`](projects/coprime_0001_countable_trace/README.md) | `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)` | `ANALYTIC_REVIEW` / `GO_WITH_LIMITATIONS` | Countable trace-class and exact cycle-ledger manuscript; compiled PDF |
| [`coprime_0001_scalar_boundary`](projects/coprime_0001_scalar_boundary/README.md) | `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_CONTROLLED_CONTINUATION, A4_FAIL)` | `STOP_SCOPED` | Punctured scalar continuation and endpoint zero-accumulation obstruction; compiled PDF |

The lower-growth stage proves `D_pol'(2)>0.0213` from the complete signed
trace ledger, hence `M_D(R)>0.0213*(R-2)` for `R>2`, and shows that the same
entire determinant is nonconstant and transcendental.  Its self-contained
1024-bit certificate freezes the exact 100-decimal-place rational bracket for
`U_c` and imports no legacy support module.  A separately locked bounded
order-lower audit may test whether Phragmen--Lindelof forces
`ord(D_pol)>=1`; after that narrow audit the breadth-first search should
pivot. Target-zero comparison and Route B remain closed.

## Provenance

- HP-Dynamics LOG-0001 growth-order research commit: `ec00bcb`
- HP-Dynamics LOG-0001 conformal-ratio research commit: `80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320`
- HP-Dynamics LOG-0001 conformal-ratio evaluation source: `dbb78f10bb3299415e022ecadb20d65e0aac5436`
- HP-Dynamics LOG-0001 lower-growth evaluation source: `8cabec587cf0a796f4f004bf5b1b0611de3305f3`
- HP-Dynamics LOG-0001 lower-growth research commit: `726e42a93a9fabcf07c4c543c1c5962aa0fa1569`
- Shared lower-growth stage commit: `0a64c01d3185826558d434f91ba55f1c66117d1d`
- HP-Dynamics LOG-0001 research commit: `e3358c3a90ec67c2f1cf8b883107ad0fcf3cc64a`
- Previous HP-Dynamics integration checkpoint: `223ba99`
- Legacy prime-dynamics source checkpoint: `2d01633de0bcf0ecd1310291e2547cff417e13a0` (RH-371)
- Canonical transport: SSH remote `git@github.com:maris205/hilbert-polya-structure.git`
- HP-Dynamics COPRIME-0001 countable-trace source commit: `a1d4550`
- HP-Dynamics COPRIME-0001 scalar-boundary source commit: `c7d50f9`
- HP-Dynamics scalar-boundary documentation checkpoint: `686c2bc`

This README is updated whenever a stage changes state or a new paper
subproject is opened.
