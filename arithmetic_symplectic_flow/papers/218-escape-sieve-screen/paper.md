# Escape labels become composite fixed orbits before they can escape

**Paper ID:** 218-escape-sieve-screen  
**Candidate ID:** ASFS-SCOUT-20260918-ERF01  
**Date:** 2026-09-18  
**Status:** PRE-P0 STOP — ABSORBING ESCAPE IS A COMPOSITE FIXED ORBIT; STATIC n ALSO FAILS ENDOGENOUS A0.  
**Evidence:** exact symbolic countercheck; no numerical experiment.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The frozen escape-gated sieve scan tries to make prime states close after
testing divisors up to the square root, while composites enter an absorbing
escape label. The local scan distinguishes the two arithmetic cases: primes
reach \(C_n\), composites reach \(E_n\). But the frozen rule sets
\(T(E_n)=E_n\), so every composite produces a primitive fixed orbit at its
escape label. Deleting those states or replacing them by a nonreturning
counter would change the carrier and requires a new card. Independently,
\(n\) is a static component label, so the rule has no endogenous generator
for the integer being tested. The screen stops before P0.

## 1. Frozen rule and lineage

The [card](candidate-card.md) was frozen before this exact check. Its state
set contains \(S(n,d)\) for every \(n\ge2,d\ge2\), together with \(C_n,E_n\).
The single deterministic map is

\[
\begin{aligned}
T(S(n,d))&=S(n,d+1)&&\text{if }d^2\le n,\ d\nmid n,\\
T(S(n,d))&=E_n&&\text{if }d^2\le n,\ d\mid n,\\
T(S(n,d))&=C_n&&\text{if }d^2>n,\\
T(C_n)&=S(n,2),\qquad&T(E_n)&=E_n.
\end{aligned}
\tag{1}
\]

The lineage is

\`\`\`
prime/composite observable
 -> divisor-admissible scan symbols
 -> sequential closure/escape update
 -> proposed return packets.
\`\`\`

This is a symbolic source screen only. It supplies no positive roof, mapping
torus, Hénon map, symplectic form, transfer operator or determinant. The
static integer label \(n\) is preserved by \(T\); no state in (1) generates
the next integer.

## 2. Exact scan dichotomy

If \(n\) is prime, every tested \(d\) with \(d^2\le n\) is a nondivisor.
The scan therefore increments \(d\) until the first \(d^2>n\), reaches
\(C_n\), and then returns to \(S(n,2)\). The \(d\)-coordinate is strictly
increasing before the closure state, so this is a least cycle.

If \(n\) is composite, let \(d\) be its least prime divisor. Then
\(2\le d\le\sqrt n\), and every \(2\le j<d\) fails to divide \(n\).
The scan reaches \(S(n,d)\) and then \(E_n\). Thus the local arithmetic
readout is exact: primes close and composites reach the designated label.

## 3. Decisive stop

For every composite \(n\), equation (1) gives \(T(E_n)=E_n\). Hence \(E_n\)
is a period-one orbit in the same carrier, not an escaping state. For
example \(4\) reaches \(E_4\) at \(d=2\), and then remains there; this is
an illustration, not a finite-census proof.

Removing \(E_n\), replacing it with an unbounded counter \(E(n,j)\), or
declaring escape labels outside the state space changes the frozen object.
None is an in-place repair. A new card would need a new carrier, positive
clock and complete orbit convention.

## 4. Independent A0 ownership failure

Even if a future card replaces the fixed escape state by genuine
nonreturning motion, the current rule stores \(n\) as a static component
label. The same \(T\) acts independently on each \(n\)-fibre and never
generates a new integer from a prior state. The divisor predicate is
internal to each update, but the integer being tested is externally present.
This is a scoped endogenous-A0 failure, not a universal no-go theorem.

## 5. Decision

| Gate | Evidence | Status |
| --- | --- | --- |
| Pre-P0 object | Exact symbolic rule in the frozen card | Defined only as a screen |
| Arithmetic readout | Prime scans close; composite scans reach \(E_n\) | Exact local dichotomy |
| Primitive packets | \(E_n\) is fixed for every composite | Prime-only ledger fails |
| Endogenous A0 | \(n\) is a static invariant label | Scoped FAIL before P0 |
| A1/A2 / geometry | No positive roof, flow or symplectic owner | NOT EVALUATED |
| Formal Route / B | No evaluation | UNASSIGNED / NOT INVOKED |

**Decision: STOP before P0 and FORK.** A successor must make escape truly
nonperiodic and must generate the integer/source state under the same rule.
Either change requires a fresh candidate ID. A later geometric lift cannot
rescue (1) by selecting only the \(C_n\) states.

## Evidence and limitations

The proof uses only the frozen all-integer rule and the least-prime-divisor
fact. It contains no numerical run, external theorem, prime table, fitted
roof, zero data, operator, determinant or geometric construction. This is a
Pre-P0 negative screen, not a Route result or a universal no-go theorem.
