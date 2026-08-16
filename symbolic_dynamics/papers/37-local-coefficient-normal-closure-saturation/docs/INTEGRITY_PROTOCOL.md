# Paper 37 integration integrity protocol

The managed artifact set is limited to the root `EXPERIMENT_REPORT.md`,
`code/`, `results/`, `experiments/`, `docs/`, and
`evaluations/route_a/SD-C39/`. Other writer-owned files are pinned by
`docs/RESEARCH_LOCK.json` and are never rewritten.

`results/SHA256SUMS.txt` is the immutable Stage-1 ledger. Each line is
`sha256  relative/path`; paths are unique and bytewise sorted. The ledger
structurally excludes itself, the mutable Route card
`evaluations/route_a/SD-C39/2026-08-15.yaml`, and the root
`PAPER_MANIFEST.sha256`. The last file must be absent in Stage 1 and, if an
owner later creates it at Stage 2, must be a sorted, unique, self-excluding
manifest of the exact paper tree.

Every managed text artifact, including the Route card and ledger, must decode
as UTF-8 without a BOM, contain LF rather than CRLF, and end in exactly one
LF. Cache directories and Python bytecode are forbidden. The cold run uses a
temporary copy below `results/` that is removed before integrity freeze.

Scientific stability is checked under four transport-metadata states
(absent, null, empty mapping, populated mapping) and under simulated absence
and presence of future manifest metadata. Metadata never enters the canonical
scientific payload or independent Route evaluation.
