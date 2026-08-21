# C87 compile report

Status: `PASS`.

- Two isolated `latexmk` builds used `SOURCE_DATE_EPOCH=0`, `TZ=UTC`, and
  `LC_ALL=C`.
- Both PDFs are byte-identical: SHA-256
  `6b676d65b14aaf6f93f8d8d5e7226cbac45f1fb1a8379a0240dcbdf1c6cabd13`.
- Pages: 3.
- Undefined references/citations: 0 after the clean multi-pass build.
- Overfull/underfull boxes: none reported.
- Fonts: all listed fonts are embedded and subsetted.
- Visual inspection: all 27 pair-orbit rows, the endpoint identity, the C82
  bridge, and the scope disclaimer render without clipping or overlap.
