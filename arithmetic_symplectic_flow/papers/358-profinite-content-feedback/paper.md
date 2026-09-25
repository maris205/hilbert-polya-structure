# Profinite division owns a Haar clock; bounded fixed-point tests do not decide its packets

**Candidate:** `ANG-20260921-PCF01`.  
**Status:** `OWNED HAAR CONTENT CLOCK; BOUNDED FIXED-POINT TESTS NEGATIVE; T2 OPEN`.

## 1. Outcome, without a false closure

On the [frozen full source](candidate-card.md), current common content is
well-defined, and actual single-register division has inverse Haar IMAGE1/d.
The nonlinear feedback preserves this exact branch factor. Thus the full
actual Borel groupoid and all-point real clock extension are owned; log d
is derived from this SAME division's measure, not supplied as a roof.
The MAIN object has no fixed source of content1 or2, by congruences valid
on their entire profinite fibers. Nothing here excludes larger-content
fixed sources or longer cycles. MAIN's prime-packet target remains OPEN.

The feedback-off control instead has a continuum of primitive packets
of least log d for every d>=2, with all incoming accounted for. This is a
control failure, not MAIN's failure. The total content-off control has
zero IMAGE time; the constant-off control has no fixed sources, but its
longer cycles remain unclassified. No selected prime or unit carrier is used.
This is round4/5; the bounded mathematical task is complete, not T2 closed.

## 2. Whole profinite carrier, division and content

K is the compatible inverse limit of Z/nZ; reduction modulo n is onto.
Multiplication by a positive integer d is injective: if dz=0, reduction
modulo dN shows z=0 mod N for every N. Its image is exactly dK=ker(mod d).
For z in that kernel, divide its representative modulo dN by d to obtain
a unique residue modulo N; these residues are compatible and define z/d.
This also proves continuous inverse division dK->K. The subgroup dK is
clopen of index d, with its d equal-mass cosets, hence h(dK)=1/d.

For a prime p define v_p(z)=sup{k:z in p^k K}, allowing infinity.
Integer multiplication gives v_p(dz)=v_p(d)+v_p(z), seen modulo powers
of p, where the factor of d coprime to p is invertible. A pair is in P
exactly when min(v_p(u),v_p(v))=0 for EVERY prime p: a simultaneous divisor
m>=2 exists exactly when one of its prime divisors divides both entries.
If(x,y)=d(u,v) with(u,v) in P, its minimum valuations are precisely v_p(d).
Unique integer factorization therefore makes d unique whenever it exists.
This does not assert every point has finite content.

P is a closed subset of compact K^2: its defining exclusions are clopen
and their intersection is closed. Each dP is compact/closed and the dP are
pairwise disjoint. The finite-content domain D=union_(d>=1)dP is Borel,
delta is a Borel integer function there, and its complement is the retained
terminal set. Each branch divides continuously on its dP; their countable
union is Borel. In particular the origin belongs to no dP and remains terminal.

For an ordinary integer pair not both zero, its positive integer gcd g
normalizes it to an ordinary coprime pair. Divisibility in mK agrees with
ordinary integer divisibility by reduction modulo m, so that pair lies in P
and delta=g. This includes signed integers and a single zero coordinate.
It proves the sieve/gcd interface on the actual registers, not a finite
algorithm for the infinitely many residue tests on arbitrary K points.

## 3. All inverse branches and nonlinear every-Borel IMAGE

Fix a finite-content source(x,y) in dP and set(a,b)=T(x,y).
Then a=y, u=b-a^2-1=x/d, and necessarily(x,y)=(du,a).
The condition(x,y) in dP is exactly a in dK and(u,a/d) in P.
By uniqueness of content this implies delta(du,a)=d, and direct substitution
gives T(du,a)=(a,b). Conversely these conditions make the inverse legal.
Thus the redundant source checks in E_d reduce to exactly those first two
conditions, with no missing target, branch or incoming cutoff. The target
may itself be terminal; its own content does not remove this inverse.
E_d is closed, and I_d is a homeomorphism E_d->dP with inverse T there.
Every legal predecessor belongs to a unique dP and is on this list.

The map B(a,b)=(b-a^2-1,a) is a Haar-product-preserving homeomorphism:
for each a, translating the second coordinate preserves h, and swapping
coordinates preserves h times h. Fubini proves preservation on EVERY Borel
set, not just cylinders. Multiplication L_d(u,a)=(du,a) is a homeomorphism
onto dK times K. Its pushforward probability is normalized Haar on that
subgroup: it is invariant under subgroup translations, as follows by pulling
them back through L_d. Therefore mu(L_d E)=mu(E)/d for every Borel E.
Equivalently normalized restricted Haar is d times the restriction of mu.

Since I_d=L_d B restricted to its actual E_d,
mu(I_d E)=mu(E)/d for EVERY Borel E subset E_d. This proves the exact
frozen constant j_d=mu(dK times K)=1/d, including its declared values on
null points. No a.e. version is changed after the fixed-point tests.

## 4. Actual clock and complete real extension

Legal iterate domains and T are Borel. Actual triples(z,m-n,w) form the
countable union of their Borel equalities. Compose by extending the shorter
middle history to the longer already-legal one; equality supplies the same
continuation on the other side. Terminals admit only their legal zero
iterates, but all incoming and identities remain. Equal triples are one
arrow, never independent copies of branch histories.

Here kappa(z)=log delta(z) on legal steps. Two presentations of an actual
triple with the same lag differ by equal further iterate counts on their
common tail; identical sums cancel. Aligning middle histories also proves
additivity of c=S_m(z)-S_n(w). It is Borel and zero at identities.
On a finite branch word, inverse IMAGE is the product of its1/d factors.
On a branch-pair chart sharing a tail, the two restricted branch IMAGE laws
therefore give density exp(-c). This verifies the SAME measure cocycle on
every such chart. Countably many legal words cover all actual arrows.
No global one-to-one T or nice topological groupoid is asserted.

The full real extension uses(w,h)->(z,h+c), with identities/inverses and
composition justified by this cocycle. All height translations commute
with it. A return of the orbit class of(z,h) is EXACTLY a loop at z with
the required height difference, so its full time group is c(G_z^z), up to
irrelevant sign. For a fixed source of finite content d, this yields

```text
source isotropy=Z; c(k)=k log d;
d>1: H=(log d)Z, kernel=extension isotropy=0;
d=1: H={0}, kernel=extension isotropy=Z.
```

These equations determine least time, repetitions and all phases for each
fixed source. Different fixed sources cannot share any common future;
incoming chains compose to that same impossible equality. Consequently
each such source gives its own packet when d>1, not a representative chosen
by content. Infinite-content terminals have source isotropy0 and H={0}.
No general periodic census is claimed by these structural observations.

## 5. MAIN's entire declared fixed-source fibers

A fixed source must have x=y=t. If its content is d, then t=d u with
u a unit in K: a diagonal pair is primitive exactly when its entry is
nonzero modulo every prime, equivalently invertible in every Z/nZ.
The second fixed equation becomes

```text
d^2 u^2-(d-1)u+1=0, u in K^times.                       (1)
```

For d=1 it requires u^2+1=0. Reduction modulo3 is impossible because
the only squares are0 and1, neither equal to-1. For d=2 equation(1) gives
4u^2-u+1=0, hence(8u-1)^2=-15. Modulo7 the right side is6, whereas
squares are0,1,2,4 (squaring0 and the pairs±1,±2,±3 exhausts all residues).
It is again impossible. These exact congruences exclude the WHOLE two
fibers, including every noninteger profinite point, without numerical sampling.

The prescribed bounded test now ends. It has produced neither a positive
primitive nor an adverse MAIN primitive. Contents>=3 and cycles of source
length>=2 remain OPEN, as do the global prime-time and multiplicity targets.
Empty fixed fibers do not make the main source acyclic or the time trivial.

## 6. Full separately owned controls

A is the total homeomorphism T_A(x,y)=(y,x+y^2+1), with the frozen full
inverse B on all X. The preceding Fubini proof directly gives its OWN
every-Borel IMAGE1; it has no source terminals, even at MAIN-terminal points.
Its actual groupoid and real extension use c_A=0 on every arrow. Therefore
H={0} everywhere, whatever its source isotropy; that isotropy stays in the
kernel, not a positive physical period. Its fixed equation t^2+1=0 has no
solution modulo3. No source-cycle classification follows or is needed.

B is defined on D with inverses L_d(a,b)=(da,b) exactly when b in dK
and(a,b/d) in P. The same uniqueness/direct-substitution proof verifies
its own full source checks and all incoming. L_d itself has every-Borel
IMAGE1/d, so the actual B-groupoid/clock/extension follow by section4's
construction using B's OWN legal histories, not MAIN's paths.
At content1, B fixes every pair in P, with time H=0 and retained kernel Z.
At content d>1, its fixed equation x/d=x implies(d-1)x=0, hence x=0
by integer-multiplication injectivity. Its content condition is then
y=d v with v a unit. Conversely EVERY(0,dv) of this kind is fixed.
The full stabilizer calculation above gives least log d and no isotropy
kernel. Distinct fixed states cannot merge through any incoming history.

There are continuum many such v. The Chinese-remainder bijections on all
finite moduli give K=product_p Z_p; choose arbitrary odd2-adic component
and component1 at every other prime. Odd2-adic digit sequences have continuum
cardinality and are all units. Thus B has continuum inequivalent primitive
log d packets for EVERY d>=2, including composite d. This is an exact
fixed-source classification, not B's full longer-cycle census or MAIN's result.

C has the same D, own inverse(d(b-a^2),a) and target conditions a in dK,
(b-a^2,a/d) in P. Shear by-a^2, swap and multiply the first register prove
its own every-Borel IMAGE1/d. The same full actual-arrow construction gives
its own cocycle and real extension, retaining its infinite-content terminals.
A fixed source again has t=d u with u a unit, now satisfying d^2 u=d-1.
For d>=2 a prime dividing d gives0=-1 modulo that prime. For d=1 it forces
u=0, not a unit. Hence C has NO fixed source of any finite content; terminals
are not fake fixed points. Longer C cycles and their time groups remain OPEN.

## 7. Disposition and exact limits

Portfolio **advance** the full Haar/content owner, **leave T2 OPEN** after
the bounded test, and **fork the fifth-round audit** to a clock-rank screening
criterion rather than expanding this local census without a new contract.
The content mechanism is an actual register operation, not a passive label;
its choice and polynomial still do not establish strong naturalness.
No decision about MAIN follows merely from B's continuum or A's zero clock.

Proof methods: compatible residues, valuations/CRT, Haar/Fubini, exact
source-check identities, actual cocycles and fixed-source equations.
No scientific program, floating point, prime/zero input table or cycle search
ran. Small residue sets above are exact algebraic obstruction proofs, not
finite evidence extrapolated to a global period claim. Same-object ledgers
remain intact; T0/specified Haar clock established; T2 OPEN; T3 NOT AUDITED;
classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
ARS/internal independent derivation are shared-history NOT_CALIBRATED,
not a novelty certification, cross-model test or external peer review.

EOF — full Haar owner established; MAIN packet question intentionally remains open.
