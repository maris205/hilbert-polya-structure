# Compile report: HCS-C358

The three revision products are compiled from `main.tex` with LuaLaTeX at the
fixed epoch `1788393600`.  Each checked PDF must match two independent fresh
two-pass builds.  The final release audit requires:

- Round 0: 2 pages, 17 font rows, SHA-256
  `64afe095dc1001253674fc8cbf00445fe4470e517ebe6356bb2132a49e07c544`;
- Round 1: 3 pages, 17 font rows, SHA-256
  `f1138767a82ccb27a5a23250a93cdf00271acc007c5b56ab7f037f34c553c8ad`;
- Round 2/final: 4 pages, 17 font rows, SHA-256
  `693e6daa517116887ecd5315f826b773ca43011592517e57a84a03320ad1740f`;

- three distinct revision digests and `main.pdf == main_round2.pdf`;
- no LaTeX/package/PDF-backend warning, overfull/underfull box, undefined reference,
  rerun request, or missing character in the settled log;
- all fonts embedded and subset;
- UTF-8-decodable extracted text with no control or draft tokens;
- successful rasterization of every page.

The exact PDF digests, byte sizes, page counts, font rows and raster receipts
are content-addressed in `C358_RELEASE_MANIFEST.json` after the release write.
