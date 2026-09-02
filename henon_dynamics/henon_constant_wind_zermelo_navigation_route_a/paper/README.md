# C305 paper builds

The source uses `\CRevisionRound` to archive:

- `main_round0_original.pdf`: reachability and value core;
- `main_round1.pdf`: optimizer, HJB, regularity, and complete boundaries;
- `main_round2.pdf`: evidence, hostile audit, collision/scope closure;
- `main.pdf`: byte-identical final round 2.

The release gate runs two fresh, double-pass LuaLaTeX builds for every round
at `SOURCE_DATE_EPOCH=1788393600`, then checks warnings, fonts, pages, text,
rasterization, and exact hashes.
