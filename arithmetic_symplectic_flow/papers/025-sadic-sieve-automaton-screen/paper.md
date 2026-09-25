# A non-stationary S-adic sieve automaton retains the symbolic seed but not an A1 carrier

**Paper ID:** `025-sadic-sieve-automaton-screen`  
**Record ID:** `ASFS-SCOUT-20260914-19`  
**Date / status:** `2026-09-14; PRE-P0 STOP — NONSTATIONARY FRONTIER; RECURRENT CARRIER NOT ESTABLISHED`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Question and source boundary

Can the reported non-stationary S-adic automaton for the sieve of Eratosthenes
provide a new carrier that retains the project's required lineage while escaping
the advancing-stage obstruction found for primorial gap recursion?

The answer at this screen is **no on the documented operational carrier**.  The
source is valuable because it begins with prime/composite observables and
constructs symbolic dynamics through three named operations on a growing tape.
It therefore realizes the first two arrows of the required lineage:

```text
prime/composite sieve -> symbolic admissibility on a tape -> sequential S-adic deformation.
```

It does not yet define the later arrows: a conservative Hénon-type lift, a
specific symplectic map, or its suspension.  This conclusion is deliberately
narrow: the screened source is a recent unrefereed preprint and its PDF was
not accessible in this audit.  Only the source's abstract-level description is
used; no claimed numerical or number-theoretic result is accepted here.

## Frozen screen and decisive test

Let `w` denote the source's current symbolic tape and let `j` count completed
applications of its documented full update (shift, expansion, filtering).  The
faithful operational state is `(w,j)`.  Since the source presents those updates
as a sequential, non-stationary evolution of a growing tape, its update map
has the form

```text
(w,j) -> (U_j(w),j+1).
```

Thus `L(w,j)=j` is strictly increasing.  By the elementary monotone-frontier
lemma in [018](../018-monotone-sieve-clock-obstruction/paper.md), this state
carrier has no periodic point: a purported period `r>0` would imply both
`L(U^r(w,j))=j+r` and `L(U^r(w,j))=L(w,j)`.

That result does **not** say that every abstract S-adic completion has no
periodic point.  It says precisely that a completion which retains the
chronological update count as an operational state cannot use its own periodic
states as the desired A1 ledger.  Forgetting `j`, taking a quotient, or selecting
a finite stage changes the owner of the prime mechanism unless a new proof
shows that the sieve rule descends and remains endogenous.  No such recurrent
carrier is supplied here.

## Same-object audit

| Required item | Owner in this screen | Result |
| --- | --- | --- |
| Arithmetic mechanism | sequential symbolic sieve update | retained lineage control |
| Symbolic coding | the source tape itself | source-described |
| Recurrent carrier | none preserving the stated update frontier | OPEN / not established |
| Symplectic base and roof | none | P0 unavailable |
| Primitive closed orbits / repetitions | none for the same carrier | A1 unavailable |
| Operator, zeta, trace | none | A2 unavailable |

No symbolic clock, geometric flow, or analytic operator was borrowed from any
other paper.  The same-object ledger therefore remains intact by stopping
before P0 rather than assembling a hybrid candidate.

## Controls and decision

The screen uses two controls.  First, it distinguishes a genuine symbolic
sieve source from generic geometry: unlike an arbitrary cat map or arithmetic
trace formula, the source starts from sieve evolution.  Second, it applies the
same strict-frontier test already used on the exact primorial-gap recursion,
instead of treating a new alphabet or substitution matrix as evidence of
recurrence.

**Portfolio decision: fork.** Retain this object as a symbolic positive
control and move to candidates with a mathematically defined recurrent global
state—not merely a finite stage, a quotient that forgets the sieve frontier,
or a time-dependent fitting schedule.  A future revisit must first supply a
precise recurrent quotient/inverse-limit construction and prove that its
periodic-orbit convention still owns the source's endogenous prime mechanism.

## Evidence index

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary and provenance](evidence/README.md)
- [Strict-frontier stop rule](../018-monotone-sieve-clock-obstruction/paper.md)
