# 385 — Independent card-only derivation

Candidate `ANG-20260922-DFR01`; scientific input: complete 71-line candidate card.
Card SHA-256: `003b19a334ca5957a16c0e34ac7039a96f47c62cb6c8c9252376abf623f4e68a`.
Original 60-line prefix SHA: `125b34c65c11d7bb9289054d432d62d130ce2830af212bb8b33fffab8c4dd862`.
CP1 initially required the missing target predicate; its 11-line pre-mathematics clarification was read and accepted.
Only afterward did the conditional mathematical release take effect. No manuscript, peer or other scientific file was read.
The prior complete ARS instruction reads and their scoped DA/runtime rules are retained; the model/history are inherited.
No auxiliary, network lookup, scientific numerical experiment or author-result input was used.

## 1. Coding construction, topology and complete inverses

Use the auxiliary interval J=[0,1/2] only to construct limits, never as the owner.
For every a>=2, I_a(t)=1/(a+t) maps J into J and has Lipschitz bound 1/4.
Finite compositions applied to 0 are uniformly Cauchy, with tails bounded by (1/2)4^-n.
Their limits do not depend on the auxiliary starting point in J and satisfy

    pi(a)=I_(a_0)(pi(shift a)),    0<pi(a)<1/2.

For fixed first digit a the value is strictly inside (1/(a+1/2),1/a).
These first-digit intervals are pairwise separated by gaps. Thus the first digit is unique,
and repeatedly applying 1/x-a recovers every digit: pi is injective.
Shared long prefixes imply the displayed diameter bound, proving continuity.
The gaps make every finite digit cylinder relatively open; digit recovery proves continuity of the inverse.
Hence pi is a homeomorphism from the declared full path space onto X.
There is no hidden finite-code endpoint: a rational reciprocal algorithm terminates because
its positive integer denominator strictly decreases, whereas every coded tail remains positive.
Thus MAIN, D and C infinite-code points are irrational; 0 and finite expansions are not admitted.
Their carriers are Borel directly: require all iterates of the Borel reciprocal/floor algorithm
to stay in (0,1/2), and impose the relevant countably many successive-digit conditions.

For MAIN, B_a is the union of first-digit cylinders b dividing a+1, b>=2; it is clopen.
All inverses are I_a:B_a->[a]. Both T I_a=id and I_a T=id on [a] follow from digit recovery.
Every target starting with b has all and only predecessors a=kb-1>=2, so T is onto.
Every state has legal continuations, for example successively increasing digits; there are no terminal states.
A finite prefix u is legal iff its internal successor edges are legal and its last digit plus one
is divisible by the target's first digit. This gives the entire finite inverse domain, not just a chosen tail.

Every point is an accumulation point inside each of its finite cylinders.
Indeed a vertex with composite a+1 has at least two successors. If a+1 is prime,
its forced successor is the odd integer a+1>=3, whose successor set includes both 2 and a+2.
Thus branching occurs arbitrarily far along every path; changing a late branch and continuing legally
gives distinct points with the same increasingly long prefix. The same holds inside every nonempty inverse domain.
MAIN is locally compact and noncompact: each fixed-first-digit path space is a closed subspace
of the product of finite sets {2,...,a+n}, while first digits are globally unbounded and their images approach excluded 0.
These facts describe the actual subspace, not an interval completion or a manifold.

## 2. Intrinsic metric clock versus the Markov IMAGE

In a relative neighborhood of any x, its first digit a is constant and T(x)=1/x-a.
For distinct x' in that neighborhood, the difference quotient is -1/(xx'), tending to -1/x^2.
Accumulation proved above makes this an intrinsic derivative on X, not a freely assigned ambient value.
Likewise the intrinsic inverse derivative on B_a is -1/(a+y)^2.
Consequently tau(x)=-2 log x>log 4 everywhere, with its declared geometric normalization.

The initial distribution eta_a=2^(1-a) sums to one. Z_a is positive because a+1 is a legal successor,
and finite because sum_(b>=2)2^-b=1/2. Each transition row is a probability.
The consistent cylinder values eta_(a_0) product P(a_i,a_(i+1)) define the Markov probability;
every legal finite cylinder has positive mass. Pushing by the coding homeomorphism gives full support on X.

The law is nonatomic. For any particular MAIN path, either digit 2 occurs infinitely often,
forcing infinitely many visits to 3, whose largest outgoing probability is 4/5;
or eventually every successor is at least 3. In the latter case odd current digits occur infinitely often,
because every successor of an even digit divides an odd integer and is odd.
At each late odd digit, successor 2 has weight 1/4, so any chosen b>=3 has probability
at most 2^-b/(1/4+2^-b)<=1/3. In either case the infinite cylinder mass tends to zero.
A positive Borel atom in this countably coordinate-separated space would give a singleton atom
by intersecting its full-mass coordinate cells. Hence there are no Borel atoms either.

For D subset B_a intersect [b], the Markov cylinder law gives

    mu(I_a D)=eta_a P(a,b)/eta_b * mu(D).

Finite cylinders generate the Borel sigma algebra; equality of the finite measures extends this identity
to every such Borel D, and the countable first-digit partition proves it for every Borel D subset B_a.
The exact all-point version is the one in the card. Here it simplifies on its whole domain to
j_a=2^-a/Z_a, which is strictly positive and finite, but need not be less than one.
For a legal prefix u ending before target first digit b, the every-Borel finite-history density is

    J_u=eta_(u_0) P(u_0,u_1)...P(u_(m-1),b)/eta_b = product_(i<m) j_(u_i).

The identity follows either on cylinders then by finite-measure uniqueness, or by repeated change of variables.
It supplies branch-pair measure IMAGE J_u/J_v on their entire actual domains.
This measure cocycle is NOT the geometric clock: at legal predecessor 2 of a tail starting 3, j_2=2,
whereas the geometric inverse derivative has magnitude 1/(2+y)^2<1.
The law is in fact not stationary: T_*mu([3])>=eta_2 P(2,3)=1/2>eta_3=1/4.
Neither stationarity nor equality of the two cocycles is needed or asserted by the frozen contract.

## 3. Actual geometric cocycle and complete kernels

For any of the three fractional-map owners, let M_a=[[0,1],[1,a]].
A finite inverse word u has matrix M_u=product M_(u_i), bottom row (C_u,D_u),
determinant (-1)^m, and intrinsic derivative magnitude 1/(C_u t+D_u)^2 on its actual tail domain.
All these finite domains are clopen unions of cylinders without isolated points, so the derivative formula is intrinsic.
With A_m the geometric sum, A_m(I_u t)=2 log(C_u t+D_u).
Actual triples retain lag m-n, source w and range z; equal triples alone identify arrows.
Common-tail padding cancels equal added sums and aligns composition witnesses. Therefore

    c(I_u t,m-n,I_v t)=2 log[(C_u t+D_u)/(C_v t+D_v)]

is an everywhere-defined Borel cocycle. This is the geometric, not the Markov, cocycle.
All source incoming states are exactly I_u(T^n x) with every legal finite u and every n>=0.
The groupoid is Borel by the countable union of its fixed-exponent equality sets.
Its full lag kernel is equal-iterate tail equivalence, with all legitimate replacements retained.

Its ENTIRE geometric clock kernel consists only of units. To see this, c=0 gives
(C_u-C_v)t+(D_u-D_v)=0. Irrationality of t forces equal integer bottom rows.
Starting with (0,1), adjoining a digit updates a row by (C,D)->(D,C+aD).
The last digit is recovered as floor(D/C), with remainder the previous C; iteration recovers
the entire word uniquely, since all digits are at least 2. Thus equal bottom rows imply u=v.
The endpoints and lag are then equal and zero. Empty words give the same conclusion.
The clock/lag-kernel intersection is therefore units as well; the lag kernel itself can be nontrivial.
For example prefixes 3 and 5 before a tail starting 2 are both legal MAIN equal-lag replacements.
This short general identity is not a higher-cycle search.

The extension arrows are (w,h)->(z,h+c) for every state and every real h.
Height translation defines a complete R action on the orbit SET. No Hausdorff, smooth/contact or invariant-measure claim is made.

## 4. Entire source and physical packet classification

Coding is injective, so a nonzero source isotropy lag is exactly equality of two shifted words.
Non-eventual histories have isotropy zero. An eventually least-d periodic tail has the ENTIRE dZ,
including every finite incoming history; no gcd of selected displayed loops substitutes for this group.
For MAIN the primitive cores are exactly closed legal words with w_(i+1) dividing w_i+1 cyclically,
reduced to their least word and identified by cyclic rotation only. There is no length-one core.
This is a complete parametrization, not a claim to enumerate all possible numerical periods.

For a core w of least length d and its real fixed point x=pi(w^infinity), set

    L(w)=sum_(i<d) tau(T^i x)=2 log(C_w x+D_w)>0.

Full c on source isotropy sends kd to kL. At every ancestor H=LZ, extension isotropy is zero,
and the whole real-height fiber over that source orbit is R/LZ. A non-eventual orbit instead has H={0}
and a translation line, with no positive return. There is one physical packet per primitive necklace.
All repeated traversals have time kL, not new primitive packets.
If T^N z=T^r x, the connecting arrow z->x has c=A_r(x)-A_N(z), so phase is
h+A_r(x)-A_N(z) modulo H. This includes the complete incoming and real-height phase set.
Every source orbit is countable and measure-null under the proved nonatomic law, but no orbit is deleted.

## 5. First MAIN test: an actual primitive, not a chosen clock subgroup

For the legal two-cycle 23, x=I_2(y), y=I_3(x) give
x=(sqrt(15)-3)/2 and y=(sqrt(15)-3)/3, with xy=4-sqrt(15).
The least symbolic period is two, so its full source isotropy is 2Z and

    L_23=-2 log(xy)=log(31+8 sqrt(15)),    H=L_23 Z.

The exponentiated least time is irrational, hence not an ordinary integer prime.
All legal finite predecessors and both core phases belong to this same packet, with the phase rule above.
No smaller physical period exists because the entire source isotropy and its image were determined first.
The clarified necessary MAIN target therefore fails. Coverage, multiplicity and sufficiency are not inferred or tested.
Target promotion stops here; the remaining work below is the three frozen own controls, not more MAIN test cycles.

## 6. D and C: their complete fractional-map owners

For D all words and all inverse prefixes are legal. For C replace the edge rule by gcd(a,b)=1,
so B_a is the clopen union of all coprime first-digit cylinders; these are the complete inverse domains.
Both graphs have infinitely many successors at every vertex, hence no isolated branch points.
The construction, injectivity, intrinsic metric derivatives and irrationality in Sections 1–2 apply
using these own graphs, not MAIN's permission. Their carriers are not locally compact:
every cylinder has unbounded next-digit choices, incompatible with compactness of its continuous discrete projection.

D's own iid row P(a,b)=eta_b gives its full-support nonatomic probability and every-Borel j_a=eta_a.
C's row normalizer is sum_(gcd(a,b)=1,b>=2)2^-b; it is positive and finite, and its Markov law has full support.
C is nonatomic: at an odd current a both 2 and 4 are allowed, so every transition probability is at most 4/5;
every allowed successor of an even a is odd, so odd departures occur infinitely often along any path.
Its own all-point/every-Borel inverse density is eta_a P(a,b)/eta_b=2^-a/Z_a^C.
Both finite-prefix and branch-pair measure laws follow by their own Markov cylinder calculation.
Neither measure density is substituted into the geometric clock.

All actual G, full incoming, geometric kernel/unit intersection and phase proofs in Sections 3–4 apply
to these complete carriers. D cores are all primitive necklaces; C cores are the primitive cyclic coprime words.
Their full H is L(w)Z on every eventual core basin and zero otherwise; extension isotropy is zero everywhere.
D's frozen constant-2 core has x=sqrt(2)-1 and least L=log(3+2 sqrt(2)), with source isotropy Z.
C's frozen 25 core has x=(sqrt(35)-5)/2, y=(sqrt(35)-5)/5 and least L=log(71+12 sqrt(35)),
with source isotropy 2Z. Both exponentiated primitive times are irrational, independently failing the same length diagnostic.
All their ancestors and phases remain. No control result is used in place of the MAIN calculation.

## 7. L: its own affine infinite-code geometry

Set L_a(t)=1/a-t/[a(a+1)]. These maps preserve J and have contraction at most 1/6.
Their first-digit intervals (1/a-1/[2a(a+1)],1/a) are disjoint, with a positive gap to the next interval.
Infinite compositions therefore define an injective coding homeomorphism on the MAIN legal graph,
by the same convergence/gap argument, now with this own family. The carrier is Borel via its piecewise
inverse algorithm and the infinite admissibility tests. It is locally compact, noncompact and has no isolated branch points.
The complete inverse domain is the own first-digit divisibility condition; the forward branch is
T_L(x)=(a+1)-a(a+1)x, and both inverse identities hold on their full domains.
Intrinsic differentiation on accumulating coded points gives |T_L'|=a(a+1), so tau_L=log[a(a+1)]>0.
There is no import of -2 log x from MAIN. Rational points may belong to this new infinite-code carrier.

The same symbolic MAIN Markov law pushed by this own homeomorphism is a full-support nonatomic probability.
Its complete every-Borel densities, finite-history laws and nonstationarity are those of the same path law,
proved by cylinder transport; they are not its affine metric derivatives.
For legal prefixes define W(u)=product u_i(u_i+1). The full geometric cocycle is log[W(u)/W(v)].
Its complete clock kernel is equality of these products on actual arrows; the lag kernel is equality of lengths,
and their intersection requires both. No unit-kernel conclusion is transferred from irrational fractional geometry.
Source isotropy, all incoming histories, phase offsets and primitive necklaces follow from this own coding.
Each least-d core has positive L=sum log[w_i(w_i+1)], full H=LZ and trivial extension isotropy;
non-eventual histories have H={0}. All real phases and repeated times kL are retained.

The frozen 23 core has x=32/71 and y=21/71, found from x=1/2-y/6, y=1/3-x/12.
It has actual least source period two and least physical L=log 72, not log of a prime.
These rational points are genuine infinite affine codes, not illicit finite continued-fraction endpoints.
Its entire incoming packet has H=(log 72)Z and the same phase-offset rule with its own A.

## 8. Bounded disposition and limitations

The full coding, intrinsic metric clocks, independent every-Borel Markov IMAGE laws and retained-lag owners are established.
The first MAIN primitive fails the clarified necessary length target; STOP / FORK concerns this frozen geometric owner.
The three controls have separate complete constructions and independently diagnosed frozen test packets.
No larger MAIN cycle table, parameter search, point selection or time/measure replacement was used.
Intrinsic derivatives are justified by actual non-isolated subspaces, rather than arbitrary values on measure-null periodic points.
The Markov cocycle remains separate: for a general branch pair its measure IMAGE is J_u/J_v, not exp(-c_geom).
No stationary physical probability, smooth quotient, stronger arithmetic naturalness, novelty or Route result is inferred.
Coverage/multiplicity/sufficiency, T3 and any later analytic owner are not decided by this necessary wrong-length test.
The scope report and original card are preserved; only this proof was written during the mathematical stage.
This is internal inherited-model/shared-history NOT_CALIBRATED work, not blind or external peer review.
Raw is to be frozen before a separate manuscript unlock and subsequent CP2/CP3; those later stages are not claimed here.
