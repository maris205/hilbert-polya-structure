# First-return clocks preserve core periods, not deleted ownership

Candidate: `ANG-AUDIT-20260923-FRC01`; batch NONLINEAR-PACKET-20260923-L.
outcome: FIRST-RETURN CLOCK INVARIANCE ESTABLISHED; CORE-DELETION CONTROL — CONDITIONAL AUDIT / FORK

## Abstract and scope

For a frozen partial Borel source with a prescribed all-point inverse IMAGE
clock, first return to a section has the integrated clock. Its retained-lag
groupoid embeds in the parent reduction, preserving clock values but not
integer-lag coordinates. A post-meeting-return condition makes this embedding
surjective. A periodic core meeting the section has the same entire clock
group and primitive time after induction. Merely meeting every parent
groupoid orbit is insufficient: an explicit full-source control has a complete
orbit section but no induced nonunit arrows, and loses the parent's periodic core.
These are conditional ownership results, not a new arithmetic candidate or
a universal impossibility theorem.

The [frozen card](candidate-card.md) and its CP1 append specify the object.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED;
Route B NOT INVOKED. No operator or determinant is supplied.

## 1. Parent object and all-point clock

Let X, mu, T and its disjoint countable legal Borel pieces P_i be exactly
as frozen. Every actual inverse theta_i has a fixed positive finite Borel
J_i on its actual target domain, including null sets, and
\[
 \mu(\theta_i E)=\int_E J_i\,d\mu                         \tag{1}
\]
for every Borel E. All X outside the legal domain remain terminal objects,
with identities and actual incoming; no self-loop is added.
Define kappa(x)=-log J_i(Tx) for x in P_i and legal sums S_n.
There is no step clock at a terminal; this is not a missing numerical value
on an existing edge.

The actual relation is
\[
 G_T=\{(x,m-n,y):T^m x=T^n y,\ m,n\geq0\},
 \qquad c_T=S_m(x)-S_n(y).                             \tag{2}
\]
An arrow goes from y to x. Equal triples, not presentations, identify arrows.
For another presentation with the same lag, both exponents change by the
same integer. Extend the shorter two histories: their common endpoint
adds the same S on both sides, proving descent. To compose arrows, extend
the shorter history at their common middle object to the longer one;
the same cancellation proves additivity. Partial domains cause no problem:
the longer middle history supplies exactly the required continuation.
Countably many Borel equality relations make G_T Borel.

The lag kernel M is the arrows represented with equal exponents.
The clock kernel K is the arrows with S_m(x)=S_n(y); their intersection
imposes both requirements. These exact conditions apply to the full source,
not only periodic or recurrent points. The extension is the full
X times R with (y,h)->(x,h+c_T).

A terminal-ending or non-eventually-periodic history has trivial source
isotropy and H=0. If x eventually enters a least-q cycle O, put
\[
 C_O=\sum_{z\in O}\kappa(z).
\]
Its source isotropy is q Z and c_T(aq)=a C_O, hence H=C_O Z.
Indeed a nonzero retained isotropy implies equality at two different legal
times, hence eventual periodicity; on a least-q tail the admissible time
differences are exactly q Z. The extension isotropy is zero if C_O!=0,
and q Z if C_O=0. H=0 does not delete that ineffective isotropy.
The least positive primitive is |C_O| when C_O!=0; repetitions are its
integer multiples. Different eventual cycles are different source packets.

For explicit phases choose z_0 on O and suppose T^ell x=T^i z_0.
Every extended point over this packet has canonical phase
\[
 h-S_\ell(x)+S_i(z_0)\quad\bmod C_O\mathbb Z.           \tag{3}
\]
When C_O=0 the phase is real, not a circle. Every legal finite predecessor
and every real h occurs. Nonperiodic packets likewise retain all their
heights, with equivalence exactly (2), and have no positive period.

## 2. First-return IMAGE and integrated clock

B is a fixed Borel section, mu_B=mu restricted to B. For each x in B
with a future visit, r(x) is the least positive legal time of that visit;
R(x)=T^{r(x)}x. Other B points are R terminals. First-return domains are
Borel because the finitely many legal intermediate iterates avoid B.

Partition D_B by return length and the finite parent branch itinerary.
Each piece is injective and its actual inverse is the reversed composition
of the parent inverses, restricted to endpoints in B and all intermediate
points outside B. This enumerates ALL inverse words, not selected returns.
If z_0,...,z_n is such a legal forward segment, its inverse density is
\[
 J_R(z_n)=\prod_{j=0}^{n-1}J_{i_j}(z_{j+1}).           \tag{4}
\]
To prove IMAGE, (1) first gives the corresponding weighted change-of-variable
identity for indicators, then nonnegative simple functions and their
monotone limits. Apply this identity successively to the inverse composition.
Restricting endpoints/intermediate domains is just restricting the Borel
integrands. This proves every-Borel IMAGE under mu_B. The product is positive
and finite at every actual point by the frozen versions; a null B does not
allow (1) alone to choose different pointwise products.

Taking negative logs of (4) gives exactly
\[
 \rho(x)=S_{r(x)}(x).                                 \tag{5}
\]
This is an integrated parent clock, neither one unit per return nor a
rescaled copy of the initial step. Formula (2), applied to R and rho, supplies
the induced G_R, kernels and all heights, with its own return-count lag.

## 3. The lag-changing embedding and sufficient surjectivity

For legal R^m x define r_m(x)=sum_{j<m} r(R^j x), r_0=0.
For an induced meeting define
\[
 \Phi(x,m-n,y)=(x,r_m(x)-r_n(y),y).                    \tag{6}
\]
Both parent histories end at the same point. If an induced presentation
is extended equally, both accumulated parent times acquire the same
increments after its common endpoint, so (6) is well-defined. This also
proves compatibility with composition. Telescoping (5) yields
c_T(Phi(g))=c_R(g) at every arrow.

This preserves the clock kernel on the image, but not generally the lag
kernel: an equal-return-count arrow can have unequal accumulated base times.
No identification of lag kernels or their intersections is inferred.

For injectivity fix x,y and two induced meetings (m,n),(p,q) with equal
parent time difference. Suppose m>=p. The equality then implies n>=q.
Starting at R^p x=R^q y, the equal additional parent duration reaches the
same endpoint along its unique forward history. Counting all intervening
first returns gives m-p=n-q. Thus the two induced lags coincide.
The cases m<p are symmetric. This proves injection, not identity of lag.

Under PMR every parent meeting u=T^k x=T^l y with x,y in B has a legal
future visit T^s u in B, s>=0. The two total times k+s and l+s are visit
times from B, hence equal r_m(x),r_n(y) for some m,n. The induced arrow
(x,m-n,y) maps under (6) to (x,k-l,y), with the same clock but not
necessarily the same lag. Therefore
\[
 \mathrm{PMR}\ \Longrightarrow\ \Phi(G_R)=G_T|_B.       \tag{7}
\]
Only sufficiency is asserted. B meeting every parent orbit is a different
condition and cannot replace PMR, as Control C proves below.

## 4. Periodic cores, whole H and full-source ownership

A least-q parent cycle O meeting B has k=|O intersect B|>=1 distinct section
points. First return traverses them in cyclic order, giving least induced
period k; no smaller return-count period can repeat one before all k visits.
The successive first-return segments partition the q parent steps, so the
induced cycle sum is exactly C_O. Source lag isotropies change from q Z to
k Z, while ENTIRE H=C_O Z and extension isotropy have the same clock test.
The phase identification is (3) using the integrated segments. In particular
a multiple of log p cannot be repaired by dividing it by the return length.

Conversely every induced cycle gives a parent periodic core meeting B.
A section point that eventually enters a parent core meeting B makes
infinitely many section returns, so its full induced eventual packet is
exactly the parent packet restricted to B. All such incoming points and
heights are retained. Thus actual core intersection suffices for this
periodic-packet statement without imposing PMR everywhere.

If every parent periodic core meets B, all parent periodic packets are
represented and their primitive times/multiplicities persist. If a core
misses B, an incoming point in B does not replace that core; the induced
source may lose the entire period. Under both PMR and a full parent-orbit
section, (7) also represents every parent source orbit with its H via
clock-preserving conjugation of isotropy. These are separate hypotheses,
not an assertion that every chosen section preserves a full ledger.

## 5. Control A — acceleration changes lag, not time

Own source {0,1} times R, counting times Lebesgue, total
T(j,x)=(1-j,2x). The inverse switches the label and divides by2.
Its one-dimensional inverse derivative gives J=1/2 everywhere; a change
of variables on each labelled line proves IMAGE for every Borel set.
Thus kappa=log2. No null-point convention is imported.

For all integer k,
\[
 ((j,x),k,(l,y))\in G_T
 \iff l=j+k\pmod2,\quad y=2^k x,\qquad c=k\log2.       \tag{8}
\]
This follows from the total bijection and proves completeness, including
negative histories. M=K=M intersect K consists of units. The only periodic
core is ((0,0),(1,0)), least period2; scaling forbids every nonzero periodic
point. Its full incoming packet consists of these two points alone.
Source isotropy is 2 Z there and zero elsewhere, H=log4 Z there, and all
extension isotropy is trivial. Zero-packet phase is h+j log2 modulo log4.

For nonzero x put n=floor(log_2|x|), u=2^{-n}|x| in [1,2).
An orbit representative is (j-n mod2,sign(x)u); its real phase is
h+n log2, with no positive period. This parametrizes every other object.

For section B={0} times R, r=2 everywhere and R(x)=4x, with own inverse
J_R=1/4, rho=log4 and every-Borel restricted IMAGE.
Induced arrows are (x,l,y) with y=4^l x, c=l log4; kernels are units.
Only x=0 has isotropy Z and H=log4 Z; extension isotropy is trivial.
All nonzero induced orbits have real phases h+n log4 using normalization
|x|=4^n u, 1<=u<4. Phi sends l to2l and is onto the full reduction.
The same single zero packet survives; changing least discrete period from2
to1 has not turned its composite primitive log4 into log2.

## 6. Control B — omitted component is omitted ownership

Own source {0,1} times R, total T(j,x)=(j,b_j x), b_0=2,b_1=3.
Each inverse stays in its label and divides by b_j. Own IMAGE gives
J_j=1/b_j, kappa=log b_j at EVERY point.
The complete relation is same label, y=b_j^k x, with c=k log b_j.
All kernels are units. At each (j,0) source isotropy is Z, H=log b_j Z
and extension isotropy zero; these are two different singleton packets.
All other points have trivial isotropy/H and no period. All incoming is
the unique inverse orbit; phases normalize |x|=b_j^n u, 1<=u<b_j,
to h+n log b_j; at zero the phase is h modulo log b_j.

The section {0} times R has r=1, R=2x, own J_R=1/2 and the complete
label0 formulas just given. PMR holds within that section, but it is not a
full orbit section and misses the second periodic core. Its single log2
packet cannot be presented as the full parent's two-packet ledger.
This is deletion, not improvement in the parent mechanism.

## 7. Control C — full orbit section still misses a periodic core

Own source {a,b,t} times R, counting-Lebesgue, with
T(a,x)=(t,2x), T(b,x)=(t,3x), T(t,x)=(t,2x).
All parent points are legal. A target (t,w) has precisely
(a,w/2),(b,w/3),(t,w/2) as predecessors; targets of labels a,b have none.
The three separate injective branches have own J=1/2,1/3,1/2 and IMAGE.
Their images overlap, so a forward-union measure is not the sum of the
three image measures. Kappa equals log2,log3,log2 on the respective labels.

Set Q(a,x)=Q(t,x)=x, Q(b,x)=3x/2, and delta_a=delta_t=0,
delta_b=log(3/2). For ALL x,y and integer k the exact relation is
\[
 (z,k,w)\in G_T\iff 2^k Q(z)=Q(w),\qquad
 c=k\log2+\delta_z-\delta_w.                           \tag{9}
\]
Necessity follows by advancing any meeting one extra step into label t.
For sufficiency choose nonnegative m,n with m-n=k and both >=1;
T^m z=(t,2^m Q(z)) and T^n w=(t,2^n Q(w)).
The clock follows S_m(z)=m log2+delta_z for m>=1; shorter meetings have
the same value by descent.

M is k=0,Q(z)=Q(w). K requires k=0 and delta_z=delta_w in addition:
no integer power of2 equals3/2 or2/3. Thus K contains exactly same-coordinate
arrows among labels a,t and units on b; K is contained in M.
Source isotropy is Z precisely at (a,0),(b,0),(t,0), and trivial elsewhere.
Those three points form ONE full incoming packet with core (t,0), H=log2 Z,
extension isotropy zero, and phase h-delta_z modulo log2.
No other periodic or eventually-periodic source points exist because a,b
feed t in one step and nonzero doubling cannot return.
For nonzero Q(z)=2^n sign(Q)u, 1<=u<2, the canonical representative is
(t,sign(Q)u) with real phase h+n log2-delta_z.
Formula (9) also retains every incoming branch and every real height.

Take B={a,b} times R. Every parent groupoid orbit meets B: each (t,w)
has predecessor (a,w/2); all a,b points are already in B. Nevertheless
no B point EVER returns to B. R has empty legal domain, all B points
remain terminal, its groupoid and both kernels consist only of units,
c_R=0 on units, all source/extension isotropy trivial and H=0 everywhere.
There is no step rho to assign, and every (z,h) is its own extended class;
height translation has no nonzero period.

The parent reduction G_T|B retains (9), including nonunit coalescences and
all isotropy at (a,0),(b,0), whereas Phi(G_R) contains only units.
PMR fails at all meetings in label t. The only parent core lies outside B.
This proves the advertised distinction without deleting the parent or
calling an undefined edge clock zero.

## 8. Consequences, limits and reproducibility

The prime-symbolic lineage application is conditional: a previously admitted
divisor-symbolic/geometric owner may be accelerated only with its own exact
return law and integrated clock. No result here admits generic controls as
an arithmetic source. Control A prevents division of period by visit count;
B shows component loss; C shows that even a complete orbit section can lose
a core. Missing cores block a claim of preserving the full periodic ledger.
Failure of the sufficient PMR test alone leaves equality with the parent
reduction unresolved; a separate argument is needed to establish or refute it.

Established: inverse-word IMAGE, clock-preserving injection, PMR sufficiency,
whole-H invariance for cores meeting the section, and full exact controls.
OPEN: naturalness/existence of an arithmetic owner satisfying the full prime
target. No numerical experiment, finite cutoff, precision estimate, external
source theorem, operator, determinant or formal Route evaluation was used.
Methods are the exact identities (1)–(9), with all inputs in the frozen card;
outputs are this paper, [ledger](claim-ledger.md) and [README](README.md).
Mechanical Markdown/hash checks cannot prove these mathematical statements.

AI assistance disclosure: root AI performed the derivation and drafted this
paper; another AI agent independently derived from the frozen card before
manuscript access, then internally reviewed the manuscript. Shared model and
history remain NOT_CALIBRATED, not blind, cross-model or external peer review.
No human or external mathematical verification is certified. Root's informal
pre-freeze control algebra and scoped197 card read are disclosed in the card;
no old analytic operator or proof is transferred. Reviewer evidence is kept
separately and was not read during this author's derivation. After the raw
froze and root read it fully, manuscript wording was sharpened to distinguish
clock kernels from lag kernels and PMR sufficiency from necessity.

Portfolio: FORK. Retain this conditional filter; do not repair a failed
candidate by deleting its core or rescaling a return clock. Any new source
or section presented as a new owner needs a fresh card and authorization.
