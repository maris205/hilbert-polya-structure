# C172 exact test report

All exact validation layers pass:

- deterministic producer: pass;
- independent exact checker: 663 assertions, pass;
- abstract primitive and nonprimitive cycle enumeration: pass;
- SymPy permutation-matrix reconstruction: 486 checks, pass;
- byte replay: pass;
- repaired-hash semantic mutations: 44 rejected of 44;
- stale-hash mutation: 1 rejected of 1.

Final PDF reproducibility, embedded-font and warning audits are recorded in
`paper/COMPILE_REPORT.md`; content closure is recorded in the release manifest.
The registered citation population is zero and no external data are used.
