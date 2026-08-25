# C164 test report

| gate | receipt |
|---|---|
| deterministic producer | PASS; 128 source bits, 32 branch rows, 392 formal cells |
| independent checker | PASS; 668 assertions |
| SymPy reconstruction | PASS; 197 checks through degree 24 and five symbolic branches |
| canonical replay | PASS; 21,764-byte evidence is byte-identical |
| hostile mutations | PASS; 61/61 repaired-hash plus 1/1 stale-hash rejected |
| theorem cutoff audit | PASS; finite rows explicitly labeled sentinels |
| operator-object separation | PASS; induced, uninduced, and scalar objects remain distinct |
| scope firewall | PASS; no forbidden input or affirmative claim flag |

PDF determinism, fonts, warnings, rendered pages, and manifest closure are
recorded in the compile report and final release manifest.
