# Prime-Fibonacci recurrence: an internal least-factor rule with a terminal, not recurrent, carrier

**Paper ID:** 083-prime-fibonacci-termination-screen  
**Record ID:** ASFS-SCOUT-20260914-56  
**Date / status:** 2026-09-14; NEGATIVE A1 SCREEN  
**Route state:** No formal ASFS Route-A coordinate; Route B NOT INVOKED.

## Abstract

This record screens the prime-Fibonacci recurrence of Alm and Herald.  For a
pair of positive integers, it replaces the next Fibonacci sum by its smallest
odd prime divisor, when one exists.  This is a fixed, endogenous
prime-factor-based deformation of a second-order symbolic recurrence and is
therefore a legitimate direct-lineage A0 control.  The source proves that all
forward sequences terminate at a power of two.  On the exact partial-action
carrier this excludes every forward closed orbit, hence any primitive-orbit or
repetition ledger.  No roof, suspension, determinant, symplectic carrier, or
Route coordinate is imported to circumvent that result.

## 1. Frozen object and ownership ledger

Let

\[
q(n)=\min\{p\geq3:p\text{ prime and }p\mid n\}.
\]

It is defined for precisely those positive integers that are not powers of
two.  The frozen partial update is

\[
T(x,y)=(y,q(x+y)),\qquad (x,y)\in D,
\]

where (D) and the terminal boundary (B) are specified in the
[candidate card](candidate-card.md).

| Item | Frozen owner | Status |
| --- | --- | --- |
| Arithmetic source | least odd prime factor of the current recurrence sum | internal to (T) |
| Symbolic lineage | prime/composite observable -> second-order recurrence deformation | established control only |
| Phase space / symplectic base | none | NOT SUPPLIED |
| Orbit convention | directed iterates of the same partial (T) until (B) | exact, terminal |
| Roof / suspension | none | NOT SUPPLIED |
| Zeta / operator | none | NOT SUPPLIED |

The construction is not a symplectic map: it is discrete, partial, and has no
claimed inverse.  Its terminal boundary belongs to the same object and cannot
be deleted or replaced by arbitrary return arrows.

## 2. Result

Alm and Herald prove that every positive prime-Fibonacci sequence terminates in
a power of two.  Equivalently, for every positive starting pair, some forward
iterate reaches (B), where (q(x+y)) is undefined.

If a point of (D) were periodic under this same partial action, all its
forward iterates would be defined and would remain in its finite cycle.  This
contradicts termination.  Thus the exact result is

\[
\operatorname{Per}(T)=\varnothing
\]

on the faithful forward carrier.  In particular there are no primitive closed
orbits and no repetition law of the kind required at A1.

## 3. Controls and scope boundary

- **Lineage control.** Unlike an imported arithmetic flow, the prime-factor
  test acts directly on the recurrence state; it realizes only the
  prime-symbolic/autonomous-deformation portion of the stipulated lineage.
- **Terminal-state control.** Treating (B) as a fixed point or adding a
  reset map would change the frozen action.  It would be a new candidate, not
  a repair of this one.
- **Comparison with 078.** The GPF-Fibonacci rule has a source-proved unique
  four-cycle.  This least-odd-factor rule has a source-proved terminal boundary.
  Their different recurrence rules and carrier behavior must not be combined.
- **Geometry control.** A post hoc Hénon, symplectic, or natural-extension
  carrier would need a new P0 card and a direct ownership relation; none is
  supplied here.

## 4. Gate assessment and decision

| Gate | Evidence for this exact object | Status |
| --- | --- | --- |
| A0 | fixed endogenous least-odd-prime-factor observable in a direct recurrence deformation | symbolic positive control only |
| A1 | universal termination at (B) implies no periodic point | scoped FAIL |
| A2 | no A1 ledger, roof, or analytic owner | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.**  This closes the smallest-factor
terminal branch without making a general claim about prime-factor recurrences.
The next broad screen should seek a fixed recurrence with a proven full
nonterminal periodic ledger, while rejecting any reset, modulus, or seed that
is externally supplied.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Alm--Herald source record](evidence/README.md)
- [077 subprime-Fibonacci contrast](../077-subprime-fibonacci-a0-a1-control/paper.md)
- [078 GPF-Fibonacci contrast](../078-gpf-fibonacci-a0-a1-control/paper.md)
