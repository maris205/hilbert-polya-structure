# Compile report — HCS-C133

- engine: pdfTeX 1.40.22;
- command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice;
- source SHA-256: `2adc1a163484ca2dceca63cf52eeb8af4b11eb551b4af5b35d2d25cf3984163e`;
- final PDF SHA-256: `bc4c75b18083a98ad272b752dff06d95cf658326f4c12973ee0e29daef73f351`;
- output: 3 US-letter pages, PDF 1.5;
- two fresh isolated two-pass builds: byte-identical to one another and to the
  checked-in final PDF;
- round snapshots: byte-identical release reconciliations of the final source;
- fonts: every font reported by `pdffonts` is embedded and subset;
- final log: no warning, overfull/underfull box, undefined reference, citation,
  or multiply-defined label;
- rendered inspection: all three pages have complete content with no clipping,
  collision, truncation, malformed formula, or blank page.

The frozen epoch removes creation-time metadata variance only and does not
change the mathematical content.
