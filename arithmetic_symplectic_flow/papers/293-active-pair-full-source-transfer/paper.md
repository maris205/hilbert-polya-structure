# Full-source transfer and the cylinder-trace mismatch

Audit ID: `ASFS-AUDIT-20260920-AFT01`.
Candidate ID: `ANG-20260920-APR01` (unchanged 288/289/291).
Paper ID: `293-active-pair-full-source-transfer`. Date: 2026-09-20.
Status: `OWNED TRANSFER; COFINAL CYLINDER TRACE MISMATCH — SCOPED ADVANCE / STOP`.
Result type: exact classical-transfer and finite-observation trace audit.

## Abstract

The complete active-pair source admits a clock-weighted inverse-branch
transfer family on all locally constant compactly supported functions.
We construct this family and its precise inductive-limit domain, then
test finite root/cylinder compressions with ordinary matrix trace.
Closed root paths force a prime root and zero branch digit, but the
finite seed diagonal counts ker(B_p^r-I modulo M), not the single
actual profinite periodic seed. Under cofinal divisibility refinement
that count stabilizes at |det(B_p^r-I)|. It equals one at r=1 but
2p-1 at r=2, so this trace prescription does not give ordinary orbit
repetition weights. The root-constant observation space does give the
finite ordinary Euler factors, but it is not a cofinal cylinder
approximation and no global determinant is established on it here.
The underlying object and its previously proved scalar zeta remain
unchanged; only the proposed full-cylinder trace identification stops.

## 1. Frozen contract and unchanged dynamical owner

The original [analytic card](candidate-card.md) has SHA-256

    ebd6c1c2a68ac1af187c93ea71e7c889ceb206d59c1b5b3e35bf1f372791c868

It is the new explicit classical-transfer contract requested by the
prior same-object handoff. The [288 owner](../288-active-pair-residue-flow/paper.md)
and [291 scalar result](../291-active-pair-orbit-zeta/paper.md) are
locked read-only inputs, not new results of this paper. Their exact
bindings appear in the [evidence index](evidence/README.md).

Keep K=Z_hat and Y=coproduct_(a,b>=2) {(a,b)} x K², each root with
joint additive Haar mass one. On the unchanged partial domain,

    w(b)=#{d:1<d<b,d|b}, j=x mod b in {0,...,b-1},
    c_pair=2b-a+w(b)+j>=2,
    T(a,b,x,y)=(b,c_pair,y,(x-j)/b+y).

Its inverse branches have joint IMAGE factor 1/b and positive inverse
arrow clock log b. The full tail groupoid and real extension retain
all terminal, null, noninteger and nonreturning states. There is exactly
one actual primitive packet per prime, least time log p, with repeats
r log p. The same scalar orbit zeta was established in 291 under
unit weights and the 1/r convention. Its full quotient is non-Hausdorff;
we neither change nor reaudit that topology.

The lineage remains proper-divisor symbolic admissibility -> active
integer-pair feedback -> this coupled residue owner. Witness/measure
naturalness remains OPEN. Nothing here imports 292's distinct rule,
constructs a symplectic lift, or uses quantum/zero data.

## 2. A genuine transfer family on the full source

Let V_(R,M) consist of complex functions supported on root square
2<=a,b<=R and constant on every seed congruence class modulo M.
It has dimension (R-1)² M². Let V be their union, ordered by growing
R and divisibility of M, with the locally convex inductive-limit
topology. This is precisely the locally constant compactly supported
function space on Y: compact support meets finitely many root fibres,
and compactness gives a common finite congruence level on those fibres.
The stages R=n,M=n! are cofinal. V separates ALL source points,
including null and nonreturning ones.

**Proposition 1.** The frozen formula

    (L_s f)(u,v,xi,eta)
      =u^(-s) sum_(0<=j<u, a=2u+w(u)+j-v>=2)
         f(a,u,j+u(eta-xi),xi)

defines a continuous linear endomorphism of V for every complex s.
It maps V_(R,M) into V_(4R,M). For each f, s->L_s f is entire
with values in one finite stage. No nuclearity or global trace follows.

*Proof.* 288's exact inverse formula gives precisely the summands shown.
There are at most u summands, each with the weight exp(-s log u)
of its actual inverse-arrow clock. If f is supported in root square R,
then u<=R, a>=2, and

    v=2u+w(u)+j-a <= 3u+w(u)-3 <= 4R-5,

using w(u)<=u-2. Hence the output has finite root support. Every
inverse seed map is integer-affine, so its reduction modulo M is
well defined and preserves the seed observation level. The claimed
finite-stage inclusion follows. Each stage restriction is a continuous
finite-dimensional linear map into another stage, proving continuity
by the inductive-limit property. For fixed f only finitely many u
occur, and all coefficient functions u^(-s) are entire. QED.

There is also an exact measure check, without a Hilbert-space model.
For compactly supported locally constant test functions f,g, change
variables branch by branch using the inverse IMAGE factor 1/b:

    integral_Y (L_s f) g dmu
      = integral_D b^(1-s) f(z) g(Tz) dmu(z).

All integrals are finite. In particular s=1 gives the ordinary
measure-transfer duality with the actual partial T. The clock weight
is not a label added to an unrelated operator. This identity does
not assert any trace, spectral or self-adjointness property.

## 3. Finite observations are not finite forward dynamical owners

Let P_R cut off the root support and let E_M be normalized conditional
Haar averaging on each seed congruence class modulo M:

    E_M f(a,b,x,y)=M² integral_((x+MK)x(y+MK)) f(a,b,u,v) dh(u)dh(v).

These are commuting projections, with image V_(R,M) for their product.
By Proposition 1 the finite compression is

    C_(R,M,s)=P_R L_s |_V_(R,M).

Neither projection changes the dynamical carrier. Forward division
by b need not descend modulo M. Only the actual INTEGER-AFFINE inverse
branches descend to finite observations; we do not claim a finite
quotient map T_M with the same periodic points.

For example, at root (2,2) the full seeds (0,0) and (2,0) are
identical modulo 2 and both use the admissible zero-digit branch.
Their forward images have seeds (0,0) and (0,1), respectively,
which differ modulo 2. The inverse branch B_2 is nevertheless an
integer matrix and acts on level-2 observations exactly as stated.

Define the finite determinant D_(R,M)(z,s)=det(I-zC_(R,M,s)), with
z a formal iterate marker, not physical time. Finite cofactor
differentiation and the formal geometric inverse give

    -d/dz log det(I-zC)=Tr(C(I-zC)^(-1))
                     =sum_(r>=1) z^(r-1) Tr(C^r).

Integrating the zero-constant-term formal series proves

    -log D_(R,M)(z,s)=sum_(r>=1) z^r Tr(C_(R,M,s)^r)/r.

Only ordinary finite-dimensional trace is used. No trace/Fredholm
determinant on V, or convergence at z=1, is thereby constructed.

## 4. Exact all-iterate cylinder trace

Put B_p=[[-p,p],[1,0]] and

    kappa_(p,r)(M)=#ker(B_p^r-I : (Z/MZ)² -> (Z/MZ)²).

**Theorem 2.** For every R>=2, M>=1, r>=1 and complex s,

    Tr(C_(R,M,s)^r)=sum_(p<=R) p^(-rs) kappa_(p,r)(M).

*Proof.* Use the indicator basis of root/seed congruence classes.
A diagonal term of a product corresponds to a closed root/branch
path staying in the root square, together with a fixed congruence
class of its composed inverse seed map. Keep every branch in this
finite trace; do not restrict to actual full-seed periodic points.

Around a closed root path the original recurrence is
b_(i+1)-2b_i+b_(i-1)=w(b_i)+j_i. Summing gives zero, so all
w and digits vanish. The cyclic first differences are then constant
and must be zero. Thus every root is (p,p) for one prime p<=R,
and each branch has j=0. This is a finite-root algebraic argument
independent of whether its seed congruences lift to a periodic K² state.

On that diagonal block the inverse seed map is B_p and its weight
is p^(-s). The trace of r-fold pullback on functions on (Z/MZ)²
counts exactly the fixed classes of B_p^r. Each contributes p^(-rs).
There is one surviving root/branch path per such p, proving the formula.
QED.

**Lemma 3.** Write delta_(p,r)=|det(B_p^r-I)|. It is a positive
integer. For all M, kappa_(p,r)(M)<=delta_(p,r); whenever
delta_(p,r) divides M, equality holds. Consequently along any cofinal
divisibility refinement of M, each fixed-(p,r) count stabilizes at delta.

*Proof.* The roots of the characteristic polynomial t²+pt-p of B_p
lie in (0,1) and (-infinity,-p), so no positive power has eigenvalue
one. Thus A=B_p^r-I has nonzero integer determinant.

For any such integer matrix A, finite-group counting gives

    #ker(A mod M)=#coker(A mod M)
      =# [Z²/(A Z²+M Z²)] <= # [Z²/A Z²]=|det A|.

The last lattice index identity follows by integer unimodular row and
column elimination (the Euclidean algorithm reduces to a triangular
matrix, whose diagonal absolute product counts residue classes).
If |det A| divides M, the adjugate formula makes M A^(-1) integral,
so M Z² is contained in A Z² and equality holds. Cofinality means
eventual divisibility by every fixed positive integer, giving the
asserted stabilization. For fixed R,r there are only finitely many
p, so the entire trace also stabilizes at the corresponding finite sum.
QED.

The full-seed periodic equation Av=0 in K² still has only v=0:
the adjugate gives det(A)v=0, and nonzero integer multiplication on
K is injective. Stabilization of finite cardinalities does NOT
justify commuting cardinality with this inverse limit.

## 5. The decisive repetition mismatch

**Corollary 4.** For r=1, kappa_(p,1)(M)=1 at every M. For r=2,

    kappa_(p,2)(M)=gcd(M,2p-1),
    delta_(p,2)=2p-1.

Therefore cofinal cylinder traces do not reproduce the ordinary
unit-weight repetition counts A_(R,r)(s)=sum_(p<=R)p^(-rs).

*Proof.* det(B_p-I)=1, so the r=1 assertion follows from Lemma 3.
For r=2 the matrix is

    B_p²-I = [[p²+p-1,-p²],[-p,p-1]].

The first row plus (p+1) times the second row is (-1,-1).
Its kernel modulo M therefore has y=-x and (2p-1)x=0.
Conversely those two conditions solve both original rows. There are
exactly gcd(M,2p-1) possibilities for x. QED.

Already at R=2 and any M divisible by 3,

    Tr(C_(2,M,s))=2^(-s),
    Tr(C_(2,M,s)^2)=3 * 2^(-2s),

where the ordinary orbit coefficient at r=2 is only 2^(-2s).
The discrepancy persists under cofinal refinement; it is not a
rounding or low-modulus error. It also changes the formal z² coefficient
of -log D, so first-iterate agreement cannot establish a determinant
identification with 291's ordinary orbit normalization.

The missing compatibility can be seen directly. For p=2,r=2,
the kernel modulo 3 is {(0,0),(1,2),(2,1)}. Modulo 9 it is
{(0,0),(3,6),(6,3)}, whose entire reduction modulo 3 is (0,0).
Thus the two nonzero mod-3 solutions have no mod-9 lift. The count
can stay three while compatible full profinite solutions are only zero.
No extra actual closed packet is inferred from these residue solutions.

## 6. Observation and normalization controls

| Frozen control | Exact result | Ownership limit |
|---|---|---|
| M=1, root-constant functions | Tr(C^r)=A_(R,r); D=product_(p<=R)(1-z p^(-s)) | Legitimate invariant observation subspace, NOT a cofinal full-cylinder approximation |
| Cofinal M, ordinary trace | Fixed-r trace stabilizes at sum_(p<=R) delta_(p,r) p^(-rs) | Extra repetition-dependent weights, not actual full-seed packet multiplicity |
| Trace divided by M² | Tends to zero for fixed R,r | Different normalization, not the desired unit weights |

For M=1 there is exactly one seed class and every kappa equals one.
The all-r trace identity proves the displayed finite determinant:
both determinant and product have constant term one and the same
zero-constant-term formal logarithm. L_s really preserves
functions constant on seed fibres, so this positive finite result is
not dismissed as an illegal representation or a change of the source.
But keeping M=1 forgets all seed distinctions and does not approach
V through its cofinal congruence levels. A future global operator on
an appropriate completion of that subspace would need its OWN domain,
boundedness/nuclearity and determinant proof. None is supplied here.

For the normalized trace control, Lemma 3 bounds the fixed-R,r
numerator uniformly in M, so division by M² gives zero along a
cofinal refinement. Dividing by the full dimension has the same limit.
Neither this rescaling nor an unproved r-dependent correction is
silently adopted. The measure-clock and original unit orbit weights
remain as frozen.

## 7. Scoped advance, precise stop and next obligation

The full-source transfer family and its actual locally convex domain
are established. This supplies a classical operator owner, not merely
a formal symbol attached to zeta. The full-cylinder ordinary matrix
trace prescription, however, fails the ordinary repetition comparison
at r=2. We stop that proposed identification now, without a large-root
limit, infinite determinant, zero comparison or further trace repair.

| Layer | Current result | Remaining boundary |
|---|---|---|
| T0/scoped T1 and T2 | Unchanged 288/289 results | Stronger arithmetic naturalness OPEN |
| Ordinary scalar T3 | Unchanged 291 result | Not automatically an operator trace |
| Full-source L_s on V | ESTABLISHED, Proposition 1 | No Banach/Hilbert/nuclear/Fredholm conclusion |
| Finite compression determinants/traces | ESTABLISHED exactly | Observations, not forward finite dynamical quotients |
| Cofinal cylinder-trace = ordinary orbit weights | FAIL, Corollary 4 | Failure of THIS prescription, not a universal analytic no-go |
| Global same-owner determinant/trace | OPEN / NOT SUPPLIED | Requires a new explicit analytic contract |
| Classical A0/A1/A2 / formal Route / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No quantum or target-zero result |

Portfolio: **scoped advance / stop**. Keep the actual transfer owner;
stop promoting its cofinal cylinder traces as the ordinary zeta trace.
The root-constant finite observation is a possible future analytic
question, not a claimed global solution. Parallel breadth has produced
a [pending explicit source definition](evidence/scout-record.md), with
no new candidate ID or result before a fresh freeze. It does not modify
APR01, and no theorem in this paper concerns that proposed source.

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md)
and [internal review](evidence/independent-review.md) record scope,
bindings and ARS's three adverse checkpoints. This is AI-assisted
shared-model/context work, not external peer review or formal proof
verification. No scientific numerical run or external source theorem
is used. Old packages and mirrors remain unchanged; 241/242 paused;
the original programme goal remains active.
