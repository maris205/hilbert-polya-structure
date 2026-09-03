# Compile Report

- Engine: LuaLaTeX.
- Fixed SOURCE_DATE_EPOCH: 1788393600.
- Each of rounds 0, 1, and 2 is compiled twice in separate fresh temporary
  directories.
- Checked-in round PDFs:
  - round 0: 1 page, 114,929 bytes, 17 embedded/subset font rows,
    SHA-256 60b895f99347cee0210c587d84620cd8ff22760391b25701fa58e3fcbc8c3d8a;
  - round 1: 2 pages, 135,779 bytes, 18 embedded/subset font rows,
    SHA-256 15a3a957f7ce1bacdb77a72fce4d1ae16f337e964aceda6c082e39d431bab8d2;
  - round 2: 3 pages, 158,451 bytes, 20 embedded/subset font rows,
    SHA-256 337274ebdc30ed4ef1a06977b235b258eb0979117284c8f375c0fd65e9c6fe79.
- Final main.pdf: byte-identical to round 2.
- Settled logs: no LaTeX/package warning, overfull/underfull box,
  undefined reference/citation, rerun request, or missing glyph.
- Font embedding/subsetting, extracted-text sentinel scan, and per-page
  pdftoppm rasterization: PASS for every round and page.
- Release manifest: 27 payload files plus the self-excluded manifest,
  totaling 28 physical files.
