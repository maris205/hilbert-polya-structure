# Test report — HCS-C300

All Python commands use `PYTHONDONTWRITEBYTECODE=1` and `TZ=UTC`.

| Gate | Result |
|---|---|
| `python -B code/c300_euler_producer.py` | `C300_PRODUCER_PASS`; 20 cases; 437 cells |
| `python -B code/c300_euler_checker.py` | `PASS (1219 assertions; producer import forbidden)` |
| `python -B code/c300_euler_sympy_crosscheck.py` | `PASS (30 symbolic identities)` |
| `python -B code/c300_euler_replay.py` | byte-for-byte `PASS` |
| `python -B code/c300_euler_mutation.py` | `PASS 110/110` |
| shock signs | family 1 negative branch and family 2 positive branch reconstructed independently |
| entropy | direct jump production equals the closed negative formula in all 17 shock rows |
| no-vacuum | every independent log-density solve returns the prescribed positive root |
| pressureless boundary | exact separating roots decrease and compressive roots increase as \(a\) halves |
| strict evidence JSON | exact recursive trees, row key sets, primitive types, ordered unique case IDs, and canonical rational/decimal strings enforced |
| strict YAML | the full expected tree and types are locked; duplicate/merge/anchor/alias/title/dynamics/artifact/verdict/scope attacks rejected |
| optimized Python | checker explicitly refuses `python -O`; its acceptance path contains no `assert` statements |
| three paper rounds | distinct 2/3/3-page PDFs, settled logs, embedded subset fonts |
| six fresh builds | each pair byte-identical to its archive |
| closed-world ledger | 27 payloads plus one self-excluded manifest |

The finite cases regress formulas and branch signs; they are not used to infer the arbitrary-data theorem.  Repaired-hash mutations demonstrate that semantic rejection is independent of a stale payload digest.  In particular, false theorem text, affirmative nonclaims, altered reference or boundary prose, unexpected keys, duplicate case identifiers, noncanonical numeric receipts, integer-for-string substitutions, and five repaired-hash YAML substitutions are all rejected.
