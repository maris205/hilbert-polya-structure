# Test report: HCS-C360

The frozen canonical run produced:

```text
C360 producer: PASS 61ad52105de3ee33b0bd97c7c3c57b974a95b3e310450ba7f6a68571c410c751
C360 independent checker: PASS 95 checks
C360 SymPy cross-check: PASS 26 exact identities
C360 byte replay: PASS 2 isolated copies
C360 hostile mutation suite: PASS 60/60
```

The release gate additionally executes every lane under `python -B`, verifies
explicit failure under `-O` and `-OO`, builds every PDF revision twice in
fresh directories, audits fonts/text/rasters, and enforces the 27-payload
ledger before it writes the self-excluded manifest.
