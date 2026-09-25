# Divisor-gap geometry, factor-sum feedback, and a composite fixed primitive

Candidate ID: ANG-20260925-DGF01.
Paper: 482-divisor-gap-factor-sum; batch PRE-P0-STRUCTURE-20260925-AA, round 3/5.
Date: 2026-09-25. Type: ANG measured-history owner.
Outcome: OWNED DIVISOR-GAP IMAGE; COMPOSITE FIXED RETURN — STOP / FORK

## Abstract

The current positive integer determines geometric gaps between its divisors.
The chosen gap determines both the real rescaling and a new factor-sum integer.
For MAIN and three separately owned controls we prove totality, exhaustive
inverse branches and every-Borel IMAGE, with all endpoint versions retained.
We classify ALL fixed states, without an integer cutoff or selected real ansatz.
MAIN has exactly the fixed core \((4,1/3)\); its entire incoming packet has
period group \((\log4)\mathbb Z\), so its primitive is composite, not \(\log2\).
The control with equal divisor-cell widths has a different prime-3 fixed packet;
it does not supply a clock for MAIN. Complete history, kernel, isotropy and
phase accounting is retained. No higher-period census or formal Route is claimed.

## 1. Frozen source, controls and lineage

The [card](candidate-card.md), version 1.1, lines 1–97, is the contract.
Its clarification requires an ACTUAL positive primitive \(\log p\) for an
ordinary integer prime, without time rescaling or equal-time packet merging.
Use
\[
X=\mathbb N_{\ge1}\times[0,1],\qquad
\mu=\text{counting}\otimes dx
\]
with the discrete × closed-interval topology and its Borel structure.
Every integer fibre has counting weight one; \(\mu\) is sigma-finite.
Let \(\mathcal D_N\) be the positive divisors of \(N\), let \(e_N(d)\) be the
largest divisor below \(d\), or zero, and let \(r_N(d)\) be the increasing
divisor rank, with \(\tau(N)=|\mathcal D_N|\).
Each owner selects its own branch label \(d\), and acts by
\[
T_V(N,x)=\left(g_V(N,d),\,\frac{x-\ell_V(N,d)}{w_V(N,d)}\right).
\tag{1}
\]

| Owner | Labels | \(\ell_V\) | \(w_V\) | \(g_V\) |
| --- | --- | --- | --- | --- |
| M MAIN | \(d\in\mathcal D_N\) | \(e_N(d)/N\) | \((d-e_N(d))/N\) | \(d+N/d\) |
| A alphabet-OFF | \(1\le d\le N\) | \((d-1)/N\) | \(1/N\) | \(d+\lfloor N/d\rfloor\) |
| F factor-return-OFF | \(d\in\mathcal D_N\) | \(e_N(d)/N\) | \((d-e_N(d))/N\) | \(N+1\) |
| U gap-geometry-OFF | \(d\in\mathcal D_N\) | \((r_N(d)-1)/\tau(N)\) | \(1/\tau(N)\) | \(d+N/d\) |

Every nonlast source interval is \([\ell_V,\ell_V+w_V)\); the last, labelled
\(d=N\), includes the right endpoint 1. Positive consecutive divisor gaps
telescope from zero to \(N\), so M/F form a partition with positive widths.
Equal integer/divisor ranks give the same conclusion for A/U.
Thus all labels are unique, cuts are right-assigned, and the whole closed
interval is covered. Each nonlast branch has actual real image \([0,1)\),
each last branch \([0,1]\). At \(N=1\) every owner has ONE branch of width
one and acts as \((1,x)\mapsto(2,x)\), including both endpoints.
All integer outputs in (1) are positive integers, in fact at least two.
Hence the four maps are total on \(X\): there are no outgoing-terminal objects
in this particular frozen carrier. The whole unit fibre remains nevertheless.
No zero integer is silently added, and no real zero, endpoint or cut is deleted.

For integers \(1<D<N\), the seed \(x=(D-\tfrac12)/N\) is strictly between
successive integer-grid points. Its MAIN label is the least divisor \(d\ge D\):
the interval inequalities are \(e_N(d)<D\le d\).
It equals D exactly when \(D\mid N\); otherwise it is the next divisor.
This proves the stated proper-divisor symbolic interface. These seeds only
identify the observable; they are not a restriction or selected periodic section.
MAIN then executes the selected factor pair's sum, changing the actual integer
that determines the next partition. Formula/measure are declared designs,
not a proof of strong naturalness or a Logistic/Hénon/conservative lift.

## 2. Complete inverses and every-point IMAGE

Fix any target \((m,v)\in X\). The complete integer predecessor lists are:

| Owner | All candidate source integers and labels |
| --- | --- |
| M/U | ordered \(d,q\ge1,\ d+q=m\); \(N=dq\) |
| A | \(d,q\ge1,\ d+q=m\); every integer \(dq\le N<d(q+1)\), \(N\ge1,\ d\le N\) |
| F | \(N=m-1\ge1\); every \(d\in\mathcal D_N\) |

For each row use that owner's own \(\ell,w\) and set
\[
\theta(N,d;m,v)=(N,\ell_V(N,d)+w_V(N,d)v). \tag{2}
\]
Its precise target real domain is \([0,1]\) if \(d=N\), and \([0,1)\) otherwise.
The integer row conditions and this domain are the exact inverse conditions.
For M/U, a source factor label has \(q=N/d\), hence \(N=dq,d+q=m\);
conversely these equations give the actual integer law and a divisor label.
For A the interval \(dq\le N<d(q+1)\) is exactly \(\lfloor N/d\rfloor=q\),
with the separate source label condition \(1\le d\le N\).
F's integer condition is exactly its increment law.
The real affine identities in (1)–(2) hold both ways; the specified target
endpoint rule is precisely membership in the unique actual source interval.
This proves necessity, sufficiency and exhaustive coverage, not formal roots.

Each target has finitely many inverse candidates: positive pairs of fixed sum
are finite, A has a finite integer interval for each pair, and F finitely many
divisors. Different labels cannot duplicate an actual predecessor because
its source partition label is unique. All distinct predecessors, including
ordered-factor alternatives and overlapping inverse domains, are retained.
No target-outgoing condition is imposed. The full image is exactly
\[
\{2,3,\ldots\}\times[0,1]. \tag{3}
\]
Indeed all outputs have integer at least two, and for any \(m\ge2\) the last
branch of \(N=m-1\) maps onto its whole target interval for every owner.
The unit target fibre has no incoming, but is not deleted or made absorbing.

An inverse branch is a Borel affine injection between two counting-weight-one
integer fibres. For EVERY Borel \(E\) in its exact target domain,
ordinary affine Lebesgue scaling therefore gives
\[
\mu(\theta E)=\int_E w_V(N,d)\,d\mu. \tag{4}
\]
This includes endpoint/cut sets, whose images remain null.
The frozen affine extension germ assigns this same finite positive value
at every such point. It is an explicit pointwise prescription, not forced by
a.e. uniqueness and not repaired after inspection of a returning point.
There is no factor for the number of predecessors or the target fibre degree.
Thus the four OWN densities and clocks are

| Owner | Full-point inverse \(J\) | \(\kappa_V(N,x)=-\log J\), using its actual label |
| --- | --- | --- |
| M/F | \((d-e_N(d))/N\) | \(\log[N/(d-e_N(d))]\) |
| A | \(1/N\) | \(\log N\) |
| U | \(1/\tau(N)\) | \(\log\tau(N)\) |

All these clocks are zero at \(N=1\) and strictly positive at \(N\ge2\):
there are then at least two positive-width cells for M/F/U, and \(N\ge2\)
for A. This does not make the total carrier a classical positive-roof
suspension, since the unit steps still have zero clock and no such lift was defined.

## 3. Whole retained-lag transport, kernels and period groups

For each owner separately, all finite iterates are legal. Put
\(S_r(z)=\sum_{i=0}^{r-1}\kappa_V(T_V^iz)\), \(S_0=0\), and
\[
\mathcal G_V=\{(z,r-s,w):T_V^rz=T_V^sw,\ r,s\ge0\},\qquad
c(z,r-s,w)=S_r(z)-S_s(w). \tag{5}
\]
Source is w, range z, and equal triples only are identified.
The Borel relation is a countable union of equalizer sets, with countable
fibres from §2. Units/inversion are the actual triple operations.
Composition follows by advancing the two intermediate histories to their
later time; lags add. Two presentations of the same lag differ by equal
advancement on both legs, so their identical added future sums cancel.
This proves pointwise descent and the cocycle law, including assigned cuts.

Restrict the two legs to actual finite branch itineraries, intersect their
Borel images, and compose inverse-first-leg with forward-second-leg.
The empty itinerary is the identity on all X. These countably many injective
branch pairs cover every arrow; iterating (4) gives their every-Borel IMAGE
\[
J_{w\mapsto z}=\exp(S_s(w)-S_r(z))=\exp(-c(z,r-s,w)). \tag{6}
\]
Thus the clock belongs to the actual history transport.
The three complete kernels are
\[
K_{\rm lag}=\{(z,0,w)\in\mathcal G_V\},\qquad
K_c=\{g\in\mathcal G_V:c(g)=0\},\qquad
K_{\rm joint}=K_{\rm lag}\cap K_c. \tag{7}
\]
These retain all off-diagonal arrows satisfying the displayed tests;
zero clock or zero lag is not by itself identification with a unit.

Keep all \(X\times\mathbb R_h\), with \((w,h)\mapsto(z,h+c(g))\).
The actual forward arrow \((T_Vz,-1,z)\) subtracts \(\kappa_V(z)\).
Height translation acts on the orbit SET; a smooth/Hausdorff quotient or
measurable global section is not presumed.
There is a nonzero source self-lag exactly when a source is eventually
periodic: it gives equality of two different forward iterates, and conversely
a repeated eventual cycle provides all its integer repetitions.
If that least cycle has period \(\ell\) and signed sum \(C_\gamma\), then
\[
\operatorname{Iso}_{\mathcal G_V}(z)=\ell\mathbb Z,\quad
c(\ell k)=kC_\gamma,\quad H_z=C_\gamma\mathbb Z. \tag{8}
\]
These are ENTIRE groups: equality on a least cycle forces lags divisible by
\(\ell\), and transient sums cancel. Non-eventual points have trivial source
isotropy and \(H_z=\{0\}\).
Every actual cycle lies in (3), so its clocks are strictly positive and
\(C_\gamma>0\). Consequently extension isotropy is trivial in all cases.
For an actual cycle the primitive translation time is \(C_\gamma\), with
repetitions \(kC_\gamma\), not a quotient by its source period.
This is a conditional structural ledger, not a census of higher cycles.

## 4. All incoming and complete phase accounting

Define \(\operatorname{Pre}_V(A)\) using EVERY actual inverse of §2 and iterate
from \(\operatorname{Pre}^0_V(A)=A\), with no source-integer or depth cutoff.
The one-step completeness proof, by induction, gives exactly all finite
incoming histories, including endpoints, cuts and empty inverse fibres.
Compatible infinite histories are exactly sequences whose every successive
pair passes those actual inverse tests. Every finite-prefix constraint remains;
we do not assert every finite history extends indefinitely.
For any object z, an exact full source-orbit test is
\[
\mathcal O_V(z)=\bigcup_{r,s\ge0}
\operatorname{Pre}^s_V(\{T_V^rz\}). \tag{9}
\]
Each membership is an equal-future arrow and every arrow has these indices.
This includes all source orbits, not only the fixed cores tested below.

For any actual cycle choose a point b, and let
\(\mathcal B_V(b)=\bigcup_{a\ge0}\operatorname{Pre}^a_V(\{b\})\).
This is its entire source orbit: an arrow to b gives eventual arrival at a
cycle point, which advances to b; the converse is an arrival arrow.
Let \(a(z)\) be the least arrival time at b and \(Q(z)=S_{a(z)}(z)\).
All arrows within this whole basin, and only those arrows, satisfy
\[
k\equiv a(z)-a(w)\pmod\ell,\qquad
c(z,k,w)=Q(z)-Q(w)+
\frac{k-a(z)+a(w)}{\ell}C_\gamma. \tag{10}
\]
Advance both legs beyond arrival to prove necessity; equal cycle positions
give the congruence and complete cycle sums give the formula.
For sufficiency choose sufficiently long nonnegative legs of the indicated
lag ending at b. Thus (10) is an exact unrestricted kernel/clock test.
The complete real phase invariant is
\[
h-Q(z)\pmod{C_\gamma\mathbb Z}. \tag{11}
\]
The actual arrow z to b subtracts \(Q(z)\); different arrivals differ by a
loop in the ENTIRE H, and (10) proves the converse classification.

In particular, for a fixed b put \(C_b=\kappa_V(b)>0\) and
\(\beta(z)=Q(z)-a(z)C_b\). Every integer k is an actual basin lag, and
\[
c(z,k,w)=\beta(z)-\beta(w)+kC_b. \tag{12}
\]
On this basin, (7) means respectively \(k=0\), the right side of (12) zero,
or both. Source isotropy is \(\mathbb Z\), extension isotropy zero,
ENTIRE \(H=C_b\mathbb Z\), with ALL phases \(h-Q(z)\bmod C_b\).
Each full fixed basin supplies one primitive circle packet, not one packet
per predecessor or per phase point on that circle.
Distinct fixed cores cannot be related: their forward iterates stay at their
different cores. Equal times therefore do not merge distinct fixed packets.
For non-eventual orbits, choose any base and actual arrow \(g_z:z\to b\);
the phase is \(h+c(g_z)\bmod H_b=h+c(g_z)\). No global measurable choice is claimed.

## 5. ALL global fixed states of the four owners

For M/U, write the selected factor pair as \(N=dq\), \(q=N/d\).
Integer fixedness is
\[
dq=d+q\quad\Longleftrightarrow\quad(d-1)(q-1)=1.
\]
Positive integer factors force \(d=q=2,N=4\), exhausting every integer root,
including the exclusion of unit choices. Here the divisor list is \(1,2,4\).
For M, the actual branch is \([1/4,1/2)\), and the real map is \(4x-1\).
It fixes exactly \(x=1/3\), strictly inside that branch.
For U, the branch is \([1/3,2/3)\), the real map \(3x-1\), and the only
fixed coordinate is \(x=1/2\), again strictly interior.
These equations exhaust the entire closed real fibre, not chosen centres.
F would require \(N+1=N\), so it has no fixed state.
This empty FIXED set is not used as a proof of global positive-ledger emptiness.

For A, let \(q=\lfloor N/d\rfloor\ge1\). Integer fixedness is \(N=d+q\).
The exact floor inequalities then give
\[
dq\le d+q<d(q+1).
\]
The strict upper inequality forces \(d>1\); the lower is
\((d-1)(q-1)\le1\). If \(q=1\), all \(d\ge2\) work, giving \(N=d+1\ge3\).
If \(q\ge2\), the two positive integer factors must both be one, so \(d=q=2,N=4\).
Conversely these cases satisfy the actual floor quotient, with no MAIN
divisibility condition imposed. Thus the complete integer-fixed branch list is
\(d=N-1,\ N\ge3\), and the additional \((N,d)=(4,2)\).
The real map is \(Nx-(d-1)\), giving the unique solution
\[
x=\frac{d-1}{N-1}.
\]
Every listed branch is nonlast, and both membership inequalities are strict:
\[
x-\frac{d-1}{N}=\frac{d-1}{N(N-1)}>0,\qquad
\frac dN-x=\frac{N-d}{N(N-1)}>0.
\]
No omitted endpoint/cut solution exists; integer fixedness was already exhaustive.
All four owners send endpoints in a first/last branch with integer output
\(N+1\), excluding endpoint fixedness as well, including \(N=1\).

| Owner | COMPLETE global fixed set | Fixed clock and ENTIRE H of each full basin |
| --- | --- | --- |
| M | \(\{(4,1/3)\}\) | \(\log4;\ (\log4)\mathbb Z\) |
| A | \(\{(N,(N-2)/(N-1)):N\ge3\}\cup\{(4,1/3)\}\) | \(\log N;\ (\log N)\mathbb Z\) |
| F | empty | No fixed-core time is assigned |
| U | \(\{(4,1/2)\}\) | \(\log3;\ (\log3)\mathbb Z\) |

For EVERY listed core, §4 supplies its whole incoming packet, complete kernels,
all source/extension isotropy, phases and repetitions, without restricting
predecessor integers to the fixed core's fibre.
A has two distinct cores at \(N=4\), coordinates \(1/3,2/3\), hence two
distinct \(\log4\) fixed packets. Its other displayed integer fibres each
have one fixed core. Those control clocks belong only to A.
U's own prime-3 fixed packet is not a prime-3 packet for M.

## 6. Target failure, controls and bounded decision

MAIN has a positive primitive \(\log4\), and 4 is not an ordinary prime.
Its source period is one and ENTIRE H is \((\log4)\mathbb Z\), so it cannot
be relabelled a repetition of a \(\log2\) primitive. Universal MAIN prime-only
purity is REFUTED, not merely OPEN. No time rescaling or packet merging is used.
The same adverse fixed point/time is present in arithmetic-OFF A.
F removes fixed returns at this gate, while U changes the actual geometric
clock and gives its different fixed result. Neither rescues MAIN.

| Obligation | Scoped result |
| --- | --- |
| T0 original carrier/total maps/actual inverse and IMAGE | ESTABLISHED |
| Proper-divisor symbolic interface | ESTABLISHED; strong naturalness OPEN |
| T1 positive prime-return target | NOT PASSED; composite MAIN primitive |
| T2 full structural ledger and global fixed gate | ESTABLISHED within the stated scope |
| Universal MAIN prime-only purity | REFUTED |
| Higher cycles, global periodic census, uniqueness/all-prime coverage | OPEN / NOT AUDITED beyond fixed gate |
| Naturalness / PROVES_TOO_MUCH beyond this adverse witness | OPEN |
| T3 / operator / trace | NOT AUDITED |
| Classical conservative/symplectic/positive-roof fields | NOT APPLICABLE |
| Formal coordinates / Route B | UNASSIGNED / NOT INVOKED |

The same-object ledger remained intact, separately for all owners. The fixed
classification has no integer cutoff; unrestricted inverse recursion is not
a finite sampled basin. No higher-period extension, fitted gap, new density,
roof or selected recurrent section is introduced. Decision: STOP / FORK.

## 7. Inputs, exposure and author assistance

Author fully read the 97-line clarified card through EOF, SHA-256
74d6ee846d89f2f19d69f360a2aa36568385d2f46674c183f65271ad62098402,
and the stream paper template. The original 87-line definition was preserved
by root; the target clarification preceded proof release and changed no map.
Exact integer factor/floor algebra, real affine equations, Borel IMAGE and
history arguments are the scientific methods. No scientific code, approximate
experiment, external literature result or network is an input.
The author did not read CP1 scope, raw, reviewer or peer scientific outputs.

Design comparison read: papers/478-count-factor-return/candidate-card.md,
1–59/123, prefix SHA
ad45d8512c47fc276edb4561c969816995df7d6040d92f649f890948072a2577.
Same-author helper read papers/306-reciprocal-factor-quotient-flow/candidate-card.md,
1–65/200, prefix SHA
3789ea84400ffc2b9aa886cbafa655372f66b1fe6c0a22794b9eedb9eeb3e9bb.
Only appended-outcome headings additionally appeared, not outcome bodies/proofs.
Original-definition assertions were visible but supplied no transferred theorem.
Inherited history and informal factor-sum integer design examples before freeze
are disclosed; this was not blind/outcome-sealed or a global novelty claim.

Released same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author
read only the 97-line clarified card, independently measured the same hash,
and supplied the exhaustive A fixed-branch/real-membership subproof.
It did not analyze another owner, higher period, incoming tree or other file,
and made no file writes or additional delegation. It is not a reviewer seat.
The author integrated and checked all derivations here.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Same-model/shared-history
work is NOT_CALIBRATED. Root's subsequent comparison/review is separate.

Navigation: [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[package README](README.md), [separate final review](evidence/review.md).
