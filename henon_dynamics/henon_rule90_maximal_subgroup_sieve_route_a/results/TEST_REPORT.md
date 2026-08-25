# C160 test report

| gate | receipt |
|---|---|
| deterministic producer | PASS; 9 family rows, 27 subset cells |
| independent checker | PASS; 186 assertions |
| SymPy reconstruction | PASS; 100 polynomial checks through `r=8` |
| canonical replay | PASS; byte-identical evidence |
| hostile mutations | PASS; 46/46 repaired-hash plus 1/1 stale-hash rejected |
| exact sieve/Möbius comparison | PASS for every finite row |
| scope/no-infinitude firewall | PASS |

The compile report and manifest record the final PDF and content-addressed
release gates.
