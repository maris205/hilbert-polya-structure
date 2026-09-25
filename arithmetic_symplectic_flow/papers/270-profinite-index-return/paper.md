# An intrinsic index cocycle without primitive return packets

**Paper ID:** `270-profinite-index-return`  
**Candidate ID:** `ANG-20260919-PIR01`  
**Date:** 2026-09-19. **Evidence:** exact source/owner construction and negative proof.  
**Status:** `OWNED HAAR INDEX; NO PRIMITIVE RETURN PACKETS — STOP / FORK`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The full profinite completion of integer residue words retains all finite
divisibility observables. Positive rational multiplication defines a
partial-action groupoid on this carrier. Its normalized additive Haar
measure gives the exact image Jacobian J_q=1/q and the additive cocycle
c(q)=log q, without a prescribed prime roof. The complete cocycle
extension owns continuous real-coordinate translation by groupoid
automorphisms. Nevertheless its full time-return equation has a decisive
answer: every nonzero profinite state has return subgroup {0}, while the
zero state has the dense subgroup log Q_{>0}. No object has a least
positive return time, so the frozen primitive-packet convention yields
no primitive circle. The coarse orbit space is not even T1, although
the groupoid itself is Hausdorff. The arithmetic index construction is
retained, but it cannot be identified with a prime closed-orbit clock.
No unit quotient, state deletion, cyclic-subgroup selection or analytic
replacement is made after this stop.

## 1. Question, lineage and exact owner

The [card](candidate-card.md) asks whether a time cocycle derived from
the SAME arithmetic action's counting index also supplies primitive
return packets. Unlike a roof chosen to have value log p, the proposed
clock must first be derived as a measure-scaling cocycle and then tested
against the full return equation.

The source interface starts with n↦(n mod m)_(m>=1), for all n in Z,
and completes these compatible residue words to

    X=lim_inverse Z/mZ = Z_hat.

For d>=1 put e_d(x)=1_(dX)(x), with e_1=1. Finite divisor-exclusion
masks are products of 1−e_d over finite sets of integer moduli. Section 2
proves that these are exactly the original divisibility observations on
embedded integers and that they intertwine with integer multiplication.
This specifies the retained prime/composite-observable -> symbolic
completion -> arithmetic-action arrow. It is not merely shared terminology.

The completion replaces the ordered integer carrier: it does not retain
chronological sieve stages, integer order or an automatically continuous
global primality predicate. In particular the varying test range d<n
used in testing a positive integer's primality is not supplied by a
profinite coordinate. No Logistic/Hénon conjugacy or conservative lift
is claimed. These boundaries are part of the declared replacement of
the [prior-work source](../../docs/prior_work/README.md).

| Same-object field | Unchanged definition |
| --- | --- |
| Arithmetic objects | All x in X, including zero; profinite topology |
| Partial arrows | q=a/b>0 reduced, theta_q:bX→aX, theta_q(by)=ay |
| Source measure | Normalized additive Haar measure mu on X |
| Clock | Negative logarithm of the same action's image Jacobian |
| Extension | (q,x,u):(x,u)→(theta_q x,u+c(q,x)), all u in R |
| Actual time action | Phi^t(x,u)=(x,u+t), extended to all arrows |
| Packet convention | Return up to an extension arrow, requiring a least positive period |
| Unavailable classical fields | No smooth symplectic base or mapping-torus suspension |
| Analytic owner | No C*-algebra, trace, zeta, determinant or quantum operator supplied |

Rational scaling and norm-type time are standard arithmetic constructions,
not new claims of this paper. The primary background is
[Neshveyev's rational-action formulation](https://arxiv.org/pdf/math/0002141),
which states the finite-adele action and its time character, and
[Laca's dilation description](https://arxiv.org/abs/math/9911135).
Our packet convention and its proof below are not inferred from their
operator or equilibrium-state results. The earlier
[061 external-control verdict](../061-bost-connes-lineage-boundary/paper.md)
is unchanged: this fresh card supplies its own explicit observable
replacement and point-return convention, not retroactive credit.

## 2. Arithmetic source and partial-action ownership

### Proposition 1 — full residue interface and groupoid

Integer multiplication on X is injective for every nonzero integer.
For each n>=1, nX is the kernel of reduction modulo n, has index n,
and multiplication by n is a homeomorphism X→nX. All theta_q are
well-defined partial homeomorphisms with their displayed domains and
images. Their arrows form a locally compact Hausdorff étale groupoid G.

**Proof.** Suppose nx=0, with n>=1. For every k, reduce modulo nk.
The equality n x_(nk)=0 mod nk forces x_(nk)=0 mod k. Compatibility
gives x_k=0 for every k, so x=0. A negative multiplier differs only by
the invertible sign. This proves injectivity without assuming that X
has no zero divisors as a ring.

Certainly nX lies in the kernel modulo n. Conversely, if x mod n=0,
choose its residue modulo nk, divide this multiple of n by n, and
reduce modulo k. The resulting y_k are well-defined and compatible;
they give y in X with ny=x. Thus the kernel equals nX. Reduction
modulo n is onto, so there are exactly n cosets, all clopen. The
continuous injective map X→nX is a homeomorphism, since X is compact
Hausdorff. Hence theta_(a/b) is a homeomorphism bX→aX, with inverse
theta_(b/a).

For the groupoid laws, embed the torsion-free additive group X into
V=Q tensor_Z X. Scalar multiplication by Q_{>0} is a genuine action
there. For coprime a,b, the set of x in X with (a/b)x in X is exactly
bX: if ax=by with y in X and ra+sb=1, then

    x=r ax+s bx=b(ry+sx).

The converse is immediate. Thus G is the restriction of this scalar
action to X. Composable partial arrows multiply their rational labels;
associativity, identities and inverses follow without incorrectly
requiring every partial composition to have the maximal product domain.

Topologize G as the disjoint union of the clopen domains bX, one for
each reduced q. Source and target are homeomorphisms from each such
component to open subsets of X. Products and inversion are continuous
on these components. Their disjoint union is locally compact Hausdorff,
and source/target are local homeomorphisms, as asserted. ∎

The integer embedding is injective: an integer zero modulo every m
is zero. It is dense: any finite compatible set of residues is matched
by a representative modulo their least common multiple. It intertwines
all multiplication arrows and their admissible integer divisions.
Furthermore e_d(r(n))=1 exactly when d divides n.

For k>=1 and d>=1, let g=gcd(d,k), d=g d', k=g k', with gcd(d',k')=1.
Injectivity of multiplication by g and invertibility of k' modulo d'
give

    kx in dX  iff  k'x in d'X  iff  x in d'X.

Consequently the exact symbolic interface is

    e_d(theta_k x)=e_(d/gcd(d,k))(x).                         (1)

On bX, division additionally satisfies e_d(theta_(1/b)x)=e_(bd)(x).
These relations preserve every finite source mask within the full
carrier. They do not produce an endogenous prime enumeration or a
global prime-to-closed-orbit dictionary.

## 3. Same-action index and complete time extension

### Proposition 2 — exact image Jacobian and cocycle

For every Borel E contained in bX and reduced q=a/b>0,

    mu(theta_q E)=(b/a) mu(E),
    J_q=1/q,   c(q,x)=log q.                                 (2)

The cocycle extension G_c is a locally compact Hausdorff étale groupoid
on X×R. Translation Phi is a jointly continuous complete real action by
automorphisms of that SAME extension.

**Proof.** The normalized Haar measure gives each of the n cosets of
nX equal measure 1/n. For a cylinder B=r+mX, its image under n is
nr+nmX, so

    mu(nB)=1/(nm)=mu(B)/n.

The finite measures B↦mu(nB) and B↦mu(B)/n agree on the clopen
cylinder algebra, which generates the Borel sets of the metrizable
profinite space. Therefore they agree on every Borel B in X. Write
E=bB using the homeomorphism in Proposition 1. Then theta_q E=aB,
so mu(E)=mu(B)/b and mu(theta_q E)=mu(B)/a, proving (2), including
null sets without taking an undefined ratio of zero measures.

The sign is an IMAGE Jacobian: multiplication by 2 halves measure,
so c(2)=log 2. An inverse arrow has J_(1/q)=q and c(1/q)=−log q.
For composable arrows, log(q'q)=log q'+log q. This is the required
cocycle law, derived from the same measure action, not a prime roof.

The complete extension has arrows

    (q,x,u):(x,u)→(theta_q x,u+log q).

Each q-component has source domain bX×R and target aX×R, related by
a homeomorphism. The same argument as in Proposition 1 proves the
stated topological groupoid properties. Composition adds the two
logarithms; inversion is

    (q,x,u)^{-1}=(q^{-1},theta_q x,u+log q).

Translating u by any real t commutes with source, target, composition
and inversion. It is jointly continuous on objects and arrows, with
inverse translation by −t. It is therefore complete. No roof crossing
or non-Zeno inference is needed for this real-coordinate action. ∎

This establishes an owned arithmetic INDEX time. It does not yet
establish any return period, and the choice of completion, measure and
extension remains a declared design rather than a natural-A0 theorem.

## 4. Complete return classification and topology stop

### Proposition 3 — no primitive packet anywhere in the frozen owner

For every u in R the time-return subgroup of (x,u) is

    H_x={0},                      if x != 0,
    H_0=log Q_{>0},                if x = 0.                   (3)

In particular, no object has a least positive return time. The groupoid
G_c has trivial isotropy at every fixed object, while the coarse orbit
space (X×R)/G_c is not T1 and hence not Hausdorff.

**Proof.** A return up to an extension arrow is exactly

    theta_q x=x,   t=log q.                                  (4)

If q=a/b and x=by, the first equation says ay=by, hence
(a−b)y=0. If a!=b, Proposition 1 forces y=0 and x=0. Thus for
nonzero x only q=1 is possible, giving H_x={0}. At x=0 every
positive rational is admissible and fixes the source, giving H_0
as in (3). The logarithm of the dense subgroup Q_{>0} is dense in R.
Explicitly, log(1+1/n)>0 tends to zero. Therefore H_0 has no least
positive element and is not T Z for any T>0. This exhausts all x;
it is not a finite sample or an almost-everywhere statement.

Isotropy of G_c at the unchanged object (x,u) additionally requires
u+log q=u. Thus q=1 and the arrow is a unit, including at zero.
This is different from the time-return subgroup, which permits an
arrow to a DIFFERENT object (x,u+t) in the same isomorphism class.

Finally, the complete extension orbit of (0,0) is

    {0} x log Q_{>0}.

It is not closed in X×R: choose positive rationals tending to sqrt(2).
Their logarithms tend to log sqrt(2), which is not in log Q_{>0}.
If the corresponding coarse quotient point were closed, its preimage
would be closed. Hence the coarse space fails T1. This does not
contradict the Hausdorff arrow and object spaces of G_c. ∎

The three distinct notions are therefore:

| Object notion | At x!=0 | At x=0 |
| --- | --- | --- |
| Isotropy in the original G | Trivial | Q_{>0} |
| Isotropy at fixed (x,u) in G_c | Trivial | Trivial |
| Stabilizer of time on isomorphism classes | {0} | log Q_{>0}, dense |

Raw translation on X×R has no point returns at all. The frozen packet
test is the third row, not raw equality of coordinates and not the
first row's abstract choice of a group generator. Under that test the
primitive packet set is empty. In particular, c(p)=log p is an exact
arrow value and a zero-state return, but NEVER a least positive period
of this full object. There are no primitive circles whose repetitions
could furnish the proposed prime-power ledger.

## 5. Controls and limits

1. **Actual source update:** theta_2(1)=2!=1. The exact index log 2
   is not a return time of the embedded integer 1. Formula (1) checks
   how all its divisor symbols change under the same arrow.
2. **Inverse and normalization:** theta_(1/2) has domain 2X and
   doubles image measure, giving c=−log 2. Omitting inverse arrows
   would change the groupoid and would not preserve its return test.
3. **Full zero state:** all positive rational arrows act there. Selecting
   a particular prime among them hides arbitrarily smaller returns.
   Zero is retained, not removed as an inconvenient exceptional point.
4. **Changed cyclic-arrow control:** restrict rational labels to powers
   of a single integer n>=2. Over zero alone the corresponding coarse
   time orbit is R/(log n)Z, a circle. This works just as well for n=6
   as for n=2, and is a DIFFERENT arrow system. It neither proves prime
   selection nor repairs the full rational-arrow owner. The card does
   not make this restriction.

The result excludes the frozen full-owner primitive-packet convention,
not every possible operator-theoretic arithmetic observable. In
particular no KMS, equilibrium-state, trace or determinant theorem is
asserted or refuted. A later unit quotient, different completion or
new notion of packet would require a fresh card. The different
[029 index-cocycle stop](../029-primorial-index-cocycle-screen/paper.md)
concerned stage advancement; here genuine inverse arrows exist, but
the complete stabilizer calculation still supplies no primitive time.

## 6. Gate assessment and decision

| Obligation | Evidence for PIR01 | Disposition |
| --- | --- | --- |
| Source interface | Dense integer residue embedding and equation (1) | Exact finite-observable replacement; no chronological-sieve claim |
| T0 groupoid owner | Propositions 1–2 | Established for G and G_c with complete time action |
| Coarse point-flow topology | Proposition 3 | Not T1 / not Hausdorff; no classical point-flow upgrade |
| T1 owned index time | Equation (2) | Established; stronger naturalness remains OPEN |
| T2 primitive return packets | Complete equation (3) | Scoped FAIL: none have a least positive return |
| T3 | No analytic owner supplied | NOT SUPPLIED / NOT ADVANCED |
| Classical A0/A1/A2 | No symplectic-map suspension | NOT APPLICABLE |
| Formal Route coordinates | No formal evaluation | UNASSIGNED |
| Route B | Not invoked | NOT INVOKED |

**Portfolio: stop PIR01 target promotion and fork.** The decisive
reason is absence of a discrete nonzero cyclic time stabilizer anywhere
in the complete owner. An intrinsic arithmetic index is real progress
in identifying what the clock actually belongs to, but it cannot be
substituted for an intrinsic prime closed orbit. Source naturalness and
the original programme remain unresolved, not solved by this negative
audit. No state, arrow, clock or packet convention was changed.

## Evidence and disclosure

The [claim ledger](claim-ledger.md) bounds each result. The
[evidence index](evidence/README.md) records source identity, frozen
hashes, review and document checks. The proof is exact and uses no
numerical approximation or finite periodic census. The primary-source
read was a bounded provenance check, not a literature-completeness claim.

This is AI-assisted research. A definition-level scout proposed the
architecture; root derived and wrote the proofs; a separate native
model worker independently checked the raw card before manuscript
comparison. Same-family internal review is not external peer review or
proof of independent errors. ARS supplies the staged adverse checking
and explicit evidence limits. No PDF, publication, Route-B evaluation
or restart of paused 241/242 was undertaken. The programme goal stays active.
