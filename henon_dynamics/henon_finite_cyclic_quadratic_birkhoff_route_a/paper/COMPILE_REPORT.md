# C161 compile report

- Engine: LuaLaTeX.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`.
- Pass-one SHA-256: `7a99b240ff6e2446a5fd97f42300314c6e9607d10add5ea76a1cab03cd0446b5`.
- Pass-two SHA-256: `7a99b240ff6e2446a5fd97f42300314c6e9607d10add5ea76a1cab03cd0446b5`.
- Deterministic double build: **PASS**.
- Pages: 2.
- The preserved stages are content-distinct:
  - round 0, one page: `55617661e94372c4b6ca627120169541ef8dbdd80cce92630dfb2a3c856ac0f8`;
  - round 1, one page: `5694c3fe6f6a7b91c48d4311f90645ef56e43fd1988c5482f1b0fd0dfac458c7`;
  - round 2, two pages: `7a99b240ff6e2446a5fd97f42300314c6e9607d10add5ea76a1cab03cd0446b5`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Font audit: all fonts reported by `pdffonts` are embedded; the CJK font is
  `DroidSansFallback` and visual inspection shows no missing glyphs.
- Log audit: zero LaTeX warnings, missing characters, undefined references,
  overfull boxes, or underfull boxes in every preserved stage and both final
  release passes.
- Visual audit: both pages inspected; formulas, bilingual abstract, unitary and
  antiunitary identities, Route-A boundary, and declarations are legible and
  unclipped.
