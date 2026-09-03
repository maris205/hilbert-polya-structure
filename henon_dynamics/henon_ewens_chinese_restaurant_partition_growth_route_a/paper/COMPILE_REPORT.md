# Compile report

LuaLaTeX built every conditional revision twice in clean temporary directories with `SOURCE_DATE_EPOCH=1788393600`.  Paired builds were byte-identical, and the final logs contained no layout, citation, reference, rerun, or missing-character warnings.

- Round 0: 2 pages, 107,788 bytes, SHA-256 `41c16a138ff09d0f21c95420569e087d1b491ad3747f5f230da8e3d0946a96b1`.
- Round 1: 2 pages, 130,419 bytes, SHA-256 `73e6df231c336ac74512d362157936f732e055e375464c2b8f83a2fe223b46ca`.
- Round 2/final: 3 pages, 148,982 bytes, SHA-256 `4a036ef295873af816d9bf73a9719cae20aafc38c7d7f06df7a0604cbda6a0e1`.

All three revision hashes are distinct and `main.pdf` is byte-identical to round 2.  Every font is embedded and subset; text extraction passes the control/draft-token checks, and all pages rasterize nontrivially.
