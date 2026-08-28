# Compile report

Build epoch: `SOURCE_DATE_EPOCH=1787875200`; engine: LuaHBTeX 1.14.0; paper
size: A4.  Each revision was compiled with LuaLaTeX in two settled passes;
round 2 was rebuilt twice from a clean sidecar state.  Final logs contain no
overfull/underfull boxes, undefined references, missing citations, or missing
characters.  As usual for a hand-written bibliography, the disposable first
pass reports citation bootstrap warnings; the second settled pass is clean.
Auxiliary sidecars are removed before manifest closure.  The settled checker
reports 509 assertions and the hostile suite rejects 15/15 mutations,
including a repaired unknown nested key.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `ae94633ed900d09260958c795c7c22b8da53bea376717e90ea5c6ff75cecaeec` |
| `main_round1.pdf` | 3 | `ce252f5f404dc2d724e070acfba9bdc0fdb0ff2e0a9f872d4d3c7c11a3361bdc` |
| `main_round2.pdf` | 3 | `bc6958a50b1cf9ce466c1ae0b0b08240306dd677afc552660356964993a7b5c0` |
| `main.pdf` | 3 | `bc6958a50b1cf9ce466c1ae0b0b08240306dd677afc552660356964993a7b5c0` |

The round PDFs are distinct and `main.pdf` is byte-identical to round 2.
`pdfinfo` reports three pages for the final manuscript, `pdffonts` reports
all fonts embedded and subset, and extracted text contains the Rayleigh, Beta,
`2/5`, Lagrangian, scope, `A3_FAIL`, and `ROUTE_A_REJECTED` locks.  The paper
also states explicitly that the source Beta clock is not target
continuation/divisor/counting law.  The revision history is recorded in
`PAPER_IMPROVEMENT_LOG.md`.
