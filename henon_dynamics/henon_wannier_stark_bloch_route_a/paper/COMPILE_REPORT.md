# Compile report

- Engine: LuaLaTeX; two settled passes per build.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`.
- Each of rounds 0, 1, and 2 was compiled in two separate fresh temporary directories; each pair was
  byte-identical.
- Round SHA-256: `3e394dcec95bcd4a111eca9f0075179ff751a9280cfa12af4f608e4b7ee689f5`,
  `e1b1f682df03ebdc755349ad709de4f6566dc8d5efc9a34e55c2ce23f2865104`, and
  `83c5a7eb7e17e770251ed769104c287e912f5a0909d8092e0926f42f472b3862`.
- `main.pdf` is byte-identical to round 2 and has SHA-256
  `83c5a7eb7e17e770251ed769104c287e912f5a0909d8092e0926f42f472b3862`.
- Final PDF: 2 pages, 150,609 bytes, PDF 1.5.
- `pdffonts` reports 21/21 fonts embedded and subset.
- The settled final log is warning-free: no LaTeX/package warning, undefined reference, overfull box, or
  underfull box.  The sole textual match for `rerunfilecheck` is package-identification metadata, not a warning.
- Visual inspection at 120 dpi confirms intact margins, equations, hyperlinks, page flow, and bibliography.
