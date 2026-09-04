# Compile report

The canonical release build uses LuaLaTeX twice per fresh temporary directory, two fresh directories per round, and `SOURCE_DATE_EPOCH=1788480000` with `FORCE_SOURCE_DATE=1`.

Release acceptance requires:

- byte-identical paired builds for each of rounds 0, 1, and 2;
- a real build through each checked-in `main_round0.tex`, `main_round1.tex`, and `main_round2.tex` wrapper, with strictly increasing page counts;
- no settled LaTeX/package warning, overfull or underfull box, missing character, undefined reference, or rerun request;
- all fonts embedded and subsetted;
- embedded `Droid Sans Fallback` for the Chinese abstract and Chinese keywords;
- clean UTF-8 text extraction with round-specific theorem tokens;
- presence of both abstracts and both five-to-seven-keyword lists, with no later-round theorem leaking into an earlier round;
- successful rasterization of every page;
- `main.pdf` byte-identical to `main_round2.pdf`.

The generated manifest records page counts, font counts, raster sizes, and SHA-256 hashes for all four PDFs.
