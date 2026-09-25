# Finite-test candidate card — ANG-20260918-GNS02

**Version:** 1, 2026-09-18; frozen before the extension run.  
**Status at freeze:** FINITE TEST AUTHORIZED — T=8 PREFIX EXTENSION ONLY.

## Purpose and lineage

This is a separately versioned evidence contract for the exact finite
period-eight prefix test of [139 — gated-neighbor sieve](../139-gated-neighbor-sieve/README.md).
It does not change the map, carrier, roof, source, or orbit convention of
`ANG-20260914-GNS01`; changing any of those would require a new mathematical
candidate rather than this test version.  The lineage remains divisor
prime/composite exclusion -> reversible two-register memory -> state-gated
neighbor feedback.

## Frozen finite object and test contract

| Field | Frozen content |
| --- | --- |
| Same-object map | The full binary action `R(x,y)=(y,x+G(y)+L(y))` from 139, with reflected ghost `y_1=y_2` and exact integer divisibility. |
| Carrier / roof | Full `X^2`, unit roof and endpoint-glued suspension, exactly as 139. |
| Temporal period | `T=8` only; cyclic words are encoded as 8-bit unsigned integers. |
| Spatial range | Coordinates `n=2,...,16`; higher boundary variables remain existentially free. |
| Prefix equation | The exact bit equation and forced/free extension rule recorded in 139 evidence. |
| New finite cap | `CAP=2_000_000` stored extensions at each equation stage; stop before storing extension `CAP+1`. The old 139 cap `100_000` is immutable. |
| Backends | A chunked NumPy CPU implementation and a chunked PyTorch CUDA implementation; integer/Boolean operations only, no tolerances. |
| Chunk / memory guard | `CHUNK=8192` input prefixes; a GPU chunk is refused if reported free memory is below 1 GiB. |
| Outputs | Per-equation input, admissible, extension, maximum-free-bit, cap and boundary flags, plus backend agreement. |
| Interpretation | A zero survivor level is a finite contradiction for a full period-8 state. Any nonzero or capped level is only a finite OPEN result, never an existence proof. |

No prime table, prime mask, logarithm, zero data, fitted parameter, stochastic
pruning, or finite upper-boundary convention is permitted.  The test is not a
Route evaluation and cannot upgrade the T1/T2 status of 139 by itself.

## Stop and safety rules

Stop on the first cap hit, on a zero admissible level, on a backend mismatch,
or on a memory guard refusal.  Do not continue to periods 12 or higher, do not
alter the Boolean rule, and do not reinterpret surviving prefixes as full
periodic points.  Record the exact command, software versions, hardware and
all completed counts in the evidence file before handoff.

## Audit append — version 1, 2026-09-18

**Current status:** FINITE TEST COMPLETE — CAP HIT, PERIOD 8 OPEN.

The frozen command completed on both NumPy CPU and PyTorch CUDA backends with
exactly matching stage records.  Equations 3--12 were uncapped; equation 13
stored 2,000,000 prefixes and stopped on extension 2,000,001 after 138,760
admissible inputs.  No finite survivor is promoted to an infinite state, and
the parent 139 candidate remains `STOP / FORK` with period eight OPEN.
