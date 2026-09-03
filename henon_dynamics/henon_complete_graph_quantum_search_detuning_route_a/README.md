# HCS-C323: complete-graph quantum-search detuning

This package proves the complete bright/dark spectral theorem and exact
detuning law for

\[
H_g=-g|s\rangle\langle s|-P_W,
\qquad a=M/N.
\]

For `0<a<1`, perfect search occurs exactly at `g=1`, at first time
`pi/(2 sqrt(a))`.  The paper also gives the full dark multiplicities,
off-resonance maximum, critical `sqrt(a)` detuning window, graph-adjacency
global phase, and all zero/full-marked and zero-driver faces.

## Reproduce

```bash
python3 -B code/c323_quantum_search_producer.py
python3 -B code/c323_quantum_search_checker.py
python3 -B code/c323_quantum_search_sympy_crosscheck.py
python3 -B code/c323_quantum_search_replay.py
python3 -B code/c323_quantum_search_mutation.py
python3 -B code/c323_release_manifest.py
```

Every lane refuses `python -O`.  The release gate additionally performs two
fresh deterministic LuaLaTeX builds of each of the three substantive paper
revisions, checks logs, fonts, rasters, hashes, and the exact 27-payload
ledger.

## Route-A result

Strict tuple:

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.

Overall verdict: `ROUTE_A_REJECTED`; Route B is locked.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
