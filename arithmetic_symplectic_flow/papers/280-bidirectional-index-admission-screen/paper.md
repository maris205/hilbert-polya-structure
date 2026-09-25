# Bidirectional residue transfer: the joint image clock cancels before routing selection

**Screen ID:** `ASFS-SCOUT-20260920-BIC01`  
**Paper ID:** `280-bidirectional-index-admission-screen`  
**Date:** 2026-09-20; exact methodological result and bounded source control.  
**Status:** `JOINT IMAGE CLOCK CANCELS FOR ALL ROUTINGS; NO MAIN ADMISSION — STOP / FORK`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

A two-source residue transfer reads a digit from one full profinite
integer and writes it into another. We audit its complete product
measure, rather than the compression of one coordinate. For every
discrete routing of the current modulus, each full branch preserves
product Haar measure. Its retained-lag groupoid therefore has zero
joint image clock. Arbitrary positive finite root reweightings change
this to an endpoint difference, still with no positive time returns
anywhere. This closes the clock-admission question without choosing
a more elaborate routing or enumerating base cycles. It does not
exclude different physical or conditional clocks. A separately checked
Farey–horocycle construction illustrates that distinction but remains
an external lineage control, not a new main candidate.

## 1. Frozen question and same-owner scope

The [version-1 screen](candidate-card.md) fixes the full class before
proof. Its question is whether a better arithmetic routing can give
positive returning time under this particular JOINT IMAGE prescription.
For each fixed routing rho and each fixed allowed measure there is
one entire source, update, groupoid and real extension. The universal
statement below holds separately on each; no orbit ledgers are pooled.

The [lineage](../../docs/prior_work/README.md) is prime/composite gcd
and congruence observables -> actual residue reading -> transfer into
a second full arithmetic source -> joint update. This is a broadened
source test, not a claimed finite-dimensional symplectic realization.
The arbitrary routing class is not itself an arithmetic A0 mechanism.

[279](../279-successor-gcd-carry-flow/candidate-card.md) keeps only one
seed and uses different rules. Its extra prime-two packet is not
repaired here. [272](../272-power-divisibility-index-clock/candidate-card.md)
proved a positive-atom clock obstruction on a different source; K²
has no positive atoms, so that theorem cannot be assumed applicable.
[269](../269-factor-redistribution-lattice/candidate-card.md) supplies
neither this transfer nor its measure clock.

## 2. Complete class and exact branch ownership

Let K=Z_hat with its full residue topology and normalized additive
Haar h. Fix any table rho(n,j)>=2 for n>=2, 0<=j<n. The state is
Y=coproduct_(n>=2){n}×K². Write j=x mod n, and define

    T_rho(n,x,y)=(rho(n,j),(x−j)/n,j+ny).

All seeds, roots and congruence coordinates remain. Root n carries
measure h×h, or in the separately frozen reweighting control,
w_n(h×h), with 0<w_n<infinity. No seed-dependent or singular
reweighting is covered. A noncomputable table is a mathematical
control, not an asserted algorithm for generating primes.

### Lemma 1 — residue division and product scaling

Multiplication by n>0 on K is injective with image the mod-n kernel.
For Borel B subset K, h(j+nB)=h(B)/n.

**Proof.** If nx=0, reduction modulo nm forces x=0 modulo m for
every m. If x=0 modulo n, divide its residue modulo nm by n,
modulo m; these compatible residues give the unique quotient.
The map K->nK is therefore a homeomorphism. Additive invariance
gives every mod-m coset mass 1/m. Applying this to residue cylinders
proves the scaling formula there; equality of finite Borel measures
extends it to Borel sets. Cylinders also prove full support and
zero singleton masses. K is not assumed to be an integral domain.
QED.

For the branch (n,j), put r=rho(n,j). Its exact domain and image are

    D_(n,j)={n}×(j+nK)×K,
    I_(n,j)={r}×K×(j+nK).

The inverse on precisely this image is

    (r,u,v) -> (n,j+nu,(v−j)/n).

### Proposition 2 — all routings give full local owners

T_rho is a local homeomorphism, and its image is exactly the union
of the displayed I_(n,j). Y is locally compact Hausdorff and second
countable, with full-support non-atomic Radon sigma-finite mu_w.
Every branch has Borel IMAGE derivative

    J_(n,j)=w_r/w_n;

in particular J=1 for the principal unit-root measure.

**Proof.** Lemma 1 proves the displayed clopen branch homeomorphisms
and inverse domains. A compact set in Y meets finitely many compact
roots, giving the topology and local measure assertions. For a Borel
rectangle A×B in (j+nK)×K, the image is

    ((A−j)/n) × (j+nB),

with product mass (n h(A))(h(B)/n)=h(A)h(B). The rectangle identity
extends to all Borel sets in the branch by uniqueness of finite
measures. Multiplying source and image by their root weights gives
the stated derivative. QED.

The first coordinate's factor n and the second coordinate's factor
1/n are BOTH part of this one image map. Their cancellation is not
an almost-everywhere deletion or a choice of a returning sector.

Local branch preservation must not be promoted to global invariance
under a many-to-one T_rho. For example, for
rho_E(n,j)=max(2,gcd(n,j)), the target set

    A={2}×K×(1+6K)

has unit-root measure 1/6. The branches (2,1) and (3,1) give disjoint
preimages, each of measure 1/6. Thus mu(T_rho_E^(-1)A)>=1/3>mu(A).
This does not contradict the bisection IMAGE calculation, which is
always made on one injective branch at a time.

## 3. Entire groupoid and clock theorem

For each fixed rho retain G_rho={(z,m−k,z'):T^m z=T^k z'}, source
z', target z, with integer lag. Local inverse branches alpha,beta
are paired on arbitrary clopen subsets of their common terminal
domains in the same root. Domain restrictions from each finite word
remain; this is not a larger affine groupoid or a symbolic quotient.

### Theorem 3 — uniform joint-clock cancellation

For every fixed rho, G_rho is a second-countable locally compact
Hausdorff étale groupoid. With the principal unit-root measure its
full continuous IMAGE cocycle is c=0. For every allowed root weighting,
an arrow from z' at root n' to z at root n has

    J(g)=w_n/w_(n'),
    c(g)=log w_(n')−log w_n.

These are exact full-arrow statements, including null seeds and
nontrivial retained-lag isotropy.

**Proof.** Composition of branch-preserving product-measure maps
preserves unweighted product mass on each actual finite branch
domain. Each inverse branch also preserves that mass. Thus a
branch-pair map between roots n' and n preserves unweighted product
mass on all Borel subsets and has weighted ratio w_n/w_(n').

The endpoint formula is independent of deletion-length presentation,
multiplicative under arrows and locally constant, since roots are
discrete. It gives a continuous image-density version. Full support
on every nonempty bisection source makes that continuous version
unique, so null points cannot be retimed separately.

Finite inverse branches and arbitrary terminal residue rectangles
give a countable compact-open bisection basis. On intersections,
extend shorter presentations along the same actual T tail and
restrict to its clopen branch domain. This gives common refinements
and the inverse/composition laws. The source/range maps are locally
homeomorphisms; endpoints and discrete lag separate arrows. This
proves the asserted full arithmetic groupoid topology. QED.

### Corollary 4 — no positive time-return packet for any routing

The real extension has complete jointly continuous time translation,
but H_z=c(G_z^z)={0} at EVERY state. In particular it has no cyclic
positive-time packet, regardless of the base's discrete periods.

**Proof.** Give the extension its product topology, with arrows
(g,u):(z',u)->(z,u+c(g)). Local bisections give local source/range
homeomorphisms, and all-real translation respects its operations.
The globally defined coordinate

    v=u+log w_(root z)

is unchanged under every extension arrow. Translation by t changes
v to v+t, so no nonzero t can return even on extension isomorphism
classes. Equivalently, the endpoint formula vanishes on every
source isotropy arrow. The coordinate change is a homeomorphism
on each root and globally, not merely a measurable a.e. gauge.
Source isotropy itself survives as fixed-object extension isotropy;
it is not a positive time-return group. QED.

No classification of all base cycles or of the coarse quotient's
separation properties is required for this all-state conclusion.

## 4. Controls and exact scope of the stop

**Current arithmetic feedback.** In rho_E,
T(6,2,0)=(2,0,2), so an actual residue changes the source root and
both seed data. Every (n,0,0) is a full fixed state, including prime
and composite n; its retained-lag isotropy is Z. The extension still
has that isotropy, but time stabilizer {0}. Thus base recurrence does
not circumvent the joint-clock failure.

This control is not onto: at any root r>=3 every incoming branch has
r dividing n and j, hence its second output is in rK. Conversely the
branch (r,0) fills K×rK. Root 2 is entirely reached by its own two
branches. All missing states remain in the owner. No deeper cycle
census is performed.

**Full reversible control.** For rho_I(n,j)=n, each root's whole map
is a homeomorphism of K². Given (n,u,v), its unique inverse uses
j=v mod n and the displayed inverse in section 2. This demonstrates
actual bidirectional residue storage, with a complete inverse; it
still has zero joint Haar clock. It is not declared a classical
symplectic manifold or Hamiltonian model.

**Marginal / owner control.** Reading only x makes the division
branch have IMAGE factor n. Reading only y makes the write branch
have factor 1/n. Neither factor alone is the full owner's derivative.
A conditional/unstable index, another measure or an independent
physical roof would need its own exact groupoid and return convention.
None is supplied here, and no such clock is proved impossible.

**Root weights and arbitrary selectors.** The endpoint theorem
covers every positive finite w_n and every frozen rho, even a
theoretically prescribed selector. Thus completing or changing the
routing within this precise class cannot recover positive times.
This is not a theorem against seed-dependent measures, other transfer
laws, conservative geometry in general or physical return clocks.
Naturalness of an unspecified arithmetic routing is not evaluated.

## 5. Separate external geometric control

Athreya–Cheung's Theorem 1.1 supplies the frozen BCZ map and actual
roof; Theorem 1.4 characterizes section periodicity by rational slope.
Section 1.3.3 gives least horocycle periods Q² for every integer Q.
These statements concern their full geometric owner, not T_rho.
[Primary source, v2](https://arxiv.org/pdf/1206.6597v2).

Our admission inference is limited: Farey coprimality does not supply
the required prime/composite admissibility feedback, and selecting
prime Q would change the source. This remains an EXTERNAL CONTROL.
No disputed omitted-orbit endpoint is needed. It also illustrates why
the joint IMAGE-clock stop is not a universal physical-clock no-go.

## 6. Portfolio decision and reproducibility

**STOP this joint-image-clock admission route / FORK. No main candidate
is admitted.** The new reusable result is uniform in routing and root
weights; future work need not search routing tables to fix this clock.
A genuinely different time owner or transfer mechanism must be frozen
before its claims. Neither the external geometric clock nor a marginal
index can be credited to the two-source product owner.

The method uses exact congruences, rectangle-to-Borel measure identities,
full bisection composition and a global real-coordinate change. There
is no numerical input, cutoff, precision choice, period enumeration,
prime table or zero fitting. Each fixed rho,w maintains its complete
same-object ledger throughout. The source check is bounded primary
literature verification, not a systematic review or novelty claim.

This methodological screen assigns no A0/A1/A2 or T0–T3 coordinates.
Classical symplectic, positive-roof, Hamiltonian/contact/quantum and
analytic owners are NOT SUPPLIED. Formal coordinates UNASSIGNED;
B NOT INVOKED. All previous packages are unchanged, 241/242 remain
paused and the programme goal stays active. ARS's staged internal
review and AI assistance are disclosed; they are not external peer
review, formal verification or independent-error certification.

- [Frozen quantified contract](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence, source scope and verification](evidence/README.md)
- [Bounded scouting record](evidence/scout-record.md)
- [Three-checkpoint internal review](evidence/independent-review.md)
