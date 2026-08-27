# Compilation report

The final round was compiled from `main.tex` with pdfTeX under:

```text
SOURCE_DATE_EPOCH=1787788800
TZ=UTC
FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error
```

Two fresh output directories were created, each compiled twice, and then
compared byte for byte.  Both fresh PDFs and the retained `main.pdf` had SHA-256
`32d7b5d7230986cb8f8d00e2cdcffcbe3e083b99be180320132bcf195333ef45`.
The final PDF is byte-identical to `main_round2.pdf`.

## Artifact audit

| Artifact | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `d9d24d5eac9d820472df18318478b350155da52b94f82d362a3a5886dc60372f` |
| `main_round1.pdf` | `e393b8371c48a0bcd9f26721f6e614f1fb15d32ec998ddc3e72c5c16324bfb83` |
| `main_round2.pdf` | `32d7b5d7230986cb8f8d00e2cdcffcbe3e083b99be180320132bcf195333ef45` |
| `main.pdf` | `32d7b5d7230986cb8f8d00e2cdcffcbe3e083b99be180320132bcf195333ef45` |

- pages: 2
- all fonts: embedded (`pdffonts` reports `yes` for every font)
- final and both fresh logs: no warnings, overfull/underfull boxes, undefined
  references/citations, or multiply defined labels
- visual inspection: both pages inspected at 130 dpi; no clipping, collisions,
  broken glyphs, table overflow, or anomalous whitespace
- all three improvement-round hashes: pairwise distinct

Auxiliary `.aux`, `.log`, and `.out` files are build sidecars and are excluded
from the release manifest.
