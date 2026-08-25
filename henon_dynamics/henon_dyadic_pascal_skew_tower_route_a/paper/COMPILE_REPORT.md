# C166 compile report

- Engine: LuaLaTeX.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, with
  `FORCE_SOURCE_DATE=1` and `TZ=UTC`.
- Final pass-one SHA-256:
  `1f1d7620b8e734f6bf3a866f3357e5d77aee4991c35c4144597548894627d8e1`.
- Final pass-two SHA-256:
  `1f1d7620b8e734f6bf3a866f3357e5d77aee4991c35c4144597548894627d8e1`.
- Deterministic double build: **PASS**.
- Pages: 2, A4.
- Preserved content-distinct stages:
  - round 0, one page:
    `b48ed71de6aba06fb873ad8b818ca4eedaa5b9fb5b68edfb904fe0dcf23aa1d2`;
  - round 1, two pages:
    `f601385d52faa45f1cb55acbe2c083e1423fb7333db2a726b321edd9901f3318`;
  - round 2, two pages:
    `1f1d7620b8e734f6bf3a866f3357e5d77aee4991c35c4144597548894627d8e1`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Font audit: every font reported by `pdffonts` is embedded; the Chinese font
  is `DroidSansFallback`.
- Log audit: every preserved stage and both final passes contain zero LaTeX
  warnings, missing characters, undefined references, overfull boxes,
  underfull boxes, or multiply defined labels.
- Visual audit: both final pages were rendered at 120 dpi and inspected.  The
  English and Chinese abstracts, all eleven displayed identities, valuation
  witness, scope statement, and declarations are legible and unclipped; there
  is no blank page, collision, truncation, malformed formula, or missing glyph.
- The post-round hostile repair makes the valuation domain explicit and the
  fresh empty-directory double build above is the released byte sequence.
- Build logs and auxiliary files were removed after this audit.
