# P211 narrative report

Status: admitted theorem contract, first manuscript/source preparation only.
No new scientific execution, canonical production, build, freeze or
manuscript review has occurred in this directory.

## One-sentence contribution

For feedback that recomputes the kernel and completed-image projections of
an order-preserving map at every step, we determine the exact terminal
projection and sharp full-carrier clock, and independently reconstruct
every one-step predecessor by ordered choices in target-local gaps.

## The problem and its two answers

The carrier is every nondecreasing map from the finite chain $[n]$ to
itself, not merely the extensive or top-fixing submonoid. A current map
has right kernel endpoints $X$ and image $Y$; set $A=Y\cup\{n\}$ and
$T(f)=e_X\circ e_A$, where $e_S(i)=\min\{s\in S:s\ge i\}$.
The right factor acts first. Both supports are recomputed from $T(f)$
before the next step. This is not repeated composition of a fixed pair.

The first image has ordered endpoint/value pairs $(w_i,z_i)$ satisfying
$w_i\le z_i<w_{i+1}$ and ending in $(n,n)$. Common endpoints are
permanent anchors. Between anchors the endpoint list alternates strictly;
each update removes its two outside endpoints. The resulting exact
pointwise clock includes the initial normalization for nonfixed sources.
The maximum is $H_1=0$, $H_n=\lceil n/2\rceil$ for $n\ge2$.
Both parity witnesses are explicit. Every orbit ends at
$e_{X\cap(Y\cup\{n\})}$, and all recurrent states are fixed projections.

For a labelled image target, every source is described by its forced
endpoint colours, forbidden sites, and ordered choices in each free gap
$(z_{i-1},w_i)$, with $z_0=0$. Selected $X$-sites precede selected
$A$-sites. The published support-rank branches $|A|-|X|=0,1$ then
recover $Y=A$ or $Y=A\setminus\{n\}$. The new target-gap factorization
gives the finite coefficient formula in the manuscript; off-image
targets have zero predecessors. This inverse argument does not use the
clock theorem or numerical enumeration.

## Known material and the exact contribution boundary

Stein's 2025 Section 5.1 already gives the kernel/image coordinates,
ceiling supports, completed-image support, and unique reconstruction for
rank differences zero and one. They receive no contribution credit.
The first manuscript implements admission item m01 by explicitly saying
so both when the map is defined and when the inverse branches are used.

Andrenšek's arXiv:2604.15497v1 Section 4 gives the Catalan floor-retraction
specialization and static product-idempotence criteria. Version 3 instead
has the general graph-path criterion in Theorem 3.6. These are separately
cited, with their distinct titles and theorem numbering. Graph-generator
content sets are not identified with our endpoint supports. Static
retractions/products/idempotence and order duality receive zero credit.
This implements m02 in the draft, subject to actual manuscript inspection.

The admitted residual is modest and specific: the recomputed dynamics,
its exact initial-step/sharp clock, and the resolved labelled-target gap
factorization. Generic deletion and ordinary finite-map bookkeeping are
not standalone advances. No theorem rules out every possible owner,
factor or lift. No global maximum fibre, maximizer, basin count or all-time
inverse theorem is asserted.

## Evidence and unfinished obligations

The self-contained deductive proofs, not finite observations, establish
the all-n statements. The earlier author exploratory pilot covered
2,353 functions for $1\le n\le7$ and passed its seven categories, but its
strict runtime-prelock audit failed. That old package remains immutable
and is not an eligible strict manuscript replay or a source of the new
canonical. We do not import its implementation or output.

A fresh standalone paper-local verifier and exact parameter/schema plan
are drafted here. The author interface emits all source/target records,
not only aggregate checks. New production, an immutable canonical,
runtime-closed replay pairs, builds, Round0/1/2, and two actual nonauthor
manuscript reviews remain pending root coordination. The current paper
text reports the verification design without claiming new executed data.

## Reader-facing story

The paper asks two concrete questions: how long does this recomputed
feedback take to stabilize, and which maps lead to a specified target in
one step? The same ordered coordinate system makes both answers explicit,
but the mechanisms differ: labelled endpoint peeling for time, and a
forced/free/forbidden partition with ordered colours for the inverse.
All proofs fit in the main text. A small comparison table clarifies what
is inherited; no decorative figure or experimental expansion is needed.
