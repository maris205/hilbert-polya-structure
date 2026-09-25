# Frozen candidate — adjacent-factor exchange with active seed parity

Candidate ID: `ANG-20260920-AFP01`.
Paper ID: `300-adjacent-factor-parity-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL PARITY OWNER, IMAGE CLOCK AND SEED RETURNS`.

## 1. Entire source and autonomous partial action

Let K=Z_hat with its full compatible-residue topology and normalized
additive Haar h. Freeze ALL Y=coproduct_(a,b>=1) {(a,b)} x K^2,
with discrete root topology and mu|_(a,b)=h x h, root mass one.
Every unit/composite root, zero seed, noninteger seed and terminal
object stays. At z=(a,b,x,y) read

    j=x mod a in {0,...,a-1}, delta=y mod 2 in {0,1},
    epsilon=1-2*delta.

The forward domain is EXACTLY b+epsilon>0 and a|b(b+epsilon).
There define

    c=b(b+epsilon)/a,
    T(a,b,x,y)=(b,c,y,(x-j)/a+y).

All other states have no forward step; do not remove their identity
or actual incoming arrows, add a restart, or adjoin an escape loop.
Division is in K, not real division or a finite-modulus approximation.
At a=1, j=0 and the seed rule is (y,x+y), with no extra unit roof.
At b=1 and delta=1 the point is terminal; when delta=0 the same
a|2 condition applies. There is no selected prime fibre or seed.

For admissible a,b,delta and 0<=j<a freeze the proposed branch

    U={roots (a,b), x mod a=j, y mod 2=delta},
    V={roots (b,c), u mod 2=delta, v arbitrary in K},
    I(b,c,u,v)=(a,b,j+a(v-u),u).

The equivalent proposed inverse test at (b,c,u,v) reads delta=u mod 2
and a=b(b+1-2*delta)/c: the numerator must be positive and a a
positive integer, then ALL j=0,...,a-1 are retained. Verify these
complete images, inverses, domain topology and possible missing image.

## 2. Full measured groupoid and clock ownership

Freeze the ENTIRE partial retained-lag tail groupoid

    G_T={(z,m-k,w): T^m z=T^k w, both defined, m,k>=0},

source w, range z. T^0 includes every terminal object. Topology
uses all actual finite inverse-branch pairs on common open terminal
domains and all clopen seed refinements. No extra affine arrows,
free word labels, germs, selected histories or conull reduction.
Prove the topological owner from the actual partial local action.

The proposed INVERSE Borel IMAGE factor is J_I=1/a, still UNPROVED.
Derive it from this mu on arbitrary Borel subsets of V, including
the parity restriction, before using c_G=-log J. For A_m(z) the
product of first roots along a defined m-step history, A_0=1,
the proposed full clock is log A_m(z)-log A_k(w). Prove all-point
presentation independence, additivity and the continuous version
owned by full support, including null returning/nonreturning seeds.

Extension objects are ALL Y x R, with arrows
(w,s)->(z,s+c_G). Physical time is s->s+t for EVERY real t.
Prove jointly continuous complete time on this owner. Zero-clock
a=1 steps stay zero; no runtime or positive roof is substituted.
No Hausdorff coarse quotient, embedded circle or classical suspension
is presumed. Source isotropy, fixed-object extension isotropy and
the time group H_z=c_G(G_z^z) are separate invariants.

Primitive cyclic-time packets require H_z=T_z Z with least T_z>0.
Repetition traverses that SAME packet ell times, yielding ell*T_z.
Packet identity uses actual tail arrows and real phases, never equal
integer products, equal lengths or a root projection alone.

## 3. Ordered discriminators and stop boundary

1. Establish the full profinite source, partial branches, inverse
   IMAGE law and same-object continuous time, retaining terminals.
2. First compare fixed/short root-return possibilities with the
   complete seed equations. As a concrete mixed-sign family test
   the proposed repeating root pattern

       (n,n),(n,n+1),(n+1,n+1),(n+1,n), n>=1,

   with required signs +,-,-,+. Check arithmetic admissibility,
   ALL digits and parity conditions; a cyclic root list alone is
   not a full return. Include arbitrary repeated traversals of this
   pattern if a uniform seed argument makes that check immediate.
3. Look for a uniform restriction on periodic seed pairs under
   the displayed residue/shear rule for ANY finite positive index
   word. A rational matrix equation must be solved in K, not just
   modulo selected integers. If a short exact argument gives an
   all-period implication, use it to decide full-state returns;
   otherwise keep the remaining return locus OPEN without a census.
4. A decisive obstruction to prime primitives, unwanted packet or
   ownership failure stops target promotion. Finish only controls
   below; do not tune parity, domains, residues, measure or roof,
   and do not construct T3 to rescue this source. Failure of only
   the tested root family is not a global nonreturn theorem.

The card is informed by definition-stage mixed-root and seed-recurrence
considerations; it is not a blind design claim. All recorded theorem
claims and scientific computations must follow this freeze.

## 4. Separately owned controls

PARITY-OFF: set epsilon=+1 at every state in both the root rule
and admissibility test. Retain both seeds, the actual j, full Y and
mu. Derive its OWN branch clock; test complete periodic roots and
full time-return groups. Do not filter odd seeds from the carrier.

ADJACENCY-OFF: replace b(b+epsilon) by b^2 and remove the parity
dependence from the domain/root rule. Domain is a|b^2 and the root
update is (b,b^2/a); both seeds, j, Y and mu remain. Derive its
OWN IMAGE clock and classify its periodic points if the same short
seed restriction applies. Retain n=1, all composite n, all seed
multiplicities and finite preimages; do not identify n=4 primitives
with repetitions at n=2 without actual arrows.

Ownership controls retain failed divisibility domains, b=1 negative
branches, a=1 steps, all inverse digits and every null seed. Strong
source/admissibility/Haar naturalness is OPEN. No scientific numerical
run, cutoff, precision parameter or external literature is planned.

## 5. Lineage, provenance and nontransfer

The [prior-work](../../docs/prior_work/README.md) arrow is divisor-
based prime/composite admissibility -> a|b(b+epsilon) -> current-
seed-controlled adjacent-factor exchange -> its full measured
groupoid action. The gcd symbols with b and b+epsilon may be read
without adding a filter. This is an explicit source replacement,
not a Logistic/Henon conjugacy or positive-dimensional symplectic lift.
No prime table, accepted-prime bit, prescribed log-prime roof,
von Mangoldt weight, zero data or per-prime parameter is inserted.

The complete definition was supplied in
[299's record](../299-quotient-remainder-reciprocal-flow/evidence/scout-record.md),
SHA-256 `1b7d92d27032ec555d6afc1041bc29246089143e51abde864128470d2b647423`,
without a Jacobian or return theorem. The local seed form and IMAGE
strategy resemble [292](../292-integral-braid-residue-flow/candidate-card.md)
and [294](../294-gcd-product-residue-flow/candidate-card.md). Their
three-root braid and gcd-product updates differ; this source's active
parity chooses a positive/negative adjacent factor and its domain.
[104](../104-qrt-factorization-lineage-boundary/candidate-card.md)
is a generic QRT external control without this rule or prime-symbolic
owner. No old clock, return theorem or formal credit transfers.

## 6. Review, authority and handoff

T0-T2 are broadened owner labels only. Classical A0/A1/A2 NOT
APPLICABLE; T3 / operator / trace / Hamiltonian / quantum owners
NOT SUPPLIED / NOT PURSUED. Formal UNASSIGNED; B NOT INVOKED.
Root owns integration and all files except the native reviewer's
evidence/independent-review.md. ARS raw-card, manuscript and adverse
checks are inherited-model/shared-context internal scrutiny, not
external peer review, formal verification or independent-error evidence.
Old packages/mirrors unchanged; 241/242 paused; goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## Appended audit outcome — 2026-09-20

Final status: `OWNED PARITY IMAGE CLOCK; ALL POSITIVE RETURN PACKETS ABSENT — STOP / FORK`.

The original 158-line version-1 bytes above remain unchanged, SHA-256
`fe1dc06ce89644078e422659e0b99cf48b45bbd97dd6ae3baa74faaa2a6553d5`.
The [paper](paper.md) proves the full clopen-domain local action,
exact inverse images, joint-Haar IMAGE factor 1/a and entire
continuous retained-lag clock with complete real time. All terminal,
missing-image, unit and null states remain in the owner.

For ANY finite positive index word, a periodic seed must be the
constant integer pair (k,k), 0<=k<every consumed index. The proof
uses an all-length rational matrix argument, Q intersect K=Z and
an exact integer recurrence, not finite congruence experiments.
Main periodicity would therefore force constant parity. The cyclic
adjacent-factor product is then impossible for either sign.
Consequently ALL source isotropy, extension fixed-object isotropy
and time groups are trivial: no positive primitive packet exists.
The explicit mixed-sign four-root cycle does not lift to a full
seed return, even after arbitrarily many root traversals.

PARITY-OFF also has no return. ADJACENCY-OFF instead has exactly
the fixed cores (n,n,k,k), n>=1, 0<=k<n. Its OWN clock gives n
distinct primitive log-n packets for n>=2, while the n=1 core
has source/extension isotropy Z and zero time group. Repetitions
and finite preimages are counted through actual arrows.

Portfolio: **stop target promotion / fork**. T0/scoped measured T1
and all-state T2 are established; naturalness and nonreturning orbit
structure/coarse Hausdorffness remain OPEN. T3 NOT SUPPLIED / NOT
PURSUED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. Same-object ledger intact. [Claims](claim-ledger.md),
[evidence](evidence/README.md), [review](evidence/independent-review.md)
and [scout record](evidence/scout-record.md) preserve boundaries.
The separate full-sublattice source is definition-only and requires
its own freeze; no second result. Old packages unchanged; 241/242
paused; programme goal active.
