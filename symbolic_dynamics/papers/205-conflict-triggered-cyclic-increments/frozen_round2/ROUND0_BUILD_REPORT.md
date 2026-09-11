# Actual Round0 production build and all-page inspection

2026-09-05 UTC; root. This is pre-review production evidence, not either
manuscript review or either required terminal build.

Three physical source-only builds were run. Attempt 1 succeeded at four
pages; root viewed all four and found the final page contained only the last
reference. Attempt 2 shortened repeated scope prose and numbered equations
by section; it still had four pages. Root viewed pages 1–3 of attempt 2,
not its fourth page, so no full-view acceptance is claimed for that attempt.
Attempt 3 shortened repeated introductory caveats/roadmap without changing
any theorem, proof or verifier. It succeeded at three pages. All earlier
build inputs/logs/PDFs remain unchanged; none was retroactively called a failure.

Actual final pre-review commands, working directory the workspace root:

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/qa_round0/attempt3/cold_build
pdftoppm -png -r 120 papers/205-conflict-triggered-cyclic-increments/qa_round0/attempt3/cold_build/main.pdf papers/205-conflict-triggered-cyclic-increments/qa_round0/attempt3/views/page
```

Build and render exited zero. With latexmk unavailable, the established
paper-compile fallback actually ran pdflatex/BibTeX/pdflatex/pdflatex.
Engine versions, reproducible environment, source pins, full logs, fonts,
metadata and PDF digest remain in the build directory. Its final diagnostic
file is empty: no undefined reference/citation, overfull box or warning.
The fonts are embedded Type 1, with blank author/personal PDF metadata.
The successful three-page PDF SHA256 is
`f4aec5af74f6ab4a78e1120270e818f20b412694d9d7938145564b9b447e41cc`.

Root then actually opened all three attempt-3 page images:

| Page | What was visibly inspected |
|---|---|
| 1 | Title/abstract, literal update, all source contexts, distance definition and first theorem/iterate formula; no clipped or overlapping content. |
| 2 | Temporal theorem continuation and complete proof, all three decoder conditions and complete converse, static bound introduction; equations/readability intact. |
| 3 | Complete static support proof and all boundary values, dynamic maximum/equality proof, limits/actual check scope and all four references; no orphan reference page or overflow. |

Ordinary page breaks split Theorem 2.1 and Lemma 3.2 from continuations;
no proof is omitted. All included section files exist, all citations resolve,
and no TODO/FIXME/VERIFY marker occurs in the scientific source.
Three pages meet the five-total-page ceiling; no padding is added.
