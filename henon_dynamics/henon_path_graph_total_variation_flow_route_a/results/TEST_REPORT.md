# C279 test report

| surface | result |
|---|---|
| deterministic exact producer | PASS, 19,530 exhaustive + 5 stress inputs |
| producer-independent coordinate reconstruction | PASS, 1,010,097 assertions |
| SymPy incidence/flux/dissipation reconstruction | PASS, 3,707 checks |
| two-fresh-tree byte replay | PASS |
| repaired-hash hostile mutations | PASS, 58/58 |
| stale-hash control | PASS |
| exact top-level and nested schemas | PASS |
| scope, evaluator, source, and Route-A locks | PASS |
| Steidl/Hoefling direct-owner semantic locks | PASS |

The checker imports no producer module.  The producer represents maximal
blocks and evolves their heights; the checker instead reconstructs an edge
flux on each coordinate plateau, forms `-D^T z`, and finds the next zero jump.
It recomputes the exhaustive and stress digests, all summary histograms, and
all eight complete witnesses.  KKT conditions are checked at events and
strictly inside affine intervals, not only at final consensus.

The mutation suite repairs the payload SHA-256 after every semantic edit, so
its 58 rejections exercise schema and meaning rather than merely stale hash
detection.  The un-repaired edit is retained separately as the stale control.
