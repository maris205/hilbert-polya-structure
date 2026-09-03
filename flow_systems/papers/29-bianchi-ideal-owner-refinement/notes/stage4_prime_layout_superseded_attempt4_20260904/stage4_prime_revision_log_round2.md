# P29 Stage 4-prime Round 2 revision log

Writer status: **LAYOUT_REEMITTED_ATTEMPT4_NOT_APPLIED**  
Patch format: **1.1**  
Patch SHA-256: `7827a265b0148151c6c317caa8c00782d3bdaec5152edee6e8ad6f2ac3868f77`

Layout-remediation lineage: the appended incident `notes/stage4_prime_layout_preflight_incident_round2.md` (SHA-256 `182cd335bc7373cc22d50828ec0cee36954c873ff3c812952bc1ce22c286eaa3`) records that the third candidate reduced the layout failures to one B0107 overfull box but remained fail-closed. That complete third patch is preserved at `notes/stage4_prime_layout_superseded_attempt3_20260904/stage4_prime_revision_patch_round2.json` (SHA-256 `d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135`). The current complete patch preserves all eight operations, targets, old hashes, authority bindings, scientific and citation prose, values, discretionary breakpoints, and the scoped `\begingroup\sloppy … \par\endgroup` controls. Its only new difference is inside B0107: the literal schema name is rendered with `\path{p29-source-inventory-to-literature-matrix-crosswalk/1.0}` instead of the attempt-3 `\texttt{}` token carrying manual `\allowbreak{}` insertions. The visible literal is identical, and the inverse substitution recovers attempt 3 byte-for-byte. No apply or build was performed by the writer.

| # | Source | Severity | Obligation class | Author triage | Exact target/op | Emitted action |
|---:|---|---|---|---|---|---|
| 1 | R1 residual (R3) | major | must_fix | will_address | B0048/replace_block | Preserved historical aggregate counts; disclosed the dated 53-query replay, exact bounded counts, and unavailable historical rows. |
| 2 | R1 residual (R3) | major | must_fix | will_address | B0080/replace_block | Added paths, schemas, and SHA-256 bindings for the raw replay, JSON/TSV current-row ledger, and JSON/TSV 22-source crosswalk. |
| 3 | R1 residual (R3) | major | must_fix | will_address | B0089/replace_block | Distinguished new bounded replay observations from unavailable original-session rows and prohibited exhaustive/novelty inferences. |
| 4 | R1 residual (R3) | major | must_fix | will_address | B0107/replace_block | Preserved the exact notes-side ledger/crosswalk bindings and frozen scientific/canonical boundaries; rendered the same crosswalk-schema literal with the line-breakable `\path{}` macro. |
| 5 | Round-3 regression NEW-1 via REV-NEW-1 | minor | should_fix | will_address | B0049/replace_block | Replaced “independently assessed” with same-model-family procedural role separation and retained correlated-error risk. |
| 6 | R3 residual (S3) | minor | should_fix | will_address | B0112/replace_block | Completed the prospective ObjectLedger → Gate Q → Gate M → PerformanceLedger → replay dependency/stop map. |
| 7 | R3 residual (S4) | minor | should_fix | will_address | B0113/replace_block | Assigned CONTROL_LABEL_DEPENDENCE_STOP, CONTROL_REPRESENTATIVE_INVARIANCE_STOP, and CONTROL_CODOMAIN_COMPARABILITY_STOP. |
| 8 | DA residual (S6) | minor | should_fix | will_address | B0084/replace_block | Limited value to prospective organization and defined SF-LITERAL-01 without execution or observed output. |

Every operation carries empty `claim_strength_changes[]` and `collateral_authorization_ids[]`. No registered ClaimIntent replacement is authorized or emitted. Mechanical post-apply fields remain unknown by writer-role design.

## Supporting evidence boundary

The 2026-09-04 replay inspected only the first three connector-visible rows for each exact frozen query and did not paginate. It contains 53 query lines, 48 with at least one visible row, five unavailable, and 139 inspected manifestations. Current-work deduplication retained 89 unique keys and marked 50 manifestations duplicate. Nineteen unique representatives matched the existing admitted set; 70 other unique representatives were excluded from this fixed-corpus replay. The P29-S01--P29-S22 crosswalk is independently complete at 22/22 because it joins the frozen inventory and matrix, not because every admitted source resurfaced in the replay window.

The original-session screened-out identifiers and decisions remain unavailable. The replay does not reconstruct history, refresh scientific results, or authorize corpus expansion.
