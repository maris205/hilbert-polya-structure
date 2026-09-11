# Prospective effective SSH side-effect gate

SOURCE_ONLY; no current effective configuration is known or accepted.
This is a required-policy checklist, not output from ssh -G.
Configuration and credential files have not been read in this task.

The derivation must cover every command context used by both read and push
phases. Policy established for one connection context is not automatically
valid for another conditional branch or later phase.

The official manual says config values normally use first-match precedence;
Include and Match can alter the active input path, and Match exec executes a
shell command. UpdateHostKeys can add post-authentication keys; CheckHostIP
can add address entries despite strict checking.
[OpenSSH configuration](https://man.openbsd.org/ssh_config).

The diagnostic -G evaluates Host/Match before printing.
It is therefore excluded, not treated as an inert file reader.
[OpenSSH client options](https://man.openbsd.org/ssh#G).

## Required root decision table

For the unchanged accepted command, derive a finite effective-value record
from complete privately received base/approved-leaf bytes and the actual
command context. The following are conservative acceptance requirements
for this checkpoint, not changes to existing settings.

| Policy field or mechanism | Required accepted condition |
|---|---|
| Destination | Original host github.com, remote user git, exact repository command; any Hostname/Port/HostKeyAlias change must have an explicit received origin |
| Parsing/context | Case-insensitive directive handling, quote/comment syntax, first-value rules and additive exceptions are accounted for; no omitted active file or guessed default |
| Include | Every selected input path, lexical expansion order and matching block is explicit and within the single bounded frontier; otherwise HOLD |
| Match | No Match exec is evaluated, even to discover its truth; unresolved final/canonical/localnetwork/command/user branches remain HOLD |
| UpdateHostKeys | Effective no; yes, ask or unresolved is not accepted as no-write |
| CheckHostIP | Effective no; strict host checking alone does not discharge this field |
| Host verification | Preserve StrictHostKeyChecking=yes and actual host-key input roles; no acceptance-new, keyscan-to-file, host-key deletion or replacement |
| KnownHostsCommand | None/absent with supported semantics; no unreceived helper |
| ProxyCommand / ProxyJump | None/absent; an existing required proxy is a new finite execution dependency, not automatically authorized |
| LocalCommand | No active local command, and PermitLocalCommand=no; no shell callback |
| Agent | AddKeysToAgent=no; ForwardAgent=no; exact existing IdentityAgent/SSH_AUTH_SOCK selection, with no add/remove/replace/forward or agent setup |
| Multiplexing | ControlPath=none with no effective master/persistence/background path; no borrowing an unreceived control master |
| Other channels | No local/remote/dynamic stream forwarding, X11, tunnel or background-after-authentication; no extra socket/listener/child work |
| Authentication/providers | No unreceived PKCS11/SecurityKey/custom helper or askpass path; no credential generation/content export or new authentication setup |
| Remote command | No configured substitution for Git's actual requested remote operation |
| Output/privacy | No key/config/environment contents in Git; no debug transcript that is silently assumed safe to publish |

Current-reference details for callback, proxy, agent and multiplexing fields
are in the same primary [configuration manual](https://man.openbsd.org/ssh_config).
It is not an installed-version observation. A valid root receipt must identify
the actual semantics supporting defaults and unsupported options; an empty
grep match or absent directive by itself is not a universal no-side-effect
proof.

## Outcome branches

1. If the freshly received finite configuration satisfies every applicable
   row for the EXACT accepted command, root can receive that scoped runtime
   evidence under ordinary tool/platform trust. No operation grant is implied.
2. If the effective value is unsafe or unknown, keep the unchanged executor
   held. Do not mutate ~/.ssh/config, known_hosts, agents or Git settings.
   A new command-local source delta may be proposed and independently received
   if root authorizes it. The accepted command cannot be strengthened by a
   phase-binding override because its environment function overwrites it.
3. If authentication needs a proxy, provider, extra key, changed user/home,
   unfamiliar Include tree or changed endpoint, stop at that finite dependency.
   It is not authorization for external coordination or broader host inspection.

## What this packet intentionally cannot establish

No connection was made, so no authentication, remote ref, host-key exchange
or server behavior was observed. Existing agent use is not cryptographically
attested agent immutability. Before/after file keys do not show continuous
immutability or exclude arbitrary actions by trusted platform components.
The policies concern prohibited data/config/credential/agent changes, not
filesystem access-time bookkeeping caused by reads. All four Git phases HOLD.
