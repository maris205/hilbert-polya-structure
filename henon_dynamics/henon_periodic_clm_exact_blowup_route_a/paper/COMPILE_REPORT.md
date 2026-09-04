# Compile report

The release builder invokes LuaLaTeX twice for each fresh build, two fresh builds per revision round, with `SOURCE_DATE_EPOCH=1788480000` and `FORCE_SOURCE_DATE=1`.

Acceptance requires identical paired bytes from each checked-in wrapper, strictly increasing page counts, no settled LaTeX/package warning, no overfull or underfull box, no missing character, no undefined reference or rerun request, fully embedded and subsetted Latin/CJK fonts, clean text extraction with one English and one Chinese abstract, two keyword lists of five to seven entries, correct round-specific theorem inclusion with no future-round leakage, and successful page rasterization. The manifest records every PDF hash, page count, font count, and raster-size vector.
