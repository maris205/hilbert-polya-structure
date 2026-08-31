# Compile report

- Engine: LuaLaTeX; two passes in each fresh build tree.
- Environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`, and a fixed hexadecimal trailer ID per retained revision.
- Round 0 SHA-256: `333752ccf96062155172a5a7e4e0903b060df49f05fff221a92cd347975dd547`.
- Round 1 SHA-256: `8f941766e6a9dd981bf28972a675e91ea816f2c6b5ea38844b9e7c2371eed920`.
- Round 2/final SHA-256:
  `eaeabde91cd9e40e80222a85e913e0706c1a9d0a548318d09a054b515a928ca3`.
- Two fresh builds of every retained round were byte-identical.  Two further
  fresh final builds were byte-identical to `main.pdf` and
  `main_round2.pdf`.
- Final output: 3 pages, 163,007 bytes, PDF 1.5; 21/21 fonts embedded and
  subset; extractable text present.
- Settled logs: no overfull or underfull boxes, undefined references or
  citations, duplicate destinations, missing assets, rerun requests, or PDF
  backend warnings.
- Visual audit: pages 1–3 rendered at 130 dpi and inspected.  Equations,
  interface cases, proof endings, references, margins, and page breaks are
  complete; the expanded correction bibliography remains legible, and no
  clipping, collision, or orphaned heading was found.

The three round hashes differ and the improvement log records substantive
theorem additions rather than metadata-only changes.
