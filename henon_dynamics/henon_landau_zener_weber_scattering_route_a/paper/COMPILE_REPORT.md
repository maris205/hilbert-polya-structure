# Compilation report

The final manuscript was compiled with LuaLaTeX from a clean temporary build
directory at fixed `SOURCE_DATE_EPOCH=1787875200`.  Two consecutive builds
were byte-identical after sidecar removal.  `pdfinfo` reports 3 pages and
`pdffonts` reports embedded subset Latin Modern fonts.  Text extraction was
checked for the model, Weber reduction, `P_diabatic`, Route-A tuple,
`ROUTE_A_REJECTED`, and the scope literal.  No overfull boxes or unresolved
references remain in the final build log.

The three revision PDFs are content-distinct; the release manifest records
their SHA-256 digests and verifies `main.pdf == main_round2.pdf`.
