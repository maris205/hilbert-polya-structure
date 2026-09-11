# Independent one-leaf os-release DATA reception

2026-09-11 UTC. **ACCEPT_ONE_OS_RELEASE_LITERAL_LINK_DATA_ONLY**.
Current Critical/Major/Minor/open findings: **0/0/0/0**.

The actual observation is root chunk `f7f84e`, exit 0, empty native output,
zero native tokens and no session. Its complete captured stdout is 4,667
bytes, SHA256 `b625162f978b20129579004c8185d659a61d41d254431fdaedaf75ececa0a009`;
stderr is empty. Independent [CHECK.cjs](CHECK.cjs) ran as actual `d8223c`,
exit 0, and returned the complete 28,017-byte DATA result preserved in
[NATIVE.json](NATIVE.json). That wrapper records the exact command and
actual native result; it is not a new observer or a replay of the capture.

## Accepted DATA and limits

Exactly one row: `OS_RELEASE`, original lexical candidate `/etc/os-release`,
role `distributor_identity_alias_or_body`, actual kind **symlink**.
The entire returned target is the literal UTF-8 text `../usr/lib/os-release`,
raw hex `2e2e2f7573722f6c69622f6f732d72656c65617365`, 21 bytes, SHA256
`d9a42455139e2bd87a1946abb3b066fb51863cfb3ddff03244e203a5a22020a8`.
Both complete ten-field lstat views are equal, with symlink mode and size 21;
readlink returned, byte count/hash/UTF-8/non-NUL checks pass, and the recorded
point-complete flag is true. The same-fd-attested flag is explicitly false.
Accepted totals are **0 regular-body bytes and 21 link bytes**.

This is two equal point-stat views around a literal readlink, not historical
race freedom, simultaneous link identity, a same-fd link attestation, or
distributor identity. The target is handed off as DATA only: it was not
normalized, reopened, followed, sourced, executed or queried. No os-release
fields or package/member/source correspondence are accepted.

## Changed-dependency checks and explicit reuse

The checker pins and reuses the accepted three-leaf and three-terminal DATA
mechanics at [three-leaf CHECK](../p212_three_leaf_data_audit01/CHECK.cjs) and
[three-terminal CHECK](../p212_three_terminal_data_audit01/CHECK.cjs); neither
old checker is executed and no old observation or history audit is repeated.
The new scope is a single exact entry, 65,536-byte regular/4,096-byte link
limits, the os-release namespace and this actual symlink packet. Legacy
three-leaf schema labels do not grant three entries. No unused regular-body
decoder is treated as evidence of a body that was never returned.

The new native wrappers are explicitly `{arguments,result}` for actual,
materialization, preflight and closed-raw records; the source replay remains
a direct result. The adapter does not permissively accept either shape.
Whole source-replay stdout is raw-equal to the independently accepted
56,987-byte source RESULT. The five changed source/control files match both
recorded complete source keys, exact source pins and current bytes. Reader
activation is the sole false-to-true replacement; entry is whole-raw equal.
The whole operation arguments match the actual request and complete capture
command. The full bound request differs from the disabled template only by
the accepted binding fields and pins the 1,301-byte root grant.

All nine outside source/copy/request/grant/control files have complete
ten-field four-view keys, hashes, byte counts, EOF and close evidence equal
across root preflight `45b3da`, closed-raw reception `66c18e` and this current
read. Root materialization `6c8bf2` retains seven whole-raw/key records,
three private-directory views and three historical actual absences; its
recorded bytes and allowed directory transitions are checked, not rerun.
Both captured streams and all 23 fixed workspace documents are read with
no-follow regular-file checks; full keys and actual reads are in the result.

The complete envelope is ordinary JSON UTF-8 plus exactly one LF, raw-equal
after serialization. Its full embedded 734-byte bound request equals the
outside request: four complete keys, bytes/hash, reads 734 then actual EOF,
successful close and no error. Every envelope/reader/row/link field is
checked; called/returned are true, entry/reader/row failures null, and all
permission, follow, ancestor-scan, source-acceptance and closure flags retain
their exact false/null values. Root's consumed-one-use record is received as
documentary context, not a reusable grant or a new timing-attestation system.

Ordinary Node/filesystem/product and trusted-ancestor bootstrap remains.
No host candidate is reopened; no collector/entry/source is imported or
executed; no new observer, nested supervisor, package/ELF interpretation,
tool/build/science operation or external action occurs. B/S and
`HOLD_EXTERNAL` remain unchanged. Existing evidence and failures are not
rewritten. The nonself SHA256SUMS covers exactly CHECK.cjs, NATIVE.json and
this receipt; root's independent replay/acceptance remains its own step.
