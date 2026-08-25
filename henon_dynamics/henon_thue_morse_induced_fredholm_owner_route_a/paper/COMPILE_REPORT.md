# C164 compile report

- Engine: LuaHBTeX 1.14.0.
- Command: `SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC
  lualatex --interaction=nonstopmode --halt-on-error main.tex`.
- Final PDF: two A4 pages.
- Fresh fixed-epoch double build: byte-identical.
- Final/main-round2 SHA-256:
  `f4fa297a1f63d43ba0676096e6c3418a492dbeafcd93baff9aab5befbfa11223`.
- Round-0 SHA-256:
  `c838a2879d426755135142037c1466fbb26a6b17e08f1158fb26db1589838d60`.
- Round-1 SHA-256:
  `186c4af5f84eb6a47ae44820cf4658613d8e6c4606dd4b1de9710971b71b4f2a`.
- The three manuscript snapshots are content-distinct; `main.pdf` is
  byte-identical to `main_round2.pdf`.
- `pdffonts`: every listed font is embedded; every CID font is subset and the
  remaining embedded Type-1 mathematical fonts are subset as reported.
- Final log: no warning, overfull/underfull box, missing glyph, undefined
  reference/citation, or multiply defined label.
- Visual audit: both rendered pages are readable; English and independently
  phrased Chinese abstracts, equations (1)--(7), declarations, and margins
  show no clipping, collision, blank region, or truncation.

Build auxiliaries are excluded from release and removed after this report.
