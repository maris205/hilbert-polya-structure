# C228 compile report

- Engine: LuaLaTeX; two passes per revision.
- Fixed environment: `SOURCE_DATE_EPOCH=1787875200`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Two independent complete builds (two LuaLaTeX passes in isolated
  directories for each revision) compared byte-for-byte: PASS for all three
  revision PDFs.
- The `hyperref` option `hypertexnames=false` is set in `main.tex`; the
  duplicate-destination warning seen in the settled log is absent from every
  pass of both builds.  First-pass bootstrap messages (unresolved citations
  and rerun labels, plus `rerunfilecheck`) resolve on pass two; pass-two logs
  have no warnings, overfull/underfull boxes, undefined references, missing
  material, or errors.
- A settled-directory regression sequence (0\to1\to2\to2) was also run;
  all four logs contain zero duplicate-destination messages.
- Page counts: round 0 = 2, round 1 = 3, round 2/final = 3; page size A4.
- Final font audit: 18 entries, every font embedded and subset.
- Extracted-text audit: PASS for Cayley, Stockmayer, Flory, both Lambert
  branches, 696 assertions, 28/28 mutations, scope and Route-A literals.
- Visual audit: all three pages inspected at 120 dpi; no clipping, overlap,
  malformed equation, broken glyph, orphaned heading or illegible reference.
- `main.pdf == main_round2.pdf`: byte-for-byte PASS.
- Release package build sidecars: none.

## SHA-256

```text
main_round0_original.pdf  f93ae3901fdade7de29dd58abf9c73f0bd9b20790dba23170761cefc2dbde0af
main_round1.pdf           8171cd946234362fa357f0879128947f9249af7cc37571ae538d258d8a0b1edf
main_round2.pdf           48e58417920260ab069196d9d2c24a56c2f772d63b3f3cfc372ce63b7a994b77
main.pdf                  48e58417920260ab069196d9d2c24a56c2f772d63b3f3cfc372ce63b7a994b77
```

The round hashes differ because round 1 adds the two postgel dynamical
closures and round 2 adds the independent audit and Route-A boundary.
