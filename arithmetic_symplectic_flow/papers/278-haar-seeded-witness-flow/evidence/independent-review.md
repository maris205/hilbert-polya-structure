# Independent internal review — Haar-seeded witness flow

**Candidate:** `ANG-20260919-HWS01`  
**Status reviewed:** `OWNED HAAR-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK`  
**Disposition:** PASS for the stated full-owner mathematical results and scoped limitations; no manuscript correction requested.  
**Review type:** internal model review, not external peer review or formal verification.

## 1. Scope, frozen inputs and method

The mathematical inputs are the complete [version-1 card](../candidate-card.md)
and the [manuscript](../paper.md). The original card was read and its raw
conclusions communicated before the manuscript was read.

- Frozen version-1 card SHA256:
  `2aa63c0c85cdaf2986722a1ac16654d6111701eb1a56ec945e3b7228abbb0a39`.
- Full 422-line manuscript SHA256, checked on reading and final binding:
  `9a53b0b5b0fa0648547d7a9d74404de16a5db82406ddec097ea97259e6d5605c`.

Any later administrative card outcome is not part of the version-1 input;
the original byte prefix is the frozen contract. The reviewed owner is
the full arithmetic space Y, its deterministic T, rootwise Haar measure,
retained-lag groupoid, derived IMAGE clock and real extension. It is not
276's path space, an itinerary quotient, or a full affine action.

ARS supplied the freeze-first, raw-input / manuscript-comparison / adverse
review discipline. Proof checks were exact local derivations, with no
numerical run, orbit census, source modification or new parameter family.
The manuscript's concrete arguments were checked directly; no result
about Haar clocks, stabilizers or packets was imported from older owners.
The Sims citation is used in the manuscript only for groupoid terminology;
this review does not claim a new independent bibliographic audit or borrow
an operator theorem from it. Companion scout records were not reviewed.

## 2. Checkpoint 1 — independent raw-card results

### Arithmetic source, topology and measure

Multiplication by a positive integer n is injective on K: the congruence
`nx=0 mod nm` forces `x=0 mod m` for every m. Its image is the kernel of
reduction mod n, since the compatible residues `(x mod nm)/n mod m`
construct the quotient when x is divisible by n. Thus each hub branch
`j+nK` maps homeomorphically onto its whole target K. In particular

    y=t mod m  iff  x=j+nt mod nm

on branch j. This does not assume that K is an integral domain.

All roots and branches are retained. T is locally homeomorphic but not
onto: exactly the scan roots S_(n,d), 3≤d≤n−1 with `(d−1)|n`, have no
incoming branch. Their whole K fibres are missing from the image, with
S_(6,3) the requested example. Every other root has an incoming branch;
for example S_(2n,n) maps onto H_n. The manuscript needs only the stated
non-surjectivity, not this fuller auxiliary description.

The countable coproduct Y is locally compact Hausdorff, second countable
and noncompact. Its rootwise measure is Radon, sigma-finite, full-support
and non-atomic. Each root is still a complete K, not a graph-path label.

A finite branch word has inverse

    theta_alpha(t)=b_alpha+D_alpha t,   0≤b_alpha<D_alpha,

where D_alpha is the product of consumed hub moduli; root labels remain
part of the formula. Deterministic steps contribute D=1 and b=0. For
every Borel terminal set C, `mu(theta_alpha C)=h(C)/D_alpha`.
Arbitrary terminal clopen residue sets are therefore indispensable to
the arithmetic topology; merely setting C=K loses state separation.

### Full-arrow clock and source normalization

For `theta_beta(t) → theta_alpha(t)`, the Borel IMAGE derivative is

    J=D_beta/D_alpha,       c=log D_alpha−log D_beta.

The sign follows from image mass divided by source mass. With integer
lag retained, two presentations of one arrow have deletion lengths
differing by the same amount. Locally extend both inverse words along
their common terminal continuation; both D factors acquire the same
multiplier. The ratio is unchanged. Composition gives multiplicativity
and hence the additive clock. On branch bisections the formula is
constant, providing the continuous version also at null states. Full
support prevents arbitrary continuous reassignment at those points.

The extension uses exactly this cocycle. Translation by all real t is
jointly continuous on its object and arrow spaces and respects its
source/range and composition. Zero-clock scan steps remain zero-clock;
the construction is not a positive-roof model of scan runtime.

All additive translations of K force equal mass 1/m on its m residue
cosets; these cylinders generate its Borel sigma-algebra. This proves
conditional uniqueness of each normalized Haar law. Root masses one
are a separate frozen condition, not a consequence of those translations.
At n=3 the WEIGHT demand 1/2 is therefore incompatible with that condition.
But translation by 1 does not commute with T at (H_2,0), and distinct
seeds at E_0 have no T-tail arrow between them. Neither dynamical
translation symmetry nor all rational-affine arrows follow from Haar.

### Full-state return ledger and controls

Hub descent and finite scans force every nonescaping itinerary eventually
onto a prime scan C_p. A late scan root can bypass an earlier witness,
but after returning to a composite hub its next full zero scan cannot.
For the repeated prime word the complete seed fibre is

    D_p=intersection_(r≥0) p^r K = {x: its p-adic coordinate is zero}.

All other prime-power coordinates are free. Hence this fibre is nonzero,
uncountable and Haar-null. A complete turn divides the seed by p. An
actual r-turn return requires `(p^r−1)x=0`, and integer-multiplication
injectivity forces x=0. No nonzero fibre element is removed or identified
with zero in reaching this conclusion.

The only periodic full states are zero-seed C_p phases. Their least
period is ell_p=p−1, including the H_2 self-loop. If B_p denotes all
states eventually reaching those zero-seed phases, the three groups are

| Full state | Base isotropy lags | Fixed-object extension isotropy | Actual time stabilizer |
| --- | --- | --- | --- |
| z in B_p | ell_p Z | trivial | (log p)Z |
| z outside every B_p | trivial | trivial | {0} |

On the first row the clock is `r ell_p → r log p`; transient factors
cancel. Nonzero states in a prime-word fibre belong to the second row.
Every B_p is one T-tail orbit, giving one abstract cyclic-return packet
per prime after including time translation. Different primes have no
common eventual full state. Equalities of symbolic itineraries alone
create no arrows between unequal arithmetic seeds.

Each B_p is countable, since each finite inverse branch takes zero to
one seed b_alpha. All returning states are null. The larger nonescaping
locus is also null, being a countable union of affine images of D_p.
The conull escaping locus is not a positive-atom stratum: mu is non-atomic.

The itinerary factor is continuous and onto by nested compact congruence
cylinders. Its finite-cylinder masses are 1/D_alpha. It is not injective:
an escaping itinerary already has a full affine K fibre, while a prime
tail has an affine D_p fibre. Pushforward agreement with the graph law
therefore does not identify the two state spaces or their isotropy.

SOURCE-OFF produces exactly C_n zero-seed periodic phases for every
n≥2, with least lag n−1 and one least-log-n packet per n. The 4-packet
is not the second traversal of the 2-packet. For the frozen PREDICATE
comparator the same proof gives exactly those packets indexed by n in A;
excluded scans reset to H_2 and late scan roots add only transients.
This preserves the generic-encoding naturalness objection despite the
conditional uniqueness of the source measure.

## 3. Checkpoint 2 — full manuscript comparison

After sending the raw results to root, the entire 422-line manuscript was
read. Its actual SHA matched §1. Lemma 1 and Propositions 2–4 reproduce
the source, division, topology, branch scaling, clock and noninjective
factor conclusions above without a borrowed symbolic-clock theorem.

Theorem 5 uses actual equalities `T^m z=T^k z`, not equality of itineraries.
It checks least periods, all eventual tails and the clock on the retained
lag generator. Its packet equivalence retains all states and distinguishes
the two isotropy layers from physical-time stabilizers. Sections 6–7
correctly preserve the null nonzero D_p fibres, non-atomic escaping locus,
SOURCE-OFF packets and arbitrary-set comparator. No mathematical change
was requested after this comparison.

The gate table remains scoped: T0–T2 concern this broadened owner only;
naturalness is OPEN; no classical A0/A1/A2 or formal Route promotion is
issued. The full arithmetic state is a new owner, not a repaired 276 or
a restriction of the larger scaling/affine owners.

## 4. Checkpoint 3 — final adverse check and verdict

The strongest failure possibilities were tested directly:

- **Hidden seed cycles:** a periodic word alone leaves a large D_p fibre,
  but the full return equation eliminates all nonzero periodic seeds.
  Nonzero integers are regular multipliers on K even though K has zero
  divisors; the manuscript uses the former, valid fact.
- **Loss of arithmetic topology:** arbitrary terminal residue cylinders
  and empty-word unit bisections are explicitly retained. The groupoid
  topology is not replaced by the coarser itinerary topology.
- **A null-set clock choice:** exact Borel branch scaling and the unique
  full-support continuous version fix null-state clock values. This is
  stronger than specifying an almost-everywhere derivative alone.
- **Inflated stabilizers:** no source translations or unrestricted affine
  ratios are adjoined. The zero state at H_p has only the actual retained
  lag group; it does not acquire the clock group of all rational scalings.
- **Atomic pushforward confusion:** an itinerary measure may have atoms
  because entire non-atomic arithmetic fibres have been mapped to points.
  The manuscript does not transfer those atoms back to Y.
- **Naturalness overclaim:** Haar is unique under an added source condition,
  not selected by T symmetry, and generic predicate encodability survives.
  The positive packet theorem establishes no necessity of the entire scan,
  escape, reset or real-extension architecture.

No blocking or nonblocking mathematical revision is requested. The
appropriate disposition is **scoped advance of the full arithmetic-source,
index-clock and packet construction; stop natural-A0 promotion / fork**.
The abstract packet R/(log p)Z is not claimed to embed as a Hausdorff
circle in a coarse quotient. Coarse topology, T3 and Route B were not
extended or evaluated.

The reviewer and root share the inherited model and project context.
A bounded auxiliary reviewer checked raw-card branch/Haar formulas;
it used the same model and did not review the full period classification.
Raw derivation preceded manuscript reading, but subsequent comparison
and root communications were not blind. This is internal corroboration,
not external peer review, formal verification or an independence guarantee.
