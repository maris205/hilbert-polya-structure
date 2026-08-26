# Paper 22 Stage-2 literature search report

Search date: **2026-08-24**  
Mode: **targeted exact-owner search for a focused pure-mathematics note**

## Search strategy

The exact query families, search surfaces, and inclusion/exclusion rules are
recorded in [the Phase-2 source screen](phase2_source_site_screen.md).  The
search covered official arXiv records/full text, publisher pages, Crossref,
and the Stacks Project.  It was designed to find (i) the exact source-defined
lifting question, (ii) a post-source answer, (iii) the nearest monoid-algebra
kernel precedent, and (iv) formal sheaf/extension lemmas.  p-typical, KEnd,
TR, and derived-Witt results were excluded from the load-bearing owner unless
their different scope was stated explicitly.

Last searched: **2026-08-24**.  Initial search hits were not treated as a
systematic-review population and were not assigned a fabricated count.  Four
source families survived for possible use; three are retained in the minimal
manuscript bibliography.

## Coverage distribution advisory

The retained corpus is concentrated in theoretical sources and in the exact
source-author line.  This is substantively appropriate for a short proof note:
the paper proves its mathematical claims internally and uses external sources
only for definitions, the posed question, nearest-prior subtraction, and
standard categorical facts.  No expansion is required merely to diversify
venues or methods.

## Screening results

| Stage | Result |
|---|---|
| Exact-owner retrieval | Deninger, arXiv `2508.05329v1` |
| Direct post-source solution | none found within the documented search |
| Nearest different-owner kernel result | Deninger--Mellit (2019) |
| Formal sheaf/extension references | Stacks Tags `03CN`, `00HS`, `0AUW`, `010I`, `06XP` |
| Optional broad F/V precedent | Dotto--Krause--Nikolaus--Patchkoria (2022); omit from minimal draft unless needed |

The official arXiv record still listed only v1 on 2026-08-24.  This temporal
statement is bounded to that date and record.

## Annotated bibliography

### Christopher Deninger (2025), *Rational Witt vectors and associated sheaves*

- **Type:** primary arXiv preprint, version 1.
- **Exact role:** defines `omega`, proves the fpqc sheaf result (Theorem 3.4),
  proves sheaf epimorphy (Proposition 4.3), supplies the nilpotent detector
  (Example 4.4), gives the domain-refinement injectivity criterion
  (Proposition 4.5), states Corollary 4.6, and asks the Verschiebung lifting
  question on PDF p. 25.
- **Boundary:** Corollary 4.6 is the assertion tested by the new example, not
  a premise.  The official record has no later version as of the search date.
- **Potential use:** every manuscript section, with exact theorem/page
  locators rather than a generic paper-level citation.

### Christopher Deninger and Anton Mellit (2019),
*ZR and rings of Witt vectors W_S(R)*

- **Type:** peer-reviewed research article.
- **Exact role:** Theorem 1.1 gives a kernel description for a nearby
  monoid-algebra-to-truncated-Witt map.
- **Boundary:** different quotient, truncation, and owner; no fppf
  sheafification or descent obstruction.
- **Potential use:** one nearest-prior sentence in the introduction.

### The Stacks Project Authors, *The Stacks Project*

- **Type:** maintained authoritative mathematical reference.
- **Exact role:** Tag `03CN` for local exactness/surjectivity of abelian
  sheaves; Tag `00HS` for flat going-down; Tag `0AUW` for torsion-free modules
  over a Dedekind domain; Tags `010I` and `06XP` for extensions and `Ext^1`.
- **Boundary:** supplies formalism, not the arithmetic obstruction.
- **Potential use:** Sections 2, 3, 5, and 6.

### Dotto--Krause--Nikolaus--Patchkoria (2022),
*Witt vectors with coefficients and characteristic polynomials over
non-commutative rings*

- **Type:** peer-reviewed research article.
- **Exact role:** broad nearby evidence that Frobenius/Verschiebung descent
  questions depend on the precise Witt owner and kernel.
- **Boundary:** not Deninger's reduced monoid sheaf and unnecessary for the
  core proof.
- **Potential use:** optional context only; omitted from the minimal draft to
  keep the owner subtraction sharp.

## Literature matrix

| Source | Exact owner | Sheaf epimorphism | Kernel/detector | Extension formalism | Source correction | Status in draft |
|---|---|---|---|---|---|---|
| Deninger 2025 v1 | main | main | main | contextual | main | include |
| Deninger--Mellit 2019 | different |  | main nearby prior |  |  | include once |
| Stacks Project | formal | main formalism | formal | main | main formalism | include |
| Dotto et al. 2022 | different |  | contextual |  |  | optional | omit unless needed |

## Identified gap and bounded novelty wording

The source explicitly leaves the fp/fppf additive lifting question open.
The documented searches found no direct post-source solution through
2026-08-24.  This is a bounded search statement, not a universal claim of
priority.  The manuscript therefore frames its contribution as an answer to
the identified source question and names Deninger--Mellit as the nearest
different-owner kernel precedent; it does not say "first", "only", or "no
prior work".

