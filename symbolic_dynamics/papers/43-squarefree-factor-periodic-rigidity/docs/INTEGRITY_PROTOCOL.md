# Paper 43 integrity and portability protocol

## Static phase

`STATIC_INPUT_SHA256SUMS.txt` is C-sorted, unique, path-safe, hash-valid, and
self-excluding. It binds all code, contracts, experiments, documentation,
portable source containers, immutable research/DA bytes, the writer manifest
pointer, the complete result-free writer baseline, the deterministic
authority-root research lock, and the explicit empty-output status. It
excludes canonical outputs, the forbidden State-A paper manifest, and the
authority writer/root-lock overlay paths whose exact ownership is audited by
a separate whole-tree state machine.

The source snapshot has exactly 40 sorted unique IDs. Every entry resolves to
one package-relative canonical base64url container with both a container hash
and a decoded-byte hash. The independent resolver checks the container schema,
typed role, exact decoded bytes, order, and uniqueness. Historical provenance
text therefore remains recoverable without placing host-specific paths in the
portable static tree. Canonical execution does not query the live historical
tree or network. The full 17-file writer tree is an archived publication-input
baseline rather than an experiment-managed output: its self-excluding
manifest, every content byte, and the unique Section-6 insertion anchor are
vendored and replayed.

## Authority overlay ownership

The static manifest builder excludes exactly the contract's writer/root-lock
overlay allowlist, and the result ledger never owns those paths. The read-only
auditor separately recognizes three states. `CANDIDATE_NO_OVERLAY` has none of
the overlay paths. `AUTHORITY_BASELINE_RESULT_FREE` has the exact 17 writer
content files, their exact baseline manifest, and the exact deterministic root
research lock, with no PDF or compilation report. `AUTHORITY_PUBLICATION_SYNC`
changes exactly `PAPER_PLAN.md`, `WRITER_HANDOFF.md`, and
`sections/6_sharpness_route.tex`, regenerates the writer manifest, retains the
root lock exactly, and adds both `main.pdf` and `COMPILATION_REPORT.md`.
Unlisted extras, missing files, partial artifacts, unauthorized writer edits,
or a changed root lock reject. Text files undergo strict UTF-8, newline, trailing
space, and host-token checks; `main.pdf` is treated as a bounded binary PDF,
not decoded as text.

## Process isolation

Every Python child is invoked with `-I -B` from an unrelated working
directory and a hostile `PYTHONPATH`. The producer, Algorithm C, Algorithm F,
Route renderer, strict validator, independent auditor, mutation harness, and
read-only integrity auditor are separate programs. The two scientific
algorithms contain no project-local import edge.

## Transaction boundary

The parent first copies only statically sealed bytes into separate A, B, and
relocated C roots. It computes the packet, both scientific wrappers, canonical
science, Route card, and two Route audits in each root and requires byte
identity. It then assembles all 53 outputs in a disposable tree, runs all
adversarial controls. Output- and static-domain mutations are applied to
disposable complete copies and must make the independent auditor exit
nonzero; pass flags or stale-ledger detection alone are not accepted. The
parent then verifies the self-excluding result ledger and obtains
the exact canonical stdout of the read-only integrity auditor.

The class registry does not impose one consumer set on heterogeneous
instances.  Each emitted instance instead carries its exact domain, variant,
designated consumers, and expectation.  The harness requires the observed
outcome-key set to equal the declared consumer set; the read-only auditor
independently rederives the profile from the instance ID and checks it against
the registry's allowed profiles. Positive relocation/isolation/hygiene
controls occupy a separate array with exact success tokens. Two additional
positive controls install the exact authority baseline and simulated bounded
publication overlay; paired negative controls exercise extra/missing writer
paths, unauthorized writer edits, missing/tampered root lock, and partial
publication artifacts.

For every canonical result and certificate, the auditor recursively compares
the exact JSON type and value at every node and then compares the complete
canonical byte rendering. Coordinated output mutations exercise integer to
Boolean, Boolean to integer, and integer to floating-point substitutions while
also regenerating the result ledger and the report's ledger binding. Thus a
rejection cannot be credited to stale checksums, and Python equivalences such
as `True == 1` or `1 == 1.0` cannot satisfy the evidence contract.

Only after those gates succeed are changed target files installed. The
`--force-late-failure` mode exits after complete stage validation and before
the first target write. A second complete invocation must generate the same
bytes and perform zero physical writes. Partial or extra pre-existing output
names stop the parent rather than being silently deleted.

## Paired provenance states

State A requires an absent `PAPER_MANIFEST.sha256`, the exact pending commit
triple, and a retrospective freeze note. State B requires one real nonzero
lowercase 40-hex Stage-1 commit in all three fields, an exact metadata-only
freeze note, and a valid self-excluding paper manifest. All mixed states
reject. The only legal A-to-B changed paths are the canonical Route card and
the new paper manifest.

The strict Route terminal mapping has four keyed fields, including the
literature disposition. `STOP_DUPLICATE` is deliberately absent from the
Route mapping and remains an external conditional claim-boundary control.
