# Divisible interpolation feedback: owned clock, no source cycles

Paper ID: `324-divisible-interpolation-feedback`.
Candidate ID: `ANG-20260920-DQI01`. Date: 2026-09-20.
Status: `OWNED DIFFERENCE-QUOTIENT CLOCK; NO SOURCE CYCLES — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The full signed four-register source transports two nodes and values to
their node difference, real interpolation difference quotient, old node and old
value. Actual floor-divisibility permission links it to the original divisor-symbolic
seed. The exact inverse is polynomial on its own permitted image, with
volume IMAGE |s| and clock -log|x1-x0|. All objects, cuts,
terminal endpoints and incoming histories remain. Complete four-state fixed and
two-step equations exclude every short return. A further exact cyclic-square
identity excludes ALL source periods, hence all nontrivial isotropy and positive
primitive times. The portfolio decision is STOP / FORK, without claiming
global termination. Two permission controls have the same all-period geometric
obstruction under their own images. The no-quotient linear control instead owns
zero clock and an exactly classified permitted period-four plane, demonstrating why
source recurrence and time image must stay distinct. No classical symplectic
construction, higher-period census or borrowed operator is asserted.

## 1. Frozen carrier, arithmetic seed and declared design

The [original card](candidate-card.md), first 150 lines, was frozen before
these results, SHA-256
`92a2dbb2213636e3c43735f3da6dc1bda13a30f2e0132ec61a8ed61a707e7ec2`.
Root read all 186 lines of the
[323 frontier](../323-quotient-batch-aggregation/evidence/scout-record.md),
SHA-256 `ef987acb435c9345b9d14ed21450ddc1c329bb532efd387feb169cdd5b85a5a8`.
Actual author access and shared-history limits are recorded in
[provenance](evidence/scout-record.md); no old theorem or clock transfers.

Take Y=R^4 with coordinates z=(x0,x1,u0,u1), usual Borel
structure and ordinary Lebesgue volume. At the CURRENT state set

    h=x1-x0, k=u1-u0, a=floor h, b=floor k,
    D={a!=0,a|b},
    Tz=(h,k/h,x0,u0).                              (1)

Here a!=0 ensures h!=0. The denominator is actual h, not
its floor. This is the real difference quotient of
P(xi)=u0+(k/h)*(xi-x0), with no polynomial added as another
state. The output is reinterpreted using the same four-register rule.
Every signed coordinate, unit difference, zero value difference and half-open
floor cut is retained. Y\D is terminal, keeping T^0 and every
actual incoming history. In particular all 0<=h<1, including h=0,
is terminal. No reset, infinity, absorbing loop or deleted null set.

The seed (n,d), n>=2,d>=1, enters at (0,d,0,n),
where the actual permission reads d|n. Proper part 1<d<n is
observed without removing units/endpoints or selecting the rest of Y away.
The lineage is divisor admissibility -> node difference divides value difference
-> real interpolation quotient -> new nodes/values generating new differences.
Floor observation, role rotation, register order and volume are DESIGN.
Stronger naturalness, canonical A0, Logistic/Henon conjugacy and conservative/symplectic
realization remain OPEN. Four dimensions alone supply none of those properties.
No prime/factor data, zero data, per-prime setting or independent scale.

## 2. Full exact inverse, own image and all retained boundaries

Solving target Tz=(s,t,u,v) forces the UNIQUE possible predecessor

    I(s,t,u,v)=(u,u+s,v,v+s*t).                    (2)

Its node/value differences are s and st, so the ENTIRE actual image is

    E={floor(s)!=0, floor(s)|floor(s*t)}.           (3)

Substitution gives I(E)=D, T(Iw)=w on E and I(Tz)=z
on D. Thus T:D->E is a Borel partial bijection. Each
target in E has exactly one predecessor and each outside has none.
The (a,b) cell restrictions in the card partition actual domains without
duplicating branches. All floor cuts use the same formula; the open
geometric map h!=0 to s!=0 is a smooth diffeomorphism, restricted
here by the exact Borel permission. No surjectivity on Y is claimed.

Outgoing permission of a target uses its OWN differences t-s and v-u,
not (3). For example (0,1,0,0) lacks an inverse because
s=0 but is a legal source: its differences are 1,0.
Conversely (1,1,0,0) is terminal because its node difference is
zero, yet has the actual predecessor (0,1,0,1). All terminal
objects and chains remain, and no step at h=0 is evaluated.
The seed (0,2,0,4) likewise legally reaches terminal (2,2,0,0);
this single seed example is not a classification of all integer seeds.

## 3. Owned volume IMAGE, signed clock and retained lag

In target coordinate order (s,t,u,v),

    D I=[[0,0,1,0],[1,0,1,0],[0,0,0,1],[t,s,0,1]],
    det D I=-s, J_I=|s|.                           (4)

For EVERY Borel A subset E, geometric change of variables restricted
to E gives mu(I A)=integral_A |s| dmu. The full-point
version uses this polynomial derivative at every permitted cut, including all
null states in E. It is finite and strictly positive since s!=0.
The a.e. identity alone does not uniquely specify null values; the
frozen analytic formula does. No derivative of a missing inverse or
nonexistent terminal step is supplied, and no measure change is made.

At an actual source the inverse density is |h|, so

    kappa(z)=-log|h|.                              (5)

This uses REAL h, not floor h. Legal sources with differences
(h,k)=(-1/2,0),(2,0),(1,0) have clock log2,-log2,0.
These are step values, not evidence of positive primitive periods. The
clock is signed, not a positive roof or runtime.

For a legal length-m history define

    D_m(z)=product_(0<=i<m)|h(T^i z)|,
    S_m(z)=-log D_m(z), D_0=1,S_0=0.

Its actual inverse has IMAGE D_m(z). A branch pair from w to
z, meeting after lengths m,n, has IMAGE D_m(z)/D_n(w).
Smooth local history charts and their Borel restrictions give this integral
and full-point composition law with the same volume. Retain exactly

    G={(z,m-n,w):T^m z=T^n w,m,n>=0,histories legal},
    c(z,m-n,w)=S_m(z)-S_n(w).                       (6)

Source w, range z, inherited Borel structure, equal triples one arrow.
Same-lag presentations differ by the same common legal future, which cancels;
composition aligns middle histories at the longer legal length. This proves
pointwise descent and additivity, including terminal T^0. The actual forward
arrow (Tz,-1,z) has clock -kappa(z)=log|h|, inverse +kappa.
All (z,eta) remain, with arrows (w,eta)->(z,eta+c) and full
eta-translation. Only Borel/set quotient is asserted, not smooth/Hausdorff
regularity, invariant volume-times-height or a classical suspension.

## 4. Complete short tests and all-period obstruction

### 4.1 Whole-state fixed and two-step tests

Fixedness in (1) forces x1=2x0, u0=x0 and u1=u0.
Then k=0, so the second output is zero and x1=0;
h=x0=0 follows, contradicting a legal step. Thus ALL fixed states
are absent, including all signed cells and cuts.

For a legal two-step return write the next differences as

    h1=k/h-h, k1=u0-x0.

Both h and h1 must be nonzero. Equality T^2z=z in ALL
four coordinates gives

    h1=x0, k1/h1=x1, h=u0, x0=u1.

Thus k=x0-h and x1=x0+h. The first equality gives
k=h*x1; the second gives h-x0=x0*x1, hence -k=x0*x1.
Adding yields (h+x0)*x1=x1^2=0. So x1=0 and k=0;
then h=-x0 and k=x0-h=2x0 force x0=0, contradicting
h1!=0. Therefore ALL legal two-step returns are absent as well.

This exact proof takes place on the full real state, not on integer
projections, slopes alone or sampled seeds. It uses only geometric legality
h,h1!=0, so stronger floor permissions cannot restore a short return.
These short tests alone do not classify higher periods. The following
identity supplies that additional result without a period census or new object.

### 4.2 Exact cyclic-square exclusion of every period

Suppose a legal P-periodic state sequence exists and let A_i denote
its first coordinate, with all indices modulo P. The SAME register
transport forces, at time i,

    x0_i=A_i, x1_i=A_i+A_(i+1),
    u0_i=A_(i-1), u1_i=A_(i-2), h_i=A_(i+1)!=0.

Its actual difference quotient then gives

    A_(i+1)*(A_(i+1)+A_(i+2))=A_(i-2)-A_(i-1).

Sum over one whole cycle. The right side telescopes to zero,
so

    sum_i A_i^2 + sum_i A_i*A_(i+1)
      = (1/2)*sum_i (A_i+A_(i+1))^2 = 0.

Every square must vanish. Thus A_(i+1)=-A_i and all second
coordinates vanish. Substitution into the unsummed quotient equality also gives
A_(i-2)=A_(i-1). Consecutive coordinates are therefore equal AND opposite,
forcing every A_i=0, contrary to legal h_i!=0. This proves
ALL periods absent on the full signed real source, including every cut.
Every eventually periodic orbit would reach such a cycle, so none exists.

This short arbitrary-cycle identity is within the card's exact-identity allowance.
It was supplied by the reviewer's original-card-only raw derivation AFTER
root's 306-line short-return manuscript was locked, and adopted after root
checked every coordinate and the cyclic sum. The first draft did not
prove this all-period claim. [Evidence](evidence/README.md) records both versions.
No higher-period enumeration, scientific computation or candidate alteration occurred.

## 5. Complete tails and zero isotropy

Any nonzero retained-lag isotropy T^m z=T^n z, m!=n,
would make the actual future eventually periodic. Section 4 excludes that.
Thus ALL source isotropy, ENTIRE H and extension kernel are zero.
No positive primitive packet exists. This does NOT prove all histories
terminate, no topological recurrence, kappa identically zero or a globally
defined Borel potential. Those are distinct claims, not consequences of H0.

Partial injectivity makes every full tail class an actual path, without
extra branches or selected representatives. All objects and real heights remain.

For a state terminating at omega after d legal steps, its full
tail class is the entire permitted backward chain I^j(omega), j>=0,
as long as each actual inverse exists. This chain may have arbitrarily
many ancestors; no finite-total-length assertion is made. Exact depth and
clock prefix give lag d(z)-d(w), c=S(z)-S(w), and full
phase eta-S(z). All source/time/extension isotropy is trivial. Different
terminal anchors never merge; no terminal clock is evaluated. All other
histories also have trivial isotropy. A set-theoretic anchor can specify a
relative phase in each such class, using its unique connecting arrow,
but no Borel transversal or natural global phase is asserted.

## 6. Three controls with their own image, clock and return ledger

### 6.1 DIVISIBILITY-OFF and DIVISIBILITY-SHIFT

OFF keeps floor h!=0 only; its own inverse (2) has image
floor s!=0. SHIFT requires floor h|(floor k+1); its own
image is floor s!=0 and floor s|(floor(st)+1). Both are
partial injections with their OWN Borel charts, IMAGE |s| and real
clock -log|h|. Equal analytic expressions do not identify their domains or histories.

For example target (2,2,0,0) has predecessor (0,2,0,4)
under main and OFF, but none under SHIFT because 2 does not
divide 5. Target (1,1,0,0) is terminal with predecessor
(0,1,0,1) under all three OWN filters. (0,1,0,0)
has no predecessor but is legal under each of them. No cut
or failed-permission object is deleted.

The fixed/two-step algebra AND cyclic-square identity in Section 4 apply
separately to both controls, since each uses the same actual quotient
and requires nonzero differences. Neither has ANY source cycle or eventual
cycle; all source isotropy, H and extension kernel are zero. Full
terminal chains/phases use ONLY their respective legal histories and images.
No altered-permission history or global termination claim transfers to main.

### 6.2 DIFFERENCE-QUOTIENT-OFF: zero clock with permitted four-cycles

This control keeps main D but uses the LINEAR transport

    Lz=(x1-x0,u1-u0,x0,u0),
    I_L(s,t,u,v)=(u,u+s,v,v+t),
    E_L={floor s!=0, floor s|floor t}.             (7)

Its inverse determinant is -1, so its OWN full Borel IMAGE is
1 and its full-point kappa/cocycle are identically zero. The main st
image and |s| density do not apply. For example (2,1,0,0)
has a main predecessor (0,2,0,2) but no L predecessor since
2 does not divide 1. The usual retained terminal/incoming distinction holds.

The linear matrix is

    M=[[-1,1,0,0],[0,0,-1,1],[1,0,0,0],[0,0,1,0]].

Its characteristic polynomial is

    lambda^4+lambda^3+lambda-1
      =(lambda^2+1)*(lambda^2+lambda-1).           (8)

All four eigenvalues are distinct. The two real roots (-1+sqrt5)/2
and (-1-sqrt5)/2 have absolute values below and above one, respectively;
no positive power equals one. The remaining roots are i and -i.
Consequently ANY real periodic vector must lie in ker(M^2+I), where
M^2=-I and M^4=I. This plane is explicitly

    z(A,B)=(A,B,A-B,-A).                           (9)

Actual periods also require every intermediate permission. Let h=B-A and
k=B-2A. The four successive difference pairs are

    (h,k), (-A,-B), (-h,-k), (A,B).              (10)

Thus the ENTIRE actual periodic locus of this control is the subset
of (9) where each pair in (10) has nonzero first floor
dividing the second floor. This is an exact four-condition characterization
over all real A,B and all cuts, not a sampled parameter set.
Origin is illegal. Every other permitted vector has least period FOUR:
M^2 z=-z cannot equal z for nonzero z, and fixedness would
imply that equality too. No other source period or eventual cycle exists
outside these actual four-cores; partial injectivity forbids external incoming tails.

The set is nonempty. A=1,B=2 gives the complete legal cycle

    (1,2,-1,-1) -> (1,0,1,-1)
      -> (-1,-2,1,1) -> (-1,0,-1,1) -> (1,2,-1,-1).

The four node differences are +1,-1,-1,+1, each dividing its
integer value difference (0,-2,0,2); all cuts/units remain. This
is an exact consequence of the short linear identity, not a general
four-dimensional cycle census. Source isotropy and extension kernel on EVERY
permitted core are 4Z, with H0. Its full basin is exactly
its four points. All other states have trivial source/time/extension isotropy.
Complete extension equivalence is actual L-tail equivalence plus equal eta.
This control proves real source recurrence need not imply positive time;
its recurrence does not repair the nonlinear main's separate no-cycle theorem.

## 7. Audit decision and limits

| Audit | Result for ANG-20260920-DQI01 | Limit |
| --- | --- | --- |
| T0 carrier / full inverse / all-point IMAGE | ESTABLISHED exact partial injection | Every terminal and incoming chain retained |
| T1 arithmetic feedback / owned clock | Explicit divisor seed and -log real difference | Stronger naturalness/canonical A0 OPEN |
| T2 return / primitive gate | ALL source periods absent; target FAILS, STOP / FORK | No global termination or topological-recurrence claim |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No imported object |
| Classical A0/A1/A2 | NOT APPLICABLE | No symplectic map/roof construction |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Same-object ledger intact. The owner-level inverse and clock calculation is
positive evidence. The cyclic-square obstruction now closes ALL source periods
for this owner, beyond the first draft's limited short-return conclusion.
Consequently all isotropy time images vanish and there are no positive
primitive packets, without an identically-zero step clock or termination theorem.
We stop this owner rather than tune its coordinates, permission or measure.

The linear control's complete four-cycle classification is separate, with its
own unit volume clock and zero time groups. Permission controls have
their own images even when the formula agrees. No selected section,
coordinate reorder, new measure or borrowed control construction repairs main.
All proofs are exact, with no scientific numerical run, finite precision,
cutoff, prime/zero input or external literature. Internal ARS three-checkpoint
scrutiny is NOT_CALIBRATED, not external peer review, machine proof or
independent-error evidence. No RH or Hilbert--Polya result follows.

See [card](candidate-card.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md),
[package](README.md). Positive 304, partial-positive 320 and old packages
unchanged; 241/242 paused; goal active. Markdown only; no PDF/LaTeX,
publication/upload or Git staging/commit.
