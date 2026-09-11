# P207 actual terminal build and all-page inspection

2026-09-06 UTC. Root: `/root`. **BUILD_PAIR_PASS / SEVEN_PAGES_ACTUALLY_VIEWED**.
This records two real post-delta source-only builds and actual visual
inspection, not a new mathematical execution or the final artifact verdict.
`OWNER_AMBER / HOLD_EXTERNAL` remains.

Both actual manuscript deltas were accepted before this work. B's exact
scientific no-change plus documentary repair is in the
[accepted delta](../../../docs/papers204_208_sequence/reviews/p207_b/DELTA.md).
Its initial underfull overstatement and later-open/resolved Minor remain
preserved. All 105 scientific/documentary inputs were physically copied
to Round2 by the scoped no-overwrite freeze adapter. Round2's manifest is
raw-identical to Round0 and Round1, SHA-256
`8d134689f8c07f9bcac65b4576a5bfca2e073ece6281f9d893148f12adb43f5d`.

## Actual physical builds

Command: `python -I -B docs/papers204_208_sequence/qa/run_p207_terminal_builds.py`
from the workspace root. The new recorder invoked the unchanged
`qa/cold_build.sh` twice on physical Round2, into two new directories.
The complete [execution receipt](BUILD_EXECUTION.json) and its ten raw
stdout/stderr files record five actual commands: freeze pins before,
build 1, build 2, PDF pair `cmp`, freeze pins after. All exited zero with
empty stderr. Both helper invocations also compared their output to the
frozen final PDF before publishing the new build directory.

Each build starts with only nine source files: main, macros, bibliography
and six sections. No auxiliary file or prior PDF is a launch input.
The complete source pins, three pdflatex passes, BibTeX output, final log,
recorder input list, extracted text, metadata and font records remain in
[build 1](cold_build_1/SOURCE_INPUTS.sha256) and
[build 2](cold_build_2/SOURCE_INPUTS.sha256).

Both PDFs are 407,557 bytes, seven A4 pages, SHA-256
`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.
Their actual raw-byte comparison exited zero. The main text and limitations
end on page 6; the four references occupy page 7. This is an anonymous
short theorem note, with no particular conference page-limit claim.
All 31 reported font objects are embedded Type 1 fonts. PDF title, author,
creator and producer metadata are blank.

The engine is pdfTeX 1.40.22, TeX Live 2022/dev/Debian, with BibTeX 0.99d.
Each helper records `SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`,
`TZ=UTC`, and `LC_ALL=C`. All 114 recorder launch dependencies were unchanged
before/after. The receipt pins every absolute external TeX file found in
each actual final `main.fls` after its build and rechecks them at the end.
The separate [post-build snapshot](POSTBUILD_RUNTIME_STYLE.json) additionally
records the actual `plainnat.bst` path/hash and the current engine/renderer
executables. These are contemporaneous post-build pins, not pre-build pins,
a hermetic environment or a complete historical shared-library archive.
Changed relevant dependencies require affected new checks.

## Diagnostics and actual visual inspection

Both complete final logs contain exactly one spacing diagnostic:

```text
Underfull \vbox (badness 1038) has occurred while \output is active []
```

It appears before the page-4 marker. No final undefined-reference,
undefined-citation, Overfull or Warning line remains. The helper's empty
`DIAGNOSTICS.txt` only reflects its `undefined|Overfull|Warning` scan;
that scan omits Underfull and is not treated as absence of this diagnostic.
The report does not suppress the warning or claim a warning-free build.

Root rendered build 1 with `pdftoppm -r 105 -png`, actual exit zero, and
then actually opened all seven PNGs in order. The
[page-by-page receipt](PAGE_VIEWS.json) binds each inspected image to the
exact PDF and records substantive observations. Page 4 has generous
vertical spacing above Section 4, but its proof, theorem and decoder table
are within the frame, readable, and show no clipping or missing content.
The other pages' equations, matrices, table, prose and references are also
legible and contained in the page. No image existence/hash is substituted
for the actual views. No TeX, PDF or scientific input was changed.

The scoped terminal artifact auditor remains a separate required gate.
This build/view receipt alone does not complete P207 or the five-paper batch.
