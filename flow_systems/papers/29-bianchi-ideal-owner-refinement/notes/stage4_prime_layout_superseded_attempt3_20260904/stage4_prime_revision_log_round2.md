# P29 Stage 4-prime Round 2 revision log

Writer status: **LAYOUT_REEMITTED_ATTEMPT3_NOT_APPLIED**  
Patch format: **1.1**  
Patch SHA-256: `d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135`

Layout-remediation lineage: the appended incident `notes/stage4_prime_layout_preflight_incident_round2.md` (SHA-256 `c4c24dede98316f569d30fa231e2cf5cd3e89c82d4f971abac00e7ba11a292e1`) records that the second candidate reduced seven overfull boxes to five but remained fail-closed. That complete second patch is preserved at `notes/stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_patch_round2.json` (SHA-256 `26df9d32270950dcfe0ac323430ab714e5666507aee4fe084486f315584f0402`). The current complete patch preserves all eight operations and every second-attempt string, then adds exactly one scoped `\begingroup\sloppy … \par\endgroup` control to the paragraph in each of B0107, B0112, and B0113. Removing those three layout controls recovers the archived second-attempt patch exactly; operation order, targets, old hashes, authority bindings, discretionary breakpoints, citation content, scientific prose, and values are unchanged. No apply or build was performed by the writer.

| # | Source | Severity | Obligation class | Author triage | Exact target/op | Emitted action |
|---:|---|---|---|---|---|---|
| 1 | R1 residual (R3) | major | must_fix | will_address | B0048/replace_block | Preserved historical aggregate counts; disclosed the dated 53-query replay, exact bounded counts, and unavailable historical rows. |
| 2 | R1 residual (R3) | major | must_fix | will_address | B0080/replace_block | Added paths, schemas, and SHA-256 bindings for the raw replay, JSON/TSV current-row ledger, and JSON/TSV 22-source crosswalk. |
| 3 | R1 residual (R3) | major | must_fix | will_address | B0089/replace_block | Distinguished new bounded replay observations from unavailable original-session rows and prohibited exhaustive/novelty inferences. |
| 4 | R1 residual (R3) | major | must_fix | will_address | B0107/replace_block | Updated the notes-side availability surface with exact ledger/crosswalk bindings and frozen scientific/canonical boundaries. |
| 5 | Round-3 regression NEW-1 via REV-NEW-1 | minor | should_fix | will_address | B0049/replace_block | Replaced “independently assessed” with same-model-family procedural role separation and retained correlated-error risk. |
| 6 | R3 residual (S3) | minor | should_fix | will_address | B0112/replace_block | Completed the prospective ObjectLedger → Gate Q → Gate M → PerformanceLedger → replay dependency/stop map. |
| 7 | R3 residual (S4) | minor | should_fix | will_address | B0113/replace_block | Assigned CONTROL_LABEL_DEPENDENCE_STOP, CONTROL_REPRESENTATIVE_INVARIANCE_STOP, and CONTROL_CODOMAIN_COMPARABILITY_STOP. |
| 8 | DA residual (S6) | minor | should_fix | will_address | B0084/replace_block | Limited value to prospective organization and defined SF-LITERAL-01 without execution or observed output. |

Every operation carries empty `claim_strength_changes[]` and `collateral_authorization_ids[]`. No registered ClaimIntent replacement is authorized or emitted. Mechanical post-apply fields remain unknown by writer-role design.

## Supporting evidence boundary

The 2026-09-04 replay inspected only the first three connector-visible rows for each exact frozen query and did not paginate. It contains 53 query lines, 48 with at least one visible row, five unavailable, and 139 inspected manifestations. Current-work deduplication retained 89 unique keys and marked 50 manifestations duplicate. Nineteen unique representatives matched the existing admitted set; 70 other unique representatives were excluded from this fixed-corpus replay. The P29-S01--P29-S22 crosswalk is independently complete at 22/22 because it joins the frozen inventory and matrix, not because every admitted source resurfaced in the replay window.

The original-session screened-out identifiers and decisions remain unavailable. The replay does not reconstruct history, refresh scientific results, or authorize corpus expansion.
