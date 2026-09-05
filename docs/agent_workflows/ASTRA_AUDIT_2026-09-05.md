# GPT-6 Astra repository instruction audit

Date: 2026-09-05. Baseline: `34c3781c7ad7231048ed01cc6ff174f3ded99433`.
Scope: `/root/autodl-tmp/hilbert-polya-structure`; repository guidance and the
prospective Hénon C-series workflow. This is not a new scientific paper.

## Official basis

The exact requested model was checked in current official documentation, not
substituted with an older model. Pages were opened; their Markdown bodies were
also fetched because the browser's Markdown reader rejected the content type.

- [GPT-6 Astra guidance](https://developers.openai.com/api/docs/guides/latest-model):
  clearer scope and initiative, instruction-conflict audits, useful parallel
  delegation, concise communication, and verification proportional to changes.
- [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md):
  directory-scoped guidance and precedence; instructions are assembled when a
  run starts. A new file does not retroactively prove live-session discovery.
- [Skills authoring and discovery](https://learn.chatgpt.com/docs/build-skills):
  repo-local `.agents/skills`, required `SKILL.md` metadata, progressive loading,
  focused triggers, and behavioral checks.
- [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra):
  exact model identifier. No pricing, access, latency, or reasoning-maximization
  claim is needed for this repository change.

The local `openai-docs` and `skill-creator` workflows informed source checking,
scope preservation, concise skill design, and independent forward-testing.
Official guidance is adapted to this repository; no prompt template was copied
as an unconditional permission grant.

## Coverage and findings

A read-only inventory covered tracked instruction filenames across the entire
repository, all eight evaluator entrypoints, and all 27 standing-workflow
authorization files. A second agent searched 74 selected entry/protocol files
and examined current symbolic recovery and authorization documents. Deep
mathematical review of all historical papers was outside this audit.

| Surface before change | Finding | Treatment |
|---|---|---|
| Repository root | No AGENTS or discoverable repo skill | Added concise stream router and a narrowly triggered C-series skill |
| `symbolic_dynamics/AGENTS.md` | Its guidance did not cover newer root `papers/` and `docs/` paths automatically | Root router now explicitly selects its guidance for symbolic tasks; its 13 lines remain unchanged |
| Four streams' A/B evaluators | Eight files, 5,078 lines; identical names with distinct versions/path semantics | Preserved all bytes; route to the correct pinned authority only when needed |
| Hénon local evaluator | v0.1.0; latest C-series packages actually pin flow v0.2.0 | Explicit authority in Hénon AGENTS and skill; no false upgrade of historical evidence |
| Long stream READMEs | Histories of hundreds of papers are poor routine recovery prompts | Short state first; targeted historical lookup for dependencies/collisions |
| Hénon recovery file | Repeated policy, previous final integration steps, and completed-batch details | Reduced to current authorization, state, evidence links, and local invariants |
| Historic standing authorizations | Stream/batch-specific provenance, not general permission | Kept all 27 unchanged; new instructions distinguish current authorization |
| New-paper workflow | Repetitive artifact shapes and blanket review/test cycles can obscure the scientific increment | Prospective workflow uses complete theorem contracts and change-dependent checks; old contracts remain binding |

### Why evaluator deduplication was not performed

Flow and symplectic A files are byte-identical, as are their B files. Symbolic
v0.2 adds stage/path-base handling. Hénon local files are v0.1 without the current
A0 entry gate. More importantly, released checkers verify the live authority
hash; even a harmless heading edit would invalidate existing release checks.
The new operational layer therefore removes ambiguity without changing the
scientific criteria or resealing history.

| File | SHA256 preserved from baseline |
|---|---|
| `flow_systems/skills/route-a-evaluator.md` and `symplectic_map/skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| `flow_systems/skills/route-b-evaluator.md` and `symplectic_map/skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |
| `symbolic_dynamics/skills/route-a-evaluator.md` | `29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a` |
| `symbolic_dynamics/skills/route-b-evaluator.md` | `295412a5b5e8e6caab5555bf1a6855220c32988bea24a9d99a69f4dc672e620b` |
| `henon_dynamics/skills/route-a-evaluator.md` | `c091577908e1e74b8b0031f527fa3a6018b928e26cdd140ecca9094c5e1130c4` |
| `henon_dynamics/skills/route-b-evaluator.md` | `e5a7ce54e3d139cb5f1210433b7c8ab5df986e97a9b26a97c3502edc4f7384db` |

### External skill and runtime boundary

Read-only inspection found older GPT-5.4 reviewer/MCP defaults and fixed review
loops in installed `paper-write`, `paper-writing`, `idea-creator`, and
`auto-paper-improvement-loop` skills outside this repo. Those files and plugin
caches were not edited or disabled. Session-required skills still apply;
conflicts with the user's requested Astra workflow must be disclosed rather
than silently importing an unavailable tool or pretending it ran.

The inspected Codex config files already select `gpt-6-astra` with medium
reasoning. No account settings, model router, API credentials, service tier,
provider, context limit, or runtime were changed. API async features require
runtime support and are not enabled by an AGENTS paragraph. The session's
available collaboration tools supply the parallelism used here.

## Prospective operational changes

The entrypoint separates stable stream rules from a task-triggered workflow and
changing state. Five papers remains the user's batch contract. Paper acceptance
depends on a substantial complete result and primary-source ownership review;
it has no minimum file count, page count, or ceremonial number of revisions.
New scientific claims retain proof, independent review, applicable adversarial
checks, deterministic final PDF builds, page inspection, and manifest closure.

Passed checks may be reused only for unchanged relevant inputs/environment.
Proof changes and unresolved review findings reopen affected gates. Small index
edits do not trigger all historical theorem checkers. Old batch protocols and
live evaluator requirements are not relaxed by this prospective workflow.

## Validation status

Completed checks:

- Bundled `skill-creator/scripts/quick_validate.py`: PASS for the new skill.
- Local Markdown targets: all 26 checked links resolve at the validation snapshot.
- Byte preservation against baseline: eight evaluators, 27 historical standing
  authorizations, and the existing symbolic AGENTS, 36 files total, unchanged.
- Hénon state reduced from 125 lines / 8,054 bytes to 48 lines / 2,794 bytes at
  the first post-edit snapshot. Old detail remains in Git and linked batch records.
- `git diff --check`: PASS. No historical paper package or release manifest changed.

An independent agent read the new instructions and performed eight read-only
behavioral scenarios. These are desktop decision checks, not executed research
tasks, unit tests, or a model-performance benchmark:

| Scenario | Observed decision |
|---|---|
| Confirm next batch; replace failed subtypes | Continue authorized scouting without another routine approval |
| Fix one README link | Scope to the link and relevant checks; ask only if the link itself is unidentified |
| Status summary disagrees with pending state | Read actual evidence; do not run missing research or rewrite state under a status-only request |
| Prime table inserted in a log-prime roof | Reject the intrinsic-arithmetic success claim; do not fabricate a full evaluation |
| Symbolic continuation from repo root | Route to symbolic's own current contract, including its two-review requirement |
| Finite samples offered for an infinite theorem | Keep the new conclusion unproved; distinguish repair from a materially expanded contract |
| Date changed, relevant bytes/environment unchanged | Reuse the qualified receipt; do not claim a fresh run |
| Unavailable legacy reviewer tool | Disclose the actual requirement, use allowed prospective fallback, preserve a genuinely pinned external gate |

The review prompted explicit wording for subtype scope, narrow-versus-formal
evaluation, and unavailable-tool fallback. A missing audit link seen during
parallel construction was subsequently resolved by creating this file.
The independent agent's targeted follow-up passed: the three amendments retain
the intended scope, all eight summaries accurately describe the desktop
decisions, and the formerly missing audit link resolves. No blanket repeat of
unrelated scenarios or scientific checks was performed.

No before/after timing or controlled model-quality experiment has been run.
The changes remove identified instruction ambiguity and unnecessary prospective
ceremony; a numerical speedup or globally maximum Astra performance is not
established. Current-session use is by explicit file reading; fresh-run skill
discovery should be verified in the actual product, from this repository.

After this maintenance checkpoint, resume the user-authorized C399–C403 batch.
Do not count the audit, scouting, or empty package scaffolds as completed papers.

## Subsequent parallel-stream integration

The audit above was committed and pushed as
`b0cdadb99a1e8b56bf08b9a77e5d5e5a27a6bd1e`; its preservation counts describe
that exact snapshot. While Hénon scouting resumed, the remote advanced by four
commits to `18765b6e`. Read-only overlap inspection found no changes to this
audit, root guidance, the Hénon instructions/state, or the eight evaluators.
The additions include a separately owned symbolic workflow/skill and symbolic
batch completion receipts. They were integrated by fast-forward, not rewritten.
See the other stream's [own audit](../research_state/INSTRUCTION_AUDIT_2026-09-05.md).

In particular, `symbolic_dynamics/AGENTS.md` is now updated by that separate
workstream; the earlier 36-file preservation result is not a claim that its
current bytes still match the pre-audit baseline. The root router remains
compatible with the new symbolic entrypoint. This integration does not count
the other stream's scientific validation as work performed by the Hénon team.
