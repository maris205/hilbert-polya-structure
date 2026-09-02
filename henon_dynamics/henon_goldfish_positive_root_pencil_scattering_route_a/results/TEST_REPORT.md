# C315 test report

| lane | result |
|---|---|
| deterministic producer | PASS |
| independent strict checker | PASS — 2,047 checks |
| SymPy cross-check | PASS — 7 groups |
| isolated byte replay | PASS |
| hostile mutation suite | PASS — 45/45 |
| optimized Python | fail closed |
| three archived PDF rounds | distinct and deterministic |
| settled LaTeX logs | warning-free |
| final PDF fonts | embedded and subset |

The release script reruns every lane, rebuilds every paper round twice, and
rejects undeclared files, stale manifests, build warnings, unembedded fonts,
or unrasterizable pages.
