# C309 compile report

The three retained revisions are built with LuaLaTeX, two settled passes,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC` in
isolated directories.  The release verifier rebuilds each round twice and
requires byte identity with its archive; `main.pdf` aliases Round 2.

Final page/font counts and SHA-256 values are recorded after deterministic
closure in `C309_RELEASE_MANIFEST.json`.  Settled logs must contain no layout,
reference, citation, rerun, destination, or missing-character warning; every
font row must be embedded and subset, and every page must rasterize.
