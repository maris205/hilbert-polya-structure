# Ordered-interaction fresh desk: GBPR

Date: 2026-09-08 UTC. Author: `round211_rational_scout`.
Decision: **NO_PROMOTION_VALUE**. One literal attempt, zero reserves, zero
paper assignments, zero scientific executions. Root reception is pending.
This is not a claim that the literal is globally new or that its mathematics
has passed independent review.

## Literal and result

GBPR means **globally best blocking-pair repair**. For each integer $n\ge1$,
the states are all perfect matchings on $[2n]=\{1,\ldots,2n\}$. Rank an
unordered pair $\{i,j\}$, $i<j$, by the lexicographic tuple
$\rho(\{i,j\})=(j-i,i,j)$. A missing pair blocks the current matching when
both endpoints prefer it to their current pair, with smaller rank preferred.
Choose the least-ranked blocking pair $\{a,b\}$; if the old pairs are
$\{a,c\},\{b,d\}$, replace them by $\{a,b\},\{c,d\}$. Fix states with no
blocking pair. All pairs are permitted, including crossing pairs. There is
no moving point, external clock, random choice, unmatched vertex or hidden
update order.

The [complete author proof](PROOF_PACKAGE.md) establishes:

- The unique fixed point is $G=\{e_1,\ldots,e_n\}$, where
  $e_i=\{2i-1,2i\}$, and there are no longer cycles.
- With common edges counted as two-coloured length-two components,
  $h(M)=n-c(M\cup G)$. The sharp maximum is $n-1$; equality holds exactly
  for a single alternating overlay cycle. The number of deepest states is
  $2^{n-1}(n-1)!$.
- For every target $Y\ne G$, let $r$ be the first index with $e_r\notin Y$.
  Then $1\le r\le n-1$ and
  $|T^{-1}(Y)|=(r-1)(2n-r)$, including zero when $r=1$.
  The target $G$ has $n(n-1)+1$ preimages and is the unique fibre maximum.
- The image is exactly the matchings containing $e_1$, of size
  $(2n-3)!!$, with $(-1)!!=1$.
- Even replacing the line-distance order by any strict global edge order
  gives a conjugate map after relabelling its ordered greedy matching.
  That general-order statement is a proof device, not a second literal or
  a claimed new deformation.

These are deductive author results, not measured tables. No enumeration,
pilot, scientific import, verifier, canonical output or manuscript was made.

## What survives the source subtraction

The decisive reduction is literal: the chosen blocking edge is always the
first absent edge of the static greedy matching. Thus the apparent
endogenous geometric interaction disappears from the functional graph.

[Abraham--Levavi--Manlove--O'Malley, *The Stable Roommates Problem with
Globally-Ranked Pairs*](https://eprints.gla.ac.uk/150540/1/150540.pdf),
printed pp. 2–3, defines globally ranked pair preferences and characterizes
stable matchings by maximal matchings in rank prefixes (Lemma 1). Its
successive-rank construction specializes to a unique greedy matching when
all ranks are distinct. This source owns the static preference/endpoint
primitive; it is not being cited for the displaced-partner repair rule.

[Hoefer, *Local Matching Dynamics in Social
Networks*](https://algo.rwth-aachen.de/team/hoefer/papers/Hoefer11Matching.pdf),
printed pp. 4–5, defines best response by the currently maximum-benefit
blocking pair. Its ordinary update removes displaced edges and can leave
vertices unmatched; it does **not** by itself identify GBPR's perfect-state
repair. The scheduler primitive receives no novelty credit, but no false
identity with that model is asserted.

[Jennings, *Geodesics in a Graph of Perfect
Matchings*](https://www.mat.univie.ac.at/~slc/wpapers/s74jenn.pdf), printed
pp. 3–5, directly defines the same edge-insertion/partner-repair operation.
Proposition 2.4 inserts the ordered edges of any fixed target matching;
Observation 3.2 and Theorem 3.4 give the component-change mechanism and
distance $n-c$, and Corollary 3.5 gives the diameter and antipodes. These
consume the time, rigidity and deepest-count axes after the reduction.
The all-target inverse formula above is explicitly proved here, but is
only a first-missing-prefix partition of ordinary two-edge flip neighbours;
the fixed-target maximum is their degree plus its self-loop (Remark 2.3).
No inspected source is claimed to state our exact autonomous scheduler and
all-target formula together.

The discovery waypoint was
[Cioabă--Royle--Tan](https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/d/5653/files/2020/06/FlipGraphPerfectMatchings.pdf),
whose introduction cited Jennings; the cited Jennings original was then
opened and read. The conclusion is an author **value judgment after exact
mechanism subtraction**, not a comprehensive novelty-clearance verdict.

## Actual old-original boundary

The [old M01 uncrossing report](../../../papers147_151_sequence/scouting/combinatorial/SCOUT.md)
was read in its substantive M01 section (lines 60–175). Its literal picks a
lexicographically first crossing and turns it into a nesting, with an
inversion clock and opener invariance. GBPR is not that literal: for
$n\ge2$ it has one terminal matching, while the old map fixes multiple
noncrossing matchings.
This establishes only a direct-rule distinction, not portfolio value.

The complete [old matching/incidence SCOUT](../../../papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md)
was read through EOF. Its M01 is $M\mapsto MFM$ and is reduced to permutation
powers; its M02–M04 are Hurwitz/component-retraction rules. GBPR is not
identified with those maps merely because it uses matching overlays.

Narrow actual text searches also inspected the relevant matching/particle
contexts in three P204–P208 scout files and the P197–P201 matching ledger.
The six whole-file pins in [INPUTS.sha256](INPUTS.sha256) identify this local
search boundary; only the recorded excerpts were read for the four
search-only inputs. No global all-history absence claim is made.

## Evidence and boundary

[NATIVE_READS.json](NATIVE_READS.json) contains six actual command returns,
including the complete old matching SCOUT read, the substantive old M01
read, two narrow searches, the six hashes, and the pre-write nonexistence
check. [SOURCES_NATIVE.json](SOURCES_NATIVE.json) retains nine actual web
returns: eleven search queries in five calls, primary opens and follow-up
find/open calls. Requests in that wrapper are transcribed from the actual
calls; their result strings are preserved unchanged. Search snippets are
discovery evidence only. No raw PDF-byte snapshot is claimed.

Two primary opens returned `Internal Error`: the `www` Hoefer PDF URL and
the ScienceDirect article URL. The non-`www` author-hosted PDF opened
successfully and supplied the model body. These failures remain in the
source record. An attempted metadata display applied `Object.keys` to web
result strings and produced a truncated, irrelevant character-index list;
it neither changed the source strings nor generated scientific evidence.
Some combined tool displays were truncated; retained per-call returns are
the evidence, and no hidden portion is represented as a fresh read.

Both raw comparisons of freshly rerun multi-file `rg` outputs against their
saved returns failed because the output ordering differed. Those failures
remain in `CHECKS_NATIVE.json`; comparing the two complete outputs after
bytewise line sorting then passed. This is **sorted-line content equality,
not raw-output equality**. The full old SCOUT read and substantive old M01
read each passed actual raw byte comparison. All six old whole-file hashes
were unchanged. No failed raw check was overwritten or upgraded to PASS.

Only this new directory was written. No children, P211/A evidence, older
manuscripts, scripts, previous sealed desks, central indices, Git, external
uploads or specialist contacts were changed. `HOLD_EXTERNAL` remains.
The proof-writer skill supplied the explicit assumption/dependency/boundary
structure; the project skill kept author proof, source subtraction and
independent acceptance separate. There is no second literal because the
first already closes at the no-promotion gate, not because a small pilot
failed to meet a count quota.

Root can inspect the source-specific reduction and inverse bijection
directly; no pilot is requested for this rejected candidate. Document/pin
checks in [CHECKS_NATIVE.json](CHECKS_NATIVE.json) and the nonself manifest
are artifact checks only, never mathematical or review PASS.
