# P208 lifecycle-only follow-up

2026-09-07 UTC. **PASS_P208_LIFECYCLE_ONLY_FOLLOWUP**.
The [actual attempt_01 command](lifecycle_01/attempt_01/COMMAND.json) exited
zero with empty stderr, unchanged executed source and an absent bytecode
prefix. It passed 1,697,335 artifact checks. The complete
[stdout](lifecycle_01/attempt_01/audit.stdout) is 23,456,613 bytes, SHA256
`cd975a507d758af1e166a57f50060e62aea3488fe89d94abe5ae45b8d8bad67d`.
No new mathematical producer, manuscript review, delta acceptance, build,
renderer or page view was performed.

## Exact permitted change

Root [accepted the initial terminal artifact gate](../P208_TERMINAL_ROOT_INSPECTION.md)
after inspecting its originals and independently rechecking all 115,334
input paths twice. Root then changed only the paper's separate lifecycle
file and its corresponding whole-paper-manifest line.

The complete paper directory still has exactly the original 2,178 payload
paths, with no addition or removal. `PAPER_STATUS.md` is the sole changed
payload; its new SHA256 is
`31b404fa539c5b67c02395d30f5a4aa677bd82f77d8d7df76a85d82ac0d07e01`.
The new whole-paper manifest SHA256 is
`0cb42abfb9e639920a973d412ffc7ab2e418df4c26819c6a0d4719007a273e46`.
Its bytes are exactly the original manifest with that one digest replaced:
all names, ordering and other lines are unchanged.

Every one of the initial audit's 115,334 input paths was checked twice.
Exactly two original path/hash pairs use historical aliases:

| Original paper path | Exact historical bytes |
|---|---|
| `PAPER_STATUS.md` | [lifecycle_before/PAPER_STATUS.md](lifecycle_before/PAPER_STATUS.md), SHA256 `1baa2adda556eba4acc1edeb9b9d4bf3974214b507333db93c33f9a18be58f05` |
| `SHA256SUMS` | [lifecycle_before/PAPER_SHA256SUMS](lifecycle_before/PAPER_SHA256SUMS), SHA256 `926afeafef8eb2e2d5d642fb1b5f9b48d81fa7d7f1dc9bdabd42e155031a93dc` |

No other original ledger change is permitted. The 108,534 original host
path resolutions were also checked twice. All accepted author/A/B,
frozen-round, strict replay and terminal-build manifests retain their exact
original hashes and full physical coverage. The original 973 local links
still resolve. Twelve links in the new lifecycle, final QA and root
acceptance documents were checked separately; all five new/current document
inputs have exact original/snapshot pins.

The complete known-resource sets remain unchanged: 925 runtime/tool files,
105,987 TeX files and 1,788 configuration records. Absent configuration
paths remain checked as absent, and resource additions/removals are checked
in addition to byte hashes. The follow-up's own early/late runtime samples
contain 57 module entries and 16 mapped files each, all covered by the
original dependency ledger plus the exact new helper source. In total,
115,403 actually read current paths were rechecked at the end.

## Preservation and execution provenance

Before the follow-up, all 54 initial artifact payloads were verified and
left unchanged. The initial outer seal and report were copied byte-for-byte
to [INITIAL_PACKAGE_SHA256SUMS](lifecycle_01/INITIAL_PACKAGE_SHA256SUMS) and
[INITIAL_REPORT.md](lifecycle_01/INITIAL_REPORT.md). The initial seal remains
`e3b64033ca95f890e87f1ca7fa669077212fd924277febfa9bc97d71cd74c1b1` at its
archived location. The old auditor source, initial successful output and
all four failed attempts are untouched.

The new [lifecycle helper](lifecycle_audit.py) is scoped artifact
infrastructure, SHA256
`c3dcb90a1f2c8dc5bafddca0118226bf2eb36d23cf7f1d6a8c6d04e31e0b0051`.
It neither imports nor executes `audit_p208.py`. Its original preparation
source and successful preparation receipt remain preserved. One
[pre-child-execution schema repair](lifecycle_01/SOURCE_REVISION.json)
recognizes that two historical B configuration formats record existence
and hash without a byte count. Their hashes/existence are still checked;
every recorded byte count is checked, and the full initial input ledger
independently requires every original size/hash before and after. No failed
child run of that prepared version occurred or is invented.

The successful attempt's five-payload nonself seal is
`4229ca27dfb84c956dadd35252b59726c35b55f4cc2e6b0853c48a057cfb948d`.
The final sealing operation separately rechecks the successful actual
streams, source and all 115,403 read inputs. Only this audit package's
evolving outer `SHA256SUMS` is replaced; its exact original bytes are already
preserved. No initial report, command, source or scientific artifact is
rewritten to describe the later lifecycle.

The project research workflow requires this change-sensitive reuse rather
than treating a lifecycle edit as new numerical or visual work. Runtime
samples and known-resource inventories remain non-hermetic; they do not
claim continuous child/transient access tracing. P208's internal completion
is compatible with the original accepted evidence. Five-paper batch
completion and private Git synchronization remain separate obligations.
**OWNER_AMBER / HOLD_EXTERNAL.**
