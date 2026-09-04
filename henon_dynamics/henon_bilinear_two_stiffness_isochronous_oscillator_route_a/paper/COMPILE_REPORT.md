# Deterministic compile report — HCS-C357

Each revision was compiled twice in separate fresh directories by LuaLaTeX
with SOURCE_DATE_EPOCH 1788393600. The paired bytes were identical. Settled
logs had zero package/LaTeX/PDF-backend, layout, reference, citation, rerun, or missing
character warnings. All fonts are embedded and subset; every page passed
pdftotext and pdftoppm checks.

| round | pages | font rows | SHA-256 | bytes |
|---:|---:|---:|---|---:|
| 0 | 1 | 10 | d9a12c6c10cea772467229dfb8bb396e050aa1c2edacc5d3fa43f269aba7ef71 | 40745 |
| 1 | 1 | 10 | f2412afc55bcf68e8e78eaf965a43e2124a10a9a6eb972c7d09050939dc2df44 | 45294 |
| 2 | 2 | 12 | 0529550d840cbf4226a1a1c7ed4aa813aa63f89107df738926ae73eebfd8cc50 | 63416 |

main.pdf is byte-identical to round 2.
