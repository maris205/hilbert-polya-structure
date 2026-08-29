# C227 compile report

- Engine: LuaLaTeX.
- Deterministic environment: `SOURCE_DATE_EPOCH=1787875200`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Passes per revision: 2, in two independent fresh temporary build
  directories for each revision selector (`\CRevisionRound=0,1,2`).
- Independent complete build directories compared byte-for-byte: PASS for all
  three revisions.
- The pre-patch settled logs emitted duplicate equation destinations because
  conditional revision sections reused numeric names.  The minimal source
  repair adds `hypertexnames=false` to the `hyperref` options.  After the
  repair, both independent settled (second-pass) logs for all three revisions
  are clean: no `Warning`, duplicate destination, `Overfull`, `Underfull`,
  `Undefined`, `Missing`, or `Error` diagnostics.  First passes retain only
  the expected cross-reference/rerun warnings.
- Page counts: round 0 = 2, round 1 = 3, round 2/final = 3; all page sizes A4.
- Final fonts: 18 entries; every font embedded and subset.
- Text extraction: PASS for theorem, Hopf, boundary, scope and Route-A
  literals.
- Visual audit: all three final pages inspected at 120 dpi; no clipping,
  overlap, broken glyphs, orphaned heading or unreadable table/equation.
- Build sidecars in release package: none.
- `main.pdf == main_round2.pdf`: byte-for-byte PASS.

## SHA-256

```text
main_round0_original.pdf  43badfbf85fc5ee07a41f2fdfc2abe1f3d811df8d60d2f54c4a0873815ced330
main_round1.pdf           f8ed0c0004ed55f77b53f22259626fa4a515033bff769a6e32a3b5eab53e5672
main_round2.pdf           c68b9335dd3b05abca45f6c9c5d0dc5fb40f7ea1b5405f98b6789b968a03b6e7
main.pdf                  c68b9335dd3b05abca45f6c9c5d0dc5fb40f7ea1b5405f98b6789b968a03b6e7
```

The three round hashes are pairwise distinct because rounds 1 and 2 add
substantive boundary/stability and reproducibility/Route-A material,
respectively.  The final hash changed after the minimal `hypertexnames=false`
repair; no theorem or data claim changed.
