# Compile report — HCS-C136

- engine: pdfTeX 1.40.22 through latexmk 4.76;
- command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`;
- final source SHA-256: `3b4048dad1ae7f7d0f94cd4fcf1d8d9cbb62b85093336827a5638d513ddf718e`;
- final PDF SHA-256: `ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d`;
- final PDF bytes: 214,166;
- output: 4 US-letter pages, PDF 1.5;
- two fresh isolated latexmk builds: byte-identical to each other and to the
  checked-in final PDF;
- round 0 SHA-256: `d7547df486ccd4c4808c92b068aa63d1c593c5cd0770b6e850f7889f9b3cb275`;
- round 1 SHA-256: `0b082ac82dbdea999ab1c51f32fef76a53b946bcce28bde4c488d68470d2fa0f`;
- round 2 SHA-256: `ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d`;
- the three snapshots are distinct successive drafts; `main.pdf` is
  byte-identical to `main_round2.pdf`;
- fonts: all 17 fonts reported by `pdffonts` are embedded and subset;
- final isolated log: zero warning, overfull/underfull box, undefined
  reference/citation, or multiply-defined-label lines;
- text scan: no `??`, `[?]`, `TODO`, `FIXME`, `XXX`, or `VERIFY` marker;
- rendered inspection: all four pages contain complete, legible content with
  no clipping, collision, truncation, malformed formula, or blank page.

The fixed epoch removes metadata variance only.  It does not alter the source,
the mathematical statements, or the real differences among revision rounds.
