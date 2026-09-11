# Tenth lane: proved reductions and nonpromotion boundaries

2026-09-06 UTC. Author/scout `batch197_fosp_gate`; QAS/DTC and OFS
proof contributor `batch197_lzk_gate`. The literal definitions and all
complete small boxes remain those of [INTAKE.md](INTAKE.md).

Five rows close **NO_PROMOTION**. OFS has a complete author theorem
package and original-box check, but is **READY_FOR_NONAUTHOR_GATE /
NO_ADMISSION / SOURCE_VALUE_OPEN**. No row receives a paper number,
reserve, manuscript-review verdict or external clearance here.

## 1. QAS: a factor is not its unresolved full dynamics

The full derivation is the separate desk's
[original proof, Section 1](../order_geometry_tenth_desk/PROOF_AND_ADAPTER.md).
This author read it completely. With the desk's explicit area variables,
the closed factor is

$$H'=H(1-H)^2-(1-H)R,\qquad
R'=(1-3H)^2(1-H)^2R.$$

The two signed area differences have common multiplier
$(1-3H)(1-H)$; the alternating point sum has multiplier $1-3H$.
These are integer-polynomial identities valid also in characteristic two.
They neither reconstruct the four vertices from two scalars nor classify
the scalar graph over every prime. The desk gives a repeated-vertex
$p=3$ counterexample to common affine homothety and a side-area-change
counterexample to the specific centroaffine source adapter.

The original complete $p=3$ box already has period twelve. Its exact
cycle remains in the raw output; no universal fixed/two-cycle theorem is
inferred from the $p=2$ box. Global temporal and separate full inverse
obligations are unclosed. Disposition: **NO_PROMOTION / HOLD_PROOF**.

## 2. DTC: cubic area base and elementary affine lifting

The separate desk's [original proof, Section 2](../order_geometry_tenth_desk/PROOF_AND_ADAPTER.md)
is complete and was read in full. In anchor/edge coordinates
$o=v_0$, $x=v_1-v_0$, $y=v_2-v_0$, with $c=x\cdot y$,
$\delta=\det(x,y)$ and $J(s,t)=(-t,s)$, the literal becomes

$$o'=o+c(x-y),\quad x'=(I+\delta J)x,\quad
y'=(I+\delta J)y,\quad \delta'=\delta+\delta^3.$$

This is a bijective coordinate change on the full carrier, including
all repeated/collinear/isotropic configurations. For a target area
$\delta'$, every nonsingular root of $\delta+\delta^3=\delta'$
gives exactly one predecessor by matrix inversion. A singular root
$\delta^2=-1$ contributes $p$ predecessors precisely when its target
edges are not both zero and lie in its rank-one image line. A collinear
target otherwise has only its root-zero predecessor. The desk proves
all these boundaries, not merely a regular-chart calculation.

When $\delta=0$, edges stay fixed and the anchor translates by
$c(x-y)$, yielding period one or $p$. The all-prime noncollinear
cubic/lift dynamics is not classified. The full static decoder is
polynomial-root counting and rank-one affine lifting, with no residual
inverse credit. Disposition: **NO_PROMOTION / HOLD_PROOF_VALUE**.

## 3. OFS: the positive author deduction, not an admission

The complete self-contained [OFS author proof](OFS_PROOF_PACKAGE.md)
proves the exact tree dictionary by protected cells, the recursive full
target inverse, maximum $2^{n-4}$ and its unique fan target for $n\ge5$,
and the unique two-cycle with sharp height $n-2$. Both small exceptions
$n=3,4$ are explicit. The two separate desk supplements
[recursion/fibres](../order_geometry_tenth_desk/OFS_RECURSION_AND_FIBRES.md)
and [temporal deduction](../order_geometry_tenth_desk/OFS_TEMPORAL_CHECK.md)
were read completely. Both workers are proof contributors.

The standalone [affected checker](verify_ofs.py) has two actual passing
executions on only $n=3,\ldots,10$; it compares the complete decoder
source sets with literal reverse adjacency sets, not only totals.
The original sequence-based standard-word image guess and naive fibre
exponent are false and remain in their original declaration/output.
The new image formula is an explicit corrected deduction, not a rewritten
old success. Old static enumeration is deducted. Plain rotation and
plain descending pop-stack are excluded; a complete composed sorting
adapter has not been excluded. Disposition: **AUTHOR_PROOF_CLOSED /
READY_FOR_NONAUTHOR_GATE / SOURCE_VALUE_OPEN / NO_ADMISSION**.

## 4. SBF: complete elementary inverse, failed convergence guess

The map is $S(x,y)=(x(1-y),xy)$ over $\mathbf F_p^2$. For a target
$(a,b)$, addition forces $x=a+b$. If $a+b\ne0$, there is exactly
one source, $(a+b,b/(a+b))$. If $a+b=0$, a source must have $x=0$,
whose image is zero. Hence zero has exactly $p$ predecessors and every
nonzero zero-sum target has none. The image has $p^2-p+1$ states,
and zero is the unique maximum-fibre target. A fixed state has
$xy=0$ from its first equation and $xy=y$ from its second, so $y=0$;
there are exactly $p$ fixed points. These are elementary deductions.

The all-fixed convergence impression from the early small primes is
false already in the unchanged $p=11$ box. A direct cycle is

$$(1,5)\mapsto(7,5)\mapsto(5,2)\mapsto(6,10)\mapsto(1,5).$$

For example the last arrow is $6(1-10)\equiv1$ and
$6\cdot10\equiv5\pmod{11}$; substitution verifies the other three.
The larger original boxes also contain periods twenty, thirty-nine,
six and twenty-seven. No all-prime classification follows.
The explicit-Euler SIR adapter is derived from the actual primary
formulas in the source notes; real positivity/convergence is not imported
into finite fields. Disposition: **NO_PROMOTION / OLD_STATIC_INVERSE /
TEMPORAL_UNCLOSED**.

## 5. HGF: support strata and low-characteristic controls

Put $Q=a^2+b^2+c^2$. The map has coordinates
$T_i=a_i(Q-2a_i^2)$. It is one fourth of the gradient of

$$\mathcal H=2a^2b^2+2b^2c^2+2c^2a^2-a^4-b^4-c^4
 =(a+b+c)(-a+b+c)(a-b+c)(a+b-c)$$

when four is invertible. The literal integer polynomial, not division
by four, defines the other characteristics. The classical identity and
homogeneous polynomial scaling carry no novelty credit.

For odd $p$, a nonzero point in $T^{-1}(0)$ with support size $r$
has equal nonzero squared coordinates $q=Q/2$. Summing says
$rq=2q$, so $r=2$, since $r\in\{1,2,3\}$. Each support pair
allows $p-1$ choices for one coordinate and two signs for the other.
Thus the zero fibre is exactly $1+3\cdot2(p-1)=6p-5$.
This does not prove that it is the global maximum, even though it is
the unique maximum in every original odd-prime box.

At $p=2$, $T(a)=Qa$, where $Q$ is support parity. Even support
maps to zero, odd support is fixed, and $T^2=T$; its zero fibre has
four points. At $p=3$, $a_i^3=a_i$ gives $T(a)=(Q+1)a$,
a scalar-action control. On a coordinate axis at any odd prime the
map is already the classical scalar power rule $u\mapsto-u^3$.
In particular the original $p=11$ four-cycle on that axis is not an
independent geometric mechanism. No all-prime full-carrier temporal
classification or evaluated all-target inverse/extremum has been
proved. Disposition: **NO_PROMOTION / HOLD_PROOF_VALUE**.

## 6. JCA: exact one-step adjugate adapter, not a new inverse axis

Let $E$ be entrywise inversion with $E(0)=0$, a bijection of the full
symmetric-matrix carrier. The literal is $T(A)=E(\operatorname{adj}A)$.
For every target $B$,

$$T^{-1}(B)=\{A:\operatorname{adj}A=E(B)\}.$$

Thus its entire one-step inverse is the old adjugate inverse under a
bijective target relabelling; adding $E$ creates no second inverse
mechanism. The following direct evaluation makes that subtraction exact.
Write $C=E(B)$.

- If $C$ is invertible, write $d=\det A$. Necessarily
  $A=dC^{-1}$ and $d^2=\det C$. Conversely each nonzero root $d$
  gives that source, since $\det(dC^{-1})=d^3/\det C=d$ and
  its adjugate is $C$. There are at most two sources, one in
  characteristic two.
- Rank two for $C$ is impossible: the ranks of a three-by-three
  adjugate are only zero, one or three, by the minor definition and
  $A\operatorname{adj}A=(\det A)I$.
- If $C=0$, exactly the symmetric matrices of rank at most one occur.
  A nonzero symmetric rank-one matrix is $\lambda uu^{\mathsf T}$.
  The pairs $u\ne0,\lambda\ne0$ describe it in exactly $p-1$ ways,
  under $(u,\lambda)\mapsto(tu,\lambda/t^2)$. Thus there are
  $p^3-1$ nonzero sources and the zero source, for fibre $p^3$.
- If $C=\lambda uu^{\mathsf T}$ has rank one, choose an invertible
  matrix $Q$ with $Qe_3=u$. The congruence $D=Q^{\mathsf T}AQ$
  has last row/column zero precisely when $Au=0$, and
  $\operatorname{adj}D=\det(Q)^2Q^{-1}C Q^{-\mathsf T}$.
  Consequently the remaining symmetric two-by-two block must have
  determinant $\delta=\lambda\det(Q)^2\ne0$. Writing it as
  $\begin{pmatrix}s&t\\t&v\end{pmatrix}$, for each $s\ne0$
  and each $t$ there is one $v$. When $s=0$, each root
  $t^2=-\delta$ allows any $v$. The fibre is therefore
  $p(p-1+r_p(-\lambda))$, where $r_p(w)$ counts roots of $t^2=w$.
  Replacing $\delta$ by $\lambda$ is valid because $\det(Q)^2$
  is a nonzero square. This count covers characteristic two as well.

The unique maximum is $p^3$ at zero: all rank-one-target values are
at most $p(p+1)<p^3$ for odd primes, at most $p^2<p^3$ for $p=2$,
and invertible-target values are at most two. These are static
rank/determinant facts, not claimed new results. The original pilot
reported the corresponding complete fibre histograms; it did not
separately assert this final rank-one counting expression.

For temporal subtraction, if $\operatorname{rank}A\le1$ then
$T(A)=0$. If $\operatorname{rank}A=2$, its adjugate is rank one,
and entrywise inversion with zeros retained preserves a rank-one
factorization. Therefore $T^2(A)=0$. At $p=2,3$, $E$ is the
identity, so $T$ is precisely the old adjugate map on symmetric
matrices. On a fully regular domain,

$$T(A)=\det(A)^{-1}E(A^{-1}),$$

so its projective action is the classical ordinary/Hadamard inverse
composition. Korepanov's generic explicit solution and the
Kontsevich-periodicity diagonal-gauge theorem are source deductions,
not full-carrier finite-field theorems. Zero entries and singular
intermediate matrices cannot be silently deleted. The original $p=5$
box has height six and periods two, four, six and eight, but no
all-prime full-carrier clock is proved. Disposition:
**NO_PROMOTION / FULL_STATIC_ADJUGATE_ADAPTER / TEMPORAL_UNCLOSED**.

## Proof and verification roles

All new OFS claims have their dedicated complete author check pair.
The original six-row pilot checks its own stated controls. The desk
has a separate coefficient-identity checker for QAS/DTC, not an OFS
execution. Reading or hashing those outputs is not a fresh replay.
The JCA rank-one source evaluation is an elementary deductive adapter;
no separate post-pilot execution is claimed for that added expression.
Neither a true partial lemma nor a finite graph fills a missing axis.
