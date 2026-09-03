# Hostile stochastic/graph review — P179

**Reviewer process:** Reviewer B, stochastic/graph lane, reopened against corrected author Round 2.  
**Review mode:** read-only; no author file was modified.  
**Reviewed `main.tex` SHA-256:**
`94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6`.  
**Reviewed PDF SHA-256:**
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

## Independent representation and evidence

The reviewer used canonical tuples of disjoint integer bit masks for set
partitions, not restricted-growth words.  All labelled histories were
generated literally.  Their endpoint counts were compared target by target
with a separately coded admissible-missing-set predicate implementing the
two blockwise cases in the theorem.  Rational ranks of the integer matrix
`nP-sI` checked geometric multiplicities, while forward arrow aggregation
kept distinct predecessor states separate from labelled predecessor/action
pairs.

The run contains **209,583 assertions** and fixes the independent arrow
digest as
`7985611dd473fe4a7677d1ba0088ca8ce43de0d4a66958b20e9859a2ff316fa1`.
It covers commuting idempotents and both inverse censuses through `n=8`,
rational eigenspaces through `n=5`, every source, every target, and
`t=0,...,5` through `n=5`, and the compressed absorption law for every
source through `n=6` and `t=0,...,4`.

The retained Round-1 delta explicitly fixes `n>=1` and subtracts P169/P110.  Direct
inspection confirms that P169 is a deterministic maximum-to-successor
transfer on canonically ordered blocks and preserves block count, whereas
P110 joins a partition with its cyclic translate and coarsens it.  Neither
has the support-only singleton-refinement update or the present coupon/kernel
atlas.  The new subtraction is technically consistent and claims no credit
for their shared carrier.

Round 2 corrects the support lemma so that the residual block `B\A` is
retained whenever it is nonempty, including when it has one label.  Three
fresh reviewer processes run after the final Round-2 byte binding reproduced
`CANONICAL.txt` exactly (`PASS/PASS/PASS`).  A read-only author replay also
reproduced the expanded **252,320-assertion** author transcript.

## Claim-by-claim proof audit

| claim under attack | hostile check | result |
|---|---|---|
| commuting idempotents | extracting two labels leaves the same residual block in either order, including labels initially in one block | pass |
| diagonal spectrum | the commuting idempotents split over `Q`; a refinement order is triangular and its diagonal is `s(pi)/n` | pass |
| multiplicities and absent layer | choosing the singleton labels leaves a singleton-free partition; `n-1` singleton blocks force the last one to be singleton too | pass |
| absorption law | absorption is exactly “at most one missing label per old block”; size-`m` admissible missing sets are counted by `e_m(b_1,...,b_k)` | pass |
| every-target kernel | exact supports are disjoint events; inside an old block they leave either one specified nonsingleton residual or a residual of size at most one | pass |
| time support condition | `r! S(t,r)>0` exactly for `r=0=t` or `1<=r<=t` | pass |
| distinct predecessors | unchanged target, singleton–nonsingleton merges, and unordered singleton–singleton merges are disjoint | pass |
| labelled action pairs | choosing the output singleton and then one of all `b` predecessor placements gives `sb`; a two-singleton merge correctly carries two labels | pass |

## Boundary audit

At `t=0`, only the missing set `[n]` contributes, so the kernel is the
identity even when several structural missing sets lead to the same eventual
target.  At `n=1`, the only partition is already absorbed, the spectrum is
`{1}`, and both the distinct-predecessor and labelled-action counts equal
one.  The corrected support lemma also covers the fragile case in which all
but one labels of an old block were observed: the one unobserved label remains
as a singleton residual, so the resulting restriction is discrete.  This is
exactly alternative (b), `|M intersect B|<=1`, in the target-kernel theorem.
The verifier tests these cases explicitly.  It also confirms that the
seemingly similar quantities

\[
1+s(b-s)+\binom{s}{2}
\quad\text{and}\quad sb
\]

are counts on different sample spaces and must not be conflated.

## Round-2 delta disposition, ownership, and kill switches

The intervening prose mismatch is repaired: `main.tex:92-104` now retains
every nonempty residual block and explicitly names the singleton case.  The
literal update and all downstream absorption/kernel formulas already had
this behavior, so no formula changed.  No Critical, Major, or Minor defect
remains in the corrected Round-2 theorem package; disposition is
`CLOSED / 0 OPEN FINDINGS`.

This is not owner clearance.  Partition lattices, singleton extraction,
coupon support, associated Bell numbers, and commuting-idempotent spectral
machinery remain explicitly subtracted.  A direct owner for the literal
chain with its full kernel/inverse atlas, an overlap among supposedly
disjoint exact-support events, or a confusion between predecessor states and
action-labelled predecessors would reopen review.  `OWNER_AMBER /
HOLD_EXTERNAL` remains unchanged.
