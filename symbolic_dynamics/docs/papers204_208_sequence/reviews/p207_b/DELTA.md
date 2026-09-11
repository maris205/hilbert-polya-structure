# P207 actual B delta — accepted scientific no-change and documentary repair

2026-09-06 UTC. Same actual B reviewer: `/root/batch197_fifth_scout`.
**MATH_VALID / ACCEPT_EXACT_SCIENTIFIC_NO_CHANGE_WITH_DOCUMENTARY_REPAIR.**
Current open Critical / Major / Minor: **0 / 0 / 0**.
Resolved after the initial report: **0 / 0 / 1**, namely P207-B-ART1.
`OWNER_AMBER / HOLD_EXTERNAL` remains. This accepts the precise B delta;
it does not create Round2, a terminal build/view gate or batch completion.

## Actual response and exact unchanged science

I read root's actual [original response](../../P207_B_RESPONSE.md), SHA-256
`d1e3f7b0ede25f375269ebedaa84c12558f7055322dfe905379974e05dbd3244`,
and its separately preserved [supplement](../../P207_B_RESPONSE_SUPPLEMENT.md),
SHA-256
`a3e3c2a36388291240f12055d44a2a4c281b3ee94800b76fa20e87124c874294`.
The original proposal was not treated as an acceptance. The later real
artifact finding was checked before this decision, not retroactively
inserted into the initial zero-finding census.

All **105 scientific/documentary inputs** in physical Round1 remain
byte-identical, including TeX, bibliography, proof/source/framing notes,
author verifier/canonical/executions and PDF. Its 105-entry manifest still
has SHA-256
`8d134689f8c07f9bcac65b4576a5bfca2e073ece6281f9d893148f12adb43f5d`.
The exact 106 physical freeze inputs, including that manifest, pass
[after pins](INPUT_PINS.after.sha256), raw-identical to the original
`INPUT_PINS.sha256`. All 105 live counterparts pass
[live after pins](LIVE_SCIENTIFIC_PINS.after.sha256).
The 144 context inputs, seven supplemental reads, nine build sources
and seven previously viewed page images are unchanged and verified.

The standalone B mathematical producer remains SHA-256
`8c364da4c9bdaa206910f95357cf813f544454fbceb021f89b8e79d09906c44a`;
the complete 1,558,382-byte canonical remains
`b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda`.
The seven-page PDF remains
`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.
No scientific source, mathematical producer, canonical, PDF or rendered
page was edited during this delta.

## The real Minor finding and its checked correction

The independent artifact-only assessor identified P207-B-ART1 in the
initial B build report. I personally read that original paragraph,
`cold_build_01/main.log` line 638, `pass3.stdout` line 88 and the helper's
actual scanner. The log contains one `Underfull \vbox (badness 1038)`
before the page-4 marker. The helper searches `undefined|Overfull|Warning`,
so an empty `DIAGNOSTICS.txt` did not establish absence of `Underfull`.
This was a real evidence overstatement, not a mathematical failure or
an inferred clipping defect.

The exact initial [build report](BUILD_REPORT.initial.md) is preserved,
SHA-256
`720bdff977f12339909dc02b7f2a60a51c1b52a2e7991349975e7e38cb50d7e0`.
The corrected [live report](BUILD_REPORT.md), SHA-256
`378c974ae2e42db9e565cba36a484e67c9387ead80bc53a52d76f5cdd5903327`,
enumerates the actual warning and exact scan scope, retains all original
logs and page-view statements, and explicitly claims no new build/view.
I checked the actual textual diff and direct complete final-log search.
The later-open finding remains in [FINDINGS.delta_open.json](FINDINGS.delta_open.json);
its now-resolved disposition is in [FINDINGS.json](FINDINGS.json).

`REPORT.md` is unchanged and has a byte-identical `REPORT.initial.md`.
The zero-finding `FINDINGS.initial.json` and original `SHA256SUMS.initial`
also remain intact. The latter's initial 118 entries have SHA-256
`6f103d933c8135563b00734d8850ce36bf2fc47aa504d669e01cf6c99ef29074`.
Historical references to mutable `BUILD_REPORT.md`, `FINDINGS.json` and
`SHA256SUMS` resolve explicitly to their initial aliases, never to invented
unchanged live bytes. Every other original initial-review object remains
unchanged.

## Artifact assessor, actual stops and transport distinction

I read the complete [closed artifact report](../../qa/P207_B_INITIAL_ARTIFACT_AUDIT.md),
its complete 402-line checker, preserved failed tool outputs and source
content differences, complete result and referenced evidence. The actual
result has **39,623 checks / 599 consumed objects**, with P207-B-ART1
still open on the initial package; it is not relabelled a clean initial
PASS. Its two stopped checks remain preserved. The first stopped after
five in-progress B additions changed physical directory membership; the
second exposed the real underfull overstatement. Neither was mathematics.

The 599-object record includes a then-provisional B delta utility. Its
exact recorded 11,515-byte version is preserved as
`check_delta_artifacts.initial.py`, SHA-256
`7c53fb7e1f857bf4fc599a67cbce7c206eea1f905b42edb7f3a261592381a1a7`.
My later check explicitly maps that one historical path to this alias;
it does not claim the current utility is unchanged or count its source
development as mathematical evidence. All 599 historical consumed
referents were rechecked under the stated aliases.

My actual delta audit first stopped on the difference between the
assessor's captured output length, 147,133 characters, and its 147,134-byte
saved JSON. That stop and its executed utility are preserved in
[DELTA_AUDIT.attempt_01.actual.json](DELTA_AUDIT.attempt_01.actual.json)
and `check_delta_artifacts.attempt_01.py`. The assessor then produced an
actual [packaging supplement](../../qa/p207_b_artifact_audit/PACKAGING_SUPPLEMENT.md)
and recovered its retained exact captured stdout separately. I checked:

```text
old archived JSON bytes == exact captured stdout bytes + one LF
```

The old file remains SHA-256
`457e3da885163d5888a95aa165f34e53580a687c63ada34d43f2568cb4ec46aa`;
the exact 147,133-byte sibling is
`5f5487bad8a7c11c73b6a6adb251f90bfa365be42ec91d4b6152ed965b334afd`.
Their parsed JSON equality is separately checked, not substituted for
raw equality. The original tool-output roundtrip and distinct byte sizes
are in the assessor's actual correction receipt. Its two old failed-code
snapshots similarly preserve source content/version with an added final
blank line, not unrecorded byte-exact historical source hashes. That
limitation stays explicit. No old output, snapshot or seal was overwritten.

The 49 [response/root/utility pins](RESPONSE_AND_ROOT_REPLAY_PINS.after.sha256)
cover both root responses, all 33 root replay objects, the utility report
and live root harness, and all twelve initial/supplemental artifact-audit
objects. The earlier 45-object pin list is also preserved. The old utility
seven-entry seal plus its separate three-entry supplement pins both pass;
their union covers the current twelve-object utility directory including
the two pin lists.

## Actual delta verification and prior mathematical evidence

[DELTA_AUDIT.json](DELTA_AUDIT.json) is the complete actual output of the
read-only [delta checker](check_delta_artifacts.py), not another
mathematical producer. Its [execution receipt](DELTA_AUDIT.actual.json)
records a successful run with **5,258 checks**, **727 actually consumed
objects rehashed before/after**, and **23 actual commands**. All expected
outcomes passed: thirteen hash-check commands and eight raw `cmp` calls
exited zero; the direct log search exited zero; `diff -u` exited one as
expected because the requested documentary correction exists. This last
status is not mislabeled a zero-exit comparison or a failed check.
The output is 396,230 bytes, SHA-256
`9afd66c12a4e02db1b2c6e2d0f0e2a0c393d936a7f2202fba66e146f09f2a749`;
an actual read-only roundtrip confirmed its file equals the complete
captured tool stdout, including trailing bytes.

The full initial B five-run evidence remains intact: each real producer
passed 2,158,999 assertions. Root's new controlled pair independently
reproduced those bytes twice; I checked all 14 real root command records,
raw streams, runtime binary hash and assertion-enabled `-I -B` probe,
before/after referents and the unchanged historical 119-object package
snapshot. Those two processes are root reproductions, not two more
independent reviews or fresh B processes. No mathematical verifier,
build or image viewer was run during this documentary delta. Existing
mathematics/build/view evidence is reused only for unchanged recorded
dependencies; no hermetic historical TeX/stdlib/library snapshot is claimed.

## Accepted scope and remaining gates

P207-B-ART1 is resolved by this checked documentary repair. There is no
current open P207 Critical/Major/Minor finding. Mukherjee's unread
convergence body, separate LNR-S1, the nonsharp computer-assisted global
clock, all deducted static/complement/classical mechanisms and the
one-rank-family-seat limit are unchanged. No sharp global height,
larger-alphabet theorem, all-time inverse, basin census, global priority
or external release is accepted. New applicable source evidence or a
changed scientific/runtime dependency reopens its affected scope.

Root must still inspect this actual accepted delta and final complete
review seal before physically freezing Round2 and performing the
remaining terminal paper gates. Terminal reports must enumerate the
underfull warning and actually inspect the affected page. This reviewer
edited only the B directory, not science, A, frozen sets, central indices
or Git. The review remains internal process-separated nonauthor review,
not blind, external or human-specialist review.
