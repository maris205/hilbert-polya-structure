# C315 compile report

All three revisions are compiled by LuaLaTeX in isolated directories with
two settled passes, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`,
and `TZ=UTC`.  Round 1 adds one-carrier scattering, explicit first
inverse-time coefficients and sharp parameter boundaries; Round 2 adds
evidence, collision and Route-A audits.

The release manifest records final page, font and SHA-256 data.  Settled
logs must be free of layout, reference, citation, rerun and missing-character
warnings; every font row must be embedded and subset, and every page must
rasterize.
