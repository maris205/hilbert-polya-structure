# Infinite gcd splitting and coprime merging: owned returns, repeated prime-2 packets

Paper ID: `325-gcd-split-coprime-merge`.
Candidate ID: `ANG-20260920-GSM01`. Date: 2026-09-20.
Status: `OWNED REWRITE CLOCK; REPEATED PRIME-2 PACKETS — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

On the full space of infinite positive-integer words, the current gcd
chooses between extraction of a common factor and merging coprime factors.
The divisor observable is retained as a precise admissibility deformation,
not an asserted conjugacy. Both actual inverse-prefix families and their
complete Borel IMAGE belong to one frozen nonatomic product measure. All
fixed words are e_N=(N,1,1,...), N>=1. Each has entire
time group (log2)Z, but these are distinct packets, not repetitions
or different representatives of one orbit. Their complete incoming basins
are classified by eventual unit tails and gcds of prime valuations;
no word or phase is selected away. Thus the positive fixed-return
result is genuine, while the required prime-packet multiplicity fails. The
bounded decision is STOP / FORK. Three controls own different inverse
families and complete fixed basins. Higher nonfixed periods remain unclassified.

## 1. Frozen source and precise arithmetic lineage

The [original card](candidate-card.md), first 149 lines, was frozen before
claims/calculation, SHA-256
`3874276bd629060b23bec238a267848936a521a056bb4bf4c5ce489b6c864435`.
Its original author later checked only those lines for faithful transcription,
PASS without changes; this was not a mathematical review. Full access
and pending-next-definition records are in [provenance](evidence/scout-record.md).

Take X=N_{>=1}^{N0}, full discrete-alphabet product topology and Borel
structure. For z=(a,b,eta), put g=gcd(a,b) and use

    g>1: Tz=(g,a/g,b/g,eta),
    g=1: Tz=(ab,eta).                                  (1)

All infinite tails, units, orders and repeated/composite letters remain. There
are no finite/empty words, no empty tails and no terminal objects.
Units use (1), not an extra loop or reset. Zero/negative
letters were not in the declared source. No real scale fibre,
external port or independent prime selector is present.

The interface (n,d,eta), for n>=2,d>=1 and ALL eta,
keeps the actual original coordinates. The divisor symbol d|n is
exactly gcd(n,d)=d, with proper part 1<d<n. Main's test
g>1 is instead common-factor admissibility: it does NOT say d|n
for arbitrary pairs. On a proper divisor its actual action is
(n,d,eta)->(d,n/d,1,eta). Thus the arrow is divisor observation
-> gcd-readable arithmetic -> common-factor/coprime rewriting -> the new
prefix determines the next branch. This retains an observable under an
admissibility deformation, not a proved lossless divisor-arrow conjugacy.

Rule/order/measure are declared design. Canonical arithmetic A0, stronger naturalness,
Logistic/Henon relations and conservative/symplectic realization remain OPEN. No prime
table, fitted log-prime roof, zero input or theorem from another owner.

## 2. Exact full inverse, source topology and probability

For a target z=(c,d,e,eta), every merge predecessor is

    (a,b,d,e,eta), ab=c, gcd(a,b)=1,                   (2)

with ALL ordered pairs retained. There is additionally precisely the
split predecessor

    (cd,ce,eta) if c>=2 and gcd(d,e)=1.               (3)

These are forced by the two equations in (1); substitution proves
both inverse identities. Different merge pairs are different source words.
The split predecessor has first-pair gcd c>1, whereas merge predecessors
have gcd1, so they cannot duplicate each other. Every target has
at least the merge predecessor (c,1,d,e,eta). Thus T is
onto, with finite nonzero predecessor count: the number of ordered coprime
factor pairs of c, plus the indicator in (3).

Each source cylinder [a,b] maps homeomorphically onto [ab] or
[g,a/g,b/g]. These are actual cylinder maps; overlapping target
cylinders do not give a single unweighted whole-map IMAGE identity. T
is a local homeomorphism on this full noncompact word space. No
extra path edges, factor swaps or selected recurrent subset are added.

Let rho(n)=1/[n(n+1)], and W(u)=product rho(u_i)
for a finite prefix, W(empty)=1. Here is a self-contained
existence construction of the frozen probability. Partition (0,1] into

    I_n=(1/(n+1),1/n],
    f(x)=(x-1/(n+1))/rho(n) on I_n.

Each affine restriction maps onto (0,1], and the interval lengths
telescope to one. Successive interval labels define a Borel infinite-word
map. Its pushforward of Lebesgue probability has each prefix mass W(u).
After any finite prefix its affine residual variable has the same
law, so for EVERY Borel F subset X,

    mu(u F)=W(u)*mu(F).                               (4)

Equivalently this is the full prescribed product probability rho^{N0}.
Surjectivity of the interval coding onto all words is neither needed
nor used to restrict X. Every nonempty cylinder has positive mass,
so support is full. Every prefix mass is <=2^{-length}; hence
every single word has mass zero. There are no other atoms:
on an atom every countable prefix partition would have a unique full-
mass cell, whose shrinking bound forces its mass to zero.

## 3. All-Borel IMAGE, full-point clock and retained lag

An actual inverse replacing prefix v by u acts on E=vF
as I(E)=uF. Equation (4) proves for ALL Borel E in
its domain, not just a cylinder,

    mu(I E)=integral_E [W(u)/W(v)] dmu.               (5)

The frozen constant version J_I=W(u)/W(v) is finite and
positive at EVERY point of that cylinder, including all null returning
words. A.e. uniqueness alone would not prescribe these values. No
point masses, conull deletion or reweighting is used.

With source (a,b,eta), the two actual inverse densities are

    merge: J=rho(a)*rho(b)/rho(ab),
    split: J=rho(a)*rho(b)/[rho(g)*rho(a/g)*rho(b/g)],
    kappa=-log J.                                    (6)

These main step clocks are in fact strictly positive. Simplification gives
J_merge=(ab+1)/[(a+1)(b+1)]<1. For a=gu,b=gv,

    J_split=(g+1)(u+1)(v+1)/[g(gu+1)(gv+1)]
           <=4/[g(g+1)]<=2/3, g>=2.

The bound uses (u+1)/(gu+1)<=2/(g+1) for u>=1,
and the same inequality for v. Thus kappa>0 on ALL main
steps, not just its returning words. These simplified ratios and positivity
were supplied by original-card-only raw review after root's first 317-line
draft was locked, then checked and adopted. The original density formulas
were already present; positivity was not a first-draft theorem. This does
not construct a classical suspension or assert a uniform non-Zeno bound.

Every finite actual history can be refined into countably many finite-
prefix charts: only finitely many letters are inspected or rewritten in
finitely many steps. Composition cancels intermediate prefix masses. A branch
pair from w to z with T^m z=T^n w has IMAGE
exp[-S_m(z)+S_n(w)], where S_m sums its actual kappas.
The same tail-section proof gives its integral identity on every Borel
subset; the frozen full-point products agree on further chart refinement.

Retain exactly G={(z,m-n,w):T^m z=T^n w}, source w,
range z, equal triples one arrow, and c=S_m(z)-S_n(w).
Same-lag presentations differ by a common legal future, whose clock cancels.
Composition aligns middle histories at the larger length. This proves pointwise
descent and additivity. The actual forward arrow (Tz,-1,z) has
c=-kappa(z), not +kappa. Empty histories have sum zero.

All X x R_h remains, with arrows (w,h)->(z,h+c)
and full h-translation. Only Borel/set quotient is asserted: no invariant
mu times dh, smooth/Hausdorff coarse quotient, positive roof or runtime clock.

## 4. Complete fixed locus and decisive packet multiplicity

Suppose Tz=z. In the merge case equality of first letters gives
ab=a, hence b=1. Equality of all later letters then forces
the ENTIRE tail to be units. In the split case equality
forces g=a and b=a/g=1, contradicting gcd(a,b)=g>1.
Therefore the complete fixed locus, with no finite-tail approximation, is

    e_N=(N,1,1,...), N>=1.                            (7)

At every e_N the actual merge inverse density is rho(1)=1/2,
so kappa(e_N)=log2. Its entire source isotropy is Z, its
entire time image is (log2)Z and its extension isotropy kernel is
zero. Thus the least positive time is exactly log2, with repeats
r log2 on that SAME packet. No smaller generator is inferred
from a different word or an incoming branch.

Two different fixed points cannot share an actual future: their futures
are themselves. Hence e_N and e_M, N!=M, represent distinct packets,
even though every time group is identical. This is a countably
infinite multiplicity at the prime-2 primitive, not one packet with many
representatives or repetitions. Already e_1 and e_2 decisively violate the
target multiplicity. We do not repair it by keeping a single N.
No T2 discriminator or higher-period census is needed or performed.

## 5. Complete fixed basins, arithmetic invariants and phase

Let E_1 be ALL words eventually equal to 1. A word
outside E_1 cannot reach e_N, because finitely many prefix rewrites leave
an infinite suffix unchanged. For z in E_1 let P(z) be
the finite product of all nonunit entries and ell(z) the length
through its last nonunit entry, with ell=0 for e_1.

If z is not already fixed, a merge preserves P and decreases
ell by one. A split decreases P to P/g<P; its
length change is immaterial. The lexicographic pair (P,ell) therefore strictly
decreases in N_{>=1} x N0 until a fixed word is reached.
There cannot be infinitely many strict P decreases; between them ell
strictly decreases. This proves convergence for EVERY eventually-unit word, not
global convergence on the full infinite source.

The exact terminal label is not the product, gcd or lcm of
the original letters. Define for each prime p, solely as a
proof invariant on this finite nonunit prefix,

    e_p(z)=gcd{v_p(z_i): i>=0},
    N(z)=product_p p^{e_p(z)},                         (8)

where all-zero exponents give gcd0 and only finitely many p occur.
No prime list enters the dynamics or the clock. For a split
write alpha=v_p(a), beta=v_p(b), m=min(alpha,beta). Replacing
alpha,beta by m,alpha-m,beta-m preserves their gcd together with
all other exponents. In a coprime merge at most one of
alpha,beta is nonzero, so replacing them by alpha+beta also preserves
that gcd. Thus every e_p is invariant, and at e_N its
value is v_p(N). Consequently the COMPLETE fixed basin is

    B_N={z eventually 1 : N(z)=N}.                    (9)

This closed form equals the union of ALL iterated actual inverse
families (2),(3); neither unit strings nor overlapping inverse images are
discarded. B_1={e_1}, since any nonunit introduces a positive valuation
gcd at some prime. For N>=2 the basin is countably infinite:
it consists of finite prefixes with an infinite unit tail and contains
the distinct words (1^k,N,1,1,...), k>=0. Each B_N is
null by nonatomicity; the frozen all-point IMAGE remains specified there.

For z in B_N let d(z) be its first hitting depth and
S(z)=S_d(z)(z). All arrows between w,z in this basin have

    lag=d(z)-d(w)+k,
    c=S(z)-S(w)+k*log2, k in Z.                      (10)

Each state, even a nonfixed ancestor, has source isotropy Z, entire
H=(log2)Z and zero extension kernel. Its full phase is
h-S(z) modulo log2. This accounts for EVERY incoming branch and
height, not a selected core point. Distinct N never merge. The
circle-valued set coordinate does not assert a Hausdorff embedded flow circle.
Source periods and time groups outside these fixed basins remain UNCLASSIFIED.

## 6. Three controls and their own complete fixed ledgers

### 6.1 MERGE-ONLY

T_M(a,b,eta)=(ab,eta) has ALL ordered factor-pair inverses on
[c], ab=c, without coprimality. These are finite, distinct and
cover every target. Its OWN J=rho(a)rho(b)/rho(ab), all-
Borel IMAGE and full-point version follow from (4), on its OWN
branches. Agreement of a formula on shared branches does not identify histories.

All fixed words are again e_N; each has source Z, H=(log2)Z,
zero extension kernel and primitive log2. Its full fixed basin is
instead {eventually1 words with finite product N}. Repeated merging proves
sufficiency, preservation of product and the unchanged infinite suffix prove necessity.
For N=1 it is singleton; otherwise it is countably infinite and
null. Complete phase is h-S_M modulo log2. For example (2,2,1,...)
belongs to main B_2 but to MERGE-ONLY B_4, so basins do
not transfer despite the common fixed times. Other periods remain unclassified.

### 6.2 REFINE-ONLY

T_R(a,b,eta)=(g,a/g,b/g,eta), INCLUDING g=1. Its exact
image consists of target (c,d,e,eta) with gcd(d,e)=1, and
its unique predecessor there is (cd,ce,eta). Thus it is injective
but not onto; (1,2,2,eta) has no predecessor but is a
legal source, since T_R is total. Its own J is the
split expression in (6) also for g=1; no main permission transfers.

Fixedness forces a=g,b=1, then a=gcd(a,1)=1 and the
whole word is e_1. At this word the inverse density is
rho(1)^2/rho(1)^3=2, so kappa_R=-log2. The entire time
group is still (log2)Z, source Z and extension kernel zero;
the positive generator comes from the opposite signed lag. Injectivity and
the already-fixed predecessor force its COMPLETE basin to be {e_1}.
Its phase is h modulo log2. Other periods remain unclassified; signed
clock and source recurrence are not confused with a positive roof.

### 6.3 GCD-COALESCENCE

T_C(a,b,eta)=(gcd(a,b),eta). Every target (c,eta) has
countably infinitely many predecessors (a,b,eta), gcd(a,b)=c,
including (c,kc,eta) for all k>=1. The branch's own
all-Borel IMAGE is rho(a)rho(b)/rho(c). Main's inverse filters
and the finite-word/real-fibre 304 density are not applicable.

Fixedness forces the entire tail to be one constant b and
the first letter a to satisfy gcd(a,b)=a. Thus ALL fixed
words are f_ab=(a,b,b,...), a|b. Their source isotropy is
Z, entire H=log[b(b+1)] Z, extension kernel zero and primitive
log[b(b+1)]. Distinct fixed pairs remain different packets even for equal b.
In particular b=2 already gives a composite primitive log6 in this
CONTROL; that clock does not replace main's log2 multiplicity obstruction.

The complete basin of f_ab consists exactly of words eventually b
whose gcd of ALL letters is a. Iteration takes gcds of
longer initial prefixes and shifts the remainder; after the constant tail
is reached the prefix gcd stabilizes to a|b. This proves both
necessity and sufficiency. Every such basin is countably infinite, for example
by the distinct predecessors (a,ka,b,b,...), k>=1, and is null.
All its states have source Z, the same H and zero kernel;
phase is h-S_C modulo log[b(b+1)]. Other periods remain unclassified.

## 7. Gate, controls and limits

| Audit | GSM01 result | Limit |
| --- | --- | --- |
| T0 source / inverse / full-point IMAGE | ESTABLISHED for full infinite words | All ordered inverse branches retained |
| T1 arithmetic feedback / clock ownership | Explicit gcd deformation and own product-measure clock | Stronger naturalness/canonical A0 OPEN |
| T2 fixed primitive / multiplicity | Positive log2 returns, but infinitely many distinct fixed packets: FAIL | Higher nonfixed source periods UNCLASSIFIED |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No imported determinant |
| Classical A0/A1/A2 | NOT APPLICABLE | No symplectic map or suspension |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK. Genuine recurrence and a prime-valued primitive do
not suffice when the full intrinsic packet ledger has extra multiplicity.
The main, control, terminal-label invariants and clocks remain separately owned.
No selecting N=1, quotienting labels, deleting units, changing probability or
copying a control repairs the frozen source. That would require another card.

PROVES_TOO_MUCH is visible: every first letter N, including composites,
can head a fixed word with the SAME log2 packet. The
negative statement is specific to this frozen owner. No claim is
made about all arithmetic rewriting, all nonfixed periods, complete prime coverage,
canonical measure selection, classical geometry or an RH/Hilbert--Polya result.
All proofs are exact; no scientific program, finite cutoff/precision, prime
input or external literature was used. Internal ARS scrutiny is NOT_CALIBRATED,
not external peer review, machine proof or independent-error evidence.

See [card](candidate-card.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md),
[package](README.md). Positive 304, partial-positive 320 and old packages
unchanged; 241/242 paused; goal active. Markdown only; no PDF/LaTeX,
publication/upload or Git staging/commit.
