# Gap-antichain histories: a full-support sequential law fails prefix IMAGE

**Paper:** `378-gap-antichain-admission`; candidate `ANG-20260922-GAC01`.<br>
**Date/status:** 2026-09-22; **SEQUENTIAL LAW OWNED / IMAGE ADMISSION FAILS — STOP / FORK**.<br>
Batch `HARD-NONLOCAL-20260922-F`, round 4/5. T0 source/law established; T1 clock admission FAIL; T2 source ledger only, physical fields NOT DEFINED.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; Route B NOT INVOKED.

## Abstract

On the entire frozen binary gap-antichain source, the sequential legal-bit recipe defines a full-support probability. Its complete atom set is
`0^r 1^s 0^infinity`, r>=0, s>=2, of masses `2^-(r+s+1)` and total mass 1/2;
the remaining mass 1/2 is nonatomic. The legal source y=`1 0^infinity` has mass zero, while prefixing 1 gives z=`11 0^infinity` of mass 1/8. Moreover
the frozen restricted-cylinder denominator at y is already zero from length 2.
Thus both the prescribed version and intrinsic every-Borel IMAGE admission
fail. Full legal incoming histories, source isotropy and null periodic paths
remain. Three own controls distinguish this failure from valid zero clocks
and a valid but target-incompatible Bernoulli clock. No physical MAIN clock
or return group is defined by a successful calculation on selected paths.

## 1. Identity and complete source

The [clarified card](candidate-card.md) fixes ALL x in `{0,1}^N_0` whose
completed gaps between consecutive ones have pairwise equal-or-incomparable
values under divisibility. Write Gamma(x) for the SET of these positive gap
values, used only for admission, never as a quotient of binary states.
The full word, its leading zeros, finite-one or infinite-one history and all boundary tails remain. Gap 1 is allowed; an infinite zero tail is not a gap label.

| Owner field | Frozen object |
| --- | --- |
| Carrier/action | Full X with product-subspace Borel; T removes first bit |
| Probability | Forward legal-prefix recipe P, not an imported stationary law |
| Inverse domains | E_a={y:ay in X}, I_a(y)=ay, a=0,1 |
| Admission | Restricted-cylinder limit and every-Borel IMAGE on each E_a |
| Histories | Actual triples (z,m-n,y) with T^m z=T^n y, all lags retained |
| Clock/geometry/operator | Clock conditional; no roof, symplectic or analytic owner supplied |

Any violation is witnessed by a finite prefix containing two incompatible completed gaps. Thus X is closed in the compact binary product, hence compact
Borel. Appending zeros to any legal finite word adds no completed gap, so every
such word has an extension in X. The constants and every listed test are retained.
T deletes at most an initial completed gap and creates none; it maps X into X.
Prefixing 0 always remains legal, so T is onto, not asserted to be invertible.

E_0=X. If y has no one, y belongs to E_1. Otherwise, with its first one at r,
prefixing 1 introduces exactly d=r+1; E_1 requires d equal or incomparable
to EVERY old completed gap. These conditions prove the stated domains and
exhaust all predecessors; I_a is inverse to T on X intersect [a]. The E_a
are closed by continuity of prefixing, hence Borel; openness is not assumed.

More generally E_w={eta:w eta in X}. If w has last one at j and eta first
one at r, the concatenation introduces the bridge gap |w|+r-j. Its completed
gap values are those of w and eta plus that bridge; if either has no one,
there is no bridge. Testing this ENTIRE union gives the exact E_w. Thus the
chart v eta -> u eta has precisely common-tail domain E_u intersect E_v and
inverse u eta -> v eta. No cross-boundary divisor test or null tail is omitted.

The lineage is proper-divisor witnesses -> full-history hard gap admission ->
actual allowed bit generation and prefix transport. The constraint and uniform
legal-choice rule are design input, not canonical prime-derived weights or
370's independent-gap measure. No equivalence/novelty theorem is claimed.

## 2. Exact prefix law, full support and COMPLETE atom ledger

For legal h, L(h) always contains 0, and contains 1 exactly when the new
completed gap, if any, is compatible with Gamma(h). Thus |L(h)| is 1 or 2.
The card's recursion sums correctly over both children, starting at P(empty)=1; illegal words and their children have weight zero. Consistent finite-coordinate
probabilities extend uniquely to a Borel probability mu. Illegal-prefix
cylinders form the complement of X and have zero mass. Every legal finite
prefix has positive weight, so mu has full support on the ENTIRE X.

Here is an exact finite-prefix formula, including forced steps. Let b(h) count the positions t<|h| at which BOTH extensions of the preceding prefix are legal.
Then mu([h])=2^-b(h) for legal h, and zero otherwise. At a proposed completion
the allowed bit 1 costs 1/2; a zero costs 1/2 if that 1 is allowed, and costs
1 otherwise. This determines every later step, not only the initial prefix.

Every path with infinitely many ones has zero singleton mass: every 1 was an optional choice with factor 1/2. A path with zero or one one also has mass zero,
because along its zero tail no gap has yet been completed and both choices
remain legal forever. Suppose a finite-one path has completed a gap 1. All
other gap values must then also be 1, so it is exactly 0^r1^s0^infinity with
r>=0,s>=2. Before its final zero, and at that zero, all r+s+1 choices are
optional. Thereafter any future completed gap would exceed 1 and is forbidden:
EVERY remaining zero is forced. Hence its singleton mass is 2^-(r+s+1).

For every other finite-one path, Gamma is finite, nonempty and excludes 1. Set M=product_(e in Gamma)e. Infinitely many potential next gaps 1+kM exceed
all e and are coprime to them, hence are legal completions. Along the infinite
zero tail each such opportunity is an optional zero with factor 1/2. Its
singleton mass is therefore zero. This proves the complete point-atom list.
On a binary product any positive Borel atom determines a nested cylinder at
every length carrying its mass, and hence a point atom; none is missing.

The total atomic mass is

    sum_(r>=0,s>=2) 2^-(r+s+1) = (1/2)(2)(1/2) = 1/2.

The complementary measure has mass 1/2 and no atoms. Finite-one paths are a countable set; outside the listed atoms they have total measure zero. Thus the
remaining mass is carried by infinite-one histories. Full support is NOT
confused with full mass on every retained history or with nonatomicity.

## 3. Restricted denominators and intrinsic transport failure

Leading zeros change no completed-gap test. The exact prefix recursion gives P(0h)=P(h)/2, and probability uniqueness extends this to

    mu(I_0 D)=mu(D)/2 for EVERY Borel D subset X.

Every legal cylinder is positive; hence the prescribed j_0=1/2 holds at all
points and all cylinder lengths, including null periodic and eventual-zero paths.
This one successful branch is not admission of the whole owner.

Use the clarified singleton notation y=1 0^infinity and z=11 0^infinity. For every m>=0, P(1 0^m)=2^-(m+1), since no gap has been completed. For every
m>=1, P(11 0^m)=1/8: the first three choices are optional and all later zeros
are forced. Continuity on decreasing cylinders therefore gives mu({y})=0,
mu({z})=1/8. Both belong to E_1; I_1(y)=z and I_1(z)=1110^infinity.

For N>=2, a tail in E_1 intersect C_N(y) starts 10. If it had another one, its first completed gap would exceed 1 and conflict with the gap 1 introduced
by prefixing. Consequently

    E_1 intersect C_N(y)={y},  mu(E_1 intersect C_N(y))=0,
    mu(I_1(E_1 intersect C_N(y)))=mu({z})=1/8.             (1)

The frozen finite-N fraction is UNDEFINED, not a ratio assigned infinity. Replacing the denominator by mu(C_N(y))=2^-N would change the contract.
More strongly the Borel singleton D={y} violates absolute continuity of the
IMAGE measure: no density version can give 1/8=integral_D j dmu. This is an
intrinsic failure for this fixed measure and branch, not just a cylinder-version
or strict-positivity failure. It cannot be repaired at null points.
Also T^-1{y}={01 0^infinity,z} has measure 1/8, whereas mu({y})=0. Thus the
sequential law is neither stationary nor nonsingular for this shift.

## 4. Named full-state tests and partial ratios, without constructing a clock

All the following words belong to MAIN and to the adjacent-gap control:

| Actual state | Gap data | Singleton mass | ENTIRE source isotropy |
| --- | --- | --- | --- |
| 0^infinity | no gap | 0 | Z |
| 1^infinity | gap 1 | 0 | Z |
| (10)^infinity | gap 2 | 0 | 2Z |
| (100)^infinity | gap 3 | 0 | 3Z |
| (10100)^infinity | gaps 2,3 | 0 | 5Z |
| 1 0^infinity | no completed gap | 0 | Z, eventual zero, not directly periodic |
| 11 0^infinity | one completed gap 1 | 1/8 | Z, eventual zero, not directly periodic |

For the four nonzero periodic words below, put y=Tx and use its actual inverse
I_1. The indicated prefix h of y contains the introduced gap again. Therefore
[h] is contained in E_1 for MAIN. Once h is read, h and 1h have the same
completed-gap set and age, so all subsequent legal-choice probabilities agree.
The following ratios therefore hold for ALL sufficiently large N, not just h:

| x | h prefix of Tx | P(h) | P(1h) | prescribed partial ratio at Tx |
| --- | --- | --- | --- | --- |
| 1^infinity | 11 | 1/4 | 1/8 | 1/2 |
| (10)^infinity | 0101 | 1/16 | 1/16 | 1 |
| (100)^infinity | 001001 | 1/64 | 1/64 | 1 |
| (10100)^infinity | 0100101 | 1/64 | 1/64 | 1 |

The optional-bit formula proves each entry, including the forced zero after
any completed gap >=2. The actual branch at 0^infinity is I_0, already covered.
For the additional incoming branch I_1 at 0^infinity, its restricted denominator
is positive at every N: for N>=1 the cylinder [0^N1 0^N1] lies inside
E_1 intersect [0^N]; for N=0 use [11]. Its numerator is P(1 0^N)=2^-(N+1).
No unused limit at that branch is claimed after the decisive universal failure
(1). At z as an inverse TARGET, restricted cylinders from length 3 are {z}
and the ratio to I_1(z) is (1/16)/(1/8)=1/2; at y they fail as in (1).
These successful partial ratios do NOT define kappa, c or any physical period.

## 5. Full actual source ledger survives failed IMAGE admission

For every source the entire incoming orbit is {w T^m x: m>=0, w finite, w T^m x legal}, with all actual witness lags. All source/range prefix charts
use E_u intersect E_v as in section 1. Equal triples alone are identified.
The full lag kernel consists of synchronous eventual-agreement arrows
(z,0,y), which can join different points, not only identity arrows.

A nonzero isotropy lag is equivalent to eventual periodicity of the complete binary tail. Its entire isotropy is pZ for the least positive binary tail
period p; otherwise it is {0}. This follows directly from equality of two
shifted tails and the least-period division argument. Every eventual-zero
source, including both singleton tests and all atoms, has isotropy Z, even
when it is not a directly periodic point. All legal finite-one histories
belong to the zero-tail source orbit, with all their incoming labels retained.

Here is the COMPLETE periodic admissibility rule. Apart from the all-zero word, a periodic binary word has a finite cyclic list of positive gaps. It
belongs to MAIN iff every two distinct values of that list are divisibility-
incomparable. Its least binary period is the SUM of one primitive cyclic
gap block, not its number of gaps or the length of an unreduced written word:
any binary period sends ones to ones and repeats that gap block, and conversely
a repeated gap block produces precisely that binary translation. The all-zero
case has least period 1. All legal incoming prefixes are still checked against
the entire tail gap set and the bridge; a periodic core does not waive that test.

MAIN has no admitted clock. Its clock kernel/intersection, height extension,
extension isotropy, H, physical phases and primitive physical repetitions are
NOT DEFINED, not zero. Source isotropy and lag kernel above do not require them.

## 6. Three independently owned controls

### 6.1 ADJACENT-GAP-ONLY

Use its full binary source and its OWN prefix law. Only successive completed gaps must be equal or incomparable. Finite violations again give a closed
source, and deleting initial bits preserves it. E_0 is all of that source;
E_1 checks the new first gap against only the first old gap, if present.
General E_w checks the ordered list of prefix gaps, bridge and tail gaps at
all consecutive boundaries. These are all inverse branches and actual domains.
The finite completed word (2,3,4) is legal here but illegal in MAIN because
2 divides 4. One full witness has ones at positions 0,2,5,9 and zeros elsewhere.
This finite-word test is NOT a periodic repetition: the cyclic 4-to-2 boundary
would fail the adjacent periodic rule.

The independent prefix recursion is consistent, has full support and obeys the same optional-count formula, now with the last gap as its sole gap memory.
Its complete atom argument must be run on this rule: infinitely many ones
again force infinitely many factors 1/2. Gap 1 can first occur only as the
first completed gap, since it is incompatible with every preceding gap >=2.
After gap 1 all later completed gaps must be 1, and a zero then forces zeros
forever. For a last gap e>=2, infinitely many later candidate gaps 1+ke are
legal; a final infinite zero tail has mass zero. With zero or one one all
choices stay optional. Thus its OWN atoms are exactly 0^r1^s0^infinity with
the OWN masses 2^-(r+s+1), total 1/2; its remaining mass 1/2 is nonatomic.

Its singleton y/z masses are independently 0 and 1/8, and E_1 intersect [10] is again exactly {y}, because its first old gap would conflict with the new 1.
The zero restricted denominators, intrinsic IMAGE failure and shift nonsingularity
failure therefore hold for this control too; no density is inherited from MAIN.
Its I_0 has its own every-Borel factor 1/2. Its source groupoid, lag kernel and
isotropy criterion are obtained by its own shift, with all legal incoming domains.
Periodic admission requires the equal-or-incomparable rule between EVERY
neighboring CYCLIC gap pair, including the wrap; least binary periods are the
primitive gap-block sums. All listed state/mass tests agree as derived above;
their partial-ratio table also follows since the ending last gaps agree.
Its failed clock-dependent fields remain NOT DEFINED, not zero.

### 6.2 INTERACTION-OFF

The full binary shift has its OWN fair Bernoulli law: mu([h])=2^-|h|, full support and no atoms. Both inverse domains are all X. Cylinder identities
extend to every Borel D and give mu(aD)=mu(D)/2. Thus its prescribed ratios
are 1/2 at every point and length. For a prefix chart v eta -> u eta, IMAGE
is 2^(|v|-|u|); on actual triples the admitted c=(m-n)log2 is well defined,
additive and has the correct inverse sign. This proves every finite-history
IMAGE without borrowing any failed MAIN version.

The full clock kernel equals the lag kernel and their intersection: ALL synchronous-tail arrows (z,0,y), not merely units. Source isotropy is {0}
for non-eventually-periodic paths and pZ for least tail period p. Extension
isotropy is trivial; H is respectively {0} or p log2 Z. All prefixes are legal.
Relative to an actual arrow g:f->x, phase is h-c(g) modulo H_f; alternative
arrows differ by the complete source stabilizer. At T^N x=f this is h-N log2.
The physical orbit over each source orbit is R/H_f as a SET, no manifold claim.
Primitive binary necklaces, modulo cyclic rotation, give exactly one packet
each: common shifted tails identify exactly such rotations. Its least time
is p log2 and repeats are k p log2 of that SAME packet. All eventual-zero
prefixes attach to the zero-core packet, not additional selected packets.
Constant 0 and constant 1 give two log2 packets; primitive 01 gives log4.
This complete ledger stops its target, not its valid measured construction.

### 6.3 EVOLUTION-OFF

This owner retains literally MAIN's X and the mixed probability proved above, but uses id_X and its unique inverse. Every-Borel IMAGE is 1; its all-point
prescription is 1, including all null histories. The retained groupoid consists
of (x,k,x) for every x,k. Clock is zero, full clock kernel ALL arrows, lag
kernel/intersection identities, source and extension isotropy Z, H=0.
All incoming labels stay at the same x; no formerly shift-related points merge.
The quotient SET is X times R, phase h, with free height translation on each
{x} times R and no positive primitive packet. This is not a clock for MAIN.

## 7. Decision and exact evidence boundary

STOP/FORK MAIN at intrinsic prefix IMAGE admission, preserving the entire source and the mixed law. No alternative density version for this SAME owner
repairs (1). No universal exclusion of other laws, sources or clocks follows.
No kappa/c/physical extension is manufactured for either failed owner. The
admitted controls retain their own complete but target-incompatible ledgers.

New inputs read in full: clarified card 1–92, scope 1–88, template 1–107, with actual totals measured by wc; card SHA256
`a29076fda9d37d4bc34ca977d4d24ad678f9d7eb89df2e77a904f09cda7a131b`,
scope SHA256 `666365f298a065f59f61fb5b4c99aa269b563e5977047517c69dfbe03592b826`.
Read commands were sed on those authorized ranges, wc -l and sha256sum;
subsequent reads/hashes concern only this authored paper. The author supplied
the earlier definition-only reserve; singleton tests and notation clarification
were root's pre-proof additions. No raw proof, peer manuscript or other new
scientific report was read; no scientific code, external search or Git was used.
ARS discipline and inherited history remain internal shared-history NOT_CALIBRATED,
not blind discovery, external peer review or novelty certification. Strong
naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED;
Route B NOT INVOKED. No sixth round or measure-repair authority is implied.
