# CRN01 — original-card independent derivation

Candidate: ANG-20260923-CRN01. Internal same-model **NOT_CALIBRATED** review.
Result: all three prescribed Borel IMAGE/history owners exist. None has a
legal fixed point. Each has exactly one two-cycle entirely in the frozen
unit cell, namely `{1/sqrt(3),-1/sqrt(3)}`, with entire time group
`(log 16) Z`. Its positive primitive is `log 16`, not an ordinary-prime log.
This actual MAIN packet decisively gives **STOP / FORK** for the target.
No other cell or longer-period census is claimed.

## 1. Scientific input and provenance

Only `candidate-card.md`, original lines 1–96 through original EOF, was read
as scientific input: 96 lines, 5749 bytes, SHA-256
`6f2c412141bb7bd87945ad054e9d426f5c70a96a8771bb35cf155326814da4d9`.
That prefix was reread and rehashed after root's separate mathematical release.
The 86-line CP1 report remains unchanged. Retained ARS workflow/DA/runtime
instructions govern the stage boundaries. No author paper, README, ledger,
outcome, peer, sibling or old scientific source was read. No auxiliary, web,
scientific code, numerical experiment or model change was used. All proofs
below are exact derivations from this card, not transferred prior results.
Shared inherited history prevents blindness, independent-error, calibrated
confidence or external-peer-review claims. This raw must freeze before any
separate PAPER UNLOCK or manuscript comparison.

## 2. All-point domains and their terminal distinctions

Write `G,R` for an owner's coefficients at its actual source and
`P(z)=z^2-Rz+G`. All `G>=1`; MAIN/E have `G=gcd(a,b)`, while C has `G=1`.
MAIN/C use `R=r`, with `0<=r<=floor|Im z|`; E uses `R=0`.
The integer interface gives exactly the stated content/remainder values.
It restricts neither later readouts nor the full real two-dimensional source.

Every actual pole is zero. Indeed `2z=R` forces real `z`; then `b=1`,
the remainder is zero, and all three owners have `R=0,G=1`, hence `z=0`.
Conversely zero is a pole in each owner.

MAIN and C have no actual critical zeros of `P`. A real source has
`P=x^2+1!=0`. If `y!=0` and `P(x+iy)=0`, then
`x=R/2` and `y^2=G-R^2/4`. For `R>0`, MAIN's gcd divides the remainder,
so `G<=R`; C also has `G=1<=R`. But `R<=|y|` would give
`G=y^2+R^2/4 >=5R^2/4>R`, a contradiction. If `R=0`, then `x=0,a=1`,
`G=1` and `|y|=1`; these actual readouts give `b=2,r=1`, not `R=0`.
Thus `D_MAIN=D_C=C\{0}`, proved separately from the formal permission.
For E, `P=0` forces `z=±i sqrt(g)`; then `a=1` makes `g=1`.
Both `±i` have the required own readouts. Hence E's full terminal set is
`{0,i,-i}`, whereas MAIN/C's is `{0}`. In particular `±i` cannot be
discarded from MAIN/C by borrowing E's critical set.

## 3. Complete inverse sets, including Delta=0 and degeneracies

Fix a source cell and its own coefficients. For a legal predecessor of `w`,
cross-multiplication gives
`z^2-2wz+Rw-G=0`, equivalently `(z-w)^2=Delta(w)=w^2-Rw+G`.
Moreover `z-w=P(z)/(2z-R)`, which is nonzero on the actual legal domain.
Thus every legal predecessor has `Delta(w)!=0` and is exactly one of the
two frozen square-root expressions. Conversely a root passing its actual
cell, readout, permission and forward-equality tests is a predecessor.
This proves completeness; target next-step permission is not required.
`Delta` uses the candidate SOURCE coefficients, not a fresh target readout.
If `Delta=0`, the only quadratic root is `z=w` and has `P(z)=0` for that
same cell, so no legal source is omitted by the prescribed exclusion.

The coefficient degeneracy `R^2=4G` also causes no loss: its fixed-label
rational germ reduces to `(z+R/2)/2` away from `z=R/2`. The other algebraic
inverse root is that fixed-label branch's pole `R/2`; the nonconstant inverse
is `2w-R/2`, subject to all own cell tests. At `w=R/2` it too is the branch
pole. Neither cancellation nor an algebraic root overrides the actual
cell/domain checks; that geometric point may be legal under a different cell.

Each nonzero-discriminant square-root sign is Borel under the frozen Arg
choice. Exact inverse domains are the Borel sets satisfying all listed
tests. Each retained branch is injective because its actual forward image
recovers `w`. Different cell/sign presentations do not duplicate an actual
source, whose readouts and nonzero square-root sign are determined.
The union of these full sets is the exact image/predecessor predicate.
No surjectivity or principal-branch selection is assumed.

There is even a finite per-target bound, not a numerical cutoff. Put
`rho=|z|`, `s=|w|`. Since `R<=rho` and `G<=rho+1` for each owner, the
quadratic inverse equation gives `rho^2<=(3s+1)rho+1`, hence
`rho<=3s+2`. Only `1<=a,b<=1+floor(3s+2)` can occur, with at most two
roots per cell. Enumerating these exact bounds is equivalent to the full
all-integer prescription; no computation or orbit census was run.

For all three owners `Inv(0)={1,-1}`: `z^2=G>0` forces a real source,
then `b=1,G=1,R=0`. Both sources are legal, although the target is terminal.
E additionally has `Inv(i)={1+i,-1+i}` and
`Inv(-i)={1-i,-1-i}`. For example at target `i`, `Delta=G-1`; a possible
source has imaginary part one and thus `b=2,G in {1,2}`. `G=1` has
excluded zero discriminant; `G=2` gives the two stated legal sources with
`a=b=2`. Their source discriminant is one despite the target being E-critical.
All deeper terminal incoming is retained by the full recursion below.

## 4. Germ derivative and EVERY-Borel IMAGE

For fixed `G,R`, direct differentiation gives
`f'(z)=2P(z)/(2z-R)^2`, nonzero and finite on its own legal domain.
Implicit differentiation of the inverse quadratic gives
`theta'(w)=(2z-R)/(2(z-w))=(2z-R)^2/(2P(z))` at `z=theta(w)`.
Therefore the prescribed real-area density and legal clock are
`J_theta(w)=|2z-R|^4/(4|P(z)|^2)` and
`kappa(z)=log 4+2 log|P(z)|-4 log|2z-R|`.
Both expressions use the actual source's frozen coefficient germ. `J` is
strictly positive and finite at every assigned inverse point. A formal root
with vanishing inverse derivative is not legal; the displayed identity proves
this, including the degenerate coefficient case. Terminal step clocks remain
undefined, not arbitrarily completed with zero.

For each fixed coefficient, cover its noncritical, nonpole source by
countably many open disks where its rational germ is a smooth diffeomorphism.
Partition each actual injective inverse-source piece into disjoint Borel
subsets subordinate to this cover. Its target images are disjoint. Local
change of variables and countable additivity then prove
`mu(theta E)=integral_E J_theta dmu` for EVERY Borel actual inverse subset.
This includes assigned root cuts, signed floor boundaries and null sets;
global differentiability across a root cut or coefficient jump is unnecessary.
The frozen germ specifies null-point values, not an a.e.-uniqueness theorem.
The branch law is not a global measure-preservation assertion.
The argument applies separately with each owner's `G,R,D`.

## 5. Full actual groupoid, kernels and all source types

All legal iterate domains and maps are Borel. Actual triples form a Borel
subset of `X x Z x X` by their countable equal-iterate witness union.
Finite one-step preimages imply countable full source orbits. Two witnesses
for the same lag differ by a common increment in both exponents; extending
the shorter common future through that existing legal increment adds equal
clock sums. They cancel, proving descent of `c=S_a(z)-S_b(w)`.
Synchronizing legal middle histories proves composition/additivity. No
continuation through a terminal is invented. Countable witness selection
makes `c` Borel. The forward arrow has lag `-1` and clock `-kappa`.

Products of the prescribed finite-history germs give, on every actual branch
pair from `w` to `z`, IMAGE density `exp(S_b(w)-S_a(z))=exp(-c)`.
Iterated change of variables proves its every-Borel law. Equal triples have
equal clocks; different retained lags are not silently collapsed.
The full extension and unrestricted height translation thus descend to the
orbit SET, without a smooth or well-behaved measurable quotient claim.

The complete arrow kernels are
`K_lag={(z,0,w):T^r z=T^r w for some legal r}`,
`K_clock={(z,a-b,w):T^a z=T^b w, S_a(z)=S_b(w)}`, and their intersection.
At `±1`, every owner's step clock is zero. Thus `(1,0,-1)` is a nonunit
joint-kernel arrow, while `(0,-1,1)` is a zero-clock nonzero-lag arrow.
These do not create isotropy or a next-step clock at terminal zero.

A nonzero source-isotropy lag is equivalent to an eventual legal cycle.
For least eventual source period `p`, `Iso_z=p Z`; otherwise it is trivial,
including all histories that terminate. Put `K=sum_cycle kappa` over that
least cycle. On its entire basin `c(np)=nK`, `H_z=K Z`, and extension
isotropy is `{np:nK=0}`. When `K!=0`, the positive primitive is `|K|`,
not one selected step; when `K=0`, there is no positive physical return
although all source isotropy survives. Non-eventual histories have `H=0`.
This is a conditional full-source ledger, not a longer-period classification.

For exact incoming let `P_O` be the complete inverse set of §3 and iterate
it by unions, identifying actual points. The source orbit of `z` is exactly
`union_(a,b>=0, T^a z legal) P_O^b({T^a z})`; incoming arrows to range `z`
are `(z,a-b,w)` for `w` in those depth-`b` sets. Every cycle basin is
`union_(r>=0) P_O^r(cycle)`, with no unit-cell restriction.
Distinct eventual cycles cannot merge under a deterministic forward map.

On a cycle `v_j` with `T v_j=v_(j+1)`, put `A_j=sum_(i<j) kappa(v_i)`.
If `z` first reaches `v_j` in `r` steps, set
`lambda_z=r-j`, `b_z=S_r(z)-A_j`. ALL arrows between two basin points have
`k=lambda_z-lambda_w+np`, `c=b_z-b_w+nK`, for `n in Z`.
This determines all three kernels by the corresponding zero conditions and
the full height phase `h-b_z mod K Z`; `K=0` gives a real, not circular, phase.
On a terminal basin the first hitting depth `r_z` is unique, with
`k=r_z-r_w`, `c=S_(r_z)(z)-S_(r_w)(w)` and phase `h-S_(r_z)(z)`.
On an infinite non-eventual source orbit choose an anchor and an actual
arrow to each point. Its clock is unique because isotropy vanishes; subtract
that clock from `h` for the real phase. This is an orbitwise description,
not a claim of a global Borel transversal or Borel potential.

## 6. ALL fixed points and the ENTIRE unit-cell two-step test

On every legal source, `f(z)-z=-P(z)/(2z-R)!=0`. Consequently all THREE
owners have empty legal fixed sets on the full complex carrier. Terminal
identity arrows and formal critical fixed roots are not dynamical fixed points.

Within `C_11`, all owners have exactly `G=1,R=0`, so their own map is
`N(z)=(z^2-1)/(2z)`. If both legal steps stay in this cell, then
`z!=0`, `N(z)!=0`, and
`N^2(z)=(z^4-6z^2+1)/(4z(z^2-1))`.
The exact return equation becomes
`3z^4+2z^2-1=(3z^2-1)(z^2+1)=0`.
The roots `±i` lie outside the strict unit cell; no E-only terminal rule
is used to exclude them from MAIN/C. The remaining roots are exactly
`alpha=1/sqrt(3)` and `-alpha`. Both have own readouts `a=b=1`, are legal,
and map to each other. This is one least-source-period-two core, not a
fixed repeat or two separate cores. The polynomial factorization exhausts
the whole complex unit cell, not a real-only or numerical sample.

There `N'(±alpha)=2`, so each area's step Jacobian is four and each step
clock is `ell=log 4`. The once-around clock is `K=2ell=log 16`.
For each owner separately, on its ENTIRE incoming basin of this core,
`Iso=2 Z`, `c(2n)=n log 16`, `H=(log 16)Z`, and extension isotropy is trivial.
The least positive primitive is `log 16`, with all positive integer repeats.
The general phase/kernel formula above applies with `p=2`, `A_0=0,A_1=ell`.
In particular the least positive generator cannot be shortened to a step
clock merely because the two source points are joined by an arrow.

All three full basins are countably infinite, not finitely sampled lists.
Countability follows from the finite-preimage bound. For infinitude start
`u_0=alpha`, `u_(r+1)=u_r+sqrt(u_r^2+1)>2u_r`. Every positive real point
has `b=1`, hence `G=1,R=0` for every owner. Thus all these distinct legal
points satisfy `T_O u_(r+1)=u_r` and eventually reach the same two-cycle.
Their unbounded real sequence is only a subset of the complete all-complex
inverse recursion; equality of the three full basins is not asserted.
All ancestors belong to ONE packet per owner, with phases modulo `log 16`.
Its area-null countable basin is retained by the frozen full-point convention.

## 7. Decisive scope and strongest alternative

MAIN has an actual positive primitive with multiplier `16`, which is not an
ordinary integer prime. This directly violates the prime-only benchmark and
ends the frozen gate; it is not a conditional existence dichotomy or a failed
search. Each control has independently the same witnessed core and time,
but different global transport/terminal/incoming rules are preserved.
The strongest positive result is a coherent all-state Newton/IMAGE owner
with real arithmetic feedback and an exactly proved primitive packet.
That owner result does not repair the wrong primitive time.
Null-set freedom of an a.e. density cannot alter the prescribed germ version.
No halved clock, selected subpacket, deleted ancestor or replacement source
is permitted. No theorem about all other cycles or all their multipliers is
claimed: fixed-cell identities are not transferred across arithmetic changes.
Strong naturalness and the remainder of the periodic ledger remain OPEN.
No T3, formal Route or Route B result is asserted. Preserve this raw unchanged
pending root's full read and a distinct PAPER UNLOCK for CP2/CP3.
