# P22 Stage 4 Round 1 token-conservation audit

Date: **2026-08-25**

Status: **ADVISORIES EXPLAINED — INDEPENDENT SEMANTIC REVIEW REQUIRED**

The current ARS `check_revision_token_conservation.py patch` checker was run
against the exact anchored Stage-3 base and the official 13-operation patch,
with the explicit protected-term roster `additive lift`, `global priority`,
`finite-flat`, `fppf`, `V_N`, and `corresponding author`.
The patch SHA-256 is
`e9c1debbb21a0b209847004de16fd76c9e1489844c4209417dd7fdb6b2ca5a6a`.

The aggregate field is `conserved: false` because authorized replacement
operations deliberately add numeric and protected-term tokens.  The checker
reported no removed protected term and no removed or added citation token.
`global priority` remains unchanged and `corresponding author` remains absent.
Its citation-token extractor does not replace a manual check of LaTeX citation
keys or semantic attachment.

| Advisory | Block / item | Added numeric tokens | Roadmap-bounded explanation |
|---|---|---|---|
| `ADV-REV-1` | `B0022` / `REV-001` | `010`, `03`, `06`, `1`, `2025`, `21`, `23`, `25`, `4.3`, `4.5`, `4.7`, `7` | Proposition, page, Stacks-tag, version, and dated-search locators required by the reproducible bounded literature comparison. |
| `ADV-REV-2` | `B0023` / `REV-006` | `0`, `1` | The source section `z_0` and displayed short exact sequence used to state the reusable conditional template precisely. |
| `ADV-REV-3` | `B0092` / `REV-006` | `1` | Restores the theorem's exact nontrivial-index bound `N>1` in the conclusion. |
| `ADV-REV-4` | `B0005` / `REV-003` | `1`, `1037`, `430070` | Confirmed affiliation label, street number, and postal code supplied by the author. |

The protected-term additions occur only in `REV-001`, `REV-004`, `REV-005`,
and `REV-006`: they add the topology names and the exact terms `V_N` and
`additive lift` in the blocks where the roadmap requires the topology-indexed
statement, bounded comparison, finite-flat definition, or reusable template.
No protected term is removed.  In the explicit-roster run this yields nine
advisory operations in total; the table isolates the four that also carry
numeric deltas.

These explanations do not certify semantic fidelity.  The apply report honestly sets
`unregistered_claim_drift_review_required: true`; the separate Stage-4 manual
semantic-drift audit must decide that boundary before the marker-free paper is
promoted.
