# Paper build — HCS-C126

Build with a frozen source date:

```text
SOURCE_DATE_EPOCH=1787529600 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The release audit performs two fresh isolated builds, compares both outputs
byte-for-byte with `main.pdf`, checks embedded fonts with `pdffonts`, scans the
final log for layout/reference/citation/package warnings, and renders every
page for visual inspection.
