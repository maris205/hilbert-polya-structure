# Bounded primary SSH-policy argument

SOURCE-LEVEL CONDITIONAL ARGUMENT; not an installed-version observation.
Public retrieval date: 2026-09-09 UTC. Only the named public OpenSSH resources
were queried. The release tag V_8_9_P1 is a bounded semantic example, not a
claim that the installed binary is that release or unpatched. No entire
upstream file is claimed manually reviewed. Locators below identify the
relevant returned lines; PRIMARY_REQUESTS.json records the actual queries,
including unsuccessful narrow find/open returns. No fetched source is
represented as an independently immutable installed-binary provenance chain.

## Client entry and configuration

In released ssh.c, process_config_files (lines 512–540) bypasses both ordinary
configuration branches for the explicit none config argument. Thus the
candidate's -F none supplies no Include/Match source from those files.
Command switches assign no agent forwarding, no X11 and no PTY (774–776,
680–682, 972–974). PKCS#11 loading requires a nonnull provider (2119–2124).
The config-test branch exits at 1427–1429 before provider-environment
expansion, multiplex connection, ordinary resolver and connect (1431–1475);
startup and earlier numeric/canonical processing still precede it. The
version branch exits at 834–839 but follows startup/getpwuid (599–628).
These are bounded code-path facts, not permission to run either branch.
[OpenSSH 8.9p1 ssh.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/ssh.c).

## Literal none and forwarding cleanup

Released readconf.c applies CLEAR_ON_NONE to local/remote/proxy commands,
control path, both PKCS#11 and security-key provider fields, and the known-host
command (2547–2561); none jump-host cleanup follows (2562–2566).
This is essential for SecurityKeyProvider=none: the provider string is cleared,
rather than interpreted as a library filename. Explicit clearing follows
default filling. ClearAllForwardings selects forwarding cleanup (2368–2372).
IdentityAgent deliberately has different null/none treatment (2577), so the
candidate leaves its genuine existing selection available.
[OpenSSH 8.9p1 readconf.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/readconf.c).

## Strict known-host acceptance and address insertion

The released known-host branch fails for a new host under strict yes
(1055–1067), and for changed/revoked keys under non-off strictness
(1143–1158, 1195–1210). A different successful-host branch can insert a
previously unknown address when CheckHostIP is true (1014–1028).
Consequently strict yes alone is insufficient for this no-write requirement.
The candidate additionally sets CheckHostIP=no; it does not replace any
host-key database or assert a verified remote exchange.
[OpenSSH 8.9p1 sshconnect.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect.c).

## Post-authentication host-key replacement

In update_known_hosts, a zero update_hostkeys value returns before file
metadata/replacement work (1948–1977). UpdateHostKeys=no supplies the explicit
policy guard, independent of unknown installed defaults and independent of
strict initial host checking.
[OpenSSH 8.9p1 clientloop.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/clientloop.c).

## Authentication and its retained dependency

Released sshconnect2.c uses the preferred/supported method intersection
(2183–2218), with explicit method-enable fields (376–405). The candidate
selects publickey and disables other listed methods. Local authenticator
keys are skipped when the provider field is null (1501–1507, 1607–1612,
1630–1635). Batch handling rejects an unavailable key passphrase
(1481–1484). Agent identities remain separately obtained (1548–1574,
1644–1675), and agent signing returns through a distinct path (1159–1163).
Therefore disabling the client's local providers does not establish the
internal behavior of an existing external agent. In particular, provider
suppression is necessary beyond relying on BatchMode for security-key paths.
[OpenSSH 8.9p1 sshconnect2.c](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/sshconnect2.c).

## Option-family interface coverage

The release manual defines AddKeysToAgent=no as no key addition; BatchMode
as suppressing user prompts; CanonicalizeHostname=no as no explicit rewriting;
EscapeChar=none as disabling escapes; ForkAfterAuthentication=no as no
requested backgrounding. GSSAPI authentication/delegation are distinct.
It identifies the existing IdentityAgent/SSH_AUTH_SOCK relation and the
effect of IdentitiesOnly, which the candidate does not change. It documents
negative PasswordAuthentication, KbdInteractiveAuthentication and
HostbasedAuthentication controls and the public-key method selection.
[OpenSSH 8.9p1 ssh_config.5](https://github.com/openssh/openssh-portable/blob/V_8_9_P1/ssh_config.5).

The current configuration manual is a cross-check only: ControlPath=none
disables sharing; ControlMaster=no alone would still permit using a configured
master, hence the explicit path/persistence guards. ClearAllForwardings
covers local, remote and dynamic forwards; Tunnel=no excludes tunnel-device
requests. ProxyCommand/ProxyJump none remove those routes; PermitLocalCommand
no excludes local commands. RemoteCommand is a separate configured command,
cleared here under the released source. KnownHostsCommand supplies host-key
callbacks, which are cleared. VerifyHostKeyDNS=no prevents alternative DNS
trust. PKCS11Provider none disables that provider. The documented update and
address-addition behavior supports the separate known-host guards. No
current-manual default is used as installed evidence.
[OpenSSH configuration manual](https://man.openbsd.org/ssh_config).

The client manual independently describes -F none, -a, -x, -T and the
version/config-dump interfaces. It is not evidence that a particular vendor
binary accepts these exact fields, has the same startup dependencies, or
implements the selected released branches.
[OpenSSH client manual](https://man.openbsd.org/ssh).

## Logical conclusion and limits

Under the specifically referenced semantics, fixed-argument integrity and
ordinary trusted runtime assumptions, the candidate suppresses the listed
SSH-client option families without writing a settings file. It does not
establish future installed option support, default known-host/identity role
paths, dynamic-loader/NSS behavior, arbitrary agent internals, remote host
trust, authentication success, transport-argument integrity or phase closure.
These are typed dependencies in DEPENDENCY_INVALIDATION.md, not gaps filled
by an absent grep match or a historic executable digest. Source preparation
alone authorizes no diagnostic or network action.
