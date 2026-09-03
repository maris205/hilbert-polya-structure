# Superseded P179 QA receipts

These directories are retained as historical build evidence and are not part
of the final QA count.

- `round1_cold_build_{1,2}` reproduce the accepted Round-1 source
  (`main.tex` SHA-256 `cb7886a6846a4a8019c6636f77bbe9faa5cd8fbc342bbde6c822d57286938b7b`)
  and PDF
  `9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d`.
- `intermediate_round2_cold_build_{1,2}` and
  `intermediate_round2_raster` record the first singleton-residual repair
  before a grammatical typo in the lemma was removed; that intermediate PDF
  has SHA-256
  `e4e193a7f94663aec649d26f128847dfe09057bd406a95896c9d90fcb9bb1b43`.
- `round1_raster` is the corresponding Round-1 visual receipt.

Only `../qa_final/cold_build_{1,2}` and `../qa_final/raster` count toward the
final Round-2 gate.  They bind the final source hash
`94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6`
and final PDF hash
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.
All external action remains `HOLD_EXTERNAL`.
