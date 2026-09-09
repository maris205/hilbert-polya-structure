# R5 independent integration audit

2026-09-09 UTC runtime snapshot; completed after E1's final native-12
repair readback. This is a bounded file/member/link/scope audit, not a new
mathematical review, execution certificate, staged-index audit or remote receipt.

## Result and exact membership

**PASS for the inspected integration scope; no pending integration repair.**
The earlier E1-pending snapshot is superseded by the actual final 370-line
review, its closed wording repair and the coordinator's updated decision.
There are **11 nonauthor review files, 3,647 lines in total**, not 12 reviews.

Before this report, R5 contained exactly 29 files, all Markdown. With this
report, the exact R5 set is the following **30 files**, relative to this
directory. The count includes this audit once; its own digest is not
self-embedded. No implicit directory wildcard is a staging authorization.

```text
INTEGRATION_AUDIT.md
ROUND5_DECISION.md
a2_excluded_congruence/CHARACTERISTIC_TWO.md
a2_excluded_congruence/PROOF_PACKAGE.md
a2_excluded_congruence/REPORT.md
a3_eventual_quotient_tower/PROOF_PACKAGE.md
a3_eventual_quotient_tower/REPORT.md
b3_composition_good_models/PROOF_PACKAGE.md
b3_composition_good_models/REPORT.md
c1_native12_tame_witness/PROOF_PACKAGE.md
c1_native12_tame_witness/REPORT.md
c2_composition_exact_spectrum/PROOF_SUPPLEMENT.md
c2_composition_exact_spectrum/REPORT.md
c4_reversor_local_global/PROOF_PACKAGE.md
c4_reversor_local_global/REPORT.md
e2_local_nine_discriminator/REPORT.md
reviews/b1_composition_admission/REVIEW.md
reviews/b1_reversor_admission/REVIEW.md
reviews/e1_composition_good_models/REVIEW.md
reviews/e1_native12_mechanisms/REVIEW.md
reviews/e4_composition_period16/REVIEW.md
reviews/e4_local_nine/REVIEW.md
reviews/e5_reversor_local_global/REVIEW.md
reviews/e6_eventual_quotient_tower/REVIEW.md
reviews/e6_mod3_nine/REVIEW.md
reviews/e8_excluded_congruence/CHARACTERISTIC_TWO_REVIEW.md
reviews/e8_excluded_congruence/REVIEW.md
x1_eventual_tower_sources/REPORT.md
x2_arithmetic_replacement/REPORT.md
x2_second_replacement/REPORT.md
```

The only three coordinator records in the proposed preservation set are:

- `henon_dynamics/CURRENT_RESEARCH_STATE.md`
- `henon_dynamics/research_c429_c433/CONTINUOUS_RUN.md`
- `henon_dynamics/research_c429_c433/ADMISSION_DECISIONS.md`

Thus the expected exact save set is **33 files**. Every R6 file, every
previous-round file and all eight inherited unrelated directories are
excluded. Only R5 was enumerated; the inherited directories were not scanned
or touched. Exclusion here describes the exact proposed membership, not
a claim that a Git index or remote already has that membership.

## Byte bindings and local links

The final [decision](ROUND5_DECISION.md) and
[admission record](../ADMISSION_DECISIONS.md) contain **31 distinct literal
SHA-256 pins**. Every pin was recomputed from actual local bytes and matched:
27 complete files (including six explicitly linked frozen R3/R4 inputs),
two historical LF-terminated prefixes, and two extracted source blocks.
No unmatched or ambiguous target remained. Embedded source was hashed only,
never executed. Supplementary checks also matched the first diagnostic's
source and the older 341-line C2 report prefix.

The historical bindings are not current-full-report certificates:

- E4's original review hash `0e866dbba4d2431fcb621c406195570aa4b8139d3614c91f44822b75d43e6572` matches precisely its first 179 lines, not its current 220-line whole file.
- C2's `0b61d292915d2ab54c6047fea37a4908df9ffbdf07598a8766d5c6c530764e36` matches precisely the first 367 report lines; its earlier 341-line pin also matches. Neither covers Sections 11–12.
- The current C2 report is 796 lines and has its separate final whole-file pin. E6's separate review covers Section 12 at its stated scope; a whole-file byte pin does not enlarge that review's mathematical remit.

E1's final native-12 review, C1's final proof and unchanged report/source
all match their decision pins. In a read-only stream, replacing exactly
the one new provenance sentence by its old text restores the original
proof digest `8dbe4db1d868b31a1a5ee9328d0df49fd1d1c0a8c2b23ac2b35eedf3fd881901`.
The current proof contains that new sentence once. This supports the
recorded one-sentence delta, not a fresh mathematical verdict.

All 29 pre-audit R5 Markdown files were checked for local Markdown links:
**85 local link occurrences**, including the one explicit heading fragment,
have existing targets and matching checked anchors. The relevant coordinator
passages added 42 local occurrences and one heading fragment, likewise
without a missing target or failed anchor. Three initial regex hits were
manually resolved as coefficient-extraction formulas, not links. No
reference-style link definitions were present in R5. This report's four
local links are included in the final readback. The 80 external link
occurrences in the pre-audit R5 set were not re-fetched; website availability
and every renderer-specific anchor convention are outside this local audit.

## Scope consistency and execution accounting

The [current-state entry](../../CURRENT_RESEARCH_STATE.md),
[continuous-run additions](../CONTINUOUS_RUN.md), admission record and final
decision agree on **4/5 contracts and 0/5 completed papers**: PC424-L, UL4,
OM4 and RLG5. Their older 3/5 and earlier run counts are historical entries,
not competing final claims. Eleven review files include directed addenda;
the two B1 substantiality reviews are not counted as extra mathematics
contracts. The CGR5 good-model result remains a GR5 extension, and the
higher-quotient and characteristic-two bridges remain within UL4/PC424-L.

RLG5's Wang obstruction, amalgam/axis machinery and classical root-twist
plus full-centralizer descent are expressly subtracted. Admission is for
the constrained inverse-pair realization with exhaustive original-field
reversor exclusion, not a new classical mechanism or worldwide-priority
certificate. The general integer spectrum remains unclosed at 9,12,18,24;
the true dyadic-nine point is not promoted to an integer witness.

The actual retained receipts identify **exactly three producer mathematical
executions**: C2's 90,000-word probe, C2's 14,400-pair staircase diagnostic,
and C1's 10,201-parameter dual-quadratic diagnostic. Each reports completion
and exit 0; their source pins, commands and complete raw receipts were
checked for accounting consistency, not rerun. The C2 subtotal of two and
C1 subtotal of one agree with the round total of three. Hash checks are
not extra mathematical executions. C1's hand lemmas preserve the imported
C428 historical-certificate dependency after the explicit wording repair.
No finite no-hit result is made into an unrestricted exclusion.

R6 is separately allocated, receives no execution authority here, is not
part of this R5 save set and need not finish before R5 preservation.
NO_BAD_EULER_OR_ROOT_NUMBER, Route-B exclusion and the absence of new
manuscripts/PDFs/formal evaluation or target-arithmetic promotion are retained.

## Handoff limits

Only this audit file was written. No author, review, shared coordinator,
old or inherited file was changed; no mathematical program, old certificate,
Git command, staging, commit, fetch, push, external source search or upload
was performed by this audit. The coordinator still owns exact staging and
actual Git-object/remote verification. A later changed input needs only
the affected byte/link/scope check; this PASS is not a proof-truth guarantee
and does not say that R5 has been synchronized.

