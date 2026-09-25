# 370 — Independent full renewal-owner derivation

Candidate: **ANG-20260922-DRE01**. Scoped result: **owned renewal clock; composite primitive tests — STOP / FORK**.
The probability and all-point owner exist. The precommitted time target fails; no repair is made.

## 1. Inputs, authority and limits

I personally read candidate-card.md lines 1–112 through its then-current EOF, including the CP1 clarification.
SHA-256: `f4a1a914d117365671d88e946d75061d525b2065cf6080b88be22a3cc0cc7e8c`.
The original 100-line prefix hashes to `46e18a3aa59d3eebfc744cf858c4b5ca516327d93124281bf47e4cfa2b5a3b08`.
This card was the sole scientific file read. No manuscript, peer/scout proof, old proof or outcome was opened.
Applicable ARS instructions and broad prior context are retained; this is inherited-model, shared-history
internal work, **NOT_CALIBRATED**, not blind, external peer review or independent-error evidence.
Root released mathematics after its CP1 review. This report is independent derivation, not manuscript CP2/CP3.
No auxiliary, external source, scientific numerical experiment or model change was used. Only this file is written.

## 2. Divisibility produces a probability law with finite mean

Write L_0=L_1=1 and L_n=lcm(1,...,n). Finite intersections of the ideals mK equal L_n K;
this follows coordinatewise from their prime-adic valuations, without treating K as a field.
Consequently {b=d}=L_(d−1)K minus L_dK, and

\[
w_d=L_{d-1}^{-1}-L_d^{-1},\qquad S_r=L_r^{-1}\quad(r\ge0).
\]

The only jumps of L_d occur at d=p^a, a>=1, and then L_d=pL_(d−1). Thus D is exactly
the prime powers, derived from all divisor tests, and w_(p^a)=(p−1)/L_(p^a)>0.
The intersection of all nK is {0}; its Haar mass is zero since 1/L_n tends to zero.
Telescoping therefore gives sum w_d=1 and every S_r>0, including S_0=S_1=1.
For n>=1, the coprime integers 2^floor(log_2 n) and 3^floor(log_3 n) divide L_n.
Their product exceeds n^2/6. Hence sum 1/L_n converges by comparison with sum 6/n^2.
This proves 0<M<infinity exactly, with M=sum_d d w_d by nonnegative double summation.
For d=p^a put N_d=L_d/(p−1). Since p−1<=d divides L_d, N_d is an integer >=2 and w_d=1/N_d.

## 3. Entire source, measure, inverse branches and observation

The discrete product X=N_0×D^N is a standard Borel, metrizable, noncompact source.
Its entire future-gap space, including every periodic or unbounded gap sequence, is retained.
One construction of nu=product(w) recursively partitions [0,1) into half-open intervals of lengths w_d,
and each interval into the same relative proportions. Coding gives every finite-prefix cylinder its
product weight; prefix cylinders generate the Borel sigma-algebra. This defines the full probability law.
Every cylinder has positive mass, and a singleton has mass at most 2^(−n) for every prefix length n.
The sum of the residual masses S_r/M is one, so mu({r}×E)=(S_r/M)nu(E) is a full-support probability.
All individual states, and all eventually periodic gap histories, are mu-null but remain in X.

The prescribed T is continuous and total. Its two inverse charts are exactly
W(r,g)=(r+1,g), on all X, and E(r,g)=(0,(r+1,g)), when r+1 belongs to D.
Their images are respectively all positive-residual and all zero-residual states; they partition X.
Both are homeomorphisms between their clopen domains/images. Every target has its W predecessor;
it has its E predecessor precisely on the stated domain. Thus T is onto, with one or two preimages.
No residual infinity, infinite gap or never-renewing boundary is present.

The actual bit observation is
0^r 1 0^(g_1−1) 1 0^(g_2−1) 1 ... .
It is a homeomorphism onto the binary sequences with infinitely many ones whose successive one-distances
belong to D. It conjugates T to the left shift on that exact subspace. The first one determines r and
successive one-distances recover all gaps. Finite-one sequences and the all-zero limit are not states.

## 4. Every-Borel IMAGE, invariance and the actual all-point clock

For a Borel target E, partition it by residual r. The W-image has mass
sum_r S_(r+1)nu(E_r)/M. The E-image has mass sum_(r+1 in D) w_(r+1)nu(E_r)/M,
using the product prefix identity nu((d,C))=w_d nu(C), valid for every Borel C.
These are exactly the integrals of j_W=S_(r+1)/S_r and j_E=w_(r+1)/S_r against mu.
All declared branch derivatives are finite and strictly positive on their full domains.
With w_1=0 and w_d=0 off D, S_r=S_(r+1)+w_(r+1); summing the disjoint charts proves T_*mu=mu.
This is a full Borel identity, not only a check of total branch masses.
The formulas prescribe values also on null paths; a.e. Radon–Nikodym uniqueness alone would not do so.

At a positive residual r, kappa=log(L_r/L_(r−1)); it is zero except at prime-power r.
At (0,(d,g)), d=p^a, kappa=log(p/(p−1))>0. Waiting at residual one has zero clock.
Let r_m be the residual of T^m x, and let P_m(x) be the product of w_d over exactly
the renewal gaps removed during those m steps, with empty product one. Then telescoping gives

\[
A_m(x)=\log\frac{S_{r_m}}{S_rP_m(x)}
=\log\frac{I_m(x)}{L_{r_m}},\qquad
I_m(x)=L_r\prod_{\text{removed gaps }d}N_d.
\]

For an actual arrow gamma=(z,m−n,y), T^m z=T^n y, the history replacement from y to z has
J_gamma=I_n(y)/I_m(z), and c(gamma)=log(I_m(z)/I_n(y)).
Iteration of the proved branch identities and inversion prove its every-Borel IMAGE law on every
finite-history chart. Common-tail extension adds identical clock sums to both sides, proving descent;
aligning common tails proves the cocycle identity. T is total, so alignment has no hidden terminal cut.
These charts give the Borel actual-lag groupoid; duplicate triples are identified, not remembered as words.

The COMPLETE arrow kernels are
ker(c)={gamma:I_m(z)=I_n(y)}, ker(lag)={gamma:m=n}, and their intersection satisfies both tests.
The tests are witness-independent. Neither kernel contains the other: the residual-one W step has
lag one and c=0; the two preimages W(2,g) and E(2,g) yield a lag-zero arrow with c=log 2.
The two preimages W(1,g) and E(1,g) are distinct and give lag zero and c=0.
Thus even the intersection is not merely identities. This does not imply nontrivial isotropy kernels.

## 5. All incoming histories, isotropy, primitive packets and phases

For a target y=(r,g), all m-step predecessors are exactly (r+m,g), and
(s,u g) with u=(d_1,...,d_a), a>=1, d_a>r, s=m+r−sum_i d_i>=0.
The latter formula records every path with at least one renewal, including its last partial wait.
It follows directly by summing waiting times; conversely these conditions make every such history legal.
For each m there are at most 2^m predecessors, by the two inverse charts.
The whole source orbit of (r,g) consists precisely of (s,v sigma^a g), s,a>=0 and v any finite D-word.
Indeed both sides reach residual zero with the same future tail; any common tail can also be advanced
to residual zero. This is a complete incoming/orbit description, not selected periodic representatives.

Nonzero isotropy occurs exactly when g is eventually periodic. Let u=(d_1,...,d_l) be its
primitive cyclic gap word, and set L=sum_i d_i and tau=sum_i log N_(d_i)>0.
At o=(0,u^infinity), returning to residual zero consumes a positive number of whole gaps;
equality of the infinite gap tail forces that number to be a multiple of l. Hence its least source
period is L, and one circuit has clock tau, not l unit times or a single logarithmic label.
A state is literally periodic iff its gap tail is purely periodic and 0<=r<d_l for its anchored
primitive word. Arbitrary larger residuals are ancestors, not extra literal periodic states.
For EVERY ancestor in this source orbit the entire isotropy is LZ and c(kL)=k tau.
For a noneventually-periodic gap history the source isotropy is zero.
Thus extension isotropy is trivial everywhere; H_x=tau Z in these basins and {0} otherwise.
The isotropy clock kernel is trivial even though the full arrow clock kernel above is not.

Primitive physical packets correspond bijectively to primitive cyclic D-words, with all their incoming
histories and residual phases. Different necklaces cannot acquire a common eventual tail and do not merge.
Each periodic source orbit gives the orbit-set circle R/(tau Z); repetitions have times k tau, k>=1.
For x with T^m x=T^j o, a complete phase is h−A_m(x)+A_j(o) modulo tau.
For a free source orbit, an anchor a gives the real phase h+c(a,k,x), independent of the arrow choice.
These are orbit-set and stabilizer statements, not claims of Hausdorff quotient geometry or an invariant
physical-flow measure. Height translation is complete and well-defined on all of the orbit set.

The four frozen tests are all legal: 2,3,4 belong to D.

| Primitive gap word | Least source period | Entire H in its basin | Least physical time |
| --- | --- | --- | --- |
| (2) | 2 | log(2) Z | log 2 |
| (3) | 3 | log(3) Z | log 3 |
| (4) | 4 | log(12) Z | log 12 |
| (2,3) | 5 | log(6) Z | log 6 |

Here w_2=1/2, w_3=1/3, w_4=1/12. All four are distinct full packets. In particular (2,3)
is primitive, not a repetition of (2) or (3). The latter two test times are logarithms of composites,
so the predeclared target fails without rescaling. No further cycle census or weight tuning is needed.

## 6. Three independently owned controls

**GEOMETRIC.** Here D_G={1,2,...}, v_d=2^(−d), V_r=2^(−r), M_G=2 and residual mass
2^(−r−1). The same construction, inverse formulas and every-Borel proofs apply with these own data;
both inverse domains are now all X_G and both derivatives are 1/2. Hence kappa=log 2 and c=k log 2.
Its complete kernel and lag kernel coincide, including nonidentity synchronized-history arrows.
Its binary image is precisely the sequences with infinitely many ones, not the full binary compactum.
For every primitive cyclic positive-gap word u, source isotropy throughout its basin is LZ,
H=L log(2) Z, and extension isotropy is trivial; other histories have zero isotropy and H.
The full incoming formula of §5 uses D_G, and phases are h−m log2+j log2 modulo L log2.
Packets are equivalently primitive binary necklaces containing a one, with the all-zero necklace excluded.
The four displayed gap tests have least source periods 2,3,4,5 and times log4,log8,log16,log32.

**DETERMINISTIC.** Its source has exactly two states (0,2^infinity) and (1,2^infinity).
T swaps them; its unique global inverse is the same swap. W exists only at target residual zero,
E only at target residual one. The stationary masses are each 1/2, so every inverse IMAGE is one.
All clocks vanish. The retained action has full source and extension isotropy 2Z at both states,
H=0, full clock kernel the entire groupoid, and lag kernel/intersection exactly the identities.
All incoming labels are retained, with their unique predecessor determined by parity. Both states form
one source orbit; its real physical phase is h, with no positive physical period despite source period two.
Only the (2) gap test is legal here. No zero-mass extra residual was appended.

**REINDEX-OFF.** On the entire MAIN X and mu, the only inverse map is id and its every-Borel IMAGE is one.
The actual retained groupoid is X×Z: all labels act at the same state, not an effective identity relation.
Here c=0 on every arrow, ker(c)=G, ker(lag)=their intersection=the identity arrows,
and source/extension isotropy is Z at every point while every H_x is zero.
All incoming arrows at x are (x,k,x); source orbits are singletons and every height h remains a phase.
Literal source period is one for every state. The four test states exist but have no positive packet;
their residuals and different gap tails are never identified. Its repeated residual-bit observation
is constant and does not reconstruct X, unlike MAIN's shifting observation.

## 7. Mechanism and final boundary

MAIN is the full path source of the countable residual graph r->r−1 for r>0 and 0->d−1 for d in D.
Every infinite graph path renews indefinitely because every wait is finite. The path measure has
stationary vertex masses S_r/M, outgoing gap law w at zero, and deterministic waiting elsewhere.
All excursions at zero can be concatenated and periodically repeated. Thus the full-path splicing
premise named in the card applies; nonproduct binary observations do not evade that mechanism.
No additional unread hypothesis or conclusion from paper 364 is invoked. The clock belongs to this
new probability owner, not to the earlier phase-transport source, and no prime-only subsource was selected.
Strong naturalness remains OPEN; T3 is NOT AUDITED, classical coordinates NOT APPLICABLE,
formal status UNASSIGNED and Route B NOT INVOKED. The bounded negative gate is complete: STOP / FORK.
No missing mathematical obligation blocks this scoped decision. Manuscript comparison remains a later task.
