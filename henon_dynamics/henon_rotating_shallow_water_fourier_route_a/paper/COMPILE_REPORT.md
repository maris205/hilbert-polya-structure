# Compile report

Build epoch: SOURCE_DATE_EPOCH=1787788800; engine: LuaTeX 1.14.0; paper size:
A4.  The three revision artifacts were compiled in two settled passes, then
round 2 was rebuilt twice in a clean temporary directory.  Hashes, page count,
font embedding, extracted-text phrases, and visual renders are recorded in
the C217 release manifest.  Logs and auxiliary sidecars are deliberately
excluded from the 27-payload closure.

| artifact | pages | SHA-256 |
|---|---:|---|
| main_round0_original.pdf | 3 | b745d4cb521d3afd6b4d15bb9645a210f285d3458a281c1fa4725a3a47abfeab |
| main_round1.pdf | 3 | 08083796a2b7f482078cc8952d85c6253d0f620ee0658c7df83b56bc44284f88 |
| main_round2.pdf | 3 | de12b191d81c6d12fe1c58800cfcc9c95481d69d8d47dfea636d74036177c7d1 |
| main.pdf | 3 | de12b191d81c6d12fe1c58800cfcc9c95481d69d8d47dfea636d74036177c7d1 |

The two clean fixed-epoch round-2 rebuilds both returned the final hash.
The settled second-pass logs contained no overfull, underfull, undefined
reference, or missing-character records; all fonts were embedded and subset.
