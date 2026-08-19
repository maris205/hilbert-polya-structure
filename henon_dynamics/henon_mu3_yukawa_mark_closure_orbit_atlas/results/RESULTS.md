# C76 results

The canonical JSON evidence is
`results/c76_closure_orbit_atlas_evidence.json`.

| Quantity | Exact value |
|---|---:|
| ambient core `|Q|` | 54 |
| named labels | 16 |
| all supports | 65536 |
| effective label group order | 1920 |
| effective group structure (GAP) | `C2 x S5 x D8` |
| support orbits | 3024 |
| closure-minimal supports | 98 |
| closure-minimal orbits | 34 |
| full-core minimal supports | 25 |
| full-core minimal orbits | 7 |

## Orbit spectrum

| Orbit size | 1 | 2 | 4 | 5 | 8 | 10 | 16 | 20 | 40 | 80 | 160 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of orbits | 128 | 256 | 416 | 128 | 192 | 384 | 16 | 672 | 608 | 208 | 16 |

The orbit count by support cardinality `k=0,...,16` is

```text
1, 7, 27, 73, 151, 252, 352, 424, 450,
424, 352, 252, 151, 73, 27, 7, 1.
```

## Closure and minimality

Aggregated by generated-subgroup order, the support/orbit counts are

| closure order | 1 | 2 | 3 | 6 | 9 | 18 | 27 | 54 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| supports | 32 | 32 | 256 | 256 | 2080 | 2080 | 30400 | 30400 |
| orbits | 6 | 6 | 24 | 24 | 150 | 150 | 1332 | 1332 |

Closure-minimal supports by cardinality are `{0:1, 1:11, 2:48, 3:38}`.
Their 34-orbit spectrum is `{1:10, 2:8, 4:14, 8:2}`.  Full-core minimal
supports all have size three; the 25 supports form seven orbits with spectrum
`{1:1, 2:2, 4:3, 8:1}` and representative masks
`[261, 265, 321, 324, 385, 448, 33025]`.

The C75 ambient C6 kernel is recorded in the evidence and excluded from the
support action.  No arithmetic/local or full Burnside-ring claim is made.
