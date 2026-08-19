# C73 pilot report

Status: **PASS**.

The generation game has apex `S9`, six dummy coordinates, and four projective
direction blocks of sizes `1,1,2,5`.  The non-isolated part of the 16-label
minimal-generation hypergraph is the 25-edge cone over `K_{1,1,2,5}`; the six
dummy labels are isolated vertices.  Its five minimal blockers have sizes
`1,4,7,8,8`.  Exact deletion enumeration gives

```text
destructive deletion sets: 35136
surviving deletion sets:   30400
```

The homogeneous reliability is

```text
R(q)=(1-q)(1-q^4-q^7-2q^8+3q^9).
```

Unprotected worst-case deletion tolerance is `0`; after protecting `S9` it
is `3`; the maximum number of deletions for which some support still survives
is `13`, attained by exactly 25 deletion sets.
