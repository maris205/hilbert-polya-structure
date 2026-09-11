# Independent regular os-release DATA reception

2026-09-11 UTC. **ACCEPT_ONE_OS_RELEASE_REGULAR_BODY_AND_LITERAL_FIELDS_DATA_ONLY**.
Current Critical/Major/Minor/open findings: **0/0/0/0**.

Actual capture `e2bc8e` exited 0, empty native output, zero tokens and no
session. Complete captured stdout: 5,860 bytes, SHA256
`c755f4dcc29702b7185070e53722e16f37a67b0534803298a87a93fdba6e5c8c`;
stderr: zero bytes. Independent [CHECK.cjs](CHECK.cjs) ran as actual
`10d45a`, exit 0; [NATIVE.json](NATIVE.json) preserves the exact request and
entire 33,917-byte result, not a reconstructed or truncated native output.

## Accepted body and literal identity text

Exactly one mandatory `OS_RELEASE` row, candidate `/usr/lib/os-release`,
role `distributor_identity_regular_candidate`, actual kind regular.
Its complete body is **386 bytes**, SHA256
`594d5ddd35aedb47f00d9c34d140017907a5b9f93c975aba125fc924daac5c07`.
All four ten-field lstat/fstat views are equal; recorded fd 20, reads
`65536 -> 386` then `65151 -> 0`, genuine EOF, successful close and null
close error. Body length matches stat size and the recomputed hex/hash.
Accepted totals: **386 regular bytes, zero link bytes**.

The complete actual body, including a final LF, is:

```text
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

The body is exact UTF-8/ASCII with 12 distinct assignments: eight simple
double-quoted and four unquoted literal values. The checker rejects duplicate
keys, unsupported syntax, escapes, substitutions, CR/NUL and extra lines;
it records every line's byte span and full raw value. It strips only literal
paired quotes, never applying shell semantics. This is the captured text's
self-description, not an installed-distribution/package provenance guarantee.
None of its paths or URLs was opened. A separate bounded read-only literal
cross-check agreed; this packet's own executed checker reproduces all fields.

## Context, adapters and bounded reuse

All nine outside source/copy/request/grant/control inputs match complete
four-view keys, byte counts, hashes, EOF and close across preflight `97e340`,
closed-raw `317e0d` and this current reception. All 25 fixed workspace
documents are read through no-follow regular-file checks with their complete
current keys/reads retained. The three exact private directory inventories
and their allowed empty-to-bound/raw transitions also match.

The full ordinary JSON UTF-8-plus-one-LF envelope is raw-equal after
serialization; every envelope, reader, request and regular-row field is
checked. Its 745-byte captured request equals the outside bound bytes and
four complete keys, with reads 745 then genuine zero EOF and close. The
entire disabled-to-bound JSON delta and 1,373-byte grant reference match;
actual native arguments equal the accepted operation and 563-byte capture.
Entry/reader/row failures are null. Follow, ancestor-scan, source-acceptance,
permission and installed-closure flags remain exactly false/null.

The accepted root source review `f64d8c` is pinned and reused, not re-executed:
its five relevant current input keys/pins and enabled-reader pin match.
Reader activation is the sole false-to-true byte replacement; entry copy is
whole-raw equal. Source/capture/regular-body history is not re-audited.
The [single-leaf DATA checker](../p212_os_release_data_audit01/CHECK.cjs) and
[regular-body DATA checker](../p212_three_terminal_data_audit01/CHECK.cjs)
are explicitly pinned, read as text and reused only for unchanged mechanics.

All five root native records use exact `{arguments,result}` wrappers.
Materializer `NATIVE.json` has a separate explicit adapter for the sole
`records[name=otmPost01]` read-only record (`request/result`, actual `520ce9`).
Its whole request and all 87,142 stdout bytes equal root POST replay `cc57fe`.
All eight original input and two copy raw bytes/four keys match current
documents. Its directory evidence is two equal pathname-based endpoint keys,
not same-fd membership; that limitation is retained. No materializer mutation
or POST command is run by this checker, and earlier archive stages are not
re-audited. The consumed grant is documentary context, never reusable.

The project workflow limits this reception to the changed DATA dependency.
No host candidate is reopened, no collector/source is imported or executed,
and no shell sourcing, package/ELF/tool/build/science or external operation
occurs. Ordinary Node/filesystem/product/trusted-ancestor assumptions remain;
equal historical points do not establish continuous race freedom or automatic
resolution of the earlier link. B/S, installed closure and `HOLD_EXTERNAL`
are unchanged. No old or central file is edited. Nonself SHA256SUMS covers
exactly CHECK.cjs, NATIVE.json and this receipt. Root's read/replay/acceptance
is a separate remaining step.
