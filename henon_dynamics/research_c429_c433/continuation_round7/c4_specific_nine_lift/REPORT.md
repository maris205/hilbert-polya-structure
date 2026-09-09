# R7 C4 — a two-shear conjugator for the specified nine-point reflection

## Frozen question, subclass, and boundary

The point set is $C=\{P_1,\ldots,P_9\}$, with

$$
\begin{aligned}
P_1&=(0,0),&P_2&=(1,0),&P_3&=(1,1),\\
P_4&=(3,1),&P_5&=(0,2),&P_6&=(-1,-2),\\
P_7&=(-1,0),&P_8&=(1,-1),&P_9&=(2,2).
\end{aligned}
$$

The exact target is an integral tame conjugate of a triangular
reflection whose restriction to this fixed set is
$\kappa=(5\ 9)(3\ 8)(6\ 7)$, fixing $1,2,4$.
The data are imported from the actually read
[C2 R7 report](../c2_nine_reflection_lifting/REPORT.md), 245 lines,
SHA-256
$\texttt{98fc3d0ed9b30c38c6050fe41ae60392e7cb720c84cb6c0b1399dcf2346f78f3}$.

Before deriving restrictions, this author freezes the following
nontrivial construction subclass:

$$
H_P(x,y)=(x+P(y),y),\quad V_Q(x,y)=(x,y+Q(x)),\quad
M=L\circ V_Q\circ H_P,\quad K=M^{-1}\rho_R M,
$$

where $P,Q,R$ range over **all** $\mathbf Z[t]$,
$L$ ranges over **all** affine maps with linear part in
$\operatorname{GL}_2(\mathbf Z)$, and
$\rho_R(u,v)=(u,R(u)-v)$. No coefficient window, degree bound,
finite parameter sweep, or unannounced field enlargement is permitted.
Constants, linear polynomials, and either determinant sign are included.

Success is either an actual such $M,R$ inducing $\kappa$, or a complete
proof of nonexistence in this frozen subclass. In the latter case the
unrestricted integral tame conjugator problem stays open: this
subclass is not asserted to exhaust all tame coordinates.
If a lift exists, the already explicit maps $I,A$ in the C2 report
give an actual native integer nine-cycle through $KIA$, not a
factor-step clock. A permutation or pair of interpolating polynomial
values alone is not success.

## 1. Result and proof status

**PROVABLE AS STATED — complete obstruction in the frozen subclass.**
For every $P,Q,R\in\mathbf Z[t]$ and every integral unimodular
affine $L$, the map

$$
K=(L V_Q H_P)^{-1}\rho_R(L V_Q H_P)
$$

cannot have restriction $\kappa$ on $C$. In fact the first coordinate
of $L V_Q H_P$ cannot be equal on all three pairs
$(P_5,P_9)$, $(P_3,P_8)$, $(P_6,P_7)$. Thus no choice of
the reflection polynomial $R$, of the second coordinate, or of the
fixed-point equations can repair the obstruction.

This is the complete negative outcome permitted by the prior freeze,
not nonexistence for the full integral tame class. General $M$ in
$\operatorname{TA}_2(\mathbf Z)$, other orders or longer words of
nonlinear shears, and the general integer-nine-period problem remain
**NOT CURRENTLY JUSTIFIED** here. No actual integer nine-cycle is
claimed. Independent mathematical review of this report is pending.

## 2. Assumptions, strategy, and dependency map

No degree or coefficient bounds are imposed on any polynomial.
All affine translations and both determinant signs of $L$ are
included. In particular, $P,Q,R$ may be constant or linear.
The conjugating map is not required to preserve $C$: its image
may be any intermediate nine-point set.

The proof uses only necessary equality of the reflection's invariant
coordinate on the three specified exchanged pairs. First the horizontal
pair forces a unit coefficient in that coordinate. After normalization,
integer polynomial difference divisibility forces a sequence of exact
values of $P$ and then of a divided difference of $S$. The final values
contradict ordinary polynomial congruence preservation modulo three.

The dependencies are:

1. Section 3 derives the normalized invariant coordinate for the
   **entire** frozen conjugator class.
2. Section 4 treats both possible signs forced by the pair $(6,7)$
   and leaves one exact pair of values at $\pm2$.
3. Section 5 treats both signs from $(3,8)$, using the odd and even
   parts of an arbitrary integer polynomial, not a bounded-degree fit.
4. Section 6 obtains the contradiction modulo three.

The elementary fact used repeatedly is

$$
r-s\mid F(r)-F(s)\qquad(r,s\in\mathbf Z,\ F\in\mathbf Z[t]).
                                                               \tag{1}
$$

It follows by factoring $r^n-s^n$ in every monomial. When the
value difference is $1$ or $-1$, the argument difference is necessarily
$1$ or $-1$; zero difference of arguments cannot occur in that case.
Also, for every $S\in\mathbf Z[t]$,

$$
g(t):=\frac{S(t+2)-S(t)}2\in\mathbf Z[t],                    \tag{2}
$$

because the binomial expansion of
$((t+2)^n-t^n)/2$ has integer coefficients.
No external classification or interpolation theorem is used.

## 3. The first coordinate is forced into one normalized form

Suppose, toward a contradiction, that a map in the frozen class
induces $\kappa$. Write the first coordinate of $L$ as
$a s+b t+e$, where $a,b,e\in\mathbf Z$ and $\gcd(a,b)=1$.
The last condition holds because the linear part of $L$ has
determinant $1$ or $-1$. Before this affine map, the coordinates are

$$
s=x+P(y),\qquad t=y+Q(s).
$$

Thus the first coordinate of $M$ is

$$
U(x,y)=a(x+P(y))+b\bigl(y+Q(x+P(y))\bigr)+e.                \tag{3}
$$

The identity $MK=\rho_RM$ implies
$U(P_j)=U(P_{\kappa(j)})$. In particular, let $m=P(2)$
temporarily. The pair $P_5=(0,2)$, $P_9=(2,2)$ gives

$$
2a+b\bigl(Q(m+2)-Q(m)\bigr)=0.                             \tag{4}
$$

If $b=0$, then $a=\pm1$, contradicting (4). Otherwise the
quantity in parentheses is twice an integer, by (1). Equation
(4) yields $a=-b n$ for some $n\in\mathbf Z$. Primitivity
of $(a,b)$ now forces $b=\pm1$.

Multiplying $U-e$ by $b$ does not change any of its level-set
equalities. It replaces (3) by

$$
u(x,y)=y+S(x+P(y)),\qquad S(t)=Q(t)+ab\,t\in\mathbf Z[t].   \tag{5}
$$

We can further assume $P(0)=0$ without loss: replace
$P(t)$ by $P(t)-P(0)$ and $S(t)$ by $S(t+P(0))$.
The expression (5) is unchanged. All these operations preserve
integer coefficients and do not place any extra condition on the
second coordinate or the reflected polynomial.

Put $p_j=P(j)$, so $p_0=0$, and now set $m=p_2$ for the
normalized $P$. Equality on the three specified pairs is exactly

$$
\begin{aligned}
S(m+2)-S(m)&=0,                              &&(5,9),\\
S(1+p_{-1})-S(1+p_1)&=2,                    &&(3,8),\\
S(-1+p_{-2})-S(-1)&=2.                     &&(6,7)
\end{aligned}                                                   \tag{6}
$$

All remaining reasoning uses only (6), $P,S\in\mathbf Z[t]$,
and $P(0)=0$. In particular it applies even before asking for the
three fixed labels of $\kappa$.

## 4. The pair $(6,7)$ and the horizontal pair force the values at $\pm2$

By (1), $p_{-2}$ divides the value difference $2$ in the
last line of (6). The number $p_{-2}$ is even because
$P(-2)\equiv P(0)=0\pmod2$. It is nonzero because the
value difference is nonzero. Therefore

$$
p_{-2}=2\sigma,\qquad \sigma\in\{1,-1\}.                   \tag{7}
$$

Let $g$ be the integer polynomial in (2). The first line of
(6) gives $g(m)=0$.

If $\sigma=1$, the last line of (6) gives $g(-1)=1$.
By (1), $m+1$ divides $g(m)-g(-1)=-1$. Hence
$m=0$ or $m=-2$.

If $\sigma=-1$, that same line gives
$S(-3)-S(-1)=2$, hence $g(-3)=-1$. Thus $m+3$
divides $g(m)-g(-3)=1$, and $m=-2$ or $m=-4$.

These four possibilities are constrained by an additional identity
valid for every integer polynomial with zero constant term:

$$
P(2)+P(-2)\equiv0\pmod8.                                  \tag{8}
$$

To prove (8), odd monomials cancel, and an even monomial of
positive degree $2j$ contributes $2^{2j+1}$ times its integer
coefficient, with $2j+1\ge3$.

When $\sigma=1$, (8) says $m\equiv-2\pmod8$, leaving only
$m=-2$. When $\sigma=-1$, it says $m\equiv2\pmod8$,
which is satisfied by neither $-2$ nor $-4$. We have therefore
proved, with both signs exhausted,

$$
P(-2)=2,\qquad P(2)=-2,\qquad g(-1)=1,\qquad g(-2)=0.       \tag{9}
$$

## 5. The pair $(3,8)$ forces two further values

The middle line of (6), together with (1), implies that
$p_1-p_{-1}$ divides $2$. This difference is nonzero and
even, since $1\equiv-1\pmod2$. Thus

$$
p_1-p_{-1}=2\varepsilon,\qquad \varepsilon\in\{1,-1\}.       \tag{10}
$$

Write the odd and even parts of the arbitrary polynomial $P$ as

$$
P(y)=y\,O(y^2)+E(y^2),\qquad O,E\in\mathbf Z[t],\quad E(0)=0.
                                                               \tag{11}
$$

Equations (9)–(10) give

$$
O(1)=\varepsilon,\qquad
O(4)=\frac{P(2)-P(-2)}4=-1,\qquad E(4)=0.
$$

Applying (1) at arguments $4,1$ shows
$3\mid(-1-\varepsilon)$. Among the two possible signs this
forces $\varepsilon=-1$.

The two equalities $E(0)=E(4)=0$ imply
$E(t)=t(t-4)B(t)$ with $B\in\mathbf Z[t]$:
divide first by the monic polynomial $t$, then by $t-4$.
Writing $c=B(1)\in\mathbf Z$, we obtain from (11)

$$
P(1)=-1-3c,\qquad P(-1)=1-3c.                              \tag{12}
$$

This factorization covers every polynomial degree, including the
zero even part. It is not an interpolation truncation.

The middle line of (6) now says
$S(2-3c)-S(-3c)=2$, that is $g(-3c)=1$.
Since $g(-2)=0$ by (9), (1) gives

$$
2-3c\mid1,\qquad 2-3c\in\{1,-1\}.
$$

The first possibility would give $c=1/3$, not an integer.
The second gives $c=1$. Consequently

$$
P(1)=-4,\qquad P(-1)=-2.                                  \tag{13}
$$

## 6. Final contradiction

Substituting (9) and (13) into the three lines of (6) yields

$$
S(0)-S(-2)=0,\qquad
S(-1)-S(-3)=2,\qquad
S(1)-S(-1)=2.                                             \tag{14}
$$

The last two imply $S(1)-S(-3)=4$. On the other hand,
integer polynomial congruence preservation at
$1\equiv-2\pmod3$ and $-3\equiv0\pmod3$ gives

$$
S(1)-S(-3)\equiv S(-2)-S(0)=0\pmod3,
$$

contradicting $4\not\equiv0\pmod3$.
Thus no $U$ in (3) can have all the specified pair equalities.
The necessary condition for $K|_C=\kappa$ already fails, completing
the theorem for every member of the frozen subclass. $\square$

## 7. Exact scope, earlier results, and remaining gap

The C2 R7 report proves a 27-permutation upper set for arbitrary
integral tame conjugates of triangular reflections and identifies
this particular $\kappa$ as a sufficient lifting target. Its
gcd and coordinatewise polynomial interpolation tests do not
distinguish these candidates. We use its exact points and target,
not an assertion that any candidate lifts. Indeed the proof here
requires only the six exchanged points and gives an additional
global-coordinate obstruction within the frozen word class.

The previously read
[C2 R6 report, §5](../../continuation_round6/c2_nine_point_stabilizer/REPORT.md)
handles post-affine single quadratic vertical-shear coordinates.
The current class allows both alternating shears in all degrees,
but the current theorem concerns only the specified $\kappa$,
not the entire reflection restriction group. These distinct
quantifiers are not interchanged. All polynomial divisibility,
odd/even splitting, and congruence facts used above are elementary
classical inputs, not a new general theory of integral interpolation.

The precise surviving question is whether a different integral
tame coordinate map $M$ can satisfy
$M^{-1}\rho_RM|_C=\kappa$. Arbitrary longer words or different
coordinate mechanisms are not ruled out by this report.
Nor does ruling out this one reflection construction rule out
an integer nine-cycle produced by another map or point set.
The conditional implication to $KIA$ remains conditional in that
larger class; no finite permutation is reported as an actual orbit.

## 8. Verification and ownership

The original C2 R7 file was read completely and its stated hash
checked. The present argument was checked by hand at every sign,
normalization, monic division, and final residue condition.
The first-coordinate obstruction makes no assumption about the
second coordinate, the degree of $R$, or fixed-point interpolation.
It covers both determinant signs and all translations of $L$.

Only this new report was written. No mathematical program, extra
agent, external-model API, enlarged search, Git/shared-file edit,
PDF operation, or primary-query batch was performed. All prior
files, including R5 reversibility, remain unchanged.
The proof-writing skill caused the explicit subclass freeze and
the distinction between its proved obstruction and the unproved
general tame lift. The repository workflow keeps this auxiliary
outcome separate from independent-contract or paper admission.
Ready for a bounded non-author actual-file review; no PASS or
additional paper count is inferred in advance.
