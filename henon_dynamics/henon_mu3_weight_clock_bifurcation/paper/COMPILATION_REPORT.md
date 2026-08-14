# HCS-C51 paper compilation report

Status: **PASS (preliminary document freeze; final machine provenance pending)**

## Build

- Working directory: `paper/`
- Command: `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Exit status: 0
- Compiler: pdfTeX 1.40.22 through latexmk 4.76
- Output: `main.pdf`
- Pages: 15
- Bytes: 384062
- SHA-256: `7957f38aa779a3c2708e1a5bccf0b83d6759d6889412b5175069e5afa13ff89b`

The final `main.log` and `main.blg` contain no undefined citation or
reference, rerun request, overfull box, underfull box, or warning.  The only
textual match for `Rerun` is the package-identification line for
`rerunfilecheck`, not a diagnostic.

## PDF checks

- `pdfinfo`: A4, 15 pages, unencrypted, PDF 1.5.
- `pdffonts`: every listed font is embedded and subsetted.
- `pdftotext`: exit status 0; 1208 lines and 33630 bytes extracted.
- Visual inspection: pages 1, 11, and 15 render cleanly, covering the
  title/abstract, C52 and Route-A discussion, and final bibliography page.

## Frozen paper-source hashes

| File | SHA-256 |
|---|---|
| `main.tex` | `6b1d6479fcf4ddada6f16bc99f9e0a694824c60c282f9658f112c4ae5730fa5e` |
| `math_commands.tex` | `f8db8121db22e2eee30a17d21fef9e4a6aa56d6fd5e93bf063c68838d15938df` |
| `references.bib` | `3c70fd1ba2cc7d398f4bb95ad12c0e5000e63fe602b27ec32ad18af7e766ccf1` |
| `sections/0_abstract.tex` | `f287920a0defa7fc096d2cd9e82db5437c642702ed0c329e2cf9a6ef617d2747` |
| `sections/1_introduction.tex` | `a8c2b8115e40e754151c5b5e86b445b4df359f67347e4284a63ba9893977b94f` |
| `sections/2_source_and_main.tex` | `ee5d790484a9f61d5a7ba9f2259f3a44141b87f80784f5924de70b0e139ae1b9` |
| `sections/3_two_weight_rank.tex` | `faa493893ae2efc66f1d6bc96489ad85e2f50b3e027299d912c6f7d3b28dc993` |
| `sections/4_log_l_extraction.tex` | `d98f127b9dd12c942e78f68bb34cd0238792f2a1f3aeb6f717788579b7b315ad` |
| `sections/5_center_tower.tex` | `b241878cce73072410aeb629d7b06bcd17d7c5c95830f09bde61b8efbb6474ce` |
| `sections/6_compatible_odd.tex` | `ef39fd9b5a2e8df2df8f20b842f7a91064bdf65fd7167b68ff0af05cc92c4f9d` |
| `sections/7_hodge_projector.tex` | `e0c0caae53ce68cc79885e026986a4462351052f6afdc91418fa0c18f30758a5` |
| `sections/8_route_a.tex` | `f11e58af2b617700091001eaba3d057b3b783bf780f51780428a11c523cbe7bc` |
| `sections/9_declarations.tex` | `21f81c89ef5555aa9c988ec30b200a6c88440f2542dea3c6c6caf532504fe816` |
| `sections/A_exact_replays.tex` | `1fbf6b47b9d99314835fa2110761563738960ba8906a5001b28aa9cf5bcbaf72` |

The report intentionally does not freeze code/result hashes.  Those remain
under the separate release-candidate promotion and must be incorporated by
the final full-project manifest.
