# Bounded author deductions and explicit missing axes

Author: `/root/twenty_seventh_finite_scout`. These deductions precede any
candidate program. They are not independent review or priority claims.

## Claim, status and dependencies

For the three literals in INTAKE.md:

- **SMV static decoder, sharp five-fibre bound, fixed set and restriction
  identities: PROVABLE AS STATED.** A complete all-field temporal/recurrent
  classification is **NOT CURRENTLY JUSTIFIED**.
- **PED exact iterates, recurrent set and pointwise death time: PROVABLE AS
  STATED**, but reducible to classical duality plus Boolean erasure. No
  separate evaluated all-target inverse result is claimed.
- **RGA3 elementary scaling/stochastic/zero-fibre identities: PROVABLE AS
  STATED.** Its required temporal and all-target inverse axes are
  **NOT CURRENTLY JUSTIFIED** here.

Assumptions are exactly those in INTAKE: SMV uses an odd finite field;
PED uses any finite field and cyclic length $n\ge3$; RGA3 uses any finite
field. All coordinates update simultaneously. Root retains value/source
judgments. Dependencies: elimination and quadratic root counting for SMV;
the determinant identity and window products for PED; inverse-matrix
identities and elementary rank counting for RGA3. No pilot is a dependency.

## 1. SMV: a complete every-target inverse decoder

Write the target as $(a,b,c)\in K^3$, where $K=\mathbb F_q$ has odd
characteristic. Define the monic polynomial

$$P_{a,b,c}(Z)=(Z+c)(Z^2-1)^2-(bZ+a)(aZ+b).\tag{1}$$

Thus

$$P=Z^5+cZ^4-2Z^3-(2c+ab)Z^2+(1-a^2-b^2)Z+c-ab.$$

Define $E=\{\varepsilon\in\{1,-1\}:b=-a\varepsilon\}$.
Every predecessor belongs to exactly one of these disjoint branches:

1. For each root $z\in K\setminus\{1,-1\}$ of $P$, take
   $$x=\frac{bz+a}{z^2-1},\qquad y=\frac{az+b}{z^2-1}.\tag{2}$$
2. For each $\varepsilon\in E$ and each root $y\in K$ of
   $$\varepsilon y^2-ay-(c+\varepsilon)=0,\tag{3}$$
   take $z=\varepsilon$ and $x=\varepsilon y-a$.

### Proof of necessity and sufficiency

The first two output equations are $x=yz-a$ and $y=xz-b$.
Substitution gives $(z^2-1)y=az+b$; inserting this into the first
equation gives $(z^2-1)x=bz+a$. If $z^2\ne1$, these force (2), and
the remaining equation $xy-z=c$ becomes precisely (1). Consequently
each root in branch1 gives one predecessor and every predecessor with
$z^2\ne1$ occurs there.

If $z=\varepsilon\in\{1,-1\}$, substitution gives
$b=-a\varepsilon$ as a necessary condition. Under this condition the
first two equations are equivalent to $x=\varepsilon y-a$. The third
equation then becomes (3), proving necessity and sufficiency in branch2.
Different $z$ branches cannot intersect. Within an exceptional branch the
free coordinate $y$ distinguishes the points. This proves completeness.

### Exact fibre number and sharp maximum

Let $\chi:K\to\{-1,0,1\}$ be the quadratic character, with $\chi(0)=0$,
and let the gcd below be monic. Since $Z^q-Z$ has precisely all field
elements as distinct roots and $q$ is odd, the decoder gives

$$|F^{-1}(a,b,c)|=
\deg\gcd\!\left(P_{a,b,c}(Z),\frac{Z^q-Z}{Z^2-1}\right)
+\sum_{\varepsilon\in E}\left[1+\chi\!\left(a^2+4\varepsilon(c+\varepsilon)\right)\right].\tag{4}$$

Indeed, the gcd counts exactly the nonexceptional field roots. A quadratic
with nonzero leading coefficient has respectively two, one or zero roots
when its discriminant is a nonzero square, zero or a nonsquare; completing
the square in (3) proves the exceptional summands.

For each $\varepsilon\in E$, both factors $bZ+a$ and $aZ+b$ are
divisible by $Z-\varepsilon$. The first term of (1) has the same square
factor, so $(Z-\varepsilon)^2$ divides $P$. Distinct exceptional signs
are distinct roots because the characteristic is odd. Thus the number of
nonexceptional roots is at most $5-2|E|$. Each exceptional quadratic has
at most two roots. Therefore **every target fibre has size at most five**.

For target zero, if any input coordinate is zero, all three equations
$x=yz$, $y=xz$, $z=xy$ force the zero triple. Otherwise multiplication and
cancellation give $x^2=y^2=z^2=1$ and $xyz=1$. Conversely the four sign
triples satisfying that product do map to zero. Therefore

$$F^{-1}(0)=\{(0,0,0)\}\cup
\{(\epsilon_1,\epsilon_2,\epsilon_3):\epsilon_i\in\{1,-1\},
\epsilon_1\epsilon_2\epsilon_3=1\},\tag{5}$$

and the maximum five is attained over **every odd finite field**. No claim
that zero is the unique maximizing target is made. Formula (4), rather
than a sample count, applies to every target including exceptional ones.

## 2. SMV: proved temporal restrictions, not a global classification

The fixed-point equations are $yz=2x$, $zx=2y$, $xy=2z$. If any
coordinate is zero, invertibility of $2$ forces all three to vanish.
Otherwise cancellation gives $x^2=y^2=z^2=4$ and $xyz=8$. Conversely
these conditions suffice. The fixed set therefore consists of zero and
the four triples $(2\epsilon_1,2\epsilon_2,2\epsilon_3)$ with sign product
one. It has exactly five elements for every allowed field.

Differences satisfy the exact identities

$$F_1-F_2=-(z+1)(x-y),\quad
F_2-F_3=-(x+1)(y-z),\quad
F_3-F_1=-(y+1)(z-x).\tag{6}$$

Expanding the displayed update proves each identity. In particular equality
of any pair persists, but in a finite field a nonzero multiplier is not a
contractive potential. The diagonal is invariant and its literal update is

$$F(t,t,t)=(t^2-t,t^2-t,t^2-t).\tag{7}$$

Over $\mathbb F_{17}$, the diagonal values $3\mapsto6\mapsto13\mapsto3$
are distinct, since $3^2-3=6$, $6^2-6=30=13$ and $13^2-13=156=3$
modulo17. Thus a claim of fixed-point-only recurrence is false. No complete
cycle/depth classification for either the full carrier or all diagonal
quadratic maps is proved here. Equations (5)–(7) do not fill that gap.

For the Markoff polynomial $M=x^2+y^2+z^2-xyz$, one has
$M(1,1,1)=2$ but $M(F(1,1,1))=M(0,0,0)=0$. Hence SMV does not preserve
the ordinary Markoff level sets. Each separate coordinate Vieta move is an
involution, so every composition is bijective. Equation (5) makes SMV
noninjective. This excludes equality and bijective conjugacy with those
compositions, without asserting the absence of all other old adapters.

## 3. PED: exact iterates expose the rejected wrapper

Let $P=(P_i)$ be any carrier state. Put $E_i=D(P)_i$, and define
$b_i=1$ if the representatives of $P_i,P_{i+1},P_{i+2}$ are independent;
put $b_i=0$ otherwise, including any zero input. Indices are modulo $n$.
For a Boolean $e$, notation $eP$ means $P$ if $e=1$ and the adjoined
zero if $e=0$; it is not multiplication of projective coordinates.

For every integer $t\ge1$ the following exact formula holds:

$$D^{2t}(P)_i=\left(\prod_{j=0}^{2t-2}b_{i+j}\right)P_{i+t},\qquad
D^{2t+1}(P)_i=\left(\prod_{j=0}^{2t-1}b_{i+j}\right)E_{i+t}.\tag{8}$$

### Determinant identity and induction

For vectors $u,v,w\in K^3$, the coordinate determinant identity is

$$(u\times v)\times(v\times w)=\det(u,v,w)v.\tag{9}$$

It follows either by expanding the three coordinates or by the vector
triple-product formula, whose polynomial identity is valid in every
characteristic. If the determinant is nonzero, projectivization gives
$D^2(P)_i=P_{i+1}$; if it is zero, both sides of (9) vanish, including
the zero-vector or dependent cases. Thus (8)'s even formula holds at
$t=1$. Applying $D$ to that formula multiplies the two adjacent Boolean
windows, giving its odd formula.

For the even induction, suppose $D^{2t}(P)_i=B_iP_{i+t}$, where
$B_i=\prod_{j=0}^{2t-2}b_{i+j}$. Applying (9) to this state gives the
Boolean coefficient $B_iB_{i+1}B_{i+2}b_{i+t}$. The first three windows
have union $b_i,\ldots,b_{i+2t}$; the index $i+t$ is already included.
The product is therefore $\prod_{j=0}^{2t}b_{i+j}$, establishing the
even formula for $t+1$. Repeated indices modulo $n$ cause no problem,
because Boolean products are idempotent. This proves (8) for all $t$.

### Recurrent set and death time

If all $b_i=1$, equations (8) and (9) imply $D^{2n}(P)=P$.
Consequently these states are recurrent and their periods divide $2n$.
The all-zero state is fixed. If some $b_i=0$, let $L$ be the maximum
cyclic run length of ones in $b$, setting $L=0$ when all bits are zero.
For $k\ge2$, (8) implies that $D^k(P)$ has a nonzero coordinate exactly
when a Boolean window of length $k-1$ is all ones. To justify the converse
without assuming nonzero labels, an all-one window in the even formula
contains a triple involving $P_{i+t}$; in the odd formula it contains a
triple involving the edge $E_{i+t}$. Thus that indicated label is nonzero.
The condition is precisely $k-1\le L$.

It follows that every nongeneric state reaches zero. Its exact entrance
time is zero if $P=0$; one if $P\ne0$ and $D(P)=0$; otherwise it is
**$L+2$**. Indeed the last case has nonzero time1, and (8) determines all
later nonzero times. Therefore the recurrent set is exactly zero together
with the all-independent-triple core. The height is at most $n+1$; no
all-$(n,q)$ sharpness assertion is required or made.

The time information is entirely the old adjacent-edge duality shift plus
an expanding AND window. This is precisely a Boolean-erasure factor, not
a new geometric temporal mechanism. For inverse counting, the formal
compatibility matrices indexed by carrier points give a trace of a product,
but that generic finite-constraint encoding is not an evaluated all-target
fibre law and is not claimed as a second residual. PED stops negatively.

## 4. RGA3: elementary facts do not supply the required axes

For an invertible $A$, inverse multiplication gives

$$\sum_j R(A)_{ij}=\sum_j a_{ij}(A^{-1})_{ji}=1,
\qquad \sum_iR(A)_{ij}=1.\tag{10}$$

For invertible diagonal matrices $D,E$,
$(DAE)^{-1}=E^{-1}A^{-1}D^{-1}$. Its entrywise pairing with $DAE$
cancels both diagonal factors, proving $R(DAE)=R(A)$. Applying inverse
and transpose definitions also gives
$R(A^{-1})=R(A)^{\mathsf T}=R(A^{\mathsf T})$.
These are elementary classical RGA identities, not candidate contributions.

Equation (10) prevents any invertible input from mapping to the zero
matrix. By the literal totalization all singular inputs do map there.
Choosing independent columns in succession counts
$|\mathrm{GL}_3(K)|=(q^3-1)(q^3-q)(q^3-q^2)$, so

$$|R^{-1}(0)|=q^9-(q^3-1)(q^3-q)(q^3-q^2).\tag{11}$$

This is only a classical rank count for one special target. It does not
evaluate all nonzero fibres or their scaling quotients, and it does not
classify finite-field recurrence. Neither the known real-matrix convergence
theorem nor adding the zero branch settles those missing claims. RGA3
therefore stops without a pilot or gate.

## Open risks and no promotion

The source search does not establish that SMV's degree-five inverse result
is new. Its essential full-carrier temporal theorem remains unproved.
PED's complete time theorem is rejected on mechanism grounds; RGA3 lacks
both required complete axes after old facts are deducted. No conjunction
meeting the candidate gate is claimed, and no all-size conclusion will be
inferred from the one bounded SMV pilot.
