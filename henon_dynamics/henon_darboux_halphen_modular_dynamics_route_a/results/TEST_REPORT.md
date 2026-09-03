# C320 test report

- Producer: PASS; payload
  `a20ea9c547a905c103cfafc9526e16ecd2d18799fe748de65f8939343234c8b0`.
- Independent checker: PASS, 1,945 checks.
- SymPy lane: PASS, 345 exact identities.
- Isolated producer replay: PASS, byte for byte.
- Hostile evidence/YAML suite: PASS, 56/56 rejected.
- `Q^128` triple lock: polynomial ODE, divisor-sum/E2 bridge, and theta
  modular `S,T` laws all pass.
- Optimized Python: all five executable lanes refuse `python -O`.
- Evaluation lock: raw SHA-256
  `ec086cb94fd2131f75bf138675e4fa2ca1ad2b8331f01f03b9159c069541b220`;
  semantic SHA-256
  `843b788e9bbfcbbfbd0e6c926921dba4efe05ef35c6e1464c6f085478fa9b25f`.
- PDF: all three cumulative revisions are rebuilt twice in fresh LuaLaTeX
  directories; clean logs, embedded subset fonts, rasterization, and exact
  ledger closure are release-gated.
