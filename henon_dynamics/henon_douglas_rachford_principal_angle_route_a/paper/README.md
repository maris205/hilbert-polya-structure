# Build C197 paper

Run LuaLaTeX twice with a fixed `SOURCE_DATE_EPOCH` after selecting the revision
round through `\CRevisionRound`.  Round PDFs 0, 1 and 2 preserve substantive
manuscript stages; `main.pdf` is the round-2 release.  Build sidecars are not
release payloads.

The final release audit checks SHA-256 reproducibility, embedded fonts with
`pdffonts`, metadata/page count with `pdfinfo`, extractable text with
`pdftotext`, log warnings and bad boxes, and rendered images of every page.
