# P212 finite bootstrap routing — proposal only

2026-09-09 UTC. SOURCE_ONLY_ROUTING / HOLD_OPERATIONAL.
Owner: /root/round211_finite_matching_scout, author of the outer preparation
and a P212 proof contributor; this is not independent review.

## Decision at the first boundary

The current [five-source contract](../p212_dependency_query_outer_preparation01/SOURCE_CONTRACT.md)
requires independently established inherited startup effects before the
product-launched Bash and env have run. The currently exposed product
interface does not establish that fact. An ordinary trusted-tool assumption
does **not** satisfy this existing gate. With no independent launch evidence
or accepted contract delta, both author probes and contract01 remain HOLD.

Two finite routes exist; this document chooses, implements and accepts neither.

- Keep the strict claim: obtain independently supplied, applicable launcher
  evidence/control binding the effective launch policy, exact invocation
  prefix and inherited startup influences to the intended launch. Receive
  the finite executable/loader/configuration key outside the later process.
  The currently exposed interface supplies no such prelaunch attestation.
- Separately propose and independently review a provenance/source delta:
  explicitly trust the ordinary product launch of the observation machinery,
  including its Bash/env/bootstrap, and claim only the received finite
  downstream dependency key and actual ENV8/runtime observations. This is
  a narrower conditional claim, not proof of the old startup requirement.
  No product settings, source contracts or enabled arguments are changed here.

The trust assumption must terminate the observer regress openly. Do not
write another executor that calls itself or certify its initial imports from
its own later maps. Current source-document reads likewise rely on the normal
tool boundary; their hashes are not platform-launch certification.

## Facts the available interface does and does not provide

| Item | Available evidence and exact limit |
|---|---|
| Product request | exec_command accepts cmd, workdir, shell, login, tty and capture/wait controls. We can retain their literal supplied values. There is no exposed per-call env object or direct executable-plus-argv field. |
| Actual product returns | Actual output, session_id or exit_code, chunk_id and timing may be retained with actual empty-stdin poll originals. They are not a kernel exec record, effective-environment receipt or implementation audit. |
| Before Bash/env | No exposed return proves the effective inherited BASH_ENV/ENV, SHELLOPTS/BASHOPTS, exported functions, LD_* or other source-applicable startup influences; actual launcher options/mode/configuration and pre-command effects are also unestablished. The names are examples, not an exhaustive closure. |
| env -i | The source requests a cleared environment for env's child. Bash has already started; dynamically linked env itself also starts before clearing its child's environment. Later Python/Node ENV8 equality cannot retrospectively rule out earlier effects. |
| Parent /proc environ | No such read occurred. A future correctly identified parent snapshot would be that process's initial exec environment region, not proof of its later changes, effective child-filtering policy or the future product launch's environment. It cannot replace the missing gate. |
| Installed settings or public docs | Public configuration documentation describes shell_environment_policy inheritance/filtering/profile options. It does not prove this deployment's effective configuration or bind it to a particular tool call. No configuration inspection/change is authorized by this routing note. |

GNU documents the noninteractive BASH_ENV startup path; this is why
login=false is not a clean-environment proof.
[GNU Bash startup manual](https://www.gnu.org/s/bash/manual/html_node/Bash-Startup-Files.html).
The dynamic linker has pre-program environment/configuration inputs.
[Linux ld.so manual](https://man7.org/linux/man-pages/man8/ld.so.8.html).
The initial-region and later-change limits of /proc/PID/environ are documented
in the [Linux proc environment manual](https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html).
The product documentation is only a capability reference:
[OpenAI configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).
None of these sources is an observation of this host.

Do not dump ambient environment or move secrets into a repository. Any future
independent launch evidence requires an explicit relevant-field/confidentiality
scope; a redacted or selected record must not be described as complete unless
its completeness for the claimed effects has actually been established.

## Exact existing inputs; no automatic historical upgrade

[INPUT_PINS.tsv](INPUT_PINS.tsv) records whole bytes and SHA256 for 43 selected
workspace documents/sources and live manuscript files. These are ordinary
documentary pins, not current host-runtime or fourteen-field metadata keys.

| Reuse input | Precisely what may be reused, subject to current matching |
|---|---|
| [Amendment final reception](../p212_execution_scope_amendment_root01/RECEPTION.md), [source reception](../p212_execution_scope_amendment_root01/SOURCE_RECEPTION.md), [APPLICATION_RESULT.json](../p212_execution_scope_amendment_root01/APPLICATION_RESULT.json) | Actual accepted amendment/application, not the old prospective state. The first two are 3954/4355 bytes; the final application record is 310447 bytes. Its final_live_sources contains all eight rich descriptors. |
| [Old dependency reception](../p212_dependency_source_root01/RECEPTION.md) | Historical dependency_source role only. It cannot supply source_amendment, outer_source, runtime or product_startup. |
| [Python discovery reception](../p212_runtime_discovery_root_reception01/RECEPTION.md), [RUNTIME_LOCK.json](../p212_runtime_discovery01/RUNTIME_LOCK.json), [ELF_NATIVE.json](../p212_runtime_discovery_independent01/ELF_NATIVE.json) | Accepted, bounded historical file/configuration/ELF observations. Exact unchanged subsets can be proposed for reuse; the old role imports and ENV4 do not cover the new Python surface. |
| [Forward guard](../p212_canonical_adoption_root01/guard_runtime.js), [pair boundary source](../p212_author_pair_binding01/check_boundary.js), [old startup contract](../p212_author_pair_binding01/ROOT_STARTUP_CONTRACT.md) | Finite whole-byte/alias/configuration/membership and real before/after absence-check mechanisms. Hardcoded old counts and four-field keys are not this task's new descriptor schema. The old startup contract explicitly excludes continuous startup tracing. |
| [Node semantic reception](../p212_saved_output_root_reception01/RECEPTION.md), [NODE_RUNTIME_LOCK02.json](../p212_saved_output_root_reception01/NODE_RUNTIME_LOCK02.json), [NODE_PROBE04.json](../p212_saved_output_root_reception01/NODE_PROBE04.json) and its native original | Old complete native-file/typed-builtin fingerprints and bounded configuration evidence. Different preload, package ancestors, ENV4 and import surface mean no whole-key transplant. A fingerprint is not an actual new import observation. |
| [Immutable five-source packet](../p212_dependency_query_outer_preparation01/SHA256SUMS) | Exact author source input only, seal 2c886f9fb07053c5ca6dcf46b5eba397a9e92e2d4949a9ca0598bb05b9779138. Actual independent outer review and root reception are separate required inputs. |

The accepted current driver is 51325 bytes /
e2bc505d81a377386dd6d6286f601bdbae86ffbda9a751ac7f67ad493251007d;
its companions/QUERY_FRONTIER.json is 33833 bytes /
f71cb32c219061f03aa54cd611d515440ac6a7baab72137b4d2401a1b9be9b09.
Current live05 is 1237 bytes /
44ab0ee97ab09a7bd0d68ddaf116d74f43314f69ef00821a77b67282d851012d.
This task's current byte observations match all eight accepted live source
pins, totaling 20092 bytes. It did not repeat the root's raw comparisons or
rich-metadata application closure, or rerun science/semantics.

Historical bootstrap candidates in the old locks are /bin/bash resolving
to /usr/bin/bash (1396520 bytes, SHA 59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4),
/usr/bin/env (43976, 85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0),
/usr/bin/python3.10 (5937704, d6bca2b84e73c7775a0dd5e6a76899cfe4ee62863d7c8f88513811d1fda23f49),
and /usr/bin/node (124679552, 81925c0995b5c1427b5d538e6a90ca2fdc4daffb786b09af749beaf7369d4e90).
These are archived candidate keys, **not freshly observed host identities**.
Parent-component aliases such as /bin and all referents still need explicit
descriptors; the old leaf symlink field alone does not establish that chain.

## Finite ordering after the first boundary is resolved

The following are proposals for separate root authority, not commands executed
or enabled by this document. Root must receive source before using a new
observer delta. No whole-host walk or recursively copied observer suite is needed.

1. Fix the accepted claim and source set. Receive the amendment above and
   actual independent outer-source result. For a narrowed route, first receive
   the explicit delta described below. Independently bind the intended product
   prefix and the finite observation scope; retain the selected trust limitation.
2. Before either new probe, perform an independently received read-only key
   observation under that boundary. Use the prior finite read/config mechanism
   as lineage, with exact lexical/resolved whole-file keys and all fourteen
   integer fields required by the new contract. Read the old lock's relevant
   entries, alias chains and finite configurations, and compare current bytes
   to the actual accepted keys. Receive any changed branch before using it.
   A later observation by the target probe cannot supply its own bootstrap.
3. Close the new pre-probe surfaces statically. For Python, read the selected
   module resolution under the exact isolated path policy and the finite
   ctypes/_ctypes/libffi, struct, subprocess, signal and traceback import/native
   dependencies. For Node, receive the selected six-builtin import/native and
   configuration surface. An unchanged executable plus its applicable accepted
   ELF evidence can support subset reuse; every new ELF/config branch needs
   finite source-derived closure. No ldd/readelf run is silently included.
   If another diagnostic is indispensable, give its exact source/argv/targets
   and bootstrap gate to root first, then stop this route until received.
4. Only after those keys and distinct source/bootstrap receipts are accepted,
   bind two separate runtime-only probe requests. Both use physical ROOT cwd
   and exact ENV8. Python uses the selected /usr/bin/python3.10 spelling,
   -I -S -B -X and an actually absent dedicated cache prefix. Node uses no
   startup options and imports only the six received builtins. The Python
   literal metadata list must include its own source, /dev/null and /.
   No driver/preload import, child spawn, tool/help query or operational
   contract binding occurs in these probes.
5. Receive actual probe originals, stdout/stderr, any real sessions/polls/final
   returns and before/after source/cache/key observations. Root obtains an
   independent fourteen-field observation for the same unchanged statx targets,
   comparing all stable fields with only the stated atime exception. Receive
   the raw 256-byte statx records, valid-field masks, actual LP64/endianness,
   and actual subreaper setter/readback/ECHILD. This is not an orphan-adoption
   or complete lifecycle experiment. Unsupported fields mean HOLD.
6. Complete the operational key before contract01: whole Python modules/maps
   with explicit probe-main to outer-main substitution; Node native bytes,
   typed builtin registry and a justified finite lazy-binding policy; Bash/env
   and their applicable configuration under the selected claim; and kpsewhich
   help/version-only executable/ELF/loader/locale/configuration/search-state
   closure. Paths/maps alone are not whole keys. Label unobserved late Node
   bindings source-derived, never observed. Unknown dependencies remain HOLD.
   Preserve the exact ENV8 values in the received source; null directory
   members never means an empty/irrelevant search directory.
7. Form the prepared Node request first, then the enabled inner binding, then
   the enabled outer binding. Supply the outer's full descriptor externally
   as the final product argument; never make a binding pin itself. Root later
   attaches actual enclosing product/tool originals after they exist. Keep
   DQD-O1's selected-binding key and before/after raw-original observations.
   Only a separately received contract01 may run help then version. Option
   semantics acceptance, lookup01, bodies01, dependency lock and build remain
   distinct later gates.

This route neither reuses the old automatic-signal native core nor opens a
hidden process test. It does not repeat old mathematical/semantic producers.
Finite samples, current keys and explicit trusted-platform assumptions do not
prove continuous loading, all historical processes, escaped-writer exclusion,
hermeticity or absence of races.

## If root selects a narrower provenance delta

It is feasible to propose that limitation without changing the mathematical
claims, exact query algorithm or accepted manuscript. It is not permissible
to reinterpret the existing receipt role silently. The reviewable delta must:

- State the ordinary product/observer/Bash/env bootstrap trust assumption,
  the missing inherited-environment evidence and the exact narrower bounded
  downstream claim. Keep observational failures and unknowns as HOLD.
- Amend SOURCE_CONTRACT, RUNTIME_PREPARATION and source-origin/interface
  descriptions consistently. Update outer receipt semantics and, preferably,
  use a distinct schema/role for a trusted-product-boundary receipt instead
  of a product_startup label that appears to certify the old strong claim.
  Audit any affected outer source, collector comments and both probe receipt
  descriptions. A boolean enabled flag is not semantic approval.
- Keep the independently received pre-Node/tool key, full descriptors,
  prepared-request/nonself ordering, selected-binding DQD-O1 gate, actual
  ENV8/flags/cache observations, actual product/session originals, no signals,
  phase separation and all scientific/build/manuscript gates unchanged.
- Preserve this packet and all earlier sealed sources; prepare new-only
  candidate files, actual complete source diff and typed invalidation map.
  Obtain an actual process-separated review and root acceptance before any
  later runtime-only authority. Reject a delta that merely renames an unmet
  strong assertion or hides a changed dependency.

No such delta, permission, current bootstrap receipt or actual runtime result
is supplied here. HOLD_OPERATIONAL / HOLD_EXTERNAL.

## Late source-reception note, before this routing packet froze

Root has now issued and this author has read the entire 7044-byte
[outer composite source reception](../p212_dependency_query_outer_source_root01/RECEPTION.md),
SHA256 b3ad160aa1ea7595fb1dc18bb90d03f9eebf9d4a259a206d658f71d57e815035.
Its 584-byte SHA256SUMS has SHA256
2470420d72e98a0d55f7d2c4809eeeaa82000f2ba3578caa04210a4bd3438fe2.
Both exact files are added to INPUT_PINS.tsv. This is acceptance of the five
sources plus the exact read-entry coverage delta and same-reviewer acceptance,
not just the old coverage document in the author packet. The receipt explicitly
retains the inherited-shell gate and grants no probe, runtime key or query.
Thus the source-reception item above now has an actual root input; the two
routing alternatives and all unresolved startup/runtime gates are unchanged.
This note neither selects a route nor implements the prospective source delta.

