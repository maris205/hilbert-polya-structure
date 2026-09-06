# P208 prepared terminal builder — read-only implementation audit

2026-09-06 UTC. Disposition: **CHANGES_REQUIRED_BEFORE_FIRST_EXECUTION**.
This is an infrastructure code audit, not a manuscript review, build result,
scientific replay, root acceptance or visual PASS. External status remains
HOLD_EXTERNAL.

## Exact version and scope

The complete 301-line [prepared builder](run_p208_terminal_builds.py) was read
at SHA256 `184162f84193c5c0aafd665883fef66df3db594a56c6c0c72e848656087e25c8`,
together with the complete 27-line [preparation note](P208_TERMINAL_BUILDER_PREPARATION.md),
[artifact contract](../ARTIFACT_CONTRACT.md), 285-line
[strict replay infrastructure](replay_p208_strict.py), and 123-line
[previous P207 builder](run_p207_terminal_builds.py). Line references below
refer to that exact P208 version, not any later root revision.

The project research skill, its complete workflow and the complete
`paper-compile` skill were applied as read-only audit criteria. The latter
informed source-only, log/reference, font/page and viewing checks; it did
not authorize compilation, cleanup, a venue rule or manuscript edits.

Only this new report and its
[exact input-pin/diagnostic record](P208_TERMINAL_BUILDER_CODE_AUDIT_INPUT_PINS.json)
were created. The builder was neither imported nor executed. No science,
P208/OFS proof body, referenced mathematical `verify.py`, or FTH material
was opened. The sealed twentieth scout was not modified. There were no
children, Git operations, changes to central indexes or automatic next task.

A separate, read-only Python metadata probe reported its own interpreter
flags and mapped filenames; `kpsewhich` queries only reported configuration.
Neither probe ran TeX, processed a P208 PDF or executed the builder. Their
actual commands, UTC times, exits and full returned combined outputs are in
the JSON record. A repeated filesystem diagnostic returned exit 2 because
`qa_final`, physical Round2 and the root B-delta actual receipt were absent.
That expected absence is not a build failure or an execution test.

## Required changes

| ID | Priority and effect | Minimal repair |
|---|---|---|
| TB-1 | Blocker for the observed current-environment launch: actual parent resource mappings are outside the accepted coverage union. | Pin parent-mapped files before/after, include normalized configuration/resource byte records in coverage, and cover gconv configuration/cache. |
| TB-2 | Blocker to the preparation note's complete resource/provenance claim: Poppler data is omitted; actual parent launch and mapping-sampling scope are not recorded. | Inventory the known Poppler data root, record a controlled parent launch/settings, and state exactly which process/maps were sampled. |
| TB-3 | Required guard hardening: an optimized invocation erases its own rejection guard and all subsequent assertions. | Make the initial optimization/isolation/cache/argument checks explicit exceptions, before any acceptance or output work. |
| TB-4 | Required failure-recording repair: spawn errors lose the command identity, and an early closure failure suppresses later available inventories. | Journal attempted commands before spawn, preserve spawn exceptions distinctly, and collect/save closure components independently. |

### TB-1 — configuration is recorded but excluded from actual mapping coverage

Lines 36–37 include `/usr/lib/locale/C.utf8` in `CONFIG_ROOTS`. However,
lines 272–276 build `coverage` only from scientific inputs, the Python/tool
inventory and `ldd`-resolved objects. Configuration records are not included.
`/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache` is absent from all
declared configuration roots as well.

The separate probe was run with the current `/root/miniconda3/bin/python3`,
`-I -S -B`, an absent alternate cache prefix, and a controlled `env -i`
containing PATH, LANG/LC_ALL=`C.UTF-8`, and TZ=`UTC`. Its actual flags showed
optimization 0, no-site 1, isolated 1 and no bytecode writes. Its actual maps
included both:

```text
/usr/lib/locale/C.utf8/LC_CTYPE
/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
```

Neither path can be supplied by the builder's current coverage union:
they are not paper/review files, Python stdlib/tool files or dynamic-link
objects listed by `ldd`. Consequently, for these observed launch conditions,
the final mapping lookup has a concrete uncovered-file failure route even
when the declared Python flags are obeyed. This is a code deduction from
an actual metadata probe, **not an executed builder failure**.

Repair before the expensive pair: collect and pin actual parent file-backed
mappings early, recheck them after, and union their byte records plus relevant
configuration records into coverage. Normalize the latter by `resolved` path
and retain their `sha256`/`bytes` shape; blindly unioning the existing richer
configuration dictionaries would fail the exact equality comparisons. Include
the relevant gconv cache/configuration tree with presence/absence records.
Do not weaken the membership check or silently drop non-library mappings.

### TB-2 — known renderer resources and recorder provenance need closure

Lines 31–37 inventory substantial TeX, font and fontconfig trees, but no
`/usr/share/poppler` tree. That directory exists in this environment; the
installed `libpoppler.so.118` contains the compiled default string
`/usr/share/poppler`. Concrete `nameToUnicode/{Greek,Thai,Bulgarian}` files
exist there and are outside the declared roots. The binary path and example
files are pinned in the audit JSON.

This establishes a real omitted resource family relevant to the Poppler
utilities invoked at lines 231–235. It does **not** establish that any specific
one of those files was read by a P208 PDF process: no child file-access trace
or PDF operation was run in this audit. The proportional repair is to add
the known data tree and its root's presence/absence/resolution to the
before/after resource inventory, together with any other resolved resource
roots exposed by the chosen tools. No OS image or all-filesystem scan is
needed.

The subprocess environment is already explicit and recorded at lines
158–160. In contrast, `current_parent_runtime()` records version, flags,
path and modules but not the recorder's actual launch command, cwd or
relevant inherited environment. The global `ENV` does not control Python
startup or the earlier imports: it is only passed to children. Record an
explicit controlled launcher, actual original argv/cwd and the controlled
settings/absence of loader, locale and Python overrides. Do not dump unrelated
ambient secrets to obtain this record.

Finally, lines 130–135 sample `/proc/self/maps` once, late, for the **parent
recorder only**. Lines 171–178 use `ldd`; they do not sample TeX/BibTeX/Poppler
children or establish every transient `dlopen` or resource access. The
receipt's current generic non-hermetic sentence at line 288 is insufficiently
specific about this boundary. Record the sample phase/process and distinguish:

- byte-pinned before/after inventories;
- link-time closure reported by `ldd`;
- actual file-backed parent mapping samples;
- resources recorded as relevant potential inputs, versus `.fls` inputs
  actually observed in TeX;
- child mappings, transient loads and resource accesses not directly observed.

An explicit finite sampling limit is acceptable here. Continuous tracing,
OS/kernel reconstruction and speculative exhaustive system hermeticity are
not demanded. Such a limit does not excuse the concrete missing known
resources or TB-1's failed coverage union.

### TB-3 — reject invalid interpreter modes outside `assert`

Lines 142–145 use assertions to reject optimization and require isolation,
no-site, no-bytecode and an absent alternate cache. `-O` removes those very
guards as well as the acceptance, manifest, PDF and coverage predicates
throughout the file. Replace the initial checks with explicit `if ...:
raise ...` logic. Once optimization zero is unconditionally established,
internal assertions can remain as scoped invariants if desired.

This is a real invalid-invocation bypass, **not evidence that a recorded
invocation used optimization**. Nothing has run. The intended `-I -S -B`
launch and the separate metadata probe both have optimization zero. A
missing Round2 or missing receipt would still produce a filesystem error
under `-O`; the finding concerns disabled predicates, not a claim that the
present absent inputs could magically be supplied.

### TB-4 — preserve the identity and extent of failed attempts

The ordinary nonzero-child route is good: lines 158–168 save both returned
streams, append the command record, then reject its exit code. The phase
handler retains a traceback and later writes a FAIL receipt.

Two narrower failure surfaces remain:

1. If `subprocess.run` raises before returning, for example because the
   executable or cwd is unavailable, lines 159–167 never create a row.
   The generic phase traceback has no guaranteed resolved label/argv/cwd/
   environment record for that attempted command. Create a start record
   before spawning, and on a spawn exception record its class/message and
   a distinct `NOT_STARTED` outcome with no invented child exit status.
2. Lines 256–265 collect all closure components before saving any of them.
   An invalid/deleted scientific input or a later `ldd` failure aborts the
   block and discards already available after-inventories; still-accessible
   later components are never attempted. Save each observation promptly,
   independently collect remaining components after a failure, and list
   which components could not be captured. Separate collection from
   equality validation where needed to preserve the observed mismatch.

The current code would report FAIL for these caught routes, so this is not
an invented-success defect. It is a concrete shortfall in the promised
failure/evidence record. Gate refusal before `OUT.mkdir` should continue to
leave `qa_final` absent; its launcher can preserve command/exit/streams outside
that directory. Disk exhaustion, termination and failure while writing the
failure receipt cannot be guaranteed away; preserve the launcher's outcome
and partial outputs rather than promising universal in-process recovery.

## Sound checks and exact remaining integration conditions

Under the intended unoptimized launch, the following implementation choices
are substantively sound and should be preserved:

- `science()` runs before `OUT.mkdir`. It validates the complete directory-
  relative Round2 manifest, checks each listed frozen file against its live
  counterpart by SHA256 and byte length, verifies both root accepted-delta
  status/zero-finding fields and exact current review-seal/DELTA hashes, and
  validates both complete review packages. It repeats these checks after.
- File creation uses exclusive mode and the terminal directory must not
  already exist. Two different physical build directories start with the
  prescribed eleven TeX/BibTeX files and no aux/PDF/bbl products. The copied
  inputs are rehashed after each build. No prior build product is copied.
- Actual pdflatex/BibTeX commands use fixed child settings, disabled shell
  escape, recorder output, three TeX passes and separately retained raw
  stdout/stderr. Per-pass log/fls/aux plus BibTeX products are preserved;
  generated cold-tree files are covered by the final nonself seal.
- External `INPUT` entries from **each** TeX pass are resolved, checked
  against the pre-build TeX inventory, pinned and rechecked. The explicitly
  located `plainnat.bst` is also checked. Local derived files are preserved
  products, not falsely called source-only initial inputs.
- Raw `/usr/bin/cmp` commands compare each generated PDF with frozen
  Round2 and compare the pair. By contrast, live/frozen input comparison
  is digest-and-length equality, not a recorded raw `cmp`; these roles
  must not be conflated in the handoff.
- Font embedding, exactly seven pages, render-count agreement and final
  log undefined/overfull checks gate each build. Underfull and other warnings
  remain recorded. Rendering does not produce a view verdict; the final
  status expressly says NOT_VIEWED and all-page human/root inspection is
  still pending.
- The final complete nonself manifest includes the retained command
  records, streams, inventories, outputs and failure material, with itself
  excluded. No accepted historical recorder is imported or modified.

Two integration conditions require an explicit root decision/check, not
speculation about the absent Round2:

1. The builder verifies a **self-consistent** complete Round2 tree and its
   live copies, but it does not bind that tree's exact manifest hash to an
   accepted Round2 freeze receipt or a required accepted payload set. A
   complete manifest can describe an incomplete choice of files. Root must
   verify the full physical freeze after accepted B and supply/pin that
   exact freeze closure, or add that linkage as a gate. This audit has not
   found an actual bad freeze: Round2 does not exist yet. Complete review
   seal/DELTA checks are valuable but do not alone prove this association.
2. Lines 196–198 hard-code three top-level sources plus eight section files.
   This is appropriate only for the exact accepted P208 source/resource
   contract. It is not a generic implementation of arbitrary local styles,
   figures or nested section resources. Without reading mathematical TeX,
   this audit does not assert that such a resource is missing now. Before
   launch, root should affirm the exact source-only allowlist, including any
   genuinely required local resources, and bind its hashes to the accepted
   freeze. Do not silently broaden the source set or import auxiliaries.

An apparent TeX-database omission was specifically checked and **not**
reported as a defect: the installed `texmf-dist/ls-R` and `texmf/ls-R` are
symlinks into `/var/lib/texmf`, which is already inventoried. Actual
`kpsewhich -all texmf.cnf` paths are within declared trees. With HOME absent,
the queried user TeX roots expand relative to the process cwd, not the
hard-coded `/root` paths; record that resolution and the cold-cwd absence
boundary, rather than claiming those `/root` entries are the effective
user search path.

## Optional polish, not reasons to demand a hermetic system

- Reject symlinked freeze/review root directories if “physical” is intended
  to mean no directory indirection at any level. Current leaf checks reject
  symlinked manifest payloads, but not every ancestor. No such directory
  substitution was observed.
- Record an exact expected command-label census for easier downstream
  completeness checks. The present straight-line pair already prevents a
  normal caught command failure from producing its two-build success state.
- Add final extracted-text `[VERIFY]`, `??`/`[?]` and explicit rerun-request
  diagnostics if useful. The existing log checks, frozen PDF equality and
  mandatory actual page views already provide substantive safeguards;
  this audit did not inspect the manuscript or find an actual marker.
- Discover TeX roots dynamically or explicitly reject an unexpected root
  set. The current `.fls` membership check already fails closed for an
  observed external TeX input outside the recorded tree.

## Handoff and evidence boundary

The five first-pinned implementation/preparation/contract inputs were
rehash-checked unchanged. The JSON records seventeen exact file inputs:
five audit targets/comparators, three applied instructions and nine
present-environment support files. The latter are support pins, not a
claimed complete runtime capsule for the audit tools or an executed build.
The seven retained diagnostic records contain six exit-zero read-only
observations and one expected exit-two absence observation, with no stream
separation invented from the terminal's combined output.

Exploratory wrong-path/missing-header/absent-directory reads and the
overbroad truncated binary-strings listing are disclosed in the JSON. The
resolved contract, full allowed code reads and narrow successful query
support this report; no missing primary body or truncated full-body read
is claimed as evidence.

The attempted post-write `jq` validation could not run because that tool is
absent; its discovery/validation exits are disclosed in the JSON. A separate
standard-library JSON/hash check is the read-only fallback, not an execution
of either audited recorder or a successful `jq` result.

Root should apply proportionate fixes in a new prepared revision, inspect
that exact delta, finish accepted B and the physical Round2 linkage, and
only then consider a recorded launch. This report neither performs those
actions nor pre-accepts their outcome. It does not waive the eventual
terminal builds, raw comparisons, artifact checks or actual all-page views.
