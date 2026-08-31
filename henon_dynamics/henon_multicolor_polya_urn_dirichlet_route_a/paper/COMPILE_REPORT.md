# Compilation report

- Engine: LuaLaTeX, two passes per revision in fresh temporary directories.
- Fixed environment: `SOURCE_DATE_EPOCH=1788048000`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- The LuaTeX trailer ID is fixed in `main.tex`.  Two additional fresh final
  builds are byte-identical to each other and to `main.pdf`.
- Round 0 and round 1 each have two pages; round 2/final has three pages.
- SHA-256 hashes are:
  - round 0: `b7807a88d80052cf0e9dc2bef90ba447c2e1dc8a64f470e0756cdd5618803daf`;
  - round 1: `e6f13c9bfa2b3e73f7186005f0ebae616ed985a687a4eeb3869c10412d697b48`;
  - round 2/final: `964abebbfeeb64af5f2d3038a790a537476faa88d0485cacfc4e055b4f946c88`.
- The final PDF contains 20 embedded, subset font records.  Text extraction,
  DOI links, page geometry, and all three rendered pages were visually checked.
- The settled second pass has no overfull/underfull box, undefined reference,
  missing citation, duplicate destination, or layout warning.  The appearance
  of the loaded `rerunfilecheck.sty` package name is not a warning.
- The final integrity pass anchored the Eggenberger--Pólya source in the
  manuscript body.  Two new fresh-directory builds were byte-identical,
  warning-free, and visually rechecked; historical rounds 0 and 1 were not
  rewritten.
