# P208 source-only author preparation builds and actual page view

Status: TWO_STABLE_AUTHOR_PREPARATIONS_AND_AUTHOR_VIEW_COMPLETE.
This is not a physical Round0 freeze, accepted manuscript review or a
post-B terminal build. Root's own adoption/view record is separate.

## Actual build sequence

All commands ran from this paper directory under the root-inspected
build_author.py recorder:

```
python3 -I -B build_author.py preparation_01
python3 -I -B build_author.py preparation_02
python3 -I -B build_author.py preparation_03
python3 -I -B record_build_pair.py
```

Each build began in an exclusive source-only directory containing exactly
the 11 TeX/bibliography inputs and no PDF, auxiliary or other build product.
Each ran three actual pdflatex passes with one intervening BibTeX command,
with full stdout/stderr, exit records and per-pass log/recorder files.
Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian),
kpathsea 6.3.4/dev. No latexmk executable was available; the skill's normal
multi-pass pdflatex/BibTeX fallback was used without installing software.
No shell escape or cleanup was run. SOURCE_DATE_EPOCH=1788652800,
FORCE_SOURCE_DATE=1, UTC and C.UTF-8 are recorded with every command.

The pre-build inventory hashed 105,987 TeX/runtime resource files under the
explicit installed roots. Each final build actually consumed 146 pinned
external TeX/font/configuration/format/style inputs, including the
separately resolved BibTeX style. Every consumed path existed in that
before inventory and matched it; every consumed byte and tool/shared
library pin was rechecked after. This is not a hermetic historical build.

## Preserved first version and final diagnostics

Preparation 01 built successfully, but its h/E display had an actual
44.62468pt overfull hbox. The writer viewed its pages 4 and 7, then split
only equation (6) into two aligned rows. Its complete sources, PDF, logs,
runtime inventory and seven renders remain unchanged in preparation_01.
It is not used as the stable final preparation.

Preparations 02 and 03 both have seven pages and zero undefined references,
zero undefined citations and zero overfull boxes in their final logs.
Both retain one actual underfull hbox diagnostic, badness 5681, in the
Ajran bibliography paragraph (generated bbl lines 9–13). This warning was
not suppressed or denied. All fonts have emb=yes in the specifically
parsed embedding column; subset/Unicode flags are not used as substitutes.
The rendered bibliography is readable within the page margins.

- [Stable preparation 02 receipt](qa_build/preparation_02/RECEIPT.json)
- [Stable preparation 03 receipt](qa_build/preparation_03/RECEIPT.json)
- [Actual raw PDF comparison](qa_build/stable_pair/RECEIPT.json)

The actual /usr/bin/cmp exited zero with empty stdout/stderr. Both final
PDFs have SHA-256 dc3b6471ac0d62e887887a20a133b96a96d420b3ea65b3b06fb847f478038b62.
main.pdf is an exclusive copy of preparation_02's output, verified by its
hash. The comparator did not claim a new build or infer viewing from bytes.

## Actual author viewing: all seven final pages

The writer actually opened and inspected every preparation_02 render after
that build completed. The identical preparation_03 PDF does not imply a
second distinct seven-page viewing session. The build receipts intentionally
retain actual_page_viewing=false because their automated render commands
preceded this separate actual human-interface inspection.

| Page | Actual inspection |
|---|---|
| 1 | Anonymous title/abstract, complete map, two theorem statements and small cases readable; no clipped text. |
| 2 | Protected-cell recursion and both ear branches readable; root-edge and schedule arguments present without clipping. |
| 3 | Operational inverse table has clear columns and boundary cases; seed/later decoder and disjointness proof readable. |
| 4 | Repaired equation (6) now fits; gap evaluation, strict exponent loss and K setup readable. |
| 5 | Strong K closure and both boundary sizes visible; both square phases and commuting odd-phase minimum fit. |
| 6 | Both sharp witness parities and the LC4/Z4 tail distinction readable; exact old edge-labelled lift and limitations fit. |
| 7 | Bounded evidence, scope, all six references and URLs readable; known Ajran underfull spacing retained and inspected. |

The exact viewed render hashes are:

```
b0e59e344860a3fd4fecec8f8f143b580d6ab12a1a9f0cdb94bfe5aa68290ba9  page-1.png
1653ccea97cba3a8ac0b15300a701be9fe194db790e9bfe464bb3e97aba12737  page-2.png
2d0479905b2a4274f6bab0c2e0317c9fe647f0c240ed6d6e80edc29c216ba2ff  page-3.png
deea7a7d68f8d3fb8da89694d4c9117f6cb953ce1121fcb3fbb80f467b201b4e  page-4.png
cca25138f8d1f6af7c79baaddc2276edcfa362e9cde4bea3ac9a4e93390ebbe5  page-5.png
457074a1d46ad72ff7650d60e5967cfb8bd8d67bd9d4428d667b6de244a2e982  page-6.png
f34a7160b53c0b04ef281b2225394cde9a712c21f6fcbe5803dcb4108128824c  page-7.png
```

These are the files in qa_build/preparation_02/pages/. Main text and
references occupy seven total pages; no proof has been cut for an arbitrary
venue limit. Root still owns physical freezing and review/terminal gates.
