# C420 first manuscript-review response and actual revision

2026-09-08 UTC. The coordinator fully read the 307-line
[first full-manuscript review](../../manuscript_reviews/round1/C420_REVIEW.md),
SHA256 9341ffdac67227001e4615f4019404a00b996650bdf722a651d578e2078844a4.
It is PASS, zero mandatory findings. Two optional improvements are adopted;
the third is declined with the review's express permission.

O1: Section 8 now uses stage-neutral language saying that formal review,
release and reproducibility records are maintained separately from the
mathematical claims. AI assistance and the absence of human peer review,
editorial decision and worldwide-priority certification remain explicit.
No unfinished gate is asserted complete in the manuscript.

O2: The Section 7 opening reference uses capitalized Cref rather than cref.
It now begins “Table 4”. No reference target, formula or theorem changed.

O3: Retain the readable bibliography with its short final page. There is no
page quota, and the complete seven-entry bibliography is useful. No source,
proof or font size is removed or compressed just to eliminate that page.

Only paper/sections/7_boundary_levels.tex and paper/sections/8_scope.tex
changed, with respective SHA256 values:

    33d913a4377193b23dc242f6e7ed26d7ba279ef5495f08c4e43b1b64bd72a73f
    86dcfa03cc35503071d3a1aab238bfdf3f47e10c7843084ae770d653c94f1286

All thirteen old input files and the original PDF remain preserved in
builds/baseline_polished/. The unchanged inspected build.sh was run as
“bash build.sh round1”; it refused to reuse an existing directory and
created a complete thirteen-input snapshot and source manifest before
compiling. Four deterministic environment settings are the same as those
in COMPILE_REPORT.md. Actual exit: 0. Full console and final logs are in
builds/round1/, together with actual environment, fonts, text and metadata.

The actual [revised PDF](builds/round1/main.pdf) has 18 pages and
428401 bytes, SHA256
9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512.
The new thirteen-input manifest SHA256 is
ba887f152fc9fe7ca9e69cf74f14a96332bcf04c998f6352786358a65acc147e.
Final main.log/main.blg scans have no warning, overfull, underfull,
undefined or error matches. No mathematical program or new source request
was executed. An initial multi-file patch failed its expected-text check
and applied no C420 changes; the corrected patch produced the two edits
above. This was not a failed mathematical test or compiler invocation.

Second full-manuscript review and final same-input fresh build pair,
all-final-page visual inspection, formal evaluation and release remain.
Neither the earlier proof review nor this response substitutes for them.
