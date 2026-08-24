# Compile report — C114

- engine: pdfLaTeX through `latexmk`;
- fixed environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`;
- isolated build A SHA-256: `54db259d2f73c1eeaa967714aad50c5bafa96c2e635a1a2666689add70425def`;
- isolated build B SHA-256: `54db259d2f73c1eeaa967714aad50c5bafa96c2e635a1a2666689add70425def`;
- final `main.pdf` SHA-256: `54db259d2f73c1eeaa967714aad50c5bafa96c2e635a1a2666689add70425def`;
- pages: 2;
- deterministic byte comparison: pass;
- font audit: every reported font is embedded;
- final log audit: no unresolved reference or citation, overfull or underfull
  box, or material warning.

The normal first-pass cross-reference rerun was resolved by `latexmk`; the
second-pass isolated logs are clean.
