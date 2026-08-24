# Test report — HCS-C133

## Deterministic exact tests

The producer reconstructs the full rational scattering matrices, symbolic
secular determinant, physical specialization, trace polynomials, primitive
counts, and both negative controls.  The checker imports no producer code and
reconstructs every headline receipt.  The separate SymPy program derives the
same determinant through the three-dimensional block reduction and checks the
Newton/log-determinant series through degree six.

## Integrity tests

- canonical evidence replay is byte-identical;
- all 48 repaired-hash semantic mutations and one stale-hash mutation are
  rejected;
- scope, tuple, Route-B flag, controls, determinant coefficients, traces, and
  primitive counts, exact text conventions, progress fields, and closed
  schema keys are mutation-covered;
- no random seed, external source, floating tolerance, or fitted input occurs.

## Release tests

The final release additionally requires fixed-epoch double PDF compilation,
embedded-font and warning scans, rendered-page inspection, and exact manifest
closure.  Their hashes and outcomes are recorded in `paper/COMPILE_REPORT.md`
and `C133_RELEASE_MANIFEST.json`.
