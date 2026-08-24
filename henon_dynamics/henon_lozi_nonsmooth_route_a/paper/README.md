# Paper artifact — C116

Compile `main.tex` with `SOURCE_DATE_EPOCH=0` and `TZ=UTC`.  The release audit
uses two isolated build directories, compares SHA-256 digests, verifies page
count and embedded fonts, and scans the final log for layout/reference
warnings.  `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` preserve the two substantive improvement stages.
