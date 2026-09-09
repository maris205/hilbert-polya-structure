# C1 proof package — denominator feasibility and integral-normalization obstruction

## Claim

The frozen main question **C1-UB3** is whether an absolute bound exists on ordinary least periods over $\mathbb Q^2$ for

$$F_{P,\epsilon}(x,y)=(y,P(y)-\epsilon x),\qquad P\in\operatorname{Int}(\mathbb Z),\quad \deg P=3,\quad \epsilon\in\{1,-1\}.$$

This package does **not** resolve C1-UB3. It proves the following auxiliary statements for the complete coefficient class, and an exact obstruction to a proposed reduction.

**Theorem F (feasibility).** Write

$$P(t)=A\binom t3+B\binom t2+Ct+D,\qquad A,B,C,D\in\mathbb Z,\quad A\ne0,$$

and define

$$\beta=3(B-A),\qquad \gamma=2A-3B+6C,\qquad \delta=6D.$$

1. Every rational coordinate on every periodic orbit belongs to $A^{-1}\mathbb Z$. An explicit prime-by-prime refinement is given in Step 2 below. The exponent of a prime greater than three in this bound cannot be uniformly lowered when the other coefficients range freely.
2. Every periodic coordinate has real absolute value at most

$$R(P)=\max\left\{1,\frac{|\beta|+|\gamma|+|\delta|+12}{|A|}\right\}.$$

Consequently there is a terminating, parameter-dependent finite-graph procedure giving every rational periodic point and its exact period for each input polynomial. Its state bound depends on the coefficients and is not the sought uniform bound.
3. If an invertible rational affine map conjugates $F_{P,\epsilon}$ to another standard-form map $F_{Q,\eta}$ of degree at least two, it is necessarily

$$T(x,y)=(\lambda x+\mu,\lambda y+\mu),\qquad \lambda\in\mathbb Q^\times,\quad\mu\in\mathbb Q,$$

with $\eta=\epsilon$ and

$$Q(t)=\lambda P((t-\mu)/\lambda)+(1+\epsilon)\mu.$$

In particular, the rational squareclass of the cubic leading coefficient is invariant under all such affine conjugacies.

**Theorem O (normalization obstruction).** For every integer $q\ge2$ and either sign, the integral cubic

$$P_{q,\epsilon}(t)=qt^3-t^2+(1+\epsilon)t$$

has the rational fixed point $z_q=(1/q,1/q)$. There is no conjugacy regular with invertible derivative at $z_q$ that sends $z_q$ to an integer point of a polynomial map $H\in\mathbb Z[x,y]^2$. In particular, no rational polynomial conjugacy, and no rational affine conjugacy, can put the entire rational periodic set of $F_{P_{q,\epsilon},\epsilon}$ inside $\mathbb Z^2$ while making the conjugated map integral-coefficient. The same pointwise obstruction holds over the ring of integers of every number field.

Theorem O disproves that universal normalization route. It does not disprove C1-UB3: its obstructing orbit has least period one.

## Status

- **Original C1-UB3: NOT CURRENTLY JUSTIFIED.** Neither a coefficient-independent period bound nor unbounded primitive periods are proved.
- **Theorems F and O: PROVABLE AS STATED.** Complete elementary proofs follow. They are auxiliary structural results, not an admitted paper.

## Assumptions and notation

- $\operatorname{Int}(\mathbb Z)=\{P\in\mathbb Q[t]:P(\mathbb Z)\subseteq\mathbb Z\}$.
- All periods refer to ordinary iteration of the displayed two-dimensional map. A cyclic coordinate word $(x_0,\ldots,x_{n-1})$ gives the states $(x_i,x_{i+1})$, with indices in $\mathbb Z/n\mathbb Z$.
- Such a word satisfies

$$x_{i+1}+\epsilon x_{i-1}=P(x_i).\tag{1}$$

- $v_p$ denotes the additive valuation with $v_p(p)=1$ and $v_p(0)=+\infty$. Zero lower coefficients are permitted throughout.
- The inverse map is $F_{P,\epsilon}^{-1}(x,y)=(\epsilon(P(x)-y),x)$. Thus each pair determines both neighboring pairs uniquely.
- A conjugacy regular with invertible derivative at a point means a change $T$ defined near that point for which $T\circ F=H\circ T$ locally and the two-by-two matrix $DT$ at the point is invertible. Theorem O includes rational polynomial automorphisms but does not require a global polynomial inverse.

## Proof strategy

Use a minimum valuation on a periodic coordinate word to bound denominators, and a real maximum to bound its height. Compare the first components of an affine conjugacy to force its shape. Finally, use derivative similarity at a fixed point to obstruct integral images. No finite scan or numerical estimate is a proof dependency.

## Dependency map

1. Newton interpolation at $0,1,2,3$ gives integral $A,B,C,D$ and the identity $6P(t)=At^3+\beta t^2+\gamma t+\delta$.
2. This identity and the cyclic recurrence imply the denominator bound by unique lowest valuation.
3. The same identity at the real maximum implies the finite box and the exact graph procedure.
4. The affine conjugacy equation determines the common scale and translation, independently of the denominator lemma.
5. Derivative similarity and the explicit fixed point prove Theorem O, independently of the graph procedure or any earlier C-series classification.

## Proof

### Step 1. Full Newton coordinates

For a polynomial of degree at most three, define

$$D=P(0),\quad C=P(1)-P(0),$$

$$B=P(2)-2P(1)+P(0),\quad A=P(3)-3P(2)+3P(1)-P(0).$$

Integer-valuedness makes these four quantities integers. The Newton polynomial formed from them agrees with $P$ at four distinct rational arguments, and hence is identically $P$: their difference has degree at most three and four roots. Degree exactly three is equivalent to $A\ne0$. Uniqueness follows from those same evaluations. Conversely, $\binom t2$ and $\binom t3$ are integers for every integer $t$, including negative $t$, because the products of two or three consecutive integers are divisible by $2$ or $6$, respectively. Expanding gives

$$6P(t)=At^3+\beta t^2+\gamma t+\delta.\tag{2}$$

This is elementary Newton interpolation, not a new method.

### Step 2. Denominator lattice, refinement, and sharp exponents

Let a periodic coordinate word be given, and fix a prime $p$. Suppose its maximum denominator exponent is positive:

$$e=-\min_i v_p(x_i)>0.$$

Choose $j$ with $v_p(x_j)=-e$. If $e>v_p(A)$, then

$$v_p(Ax_j^3)=v_p(A)-3e<-2e.$$

Every other term on the right-hand side of (2) at $x_j$ has valuation at least $-2e$, because $\beta,\gamma,\delta$ are integers and $e>0$. The term $Ax_j^3$ therefore has unique lowest valuation, so

$$v_p(6P(x_j))=v_p(A)-3e<-2e.$$

On the other hand, (1) and $v_p(\epsilon)=0$ give

$$v_p\bigl(6(x_{j+1}+\epsilon x_{j-1})\bigr)\ge v_p(6)-e\ge-e.$$

This contradicts (1). Hence $e\le v_p(A)$ at every prime. Every rational periodic coordinate is therefore in $A^{-1}\mathbb Z$. If $|A|=1$, all such coordinates are integral, with no restriction on $B,C,D$ or on the sign.

A finer bound is sometimes useful. Put

$$a_p=v_p(A),\quad b_p=v_p(\beta),\quad c_p=v_p(\gamma),\quad d_p=v_p(\delta),\quad \ell_p=v_p(6),$$

and define

$$E_p(P)=\max\left\{0,\ a_p-b_p,\ \left\lfloor\frac{a_p-c_p}{2}\right\rfloor,\ \left\lfloor\frac{a_p-d_p}{3}\right\rfloor,\ \left\lfloor\frac{a_p-\ell_p}{2}\right\rfloor\right\}.\tag{3}$$

An entry involving subtraction of $+\infty$ is omitted from this maximum. In particular the final entry is always finite. If $e>E_p(P)$, then

$$a_p-3e<b_p-2e,\quad a_p-3e<c_p-e,\quad a_p-3e<d_p,\quad a_p-3e<\ell_p-e.$$

Thus $Ax_j^3$ is uniquely lowest among the four polynomial terms and lower than the minimum possible valuation of the neighboring sum. This again contradicts (1). Consequently the reduced denominator of every periodic coordinate divides

$$L(P)=\prod_p p^{E_p(P)}.\tag{4}$$

All exponents in (3) are nonnegative and at most $v_p(A)$, so $L(P)$ is a finite product and divides $|A|$. This is a necessary denominator bound; it does not assert that every permitted denominator is realized.

To see why the simpler exponent cannot be uniformly reduced, fix any prime $p>3$ and positive integer $e$, put $q=p^e$, and take $P_{q,\epsilon}$ from Theorem O. Direct substitution yields

$$P_{q,\epsilon}(1/q)=\frac{1+\epsilon}{q},$$

so $(1/q,1/q)$ is fixed. Here $A=6q$, and its denominator exponent is exactly $e=v_p(A)$. Hence even full integrality of the original polynomial's coefficients does not imply integrality of its rational periodic points, or a uniformly smaller exponent at primes greater than three.

### Step 3. Parameter-dependent finite completeness

For any periodic word, let $M=\max_i|x_i|$ at the real absolute value. At an index attaining $M$, equations (1) and (2) imply

$$|A|M^3\le |\beta|M^2+(|\gamma|+12)M+|\delta|.\tag{5}$$

If $M\ge1$, the right-hand side is at most $(|\beta|+|\gamma|+|\delta|+12)M^2$. Dividing by $|A|M^2$ gives the asserted bound. If $M<1$, the bound follows from the definition $R(P)\ge1$.

Define the finite coordinate set

$$\mathcal E_P=\left\{\frac{k}{A}:k\in\mathbb Z,\ |k|\le\lfloor |A|R(P)\rfloor\right\}.$$

All rational periodic points lie in $\mathcal E_P^2$. Make a directed graph with these vertices, drawing an edge from $z$ to $F_{P,\epsilon}(z)$ exactly when the image is also in the set. Arithmetic in this construction is exact rational arithmetic. Each vertex has at most one outgoing edge, and injectivity of $F_{P,\epsilon}$ makes the indegree at most one. Every directed cycle is an actual periodic orbit. Conversely, every actual rational periodic orbit is wholly in the set and is a directed cycle. Traversing the finitely many components therefore gives every periodic point and its exact least period, without a guessed period cutoff.

The resulting elementary bound is

$$\#\operatorname{Per}(F_{P,\epsilon},\mathbb Q^2)\le\bigl(2\lfloor |A|R(P)\rfloor+1\bigr)^2.\tag{6}$$

The right side is coefficient-dependent. Formula (6) and the algorithm do not answer C1-UB3. The graph has not been implemented or run in this investigation.

### Step 4. All affine conjugacies between standard forms

Suppose

$$T(x,y)=(rx+sy+u,tx+vy+w)$$

is invertible and satisfies $T\circ F_{P,\epsilon}=F_{Q,\eta}\circ T$. Comparing the first components gives the polynomial identity

$$ry+sP(y)-s\epsilon x+u=tx+vy+w.$$

Since $\deg P\ge2$, comparison of the highest power of $y$ gives $s=0$. The remaining coefficients give $t=0$, $v=r$, and $w=u$. Invertibility then gives $r\ne0$. Comparing the coefficient of $x$ in the second components gives $\eta=\epsilon$. Comparing their remaining parts gives

$$rP(y)+u=Q(ry+u)-\epsilon u,$$

which is the claimed formula with $\lambda=r$ and $\mu=u$. Conversely that formula directly verifies the conjugacy.

If $a=A/6$ is the original cubic leading coefficient, the new one is $a/\lambda^2$. Thus $[a]\in\mathbb Q^\times/(\mathbb Q^\times)^2$ is invariant. There are infinitely many such classes even in the subclass $P(t)=p t^3$ as $p$ runs through primes: if $p\ne r$ are primes, $p/r$ is not a rational square since its $p$-valuation is odd. No finite set of prescribed leading coefficients can therefore cover the entire coefficient class by rational affine normal forms.

The obstruction is specifically to finitely many fixed leading-coefficient branches, not to normal forms retaining an unbounded squareclass parameter. Passing to a quadratic extension may make a leading coefficient square; this changes the rational-point domain and does not establish integral coefficients or an integer periodic lattice.

### Step 5. A pointwise obstruction surviving nonlinear conjugacy

We first record the general derivative fact used here. If $z$ is fixed under $F$, $T\circ F=H\circ T$ locally, and $DT(z)$ is invertible, then $z'=T(z)$ is fixed under $H$. Differentiating the conjugacy equation at $z$ gives

$$DT(z)\,DF(z)=DH(z')\,DT(z).$$

Hence $DF(z)$ and $DH(z')$ are similar, and have the same trace and characteristic polynomial. If $H$ has integer coefficients and $z'\in\mathbb Z^2$, every entry of $DH(z')$ is an integer; in particular its trace is an integer.

For the family in Theorem O, direct substitution already showed that $z_q$ is fixed. Its derivative is

$$DF_{P_{q,\epsilon},\epsilon}(z_q)=
\begin{pmatrix}0&1\\-\epsilon&P'_{q,\epsilon}(1/q)\end{pmatrix},$$

and

$$P'_{q,\epsilon}(1/q)=3q\frac1{q^2}-\frac2q+1+\epsilon=1+\epsilon+\frac1q.\tag{7}$$

This is not an integer for $q\ge2$, contradicting the necessary trace condition. The claimed conjugacy cannot exist.

If $H$ has coefficients in $\mathcal O_K$ and $z'\in\mathcal O_K^2$ for a number field $K$, the same derivative calculation makes the trace an algebraic integer. A rational algebraic integer is an integer: if a reduced fraction $a/b$ satisfies a monic integer polynomial, multiplying by the appropriate power of $b$ shows that $b$ divides $a^{n}$ and therefore $b=1$. Thus (7) also excludes that larger target ring.

For completeness, at any periodic point of least period $n$ the same argument applied to $F^n$ preserves the characteristic polynomial of $DF^n$. If the image is an integral point of an integral polynomial map, this characteristic polynomial must have integral coefficients. The fixed-point example is the native-period-one instance, not an averaged or rescaled clock.

This proves Theorems F and O. $\square$

## Explicit separation witness and its ownership

The known discrete-sine cubic from Kim–Krieger–Postolache–Szeto is

$$s_3(t)=\frac{t^3-7t}{6}.$$

It is integer-valued because $t^3-t$ is divisible by $6$ for every integer $t$. For its conservative Hénon map, the ten-state cycle is represented by

$$w=(0,2,-1,-1,2,0,-2,1,1,-2).\tag{8}$$

For a direct exact check, the values at the five symbols are

$$s_3(-2)=s_3(-1)=1,\quad s_3(0)=0,\quad s_3(1)=s_3(2)=-1.$$

The neighboring sums along (8), in its displayed order, are

$$0,-1,1,1,-1,0,1,-1,-1,1,$$

which equal the corresponding $s_3$ values. Its adjacent ordered pairs are

$$(0,2),(2,-1),(-1,-1),(-1,2),(2,0),(0,-2),(-2,1),(1,1),(1,-2),(-2,0);$$

these are pairwise distinct, so the least period is exactly ten. Thus extending C428's positive-sign integer-coefficient spectrum unchanged to integer-valued cubics is false. This witness uses a source-owned family; it is a direct consequence and not a new classification.

For any positive $q$ coprime to $6$, the polynomial

$$S_q(t)=\frac{q^2t^3-7t}{6}
=q^2\binom t3+q^2\binom t2+\frac{q^2-7}{6}t$$

is in $\operatorname{Int}(\mathbb Z)$, since $q^2\equiv1\pmod6$. The rational linear map $(x,y)\mapsto(qx,qy)$ conjugates its conservative Hénon map to the map for $s_3$. The word $w/q$ therefore gives a rational ten-cycle with coordinate denominator exactly $q$. This shows that nonintegral denominators of nonfixed cycles are unbounded across the full coefficient class. Its period remains ten, so it is not an unbounded-period construction.

## Corrections or missing assumptions

No hypothesis was narrowed to establish Theorems F and O. They are explicitly separated from the original uniform question. The proposed universal normalization to an integral map acting on integer periodic points is false, even if one permits nonlinear conjugacies regular with invertible derivative at the obstructing point. The full uniform-period claim itself has not been shown false.

## Open risks and exact surviving gap

1. The lattice spacing in Theorem F degenerates with $A$. Neither (5) nor the elementary finite graph supplies a coefficient-independent state count.
2. Scaling by $A$ makes periodic coordinates integral, but transforms the cubic leading coefficient to $1/(6A)$ and generally destroys integer-valuedness of the transformed polynomial. Therefore C428 cannot be applied merely because the observed orbit coordinates have become integers.
3. C417's integer secant slope and integer third secant root are not available on the whole rational lattice. A replacement argument must control rational secants together with denominator strata; no such all-input replacement is proved here.
4. Infinitely many squareclasses and nonintegral derivative traces rule out stated normalizations, not every possible arithmetic method.
5. Source priority of these elementary auxiliary observations is not asserted. They reuse Newton interpolation, local escape, affine coefficient comparison, and derivative similarity. No mathematical execution or independent proof review has been claimed.
