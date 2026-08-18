# P46 isolated integration architecture checkpoint

Checkpoint date: `2026-08-18 UTC`

Status: `ARCHITECTURE_FROZEN_BEFORE_IMPLEMENTATION`

## Frozen-input gate

The only research input is the immutable directory `preauthority/`. Its
self-excluding manifest is `preauthority/SHA256SUMS.txt`, whose SHA-256 is

```text
fc132644764bb93927dbcd5cbf63917e48e2c512d72adc375ef7590210226bab
```

All 15 rows were verified before copying, the copied file set is exact, no
symbolic link was accepted, the copied tree was made non-writable, and the
manifest was verified again. Authority, Git, repository README, mirror,
registry, and repository-manifest paths are outside this architecture.

## Two physically independent evaluators

Evaluator M is a standalone program that constructs a finite matrix from the
literal bit predicate, enumerates based walks directly, multiplies exact
rational matrices, and derives valuation blocks from the resulting edges.

Evaluator C is a second standalone program that never constructs or imports
M's matrix or walk routines. It enumerates dyadic anti-diagonals, solves the
ordered cyclic equations by the odd/even recurrence, and evaluates traces by
its own valuation-block/cyclic solver. The only shared research input is the
typed raw case contract; no helper, expanded fixture, expected table, cache,
or serialized intermediate is shared.

The finite cutoff identity is always the scale-dependent sum

```text
sum_k 2^(-k*r*s) Tr((A_s^(floor(N/2^k)))^r).
```

The varying odd-block cutoff is retained for every `k`; no finite geometric
collapse exists in either implementation or comparison. The infinite
geometric identity is a separately typed theorem certificate owned only by
the proof auditor.

## Independent audit and evidence lanes

Separate, non-importing programs own proof/quantifier replay (`P`), recursive
object and determinant types (`T`), source/literature ownership (`S`),
evaluator independence (`I`), primary Route-A validation (`R1`), independent
Route-A validation (`R2`), and exact finite comparison (`X`). Fournier--Wagner
retains zero-credit ownership of the Schur/reflection/folding/alternating
lacunary machinery; the P46 residue is the weighted valuation direct sum,
positive cyclic closure, and legal trace/determinant ledger.

## Typed contracts and mutations

`contracts/RAW_CASE_CONTRACT.json` fixes only raw typed cases and exact
serialization. Every result is reconstructed independently. The mutation
registry atomizes every frozen falsifier F01--F14 and adds packet, result,
ledger, report, Route, provenance-state, path, namespace, symlink, cache,
auditor, and transaction instances. Every row fixes one literal payload,
domain, exact ordered designated-consumer set, exact rejection code, and
required nonzero exit `2`.

The harness is exception-total: its only outcomes are `ACCEPT`, `REJECT`, and
`HARNESS_ERROR`; any missing or extra consumer, zero exit, wrong code,
noncanonical envelope, exception, or unlisted consumer makes the instance a
survivor and fails the run. An external frozen whole-tree auditor is outside
the producer namespace and is itself mutation-tested on disposable copies.
The physical registry binds every expected exit, canonical stdout envelope,
and zero-byte stderr receipt. For the coordinated nested-count, nested-cutoff,
and comparison-Boolean attacks, the driver invokes X, T, G, and F on the
actually edited/reledgered clone; it never substitutes a synthetic mutation
switch for that physical audit.

The field-level result contract additionally fixes every recursive key set,
the 4/7/16/36 certificate array shapes, fraction encodings, and the exact
types of all counts, `N`, `r`, `s`, cutoffs, vertices, and valuations.
Integers require `type(x) is int`; Booleans are legal only at explicitly
declared Boolean paths. Coordinated M/C type changes remain invalid even if a
comparison hash and every affected result-ledger row are recomputed.

Comparator production and installed-output audit are separate modes. The
installed-output mode reconstructs the comparison from M/C and exact-compares
the stored comparison, so a coordinated comparison edit cannot be hidden by
re-running producer logic. Every X/T/G physical entry point, F, and the runner
use the frozen CLI rejection contract: unknown flags are rejected, and all
argument, path, unknown-mutation, and runtime validation failures terminate
as canonical exit-2 JSON with empty stderr and no traceback.

## Canonical reconstruction and two provenance states

Canonical JSON requires duplicate-key rejection, finite numbers, strict
recursive Python type/value equality, ASCII, sorted keys, two-space indent,
and one terminal newline. The report is rendered only from sealed result and
audit objects. The result ledger hashes every declared pre-ledger output.

State A retains all three exact pending commit sentinels and forbids a paper
manifest. State B requires the same nonzero lowercase 40-hex commit in all
three fields plus an exact acyclic paper manifest. That manifest includes the
exact package files and State-A output namespace but excludes both
`PREOUTPUT_STATIC_SEAL.json` and `outputs/PAPER_MANIFEST.sha256`. The static
manifest separately excludes itself, the pre-output seal, and `outputs/**`.
Mixed states fail. Integrity consumers G and F reconstruct this inclusion
domain independently and reject an attempted seal row.
The Route tuple is frozen as
`[A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC,
A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`, overall
`ROUTE_A_REJECTED`, and Route B is locked. `STOP_DUPLICATE` remains an
external literature disposition, never a Route terminal.

## Transaction, containment, and pre-output rule

Before opening any caller-selected path or producing a target byte, the
runner validates lexical containment, resolved-parent containment, absence
of symlinks, the exact output namespace, and the static input seal. Every
child runs from an unrelated hostile working directory under `python -I -B`,
with a minimal environment, hostile `PYTHONPATH`, and cache writes disabled.

All bytes are first materialized in a disposable sibling stage. Two canonical
reconstructions, relocation, science mutations, external-auditor mutations,
ledger/report reconstruction, Route/state checks, and integrity checks must
pass before one atomic `outputs/` rename. A forced late failure after all
validation but before rename must preserve every target byte and metadata.
If an installed tree is already exact, the second full run performs zero
physical target writes.

The integration receipt hashes only the final output map, using each relative
output path, a NUL delimiter, and its raw bytes. No package-static byte and no
pre-output-seal byte enters that tree domain. The pre-output seal records this
acyclic manifest/tree evidence but never records its own hash internally;
changing only seal bytes must leave a fresh State-B manifest, output map, and
tree hash unchanged.

The canonical candidate is never executed and must retain zero canonical
outputs and zero cache files. Full smoke, first install, late failure,
idempotence, relocation, and State-B checks run only in fresh disposable
clones. The final act is a single pre-output static seal containing contract
counts, namespace counts, static inventory, smoke hashes, first-write count,
late-failure unchanged evidence, second-run zero-write evidence, and the
candidate's continuing zero-output state.
