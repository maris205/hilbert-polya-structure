# C249 test report

| gate | result |
|---|---|
| deterministic producer | `C249_PRODUCER_PASS` (8 parameter, 5 cycle rows) |
| independent checker | `PASS` (264 assertions; full reintegration) |
| quick hostile preflight | `PASS` (234 assertions) |
| SymPy cross-check | `C249_SYMPY_PASS` (81 symbolic identities) |
| clean byte replay | `C249 byte replay: PASS` |
| hostile mutations | `PASS 40/40`, repaired payload hashes |
| PDF build | three distinct fixed-epoch LuaLaTeX PDFs; each double-build byte match |
| scope firewall | all nine flags false; Route B not invoked |

The release manifest is generated only after the commands above, PDF text and
font checks, and the exact file-ledger check succeed.
