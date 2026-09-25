# Square-distance coprime histories: a source-level return obstruction

Paper379; screen `ANG-SCREEN-20260922-SDC01`; 2026-09-22.
Batch `HARD-NONLOCAL-20260922-F`, round5/5.
Status: `NONEMPTY SOURCE; NO EVENTUAL PERIOD; PRE-P0 STOP / FORK`.
No measured clock owner. Classical A0/A1/A2 NOT APPLICABLE;
T1 and T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

On the entire alphabet of integers at least two, require coprimality at
every square separation. The full source is nonempty, but every proposed
eventual period l conflicts with the constrained separation l squared.
Its actual lag-retaining groupoid therefore has trivial isotropy everywhere.
Conditionally, no real cocycle on this same groupoid can produce a positive
return of height translation on its full extension orbit set. No measure or
clock is fabricated to express that implication. Three source-only controls
have exact primitive-word and least-period classifications. This stops the
MAIN screen before measured P0; it is not a theorem excluding invariant
probabilities, arbitrary arithmetic sources, or other kinds of physical flow.

## 1. Frozen question and lineage

The [original82-line card](candidate-card.md) freezes A={2,3,...}, the distance
set D={n^2:n>=1}, and ALL histories satisfying its distance constraints.
Its SHA256 is `111aeaa1b7599fa9ac05367b1b020865084a104d99a31114ec13ea40fc87afdb`.
Root read the full [CP1 scope](evidence/scope-review.md) before mathematical release.
The prior-work arrow is common-divisor exclusion -> separation-dependent
symbolic admissibility -> test whether genuine source returns survive.
No prime-label alphabet, prime table, inserted roof, imported analytic object,
or symplectic realization is present. A real cocycle below is a universally
quantified conditional object, not a constructed field of this candidate.

For any of the four explicitly frozen distance sets D', write

    X_D'={x in A^N0: gcd(x_i,x_(i+d))=1 for all i>=0,d in D'}.

All bounded and unbounded histories, all finite prefixes, and every actual
incoming branch are retained. The general arguments below are proved for
this definition, then applied to each control's OWN D' and X_D'.

## 2. Entire carrier, nonemptiness, and all actual inverses

Each forbidden coordinate pair is detected on a cylinder. Thus X_D' is
closed in the discrete-product Polish space, with its Borel structure.
Left shift T preserves every retained distance condition, so is a continuous
self-map. Neither surjectivity nor local-homeomorphism structure is assumed.

Let f_i=2^(2^i)+1. Induction by difference of squares gives
product_(i<j)f_i=f_j-2. A common divisor of f_i and f_j for i<j therefore
divides 2. Both are odd, so they are coprime. Thus x_i=f_i belongs to each
X_D', proving nonemptiness without presuming any f_i prime.

The exhaustive one-step inverse domains are exactly

    E_a={y in X_D': gcd(a,y_(d-1))=1 for every d in D'}, I_a(y)=ay.       (1)

They are closed Borel sets; an infinite intersection is not declared open.
All old-tail constraints are already true, and (1) tests precisely the pairs
involving the inserted coordinate. Every preimage has a unique first letter,
so this list is complete. I_a is a homeomorphism onto [a] intersect X_D',
with inverse the restricted shift. Empty domains are not filled artificially.

For a finite word u of length m, the exact domain E_u consists of y in X_D'
such that gcd(u_i,u_j)=1 whenever 0<=i<j<m and j-i in D', AND

    gcd(u_i,y_j)=1 whenever i<m,j>=0 and m+j-i in D'.                    (2)

Empty prefixes have the whole source as domain. Formula (2) includes every
cross-boundary interaction, and is sufficient because it exhausts all new
pairs. These are all iterated inverse branches, not a finite-memory proxy.

## 3. Actual groupoid, full incoming relation, and source isotropy

Keep exactly G_D'={(z,m-n,y):T^m z=T^n y}, with nonnegative m,n,
source y and range z. Equal triples alone are identified; integer lag stays.
The countable union of the equality-of-shifts sets is Borel. Its arrows
compose by adding lags after padding the middle exponents to agree; inverse
negates lag. Prefix presentation (u xi,|u|-|v|,v xi), on E_u intersect E_v,
enumerates every arrow and gives countable source fibers.

The complete source orbit of x and the entire lag kernel are

    O_x={u T^n x:n>=0, u any finite word with T^n x in E_u},
    ker lag={(z,0,y):T^m z=T^m y for some m>=0}.                         (3)

Every incoming arrow to z is obtained by m,n>=0 and a legal length-n word v
with y=vT^m z, giving (z,m-n,y). Repeated presentations of the same triple
do not add multiplicity. Conversely any witness gives exactly that form.
This is the entire ledger, including nonperiodic and arbitrarily long histories.

The lag kernel is not merely the units. Let xi=(f_2,f_3,...) from Section2.
Both f_0 xi and f_1 xi are legal in each source, distinct, and have the same
one-step tail. They give a nonidentity zero-lag arrow. This merging of
different histories must not be confused with isotropy at one history.

For ANY x in one of these sources, its entire source isotropy is

    I_x={0} if x is not eventually periodic;
    I_x=l Z if its eventual tail has least word period l.              (4)

Indeed a nonzero-lag equality of shifts is exactly an eventual period.
After the preperiod, every multiple of l is realized. Any other equality
would give a smaller period of the periodic tail, so there are no other lags.
One can also see the latter assertion by writing a period d=q l+r and using
periodicity to deduce period r; minimality forces r=0.

## 4. MAIN: universal eventual-period failure

Suppose x in X_D is periodic after position N with period l>=1. For every
i>=N it has x_(i+l^2)=x_i, since l^2 is a multiple of l. But l^2 belongs
to the frozen square distance set, so gcd(x_i,x_(i+l^2))=1. The left side
equals x_i>=2, a contradiction. This handles EVERY l, preperiod and tail;
no finite scan or restriction to literal periodic points is involved.

It follows from (4) that the full MAIN groupoid is isotropy-free everywhere.
For given source and range there is at most one lag: two different lags would
compose to nonzero isotropy. Actual incoming arrows and merging (3) still
exist; they are not periodic packets. No return survives under this source rule.

## 5. Exact conditional implication for a height extension

Only in this paragraph suppose a real additive cocycle c on the ACTUAL
G_D' has been supplied. Keep all X_D' times R with arrows
(y,h)->(z,h+c(z,k,y)). Translation by t commutes with arrows, so acts on
their orbit SET. For a represented object (x,h), its full stabilizer is

    H_x={t: [(x,h+t)]=[(x,h)]}=c(I_x).                                 (5)

To prove both directions, equality of those orbit-set points means an actual
composite arrow with source and range x and clock t. A composite is already
an arrow of G_D'. Conversely each such isotropy arrow realizes that equality.
The fixed-object isotropy of the extension is ker(c restricted to I_x).
Over each source orbit, transporting height to a reference point identifies
the phase set with R/c(I_x); this is a set statement, not a manifold assertion.

For MAIN, (4) and Section4 force c(I_x)={0} for EVERY such c, and extension
isotropy trivial. The conditional physical action has no positive return.
This does not specify an actual c, clock kernel, measure, IMAGE law, physical
H, or flow for the present screen. Those actual fields remain NOT DEFINED.
A different relation, owner or roof cannot be added as a rescue under this ID.

## 6. Three complete source-only controls

For any period length l and one of the declared distance sets, let
R_l(D') be its complete set of residues modulo l. A displayed cyclic word
w=(w_0,...,w_(l-1)) is admissible exactly when

    gcd(w_i,w_(i+r mod l))=1 for every i and every r in R_l(D').         (6)

Necessity tests the corresponding coordinates of its infinite repetition.
Sufficiency reduces every actual distance pair modulo l. For primitive
words additionally require that w is not a proper power; cyclic rotations
are identified, but reversal and equal arithmetic costs are not quotiented.
All eventual-periodic source classes consist of the legal prefixes in (3)
of these rotated primitive cores. Distinct primitive necklaces cannot merge,
because equality of periodic tails forces cyclic equality of primitive words.
Their entire source isotropy is lZ, with source repetitions kl, not clock time.

**Least-period existence lemma.** There is a legal word of least period l
if and only if 0 is absent from R_l(D'). If present, (6) requires an integer
at least two to be coprime to itself, impossible. If absent, choose l distinct
Fermat-form integers f_0,...,f_(l-1); all residue comparisons are between
distinct entries and pass. Distinctness ensures least period l (also for l=1).
This proves constructive sufficiency, not just a necessary exclusion.

| Separate source owner | Complete distance rule | Possible least periods |
| --- | --- | --- |
| ODD-SQUARE | D'={(2n+1)^2:n>=0} | Exactly positive even l |
| FINITE-SQUARE | D'={1,4} | Exactly l=3 or l>=5 |
| INTERACTION-OFF | D'=empty | Every positive integer l |

For ODD-SQUARE, odd l has its own square in D', a multiple of l; no odd
integer is divisible by an even l. For FINITE-SQUARE, a zero residue occurs
exactly when l divides 1 or 4, namely l=1,2,4. OFF has no residues to test.
These arguments and the constructive lemma prove every entry in the table.
For each control the actual words are still exactly (6), not every word of
an allowed length. MAIN itself has no allowed l by the same lemma.

Equations (1)–(4) specify each control's own full source, inverse domains,
incoming arrows, lag kernel and entire isotropy; they are recomputed with
that control's D'. No MAIN probability or clock is transferred. A conditional
c would satisfy (5), but its value on lZ is unspecified here: source cycles
alone supply neither a positive time nor a prime packet. Actual clock kernels,
extension, H-values, physical packets and target verdicts are NOT DEFINED
for these unmeasured controls as well. Their mathematical source differences
are positive comparison results, not cumulative credit for MAIN.

## 7. Decision, limitations, and reproducibility

**STOP MAIN before measured P0; FORK only after batch confirmation.**
Nonemptiness and complete source ownership are established; all eventual
returns fail. The obstruction concerns the square-distance rule and the
conditional actual-groupoid extension only. It does not prove absence of
invariant probabilities: that different question remains OPEN and outside
this screen. No strong arithmetic naturalness, operator, trace, formal Route
coordinate or quantum conclusion is claimed. The same-object ledger remains
intact precisely because no missing measured or physical fields were borrowed.

Inputs are the frozen card and exact definitions above. Methods are symbolic
proofs: pairwise-coprime construction, full inverse enumeration, equality of
shifts, and the residue criterion; there are no scientific numerical commands,
cutoffs or sampled-period extrapolations. No external source was required for
these original derivations; no literature priority or novelty claim is made.
The bounded old-card phrase search recorded in the card is not a novelty audit.

Root wrote this main proof before reading the separate raw derivation. Its
suspected distance/period resonance was disclosed before scope release.
Shared history and model-assisted work are NOT_CALIBRATED, not blind or
external peer review. ARS supplies separate scope/raw/manuscript review stages,
not mathematical authority. See [claim ledger](claim-ledger.md) and the
subsequent [review](evidence/review.md) for the final evidence binding.
All data are definitions and proofs in this Markdown package. No human or
animal subjects or private dataset. Human authorship, funding and conflicts
were not supplied; none is inferred. No PDF, publication or Git action.
This is round5/5: summarize and await the user's decision, without a sixth.
