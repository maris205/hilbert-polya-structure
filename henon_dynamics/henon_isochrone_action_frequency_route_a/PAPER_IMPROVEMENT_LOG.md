# Paper improvement log

## Round 0 — core theorem

The initial complete manuscript fixes \(\ell=|L|\), proves the unique circular/central minimum, derives the quadratic turning-point reduction, evaluates the radial period, integrates the action, and states the exact bound domain.  It already separates all-parameter proof from finite regression evidence.

## Round 1 — closure and boundary audit

The first substantive revision adds the independent apsidal integral, derives the action-frequency ratio, and proves the rational closure criterion for noncircular \(\ell>0\) motion.  It then repairs the three most dangerous statement-level ambiguities: circles are closed without a rationality condition; nonstationary \(L=0\) motion has full Cartesian period \(2T_r\); and negative \(L\) reverses angular frequency without changing radial geometry.  Escape and the singular Kepler collision corner are also made explicit.

## Round 2 — evidence and claim boundary

The second substantive revision adds the 116-cell exact certificate, direct 90-digit quadratures, independent SymPy checks, strict duplicate-rejecting JSON/YAML validation, fresh-path replay, and hostile mutations.  It proves the natural bounded-potential Schrödinger realization but refuses a target spectral upgrade.  Route-A reasons, source ownership, nonclaims, data/code statements, conflicts, funding, contributor roles, ethics, and AI-use disclosure are included.

## Release checks

All three rounds are compiled twice from isolated directories with `SOURCE_DATE_EPOCH=1788307200`, two LuaLaTeX passes per build, a settled warning scan, embedded/subset font checks, text sentinels, raster rendering, and byte comparison.  Exact round hashes, pages, and font-row counts are recorded in `paper/COMPILE_REPORT.md` after the builds and rechecked by the release manifest.
