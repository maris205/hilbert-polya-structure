# Actual pre-review build and page inspection

2026-09-05 UTC; inspected by root. This is Round0 production evidence, not
either independent review or either terminal build.

The first source-only attempt failed with exit 1 because `Seg` and `Fix`
were passed as unescaped operator command names. Original failed logs and
inputs remain under `qa_round0/attempt1/.build.EbWWmE/`; they were not
rewritten. The two live macro declarations were corrected before a new
physical source-only build in `qa_round0/attempt2/cold_build/`.

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/204-previous-smaller-distance-feedback /root/autodl-tmp/symbolic_dynamics/papers/204-previous-smaller-distance-feedback/qa_round0/attempt2/cold_build
pdftoppm -png -r 120 papers/204-previous-smaller-distance-feedback/qa_round0/attempt2/cold_build/main.pdf papers/204-previous-smaller-distance-feedback/qa_round0/attempt2/views/page
```

Build and rendering exited zero. `latexmk` is unavailable; the scoped build
script performs the actual pdflatex/BibTeX/pdflatex/pdflatex fallback.
Engine versions, source input hashes, environment, complete pass logs,
font table, PDF metadata and digest remain in the build directory.
The final diagnostic file is empty. All listed fonts are embedded Type 1;
there are no undefined references/citations or overfull boxes in the final log.
The PDF is three A4 pages, below the five-total-page cap, with blank personal
metadata. SHA-256:
`812ac643316efaacea763a31770f15c59fca9716f7abffb8c355a745d96e6e8a`.

Root actually opened all three rendered page images, not just their hashes:

| Page | Visible inspection |
|---|---|
| 1 | Title/abstract, literal strict map and tie example, first-image lemma/proof; no clipping or overlap. |
| 2 | Core definition, exact endpoint, height and Fibonacci proofs, fibre statement; equations and footer are readable. |
| 3 | Complete fibre proof, flagged example, limitations and all three references; no missing glyphs or overflow. |

The split between Theorem 3.1 and its proof is a normal page break. No figure
is needed. Three pages are sufficient for these complete proofs; no padding
was added merely to reach the approximate four-page plan.
