# P211 BLD-I1 independent revision verdict

2026-09-08 UTC. Same auditor: `/root/p211_runtime_independent_audit`.
**BLD-I1 RESOLVED FOR REVISION01; PENDING EXACT ROOT BINDING.**
No new concrete blocker was identified in the changed code or dependency
delta. This is a revision-specific infrastructure verdict, not permission
to execute a build and not build, manuscript or terminal acceptance.

The [original report](../p211_build_independent_audit/REPORT.md) remains
unchanged, including its Major/open conclusion for the original preparation.
All 50 original audit payloads and its manifest were independently checked.
This separate verdict does not retroactively repair or relabel that package.

## Why BLD-I1 is resolved

The complete current five operational files, standalone infrastructure
fixture and original report were read, together with all five actual
final-original-to-revision diffs. In the revised
[build_core.py](../p211_build_revision01/build_core.py), `settled` starts false
at line 216. Only a returned handle and the owned-session settlement path
can change it. At lines 262–272 the no-handle outcome is explicitly UNKNOWN,
has null native exit and false stream settlement, writes UNCLOSED, then
raises before line 273's final hashes, INPUTS_AFTER or RECEIPT creation.
No exception-type exemption asserts that absence of a handle means absence
of a native writer. The unchanged core and enclosing inner/outer guards
reject UNCLOSED or incomplete attempts.

The focused saved regression is a real CPython audit-hook refusal before
Popen returns, not a mocked receipt. Its exact event/argv/environment and
traceback match the retained unknown attempt. The installed
`/usr/lib/python3.10/subprocess.py` was independently inspected and pinned;
its POSIX audit event at line 1735 precedes both native-creation branches.
The fixture uses that controlled precreation event and does not explicitly
fork or create an escaped writer. Thus this regression reaches the corrected
no-handle branch safely; it is not a general unknown-writer settlement test.

The refused call still has ATTEMPT and UNCLOSED, false settlement, no final
stream-pin field, no SPAWNED, no INPUTS_AFTER and no RECEIPT. Saved real
fixture output records native-seal refusal at the unknown subtree and its
two enclosing levels. None has acquired a native SHA256SUMS. A separate
ordinary child produced the exact `known stdout` and `known stderr` lines,
returned native exit 0 and had no remaining owned-session members or
interventions. Its normal known-handle subtree is complete and sealed.

The enclosing fixture's own actual receipt records native exit 0 and a
quiescent owned session. The saved product-tool envelope independently
corresponds to completed exit 0 and the exact fixture RESULT. This justifies
a post-completion **documentary snapshot of this controlled package**, not
a native seal or discharge of its intentionally UNKNOWN subtree.
`DOCUMENTARY_SHA256SUMS` preserves that distinction. It cannot authorize
finalization of a general unknown, detached or escaped writer.

## Delta and evidence

[RESULT.json](RESULT.json) records **922 checks**, **353 complete read inputs
/ 2,850,303 bytes**, **34 completed saved native receipts**, one deliberately
incomplete unknown attempt, and **10 fresh read-only native commands**.
Every complete receipt's literal attempt fields, spawned identity/times,
actual expected exit, ENV8, session settlement, unchanged direct-input
inventories and full separate raw stdout/stderr hashes were checked.
Five new actual cmp commands confirm physical executed adapter equality;
five actual diff commands reproduce every saved delta byte and native exit.
Original raw outputs and fresh real exits are retained in `native/`.

All **290 revision payloads** were verified under documentary manifest
SHA-256 `3aa7db50e9d6039686db3b647e50b9bd021f7b6b3785103888e7f58489176b30`.
The 61-, 187- and 8-payload native sub-manifests are fully checked. The
original preparation's supplied 891-payload manifest pin still matches;
this delta audit verifies only seven selected payloads within it, not all
891. The producer's own broader audit is not treated as independent proof.

The exact revision candidate is
[DEPENDENCY_LOCK.candidate.json](../p211_build_revision01/discovery01/DEPENDENCY_LOCK.candidate.json),
570,037 bytes, SHA-256
`bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec`.
Its five current code pins equal the physical executed copies and both
saved before/after inventories. The configuration still contains 840 path
spellings, 795 file entries and 33 unchanged selected ELF paths. Comparing
the full old/new entry maps, the only removed/added path is the relocation
of byte-unchanged `prepare_build.py`; no shared entry changes. Exact ENV8
and the three separate future-cwd ABSENT roles are unchanged. The nine
science-source metadata pins equal the old candidate and saved closures;
their physical bodies were not read in this infrastructure review.

`prepare_build.py` and `build_p211.py` are byte-for-byte unchanged.
The remaining deltas are the narrow recorder correction, versioned path
and final-original diff baseline, and explicit historical diagnostic path
in static checks. The fixture is standalone, not a new production import.
No ordered-command, FLS/BibTeX, page/font/render measurement or source-graph
redesign was introduced. The actual diagnostic session 55993 completed
with exit 0; its exact full tool output matches RESULT and native seal.

[READ_INPUTS_BEFORE.json](READ_INPUTS_BEFORE.json) and
[READ_INPUTS_AFTER.json](READ_INPUTS_AFTER.json) are equal complete byte/hash
inventories. [TOOL_RETURN.actual.json](TOOL_RETURN.actual.json) is the actual
decoded checker request/return, not invented outer stdout/stderr files.

## Scope and remaining gate

Root must separately finish receiving the exact current code, fixture,
candidate, actual science/source graph and applicable evidence, then issue
a new exact binding and actual root-read receipt for this version. The old
binding cannot authorize changed code. BINDING.pending remains disabled.
Existing ENV8/Python isolation, future-cwd binding, fresh-output/no-retry
and HOLD_EXTERNAL restrictions are not waived.

No submitted script was executed or imported by this auditor. No TeX,
science, old builder or canonical body was executed/read; no rendering,
process stress test, cleanup, Git, external action or original mutation
occurred. Host dependency referents were not generally recaptured; the
single installed subprocess source was inspected only for the documentary
fixture's precreation premise. No central index was read during this delta
audit, avoiding reinterpretation of refreshed controls as historical pins.

Project and paper-compile skills were used for versioned evidence,
preserved native records, source/configuration closure and separate
acceptance gates. The explicit read-only task keeps compilation, repair,
cleanup, retry, page viewing and manuscript review out of scope. This
auditor did not delegate the verdict or contribute to the producer's fix.
