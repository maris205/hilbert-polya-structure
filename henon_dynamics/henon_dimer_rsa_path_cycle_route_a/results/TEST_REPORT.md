# Test report

## Exact and symbolic gates

```text
C291_PRODUCER_PASS path_rows=11 cycle_rows=7 factorial_rows=21 payload_sha256=1e9911ffb46b20b1c50e0a22566eb5048860d50ff0fb3be787fb9e64d6092af4
C291 independent bitmask/order checker: PASS (19371 assertions; strict duplicate-rejecting JSON/YAML schema)
C291_SYMPY_PASS (132 symbolic checks; Riccati, H1, H2, pole algebra, supports)
C291 fresh-path byte replay: PASS sha256=65fdb2333d3fbb6c3177eaa7da5d303ab0b42f2ff99b8d55ecd97e1863008a0f bytes=23778
C291 hostile mutation audit: PASS 105/105
```

The checker imports no producer code.  Its edge-order oracle evolves exact
counts on `(processed-edge mask, matched-vertex mask)` states and therefore
counts every labeled permutation.  It separately applies the general
falling-factorial conditional identity, so altered higher-order cells are not
accepted merely because the first two moments remain intact.

## Schema and semantic attacks

All repaired-hash attacks were rejected, including altered PGF/Riccati/moment
contracts, maximal-to-maximum drift, wrong support endpoints, cycle-index and
boundary edits, high-order moment edits/truncation, decimal cells, source and
collision text, Route tuple, scope flags, bool-as-int, unknown/missing keys,
row drops, order swaps, and duplicate replacements.  The checker additionally
rejected a stale payload hash, raw JSON duplicate key, raw `NaN`, YAML
schema/source/unknown/missing/tuple/verdict/Route-B/scope/cutoff/type changes,
and raw duplicate keys at both the YAML top level and a nested mapping.
The recursive safe loader, exact key/type/value contracts, and frozen semantic
hash are exercised both by the checker and directly by the release gate.

## Paper/release gates

The definitive PDF hashes, page/font counts, two-build comparison, settled-log
scan, and manifest closure are recorded in `paper/COMPILE_REPORT.md` and
`C291_RELEASE_MANIFEST.json` after the final deterministic build.
