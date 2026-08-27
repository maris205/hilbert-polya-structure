# C200 compile report

The final manuscript is built twice with LuaLaTeX under a fixed epoch.  The
release audit verifies three distinct revision hashes, `main.pdf == round2`,
byte-identical fresh final builds, embedded fonts, extractable English and
Chinese text, no warnings/bad boxes, and visual inspection of every page.

Final PDF size, page count and hashes are recorded in the self-excluded release
manifest, avoiding a self-referential rebuild cycle.
