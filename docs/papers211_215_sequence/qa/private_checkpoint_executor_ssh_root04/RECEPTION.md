# Checkpoint03 SSH delta04 — root source acceptance

2026-09-09 UTC. SOURCE_ACCEPTED_WITH_DECLARED_LIMITS.
HOLD_OPERATIONAL / OWNER_AMBER / HOLD_EXTERNAL. No diagnostic or checkpoint
phase is enabled by this source receipt.

Root accepts the exact 804-line / 47,072-byte source, SHA256
32900d88796c8dcc0dceda62f7d650be184d104202b2dea0ca257d356d65db48,
under its [source contract](../private_checkpoint_executor_ssh_delta04/SOURCE_CONTRACT.md)
and the [actual independent delta report](../private_checkpoint_executor_ssh_audit04/REPORT.md).
The 774-line old implementation and its
[accepted nonauthor baseline](../private_checkpoint_executor_source_root03/RECEPTION.md)
remain unchanged. The old author reviewed only the new two-change delta,
not his own unchanged code; this disclosed boundary was agreed before judgment.

## Substantive source result

The entire new implementation was read in three complete slices. The current
source equals precisely two replacements in the accepted old source: the
PREP/SELF package location and the fixed GIT_SSH_COMMAND. The command has
-F none, -a, -x, -T and 31 distinct -o fields, with all four old fields retained.
Source concatenation, policy, independent field table and disabled D02 prefix
agree exactly. All non-SSH/PREP text, selected scope, endpoint and phase logic
remain unchanged. This is source-text analysis, not Python import, AST, test,
executor run, new selected-data capture or live remote verification.

The scope remains the previously chosen 43-closed snapshot of 8,207 files /
386,716,363 bytes, 178 core plus four bridge groups, 8,204 additions / two
modifications / one unchanged / zero deletions. It does not include this
receipt, current 50-closed controls or later unselected P212 work.

Under the referenced released OpenSSH semantics, CheckHostIP=no suppresses
the otherwise possible known-IP insertion even after a known host matches;
StrictHostKeyChecking=yes refuses a new key. Separately, UpdateHostKeys=no
returns before the later host-file replacement loop.
[Initial host branch](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect.c),
[later update branch](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/clientloop.c).
These are conditional source conclusions, not this machine's installed
defaults, host verification or no-side-effect observations.

The independent OBS01 is accepted as a mandatory future receiver constraint:
the option dump omits some cleared string fields, and conditional build
fields differ. A field's absence is not automatically success; every intended
semantic field needs an explicit installed-source/output disposition.
[Released string-dump branch](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/readconf.c).
Suppressing local security-key providers does not suppress arbitrary retained
agent internals or prove that existing noninteractive authentication works.
[Released authentication paths](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect2.c).
No blocking source finding remains in this exact bounded delta; all runtime
and installed-semantics holds survive.

## Actual original reception

The corrected source-data receiver receive03.cjs returned native 440f8f,
exit 0: 1,756 checks, 47 complete workspace byte/SHA/ten-field stable keys,
and 35 complete native read matches covering 476,642 bytes. It checked both
complete nonself packages (15 author and 13 independent payloads), all seven
author and 22 independent input pins, both full source representations,
all final author key lists and the actual independent 22-key before/after
outputs. It parsed each package JSON as data and checked original full JSON
read returns, without running commands stored in those originals.

Root's actual ordinary diff 00f67f returned the expected exit 1. All 2,684
returned bytes equal both the author's and the independent reviewer's actual
patch files. It has exactly two hunks. Complete original source/prose selected
reads are in ROOT_SELECTED_READS_NATIVE.json; raw native archives were parsed
and checked as data, not claimed to have been manually read line by line.
The separate prior private runtime receipt remains accepted but its raw
private originals were not reopened for this source reception.

Two actual root document-receiver failures remain unchanged. receive.cjs
assumed every saved document record carried a path field; the last instead
contains an explicit old-contract sed request. receive02.cjs fixes that exact
record but then incorrectly compares a pre-jq scope read to the later scope
with its added jq-failure disclosure. receive03.cjs recognizes only that exact
365-byte later paragraph in the historical comparison; the separate final
scope read must still equal the whole current file. Reports and source are
unchanged. Both failed native returns, diagnostic comparison and all three
receiver sources are retained. Original author failed paths, independent
path failure and jq-unavailable exit 127 also remain preserved.

## Finite next gate and limits

The five accepted baseline limits remain: ordinary startup/role acceptance
is external; time bounds are per native handling rather than a whole-phase
SLA; early failures can precede artifacts; exclusive finite regular-file
attachment is not hostile concurrency isolation; and native, remote, CAS and
root-reception outcomes are separate. New SELF/hash, runtime premises and
every future phase binding must identify this source without a hybrid.

D01 version-only and D02 option dump remain disabled and mutually separate.
Root may next receive a compact ordinary-trusted D01 direct-argv launcher,
choose exact private capture and finite owned-process handling, then grant
only that diagnostic. This does not require an observer-of-observer chain,
but a banner cannot certify vendor-source correspondence or option support.
D02 additionally requires its explicit installed-branch decision; the old
no-G gate is not waived. Neither diagnostic automatically opens Git phases.

No SSH/Git command, host-role/config/environment/private-original read,
observer/probe, enabled phase, scientific replay, manuscript build, settings
change or external release occurred here. Ordinary Node documentary readers
were executed and are explicitly recorded. Counts remain two retained /
one complete / three open seats / 50 closed attempts. Complete root closing
keys and the nonself seal are required to finish this source receipt.
