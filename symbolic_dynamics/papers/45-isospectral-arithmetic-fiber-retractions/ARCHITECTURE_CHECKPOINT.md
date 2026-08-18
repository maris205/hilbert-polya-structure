# Paper 45 integration architecture checkpoint

Status: `PREOUTPUT_HOLD_FOR_INDEPENDENT_STATIC_AUDIT`.

The immutable input is the 17-file tree at `inputs/preauthority/`.  Its
self-excluding manifest has SHA-256
`4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849`.
Every file in that tree is mode `0444`; the directory is mode `0555`.

## Physical lanes

- `code/evaluator_a/`: direct trial-division maps, enumeration, and rank-one
  finite matrices.  It emits 21 finite records and exactly zero infinite
  records.
- `code/evaluator_b/`: an independently authored sieve/exponent-state,
  closed-fiber, Euler, and analytic lane.  It emits the independently
  reconstructed same 21 finite records and the exact frozen 15-case infinite
  certificate sequence.  Every analytic case carries a formula AST, local
  Euler factors indexed by every frozen parameter and sampled prime,
  endpoint/witness provenance, and directed 768-bit partial-product
  enclosures. Power-S and power-M, the two commutator products and their
  difference, C/D/eigen constants, Tauberian inversion, three primorial
  regimes, and the free-UFD clone are distinct typed operation families.
- `code/proof_auditor/`: a third implementation which derives proof and
  analytic anchors from the frozen proof package, parses section-byte and
  normalized semantic AST bindings plus typed quantifier/operator/domain/
  witness/conclusion nodes. It derives each certificate triple from those
  nodes, independently rebuilds every formula, recomputes each Euler witness
  at 320 decimal digits, and checks B case by case.
  It emits exactly the same 15 IDs, owner closure, three hashes, and an
  overall verdict equivalent to the conjunction of the 15 verdicts.
- `code/comparator/`: a non-scientific comparator for the common finite
  projection only.  It is forbidden to consume infinite records.
- `code/auditors/`: source, type, independence, and integrity auditors.
- `code/route_main/` and `code/route_independent/`: separately authored
  strict Route-v0.2 validators.  Neither owns a GO/HOLD/STOP publication
  token.

A and B do not import a common production module, do not read one another's
source or output, and contain their own parsers, factorization code,
canonical AST/JCS implementation, interval construction, and finite-case
expansion.  The driver exposes neither output until both sealed evaluator
processes have completed.

## Evidence and mutation boundaries

The A namespace is finite only.  The B namespace owns all 15 frozen INF
certificates in bytewise C-sort order.  P audits precisely that ordered set,
whose LF-joined hash is
`6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84`.
For each case, B owns `certificate_owner=B`; P owns `audit_owner=P`; P copies
and verifies the payload, proof-dependency, and analytic-derivation hashes.

All 75 registered mutations are performed on fresh disposable physical
copies.  Consumers never read the registry and receive neither a mutation ID
nor an expected result.  A normal validator derives a fixed semantic code
from the actual malformed case/output/Route/filesystem artifact; only the
harness compares that code with the immutable registry.  A kill requires
every and only the designated consumers, exit 2, and the exact row code.  The
separate frozen external auditor repeats the physical protocol, exercises
eight recursive type/key/order attacks, and runs 32 independent audit
reproductions (including all 15 proof-source edits and eight reclosed analytic
AST/output edits) without adding rows to the registry.

## Transaction and chronology

`PRE_CERT` verifies the immutable input, strict contracts, parser grid,
Route validators, physical separation, and read-only source seals without
creating `results` or a cache.  `FINAL` repeats PRE_CERT, runs A and B under
mutual source/output embargoes, seals both outputs, then runs P, X, all 75
mutations, and the report reconstruction.

Before the first filesystem output action, the driver requires an exact
disposable-root marker under an explicit `/tmp` root, rejects symlinks,
ignores hostile temporary-directory environment variables, and validates
path containment, file kinds, the exact eight-path whitelist, and target
state.  It builds all eight files in a sibling stage,
validates the complete stage and a self-excluding C-sorted manifest, and
installs it with one same-filesystem directory rename.  A forced failure at
the registered late checkpoint removes only the stage and requires the
target's full `(path, file_type, sha256, size_bytes, mode, mtime_ns)` state to
remain bytewise unchanged.  Every run with a pre-existing target first
rebuilds a fresh canonical eight-file sibling from frozen inputs and code,
then compares bytes and recursive kind/mode/hash/size/mtime metadata.  It
never trusts the target manifest.  An identical rebuild performs zero
physical replacements; a different target is rejected without a write.

Candidate state is intentionally result-free: `results` and every cache
path are absent.  Only disposable `/tmp` clones may be executed before an
independent audit accepts the final pre-output static seal.
