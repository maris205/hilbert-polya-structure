# Compile report

- LuaLaTeX, two settled passes per build, with `SOURCE_DATE_EPOCH=1788048000` and `FORCE_SOURCE_DATE=1`.
- Each of three rounds was compiled in two fresh directories; every same-round pair was byte-identical.
- Round SHA-256 values: `6af4f2ccf1e5bbb286c204a937ff46ea5de9523ac157398493ca57b6114e198e`,
  `b8bcc8f73fcc86cca88967c09532c559c469b40ec207a78b294eaafa4da77256`, and
  `1076dfc4469cd42aa86a2addc1bd757ebb5139d2b633d5c1a7c761bcf0db180a`.
- `main.pdf` is byte-identical to round 2, SHA-256
  `1076dfc4469cd42aa86a2addc1bd757ebb5139d2b633d5c1a7c761bcf0db180a`.
- Final PDF: 2 pages, 133,482 bytes; 18/18 fonts embedded and subset.
- Settled log is warning-free: no LaTeX/package warning, undefined reference, overfull box, or underfull box.
  The `rerunfilecheck` textual hit is package metadata only.
- Both pages were visually inspected at 110 dpi; matrices, projectors, equations, margins, references, and page
  break are intact.
