# P198 complete proof obligations and location map

The all-parameter proofs are written in [main.tex](main.tex), with their frozen original in [round0_frozen/main.tex](round0_frozen/main.tex). This package restates the contract and highlights the necessity/sufficiency and boundary arguments. It does not replace proof by finite enumeration.

## Carrier and rule

Fix n=2m+1 at least 3, vertices 0,...,n−1 and edges e_i={i,i+1 mod n}. The state is any matching. At least three monomers: flip the clockwise arc from the ordinary least monomer a to its next clockwise monomer b. Exactly one monomer a: flip e_a and e_(a+1). No externally supplied schedule or time counter is present.

## Closure (Lemma 2.1)

No interior vertex of a consecutive-monomer arc can be matched outside the arc, because the endpoints are unmatched. Hence the pattern alternates 0,1,...,0; its reversal is a matching and gains one edge. Deleting a unique monomer leaves a uniquely tiled even path, so e_a is absent, e_(a+1) present and the two-edge flip moves the monomer by two. This covers the wrap case.

## Temporal axis (Theorem 3.1 and Corollary 3.2)

Strict rank increase precludes recurrence below rank m, and reaches rank m after exactly m−|M| steps. There is one maximum matching for each monomer label. Since gcd(2,n)=1, their monomer advance gives one n-cycle, no fixed points, and no further recurrent states. Only the empty matching has tail m.

The depth coefficient at rank r is the classical cycle-matching count. Splitting on the wrap edge gives binom(n−r,r)+binom(n−r−1,r−1), with the second term zero at r=0. This equals n/(n−r) binom(n−r,r). The manuscript proves the path count by subtracting successive offsets from the selected nonadjacent edge indices. This is attributed background applied to the proved clock.

## Independent inverse axis (Theorem 4.1)

Let u be the target's least monomer and r=floor(u/2). If u is even, backward forcing from u−1 gives internal dimers e_0,e_2,...,e_(u−2). If u is odd, it gives e_1,e_3,...,e_(u−2), plus the forced wrap edge e_(n−1). That wrap edge is not one of the r reversible internal dimers.

Necessity: a transient source has at least three monomers, so its first two satisfy a<b with no wrap. The update removes exactly these monomers. All surviving monomers are larger than b, giving a<b<u. The target arc is therefore a nonempty consecutive interval of the forced internal dimers.

Sufficiency: reverse any such interval. Its two endpoints become unmatched and lie below every old target monomer. They are precisely the first two source monomers; hence the scheduler selects the same interval. Distinct intervals give distinct endpoint pairs and distinct sources. There are r(r+1)/2 intervals. A maximum target also has the one rotor predecessor with monomer u−2 modulo n. It has a different rank from every transient predecessor, so the two contributions are disjoint. The result is
|F^−1(Y)|=r(r+1)/2+1_(|Y|=m).

## Extremality and first image (Corollaries 4.2 and 5.1)

For a nonmaximum target support is equivalent to u≥2; all maximum targets have a rotor predecessor. The largest possible r is m, requiring u=2m and hence the unique maximum matching with that monomer. Every other target has r≤m−1. The unique largest fibre is 1+m(m+1)/2.

Count targets matching labels zero and one. If e_0 is present, the residual path contributes Fibonacci F_(n−1). Otherwise e_(n−1) and e_1 are both forced, contributing F_(n−3) for n≥5. At n=3 these two edges conflict and contribute zero=F_0; there is no appeal to a negative-length path. Add the two maximum targets with monomer zero or one. Thus the first image has F_(n−1)+F_(n−3)+2=L_(n−2)+2 states.

## Verification and ceiling

The complete-carrier verifier checks forward closure, an independently peeled functional graph, all target indegrees including zero, endpoint-set inverse reconstruction, every depth coefficient, the image and unique extremizer for every odd n from 3 through 21. The proof is all-parameter; these 237,845 assertions are bounded controls. No all-time inverse, arbitrary-graph extension, or external priority is claimed.

