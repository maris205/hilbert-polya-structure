# R3 B4: branch discriminants and the missing different upper bound

2026-09-09 UTC. Proof-only complementary attack on A3's branch
preservation problem. The accepted R2 files are read-only inputs.

## Frozen question and success criterion

For every odd prime $p$ and $e\ge1$, retain
$k=\overline{\mathbb F}_p$, $K=k((s))$, $R=k[[s]]$,
$v(s)=1$, $P_s(z)=(1+s)z+z^2$, and the exact native small factor
$M_e$ from A3. Put $n=p^e$ and $r=(p-1)/p$.

Suppose a root $\alpha$ generates a proper cyclic root field
$L/K$ of degree $q=p^h$, with $1\le h<e$. The accepted lower
bound is

$$
d_L\ge q-1+n r.                                           \tag{LB}
$$

The named upper-bound target is:

> **(BD-U)** Use the exact branch polynomial, its discriminant,
> branch intersections, or the normalization index to prove
> $d_L<q-1+n r$ for every such proper root field.

A proof of (BD-U) would exclude every proper branch and settle the
local question. Alternatively, success for this bounded attack is a
proof that a specified discriminant-based inequality cannot produce
that contradiction from the currently available inputs. Failure of
that inequality is not a counterexample to branch preservation.

Read inputs:
[A3 branch preservation](../../continuation_round2/a3_wild_local_tower/BRANCH_PRESERVATION.md),
the accepted
[R2 displacement/different supplement](../../continuation_round2/b4_local_period_degree/PROOF_SUPPLEMENT.md),
and A3's separate conditional
[pair ramification note](../../continuation_round2/a3_wild_local_tower/PAIR_RAMIFICATION.md).
The branch-count equivalence, cyclic root fields, root slope,
coordinate-axis intersections, and R2 lower bounds are not reproved.
The proof-writer skill is used to separate the proved arithmetic
ledger from the unproved upper-bound target.

## Outcome

**NOT CURRENTLY JUSTIFIED:** (BD-U), branch preservation, and the
uniform full-inertia claim.

**PROVABLE AS STATED:** the exact branch-discriminant ledger, the
slope-forced order-index correction, and the failure of the resulting
upper bound to contradict (LB). Complete proofs are in
[PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md).

Let

$$
\delta_j=v(P_s^{p^j}(\alpha)-\alpha),\quad 0\le j<e,
\qquad T_e=v(\operatorname{Disc}(M_e)).
$$

If $D$ is the minimal polynomial of $\alpha$, set
$S_D=v(\operatorname{Disc}(D))$ and
$I_D=\operatorname{length}_R(O_L/R[\alpha])$. Then

$$
\begin{aligned}
T_e&=n(p-1)\sum_{j=0}^{e-1}p^{e-j-1}\delta_j,\\
S_D&=q(p-1)\sum_{j=e-h}^{e-1}p^{e-j-1}\delta_j,\\
d_L&=S_D-2I_D,\qquad
I_D\ge\frac{q(p-1)(q-2)}{2p}.
\end{aligned}
$$

Consequently the total discriminant and the accepted displacement
lower bounds supply the valid upper estimate

$$
d_L\le U_{e,h}(T_e):=
\frac qn T_e
-q r\big((p-1)(e-h)p^{e-1}+n-2\big).                    \tag{U}
$$

However, the same accepted displacement bounds force

$$
U_{e,h}(T_e)
\ge q r\big((p-1)h p^{e-1}+1\big)
>q-1+n r.                                               \tag{NC}
$$

Thus (U) cannot contradict (LB), even if $T_e$ is known exactly.
The statement remains true if every intra-branch contact is known
exactly and $S_D$ is used directly: the upper bound
$S_D-q r(q-2)$ is still strictly above (LB).
This is a boundary for the stated inequality, not for every possible
use of Newton coefficients or discriminants.

## Prime-degree control and what is actually missing

When $h=1$, the index estimate is exact:

$$
I_D=\frac{(p-1)(p-2)}2,\qquad
d_L=(p-1)\big(p\delta_{e-1}-p+2\big).
$$

The scaled monomial basis has all distinct valuation residues modulo
$p$, so it is already an integral basis. Thus an improved index
estimate cannot rescue this particular route at degree $p$:
the branch discriminant supplies the field different exactly, and
large contact simply permits large conductor.

For example, conditionally using only the existing $(3,2)$
discriminant input $T_2=144$, the hypothetical degree-$3$ branch
would have $S_D=24$, $I_D=1$, and $d_L=22$. These values are
compatible with both the R2 trace lower bound and its stronger
degree-$p$ break lower bound. This is an arithmetic consistency
check of a hypothetical branch, not construction of that branch.

Additional information is therefore necessary:

- for $h>1$, a sufficiently stronger lower bound on the
  normalization index, not just the slope-forced correction;
- or an upper restriction on the actual tail contacts
  $\delta_{e-h},\ldots,\delta_{e-1}$ from the exact quadratic
  coefficients;
- or genuine interlevel constraints, including contacts with another
  native small-cycle field and compatibility of ramification under
  quotients.

A3's new interlevel argument for $(3,2)$ uses the last ingredient
and was independently checked in messages. It does not contradict
(NC), whose input deliberately contains no second periodic field.
Its write-up and the actual pair's ramification refinement remain
A3/coordinator-owned, not extra results counted by this lane.

## Source subtraction and execution boundary

All small-cycle geometry and the exponential displacement bound are
accepted from the linked A3/R2 proofs. The new calculations are
elementary discriminant products, trace-form determinants, and
valuation-lattice arguments, proved explicitly. They are auxiliary
interfaces, not claimed as novel general discriminant theory.

Fixed-degree cyclic fields genuinely have no general conductor cap:
the directly checked
[Elder–Keating Section 2](https://arxiv.org/html/2503.16830v1)
permits Artin–Schreier fields of any positive break prime to $p$.
Such fields are only a logical control; no periodic points of this
exact $P_s$ are inferred in them. No new external source theorem is
used for the ledger or index proof.

Mathematical executions: **zero**. No new diagnostic requested.
Only the two new files in this assigned R3 directory were written.
No R2 mutation, Git/shared/index/PDF/API work, or claim of paper
admission. The exact root-field/full-inertia problem remains open.

NO_BAD_EULER_OR_ROOT_NUMBER.
