# P191 Review A — source, owner, and collision audit

## Decision

`PASS_DELTA_ACCEPTED / OWNER_AMBER / HOLD_EXTERNAL`.

The manuscript's five citations and their uses are supportable.  Round-0
Review A found that one companion source-verification line had mislabelled an
OEIS database date as an entry modification date.  The requested-only delta
now gives the correct entry-history date, so no source finding remains open.
The direct-owner search is bounded and cannot establish
novelty, priority, ownership, completeness, freedom to operate, or release
permission.

## OEIS A398023 check and finding

The [authoritative OEIS entry](https://oeis.org/A398023) states “Number of
integer compositions of `n` such that every initial segment has an integer
average,” and its comments spell this out as the index `i` dividing the
prefix sum.  This supports the manuscript's static-neighbour description and
is literally distinct from P191's current-part condition `a_i | s_i`.

However, the [official entry history](https://oeis.org/history?seq=A398023)
lists the latest entry revision as #12 at 22 July 2026.  It contains no
27 August 2026 revision.  OEIS page footers report when the entire database
was last modified and change independently of this entry.  Round-0 finding
`P191-A-MI-01` recorded that mismatch.  The accepted source-ledger row now
says “approved/latest entry revision 22 July 2026”; the false 27 August phrase
is absent.  The bibliography's narrower submitted/accessed note was and
remains unaffected.

## Citation metadata and scope

DOI content negotiation and official publisher/journal records support the
remaining metadata:

| record | authoritative identifier | permitted role |
|---|---|---|
| Stanley, *Enumerative Combinatorics*, vol. 1, 2nd ed. | [Cambridge DOI 10.1017/CBO9781139058520](https://doi.org/10.1017/CBO9781139058520) | standard compositions and cut encodings |
| Billera–Thomas–van Willigenburg, *Decomposable Compositions...* | [DOI 10.1016/j.aim.2005.05.014](https://doi.org/10.1016/j.aim.2005.05.014) | partial-sum subset/coarsening language |
| Heubach–Mansour, *Combinatorics of Compositions and Words* | [DOI 10.1201/9781420072686](https://doi.org/10.1201/9781420072686) | static composition background |
| Bender–Canfield, *Locally Restricted Compositions I* | [DOI 10.37236/1954](https://doi.org/10.37236/1954) | locally restricted composition background |
| Navarro, OEIS A398023 | [OEIS](https://oeis.org/A398023) | nearest static prefix-divisibility warning |

The exact cite-key set equals the exact bibliography-key set (five each).
No citation is presented as proving a P191 theorem.

## Bounded direct-owner pressure

Queries included exact and semantic variants of:

```text
"part divides" "partial sum" integer compositions dynamics
"a_i divides" "prefix sum" composition
"delete" cuts composition divisibility dynamics
site:oeis.org/A398023 A398023 composition initial segment average
```

The exact OEIS static neighbour was found and is explicitly subtracted.  No
inspected primary or authoritative result in this bounded pass states the
literal simultaneous old-cut filter together with its `N-3` unique clock and
every-target inverse atlas.  Search coverage is incomplete; this non-hit has
no positive novelty meaning.

## Internal collision pressure

| neighbour | subtraction |
|---|---|
| P126 | splits composition parts; P191 only deletes old cuts |
| P147 | merges equal maximal runs; P191 uses a full-prefix divisibility predicate |
| P131 | rotates normalized Euclidean quotients rather than monotonically deleting cuts |
| P181 | permutation prefix reversal with possible two-cycles, not composition coarsening |
| P185 | rewrites word coordinates by prefix diversity, without cuts or divisibility |
| P186 | rank-compresses subset support; predecessor gaps do not control its update |

Generic composition/cut encodings, coarsening, divisibility, and path DP
receive zero contribution credit.  This history comparison does not supply
external ownership clearance.

## Accepted boundary

- The false OEIS modification-date clause is repaired and mechanically pinned.
- `OWNER_AMBER / HOLD_EXTERNAL` is preserved.
- A bounded non-hit is not translated into a novelty or priority assertion.
- A literal/equivalent owner discovered later still requires withdrawal or complete
  repositioning.
