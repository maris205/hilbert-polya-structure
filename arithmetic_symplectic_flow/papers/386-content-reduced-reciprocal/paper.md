# Content-reduced reciprocals: owned geometric clocks and a noninteger primitive multiplier

Candidate `ANG-20260922-CRR01`; paper `386-content-reduced-reciprocal`.  
Batch `GEOMETRIC-RETURN-20260922-H`, round 2/5; 2026-09-22.  
Outcome: `OWNED RECIPROCAL IMAGE CLOCK; NONINTEGER PRIMITIVE MULTIPLIER — STOP / FORK`

## Abstract

The reciprocal transport has a complete countable-branch Borel owner.
Its own measure gives positive continuous IMAGE densities on every inverse domain, including endpoints.
These versions define a presentation-independent cocycle on the entire partial retained-lag groupoid.
The prescribed unit branch has one fixed point with entire physical stabilizer \(L\mathbb Z\),
where \(L=\log((3+\sqrt5)/2)\) lies strictly between \(\log2\) and \(\log3\).
This is an owned primitive obstruction, not a null-point reassignment or a shorter packet's repetition.
Three separate controls have the same local obstruction but different complete predecessor relations.

## 1. Frozen identity, scope and arithmetic interface

The [card](candidate-card.md), original 66 lines including the pre-mathematics target clarification,
fixes \(Y=\mathbb N_{\ge1}\times[0,1]\), its product Borel structure and \(\mu=\#\times\mathrm{Leb}\).
This is a sigma-finite, full-support, nonatomic measure, not a probability or claimed invariant measure.
Every root, rational, irrational and endpoint is an object.
A point \((n,0)\) has no forward step; \(T^0\) remains its identity.
For \(x>0\), put \(a=\lfloor n/x\rfloor\), \(d=\gcd(n,a)\), and use:

| Owner | Next root \(R(n,a)\) | Remainder scale \(S(n,a)\) |
| --- | --- | --- |
| MAIN | \(a/d\) | \(d\) |
| D: CONTENT-OFF | \(a\) | \(1\) |
| H: ROOT-HOLD | \(n\) | \(d\) |
| Q: REAL-CONTENT-OFF | \(a/d\) | \(1\) |

In each row, \(T(n,x)=(R(n,a),(n/x-a)/S(n,a))\), with its own full \(Y,\mu,T,G,c\).
No control is a subsystem or replacement clock for MAIN.
All claims through Section 6 are proved for each row by the displayed formulas.

For integers \(1<D<N\) and every \(0\le\rho<1\), \((D,D/(N+\rho))\) has actual quotient \(N\).
Thus \(\gcd(D,N)=D\) exactly when \(D\mid N\); content changes MAIN's next root and real remainder.
The lineage is divisor-symbolic admissibility to current geometric division to coupled content reduction.
This interface is established; stronger naturalness is OPEN.
The necessary target requires every positive physical primitive to have length \(\log p\)
for an ordinary integer prime. One violation suffices to stop.

## 2. Exact branch partition and every predecessor

Since \(0<x\le1\), the integer \(a\) ranges over all \(a\ge n\). The cells
\[
B_{n,a}=\{n\}\times(n/(a+1),\,n/a]                                      \tag{1}
\]
are disjoint and partition the entire forward domain.
Their endpoints implement floor literally: \(n/a\) belongs to \(B_{n,a}\);
the excluded left endpoint belongs to the next cell.
On a cell \(d,R,S\) are constant, and \(0\le n/x-a<1\). Thus \(T\) is
a partial Borel map into \(Y\), without an added reset or terminal loop.
Its restriction to (1) is a bijection onto
\[
E_{n,a}=\{R(n,a)\}\times[0,1/S),\qquad
\theta_{n,a}(R(n,a),y)=\left(n,\frac n{a+Sy}\right).                    \tag{2}
\]
Indeed \(a+Sy\in[a,a+1)\), so this inverse lies in (1), has precisely the
required floor and gcd, and both compositions are the identity.
The card's extra condition \(0<n/(a+Sy)\le1\) follows from \(a\ge n\).
No nonempty branch has an isolated target domain.

For a target \((b,y)\), the following is the exhaustive, untruncated list:

| Owner | Parameters and target domain | Actual predecessor |
| --- | --- | --- |
| MAIN | \(1\le k\le b,\ \gcd(k,b)=1,\ d\ge1,\ 0\le y<1/d\) | \((dk,k/(b+y))\) |
| D | \(1\le n\le b,\ 0\le y<1\) | \((n,n/(b+y))\) |
| H | \(a\ge b,\ d=\gcd(b,a),\ 0\le y<1/d\) | \((b,b/(a+dy))\) |
| Q | \(1\le k\le b,\ \gcd(k,b)=1,\ d\ge1,\ 0\le y<1\) | \((dk,dk/(db+y))\) |

For MAIN and Q, write \(n=dk,a=db\): \(d=\gcd(n,a)\) iff \(\gcd(k,b)=1\), and \(a\ge n\) iff \(k\le b\).
D and H follow from their target-root equations; conversely every row reproduces (2), proving completeness.
No two retained parameters in a row give the same predecessor: its root and floor determine \(n,a,d\).
The relation counts actual points, not extra word-labelled copies.

For all four owners the full image is exactly \(\mathbb N_{\ge1}\times[0,1)\).
For MAIN, D and Q, take \(n=1,a=b\); for H take \(n=b,a=b+1\), so \(S=1\).
No source maps to a real coordinate \(1\), but those objects remain.
At \(y=0\) the table gives all incoming to every terminal: MAIN and Q give
\((dk,k/b)\), D gives \((n,n/b)\), and H gives \((b,b/a)\).
All longer incoming histories are obtained by repeated use of the same table.
At \(x=1\), MAIN and Q map to \((1,0)\), while D and H map to \((n,0)\).

## 3. Every-Borel IMAGE and the exact version boundary

Direct differentiation of the actual inverse in (2) gives
\[
J_{n,a}(y)=\frac{nS}{(a+Sy)^2}>0,\qquad
\mu(\theta_{n,a}(A))=\int_A J_{n,a}\,d\mu                              \tag{3}
\]
for every Borel \(A\subset E_{n,a}\).
One-dimensional change of variables applies to this strictly monotone rational map;
both discrete fibres have counting weight one. The identity covers arbitrary Borel sets, not just intervals.
Endpoints and their images have zero measure, so no atomic ratio is inserted.
The rational formula is finite and continuous on the whole half-open domain, including \(y=0\).

It is the unique continuous IMAGE version on each \(E_{n,a}\): two versions agree almost everywhere,
and any pointwise difference, including at \(0\), would persist on a relative interval of positive measure.
No uniqueness among merely Borel versions, global continuity across cells, or uniqueness
from a measure restricted to an isolated point is asserted.
The frozen branchwise continuous prescription owns the return values before the return is tested.

For \(z=(n,x)\) with \(x>0\), substituting \(Tz\) into (3) yields
\[
\kappa(z)=-\log J_{\theta_z}(Tz)=\log\frac n{S(n,a)x^2}.                 \tag{4}
\]
There is no \(\kappa\) on a missing terminal step.
In all four rows \(1\le S\le n\), so \(\kappa\ge0\).
Equality requires \(x=1,S=n\). Such a step enters a terminal; MAIN/H allow
it for every \(n\), D/Q only for \(n=1\).
Consequently this partial system is not supplied with a strictly positive
roof or a classical suspension. Its groupoid cocycle below has signed arrows.

## 4. Actual groupoid, finite branch pairs and all clock kernels

Let \(D_m\) be the Borel domain of \(T^m\), with \(D_0=Y\), and set
\[
A_m(z)=\sum_{i=0}^{m-1}\kappa(T^iz),\quad A_0=0,\quad
G=\{(z,m-\ell,w):z\in D_m,\ w\in D_\ell,\ T^mz=T^\ell w\}.              \tag{5}
\]
The source is \(w\), range \(z\); the Borel structure is inherited from \(Y\times\mathbb Z\times Y\).
The countable union in (5) is Borel. Every fibre is countable by the inverse table and finite iteration.
No germ quotient or freely generated arrow is added.

Multiplication adds lag; inverse swaps endpoints and negates lag.
To compose witnesses, align the depths at their common middle object to the larger depth.
That continuation already exists along the middle history, and equality transports it to the other endpoint.
This proves closure even at a terminal common future; nothing continues beyond the existing deeper history.
Identities include every terminal.

Define
\[
c(z,m-\ell,w)=A_m(z)-A_\ell(w).                                       \tag{6}
\]
For two witnesses of the same triple, the depths differ by the same integer \(r\).
The larger pair adds the same \(A_r\) at their shared future to both sums: (6) is well-defined everywhere.
The same alignment proves \(c(gh)=c(g)+c(h)\); inversion negates \(c\).
On each Borel witness chart it is Borel, hence it is Borel on \(G\).

For a legal history define
\[
\Delta_m(z)=\prod_{i=0}^{m-1}\frac{S_i x_i^2}{n_i}=e^{-A_m(z)},
\qquad \Delta_0=1,\quad T^iz=(n_i,x_i).                               \tag{7}
\]
It is the absolute derivative of the composed inverse history at the shared future.
Every actual arrow is covered by a pair of these inverse histories.
Their source-to-range IMAGE density is \(J_g=\Delta_m(z)/\Delta_\ell(w)=e^{-c(g)}\):
apply (3) successively, then change from common future to source.
This proves every-Borel IMAGE on every branch-pair domain and its Borel restrictions.
Derivative products are the frozen all-point completion, without a uniqueness claim for isolated charts.

The full clock kernel consists exactly of actual arrows with \(\Delta_m(z)=\Delta_\ell(w)\).
The lag kernel consists exactly of actual arrows with \(m=\ell\); their intersection requires both.
These criteria cover every legal finite history and source point, not just periodic data.
Word-label equalities do not enlarge either kernel.

## 5. Whole-source isotropy, heights, incoming and repetitions

The extension has all objects \(Y\times\mathbb R\) and arrows
\[
(w,h)\longrightarrow(z,h+c(g)),\qquad g:w\longrightarrow z.           \tag{8}
\]
Its operations are Borel and fibres countable. Jointly Borel translations \((z,h)\mapsto(z,h+t)\)
commute with arrows and descend to the quotient SET. No standard-Borel coarse quotient,
Hausdorff manifold, invariant flow measure or symplectic realization is asserted.

Source isotropy is zero unless the actual forward orbit is eventually periodic;
this includes every finite terminal history. A nonzero lag self-arrow equates two distinct
iterates, so determinism gives an infinite repeated tail.
If that tail has least period \(r\), isotropy is \(r\mathbb Z\): its \(r\) distinct cyclic states
force every repeat lag to be a multiple of \(r\), and every such multiple occurs.

For such a cycle \(z_0,\ldots,z_{r-1}\), put
\[
\tau=\sum_{i=0}^{r-1}\kappa(z_i).
\]
Each cycle point has \(0<x_i<1\), since \(x=0\) is terminal and \(x=1\)
enters a terminal. Equation (4) therefore makes every summand positive.
Preperiod sums cancel in a self-arrow, giving \(c(kr)=k\tau\).
Consequently the ENTIRE \(H_z=c(G_z^z)\) is \(\tau\mathbb Z\) on an
eventually periodic orbit, and \(\{0\}\) otherwise. All extension-object
isotropy is trivial: in the periodic case \(c\) is injective on \(r\mathbb Z\).
This is a conditional classification, not a census of other cycles.

The translation stabilizer is exactly \(H_z\) by (8); phases over a source orbit are \(\mathbb R/H_z\).
Periodic source orbits give primitive time \(\tau\) and repetitions \(k\tau\);
aperiodic and terminal orbits have no nonzero period. Equal times never identify distinct source orbits.

All incoming to \((z,h)\): choose every legal \(m\), every \(\ell\ge0\), and every predecessor
\(w\) from the iterated inverse table with \(T^\ell w=T^mz\).
Its source height is \(h-A_m(z)+A_\ell(w)\); count each actual triple once.
For a terminal \(z\), necessarily \(m=0\), so this retains all its finite
incoming histories at heights \(h+A_\ell(w)\), without a terminal self-loop.

## 6. Entire prescribed fixed-point probe and its full packet

In all four owners, \(B_{1,1}=\{1\}\times(1/2,1]\), \(d=R=S=1\), and
\(T(1,x)=(1,1/x-1)\). The fixed equation is \(x^2+x-1=0\).
Its sole admissible root is
\[
\alpha=\frac{\sqrt5-1}{2}\in(1/2,1),\qquad p=(1,\alpha).              \tag{9}
\]
The other root is negative; \(x=1\) maps to the terminal, and \(1/2\)
belongs to the next floor cell, not to this branch.
Thus (9) exhausts the requested fixed set, rather than selecting a centre.

The inverse \(\theta_{1,1}(1,y)=(1,1/(1+y))\) is defined on the whole
\(\{1\}\times[0,1)\). Its continuous IMAGE value at \(\alpha\) is
\[
J(\alpha)=(1+\alpha)^{-2}=\alpha^2,\quad
L=-2\log\alpha=\log\frac{3+\sqrt5}{2},\qquad \log2<L<\log3.             \tag{10}
\]
The inequalities follow from \(1<\sqrt5<3\), without numerical approximation.
Source isotropy at \(p\) is all \(\mathbb Z\), with \(c(p,k,p)=kL\), so the entire \(H_p=L\mathbb Z\).
Extension isotropy is zero and all phases form \(\mathbb R/L\mathbb Z\).
No smaller positive time or hidden packet exists. Since \(2<e^L<3\),
this primitive violates the frozen necessary target.

For each owner the full packet source orbit is
\(\mathcal O_p=\bigcup_{j\ge0}T^{-j}\{p\}\). This equality follows directly
from (5), since every forward iterate of \(p\) is \(p\).
All its incoming histories and phases are included by Sections 2 and 5.
No conclusion about fixed points outside \(B_{1,1}\) or other cycle lengths
is needed or asserted; target development stops at (10).

## 7. Complete own controls and the scope of the common failure

Sections 1 and 2 give each control's full autonomous map and every actual predecessor.
Equations (3)–(8) separately prove its own transport, versions, kernels, isotropy and phases.
The different incoming to the probe are exact:
D has only \(p\); H has all \((1,1/(a+\alpha))\), \(a\ge1\);
Q has all \((d,d/(d+\alpha))\), \(d\ge1\).
MAIN has only \(p\): its inverse table at root 1 has \(k=1\) and
\(d\alpha<1\), which forces \(d=1\) because \(\alpha>1/2\).
For H and Q every further ancestor is retained by their own inverse table, not MAIN's singleton orbit.
All four have entire probe \(H=L\mathbb Z\): four owner diagnoses, not four packets credited to MAIN.

The unit branch contains no nontrivial gcd information. Its common failure cannot validate naturalness:
it is a PROVES_TOO_MUCH control against interpreting an owned reciprocal clock as a prime mechanism.
No probability reweighting, null-point edit, time rescale or prime selection altered the obstruction.

## 8. Decision, evidence and integrity

T0 carrier/transport ownership and the specified all-point clock are established.
T1 has an explicit coupled divisibility interface; strong naturalness remains OPEN.
T2's owned primitive violates its necessary arithmetic target: STOP / FORK. Same-object ledgers intact.
T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.

Proofs use the [frozen card](candidate-card.md) and exact algebra/change of variables.
[Claims and limits](claim-ledger.md) and the [overview](README.md) are the companion records.
No scientific numerical run, finite orbit survey, external citation or literature-priority claim was used.
Definition-stage comparison read only 299-card 1–87 and 313-card 1–102;
heading discovery also exposed their outcome titles and 313's status line.
Neither comparator supplies a theorem or clock here.
No evidence/raw/peer or other new manuscript was read by this author.
AI-assisted shared-history conceptualization, formal analysis and writing are internal and NOT_CALIBRATED,
not independent or external peer review.
Data availability: all definitions and exact proofs are in this package.
Human-subject ethics: not applicable. Funding and conflicts: not supplied;
no unsupported assertion of funding or conflict absence is made.
