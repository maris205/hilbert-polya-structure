# P211 initial source-only build preparation

Status: **HOLD_PENDING_ROOT_BINDING**. This is a new, bounded build adapter and
diagnostic evidence package, not an initial PDF, scientific run, manuscript
review, terminal pair, or acceptance. No TeX compilation, BibTeX bibliography
run, PDF inspection/rendering, or scientific execution occurred in this task.

The final operational source is the five Python files at this directory's
top level. The only current candidate lock is
`discovery05/DEPENDENCY_LOCK.candidate.json` (SHA-256
`4c66d15e0720bb064fe890c81d531d2400b99891e7f59e537a42657c685d31e6`).
Do not substitute discovery04: later adapter changes deliberately superseded it.
`BINDING.pending.json` is an intentionally rejected template, not authorization.

## Root reading and exact binding gate

Root must read the complete current five source files, this plan, the actual
source deltas in `diagnostic_capture05/commands/diff_*/stdout.raw`, and the
dependency selector/closure evidence before authorizing a launch. Static PASS
and this preparer's familiarity do not replace that read or root approval.

1. Bind a new physical absolute output directly under
   `docs/papers211_215_sequence/qa/`, named `p211_initial_build_NN`.
   It and the proposed unused cache paths must not exist. The adapter never
   replaces, resumes, cleans, installs, fixes TeX, or retries a build.
2. Create a separate actual root-read receipt and a separate binding JSON;
   preserve this pending template. Use schema
   `p211-initial-source-only-root-binding-v1`, status
   `ROOT_AUTHORIZED_INITIAL_SOURCE_ONLY_BUILD`, scope
   `ONE_INITIAL_BUILD_ONLY`, and the exact ENV8 below.
3. Set `source_pins` to exactly the nine relative-name byte/hash records in
   final `source_observations`; set `adapter_pins` to all five records in
   final `code_observations`. The adapter independently rehashes physical
   originals, rejects aliases, and requires agreement with the candidate.
4. Set `dependency_lock` and `root_read_receipt` each to an absolute physical
   `path` and a `pin` object with actual `sha256` and `bytes`.
   Root must approve the bounded lock, not change its schema to imply OS closure.
5. Set `cwd_relative_configuration` to three absolute keys under the future
   output's `inner/source_only/`: `texmf`,
   `.texlive2021/texmf-config`, and `.texlive2021/texmf-var`.
   Each record is exactly
   `{"path":ABSOLUTE,"present":false,"symlink":false,"resolved":ABSOLUTE}`.
   These represent the observed unset-HOME TeX roots at the actual future
   command cwd; diagnostic-cwd absence is not substituted for this binding.
6. Keep `scientific_execution`, `manuscript_review`, and
   `terminal_acceptance` all JSON false. Hash the final binding externally.
   Source/runtime/key drift must stop the proposed run for renewed inspection.

Exact child environment, with no inherited variables and no HOME assignment:

```text
PATH=/usr/bin:/bin
LANG=C.UTF-8
LC_ALL=C.UTF-8
TZ=UTC
SOURCE_DATE_EPOCH=1788825600
FORCE_SOURCE_DATE=1
openin_any=p
openout_any=p
```

After root approval only, the invocation shape is
`/usr/bin/env -i [the eight literal assignments] /usr/bin/python3.10
-I -S -B -X pycache_prefix=ABS_OUTPUT/unused_outer_cache
ABS_PREP/launch_build.py --binding ABS_BINDING --binding-sha256 ACTUAL_DIGEST`,
with cwd exactly `/root/autodl-tmp/symbolic_dynamics`.
The square-bracket words and ABS names here are placeholders, not an executed
command. An optional `--preflight-only` validates binding and observed parent
runtime without creating output or native children; it is not a build.

Root must retain the actual product-tool launch, session identity when yielded,
and actual final completion separately. The adapter captures complete separate
raw stdout/stderr of its native inner builder and native grandchildren. A
product tool's combined output envelope is not fabricated into a raw stderr
file. Root must not bypass the outer recorder with a direct build invocation.

## What the four-command adapter records

`build_core.py` contains new recorder/pin/source/runtime primitives.
`prepare_build.py` performs static/configuration dependency discovery only.
`build_p211.py` implements the one initial build.
`launch_build.py` records the outer native builder and before/after closure.
`static_checks.py` exercises import-only data/AST refusal cases.

A new cold `inner/source_only` starts with exactly:
`main.tex`, `math_commands.tex`, `references.bib`, and
`sections/{0_abstract,1_introduction,2_image,3_clock,4_inverse,5_scope}.tex`.
The actual graph is amsart 11pt/a4paper; T1/lmodern; geometry; amsmath;
amssymb; mathtools; booktabs; microtype; hyperref; and amsplain bibliography.
There are no external figures or manuscript-side nested inputs. Only the
nine approved manuscript sources were read; no verifier/proof dossier or
canonical-body inspection was used. This agent is manuscript-familiar, but
did not author or modify the proof or any paper source.

The build order is exactly one
`pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error
-file-line-error -recorder main.tex`, one `bibtex main`, then two more
identical pdflatex invocations, each with explicit /usr/bin executable paths.
Version/config/linkage queries and later PDF measurements are separately
recorded native commands, not extra compilation passes.

Every native attempt has a pre-spawn ATTEMPT, direct input before/after keys,
SPAWNED identity, separate raw stdout/stderr, actual native exit distinct from
wrapper reason, and owned-session settlement. A timeout may kill only the
owned process session to settle streams; it does not delete evidence.
Unsettled sessions or attempts without receipts prevent a final package seal.
This guard has static/archive coverage, not a live timeout/kill stress test.

Each actual TeX .fls is interpreted in order, preserving duplicate records
and exact spellings. Allowed input roles are SOURCE, EXTERNAL_PRELOCKED,
GENERATED_BEFORE, and GENERATED_EARLIER_OUTPUT_SAME_PASS. Unknown external
spellings, ungenerated local inputs, and unsupported/source outputs fail.
Same-pass INPUT following OUTPUT is explicitly not a read-time byte snapshot.
Before/after main.log, .fls, .aux, .bbl, .blg, .out and .toc are copied
immutably per pass; generated state and PDF hashes are retained. BibTeX has
no .fls: exact auxiliary/style/database roles are instead checked against
the auxiliary and actual .blg, with no non-FLS tracing claim.

Successful native completion would still yield only recorded-not-accepted
status. Actual pdfinfo/pdffonts/pdftotext measurements and one rendered PNG
for every actual page are planned, all marked NOT_VIEWED. Font embedding
is required for the bounded renderer premise. Warnings, undefined markers,
rerun messages, missing characters, and bibliography findings remain exposed
for root inspection. There is no guessed page count, 100 KB acceptance
threshold, venue limit, expected PDF hash, manuscript review, or terminal
equality assertion.

## Bounded dependency selector and limits

The selector starts from the actual accepted 139-path P210 consumed TeX key,
then explicitly adds this source graph's amsart/amsplain and font/configuration
requirements. The old key is a conservative input seed, not a claim that every
old path will be consumed here. Explicit font-definition literals select 173
metrics; their map edges select 115 font/encoding files. The final candidate
has 840 path spellings (795 regular-file entries), 33 selected ELF tool/module
inputs, and three separately bound future-cwd ABSENT roots.

The record includes native versions, effective kpsewhich queries using
pdflatex/pdftex or BibTeX program selection, selected ldd closure, parent
Python module/maps observations, configuration bytes, explicit symlink
spellings, and bounded immediate memberships. The six membership roots are
/etc/ld.so.conf.d, /etc/fonts/conf.d, /var/cache/fontconfig,
/usr/lib/locale/C.utf8,
/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.d, and
/usr/share/poppler/nameToUnicode. Their inclusion is explicit in code and
selection reasons. No whole TeX/font/library/host/history recursive inventory
was performed. Optional amsart.cfg lookup is explicitly recorded and will
be checked before and after any approved build.

These are bounded source/configuration/native-link and declared-FLS evidence,
not an OS sandbox, every-child /proc map trace, exact transient dlopen history,
or proof of every non-FLS read. Root must judge this disclosed residual scope.
If actual FLS reveals an unprelocked dependency, preserve the failure and
request the smallest explicit selector/binding revision; do not widen the
selector silently, delete the failure, or auto-retry.

## Diagnostic history and documentary audit

All five diagnostic captures and four discovery attempts are retained,
including three native failures. The history is:

| Diagnostic | Actual outcome | Preserved reason or change |
|---|---|---|
| 01 | FAIL_PRESERVED | Refused relative ./texmf under the original absolute-root assumption. |
| 02 | FAIL_PRESERVED | AST guard mistakenly classified string.replace as a filesystem replacement; discovery02 was never created. |
| 03 | FAIL_PRESERVED | Generic kpsewhich did not resolve pdflatex.fmt; corrected program/engine-specific queries retained the format requirement. |
| 04 | DIAGNOSTICS_RECORDED_NO_BUILD | First complete candidate; superseded by optional amsart.cfg and incomplete-attempt seal guard changes. |
| 05 | DIAGNOSTICS_RECORDED_NO_BUILD | Final 25-command discovery and final static/data checks passed. |

The diagnostic01 source was copied byte-for-byte to
`history/diagnostic01_source` before any correction and matched its recorded
CODE_BEFORE key. Later captures contain their actual `executed_adapter`
five-file snapshots. Native unified diffs are captured, not manually
reconstructed. `NATIVE_TOOL_ENVELOPES.json` preserves the actual product-tool
launch/completion envelopes and exact package/class graph read envelopes.
Missing completion in diagnostic02 is intentional: its launch returned an
actual completed exit 1 directly, with no yielded session.

`DOCUMENTARY_AUDIT.json` and its native tool envelope report independent
read-only verification: all nine nested nonself manifests, all 110 native
attempt/receipt pairs and raw-stream hashes, empty settled sessions, all five
historical executed-code snapshots, source before/after equality, current
nine-source equality, current five-code equality to discovery05, and exact
current bounded configuration equality. The three failed native commands
remain failures. The audit imported no operational adapter and ran no TeX.
The final top-level SHA256SUMS covers every package payload, including old
failures and nested seals, and excludes only itself.

## Reuse and skill disclosure

The accepted P210 builder was read at lines 1–102 and 325–726; its terminal
root-inspection receipt was read completely, as was the actual 139-path
consumed key. Their exact physical pins are retained in
`discovery05/HISTORICAL_INPUTS.json`. Recording ideas were adapted into new
source; no old helper was imported/executed and no old actual-build schema,
Round2 PDF equality, terminal run pairing, or full-host inventory was reused.
An attempted read of the guessed old outer-helper filename failed because
it did not exist; it supplied no evidence.

The symbolic-dynamics-research and paper-compile skills were read and used.
The project/task restriction keeps this step preparation-only; paper-compile's
generic latexmk cleanup/install/retry/source-fix and 100 KB defaults were not
applied. The useful adopted obligations are explicit build graph, preserved
logs, measured pages, embedded-font checks, visible warnings and later visual
inspection. Scientific generation, independent A/B gates, root PDF inspection,
terminal acceptance and HOLD_EXTERNAL remain separate.
