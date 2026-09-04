# Deterministic compile report — HCS-C354

Each revision was compiled twice in separate fresh directories by LuaLaTeX
with SOURCE_DATE_EPOCH 1788393600. The paired bytes were identical. Settled
logs had zero package/LaTeX/PDF-backend, layout, reference, citation, rerun, or missing
character warnings. All fonts are embedded and subset; every page passed
pdftotext and pdftoppm checks.

| round | pages | font rows | SHA-256 | bytes |
|---:|---:|---:|---|---:|
| 0 | 1 | 10 | f21fb61812199c94f3ba16636d23c82c403d92d3edfc333f75d19e27c7a4d5dd | 42747 |
| 1 | 2 | 10 | 928b69e0b0965b671ca945564d4c578294c52e500e24aa90d24a7615f670e88e | 51356 |
| 2 | 2 | 12 | ad71ed25f9c2b67bd14eeadaa194b1623eeeef4149bb26e764dd12372528e564 | 68775 |

main.pdf is byte-identical to round 2.
