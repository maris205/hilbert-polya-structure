# Deterministic compile report

## Method

Each revision is built in a fresh temporary directory with two settled LuaLaTeX passes:

```bash
SOURCE_DATE_EPOCH=1788393600 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{N}\input{main.tex}'
```

The release gate performs two independent fresh-directory builds for every (N\in\{0,1,2\}) and compares both with the checked PDF.

## Checked artifacts

| round | pages | SHA-256 |
|---:|---:|---|
| 0 | 2 | `f8a65c7f1616d2e4196b2053482acb1e55d3ede086ccffb6fdf800b501a11921` |
| 1 | 2 | `0158395607b4d9fe43c28cc06d8dfc5a8ed377abd895c45bd6525fe40c1ee517` |
| 2 | 3 | `28d82beba070c42b33b211e2a2699c272397fa877c66bac0a26c8a2210947dd1` |
| final | 3 | `28d82beba070c42b33b211e2a2699c272397fa877c66bac0a26c8a2210947dd1` |

All three revision hashes are distinct and `main.pdf` is byte-identical to round 2.

## Quality gates

- settled warning matches: 0;
- overfull/underfull boxes: 0;
- undefined references/citations and rerun requests: 0;
- missing glyphs: 0;
- all font rows embedded and subset: yes;
- unexpected extracted-text control bytes or literal TeX garbage: 0 (the known Poppler DC2/DC3 mapping of two Type-1 large-integral glyphs is normalized after visual confirmation);
- all 7 total revision pages rasterized successfully;
- visual inspection of all 3 final pages: passed.
