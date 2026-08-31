# Compilation report

- Engine: LuaLaTeX; two passes per fresh build.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1, TZ=UTC.
- Every revision was built twice in a fresh directory with two passes; each
  same-source pair is byte-identical.
- Round-0 SHA-256:
  `d687648e5f50a3a7deda98d4a658ebd9597f278743df56035c1c9afc2d7ab4d4`.
- Round-1 SHA-256:
  `e7b88bcc9fbd32b0b2406601300b9f65619ccfd22b7b804f861b032d96b48a12`.
- Round-2/final SHA-256:
  `e6a7a93d3528e4d685c5bbd5c79592a73268c2d027041ae80f8ffb5b820a3e81`.
- The three hashes are distinct and `main.pdf == main_round2.pdf`.
- The final PDF has two pages and 18 embedded/subset font entries.  The settled
  log has no layout, reference, citation or rerun warning.
- Both pages were inspected at 120 dpi.  The inertia matrix, two heteroclinic
  charts, endpoint/period formula, clean-family statement, Poisson bracket,
  boundary table, strict tuple and bibliography are unclipped and legible.
