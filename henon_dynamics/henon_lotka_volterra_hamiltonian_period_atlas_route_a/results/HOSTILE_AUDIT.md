# Hostile audit

The mutation harness applies 11 repaired-hash semantic edits and one stale-hash
edit.  The independent checker rejects all 12:

```text
repaired_hash=11
stale_hash=1
caught=period,area,branch,action,route,route_b,scope,flag,parameter,unknown,stale,source
```

Per-level hashes are checked in a cheap preflight before expensive quadrature,
so a repaired numerical mutation cannot hide behind unchanged cells.  The
unknown-key attack tests recursive key closure; the stale attack leaves the
original payload hash unchanged.
