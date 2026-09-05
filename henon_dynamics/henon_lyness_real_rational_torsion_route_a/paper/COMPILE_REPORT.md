# Actual deterministic compilation and visual audit

Engine: LuaLaTeX; fixed SOURCE_DATE_EPOCH=1788566400 and FORCE_SOURCE_DATE=1.
Each round was compiled twice to settle references in each of two distinct
fresh directories. Each pair of PDF byte streams was identical.

| Round | Pages | Embedded subset fonts | PDF SHA256 |
|---|---:|---:|---|
| Zero | 3 | 9 | 29bc7b501f4c6b4b0a57043365a8df60ea611c802b4c58665a5126cb689fcc09 |
| One | 4 | 9 | 7270c29deabc542e176f83ca59da4cafb7d496bb37713e1610d5b022aeb33bfc |
| Two / main | 5 | 9 | 398163e43de109d0ff0f5f06534e6d78600562c5d978eb428cef76f0f7f7b2c4 |

All three settled logs are retained verbatim as compile_round0.txt,
compile_round1.txt and compile_round2.txt. Final settled warnings: zero
overfull/underfull boxes, undefined references, undefined citations,
missing characters, font-shape substitutions and package warnings.
English/Chinese abstracts, exactly six keywords per language, round
markers and substantive section presence were checked by PDF text extraction.
Poppler rasterization produced exactly the declared page count in each round.
main.pdf equals main_round2.pdf byte for byte.

Actual image inspection: all five final pages were opened with view_image
at 90 dpi from /tmp/c390-final-pages-nxGitH/page-[1-5].png. Page 1 title,
abstracts and keyword lines are legible; page 2 oval and return formulas
are complete; page 3 the discriminant, elliptic translation and nine-cycle
are not cropped; page 4 the prime-period and Koopman proofs remain readable;
page 5 the scope paragraph and bibliography are complete. No missing glyph,
clipping, overlap or detached negation was observed. The whole final scope
and “Route B remains disabled” occur together on page 5. Temporary raster
images are diagnostic files outside the publication payload.

During initial layout checks, overlong Chinese source lines and an unsupported
bold CJK request were corrected. The evaluator tuple was given its own
paragraph to remove an overfull line. No warning was hidden or relabeled
as a successful check; the retained logs are the settled corrected runs.
This is a standalone mathematical article, not a conference submission
or acceptance claim.
