# Compilation report

- Engine: LuaLaTeX / LuaHBTeX 1.14.0 in two independent fresh temporary trees
  per retained revision.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1,
  TZ=UTC.  The LuaTeX trailer ID is fixed in `main.tex`.
- Round 0 used two convergence passes per fresh tree; rounds 1 and 2 used
  three.  The two fresh builds of every round were byte-identical.
- The retained PDFs each have 2 pages and pairwise distinct
  SHA-256 values:
  `bdc2516eb436d16a5bb88b3d7663e0a0047c66db306832bc281021046486b139`,
  `1dd3cf5b8800b2bf7bf1602bc315cc5e88476270a3bb5976f50a8dd95da1acaf`,
  and `15e020b8c67721fbd22a1a85943eedee4b60c0c9c4a1c1423abefffb47c43946`.
  `main.pdf` equals the final hash byte-for-byte.
- The settled build has no layout, citation, reference, destination, or rerun
  warning.  Text extraction passes; every listed font is embedded and
  subset.  All three rendered pages were visually inspected.
