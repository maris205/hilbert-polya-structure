# LY4: arithmetic helper lemmas and the unclosed full classification

Date: 2026-09-08 UTC. This is a coordinator-authored research note,
not an admitted contract, paper, priority claim, or formal evaluation.

## Claim and status

The [frozen full claim](FROZEN_CONTRACT.md) asks for every ordinary
nonzero integral periodic orbit of
$$L_a(x,y,z)=(y,z,(a+y+z)/x),\qquad a\in\mathbb Z,$$
with explicit necessary-and-sufficient families and native least periods.
Its status remains **NOT CURRENTLY JUSTIFIED**. No bounded alphabet is
substituted for that quantifier. The following auxiliary statements are
proved here, without claiming their global novelty:

1. Away from coordinates equal to $-1$, every such orbit of least period
   greater than two has two nonzero **integer** alternating 2-integrals.
2. For $a\ne1$, every such orbit meeting $-1$ is, up to rotation, the
   ordinary repeated word $(-1,b,-1,1-a-b)$.
3. There are least-period-six words with no $-1$ and unbounded height
   outside $a=1$. They disprove the frozen naive finite-core hypothesis.

Auxiliary status: **PROVABLE AS STATED**. These do not exhaust the
remaining signed integral dynamics and are not separate admissions.

## Assumptions, notation, and strategy

Write an orbit as a two-sided periodic scalar sequence $(x_i)_{i\in\mathbb Z}$
with $x_i\in\mathbb Z\setminus\{0\}$ and
$$x_i x_{i+3}=a+x_{i+1}+x_{i+2}.\tag{1}$$
Its least scalar period equals the least period of the consecutive
three-coordinate states. Words are identified only by rotation.
All products and divisions below take place in the ordinary domain;
no zero coordinate is canceled to extend an orbit. For a prime $p$,
$|\cdot|_p$ is normalized by $|p|_p=p^{-1}$.

The strategy is a parameter-free identity, a non-Archimedean diameter
argument, a separate zero-factor stratum, and a symbolic counterfamily.
The identity and 2-integral are classical, explicitly recorded in
[Cima–Gasull–Mañosa, Theorem 2(a), its proof, and §3.1](https://arxiv.org/html/0801.4360).
That source credits earlier third-order work. We derive the identity
directly so its extension to the signed ordinary domain is justified;
the source's positive-domain rotation results are not extended silently.

## Dependency map

1. Step 1 uses only (1) and nonzero coordinates; it is classical structure.
2. Step 2 uses Step 1, integer coordinates, periodicity, and exclusion of $-1$.
3. Step 3 uses Step 1, integer coordinates and periodicity, but treats $-1$
   explicitly. Its real Möbius argument is proved within the step.
4. Step 4 verifies an infinite family directly in (1). The finite run
   motivated it but is not a proof dependency.
5. The original full classification additionally needs the exhaustion
   stated in Step 5; none of Steps 1–4 supplies it.

## Proof

### Step 1. The classical parameter-free identity

Subtract (1) at indices $i$ and $i+1$. Rearrangement gives
$$x_{i+1}(x_{i+4}+1)=x_{i+3}(x_i+1).\tag{2}$$
Thus
$$\kappa_i=\frac{(x_i+1)(x_{i+2}+1)}{x_{i+1}}
\quad\hbox{satisfies}\quad \kappa_{i+2}=\kappa_i.\tag{3}$$
No division by $x_i+1$ is needed for this equality. Equivalently a
four-coordinate state has successor
$$G(x,y,z,w)=(y,z,w,w(x+1)/y-1),\qquad a=xw-y-z.\tag{4}$$
The value of $a$ is invariant because for the successor's last coordinate
$v=w(x+1)/y-1$ one has $yv-z-w=xw-y-z$. A cyclic $G$ word with
nonzero integral coordinates therefore satisfies the original recurrence
with that same integer parameter.

### Step 2. Arithmetic integrality of both 2-integrals

Assume every $x_i\ne-1$ and the least period is greater than two.
Repeat an odd period twice if necessary to work with an even cyclic
length. Let $u$ be the even-index value of $\kappa_i$ and $v$ its
odd-index value. Both are nonzero rational numbers.

Fix a prime $p$ and define the finite diameters
$$D_e=\max_{i,j\ {m even}}|x_i-x_j|_p,\qquad
D_o=\max_{i,j\ {m odd}}|x_i-x_j|_p.$$
All $x_i$ and $x_i+1$ have $p$-adic norm at most one. For any two
even indices, subtract $u x_{i+1}=(x_i+1)(x_{i+2}+1)$ and its
counterpart at $j$. The identity
$$AB-CD=(A-C)B+C(B-D)$$
and the ultrametric inequality bound the right side by $D_e$.
Taking the maximum over all such pairs yields
$$|u|_pD_o\leq D_e,\qquad |v|_pD_e\leq D_o.\tag{5}$$
The second inequality follows from the same displayed product identity
with both indices odd, so every parity has been included.

Suppose $|u|_p>1$. The equations for $u$ imply that every odd $x_i$
has $|x_i|_p<1$. Every odd $x_i+1$ is therefore a $p$-adic unit.
The equations for $v$ imply $|v|_p=1/|x_i|_p\geq1$ for every even
coordinate. Hence $|uv|_p>1$. Combining (5) gives
$$|uv|_pD_e\leq D_e.$$
It follows that $D_e=0$, and then the first inequality gives $D_o=0$.
All even coordinates are equal and all odd coordinates are equal, so
the sequence has period dividing two, a contradiction. Consequently
$|u|_p\leq1$. Interchanging the two named parities gives $|v|_p\leq1$.
This holds at every prime. A rational number integral at every finite
prime is an integer, proving $u,v\in\mathbb Z\setminus\{0\}$. $\square$

The period exclusion is essential to the argument. For a constant
integer word $t$, the value $(t+1)^2/t$ need not be integral; that
word occurs at the integer parameter $a=t^2-2t$.

### Step 3. Complete $-1$ stratum for $a\ne1$

Assume $x_0=-1$. Equation (2) and $x_1\ne0$ force $x_4=-1$;
periodicity propagates this through every index divisible by four,
in both directions. Take a common multiple of the period and four
and write its blocks as
$$(-1,b_j,c_j,d_j),\qquad d_j=-a-b_j-c_j.$$
All $b_j,c_j,d_j$ are nonzero integers. From (2) at index $4j+1$,
$$c_j(b_{j+1}+1)=-(b_j+1).\tag{6}$$

First suppose no $b_j$ is $-1$. Multiplying (6) around the block
cycle of length $m$ gives $\prod_j c_j=(-1)^m$. Since the factors
are nonzero integers, every $c_j$ is $1$ or $-1$.
If one is $-1$, its four-step propagation makes every $c_j=-1$.
Every even coordinate is now $-1$, and (1) successively gives
$$d_j=1-a-b_j,\qquad b_{j+1}=1-a-d_j=b_j.$$
The sequence is the claimed four-word. If instead every $c_j=1$,
(6) gives $b_{j+1}=-b_j-2$. The recurrence at index $4j+3$ gives
$d_j=a-1+b_{j+1}=a-b_j-3$, whereas its definition gives
$d_j=-a-b_j-1$. Thus $2a=2$, contrary to $a\ne1$.

It remains to treat a block with $b_j=-1$. Equation (6) then forces
every $b_j=-1$ by periodicity and $c_j\ne0$. The remaining block
relations are
$$d_j=1-a-c_j,\qquad c_{j+1}=\frac{a-2}{1-a-c_j}.\tag{7}$$
For $a=2$ the next $c_{j+1}$ would be zero, which is excluded. For
$a\ne2$ the Möbius map in (7) is represented by
$$A=\begin{pmatrix}0&a-2\\-1&1-a\end{pmatrix},$$
whose real eigenvalues are $-1$ and $2-a$. If $a\ne3$ they are
distinct and nonzero. A non-eigenline can be periodic under $A$
only when the quotient of these eigenvalues has finite multiplicative
order in $\mathbb R^*$, that is, is $1$ or $-1$: in an eigenbasis
the ratio of its two nonzero coordinates is multiplied by that
quotient at each iterate. The quotient is $1$ only at $a=3$ and
$-1$ only at $a=1$, both excluded in this case. Thus all periodic
points are fixed. At $a=3$, $A=-I+N$ with $N\ne0$, $N^2=0$;
for every $m>0$, $A^m=(-1)^m(I-mN)$ has exactly the same eigenline
as $A$. Periodic points are fixed in this case as well.

The fixed-point equation for (7) is
$$c^2+(a-1)c+(a-2)=(c+1)(c+a-2)=0.$$
Thus $c=-1$ or $c=2-a$, and $d$ is the other of these values.
The resulting words $(-1,-1,-1,2-a)$ and $(-1,-1,2-a,-1)$ are
rotations of the claimed family.

Conversely, for any $a\ne1$ and integer $b$ with
$b\ne0$ and $d=1-a-b\ne0$, direct substitution at the four
indices verifies $(-1,b,-1,d)$ in (1). Its least period is one
when $b=d=-1$ (necessarily $a=3$), two when $b=d\ne-1$, and
four when $b\ne d$. This proves both necessity and sufficiency
for the specified stratum. $\square$

At $a=1$ the global birational order eight is classical. The ordinary
integer locus there must still respect all nonzero-domain conditions;
we do not substitute that identity for an explicit integral atlas.

### Step 4. A symbolic, unbounded obstruction to the frozen core

For every integer $M\geq5$, set $a=M$ and consider
$$(-M,M-1,1,-2,1,M-1).\tag{8}$$
All coordinates are nonzero and none is $-1$. The six values of
$x_i x_{i+3}-x_{i+1}-x_{i+2}$ are, in order,
$$2M-(M-1)-1,\quad (M-1)-1+2,\quad
(M-1)+2-1,\quad 2M-1-(M-1),\quad
(M-1)-(M-1)+M,\quad (M-1)+M-(M-1),$$
each equal to $M$. Hence (8) satisfies the original recurrence.
The coordinate $-M$ occurs exactly once in this six-word, so no
proper divisor of six is a period. Its least period is six and its
height $\max_i|x_i|$ is $M$.

Thus there is no parameter-independent height bound after excluding
only $a=1$, the $-1$ stratum and periods at most three. This disproves
the frozen height-four hypothesis and every raised constant in that
same hypothesis. It does **not** disprove a repaired finite-core
theorem after explicitly classifying and removing further unbounded
families, such as (8). $\square$

For orientation, the hand-verified family $(r,r,-r-1)$ at $a=r^2+1$
has least period three for every integer $r\notin\{0,-1\}$.
The word $(-2,-3,-4,-3,-2)$ at $a=13$ has least period five.
Neither family is claimed to exhaust its period stratum or to be new.

### Step 5. Exact remaining obligation

On the no-$-1$ stratum put $z_i=-x_i-1$. Equations (3) become
$$z_i z_{i+2}=-\kappa_i(z_{i+1}+1).\tag{9}$$
Step 2 makes the two alternating parameters integers, but it does
not classify all ordinary integral periodic solutions of (9).
Nor does it prove that the periods observed in one finite alphabet
are the only possible periods. General Lyness coefficients cannot
be silently treated as the coefficient-free finite-type cluster
five-cycle; this distinction is explicit in
[Hone–Kouloukas, §1, equations (1.3)–(1.6)](https://doi.org/10.1007/s10801-022-01203-5).

The missing statement is a uniform exhaustion of these remaining
alternating-coefficient periodic channels, with the original
integrality, parameter, native-clock and exceptional-domain conditions.
A finite-height atlas, a few invariant fibers, or the short lemmas
above do not prove it. No closing mechanism is currently supplied.

## Computation boundary and open risks

The one frozen run is reported separately in [SCOUT_REPORT.md](SCOUT_REPORT.md).
It enumerated all cycles in its finite alphabet without a period cap;
it did not enumerate all integer or rational orbits. The infinite
counterfamily (8), not an enlarged computation, is the final falsifier.
No subsequent mathematical program is authorized by this note.

The full claim is unchanged and unclosed. The auxiliary proofs are
subject to a separate internal non-author check. No exhaustive global
priority claim, fourth admission, manuscript, zeta formula, A2 upgrade,
target Euler factor, root number or Hilbert–Pólya realization follows.
