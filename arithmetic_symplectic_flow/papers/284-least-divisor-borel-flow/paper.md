# Least-divisor Borel dynamics: a declared full-point clock and duplicate log-two packets

**Candidate ID:** `ANG-20260920-LDB01`  
**Paper ID:** `284-least-divisor-borel-flow`  
**Date:** 2026-09-20.  
**Status:** `DECLARED ALL-POINT CLOCK; DUPLICATE LOG-TWO PACKETS — STOP / FORK`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The current complete arithmetic seed selects its first nontrivial
integer divisor and is divided by it; if none exists, it is translated
by one. Only these restricted branches and their actual inverses
generate the Borel groupoid. A separately declared maximal-domain
Haar scaling rule supplies a finite clock at every arrow, including
null branches. This rule is coherent but is not uniquely forced by
the a.e. derivative of the actual null branch. The first packet test
already stops the candidate: zero and the 1-to-2 cycle have two
inequivalent primitive packets, each of least time log 2. An arbitrary
embedded prime enters the second packet; its division arrow's log-p
magnitude is not a prime primitive period. All states remain. Following
the frozen early-stop rule, no global return census is pursued.

## 1. Frozen source, lineage and category

The [version-1 card](candidate-card.md) freezes K=Z_hat with full
residue Borel structure and normalized additive Haar h. For all
integers d>=2 set

    B_d=dK minus union_(2<=e<d) eK,
    U=K minus union_(d>=2) dK,
    T(x)=x/d on B_d;       T(x)=x+1 on U.

All seeds, including zero, negative integers, nonintegers and null
points, remain. The branches are re-evaluated at the current seed.
There is no fixed input n, modulus register, scan phase, prime table
or supplied return-time list.

The [prior-work interface](../../docs/prior_work/README.md) is integer
prime/composite divisibility -> all compatible residue observations
-> this state-dependent divisor reduction / remaining-branch update
-> its actual restricted arithmetic arrows. It realizes a source
deformation, not a Logistic/Hénon conjugacy or classical symplectic
lift. The proposal first appeared, without a proof, in the separate
[283 D lane](../283-nonlinear-residue-clock-screen/evidence/scout-record.md).

The arrow category is Borel. A complete real-coordinate translation
will be established as a Borel groupoid action, not silently promoted
to a locally compact étale or Hausdorff coarse flow. Naturalness of
the update and the additional full-point clock choice remains OPEN.

## 2. All branches and their Borel owner

### Lemma 1 — partition, actual divisors and remaining seeds

The nonempty B_d are exactly those with d prime. They and U partition
K. Each B_d is clopen; U is the closed unit group K^times and is
Haar-null. The maps x->x/d on B_d and x->x+1 on U are Borel
isomorphisms onto their actual images.

**Proof.** Multiplication by d is injective: dx=0 modulo dm implies
x=0 modulo m for every m. Its image is dK, the mod-d kernel;
compatible residues modulo dm give the unique quotient. The resulting
map K->dK is a homeomorphism. Thus every finite Boolean combination
defining B_d is clopen, and division on it has a Borel inverse with
its exact restricted image.

If d is composite, any proper factor e>=2 has dK subset eK, so
B_d is empty. If p is prime, the embedded integer p belongs to B_p.
Every seed in the union of the dK has a least such d, giving the
partition. A seed outside that union is invertible modulo every m;
its finite inverses are compatible. Conversely a unit is in no dK.
Hence U=K^times is closed. Translation is a homeomorphism on K,
so its restriction to U has the stated Borel inverse.

For any finite set of primes P, avoiding zero modulo each p has
Haar mass product_(p in P)(1−1/p), by CRT. For primes at most N,
the reciprocal product is at least sum_(n=1..N)1/n: expanding the
finite geometric products includes every such n through its prime
factorization. The harmonic sums diverge, so h(U)=0. QED.

In particular B_2=2K, zero follows the same division rule as every
other point there, and 1,−1 belong to U. No exceptional state rule
has been introduced. U is nonempty but not open, since h has full
support. Its branch must not be called an open local-homeomorphism
chart just because the ambient translation is continuous.

### Proposition 2 — entire restricted affine-labelled groupoid

Let G consist of all actual finite words in these branches and strict
restricted inverses. Identify words precisely by affine label (q,r)
and source x, with target qx+r. Then G is a countable standard Borel
groupoid, retaining all states and all its isotropy labels.

**Proof.** Integer multiplication is injective, so K embeds in the
algebraic localization S^{-1}K; rational affine formulas are valid
there. Every generator is an injective Borel map between Borel
subsets of K. Finite compositions and inverses have Borel domains
and images. There are countably many finite words. For each rational
affine label, its actual domain is the countable union of its word
domains, hence Borel. The arrow space is a Borel subset of the
countable disjoint union of copies of K indexed by (q,r).
Source fibres are countable. The affine composition and inverse
laws are Borel on actual composable arrows and preserve this set.
Identity words give every unit. QED.

This is not the full affine groupoid of 275 and not a word-lag
groupoid. Calculating an ambient affine formula never enlarges an
actual word domain. No a.e. reduction is taken.

## 3. Exact scaling, with its all-point choice disclosed

### Proposition 3 — maximal-domain scale and restricted clock

For any actual label q=a/c>0, r=b/c, with a,c positive integers
and b integer, its maximal domain D={x:ax+b in cK} is nonempty
and clopen. On every Borel E subset D,

    h(qE+r)=q^(-1) h(E).

The card's extension-and-restriction prescription therefore gives
the full Borel cocycle c(q,r,x)=log q on G.

**Proof.** Write d=gcd(a,c), a'=a/d, c'=c/d. Nonemptiness forces
d to divide b, by reduction modulo d. Put b'=b/d and solve
a'x_0+b'=0 modulo c' in ordinary integers; gcd(a',c')=1.
Then D=x_0+c'K, with image y_0+a'K, where
y_0=(a'x_0+b')/c'. For any Borel B subset K,

    q(x_0+c'B)+r=y_0+a'B.

Haar cylinder counting and finite-measure uniqueness give
h(t+nB)=h(B)/n for every positive integer n. Applying this to
the last identity gives the ratio c'/a'=1/q for arbitrary Borel
E. A nonempty D has positive measure, so the constant is unique.
The formula depends only on the label, not its denominator
presentation. Under affine composition q multiplies, so c adds.
Restriction proves the Borel IMAGE identity on every actual domain,
without adding its missing ambient arrows. QED.

The division branch has c=−log d; the U translation has c=0 under
THIS declared version. On U, however, both h(E) and h(E+1) vanish
for every Borel E subset U. That restricted measure identity alone
does not determine the pointwise derivative there. The maximal-domain
rule is real additional structure, not a consequence of a.e. uniqueness
on the actual null branch. No continuous full-arrow uniqueness theorem
is asserted for this Borel owner.

Every actual branch preserves the Haar null-set class, as does its
inverse. Countably many words therefore give the usual nonsingular
measured Borel owner. This fact does not remove the extra all-point
clock specification at null states.

The real extension has arrows

    (x,u) -> (qx+r,u+log q).

Real translation in u is defined for every real parameter, jointly
Borel, and respects composition; it is a complete action. On K×R
the translation itself is continuous. No topological groupoid-flow
or positive-roof suspension assertion follows from these facts.

## 4. Entire-word control before counting packets

For the actual forward itinerary of x let A_m(x) denote the affine
label of its first m T steps, with A_0 the identity. Domains always
remain restricted to that itinerary.

### Lemma 4 — generated arrows have a common-forward-tail form

An actual arrow x->y has label

    A_k(y)^(-1) A_m(x),  with T^m(x)=T^k(y), m,k>=0.

Conversely every such pair of actual prefixes gives an arrow.

**Proof.** A generator or inverse has this form. For two composable
forms x->y and y->z, align the two prefix lengths at y by extending
both to their maximum. The added forward tail is the same actual
branch word, because T has exactly one selected branch at each point.
Its affine labels cancel. This proves closure under composition;
inversion exchanges the prefixes. Induction covers every finite word.
The converse simply follows the first prefix and reverses the second
on its strict actual image. QED.

Thus a displayed loop is not being mistaken for the full stabilizer.
The lemma controls possible extra words and excursions through any
other seed. Equal endpoints do not justify adding an absent affine
label or importing the full affine stabilizers of 275.

## 5. Decisive early packets and arithmetic controls

### Theorem 5 — two different least-log-two packets

At both x=0 and x=1, the COMPLETE time-return group is (log 2)Z.
These states belong to two different primitive cyclic-return packets,
each of least positive time log 2 and repeated times k log 2.
At these states fixed-object extension isotropy is trivial, whereas
source isotropy is infinite cyclic.

**Proof.** At zero every forward step is x->x/2, so T^m(0)=0 and
A_m(0) has label (2^(-m),0). Lemma 4 gives exactly the stabilizer
labels (2^j,0), j in Z. All occur, and their clocks are j log 2.

At one the actual itinerary is 1->2->1->2. Each two-step prefix
has affine map x->(x+1)/2. Thus A_m(1) has slope
2^(-floor(m/2)). A common tail of two prefixes at 1 requires equal
parity of m and k. Their quotient has slope 2^j, and fixing 1
forces translation 1−2^j. Conversely every such label occurs by
iterating the two-step cycle or its inverse. The complete stabilizer
is therefore {(2^j,1−2^j):j in Z}, again with clock j log 2.

The forward tail of zero never meets the forward tail {1,2} of one.
By Lemma 4 no actual groupoid arrow connects them. Adding real-time
translation does not change that base-orbit obstruction. They are
two packets, not two phases or repetitions of one packet. In each
stabilizer c is injective, leaving trivial fixed-object extension
isotropy. The stated primitive and repetition laws follow. QED.

**Minus-one control.** Since −1 belongs to U and T(−1)=0, it is
in the zero packet, not a third packet. This uses the actual branch,
not a deleted negative-seed sector.

**Arbitrary prime input.** For every ordinary prime p, p belongs to
B_p and T(p)=1. The arrow has clock −log p, but it is not a closed
arrow at p. Every such prime state lies in the packet of 1, whose
time group is (log 2)Z by conjugation of isotropy. A correctly owned
log-p ARROW therefore does not produce a least-log-p PRIME PACKET.

Both packets include null points in the retained full source.
Nothing is deleted to force uniqueness. This early test proves
AT LEAST two incompatible log-two primitives. It does not claim
that these exhaust every noninteger state or every packet in G.
The exact global packet ledger is NOT PURSUED after the decisive stop.

## 6. Gate disposition, limitations and evidence

| Gate | Evidence for this exact owner | Scoped disposition |
|---|---|---|
| T0 | Full restricted countable Borel groupoid, measure class and complete Borel real extension | ESTABLISHED in the stated Borel category; topological enhancements not claimed |
| T1 | Actual current least-divisor law; same-label Haar scaling with an explicit extra full-point rule | ARITHMETIC MECHANISM PRESENT; clock naturalness / intrinsic uniqueness OPEN |
| T2 | Complete stabilizers at the precommitted controls; two inequivalent least-log-2 packets | PRIME-SINGLE-PACKET TARGET FAIL; other returns unclassified |
| T3 | No analytic object | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No classical symplectic map or positive roof | NOT APPLICABLE |
| Formal Route / B | No evaluation | UNASSIGNED / NOT INVOKED |

Portfolio: **STOP target promotion / FORK**. The single decisive
reason is the duplicate primitive log-two packet, independently
reinforced by the prime-input/closed-packet mismatch. Do not repair
the source, remove null points, change translation or attach a roof.
Possible naturalness and PROVES_TOO_MUCH issues remain open rather
than replacing this exact obstruction with a rhetorical no-go.

No global noninteger return classification, coarse-topology audit,
cycle census, numeric cutoff, precision, prime list, target-zero
comparison or external novelty claim is made. The self-contained
methods are compatible congruences, Haar scaling, Borel word domains
and the exact common-forward-tail argument. No earlier clock or
stabilizer theorem is inherited. The separate [scout record](evidence/scout-record.md)
preserves the nonadmitted reciprocal-divisibility proposal without
proving or disproving its new dynamics.

See the [claim ledger](claim-ledger.md), [evidence bindings](evidence/README.md)
and [three-checkpoint review](evidence/independent-review.md). ARS
and AI assistance were used; internal same-model review is not
external peer review or formal verification. Same-object ownership
is intact, 278 unchanged, 241/242 paused, programme goal active.
