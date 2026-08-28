# Compile report

- Engine: LuaHBTeX / LuaLaTeX
- Fixed epoch: `SOURCE_DATE_EPOCH=1787875200`
- Optional metadata suppression: `\pdfvariable suppressoptionalinfo 611`
- Final revision: 2
- Final pages: 3, A4
- Fonts: 14 reported entries; every font embedded and subset
- Log audit: no overfull/underfull boxes, undefined references, multiply
  defined labels or residual warnings
- Text audit: title, global reachable-moment theorem, Route verdict and scope
  literal are extractable
- Revision hashes:
  - round 0: `d7709379b2c6e7d2b53d5689a1ab747be4f1b509486a283ef49523ed0a16414d`
  - round 1: `9702ded9a7e53848250ad59900fe9e259b78d3734be21caad5dee423d476ab25`
  - round 2/final: `7461145393e71f9517e9af55642b1b9f3207981ccc57a2389e5731c540ef16ee`

All three revision hashes differ, and `main.pdf` is byte-identical to
`main_round2.pdf`.  A fresh two-directory deterministic rebuild and visual
inspection are repeated by the batch-level release audit.
