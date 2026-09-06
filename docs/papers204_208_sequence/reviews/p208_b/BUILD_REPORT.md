# P208 B source-only build and artifact review

PASS: eleven copied TeX/BibTeX source files produced the same seven-page
PDF as the immutable Round1 original. No preexisting aux, bbl or PDF was
seeded into `source_build/source_only/`; SOURCE_ONLY_INITIAL.json records
the exact starting files. The actual pdflatex/bibtex/pdflatex/pdflatex
commands, exits, stdout/stderr, intermediate aux/log/fls/out, bbl and blg
are retained. `cmp_frozen.command.json` records actual exit zero.

PDF SHA-256:
`dc3b6471ac0d62e887887a20a133b96a96d420b3ea65b3b06fb847f478038b62`.
All 27 fonts are embedded. The final log has no undefined references,
undefined citations, unresolved rerun warnings or overfull boxes. Extracted
text contains no `??`, `[?]` or `[VERIFY]` marker. The real final warning is
`Underfull \\hbox (badness 5681) in paragraph at lines 9--13` in the
bibliography. It is retained, not relabeled a clean warning-free build.

The source-only build recorder ran with isolated/no-site Python,
optimization zero, bytecode writing disabled and an unused alternate
cache prefix. Its relevant before/after set covers copied/original source,
recording source, Python and imported runtime files, TeX tools, ldd/Bash,
105,987 TeX/package/font/format files, 1,438 configuration/resource files,
35 resolved shared libraries and explicit missing configuration/search
locations. The 146 actually consumed external TeX inputs from the three
`.fls` logs plus bibliography style all match the before inventory.
Generated local inputs have their successive chain recorded separately.
The complete 41 observed runtime-map files match the pre/post inventories.
The build's 35 raw library aliases also happen to resolve to 35 files;
this is distinct from the mathematical replay's 35-to-32 alias count.

Every command has its actual argv, cwd, minimal environment, exit and
streams. Relevant input inventories are unchanged before/after. Runtime
map sampling is not a syscall trace or a hermetic historical-OS claim;
that limitation is explicit in RECEIPT.json. The build evidence is
proportionate present-environment reproducibility, not an assertion that
an unrecorded external historical environment has been reproduced.

All seven final pages were rendered and then actually viewed by this same
reviewer. `PAGE_VIEWS.md` is the later visual record. The automated receipt
retains its earlier `PASS_BUILT_RENDERED_NOT_YET_VIEWED` text unchanged;
the current combined status is BUILT / RENDERED / ALL_SEVEN_VIEWED.
