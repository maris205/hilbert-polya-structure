# Test report: HCS-C363

The frozen canonical run produced:

```text
C363 producer: PASS 26d850afd510acc733eb08350e39894eeb72af524df0dcce5d495503f89d6f47
C363 independent checker: PASS 99 checks
C363 SymPy cross-check: PASS 17 exact identities
C363 byte replay: PASS 2 isolated copies
C363 hostile mutation suite: PASS 61/61
```

The release gate also checks `-O`/`-OO` refusal, two fresh two-pass builds for
each manuscript round, exact PDF bytes, logs, fonts, text, page rasters, and
the complete 27-payload ledger.
