# Checkpoint03 SSH delta04 — source contract

2026-09-09 UTC. SOURCE_PREPARED_NOT_INDEPENDENTLY_ACCEPTED.
HOLD_OPERATIONAL / OWNER_AMBER / HOLD_EXTERNAL.

## New source and exact scope

The new full checkpoint.py is 47,072 bytes / 804 lines, SHA256
32900d88796c8dcc0dceda62f7d650be184d104202b2dea0ca257d356d65db48.
The accepted checkpoint03 source remains 45,584 bytes / 774 lines, SHA256
4851f2c1c39335c1d0f0de270c2d3ae9637a96991425a7cd1891e32da6f9b0d5.
The ordinary complete EXACT_DELTA.patch has exactly two hunks: relocate PREP
to this new packet, and replace the literal GIT_SSH_COMMAND value. No other
source text changes. No old source, review, scope, role or private file changes.

The chosen 8,207-file / 386,716,363-byte, 43-closed selection is unchanged:
8,204 additions, two modifications, one unchanged, no deletions; 178 core
plus four bridge groups. Its source pin remains
76e633c45920f46fc6c1d3e840d9d82fd7025946b31a397356c1d771b1ba5c92.
The exact endpoint, BASE/tree, original-mirror and bare paths, existing
command-local identity, Git settings and all data checks remain byte-identical.
This packet, ongoing P212 and current controls are not added to that selection.

The earlier SOURCE_CONTRACT.md remains the unchanged phase/protocol baseline
listed in INPUT_PINS.sha256; its old SSH sentence is superseded only for this
new source by OPTION_POLICY.json and the boundaries below. The existing
checkpoint03 protocol names, run-prefix and four binding path constants stay
unchanged deliberately. They identify the same finite protocol, not source
identity. Every new operative binding must instead pin this exact new source
and genuine new independent source/runtime receipts. The old disabled examples
are not copied, edited, enabled or treated as authority for delta04.

## Command-local policy, not host settings

OPTION_POLICY.json records the exact shell command string and literal token
sequence. It retains all four original explicit options and adds no-config,
no-agent-forward, no-X11, no-PTY and 27 explicit -o guard fields. All option
values are fixed source text; no new interpolation, wrapper, config file,
key path, provider path, agent socket, host alias or endpoint is introduced.
The environment constructor still overwrites a would-be inherited SSH-command
override. All five genuine inherited role names and their checking logic are
unchanged; none is assigned an author-created value.

PRIMARY_PROOF.md gives a bounded published-semantics argument, particularly
the released-source treatment of SecurityKeyProvider=none. It is explicitly
conditional, not an installed OpenSSH version/default observation or a
cryptographic build correspondence. This author has not invoked ssh -V/-G,
the submitted source, observer, parser, helper or test.

This is a narrow source delta, not a mathematically smallest flag set.
Several explicit guards overlap: removing configuration eliminates callbacks,
and publickey-only preference overlaps negative alternative-authentication
flags. The overlap makes each required policy family an explicit field to be
checked in a later installed-semantics reception. It is not a fallback that
silently ignores an unknown or unsupported option; IgnoreUnknown is not set.
An unsupported/ignored field remains HOLD, even if a version merely warns.

No UserKnownHostsFile/GlobalKnownHostsFile replacement, acceptance-new mode,
key deletion, keyscan, hash rewrite or credential generation is proposed.
StrictHostKeyChecking=yes remains literal. Suppressing UpdateHostKeys,
CheckHostIP and DNS-based alternative trust is not proof that the actual
known-host files contain the correct remote host key. Their actual input-role
selection and successful strict verification are still unobserved.

## Authentication compatibility and the agent boundary

Ordinary existing software public-key and existing-agent authentication remain
available. This source does not set IdentityFile, CertificateFile,
IdentityAgent or IdentitiesOnly, remove a genuine inherited role, introduce
credentials or relax cryptographic algorithm policy. It does not certify that
this preserves a successful authentication: none was observed for checkpoint03.

Configuration-dependent authentication, GSSAPI/hostbased/password/keyboard
paths, local PKCS#11 and local security-key providers are intentionally not
a permitted fallback. If an existing requirement depends on one of those
paths, stop at that incompatibility. Do not weaken the policy or create
authentication setup. The prior empty user config and empty selected Include
frontier are historical observations only, not authority to assume all future
configuration, compiled defaults or authentication dependencies match.

Keeping the genuine SSH_AUTH_SOCK selection cannot establish that an already
running agent never asks for confirmation, accesses hardware, updates its own
internal state, or delegates internally. AddKeysToAgent=no and -a do not mean
no agent use. Local-client provider suppression is distinct from the agent's
implementation. No credential or agent inspection was made here, and no such
inspection is granted. This unresolved external-agent/actual-authentication
condition must be received explicitly under the finite ordinary-platform
boundary or remain HOLD; no global no-side-effect/hermeticity claim.

Removing SSH configuration also removes configured environment forwarding.
Git's actual appended transport arguments and requested repository operation
must still be received in the appropriate future command context. No claim
that a fixed GIT_SSH_COMMAND is the complete future ssh argv is made.

## Unchanged four-phase and product gates

Capture, stage, commit and push remain separate, exactly one per externally
hash-bound root binding. There is no prepare mode or automatic successor.
The old selected plan, physically chosen historical controls, complete selected
membership/bytes/mode/OIDs, isolated index, full unfiltered diff, single-parent
commit and ordinary non-force push/CAS rules remain unchanged. All command
construction, timeout/signal handling and native/product evidence logic are
identical outside the SSH command value. Existing bindings/receipts/runs are
not probed, reused, migrated or reauthorized by this packet.

All five earlier root source-reception limits still apply:

1. Real startup, actual protected roles and effective SSH runtime policy are
   external reception gates, now for this new source and policy.
2. The 50-second guard bounds each native communicate, not startup, Python
   file reads, allocation, fsync, total phase time or memory/capacity reservation.
3. Early failure can precede a run or FAILURE.json; retain actual enclosing
   requests/returns/errors. Missing evidence is not success or a retry grant.
4. Regular-file seals and alias checks assume root's finite exclusive
   attachment; they do not prove hostile all-node or concurrent isolation.
5. Native exit, remote update, local CAS and root product acceptance are
   separate. A partial remote update must survive as evidence, with no
   invented rollback, retry, successor or process-tree closure.

Every phase remains HOLD. DIAGNOSTIC_PROPOSALS.disabled.json is a separate
unexecuted proposal, not a phase binding, shell script or operational grant.
Root must independently inspect this source, obtain a nonauthor review,
resolve installed semantics/runtime/role/authentication limits and then
separately decide whether any exact future diagnostic or phase is authorized.
