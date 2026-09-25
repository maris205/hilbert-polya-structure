# Independent conditional proof — actual-clock rank boundary

Audit: `ANG-AUDIT-20260921-FRC01`; this is not a new candidate.
Standing: the stated finite-rank implication and finite-block bridge hold;
U/V/W have separately verified full suspensions and complete return ledgers.
Internal derivation: `NOT_CALIBRATED`, not external peer review.

## 1. Exact input and provenance

I personally read candidate-card.md original lines 1–116 through EOF and
measured SHA-256
`1054a232c9d6c7e27f60a9f9bbfc4dd3a3822f1ca9da5ceaeb3b0444c1a9c374`.
That frozen contract was the sole new scientific input. No manuscript, peer,
scout, outcome, historical proof, external source, numerical computation or
auxiliary agent was accessed. All proofs below were derived from that input,
and the results were sent to root before this report was written.
The ARS router/DA/runtime guidance read in the preceding assignment and the
previously read workflow are retained. Shared history and disclosed design
expectations remain exposure; no blindness or independent-error claim is made.
The existing model/effort was retained. This report supplies the independent
proof and adverse check, not a claim to have reviewed an unread author draft.

## 2. Rank theorem on the entire actual groupoid

Assume exactly the frozen equality, on every arrow g:x->y,
c(g)=sum_j a_j(g) omega_j+b(y)-b(x).
Let Gamma=sum_j Z omega_j and V=span_Q{omega_j}, with dim_Q V=d.
For every isotropy arrow at every x the b terms cancel, so
H_x=c(G_x^x) is a subgroup of Gamma subset V. This uses the same fixed V
for ALL objects and ALL actual isotropy, not one fitted span per orbit.
Indeed a height translation returns [x,h] precisely when an actual isotropy
arrow supplies that height difference. Thus H_x is the physical stabilizer.

For distinct primes p_1,...,p_N, the numbers log p_i are Q-linearly
independent: clear denominators in a proposed relation and exponentiate;
equality of positive integer prime products forces every exponent to vanish.
Multiplication by one nonzero real lambda preserves this independence.
If lambda log p_i lies in SOME H_{x_i} for each i, all N independent numbers
lie in V. Therefore N<=d. Applying this to every finite selection proves
the same bound on the total number of eligible primes across the full owner.
It applies to arbitrary returns, hence also to primitives. It allows any one
common lambda>0, but no per-prime scales, approximation or asymptotic fit.
For d=0 every H_x is zero. No all-prime exact packet ledger can satisfy
this hypothesis for finite d, irrespective of multiplicities or repetitions.

Zero and nondiscrete H_x stay as such. A positive primitive is assigned only
if the entire H_x=L Z, L>0; the proof has not manufactured such an L from
one loop. In particular the rank theorem does not classify which source
objects are periodic or turn a noncyclic subgroup into a primitive packet.

On the full extension the Borel height change F(x,h)=(x,h-b(x)) conjugates
c to alpha(g)=sum_j a_j(g) omega_j, since
h+c(g)-b(y)=h-b(x)+alpha(g). It commutes with height translation.
This proves a same-owner flow conjugacy without discarding any object,
incoming, lag or null state. Source isotropy and its zero-character kernel
are retained; extension isotropy at (x,h) is exactly ker(c|G_x^x).
The full-arrow kernel is {g:alpha(g)+b(y)-b(x)=0}; it need not equal
the full-arrow kernel of alpha. Coboundaries cancel on isotropy, not on
arbitrary arrows. No nice topology of an abstract coarse quotient is needed.

## 3. The finite-block bridge, with negative histories

Let X be the complete two-sided legal edge shift of the specified finite
graph, and sigma its invertible shift. A fixed finite block has finitely
many possible values B. Write the positive block roof as
f(x)=sum_{B} omega_B 1_B(x), with omega_B>0 on realized blocks.
For n>0 put N_B(n,x)=sum_{i=0}^{n-1}1_B(sigma^i x), N_B(0,x)=0,
and N_B(-n,x)=-N_B(n,sigma^{-n}x).
Directly splitting or cancelling signed intervals gives, for all integers,
N_B(n+m,x)=N_B(n,x)+N_B(m,sigma^n x).
Thus these are integer Borel cocycles on the ACTUAL retained-lag arrows
(sigma^n x,n,x), including periodic points with distinct nonzero lags.
The actual suspension clock is c_f=-R_n f=-sum_B N_B(n,x) omega_B.
The rank hypothesis follows with a_B=-N_B and b=0 on all arrows.
No periodic-only restriction, return-table fit or free-history lift was used.

If on this same entire source tau(x)=f(x)+u(sigma x)-u(x) for a
single-valued Borel u, telescoping for positive and negative n gives
c_tau=-R_n f-u(sigma^n x)+u(x).
The required representation has b=-u, and the exact cover height change
(x,h)->(x,h+u(x)) conjugates it to the f suspension. A claimed cohomology
without that full identity does not establish the bridge. Finite-block roofs
are sufficient, not asserted necessary; arbitrary continuous roofs are not
declared finite rank. Sequential schemes need all controlling phase/memory
in the stated autonomous source, not an omitted unbounded stage variable.

## 4. Separate full owners and measures for U, V and W

For each control independently the source is all X={0,1}^Z. Sigma is a
homeomorphism with inverse (sigma^{-1}x)_i=x_{i-1}; every source incoming
is sigma^{-n}x for its retained lag n. Fair Bernoulli probability nu is
shift invariant: finite-coordinate cylinder probabilities are unchanged,
and their finite-intersection generating family determines the Borel measure.
No periodic sequence is deleted despite its zero nu measure.

U and V are positive continuous roofs, with ranges {1} and {1,sqrt(2)}.
For W the series sum_{k>=1}2^{-k}x_k converges uniformly, since its tail
after N is at most 2^{-N}. Hence tau_W is continuous and 1<=tau_W<=2.
In each owner the signed sums R_n are defined as in section 3, strictly
increase with n, and tend to both infinities; R_{n+1}-R_n=tau(sigma^n x).
Their identities prove c_tau=-R_n is a Borel cocycle on every actual arrow.
In particular the relation is exactly (x,h+tau(x))~(sigma x,h), with no
sign change or a replacement clock borrowed from another owner.

Every equivalence class in the full X x R has a unique representative in
F_tau={(x,h):0<=h<tau(x)}. For any real t and (x,h) in F_tau choose the
unique n with R_n tau(x)<=h+t<R_{n+1}tau(x). The induced map is
Phi^t(x,h)=(sigma^n x,h+t-R_n tau(x)).
This defines the complete Borel flow, all real-time inverses Phi^{-t}, and
the group law, including every roof seam and every nonperiodic sequence.

Each global history map (x,h)->(sigma^n x,h-R_n tau(x)) preserves nu dh
by Fubini, height translation and invariance of nu under sigma^n.
Partitioning F_tau by the selected n in the previous formula gives disjoint
Borel pieces with disjoint images covering F_tau. Consequently Phi^t
preserves nu dh on EVERY Borel subset, not just cylinder rectangles.
The finite, unnormalized masses are respectively
mu_U(F_U)=1, mu_V(F_V)=(1+sqrt(2))/2, mu_W(F_W)=3/2.
The last equality follows by integrating the uniformly convergent series.
These declared roof clocks are not inferred as Haar or other IMAGE clocks.

## 5. Entire groups, all incoming, phase and packet convention

For each of these positive-roof owners the FULL c-kernel contains only
identity arrows: R_n has the sign of n and is nonzero for n!=0.
If x is aperiodic, its source isotropy and physical stabilizer are both zero.
If x has least shift period q, its entire source isotropy is q Z. Set
L=R_q tau(x)>0. The isotropy character is kq->-kL, hence
H_x=L Z, its least positive time is L, and all repetitions have time kL.
The isotropy-kernel and extension isotropy are zero in both cases.
These statements follow from ALL isotropy lags; a period of a nonprimitive
word is not mislabelled the least source period or least physical time.

Complete source orbits are exactly two-sided shift orbits. Invertibility
leaves no additional incoming basins outside them. A physical flow orbit
in the quotient corresponds to one such source orbit, not to a shared L.
For a chosen representative x and y=sigma^j x the complete phase is
h+R_j tau(x), modulo L in the periodic case and as a real number in the
aperiodic case. All j choices differ by exactly the stated period lattice.
Thus each primitive binary necklace of least period q gives precisely one
closed physical packet; different necklaces never merge even at equal times.

For U its complete length ledger is L_U=q. For V, if k of the q symbols
are 1, L_V=(q-k)+k sqrt(2). These formulas use the complete least-period
necklace, not an arbitrary repetition or a selected subset of sequences.
Their all-arrow rank representations have dimensions 1 and 2 respectively;
the fixed sequences all-0 and all-1 show that V cannot have rank dimension 1.

## 6. W's actual full cohomology, not merely a periodic identity

Put w(x)=sum_{k>=1}2^{-k}x_k and
u(x)=sum_{k>=0}2^{-k}x_k=x_0+w(x).
This u is a single-valued continuous function on all X, bounded by 2.
Directly u(sigma x)=2w(x), so u(sigma x)-u(x)=w(x)-x_0.
Therefore tau_W=(1+x_0)+u(sigma x)-u(x) EVERYWHERE, including the
constant sequences and all nonperiodic tails, not only almost everywhere.
For every positive or negative actual history,
c_W=-R_n(1+x_0)-u(sigma^n x)+u(x).
This is rank dimension 1 with omega=1, integer a=-R_n(1+x_0) and b=-u.
The map (x,h)->(x,h+u(x)) is an explicit whole-extension conjugacy to
the two-valued roof 1+x_0 and commutes with physical time. Its cover
translation preserves nu dh; fundamental-domain identifications use the
same measure-preserving history maps already proved above.

On a least-q periodic necklace with k ones the coboundary telescopes,
giving L_W=q+k and entire H=(q+k) Z. Distinct necklaces still give distinct
packets, with phase and source/extension isotropy as in section 5. The
all-0 packet has period 1, so rank zero is impossible. Although W takes
every value in [1,2] by binary expansion and reads infinitely many coordinates,
its actual whole-clock representation has dimension exactly 1.

## 7. Adverse check, assumptions and stopping boundary

The strongest positive alternative is not excluded: an actual roof outside
the proved finite-rank class might have infinitely many rationally independent
return lengths. Nor does the theorem forbid prime-related observables or
finite collections of prime returns within its class. It excludes targets
exceeding d eligible primes under the displayed full-arrow hypothesis.
The common lambda and entire source are essential. A fit on selected loops,
independent clocks per prime, a multi-valued b or an unproved roof cohomology
does not meet the contract. Infinite-range appearance alone is inconclusive,
as W demonstrates. Zero/nondiscrete groups cannot rescue positive primitives.

No assertion is made that 358 has or lacks this representation. No assertion
about 357's separate geometric physical flow follows from its IMAGE clock.
The controls are declared symbolic suspensions, not endogenous prime objects
or conservative geometric realizations of the prior-work lineage. Strong
naturalness stays OPEN. T/Route coordinates are not newly awarded; Route B
is not invoked. The fifth-round conditional obligations are complete, and
this report neither starts nor authorizes a sixth round or new candidate.

EOF — conditional theorem and all three boundary owners; report frozen.
