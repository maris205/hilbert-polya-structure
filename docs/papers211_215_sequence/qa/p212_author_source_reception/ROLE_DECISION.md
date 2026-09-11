# Exact P212 source and artifact interface

2026-09-09 UTC. Root decision after complete source reception. This is an
additive interface decision before any P212 scientific invocation or review
package generation, not a runtime binding or execution authorization.

The inherited [artifact contract](../../../papers204_208_sequence/ARTIFACT_CONTRACT.md)
applies directly. The paper root is `papers/212-closed-pointer-orbits/` under
the workspace. The following roles are now fixed:

| Role | Exact paper-relative path / interface |
|---|---|
| Independent-source author program | `verify.py`, SHA-256 `16cc2ff86854c6c28d530de65225b941f9e063fa22159ccd8f0c4082b80654e7` |
| Sole explicit scientific data | `PARAMETERS.json`, SHA-256 `0870d9de8a1e2dde2c568656ea69b39511ae3a8ebf992f787c6e5ae060ca4550` |
| Application arguments | `verify.py --parameters ABSOLUTE_PARAMETERS_JSON`; actual absolute program/parameter paths, interpreter flags and runtime settings require a later exact binding |
| Actual accepted author stdout | `CANONICAL.json`, created exclusively from the complete accepted initial raw stdout; absent at this decision |
| Historical prospective name | `canonical.stdout.json` stays absent; it is not a second canonical or an alias |
| Frozen scientific/documentary inputs | `frozen_round0/`, `frozen_round1/`, `frozen_round2/`, each physical with a complete directory-relative nonself `SHA256SUMS` |
| Terminal physical builds | `qa_final/cold_build_1/` and `qa_final/cold_build_2/` |

`OUTPUT_PLAN.md` expressly permits root to fix a different exact canonical
path before adoption. Selecting `CANONICAL.json` therefore changes no
scientific source, parameter, output field or serialized byte convention.
The complete 22-file original preparation is physically retained under
[source_preparation_original](source_preparation_original/), including its
old prospective wording and its original manifest. Nothing is renamed or
overwritten to force a historical manifest to describe a later lifecycle.

The exact review package paths will be the inherited current-batch
`reviews/p212_a/` and `reviews/p212_b/`. Their required roles remain one
standalone `verify.py`, one actual `CANONICAL.json`, `REPORT.md`,
`REPLAY_LOG.md`, `SOURCE_AND_PROOF.md`, `BUILD_REPORT.md`,
`INPUT_PINS.sha256`, `FINDINGS.json`, `DELTA.md` and complete nonself
`SHA256SUMS`, with all additional actual evidence sealed too. Paper-package
manifests are package-relative; review input pins are workspace-relative.
No review package is generated at this source milestone. The two concrete
nonauthor processes must be assigned and their familiarity disclosed before
their actual review tasks; neither candidate admission nor this source
reception is either manuscript review.

All four actual contributor roles listed in the unchanged paper README are
authors and ineligible to review P212: root; original pointer scout;
paper-source author; and paper-local verifier coauthor. No agent is made
independent merely by changing its task name. Infrastructure-only work must
remain distinguished from a new mathematical or scientific contribution.

Exactly the four complete carriers 1,2,3,4 remain authorized for future
preparation. The initial accepted output must precede canonical adoption;
a separately bound strict pair must then perform two real runs and all three
raw comparisons. This decision does not approve any as-yet-unread runtime
adapter, host lock, import, AST parse, compilation, scientific run, build,
freeze, review verdict or completion. OWNER_AMBER / HOLD_EXTERNAL.
