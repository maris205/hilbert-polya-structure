# P206 — Round0 source-only build and all-page inspection

2026-09-05 UTC. **BUILD PASS / FOUR PAGES ACTUALLY VIEWED**.
Two physical source-only builds exist in qa_round0/attempt1/cold_build
and attempt2/cold_build. No failed compiler attempt or manuscript repair
occurred. The second was an explicit fresh closure check, not a replacement
for a hidden failure. Neither is a future terminal Round2 build.

Root read the helper and actually executed the second build as follows:

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/206-ternary-cyclic-record-feedback /root/autodl-tmp/symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/cold_build /root/autodl-tmp/symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/qa_round0/attempt1/cold_build/main.pdf > papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/build.stdout 2> papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/build.stderr
```

Actual helper and PDF raw comparison exit: zero. The helper copies only
the eight TeX/bibliography source files into a fresh mktemp directory, never
PDF/auxiliary/bbl input. latexmk is unavailable; the recorded fallback is
pdflatex, BibTeX, pdflatex, pdflatex, all success-checked. The complete
pass logs, source hashes, recorder file, environment, engine versions and
font/PDF reports are retained in each cold_build directory.

Settings: SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, TZ=UTC,
LC_ALL=C; pdfTeX 1.40.22 (TeX Live 2022/dev/Debian), BibTeX 0.99d.
The second built PDF was copied to live main.pdf after successful comparison.
It is 267,983 bytes, four A4 pages, SHA256
`fe69210f090939d0a0b1f284811d25a5b81c711e7d7359d11116cc1e1f11793b`.
Final DIAGNOSTICS.txt and stderr are empty. All listed fonts are embedded;
personal/title/creator/producer metadata are blank. All two bibliography
entries resolve, with no missing section or placeholder. Four total pages
meet the five-page plan including references.

Root actually opened ALL four complete page images in
qa_round0/attempt1/views/. The second PDF is raw-byte identical to that
rendered PDF, so this viewing is reused for the identical second build,
not falsely labelled a second rendering or a new terminal view.

| Page | Actual content inspected | Result |
|---|---|---|
| 1 | Anonymous title/abstract, literal cyclic map, prior-work deduction, both image sets and full temporal statement | Readable, no clipping or overlap |
| 2 | Complete image/reflection/sharpness proof, count corollary/matrices, run definition and inverse theorem/proof start | All formulas and continuity intact |
| 3 | Complete run decoder, J formula, maximum theorem/all equality proof, scope and check description | No omitted proof, readable margins |
| 4 | Final verification-count sentence and both complete references | Short final page, no truncation or unresolved citation |

The reference spill is ordinary pagination; no theorem proof is relegated
to an appendix. Image pins in order are:

```text
41cf1872ddc109d7fa57abc11500fd4e0378d51a6ab64ad5414b54024bc48c37
8f1076b4a3b4fbfc5d4b90cf4d3326011b167fd5feb8604f4607005b9a883edf
a31bdb6ee8b5fdf7d1610c36eb64366fb35202e91b237746a1133934694c11a9
fe98fa0c417a0483a91e6fc0290d0c142bb52f8e323a728e6f06841b9993238b
```

This is source/build/view evidence, not manuscript review or a novelty
certificate. HOLD_EXTERNAL and both future review/delta obligations remain.
