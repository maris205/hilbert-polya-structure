# Test report

| Gate | Result |
|---|---|
| Producer | PASS; 12 finite rows, 298 cells, 60 diagnostics |
| Independent checker | PASS; 5,606 explicit checks |
| Exhaustive enumeration | PASS; 33,867 graph masks through n=6 |
| SymPy lane | PASS; polynomial, tail, factorial identities |
| Isolated replay | PASS; two fresh outputs equal archive bytes |
| Hostile mutation | PASS; 82/82 killed, including three collision-map attacks, repaired/stale hash, and `-O` |
| Strict YAML/JSON | PASS; exact trees/types and parser attacks |
| Paper release | PASS; three distinct progressive deterministic rounds |
| Font/text/render | PASS; embedded/subset fonts, sentinels, rendered pages |
| Closed-world manifest | PASS; 27 payload plus self-excluded manifest |

The independent checker does not import the producer.  The exact finite table
and the asymptotic proof have separate evidence owners.  The C301/C291/C276
collision map is an exact checked evidence subtree.
