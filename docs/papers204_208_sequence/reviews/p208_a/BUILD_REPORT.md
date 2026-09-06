# P208 A source-only build and actual full-page inspection

2026-09-06 UTC. Final qualifying build: build03. This is an actual
independent reviewer build of immutable Round 0, with no manuscript edits.
Earlier build01 and build02 remain as separate physical attempts.

The cold directory started with exactly eleven files: main.tex,
math_commands.tex, references.bib and the eight section TeX files. No aux,
bbl, log, fls or PDF was copied into it. SOURCE_ONLY_INITIAL.json gives all
eleven relative paths and hashes. INPUTS_BEFORE/AFTER pin the originals,
recorder/helper and frozen PDF comparator. build_preserved.py and
record_preserved.py preserve the exact execution programs before launch.

Final build.py SHA-256:
85f983fc8cb56db550470743e42510aff9afd6c6eb47e46b387c0e20f080d929.
Its actual outer launch used Python -I -S -B and a unique nonexistent
pycache prefix. The engine is pdfTeX 3.141592653-2.6-1.40.22,
TeX Live 2022/dev/Debian, with kpathsea 6.3.4/dev.

The actual sequence is pdflatex, bibtex, pdflatex, pdflatex. Each engine
run uses -no-shell-escape -recorder -interaction=nonstopmode -halt-on-error.
Every command's full argv, cwd, explicit environment, exit, stdout and
stderr is retained in build03/<label>.*. All child exits are zero.
Each pass's .log/.fls/.aux is preserved independently, as are generated
bbl/blg, engine versions, PDF metadata, font listing, full text extraction,
renderer output and raw frozen-PDF cmp.

Environment: PATH=/usr/bin:/bin; LANG=LC_ALL=C.UTF-8; TZ=UTC;
SOURCE_DATE_EPOCH=1788652800; FORCE_SOURCE_DATE=1;
openin_any=p; openout_any=p. These are explicit reproducible settings,
not an inference from equal PDF hashes.

The pre-run TeX inventory covers 105,987 actual resource files. Each
externally consumed .fls input and the explicitly resolved plainnat.bst
is checked against that pre-inventory; the 146 consumed resource paths
are pinned after and unchanged. TOOLS_BEFORE/AFTER include the engine,
bibliography executable, kpsewhich, PDF inspectors/renderers, cmp, ldd,
Bash, Python, build/helper programs and loaded recorder modules.
Real ldd probes capture resolved tool libraries. CONFIG_BEFORE/AFTER
also cover loader configuration, fontconfig/font resources and C.UTF-8
locale resources. These concrete resources and binaries are unchanged.
This is not a hermetic archived OS/kernel claim.

## Actual output and warnings

The final PDF has seven pages and all 27 listed fonts embedded.
Its SHA-256 is
dc3b6471ac0d62e887887a20a133b96a96d420b3ea65b3b06fb847f478038b62.
The actual frozen_pdf_cmp command exits zero, establishing raw byte
identity with Round 0. artifact_inspection02 additionally compares
build02 and build03 raw PDFs. No normalized-PDF comparison is used.

The final log actually reports:

    Underfull \hbox (badness 5681) in paragraph at lines 9--13

This is the Ajran bibliography entry. It remains visible as loose spacing
on page 7, not clipped or overlapping text. There is no final Overfull box,
undefined reference/citation, or unresolved rerun warning. Intermediate
pass logs are retained with their genuine initial citation/reference
messages; they are not called clean final logs.

The older author preparation01's 44.62468pt overflow is preserved in the
freeze as failed preparation evidence. It is not the current equation:
the final equation (6) is in two rows and fits. Root's earlier
artifact-inspector self-seal error is also retained as an invalid old
artifact attempt, not a valid seal or an OFS mathematical failure.

## Actual viewing, distinct from building

A rendered all pages of build01, build02 and build03 using pdftoppm at
120 dpi and actually opened/viewed every one of the seven PNGs of each
build. Build03 pages 1–4 and 5–7 were viewed in two actual image-tool calls
after that build completed. PAGE_VIEWS.md records the page-specific
observations; PAGE_INPUT_PINS.json seals the exact images/PDF inspected.
The build program's original RECEIPT status remains
PASS_BUILT_NOT_YET_VIEWED, because it was emitted before the separate
human-visible inspection. It was not retrospectively rewritten into a
viewing receipt.

Result: final build and all-page inspection pass with the disclosed
nonblocking bibliography underfull warning. No manuscript change is
requested from this inspection; public/external release remains held.
