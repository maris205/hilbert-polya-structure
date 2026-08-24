# C130 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `b3e063054b7b9ae28a231adad4f7ec3a4779d61e29151e033109c177faf4b77d`
- PDF: `paper/main.pdf`
- PDF SHA-256: `9ec16deb5b639f29e101c56dd1a74b9662292a875d29e2b8263d82920b3ef9b6`
- Size: 302,023 bytes
- Pages: 2 (A4)
- Engine: pdfTeX 1.40.22 via latexmk 4.76
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `TZ=UTC`

## Preserved rounds

| PDF | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `d8e26ca9cec8921fb03a4eed4024756fe27940863cfd577ce1a4b1f09ecc2b09` |
| `main_round1.pdf` | `7ba1bde9a12d524c432678c0dddecd3efdd550bae5ad437ff75a02b888f7aa21` |
| `main_round2.pdf` | `9ec16deb5b639f29e101c56dd1a74b9662292a875d29e2b8263d82920b3ef9b6` |

`main.pdf` and `main_round2.pdf` are byte-identical.

## Deterministic build audit

Two isolated builds, each starting with only the final `main.tex`, were run
with the fixed epoch.  Isolated A, isolated B, and the retained final PDF all
have SHA-256
`9ec16deb5b639f29e101c56dd1a74b9662292a875d29e2b8263d82920b3ef9b6`
and compare byte-for-byte equal.

## Submission-quality checks

- `pdffonts` lists 22 font instances and reports `emb=yes` for every one.
- The final log contains no LaTeX/package warning, overfull or underfull box,
  undefined reference/citation, multiply-defined label, or badness report.
- Extracted PDF text contains no `??`, `[?]`, `TODO`, `FIXME`, `XXX`, or
  `[VERIFY]` marker.
- Both pages were rendered at 150 dpi and inspected.  Titles, equations,
  product subscripts, the ten-period table, monospace boundary tuple, margins,
  and page break are legible; no clipping, overlap, truncation, blank page, or
  broken formula/table layout was found.

Build auxiliaries and temporary render/build directories are excluded from the
manifest and removed after this audit.
