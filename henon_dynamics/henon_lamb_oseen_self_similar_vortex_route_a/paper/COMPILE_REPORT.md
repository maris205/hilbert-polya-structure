# Deterministic compile report

## Contract

- Engine: LuaLaTeX
- Passes per build: 2
- Environment: `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`
- Isolation: two isolated directories per round, six fresh builds total
- Settled-log rule: no LaTeX/package warning, overfull or underfull box, undefined reference/citation, rerun request, or missing character

## Results

| Round | Pages | Bytes | Embedded subset-font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 3 | 145358 | 20 | `1c127bc83686c042835e589ccbfbbe84609b5ac90e336f973557f03c4a4fedc9` |
| 1 | 3 | 176677 | 23 | `8e2ba5c010ae21cf61edffcfa77f69df2f49c0293c3e2a94bc2ae915ffd19de7` |
| 2 | 4 | 187981 | 24 | `5b1a4d4dd9480e55ff970b5ae01dac8435c5c9ac4a62ee3c1f740288cd342b61` |

For each round, both fresh outputs were byte-identical to the archived artifact.  `paper/main.pdf` is byte-identical to round 2.  All font rows reported both embedded and subset status, every page rasterized at 72 and 90 dpi, and direct visual inspection passed all 10 archived pages, including the UTF-8 journal title `för` and the real-lift angle convention.  Extracted-text contracts distinguish the three substantive revisions.
