# Clock-scope review — ANG-20260915-DDC01

**Date:** 2026-09-15.  
**Candidate status:** STOP PROMOTION — EXACT MARKED RETURNS; BATCH CLOCK NOT GEOMETRICALLY JUSTIFIED.  
**Review type:** independent model scope and ownership audit, not external peer review or a formal Route evaluation.

## Reviewed inputs and limits

Reviewed the [frozen version-1 card](../candidate-card.md), the exact-return
and clock sections of the [paper](../paper.md), its
[claim ledger](../claim-ledger.md), the controlling
[plan, especially A0 and the same-object ledger](../../../plan.md),
[AGENTS](../../../AGENTS.md), and the earlier
[all-integer carrier-scope distinction](../../140-cyclic-divisor-counter/evidence/carrier-scope-audit.md).
This report independently checks the scope of the arithmetic and timing
claims. It does not certify the complete analytic proof or finite evidence.

## Operational arithmetic and a valid frozen macroclock

The action includes every integer n >= 2, every prescribed batch phase, and
every modular counter. Its dyadic blocks process the proper-divisor
witnesses once per phase cycle. Consequently the full-cycle increment is
the actual proper-divisor count a(n), with 0 <= a(n) <= n-2 < n. Reduction
modulo n cannot hide a nonzero count. Zero increment therefore recognizes
primes inside the action, not through an externally supplied completed
prime word. Suppressing increments selects every n; replacing them by
block cardinalities gives total increment n-2 and selects only n=2.
These controls distinguish the arithmetic return from the phase geometry
alone.

The unit roof was frozen for this new macro-action before its results.
It is not a substituted clock on the unchanged serial action of 140.
Using an all-integer binary partition is also not literally the forbidden
manual assignment of a roof T_p = log p on a selected prime family.
The resulting elapsed time is a genuine mathematical suspension clock.
Its increasingly large block operations are not asserted to have constant
cost on a sequential machine.

## What the logarithmic comparison does and does not establish

The complete packet formula is T(n)=K_n n/g(n), where
g(n)=gcd(n,a(n)). A prime p consequently owns p primitive packets, each of
length K_p, and

\[
K_p=\frac{\log p}{\log 2}+O(1),\qquad
\frac{K_p}{\log p}\longrightarrow\frac1{\log 2}.
\]

Thus the frozen unit-roof system has a logarithmic-order prime macroperiod.
It does not have ratio-one asymptotics to the natural logarithm in its
current units, nor exact log p lengths. Multiplying this comparison by
log 2 must not silently change the roof.

The binary block schedule supplies the logarithmic scale; the arithmetic
witnesses determine whether additional phase cycles are required. Serial
scanning and other fixed blocking schedules are different owners, so their
different times do not invalidate this action's clock or establish an
ownership violation. They do show that a canonical arithmetic, geometric,
or physical reason for choosing these macrotime units has not been given.
Generic bounded-witness algorithms remain a naturalness control, without
negating this particular proved arithmetic return.

No new requirement of a unique canonical geometry is added to A0 by this
audit. Conversely, the card's explicit clock-promotion boundary must be
respected: valid operational timing cannot alone certify the stronger
natural prime-log interpretation.

Recommended scoped wording is: **T1 operational marked arithmetic return
established; logarithmic macroperiod established; canonical arithmetic or
geometric timing origin OPEN.** The package's STOP PROMOTION decision
applies to the stronger interpretation, not to the existence of its action,
return selector, or macroclock. It is neither an unconditional T1 pass nor
a finding that all its arithmetic is external.

## Bounded geometric fork and nontransfer boundary

The current user authorization for candidate engineering permits the fresh
[144 geometric card](../../144-dyadic-counter-henon-lift/candidate-card.md)
to ask a distinct, bounded question: can a positive-dimensional symplectic
owner retain this complete finite-packet convention, multiplicity,
primitive periods, and unit macro-roof? This review supplies no additional
authority beyond that existing request and grants no gate credit.

Such a fork is justified by a concrete arithmetic-return mechanism and an
explicit ledger, not by an assumption that every earlier obligation has
already passed. The new owner must prove its geometry and full intrinsic
periodic set anew; selecting centres from a continuum would fail the stated
contract. Even an exact lift cannot by itself remove the prime multiplicity,
discard composite packets, establish a prime-power trace formula, or turn
schedule-selected logarithmic timing into a canonical arithmetic clock.

**Portfolio:** preserve 143's exact operational results, stop promotion of
the unsupported stronger clock interpretation, and permit the separately
frozen bounded geometric fork. No theorem, clock owner, or Route credit is
transferred. Formal Route coordinates remain UNASSIGNED; Route B is
NOT INVOKED.
