# R7 E4 — full mathematical review of the specified two-shear obstruction

2026-09-10 UTC. Internal nonauthor reviewer: `/root/c429_e4_cover_review`.

Reviewed all 342 lines of [C4 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round7/c4_specific_nine_lift/REPORT.md), bound to SHA-256:

```text
1dfc67f4171979139817231b6f95bf667cff58d87ea169e681f019370acc274f
```

## Verdict and exact theorem

**PASS — PROVABLE AS STATED for the entire frozen subclass. Zero mathematical or source-applicability must-fixes found.**

The maps are $H_P(x,y)=(x+P(y),y)$, $V_Q(x,y)=(x,y+Q(x))$ and $\rho_R(u,v)=(u,R(u)-v)$; composition is from right to left.

For the six exchanged points

$$P_5=(0,2),\ P_9=(2,2),\quad
P_3=(1,1),\ P_8=(1,-1),\quad
P_6=(-1,-2),\ P_7=(-1,0),$$

no first coordinate of $M=L\circ V_Q\circ H_P$, with unrestricted $P,Q\in\mathbb Z[t]$ and integral unimodular affine $L$, is constant on each of these three pairs. Consequently no such $M$, with any $R\in\mathbb Z[t]$, can make $M^{-1}\rho_RM$ restrict to $\kappa=(5\ 9)(3\ 8)(6\ 7)$ on the prescribed nine-point set.

The stronger first-coordinate statement is genuinely proved. It neither uses the three fixed-point equations nor assumes that $H_P$, $V_Q$, $L$, or $M$ preserves the original set. Both determinant signs, all affine translations, zero/constant/linear polynomials and arbitrary higher degrees are included. The order of the two shears and the selected permutation are fixed; unrestricted tame conjugators and the general integer-nine-period problem are not excluded.

## 1. Complete normalization audit — author lines 117–172

Let the first row of the affine map be $a s+b t+e$. A unimodular linear part implies $\gcd(a,b)=1$, including the cases where one entry is zero. Direct composition gives

$$U(x,y)=a(x+P(y))+b\{y+Q(x+P(y))\}+e.$$

Since $\rho_R$ fixes its first coordinate, $MK=\rho_RM$ gives $U(P_j)=U(P_{\kappa(j)})$. All subsequent reasoning needs only these equalities; it applies equally if one starts by hypothesizing a first coordinate with the three pair equalities, without a reflection $K$.

For the horizontal pair, putting $m=P(2)$ yields

$$2a+b\{Q(m+2)-Q(m)\}=0.$$

The polynomial difference in braces is $2d$ for an integer $d$. If $b=0$, primitivity gives $a=\pm1$, contradicting $2a=0$. Otherwise $a=-bd$, so $\gcd(a,b)=|b|$ and $b=\pm1$. There is no division by an unproved unit, and $a=0$ is covered.

Now $b(U-e)=y+S(x+P(y))$ with $S(t)=Q(t)+ab\,t\in\mathbb Z[t]$. Multiplication by $b=\pm1$ preserves every level-set equality. This is a normalization of the necessary invariant-coordinate condition, not an assertion that the original second coordinate or $R$ has a special form.

For $k=P(0)$, replacing $P(t)$ by $P(t)-k$ and $S(t)$ by $S(t+k)$ leaves the expression unchanged and preserves integer coefficients. Hence $P(0)=0$ is legitimate. Writing $p_j=P(j)$ and using $m=p_2$ after this normalization gives exactly

$$
\begin{aligned}
S(m+2)-S(m)&=0,\\
S(1+p_{-1})-S(1+p_1)&=2,\\
S(-1+p_{-2})-S(-1)&=2.
\end{aligned}\tag{A}
$$

The signs of both value differences 2 were checked directly from the points: their input $y$-coordinates differ by 2 in each case. The horizontal pair's input $y$-coordinates are equal. No condition on any intermediate image set entered this calculation.

## 2. Both signs at $-2$ — author lines 176–213

For $F\in\mathbb Z[t]$, the divisibility $r-s\mid F(r)-F(s)$ follows monomial by monomial. When the value difference is nonzero, equal arguments are impossible. For any $S\in\mathbb Z[t]$, the polynomial

$$g(t)=\frac{S(t+2)-S(t)}2$$

has integer coefficients: each nonconstant binomial contribution contains a factor 2 before division. This includes polynomials of every degree, not merely integer-valued samples.

The last equation in (A) implies that $p_{-2}$ is a nonzero divisor of 2. Since $p_{-2}\equiv P(0)=0\pmod2$, it must be $2\sigma$ with $\sigma=\pm1$. The first equation gives $g(m)=0$.

The complete sign exhaustion is:

| $\sigma$ | Forced value of $g$ | Difference dividing a unit | Candidates for $m$ |
| --- | --- | --- | --- |
| $+1$ | $g(-1)=1$ | $m+1\mid-1$ | $0,-2$ |
| $-1$ | $g(-3)=-1$ | $m+3\mid1$ | $-2,-4$ |

In the negative case, $S(-3)-S(-1)=2$ does give $g(-3)=-1$, not $+1$. In both rows the argument difference cannot be zero because the value difference is a unit.

Since $P(0)=0$, cancellation of odd monomials in $P(2)+P(-2)$ leaves even-degree contributions divisible by 8. Thus $m+2\sigma\equiv0\pmod8$. For $\sigma=1$, only $m=-2$ survives. For $\sigma=-1$, the candidates give $m-2=-4$ or $-6$, neither divisible by 8. Therefore

$$P(-2)=2,\quad P(2)=-2,\quad g(-1)=1,\quad g(-2)=0.\tag{B}$$

This uses the zero-constant normalization essentially; it does not assume an unjustified parity condition on arbitrary unnormalized polynomials.

## 3. Both signs at $\pm1$ and arbitrary-degree splitting — author lines 218–268

The middle equation in (A) forces $p_1-p_{-1}$ to be a nonzero even divisor of 2. Its sign is not predetermined, so write it as $2\varepsilon$, $\varepsilon=\pm1$.

For an arbitrary integer polynomial, separating its even and odd monomials gives

$$P(y)=yO(y^2)+E(y^2),\qquad O,E\in\mathbb Z[t],\quad E(0)=0.$$

No coefficient division by 2 is required for this decomposition. From (B) and the definition of $\varepsilon$,

$$O(1)=\varepsilon,\qquad O(4)=-1,\qquad E(4)=0.$$

The argument difference $4-1=3$ divides $O(4)-O(1)=-1-\varepsilon$. For $\varepsilon=1$ the difference is $-2$, which is excluded; for $\varepsilon=-1$ it is zero, which is allowed. Hence $\varepsilon=-1$.

The factorization $E(t)=t(t-4)B(t)$ remains in $\mathbb Z[t]$. Indeed $E(0)=0$ first gives $E=tA$ with integral coefficients, and $E(4)=4A(4)=0$ implies $A(4)=0$ in $\mathbb Z$. Division of $A$ by the monic polynomial $t-4$ then has zero remainder and integral quotient. The zero even part is included by $B=0$.

Putting $c=B(1)\in\mathbb Z$ now gives

$$P(1)=-1-3c,\qquad P(-1)=1-3c.$$

The middle equation of (A) becomes $S(2-3c)-S(-3c)=2$, so $g(-3c)=1$. Together with $g(-2)=0$, polynomial difference divisibility gives $2-3c\mid1$. The two possible values are $+1$, which would require $c=1/3$ and is forbidden, or $-1$, which gives $c=1$. Thus

$$P(1)=-4,\qquad P(-1)=-2.\tag{C}$$

Every division and sign choice above is in the integers. There is no rational interpolation assumption, coefficient cutoff, degree truncation or discarded higher-degree term.

## 4. Final contradiction — author lines 273–292

Equations (B)–(C) turn (A) into

$$S(0)=S(-2),\qquad S(-1)-S(-3)=2,\qquad S(1)-S(-1)=2.$$

The last two give $S(1)-S(-3)=4$. But $1\equiv-2\pmod3$ and $-3\equiv0\pmod3$ imply

$$S(1)-S(-3)\equiv S(-2)-S(0)=0\pmod3,$$

contradicting $4\equiv1\pmod3$. The sign in the final substituted difference is correct.

An equivalent manual consistency check is available directly from $g$. For every integer polynomial $S$,

$$2\{g(-3)+g(-2)+g(-1)\}
=S(0)+S(1)-S(-3)-S(-2)\equiv0\pmod3.$$

The forced values are $g(-3)=1$, $g(-2)=0$ and $g(-1)=1$, giving 4 on the left, the same contradiction. This is an algebraic check on all polynomial degrees, not a mathematical program or a finite search.

## 5. Dependency compatibility and limits

The [C2 R7 report](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round7/c2_nine_reflection_lifting/REPORT.md) was read for its actual data and inherited claims; its SHA-256 is `98fc3d0ed9b30c38c6050fe41ae60392e7cb720c84cb6c0b1399dcf2346f78f3`, matching C4's citation. I also read the verdict/data and conditional-target passages of the accepted [E6 review](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round7/reviews/e6_nine_reflection_lifting/REVIEW.md). This is not another independent whole-proof audit of the 27-candidate and interpolation results.

The nine coordinates and $\kappa$ agree exactly. The available restrictions are $a=(1\ 2\ 3)(4\ 5\ 6)(7\ 8\ 9)$ and $i=(1\ 5)(3\ 8)(6\ 7)$. Direct right-to-left multiplication gives $\kappa i=(1\ 9\ 5)$ and

$$\kappa ia=(1\ 2\ 3\ 9\ 7\ 8\ 5\ 6\ 4).$$

Therefore the inherited conditional implication to the native word $KIA$ is compatible: a genuine lift outside the excluded subclass would produce that orbit, with one application of the complete map as one tick. It remains conditional, and nothing in this proof constructs a lift or an integer nine-cycle.

The earlier quadratic-shear reflection classification has different quantifiers and is not a premise of the new obstruction. In particular, this theorem is about one selected restriction and one specified two-shear order, with an affine map only in the displayed postcomposition position. It does not exclude arbitrary pre-affine coordinate changes, every order of two shears, longer tame words, other reflection restrictions, or other nine-point sets merely by analogy.

## Coverage and final handoff

All proof-bearing sections were checked: invariant-coordinate necessity; primitive affine row and $b=0,\pm1$ cases; integral constant normalization; all three signed pair equations; both $P(-2)$ branches and the modulus-8 filter; both $P(1)-P(-1)$ signs; all-degree odd/even decomposition; both monic divisions; the integer alternatives for $c$; and the final modulus-3 contradiction. **No open must-fix item remains for the bound theorem.** Its full tame-lift boundary remains open, not silently strengthened into a universal obstruction.

The proof is self-contained elementary algebra. No external classification or source theorem is needed for its new conclusion, and no source-priority or literature-absence claim is certified by this review. The proof-writer, research-review and repository batch guidance required the exact theorem/normalization audit and restricted final verdict; no external-model review or full ARS panel/calibration is claimed.

Only this allocated review file was written. No mathematical program, old checker rerun, extra agent, source query, external-model/API call, author/shared edit, Git operation or PDF build occurred. All prior proof and review files remain unchanged. This result is an auxiliary obstruction in the frozen subclass, not a new contract or completed paper. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
