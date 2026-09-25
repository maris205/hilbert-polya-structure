# Breadth-first architecture screen: modular, Hecke, and Frobenius proposals

**Paper ID:** `002-architecture-scouting-cycle-01`  
**Candidate ID:** `NONE — pre-P0 scouting record`  
**Date / status:** `2026-09-13; INCONCLUSIVE SCREEN / NO ADMISSION`  
**Route state:** `UNASSIGNED; Route B NOT INVOKED`

## Abstract

This first breadth-first screen compares three ways arithmetic might meet a
symplectic suspension flow. Modular geodesic dynamics has unusually strong
primitive-orbit geometry, but the exact P0 return map and an endogenous varying
prime mechanism are not jointly supplied. Hecke operators furnish prime-indexed
arithmetic structure, but are correspondences rather than one deterministic
symplectic base map. Fixed-characteristic Frobenius naturally produces powers
of one fixed prime, not the family of rational primes required for A0. None is
admitted as a candidate; the result is a short portfolio decision, not a
negative theorem about the underlying theories.

## 1. Scope and one-object boundary

This paper owns no mathematical candidate. Its scope card is
[candidate-card.md](candidate-card.md). Consequently, no orbit convention,
roof, transfer operator, determinant, trace, or formal Route coordinate can be
inferred. The aim is to prevent expensive work on architectures that already
fail a type or ownership requirement.

## 2. Screening question and test

For each family ask four pre-admission questions:

1. Can one state a concrete symplectic map \(F\) and one positive roof \(\tau\)?
2. Is an arithmetic mechanism endogenous and capable of varying over rational
   primes without a supplied prime list?
3. Does the same construction naturally own primitive closed orbits and their
   repetitions?
4. Is the arithmetic object a deterministic map, rather than a correspondence
   or separately indexed family?

Failure of any question means `do not admit to P0 yet`, rather than attempting
to repair the architecture with a borrowed object.

## 3. Family screen

| Family | Attractive feature | Decisive early obstacle | Portfolio decision |
| --- | --- | --- | --- |
| Modular geodesic return dynamics | Closed geodesics correspond to hyperbolic conjugacy classes; their lengths obey \(2\cosh(\ell/2)=|\operatorname{tr}\gamma|\). A two-dimensional return-section tradition exists. | This screen does not yet freeze the exact section/return map/roof, and the length spectrum is indexed by integral traces or quadratic units, not internally by rational primes. | `HOLD AS A1 BENCHMARK; NOT ADMITTED TO P0` |
| Hecke-enhanced modular geometry | Hecke structure is canonically indexed by primes and is genuinely arithmetic. | At fixed level it is a family of finite étale correspondences/double cosets, not a single-valued fixed base map \(F\). Combining it with a different geodesic flow violates the one-object rule. | `REJECT AS DIRECT P0 FIT` |
| Fixed-characteristic Frobenius | The characteristic \(p\) and powers \(p^n\) can be intrinsic, and Frobenius is a map. | It privileges one fixed characteristic; changing \(p\) changes the object. It cannot provide a single-object varying-prime A0 mechanism without an external family/selector. | `REJECT AS A0 FIT` |

The modular direction remains conceptually useful because it demonstrates what
strong A1 geometry looks like. It is not rescued by calling primitive geodesics
“primes”: primitivity is an orbit convention, whereas A0 requires an
endogenous rational-prime relation.

## 4. Adverse controls

| Control | Result |
| --- | --- |
| Same-object control | A modular flow plus a Hecke correspondence would have distinct owners; no mixed candidate is formed. |
| Prime-label control | Replacing prime labels by all traces, all integers, or quadratic-unit labels changes the claimed arithmetic statement; no intrinsic selection was found. |
| Family-versus-map control | A family indexed by \(p\) is not a single \(F\); encoding the family into one map would require a new construction, not notation. |
| `PROVES_TOO_MUCH` control | Calling every primitive orbit a “prime” produces a prime-like analogy for many nonarithmetic flows and therefore cannot establish A0. |

## 5. Gate assessment and decision

| Gate | Status | Reason |
| --- | --- | --- |
| P0 | `NO ADMISSION` | No screened family presently supplies all required frozen owners. |
| A0 | `NOT EVALUATED` | No P0 candidate exists; the architecture obstacles are recorded instead. |
| A1 | `NOT EVALUATED` | Modular geometry is a benchmark, not a credited candidate. |
| A2 / formal Route A | `UNASSIGNED` | No analytic object or formal evaluation. |
| Route B | `NOT INVOKED` | No Route-A readiness. |

**Portfolio decision:** `fork`. Keep searching for a construction in which the
prime-varying arithmetic mechanism is internal to one deterministic symplectic
map and its roof, while retaining an A1-quality primitive-orbit owner. Do not
deepen any of the three screened families without a new P0 card that resolves
its stated obstacle.
