# Independent bounded primary argument

Public retrieval date 2026-09-09 UTC. This concerns referenced published
semantics, not installed provenance. Only relevant returned branches were
reviewed, not every line of every upstream file. PRIMARY_REQUESTS.json
indexes actual public requests and returned line spans.

## Configuration and D02 control flow

In V_8_9_P1 ssh.c, process_config_files (512–540) skips user/system
configuration when config is none; with this fixed argv there is no
configuration Match/Include source. Startup still reaches randomness and
account lookup (599–628); -V exits later (834–839). D02's numeric target uses
numeric address processing (272–353, 396–428), while its explicit
CanonicalizeHostname=no and CanonicalizePermittedCNAMEs=none block the named
rewriting/CNAME route (1114–1169). The config-test exit (1427–1429) precedes
provider expansion, mux connection, ordinary resolver/SSH connection,
identity loading and login (1431–1577). Thus, conditional on these semantics
and exact arguments, D02 avoids SSH transport and SSH authentication helpers;
it does not prove that platform/NSS startup is network-free or side-effect-free.
User known-host path expansion already occurs before the dump (1375–1386).
[Released ssh.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/ssh.c).

## Literal clearing

readconf.c clears the named command/control/provider fields on literal none
after filling defaults (2547–2577); security-key none is not a library name.
ClearAllForwardings triggers cleanup (2368–2372). IdentityAgent retains
distinct null/none handling. [Released readconf.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/readconf.c).

## Initial and later host-file changes

Strict yes rejects the new-key branch (1055–1067), but the successful-host
branch can add an unknown IP when CheckHostIP is enabled (1014–1028).
The separate CheckHostIP=no guard matters; it does not attest any actual
key exchange. [Released sshconnect.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect.c).

UpdateHostKeys=no makes update_known_hosts return before the file
replacement loop (1948–1977), independently of strict initial verification.
[Released clientloop.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/clientloop.c).

## Authentication and retained agent

sshconnect2.c chooses enabled methods from the preference/server intersection
(2149–2218). Batch mode rejects unavailable software-key passphrases
(1481–1484). Missing local SK provider skips those local keys/certificates
(1501–1507, 1607–1612, 1630–1635). Agent identities are independently obtained
and appended (1548–1574, 1644–1675), and agent-backed signing uses a separate
return path (1159–1163). Therefore the candidate's local-provider and
alternative-method suppression is not a proof about arbitrary retained-agent
internals or successful authentication. [Released sshconnect2.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect2.c).

## Interface cross-check

The current manual documents no agent addition, forwarding cleanup,
no control path/persistence, no proxy routes, no permitted local command,
no escapes and distinct host-key controls. ControlMaster=no alone would
still allow a configured shared connection, so explicit ControlPath=none
is material. IdentityAgent and SSH_AUTH_SOCK relate to authentication,
not merely agent forwarding. Password, keyboard-interactive, hostbased and
GSSAPI controls are distinct. These support the listed option-family
intent, not installed defaults. [Configuration manual](https://man.openbsd.org/ssh_config).

The released manual separately describes GSSAPI delegation, hostbased
authentication, agent forwarding and the argument-value interface.
[Released ssh_config.5](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/ssh_config.5).
The client manual defines -T/-x and version display; documentation does
not establish this binary's implementation. [Client manual](https://man.openbsd.org/ssh).

## Dump reception observation OBS01

readconf.c dump_cfg_string returns without output for NULL (3048–3052).
Thus cleared ControlPath, LocalCommand, RemoteCommand, PKCS11Provider,
SecurityKeyProvider and KnownHostsCommand lack literal echo rows; cleared
ProxyCommand/ProxyJump similarly disappear (3293–3317). GSSAPI output depends
on compilation (3147–3150). Identity-agent absence does not itself certify
no agent, and identity path strings can remain symbolic defaults
(3186, 3209–3213). Therefore a future receiver needs a field-specific,
installed-source-supported interpretation of emitted, omitted and unsupported
values; arbitrary omission or warning cannot count as PASS.
[Released dump implementation](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/readconf.c).

The candidate already requires independent installed-source analysis and no
silently ignored diagnostic fields. OBS01 clarifies that obligation; it does
not relax the no-G gate, authorize an output parser or require a diagnostic
before this source-only review can conclude.
