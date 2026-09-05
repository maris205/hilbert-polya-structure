# Compilation receipt

The release builder uses two fresh directories and two settled LuaLaTeX
passes for each of three revisions at SOURCE_DATE_EPOCH=1788566400.
The nonwrite release verifies fresh PDF equality, embedded/subset fonts,
bilingual abstract and keyword text, all-page rasterization, exact source
membership and the final-copy identity. Actual logs are retained as .txt.
Final page counts and hashes are carried by C385_RELEASE_MANIFEST.json.
The executed round page counts are 2, 3 and 4; the final paper is four pages.
On 2026-09-05 the root reviewer rendered and actually viewed all four final
pages at a 1400-pixel maximum dimension. No clipping, overlap, missing glyph,
unreadable equation or misplaced reference was found. Both language abstracts,
six keywords per language, theorem endings and the final scope paragraph are
visible. This is an internal visual check, not a venue acceptance decision.

Build corrections before the successful run: Latin names in the Chinese font
were assigned an English font; a switching-line sentence was reflowed; and
the strict-route tuple was moved to display math. The settled final logs have
no layout, glyph, unresolved-reference or rerun warnings. Fresh double builds
were byte-identical. The raw compiler logs have not been whitespace-cleaned.

After independent review repaired the standalone checker's two boolean type
gaps, the hostile count changed from 34 to 36 and the final audit paragraph
recorded the correction. All three PDF rounds were rebuilt twice afresh;
the final still has four pages. The root reviewer rendered and actually
viewed all four revised pages again on 2026-09-05. The added paragraph and
updated table are readable, with no new layout or glyph issue.
