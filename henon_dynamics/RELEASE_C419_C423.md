# C419–C423 external release approval and execution receipt

2026-09-08 UTC. This file is deliberately outside the exact payload root,
so approval and post-seal results can be recorded without rewriting a seal.
The actual root is:

```text
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423
```

## Completed scientific and manuscript gates

Five final PDFs contain 67 pages, with two actual full-manuscript reviews
per article, genuine revisions, final same-input build pairs and every-page
visual inspection. The coordinator read all review/build reports and
independently verified the five PDF pairs and 71 recorded TeX/Bib inputs.
See [five-paper delivery](research_c419_c423/README.md),
[review adjudication](research_c419_c423/REVIEW_ADJUDICATION.md),
[final builds](research_c419_c423/FINAL_BUILD_REPORT.md) and
[evaluation closure](research_c419_c423/EVALUATION_ADJUDICATION.md).

All five formal evaluations remain ROUTE_A_EXPLORATORY. C420 has
A4_FORMAL_HINT for genuine classical source scattering only; all 45 A2
metrics are NOT_TESTABLE, required A0 controls INCOMPLETE, and every
target/Route-B flag false. This is not human peer review, worldwide-priority
certification, external publication or a Hilbert–Pólya realization.

## Fixed tool and authorization boundary

Use the unchanged reviewed implementation at
continuation_c414_c418_round2/release/exact_payload.py, SHA256
529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f.
Its legacy schema c414-c418-exact-payload-v1 is a format identity, not the
new batch identity. The [reuse policy](research_c419_c423/release/README.md)
and [preflight](research_c419_c423/release/PREFLIGHT_REUSE.md) explain the
unchanged-code historical failure-path-test evidence and exact scope.
No old test or old payload seal is relabeled as a new execution.

The research baseline is 2974f8ea5f9e7cb0f8146cae017add38a6939da0.
Routine commit/synchronization to the configured repository is authorized;
new remotes, force-push, journal submission, third-party manuscript upload
and another research stream are not. Eight inherited unrelated untracked
directories and all older frozen packages must remain untouched.

## Exact inventory approval

The coordinator read all 306 lines of the final
[documentation review](research_c419_c423/release/REVIEW_DOCUMENTATION.md),
SHA256 3651f006aeaca9055ba9f8a378b708eb0ccbccaef1b670bd9a1b745f229a2f24,
and accepts PASS with zero outstanding mandatory items. Its 11 historical
snapshot-navigation exceptions are explicit and have working sidecar
navigation; the preserved original bytes remain unchanged. All package
writers, including the final reviewer and helper, confirmed stopped.

Only after that freeze, the fixed verifier's inventory command was actually
run from the repository root, capturing stdout outside the payload. It
exited 0 and produced a canonical 209134-byte candidate ledger containing
**1062 payload files and 66,117,408 payload bytes**. This includes the final
documentation report, all 801 paper-directory files, all ten manuscript
reviews, five final evaluations, three evaluation-revision files and every
retained research/scouting artifact. No ignored file was filtered out.
All-policy scanning passed; no invalid names, links, special files or empty
unrepresented directories required deletion or exception.

The coordinator reviewed the actual category/member inventory, root
documents and five final PDF identities against the accepted artifacts,
and approves the candidate's exact bytes for the absolute root above.
The **new externally approved ledger SHA256 literal**, fixed here before
any check/seal/verify invocation, is:

```text
82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14
```

The schema remains the explicitly reused format, and the fixed tool hash
above remains the trusted implementation. This approval does not derive a
new pin from a live installed ledger at verification time. The approved
candidate was installed through apply_patch and compared byte-for-byte
with the outside candidate, exit 0, before sealing. This approval section
was written before the separate actual seal results below.

## Actual seal, independent verification and synchronization

The following four actual invocations ran from the repository root using
the unchanged implementation named above and the exact absolute payload
root in this receipt. Inventory stdout was captured outside the payload;
all later invocations explicitly supplied the approved literal pin, not
a command substitution or a freshly selected live-ledger digest.

```text
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py inventory /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py check /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423 --ledger-sha256 82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py seal /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423 --ledger-sha256 82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14
python3 -B henon_dynamics/continuation_c414_c418_round2/release/exact_payload.py verify /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423 --ledger-sha256 82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14
```

All four exited **0**. Check, seal and the subsequent verify each reported
PASS for 1062 payload files and 66117408 payload bytes. Seal ran once, with
no failure or repinning. The final [manifest](research_c419_c423/MANIFEST.sha256)
contains 1063 lines: every payload file plus the approved ledger, excluding
itself. Its SHA256 is:

```text
6d4be9ad32e930f36f4aa5266f83dd4dbe39cb9b4fd8a0c0489afb45581fdcbc
```

The [ledger](research_c419_c423/PAYLOAD_LEDGER.json) excludes both root
metadata files. Adding those two to the 1062 payload files gives 1064
actual files. No package file has been edited after sealing; all later
records belong outside it. No payload was removed to satisfy the policy.

The independent post-seal check actually ran once at 11:31:44 UTC, exit 0,
without importing or calling the producer. The coordinator read the complete
[467-line independent report](RELEASE_C419_C423_INDEPENDENT.md), including
all 243 lines of the actual invoked code and its raw output, and accepts
PASS with zero discovered mismatch. Report SHA256:
322e37c3388603d57a7c7f25110d78bd7594e53578ed4bbd7c81dc17e3f9b3c9.

It independently confirms 1062 payload files / 66117408 bytes, a 209134-byte
ledger, a 136358-byte manifest with 1063 entries, and 1064 actual regular
files totaling 66462900 bytes across 181 nonroot directories. Exact member
sets, every length/digest, strict JSON, canonical manifest and the external
literal pin agree. Three metadata/member snapshots and two full content
passes are identical; no missing/unexpected member or forbidden type was
accepted. This is one actual audit invocation, not a universal attack test.
The report and its full code are outside the payload. No package write
occurred after sealing. Mathematical/source and human-review limits remain.

## Git integration and exact staging

After all release gates closed, an actual `git fetch origin` succeeded.
The configured `origin/main` had advanced by seven commits from the research
baseline to `7d43cb323adf7d27326263b8ce4158d4eefff43a`. A read-only check
consumed all 15328 changed paths and found no overlap with the entire
`henon_dynamics/` stream, the three inherited untracked root directories,
repository/stream instructions, or the fixed evaluator. The remote changes
belong to the independent symbolic-dynamics stream. The five inherited
untracked directories within `henon_dynamics/` were covered by the whole-
stream exclusion. No inherited material was staged, moved or removed.

`git merge --ff-only origin/main` then actually exited 0, and HEAD was
verified as `7d43cb323adf7d27326263b8ce4158d4eefff43a`. This is a safe
integration baseline, not a replacement for the recorded scientific
baseline `2974f8ea5f9e7cb0f8146cae017add38a6939da0`. No force operation,
new remote, other-stream research edit or payload edit was performed.

Both exact staging invocations actually exited 0:

```text
git add -f -- henon_dynamics/research_c419_c423
git add -- henon_dynamics/CURRENT_RESEARCH_STATE.md henon_dynamics/docs/candidate_registry.md henon_dynamics/docs/obstruction_registry.md henon_dynamics/RELEASE_C419_C423.md henon_dynamics/RELEASE_C419_C423_INDEPENDENT.md
```

The coordinator then read all actual staged Git blobs through
`git cat-file --batch`: the 1062 payload entries match every approved
ledger length/SHA256, both root metadata files match their fixed lengths
and literal hashes, and the five intended outside files match their
worktree bytes. The exact staged set is 1069 paths, every mode 100644;
the initial audit read 67210342 blob bytes. Updating this outside receipt
after that audit does not change any sealed or independent-report byte.
The affected receipt is restaged separately before committing.

A nonauthor independently audited the staged names/status/modes after
INDEX_READY using read-only Git commands, without rerunning the blob,
payload, mathematical or build checks. Its actual result is PASS:
1069 exact paths, zero missing/unexpected, 1066 additions and three
modifications, all stage 0 and mode 100644, no other tracked worktree
change, and exactly the eight inherited untracked directories with no
indexed descendants. No new research file in another stream is staged.

The unrestricted `git diff --cached --check` actually exited 2, not PASS:
368 cosmetic whitespace findings in 81 preserved files (340 trailing
whitespace and 28 final-blank-line findings). Of these, 69 occur in `.aux`,
281 in `.log`, 17 in recorded `pdfinfo.txt` outputs and one is the final
blank line of the accepted independent report. There are no other
affected extensions. The four coordinator-edited outside documents pass
the scoped whitespace check with exit 0. Sealed generated bytes and the
independent report's accepted identity were preserved; no exemption rule
or payload rewrite was used to manufacture a clean lint result.

Commit and push are the remaining synchronization actions. Their real
results will be appended after execution. The final checkpoint remains
C423; no C424 work is authorized by this release.
