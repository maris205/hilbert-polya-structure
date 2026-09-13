# Paper28 one-time read-only dependency capture plan

Date: 2026-09-05. Status: prospective; independent code/scope review required before execution. This opens only the already authorized E0230 capture, not a compiler invocation or build acceptance.

## Scope and effect

The accepted Paper27 prerequisite and unchanged Paper28 source identities are bound by RECOVERY_CONTEXT_20260905.md. The user's request to start the next step continues that authorized recovery. This plan replaces the failed profile's discovery-compilation proposal prospectively; every old source, profile, lock, failure and build namespace remains untouched.

Run one scanner transaction. It performs directory enumeration, lstat/fstat, readlink and read-only byte reads, with explicitly scoped new local evidence writes. It never invokes a compiler, BibTeX, kpsewhich, ldd, a loader, version command, PDF tool, shell child or network client. Dynamic-library requirements are parsed from captured ELF bytes, not inferred by executing tools. No original manuscript file is changed and no build root is created or inspected.

## Input envelope

The scanner may recursively enumerate and capture these local resource trees, omitting only top-level `doc` and `source` under the first two roots, and top-level `site-packages` under the Python standard-library root:

| Root | Purpose |
| --- | --- |
| /usr/share/texlive/texmf-dist | TeX class/packages, formats/configuration, bibliography styles, fonts/maps/encodings and lookup data |
| /usr/share/texmf | Debian/Latin Modern resource tree |
| /var/lib/texmf | Installed formats and generated static font maps/lookup data; never regenerate |
| /etc/texmf | Installed TeX configuration |
| /usr/share/poppler | PDF character maps and related Poppler resources |
| /etc/fonts | Fontconfig configuration |
| /usr/share/fontconfig | Fontconfig support data |
| /usr/share/fonts | Installed public rendering fonts |
| /var/cache/fontconfig | Existing read-only font caches; never refresh |
| /root/miniconda3/lib/python3.12 | Configured controller/PDF-parser Python standard library, excluding site-packages |
| /root/miniconda3/lib/python3.12/site-packages/pymupdf | Configured PDF parser and rendering library |
| /root/miniconda3/lib/python3.12/site-packages/fitz | Configured PyMuPDF compatibility entry |

Named executable aliases: `/usr/bin/pdflatex`, `/usr/bin/bibtex`, `/usr/bin/kpsewhich`, `/usr/bin/pdfinfo`, `/usr/bin/pdftotext`, `/usr/bin/pdffonts`, `/usr/bin/pdftoppm`, `/root/miniconda3/bin/python3`, `/root/miniconda3/bin/python3.12`. Allowed final executable targets additionally include `/usr/bin/pdftex` and `/usr/bin/bibtex.original`; record the `/etc/alternatives/bibtex` hop. No executable is run during capture.

Capture `/etc/ld.so.cache` and `/usr/share/zoneinfo/UTC` as exact runtime data (the UTC link may resolve to the named `/usr/share/zoneinfo/Etc/UTC`). Resolve ELF64 little-endian x86-64 PT_INTERP, DT_NEEDED, RPATH and RUNPATH by static parsing. Library candidate metadata/bytes are limited to `/root/miniconda3/lib`, `/usr/lib/x86_64-linux-gnu`, `/lib/x86_64-linux-gnu`, `/lib64`, `/usr/lib64`, and the explicitly listed resource trees. Candidate names are simple `lib*.so*` or `ld-*.so*` basenames; `$ORIGIN`/`${ORIGIN}` may expand only within this envelope. Capture all matching allowed candidates, not a guessed loader winner; record requester/name/candidates and unresolved edges. This is a conservative input superset for a later explicitly pinned loader/search environment, not proof of arbitrary host-loader behavior. No extra dependency prefix can be added silently during execution.

Metadata/readlink access is permitted for the exact ancestors needed to traverse these inputs, including `/lib`, `/lib64` and `/usr/lib` aliases; it is not permission to list a workspace, home directory, `/etc` or library directory generally. A link target outside the envelope is recorded as excluded without dereference. A raw link target with non-leading parent components (for example `dirlink/../file`, or any parent component in an absolute target) is also recorded but not traversed, avoiding incorrect lexical normalization across an unvisited symlink; ordinary leading `../` chains from a canonical containing directory are supported. Missing optional trees, dangling links, unsupported library search tokens and unresolved ELF edges are disclosed, not silently converted into closure. An essential named tool or the four primary TeX trees missing is a capture failure. Symlinked files and directories are recorded with raw target text; admitted in-envelope targets are captured once under their resolved absolute path. Hard links are recorded as independent path identities, not assumed to be distinct content.

Every regular file is opened without following the final symlink, read once with size bounds, hashed and copied from the same bytes; before/after descriptor and pathname identities must agree. Modes, link counts, byte counts, LF counts, SHA256 and resolved locations are recorded. Directory membership is checked before/after walking; directory storage size is recorded only as observational metadata, not a content-equality condition. Concurrent mutations stop capture. At most 250,000 entries, 256 MiB per regular file and 2 GiB total regular input bytes are permitted; exceeding a bound stops rather than expands scope.

## Controller trust boundary

The already configured Python interpreter and standard-library imports used to run this scanner are the local administrative control plane. Invoke it with `-I -S -B`: isolated imports, no site/.pth processing, no bytecode writes. Their startup reads necessarily precede the scanner's own observations; the capture does not fabricate a pre-import trace or claim to certify its own bootstrap. Their bytes, standard library and native dependencies are captured for prospective later binding. Kernel, filesystem implementation, platform tool launcher and CPU remain host assumptions, not bundled/attested dependencies. No credentials or unrelated user resources are inspected. This is a renderer/resource capsule, not a VM image or claim of OS-level hermetic isolation.

Literal invocation after review (replace only REVIEW_SHA256 with the actual reviewed-note digest): `/usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /root/miniconda3/bin/python3.12 -I -S -B /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/notes/DEPENDENCY_CAPTURE_20260905.py --capture REVIEW_SHA256`. Do not set or repurpose HOME/CODEX_HOME. The configured shell/env launcher is also part of the administrative trust boundary, not an additional publication command.

## Exact new artifacts and order

The only capture output root is `notes/dependency-capture-20260905`, relative to the Paper28 project. `mkdir` is its exclusive freshness test; if the path exists, do not list, reuse, delete or overwrite it. No earlier build/evidence namespace is touched.

1. Bind the plan, scanner, ELF helper, intake and exact source trio; require the independently recorded plan/code review before launching capture.
2. Exclusively create the new capture directory (0700). Write `intent.json` (0600) before any system-resource census/read. It records plan/code/source identities, allowed scope and fixed limits. This is a simple local start record, not a host exactly-once or crash-recovery guarantee.
3. Exclusively create `events.jsonl` and `capsule.tar` (0600). Append capture events in deterministic discovery order and write canonical root-relative tar members from the same observed bytes. Tar contains resource bytes and literal symlink records, not runnable manuscript/build output. Do not extract this archive blindly onto a host filesystem.
4. Write `manifest.json` (0600) with exact sorted file/directory/link identities, excluded/absent paths and static native-dependency edges. Check source trio again. Close/fsync outputs; stream-hash the completed evidence.
5. Write `outcome.json` (0600) last, containing hashes/sizes of the four preceding artifacts, capture counts, limitations and `CAPTURE_RECORDED_REVIEW_REQUIRED`. It is deliberately not a member of its own hash set. A failure after root creation writes an exclusive `failure.json` when possible; partial evidence remains untouched and there is no automatic retry. A process interruption may leave no final outcome; do not infer success from its absence.

Administrative notes created through apply_patch are the plan, scanner `DEPENDENCY_CAPTURE_20260905.py`, pure-byte ELF helper `CAPTURE_ELF_20260905.py`, independent review, post-capture review/result and the mutable Batch07 short context. Their writing is distinct from resource-input reads. No fourth manuscript source is introduced. Only newly owned draft code/plan may be corrected before execution; once capture starts, freeze their exact bytes and preserve any failure.

## Acceptance and next build gate

A capture outcome only means the stated bytes were recorded. Independently verify manifest/archive correspondence, native/resource coverage and any excluded/unresolved paths before use. The later successor build profile must freeze the actual namespace/search paths, loader/runtime choices, environment, source bindings, commands, validators and stage ordering; it must prevent undeclared first-read dependencies rather than pretending recorder output itself enforces that rule. No formal compiler invocation is authorized by this capture result alone.

Paper28 output requirements remain its own: 22–30 physical content pages, references on the next fresh page after the final Section 8 sentence, eight sections/32 subsections/three tables/18 cited records, exact anonymous trio and normal locked hyperref/bookmarks/public bibliography links. Do not import Paper27's no-annotation rule or alter layout/source merely to fit a validator. Warning disposition and PDF parsing are fixed before any build, followed by actual visual/output and independent terminal-integrity checks.

The paper-compile skill supplies prerequisite/output-check discipline; this project's explicit immutable-source, no-cleanup, no-discovery-compile and physical-page requirements supersede generic latexmk/install/retry examples. No package install, cache update, cleanup, upload, submission, hosting or external message is permitted here.
