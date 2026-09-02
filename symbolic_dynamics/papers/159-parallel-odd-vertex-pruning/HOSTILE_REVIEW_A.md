# P159 Hostile Review A — original report

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Criteria binding:** `criteria_binding_unavailable`; no venue-fit claim is
made.  
**Execution boundary:** one role-separated adversarial review, not evidence of
independent error processes.  I did not consult a formal Review B.  The
phase-one pre-paper gate was treated as frozen background, not as a substitute
for manuscript review.  No P159 author file was modified; this report is the
only new paper-local file, and the reviewer verifier is outside the paper.

## Verdict

**PASS — 0 Critical / 0 Major / 0 Minor.**

The strict positive-even-`d` transfer, its zero diagonal, the fixed-`D`
`s=0,d=2` source, target-row/source-column orientation, all `n=0,1` and `t=0`
boundaries, the `B_n^t` versus `I+B_n+...+B_n^t` split, image criterion, fixed
and image counts, depth CDF and shells, source subtraction, anonymity,
`HOLD_EXTERNAL` status, exact controls, and five-page PDF all survive
independent reconstruction.  No revision is required by Review A.  This is an
internal mathematical/artifact pass only, not external owner clearance.

## Strongest counter-argument

The strongest objection is that nearly every ingredient is classical and the
remaining residual may be too elementary or already present under another
name.  The handshaking lemma forces an even deleted set; a connected binary
incidence matrix gives consistency and nullity; target independence then makes
ordinary matrix multiplication work; and the image and CDF are short
positivity and summation consequences.  Sequential parity-deletion games,
Eulerian deletion, and parallel peeling already occupy the surrounding
language.  A direct source on an “odd-degree core,” synchronous parity
stripping, or iterated odd-vertex deletion could therefore absorb most of the
paper at once, even if it does not use the manuscript's rank-transfer notation.

That objection does not identify an internal defect.  The manuscript explicitly
assigns the classical ingredients zero contribution credit, restricts the
residual to the conjunction of a target-uniform strict inverse, correctly
oriented every-time fibres, and exact image/CDF consequences, and retains a
bounded-search warning plus `HOLD_EXTERNAL`.  The inverse count is genuinely
stronger than the forward clock: it resolves every fixed labelled target and
source rank.  Until a direct owner is found, the appropriate hostile-review
outcome is a narrow internal pass with continued ownership screening, not a
fabricated mathematical objection.

## Independent theorem audit

| Interface | Independent reconstruction / attack | Verdict |
|---|---|---|
| literal update / clock | The odd-degree set has even cardinality.  A non-even state therefore loses at least two vertices, while an even state is fixed.  The path loses exactly its two endpoints per active round. | PASS |
| strict `d>0` consistency | For fixed target set `S` and deleted set `D`, free edges are exactly those meeting `D`.  Their incidence syndromes have even total weight; the required syndrome has weight parity `d`, so it is attainable exactly for even `d`. | PASS |
| strict nullity | The variable-edge graph is connected for every `d>0`, including the single-vertex boundary.  Its binary incidence rank is `s+d-1`, leaving nullity `s(d-1)+binom(d-1,2)`. | PASS |
| target independence | Every attainable right-hand side is a translate of the same incidence kernel.  The only consistency condition is its total parity, already fixed by `d`; no edge statistic of `H` remains. | PASS |
| label aggregation | Choosing `D` from the `n-s` unused ambient labels multiplies the fixed-`D` count by `binom(n-s,d)`. | PASS |
| fixed diagonal | `d=0` is not strict.  A same-rank source deletes nothing, hence must equal the target and exists exactly when that target is even.  The zero diagonal of `B_n` is therefore necessary. | PASS |
| matrix direction | With targets on rows and sources on columns, composition is `sum_k B_n(s,k)B_n(k,m)`.  The sentinels `B_4(0,2)=6`, `B_4(2,0)=0`, and `(B_4^2)(0,4)=24` reject transposition. | PASS |
| temporal split | A strict predecessor is non-even and cannot wait.  All `t` steps into a non-even target are strict, giving `B_n^t`; an even target can first arrive after any `j<=t` and wait, giving the disjoint geometric sum. | PASS |
| image iff | A non-even time-`t` target needs `t` positive even reverse increments, hence at least `2t` unused labels.  Choosing `t` increments of two proves sufficiency.  Even targets are fixed self-predecessors. | PASS |
| censuses | Even graphs on a fixed `s`-set form the complete-graph incidence kernel and number `e_s`.  Summing the fixed-target geometric fibres counts exactly the states with entrance time at most `t`. | PASS |

The abstract, theorem, proofs, claims ledger, and frozen theorem contract agree
on each interface.  “Even” consistently means all degrees even and never
silently imposes connectivity.

## Boundary attacks

### Strict transfer and fixed diagonal

The displayed `B_n(s,m)` correctly requires `d=m-s>0`.  Odd `d` has no
solution.  At `d=0`, the manuscript does not insert a false diagonal into
`B_n`: the one-step same-rank fibre is separately one for an even target and
zero for a non-even target.  This distinction also makes the `t=0` fibre
correct, since both branches reduce to the identity matrix.

### Empty target with `s=0,d=2`

For a fixed deleted pair, the variable graph has one possible edge.  Both
vertices must be odd, so that edge is forced and the unique source is `K_2`.
Choosing the pair gives `B_n(0,2)=binom(n,2)`.  Literal enumeration confirms
the fixed-pair and aggregate statements.

### Degenerate carriers

At `n=0`, the only state is the fixed empty graph.  At `n=1`, the empty and
singleton graphs are both fixed.  The phase, fixed, CDF, image, and clock
formulas return `1,1,1,1,0` and `2,2,2,2,0`, respectively.  No positive-even
strict increment is available.

### `B^t` versus the geometric sum

The labelled `K_2` target is non-even.  At `t=1` it has no same-rank
predecessor: the literal count and `B_2(2,2)` are both zero, whereas the
incorrect geometric sum would contribute the identity entry one.  For an
even target, by contrast, the identity term records the fixed self-source and
is indispensable.  The manuscript and both verifiers maintain this split at
all audited times, including two epochs beyond stabilization.

### Time-zero image

The theorem's image criterion is explicitly restricted to `t>=1`.  At
`t=0`, the manuscript separately uses the identity map and the complete phase
size.  No non-even rank layer is incorrectly removed at time zero.

## Exact-control audit

The author verifier was cold-replayed twice with bytecode disabled.  Both runs
match `verification_output.txt` byte for byte, contain **3,167,525 exact
assertions**, and preserve transcript SHA-256
`363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879`.
It enumerates all 41,658 labelled graph states through ambient order six,
checks every literal target/source-rank fibre through stabilization and two
extra epochs, and separately row-reduces 511 incidence systems through total
order nine.  The matrix and literal-state lanes are genuinely distinct.

The reviewer-owned verifier is
`docs/papers157_161_sequence/reviews/p159_a/verify_p159_review_a.py`.  It does
not import or call the author verifier.  It represents every state by global
vertex and edge bit masks, constructs literal updates from endpoint-parity
toggles, and builds the transfer independently.  Its graph-free second lane
uses syndrome-counting dynamic programming rather than Gaussian elimination;
it checks every attainable target parity vector through total order twelve.
It also checks every target and source rank through `n=6`, all `n=0,1,t=0`
boundaries, every fixed deleted pair for `s=0,d=2`, the even/non-even temporal
discriminator, exact images/CDFs/shells, and matrix positivity/nilpotence
through `n=20`.

The reviewer verifier performs **3,605,601 exact assertions**.  Two cold runs
match `CANONICAL.txt` byte for byte.  Reviewer transcript SHA-256:
`d4a1592bd29c3f652bef0cb955b2f0b74181c98b6800eeee7df59e5e3a556095`.
Finite agreement remains counterexample pressure only; it is not proof,
novelty evidence, owner clearance, or release authorization.

## Source and ownership audit

The six bibliography entries and their subtraction roles are accurate:

- The [EuDML record](https://eudml.org/doc/129047) confirms Nowakowski--
  Ottaway, *Integers* 5(2), A15 (2005), a sequential parity-restricted vertex
  deletion game.
- The [journal version of Krüger](https://math.colgate.edu/~integers/og7/og7.pdf)
  confirms *Note on Odd/Odd Vertex Removal Games on Bipartite Graphs*,
  *Integers* 14, G07 (2014); it studies sequential moves and Grundy values.
- The [Springer record for Cygan et al.](https://link.springer.com/article/10.1007/s00453-012-9667-x)
  confirms *Algorithmica* 68(1), 41--61 (2014), DOI
  `10.1007/s00453-012-9667-x`, and its selected-deletion optimization scope.
- The [primary arXiv record for Dabrowski et al.](https://arxiv.org/abs/1410.6863)
  and DOI metadata confirm *JCSS* 82(2), 213--228 (2016), DOI
  `10.1016/j.jcss.2015.10.003`, concerning chosen edits under parity and
  connectivity constraints.
- The [primary arXiv record for Jiang--Mitzenmacher--Thaler](https://arxiv.org/abs/1302.7014)
  confirms SPAA 2014, 319--330, DOI `10.1145/2612669.2612674`; its parallel
  rule removes all vertices below a threshold in random hypergraphs.
- Springer DOI metadata confirm Reinhard Diestel, *Graph Theory*, fifth
  edition, GTM 173 (2017), DOI `10.1007/978-3-662-53622-3`.

A bounded alternate-term screen for deleting all odd-degree vertices,
synchronous parity stripping, odd-degree cores, and parallel parity peeling
did not locate the literal process together with the rank-transfer atlas.  No
absence inference follows.  The paper correctly distinguishes the sequential
games, chosen editing problems, and degree-threshold peeling from its forced
simultaneous update, assigns standard graph algebra zero credit, and keeps the
direct-owner question unresolved.

## Anonymity, external status, and PDF audit

The TeX source uses `\author{Anonymous}`.  PDF title, author, subject,
keywords, and custom metadata are blank; there is no identifying metadata,
form, JavaScript, or encryption.  The tool-use statement is generic and does
not de-anonymize the manuscript.  `HOLD_EXTERNAL` appears visibly in the paper
and support package, with posting, submission, circulation, and author contact
explicitly prohibited.

Two isolated source-only builds using
`pdflatex -> bibtex -> pdflatex -> pdflatex` are byte-identical to each other,
`main.pdf`, and `main_round0_original.pdf`.  The artifact has five A4 pages,
363,455 bytes, and SHA-256
`bba68d57e9f46cda2996db072b703ff0b18e5d19c7edab2a53ef24d3032c8602`.
All 27 font rows are embedded, subsetted, and Unicode mapped.  The settled log
contains no unresolved citation/reference, rerun request, BibTeX warning,
pdfTeX warning, overfull/underfull box, duplicate label, or error.  All five
pages were independently rasterized and inspected; equations, theorem lists,
the audit table, declarations, and references are legible and unclipped, with
no collision or malformed glyph.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Observations (non-defects)

1. The target-uniform strict inverse is the only claim-bearing mathematical
   engine; the path clock and fixed-even locus should remain supporting context.
2. The direct-owner search remains the external risk.  Review A found no
   checked source collision, but its bounded non-hit cannot clear ownership.
3. The page-five whitespace is a harmless consequence of a short six-entry
   bibliography and does not impair the five-page manuscript.

Final Review-A disposition: **PASS_INTERNAL / HOLD_EXTERNAL**, subject to an
independent Review B and continued direct-owner screening.  This report does
not authorize external posting, circulation, submission, author contact,
novelty, or priority claims.
