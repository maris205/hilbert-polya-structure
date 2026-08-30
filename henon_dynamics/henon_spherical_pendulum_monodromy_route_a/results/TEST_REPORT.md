# C244 test report

| gate | result |
|---|---|
| deterministic producer | C244_PRODUCER_PASS (7 critical, 8 regular) |
| independent checker | PASS (308 assertions) |
| SymPy and original-action cross-check | C244_SYMPY_PASS (77 checks) |
| byte replay | C244 byte replay: PASS |
| hostile mutations | PASS 34/34, with repaired payload hashes |
| PDF build | three distinct fixed-epoch LuaLaTeX PDFs; final double-build byte match |
| scope firewall | all nine flags false; Route B not invoked |

The release manifest is generated only after the commands above and the PDF
font/text checks succeed.
