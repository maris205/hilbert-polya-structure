# Source verification and owner subtraction — P181

**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`  
**Rule:** a direct owner removes credit; a bounded query miss supplies no
novelty, priority, or release authority.

## Verified primary controls

| Key | Verified record | Independent surfaces | Zero-credit assignment |
|---|---|---|---|
| `GatesPapadimitriou1979` | William H. Gates and Christos H. Papadimitriou, “Bounds for Sorting by Prefix Reversal,” *Discrete Mathematics* 27(1) (1979), 47–57, DOI `10.1016/0012-365X(79)90068-2` | Elsevier/ScienceDirect, DBLP, Crossref DOI BibTeX, and the primary article PDF | classical permutation pancake sorting, arbitrary prefix reversals, and worst-case reversal distance |
| `HurkensEtAl2007` | Cor Hurkens, Leo van Iersel, Judith Keijsper, Steven Kelk, Leen Stougie, and John Tromp, “Prefix Reversals on Binary and Ternary Strings,” *SIAM Journal on Discrete Mathematics* 21(3) (2007), 592–611, DOI `10.1137/060664252` | SIAM version-of-record page, Crossref DOI BibTeX, and `arXiv:math/0602456` | generic prefix-reversal definition, pancake vocabulary, and optimal sorting questions on binary/ternary strings |
| `PudwellSmith2024` | Lara Pudwell and Rebecca Smith, “Sorting via Shuffles with a Cut after the Longest Increasing Prefix,” *Theoretical Computer Science* 1008 (2024), article 114679, DOI `10.1016/j.tcs.2024.114679` | Elsevier/Crossref DOI metadata and an author publication list | state-selected cuts after the longest increasing prefix and four cut-and-riffle sorting maps |

The Gates–Papadimitriou DOI ends in `90068-2`; the superficially plausible
ending `90068-X` is wrong.  Pudwell–Smith has article number 114679 and no
issue number in the verified record.

## Claim-level scope

Gates and Papadimitriou allow prefix lengths to be chosen in a sorting
sequence and study minimum/worst-case numbers of moves.  Hurkens et al.
define the same generic operation and study binary/ternary string sorting.
Neither source prescribes the autonomous choice “stop immediately after the
first descent,” nor studies the resulting functional graph.

Pudwell and Smith select a cut after the longest increasing prefix, but their
four operations are cut-and-riffle shuffles; reversal variants reverse the
second part before the riffle.  They do not reverse the entire prefix ending
at the first descent's follower.  The longest-increasing-prefix vocabulary
therefore receives zero credit without transferring P181's theorem.

## Exact negative control: Project Euler First Sort

The official [Project Euler Problem 523](https://projecteuler.net/problem=523)
and [Problem 524](https://projecteuler.net/problem=524) use the same scan
trigger but a different update.  At the first descent they move the smaller
follower to the front:

```text
(pi_1,...,pi_d,pi_(d+1),...) ->
(pi_(d+1),pi_1,...,pi_d,...).
```

P181 instead reverses that whole prefix:

```text
(pi_1,...,pi_d,pi_(d+1),...) ->
(pi_(d+1),pi_d,...,pi_1,...).
```

For example, `1324` maps to `2314` in P181 and to `2134` under First Sort.
The rules agree only when the first descent is at position one.  Project
Euler directly owns the move-follower-to-front rule and its counting
questions; it does not own P181.  For this reason the manuscript never calls
P181 “First Sort.”  These official webpages are used as negative controls,
not added as journal entries to `references.bib`.

## Internal collision firewall

| Existing line | Shared shell assigned zero credit | Literal separation |
|---|---|---|
| P122, even record-block reversal | deterministic permutation reversal, lexicographic/descent reasoning, target-local inverse cuts | P122 reverses all even left-to-right-record blocks synchronously and is acyclic; P181 reverses one first-descent prefix and has a two-cycle core |
| P117, odd-run reversal | reversal language, fixed/two-cycle bookkeeping, sharp tails | P117 acts on cyclic binary runs by value flips, not on a permutation prefix by order reversal |
| killed FDF spike | identical first-descent trigger and target-at-front flavour | FDF is exactly the Project Euler move-follower-to-front rule; P181 reverses the full selected prefix |
| FAR scout conjugate | the same aggregate statistics | FAR is value-complement conjugate to P181 and is excluded from independent credit |

## Retained ceiling and kill switch

Arbitrary prefix reversals, pancake graphs, sorting distance, longest
increasing prefixes, descents, peaks, and generic functional-graph/tail/fibre
bookkeeping receive zero contribution credit.  The retained conjunction is

```text
the autonomous first-descent-plus-one prefix reversal
+ exact half-image
+ identity/peak two-cycle core
+ complete depth census
+ decreasing-run inverse atlas and all maximizers.
```

A source stating this literal conjunction, or a routine transfer of its two
independent axes from an occupied system, is an immediate kill switch.  The
bounded non-hit leaves `OWNER_AMBER / HOLD_EXTERNAL` in force.
