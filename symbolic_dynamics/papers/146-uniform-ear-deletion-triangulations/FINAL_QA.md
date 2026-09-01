# Final QA — P146 uniform ear-deletion triangulations

**Date:** 2026-09-01 UTC.  **Result:** **PASS / GO_INTERNAL OWNER-THIN**.
**External status:** **HOLD_EXTERNAL**.

The final anonymous paper is 3 A4 pages and 345,511 bytes.  Its SHA-256 is
`a0a6145009b4882150489b43fe403a3d76be02725621afa358d678fb3cd02517`;
`main.pdf` and `main_round2.pdf` are byte-identical.  The visibly defective
Round-0 and repaired Round-1 PDFs remain distinct provenance artifacts.

The canonical verifier replays byte for byte with 9,562 exact assertions.  It
enumerates every deletion history through `n=9`, independently computes
unrooted leaf orders, brute-forces bounded rooted extensions, and verifies
normalization and the path equality class.  A source-only build in
`/tmp/p146-final-7X79f2` reproduces the final PDF exactly; the sole pdfTeX
font-expansion ordering notice is deterministic and visually harmless.

All 26/26 font rows pass.  The PDF is A4, rotation zero, unencrypted,
form-free, JavaScript-free, attachment-free, and has blank identifying
metadata.  All 3/3 pages were inspected after the fourth citation was added.
All 4/4 references are cited and resolved.  Text, identity, placeholder,
local-path, and unresolved-reference scans are clean.  The package remains
owner-thin and externally held.
