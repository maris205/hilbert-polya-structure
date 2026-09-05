# P201 complete theorem contract and proof map

Full all-parameter proofs appear in [main.tex](main.tex), preserved in [round0_frozen/main.tex](round0_frozen/main.tex). The pre-paper accepted proof package is [THEOREM_CONTRACT_AND_PROOF.md](../../docs/papers197_201_sequence/scouting/fifth_fresh_20260905/period_feedback_reentry/THEOREM_CONTRACT_AND_PROOF.md). This record states the full obligations and explicitly identifies equality, boundary and strictness arguments.

## 1. Literal carrier and rank cost

For n≥1 use every function f:{0,...,n−1}→{0,...,n−1}; let P(f)(i)=ell_f(i)−1, where ell_f(i) is the eventual cycle length reached from i. This is simultaneous and autonomous. Each cycle length is at most n, so it is a self-map. Rank r(f)=|im f|.

Let L(f) be the set of distinct cycle lengths and Q(s)=s(s+1)/2. Lemma 2.1 proves r(Pf)=|L(f)| and r(f)≥sum_(d in L(f))d≥Q(r(Pf)). Select one disjoint cycle of each distinct length; each selected vertex is an original image vertex. Distinct positive lengths give the triangular sum.

If output rank is at least two it is strictly smaller than input rank. A rank-one output is constant and its next output is zero. Proposition 2.2 therefore proves every orbit reaches zero and zero is the only recurrent/fixed state. Height h(f) is its first zero time. For n=1 the unique state has height zero.

## 2. Core extension, including the boundary

If g maps all n labels into the first k and u is its restriction to those k, every cycle is in the core. Feedback still maps into the core and restricts to P_k u. Inductively this holds at every epoch. At any epoch feedback is zero iff all cycles are loops, a condition shared by g and u. Thus at every positive time the full feedback vector is zero iff its restriction is zero.

Lemma 2.3 concludes h(g)=h(u) whenever h(u)≥1. If u=zero, h(g) is zero for g=zero and one otherwise. This explicit exception prevents an incorrect time-zero claim for nonzero leaf extensions of a zero core.

## 3. Sharp all-rank hierarchy

Set N_2=2 and N_(h+1)=Q(N_h). Rank-one functions have height at most one. If a function has height at least h+1 then its output has height at least h; induction plus packing gives r(f)≥Q(N_h)=N_(h+1).

For attainment start from the transposition on two labels, of height two. From a height-h permutation u on k=N_h labels, build blocks B_j consisting of its unique old inverse image u^−1(j) and j fresh labels. These partition Q(k) labels. Put a single cycle on each block. The resulting permutation's feedback is j on B_j and restricts on the old labels to u. Core extension gives height h+1. This proves every threshold, not just finitely many tested values.

For each r≥2 choose k=N_H(r)≤r, extend its critical permutation by fixed points to r labels, and then extend by leaves mapping to zero to any n≥r. The first extension's feedback has the same core and zero outside, hence the same positive height; the second preserves rank r and height. Thus the exact rank-r maximum is H(r)=max{h≥2:N_h≤r}; H(1 carrier)=0. Rank-one maximum is one whenever n≥2, achieved by a nonzero constant, and zero at n=1. These are Theorem 3.1's all-size and all-rank statements.

## 4. Full critical-size equality, not arbitrary-size equality

At n=N_h, height h forces full rank, hence a permutation. For h≥3 let k=N_(h−1). The chain
N_h=r(f)≥sum_(d in L(f))d≥Q(r(Pf))≥Q(k)=N_h
has equality throughout. Strict monotonicity forces r(Pf)=k, the distinct-positive sum forces lengths exactly 1,...,k, and the first equality forces their selected cycles to exhaust all vertices. Thus there is exactly one cycle of each length and no duplicate or additional cycle.

Feedback maps into the first k labels. Its core has height h−1 by the core-extension lemma and full rank by the hierarchy, so that core is a deepest permutation. Conversely exactly those cycle lengths and such a deepest core force feedback height h−1 and input height h. This proves Theorem 4.1's necessity and sufficiency.

For each eligible core u, the unique old inverse image u^−1(j) must sit in the cycle block of length j+1. Allocate the N_h−k new labels with j in each block: (N_h−k)!/product j! choices. Cyclic orders contribute product j!, canceling the denominator. Every extremizer is covered by the equality characterization, so D_h=D_(h−1)(N_h−k)!. D_2=1; D_3=1, D_4=6, D_5=6·15!. No equality classification away from critical sizes is claimed.

## 5. Independent inverse atlas and classical input

For target g put B_j=g^−1(j), k_j=|B_j|. An f arrow preserves eventual cycle, so Pf=g implies f(B_j)⊆B_j and every cycle of f on B_j has length j+1. Conversely those conditions give Pf=g. Hence restrictions to different blocks are independent and
|P^−1(g)|=product_j a_(j+1)(k_j).

Here a_d(0)=1 and, for k>0,
a_d(k)=sum_(c=1..floor(k/d)) k!/((k−dc)! d^c c!) R(k,dc),
where R(k,s)=s k^(k−s−1) for s<k and R(k,k)=1. Choose cyclic labels, disjoint d-cycles, and an attached forest. The manuscript includes a prescribed-root Prüfer-code proof of R: remove the least nonroot leaf and record its parent; the last record is a root. Conversely each sequence of k−s labels ending in a root decodes by the least remaining nonroot absent from its suffix, so there are s k^(k−s−1) codes. The k=s boundary has one forest.

Equivalently sum a_d(k)z^k/k!=exp(T(z)^d/d), T=z exp(T). These forest/cycle formulas are classical and explicitly receive zero independent credit.

A nonempty block is feasible iff k_j≥j+1: one cycle plus attached leaves suffices and a cycle needs that many vertices. Theorem 5.1 therefore gives all zero and nonzero fibres. Summing n!/product k_j! over feasible block-size vectors gives the first image. This theorem does not require the height hierarchy.

## 6. Unique maximal fibre, all strictness cases

Connected k-label functions with sole d-cycle have c_d(k)=(k)_d k^(k−d−1) for k≥d; at k=d it means (d−1)!. Compare c_1(k)=k^(k−1). Their ratio is (k)_d/k^d, strictly below one for d≥2; below d the d-class is empty. Nonnegative coefficientwise products and the SET exponential give a_d(k)≤a_1(k), strictly for every admissible nonempty d≥2 block, already from the connected term.

A product of rooted-forest counts on two or more fixed nonempty blocks is strictly below the count on their union: disjoint union is injective, but a forest with an edge crossing two blocks is excluded. Equality in the target product can therefore hold only for a single nonempty d=1 block, precisely target zero. Its rooted forests correspond bijectively to trees on n+1 labels by adding a new vertex joined to all roots. Cayley gives (n+1)^(n−1). Unsupported targets have zero fibres; at n=1 the sole target is zero. This completes Theorem 5.2.

## 7. Verification and claim ceiling

Full source boxes n≤7; independently orbit-traced update on all n≤6 plus the first 256 sources at n=7; every target including absent n≤6; critical equality at n=2,3,6; recursive witnesses at n=2,3,6,21,231,26796 and leaf padding. Paper-local assertion count: 3,366,093. These controls do not prove all-n statements.

Packing is an inequality, not a scalar closed rank evolution law. No closed height for each individual function, no full noncritical extremizer atlas and no all-time inverse are asserted. The same-histogram pair (0,1,1)/(1,0,1) refutes only histogram factorization, not the historical statistic-writeback filter or external ownership. The known triangular sequence and static counts remain attributed.

