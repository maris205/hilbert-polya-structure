# Quotient-driven batch aggregation: owned composite primitive packets

Paper ID: `323-quotient-batch-aggregation`.
Candidate ID: `ANG-20260920-QBA01`. Date: 2026-09-20.
Status: `OWNED BATCH CLOCK; COMPOSITE PRIMITIVES — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

On the whole space of infinite nonnegative integer words, Euclidean division
of the first two letters determines how many following letters are consumed.
Their sum plus the remainder feeds the next division. A frozen full-support
nonatomic product measure and actual cylinder replacements give an all-Borel IMAGE
and a fixed full-point clock version. The predeclared complete words 1^infinity
and 2^infinity are distinct source-fixed packets with primitive times log6
and log12. The predeclared (4,2,2,...) has a genuine least-two
core and primitive log144, not a repetition of the log12 packet.
All incoming histories, isotropy and phases are retained. Three controls own
different inverse/clock ledgers; no deletion gives a global zero-time coboundary,
while no batch feedback makes every history terminate. Composite primitive times
decide STOP / FORK without classifying all returns or changing the measure.

## 1. One frozen word owner and its symbolic lineage

The [original card](candidate-card.md), first 152 lines, was frozen before
the results, SHA-256
`8c43530ded5637d2d975d951c3a167201a04bdcd174c10c61fb881b8f5333cde`.
Root read all 210 lines of the
[322 frontier](../322-factor-quadratic-coefficient/evidence/scout-record.md),
SHA-256 `586c2ea8a46bd8ad7386b6b75d65632187621332dd9a4b44d672fb0ea53c6c59`.
Access and shared-history limits are in [provenance](evidence/scout-record.md).

Take X=N_0^N_0 with discrete-letter product topology and Borel structure.
Every infinite word remains, including units, zeros, composites and arbitrary
unbounded/nonperiodic tails. This is a symbolic/groupoid carrier, not a
finite-dimensional symplectic map, conservative realization or classical mapping torus.
The whole second-letter-zero fibre is terminal, retaining T^0 and incoming
histories. With b>0, write a=qb+r, 0<=r<b, and read
the next q actual letters cword=(c_1,...,c_q). Set S=sum c_i:

    T(a,b,cword,eta)=(b,r+S,eta).                   (1)

For q=0, S=0 and no tail letters are consumed. No
reset, padding, absorbing loop or infinite letter. Arithmetic r=0 reads
b|a, with proper interface 1<b<a; failed divisibility remains live.
The exact lineage is divisor observation -> current quotient/remainder ->
quotient-controlled reading length -> aggregate of actual source letters plus
remainder -> next division. There is no independent integer root or scale,
factor oracle, prime filter, zero data or prescribed prime time. Batch
sum/consumption and reference measure are declared design; stronger naturalness,
canonical A0 and Logistic/Henon/conservative realization stay OPEN.

## 2. Actual probability measure, full support and null single words

Freeze pi(n)=1/((n+1)(n+2)), n>=0. Telescoping gives
sum_(n=0)^M pi(n)=1-1/(M+2), so total mass is one.
For completeness the product measure can be constructed directly, without merely
asserting formal cylinder masses. Partition [0,1) into intervals

    I_n=[1-1/(n+1),1-1/(n+2)), length pi(n).

Given u in I_n, emit n and replace u by its affine
coordinate in I_n, again in [0,1). Iterate indefinitely; every step
has a unique finite letter. This defines a Borel map from [0,1)
to X. Push forward Lebesgue probability to obtain mu. A prescribed
m-letter prefix alpha corresponds to an interval of length product pi(alpha_i),
with residual affine coordinate ranging over all [0,1). Consequently

    mu(C(alpha))=product_i pi(alpha_i),
    mu({alpha eta:eta in E})=mu(C(alpha))*mu(E)      (2)

for every Borel tail set E: the residual coordinate produces the same
digit map. Finite-prefix cylinders generate the Borel structure, so this is
the stated product law. No assertion that every infinite word has an
individual real-code representative is needed for this measure construction.
Every cylinder has positive measure; the countable cylinder base gives full
support. For any single word its m-prefix mass is at most 2^(-m),
so every singleton has zero mass. Null words remain source objects.
This particular probability law is design, not an arithmetic uniqueness theorem.

## 3. Complete inverse, IMAGE and full-point lag clock

Source prefixes alpha=(a,b,cword), b>0, length(cword)=floor(a/b),
partition the legal source into disjoint cylinders. Each maps homeomorphically
onto the full cylinder beta=(b,d), d=r+sum c_i, preserving eta.
For ANY target (b,d,eta), all actual predecessors are exactly

    b>=1, q>=0, length(cword)=q,
    S=sum c_i, r=d-S in {0,...,b-1},
    (qb+r,b,cword,eta).                            (3)

Both directions follow by the actual division identity. Every target with
first letter >=1 has countably infinitely many predecessors: for each q>=1
choose cword=(d,0,...,0), r=0, giving distinct first letters qb.
There are only countably many finite prefixes. Targets with first letter
zero have none. Hence the exact image is first-letter-positive, not all X.
For instance (0,1,0,...) has no predecessor but legally maps to
terminal (1,0,0,...), which has infinitely many predecessors. Terminality
is read from the second letter, not from inverse existence.

Let W(alpha)=mu(C(alpha)). By (2), every Borel subset E of
C(beta) has a Borel tail section E_tail and

    mu(theta_alpha E)=W(alpha)*mu(E_tail)
                    =[W(alpha)/W(beta)]*mu(E).

Thus the OWN all-Borel inverse IMAGE and full-point version are

    J_alpha=pi(a)*product_i pi(c_i)/pi(d)>0,
    kappa=log pi(d)-log pi(a)-sum_i log pi(c_i).    (4)

Each finite batch makes this finite and positive as a density; kappa
is not asserted positive. The same cylinder-constant version applies to every
null infinite word. A.e. density alone would not fix arbitrary singleton
values; this is the explicit version frozen before returns. No atomic
ratio, special returning-word rule or later time normalization is used.
The single-branch IMAGE is not an unweighted global formula across overlapping images.

Any finite actual history reads finitely many letters. Refine its source
cylinder enough to fix every intermediate batch, obtaining an actual prefix
replacement. Common further tail-prefix refinement multiplies numerator/denominator
by the same tail mass. Formula (2) proves the full Borel finite-
branch IMAGE, and its pointwise density is the product of step densities.
For S_k(z)=sum_(0<=i<k)kappa(T^i z), inverse history IMAGE is
exp(-S_k(z)); an actual branch pair from w to z has IMAGE
exp(-S_k(z)+S_l(w)). Retain exactly

    G={(z,k-l,w):T^k z=T^l w,both histories legal},
    c(z,k-l,w)=S_k(z)-S_l(w).                       (5)

Source w, range z, same triples one arrow, inherited Borel structure.
The countable legal-prefix partition makes the partial iterates and G Borel.
Same-lag presentations differ by a common legal future, which cancels;
composition aligns middle histories at the longer legal length. Thus the
full-point cocycle descends even on null words. The actual forward arrow
(Tz,-1,z) has clock -kappa(z), its inverse +kappa(z).
Keep all X x R_h, arrows (w,h)->(z,h+c) and full
h-translation. No separate roof, invariant mu times dh, smooth/Hausdorff
quotient or selected conull carrier is claimed.

## 4. Entire packet machinery, not isolated return arrows

For each discovered least-P core gamma=(q_0,...,q_(P-1)), retain

    B_gamma=union_(d>=0) {z:T^d z is in gamma},

with EVERY inverse branch (3) at every finite depth. This is the
entire actual tail class, not a constant-word subsystem. Determinism makes
basins of different cycles disjoint. At any point in B_gamma, source
isotropy is PZ. Write K=sum_(j<P)kappa(q_j); then the
ENTIRE time group is KZ. Extension isotropy is zero for K!=0,
and PZ for K=0. In the former case the least positive time
is |K|, and its integer multiples are repetitions of this SAME packet.

If T^d z=q_j, put A_j=S_j(q_0). The full phase at
q_0 is h-S_d(z)+A_j, modulo |K| for K!=0 and
as a real number for K=0. Other legal hitting choices change
this by an integer multiple of K. Every state/branch/phase remains;
equal numerical times do not identify distinct basins. No regular embedded
circle is inferred from the setwise phase description.

For every terminating history define its exact depth d, anchor omega and
S=S_d. Its complete basin is all actual finite ancestors of omega;
arrows have lag d(z)-d(w) and c=S(z)-S(w), full phase
h-S, with source/time/extension isotropy zero. No fictitious terminal loop.
These constructions neither truncate incoming trees nor classify every possible core.

## 5. Predeclared four-word tests and decisive composite primitives

Let e_0=0^infinity, e_1=1^infinity, e_2=2^infinity and
u=(4,2,2,...). Every equality below is of complete infinite words.

| Word | Exact main history | Least source period / time |
| --- | --- | --- |
| e_0 | Terminal, no incoming branch because first letter zero | Isolated source object; all isotropies0 |
| e_1 | q1,r0,cword=(1), fixed | P1, K=log6 |
| e_2 | q1,r0,cword=(2), fixed | P1, K=log12 |
| u | q2,r0,cword=(2,2) gives v=(2,4,2,...); v has q0,r2 and returns to u | P2, K=log144 |

For e_1/e_2, (4) gives J=pi(1)=1/6 and pi(2)=1/12.
For u, J=pi(2)^2=1/144, so kappa=log144. At v,
the empty batch gives J1 and kappa0. u!=v establishes least
period TWO; neither is e_2. Thus their complete basins have

    B_(e_1): source Z, H=(log6)Z, kernel0;
    B_(e_2): source Z, H=(log12)Z, kernel0;
    B_(u,v): source 2Z, H=(log144)Z, kernel0.       (6)

Each full basin contains all countably many recursively prescribed predecessors,
not just its core. Fixed-core phase is h-S modulo its K.
For the two-core case A_0=0,A_1=log144, so both hitting
phases reduce to h-S modulo log144. e_0 has phase h
and no incoming state. The complete time groups prove minimality, not
merely an available return. log144=2log12 does NOT make the u/v
packet a repetition of e_2: their actual basins are disjoint. Similarly
two turns at e_1 do not create a new primitive log36 packet.

Already e_1 gives a composite primitive log6 rather than log prime,
so the prime-selective target fails for this frozen owner. e_2 and
u/v reinforce the same defect, not separate repair options. This is
a decisive counterexample, not a complete classification of fixed words, higher
cycles or prime coverage. Those untested source/packet questions remain OPEN.

## 6. Controls, each with its own complete ownership

### 6.1 BATCH-FEEDBACK-OFF

Use F(a,b,cword,eta)=(b,r,eta), still consuming q letters.
Its exact inverse at (b,d,eta) requires b>=1 and 0<=d<b;
retain ALL q>=0 and ALL length-q cword, with a=qb+d.
Hence this precise image has countably infinitely many predecessors per target,
and targets outside it have none. Actual batches do not disappear from
the inverse ledger just because their sum no longer enters the output.
Its OWN cylinder IMAGE is pi(a)*product pi(c_i)/pi(r), giving
kappa_F=log pi(r)-log pi(a)-sum log pi(c_i).

At every actual step the second header decreases from b>0 to r<b,
independent of the consumed tail. Therefore EVERY history terminates after at
most its initial second letter b steps. All source/time/extension isotropy
is trivial globally, but nonloop clocks need not vanish. Entire terminal
basins/phase h-S use F's own inverse trees and prefixes. Equivalently
the finite Borel potential -S realizes its full cocycle as a coboundary.

e_0 is isolated terminal. e_1 maps to (1,0,1,...) with
kappa log18. e_2 maps to (2,0,2,...) with kappa log72.
u maps to that same latter terminal with kappa log2160. None
returns; these positive step values are not primitive periods. u and
e_2 now lie in the SAME terminating basin, unlike the main owner.

### 6.2 ONE-LETTER-BATCH

Use O(a,b,c,eta)=(b,r+c,eta), reading one letter even when
q=0. The complete inverse at (b,d,eta) keeps b>=1 and
all integers c in [max(0,d-b+1),d], q>=0, with
r=d-c and predecessor (qb+r,b,c,eta). Its image is exactly
first-letter-positive, each such point having countably infinitely many predecessors.
Own J=pi(a)*pi(c)/pi(d), kappa_O=log pi(d)-log pi(a)-log pi(c).
Its actual cylinder restrictions and history refinements prove its own full
IMAGE and cocycle, not a transferred batch-consumption rule.

e_0 is isolated terminal. e_1/e_2 are fixed with J1/6,J1/12.
Their full basins have sourceZ and kernel0, with respective time groups
H=(log6)Z and H=(log12)Z.
Every incoming predecessor above is retained, with phase h-S modulo K.
But u maps directly to e_2, with J=pi(4)=1/30 and
kappa log30. It is NOT periodic at one or two steps: it
is an actual tail in B_(e_2), phase h-log30 modulo log12.
No new log30 primitive is created by this incoming step. Higher source
returns and other packets are UNCLASSIFIED, not erased by the two fixed examples.

### 6.3 NO-DELETION

Write the complete tail after the first two letters as eta. This
control is N(a,b,eta)=(b,r+S_q(eta),eta), retaining that SAME
tail. At target (b,d,eta) its ENTIRE inverse is

    b>=1, q>=0, S_q=sum of first q ACTUAL letters of eta,
    r=d-S_q in {0,...,b-1},
    predecessor=(qb+r,b,eta).                       (7)

Distinct valid q give distinct a, since floor(a/b)=q. The
exact count is the number of q whose S_q lies in [d-b+1,d];
it can be zero, finite or infinite, unlike main's all-positive-first image.
For example (1,1,2,2,...) has none: its tail prefix sums
skip 1. It is nevertheless a legal source. Terminal (1,0,1,...)
has exactly the q0 predecessor; terminal (1,0,0,...) has all
q>=0 predecessors. Targets with first letter zero have none. No
batch is invented to fill a missing target prefix.

The actual source/target cylinder ratio cancels BOTH the retained batch and
b, yielding J_N=pi(a)/pi(d) and kappa_N=log pi(d)-log pi(a).
This is not the main deletion density. On all X the finite
Borel potential P(z)=log pi(z_0)+log pi(z_1) satisfies

    kappa_N=P(Nz)-P(z) on every legal step,
    c_N(z,ell,w)=P(w)-P(z).                         (8)

Thus ALL H0, and complete extension equivalence is actual source-tail
equivalence plus equal h+P. Source recurrence is not erased. e_0
is isolated terminal. e_1/e_2 are fixed, source/extension Z, H0.
Each has only itself as immediate predecessor under (7), hence its
complete basin is a singleton. The same u/v form a least-two
core, source/extension 2Z, H0; both step clocks are zero here.

For this tested two-core basin there is a sharper exact description,
adopted from raw review. The tail must be 2^infinity, and its
head (a,b) must satisfy a,b>=2 and gcd(a-2,b-2)=2.
Necessity follows backward from (7): a=d+(b-2)q preserves that
nonnegative shifted-header domain and gcd. For sufficiency put U=a-2,V=b-2.
The actual forward header update becomes

    (U,V)->(V,U-qV), q=floor((U+2)/(V+2)).         (9)

If U<V, q0 swaps them. If U>=V>0, then
1<=q<=U/V, so both remain nonnegative, gcd is unchanged and
U+V strictly decreases. After finitely many such steps a coordinate is
zero; gcd2 forces (2,0) or (0,2), exactly the tested core.
This describes ALL its incoming states, not a new search for other cores.
The basin is countably infinite and null. Its real phase is
h+log[pi(a)pi(b)], not a positive-time circle. Different cores do
not merge despite H0; other source periods remain UNCLASSIFIED even though
the global time theorem is complete.

## 7. Gate decision and research boundaries

| Audit | Result for ANG-20260920-QBA01 | Limit |
| --- | --- | --- |
| T0 carrier / all branches / measure IMAGE | ESTABLISHED | Full words and incoming multiplicity retained |
| T1 arithmetic feedback / owned full-point clock | ESTABLISHED within declared design | Stronger naturalness/canonical A0 OPEN |
| T2 prime-selective primitive target | FAILS at log6 fixed packet | Other source cycles/prime coverage not classified |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No imported analytic object |
| Classical A0/A1/A2 | NOT APPLICABLE | No symplectic lift or classical suspension |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK. The same-object ledger is intact: quotient-driven
consumption, batch feedback, full word carrier, frozen measure, actual all-point
cylinder clock and complete packets have one owner. Its failure is the
wrong primitive time, not inability to exhibit recurrence. A new measure,
normalization, selected word subsystem or no-deletion clock would change that owner.

Controls distinguish source recurrence from positive time and incoming step values
from primitives. Main's u/v cycle, ONE's tail into e_2 and
FEEDBACK-OFF's shared terminal basin are genuinely different source ledgers.
NO-DELETION's same displayed cycles have zero time under its OWN clock.
None supplies a repair or accumulated Route credit. No full-period census,
finite-tail simulation, numerical experiment, prime table or external literature is used.

Internal ARS three-checkpoint scrutiny is NOT_CALIBRATED, not external peer
review, machine proof or independent-error evidence. No RH/Hilbert--Polya,
invariant-measure quotient, canonical arithmetic mechanism or physical-flow claim follows.
See [card](candidate-card.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md),
[package](README.md). Positive 304, partial-positive 320 and older packages
unchanged; 241/242 paused; goal active. Markdown only; no PDF/LaTeX,
publication/upload or Git staging/commit.
