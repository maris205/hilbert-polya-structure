# Divisibility-directed Euclidean tapes: owned clock, nonprime fixed primitives

Paper ID: `326-divisibility-directed-euclid-tape`.
Candidate ID: `ANG-20260920-DET01`. Date: 2026-09-20.
Status: `OWNED TAPE CLOCK; NONPRIME FIXED PRIMITIVES — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The full bilateral nonnegative-integer tape undergoes a local Euclidean writeback
and a shift directed by whether the actual remainder vanishes. Complete
inverse branches, terminal incoming histories and a fixed nonatomic iid measure
own one all-point IMAGE clock. All fixed tapes form two explicit
families. A genuine primitive log2 packet survives, but other fixed tapes
have primitives log(10/3) and log(21/10), already excluding the
prime-length target. Entire finite-inverse basins and phases remain, rather than
selected fixed representatives. Three controls own separate images and clocks;
the no-shift control has a global potential and eventual fixed sources
with zero time. This is a same-object owner result and STOP /
FORK, not a symplectic construction, canonical arithmetic A0 or formal Route pass.

## 1. Frozen source, exact lineage and comparison boundary

The [original card](candidate-card.md), first 160 lines, was frozen before
claims/calculation, SHA-256
`7e5048a2627c07c53d83ee562a5e7d054f65084427a81d6fb69f438075e72523`.
The original author subsequently read only these lines and confirmed faithful
definition transcription, not mathematics. Root's pre-freeze decision to classify
ALL fixed tapes extends the original five-tape testing proposal without changing
the tuple; the distinction is explicit in the card and [provenance](evidence/scout-record.md).

Let X=N0^Z with full product topology/Borel structure. Put
(sigma x)_i=x_(i+1), a=x_0,b=x_1. For b>0 set
q=floor(a/b), r=a-qb, and define

    (Rx)_0=q, (Rx)_1=b+r, (Rx)_i=x_i otherwise,
    epsilon=+1 if r=0, -1 if r>0,
    T x=sigma^epsilon(Rx).                             (1)

All b=0 objects are terminal: no step, but identity and every
actual incoming history remain. All zeros, units, arbitrary unbounded tails
and nonperiodic tapes are present. No finite-support restriction, padding, spatial
quotient, extra shift arrow, absorbing loop or chosen geometric centre.

On the full cylinder x_0=n,x_1=d>0, the divisor symbol
d|n is exactly r=0. Proper part 1<d<n does not
remove other letters. This actual symbol changes transport direction, and q,
b+r change the next neighborhood. Nondivisibility is not rejected and
primality is not an acceptance bit. Thus the lineage is divisor
symbol -> quotient/remainder -> arithmetic writeback and directed motion ->
the next actual neighborhood. Direction, writeback and probability are design;
stronger naturalness, Logistic/Henon relations and conservative/symplectic realization OPEN.

Limited comparison with 225 found a different finite-word graph/shortlex-port
action, whole real fibres and unit roof, not (1). This
definition difference supplies no nonconjugacy or global novelty theorem, and no
old clock, theorem or Route credit is inherited. No prime/zero tables.

## 2. Complete inverse and all terminal boundaries

For a target w, all possible predecessors are exactly the following:

    Plus: b=w_0>=1, a=b*w_(-1),
          x_0=a,x_1=b,x_i=w_(i-1) for i!=0,1;
    Minus: w_2/2<b<w_2, b integer,
           r=w_2-b, a=b*w_1+r,
           x_0=a,x_1=b,x_i=w_(i+1) for i!=0,1.       (2)

Undoing the actual shift forces the two target window values; undoing
the quotient/remainder then gives these exact equations. Substitution proves both
inverse identities. Distinct b's give distinct old divisors. A common source
cannot occur in both directions since its own remainder determines epsilon.
Consequently the predecessor count is

    1_{w_0>=1} + max(0,floor((w_2-1)/2)),
    image(T)={w:w_0>=1 or w_2>=3}.                    (3)

The map is finite-to-one but NOT onto. On every source window
(a,b), b>0, it is a homeomorphism onto the corresponding target
two-coordinate cylinder. Outside those windows all coordinates are shifted bijectively.

Outgoing status instead tests w_1. For example the tape with w_0=1
and all other coordinates zero is terminal but has the actual plus
predecessor with x_1=1 and all other coordinates zero. Conversely the
tape with w_1=1 and all other coordinates zero has no predecessor
but is legal. The all-zero tape is isolated terminal, with neither
incoming nor outgoing nonidentity arrows. No terminal derivative is evaluated.

## 3. Entire iid measure, finite-window IMAGE and lag

Freeze pi(n)=1/[(n+1)(n+2)] for n>=0 and mu=pi^Z.
For completeness, partition (0,1] into I_n=(1/(n+2),1/(n+1)]
and iterate each interval's affine rescaling onto (0,1]. The successive
labels have the prescribed product law on N0. Assign them to
Z by a fixed enumeration 0,1,-1,2,-2,... . Every finite-
coordinate cylinder then has mass equal to the product of its pi's.
Cylinder generation proves uniqueness of this Borel probability. Its construction
does not restrict X to coded representatives or select a different tape.

Every nonempty cylinder has positive mass, so support is full. Specifying
k coordinates gives mass at most 2^{-k}; points have zero mass,
and the countable coordinate partitions exclude any other atom. A shift
preserves all finite-cylinder probabilities, hence all Borel sets. Conditional
outside-coordinate laws are the same iid law after any finite specification.

On an actual branch with source pair (a,b) and target window
(q,b+r), all remaining coordinates are merely reindexed. Independence and
shift invariance give, for EVERY Borel subset E of that target cylinder,

    mu(theta E)=integral_E J dmu,
    J=pi(a)*pi(b)/[pi(q)*pi(b+r)],
    kappa=-log J.                                    (4)

One may first check outside finite cylinders and extend by the generated
Borel class. This proves the whole integral law, not just a
two-window mass ratio. Inverse domains (2) are refined by their target
window values as needed. The frozen branch-constant version is finite positive
at EVERY tape, including all null fixed tapes, and is unchanged by
further outside-window refinement. A.e. uniqueness alone does not fix null values.

The main step clock is nonnegative, with zero precisely when a=0
or b=1 (on the legal domain b>0). For r=0,
J=pi(bq)/pi(q)<=1, with exactly those equality cases. For r>0,
b>=r+1; each factor (q+j)/(bq+r+j), j=1,2,
is nonincreasing in q, and each (b+r+j)/(b+j) decreases
in b. Bounding successively at q=0 and b=r+1 gives

    J<=4(2r+3)/[(r+2)^2(r+3)]<1.                     (4a)

The last strict inequality follows from
(r+2)^2(r+3)-4(2r+3)=r(r^2+7r+8)>0. These simplified
bounds and the all-step sign conclusion were supplied by original-card-only
raw review after root's 369-line first draft, then checked and
adopted. The first draft already had (4), but not this sign
theorem. Nonnegativity does not supply canonical naturalness or a positive roof.

A finite actual history is a finite-coordinate substitution plus one net
shift on countably many cylinder charts. Its inverse IMAGE is the
product of actual step densities. Finite branch pairs are obtained by
common-window refinements; reindexed outside factors cancel and the same Borel
law proves their IMAGE. No unweighted whole-map formula is inferred from
overlapping target windows. For legal T^m z=T^n w the pair
IMAGE is exp[-S_m(z)+S_n(w)]. Thus

    G={(z,m-n,w):T^m z=T^n w, histories legal},
    c(z,m-n,w)=S_m(z)-S_n(w).                          (5)

Source w, range z; same triples one arrow. Same-lag presentations
append a common legal future whose clock cancels; composition aligns the
middle histories. This proves pointwise descent/additivity, including terminal identity.
Actual forward (Tz,-1,z) has clock -kappa(z), not +kappa.
All X x R_s and s-translation remain. No invariant mu times ds,
smooth/Hausdorff coarse quotient or separate positive suspension roof is asserted.

## 4. ALL fixed tapes and their entire time groups

### 4.1 Divisible branch

If epsilon=+1 and Tx=x, all positions i<=-2 and i>=1
force constant left and right tails. At the two changed positions,
x_(-1)=q and x_0=b; consequently a=b, q=1,r=0.
The ENTIRE family is

    F_B(i)=1 for i<0, B for i>=0, B>=1.              (6)

Its core clock is

    L_B=log[pi(1)/pi(B)]=log[(B+1)(B+2)/6].           (7)

Source isotropy is Z. For B=1, L_B=0, entire H0 and
extension kernel Z persist. For B>=2, L_B>0, entire H=L_B Z,
extension kernel zero and primitive L_B. F_2 supplies a genuine log2
packet. F_3 instead has primitive log(10/3), whose exponential is
not a prime integer. It is not merely a nonprimitive multiple
of some other packet: the FULL isotropy of this fixed source is Z.

### 4.2 Nonzero-remainder branch

If epsilon=-1, unchanged coordinates force a constant left tail including
position0, and a constant right tail starting at2. At position1,
b=q, so a=b^2+r with 1<=r<b. Thus the ENTIRE
second family is

    G_(b,r)(i)=b^2+r for i<=0;
                 b for i=1;
                 b+r for i>=2,
    b>=2, 1<=r<b.                                    (8)

Substitution verifies every member, so these two families exhaust ALL fixed
tapes, not just the original five test tapes. Its core clock is

    K_(b,r)=log[pi(b+r)/pi(b^2+r)]
      =log[(b^2+r+1)(b^2+r+2)/((b+r+1)(b+r+2))]>0.   (9)

Every source group is Z, entire H=K_(b,r) Z, extension kernel
zero and primitive K_(b,r). Already G_(2,1) has primitive log(21/10),
a second nonprime target obstruction. Distinct fixed tapes cannot meet under
actual iteration and hence remain distinct packets, even if some times agree.
Same-packet repetitions are integer multiples of the corresponding primitive.

The decisive gate is therefore STOP / FORK. It preserves the
positive F_2 result while retaining the nonprime fixed packets. No choice
of spatial quotient, fixed representative, inverse branch or normalization removes them.

## 5. Full fixed basins and phases, including every inverse branch

For any fixed core f in (6) or (8), define A_0={f}
and A_(j+1) as ALL predecessors (2) of EVERY member of A_j.
Then

    B_f=union_(j>=0) A_j                              (10)

is an explicit complete inverse-generation specification. At every stage the
finite b ranges and all outside coordinates are fixed by (2).
Necessity follows by undoing each actual step; sufficiency by the inverse
identities. No depth cutoff, representative section or discarded overlap is used.
Repeated representations are sets of actual tapes, not additional states.

B_(F1) and B_(F2) are singleton: each core has only itself
as predecessor. All other main fixed basins are countably infinite. For
G_(b,r), put A=b^2+r>=5. Repeated plus inverses have first
coordinates A^2,A^3,..., since the entire far-left tail stays A.
These are distinct actual ancestors. For F_B, B>=3, take its
minus predecessor with old divisor B-1. Put A=B^2-B+1 and
C=AB. After one subsequent plus inverse obtain a tape with left
tail1 and rightward entries (C,A,B-1,B,B,...), starting at0.
Further plus inverses give (C,C,...,C,A,B-1,B,B,...) with
arbitrarily many C's before the fixed A marker. All are legal and
distinct. Finite branching bounds every B_f above by countability. Hence
the fixed-family basins are null under mu, but their full-point clocks remain.

Let d(z) be first hitting depth of f and S(z) its
accumulated kappa. Write K=kappa(f), allowing K=0. Every arrow
w->z within B_f has, for some integer k,

    lag=d(z)-d(w)+k,
    c=S(z)-S(w)+kK.                                  (11)

Thus EVERY ancestor has source Z and entire H=KZ; its extension
kernel is zero if K!=0 and Z if K=0. Full phase
is s-S(z) modulo abs(K) when K!=0, real when K=0.
Distinct fixed basins never merge. This is a set/Borel phase statement,
not an ambient embedded-circle theorem. Other main source periods remain UNCLASSIFIED.

Terminal basins are likewise obtained by all inverse generations of their
actual terminal anchor. There is no arbitrary outgoing loop. Their exact
depths give lag d(z)-d(w), clock S(z)-S(w), phase s-S(z),
and trivial source/time/extension isotropy. No global finite-termination claim.

## 6. Three controls with their own complete fixed ledgers

### 6.1 DIRECTION-OFF

Keep R but always shift +1. All inverses have integer b with
w_0/2<b<=w_0, restore (b*w_(-1)+w_0-b,b), and set
x_i=w_(i-1) elsewhere. Exact image w_0>=1; the predecessor count
is ceil(w_0/2). Terminality still uses w_1, so incoming terminal
histories remain. The actual-window proof gives its OWN density (4),
now without the main remainder/direction filter.

ALL fixed tapes are H_(B,r): left1, central B+r, right B,
where B>=1,0<=r<B. Indeed the fixed equation a=b+r forces
q=1 and the left tail1, and conversely these conditions suffice.
Their clock is L_B of (7), independent of r. The unit
core has H0/kernel Z; the others have H=L_B Z/kernel0.
For each B>=2 there are B distinct fixed packets at this
time. This changed-domain multiplicity is a control result, not main's ledger.

Every full basin is ALL iterated own inverses, with groups/phases (11)
using that control's prefixes. Only H_(1,0),H_(2,0) have singleton
basins; the others are countably infinite. If r>0, repeatedly taking
old divisor C=B+r inserts arbitrarily many C's before the different
right-tail letter B. If r=0,B>=3, first take old divisor
B-1, then repeatedly B, moving the distinct B-1 marker rightward.
This proves infinitude without omitting any other inverse generation.

### 6.2 REMAINDER-FEEDBACK-OFF

Write (q,b), with direction still from original r. All plus
predecessors use b=w_0>=1,r=0; all minus predecessors use b=w_2>=2
and EACH r=1,...,b-1. Restore a=b*w_(-epsilon)+r and all
outside coordinates w_(i-epsilon). Exact image w_0>=1 or w_2>=2,
count 1_{w_0>=1}+max(0,w_2-1). Own IMAGE is

    J_F=pi(a)*pi(b)/[pi(q)*pi(b)]=pi(a)/pi(q).         (12)

This is not main's b+r window. Complete fixed tapes are F_B,
plus J_(b,r) with left/central A=b^2+r and EVERY position i>=1
equal b, b>=2,1<=r<b. Positive-direction clocks are L_B; negative-
direction clocks are log[pi(b)/pi(A)]>0, already log(7/2) at
(b,r)=(2,1). Only F_1 has H0; other fixed groups use
their displayed positive K, source Z and zero extension kernel.

Full basins are all own inverse generations, with (11) and their
OWN clock prefixes. F_1's basin is singleton; all other fixed basins
are countably infinite. For negative cores repeated plus inverses multiply
the first coordinate by the constant A. For F_B,B>=2 use
the actual minus predecessor with r=1, followed by plus inverses;
after one multiplication by B, repeated inverses insert a fixed large
letter before a different marker, as in Section 5. In particular
F_2 now has external ancestors, unlike main: same core time does
not mean the same full basin. No control source is substituted for main.

### 6.3 SHIFT-OFF: global zero time, including all incoming fixed basins

Apply only R. Inverse old divisors satisfy w_1/2<b<=w_1;
restore (b*w_0+w_1-b,b), all outside coordinates unchanged. Exact image
w_1>=1, count ceil(w_1/2), and own IMAGE is (4) without
any coordinate shift. Every b=0 terminal object is isolated from incoming
arrows for this control, not for the shifted owners.

The finite everywhere-defined potential

    V(x)=log[pi(x_0)*pi(x_1)]

satisfies kappa_S=V(T_S x)-V(x) on each actual step. Thus its
full retained-lag cocycle is V(w)-V(z), ALL H0, and full
extension equivalence is actual own-tail equivalence plus equal s+V(x).
This does not identify different unchanged outside tapes.

ALL fixed sources have b=1 with ANY a>=0, or a=0 with
ANY b>=1; every outside coordinate is arbitrary and retained. These
are entire uncountable families, not selected centres. Every other legal
source has b>=2,a>=1, and next a=floor(a/b)<a. Consequently
every legal source reaches a fixed source in finitely many steps;
there are no other source cycles. No such result transfers to main.

Each fixed basin keeps exactly the same outside tape and ALL iterated
pair inverses above. For b=1 and for (a,b)=(0,2) it is
singleton. For (0,B),B>=3, there is predecessor (1,B-1),
then (B-1,B-1),((B-1)^2,B-1),...; the whole basin is countably
infinite. Every basin state has source Z, H0 and extension kernel
Z, whereas isolated terminal objects have all three groups trivial. The
global s+V phase retains all these own basins, without a positive primitive.

## 7. Original complete-tape one/two-step checks

Let tau_m have left tail1, central m, and all positive positions2.
All-zero is isolated terminal and all-one is fixed with zero clock
under each owner. The remaining checks retain every infinite coordinate:

| Owner | tau_2 | tau_3 | tau_4 |
| --- | --- | --- | --- |
| Main | Fixed F_2, primitive log2, singleton basin | T: ones through i=1, value3 at2, then2; T2: ones through0, value3 at1, then2; no return | T: value2 at -1 and all i>=0, ones below -1; T2: value2 at -2, value1 at -1, all i>=0 equal2, ones below -2; no return |
| DIRECTION-OFF | Fixed H_(2,0), primitive log2 | Fixed H_(2,1), separate primitive log2 packet | Same first/two outputs as main; no return |
| FEEDBACK-OFF | Fixed F_2, log2, nonsingleton full basin | T: ones through1, twos from2; T2: ones through0, twos from1; no return | Same first/two outputs as main; no return |
| SHIFT-OFF | Local pairs (1,2), then fixed (0,3) | Local pairs (1,3), then fixed (0,4) | First step is tau_2; second local pair (1,2) |

For SHIFT-OFF all outside coordinates stay exactly as in the input;
tau_4 therefore shares tau_2's eventual fixed basin, not tau_3's. The
global potential gives H0 and source/extension Z on these ancestors, not
a positive primitive from their nonzero incoming clocks. In the shifted
owners, nonreturn at two steps is NOT used to assign eventual
isotropy or rule out later returns for tau_3/tau_4. No further
period census or truncation of their left/right tails is performed.

## 8. Gate and nonclaims

| Audit | DET01 result | Limit |
| --- | --- | --- |
| T0 carrier / exact inverse / all-point IMAGE | ESTABLISHED full bilateral partial owner | All terminal incoming histories retained |
| T1 arithmetic / owned clock | Divisor-directed actual motion and same-measure clock | Stronger naturalness/canonical A0 OPEN |
| T2 fixed primitive ledger | log2 positive control plus nonprime fixed primitives: FAIL | Other main source periods UNCLASSIFIED |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No imported analytic owner |
| Classical A0/A1/A2 | NOT APPLICABLE | No finite-dimensional symplectic map/roof |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK; same-object ledger intact. Nonprime fixed packets
are a decisive counterexample, not a failure of finite testing to find
returns. Their all-point clocks were fixed before discovery. PROVES_TOO_MUCH
is visible in the unrestricted family of divisor-directed fixed tapes, not
a claim that all arithmetic carriers fail. Controls retain their own images,
basins, cardinalities and kernels; zero control time cannot repair main.

Exact proofs use no scientific program, numerical cutoff/precision, prime data
or external literature. No global main termination or full higher-period census,
natural symplectic realization, Hausdorff quotient, invariant height measure, RH or
Hilbert--Polya theorem is claimed. Internal ARS three-checkpoint scrutiny is
NOT_CALIBRATED, not external peer review, machine proof or independent-error evidence.

See [card](candidate-card.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md),
[package](README.md). Positive304, partial-positive320 and old packages unchanged;
241/242 paused; programme goal active. Markdown only; no PDF/LaTeX,
publication/upload or Git staging/commit.
