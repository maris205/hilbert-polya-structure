# P210 author-evidence helper

Authorship: `/root/p210_author/author_runtime`, an author-evidence implementation
helper, not an independent reviewer. The parent authors the mathematics/verifier
and must independently read these two Python sources before running them.
No scientific checker or TeX build was executed during helper authorship.

`evidence.py` implements three modes, using only the Python standard library.
Each `--out` must be an absent strict descendant of `--paper`. Existing evidence
is never overwritten. All generated files stay under that fresh directory.
The driver itself and each scientific child require a dedicated absent cache
prefix, isolated/no-site Python and disabled bytecode writes. Input copies are
source/data/documentary only; neither an interpreter nor a system tree is copied.

Example invocations (replace each fresh output/cache path if it already exists):

```bash
/usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/author_produce_01/absent_driver_cache papers/210-weakly-increasing-run-aggregation/evidence_tools/evidence.py produce --paper /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation --out /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/author_produce_01
/usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/author_pair_01/absent_driver_cache papers/210-weakly-increasing-run-aggregation/evidence_tools/evidence.py pair --paper /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation --out /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/author_pair_01
/usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/draft_build_01/absent_driver_cache papers/210-weakly-increasing-run-aggregation/evidence_tools/evidence.py build --paper /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation --out /root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/draft_build_01
```

Run these from the workspace root. `produce` runs one fresh source-copy verifier
but never creates a canonical file. The parent may copy its actual
`commands/run_1/stdout` unchanged to live `CANONICAL.json`, then run `pair`.
`pair` runs twice in new processes and invokes native `/usr/bin/cmp` for all
three comparisons: run 1/run 2, run 1/canonical and run 2/canonical. Every
command has exact argv/environment/cwd, full raw stdout/stderr and the actual
native return code, including comparison failures. No output is normalized.
Default scientific inputs are `verify.py`, `PARAMETERS.json`, `PROOF_PACKAGE.md`,
`CLAIMS_EVIDENCE.md`, `SOURCE_AUDIT.md`, plus the canonical in pair mode. Repeated
`--input` replaces that default list; `verify.py` and the pair canonical are
always included. The self-contained verifier takes no arguments.

The two input inventories bind live/copied inputs, both helpers, interpreter,
stdlib sources/extensions, tool binaries/link dependencies, shared libraries,
locale alias/data, every installed gconv table/module, loader/configuration
files and explicit environment settings. Symlink spellings and resolved targets
are recorded. The post-hook Python audit records imports/read attempts and
loaded module paths; before/after `/proc/self/maps` records mapped libraries.
Every extant observed file must have a pre-pin. Bytecode/site-package inputs
fail. Attempted nonexistent reads remain in the raw runtime record but are not
claimed to have supplied bytes. Cache prefixes must remain absent.

This is a conservative bounded runtime inventory, NOT an OS syscall trace or
an interpreter-startup trace. Short-lived mappings can evade the two maps
snapshots; the conservative library/stdlib/configuration pins provide additional
coverage without claiming that every pinned file was actually read.

`build` copies only `main.tex`, `math_commands.tex`, `references.bib` and
`sections/*.tex`. It runs the explicit sequence pdflatex, bibtex, pdflatex,
pdflatex, with recorder/no-shell-escape and fixed UTC/C locale/source-date
settings. It records per-pass products, all stdout/stderr, logs and native exits.
Every `.fls` INPUT is classified against pre-pinned inputs, prior-pass products
or an earlier OUTPUT entry in the same recorder stream. Installed TeX/font/
configuration trees are hash inventories only. Their large before/after JSON
inventories are losslessly gzip-compressed; replay inventories stay plain JSON.
No `latexmk`, old auxiliary files or prebuilt PDF is used. The PDF is inspected
with pdfinfo/pdffonts/pdftotext and all pages are rendered to PNG; the report
checks unresolved markers/references, font embedding and page/render counts.
Warnings are preserved. Actual human/agent page viewing remains the parent's
separate obligation and is always labelled `NOT_PERFORMED` here. A single
`build` invocation is draft evidence, not a two-build terminal gate.

`REPORT.json` records the actual status. Any native nonzero return, changed
input, unpinned observed input or mandatory check failure prevents PASS.
`PAYLOADS.json` is a directory inventory of generated artifacts except itself,
not the outer paper manifest. This helper creates no review, freeze, index,
Git record or paper `SHA256SUMS`, and it does not confer manuscript acceptance.

Static helper-author checks: Python 3.10 AST parsing passed for both sources.
A default `kpsewhich -all pdflatex.fmt` diagnostic returned native 1; the explicit
`-engine=pdftex -progname=pdflatex -all pdflatex.fmt` diagnostic returned native 0
and resolved `/var/lib/texmf/web2c/pdftex/pdflatex.fmt`. The driver uses the latter
engine/progname for every configuration lookup. This was configuration discovery,
not a TeX compilation. Final helper hashes are delivered in the parent handoff.
