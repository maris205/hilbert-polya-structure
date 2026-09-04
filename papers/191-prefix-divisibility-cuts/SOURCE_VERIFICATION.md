# Source verification — P191 Round 0

**Checked:** 2026-09-04 UTC.  **Scope:** all bibliography entries, every
citation context, and a bounded direct-owner search.  **Status:**
`PASS_INTERNAL / OWNER_AMBER / HOLD_EXTERNAL`.

## Cited records and scope

| key | verified record | manuscript use | excluded inference |
|---|---|---|---|
| `Stanley2011EC1` | Richard P. Stanley, *Enumerative Combinatorics*, vol. 1, 2nd ed., Cambridge University Press; DOI `10.1017/CBO9781139058520`; print ISBN `978-1-107-60262-5` | standard enumerative background for compositions and Boolean cut encodings | the update, clock, or inverse formulas of P191 |
| `BilleraThomasVanWilligenburg2006` | *Advances in Mathematics* 204(1), 204–240 (2006); DOI `10.1016/j.aim.2005.05.014`; arXiv `math/0405434` | the explicit partial-sum subset encoding and adjacent-part coarsening/refinement language in Section 1 | divisibility filtering or iteration |
| `HeubachMansour2009` | Silvia Heubach and Toufik Mansour, *Combinatorics of Compositions and Words*, Chapman & Hall/CRC; DOI `10.1201/9781420072686`; print ISBN `978-1-4200-7267-9` | static composition and restricted-composition background | P191's state-dependent prefix predicate or dynamics |
| `BenderCanfield2005` | *The Electronic Journal of Combinatorics* 12(1), R57 (2005); DOI `10.37236/1954` | established locally restricted-composition framework | ownership of a predicate depending on the full current prefix, simultaneous coarsening, or iteration |
| `Navarro2026OEISA398023` | Oliver Navarro, OEIS A398023, submitted 16 July 2026 and modified 27 August 2026; accessed 4 September 2026 | the closest inspected static prefix-divisibility neighbour | the literal P191 predicate, cut deletion, or any dynamical theorem |

The first four records were checked against DOI/Crossref metadata and official
publisher or journal records.  The Billera--Thomas--van Willigenburg content
claim was also checked in the author/arXiv text: its opening definitions give
the partial-sum subset and the coarsening order obtained by merging adjacent
parts.  Crossref dates Stanley's second edition to 2011; Cambridge also lists
later online/publication dates, so the bibliography follows the DOI deposit.

The exact cite-key set in `main.tex` equals the five-key bibliography set.
Each citation is used only for background or subtraction.  No citation is
presented as support for a P191 theorem.

## Nearest external object

OEIS A398023 is deliberately named in the manuscript because its wording is
easy to confuse with the present predicate.  The distinction is literal:

```text
A398023: index i divides the prefix sum s_i; static enumeration.
P191:    current part a_i divides the prefix sum s_i; failing old cuts are
         deleted simultaneously, new parts are formed, and the map iterates.
```

The OEIS entry does not state the P191 self-map, its transient theorem, or its
target-resolved inverse recurrence.

## Bounded owner-search log

The following exact and semantic queries were inspected across web search,
Google Scholar-style indexing where exposed, arXiv, DBLP, Crossref, OEIS, and
publisher pages:

```text
"part divides" "partial sum" compositions
"divides the partial sum" composition integer
"prefix sum" divisible "compositions"
("divisible composition" OR "divisor composition") integer compositions
"a_i divides s_i" composition dynamics
"retain the cut" composition divisibility
"delete the cut" "prefix sum" composition
"part divides its prefix sum"
site:arxiv.org composition "partial sums" divisibility parts
site:combinatorics.org composition "partial sum" divides
integer composition self-map delete separators divisibility
dynamical system on integer compositions coarsening cuts
"a_i divides a_1 + ... + a_i"
"c_i divides c_1 + ... + c_i"
"each part divides the sum" "initial segment" composition
"nonterminal part" divides "partial sum" composition
```

Database controls included an arXiv API query for integer composition,
partial sum, and divisibility (zero records); a DBLP query for the same terms
(zero records); a Crossref bibliographic query, whose returned records were
about unrelated divisibility sequences; and an OEIS exact search for the
fixed-count segment `13,20,37,55,97,157,267` (no registered hit).

No inspected primary or authoritative record states the literal iterative
map

```text
retain an old internal cut s_i iff its current incoming part a_i divides s_i
```

together with the sharp clock or every-target inverse atlas.  Coverage is
necessarily incomplete.  This bounded non-hit is not novelty, priority,
completeness, freedom-to-operate, or external-release evidence.  Discovery of
a literal or equivalent owner requires withdrawal or complete repositioning.

## Internal history subtraction

| paper | proximity | literal difference |
|---|---|---|
| P126 | same positive-composition carrier | splits parts and adds cuts; P191 only deletes existing cuts by a prefix arithmetic test |
| P147 | same carrier and simultaneous merging | merges maximal equal runs by a local equality predicate; P191 tests each current incoming part against its full endpoint |
| P131 | composition encoding and Euclidean/divisibility flavour | rotates normalized continued-fraction quotients; it is not monotone cut deletion |
| P169 | synchronous update and target-resolved fibres | transfers maxima in canonical set partitions, not composition cuts |
| P181 | prefix-triggered rule | reverses a permutation prefix and may have two-cycles; P191 is monotone coarsening |
| P185 | prefix-statistic language | rewrites word coordinates by prefix diversity; there is no composition, divisibility, or cut deletion |
| P186 | a composition cut set is itself a subset | rank-compresses and moves subset support; P191 retains a subset of the old cuts according to predecessor gaps |

The closest internal dynamical silhouette is P147 because it shares both the
carrier and coarsening direction; P186 is the strongest representation-level
warning.  Neither supplies the literal update or transfers the two proofs.

Final gate: `OWNER_AMBER / HOLD_EXTERNAL / NOVELTY_CLAIM_NOT_AUTHORIZED`.
