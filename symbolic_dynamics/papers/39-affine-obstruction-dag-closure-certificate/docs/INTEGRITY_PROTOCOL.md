# Paper 39 authority integrity protocol

The authority experiment is a deterministic reconstruction from immutable
local inputs. It has no network, target-data, mirror, Git, mutable-writer, or
`/tmp` runtime dependency.

The complete runner must:

1. verify the research, prototype, plan, dependency, predecessor, registry,
   Route-A evaluator, and bridge hashes before accepting science;
2. launch source, main evaluator, and independent evaluator in distinct fresh
   Python processes, with no cross-directory imports;
3. create runs A and B from empty output directories and require exact source,
   science, and Route bytes;
4. reproduce the 535/535 and 278/278 evaluator counts, 29/29 dual mutation
   rejection, and science SHA-256
   `77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93`;
5. run an empty-results isolated cold copy with external provenance hidden,
   then run that complete copy a second time with zero changed managed paths;
6. freeze exact result and text sets plus a SHA-256 ledger that excludes
   itself, the mutable fixed Route card, and `PAPER_MANIFEST.sha256`;
7. verify UTF-8/LF/exact-one-EOF/trailing/control hygiene, exact Python import
   dependencies, and no symlinks/caches/bytecode/hidden temporary residue;
8. require normal and hidden-provenance standalone audit stdout to be
   byte-identical; and
9. construct an isolated dummy Stage-2 seal, verify its complete manifest, and
   require its normal and hidden audit bytes to reproduce the stored Stage-1
   audit exactly, while rejecting every frozen mixed-state control.

The fixed Route card is
`evaluations/route_a/SD-C41/2026-08-16.yaml`. In Stage 1 its `source_commit`,
top-level `code_commit`, and `source_lock.code_commit` are all exactly
`PENDING_FIRST_ARTIFACT_COMMIT`, its Stage-1 note is exact, and the root
manifest is absent. Stage 2 is metadata-only: it may change only those
fixed-card metadata bytes and add the root manifest.

The read-only auditor accepts exactly two paired live states. State A is the
Stage-1 state just described. State B has a present regular-file manifest,
three identical lowercase nonzero 40-hex commit fields, and an exact seal note
binding those fields to the Stage-1 artifact commit. In State B the auditor
independently requires the manifest to use lowercase SHA-256 plus two spaces,
have sorted unique safe relative paths, exclude itself, enumerate the exact
current file set, and match every declared hash. Pending fields with a
manifest, sealed fields without a manifest, mismatched fields or notes, and
malformed/inexact manifests all fail. Check names, counts, and passing values
are state-independent, so legal A and B audits are byte-identical.

The 6-node/5-edge executable spine is only a projection. The retained
22-node/28-edge proof DAG, 17 tags, 14-class 6/6/2 census, 16-token 8/8 census,
E36--37 four-field reset, E22 zero-credit firewall, distinct live/empty
registry branches, and retrospective timing boundary are scientific
invariants checked independently by both evaluators.
