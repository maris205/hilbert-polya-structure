# Paper improvement log

The manuscript was improved in three genuinely content-distinct rounds. No external reviewer was simulated and no acceptance rate is reported.

## Round 0 — complete theorem draft

The first draft stated the full all-moduli/all-\(m\) theorem, proved the three torsion channels and multipliers, derived the Lefschetz identity and Artin--Mazur zeta, and included the even-Fourier Wold model and Route-A verdict.

Saved PDF SHA-256: `3bcc5e5e7a91eeb59746e05be967906d9ae1b8e753ead4a2f44e14c251114f8d`.

## Round 1 — branch and operator boundary

The second round added a dedicated explanation of why branch classes cannot be merged into either regular channel, clarified the quotient local coordinate and the line-bundle change-of-space issue, strengthened the ownership boundary, and removed missing-glyph warnings in the bilingual abstract.

Saved PDF SHA-256: `990704a10b9f358e738768ee71c7b1ce286a6dcad06ae1ddee18fa55ade0af1b`.

## Round 2 — evidence, gate table, and limitations

The final round added the exact validation census, independent-checker/CAS/mutation totals, a compact gate-by-gate Route-A table, explicit family limitations, a sharper distinction between an observable Wold theorem and a quantization-space change, and the classical/source ownership audit.

Saved and final PDF SHA-256: `ed64388d59e5717f588ec6b750c079eeb3aa99df4879236d2bb18ea3fb6c4a93`.

The final release correction added the exact Route-A v0.2 source-lock semantic gate and its repaired-hash mutation, so the round-2 validation table now reports 43,184 checker assertions and 23+1 mutation rejections. The mathematical theorem and the content-distinct round-0/round-1 snapshots are unchanged.

All three hashes differ. `main.pdf` is byte-identical to `main_round2.pdf` and was reproduced from a clean LuaLaTeX build under the frozen epoch.
