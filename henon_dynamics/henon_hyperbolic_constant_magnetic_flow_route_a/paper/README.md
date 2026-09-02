# Manuscript build

`main.tex` is a single audited source with revision switch `CRevisionRound`.  Round 0 contains the core theorem and Lorentz-frame proof; round 1 adds the independent geometric period derivation and completeness analysis; round 2 adds finite evidence, hostile audit, Route-A firewall, limitations, and declarations.

Each archived round is built twice in separate temporary directories, with two LuaLaTeX passes per build under `SOURCE_DATE_EPOCH=1788307200`, and compared byte-for-byte.  `main.pdf` equals `main_round2.pdf`.  The release manifest verifies settled logs, PDF text, pages, and embedded subset fonts.
