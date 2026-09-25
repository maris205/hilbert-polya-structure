# Sum–product root germs: complete positive-axis packets and dense return groups

Paper ID: `341-sum-product-root-correspondence`.
Candidate ID: `ANG-20260920-SPR01`. Date: 2026-09-20.
Status: `DENSE RETURNS AND SUBPRIME AXIS PRIMITIVES — STOP / FORK`.
Evidence: exact local/germ and entire positive-axis-orbit proofs; no numerical census.
Formal Route UNASSIGNED; B NOT INVOKED.

## Abstract

The whole real plane carries two actual sum–product correspondences, both regular
inverse sheets, and their full analytic germ groupoid. Its own Lebesgue IMAGE
derivative supplies a full-point cocycle and complete height translation. We classify
EVERY positive-axis source orbit, its complete return-time group, actual germ isotropy
and kernel, including all incoming arrows. For an axis seed a>0 the
group is Z log a + Z log 2. Irrational log_2(a) produces a
countable dense group, not a primitive period. For log_2(a)=p/q reduced,
the least positive time is log2/q; orbit identity identifies p/q only modulo
integers. In particular q=2 already gives a nontarget primitive, not a
repetition of the q=1 packet. The three controls are rebuilt independently.
This is a scoped full-axis obstruction, not classification of the rest of the
plane or a no-prime-orbit theorem. The same-object ledger remains intact.

## 1. Candidate identity and ownership

| Item | Exact owner | Scope |
| --- | --- | --- |
| Carrier | ALL R², ordinary Lebesgue measure | Critical points and all signs retained |
| Arithmetic interface | Integral a,b>=2, n=ab, checksum s=a+k*b | Factor-witness observable, not prime-only state space |
| Actual evolution | k=1,2 sum–product branches and BOTH regular root sheets | Full legal compositions, not a deterministic chosen branch |
| Arrow identity | Equality of actual analytic germs | Not endpoints, formal words or an added lag |
| Clock | -log of the SAME source-to-range IMAGE derivative | Analytic full-point version |
| Time/packets | Entire height extension; translation; full source orbit and H | No selected generator period |
| Controls | Product-off, sheet-off, second-channel-off | Separate maps, germs and clocks |
| Classical symplectic base/roof/suspension | None | NOT APPLICABLE |
| Trace/operator/zeta | None | NOT SUPPLIED / NOT PURSUED |

The [original card](candidate-card.md) freezes this object before reported results.
The [source record](evidence/scout-record.md) separates definition delivery, shared history,
root's preliminary thoughts and a parallel NONE. No earlier candidate theorem transfers.

## 2. Question and precise claim boundary

Does this full measured germ owner possess a primitive arithmetic-time ledger,
with EVERY returning class assigned its entire stabilizer rather than one chosen loop?

The strongest result is an exact classification on the entire positive-axis sector,
which is proved saturated under ALL actual arrows. Its dense return groups and
extra primitive times suffice for the frozen stop. In particular log2/2 is
not log n for any integer n>=2, since its exponential is sqrt2.
No Riemann-zero comparison or externally assigned prime roof enters this argument.

The complete global return groups away from this sector are UNCLASSIFIED. We
do not claim all main isotropy groups are free, all kernels trivial, no
prime-time packets anywhere, or a universal obstruction for algebraic correspondences.
The arithmetic interface is exact but strong A0 naturalness remains OPEN.

## 3. Entire maps, critical rules and symbolic lineage

For k=1,2 and sigma=+/-1 use

    D_(k,sigma)={sigma*(a-k*b)>0},  P_k(a,b)=(a+k*b,a*b),
    E_k={Delta_k=s²-4*k*n>0},
    Q_(k,sigma)(s,n)=((s+sigma*sqrt(Delta_k))/2,
                       (s-sigma*sqrt(Delta_k))/(2*k)).

Every object of R² remains. Each absent equality branch stays absent, while
other available charts remain legal. A finite word exists only on the open
set where every intermediate chart is legal. No endpoint completion or waiting loop.

Direct substitution gives P_k Q_(k,sigma)=identity, a-k*b=sigma*sqrt(Delta_k)
on Q's range, and Q_(k,sigma) P_k=identity on D_(k,sigma).
Thus these are analytic diffeomorphisms D_(k,sigma)<->E_k, including the ENTIRE
domains displayed, not merely a favourable component or integer sample.

For each proper integral factor pair a,b>=2, at most one of a=b
and a=2*b holds. It therefore supplies a regular witness in at least
one channel, with its OWN checksum. At a critical equality it is absent
in that channel, not represented by a limiting inverse; the other channel has
a different checksum. Conversely an integral Q output >=2 has product n and
is exactly such a witness. This does not filter all real states into primes.

The [prior-work guide](../../docs/prior_work/README.md) supplies the conceptual arrow:
proper-divisor symbolic observable -> factor witnesses with checksum -> actual coupled real
algebraic correspondence. No Logistic/Henon conjugacy or conservative dimensional lift is proved.
Integers, elementary arithmetic, the two fixed channels and Lebesgue measure are allowed;
prime tables, zero data, per-prime choices and fitted schedules are not.

## 4. Full germ and measured-time ownership

### 4.1 Actual arrows, topology and Borel structure

Let G consist of [w]_x for all legal words, identifying exactly locally equal
maps. Restriction, inverse and composition of the actual diffeomorphisms define an etale
germ groupoid with charts x->[w]_x. Empty words give all identity objects.

There are countably many finite words. Each source orbit and isotropy group is
therefore countable: a word contributes at most one image and germ at x.
Open restrictions do not create new germs. For two words, germ agreement is
an open subset of their common domain. It is also relatively closed there:
on a small connected ball where both maps are analytic, agreement on a
nonempty open subset forces equality on the ball. The analytic uniqueness assertion
follows by Taylor expansion and continuation through overlapping balls.

One can choose the least indexed word representing an arrow. Its representative
domain is Borel after removing the agreement sets with earlier words. These
countably many Borel pieces give a standard Borel arrow space and Borel operations.
The same analytic uniqueness separates distinct germs over one source by disjoint
charts; distinct sources are separated in R². Thus the arrow space is
Hausdorff and second countable. This does NOT make the coarse orbit quotient Hausdorff.

At the origin no P or Q is legal; it has only identity germ
and no incoming nonidentity arrow. At any nonzero point at least one P
is legal since a=b and a=2*b intersect only at zero. Its polynomial
map is not locally identity. Hence the main object's only terminal is the origin.

### 4.2 Every-Borel IMAGE and height translation

Direct differentiation of the OWN maps yields

    det D P_k(a,b)=a-k*b,
    J_P=|a-k*b|, c_P=-log|a-k*b|,
    J_Q=1/sqrt(Delta_k), c_Q=(1/2)*log Delta_k.

Each denominator is strictly positive on its actual chart. The ordinary diffeomorphism
change-of-variables formula proves mu(wE)=integral_E |det Dw| dmu for EVERY
Borel E, first on each generator and then on every legal finite composition.
These are analytic versions on all domain points, including retained null axis states;
the formula does not create an arrow where its chart is absent.

Equal germs have equal derivatives. The chain rule proves c(gf)=c(g)+c(f)
pointwise on G and c(g^-1)=-c(g). The WHOLE kernel consists of actual
germs with absolute determinant1, not just identity germs or an a.e. quotient.

Keep all X x R_u, arrows (x,u)->(g x,u+c(g)), and translation by
every real t. Translation is jointly continuous, complete and commutes with the arrows.
It descends to the coarse orbit set/topological quotient without a separation claim.
For ANY source x, its time stabilizer is EXACTLY H_x=c(G_x^x): two
heights over that same source represent the same extension orbit precisely when their
difference belongs to H_x. Fixed-object extension isotropy is ker(c|G_x^x).

## 5. Entire positive-axis ledger

### 5.1 Full saturation and the actual orbit graph

Write h_a=(a,0), v_a=(0,a), a>0. ALL available generators there are

    P_(k,+): h_a -> h_a,
    P_(k,-): v_a -> h_(k*a),
    Q_(k,+): h_a -> h_a,
    Q_(k,-): h_a -> v_(a/k).

No Q is defined at v_a: Delta_k=-4*k*a<0. The displayed opposite-sign
P choices are absent. These formulas enumerate ALL arrows of length one, both
directions; therefore they also prove the entire positive-axis union is saturated.
There are no off-axis incoming ancestors to add after the calculation.

The complete source orbit of h_a is

    O_a={h_(2^m*a), v_(2^m*a):m in Z}.

Every listed point is reachable, using v_b->h_b and v_b->h_(2*b) and
their inverses. Conversely the generator list produces only these points. O_a=O_b
if and only if b/a is an integer power of2; equal clocks alone
do not identify orbits. All positive-axis transients and incoming histories are already here.

### 5.2 Complete germ isotropy, character and kernel

Let S be the ACTUAL germ P_(2,-) Q_(1,-) at h_a. It sends
h_a to h_(2*a); it and its inverse give a transport B_m from
h_a to h_(2^m*a), for every integer m. Choose B_0=identity.
Let A_(k,m) be the germ of P_(k,+) at h_(2^m*a). Define

    R_(k,m)=B_m^-1 A_(k,m) B_m in G_(h_a)^(h_a).

The ENTIRE isotropy Gamma_a is the group of actual analytic germs generated by
all these R_(k,m), k=1,2, m in Z, with their actual germ relations.
Indeed the nonloop edges v_(2^m*a)--h_(2^m*a) and
v_(2^m*a)--h_(2^(m+1)*a) form a tree. Any finite loop in the
complete orbit graph reduces to conjugated horizontal loops by cancelling tree excursions.
This proves generation, not a free-group presentation; derivative equality is never an
extra relation. Isotropy at every other orbit point is conjugate by actual transport.

All generator IMAGE factors on O_a are powers of2 times a or their
reciprocals. Conversely conjugation cancels its transport clocks, giving

    c(R_(k,m))=-log a-m*log2.

Hence the ENTIRE image, not merely a subgroup found in a sample, is

    H_a=Z*log a + Z*log2.

Surjectivity follows from m=0 and the difference between m=1 and m=0.
For a word in the R generators, let N be its signed total exponent
and M its signed m-weighted exponent. Its clock is -N*log a-M*log2.
Thus the entire isotropy kernel consists EXACTLY of the actual germs represented
by words with that expression zero. Relations preserve the expression; N and M
need not individually be invariants when log_2(a) is rational. No kernel germs
are erased from the extension. This describes the complete group/character without claiming
an unknown presentation of all analytic germ relations.

The kernel is nontrivial for EVERY a>0. At h_b the derivatives of
the two horizontal loops are [[1,1],[0,b]] and [[1,2],[0,b]]. Their
products have upper-right entries2+b and1+2*b, so for b!=1 their
commutator is a nonidentity germ of determinant1. Choose b=2^m*a!=1
and conjugate back. The extension therefore retains nontrivial fixed-object isotropy.

### 5.3 Primitives, dense groups, phases and multiplicity

Put r=log_2(a). If r=p/q in lowest terms, q>=1, then Bezout's
identity gives H_a=(log2/q)*Z. Its least positive time is L=log2/q.
In the preceding kernel formula the exact condition is p*N+q*M=0.
The entire source packet is indexed by r modulo Z, not by q alone.
There is one such axis packet for q=1, and for each q>1 there
are precisely as many as residues1<=p<q coprime to q. All their
height phases modulo L belong to the SAME packet, not extra primitive copies.
Its repetitions have times j*L for integers j>=1 on that same source orbit.

If r is irrational, H_a is countable dense and has no least positive
element. For completeness, pigeonhole the fractional parts0,r,...,N*r into N
equal intervals: two yield a nonzero element of Z+rZ of absolute size
<=1/N. Arbitrarily small positive subgroup elements approximate every real number by
integer multiples, proving density. The exact kernel condition is then N=M=0.
Here phases are R/H_a, not a circle or a quotient by one selected
return; the orbit is still retained. Countable H_a is not all R.

More generally choose any actual transport g:h_a->x in O_a. The phase
of (x,u) is u-c(g) modulo H_a; replacing g changes it by H_a.
This gives the ENTIRE extension-orbit ledger over O_a, including every incoming
history and the nontrivial kernel. Translation is transitive on this phase set.

For irrational r an extension orbit meets the height fibre over h_a in
a dense proper coset of H_a, hence is not closed. The global coarse
quotient is not T1 and therefore not Hausdorff. This does not contradict the
Hausdorff arrow-space result. There are continuum distinct dense-return axis packets, since
their parameter is the irrational r classes modulo Z.

Already r=1/2 gives a complete cyclic packet O_(sqrt2) with least time
log2/2. Its twice traversal has time log2 but does NOT identify it
with O_1, whose least time is log2. This exact extra primitive and
the dense-return packets trigger the frozen STOP / FORK. Nothing about the
unclassified off-axis sector can remove these saturated actual orbits.

## 6. Own controls and adverse checks

### 6.1 PRODUCT-OFF: full linear owner

L_k has matrix [[1,k],[1,-1]], determinant -(k+1), and inverse

    (s,n)->((s+k*n)/(k+1),(s-n)/(k+1)).

These are global diffeomorphisms of the WHOLE plane. Their own clocks are
-log(k+1), inverse clocks +log(k+1), from their actual Lebesgue IMAGE.
Germs of these linear words are equal exactly when the matrices are equal.
At zero the complete source orbit is the singleton and the ENTIRE isotropy
is the actual matrix group Gamma=<L_1,L_2>. Its complete clock image is
Z log2+Z log3, dense because an integer relation would give2^m*3^n=1
and hence m=n=0 by elementary divisibility. Its entire kernel is exactly
{A in Gamma:|det A|=1}; it is nontrivial, since L_1 L_2
has first row(2,1) and L_2 L_1 has first row(3,-1), so their
commutator is a nonidentity determinant1 matrix. Keep that extension isotropy and
R/H phases. Other control source orbits are unclassified; zero already decides the gate.

### 6.2 SHEET-OFF: complete positive horizontal cores

Rebuild only the + charts, with J and c differentiated from those same maps.
At EVERY h_a, a>0, all four retained generators fix h_a; the other
sheet is absent. Thus its ENTIRE source orbit is the singleton, including all
incoming arrows. Each positive v_a is instead an identity-only terminal with no
incoming arrow, by the exact domain tests; do not import the main tree.

The complete isotropy at h_a is the actual analytic germ group generated by
P_(1,+),P_(2,+), not a free group by decree. All generator clocks
are -log a, so its ENTIRE H is Z log a. For a!=1
the kernel is exactly germs represented by words of total signed exponent zero;
the noncommuting-derivative commutator above proves it nontrivial. For a=1 ALL isotropy
has zero clock and belongs to the kernel; it is not trivial, as the
first generator has derivative [[1,1],[0,1]]. All phases and terminal heights remain.

For a!=1 each singleton source packet has least time |log a|; there
are continuum distinct packets. In particular a and1/a are distinct packets of
equal time, not two phases of one. For a=1 there is no positive
return although extension isotropy is nontrivial. No rest-of-plane census is claimed.

### 6.3 SECOND-CHANNEL-OFF: complete two-point cores

Rebuild only k=1 and both sheets. For EVERY a>0 its complete axis
source orbit is exactly {h_a,v_a}. The horizontal loop A=P_(1,+)
and the single tree edge B=P_(1,-):v_a->h_a exhaust actual generators
there and their inverses; no other incoming point exists. Every isotropy loop
reduces to a power of A. It has infinite order: for a!=1 its
derivative determinant is a, and for a=1 its derivative is the nontrivial
unipotent matrix above, whose nonzero powers remain nonidentity.

Thus ENTIRE source isotropy is Z at both points, H=Z log a,
and the entire extension isotropy is0 when a!=1 and Z when a=1.
For a!=1 there is one primitive packet per a, least time |log a|,
with both source points and all phases u-c(g) modulo that group. At a=1
time phases are R with zero time stabilizer, retaining source/extension isotropy Z.
Other sources, critical-line terminals and negative-axis behaviour are not classified in this manuscript.

| Control | Exact studied complete core | Decisive distinction |
| --- | --- | --- |
| Product-off | Singleton zero; full actual matrix isotropy | Dense log2/log3 group without factor witnesses |
| Sheet-off | Every positive h singleton, positive v terminal | Continuum primitive times; kernels retained |
| Second-channel-off | Every positive {h_a,v_a} pair | Cyclic source isotropy, continuum primitive packets |

These are OWN results, not transplanted main formulas. The main arithmetic observable
does not remove its bad axis packets. PROVES_TOO_MUCH is limited to these
defined comparisons: no arbitrary-data encodability or general correspondence no-go is asserted.

## 7. Gate assessment

| Gate | Evidence | Standing |
| --- | --- | --- |
| T0 | Actual analytic germs, full-point every-Borel IMAGE, full height extension | OWNED at stated germ/groupoid level |
| T1 | Exact integral factor interface and own derivative clock | Strong arithmetic naturalness OPEN |
| T2 | Entire saturated positive-axis ledger, dense groups and log2/q primitives | FAIL target full primitive ledger |
| T3 | No same-object trace/operator/zeta supplied | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No symplectic map and roof supplied | NOT APPLICABLE |
| Formal Route A / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

## 8. Conclusion and decision

Portfolio STOP / FORK for this frozen object's full-axis return structure. No
retiming, sheet deletion, channel adjustment or conull excision repairs the same object.
The controls show why those changes would require fresh identities and still have
their own adverse core ledgers. Off-axis main/controls remain unclassified after the gate.

The parallel conservative-geometric source search returned Pre-P0 NONE for an unfilled
autonomous transport/time interface, not a mathematical no-go. There is no complete
next tuple pending. Earlier objects, positive304/partial-positive320 and paused241/242 remain
unchanged; the breadth-search goal remains active, not complete or blocked.

## Reproducibility and evidence

Exact inputs are the card and its supplied algebraic charts. Methods are inverse
substitution, differentiation, every-Borel change of variables, analytic germ uniqueness, an
exhaustive axis adjacency proof, tree-loop reduction and elementary additive-subgroup arithmetic.
No scientific numerical command, word/period cutoff, precision parameter, prime table or
external literature source was used. Proof scope is exact, not an extrapolated sample.
See [claim ledger](claim-ledger.md), [evidence](evidence/README.md) and
[internal review](evidence/independent-review.md) for input locks, accesses and dispositions.
AI-assisted ARS review is inherited-model/shared-history NOT_CALIBRATED, not external peer
review or independent-error evidence. A clean package is not a Route certificate.
