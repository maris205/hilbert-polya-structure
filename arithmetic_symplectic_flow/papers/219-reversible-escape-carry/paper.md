# Endogenous escape-carry: a bounded return screen

**Paper ID:** `219-reversible-escape-carry`  
**Candidate ID:** `ASFS-SCOUT-20260918-REC01`  
**Date/status:** 2026-09-18; `PRE-P0 STOP — NONINVERTIBLE RESET AND SQRT-SCALE PRIME CLOCK`.  
**Evidence class:** exact case analysis of the frozen rule; no numerical search.

## Question and lineage

Can a divisor scan avoid 218's two failures by (i) updating its integer label
on a divisor hit and (ii) sending the hit to a genuine, nonfixed escape phase?
The proposed source is still the prior-work arrow

\[
\text{divisor admissibility}\to\text{sequential symbolic scan}\to
\text{conservative/reversible carrier test}.
\]

The object is intentionally only a discrete Pre-P0 screen. It does not claim
that a noninvertible map is symplectic, and it supplies no roof, suspension,
operator, or determinant.

## Exact rule

The carrier and four branches are exactly those in the [frozen card](candidate-card.md).
All integer arithmetic is ordinary divisibility; `k` is an unbounded integer
counter. No prime list or logarithmic value is supplied.

## Decisive checks

### The escape is genuinely moving

Whenever a divisor is encountered, the second branch changes `n` to `n+d` and
increments `k`; the next escape branch changes `n` once more and resets the
scan. Thus the absorbing fixed state `E_n` from 218 is absent. A state at a
composite `n` cannot return to that pre-hit state because both `n` and `k`
have increased. The later trajectory may nevertheless land on a prime reset
cycle (for example, `(4,2,0,0) -> (6,3,1,1) -> (7,2,1,0)`), so this is not a
claim that every hit escapes forever. It is only an exact positive result for
the narrow ``moving escape'' diagnostic, not an A0 pass.

### The reset is not injective

For any fixed `n` and `k`, every state `(n,d,k,0)` with `d^2>n` is sent to the
same `(n,2,k,0)`. For example, both `(5,3,0,0)` and `(5,4,0,0)` have the same
image. Hence `T` has no inverse on the frozen full carrier. A finite-
dimensional symplectic base map, and therefore the requested classical
suspension owner, cannot be obtained from this exact rule without changing the
candidate and recording the discarded scan phase.

### Prime returns do not carry a logarithmic clock

If `n=p` is prime and the scan starts at `d=2`, no divisor branch occurs before
the first `d` with `d^2>p`. The reset then returns to `d=2`. The clean scan
cycle therefore has unit-step length

\[
 m(p)=\min\{d\ge2:d^2>p\}-1=\lfloor\sqrt p\rfloor,
\]

up to the displayed phase convention. The rule contains no scale variable
from which `m(p)` could become `log p`; a unit roof would retain the
square-root clock, while inserting `log p` would violate the permitted-data
rule. This is an early A1 clock failure even before a primitive packet could
be transferred to geometry.

### Composite hit states do not rescue the packet

Every composite `n` has a divisor `d<=sqrt(n)`, so a scan from `d=2` reaches
the hit branch and strictly increases `k`. Such a state cannot be periodic
under the full map, although it can subsequently enter a prime-like cycle at
a larger `n`. For each prime `p`, the full states with a fixed `k` and the
scan phases through the first `d` with `d^2>p` form one clean cycle; varying
`k` gives countably many copies of that discrete prime cycle. This removes
the fixed composite orbit of 218, but leaves prime-like reset cycles with the
wrong clock and a noninvertible carrier; it does not establish a prime packet
for a symplectic flow.

## Gate assessment and decision

| Gate | Result | Reason |
| --- | --- | --- |
| Lineage / source | partial positive | current divisibility drives the branches; no prime table |
| P0 same-object owner | fail | `T` is many-to-one; no symplectic base or positive roof |
| A0 | `NOT_TESTABLE` as a flow | arithmetic update exists, but no owned geometric carrier |
| A1 | pre-A1 scoped fail | under the frozen unit-step screen, the prime scan period is `floor(sqrt p)`; no geometric roof is supplied |
| A2 | not evaluated | no operator or determinant |

**Decision:** stop this exact screen and fork only to a new reversible carrier
that retains the discarded reset phase. Adding such a history register is not
a repair under this ID; it must pass a fresh recurrence and packet audit. The
stronger ordered-cover candidates 163/169 remain separate positive engineering
controls, with their own source/scale naturalness question.

## Same-object and integrity boundaries

No symbolic clock, physical flow, determinant, or operator was imported. The
only positive result is the exact moving-escape observation. No Route-A
coordinate is assigned and Route B is not invoked.
