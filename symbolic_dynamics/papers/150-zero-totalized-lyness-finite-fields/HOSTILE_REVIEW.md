# Consolidated hostile-review closure — P150

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**  
**Source records:** `HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md`

## Final internal verdict

**ACCEPT**, with **0 unresolved Critical / 0 unresolved Major / 0 unresolved
Minor** after the documented Markdown provenance repair.

This file consolidates rather than replaces the two independent hostile
reviews.  Review A found two Minor hardening needs and no theorem or direct-
owner failure.  After both repairs, Review B independently accepted every
mathematical, owner-boundary, computational, source, build, and visual
interface, but returned one Minor because the then-current `FINAL_QA.md`
still described the round-zero artifact as current.  The present closure
repairs that documentation defect without changing the manuscript,
bibliography, verifier, transcript, PDF, or frozen hash manifest.

## Round A — proof and owner hardening

Hostile Review A returned **ACCEPT WITH MINOR REPAIRS — 0 Critical / 0 Major /
2 Minor**.

| Finding | Required closure | Final disposition |
|---|---|---|
| The owner-search record was too aggregate to replay and did not yet subtract Lyness (1942) and Kanki (2013) explicitly | expose exact query lanes plus candidate/exclusion decisions; cite both primary sources and assign their owned material zero credit | **CLOSED** |
| The five-cycle quotient needed a literal orbit-partition justification, and the smallest/ramified boundaries needed explicit treatment | state that nonfixed generic states partition into five-element orbits; record the `q=3` degeneration and characteristic-five double-root case | **CLOSED** |

The repaired source ledger now records seven replayable query families,
access lanes, candidates, and exclusion reasons.  The paper explicitly
credits Lyness's 1942 rational five-cycle and Kanki's distinct
extended-space/almost-good-reduction treatment of finite-field singularities.
Neither is represented as the manuscript's `inv0(0)=0` totalisation.

The repaired proof now partitions the nonfixed generic locus into disjoint
five-element `L`-orbits.  This simultaneously proves divisibility of

```text
(q-2)(q-3)-r_q
```

by five and the displayed five-cycle count.  It also states that at `q=3`
the generic, four-cycle, and five-cycle families are empty while the
depth-three layer is nonempty, and that in characteristic five the fixed
quadratic has one distinct double root.  No theorem statement changed.

## Round B — independent closure review

Hostile Review B returned **0 Critical / 0 Major / 1 Minor, REVISE**.  It
confirmed that both Review-A repairs were genuinely closed and independently:

- rederived the five-stratum disjoint partition and all generic iterates;
- rederived the exact tails, complete `1/2/4/5` cycle census, integrality,
  zeta product, every-target `0/1/q` fibre law, image size, and complete
  distinguished in-tree;
- checked `q=3`, `q=5`, and arbitrary characteristic-five fields;
- inspected the official Lyness and Kanki primary records and replayed the
  seven-query owner ledger;
- cold-replayed the exact verifier to a byte-identical frozen transcript;
- performed two isolated source-only builds, each byte-identical to current
  `main.pdf`; and
- visually accepted all 5/5 pages.

The sole Review-B Minor was documentary: `FINAL_QA.md` still called the
396,310-byte round-zero PDF current, counted three rather than five
references, and said that no hostile reviews existed.

## Post-B documentation repair

The current `FINAL_QA.md` now distinguishes historical round-zero provenance
from the accepted current artifact.  It records the correct five-entry
bibliography, both hostile reviews, the two isolated builds, and the 5/5-page
visual audit.  The six public package ledgers and this consolidated closure
now carry one status:

```text
ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL
```

This fixes the sole Review-B Minor.  It is a Markdown-only consistency repair;
no evidence-bearing artifact has been regenerated or silently substituted.

## Final source and contribution boundary

The following receive **zero contribution credit**:

- Lyness's 1942 cycle observation and the classical rational five-period
  identity;
- QRT, type-`A_2` cluster, associahedral, and integrability interpretations;
- projective denominator handling and generic finite-field birational-map
  methods;
- Kanki's extended-space, blow-up, `p`-adic reduction, and almost-good-
  reduction treatment of finite-field singularities;
- elementary finite-field inversion and quadratic-root bookkeeping; and
- generic functional-graph cycle, fixed-iterate, and zeta identities.

The residual internal claim is only the conjunction for the literal affine
map with `inv0(0)=0` over every odd finite field:

```text
five-stratum all-plane scheduler
+ exact tail and cycle census
+ all-target fibre/image atlas
+ complete maximal-fibre in-tree.
```

The primary-source search found no direct owner for that full conjunction in
the inspected lanes.  This is a bounded non-hit, not a novelty, priority,
ownership-completeness, or freedom-to-release certificate.  A direct owner
would reopen the gate.

## Accepted artifact evidence

| Item | Accepted current value |
|---|---|
| `main.pdf` | 5 A4 pages; 403,358 bytes |
| PDF SHA-256 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |
| Exact verifier | 2,144,131 assertions; `STATUS=PASS` |
| Frozen replay | byte-identical to `verification_output.txt` |
| Bibliography | 5/5 references cited and resolved |
| Isolated builds | two source-only builds, both byte-identical to `main.pdf` |
| Visual audit | 5/5 pages accepted |

`main_round1.pdf` is byte-identical to the accepted current `main.pdf`.  During
this Markdown closure, root separately froze `main_round2.pdf`; a read-only
comparison confirms that it is also 403,358 bytes and byte-identical to
current `main.pdf` at the digest above.  This closure did not create or modify
the PDF.

## Disposition

P150 passes the round-2 internal proof, owner-boundary, exact-control,
reproducibility, and visual gates under the narrow residual above.  Internal
acceptance authorizes no public release, posting, submission, specialist
contact, novelty/priority claim, Git action, or other external use.  External
status remains **HOLD_EXTERNAL**.
