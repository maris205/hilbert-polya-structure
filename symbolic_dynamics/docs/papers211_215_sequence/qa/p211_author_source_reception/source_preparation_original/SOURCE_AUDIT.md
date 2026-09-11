# P211 source audit and attribution implementation

2026-09-08 UTC. Author source/positioning work, not independent manuscript
review, owner clearance or an external submission audit. The candidate
gate and its source addendum were independently accepted by root; this
document records how their two Minor carry-forwards enter the first draft.

## Cited primary sources

| Key | Verified record | Exact use and subtraction |
|---|---|---|
| `stein2025order` | Itamar Stein, *The algebra of the monoid of order-preserving functions on an n-set and other reduced E-Fountain semigroups*, Semigroup Forum 111, 798--819 (2025), DOI 10.1007/s00233-025-10595-2; version of record published 20 November 2025 | Section 5.1 supplies the carrier coordinates, ceiling retractions, completed-image support and unique reconstruction for rank differences 0/1. All receive zero novelty credit. |
| `andrensek2026endomorphismsv1` | Luka Andrenšek, *Endomorphisms of Hecke-Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497v1, submitted 16 April 2026 | Version 1 Section 4, Proposition 4.1, Theorem 4.4 and Lemma 4.6 supply the Catalan floor-retraction/static-idempotence neighbor. |
| `andrensek2026homomorphismsv3` | Luka Andrenšek, *Homomorphisms of Hecke-Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497v3, 4 August 2026 | Version 3 Theorem 3.6 gives the general directed-path predicate for fixed idempotent products. Its graph-generator content sets are not our kernel/image endpoint sets. |

Primary links: [Stein version of record](https://link.springer.com/article/10.1007/s00233-025-10595-2),
[Stein v2 support paragraph](https://arxiv.org/html/2404.08075v2#S5.SS1),
[Andrenšek v1 Section 4](https://arxiv.org/html/2604.15497v1#S4),
[Andrenšek v3 Section 3](https://arxiv.org/html/2604.15497v3#S3).

The two Andrenšek entries are intentional version-specific citations to
different stated results, not accidental bibliography duplication.
No journal publication is invented for that preprint. Its v1 theorem
numbers are not labelled as v3 theorem numbers.

## Author's actual primary read extent for this draft

- Fresh direct Springer Section 5.1 definition/coordinate/support body,
  browser lines 403--428, and the complete paragraph after Lemma 5.12,
  lines 554--556. The matching explicit v2 paragraph, lines 556--557,
  was read directly as a cross-check. The publisher's citation metadata,
  version-of-record date, volume and pages were read directly.
- The immutable source-addendum browser records were JSON-decoded before
  reading, not treated as legible from one-line grep hits. In v1 the full
  mathematical prose/formulas of Section 4, lines 615--906, were read
  through the overlapping body02/body03/body04 records: carrier,
  composition, floor formula, product condition and interval criterion,
  with their proofs and the endpoint of the endomorphism statement.
  The damaged opening drawing was not reconstructed or visually credited.
- In v3, the decoded records cover graph content/idempotent background,
  Definition 3.1 and Lemma 3.3, both complete Proposition 3.4/3.5 proofs,
  Theorem 3.6 and its sandwich-identity neighborhood. The v1 and v3 blocks
  were distinguished by their source headers and theorem text; shared
  browser line numbers across different versions are not source identity.
  No claim here requires a full new reread of v3 Sections 4--5.
- Version-specific arXiv abstract metadata for both titles, the single
  author and submission/version dates was freshly checked directly.

The saved fresh returns are `sources/stein_definition_web.json`,
`sources/stein_support_web.json` and
`sources/bibliographic_metadata_web.json`. They serialize actual browser
returns, not raw HTTP bodies or native execution receipts. The older raw
v1/v3 HTML and exact browser originals remain in the separately sealed
[source addendum](../../docs/papers211_215_sequence/scouting/kip_candidate_gate_source_addendum/HANDOFF.md).
Nothing in that packet or any older proof/source packet was rewritten.

Several broad navigation displays were truncated and not credited as
complete reads; subsequent narrow decoded-body reads supply the extents
above. A guessed `finite_semigroup_source_desk` path did not exist; the
actual read-only source desk is `kip_source_desk`. No result is attributed
to the failed locator or truncated display. An early JSON lookup used the
wrong field name and returned no lines; it was corrected to `tool_result`
before relying on those source contents.

## m01: completed supports are explicitly owned

The first section states that $(X,A)$, the completion of the image by $n$,
the two allowed rank differences, and recovery of the original image
are already in Stein Section 5.1. The inverse proof credits that fact
again immediately before using its two branches. The manuscript does
not label those branches as a new lemma or contribution.

The target-specific forced/free/forbidden partition and its ordered-gap
factorization are the retained inverse result. Merely knowing which
support pairs are valid is not that target-specific atlas.

## m02: static neighbor and version boundaries

The first section uses separate citations for v1 Catalan results and v3
Theorem 3.6. In the v1 convention graph-generator subsets determine floor
retractions via a different fixed-set encoding; they are not literally
the endpoint supports of this note. Order duality supplies ceiling
retractions, but changing floor to ceiling earns no contribution credit.
The source criteria compose a fixed pair. Here the update recomputes
both supports after each whole-function step. This distinction describes
the studied problem; it is not a theorem of global originality.

## Bibliography method and limits

The project keeps automatic bibliographic API clients off. Entries were
manually formatted from the inspected publisher/arXiv records and checked
against the exact archived version-specific primary bodies, not generated
from memory. The paper-plan/paper-write citation-discipline fallback was
used for this explicit metadata route. There are no unresolved metadata
placeholders and no uncited filler entries. The first manuscript must
still undergo its own actual bibliography and source review.

No broad new literature search or global absence/priority claim is made.
The admitted subtraction of old P167/P190/P209/TM rules remains bounded
to the separately sealed gate's actual reads, not a new all-history audit.
No new author reading of all their manuscripts is claimed for this task.
Source discovery limits, the candidate's thinness risk, and any later
actual owner or mechanism transfer can reopen the scientific assessment.
This is not an ORCID/COI/retraction or specialist-contact audit.

m01/m02 are implemented in draft text, **pending root/reviewer inspection**;
the author does not self-close the findings. External status remains
OWNER_AMBER / HOLD_EXTERNAL.
