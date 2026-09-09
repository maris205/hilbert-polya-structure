# E7 R3 — branch discriminant bounds

2026-09-09 UTC. Bounded, current-session nonauthor internal review.
This is not human peer review, a formal evaluation, or paper admission.

## Verdict and frozen inputs

**PROVABLE AS STATED for the displayed auxiliary claims;
ZERO OPEN MATHEMATICAL OR SOURCE MUST-FIXES.**

The exact contact ledger, normalization-index bound, strict
noncontradiction of the two specified scalar upper bounds, and
degree-$p$ integral-basis argument pass. They do not prove or refute
branch preservation, uniform full local inertia, or the global
dynatomic component question. Paper-count contribution: **zero**.

Both assigned files were read completely, and their hashes match
the coordinator's frozen inputs:

| File | Lines | SHA-256 |
| --- | --- | --- |
| [REPORT.md](../../b4_branch_different_upper/REPORT.md) | 158 | `71f0c069813405e57992ed727eee81be85283b10a613ded0fd67145d71124d85` |
| [PROOF_SUPPLEMENT.md](../../b4_branch_different_upper/PROOF_SUPPLEMENT.md) | 318 | `3e51aa38d00af3dc5843bfd25a4dbcc475b70b077bf4a35e6249d54bd5cce4da` |

The R2 displacement and field-different inequalities are accepted
inputs, not reopened results. I read their actual statements in the
[R2 supplement](../../../continuation_round2/b4_local_period_degree/PROOF_SUPPLEMENT.md)
and the accepted-interface/normalization sections of
[E6's review](../../../continuation_round2/reviews/e6_local_displacements/REVIEW.md).
I also read the complete
[A3 branch-preservation note](../../../continuation_round2/a3_wild_local_tower/BRANCH_PRESERVATION.md)
and the scalar-discriminant derivation in
[PAIR_RAMIFICATION.md](../../../continuation_round2/a3_wild_local_tower/PAIR_RAMIFICATION.md).
The latter supplies only the already available scalar used in the
conditional example here, not its full-group or AS-class conclusion.

The new A3 interlevel proof is expressly excluded. REPORT lines
131–135 and supplement lines 309–312 merely identify a different
input route; this review does not certify that proof or treat
author-side checking in messages as this nonauthor review.

## 1. Exact setup and root-contact counts

The domain is $K=k((s))$, $k=\overline{\mathbb F}_p$, with $p$
odd, $v(s)=1$, and $P_s(z)=(1+s)z+z^2$. The imported small factor
has $n=p^e$ distinct roots forming one native cycle, all with
valuation $r=(p-1)/p$. Its root field has degree $q=p^h$,
$1\le h\le e$, and the actual Galois subgroup consists of shifts
divisible by $p^{e-h}$.

The proof does not identify the native map with a field automorphism
when $h<e$. It uses all native shifts for contacts, but only the
actual subgroup shifts for the minimal polynomial $D$.

For two distinct cycle points $x,y$, the quotient

$$
\frac{P_s(x)-P_s(y)}{x-y}=1+s+x+y
$$

has residue $1$. A finite product gives the same assertion for
every positive iterate. Thus the $p^j$-step displacement at any
starting point has the same valuation and the same leading residue
after division by the displacement starting at $\alpha$.
Telescoping $b$ such displacements produces residue $b$, which is
nonzero exactly in the case used, $p\nmid b$. This verifies the
contact identity at supplement lines 66–85, including independence
of starting point. Distinctness and exact native period ensure that
all denominators there are nonzero.

The number of nonzero native indices of $p$-adic order $j$ is
$(p-1)p^{e-j-1}$. This count sums to $n-1$. Restricting to indices
divisible by $p^{e-h}$ retains precisely $j=e-h,\ldots,e-1$;
those counts sum to $q-1$. Multiplying the derivative products over
the $n$ or $q$ roots therefore gives exactly

$$
T_e=n(p-1)\sum_{j=0}^{e-1}p^{e-j-1}\delta_j,
\qquad
S_D=q(p-1)\sum_{j=e-h}^{e-1}p^{e-j-1}\delta_j.
$$

There is no missing factor of two: the product of derivatives
already counts every unordered pair twice, as the discriminant
requires. The valuation ignores its sign.

Consequently the subtraction in equation (2) is exact. The factor
$q/n$ averages to one branch's worth of roots but still includes
contacts with other branches. The prefix subtraction removes those
contacts. Simply using $(q/n)T_e$ as the branch discriminant would
be incorrect; the submitted proof does not do that. For $h=e$ the
prefix is empty, and $S_D=T_e$ as required.

## 2. Slope-forced index and field normalization

For $0\le i<q$, the elements
$\beta_i=s^{-\lfloor ir\rfloor}\alpha^i$ are integral, form a
$K$-basis, and span an $R$-lattice containing $R[\alpha]$.
Integrality alone is used here; the lattice is not assumed to be a
ring or to equal the normalization.

Writing $q=pu$ and $i=cp+b$ separates the floor sum into complete
blocks. The block remainders are $0,0,1,\ldots,p-2$, and hence

$$
\sum_{i=0}^{q-1}\lfloor ir\rfloor
=p(p-1)\frac{u(u-1)}2
 +u\frac{(p-1)(p-2)}2
=\frac{q(p-1)(q-2)}{2p}.
$$

The diagonal basis-change determinant proves the asserted lower
bound for $I_D$. The containment direction is correct: any missing
integral elements can only increase the normalization index.

The field is totally ramified with residue degree $1$, so
$v_L=qv$. The trace-dual quotient
$\mathfrak p_L^{-d_L}/O_L$ has $R$-length $d_L$, not $d_L/q$.
Its length is the valuation of the integral-basis trace determinant.
Passing to the monogenic basis multiplies that determinant by the
square of a determinant of valuation $I_D$. Therefore

$$
S_D=d_L+2I_D,
\qquad
d_L\le S_D-qr(q-2).
$$

This is a field-different identity with an order-index correction;
it does not substitute the derivative of the full small factor for
the field different. In a setting with nontrivial residue degree,
the field-discriminant term would carry that degree. The present
algebraically closed residue-field convention justifies its absence.

## 3. Both explicit upper bounds remain above the lower bound

Let $a=e-h$. Inserting the accepted
$\delta_j\ge(p^j+1)r$ into the subtracted prefix gives

$$
(p-1)\sum_{j=0}^{a-1}p^{e-j-1}(p^j+1)
=(p-1)a p^{e-1}+n-q.
$$

Because this prefix is subtracted, its lower bound supplies an
upper bound for $S_D$. Combining it with the index correction gives
equation (6), with precisely the displayed $n-2$ term.

For the direct branch bound, the corresponding tail sum is

$$
(p-1)\sum_{j=a}^{e-1}p^{e-j-1}(p^j+1)
=(p-1)h p^{e-1}+q-1.
$$

Thus both upper expressions, separately, satisfy

$$
U_{e,h}(T_e),\quad S_D-qr(q-2)
\ \ge\ qr\big((p-1)h p^{e-1}+1\big).
$$

This assertion concerns the values of the upper expressions, not a
new upper bound on the right-hand side. It remains valid if $T_e$
or every tail contact is known exactly.

To check the strict comparison uniformly, put $c=q/p\ge1$. The
difference from the imported lower threshold $q-1+nr$ is

$$
nr\big(ch(p-1)-1\big)-c+1.
$$

Here $ch(p-1)-1\ge1$, while $n\ge q=pc$ implies
$nr\ge c(p-1)$. The difference is at least
$c(p-2)+1>0$. This proves strictness for every odd $p$ and every
$1\le h\le e$, without an asymptotic or finite-table inference.
The $e=1$ case has no proper branch, but the displayed auxiliary
formulas still hold at $h=e=1$. Empty prefixes are handled correctly.

Accordingly, equations (5) and (6) cannot contradict the imported
lower bound. This does not establish the existence of a proper
branch compatible with all the quadratic's coefficients. Nor does
it show that every use of branch discriminants, stronger index
information, or interlevel arithmetic must fail.

## 4. Degree-$p$ exactness and the conditional scalar example

For $q=p$, the valuations $v_L(\beta_i)$ are exactly the integers
$0,\ldots,p-1$ in a different order. Coefficients from $K$ change
those valuations by multiples of $p$. Hence nonzero terms in a
$K$-linear combination have distinct valuations modulo $p$ and
cannot cancel at the minimum. Such a combination is integral if
and only if all its coefficients belong to $R$.

This proves $\Lambda=O_L$, not merely linear independence or an
index lower bound. It establishes equations (8) and (9), including

$$
I_D=\frac{(p-1)(p-2)}2,
\qquad
d_L=(p-1)(p\delta_{e-1}-p+2).
$$

When $h>1$, those valuation residues repeat. The proof appropriately
does not extend the exact integral-basis conclusion to that case.

For the conditional $p=3,e=2$ check, the imported scalar
$T_2=144$ and $\delta_0=4/3$ give
$144=9(6\cdot4/3+2\delta_1)$, hence $\delta_1=4$.
Under a hypothetical $q=3$, this yields $S_D=24$, $I_D=1$,
and $d_L=22$. The two compared lower values are $8$ and $14$;
the stronger degree-$p$ break would be $10$, consistent with its
imported lower bound $6$. No full Galois group or AS-class input is
used to obtain these conditional numbers. They are not a claimed
proper root field of the actual polynomial.

## 5. Primary-source applicability and subtraction

I directly read the perfect-residue-field setup, valuation and
ramification conventions, and Lemma 2.1 with proof in
[Elder–Keating, Section 2](https://arxiv.org/html/2503.16830v1).
The neighboring Lemma 2.2 and Theorem 2.3 statement were also checked
for the finite-versus-perfect-residue distinction. The source
expressly allows arbitrary perfect residue fields, so
$\overline{\mathbb F}_p$ is permitted; no finite-residue local
class-field theorem is silently substituted. Lemma 2.1 applied to
$X^p-X-s^{-b}$, with $b>0$ prime to $p$, gives the fixed-degree,
arbitrarily large-break control. This is not a construction of
periodic points of $P_s$. The full higher-Witt proof is not needed
for that control and is not recertified by this review.

I also read the definitions and trace-dual identification in
[Stacks, Section 49.8](https://stacks.math.columbia.edu/tag/0BW0).
Here $R$ is a Noetherian DVR, $O_L$ is finite free, and the generic
extension is separable, so the hypotheses are satisfied. The
submitted determinant and length argument supplies its own index
formula; this source check is for conventions, not a missing proof.

Small-cycle geometry, cyclicity, slope, the accepted lower bounds,
and the pair discriminant remain imported. General discriminant
products, trace forms and valuation lattices are classical tools.
The author subtracts them appropriately and makes no general
priority or paper-admission claim.

## Final disposition and execution boundary

No mathematical or source-applicability revision is required for
the frozen auxiliary claims. Retain exactly these boundaries:

| Claim | Disposition |
| --- | --- |
| Exact total/branch contact discriminants | Pass under the imported small-cycle setup. |
| Slope-forced index lower bound | Pass for all $1\le h\le e$. |
| Degree-$p$ scaled-monomial integral basis and exact index | Pass, specifically $h=1$. |
| Equations (5) and (6) cannot contradict the accepted lower bound | Pass uniformly for all stated parameters. |
| Every discriminant-based argument fails | Not established and not claimed. |
| BP, uniform full local inertia, or global component classification | Not proved or refuted by this package. |
| New A3 interlevel argument | Outside this review's scope. |

Only this assigned new review file was written. Mathematical
executions, old reruns, author/shared-file edits, Git operations,
PDF builds, formal evaluations, external-model/API uploads and
additional agents: **zero**. The research-review/proof-writer
checklists and repository batch workflow supplied the claim,
dependency and source discipline; their external-review examples
were not executed. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
