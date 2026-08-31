# Paper build

The retained source is `main.tex`; `main.pdf` is byte-identical to
`main_round2.pdf`.  Round 0 contains the frozen SDE, kernel, interface, and
resolvent.  Round 1 adds speed symmetry and the complete exit atlas.  Round 2
adds the occupation law, endpoint faces, certificate, collision boundary, and
strict Route-A verdict; its release revision also incorporates the independent
hostile review of resolvent normalization, cross-references, and the complete
two-item errata chain.

All retained PDFs are built with LuaLaTeX, `SOURCE_DATE_EPOCH=1788048000`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, and fixed trailer IDs.
