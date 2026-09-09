# R5-C1 proof package — precise two-involution boundaries

## Claim and status

The construction target remains an exact integer cycle of native period $12$ or $24$ for some integral tame automorphism. **Status of that target: NOT CURRENTLY JUSTIFIED.** The following are proved auxiliary obstructions to explicit construction mechanisms, not exclusions of $12$ in the full tame group.

Let

$$I_q(x,y)=(x,q(x)-y),\qquad J_p(x,y)=(p(y)-x,y),\qquad p,q\in\mathbb Z[t].$$

Both are integral triangular involutions. One native tick is the full map $T=J_p\circ I_q$.

**Lemma A.** If $p(y)=ky+c$ is affine, no integer orbit of $T$ has native period $12$ or $24$. The conclusion also holds if $p$ merely agrees with such an affine polynomial on all the second coordinates where $J_p$ is applied along the selected orbit.

**Lemma B.** The monotone-index alternating staircase described in Step 2 cannot be realized by integral $p,q$ when both lists of levels are nonconstant arithmetic progressions, with any nonzero integer spacings. This is an interpolation obstruction, not an orbit exclusion outside this template.

**Lemma C.** No $p,q\in\mathbb Z[t]$ realize the twelve-vertex staircase in Step 2 if $(x_0,\ldots,x_5)$ is any permutation of $\{0,1,2,3,4,5\}$ and $(y_0,\ldots,y_6)$ is any permutation of $\{0,1,2,3,4,5,6\}$. The result covers all $6!7!$ arrangements without a program. Integer translations and independent sign reflections of the two coordinate sets are covered by conjugacy.

**Status of Lemmas A–C: PROVABLE AS STATED.** No new R5 mathematical execution is a dependency of Lemmas A–C; the imported C428 theorem retains its accepted historical certificate dependencies.

## Assumptions, notation, and source subtraction

All coordinates are integers. The twelve staircase vertices are required to be distinct. The full finite word, not each involution, is the native map. A polynomial of unrestricted degree can be replaced on a finite integer input set by its remainder modulo the monic vanishing polynomial; the remainder still has integer coefficients.

The only imported cycle exclusion is C428's actual all-degree single-factor theorem for integral coefficients and integer points. Its positive-sign spectrum is $\{1,2,3,4,6\}$. For a scalar polynomial of degree less than two one can pad it by an integral polynomial vanishing on the finite coordinate support, as already proved in R5-C2 `PROOF_SUPPLEMENT.md`, §§1–4; this makes a degree-at-least-two single factor agree on the entire chosen cycle. Neither C428 nor the padding argument is a new result here.

## Strategy and dependency map

1. An explicit rational linear/affine injection collapses a two-involution word with one affine center to a single integral Hénon factor while retaining integer orbit images.
2. The staircase's two matchings give exact interpolation equations and an exact abstract twelve-cycle.
3. First and third divided differences exclude all nonzero arithmetic-progression spacings.
4. On the consecutive seven-node set, bounded integer values force the interpolation remainder to degree at most two. The four possible genuinely quadratic polynomials violate the staircase endpoint/total-sum conditions. Affine cases fall under Lemma A.

## Proof

### Step 1. Exact affine-center collapse

Assume $p(t)=kt+c$ and $k\ne0$. Define

$$L(x,y)=(ky-x+c,x).$$

Its determinant is $-k$, so it is an invertible rational affine map and maps $\mathbb Z^2$ injectively into $\mathbb Z^2$. Writing $(u,v)=L(x,y)$ gives $x=v$ and $ky=u+v-c$. Since

$$T(x,y)=(kq(x)-ky+c-x,q(x)-y),$$

direct substitution yields

$$L\circ T\circ L^{-1}(u,v)
=(v,kq(v)-2v+2c-u).\tag{1}$$

The scalar polynomial in (1) has integer coefficients. The rational inverse of $L$ does not have to preserve all integer points: each original integer cycle has an integer image under the injective forward map $L$, and conjugacy preserves its least period. C428, with finite-support degree padding if needed, excludes periods $12$ and $24$ in (1).

If $k=0$, then

$$T(x,y)=(c-x,q(x)-y),$$

and

$$T^2(x,y)=(x,y+q(c-x)-q(x)).$$

At a periodic point, some positive iterate of $T^2$ returns. The displayed translation of the second coordinate must therefore be zero over characteristic zero. That point has period dividing two under $T$.

If $p$ only agrees with $kt+c$ at the relevant finitely many intermediate inputs, replacing $p$ by the affine polynomial leaves every transition of the selected cycle unchanged. The proved affine cases apply to this actual cycle. This proves Lemma A.

### Step 2. The exact twelve-point staircase equations

Take distinct integers $x_0,\ldots,x_5$ and distinct integers $y_0,\ldots,y_6$. Define

$$P_{2i}=(x_i,y_i),\qquad P_{2i+1}=(x_i,y_{i+1})\qquad(0\le i\le5).\tag{2}$$

All twelve vertices are distinct. The desired involution actions are: $I_q$ swaps $P_{2i}$ with $P_{2i+1}$; $J_p$ swaps $P_{2i-1}$ with $P_{2i}$ for $1\le i\le5$ and fixes $P_0,P_{11}$. These actions are equivalent to

$$q(x_i)=y_i+y_{i+1}\quad(0\le i\le5),\tag{3}$$

$$p(y_0)=2x_0,\quad p(y_i)=x_{i-1}+x_i\ (1\le i\le5),\quad p(y_6)=2x_5.\tag{4}$$

The product $J_p\circ I_q$ would have the exact native orbit

$$P_0,P_2,P_4,P_6,P_8,P_{10},P_{11},P_9,P_7,P_5,P_3,P_1,P_0.\tag{5}$$

For example, each even vertex other than $P_{10}$ is first sent to the next odd vertex and then to the next even vertex; $P_{10}$ is sent to the fixed endpoint $P_{11}$; the odd vertices then traverse the chain in reverse two-step increments. Thus (5) is a twelve-cycle if integral interpolating $p,q$ exist. Equations (3)–(4), not merely the abstract permutation (5), are the missing realization condition.

### Step 3. All nonzero arithmetic-progression spacings fail

Suppose

$$x_i=b+ai,\qquad y_i=d+ci,\qquad a,c\in\mathbb Z\setminus\{0\}.$$

The values in (3) at two successive $x_i$ differ by $2c$. The value difference of an integral polynomial is divisible by the input difference, so $a\mid2c$.

The first four prescribed values in (4) are

$$2b,\quad 2b+a,\quad 2b+3a,\quad 2b+5a.$$

Their third forward difference is $-a$. For every integral polynomial $p$, its third forward difference at the equally spaced nodes $d,d+c,d+2c,d+3c$ is divisible by $6c^3$. To justify the factor without a degree restriction, expand $p(d+ct)$ as an integral polynomial in $t$. A monomial of degree $m<3$ has zero third difference; for $m\ge3$, its coefficient contains $c^m$, and the third difference of $t^m$ at zero is $3!S(m,3)$, where the integer $S(m,3)$ counts partitions of an $m$-element set into three nonempty blocks. Equivalently this divisibility follows by expanding the integer polynomial in the monic falling-factorial basis. Thus $6c^3\mid a$.

These two necessary conditions imply

$$6|c|^3\le|a|\le2|c|,$$

which is impossible for a nonzero integer $c$. This proves Lemma B. The same first-four-node argument applies to the analogous nine-vertex staircase, but that target remains C2's separate complementary responsibility.

### Step 4. Seven bounded integer values force a quadratic remainder

Assume the coordinate-level sets of Lemma C. By (4), all seven values of $p$ at $0,1,\ldots,6$ lie in $[0,10]$. Divide $p$ by the monic polynomial $\prod_{j=0}^6(t-j)$ and replace it by the integral remainder $r(t)$ of degree at most six. Its values are unchanged at every input used in (4). Put $r_j=r(j)$.

If $a_6$ is the sixth-degree coefficient, then

$$720a_6=\Delta^6r_0=r_6-6r_5+15r_4-20r_3+15r_2-6r_1+r_0.$$

The sum of the positive coefficients and the absolute sum of the negative coefficients are both $32$. Since $0\le r_j\le10$, the displayed expression has absolute value at most $320$. Therefore the integer $a_6$ is zero.

Now $\deg r\le5$. If $a_5$ is its fifth-degree coefficient, each of the fifth differences on nodes $0,\ldots,5$ and $1,\ldots,6$ equals $120a_5$. Adding them gives

$$240a_5=-r_0+4r_1-5r_2+5r_4-4r_5+r_6.$$

Each sign's total coefficient magnitude is $10$, so the right side has absolute value at most $100$. Hence $a_5=0$.

For a degree-at-most-four polynomial, its leading coefficient is its fourth divided difference at the five nodes $0,1,3,5,6$. Multiplication of the usual Lagrange leading-coefficient identity by $360$ gives

$$360a_4=4r_0-9r_1+10r_3-9r_5+4r_6.$$

The signed coefficient totals are $18$ and $-18$, so its absolute value is at most $180$. Thus $a_4=0$.

Finally, for $\deg r\le3$, the third forward difference with step two is

$$48a_3=r_6-3r_4+3r_2-r_0.$$

Its absolute value is at most $40$. Therefore $a_3=0$, and $r$ has degree at most two.

### Step 5. The quadratic candidates all violate the endpoints

Write $r(t)=at^2+bt+c$. Its second difference on the nodes $0,3,6$ gives

$$18a=r_6-2r_3+r_0,$$

whose absolute value is at most $20$. Thus $a\in\{-1,0,1\}$.

If $a=1$, the endpoint difference $r_6-r_0=36+6b\in[-10,10]$ forces $b\in\{-7,-6,-5\}$. The polynomials $t^2-7t$ and $t^2-5t$ each have range width $12$ on these seven nodes, independently of the added constant, so only $b=-6$ is possible. The two allowed polynomials are

$$r(t)=(t-3)^2\quad\text{or}\quad r(t)=(t-3)^2+1.$$

For $a=-1$, apply the preceding calculation to $10-r(t)$, which also has values in $[0,10]$. The two candidates are

$$r(t)=9-(t-3)^2\quad\text{or}\quad r(t)=10-(t-3)^2.$$

On the other hand, summing all seven equations (4), and using $\sum_{i=0}^5x_i=15$, gives

$$\sum_{j=0}^6r(j)=30+x_0+x_5.\tag{6}$$

The endpoints $x_0,x_5$ are distinct, so $1\le x_0+x_5\le9$.

- For $r(t)=(t-3)^2$, the left side of (6) is $28$, impossible.
- For $r(t)=(t-3)^2+1$, the sum is $35$, so $x_0+x_5=5$. Its even values are only $2$ and $10$, so (4) forces the two distinct endpoints to be $1$ and $5$, whose sum is $6$, a contradiction.
- For $r(t)=9-(t-3)^2$, the sum is $35$, again requiring endpoint sum $5$. Its even values are only $0$ and $8$, forcing distinct endpoints $0$ and $4$, whose sum is $4$, a contradiction.
- For $r(t)=10-(t-3)^2$, the sum is $42$, requiring endpoint sum $12$, a contradiction.

Hence only $a=0$ remains. The polynomial $p$ agrees with an integral affine polynomial at all seven intermediate $J_p$ inputs. Lemma A excludes a native twelve-cycle. But equations (3)–(4) would produce exactly the distinct twelve-cycle (5). Therefore they cannot all be satisfied. This proves Lemma C. $\square$

## Exact unclosed boundary

The lemmas do not exclude unequal nonconsecutive coordinate-level sets, repeated heights shared by several involution pairs, other finite configurations, products of more involutions, or arbitrary tame words. They do not decide $12$ or $24$ in the full R5-C2 spectrum. The small consecutive-letter template is exhausted analytically, not by a new census. No code, old certificate, or independent-review outcome is asserted in this supplement.
