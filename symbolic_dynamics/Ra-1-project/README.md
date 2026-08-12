# Ra-1-project — Hilbert–Pólya Symbolic Dynamics

This directory contains all generated research outputs for the
symbolic-dynamics branch: stage reports, papers, proofs, experiments, numerical
results, evaluations, and reproducibility manifests.

Naming convention: `R<route>-<roadmap-phase>-<project>`.  Here `Ra-1` is the
current Route-A roadmap-phase marker, and the final component names its
subproject container (currently `project`).

The concise cross-stage conclusions and shareable-paper links live in the
[root README](../README.md).  Shared inputs remain outside this subproject:

- [research proposal](../propose-symbolic-dynamics.md);
- [Route-A evaluator](../skills/route-a-evaluator.md);
- [Route-B evaluator](../skills/route-b-evaluator.md);
- [prior-work corpus guide](../docs/prior_work/README.md).

## Stages

- [Stage 01 — scope screening](stages/stage_01_scope_screening/README.md)
- [Stage 02 — wheel-sieve stationarization audit](stages/stage_02_stationary_wheel_extension/README.md)
- [stage lifecycle and status vocabulary](stages/README.md)

Each stage owns a `paper/` directory with a shareable PDF, LaTeX source,
figures, a claims–evidence plan, and its two-round improvement log.

`PROJECT_MANIFEST.sha256` covers this subproject and is verified from this
directory.  Each stage also has a stage-local `STAGE_MANIFEST.sha256`.
