# Compile report

- Engine: LuaLaTeX, two passes per artifact.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787788800`.
- Pages: 3; final bytes: 244591; extractable words: 1191.
- Round 0 SHA-256: `fe08600335ac8ddbcf84cbba3df26f32396e2d5a5b0670f465eabec8359f6a07`.
- Round 1 SHA-256: `c3f45be643c49adc61bdeb01c00b13b6f1a1b136916c7829b91bf97ad08502f8`.
- Round 2/final SHA-256: `203531a0984884266508021d163ed6a5d03b651919698f34b140495b939c4986`.
- Three round hashes are distinct; `main.pdf` equals round 2.
- Two independent-directory final builds are byte-identical to the release PDF.
- `pdffonts`: every font embedded and subset.
- `pdftotext`: theorem, declarations, AI disclosure, and exact scope literal
  extract successfully.
- All round logs: no warning, error, overfull, underfull, undefined-reference,
  or rerun request.  Visual inspection: PASS.
