# Intrinsic pruning would solve the ownership problem, but not the sieve admissibility problem

**Paper ID:** `013-intrinsic-pruning-admission-screen`  
**Record ID:** `ASFS-SCOUT-20260913-11`  
**Date / status:** `2026-09-13; PRE-P0 NEGATIVE SCREEN`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Abstract

The Phase-I route from prime sieve words through Logistic kneading to an
area-preserving Hénon lift suggests a more serious alternative to record 012:
make the desired language an intrinsic pruning/kneading invariant of one
specified Hénon-type map.  This would give the language a geometric owner and
could, in principle, retain ordinary periodic orbits.  It cannot be admitted
here. The input sieve-stage words have documented finite MSS admissibility
failures, and the later apparent restoration concerns only finite
valid-horizon words (conditionally or numerically). Thus they do not provide
the needed established infinite kneading input from which a map parameter could
be derived. Choosing a parameter while overlooking that gap merely reintroduces
external arithmetic selection. This is a negative pre-P0 result, not a claim
about all pruning models.

## 1. Lineage and prospective object

The exact retained lineage is

```text
prime/composite sieve observables
  -> sieve-stage symbolic words and MSS admissibility
  -> Logistic-type kneading prototype
  -> Hénon-type area-preserving lift via intrinsic pruning
  -> later symplectic suspension, only if a map is actually frozen.
```

The first two arrows are the specific Phase-I material.  The final arrows are
only a proposed geometric lift.  No phase space, symplectic form, map, roof,
mapping torus, primitive-orbit convention, or determinant is frozen: therefore
there is no same-object candidate to assess.

## 2. The distinction from record 012

A full horseshoe plus an externally chosen sieve subshift has two owners: the
map owns its full language, while an arithmetic rule owns the retained words.
Record 012 rejects that construction.  By contrast, a genuine pruning front or
kneading invariant changes the allowable language of the particular map.  That
would resolve the ownership defect *if* the proposed sieve language were an
admissible invariant and were obtained without manual prime-indexed choices.

This distinction is methodological only.  It supplies neither a parameter nor
an arithmetic mechanism by itself.

## 3. Admission test

The source constraint is decisive but more nuanced than a universal
impossibility claim. The local prior-work record reports finite-stage
parity/MSS failures (including the stage-3 and stage-5 defects), alongside an
eventual-admissibility programme for later *finite valid-horizon* words. The
latter is conditional on strong gap information or supported by finite
experiments; it is not a proof that one infinite sieve word is a kneading
invariant of an autonomous map. A construction cannot freeze a parameter by
silently treating either the early defects or the finite-to-infinite gap as
resolved. Nor may it truncate to a convenient finite word and repeat it: that
produces a manually chosen periodic language and loses the claimed prime
mechanism.

Consequently the candidate fails before P0, not because pruning theory is
invalid, but because this precise arithmetic input cannot yet discharge the
infinite/adaptive admissibility prerequisite.

## 4. Controls and nonclaims

- **Ownership control:** intrinsic pruning would be acceptable in principle;
  exogenous subshift filtering is not.
- **Arithmetic control:** an arbitrary admissible kneading word, even one that
  looks irregular, is not evidence of a prime mechanism.
- **Finite-truncation control:** a periodic approximation neither represents
  the sieve process nor supplies a global A0 clock.
- **Cross-object control:** no determinant, orbit formula, or operator from
  the Logistic, Hénon, or arithmetic-flow controls is attached to this screen.

No general impossibility theorem for prime-related Hénon maps is claimed.

## 5. Gate assessment and decision

| Gate | Evidence for this screen | Status | Decision |
| --- | --- | --- | --- |
| P0 | no admissible, endogenous parameter rule; no map frozen | not admitted | stop this object |
| A0 | no object exists | NOT EVALUATED | do not infer a pass from the source words |
| A1 | no object exists | NOT EVALUATED | do not borrow horseshoe periodic orbits |
| A2 | no object exists | NOT EVALUATED | unassigned |
| Route B | no Route-A-ready candidate | NOT INVOKED | prohibited |

The next admissible fork may instead construct a genuinely nonautonomous
kneading/pruning theory that owns the changing valid horizon and proves its
compatibility with one specified conservative map. Alternatively it must
present a different prime-symbolic generator whose allowed language is proved
intrinsic to a specified map. It receives no credit from this screen.

## Evidence index

- [Candidate scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and provenance](evidence/README.md)
- [Phase-I prior-work index](../../docs/prior_work/README.md), especially
  the sieve/MSS and Hénon-bridge papers.
