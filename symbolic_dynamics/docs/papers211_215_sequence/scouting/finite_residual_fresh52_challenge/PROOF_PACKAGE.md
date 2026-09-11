# Diameter coarsening: a linear-time cascade

Author/proof-contributor challenge, 2026-09-11. This agent is not eligible to serve as a nonauthor manuscript reviewer for a paper using this construction. No scientific code or pilot was executed. Only this challenge directory is changed; no author-desk, central-state, count or Git change is made.

## Claim

Let $D$ act on set partitions of the ordered set $[n]$ by simultaneously merging all blocks with the same diameter, where $\delta(B)=\max B-\min B$. Singleton diameter is zero. Let $h(\pi)$ be the least nonnegative time at which the iterated partition is fixed.

For every integer $m\ge1$, there is a partition of $[5m+5]$ with

$$h(\pi)=2m.$$

Consequently the worst-case convergence time is $\Theta(n)$, not $O(\sqrt n)$. In particular, a longest collision lineage does not force quadratic growth of its span.

## Status and assumptions

**PROVABLE AS STATED** for the displayed counterexample theorem. The proposed square-root universal upper bound is false. The map acts on arbitrary set partitions, not just partitions into interval blocks. This definition was confirmed with the fresh52 author.

## Strategy and dependency map

1. Construct disjoint endpoint pairs for one active block and its successive partners.
2. Fill unused integer points without changing any endpoint or diameter.
3. Check the complete list of initial diameters, ensuring exactly one merger per round.
4. Add harmless padding for arbitrary larger ground-set sizes; combine with the block-count upper bound.

The collision partner alternates a rightward shift by two with a leftward shift by three. Their different residue classes prevent endpoint reuse.

## Proof

### 1. Endpoint skeleton

Work first on the consecutive integer set

$$I_m=\{-3m,-3m+1,\ldots,4+2m\},\qquad |I_m|=5m+5.$$

Take the initial endpoint sets

$$A=\{0,4\},$$
$$P_k=\{2-3k,6+2k\},\qquad Q_k=\{-3k-3,3+2k\},\qquad 0\le k<m.$$

They are pairwise disjoint. Indeed, the left endpoints of the $P_k$ are at most two and congruent to two modulo three. The left endpoints of the $Q_k$ are negative multiples of three, and the remaining left endpoint is zero. Thus no two left endpoints coincide. The right endpoints of the $P_k$ are even and at least six; those of the $Q_k$ are odd and at least three; the remaining right endpoint is four. Thus no two right endpoints coincide. Every left endpoint is at most two and every right endpoint is at least three, excluding cross-collisions as well. All endpoints lie in $I_m$.

### 2. Filling the ground set

The skeleton need not yet cover $I_m$. Preserve every existing endpoint in its designated block. For each integer not in any endpoint set, put it into $Q_{m-1}$ if it is at most $2m+1$, and into $P_{m-1}$ otherwise.

This preserves their endpoints: the hull of $Q_{m-1}$ is $[-3m,2m+1]$, while the hull of $P_{m-1}$ is $[5-3m,4+2m]$. Since $m\ge1$, $5-3m\le2m+1$. A point assigned by the stated rule lies inside the receiving hull. The resulting sets, still denoted $A,P_k,Q_k$, therefore form a partition of all of $I_m$, without any singleton padding. Their diameters are

$$\delta(A)=4,\qquad \delta(P_k)=4+5k,\qquad \delta(Q_k)=6+5k.$$

Among these values, only $\delta(A)=\delta(P_0)$ repeats. Within each partner sequence the values strictly increase; the two sequences have different residues modulo five.

### 3. Exact orbit

For $0\le k\le m$, define the active block after the first $2k$ rounds as the union

$$U_k=A\cup\bigcup_{0\le j<k}(P_j\cup Q_j).$$

Its hull is

$$[-3k,4+2k],\qquad \delta(U_k)=4+5k.$$

For $k=0$ this follows from the definition of $A$. Suppose $k<m$ and the state consists of $U_k$ and all unconsumed partners $P_j,Q_j$ for $j\ge k$. The sole repeated diameter is that of $U_k$ and $P_k$: all later $P_j$ have larger diameters, all $Q_j$ have the other residue modulo five, and the partner diameters are pairwise distinct. Thus the next round merges exactly $U_k$ and $P_k$. Their union has hull

$$[-3k,6+2k],\qquad \text{diameter }6+5k.$$

At that state its unique matching partner is $Q_k$. The next round merges exactly those two blocks, producing hull

$$[-3k-3,6+2k]=[-3(k+1),4+2(k+1)].$$

This proves the induction statement for $U_{k+1}$. Added interior points from Step 2 cannot change any of these hulls, because each lies within its own partner's hull.

There is one nontrivial merger at each of rounds $1,\ldots,2m$. At time $2m$ there is just one block, namely $I_m$, so the state is fixed. Before then, the next displayed partner forces a merger. Hence $h=2m$ exactly. Translating each label by $3m+1$ identifies $I_m$ with $[5m+5]$ and preserves all diameters, completing the construction.

### 4. Worst-case order for every sufficiently large size

For any $n\ge10$, set $m=\lfloor(n-5)/5\rfloor\ge1$ and $N=5m+5$. Use the construction on $[N]$. If $r=n-N$ is positive, add the single block $\{N+1,\ldots,n\}$, of diameter $r-1\in\{0,1,2,3\}$. Every block diameter occurring in the cascade is at least four, so this added block never participates in a merger. The convergence time remains $2m$.

Therefore, with $H(n)$ denoting the maximum convergence time over partitions of $[n]$,

$$H(n)\ge2\left\lfloor\frac{n-5}{5}\right\rfloor\qquad(n\ge10).$$

Every nonfixed application strictly decreases the number of blocks, and every partition of a nonempty $[n]$ has between one and $n$ blocks. Thus $H(n)\le n-1$ for $n\ge1$. For $n=0$, the empty partition is fixed. These bounds prove the stated linear worst-case order. No sharp leading constant is claimed.

## Local cardinality-collision boundary

The complete actual old files `docs/papers147_151_sequence/scouting/root/SCOUT.md` and `docs/papers147_151_sequence/phase1/OWNER_AUDIT_EQC.md` were read. EQC merges equal-cardinality blocks and factors through the multiset of block sizes; the old author report gives a logarithmic clock and a powers-of-two cascade. The owner audit's disposition is `KILL_UNRESOLVED_DIRECT_OWNER`, not source clearance.

The construction here does not import that clock. In the present map, an equal-diameter partner can be a widely overlapping interval hull with a different point set; its union increases diameter by only two or three. In particular, along the explicit lineage, the span after $2k$ rounds is $4+5k$. Equal-diameter merging is not equal-cardinality doubling. The old report alone neither owns this construction nor clears it against external literature.

## Corrections, risks and scope

- The quadratic-span inference is refuted under the confirmed full-Bell-set definition. A theorem restricted to interval blocks would be a different claim and is not assessed here.
- The proof supplies a temporal lower-bound mechanism, not an all-target inverse, novelty clearance, admission decision or complete manuscript contract.
- No external source is invoked for the construction. No broad rescan, scientific execution, independent verifier result or runtime PASS is asserted.
- The proof-writer skill supplied the explicit claim/assumptions/dependency and boundary checks. This is disclosed author work; any eventual manuscript must use other agents for its nonauthor review gates.
