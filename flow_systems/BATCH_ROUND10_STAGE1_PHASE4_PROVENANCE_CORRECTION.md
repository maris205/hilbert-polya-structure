# Round 10 Stage 1 Phase 4 — manifest UTC provenance correction

Correction date: **2026-09-02 UTC**  
Scope: **clerical provenance fields only**

## Defect

Independent Phase-4 integrity review found that all five fresh claim-intent
manifests serialized a local `+08:00` wall-clock hour as though it were UTC.
For example, `17:00:00Z` was later than the host's actual UTC time and later
than the original file creation event. The manifests did exist before their
reports, but the embedded `Z` timestamps were false and could not be retained
in a signed checkpoint.

The correction changes only each manifest's `manifest_id` and `emitted_at`,
plus the corresponding report-ledger identifier and deterministic audit
constant. Claim text, evidence kinds, planned references, negative constraints,
source inventories, scientific content, and Route boundaries are unchanged.

## Original observed host events and corrected fields

Host `stat` displayed local time with offset `+0800`; the UTC values below are
the same observed instants converted by subtracting eight hours.

| Paper | Pre-correction manifest SHA-256 | Original observed file event | Incorrect serialized ID | Corrected ID and `emitted_at` |
|---|---|---|---|---|
| P29 | `6d313e3f9823e63743228b5737e3719c1e3d79bc2062680d0cb93a50deb55a2b` | `2026-09-02 17:25:28.108809551 +0800` = `2026-09-02T09:25:28.108809551Z` | `M-2026-09-02T17:00:00Z-29d4` | `M-2026-09-02T09:25:28Z-29d4`; `2026-09-02T09:25:28Z` |
| P30 | `6ad236e0d21b7c54ff34c60d7b790b003ea5c296f96d3774bcd9402744a208e1` | `2026-09-02 17:25:28.108809551 +0800` = `2026-09-02T09:25:28.108809551Z` | `M-2026-09-02T17:00:01Z-30d4` | `M-2026-09-02T09:25:28Z-30d4`; `2026-09-02T09:25:28Z` |
| P31 | `b9f900033a423939dbe7c2355cde2e08972cd696138b72533b2d646e179f68b0` | `2026-09-02 17:26:20.012205615 +0800` = `2026-09-02T09:26:20.012205615Z` | `M-2026-09-02T17:00:02Z-31d4` | `M-2026-09-02T09:26:20Z-31d4`; `2026-09-02T09:26:20Z` |
| P32 | `836355db1ef7a05d54b0bf66c758f3d0124684c255acff68e1f7aa18906847e6` | `2026-09-02 17:26:20.012205615 +0800` = `2026-09-02T09:26:20.012205615Z` | `M-2026-09-02T17:00:03Z-32d4` | `M-2026-09-02T09:26:20Z-32d4`; `2026-09-02T09:26:20Z` |
| P33 | `eb1ec3cc2d9c9e004fe047660e94c5ce14d5099a801a93384017d859acb1dc24` | `2026-09-02 17:24:48.297306798 +0800` = `2026-09-02T09:24:48.297306798Z` | `M-2026-09-02T17:00:04Z-33d4` | `M-2026-09-02T09:24:48Z-33d4`; `2026-09-02T09:24:48Z` |

Second-level truncation is explicit and remains earlier than the observed
nanosecond event. The suffixes remain paper-specific and the five corrected
manifest IDs remain unique.

## Integrity disposition

The false UTC fields are superseded and must not be cited as valid provenance.
All final report/checkpoint hashes are issued only after the corrected manifest
IDs are embedded in report ledgers. This correction authorizes no new source,
claim, experiment, computation, Route evaluation, manuscript edit, or Phase-5
review.

CORRECTION_SCOPE=MANIFEST_ID_AND_EMITTED_AT_ONLY
SCIENTIFIC_CONTENT_CHANGED=false
PLANNED_REFS_CHANGED=false
NEGATIVE_CONSTRAINTS_CHANGED=false
SCIENTIFIC_COMPUTATION=NOT_RUN
ROUTE_EVALUATION=NOT_RUN
PHASE_5_REVIEW=NOT_AUTHORIZED
