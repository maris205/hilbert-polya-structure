# System and proof-engine collision firewall — P157–P161

**Status:** Round-2 five-paper collision gate accepted; P160 Review B closed
`0 Critical / 0 Major / 0 Minor`.  **External state:** `HOLD_EXTERNAL`.

Broad similarities such as finite state spaces, exact fibres, shallow
collapse, or zeta functions provide no separation credit.  The table fixes
the literal and proof-level distinctions that every draft must preserve.

| pair / occupied neighbour | superficial overlap | decisive separation |
|---|---|---|
| P157 vs P44/P100/P107/P142 | valuations and prime-power strata | cubic on every residue with two parity basins and normalized units modulo 8; not exponent erasure or a divisor map |
| P157 vs P150 | finite arithmetic map with fibres | absorbing chain-ring cubic and odd-unit lifting; not a totalized finite-field rational map |
| P158 vs P143 | Boolean encoding and labelled fibres | random decreasing edge intersection via complementary histories; not deterministic row-inclusion retraction |
| P158 vs P145/P146 | stochastic graph epochs | global fresh cuts with word occupancy; not cut-space orientation reversal or random ear deletion |
| P159 vs P114/P148 | simultaneous graph/tree pruning and all-time fibres | unrestricted graphs, parity-defined deleted set, connected binary incidence system; not height peeling or Catalan promotion |
| P159 vs P123 | graph parity | changes the vertex set and preserves induced edges; never complements a component |
| P160 vs P113 | partition/Durfee or hook coordinates | RCS repeatedly applies a fixed southeast coordinate crop and resolves arbitrary-time targets plus an empty branch; P113 transforms principal-hook partition data and does not supply this literal update or interface |
| P160 vs P126 | integer compositions/partitions and exact fibres | RCS deletes a global Ferrers coordinate window and decreases both row and column support; it never splits parts or uses a refinement tree |
| P160 vs P129/P148 | rank loss and diagram/tree language | deterministic fixed-coordinate stripping with all-time arbitrary-target/empty-branch recovery; not stochastic pile coalescence or local plane-tree promotion. Static two-boundary structure earns no separation credit |
| P161 vs P81 | orthogonality language | finite affine triangle center, singular sink, and oriented shells; not a spherical orthogonality shift |
| P161 vs P150/P153 | finite-field collapse/totalization | orthocentric four-window reverse equation and right-angle singularity; not Lyness or factorial-collapse algebra |
| P160 vs P161 | finite exact collapse | Ferrers coordinate translation with unbounded square-root-scale capped height versus a depth-two affine orthocenter window |
| P157 vs P159 | powers-of-two and linear parity checks | odd-unit Hensel lifting on a fixed residue ring versus incidence rank on variable labelled vertex sets |
| P158 vs P159 | graph deletion/collapse | stochastic edge intersection on a fixed vertex set versus deterministic simultaneous vertex removal and nilpotent inverse ranks |

## Pairwise fingerprints

| paper | carrier/update | recurrent object | second-axis engine | height |
|---|---|---|---|---|
| P157 | fixed chain ring; cubic | two endpoints | branchwise odd-unit lifting | `ceil(log_2 n)` |
| P158 | fixed labelled vertices; random cut intersection | empty graph in the stopped process | complementary-pair occupancy | unbounded random, exponential tail |
| P159 | graphs on variable subsets; odd-vertex deletion | every even graph | binary incidence rank and `B_n` powers | `floor(n/2)` |
| P160 | integer partitions; fixed deletion of `a` rows and `b` columns at every step | empty partition | arbitrary prescribed target plus distinct empty branch, exact cap support, ordered recovery (static two-boundary factorization is zero credit) | `min{t:(at+1)(bt+1)>N}` |
| P161 | affine ordered triangles plus sink; orthocenter window | sink plus 4-cycles | unique reverse orthocenter window | 2 |

Any draft that erases these fingerprints and falls back to a generic
functional-graph story fails the portfolio gate even if all displayed
formulas are correct.
