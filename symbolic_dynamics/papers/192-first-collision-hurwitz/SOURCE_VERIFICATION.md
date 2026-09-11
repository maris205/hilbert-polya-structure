# Source Verification

Audit date: 2026-09-04 UTC.

Status: citation metadata audited; external direct-owner clearance incomplete. Gate remains `OWNER_RED_AMBER/HOLD_EXTERNAL`.

## Scope

This audit verifies the six sources actually cited by `main.tex` and records what they are used for. It does not claim a complete literature search for the adaptive first-collision scheduler. Links below point to publisher, journal, institutional-repository, author, or arXiv records.

## Citation ledger

| BibTeX key | Verified record | Use in manuscript | Audit result |
|---|---|---|---|
| `Denes1959` | [Hungarian Academy repository record](https://real.mtak.hu/200901/) | Classical minimal transposition factorizations and Cayley count | Author, title, year 1959, volume 4(1), and pages 63--71 match. Journal abbreviation retained. |
| `GorskyGorsky2013` | [arXiv:1112.0381v2](https://arxiv.org/abs/1112.0381) and [Mikhail Gorsky's publication list](https://sites.google.com/site/homepageofmikhailgorsky/) | Classical braid-group action on parking functions | Title/authors and the 2013 revised arXiv version match. No primary record supporting the previous Moscow Mathematical Journal coordinates was found; entry corrected to an arXiv preprint. |
| `Stanley1997` | [Electronic Journal of Combinatorics article page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v4i2r20) | Classical parking-function context / lower-endpoint correspondence attribution | Volume 4, issue 2, article R20 and DOI `10.37236/1335` verified. The issue is dated 1997, while the article page reports acceptance/publication metadata in November 1996; the conventional volume year 1997 is retained. |
| `IrvingRattan2021` | [Elsevier article record](https://www.sciencedirect.com/science/article/pii/S0195669820301773) and [arXiv:1907.10123](https://arxiv.org/abs/1907.10123) | Factorizations of full cycles, parking functions, and tree correspondences | European Journal of Combinatorics 93 (2021), article 103257, DOI `10.1016/j.ejc.2020.103257` verified. |
| `Stanley2011EC2` | [Cambridge University Press book page](https://www.cambridge.org/core/books/enumerative-combinatorics/360F1EEA6B91AE359EE489AC4145EF49) | Pollak's circular parking model | Volume 2, second edition, 2023, and book DOI `10.1017/9781009262538` verified. The BibTeX key is historical; its embedded `2011` is not metadata. |
| `CampionLothRattan2025` | [Wiley article page](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70170), [arXiv:2403.08354](https://arxiv.org/abs/2403.08354), and [Bristol publication record](https://research-information.bris.ac.uk/en/publications/centrality-of-star-and-monotone-factorisations/) | Nearest located conditional-Hurwitz construction; exact subtraction from the residual scheduler claim | Title, authors, DOI, volume 57(11), pages 3567--3585, and 2025 publication metadata verified. Its Theorem 7 uses ordered strings of conditional Hurwitz moves, with equal lower endpoints in one case. The manuscript now credits that machinery and distinguishes its move convention, monotone/string scheduler, bijection objective, and theorem output from P192's iterated least-adjacent-collision map. |

All six keys are cited in `main.tex`, and the generated bibliography has six entries. No uncited entry remains in `references.bib`.

## Round-0 bibliography delta

Four clear metadata problems were corrected without changing `main.tex`:

1. `Stanley1997`: DOI `10.37236/1321` was replaced by `10.37236/1335`.
2. `IrvingRattan2021`: the incorrect Journal of Combinatorial Theory, Series A 179 / 105379 record was replaced by European Journal of Combinatorics 93 / 103257, DOI `10.1016/j.ejc.2020.103257`.
3. `Stanley2011EC2`: `10.1017/9781009262491` was an ISBN-shaped identifier, not the book DOI; it was replaced by `10.1017/9781009262538`.
4. `GorskyGorsky2013`: unsupported Moscow Mathematical Journal volume/page data were removed, and the source is now accurately described as arXiv:1112.0381v2.

These changes alter only bibliographic metadata. The mathematical text and theorem contract are unchanged.

## Hostile-review source delta

Reviewer A located Campion Loth--Rattan (2025), which the Round-0 bounded
pass had omitted. The paper is close enough that omission was material: its
deterministic bijection is implemented by an ordered string of conditional
Hurwitz moves, and one local case is triggered by equal lower endpoints. It
does not literally establish P192's scheduler package: its Hurwitz convention
and monotone/string order-change scheduler differ, its construction is
reversible, and it does not prove the first-collision tail or target-resolved
fibre theorems stated here. The source is nevertheless now cited and receives
explicit zero contribution credit. This repair does not upgrade the owner
gate; status remains `OWNER_RED_AMBER/HOLD_EXTERNAL`.

## Attribution boundary

The note gives zero contribution credit to:

- Dénes/Cayley enumeration of minimal transposition factorizations;
- ordinary Hurwitz and braid actions;
- established factorization/parking/tree correspondences;
- Pollak's circular parking argument;
- ordinary Prüfer enumeration.
- the conditional Hurwitz-string bijection of Campion Loth--Rattan.

The citations support classical ingredients, not the adaptive scheduler theorem package. No cited paper is represented as proving the first-collision dynamics.

## Owner-search boundary

The frozen manuscript reports a bounded search that did not locate the literal conjunction of the least-collision scheduler, strict history theorem, and complete target-resolved inverse atlas. Round 0 does not include a reproducible, query-by-query external search log broad enough to establish an owner conclusion. This is a material open gate.

Required external search families include:

- greedy, priority, or first-collision Hurwitz dynamics;
- deterministic schedulers on reduced/minimal transposition factorizations;
- parking-function dynamics induced by conditional braid moves;
- target-resolved inverse Hurwitz fibres and indegree extremizers;
- equivalent scheduler formulations under factorization-tree bijections.

Until that search is completed and independently reviewed, the correct statement is only: no literal owner was established in the bounded internal pass. This is not a novelty, priority, or freedom-to-operate claim.
