# Compile report

- Engine: LuaLaTeX, two passes per artifact.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787788800`.
- Pages: 2; final bytes: 261852; extractable words: 801.
- Round 0 SHA-256: `85a289970b446949b6d4bd68a7b404e1c3125c8e0e7eeb1c69a3d44f81e4fca9`.
- Round 1 SHA-256: `3b5c87a9e459d48bd349c4c8aac0bee885c5e6dc5a04754d1904f5d9b846c3d8`.
- Round 2/final SHA-256: `336d039d320202a36f7c3c64af1c6bc7a058431575b8ce4e78336d2e5016a38a`.
- Three round hashes are distinct; `main.pdf` equals round 2.
- Two independent-directory final builds are byte-identical to the release PDF.
- `pdffonts`: every font embedded and subset.
- `pdftotext`: theorem, declarations, AI disclosure, and exact scope literal
  extract successfully.
- All round logs: no warning, error, overfull, underfull, undefined-reference,
  or rerun request.  Visual inspection: PASS.
