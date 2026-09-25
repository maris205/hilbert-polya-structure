# Strict residue generation changes domains, but not the return obstruction

Candidate ID: `ANG-20260920-CRG01`.
Paper ID: `295-canonical-residue-generated-flow`. Date: 2026-09-20.
Status: `STRICT GENERATED DOMAINS; NO PRIMITIVE TIME PACKETS — STOP / FORK`.
Result type: exact generated-owner, IMAGE-clock and all-state return audit.

## Abstract

Canonical residue embeddings and their strict inverses generate a
proper subowner of the maximal rational-affine residue action. The
generated translation +1 has domain Z_hat minus {-1}; translation -1
has domain Z_hat minus {0}. All noninteger seeds are included in these
formulas. The embedded integers split into two actual generated orbits,
nonnegative and negative. Nevertheless the own Haar IMAGE clock has
full return group log Q_(>0) at every integer and zero at every
noninteger. Thus no state has a least positive time return. The domain
distinction is real, but does not resolve the primitive-packet obstruction.
We stop promotion without maximal-domain completion, selected scale
subgroups, extra word lag, state deletion or analytic rescue.

## 1. Frozen owner and the previously open question

The original [card](candidate-card.md) has SHA-256

    18c85fe523becc702dc9204468b874846ab775ee95fd323ce30812c36a0f41de

This audits the exact lane-R proposal left OPEN in
[290](../290-composition-admission-frontier/candidate-card.md).
Root's prefreeze definition ideation suggested an integer-boundary
discriminator; the card does not claim a blind freeze before that
idea. All theorem statements below follow the new contract.

Set K=Z_hat, with normalized additive Haar h, and B=S^(-1)K for
S=N_(>0). On ALL K use only

    theta_(n,j):x -> nx+j, domain K, image j+nK,
    theta_(n,j)^(-1):x -> (x-j)/n, domain j+nK,
    n>=1, 0<=j<n.

Arrows are finite valid words, identified by their actual rational-affine
label (q,r) and source x, not by a free word or extra lag. Thus
G_gen consists of (q,r,x) actually realized by such a word at x.
No generator is silently extended beyond its strict intermediate domains.

| Same-object item | Frozen content | Boundary |
|---|---|---|
| Source and symbols | All compatible residue phases in K; canonical integer digits | All integers, nonintegers and null states retained |
| Arrows | Actual finite branch/inverse compositions and their affine labels | Neither germs nor maximal-domain completion |
| Measure and time | Own Haar IMAGE law; full real cocycle extension | No supplied positive roof or log-prime periods |
| Returns | Full H_x from all generated isotropy arrows | One selected scale loop cannot define primitivity |
| Geometry / analytic object | Classical fields NOT APPLICABLE; analytic owner NOT SUPPLIED | No borrowed symplectic, trace or quantum owner |

The precise lineage is residue/divisibility symbols -> canonical
embeddings -> radix/factor composition with actual intermediate
admissibility. It is a source replacement, not a proved Logistic/Hénon
conjugacy or finite-dimensional lift. Generator/measure/completion
naturalness remains OPEN. There is no prime table, fitted parameter,
specified prime subgroup, von Mangoldt weight or zero input.

The [275 comparator](../275-rational-affine-residue-flow/candidate-card.md)
instead permits every rational-affine label wherever its endpoints lie
in K. Its negative return theorem is NOT a proof for the generated
owner. We derive the present domains, clock and stabilizers directly.

## 2. Generated domains and topological ownership

Nonzero integer multiplication on K is injective: in its product of
p-adic integer components it is injective in each component. Equivalently
this follows from compatible integer residues. Thus K embeds in B,
and Q embeds by rational multiples of 1. Their intersection is exactly
Z: if a/c in Q lies in K, then a lies in cK, so the ordinary
congruence a=0 mod c gives c|a. Conversely integers belong to both.
No integral-domain or field property of K is assumed.

**Proposition 1.** Every finite valid word is a homeomorphism between
clopen subsets of K. Its label (q,r) acts there by x->qx+r in B.
For a fixed label, the union D_gen(q,r) of its word domains is open.
These domains define a topological groupoid with source/range local
homeomorphisms and with the actual affine composition law.

*Proof.* A generator is a homeomorphism onto j+nK; its strict inverse
is continuous there. Composition restricts the first clopen domain
by the inverse image of the next clopen domain, again clopen. Inverse
words give clopen images. Induction also proves the affine label and

    (q,r)(q',r')=(qq',qr'+r).

There are countably many finite words, so each D_gen is a countable
union of clopen sets. At every arrow one realizing word gives an
open source chart and a homeomorphic range chart. Word concatenation
and reversal supply the groupoid laws on precisely the actual valid
domains. Continuity follows on these charts with discrete affine
labels. The arrow space is the open subset consisting of these
label-domain pieces in (Q_(>0) semidirect Q) x K, so is Hausdorff
and locally compact; no such separation claim for its orbit quotient
is implied. QED.

The symbolic factor identity is an exact identity of full-domain
generators:

    theta_(m,i) theta_(n,j)=theta_(mn,i+mj),
    0<=i+mj<mn.

This records genuine digit composition. It does not settle the
domains of words containing strict inverses or the full time stabilizer.

**Theorem 2.** The exact generated translation domains are

    D_gen(1,1)=K minus {-1},
    D_gen(1,-1)=K minus {0}.

The embedded integers form exactly two generated orbits,
Z_(>=0) and Z_(<=-1). Thus G_gen is strictly smaller than the
maximal-domain affine owner, even though all affine formulas look alike.

*Proof.* Every generator preserves both integer half-lines: for k>=0,
nk+j>=0; for k<=-1, nk+j<=-1. A strict inverse, when defined at
an integer, returns its integer quotient after canonical remainder
removal. That quotient is nonnegative in the first case and negative
in the second. No intermediate step can move an integer to a noninteger.
Hence no valid word sends -1 to 0 or 0 to -1.

For x!=-1 there is an n with canonical residue j<=n-2, since
having residue n-1 for EVERY n is exactly x=-1 in the inverse limit.
On the full clopen set j+nK the valid word

    theta_(n,j+1) theta_(n,j)^(-1)

is translation +1. This proves inclusion of every x except -1;
the half-line obstruction proves the missing point is impossible.
Similarly, every x!=0 has a residue j>=1 for some n, and

    theta_(n,j-1) theta_(n,j)^(-1)

gives translation -1 there. The only missing point is 0. These
arguments apply to all K, not only to embedded integers.

Finally theta_(k+1,k) sends 0 to every integer k>=0, and
theta_(n,0) sends -1 to every -n<=-1. Together with the invariant
half-lines this proves the two complete integer orbits. Maximal affine
translations have domain all K, proving strict inequality of owners.
QED.

The two punctured domains are open but not closed: K has no isolated
points, since every residue neighbourhood contains further integer
translates of any one of its points. Hence even the claim that every
generated label domain is clopen would be false. Other arbitrary
D_gen(q,r) are not classified in this bounded audit.

## 3. The generated owner's own IMAGE clock

**Proposition 3.** On each actual label domain, the Borel IMAGE law is

    h((qx+r)_(x in E))=h(E)/q, E subset D_gen(q,r) Borel.

Thus c(q,r,x)=log q is a continuous additive full-point cocycle.
Its real extension carries a jointly continuous complete R-action.

*Proof.* Multiplication by n identifies Haar on K with normalized
Haar on the index-n subgroup nK. Ambient mass of that subgroup is
1/n, and translation preserves Haar. Therefore every theta_(n,j)
has IMAGE factor 1/n on every Borel set, and its strict inverse has
factor n. Multiplying these factors along a valid word gives 1/q.
The answer depends on its actual affine label, not the chosen word.

To patch the law on the union domain, enumerate the word domains
for that label and partition E into disjoint Borel pieces by the
first domain containing each point. The affine map is injective,
so their images are disjoint; countable additivity gives the displayed
law on all E. Thus c=-log IMAGE is log q everywhere, including
null boundary points. Discrete labels make c continuous, and the
affine composition law makes it additive.

The extension arrow is

    (x,u) -> (qx+r,u+log q).

Every branch chart gives a homeomorphism of open subsets of K x R,
so orbit saturation and the orbit projection are open. Real translation
in u commutes with arrows and descends. Since the product of an open
quotient map with the identity is a quotient map, this descended
action is jointly continuous. It is defined for all real times and
therefore two-sided complete. QED.

The clock is derived from the full-support measure on actual domains;
it was not assigned only to fixed points or chosen prime loops.
Coarse quotient separation and embedded-circle properties are not audited.

## 4. Complete time-return classification

**Theorem 4.** For every x in K,

    H_x=log Q_(>0)  if x is an embedded integer,
    H_x={0}         otherwise.

At an integer k the entire base isotropy is exactly
{(q,(1-q)k,k):q in Q_(>0)}; at a noninteger it is only the
identity label. Fixed-object extension isotropy is trivial everywhere.
There is no primitive cyclic time packet anywhere on the full owner.

*Proof.* If an affine arrow fixes x, then (q-1)x=-r in B.
For q!=1 division by the nonzero rational q-1 gives x in Q,
so Q intersect K=Z forces x to be an integer. For q=1 the
equation forces r=0, the identity label. This proves the noninteger
assertion and bounds integer isotropy by the stated list.

At 0, every theta_(n,0) and its strict inverse fixes 0.
Composing a scale a with the inverse scale b realizes every positive
rational q=a/b. At -1 the same statement holds with
theta_(n,n-1), since n(-1)+(n-1)=-1. The generated arrows of
Theorem 2 connect each remaining integer to one of these two points.
Conjugating their scale loops gives a valid generated loop at that
integer, with the same q and necessarily r=(1-q)k. Thus the full
list, not merely a selected subgroup, is realized.

Applying the owned clock gives H_k=log Q_(>0). This group contains
the strictly positive numbers log((N+1)/N) tending to zero, so
has no least positive element. It is dense: arbitrarily small positive
group elements and their integer multiples approximate any real
number. It is proper since it is countable. A noninteger has no
positive return at all. Neither case meets H_x=T Z with T>0.

Finally an extension arrow fixing (x,u) must have log q=0,
hence q=1; its base fixed equation gives r=0. With actual labels,
this is the identity, not an extra free-word isotropy element. QED.

The returning source locus is exactly the embedded integers, a
countable Haar-null set; singleton mass is bounded by 1/n for every
modulus n. Nullness does not remove these states from the frozen
owner. Their two different source orbits both have the dense full
time group. No nonreturning-orbit classification is needed or claimed.

## 5. Controls, failure reason and next decision

| Frozen discriminator | Exact result | Scope lesson |
|---|---|---|
| Strict versus maximal affine translations | Two singleton domain exclusions and two integer orbits | Generated and maximal owners are genuinely different |
| Identity scale n=1 | theta_(1,0)=identity, clock zero | No unit roof or runtime substitution |
| One selected scale at 0 | Its powers give a cyclic subgroup | Not the full time stabilizer and not a primitive-packet proof |
| Complete scale loops | log((N+1)/N)>0 tends to zero | The full owner has no least positive return |
| Actual composition theta_(2,0)^2=theta_(4,0) | Equality of actual labels and maps | A genuine power identity still does not choose a primitive among all loops |
| Integer versus noninteger points | Dense time group versus zero group | No hidden noninteger cyclic-return sector |

This resolves the particular OPEN comparison from 290 without changing
that historical package. The strict boundary constraint is an actual
arithmetic admissibility effect, but insufficient for prime-primitive
organization: every returning state admits incompatible scales under
the full generated action. Strong naturalness remains OPEN, and this
is not a no-go for all residue-symbolic dynamics or restricted actions.

Portfolio: **stop primitive-packet promotion / fork search**. T0 and
scoped clock T1 are established. T2 has a complete all-state stabilizer
classification and no primitive cyclic packets. T3 NOT SUPPLIED /
NOT PURSUED. Classical A0/A1/A2 NOT APPLICABLE; formal coordinates
UNASSIGNED; Route B NOT INVOKED. No selected scale subgroup, changed
roof, maximal completion, removed integer or borrowed determinant is used.

The [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md) and
[parallel breadth record](evidence/scout-record.md) preserve the limits.
ARS checkpoints are internal shared-model/context review, not external
peer review, formal verification or independent-error evidence. No
scientific numerical run or external theorem is used. Old packages
and mirrors remain unchanged; 241/242 paused; programme goal active.
