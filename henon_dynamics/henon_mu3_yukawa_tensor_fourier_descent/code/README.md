# HCS-C61 exact replay implementation

Status: `TARGET_LOCKED / PREFREEZE_CODE_RESULTS_PASS / NO_REFRESH /
PAPER_PENDING / NOT_RELEASED`.

This directory is the hardened C61 implementation for the fixed
exact13-code/exact8-result topology.  The six theorem sources are installed
beside seven strict-I/O, backend-preflight, scoped-manifest,
persistent-directory-fd, rollback-atomic-promotion, runner, and hostile-test
support files.  The code/results layer passed the independent prefreeze
producer/checker lifecycle; this is not a paper, promotion-authority, or
repository-release claim.

The six owner-frozen theorem sources are:

```text
c61_group.py
c61_checker_group.g
c61_resolvent.py
c61_checker_resolvent.py
c61_producer.py
c61_checker.py
```

Together with the seven support files they form the exact13 inventory.  The
component source/evidence tuples, independently owned producer/checker hashes,
exact15 payload keys, schema descriptor, G7 counters, named hostile families,
and runtime-report adapter are frozen explicitly.  The runtime adapter
recomputes the certificate, schema, evidence, exact13 source, and gate seals;
it does not consume chronology-only `/tmp` reports.  The C61 counts were
measured directly and are not inherited from C60.

## Frozen target and predecessor boundary

The accepted target-lock inputs are bound to:

- formal-root13 aggregate
  `c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28`;
- Route
  `c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b`;
- Batch
  `13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814`;
- exact15 ledger
  `61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5`;
- target report
  `eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026`;
- novelty/source audit
  `d8fb7baa602cf32c89e2b457f9f0abf5f52c70ff377c8b23aae0e48ab921be25`;
  and
- formal hostile-pass report
  `78899bcda2ac3c5763b7622eed6340a57e23c248506d58d406f93f4debec01f7`.

G0 independently rebinds released P60 commit
`fe1217810b72840619efdf40a2af31b8b80d96f6`, parent
`f3b3726c40519cdd8ac7832f9f22df16d451b890`, tree
`22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a`, and its immutable committed
Batch blob
`d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5`.
That released blob is a different authority layer from the installed C61
target-lock Batch
`13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814`
above.  The one-time pre-I61 hostile audit
also accepts exactly 16 porcelain entries: that modified Batch, the protected
guard, and the 13 C61 root Markdown files plus Route as untracked leaves.  It
does not create a generic dirty-worktree allowance for later implementation.
The four component sources and producer/checker are source-tested to
reject every `/tmp` literal and the path or digest of the target-report,
source-audit, arithmetic-design, and formal-hostile chronology files.  Only
installed formal/Route/Batch bytes and immutable P60 objects may enter the
production authority rebind.

G0 also rebinds the complete released C60 project.  In particular,
the C60 full manifest is
`37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4`,
its certificate/payload are
`d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518` /
`dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`,
and its scoped manifest is
`f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7`.
These are predecessor inputs, never C61-produced artifacts.

## Fixed runner boundary

The intended backends remain miniconda Python 3.12.3 with python-flint 0.9.0,
SymPy 1.14.0, NetworkX 3.5, and jsonschema 4.25.0, plus GAP 4.11.1 with
TomLib 1.2.9, SmallGrp 1.4.1, and CTblLib 1.3.1.  No PARI or Singular
dependency is inherited.

With all independent source and semantic contracts frozen, a default
`./run_all.sh` is a nonmutating live replay.  A deliberate prefreeze shadow
refresh requires `./run_all.sh --refresh-prefreeze --evidence-dir DIR`,
where `DIR` contains exactly `c61_group_evidence.json` and
`c61_resolvent_evidence.json`.  The runner alone may set the reserved
`C61_TEST_EVIDENCE_DIR`, and only for its unittest child.

The shadow refresh promotes exactly six files as one rollback-safe transaction: the
two evidence carriers, schema, certificate, independent check report, and the
self-excluding scoped manifest.  The manifest scope is exactly 20 entries;
the live code/results inventory is exactly 21.  A successful refresh must
launch and pass a clean mandatory default replay.  `NO_REFRESH` here forbids
refreshing the authoritative repository; disposable-shadow lifecycle testing
does not grant that authority.

The active-stage basename is exactly `.c61-stage-[A-Za-z0-9]{8}`.  Result,
stage, transaction, and lock bindings retain directory fds and recheck device
and inode across every boundary.  Leaf seals include mode, link count, size,
mtime, and ctime.  Exit 74 means `ROLLED_BACK_VERIFIED`; exit 75 means
`LIVE_COMMITTED_WITH_DEBRIS`; all uncertain atomic failures retain recovery
evidence and forbid blind retry.

This is not a same-UID concurrent-mutator security boundary.  The trusted
parent must provide no concurrent pathname mutator between an external child
`exec` and that child's first path open.  Closing that launch window would
require producer/checker interfaces that accept inherited directory fds.
Likewise, the dynamic loader precedes Bash: a trusted parent must leave
`LD_PRELOAD`, `LD_LIBRARY_PATH`, `BASH_ENV`, `ENV`, `PYTHONOPTIMIZE`,
`PYTHONPATH`, `PYTHONHOME`, `PYTHONSAFEPATH`, and `C61_TEST_EVIDENCE_DIR`
unset before invoking `/usr/bin/bash -p ./run_all.sh`.

The literal semantic firewall remains `NO_BAD_EULER_OR_ROOT_NUMBER`; all 30
scope nonclaims remain Boolean `false`.  The independent runtime report binds
19,078 payload leaves, 29 schema leaves, 19,109 value and 19,109 type
rejections, 14 structural rejections, six group plus four resolver evidence
rebounds, and two additional artifact rebounds.  The asserted state is only
`PREFREEZE_CODE_RESULTS_PASS`; no paper result, authoritative refresh,
promotion authorization, or release is asserted here.
