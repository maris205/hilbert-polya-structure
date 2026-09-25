# Candidate card — dynamic integer adjacency and double-layer exchange

**Candidate ID:** `ANG-20260920-DAE01`  
**Version:** P0 v1, frozen before this package's reported mathematical results.  
**Initial status:** `FROZEN / OPEN; FULL OWNER AND IMAGE CLOCK TO AUDIT`.  
**Track:** arithmetic Borel groupoid / IMAGE-height extension, not classical ASFS.
Classical symplectic form/base/roof/mapping torus NOT APPLICABLE; no physical
Hamiltonian time supplied. Formal coordinates UNASSIGNED; B NOT INVOKED.

## 1. Full carrier, category and measure

```text
Bcal={B in M_4(Z): transpose(B)=-B};
Y=coproduct_(B in Bcal, a in positive-integer^4) {(B,a)} x [0,infinity)^4;
mu=counting_(Bcal x positive-integer^4) x Leb_4.
```

Use discrete integer labels, usual closed-orthant topology and its full Borel
structure. Retain zero/degenerate matrices, negative adjacency entries,
units, every real zero face, the origin, ties and all terminal points.
No selected root, positive-interior replacement, centre, boundary mass,
new density or fixed mutation schedule is allowed. Geometric dimension four
does not by itself provide a symplectic form or conservative physical flow.

## 2. Current selector, exchange polynomials and matrix evolution

For [r]_+=max(r,0), define for k=1,2,3,4

```text
P+_(B,k)(z)=product_(i!=k) z_i^[b_ik]_+;
P-_(B,k)(z)=product_(i!=k) z_i^[-b_ik]_+;
E_(B,k)(z)=P+_(B,k)(z)+P-_(B,k)(z);
sigma(x)=min argmax_(1<=i<=4) x_i;
C_k={x: x_k>x_i for i<k, x_k>=x_i for i>k}.
```

Empty products equal1. Zero exponents contribute1, including the polynomial
0^0 convention. Current x selects k; no unchosen k is tried after failure.
Define the integer matrix operation, with every entry specified, by

```text
(M_k B)_ij = -b_ij                                  if i=k or j=k;
             b_ij+[b_ik]_+[b_kj]_+-[-b_ik]_+[-b_kj]_+ otherwise.
```

At selected k=sigma(x), the step exists exactly when

```text
a_k divides E_(B,k)(a),  x_k>0,  E_(B,k)(x)>0.
```

On that domain T(B,a,x)=(M_k B,a',x'), where

```text
a'_k=E_(B,k)(a)/a_k, x'_k=E_(B,k)(x)/x_k;
a'_i=a_i, x'_i=x_i for i!=k.
```

This changes both integer data and real data by the same exchange relation,
and changes the adjacency used in the next relation. All failed points remain
terminal with T^0 and every legal incoming history. In particular sigma(0)=1
but no step from0 exists. No reset, fallback vertex, or completion cycle.

## 3. Every actual inverse and full-point IMAGE prescription

For arbitrary target (D,b,y), enumerate every k and EVERY skew-integer B
with M_k B=D; do not assume involution or cite an old matrix theorem.
Set a_i=b_i,x_i=y_i for i!=k and reconstruct

```text
a_k=E_(B,k)(b)/b_k;    x_k=E_(B,k)(y)/y_k.
```

Keep exactly candidates satisfying positive-integral a_k, y_k>0,
E_(B,k)(y)>0, reconstructed x in C_k, all original source permissions,
and the FULL forward equality T(B,a,x)=(D,b,y). Identical actual sources
are counted once; all distinct sources remain. No matrix, integer, depth or
size cutoff is supplied. All inversion, completeness and matrix identities
are proof obligations, not results implicit in the notation.

For each fixed discrete source (B,a) and arithmetically permitted k, the
real source domain is C_k intersect {x_k>0,E_(B,k)(x)>0}; its target domain
is exactly the reconstructed-source-check set above. On this ENTIRE domain
prescribe J_I(y)=abs(det D I_real(y)), using the displayed polynomial/rational
inverse and its same analytic derivative at zero/tie faces. Prove a positive
finite ALL-POINT version and mu(I A)=integral_A J_I dmu for EVERY Borel A,
with compatible finite compositions. Do not fill null values by convention
after seeing returns; do not change the original Lebesgue density.

## 4. Actual retained lag, extension and time convention

```text
G={(z,m-n,w): m,n>=0, T^m z=T^n w, ALL required iterates valid};
source=w, target=z; inherited Y x Z x Y Borel structure.
```

Equal triples are a single arrow; retain lag and all actual terminal/incoming
data, not an artificial free mutation-word groupoid. Prove Borel/groupoid
ownership rather than assert an étale or Hausdorff coarse quotient.
For the actual inverse branch I_z:Tz->z define

```text
kappa(z)=-log J_(I_z)(Tz);
S_m(z)=sum_(0<=j<m) kappa(T^j z), S_0=0;
c(z,m-n,w)=S_m(z)-S_n(w).
```

Prove presentation independence and the full-point cocycle law. Use the
ENTIRE Y x R_h extension, with arrows (w,h)->(z,h+c) and proposed time
h->h+t. This is IMAGE-extension time, NOT a supplied physical Hamiltonian
or contact time. No positive roof, unit lag, or extra flow is substituted.

## 5. Entire isotropy, primitive packets and repetitions

Keep I_z=G_z^z, its entire clock kernel and H_z=c(I_z). Only a whole
H_z=L Z with least L>0 permits a primitive cyclic packet. rL repeats that
SAME packet, using actual arrows. Do not merge different packets by their
period value, integer root, matrix, finite prefix or geometric centre.
Keep all zeros, terminal states, predecessors, zero-clock and non-discrete
groups. Source periodicity, retained lag and extension returns are distinct.
All phases are identified only by actual extension arrows, not by an added
time-reversal or representative-selection rule. All conclusions must cover
the full stated domain, including any null support strata used by the proof.

## 6. Three separately owned controls

Each keeps the entire Y and separately declared same mu, but has its own
permission, inverse/IMAGE, actual G, cocycle and packet calculation.

1. FIXED-ADJACENCY: keep the selected exchange and permissions, but B'=B.
   Inverse enumeration requires source B equal target D; use E_(D,k) and
   the control's full source check. No matrix mutation is performed.
2. SELECTOR-OFF: always k=1, still update matrix and both coordinate layers.
   Remove the main C_1 restriction; inverse enumeration uses only k=1,
   with this control's own full permissions. Other x_i may be larger than x1.
3. SUM-TO-PRODUCT: replace E in BOTH layers by
   F_(B,k)=P+_(B,k) P-_(B,k), retaining selector and matrix evolution.
   Require a_k|F(a),x_k>0,F(x)>0. Every inverse numerator, source check and
   derivative uses this F, not the main E.

These remove adjacency evolution, geometric selection and the sum of the two
factor channels, respectively. They are not three tests of one boundary face.

## 7. Lineage and first discriminating gate

The exact proposed proper-divisor interface is

```text
B*=[[0,-1,1,0],[1,0,0,0],[-1,0,0,1],[0,0,-1,0]];
a=(d,n-1,1,1), n>=2, 1<d<n;
x in C_1, x1>0, x2+x3>0.
```

Check that its first integer permission really is d|n. This interface is
not a restriction of the carrier. The claimed lineage arrow, to verify, is
proper-divisor admissibility -> current factor exchange -> same-expression
real transport and dynamic integer adjacency -> a new successor relation
and new current selector. This is a defined deformation/realization, not a
Logistic/Hénon conjugacy theorem. Matrix size, max selector, sum, orthant and
Lebesgue density are designs; strong naturalness and prime selectivity OPEN.

First audit full inverses, matrix algebra, null/terminal ownership, IMAGE and
cocycle. A decisive GLOBAL clock identity is allowed to end the gate before
a periodic census. One exact elementary closed-source example may illustrate
the source/time distinction; it is not an extra census or a clock repair.
If the global gate does not decide, inspect ONLY fixed/legal T^2 returns in
the ENTIRE fiber B*,a=(1,1,1,1), for MAIN and all three controls separately,
keeping intermediate matrices/roots and checking full groups, least time and
multiplicity. Then STOP/FORK or bounded OPEN; no parameter, density, selector,
matrix or polynomial tuning. Do not repeatedly refine a failed clock owner.

## 8. Unavailable owners and provenance

No operator, trace, zeta, determinant, function space, analytic continuation
or quantization is supplied. T3 NOT SUPPLIED / NOT AUDITED. Classical
A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
This object cannot borrow 344's contact flow or its prime periods.

The definition was delivered by the arithmetic-feedback scout in344 and
transcribed/author-QA'd in344 scout-record B, current lines42–153. Root
re-read that record here, not the old312/330 scientific papers. The author's
bounded old-original-card exposures and shared history are preserved in the
new source record; no global novelty or blind-discovery claim is made.
Root had preliminary thoughts about a possible global clock identity before
this freeze; all new reported proof is to follow this frozen specification.
The only gate addition to the earlier suggested audit is permission for one
exact closed-source sanity example, not a change to the mathematical object.

The reviewer receives only this original card before root FIRST is locked
and the raw report released. No scientific numerical run, web dependency,
external upload, auxiliary review delegation, PDF, model/configuration change,
old-package edit, staging or commit is authorized by this card. 241/242 remain
paused;344 is preserved as its own positive construction, without credit transfer.

EOF — original card; append-only outcomes must preserve this prefix.

## Notation-only clarification — original 195-line prefix unchanged

The original prefix uses I_z first for an inverse branch and later for the
isotropy group. These are distinct typed objects. In the paper write
I_z^inv:Tz->z for the former and Iso_z=G_z^z for the latter, with
kappa(z)=-log J_(I_z^inv)(Tz) and H_z=c(Iso_z). No domain, transport,
clock, packet convention or other definition is changed by this clarification.
The source author's transcription QA identified the overload, not a new
mathematical result. The frozen prefix and its hash remain intact.

## Appended outcome — full-support clock gate

**Current status:** `OWNED DYNAMIC EXCHANGE; GLOBAL ZERO TIME RETURNS — STOP / FORK`.

The [own proof](paper.md) establishes matrix skew/involution identities,
all actual inverse candidates and domains, the frozen all-point analytic
IMAGE and the actual retained-lag Borel extension. The B* interface really
tests d|n. The inverse density is E(y)/y_k^2 and the one-step clock is
log(y_k/x_k), which may be nonzero.

The decisive GLOBAL identity is kappa(z)=V(Tz)-V(z), with
V=sum_(i:x_i>0)log x_i and empty sum0. Valid steps preserve support, so
this holds on every zero/tie stratum, not only the interior. Consequently
c(z,lag,w)=V(w)-V(z) on every actual arrow and H_z={0} at every point.
Every source-isotropy group is retained in its clock kernel. The full
extension invariant h+V excludes ALL nonzero time returns, with every
incoming and height phase kept. It is only a Borel gauge, not a new
topological/coarse-space theorem or a changed measure.

The exact zero-matrix axis family has true source2-cycles and full two-point
incoming classes, despite zero time returns. Each control owns its own
full inverse/IMAGE and the same global obstruction; PRODUCT also retains
its own fixed/reciprocal two-cycle cases. The conditional B* fixed/T^2
census was NOT RUN because the precommitted global gate already decided.

Portfolio **stop / fork** this IMAGE-height prime-time direction. T0
established; T1 clock owned but globally obstructed for returns; T2 no
positive time packets; strong naturalness OPEN; T3 NOT AUDITED. Classical
A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED. Do not borrow
344's contact action or retune this ID. The full coefficient-field proposal
remains separately UNFROZEN; older positives and paused241/242 are unchanged.

EOF — outcome append; original195-line definition and FIRST proof unchanged.
