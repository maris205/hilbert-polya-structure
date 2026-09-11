# P213 A source-only build — source-ready preparation

No build, TeX, renderer, scientific verifier or output-directory creation was
performed. Root must accept this exact request and issue a new single-build
grant. Both old initial-build grants remain consumed. This packet supplies
author-side mechanics, not A's manuscript verdict or actual page views.

## Exact reuse and changed roles

The controlling accepted baseline is
../p213_initial_build_artifact_root01/RECEPTION.md: confirmation02 only,
under the existing ordinary trusted TeX/bootstrap boundary. The old run01
missing texfonts.map prepin remains historical; the accepted 223-item run02
manifest includes that map and is preserved byte-for-byte here.

EXACT_DELTA.json and DOCUMENTARY_NATIVE.json record actual d55b51, exit0:
the new 127-line BUILD_REQUEST.sh differs from the accepted run02 script
only in four complete assignment lines, 11–14:

- P213_PREP and P213_BIND now identify this new source/request/runtime package.
- P213_SRC selects physical papers/213-receiver-limited-cyclic-transfer/frozen_round0.
- P213_OUT selects the distinct future qa/p213_a_build_run01.

Every other script byte is unchanged. Source-copy, snapshots, commands,
timeouts, failure handling, diagnostics and rendering are mechanically reused.
The native arguments differ only in the exact invoked BUILD_REQUEST.sh path.

The inherited REQUEST_AND_BINDING.sha256 generation now correctly resolves
both script and NATIVE_REQUESTS.proposed.json through the new P213_PREP;
it will therefore pin the actual A request source, not an old initial script.
The legacy P213_INITIAL_BUILD_SUPERVISOR_EXIT label and live_source.* filenames
are unchanged labels only: actual grant/request/output identify the A build,
and live_source.* will refer to the fixed Round0 source tree. The inherited
opening comments refer to the already accepted author strict/delta premises;
they neither create an A verdict nor replace the required new A build grant.

## Finite source and runtime inputs

Only these nine relative sources are copied into a freshly empty source_only/:

    main.tex
    math_commands.tex
    references.bib
    sections/00_abstract.tex
    sections/01_introduction.tex
    sections/02_temporal.tex
    sections/03_inverse.tex
    sections/04_fibres.tex
    sections/05_verification.tex

No old PDF, AUX, BBL, BLG, FLS, LOG, verifier, canonical or review report is
copied. FREEZE_SCOPE requires A to work from this physical Round0.
Current ee6363 checks all nine frozen source pins; d55b51 additionally compares
each entire frozen source against its accepted run02 copy as raw bytes.
PROPOSED_SOURCE_ONLY.sha256 is byte-identical to the accepted nine-source pin
file, SHA256 1f0c45bcd19104d97ef3461ad50c055f52db8d89025ec043c5188475cd33978b.

RUNTIME_INPUTS.sha256 contains exactly the accepted 223 fixed entries,
SHA256 35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530.
Current preparation-time strict546326 passed all223. This is a current
content-pin check, not a future execution key or a new loader census.
The proposed actual build repeats the complete selected runtime hash checks
before and after, and nine-source checks before copy, after copy, after each
of four build steps and after completion. Source copies are raw-compared.

These are fixed ordinary content guards. They do not claim full-stat,
continuous memory, hostile-path or complete syscall/loader closure.
No unknown recorder path is adaptively opened by the script. Any new unknown
input or changed dependency requires root's affected-scope decision.

## Exact launch and capture

NATIVE_REQUESTS.proposed.json contains the complete native tool arguments.
Cwd is /root/autodl-tmp/symbolic_dynamics, tool shell /bin/bash,
login=false, tty=false, yield_time_ms=1000, max_output_tokens=16000.
The script is invoked by /bin/bash --noprofile --norc with the single
--execute-under-separate-root-grant argument after env -i supplies exactly:

    PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC
    SOURCE_DATE_EPOCH=1789084800 FORCE_SOURCE_DATE=1
    openin_any=p openout_any=p
    MKTEXFMT=0 MKTEXPK=0 MKTEXTFM=0 MKTEXMF=0 MKTEXTEX=0

The four passes are pdflatex, bibtex, pdflatex, pdflatex. Every TeX pass uses
-no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error
-recorder main.tex. Fixed /usr/bin/bibtex receives main. Each build command
is supervised by timeout --signal=TERM --kill-after=10s 600s.
Diagnostics and each render use the same supervisor with180s. These are
supervisor return codes, not invented native child exits.

The source creates only the distinct new output tree, nonrecursively under
umask077/noclobber, and never cleans or resumes an existing failed tree.
That future output path has not been queried, created or reserved here.

Every step preserves complete stdout/stderr, exact cwd/argv and supervisor
status. All four before/after product snapshots retain present hashes and
absent-file lists. Final original PDF/LOG/FLS/AUX/BBL/BLG stay in source_only/.
Full pdfinfo, pdffonts, pdftotext -layout and literal warning/error diagnostics
are captured. Every actually reported page is rendered with pdftoppm at150dpi
to a separately pinned PNG; page count and final product hashes are retained.
No old PDF bytes or expected new page count is substituted.

If a native session is returned, only empty-input reception of that actual
session to completion is proposed. Preserve timeout/nonzero/partial evidence;
no automatic retry, cleanup, enlarged scope or reused grant follows.
The tool output budget is not a raw-file truncation limit or storage promise.

## Handoff boundary

Root may now receive these exact source/request/delta/manifest bytes, perform
its new current preflight, and separately grant one A source-only build.
Then full new log/ordered-FLS/BibTeX/source/runtime/artifact reception and A's
actual all-page interpretation are still required. Hashes/PNG existence are
not a visual review. This distinct A build is not either terminal build.

The project research skill supplies changed-dependency and review ownership
rules; paper-compile supplies diagnostic/font/page requirements. Generic
cleanup/auto-retry instructions do not override this bounded preparation.
The recipe has not been executed or syntax-tested here. READ_AND_KEY_NATIVE
retains complete individual reads/current hash checks; any truncated combined
display is not claimed as a complete display. No proof, live/frozen source,
central index, reviewer output, Git or external artifact was changed.
HOLD_EXTERNAL; current five-paper round only.
