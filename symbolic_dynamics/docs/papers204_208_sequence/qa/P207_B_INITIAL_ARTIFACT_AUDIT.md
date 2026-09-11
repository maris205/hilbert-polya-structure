# P207 B initial package — independent artifact-only audit

2026-09-06 UTC. Assessor: `/root/batch197_lzk_gate`, the prior P207 A
reviewer and not a P207 author. **ONE MINOR EVIDENCE FINDING ON THE EXACT
INITIAL PACKAGE; NO MATHEMATICAL, HASH, RAW-REPLAY OR INPUT-COVERAGE DEFECT
FOUND IN THIS ARTIFACT SCOPE.** This is not a third manuscript review,
mathematical reassessment, B-delta acceptance, Round2 or terminal gate.

## Finding requiring the actual documentary delta

**P207-B-ART1 — Minor / open on the audited initial package.** The initial
[B build report](../reviews/p207_b/BUILD_REPORT.initial.md) lines 48–50
includes absence of an underfull-box diagnostic. The original
[complete build log](../reviews/p207_b/cold_build_01/main.log) line 638
instead contains:

```text
Underfull \vbox (badness 1038) has occurred while \output is active []
```

It occurs immediately before the page-4 marker. The unchanged
[source-only helper](cold_build.sh) line 34 scans
`undefined|Overfull|Warning`, not `Underfull`; therefore its empty
`DIAGNOSTICS.txt` cannot establish the broader statement. The finding is
an evidence-report overstatement. It is not a failed TeX command and does
not, without viewing, demonstrate clipping or another manuscript defect.

Required correction: preserve the initial build report and initial finding
census, accurately report the one underfull-vbox diagnostic and the
helper's actual scan scope, and record the newly discovered Minor and its
documentary resolution in the actual B delta. No scientific/PDF change or
new numerical execution is required merely by this report correction.
No clean initial artifact PASS is asserted here.

Root and B independently acknowledged this exact finding. Root's actual
[response supplement](../P207_B_RESPONSE_SUPPLEMENT.md), SHA-256
`a3e3c2a36388291240f12055d44a2a4c281b3ee94800b76fa20e87124c874294`,
authorizes only that evidence correction and preserves the initial root
response. I read the supplement; it is a response, not an accepted delta.
This audit does not preaccept B's subsequent resolution or final manifest.

## Actual independent check and preserved stopped attempts

The current project research skill, workflow and artifact contract governed
this bounded inspection. The main assessor fully read B's verifier,
execution recorder, artifact checker, intake/replay/build/source-access
records and the root replay/build utilities. Root separately owns the
full original mathematical/source/proof assessment and actual root pair;
I supplied no P207 lemma, manuscript text or mathematical producer change.

The actual command was:

```text
python3 -I -B docs/papers204_208_sequence/qa/p207_b_artifact_audit/check_initial.py
```

The completed artifact check ran at 09:19:05–09:19:08 UTC and exited zero
after **39,623 integrity/shape checks over 599 consumed objects**. Its
explicit result is `INITIAL_ARTIFACT_MINOR_FINDING_REQUIRES_DOCUMENTARY_DELTA`,
not a clean PASS; zero denotes successful completion of the inspection,
not disappearance of P207-B-ART1. The complete output, including all 599
before/after byte hashes, is
[attempt_03.stdout.json](p207_b_artifact_audit/attempt_03.stdout.json);
its [actual execution record](p207_b_artifact_audit/attempt_03.actual.json)
is separate. The output has SHA-256
`457e3da885163d5888a95aa165f34e53580a687c63ada34d43f2568cb4ec46aa`.
The exact [completed checker](p207_b_artifact_audit/check_initial.py)
has SHA-256
`eb126293327d4b07d76b111bee852dc5496a0409eabe0234a119dcf2e5b27f08`.

Two genuine earlier stops remain preserved with their exact checker
versions and actual tool outputs:

1. [Attempt 01](p207_b_artifact_audit/attempt_01.actual.json) correctly
   rejected live-directory closure after five B-delta additions appeared
   during phase transition. No initial-file hash mismatch occurred. The
   exact source is [attempt-01 checker](p207_b_artifact_audit/check_initial.attempt_01.py).
2. [Attempt 02](p207_b_artifact_audit/attempt_02.actual.json) reached the
   complete-log diagnostic test and exposed P207-B-ART1. The exact source
   is [attempt-02 checker](p207_b_artifact_audit/check_initial.attempt_02.py).
   The completed checker retains that diagnostic and reports the finding;
   it does not make the issue disappear by dropping it from the result.

No mathematical verifier, build or image viewer was run by this audit.
The two stopped artifact checks and one completed artifact check are not
additional B mathematical runs.

## Exact initial snapshot and dependency coverage

The audited initial B manifest is SHA-256
`6f103d933c8135563b00734d8850ce36bf2fc47aa504d669e01cf6c99ef29074`:
118 nonself entries and 119 physical objects including itself. During
this audit, B had begun the actual response phase and added exactly
`DELTA_INTAKE_CHECKS.json`, `FINDINGS.initial.json`, `REPORT.initial.md`,
`SHA256SUMS.initial` and `check_delta_artifacts.py`. B then held all writes
until this check completed. No initial object had changed at that point.

The disclosed historical-scope adapter checks exact manifest membership
against root's already recorded 119-object `before_package_files` baseline,
and checks the three preserved aliases byte-for-byte. It also explicitly
checks that those five, and no other files, are the phase-transition
additions. This is not permission to omit unlisted files from the eventual
complete B delta manifest. The recorded result is a point-in-time initial
audit; later documentary changes require their own alias-aware delta check.

| Dependency or artifact | Independently checked coverage |
|---|---|
| Physical Round1 | Exactly 106 files, including its 105-entry manifest; all referents match and Round0/Round1 manifests are raw-identical |
| B context pins | All 134 physical final-A objects plus ten other contexts: 144 exact pinned referents |
| Supplemental source/read pins | Seven additional unchanged local records; separate from B producer inputs |
| Page pins | The exact seven expected page PNGs; hashes do not constitute new viewing |
| B initial runtime set | Exactly 106 + 144 + four B code/manifest roles = 254 unique referents |
| Each B replay-pair runtime set | The same 254 plus the already-existing canonical = 255 unique referents |
| B before/after snapshots | All three pairs byte-identical; all current referents rehashed |
| B's separate audit result | All 501 recorded consumed-object referents rehashed, not only the result file; its 313 inventory rows and complete parsed JSON-leaf counts checked |
| Recorded prior manifests | Every listed seal revalidated with the correct directory/workspace base; author source-input copies and historical A aliases handled explicitly |
| Initial root replay | Exact 119-object before/after snapshot, all real streams and new harness copy checked |

There were 43 manifest-validation invocations including repeated/overlapping
sets; this is not 43 disjoint packages. All 599 actually consumed objects
were rehashed again at the end. In particular, a canonical/receipt digest
was never used as a substitute for checking its declared referents.

## Mathematical-output and recorder provenance, not a new replay

The main assessor read all 507 lines of B `verify.py` and all 155 lines
of its recorder. Its direct imports are exactly `collections`, `fractions`,
`hashlib`, `itertools`, `json`, `sys`. Direct reading and the scoped AST
checks found no file input, dynamic loader, author/A/gate import, subprocess
or canonical lookup in that producer. This is a source inspection, not a
formal sandbox/security proof. The recorder and artifact auditor do read
comparison data, in separate disclosed roles.

All five archived B numerical processes have intact complete stdout,
empty stderr, source-only child directories and exact copied-source
identity. Every recorded producer/canonical comparison, both pairwise
comparisons and each canonical-live/input-before-after comparison was
checked against the real raw bytes. There are exactly 21 command records:
five producers, three runtime probes and 13 raw `cmp` calls. Their
recorded exits, stream hashes, copied source paths/cwd and actual
`-I -B` assertion-enabled probes agree. The initial canonical was created
only after the initial successful producer, while each later pair pinned
its preexisting canonical; those roles are not conflated.

The 1,558,382-byte canonical is complete producer stdout, SHA-256
`b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda`.
All eleven top-level fields and all 84,634 scalar leaves were parsed.
The structural checks cover all 20,115 unique changed sign records and
their census/shape; 37 determinant samples and all 37 coefficient slots;
60 formal traces; all eight n=3,...,10 boxes totalling 88,560 sources and
targets each; the complete labelled maximizer lists and height histograms;
six local-run rows; nine matrix-word boxes; 61 seed-only witnesses; and
four classical-attainer rows. Fixed identity bounds through exponent 100
are present in the inspected producer, not expanded into new carrier boxes.

Exhaustive inverse/source sets are validated by the producer and retained
as fingerprints in its output, not fully printed enumerations. The
canonical's completeness means full stdout, not a claim that every
intermediate enumeration was dumped. Its archived 2,158,999 assertions
and the separate audit's archived 12,845 checks remain separate counts;
the latter's recomputation of prior witnesses is not a B producer run.
This artifact audit did not rederive the theorem or recompute those
mathematical certificate witnesses.

## Root B context-name adaptation

The actual root controlled pair is
[p207_b_controlled/RECEIPT.json](root_replays/p207_b_controlled/RECEIPT.json).
Before that first B root pair, root changed the scoped utility to require
`CONTEXT_SOURCE_PINS.sha256` for A and `CONTEXT_PINS.sha256` for B. Its
exact recorded harness copy has SHA-256
`aa6eb9cccb7d0e9a4fc3ef662def02c506a7b7ce8dd9a4bf63d79ea76b9e462d`
and matched the then-current utility. Historical A harness copies remain
unchanged and are not relabelled as the new B adaptation.

All 14 actual root command records and their raw streams were checked,
including mandatory B context referent checks both before and after,
the isolated assertion-enabled runtime probe, two actual 2,158,999-count
producer outputs and their raw canonical/pair comparisons. The full
initial package stayed unchanged. These are root reproductions, not two
additional independent manuscript reviews. Root's old baseline stays
historical after the B evidence-only correction; aliases must be explicit.

## Source/build/view provenance and limits

The source-access log distinguishes successful pinned local reads,
metadata/abstract/preview contexts, failed web opens and unread theorem
bodies. I checked its local source referent pins and recorded scope; I
did not repeat those web searches or convert the log into a new primary
source read. Root's source/proof assessment is separate. Mukherjee's
convergence body and independent LNR-S1 remain unresolved; no artifact
check closes them or establishes global priority.

The actual B source-only build record is intact. All nine TeX/bibliography
source inputs equal frozen Round1 bytes. The helper's successful `set -e`
sequence, full stage logs, engine versions, four reproducibility settings,
BibTeX database/style evidence and final PDF are preserved. The B PDF was
raw-compared with the frozen seven-page PDF in this audit as well. The
last-pass `.fls` lists only the eight local TeX sources plus this build's
own aux/bbl/out; bibliography provenance is separately in the BibTeX log.
Thus those last-pass intermediates are not evidence of stale initial
build products. All 31 saved font objects are embedded Type 1.

The `.fls` also records 157 distinct absolute host-system input paths;
the package records engine versions and configuration, not a hermetic
historical hash snapshot of every system TeX file, bibliography style,
stdlib module or dynamically linked library. No such stronger claim is
made here. The actual isolated B runtime binary hash is intact; changes
to relevant host dependencies still require affected fresh checks and
cannot be cleared merely by rehashing the main producer/source files.

B's seven-page inspection record is explicit and separate from the
earlier build receipt's honestly preserved pending-view field. I did not
infer viewing from seven PNG hashes or claim a fresh visual review.
P207-B-ART1 must be acknowledged in the documentary delta, and the
terminal reports must accurately enumerate the warning and inspect the
affected page. Accepted B delta, Round2, two terminal source-only builds,
actual final-page views and final artifact closure remain later gates.

Write ownership for this task was only this report and its scoped
`p207_b_artifact_audit/` evidence. No B artifact, manuscript, freeze,
central index, historical evidence or Git state was edited by the assessor.
`OWNER_AMBER / HOLD_EXTERNAL` remains.
