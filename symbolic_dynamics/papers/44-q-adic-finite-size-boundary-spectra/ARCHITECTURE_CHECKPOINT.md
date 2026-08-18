# P44 isolated integration architecture checkpoint

Checkpoint date: `2026-08-18 UTC`

Status: `SUPERSEDING_REPAIR_ARCHITECTURE_IMPLEMENTED_PREOUTPUT_STATIC_SEALED`

## Frozen input gate

The only research input is the immutable directory `preauthority/`.  Its
self-excluding manifest is `preauthority/SHA256SUMS.txt`, whose SHA-256 is

```text
1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd
```

All 17 manifest rows were checked before copying, the exact file set matched,
the rows were C-sorted and unique, and the source contained no symbolic link.
The copied tree was then made non-writable and checked again.  No authority,
Git, root-README, mirror, registry, or repository-manifest path is an input or
an output of this architecture.

## Evidence boundary

The executable layer has two disjoint evidence classes.

1. `FINITE_EXACT_OR_CERTIFIED_DIAGNOSTIC` contains finite prefix counts,
   exact rational increment records, exact residue-coefficient identities,
   finite q-adic cylinder invariants, independently enclosed golden
   coefficients, the exact `99044` algebraic witness, and finite cyclotomic
   identities.
2. `INFINITE_THEOREM_CERTIFICATE` is owned only by the read-only proof
   auditor.  It checks the frozen proof's assumptions, dependency chain,
   uniform-tail statements, reverse accumulation inclusion, all-level
   separation certificate, dominated Abelian passage, and scope exclusions.

No finite agreement rate, cutoff, plot, interval overlap, or mutation score
is permitted to set an infinite theorem field to true.  The Ban--Hu--Lai
author-manuscript correction boundary remains immutable in
`preauthority/LITERATURE_NOVELTY_AUDIT.md` and
`preauthority/SOURCE_LOCK.md`; the source auditor verifies those exact frozen
bytes and keeps the version-of-record caveat and zero-credit ownership.

## Physical independence

Evaluator A and Evaluator B are standalone Python programs in different
directories.  Neither imports any project-local module.

- Evaluator A constructs the finite source graph on `[1,N]`, finds its
  connected components, and exhaustively counts component labelings against
  the literal edges `n -> q*n`.  It derives residue identities from integer
  cutoffs and obtains golden coefficients from Fibonacci-ratio log intervals.
- Evaluator B independently parses and expands the neutral raw manifest,
  generates primitive matrices using its own primitive test, computes word
  counts by integer matrix-vector powers, constructs the closed
  chain-histogram product, evaluates the positive Binet series, and checks
  cyclotomic identities in `Q[x]/(x^(Q/2)+1)`.

They share only immutable raw configurations and public typed schemas.  They
do not share helpers, expanded fixtures, expected tables, serialized
intermediates, caches, or generated outputs.  A separate exact comparator
accepts only equal canonical case sets and recursively type-equal values;
Python's `True == 1` and `1 == 1.0` are explicitly insufficient.

## Independent auditors

The integration has separate, non-importing consumers for:

- proof and quantifier certificates (`P`);
- source, literature ownership, and correction boundary (`L`);
- object, marker, analytic, and residue types (`T`);
- evaluator import/file-access separation (`I`);
- primary and independent full-object Route-A v0.3 validation (`R1`, `R2`);
- exact comparison (`X`); and
- a frozen whole-tree auditor outside the producer namespace (`F`).

Each auditor writes only a typed canonical envelope.  The frozen auditor is
also tested externally on disposable copies with byte drift, file-mode drift,
an extra empty directory, a FIFO, a symlink, deletion, seal-key drift, and
manifest-order drift.

## Typed contracts and adversarial instances

`contracts/CASE_REGISTRY.json` fixes raw case expansion, stable case-ID
serialization, precision levels, digit-stream cases, evidence classes, and
canonical record schemas without embedding an expected scientific output.
`contracts/MUTATION_REGISTRY.json` expands the 19 frozen mutation families
into concrete instances (the reducible and period-two `MUT-APR` controls are
separate instances).  Every instance freezes its literal payload, domain,
exact designated-consumer set, exact rejection code, and required process
exit `2`.

The mutation harness requires every and only the designated consumers.  A
consumer that is missing, unlisted, returns zero, returns a different code,
emits a noncanonical envelope, or raises an uncaught exception makes the
mutation survive and fails the run.

## Canonical reconstruction and namespace

All runtime artifacts live under one package-relative `outputs/` directory.
The exact State-A and State-B namespaces recursively bind every path, node
kind, mode, and regular-file hash.  Extra empty directories, chmod drift,
nonregular nodes, symlinks, renamed nodes, and missing nodes reject.  Reports
are reconstructed solely from independently rerun canonical result objects;
the result ledger and runtime integrity auditor reconstruct the comparison,
P/L/T/I, the complete mutation records, both Route audits, report, ledger,
exact set, and provenance state rather than trusting stored `PASS` labels.

The only legal integrity phases are `PRE_CERT` and `FINAL`.  `PRE_CERT`
requires the certificate and State-B paper manifest to be absent and emits the
exact final certificate.  `FINAL` reconstructs that certificate byte for byte
without writing, then verifies the final namespace and State-B manifest.

- State A is preauthority: commit sentinels are exact, and
  `PAPER_MANIFEST.sha256` is forbidden.
- State B is publication-shaped only: three equal nonzero lowercase 40-hex
  commit fields and an exact physical self-excluding paper manifest are
  mandatory.  That manifest excludes both itself and
  `PREOUTPUT_STATIC_SEAL.json`; the static tree manifest also excludes the
  seal, so the final seal DAG is acyclic.  Mixed A/B states reject.

The State-A and State-B `final_tree_sha256` values are hashes of canonical
recursive rows strictly below `outputs/` only.  The static root, static
manifest, and `PREOUTPUT_STATIC_SEAL.json` are outside that domain.  A
disposable control changes one seal byte, observes the identical output-tree
hash before and after, and requires the frozen auditor to reject the changed
seal; this makes the exclusion both explicit and physically exercised.

`STOP_DUPLICATE` remains an external literature disposition and never becomes
a Route terminal.  The strict Route tuple remains
`[A0_FAIL, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]` with
overall `ROUTE_A_REJECTED`; Route B remains locked.

## Transaction and environment model

Before opening any caller-selected path or creating any target byte, the
parent validates lexical containment, resolved-parent containment, the
absence of symlinks, the exact output namespace, and the static input seal.
Every subprocess runs from an unrelated hostile working directory with
`python -I -B`, a minimal allowlisted environment, hostile `PYTHONPATH`, and
cache writes disabled.

The parent builds every byte in a disposable sibling stage, validates two
byte-identical reconstructions plus a relocated reconstruction, runs all
scientific and frozen-auditor mutations, and only then atomically renames the
single staged `outputs/` directory.  A forced late failure occurs after all
validation but before that rename.  If an already installed tree is exactly
equal, a second run performs zero physical target writes.

## Pre-output rule

The canonical candidate itself is never executed.  It must retain zero files
under `outputs/` and zero cache files.  Full smoke, late-failure, first-install,
idempotence, relocation, and State-B checks run only in fresh disposable
clones.  After those controls pass, one `PREOUTPUT_STATIC_SEAL.json` records
the complete frozen-input map, static inventory hash, contract counts,
namespace counts, smoke hashes, first-install count, late-failure unchanged
certificate, second-run zero-write certificate, and the continuing
zero-output state of this candidate.
