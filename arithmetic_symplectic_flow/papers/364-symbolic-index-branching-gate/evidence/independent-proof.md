# Independent raw-card proof — symbolic index branching gate

Audit: `ANG-AUDIT-20260921-SIB01`. Date: 2026-09-21.
Author: `/root/algebraic_henon_author`; internal AI, `NOT_CALIBRATED`.
Sole newly read scientific input: [card](../candidate-card.md), complete lines 1–113
through EOF; line count and SHA-256 independently checked:
`ea095eca49dbaa720f1b6973ee25f7005c6184dc83babaf27105e3a53ea99e98`.
No manuscript, peer/scout receipt, other package, web or numerical experiment.
Prior agent context is shared-history, not blindness. The card itself exposes
root's anticipated branching/escape issue; no independent-error claim follows.
ARS router, deep-research workflow, runtime policy and Devil's Advocate instructions
were previously read completely and reused; the router was last reread in task362,
not reread here. Scope: raw-card exact proof, not a Hénon/C-paper workflow.
Decisive mathematics was sent to root before writing this report.

## 1. Full path and measured groupoid owner

For a finite edge path u let |u| be its length, D(u) its index product,
and [u] its cylinder; empty paths have D=1 and their specified vertex.
Every rooted level has finitely many paths, by row finiteness. Thus X_v is a
nonempty compact inverse limit of finite prefix sets; X is their countable
topological disjoint union. The cylinder masses D(u)^(-1) are consistent because
the sum of 1/d_e over each next-edge choice is one. They therefore extend uniquely
to Borel probabilities mu_v; mu=sum_v mu_v is sigma-finite and has full support.
No source or edge, including a parallel edge, is removed.

For each u ending at w, eta->u eta is a homeomorphism X_w->[u]. Its pushforward
is D(u) times mu restricted to [u], first on cylinders, then on every Borel set
by uniqueness of finite measures. Consequently the replacement v eta->u eta,
where t(u)=t(v), satisfies on EVERY Borel E subset [v]

    mu(theta_(u,v) E) = D(v)/D(u) * mu(E).                 (1)

This includes all null tails. For u=e and v empty it gives J=1/d_e.
The total shift is a local homeomorphism on every [e], without requiring
incoming edges at every vertex. For any Borel A, directly summing these branches
gives mu(sigma^-1 A)=sum_w kappa_w*mu_w(A intersect X_w), understood as the
nonnegative edge sum/integral when kappa_w is infinite. Invariance is not assumed.

Let Z(u,v) contain all triples (u eta,|u|-|v|,v eta). These countably many
prefix charts cover the entire stated groupoid, with source and range charts
[v],[u]. Prefix refinements give their overlap charts. Inversion exchanges u,v;
composition aligns the intermediate prefixes by further common-tail shifts.
This constructs the usual countable local-homeomorphism atlas and Borel owner;
source fibres are countable since finite words and nonnegative shifts are countable.

If two representations have the same lag, their (m,n) pairs differ by (r,r).
After passing to the larger pair, the same tail product multiplies numerator and
denominator. Hence c=log D_m(x)-log D_n(y) is representation-independent.
For composing two arrows, extend their representations until the intermediate
shift exponents agree. The intermediate D factor cancels, proving additivity.
Equation (1) gives c=-log J on every full chart. These locally constant versions
agree on overlaps at ALL points, not just almost everywhere.

## 2. Full kernels, source isotropy, extension and phase

Write ell(x,k,y)=k. Exact complete kernel descriptions are

    ker c   = union Z(u,v) with D(u)=D(v);
    ker ell = union Z(u,v) with |u|=|v|;
    ker c intersect ker ell = union Z(u,v) satisfying BOTH equalities. (2)

These describe entire arrow sets, including arrows between different sources,
not only periodic isotropy or a finite collection of prefixes.
For each x, G_x^x is a subgroup of Z. A nonzero isotropy lag is equivalent to
eventual periodicity of its EDGE sequence: unequal shifts give a periodic tail,
and conversely such a tail gives an isotropy lag. If x is not eventually periodic,
G_x^x={0}. Otherwise let l>0 be its least eventual edge period and N the product
on that primitive tail word. Its positive isotropy generator is precisely l,
so G_x^x=lZ. Moving both shift exponents beyond the preperiod proves

    c(x,kl,x)=k log N,       H_x=(log N)Z.                (3)

Thus H_x={0} for N=1. On source isotropy, ker ell and the intersection in (2)
are always the identity; ker c is all lZ if N=1, and the identity if N>1.
Extension isotropy at (x,h) is exactly this last ker(c|G_x^x), independently of h.

The extension uses every (x,h) and every prescribed arrow. Translation commutes
with arrows. Its stabilizer at [x,h] in Q is exactly H_x: an equality after time
t is an actual isotropy arrow of clock +/-t, and conversely. Each source orbit
therefore supplies one physical orbit, set-theoretically R/H_x. An incoming
prefix identifies heights by its actual c; it neither creates another packet
nor deletes a phase. No Hausdorff or embedded-circle topology is inferred.

Eventually periodic sources are tail-related iff their primitive cyclic EDGE
words agree up to rotation. Indeed equality after shifts identifies their infinite
periodic tails; least periods then identify the primitive words, and the converse
follows by aligning rotations and removing prefixes. Therefore positive packets
are in bijection with primitive cyclic edge words w with D(w)>1; their least
time is log D(w). Powers w^r are repetitions at r log D(w), not new packets.
Index-one words retain their full isotropy but yield physical lines, not positive
packets. Non-eventually-periodic source orbits also yield lines and remain present.

## 3. Complete SCC criterion, including infinite components

The requested target holds IFF the following three conditions hold:
(i) every SCC containing a directed cycle is a finite directed simple cycle,
with precisely one internal outgoing edge per vertex, counting parallel edges;
(ii) the index product of that cycle is either 1 or an ordinary prime;
(iii) the prime products of all positive cyclic SCCs are pairwise distinct.
All-prime coverage requires, in addition, that this set of prime products
equal the entire set of ordinary primes. This is a conditional characterization,
not an endogenous construction or an instruction to install prime labels.

Here is the branching step with full primitivity justification. Suppose v has
two distinct internal outgoing edges e,f in one SCC. Following each by a shortest
return to v gives first-return loops U,V: their interiors do not visit v.
Consequently e occurs EXACTLY ONCE in the closed word UV: once as U's first edge,
never inside either loop, and not as V's first edge f. A proper power, even after
cyclic rotation, has every edge count divisible by its exponent >=2. Therefore
UV is genuinely primitive. Normalization and at least two outgoing choices force
d_e,d_f>=2. Thus D(U),D(V)>=2 and D(UV)=D(U)D(V) is composite, contradicting
the target. This proof does not assume the SCC is finite or the loops equal-length.

In any cyclic SCC every vertex has an internal successor. If each successor is
unique, a positive return walk forces the unique forward path onto a finite cycle.
Every other vertex in that SCC is reachable by an internal path and hence lies
on this same cycle. Thus absence of internal branching forces exactly (i), also
ruling out infinite cyclic SCCs. Every closed word stays in one SCC: leaving and
returning would make the supposedly external vertices strongly connected to it.
Within a simple cycle, the only primitive cyclic edge word is one traversal.
The packet classification then proves necessity of (ii),(iii) and sufficiency
of all three, without ignoring any incoming path or any nonperiodic component.

## 4. Forced escape is not deletion of the periodic path

On a prime-index cycle, integer factorization of its product shows there is
exactly one internal edge with d=p and all other internal edges have d=1.
A d=1 edge exhausts its row. At the d=p vertex other outgoing edges MUST exist,
with total probability 1-1/p; by (i) they leave the SCC. No exit can return,
since a return would put its target in the same SCC.
Starting at any cycle vertex, first return has probability 1/p and length one
cycle; surviving r complete circuits has probability p^(-r). Hence this SCC is
Markov-transient and escape occurs almost surely. The forever-periodic path
still exists, has measure zero, and owns the positive packet by (3).
Every finite incoming prefix of that tail is also null; all remain in the owner.
By contrast an index-one simple cycle has no exits and is a closed deterministic
Markov class, while its clock group is zero. This local statement implies neither
eventual absorption elsewhere nor finite expected return, positive recurrence of
the full countable chain, or any global invariant physical measure.

## 5. BINARY: its own entire ledger

Both prefix weights are 1/2, so its own Bernoulli cylinder mass is 2^(-|u|).
The every-Borel replacement IMAGE is 2^(|v|-|u|), hence c=k log2 on lag k;
kappa=1 and the shift preserves this own measure. Here ker c=ker ell, and their
intersection is that same full equal-lag-zero tail relation.
Every primitive binary necklace of length l gives one packet of time l log2;
ALL finite incoming binary prefixes and rotations belong to that packet's source
orbit. Eventually periodic isotropy is lZ, H=l log2 Z, and extension isotropy
is trivial. Aperiodic-tail isotropy is trivial and its physical orbit is a line.
The two length-one words give TWO log2 packets. For every l>=2, a^(l-1)b is
primitive because b occurs once, and has composite index 2^l. Other primitive
binary words are also retained by the complete necklace parametrization; powers
are only repetitions. All individual infinite paths are Bernoulli-null, not deleted.

## 6. UNIT: its own entire ledger

There is one path z^infinity of mass one. Every prefix map is the identity on
this singleton, with every-Borel IMAGE 1. Actual lag arrows still give G=Z,
not a germ-trivialization. Thus c=0, ker c=G, ker ell={0}, intersection={0}.
Source and extension isotropy are Z at every height; H={0}, Q=R with its full
translation action, and there is no positive packet. Its own P=kappa=1.

## 7. ESCAPE(p): its own full paths, kernels and phases

Put A=a^infinity, Z=z^infinity, and B_(r,i)=a^r b_i z^infinity for r>=0,
1<=i<=p-1. These are ALL paths. The own masses are mu_v(A)=0,
mu_v(B_(r,i))=p^(-(r+1)), mu_w(Z)=1; the B masses sum to one.
Prepending a scales every B mass by 1/p and preserves the null A; b_i maps
the mass-one singleton Z to mass 1/p; z has IMAGE 1. Since these path spaces
are countable, these statements prove the respective IMAGE on every Borel set.
Composing these actual prefixes gives all replacement IMAGE and clock values.

There are exactly two source orbits: {A}, and O={Z} union {all B_(r,i)}.
Define L(Z)=0 and L(B_(r,i))=r+1. At A all lags occur and c(k)=k log p.
On O, EVERY triple (x,k,y), k in Z, occurs: choose the two shift exponents
beyond their exit depths with prescribed difference k. Its clock is

    c(x,k,y)=(L(x)-L(y)) log p, independent of k.         (4)

Indeed beyond the exit each D stabilizes at p^L; common-tail refinements prove
the formula for every representation, including earlier matching prefixes.
On {A}, ker c and ker ell are identities. On O, ker c is all triples with
L(x)=L(y), ker ell is all triples with k=0, and their intersection requires both.
Every O source has isotropy Z, H=0 and extension isotropy Z; no exits are merged
as paths merely because they have the same depth. The whole basin supplies one
physical line, with coordinate h-L(x)log p by (4). The orbit {A} supplies exactly
one positive packet R/(log p)Z, trivial extension isotropy and all repetitions.
Thus Q is set-theoretically that line disjoint-union that one packet; no further
positive packet is concealed in incoming prefixes, equal depths or nonzero lags.

Own Markov probabilities are P(v,v)=1/p, P(v,w)=(p-1)/p, P(w,w)=1.
The number R of a-loops before exit has probability (p-1)*p^(-(r+1)) at r,
so escape is almost sure, while A remains the null periodic source.
Own incoming masses are kappa_v=1/p and kappa_w=2-1/p: mu is NOT invariant.
This externally prime-parameterized control is not pooled into a main source.

## 8. Boundary

The complete conditional graph owner and its prefix clock are established;
the SCC test is a search filter, not an arithmetic-origin theorem. No T3,
classical Route coordinate, Hausdorff flow manifold or invariant physical measure
is supplied. Formal Route unassigned; B not invoked. This ends the fifth-round
proof task; it authorizes neither another graph search nor a sixth round.
