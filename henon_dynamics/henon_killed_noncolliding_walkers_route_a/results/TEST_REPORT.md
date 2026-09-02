# Test report

All tests are run from the package root.

| Gate | Result |
|---|---|
| Producer | PASS; 36 cases, 502 states, 273 probes |
| Independent checker | PASS; 5,803 explicit checks, producer import forbidden |
| SymPy cross-check | PASS; 15 exact characteristic cases |
| Isolated replay | PASS; two fresh outputs equal archive bytes |
| Hostile mutations | PASS; 68/68 killed, including repaired/stale hash and `-O` |
| Route-A YAML | PASS; strict keys/types, no aliases/merges/duplicates |
| PDF build | PASS; three distinct content-progressive archives, deterministic |
| Fonts/text/render | PASS; embedded/subset fonts, sentinels, all pages rendered |
| Closed-world ledger | PASS; 27 payload files plus self-excluded manifest |

The checker reconstructs the generator and never imports the producer.  The
finite cutoff is not used as evidence for the analytic quantifiers.
