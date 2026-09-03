# Round 10 P30/P31 expanded Stage 4-prime correction authorization request

**Status: AWAITING NEW EXPLICIT AUTHOR CONFIRMATION. No correction was applied.**

The previously authorized 34-pair track stopped fail-closed before application.
A read-only coherence scan found 13 additional current-status blocks that would
contradict the frozen source-finalization result after the original citation
blocks were updated. The controlling stop condition was therefore met: an
operation outside the original target set became necessary.

## Exact authority and freeze bindings

- Original 34-pair request: 0c44b40fb5cdea77ccc277dd85b2b713d14f7e5d2d18de4636e7b09e046b3a9c
- Corrected execution-authorization receipt: 7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf
- Execution input freeze: 87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff
- Fail-closed incident: 7833c8e8796ba1fa691dfaad95460406fd8026e8d12a6d6d9665011d41685b6e
- This expanded machine request: 9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135

The old author confirmation does not cover the 13 added pairs. A new explicit
confirmation must bind this expanded request before any patch emission,
application, in-place matrix regeneration, or build.

## Expanded operation envelope

| Paper | Original pairs | Added status/coherence pairs | Expanded pairs | Matrix regenerations |
|---|---:|---:|---:|---:|
| P30 | 29 | 5 | 34 | 1 |
| P31 | 5 | 8 | 13 | 1 |
| **Total** | **34** | **13** | **47** | **2** |

All 47 manuscript operations are replace_block, each gated by the full
normalized-block SHA-256 in the machine request. Source finalization remains
48/48 rows: 25 locator-available and 23 explicit bounded-unavailability rows.

## Newly required exact-hash targets

| Paper | Block | Full expected old SHA-256 | Parser hash | Surface |
|---|---|---|---|---|
| P30 | B0004 | 945f2526d24f9a590e9a502564eff59eec68e36df98bc3e1b8af72ca895d9515 | 945f2526d24f | abstract_source_status |
| P30 | B0006 | 5a52b62c7e2302c15887dc5f486ec635c3211532932b25c54182681e66febedf | 5a52b62c7e23 | traditional_chinese_abstract_source_status |
| P30 | B0062 | 24d81b87425bbd1ac99a400ec5cf7081b7b96c0067dcf3958f51655041b88d69 | 24d81b87425b | claim_passage_matrix_summary |
| P30 | B0065 | 8ccfbe23391a83380567eb8649ea6d50082c5ef4ec24af4d813e675066865203 | 8ccfbe23391a | method_source_status_summary |
| P30 | B0106 | f5375befe2e64e5424b3ac95dfe5505ca0492ae1ac60133dba1ef4c0d452635e | f5375befe2e6 | limitations_matrix_summary |
| P31 | B0006 | 91b5a797215ff03d915ef6f84b826b7bd2f9e71c004ba971e8cbe52b54b8d871 | 91b5a797215f | english_abstract_source_status |
| P31 | B0007 | 026456b0e10c2e8219cf07d999eacdd7c45372f546559a67cca9e08468e1e042 | 026456b0e10c | traditional_chinese_abstract_source_status |
| P31 | B0023 | 9bc068693d8b572b21f12eec72afd1c8d5d18618f2cada47a96b7bfeafece4fc | 9bc068693d8b | current_literature_boundary_status |
| P31 | B0037 | 5a463d97ca65bd7b04e42e6e224e4e56ae63915adbf2f64dd4205e4286369d00 | 5a463d97ca65 | method_component_matrix_summary |
| P31 | B0039 | e300ea71485ec5e071517a8e2f1298a45ec4f9c8796987c4511c9088abe63707 | e300ea71485e | citation_closure_summary |
| P31 | B0089 | 53a9936a2de22c60db44e8250b2d760aa69e0e2f47f95bad8911f2b8daa2f278 | 53a9936a2de2 | limitations_matrix_summary |
| P31 | B0099 | 8379b1b4041bf67893f2efd966197b936066692a256d660eef70237d8dbcb4a5 | 8379b1b4041b | conclusion_source_status |
| P31 | B0108 | 184a6e18123e4a3a0a6d0c389ecb551239341148c087aa9091ed4c1a992e5024 | 184a6e18123e | accountability_limitation_source_status |

The complete machine request reproduces the original 34 pairs at the
target/hash/constraint level and appends only these 13 pairs.

## Exact matrix exceptions

- P30: regenerate the existing
  papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_claim_passage_matrix_round2.json
  in place, gated by 583ce6edb27860ca77967af7c2cb1afb64214fa8f84c30cf7ede9f6578343dc0.
- P31: regenerate the existing
  papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_method_passage_matrix_round2.json
  in place, gated by e18e78cd31f85858184d01ef1e2a36ae80f80830c80b6b3a2977d0f00206f06b.

These are the only allowed Round-2 mutations. Every other Round-2 artifact
remains frozen. Later execution, if newly authorized, must write new versioned
Round-3 drafts and isolated PDFs; it may not mutate either bibliography,
canonical/science/result/initial-system/Route material, or root README.

## Current stopped state

No manuscript patch exists, no replacement was applied, neither matrix was
regenerated, no Round-3 draft/PDF exists, no build was started, and no Stage 4.5
rerun was started. Stage 4.5 therefore remains FAIL. The machine validation at
BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json records 47/47 block-hash replay and frozen-boundary checks.
