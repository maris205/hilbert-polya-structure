# R401-VAL-L2-A1 final release-provenance contract

Protocol: `R401-VAL-L2-A1`  
Contract version: `write_once_exact_hash_dag_v1`  
Status: **IMPLEMENTED_AND_MOCK_TESTED — NON-LICENSING BEFORE MAIN FREEZE**.

## Purpose

This contract fixes, before any held-out production result is inspected, the
last provenance edge for the prospective A4.15 all-slab local-complement
milestone.  It is implemented by
`scripts/build_r401_val_l2_a1_release_provenance.py`.  The script never runs
the evaluator and never assigns a broader theorem.  It can only seal an
already accepted 102-tree checker generation.

The main A1 freeze must bind the exact bytes of this contract, the release
builder, producer, independent checker, S0 schema adapter, S0 compatibility
replay, formal protocol, machine freeze, pre-freeze review, and evaluator
source, together with the CAPD dependency lock, L1 plan, and the complete
five-object accepted L1 release chain.  This is one exact 17-input mandatory
union shared by producer, checker, and release builder.  The main freeze does
not hash itself.  The final release object does not hash itself.

## Exact release prerequisites

The builder requires all of the following before it writes anything:

1. a formal protocol and machine/main freezes in the exact
   `R401-VAL-L2-A1` namespace;
2. a pre-freeze review whose sole verdict declaration is the exact line
   `Verdict: ACCEPT_FOR_FREEZE`;
3. the read-only six-tree/3,016-node S0 compatibility replay with its exact
   pass status;
4. a sealed `run_config.json` bound to the main freeze and its complete input
   hash DAG;
5. producer aggregate summary and manifest objects with all scientific status
   fields null;
6. exactly 102 manifest entries in canonical order: `128:S000..S050`, then
   `256:S000..S050`, with canonical paths and exact file hashes;
7. an authoritative independent checker and postcheck that agree on
   `PASS_LOCAL_COMPLEMENT_ALL_SLABS`, retain `final_status = null`, and bind
   the same generation;
8. a future A4.15 certificate and production report with exact accepted
   status lines and the literal boundary marker `final_status = null`.

The main freeze's `checker_source_sha256` must equal the checker entry in its
own `input_hashes` map (whose bytes are independently rehashed).  Its evaluator
object has exactly the producer/checker ABI keys `source_file`,
`source_sha256`, `binary_file`, `binary_sha256`, `capd_commit`, `capd_flags`,
and `status_returncode_whitelist`; the status/return-code whitelist is the
closed formal namespace.  The run-config binding uses the exact runner key set,
repeats the formal namespace and licensing fields with exact JSON types, and
its complete evaluator object must be byte-canonically equal to the frozen
evaluator object.

The S0 replay is a closed semantic object, not a two-counter smoke marker.
Its top-level key set is exact.  The checker and S0 adapter hashes are rebound
to their current project files, while the reported S0 release provenance,
manifest, and postcheck hashes are rebound to the three actual public S0 JSON
objects; all parses and hashes use the same captured byte snapshot.  The only
accepted totals are 6 ordered trees, 3,016 nodes, 6,055 manifest hash checks,
and status counts 183 `ENERGY_EXCLUDED`, 1,349 `RETURN_EXCLUDED`, and 1,484
`UNKNOWN`.  Each of the six ordered per-tree records has an exact key set,
integer types, identity, node count, and three-status count map:
`128:S000` (486; 18/229/239), `128:S025` (546; 31/246/269), `128:S050`
(574; 44/247/283), `256:S000` (436; 18/204/214), `256:S025`
(488; 31/217/240), and `256:S050` (486; 41/206/239), with counts shown in
`ENERGY_EXCLUDED/RETURN_EXCLUDED/UNKNOWN` order.

## Independent generation recomputation

The release builder does not trust a digest merely because it appears in the
checker output.  It independently:

- validates and hashes every one of the 102 tree-manifest files;
- reconstructs the exact ordered manifest-entry list;
- recomputes
  `sha256(canonical_json(ordered_manifest_entries))`;
- compares that result with the checker's `tree_manifest_root`;
- removes `archive_generation_sha256` from the checker's provenance binding
  object and recomputes its canonical digest;
- verifies the postcheck's checker hash, generation hash, and full provenance
  binding hash.
- reopens all 102 bound tree payloads from the same captured byte snapshot,
  recounts `evaluated_node_count` and every node classification, reconstructs
  terminal counts, and requires exact agreement with each ordered checker
  `tree_stats` record;
- rehashes the actual five accepted L1 release-chain files and requires exact
  agreement with all five hashes reported by `l1_protected_box_replay`.

The release contains exactly nineteen named artifact roles: formal protocol,
machine freeze, main freeze, pre-freeze review, S0 replay, producer, checker,
S0 adapter, release builder, this contract, evaluator source and binary, run
config, aggregate summary and manifest, independent checker, postcheck, A4.15
certificate, and production report.  Its `files` map must be exactly the set
of those nineteen paths—no missing or extra hash is accepted.

## Immutability and adversarial rules

- Every JSON input is parsed with duplicate-key and non-finite-value rejection.
- Every additional `.json` path placed in the main freeze hash map is also
  strictly parsed from the same captured bytes; an extra hash cannot turn
  ambiguous JSON into an opaque accepted blob.
- Every one of the 102 tree manifests and its bound tree object is parsed as
  strict JSON and replayed in the formal producer namespace; matching a hash
  alone is insufficient.
- JSON exponent overflow (for example `1e400`) is rejected even though Python's
  ordinary JSON parser would otherwise convert it to a non-finite float.
- Schema versions, resource counts, limits, precision bits, and all other
  frozen integer fields require the JSON integer type.  Booleans and integral
  floats are not equal substitutes.  Ordered matrix identities are compared by
  canonical JSON bytes, not Python's coercive equality.
- Project-bound role/input paths reject absolute, hidden, backslash,
  dot-segment, repeated-separator, trailing-slash, normalization-alias, NUL,
  and traversal forms.  The sole frozen evaluator binary locator is instead
  required to be a canonical absolute path and is rebound to a regular file
  inside this project before it can enter the release role map.
- A symlink in any authoritative path component is rejected before hashing.
- Duplicate artifact paths and duplicate/reordered tree identities are rejected.
- Status disagreement anywhere in the checker/postcheck/certificate chain is
  rejected.  Checker and postcheck use exact top-level schemas, so extra or
  nested metadata cannot smuggle a second authority declaration into either
  accepted object.
- Every semantic parse and its recorded digest uses one in-memory byte
  snapshot.  All opened authoritative inputs are rechecked for mutation before
  publication, so a certificate or JSON object cannot be swapped between its
  semantic gate and its hash.
- Publication creates an unpredictable same-directory temporary through a
  pinned directory descriptor, keeps its descriptor open, and hard-links
  `/proc/self/fd/<fd>` rather than the mutable temporary pathname.  The
  published device, inode, and exact bytes are then checked before success.  An
  identical existing release is accepted; a different existing release is
  never overwritten, including under a publication race.
- A pre-existing release with a second hard-link name is rejected.  The
  production result directory is an operator-owned single-writer directory;
  these checks detect accidental/concurrent publication races but do not claim
  isolation from a malicious same-UID process with authority to rewrite that
  directory.
- `--verify-only` performs no write and replays the entire release DAG from
  current bytes.  It also requires the release itself to have the exact
  canonical serialized bytes emitted by the builder; reordered or minified
  semantically equivalent JSON is rejected.
- The certificate and production report each contain exactly one ordered
  five-line authority block (`Status`, `milestone_status`, `theorem_status`,
  null `final_status`, and the frozen claim boundary).  Appended or conflicting
  declarations are rejected.  Declaration discovery treats every standalone
  `Status`, arbitrary `*_status`, `Verdict`, `promotion_authorized`, or
  `Claim boundary` token as a candidate without enumerating separators.  Thus
  Markdown escapes, HTML entities, tables, dashes, full-width punctuation, and
  bare tokens all reach the exact-line comparison.  The pre-freeze `Verdict`
  gate applies the same standalone-token rule before demanding its one literal
  accepted ASCII line.

## Claim boundary

Even a passing release certifies only pointwise reduced-root uniqueness in the
frozen local `P_+=0` chart over the frozen 51 slabs.  It is not an energy-shell
or global phase-cover result, not a trace formula, not an arithmetic-prime
result, not a Hilbert--Polya operator, not a Riemann-zero reconstruction, and
not a result toward RH.  The final scientific status remains null.
