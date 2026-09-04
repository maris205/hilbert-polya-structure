# P189 Review-B Build and PDF QA

## Scope

This note expands the rendered-artifact checks from `REVIEW.md` into a
standalone QA record for the immutable bound PDF:

```text
papers/189-transpose-row-compression/main_round1.pdf
SHA-256: 6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81
```

No PDF was rebuilt or modified during this hardening pass.

## Static artifact checks

Review B re-ran `pdfinfo`, `pdffonts`, and `pdftotext` against the frozen
Round-1 PDF and confirmed:

| field | value |
|---|---|
| Pages | `4` |
| Page size | `595.276 x 841.89 pts (A4)` |
| File size | `363099 bytes` |
| PDF version | `1.5` |
| Encrypted | `no` |
| Form | `none` |
| JavaScript | `no` |
| Metadata Stream | `no` |
| Title / Subject / Keywords / Author / Creator / Producer | all blank |

The extracted text still contains the expected anchors:

- `Four-Iterate Collapse`
- `Every-Target Fibres at Times One and Two`
- `References`
- `OWNER_AMBER / HOLD_EXTERNAL`

## Font audit

`pdffonts` reported `29` font rows.  Every row remained:

- embedded;
- subsetted;
- Unicode-mapped.

No missing-font or partial-embed defect was observed.

## Visual page audit

The four pages were rasterized and inspected at `180 dpi`.  Review B found:

- no blank page;
- no truncated or clipped text block;
- no malformed displayed equation;
- no broken table;
- no broken bibliography page;
- no visible overlap or runaway text.

Page 4 remains short but valid: it is a complete references page with expected
white space, not a build failure or truncation artifact.

## Bound source/PDF consistency

The current pinned theorem source and rendered artifact remain:

- `main.tex` SHA-256:
  `c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457`
- `main_round1.pdf` SHA-256:
  `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`

The QA pass checked only consistency and render integrity for the already
frozen Round-1 artifact.  It does not certify any rebuilt output or authorize
external circulation.

## Conclusion

No rendered-artifact defect was found.  The Review-B package conclusion
remains unchanged:

- verdict: `PASS`
- findings: `critical=0`, `major=0`, `minor=0`
- external status: `OWNER_AMBER/HOLD_EXTERNAL`
