# C424–C428 external release approval and execution receipt

2026-09-09 UTC. This record is outside the exact payload root so later
approval, seal and Git results can be recorded without editing sealed
bytes. Current stage: scientific/manuscript/evaluation/final-build,
final-documentation, exact seal and independent member-verification gates
complete; Git synchronization pending.

## Scientific and final-document gates already completed

Five independent papers have final PDFs, 72 pages (21/12/10/13/16), two
actual nonauthor manuscript passes per paper, genuine required/optional
revisions and no-change second-round aliases. Every final PDF was built
twice in fresh directories with fixed reviewed inputs, with byte-identical
outputs and all-final-page visual inspection. The coordinator read the
ten complete reviews and five final build reports and independently
checked 77 reproducibility inputs, final/reviewed PDF aliases, both
final copies' fonts/pages and 20 converged logs. No old mathematical
certificate was rerun in the manuscript/final-build/release stage.

See [five final papers](research_c424_c428/README.md),
[manuscript closure](research_c424_c428/REVIEW_ADJUDICATION.md),
[final builds](research_c424_c428/FINAL_BUILD_REPORT.md) and
[evaluation closure](research_c424_c428/EVALUATION_ADJUDICATION.md).
All five are ROUTE_A_EXPLORATORY, A0_WEAK; C426 is static A1_FAIL and
the others A1_WEAK; A2/A3/A4 all FAIL with target evidence NOT_TESTABLE.
All 45 A2 metrics are NOT_TESTABLE, A0 controls INCOMPLETE and all
target/Route-B flags false. Internal AI-assisted review is not human
peer review, journal acceptance or worldwide-priority certification.

## Fixed release implementation and root

The unchanged reviewed implementation is
`continuation_c414_c418_round2/release/exact_payload.py`, SHA256
`529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f`.
Its legacy schema `c414-c418-exact-payload-v1` identifies the reused
format, not the current batch. The explicit approved-scope root is:

```text
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c424_c428
```

[Release policy](research_c424_c428/release/README.md) records full
source/test inspection, actual unchanged hashes and reuse of the old
21+21-method failure-path receipt. This is not a claim that those old
tests ran anew or that the old payload seal applies to this tree.
Every new-tree check/seal/verify must actually run with a newly approved
literal pin. Existing manifests will not be overwritten.

All actual historical files are to be preserved, including ignored
logs, rendered pages and the existing IH6 Python cache. Keeping that
bytecode records actual tree membership; it does not import it, count
it as a new mathematical execution or certify portability. Ordinary
Git-ignore filtering is not an acceptable payload-member selector.

## Research baseline and actual remote inspection

Research baseline: `2895b07238d4cef2ed35faaad251e4cfceb08ec1`.
The configured branch is main, tracking origin/refs/heads/main.
The actual `git fetch origin` exited 0; the subsequent
`git rev-list --left-right --count HEAD...origin/main` returned `0 0`.
Both refs resolved to the research baseline. There was no remote
advance or overlapping change to integrate at that check. The selected
evaluator still has SHA256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
repository instructions, evaluator and earlier sealed packages remain
unchanged. Only this batch and specified Hénon indexes/receipts are in
scope, not the eight inherited unrelated untracked directories.

Routine exact-path commit/synchronization is authorized; no new remote,
force push, other stream, journal submission, third-party manuscript
upload, Route B or C429 is authorized. No commit or push is claimed at
this write. Exact approval and actual execution results follow only
after the remaining documentation writers stop.

## Final documentation closure and quiescence

The coordinator read the full 368-line tree preflight, 121-line historical
navigation overlay and 322-line bounded integration review. Their SHA256
identities are, respectively:

- `c3a0a2bd8adb80f4915e6e3c210b360b7cec7a4a44d80b9f6a8bbc635b87f742`
- `609eb5b29cb6c4e692d6e09835a6ad1ef9603ca4eb5a2b2d364fcb99239ec285`
- `53908c308400cd66a8f89bc6b8db648e5fc329cf16cb172c1bf4013a63665f7c`

See [tree preflight](research_c424_c428/release/PREFLIGHT_TREE.md),
[historical-link overlay](research_c424_c428/release/HISTORICAL_NAVIGATION.md)
and [integration review](research_c424_c428/release/REVIEW_INTEGRATION.md).
The 40 historical literal-link exceptions are disclosed and mapped without
rewriting frozen copies. The integration review identified one genuine
registry quantifier omission: HEN-O409's periodic-line statement needs the
orbit to meet the complement of the proved core box. The coordinator made
that single registry correction and the reviewer independently closed it.
There are zero open required integration corrections; no paper or code
changed. The coordinator adopts this bounded disposition, not a new proof
certification or seal. All package writers have explicitly stopped.

A fresh standalone `git fetch origin` exited 0. At 2026-09-09 10:51:47 UTC,
HEAD and origin/main still equal the research baseline above and the
left/right count is `0 0`. An earlier combined diagnostic ended with exit 2
only because it tried to read the then-unwritten integration report; no
fetch failure or altered research artifact resulted. No remote change
needs integration. Exact approval and seal results will follow below.

## Literal inventory approval — recorded before check and seal

With all writers stopped, the unchanged tool's actual `inventory` action
exited 0 and produced the candidate outside the root at
`/tmp/c424_release_PcDhlv/PAYLOAD_LEDGER.candidate.json`. The coordinator
read all 5,792 candidate lines through bounded chunks, parsed the complete
member list, and reviewed its directory/extension totals, root and release
members, largest files and explicitly retained bytecode against the tree
preflight and completed artifacts. No member was silently dropped.

The approved canonical ledger is **229,388 bytes**, listing **1,157 payload
files and 81,980,859 payload bytes**. The five paper directories contain
222/242/120/162/214 members; the other 197 members retain the actual
scouting, round-two through round-six continuations, evaluations, reviews and release
documentation. The exact inventory includes 56 PDFs, 265 rendered PNGs,
19 source archives and the single 6,936-byte historical IH6 cache with
SHA256 `26d59b5833e6cda61d4cf768cbbbfe0818ba3b6fb2e6196d3c38f779b295fb87`.
These are artifact counts, not counts of new papers, experiments or
independent mathematical results. Earlier preflight totals preceded the
reviewer's final self-documentation and integration report; they are not
the final approved totals.

The coordinator explicitly approves this literal ledger SHA256:

```text
0441eb689728c3ca06b4ba63ebaee62af0676d69c57a1c7f123c5df95caa4fc0
```

Use that fixed value, not a newly calculated live hash, in every actual
check/seal/verify and independent validation. The approved ledger excludes
only its own root name and the root manifest. Install the reviewed bytes
using apply_patch, then compare against the outside candidate. This
approval authorizes the exact local integrity seal, not a mathematical or
external-publication claim. At this entry's write, no seal has run.

## Actual check, one seal, and post-seal verify

Completed by 2026-09-09 10:56:13 UTC. The approved 229,388-byte candidate
was installed with apply_patch and `cmp` against the outside candidate
exited 0. Three separate actual invocations of the unchanged tool then
ran with `python3 -B`, the explicit absolute root and the same previously
approved literal pin above:

| Action | Actual exit | Actual result |
| --- | ---: | --- |
| check | 0 | PASS; 1,157 payload files, 81,980,859 payload bytes |
| seal | 0 | PASS; one new manifest, no overwrite |
| verify | 0 | PASS; exact post-seal members, bytes and canonical manifest |

The seal is the only manifest publication for this tree. Its
MANIFEST.sha256 is **149,896 bytes / 1,158 rows**, SHA256
`bbaa5b44994c032c663155f6eb72789fb28d3d8f82ed14d24e33bbe78b648f3e`.
It includes every payload member and the approved ledger, and excludes
only itself. The sealed directory therefore has 1,159 regular files and
82,360,143 total file bytes including both metadata files. No in-tree
receipt, program run or build follows the seal. Independent reconstruction
of actual membership/bytes is a separate pending check, not inferred from
this tool's successful verification. All later receipts stay outside.

## Independent verification accepted

The separately authored [independent report](RELEASE_C424_C428_INDEPENDENT.md)
records one actual Python 3.12.3 `-B` standard-library invocation completed
at 2026-09-09 11:05:15 UTC, exit 0, with zero unresolved findings.
The coordinator read its complete 347 lines, including the complete
executed checker and actual output, and measured report SHA256
`26b1db8b7113b0d6b3b79ee517127b904706b2930a9dffdfae51af543d37e828`.
The report is now kept unchanged; subsequent Git checks do not append to
it or retroactively claim a staged-index result at its execution time.

The independent implementation uses os.fwalk and descriptor-relative
nonfollowing reads, without importing/invoking the production verifier.
It measured every actual name, byte length and digest, checked strict
canonical ledger structure against the same prior literal pin, rebuilt
the manifest from measured payload members, and matched all 25 frozen
PDF aliases/final copies against five pre-ledger anchors. It also checked
all six root/ancestor directories and exactly 162 represented subdirectories.
Totals agree: 1,157 payload members / 81,980,859 bytes; 1,159 complete-tree
files / 82,360,143 bytes with metadata. The coordinator adopts this bounded
independent PASS. No mathematical run, PDF build, in-tree write, old test,
new authenticity claim or Git publication is inferred from it.

The exact intended staging list has 1,164 literal paths: all 1,159 sealed
members and exactly five outside files (current state, candidate register,
obstruction register, this receipt and the independent report). Ignored
members are intentionally included. The eight inherited unrelated
untracked directories remain outside this list. Stage/object checks and
actual commit/push results will follow only after execution.

## Actual first staging and two object audits

The explicit 1,164-line literal path list was staged with `git add -f
--pathspec-from-file=/tmp/c424_release_PcDhlv/stage_paths.txt`; exit 0.
The five outside documents passed the scoped cached whitespace check.
Historical source/build bytes were retained, not reformatted to satisfy
a broad whitespace cleanup. Only this approved package and its five
outside documents were staged.

The coordinator's actual read-only Python `-B` audit completed at
2026-09-09 11:09:12 UTC, exit 0. A separate reviewer independently
audited the unchanged index at 11:10:29–11:10:31 UTC, exit 0. Both used
the actual cached changed-set and stage entries, then read all actual
staged blob contents with `git cat-file --batch`, not just filenames.
All 1,164 blobs match working-tree bytes and lengths/SHA256; the sealed
1,159 additionally match the previously pinned ledger and manifest.
All entries have stage 0 and Git regular mode 100644, matching the
workspace executable bits. The independent implementation also
recomputed each Git SHA1 blob-object identity and checked that the
complete index and cached changed-set remained stable across its audit.

Actual shared snapshot totals: 1,161 added / 3 modified paths,
83,125,043 staged bytes = 82,360,143 sealed-tree bytes + 764,900 outside
bytes. There were zero unexpected staged paths or unstaged tracked
changes. The eight inherited unrelated directories remain untracked
and unstaged. The independent report remains unchanged at its recorded
347 lines / 16,338 bytes / `26b1db8b...37e828` identity.

For this first snapshot, sorting `mode + space + oid + space + path + LF`
gives SHA256
`6f6972591e6d18ef98b281f427ccd742cdb648428998ccd235b54ab59026011d`.
This is a review-time index fingerprint, not a replacement for the
external payload approval pin. This new receipt section changes only
its own outside file, so the coordinator must re-stage it and perform
the final complete index/blob comparison before committing. The totals
above describe the audited prior receipt version; no self-referential
final index hash or future commit/push result is preclaimed here.
