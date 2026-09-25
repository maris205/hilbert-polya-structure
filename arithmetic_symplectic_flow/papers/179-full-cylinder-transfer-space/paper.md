# A full finite-cylinder RKHS for the ordered source's ordinary transfer determinant

**Paper ID:** 179-full-cylinder-transfer-space  
**Candidate ID:** ANG-20260915-FCT01  
**Date:** 2026-09-15  
**Status:** ADVANCE — INJECTIVE FULL-CYLINDER RKHS AND OWNED TRACE-CLASS DETERMINANT; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

For the complete ordered divisibility-cover source, we construct the
frozen coefficient Hilbert space of all finite cylinder indicators.
Every coefficient vector gives a bounded continuous observable and
the realization is injective: infinite branching and finite subtree
energy exclude the formal parent/children relations from its kernel.
The resulting reproducing-kernel Hilbert space contains every finite
cylinder and distinguishes all one-sided histories. The actual full
predecessor transfer, with the same scale-return roof, preserves this
space and is ordinary trace class for Re s>3/2. A trace-norm sequence
of genuine finite-rank operators proves all power traces and the
Fredholm determinant; higher-depth columns lower depth and contribute
no additional trace cycles. At z=1 the determinant equals the
reciprocal of the complete scale flow's orbit product. The strong
ordinal weights and the ordering/scale law are declared engineering.
The space is still a proper subspace of bounded continuous functions,
the half-plane is only sufficient, and arithmetic naturalness is OPEN.
The scalar product extends to Re s>1, but no operator extension,
continuation beyond the product domain, new geometric owner or formal
Route pass is established.

## 1. Frozen question, lineage and same-object ledger

The [version-1 card](candidate-card.md) fixes all definitions before
proof. The new question is whether an injective observable space
containing **every finite cylinder**, rather than only the first-symbol
space of [174](../174-ordered-source-transfer-determinant/paper.md),
can carry this same source's actual ordinary transfer determinant.
The source and scale law are explicitly restated; the new Hilbert
norm and representation receive a new ID and are proved here.

| Item | ANG-20260915-FCT01 owner | Boundary |
| --- | --- | --- |
| Arithmetic | Strict covers of positive-rational integer divisibility | Atoms derived, not supplied as a prime table |
| Source | Entire nondecreasing one-sided and bilateral atom words | Every admissible mixed history retained |
| Flow and roof | Full bilateral scale quotient Q and actual section r=1 | The roof is derived from its fixed scale law |
| Observable representation | Unique finite-energy expansion in all finite cylinders plus 1 | All futures separated; not all continuous functions |
| Operator | Full predecessor transfer in that representation | Ordinary trace class proved on Re s>3/2 |
| Trace and determinant | Ordinary Hilbert traces and det(I-zT_s) | No flat trace, regularization or diagonal replacement |
| Orbit comparator | All oriented primitive Q-circles and positive traversals | Complete multiplicity and unchanged clock |
| Classical/later geometry | NOT APPLICABLE / NOT SUPPLIED | No operator on 171, 176 or 177 |

The [prior-work lineage](../../docs/prior_work/README.md) is divisor
exclusion -> multiplicative cover indecomposability -> ordered
symbolic admissibility -> its scale flow -> a full finite-cylinder
transfer representation. This advances the symbolic-observable side
of the lineage; it does not pretend to be a new Logistic/Henon
realization, chronological sieve, or classical symplectic lift.

## 2. Complete source, inverse histories, clock and orbit ledger

Write x <=_D z if z/x is a positive integer, and use its strict covers.
If a cover ratio n factors n=uv with u,v>=2, then ux is intermediate.
Conversely any intermediate supplies that factorization. Thus the
set A of cover ratios consists exactly of integer irreducibles, the
primes. There are infinitely many: from a finite list, the product
plus one has an irreducible divisor outside it. Enumerate increasingly
a_1,a_2,... . Since these are distinct integers >=2, a_j>=j+1.
No numerical atom list or prime-count estimate is used.

Give A its discrete topology, and freeze

\[
Y_+=\{x\in A^{\mathbb N_0}:x_i\le x_{i+1}\},\qquad
Y_{\mathbb Z}=\{b\in A^{\mathbb Z}:b_i\le b_{i+1}\}.
\tag{1}
\]

S and F are respectively the one-sided and bilateral left shifts.
The complete S-preimage of x is exactly ax with a<=x_0 in A.
This is a finite set, and S is onto by prepending x_0.

The entire inverse limit
\(\widehat Y=\{(x^{(m)})_{m\ge0}:Sx^{(m+1)}=x^{(m)}\}\)
is homeomorphic to Y_Z: put x^(m)_k=b_(k-m). Conversely use
b_k=x^(0)_k for k>=0 and b_-m=x^(m)_0 for m>=1.
Compatibility verifies all coordinates and inequalities. Both maps
are continuous coordinate maps and interchange the inverse-limit
homeomorphism with F. No history is selected. The future projection
pi_+(b)=(b_0,b_1,...) is onto, intertwines F with S, and can forget
past information.

Set y_0=1, y_(m+1)/y_m=b_m for all integers m. The finite products
identify the full normalized rational cover-chain source. Define

\[
G(b,r)=(Fb,r/b_0),\quad
Q=(Y_{\mathbb Z}\times\mathbb R_{>0})/\langle G\rangle,\quad
\Phi^t[b,r]=[b,e^tr].
\tag{2}
\]

For all integers m, \(G^m(b,r)=(F^m b,r/y_m)\).
In log r coordinates each nonzero iterate changes the coordinate
by at least |m| log2, with sign opposite m. The action is free.
Bounded log-scale neighborhoods have only finitely many potentially
intersecting translates. For two inequivalent points, separate each
such pair by Hausdorff neighborhoods and intersect the finite
choices; the open saturated neighborhoods are disjoint. Hence Q is
Hausdorff. The quotient projection is open, scale multiplication
commutes with G, and the descended flow is jointly continuous for
all real t. No local-compactness hypothesis is needed or asserted.

The values y_m strictly increase from zero to infinity. Every r
has a representative 1<=r<b_0 after a unique appropriate iterate.
The closed strip has seam (b,b_0)~(Fb,1). A log-scale strip of
width less than log2 has no self-identification, so r=1 is an
embedded section. Its first positive return is F at time

\[
\tau(b)=\log b_0=\tau_+(\pi_+b),\qquad \tau_+(x)=\log x_0.
\tag{3}
\]

All consecutive crossing times are separated by at least log2;
there is no forward or backward Zeno accumulation. Equation (3)
holds on all histories, not merely on periodic words. The units
exp(t) are a frozen design input; no prime-specific roof is added.

A positive time t closes [b,r] precisely when F^m b=b and
e^t=y_m for an integer m>0. The cyclic inequalities force every
entry of b to equal one atom a. Conversely its time stabilizer is
(log a) Z. All its scales form one oriented primitive circle, and
distinct constants are not identified. Thus the full Q-ledger is
one primitive circle per a, time log a, with all times k log a
for its positive repeated traversals. Mixed states are retained
and aperiodic. Similarly Fix(S^k) contains precisely the constant
words for every k>=1. Each has exactly one F^k-periodic past,
though it can have nonperiodic pasts; periodic multiplicity is
neither multiplied nor lost by the one-sided presentation.

## 3. Frozen coefficient space and its first decisive gate

Let W be the empty word and all finite nondecreasing atom words.
For w of length k, phi_w is the first-k-symbol cylinder indicator;
phi_empty=1. Denote the raw coefficient unit vector by e_w.

For an index word (j_1,...,j_k), code(w) is the positive integer
whose binary expansion is a leading 1 followed by j_1 ones then
0, ..., j_k ones then 0; code(empty)=1. After the leading 1,
the zero-terminated unary groups are uniquely parsed. This is an
injection on all finite positive-index words, hence on W, without
using atom values. In particular only finitely many codes are <=N.
Every index appearing in a nonempty w is strictly less than code(w).

Freeze exactly

\[
\rho_\emptyset=\rho_{(a)}=1,\qquad
\rho_w=4^k(1+\operatorname{code}(w))^4\rho_{\operatorname{tail}(w)}
\quad(k\ge2),\qquad H=\ell^2(W,\rho).
\tag{4}
\]

All rho_w>=1, and rho_w>=4^k for k>=2. The proposed realization is

\[
(Jc)(x)=\sum_{w\in W}c_w\phi_w(x).
\tag{5}
\]

### Proposition 1 — Bounded continuous realization and injectivity

Equation (5) defines a bounded linear injection H -> C_b(Y_+),
with sup norm at most C_0 times the H-norm, where
\(C_0=\sqrt{25/12}\). The image, with its transported norm, is an
RKHS containing every finite cylinder and separating every pair
of distinct one-sided histories.

**Proof.** At any x, only the empty word and its unique prefix
of each positive length contribute. Cauchy--Schwarz gives

\[
\sum_{w\preceq x}|c_w|
\le\|c\|_H\left(\sum_{w\preceq x}\rho_w^{-1}\right)^{1/2},
\qquad
\sum_{w\preceq x}\rho_w^{-1}
\le 1+1+\sum_{k\ge2}4^{-k}=\frac{25}{12}.
\tag{6}
\]

Here w preceq x includes the empty prefix. Arbitrary finite
coefficient exhaustions converge in H, hence uniformly under (6).
Their images are finite sums of clopen cylinder indicators.
Therefore Jc is bounded and continuous, and all evaluations are
bounded by C_0.

To prove injectivity, suppose Jc=0. For a finite admissible prefix
u, including the empty one, write

\[
P(u)=\sum_{v\preceq u}c_v.
\]

Each u has infinitely many admissible next symbols a_j. Let W_(u,j)
be all finite words beginning with u a_j, and define their energy
E_(u,j)=sum_(w in W_(u,j)) rho_w |c_w|^2. For fixed u these sets
are pairwise disjoint, so sum_j E_(u,j)<=||c||_H^2 and
E_(u,j)->0 as admissible j->infinity. Evaluate Jc at the actual
admissible history x^(u,j)=u a_j a_j a_j ... . All terms after
prefix u lie in W_(u,j), and (6) bounds their sum in absolute
value by C_0 sqrt(E_(u,j)). Consequently

\[
|P(u)|\le C_0\sqrt{E_{(u,j)}}\longrightarrow0.
\tag{7}
\]

Thus P(u)=0 for every u. First c_empty=P(empty)=0; then
c_u=P(u)-P(parent(u))=0 for every nonempty u. The formal infinite
parent/children relations therefore create no coefficient kernel.

Transport the complete Hilbert norm to JH. Bounded evaluations
make it an RKHS with reproducing kernel

\[
K(x,y)=\sum_{w\in W}
\frac{\phi_w(x)\overline{\phi_w(y)}}{\rho_w}.
\tag{8}
\]

The series is absolutely bounded by (6), and its coefficient
representer has finite H-norm. Each phi_w=Je_w belongs because
rho_w is finite. Distinct histories differ in a finite coordinate;
their corresponding finite-prefix indicator separates them. QED.

Here every finite cylinder means an exact finite-coordinate event.
If only some coordinates are specified, its last specified atom
bounds all earlier coordinates by one finite initial segment of A;
the event is therefore a finite union of prefix cylinders. Their
indicators and finite linear combinations belong to JH. This does
not include arbitrary infinite unions of atom cylinders, or every
bounded observable depending on finitely many coordinates.

This space is **proper even in C_b(Y_+)**. Partition all nonempty
words by their first symbol a_j and use the same energy estimate:
for every c in H,

\[
(Jc)(a_j,a_j,\ldots)\longrightarrow c_\emptyset
\quad(j\longrightarrow\infty).
\tag{9}
\]

The bounded continuous observable h(x)=(-1)^j when x_0=a_j fails
this property and cannot belong to JH. Separation of histories is
not representation of all continuous functions or their algebra.
Nor does it recover the past discarded by pi_+.

## 4. Actual full transfer and ordinary trace class

On C(Y_+) define the pointwise finite predecessor sum

\[
(\mathcal L_s h)(x)
=\sum_{a\le x_0}e^{-s\tau_+(ax)}h(ax)
=\sum_{a\le x_0}a^{-s}h(ax).
\tag{10}
\]

The real logarithm fixes a^-s. On a neighborhood with x_0 fixed
this is a fixed finite sum of continuous prefix maps, so it is
continuous. For Re s>1 it is also bounded on C_b with sup norm
at most sum_a a^-Re(s); we make no trace-class claim on C_b.

Decompose H=V plus its orthogonal complement, where V is the
closed span of e_empty and all e_(a_j), isometric to C plus ell2.
Extend the following functionals by zero on higher-depth vectors:

\[
\psi_j=e_\emptyset-\sum_{i<j}e_{(a_i)},\qquad
\ell_j(c)=c_\emptyset+c_{(a_j)}.
\tag{11}
\]

Their actual function images satisfy J psi_j=1_(x_0>=a_j).
For a word w=(a,v) of length at least two, direct substitution in
(10) gives

\[
\mathcal L_s\phi_w=a^{-s}\phi_v.
\tag{12}
\]

The admissibility a<=v_0 is already part of w. At a history in
the v-cylinder the unique relevant predecessor is a; outside that
cylinder none contributes. For length-one words,
L_s phi_(a_j)=a_j^-s J psi_j; also
L_s 1=sum_j a_j^-s J psi_j, pointwise a finite sum.
These identities include all predecessors.

### Proposition 2 — Full invariant RKHS and trace-class family

For Re s>3/2 the actual operator is

\[
T_s=A_s+R_s,\qquad
A_s=\sum_{j\ge1}a_j^{-s}\psi_j\ell_j,\qquad
R_s=\sum_{\substack{w=(a,v)\in W\\ |w|\ge2}}
a^{-s}e_v\,\epsilon_w,
\tag{13}
\]

where epsilon_w(c)=c_w. Both series converge in ordinary trace norm
on the same entire H, and L_s J=J T_s. The family is holomorphic
in trace norm on this sufficient half-plane.

**Proof.** Since the coefficients in V have weight one,
||psi_j||=sqrt(j) and ||ell_j||=sqrt2, exactly. Thus

\[
\|A_s\|_1
\le\sqrt2\sum_{j\ge1}\sqrt j\,a_j^{-\sigma}
\le\sqrt2\sum_{j\ge1}\sqrt j\,(j+1)^{-\sigma}<\infty,
\qquad \sigma=\Re s>3/2.
\tag{14}
\]

For a long word w=(a,v) of length k, the norm of its rank-one
column is exactly

\[
|a^{-s}|\|e_v\|\,\|\epsilon_w\|
=a^{-\sigma}\sqrt{\frac{\rho_v}{\rho_w}}
=a^{-\sigma}2^{-k}(1+\operatorname{code}(w))^{-2}.
\tag{15}
\]

By injectivity of code and k>=2, for sigma>0 its sum is at most

\[
\frac14\sum_{n\ge1}(1+n)^{-2}<\infty.
\tag{16}
\]

These are full output columns; no cylinder tail is removed.
Trace class is a Banach ideal, so (14)--(16) construct the bounded
operator (13). Its finite-vector action is exactly (10)--(12).
For general c, choose finite coefficient truncations c^(m)->c.
Then Jc^(m)->Jc uniformly, JT_sc^(m)->JT_sc uniformly, and at each
x the finite predecessor sum converges. Hence L_sJc=JT_sc
everywhere. Injectivity makes this the unique realized operator.

On each compact subset of Re s>3/2, (14)--(16) give uniform
summable majorants, while each rank-one summand is entire in s.
The trace-class-valued series is therefore holomorphic there.
This proves sufficiency only, not the optimal domain. QED.

In particular T_s is not a diagonal assigned to constant words:
it maps e_(a_j) to a_j^-s psi_j and every nonempty higher cylinder
to its actual suffix. The empty-vector interaction is essential.
It cannot be dropped while retaining (10).

The standard trace-ideal bound, ordinary trace continuity and
finite-rank Fredholm determinant limit used below are recorded in
[Bornemann, Sections 2--3, equations (2.3)--(2.5) and (3.2)](https://arxiv.org/pdf/0804.2543).
Only those functional-analysis facts are invoked; the source,
injectivity, columns and finite invariant spaces are proved here.

## 5. Exact finite-rank limits, all power traces and the determinant

Use the finite-rank operators on the same full H

\[
T_{s,N}=A_{s,N}+R_{s,N},\quad
A_{s,N}=\sum_{j=1}^N a_j^{-s}\psi_j\ell_j,\quad
R_{s,N}=\sum_{\substack{|w|\ge2\\\operatorname{code}(w)\le N}}
a(w)^{-s}e_{\operatorname{tail}(w)}\epsilon_w ,
\tag{17}
\]

where a(w) is the first atom. Their complete output vectors remain
unchanged. Equations (14)--(16) give the explicit error estimate

\[
\|T_s-T_{s,N}\|_1
\le\sqrt2\sum_{j>N}\sqrt j\,a_j^{-\sigma}
+\sum_{\substack{|w|\ge2\\\operatorname{code}(w)>N}}
a(w)^{-\sigma}2^{-|w|}(1+\operatorname{code}(w))^{-2}
\longrightarrow0.
\tag{18}
\]

### Proposition 3 — Higher-depth observables add no closed trace cycles

For every k>=1, Re s>3/2 and z in C,

\[
\operatorname{tr}_H(T_s^k)=\sum_{j\ge1}a_j^{-ks},\qquad
D(s,z)=\det_H(I-zT_s)=\prod_{j\ge1}(1-za_j^{-s}).
\tag{19}
\]

**Proof.** First E_N^0=span(psi_1,...,psi_N) is N-dimensional:
psi_1=e_empty and psi_(j+1)-psi_j=-e_(a_j).
It is the range of A_(s,N), since the functionals ell_1,...,ell_N
are jointly onto C^N. Moreover

\[
\ell_i(\psi_j)=1_{i\ge j},\qquad
[A_{s,N}|_{E_N^0}]_{ij}=a_i^{-s}1_{i\ge j}.
\tag{20}
\]

Thus the finite invariant range matrix is lower triangular with
diagonal a_1^-s,...,a_N^-s.

For the full T_(s,N), let E_N contain e_empty, all e_(a_j) with
j<=N, and e_v for every proper suffix v of length >=2 of a long
word w with code(w)<=N. This is a finite-dimensional space.
Every atom index in such a w is <code(w)<=N, so every length-one
output is among its declared low vectors. The range of T_(s,N)
lies in E_N. The space is invariant: A_(s,N) has its range in
E_N^0, while R_(s,N) either kills a coefficient vector or sends
it to a shorter suffix already in E_N.

On the low subspace V_N=span(e_empty,e_(a_1),...,e_(a_N)),
R_(s,N)=0. The restriction of A_(s,N) has invariant range E_N^0
and one extra zero quotient direction. On the remaining finite
depth filtration, R_(s,N) strictly lowers length. Therefore,
in a basis ordered by depth, the finite matrix on E_N has the
low block from (20), zero extra diagonal directions, and strictly
depth-lowering off-diagonal blocks. All its positive power traces
and its determinant are consequently

\[
\operatorname{tr}(T_{s,N}^k)=\sum_{j=1}^N a_j^{-ks},\qquad
\det(I-zT_{s,N})=\prod_{j=1}^N(1-za_j^{-s}).
\tag{21}
\]

These are also the full-H trace and determinant: since E_N contains
the range, the operator has block form [[B,C],[0,0]] relative to
E_N and its orthogonal complement. No compression of the actual
source or choice of periodic sector is involved.

The trace-norm convergence (18) and a common bound B for all
operator norms imply by telescoping and the ideal inequality

\[
\|T_s^k-T_{s,N}^k\|_1
\le k B^{k-1}\|T_s-T_{s,N}\|_1\longrightarrow0.
\tag{22}
\]

Ordinary trace continuity gives the first equality in (19).
The finite-rank determinant continuity theorem gives the second
for every z, locally uniformly. Its product is locally uniformly
convergent on {Re s>3/2} times C because sum_j a_j^-sigma is
locally uniformly finite. Thus D is jointly holomorphic there
and entire in the auxiliary variable z. QED.

The trace's periodic interpretation is exact. Iterating (10)
includes every length-k admissible predecessor word with weight
equal to exp(-s times the sum of its predecessor roofs).
A closed nondecreasing path must be constant. Section 2 proves
that these and only these are Fix(S^k), each with its unique
periodic bilateral lift. Hence

\[
\operatorname{tr}_H(T_s^k)
=\sum_{x\in\operatorname{Fix}(S^k)}
\exp\left(-s\sum_{m=0}^{k-1}\tau_+(S^m x)\right).
\tag{23}
\]

Higher cylinders distinguish previously invisible future histories
and have nonzero transfer action, but cannot form a depth cycle.
This is proved by the complete finite-rank limit, not an informal
assertion that a triangular infinite matrix has its diagonal trace.

For sigma>3/2 the absolute double sum obeys

\[
\sum_{k\ge1}\frac1k\sum_j|a_j^{-ks}|
\le\frac1{1-2^{-\sigma}}\sum_j a_j^{-\sigma}<\infty.
\]

Thus elementary scalar logarithms in the product (19), without
assuming ||T_s||<1, give the central owner identity

\[
D(s,1)=
\exp\left(-\sum_{k\ge1}\frac{\operatorname{tr}(T_s^k)}k\right)
=\prod_{a\in A}(1-a^{-s})=Z_Q(s)^{-1},
\qquad \Re s>3/2.
\tag{24}
\]

The factor 1/k counts positive repeated traversals of the same
primitive circle, not distinct new orbits. The ordinary orbit
product itself is defined on Re s>1 by its full ledger; the
operator equality is proved only on the sufficient domain stated.
Unique integer factorization identifies the z=1 product with the
Dirichlet Euler product there. For arbitrary z the locally normally
convergent product in (19) also defines a scalar holomorphic extension
of D to Re s>1, entire in z. This does not extend T_s as a trace-class
operator on this H, or its ordinary determinant representation, past
the proved Re s>3/2 domain. No continuation beyond the ordinary
product domain, completed determinant or target zeros is established.

## 6. Controls, adverse findings and limitations

| Control | Exact finding | Scope consequence |
| --- | --- | --- |
| Infinite parent/children relations | Finite subtree energy and infinitely many admissible children force every prefix coefficient sum to vanish in a kernel vector | Injectivity is proved, not presumed from formal indicators |
| Replace A by a finite alphabet | 1 minus the finite sum of first-symbol indicators is a nonzero finite-energy kernel vector | Infinite branching is essential; no general finite-alphabet injectivity claim |
| Mixed futures (2,2,...) and (2,3,3,...) | The cylinder phi_(2,2) distinguishes them and both states remain in the source | Genuine advance beyond first-symbol observations |
| Different pasts of (3,3,...) | Constant-3 and negative-2/positive-3 histories share a future | The one-sided factor still forgets pasts |
| Alternating first-symbol observable | Equation (9) excludes it from JH despite continuity and boundedness | All finite cylinders does not mean all of C_b(Y_+) |
| Delete the empty coefficient interaction | L_s 1 is still nonzero and the low rank-one formula fails | No omitted constant or artificial diagonal trace |
| Unweighted coefficients on all words | c_(2,...,2)=1/k at length k has finite ell2 norm but divergent value at the constant-2 history | The strong weights have a real analytic role, not cosmetic normalization |
| Remove covers | Ordered constants at composite integers become additional packets | Arithmetic specificity belongs to the cover source |
| Remove ordering | The mixed cycle (2,3) with time log6 becomes admissible | The unchanged Euler trace cannot be assigned to that changed owner |
| Other infinite ordered integer alphabets | The injectivity and trace-class construction repeats whenever the analogous sums converge | PROVES_TOO_MUCH: the RKHS technique itself does not establish prime naturalness |
| Change the scale law or geometric carrier | Equations (3), (10), (23) no longer identify that different roof automatically | No transfer to 171, 176 or 177 |
| Truncate columns at N | Bound (18) proves an actual infinite trace-norm limit, with complete output tails | Finite checks are not used as infinite evidence |

The weights grow strongly and use a deliberately selected combinatorial
code. No canonical norm, invariant measure on Q, or uniqueness of this
design is claimed. The result answers the frozen engineering question;
arithmetic naturalness is still OPEN. The source/clock remains the
declared ordered-cover scale construction, not a newly derived
physical Hamiltonian clock. The sufficient half-plane Re s>3/2 is
narrower than 174's Re s>1 and is not claimed optimal. The new H is
not asserted to contain all observables in 174's weighted first-symbol
space; those include unbounded functions, whereas JH lies in C_b.
The Hilbert norm is transported from coefficients, not the sup norm:
normalized vectors e_w/sqrt(rho_w) have unit H-norm while their
images can have sup norm tending to zero. No bounded inverse from
the sup-norm image to H is asserted.

## 7. Gate assessment and decision

| Audit | Result | Unresolved boundary |
| --- | --- | --- |
| T0 carrier and ownership | ESTABLISHED: full inverse-limit source, complete scale quotient and injective observable realization | Broadened carrier, no classical symplectic map supplied |
| T1 arithmetic and clock | SCOPED ESTABLISHED: covers derive atoms and the transfer uses the actual scale roof | Ordering, scale units and norm design; naturalness OPEN |
| T2 packets and repetitions | ESTABLISHED: complete one-circle-per-atom ledger and unique periodic history | No chronological prime-execution or new geometric theorem |
| T3 ordinary analytic owner | ESTABLISHED on Re s>3/2: full finite-cylinder RKHS, power traces and Fredholm identity | Scalar product extends to Re s>1; optimal operator domain and continuation beyond that product domain unproved |
| Classical A0--A2 | NOT APPLICABLE | No natural A0 or formal Route pass inferred |
| Formal Route / B | UNASSIGNED / NOT INVOKED | Neither evaluated |

**Decision: advance this scoped analytic construction; fork before
changing its space, weights, source, clock or normalization.**
The decisive initial gate is the injectivity proof (7); the decisive
analytic gate is complete column trace-norm summability followed by
the finite invariant depth filtration. All modules belong to the
single frozen object, with the full source present throughout.
A stronger natural or geometric claim is not inferred from success.

## Reproducibility and integrity

The exact inputs are rational divisibility, strict covers, ordinary
integer order, all finite words, the explicit binary/unary code,
the fixed recursive rho, and exp(t) scale units. All mathematical
evidence consists of the displayed proofs and inequalities.
There is no numerical experiment, atom table, fitted coefficient,
zero data or finite-cutoff inference. N in (17) is an exact proof
parameter with the rigorously vanishing bound (18), not measured data.

See the [card](candidate-card.md), [claim ledger](claim-ledger.md),
[summary](README.md) and [evidence index](evidence/README.md).
The separate mathematical review is a different invocation with
inherited model and visible proposal, not human peer review or an
independent-error guarantee. ARS was applied only as bounded
claim/evidence/reasoning and counterargument discipline, not a
publication pipeline. No human-subject experiment, external-model
upload or publication artifact is included.
