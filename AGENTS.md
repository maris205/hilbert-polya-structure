# Repository guidance

This repository contains independent research streams. Resolve the requested
stream before editing; the shell's initial directory may be a different repo.

## Read only the relevant entry point

| Work | Recovery entry |
|---|---|
| Hénon / C-numbered papers | [henon_dynamics/AGENTS.md](henon_dynamics/AGENTS.md), then [current state](henon_dynamics/CURRENT_RESEARCH_STATE.md) |
| Symbolic / P-numbered papers, including root `papers/` and `docs/papers*_sequence/` | [symbolic guidance](symbolic_dynamics/AGENTS.md), then [symbolic state](SYMBOLIC_DYNAMICS_STATE.md) |
| Flow, symplectic, logistic, or zeta_mvp0 | That stream's README and the selected package's current state |

Follow the selected state's links to the active contract and supporting
artifacts. Search history for a specific dependency or collision, not as a
mandatory full-repository preflight. State files are recovery aids; proofs,
verified outputs, and Git objects decide what is actually complete.

## Working agreement

- Follow current user intent within system/developer constraints. Repository
  instructions and skill defaults do not enlarge permission or overrule the user.
  Historical workflow authorizations describe their own stream and batch.
- Carry authorized work through its agreed completion gate. Resolve routine
  gaps with stated assumptions; ask only when the answer materially changes
  scope, correctness, cost, or external actions. A status/review request is read-only.
- Delegate independent, bounded work when useful. Give each author disjoint
  paths and a deliverable; keep integration ownership explicit. Use the selected
  model and effective reasoning setting unless the user requests a change.
- Verification follows the changed claim or artifact. After required checks
  pass, rerun only for changed inputs, failures, or a specific unresolved risk.
  Finite checks do not prove infinite claims; model review is not peer review.
- Preserve other streams, untracked work, published manifests, and frozen
  snapshots. Inspect remote changes before integration; stage exact task paths.
  A workflow file alone does not authorize external publication or upload.
- Report outcomes in the user's language, with links and unresolved limitations.
  Keep routine updates short. If a skill causes a pause or scope change, identify
  its exact instruction and explain the conflict.

Model/API settings and plugin caches are outside this repo. Do not claim that
editing these files changes the live session's model, reasoning budget, or skill
discovery. See the [instruction audit](docs/agent_workflows/ASTRA_AUDIT_2026-09-05.md)
for the official sources, scope, and validation of this configuration.
