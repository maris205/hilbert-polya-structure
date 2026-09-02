# Deterministic compile report — HCS-C300

## Contract

- Engine: LuaLaTeX
- Passes per build: 2
- Environment: `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`
- Isolation: two fresh directories per round, six builds total
- Settled-log rejection: LaTeX/package warnings, overfull/underfull boxes, undefined citations/references, rerun requests, and missing characters

## Results

| Round | Pages | Bytes | Embedded subset-font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 2 | 123246 | 17 | `d494467b8163758a36e942a588982ab358a18d263be3236eeef0aa86755a9a69` |
| 1 | 3 | 130845 | 17 | `32020b4388648121ae19fd60ece4ca076476c023190d8265566335017d79936a` |
| 2 | 3 | 139604 | 18 | `051da17fe465f1314e40a00329bf06d677b598080f8609cd05f6b9af4790e90a` |

Both isolated outputs for every round were byte-identical to the corresponding archive.  `paper/main.pdf` equals round 2.  Every font row is embedded and subset, all eight archived pages rasterize, and direct visual inspection found no clipping, overlap, malformed formula, naked `qquad`, or unreadable text.  All settled logs are warning-free, and extracted-text contracts distinguish the three revisions.
