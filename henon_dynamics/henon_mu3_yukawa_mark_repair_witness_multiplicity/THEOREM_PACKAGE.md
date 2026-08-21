# C79 theorem package

Let `I(D)` be the set of direction blocks fully contained in `D`, with sizes
`(1,1,2,5)`.  The source-bound C73 generation criterion says that a retained
support generates the full core exactly when it contains `S9` and hits at
least two blocks.  Restoring the pivot and one label for each excess deleted
block proves

```text
rho(D)=1_{S9 in D}+max(0,|I(D)|-2).
```

If three blocks are fully deleted, any one label from those blocks repairs the
direction condition, giving `sum_{i in I}s_i` witnesses.  If all four are
deleted, two restored labels must come from distinct blocks, giving
`sum_{i<j} s_i s_j`; for at most two deleted blocks the minimum witness is
unique.  The direct C75 point-set closure enumeration verifies these formulas
and the complete coefficient table for all 65536 masks.

The result is finite and presentation-specific; the arithmetic/local firewall
is explicit.
