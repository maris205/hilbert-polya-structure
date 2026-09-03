# Compile report

LuaLaTeX compiled revision rounds 0, 1 and 2 twice each in distinct fresh
directories with SOURCE_DATE_EPOCH=1788393600, a fixed trailer ID and two
passes per build. Both builds of every round were byte-identical.

| Round | Pages | SHA-256 |
|---|---:|---|
| 0 | 2 | 97ba22907b30ed8be4e2addd35b93fd948329f3c8236cc4f77fdc7cee7a2ff95 |
| 1 | 2 | 492bda718671e78f029054487dd8bc51c17cb2f489b9def0d72f37254530180f |
| 2 | 2 | 73435d91fbbdd8b8d6b9abe61b60cab01dba7bd9c457d0089d04638d9f5abec1 |

main.pdf is byte-identical to round 2. Settled logs contain no warnings,
overfull/underfull boxes, undefined references or missing characters.
pdffonts reports 21 font rows, all embedded and subset. pdftotext passes
the control-byte and drafting-sentinel gate; both pages pass pdftoppm
rasterization and visual inspection.
