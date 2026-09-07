# P209 A — actual source-only build and visual inspection

2026-09-07 UTC. **PASS_SOURCE_BUILD_AND_ALL_RENDERED_PAGE_VIEWS**, with the
separate optional structural preflight **UNAVAILABLE**. This process ran one
new physical build for its initial Round0 manuscript review. It did not
reuse archived author/root build receipts as a new execution and does not
claim the later required pair of terminal builds.

## Source, command and dependency closure

The fresh `review_build_01/cold_build/` began with exactly eight copied
Round0 sources: main.tex, math_commands.tex, references.bib and the five
sections 00_abstract through 04_scope. SOURCE_ONLY_INITIAL.json records
their exact hashes; no PDF, auxiliary, bibliography product or style cache
was initially copied. All copies were checked against the pinned freeze.

Actual launcher command from the workspace root:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p209_a/launcher_review_build_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p209_a/launch_review.py build review_build_01
```

Both launcher and recorder exited zero. The actual TeX sequence is
pdflatex / BibTeX / pdflatex / pdflatex, with full pass stdout/stderr,
copied .log/.fls/.aux, generated .bbl/.blg and commands retained. Each
pdflatex uses `-no-shell-escape -recorder -interaction=nonstopmode
-halt-on-error`. Explicit reproducibility settings are SOURCE_DATE_EPOCH
1788652800, FORCE_SOURCE_DATE=1, UTC, C.UTF-8, openin_any=p and openout_any=p.
TEXMFHOME, TEXMFCONFIG and TEXMFVAR point to distinct nonexistent owned
paths; actual kpsewhich queries and before/after absence checks confirm
them. No manuscript edits or compiler fixes were made.

Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), with
the full `--version` output retained. Build receipts contain 120,345 known
input paths, 4,598 runtime files and 113,733 TeX resources, checked before
and after. All 131 consumed external TeX resources were matched to the
initial conservative inventory; each pass's .fls distinguishes generated
local inputs from original sources. Runtime/linkage/configuration evidence
uses the same disclosed conservative/sampled method as REPLAY_LOG.md,
not continuous tracing or OS-hermeticity.

## Output checks

The result is an anonymous, unencrypted four-page A4 PDF, 280,267 bytes,
SHA256 `ca2e381904905939e121b7931641b050ba24657c16661df3bb5008c88c28884f`.
pdfinfo reports four pages; pdftoppm emitted four PNGs; all 20 font rows
are embedded. Final undefined-reference/citation, warning, overfull,
underfull and rerun lists are empty, and extracted text has no `??`, `[?]`
or `[VERIFY]` markers. Full logs and fonts/text records are preserved.
An actual `/usr/bin/cmp` against frozen Round0 main.pdf exited zero;
its complete receipt is in auxiliary_01/pdf_cmp.command.json. Matching
bytes do not substitute for the actual views below.

## Actual visual inspection by this reviewer

I opened and viewed every one of the four *newly rendered* PNGs in this
process, using two calls displaying two images each. These observations
are about the rendered outputs, not certified PDF extraction page anchors.
The proof/source report uses TeX section/theorem anchors instead.

| Rendered file | Actual observation | SHA256 |
|---|---|---|
| `review_build_01/cold_build/pages/page-1.png` | Title/anonymous author, abstract, operation, two-cycle witness and nearest-source comparison all visible; no clipping, overlap, missing symbols or citation placeholder. The amsart title/abstract spacing is generous but acceptable. | `fc7bb428c539008212cbfa93c094101aa96472513787136a8e8023a4c645f7af` |
| `review_build_01/cold_build/pages/page-2.png` | Theorem 1, height definition, inclusions and necessity steps legible; infinity symbols, labels and equations fit. Sufficiency continues normally onto the next rendered page. | `8c93a002f94d9191c39f514656f444c5e8b1cbae53e83be95d3150d65ba4bdd3` |
| `review_build_01/cold_build/pages/page-3.png` | Period argument closes, both admissibility conditions and Theorems 2/3 are fully readable; superscripts, endpoints, empty-set notation and proof-end markers render correctly. | `6843be793eafb17ae752a441ca8119cc09032c75c163ee5afd03b292b3a9fcd7` |
| `review_build_01/cold_build/pages/page-4.png` | Finite-check limitations and all four references visible; long title, URLs and DOI wrap within margins. Lower whitespace is natural at the end of a short note. | `0a320b457523122f55637c5d34176e26aaa37129974459a1808b6b700c43888d` |

The immutable machine build receipt still says NOT_YET_VIEWED because that
was true when it was sealed. This later signed-in-process report supplies
the actual viewing event; the original machine receipt is not rewritten.

## Skill-induced extra check and preserved limitation

The ARS local-PDF-structure preflight was also attempted. The initial
`-I -S -B ...pdf_read_preflight.py --help` invocation actually exited 1:
isolated Python omitted the sibling audit_snapshot import. Full original
command, exit and stderr are preserved in PREFLIGHT_INITIAL_FAILURE.json;
it read no PDF. A new explicit minimal-environment `-S -B` invocation of
the unchanged script resolved that sibling import and exited zero with
a produced structural verdict **UNAVAILABLE**, because `pypdf` is not
installed. Its exact PDF hash, null three-way counts, warning and raw
command streams are retained in auxiliary_01/PDF_PREFLIGHT.json and its
neighbouring files. Zero process exit is not a structural PASS.

Accordingly this review claims actual compilation, Poppler output checks
and all-four rendered-image views only, not the unavailable three-way
structural certification or licensed extracted-PDF page anchors. This
optional tool limitation does not invalidate the separately completed
source-only build and actual image inspection required by the project
contract. No dependency installation or external manuscript transfer was
performed. All external actions remain HOLD_EXTERNAL.
