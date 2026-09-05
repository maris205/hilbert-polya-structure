# Review A source-only build and actual three-page inspection

2026-09-05 UTC; performed and viewed by `/root/batch197_lzk_gate`.
This is an independent Review A production check, not a terminal paper
acceptance build. The paper is KILL_VALUE despite successful compilation.

## Actual cold invocation

The target directory did not exist before invocation. I read the build
helper completely, then executed from the workspace:

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh \
  /root/autodl-tmp/symbolic_dynamics/papers/204-previous-smaller-distance-feedback/frozen_round0 \
  /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p204_a/cold_build \
  /root/autodl-tmp/symbolic_dynamics/papers/204-previous-smaller-distance-feedback/frozen_round0/main.pdf
```

Exit 0. Complete invocation stdout:

```text
SOURCE_ONLY_BUILD_COMPLETE /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p204_a/cold_build
812ac643316efaacea763a31770f15c59fca9716f7abffb8c355a745d96e6e8a  /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p204_a/cold_build/main.pdf
```

The helper created a fresh staging directory inside this review package,
copied only `main.tex`, `math_commands.tex`, `references.bib`, and the five
section `.tex` files, and started with no `.aux`, `.bbl`, `.pdf` or prior
build products. The expected frozen PDF was used only by the final `cmp`,
not copied into the build inputs. The script's final move put the physical
build at `cold_build/`; no previous build was overwritten.

The eight complete source hashes are in `cold_build/SOURCE_INPUTS.sha256`
and agree with the corresponding immutable Round0 inputs. That manifest's
eight checks were physically rerun afterwards and all returned OK.
The build helper itself is pinned in `SUPPORTING_INPUTS.sha256`.

## Engine, environment and complete logs

The actual fallback sequence was:

```sh
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
```

Every command completed with exit 0: the helper runs them under
`set -euo pipefail`, and reached its final success receipt and expected-PDF
comparison. This was an actual pdfLaTeX/BibTeX fallback, not an invented
`latexmk` call. Complete stdout is preserved in `pass1.stdout`,
`bibtex.stdout`, `pass2.stdout`, and `pass3.stdout`; the full final TeX
log, BibTeX log, recorder `.fls` and all generated products are retained.

- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian.
- BibTeX 0.99d, TeX Live 2022/dev/Debian.
- `SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`.
- Full engine/version notices: `ENGINE.txt`, `BIBTEX_ENGINE.txt`.
- Full settings: `BUILD_ENVIRONMENT.txt`.
- Final log diagnostics: `DIAGNOSTICS.txt`, zero bytes; no final undefined
  reference/citation, warning or overfull-box entry. Earlier first-pass
  unresolved references remain honestly visible in their actual logs.
- Font report: `FONTS.txt`; all 22 listed font resources are embedded
  Type 1, with no unembedded font.
- `PDFINFO.txt`: three A4 pages, 281,200 bytes, blank personal metadata,
  no encryption or JavaScript. Extracted body: `main.txt`.

The PDF digest is
`812ac643316efaacea763a31770f15c59fca9716f7abffb8c355a745d96e6e8a`.
The build helper physically compared this new PDF against frozen Round0
with `cmp`; exit 0 establishes byte identity under these inputs/settings.
This does not claim equivalence from a hash alone.

## Rendering and actual viewing

I executed:

```sh
pdftoppm -png -r 120 \
  docs/papers204_208_sequence/reviews/p204_a/cold_build/main.pdf \
  docs/papers204_208_sequence/reviews/p204_a/views/page
```

Rendering exited 0. I then actually opened **each** of the three resulting
images with the image-view tool, inspecting the complete page. Their
existence and hashes are supporting pins, not the viewing action.

| Page | Actual visible inspection | SHA-256 |
|---|---|---|
| 1 | Title, abstract, strict map, carrier, ties, citation contexts and Lemma 2.1 with its complete proof are readable. No clipping, overlap or missing symbols; footer and keywords clear. | `5731c79bcfe045e9a475daaa560f88b14e76ad64ba00ac62a88a8d6a9313e69d` |
| 2 | Core, local $j$ exchange, Theorem 2.2, sharp-height cases, Fibonacci proof, signed cuts, phase masks and Theorem 3.1 fit cleanly. The fibre cardinality bars and binomial arguments render correctly. | `f96e49f822e8e0d03fd42c02f7167f52c99865ae9bb5bf2ae711ad2b77254cf8` |
| 3 | Full fibre proof continues normally after the page break. Offset example, limitations and all three references are legible, with correct accented publisher text and no overflow. | `5bac384423140623a364939c4d4831e9613ada2e62895a6b26a054c22278e7e6` |

The theorem/proof break between pages 2 and 3 is normal and does not omit
content. Three total pages are below the approved five-total-page cap.
The absence of figures is appropriate for these short complete proofs.
There was no build or visual defect requiring an author source edit.
