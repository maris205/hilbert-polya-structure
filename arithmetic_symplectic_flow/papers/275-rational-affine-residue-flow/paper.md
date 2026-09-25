# Full rational-affine residue dynamics: logarithmic index, no primitive packets

**Paper ID:** `275-rational-affine-residue-flow`  
**Candidate ID:** `ANG-20260919-RAF01`  
**Date:** 2026-09-19.  
**Status:** `OWNED AFFINE INDEX; NO PRIMITIVE RETURN PACKETS — STOP / FORK`.  
**Type:** exact bounded full-action and stabilizer audit.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We retain the full profinite integer source and every admissible
positive-rational affine map x -> qx+r. Finite residue observables
have an exact update interface. Additive Haar measure gives the Borel
image Jacobian 1/q and the complete same-object real clock log q.
However, every noninteger source state has no nontrivial stabilizer,
whereas each embedded integer has all positive rational dilations in
its affine stabilizer. Its time-return group is dense log Q_(>0),
with no least positive time. Thus no primitive cyclic-return packet
exists anywhere. The integer extension orbit is dense and not closed,
so the coarse quotient is not T1. No subgroup is chosen to manufacture
a prime period; all phases, null integer states and arrows remain.

## 1. Frozen source, lineage and question

The [card](candidate-card.md) freezes X=Z_hat, the inverse limit of
all integer residue rings, and its normalized additive Haar measure
mu. Let B=S^(-1)X for S=N_(>0). Let the discrete group

    Gamma=Q_(>0) semidirect Q,
    (q,r)(q',r')=(qq', qr'+r)

act on B by x -> qx+r. The full partial action on X is

    D_g={x in X: qx+r in X},
    theta_g(x)=qx+r,              g=(q,r).

All nonempty branches are retained. G has arrows (g,x) from x to
theta_g(x), with their labels and disjoint domain topologies. The
clock must be derived from this action's IMAGE Jacobian, not borrowed
from the multiplication-only action of 270.

| Field | Same-object definition / boundary |
| --- | --- |
| Source | Every compatible finite-residue word in X; no unit or tail quotient |
| Arithmetic evolution | All rational affine branches on their complete domains |
| Symbolic interface | All residue cylinders, including divisibility observables |
| Measure | Normalized ADDITIVE Haar probability on X |
| Clock / time | Derived negative log image Jacobian; real translation in its full extension |
| Packets | Actual isomorphism-class time stabilizers and groupoid/time equivalence |
| Classical symplectic base, mapping torus, Hamiltonian/contact owner | NOT APPLICABLE / NOT SUPPLIED |
| Analytic or quantum owner | NOT SUPPLIED; no T3 pursuit after the return stop |

The [prior-work arrow](../../docs/prior_work/README.md) is finite
prime/composite divisibility symbols -> compatible residue completion
-> full affine arithmetic updates of that same source. This preserves
an exact finite-language interface, not chronological sieve order,
integer order or a Logistic/Hénon conjugacy. No prime table, zero data,
selected prime subgroup, per-prime parameter or log-prime roof enters.
Completion, the affine group and Haar measure remain structural choices;
naturalness is OPEN. This is a bounded mechanism audit, not admission
as a promising prime-only architecture.

## 2. Full domains, localization and residue interface

### Lemma 1 — elementary profinite arithmetic

Multiplication by each positive integer m is injective on X, and
mX is the clopen kernel of reduction modulo m, of measure 1/m.
X and Q embed in B, and X intersect Q=Z inside B.

**Proof.** If mx=0, reduce modulo mN for any N. The coordinate of
x modulo mN must be a multiple of N, so x=0 modulo N for every N,
hence x=0 in X. The image mX is compact and thus closed, and lies
in the kernel of reduction modulo m. Conversely an element of that
kernel can be approximated in every residue coordinate by an integer
multiple of m: use its coordinate modulo mN for a desired modulus
N. Thus the kernel lies in the closed image mX. Its index is m,
so Haar measure gives mass 1/m.

The absence of integer torsion makes localization injective on X.
The integer embedding is injective, and its localization embeds Q.
If u/v in reduced form belongs to X, then vx=u in X. Reducing
modulo v forces v to divide u, hence v=1. Conversely every integer
belongs to X. This proves the intersection without selecting any
p-adic component. ∎

### Proposition 2 — exact affine partial action

Take any common-denominator presentation q=a/c, r=b/c with a,c>0
and b in Z, and let h=gcd(a,c). If h does not divide b, D_g is
empty. Otherwise choose an integer x_0 solving ax_0+b=0 mod c and
set y_0=(ax_0+b)/c. Then

    D_g=x_0+(c/h)X,
    theta_g(D_g)=y_0+(a/h)X,
    theta_g(x_0+(c/h)z)=y_0+(a/h)z.

These are clopen sets and theta_g is a homeomorphism between them.
The definition is independent of the presentation. The inverse label
is (q^(-1),−r/q), and the complete composition-domain rule is

    x in D_k and theta_k(x) in D_g
       iff x in D_k intersect D_(gk).

On that domain theta_g theta_k=theta_(gk). In particular the product
domain must not be replaced by all of D_(gk) without its intermediate
state condition.

**Proof.** Membership ax+b in cX is precisely the finite congruence
ax=−b mod c by Lemma 1. The elementary congruence is solvable iff
h|b; its complete solution set modulo c is x_0+(c/h)Z modulo c.
Taking all compatible residues gives the displayed coset in X.
Substitution gives its exact image and parametrization. Multiplication
by a positive integer is a continuous injection of compact X into
Hausdorff X, hence a homeomorphism onto its image. Translation then
proves the asserted branch homeomorphism.

All formulas express the single element qx+r in B, so changes of
common denominator or choice of x_0 do not change the map or domain.
The affine inverse and group product are valid on B. Restricting to
X gives precisely the inverse domains and the intermediate-state
composition condition written above. ∎

For every residue cylinder t+mX the exact symbolic update is

    theta_g(x) in t+mX
       iff ax+b−ct in cmX.

Indeed multiply the first membership by c; the converse follows
by injectivity of multiplication by c. The right side also implies
the domain condition. Thus each finite residue question after an
update is a finite congruence before it. This is an explicit source
interface, not an external sieve applied to a separately chosen orbit.

As a useful edge case, q=1 has a nonempty domain exactly when r is
an integer. Then theta is translation on all X. A noninteger rational
translation alone has empty domain: a difference of two X elements
would put r in X intersect Q, contradicting Lemma 1.

## 3. Same-object Borel clock and complete time

### Proposition 3 — image Jacobian and topology

For every nonempty affine branch and every Borel E in D_g,

    mu(theta_g E)=q^(-1)mu(E).

Consequently c(g,x)=log q is a continuous additive cocycle on the
entire G, including its null source states. G is locally compact
Hausdorff, second countable and étale. Its real cocycle extension
and physical translation time are complete and continuous.

**Proof.** For every positive m and Borel A in X,
mu(mA)=mu(A)/m. First check this on residue cosets, where their
images have the corresponding m-fold larger modulus, and extend by
uniqueness of finite Borel measures on the generating cylinder
algebra. Translation invariance and Proposition 2 now give

    mu(x_0+(c/h)A)=(h/c)mu(A),
    mu(y_0+(a/h)A)=(h/a)mu(A).

Their ratio is c/a=1/q. This proves the image identity for every
Borel E by the branch parametrization, including presentations
that have not been reduced. It also fixes the sign of the clock.
The value is unchanged by the translation r, but admissible domains
and isotropy depend on r and have not been ignored.

Each group label has a compact-open domain or is absent. Domain
charts form bisections: source is its inclusion and range is the
proved branch homeomorphism. The countable disjoint union is locally
compact Hausdorff and second countable. The explicit product-domain
law and continuous affine maps make multiplication and inversion
continuous. Thus G is étale. Its clock is constant on each label
chart and additive because log(qq')=log q+log q'. Every nonempty
open source subset has positive Haar measure, so its continuous
Jacobian version is unique even at individual null points.

Extension arrows go from (x,u) to (theta_g x,u+log q), with
topology G×R. On a bisection times an open real interval, source
and range are homeomorphisms onto open object subsets. The extension
is locally compact Hausdorff and étale. Translation u->u+t is a
jointly continuous automorphism for all real t and has inverse
translation by −t. This is the whole physical-time owner; there
is no extra positive roof or possible finite-time blowup. ∎

Every singleton of X is null: it is contained in a residue cylinder
of measure 1/m for every m. In particular embedded integers are a
countable null set. They remain in the full source and clock audit.

## 4. Full stabilizers: none is a primitive cyclic clock

### Proposition 4 — complete return classification

For x outside the embedded integers Z, base isotropy is trivial and
H_x={0}. For each n in Z, base isotropy is

    Gamma_n={(q,(1−q)n):q in Q_(>0)},

and H_n=log Q_(>0), a dense subgroup of R without a least positive
element. Extension fixed-object isotropy is trivial everywhere.
No primitive cyclic-return packet exists on the frozen owner.

**Proof.** A fixed arrow satisfies (q−1)x=−r in B. If q=1,
it requires r=0 and is the identity. If q!=1, it forces the unique
rational value x=−r/(q−1); Lemma 1 then forces x to be an integer.
Conversely for every integer n and EVERY positive rational q, the
choice r=(1−q)n is rational and fixes n. Its domain contains n
because its image n lies in X. No dilation has been excluded.

The clock image of that full stabilizer is log Q_(>0). It is dense
because Q_(>0) is dense in R_(>0) and log is a homeomorphism to R.
In particular log((k+1)/k)>0 tends to zero, so there is no least
positive time. Selecting q=p would hide other stabilizer arrows
and change the owner. At an integer, clock zero forces q=1 and
then r=0; at a noninteger base isotropy was already trivial.
This proves the extension-isotropy assertion and the absence of
any H_x=T Z with T>0. ∎

Thus finding an individual arrow with clock log p is not finding a
primitive log-prime packet. Under the full affine action all primes,
composites, zero and negative embedded integers have the SAME dense
time-return group. Nonintegers have no positive return at all. This
is a full algebraic classification, not a finite census.

## 5. Precommitted coarse-topology control

### Proposition 5 — dense nonclosed integer extension orbit

The extension orbit of (0,u) is exactly

    Z × (u+log Q_(>0)).

It is dense and proper in X×R. The coarse quotient by extension
arrows is therefore not T1 and not Hausdorff.

**Proof.** An arrow from zero has range r, so r must lie in
Q intersect X=Z, and its target time is u+log q. Conversely every
integer r and positive rational q give such an arrow at zero.
Embedded Z is dense in X by the finite-residue definition, and
the logarithmic rational subgroup is dense in R. Their product
is dense. The orbit is countable, whereas its ambient real factor
is uncountable, so it is proper and not closed. The inverse image
of its quotient singleton is this nonclosed orbit; that singleton
cannot be closed. ∎

This is a separate topology control, not an attempt to rescue the
already failed primitive-clock test. Hausdorff arrow/object spaces
alone do not supply Hausdorff embedded physical flow circles.

## 6. Gate assessment and portfolio decision

| Gate / control | Result | Boundary |
| --- | --- | --- |
| T0 | Full partial action, groupoid and complete time established | Coarse quotient not T1/Hausdorff |
| T1 | Exact finite-residue interface and Haar-derived image clock log q | Naturalness of completion/action/measure OPEN |
| T2 | All H_x classified: {0} or dense log Q_(>0) | No primitive cyclic-return packet anywhere |
| T3 | NOT SUPPLIED / NOT PURSUED | No trace, zeta, determinant, spectral owner or correction |
| Translation control | Integer translations act on all X; other rational translations alone have empty domain | Full affine domains, not a fictitious global action on X |
| Prime-generator control | A q=p fixed arrow exists at each integer but is not a least return | Full stabilizer cannot be replaced by p^Z |
| Null-state control | All integer states are null but retained | No almost-everywhere deletion |
| Ownership control | All residue phases and arrows retained | Neither 271's unit quotient nor a borrowed clock/packet |

Portfolio: **stop target promotion / fork**. Adding translations
changes the source action and moves the nontrivial stabilizers to
all embedded integers, but does not produce a least positive return.
The decisive reason is the full stabilizer, not a failed Jacobian
formula. A future carrier or acting subgroup must be separately
defined and justified; selecting a prime generator here is prohibited.

The same-object ledger stayed intact. Classical A0/A1/A2 NOT
APPLICABLE, formal coordinates UNASSIGNED, Route B NOT INVOKED.
241/242 remain paused; the open-ended goal remains active. This is
not a theorem against all affine arithmetic dynamics and not a
novelty claim about rational affine groupoids.

## 7. Reproducibility and disclosure

Exact inputs are X, its Haar measure, the algebraic localization,
ALL positive-rational affine labels, all complete domains and the
frozen image/time convention. Methods are finite congruences, integer
torsion cancellation, uniqueness of Borel measures, affine fixed
equations and density. No numerical approximation, experiment,
cutoff, optimization or cycle enumeration was used.

See [claim scopes](claim-ledger.md), [evidence and provenance](evidence/README.md),
[other scout dispositions](evidence/scout-record.md), and the
[separate internal review](evidence/independent-review.md).
AI-assisted research and native shared-context/model-lineage review
were used. Internal review is not external peer review or formal
proof verification. No earlier candidate, Phase-I source, PDF/LaTeX
or publication artifact was modified.
