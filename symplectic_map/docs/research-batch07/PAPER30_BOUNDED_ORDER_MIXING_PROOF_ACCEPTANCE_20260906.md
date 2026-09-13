# Bounded-order Hénon mixing: completed mathematical stage

Date: 2026-09-06. Status: `PROOF_STAGE_COMPLETE; CANDIDATE_SELECTION_PENDING`.
This is not a manuscript, local paper acceptance, Route PASS or page measurement.

## Exact result accepted at the mathematical stage

For every fixed $d\geq2$, every prime $p\geq16d^2$, every monic polynomial
$P\in\mathbb F_p[t]$ of degree $d$, and every $1\leq m\leq d+1$, the same
lazy symmetric random word in
$H_{P,j}(x,y)=(P(x)+j-y,x)$, $j=0,1$, has a common gap depending only on
$d$ on ordered distinct $m$-point configurations. The prescribed law is
one half identity and one eighth on each of the four Hénon/inverse maps.
The theorem includes all lower coefficients and the whole allowed range
of point orders simultaneously. Fixed-accuracy mixing is logarithmic in $p$.

The new proof combines a uniform polynomial-shear realization in a relative
affine/Hénon alphabet, polynomial evaluation, an auxiliary pointwise
minorisation, and the already checked affine energy comparison. It does not
pretend that all affine maps have constant length in the original four letters.

## Completed independent checks and input bindings

Root has fully read the following reports and accepted their actual conclusions:

- [Original affine-chain/three-point audit](PAPER30_THREE_POINT_AFFINE_CHAIN_INDEPENDENT_CHECK_20260906.md):
  343 lines, SHA256 `1f471faad2485966c22bb8477ea47fc375d0f9ddb550672329e6ca74832d9bb1`.
  The original full three-point theorem is PROVABLE AS STATED. The only
  issue is the Wan–Wang bibliographic `of`/`with` typo, not mathematics.
  Original author file remains frozen at SHA256
  `1b2e03a56164f62d02fa8e11ed63b8169105be3a831d0148c3fd72b1896398ba`.
- [Bounded-shear complete derivation](PAPER30_BOUNDED_POLYNOMIAL_SHEAR_PROBE_20260906.md):
  253 lines, SHA256 `cd49ecdd80d9ef2694cf3305ea628a43f6a6023c5f4fd88eabd5bd0a2acc3ed5`.
  It proves the explicit relative-length bound $12\,2^d-4d-11$ for every
  polynomial shear of degree at most $d$, already for every prime $p>d$.
- [New higher-order audit](PAPER30_BOUNDED_ORDER_MIXING_INDEPENDENT_CHECK_20260906.md):
  356 lines, SHA256 `932bb59d553b6e555f343a0bba5d1969bae5958de58a08de862ae45be06774e0`.
  It fully checks the shear input and the 343-line
  [interpolation author proof](PAPER30_INTERPOLATION_MINORISATION_PROOF_20260906.md),
  SHA256 `0f0e3b0a00a51a6165d3795efb1ab028118ca94067bc79df27f7d95bfcee8956`.
  No new formula, field, threshold, coefficient or point-order repair is needed.
  It reuses the unchanged arbitrary-representation affine interface, without
  reopening BG/LV or the now-unneeded old three-point quotient argument.

The actual new audit checks every source and target configuration, the
independence after conditioning, non-reversible real energy, both interpolation
endpoints, and the exact denominator
$(2B_d+4)^2(4C_d/\gamma_d+8)$. There is no remaining OPEN obligation in
the stated mathematical theorem, while all out-of-scope cases remain unclaimed.

## Attribution and selection are separate

Root has fully read the three bounded prior reports, including the final
[Naor–Reingold supplement](PAPER30_BOUNDED_ORDER_MIXING_PRIOR_SUPPLEMENT_20260906.md),
178 lines, SHA256 `01d4e12be47a9e4016cc9617030b0bdd0781094c2da8161ff9522db53eceb658`.
Root also directly read the published Naor–Reingold Definition 3.5,
Proposition 3.4, Lemma 3.5 and Corollary 8.1. The outer randomization,
good-event and exact conditional-mass method has a strong direct precedent;
the old source cannot be dismissed as only a TV estimate. The candidate
brief deducts it explicitly, alongside the affine and additive-combinatorial
tools. No direct complete covering theorem was located in the bounded search;
that fact alone is not a novelty PASS.

The [same complete candidate brief](PAPER30_BOUNDED_ORDER_MIXING_CANDIDATE_BRIEF_20260906.md)
is frozen at 315 lines, SHA256
`2d3533e627c68f92e14f824b19d16ac4e8b759898213328ca0d0f4744f8f8382`.
Two fresh mutually blind reviewers, `p30_bounded_order_candidate_r1` and
`p30_bounded_order_candidate_r2`, are evaluating its identical eight full
inputs with disjoint report ownership. Neither is an author or previous
mathematical checker of this result. They use the actual available secondary
review mechanism; no unavailable GPT-5.4 MCP or human review is claimed.

The four locked gates remain novelty at least 7.5, stand-alone value at least
7.5, complete-proof confidence at least 9, and credible natural 22–30-page
substantive English body. Both complete reports must pass all four. The
old area/Jacobi/Weil route is retained but cannot supply duplicate body capacity.
Paper29's special one-time natural-draft permission does not apply here.

Batch07 remains 3/5 locally accepted. Paper30 is not selected, Paper31 has
not begun, and no manuscript, publication lock, build or external action
has been performed for this candidate.
