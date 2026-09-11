# B actual independent cold build

One complete independent source-only cold build succeeded, on the second
attempt. This is not the batch's terminal double-build gate.

`build01` failed with native parent return 1, a real `KeyError: 'real'`
before any TeX pass, after 18 successful native prerequisite queries.
The adapter had treated the structured `cap.before` object as the file map.
`native/build01/{ATTEMPT.json,RESULT.json,stdout,stderr}`, the initial adapter,
and the complete partial `build01/` directory remain unchanged. There is no
fabricated AFTER ledger or PASS report for that failed build.

`instrumentation/evidence_build_v2.py` corrects only that dictionary lookup;
the original adapter and all scientific sources remain unchanged. The
separate `native/build02` parent and all 26 child commands returned native 0.
The input directory was absent and received exactly 10 TeX/bibliography source
files from the pinned Round1, no existing PDF/aux/bbl/log products.

Because `latexmk` was actually unavailable, the complete cold sequence was:

```text
/usr/bin/pdflatex -recorder -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -recorder -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
/usr/bin/pdflatex -recorder -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The cwd is the absolute `build02/source` directory specified in each actual
attempt. The environment contains only PATH/LANG/LC_ALL/TZ as in REPLAY_LOG.
All four complete raw command streams, per-pass SOURCE_BEFORE/SOURCE_AFTER
pins and every extant overwritten log/fls/aux/bbl/blg/out are physically kept
under `build02/commands/pass_1` through `pass_4`.

The first pass has unresolved citations/references and rerun warnings;
the third pass still has citation rerun warnings. These are preserved normal
cold-build history, not silently dropped or claimed warning-free. The final
fourth pass has no unresolved citation/reference, rerun, overfull or underfull
warning under the recorded checks. Final extracted text has no `??`, `[?]`
or `[VERIFY]` marker.

Before/after ledgers contain 118,355 full physical file keys, 61 configuration
and presence keys, and exact membership. They cover the 10 manuscript sources,
engines, styles, formats, loader/shared libraries, TeX/font/configuration and
rendering resources. Every actual FLS input is classified as a pinned external
input, pinned prior product or earlier same-pass recorded output; none is
unresolved. Three actual `kpsewhich` user-root queries established the user
TeX roots absent. Complete resource-key ledgers are compact gzip metadata,
not copies of the host's resource trees.

The final `build02/source/main.pdf` is 323,806 bytes, six pages, with all 20
listed fonts embedded. Its SHA256 is
`46afb4e470090087d3d57097849219f24d2e415495d4454e301a99c9847d9306`.
Actual `pdfinfo`, `pdffonts`, `pdftotext` and PNG rendering outputs are kept.
An additional actual `/usr/bin/cmp` against the pinned Round1 PDF returned 0.

Every rendered page was actually opened and visually inspected, in groups
1–3 then 4–6. `VIEW_build02.actual.json` binds each distinct page image and
the PDF to specific observations. All mathematical cases, displays, tables
and references are readable; no clipping or overlap was found. Page 6's
final whitespace is benign. The instrumentation's earlier mechanical report
correctly still says `visual_inspection: NOT_PERFORMED`; it predates and does
not stand in for the later actual view record. The binder records observations,
not an invented automated visual pass.
