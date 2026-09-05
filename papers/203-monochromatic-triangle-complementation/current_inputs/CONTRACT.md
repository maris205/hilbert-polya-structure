# MCT literal contract and status boundary

Date: 2026-09-05 UTC. **SCOUTING THEOREM SPIKE / NO NUMBER / HOLD_EXTERNAL**.
This is one proposed finite autonomous deterministic system. Parameter
boxes and the two colours are not counted as additional systems.

## Literal carrier and update

For every $n\geq0$, take all simple loopless undirected graphs on
$[n]=\{0,\ldots,n-1\}$. Each pair has bit 0 or 1, so the carrier size is
$2^{\binom n2}$. There is no acyclicity restriction. Among sorted triples
$(a,b,c)$ with all three pair bits equal, choose the lexicographically
least and complement all three bits. If no such triple exists, hold.

This fixes the parameter, labels, tie-breaking, update simultaneity,
meaning of colour 0, and boundary $n<3$.

## Claim spine

1. **Non-generic temporal structure:** on the strictly descending selector
   trace through the first recurrent state, every next triple replaces one
   vertex by a previously unused lower-labelled vertex. After the first
   strict transition the least vertex is constant. A fixed-anchor trace is
   a sliding pair with strictly decreasing same-parity vertex subsequences.
   Consequently the sharp maximum tail is $\max\{0,n-3\}$; explicit
   colourings attain it for every $n\geq3$.
2. **Complete target inverse and extrema:** every source is reconstructed
   by conditions D/C in `INVERSE_THEOREM.md`, including zero fibres.
   Nonfixed inverse triples form a Johnson clique; actual targets attain
   both star and four-face capacities. Thus the maximum fibre is 1 for
   $n\leq3$ and $\max\{4,n-2\}$ for $n\geq4$. Conditions S1–S3 and
   K1–K3 characterize **all** maximum-fibre targets, with both equality
   families retained at the crossover $n=6$.

The inverse axis is fully proved in `INVERSE_THEOREM.md`. The temporal
axis is the collaborator's separate proof at
`../../reviews/mct_temporal_pressure_20260905/PROOF_PACKAGE.md`, fully read
and challenged by this inverse author. Its exact source pin is recorded
in `PINNED_INPUTS_SHA256SUMS`; messages alone are not the proof evidence.
This contract is not an independent gate acceptance.

## Generic recurrent facts, zero contribution credit

The selected triple remains monochromatic after complementation, so its
label cannot increase at the next step. If it stays equal, complementing
that same triple again returns to the original graph. Thus all cycles
have length 1 or 2. The fixed points are exactly graphs with neither a
triangle nor an independent triple. A nonfixed graph cannot map to a
fixed point.

There is also a complete target-local recurrent test. For a graph $Y$ with
least monochromatic triple $Q$ of colour $c$, it is recurrent if and only
if for each $u\notin Q$ and pair $\{x,y\}\subset Q$ with
$\{u,x,y\}<Q$, the two bits $y_{ux},y_{uy}$ are not both $1-c$.
Indeed, no earlier triple was monochromatic before the move. The only
possible new earlier triple shares one flipped edge with $Q$, and it
becomes monochromatic exactly in the excluded two-edge configuration.
Absence of such a triple leaves the selector unchanged, yielding a strict
two-cycle; its presence gives a smaller selector and precludes recurrence.

The fixed-point counts for $n=0,\ldots,5$ are $1,1,2,6,18,12$, and zero
for every $n\geq6$. The $n=4$ graphs are the twelve labelled paths, three
four-cycles and three two-edge perfect matchings. For $n=5$, every vertex
has degree at most two in both graph and complement, hence degree two;
triangle exclusion forces a five-cycle, giving $5!/10=12$ graphs. On six
vertices, one vertex has three incident edges of one colour. Either a
pair of their other endpoints has that colour, or all three connecting
edges have the other colour; both cases produce a monochromatic triangle.
This is the classical Ramsey argument and receives no credit.

## Hard limitations and process separation

- No all-time inverse formula, closed image census, full basin census or
  closed count of the maximum-fibre targets is asserted.
- Generic minimum-involution descent, static Ramsey facts, induced
  complementation and Johnson star/top classification are zero credit.
- The full author probe remains capped at $n\leq6$; its observed no-return
  properties do not replace the all-parameter proof.
- The inverse author and the temporal collaborator are co-contributors,
  not independent reviewers of this candidate. A later process-separated
  owner/value gate controls admission. No model-diversity endorsement is
  implied by delegation or repeated runs.
- No P202 paper review was undertaken by this scout, who authored its OR
  candidate. No central file, accepted paper or historical frozen file is
  changed by this scouting package.
