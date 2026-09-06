# SI: singleton-preimage reversal — proofs and the P167 adapter

Proof author: `/root/batch197_lzk_gate`, 2026-09-05.
Status: deductive candidate package; OWNER_AMBER / VALUE_GATE_PENDING.
No independent review, accepted paper, or formal paper number is claimed.

## Literal map and assumptions

For every integer n>=1 use the full carrier X_n=[n]^[n], with
[n]={0,...,n-1}. Define

    S(f)(v) = u, if f^{-1}(v)={u};
              v, if |f^{-1}(v)| is 0 or at least 2.             (SI.1)

The identity default for a multiple fibre is essential. This is not a
choice of one element from every nonempty kernel class. No order on
labels is used; S commutes with every simultaneous relabelling.

## Exact temporal theorem

Every first image is a disjoint union of directed cycles and loop-rooted
directed paths. On a nontrivial path in root-to-leaf order
(p_0,...,p_{s-1}), one update fixes p_0 and reverses the remaining path:

    (p_0,...,p_{s-1}) -> (p_0) + (p_{s-1},...,p_1).            (SI.2)

Cycles invert. Hence the recurrent set is exactly the n! permutations,
and S acts there as permutation inversion. Its fixed count is

    I_n = sum_{j=0}^{floor(n/2)} n!/(2^j j! (n-2j)!),

and the strict 2-cycle count is (n!-I_n)/2. There are no other periods.
The sharp full-carrier height is n-1. The sharp first-image height is
max(n-2,0). For n>=3 the deepest full-carrier layer has exactly 2 n!
states; its sizes at n=1,2 are respectively 1 at depth 0 and 2 at depth 1.

Proof. If g=S(f) and g(v)!=v, then f(g(v))=v and that preimage is unique.
Two distinct nonfixed v cannot have the same g(v). Consequently every
vertex has at most one incoming **nonloop** arrow. A cycle of length at
least two can have no attached vertex, and each loop can have at most one
incoming chain. This is the stated component classification.

On a path, the root p_0 has two preimages p_0,p_1 and is therefore sent
to itself. Each p_j with 1<=j<=s-2 has unique preimage p_{j+1}; the leaf
p_{s-1} has no preimage and becomes the new root. This proves (SI.2).
Each such step removes exactly one path edge. Cycles have exactly one
preimage at every vertex, so all their arrows reverse. Components cannot
merge. Thus a map in the path/cycle class has exact tail equal to its
largest path size minus one, with value 0 when no nontrivial path exists.
All recurrent states are permutations, since a nontrivial path cannot
return. Conversely every permutation is periodic under inversion.

A first image cannot be a single n-vertex nontrivial path. If its
root-to-leaf list is (p_0,...,p_{n-1}), the nonloop edges force
f(p_{j-1})=p_j, uniquely over p_j, for 1<=j<=n-1. The remaining source
p_{n-1} cannot map to any p_j with j>=1 without violating uniqueness.
If it maps to p_0, the unique preimage of p_0 is p_{n-1}, contradicting
the root loop. Hence a first-image path has at most n-1 vertices.
This gives full height <=n-1. An arbitrary full-label path itself is
in X_n and has tail n-1 by (SI.2), proving sharpness. Its first image
has a path of size n-1, proving the sharp image height for n>=2.

The formulas for inversion-fixed permutations and strict 2-cycles are
the classical involution count and division by two. For the deepest layer
at n>=3, the first image must consist of one path on n-1 vertices and one
isolated loop. There are n(n-1)!=n! such targets, and each has exactly two
predecessors by the fibre theorem below, N(2,1)=2. Each of those sources
has tail 1+(n-2)=n-1. The n=1,2 cases follow directly from (SI.1). QED.

More pointwise, for nonpermutation f,

    tail(f)=1+max{path-edge count in S(f)}.                      (SI.3)

The nontrivial cycles surviving forever are precisely the original
components which were pure directed cycles, with no attached vertices.
On such a component S^t(f)=f^{(-1)^t}; all other vertices become fixed.
Indeed a nontrivial cycle in S(f) forces a reversed original cycle whose
vertices all had indegree one, hence a whole original component. No later
step can create a cycle from a path. This is a structural statement, not
ordinary composition-power iteration of f.

## Every-target inverse atlas: forbidden-singleton occupancy

For an arbitrary target g put

    U={v:g(v)!=v}, V=g(U), L=[n]\U, D=[n]\V.

If the values g(v), v in U, repeat, the fibre is empty. Otherwise set

    k=|L|=|D|, p=|L intersect V|.

Here k is the number of loop-rooted path components, including isolated
loops, and p is the number of nontrivial path components. Let

    A_m = sum_{b=0}^{floor(m/2)} {m brace b}_{>=2} (m)_b,
    N(k,p)=sum_{s=0}^{k-p} binom(k-p,s) A_{k-s}.                (SI.4)

The associated Stirling number in (SI.4) counts partitions into b blocks
of size at least two, and (m)_b=m!/(m-b)!. Empty structures have count 1.
Then

    |S^{-1}(g)| = N(k,p).                                     (SI.5)

Proof and decoder. For each v in U the equation f(g(v))=v is forced,
and v must have no second preimage. These equations define f on V and
are inconsistent if the forced source positions repeat. All free source
positions lie in D; they must map to L. For a target label v in L, the
free fibre is allowed to have size zero or at least two, or to be the
singleton {v}. The last possibility exists only for v in D intersect L,
of which there are k-p. Conversely any free assignment satisfying these
conditions, together with the forced assignments, yields S(f)=g.

Select the s labels whose free fibres are their self singletons, in
binom(k-p,s) ways. Partition the remaining k-s sources into b blocks,
each of size at least two. Assign the blocks injectively to the remaining
k-s target labels, in (k-s)_b ways. This constructs each admissible free
assignment exactly once and proves (SI.4)-(SI.5). Notice that the free
assignments are independent of all path lengths, path label orders and
nontrivial cycle lengths; they are not a backwards path-peeling code.
QED.

An inclusion-exclusion formula, used by the author pilot rather than
imported from the proof, provides an alternate check:

    N(k,p) = sum_{j=0}^k (-1)^j (k-j)^{k-j}
      sum_{h=max(0,j-p)}^{min(j,k-p)} binom(k-p,h) binom(p,j-h)
        sum_{a=0}^h (-1)^a binom(h,a) (k-a)_{j-a}.             (SI.6)

Select j forbidden singleton target events, h of them with matched
self-labels. The innermost sum counts injections of these target events
to distinct source labels avoiding those h self-matches. All remaining
sources can map to any of the k-j unselected targets. This proves (SI.6).

### Image support, maximum, and a closed image census

For a target with distinct off-diagonal values, N(k,p)>0 except when
(k,p)=(1,1). At k=0, or k=1,p=0, the forced/self assignments give one
source. If k>=2, assigning all k free sources to one fixed target gives
a permitted nonsingleton fibre. If k=p=1, the sole free source is not
the sole fixed target, so its singleton is forbidden.

For every n the identity is the unique maximizing target and its fibre
equals N(n,0). The first values, n=1,...,5, are 1,3,10,65,456.
Proof. From (SI.4), N(k,p)<=N(k,0). The latter increases strictly from
k to k+1 for k>=1: extend every admissible map by a new self-fixed label,
and observe that the constant map to the new label is an additional
admissible map. For n>=2, g!=id has k<n and therefore
N(k,p)<=N(k,0)<N(n,0); k=0 has count 1 and causes no exception.
The singleton carrier is immediate. QED.

The first-image cardinalities have exponential generating function

    sum_{n>=0} |im S_n| z^n/n!
      = exp(z^2/(1-z))/(1-z) - z^2 exp(-z)/(1-z)^2.            (SI.7)

For this one formula S_0 is the empty map. Directed cycles of length at
least two contribute sum_{j>=2} z^j/j, and ordered loop-rooted paths of
size j>=1 contribute sum_{j>=1} z^j. Their labelled-set EGF is the first
term. The excluded k=p=1 structures consist of exactly one path of size
at least two and arbitrary nontrivial cycles, yielding the second term.
All labelled-species and associated-Stirling machinery is owned background.

## Exact adapter to P167, and obstructions to overclaiming it

P167's M(f)(v) selects the minimum of every nonempty preimage and defaults
to v only for an empty preimage. Its first-image proof establishes the
same distinct-off-diagonal-values lemma and therefore exactly the same
ambient class of cycles and loop-rooted paths. That lemma transfers to
SI without a new proof mechanism and is assigned zero contribution credit.

On a loop-rooted path P=(p_0,...,p_{s-1}), P167 has two branches:

    p_0<p_1: split p_0 and reverse the rest;
    p_0>p_1: reverse the whole path.

SI always takes the first branch, regardless of the labels. Therefore
SI's entire path action is the **unconditional split branch already
present in P167**. Height n-1 and the absence of recurrent nontrivial
paths are immediate consequences of that branch choice. This is a
specific proof adapter, not a vague claim that all peeling is old.

It would nevertheless be false to claim literal equality, conjugacy, or
that SI is a fixed iterate of P167:

- At n=2, SI has height 1 and P167 has height 2, obstructing a functional
  graph conjugacy. At n=3 their recurrent counts are respectively 6 and 8.
- Let g=(2,0,2), the path with root-to-leaf order (2,0,1). P167 alternates
  g with (1,1,0), while SI(g)=(1,1,2) and SI^2(g)=id. Thus SI(g) is not
  M^r(g) for any r>=0.
- P167 always satisfies f M(f) f=f. SI does not: for f=(1,0,1),
  S(f)=(1,1,2) and (f S(f) f)(0)=0 != f(0)=1. Thus inverse-matching
  results requiring a generalized inverse do not directly identify SI.

The inverse constructions also differ concretely. P167 forces **first**
occurrences and counts legal later letters by order inequalities; fixing
the source kernel partition then determines at most one source, yielding
its Bell bound. SI forces **unique** occurrences and allows all remaining
labels only in the fixed-target set, subject to forbidden-singleton
occupancy. Its identity fibre already has 10 sources at n=3, exceeding
Bell(3)=5, so P167's kernel-to-source injection cannot transfer.
Formula (SI.4) is a different target-local construction from that injection,
but associated-Stirling occupancy itself receives zero credit.

### Value ceiling after subtraction

The common first-image classification and the entire unconditional
path-splitting temporal engine are transferred from P167 and have zero
independent mechanism credit. The remaining mathematical difference is
the singleton-occupancy atlas and its attachment to the full selector.
That is a complete inverse theorem, but this author has **not** shown
that it supplies a materially new temporal axis as well. Hence the
package must not be promoted solely on the strength of the small-box
PASS, different numeric counts, or failure of literal conjugacy.
Independent gate should decide whether any irreducible two-axis residual
survives; otherwise recommend NO_PROMOTION rather than enlarging n.
