# Material Passport — P102–P106 internal freeze

This is a project-local, Schema-9-aligned provenance record for the five
internal paper packages.  It is not a validated ARS runtime passport and it
does not substitute for the paper-local final QA or SHA-256 manifests.

## Passport identity

| field | value |
|---|---|
| `origin_skill` | `ars-codex:academic-research-suite` (batch evidence integration only) |
| `origin_mode` | `stage2-final-internal-freeze` |
| `origin_date` | `2026-08-29T03:45:05Z` |
| `verification_status` | `VERIFIED_INTERNAL` |
| `version_label` | `batch_p102_106_stage2_v2` |
| `integrity_pass_date` | `2026-08-29 UTC` |
| `content_hash` | SHA-256 of `CANONICAL_PDF_MANIFEST.sha256`: `24748abdd50aa0ab5b622dd40fde7be3cbaccb97b3a624c0172bb9664089aa51` |
| `repro_lock` | `null` -- commands and tool boundaries are retained in the paper BUILD/control records, but no environment lockfile is claimed |
| `upstream_dependencies` | problem anchor, Stage-1 selection, theorem contracts, proof-spike ledger, current five paper packages, source-verification report, collision firewall |

`VERIFIED_INTERNAL` means the theorem-bearing sources, exact controls, two
nonauthor hostile reviews, final mechanical QA, and package hashes pass on the
current local tree.  It does not mean external peer review, novelty, priority,
or release clearance.

## Material inventory

| paper | package | system and residual theorem package | pages | canonical exact assertions | present hostile ledgers | final seal |
|---:|---|---|---:|---:|---|---|
| P102 | [`papers/102-...`](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/README.md) | split cyclic group algebra under `a -> a a*`; synchronized Fourier blocks, fixed/cycle census, sharp depth, recovery | 6 | 116,278 | A and B | pass |
| P103 | [`papers/103-...`](../../papers/103-double-adjugate-matrix-dynamics/README.md) | all finite-field matrices under double adjugation; singular collapse, fixed/image staircases, cycles, zeta | 4 | 141,190 | A and B | pass |
| P104 | [`papers/104-...`](../../papers/104-monomial-toggle-contraction-cocycles/README.md) | iid monomial-toggle products; exact normal form, folded CLT, annealed exponent and gap | 5 | 741,486 | A and B | pass |
| P105 | [`papers/105-...`](../../papers/105-cycle-minimum-pruning-dynamics/README.md) | simultaneous permutation cycle-minimum pruning; exact depth census and reverse-fibre formula | 5 | 17,219,241 | A and B | pass |
| P106 | [`papers/106-...`](../../papers/106-synchronous-mis-polarity-dynamics/README.md) | synchronous MIS Boolean polarity; cubic collapse, one/two-cycle zeta, bipartite square law | 4 | 6,462,317 | A and B | pass |
| **batch** | five internal packages | five distinct phase spaces/actions | **24** | **24,680,512** | **complete** | **pass** |

The author-freeze proof-spike ledger recorded 24,679,662 assertions.  During
P103 cross-hostile strengthening, 850 non-circular scalar-line image-
staircase assertions were added, producing the current canonical total
24,680,512.  This is an audit-strengthening delta, not a new theorem.

## Evidence provenance and boundary

Each package contains four evidence layers:

1. `main.tex` supplies the infinite-family proof and exact quantifiers.
2. `CLAIMS_EVIDENCE.md` maps theorem claims to analytic and deterministic
   evidence.
3. A standard-library exact verifier plus stored stdout supplies finite,
   convention-sensitive falsification lanes.
4. `BUILD.md` and the available hostile-review ledgers record compilation,
   reconstruction, and known residual risks.

The assertion total counts deterministic checks, not statistical samples and
not independent proofs.  Finite controls cannot establish the field-uniform,
large-`n`, or asymptotic statements by extrapolation; those statements rest
on the written arguments.  No GPU or empirical experiment is part of this
batch.

## Owner passport

| paper | established material assigned zero novelty credit | residual owner gate |
|---:|---|---|
| P102 | finite Fourier analysis; group-algebra involutions/symmetric units; scalar power maps; zeta bookkeeping | exact whole-algebra involution-norm temporal package not located in the bounded search; canonical map gives medium-high specialist-owner risk |
| P103 | Jacobi/hyperadjugate identity; Cremona adjugation; finite-field and scalar power-map facts | exact full-matrix temporal conjunction not located in the bounded search |
| P104 | random-product limits; generalized-Lyapunov/tilted transfer methods; martingale CLT | exact two-atom cocycle specialization may have a direct owner; medium release risk |
| P105 | labelled cycle enumeration; longest-cycle laws; deletion structures; zeta | exact simultaneous labelled surgery and fibre formula may have a direct owner |
| P106 | same MIS Boolean network/fixed-point literature; formal-concept polarity; classical path recurrence | **high risk/direct-system collision**; only the synchronous temporal/zeta conjunction remains as the bounded residual package |

P106 carries a repaired source identity.  The valid direct conjunctive-network
record is Aracena--Richard--Salinas (2017), DOI
`10.1016/j.jcss.2017.03.016`; the path recurrence is assigned to
Euler--Oleksik--Skupień (2013), DOI `10.7151/dmgt.1707`.  The unrelated DOI
`10.1016/j.jcss.2018.01.003` is excluded.  Full details are in the
[source-verification report](phase2/SOURCE_VERIFICATION_REPORT.md).

## Collision passport

The [pairwise firewall](phase1/SYSTEM_COLLISION_FIREWALL.md) contains all ten
within-batch comparisons.  At this freeze:

- no pair shares the same phase space, update rule, headline invariant, and
  proof engine;
- nearest historical motif neighbors are P86/P97/P99/P87 for P102,
  P99/P97 for P103, P91/P93/P101 for P104, P100 for P105, and
  P68/P75/P80 for P106;
- shared background lemmas and proof motifs receive no separate credit; and
- `NO_INTERNAL_DUPLICATE` is not an external novelty or owner conclusion.

## Review and integrity gates

| gate | frozen result | consequence |
|---|---|---|
| theorem contract represented in each manuscript | present | internal scientific audit may continue |
| canonical exact controls | present; 24,680,512 current assertions | finite falsification evidence available |
| pairwise internal firewall | reconciled with current papers/reviews | no same-system pair within P102--P106 |
| owner subtraction | reconciled; P106 direct-system collision explicit | external release remains HOLD |
| two retained hostile ledgers per paper | complete for all five | internal mathematical/evidence gate passes |
| final mechanical QA | pass | 24 pages, 20 build stages, 117 fonts, text and visual gates pass |
| canonical SHA-256 manifests | pass | every paper manifest and the batch PDF manifest verify |

The frozen packet contains 24 pages, 1,562,518 PDF bytes, and 24,680,512
assertions.  Any later change to theorem text, verifier logic, evidence, or
review documents invalidates the affected paper hash and requires a new
passport version and fresh QA rather than silent mutation.

## Release decision

**EXTERNAL HOLD.**  Public posting, journal/conference submission, author or
editor contact, absolute novelty language, and priority claims are outside
this passport's authority.  The next authorized internal state transition is
the next five-paper Route-A round; the external owner gates remain closed.
