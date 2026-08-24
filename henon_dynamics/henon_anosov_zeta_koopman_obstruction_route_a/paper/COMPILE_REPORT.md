# Compile report — C125

- engine: pdfLaTeX through `latexmk`;
- fixed environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`;
- isolated build A SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- isolated build B SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- final `main.pdf` SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- round-zero snapshot SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- round-one snapshot SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- round-two snapshot SHA-256:
  `41d702ca3649ffcea781739895a1bd6290af1c823d4c4e3f7513f383c5bb6f83`;
- source `main.tex` SHA-256:
  `f6fce65d8828c987411a7b38c4e53205be533a28d92016f786646eec25efc4ef`;
- pages: 2;
- deterministic byte comparison: pass;
- checked-in PDF agrees with both isolated builds: pass;
- font audit: every reported font is embedded;
- final log audit: no unresolved reference or citation, overfull or underfull
  box, undefined or multiply-defined label, or material package warning;
- raster inspection: both pages pass, with no clipping, collision, truncation,
  blank content, or malformed formula/table text.

All three named round snapshots will be synchronized with the final source;
their byte identity is intentional and documented in the improvement log.
