# Static Stage-0 science candidate

This is the output-free static candidate for
`49-transient-phase-allocation-tree-shifts`.  It contains immutable copies
of the reviewed plan, theorem package, reciprocal audit, and root audit.  It
is neither a manuscript nor an authority, publication, repository, Route-ID,
or novelty record.

The analytic claims remain owned by the byte-locked proofs under `inputs/`.
State A is deliberately finite and has the sole evidence class
`FINITE_EXACT_FALSIFICATION_ONLY`; no passing enumeration can promote a
claim to proved status.  The production engine uses rational prime-log
forms and residue-grouped formulas.  The independent science auditor uses
its own factorization, arithmetic, direct level loops, and enumerators and
does not import production code or any project-local helper.

`python3 -I -B code/integration/run_integration.py --root ABSOLUTE_ROOT --state A` first
checks the static manifest, raw PREOUTPUT seal, copied-source lock, schemas,
engine separation, and mutations from a hostile working directory with
isolated Python.  Only after every check passes may it atomically create
files below `outputs/state_A/`.  The canonical candidate itself must retain
no `outputs/` node and no cache, symlink, nonregular node, manuscript, PDF,
README, final paper manifest, publication seal, or Git metadata.

The entrypoint and the dynamic result-schema auditor fail closed unless the
orchestrator itself is already running with isolated imports and bytecode
writes disabled (`-I -B`).

Before reading or hashing either self-excluded static anchor, both the parent
entrypoint and static verifier use `lstat`: the candidate root must be a real
directory at mode `0755`, and `STATIC_MANIFEST.json` plus
`PREOUTPUT_SEAL.txt` must each be real regular files at mode `0644`.  When an
`outputs/` root exists for an idempotent replay, it must itself be a real
directory at mode `0755` with the exact child namespace `state_A`;
descendant modes remain manifest-audited.  Manifest/seal rewrites require
platform `O_NOFOLLOW` support and fail closed if it is unavailable.

The Route expectation is intentionally unassigned.  No `SD-C` identifier is
present or implied.
