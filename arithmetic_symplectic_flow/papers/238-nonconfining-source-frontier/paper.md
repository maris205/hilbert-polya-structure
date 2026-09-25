# Reversible divisor-source transport with a unit-clock obstruction

**Paper ID:** `238-nonconfining-source-frontier`  
**Scope ID:** `ASFS-SCOUT-20260918-NCF01`  
**Candidate ID:** `ANG-20260918-RDS01`  
**Date:** 2026-09-18. **Status:** `FULL REVERSIBLE OWNER; PRIME SCAN CLOCK — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The frozen RDS01 control composes a cyclic divisor scan with a reversible
transport of the current integer quotient. Its full countable carrier retains
every composite state and has no auxiliary counter. Explicit inverse formulas
give a complete two-sided unit-roof suspension, and a divisor hit genuinely
changes the source integer. For every prime p, the whole prime fibre forms
one primitive suspension circle with least physical period p−1. This includes
p=2: a fixed base state suspends to a nonstationary circle of period 1.
The strict inequality log p<p−1 stops the frozen target-clock audit. Composite
recurrence and source naturalness remain open; neither is needed for this
scoped negative result. No operator or formal Route result is supplied.

## 1. Identity, question and ownership

The [version-1 card](candidate-card.md) froze RDS01 as a short gate-control,
not a commitment to prolonged packet classification. The question is whether
reversible source updates retain the intended prime clock on the same flow.
The scope NCF01 is a search record, not another dynamical object.

| Item | Frozen owner and boundary |
| --- | --- |
| Carrier | All X={(n,d): n≥2, 1≤d<n}, with discrete topology |
| Action | F=C∘R, exactly as in section 2; all integer parameters fixed |
| Flow / time | S=(X×R)/((x,u+1)∼(Fx,u)), with elapsed-time translation |
| Arithmetic source | Local proper-divisor test and transport of the current quotient n/d |
| Packets | Every primitive closed orbit of this full suspension, modulo actual time translation |
| Repetitions | Repeated traversal of the same primitive circle; no new label substituted |
| Classical symplectic fields | NOT APPLICABLE; no finite-dimensional symplectic realization supplied |
| Operator / trace / determinant | NOT SUPPLIED; no other candidate's object is imported |

No carrier coordinate, phase, orbit, clock or topology is removed in the audit.
The strongest claim is an exact owner construction and a prime-clock failure;
it is not a full composite-orbit classification or a natural arithmetic source.

## 2. Definitions, inputs and lineage

For 1≤d<n let d⁺=d+1 when d<n−1, and d⁺=1 when d=n−1. Set

\[
 R(n,d)=(n,d^+),\qquad
 h(k)=\begin{cases}
 k+2,&k\ge2\text{ even},\\
 k-2,&k\ge5\text{ odd},\\
 2,&k=3.
 \end{cases}                                                   \tag{1}
\]

The divisor-hit subset and update are

\[
 A=\{(n,d)\in X:d\ge2,\ d\mid n\},\qquad
 C(n,d)=\begin{cases}(d\,h(n/d),d),&(n,d)\in A,\\
 (n,d),&(n,d)\notin A,
 \end{cases}\qquad F=C\circ R.                                 \tag{2}
\]

Only integer arithmetic, parity and the displayed all-integer rules are inputs.
There is no prime table, prime-specific parameter, logarithmic roof, von
Mangoldt weight, zero data or chosen prime subsystem in the definition.
The [prior-work lineage](../../docs/prior_work/README.md) is explicitly
local prime/composite divisor observables → sequential admissibility scan →
reversible transport of the source quotient. This is a defined deformation,
not a claimed conjugacy to the chronological sieve, Logistic or Hénon dynamics.
The parity routing and cyclic scan are designs with naturalness OPEN.

## 3. Exact bijection and full flow

**Lemma 1 (inverse on the whole carrier).** The maps h, C, R and F are
bijections of their stated domains. Their inverses introduce no new state.

**Proof.** The three image classes for h are respectively the even integers
at least 4, the odd integers at least 3, and {2}. They are disjoint and exhaust
all integers at least 2. Thus

\[
 h^{-1}(j)=\begin{cases}3,&j=2,\\
 j-2,&j\ge4\text{ even},\\
 j+2,&j\ge3\text{ odd}.
 \end{cases}                                                    \tag{3}
\]

For each fixed d≥2, the part of A with second coordinate d consists exactly
of (dk,d) with k≥2. On this complete set C acts as k↦h(k); its image stays
in that same set because h(k)≥2. Thus C maps A bijectively onto A and fixes
its complement. Its inverse uses h⁻¹ in (2), with the identical hit predicate.
In particular no hit image collides with a state from the fixed complement.

The inverse of R is R⁻¹(n,d)=(n,d−1) for d>1, and R⁻¹(n,1)=(n,n−1).
This includes n=2. The composition inverse is F⁻¹=R⁻¹∘C⁻¹, in that order.
All maps are continuous on their discrete domains, as are their inverses. ∎

**Proposition 2 (same-source change).** The full map changes its integer
source: F(4,1)=(8,2), and its full inverse returns (8,2) to (4,1).

**Proof.** R(4,1)=(4,2) lies in A, with quotient 2; h(2)=4. Conversely
h⁻¹(4)=2 gives C⁻¹(8,2)=(4,2), then R⁻¹(4,2)=(4,1). ∎

This exact witness distinguishes a source update from a static integer label.
Every hit output has n′=d h(n/d), with both factors at least 2, and is
therefore composite; the inverse hit has the same property. Non-hit C and R
preserve n. Thus the full composite sector is F-invariant in both directions,
and each prime fibre is separately invariant. Source updates occur only
among composites and do not dynamically generate prime labels. No escape
theorem or naturalness conclusion follows; no trajectory experiment was used.

**Theorem 3 (complete suspension and periodic convention).** The frozen
quotient S is Hausdorff and owns a continuous two-sided action
φᵗ[x,u]=[x,u+t]. For every x, its suspension orbit is a line or a circle;
it is a circle precisely when x belongs to a finite F-cycle. A least base
period m gives least physical period m and traversal times rm.

**Proof.** The equivalence relation is generated by
(x,u)↦(Fx,u−1). By Lemma 1 it is the orbit relation of a Z-action.
It commutes with translation in u, so φᵗ is well defined and satisfies
φ⁰=id and φᵗφˢ=φᵗ⁺ˢ, including negative times.
For the representative 0≤u<1, write j=⌊u+t⌋. Then

\[
 \varphi^t[x,u]=[F^j x,u+t-j].                                \tag{4}
\]

There are finitely many crossings on any bounded time interval. No forward
or backward Zeno accumulation is possible because every roof is exactly 1.

For each complete F-orbit O, its suspension is an open-and-closed component
of S, since O is open-and-closed in discrete X. Fix x∈O. The map
t↦[x,t] parametrizes this component: [Fʲx,u]=[x,u+j]. If O is infinite,
this gives a line; if its least length is m, precisely t and t+km are
identified, giving R/mZ. These are homeomorphisms, as can be checked on the
open interval charts inside strips and across their glued endpoints.
Thus S is a disjoint union of Hausdorff lines and circles, and translation
is continuous on every component and hence on S.

Equivalently, [x,u+t]=[x,u] requires t∈Z and Fᵗx=x. On a finite cycle
the full return subgroup is mZ. Its least positive element is m, and an
r-fold traversal has time rm. This argument retains all of X; it does not
decide which composite states lie in finite cycles. ∎

Both X⋊F Z and the continuous-flow transformation groupoid S⋊φ R belong
to these same frozen maps. This establishes the broadened action owner,
without supplying a symplectic base, trace representation or quantum owner.

## 4. Prime packets and decisive clock failure

**Theorem 4 (prime scan times).** For every ordinary prime p, all p−1
states (p,d), 1≤d<p, form one F-cycle. They supply exactly one primitive
suspension circle within that prime fibre, with least time T_p=p−1 and
repetitions r(p−1). Every such T_p strictly exceeds log p.

**Proof.** No d with 2≤d<p divides p, and d=1 never triggers C. Therefore
C is the identity on the entire prime fibre, F restricts there to R,
and Fʲ(p,d) advances d by j modulo p−1. The least positive return is p−1.
These phases are the same base cycle, not p−1 distinct packets.
Theorem 3 gives its one primitive circle and physical traversal times.
When p=2 the only base state (2,1) is fixed, but its suspension is R/Z:
the continuous-time orbit is not stationary and has least period 1.
Finally

\[
 \log p=\int_1^p\frac{dx}{x}<\int_1^p dx=p-1,\qquad p>1.       \tag{5}
\]

Also 1/x≤1/√x on [1,p] gives log p≤2(√p−1), hence
(p−1)/log p≥(√p+1)/2→∞ along the primes. Thus no fixed time-unit
multiplier turns these linear scan times into logarithmic-scale times. ∎

Prime fibres are invariant in both directions by Lemma 1 and their cyclic
restriction. Their retained returns rule out the concern that this control
lost every prime return. The theorem neither excludes nor enumerates
composite cycles. In particular the nonperiodic successor chain of h alone
cannot classify cycles of the different composition F=C∘R.

## 5. Controls, adverse findings and limits

| Control | Exact finding and limitation |
| --- | --- |
| Inverse / branch-image control | A and its complement are preserved by C; (3) and the predecessor scan recover every state without a counter |
| Source-changing witness | (4,1)↔(8,2) under F/F⁻¹; changes stay in the invariant composite sector, with no generated prime labels |
| No-hit prime control | The full prime fibre returns; p=2 remains a nonstationary suspended circle |
| Zero-update comparator C=id | On that different owner, every n-fibre is an R-cycle with time n−1, including composites; the prime clock is already the scan clock |
| Ownership / roof control | Importing 226's adjacent-ratio roof changes RDS01; no such repair is made |
| PROVES_TOO_MUCH / naturalness | Many quotient permutations could be inserted while preserving invertibility; no uniqueness or arithmetic naturalness follows from Lemma 1 |
| Cutoff / precision | No enumeration, numerical approximation or cutoff enters any theorem |

Nearest comparisons are the source-changing but noninvertible
[219](../219-reversible-escape-carry/candidate-card.md), the history and
counter multiplicity in [221](../221-natural-extension-carry/candidate-card.md),
the finite-component recurrence caution in
[229](../229-chord-ribbon-scattering/candidate-card.md), and the separately
engineered clock in [226](../226-exact-telescoping-clock/candidate-card.md).
No result, clock or geometry is transferred from these controls.

## 6. Gate assessment and decision

| Gate | Exact RDS01 status and limit |
| --- | --- |
| T0 | ESTABLISHED: full bijection, Hausdorff carrier and complete physical action |
| T1 | Source update ESTABLISHED; target prime clock scoped FAIL; naturalness OPEN |
| T2 | Prime-fibre packets and repetition ESTABLISHED; complete composite ledger OPEN |
| T3 | NOT SUPPLIED; no analytic owner pursued after the clock stop |
| Classical A0/A1/A2 | NOT APPLICABLE to this broadened carrier |
| Formal Route / B | UNASSIGNED / NOT INVOKED |

**Portfolio decision: STOP RDS01 at the unit clock; FORK the search.**
The same-object ledger remains intact. A new source update, roof, geometry,
quotient or operator would require a new card. The distinct BFT01 owner has
its [separate card in 239](../239-bilateral-factor-transport/candidate-card.md);
none of the proofs above depends on it. NCF01 itself receives no T0–T3 score.

## 7. Separate lanes and portfolio outcome

The separately completed [239 audit](../239-bilateral-factor-transport/paper.md)
removes the growing diagonal and uses every integer multiplication/division
move on the full positive-rational norm sphere. Its own Fourier proof gives
ker(Phi_T-I)={0} for every T>0: all nonzero exact returns disappear, including
prime returns. That is a different stop from the scan-scale prime clock in
RDS01. Its generator, representation and empty periodic ledger are not used
as evidence for this discrete scanner or a unilateral integer model.

A third read-only scout considered replacing divisor registers by all
compatible finite-modulus registers, with multiplication correspondences
and logarithmic scale arrows. It was not admitted as a new frozen object:
no new source-feedback or intrinsic prime-return mechanism was supplied
beyond the relevant [024 lineage bridge](../024-primorial-scaling-site-bridge/README.md)
and [146 localization-scaling control](../146-localization-scaling-groupoid/README.md).
The [061 lineage boundary](../061-bost-connes-lineage-boundary/README.md) and
[136 factor-path control](../136-factorization-nonbacktracking-flow/README.md)
were additional comparisons. This is a bounded admission decision, not a
theorem about a new profinite flow or a literature-wide exclusion. No
provisional arrow time is credited as a primitive period.

The portfolio position is STOP / FORK for both frozen gate-controls and
NO ADMISSION for that third proposal. One must retain prime returns as well
as exclude unwanted mixed packets, and the same action must supply their
physical clock. RDS01's reversibility without an extra register is a scoped
engineering result; BFT01's full no-return theorem is a separate adverse
control. Their statements do not combine into positive Route credit or a
general impossibility theorem.

## Reproducibility and declarations

The [card](candidate-card.md), [claim ledger](claim-ledger.md) and
[evidence record](evidence/README.md) identify inputs and actual checks.
Data availability: all evidence is the displayed proof; no dataset exists.
Codex assisted drafting; human CRediT roles, funding and conflicts are
unspecified. No human-subject/private-data study or external peer review
was performed; no venue-fit, publication or Route claim is made.
ARS informed the frozen definitions, proof/evidence separation and adverse
controls; venue criteria are unavailable (`criteria_binding_unavailable`).
