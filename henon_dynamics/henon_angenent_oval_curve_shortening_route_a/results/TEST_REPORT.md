# C314 test report

| lane | result |
|---|---|
| deterministic producer | PASS |
| independent strict checker | PASS — 2,632 checks |
| SymPy cross-check | PASS — 9 groups |
| isolated byte replay | PASS |
| hostile mutation suite | PASS — 44/44 |
| optimized Python | fail closed |
| three archived PDF rounds | distinct and deterministic |
| settled LaTeX logs | warning-free |
| final PDF fonts | embedded and subset |

The release script reruns every lane twice where determinism is claimed and
rejects any undeclared file or stale manifest.
