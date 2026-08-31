# Compilation report

- Engine: LuaLaTeX, two passes per fresh build.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1, TZ=UTC.
- Every revision was built twice in a fresh temporary directory, with two
  LuaLaTeX passes per build.  Each same-source pair was byte-identical.
- Round-0 SHA-256:
  `e8ae74216e0fdddd7ce7e043ca9f1b08e857b9d76edff00a8b2ca22eb85fab1c`.
- Round-1 SHA-256:
  `4c1e9071d1a2f7109ebe68e5b7ad5dda92117fe9b5a042b7717d63109c1817ac`.
- Round-2/final SHA-256:
  `b5cf728e479ac429e44f424a23fb8e3f7fd15ef461966fbce61e352b9eecb585`.
- The hashes are pairwise different and `main.pdf == main_round2.pdf`.
- The final PDF has two pages and 20 embedded/subset font entries.  The settled
  log has no layout, reference, citation or rerun warning.
- Both rendered pages were inspected at 120 dpi: equations, theorem endings,
  boundary table, scope tuple and bibliography are visible without clipping or
  collision.  Text extraction includes all required scope and Route-A tokens.
