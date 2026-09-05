# P199 Review A — independent word and block derivation

2026-09-05 UTC. Frozen Round0 only; exact inputs in PINNED_INPUTS.sha256.
This review did not author FOSP's candidate proof, Stage1 gate, or manuscript.
The Stage1 gate and paper share an author; they are not two independent
paper reviews. The present implementation shares no author modules.

## 1. Closure and the exact owned factor

Write w=A1B1C. A label j>1 cannot have its two copies separated by an
occurrence of 1, because that violates the defining strict inequality.
Consequently both copies belong to the same one of A,B,C. Removing both
ones and decreasing the other labels preserves every strict interval
inequality. The inserted maximum pair is adjacent; its gap is exposed,
because no interval could contain 1. Thus T is a self-map at every n.
At n=0 it is the stipulated identity.

The exact factor T=c J_1 follows directly, where J_1 moves the second 1
next to the first. This is a source-owner comparison, not new mathematics
attributed to this note. Relabelling alone is not a self-map: c(1221)=2112
at n=2. This counterexample does not by itself establish residual value.

## 2. Point clock without assuming a tree representation

For j>1, both occurrences lie within one compartment A,B,C. Removing the
ones cannot remove any symbol strictly between them, and inserting the
new pair cannot enter their interval. Hence their adjacency status is
unchanged before decrement. The old label 1 loses its interval, and the
new n-pair is adjacent. Therefore

    I(Tw) = {j-1 : j in I(w), j>1}.

After t steps the surviving nonadjacent labels are {j-t:j in I(w),j>t}.
The first doubled word occurs at d=max I(w), empty maximum zero. The
positive maximum decreases strictly, precluding any other recurrent
state. On a doubled word the pair slots do not move and each slot's
label undergoes the n-cycle c. Any returning slot forces n to divide the
elapsed time, so periods are exactly n for n>=2, not merely divisors.
There are n! such states and (n-1)! cycles. Orders zero and one each have
one fixed state. Since n is always adjacent, d<=n-1; the manuscript's
explicit (n-1) nn (n-1) witness with doubled lower prefix attains it,
including n=2. No maximum-tail assertion is made at n=0 beyond zero.

## 3. A different all-size derivation of the depth CDF

Fix 0<=t<=n-1. In a word of depth at most t, all labels t+1,...,n
are adjacent pairs. Delete these n-t pair blocks simultaneously. The
remaining word is an arbitrary order-t Stirling word, in (2t-1)!! ways.
Conversely, arrange the n-t distinct high-label blocks in any order and
distribute this ordered list into the 2t+1 gaps of the residual word.
No high-label interval may contain another block, while any low-label
interval accepts them. Thus this construction is bijective, including
empty gap lists and the t=0 empty core. Its number is

    (2t-1)!! (n-t)! binom(n+t,2t) = (n+t)!/(2^t t!).

This simultaneous block distribution independently checks the author's
successive protected-gap product. It is still classical gap enumeration,
not an additional claimed contribution. Exact levels are differences of
nested sublevels, with baseline F_n(-1)=0. In particular the top CDF
equals the whole carrier, not the top exact layer.

## 4. Full target inverse from all word gaps

Let a be the first position of the necessarily adjacent nn in a target y.
Any predecessor must delete this nn, increment all remaining symbols,
insert the first 1 at position a, then insert its second 1 at a later
character gap. These are all possible reconstructions before imposing
Stirling validity; this is the exhaustive search used by the verifier.

The first 1 is valid only if a is an exposed gap: a lower interval
containing it would contradict increasing labels. Thus n must be a root
leaf, not merely a leaf. When a is exposed, the second 1 must occur at
an exposed boundary after a complete sequence of subsequent root blocks.
Placing it inside any block splits a larger pair around 1 and is invalid.
If r complete root blocks follow nn, exactly r+1 boundaries remain. The
boundary is uniquely reconstructed from the second 1, proving both
completeness and distinctness. Every root-n target has the empty-block
choice, proving the image iff. Every other target has zero predecessors.

Since r+1<=n, equality forces all n vertices to be exposed single pairs
and nn to be first. Conversely each such target has n predecessors.
The equality census is exactly (n-1)!, including n=1; n=0 is separate.

## 5. Independent labelled convolution for the image

Every root-n target is uniquely P nn Q where P,Q are Stirling words on
complementary subsets of [n-1]. If q_m=(2m-1)!! and q_0=1, its count is

    sum_{a=0}^{n-1} binom(n-1,a) q_a q_{n-1-a}.

The exponential series of q_m is (1-2z)^(-1/2). Squaring it gives
(1-2z)^(-1); hence the convolution equals 2^(n-1)(n-1)!. This is an
independent check of the paper's root-degree differentiation. Direct
differentiation also checks the latter: the derivative of
z(z-1)R_m'(z)+(2m+1)R_m(z) at 1 is (2m+2)R_m'(1), with no missing
R_m(1) term. The verifier checks every coefficient of the proposed
root-gap recurrence against word-derived gap counts through n=7.

## 6. Finite pressure and independence boundaries

The sole verifier generates byte words by maximum-pair insertion, builds
the full successor graph, and extracts cycle lengths and tails by orbit
path discovery and reverse assignment, not author Kahn peeling. Every
target's entire predecessor set is compared with the all-character-gap
validity search. Word prefix parity signatures supply an additional
root-boundary control; no child-array construction is used.

All orders 0 through 7 cover 146,600 sources and the same number of targets.
Two fresh saved replays each pass 1,926,465 assertions with identical
bytes. Through n=5, all joins' idempotence/commutation and the unrolled
identity T^t=c^t J_t...J_1 for t<=n are explicit subtraction controls.
The graph computations never use the proposed clock to determine tails.
These finite boxes do not prove the all-order claims or external novelty.

Open mathematical findings: Critical 0, Major 0, Minor 0.
