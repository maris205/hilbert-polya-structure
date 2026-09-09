# SF2: exact symmetry restriction and a one-way specialization test

## Claim and status

The frozen question is SF2 in [REPORT.md](REPORT.md). It remains
**NOT CURRENTLY JUSTIFIED**. This package proves an exact restriction
of its quadratic character and a sufficient two-parameter test; it
does not prove that test.

Throughout, $k=\mathbb Q(A,B,C,D)$ and $T=s_zs_ys_x$ are the unchanged
Fricke family and native clock. Let $E/k$ be FG2's degree-$11$ cycle
field. Its discriminant squareclass is $d_2$; its phase-norm squareclass
is $p_2$. Thus $k(\sqrt{d_2})$ is the cycle-sign field, while
$k(\sqrt{p_2})$ is the total-phase-parity field. These symbols are
squareclasses, not point cardinalities.

Write $\Sigma=\{A=B=0\}$ and $K=\mathbb Q(C,D)$. A restricted character
means pullback of a finite étale character cover to the generic point
of $\Sigma$, not blind substitution into a rational discriminant
representative which might have a zero denominator there.

The accepted inputs are FG2's full two-cycle presentation, its
twenty-two étale point sheets at $(0,0,0,1)$, and C4's reviewed NI
all-sheet continuation at $(0,0,0,4)$ for every exact period $n\ge3$.
No higher-layer Galois group is presumed maximal.

## Strategy

1. Decompose all eleven cycle labels on $\Sigma$ into finite étale
   algebras of dimensions $1,2,4,4$, treating the omitted chart.
2. Compute trace discriminants of the point and cycle algebras.
3. Use NI only to make each finite higher splitting cover specialize
   legitimately to $\Sigma$, then transport any hypothetical inclusion.
4. Retain the distinction between a sufficient specialization test
   and an actual answer to SF2.

## 1. The two-parameter character restriction

**Proposition 1.** On $\Sigma$, the two FG2 quadratic characters have
squareclasses

$$
\left.d_2\right|_\Sigma=[D^2-C^2],\qquad
\left.p_2\right|_\Sigma=[C^2+4D]
\quad\text{in }K^\times/K^{\times2}.
\tag{1}
$$

Both are nontrivial, and they are independent. The same statements
hold over $\overline{\mathbb Q}(C,D)$.

### 1.1 Why the restriction is well defined

FG2 gives all twenty-two point sheets as distinct and étale over
the full parameter base at $(0,0,0,1)$. That point lies on $\Sigma$.
Hence a nonempty open subset of $\Sigma$ belongs to the finite étale
locus for the point and cycle covers. Their pullbacks to the generic
point of $\Sigma$ have dimensions $22$ and $11$, respectively.
Formation of the trace form, its determinant squareclass and the
sign character commute with this étale base change.
The generic surface on $\Sigma$ is smooth, since the same $D=1$
point is smooth. FG2 identifies $T$-fixed points with surface
critical points, so every constructed $T^2$ point is of exact
native period two at this generic point.

This step uses the whole FG2 sheet inventory, not the presence of
one simple point in a nonnormal cover.

### 1.2 The finite-$q$ chart: one plus four plus four cycles

Use the accepted cycle coordinates

$$
A=X-qYZ,\quad B=Y-qXZ,\quad C=Z-qXY,\quad
D=q(XYZ-X^2-Y^2-Z^2).
\tag{2}
$$

Their point phases are given by $\delta^2=1-4q$. On $\Sigma$,
if $X=0$ then $Y=0$. There is one cycle

$$
X=Y=0,\qquad Z=C,\qquad q=-D/C^2.
\tag{3}
$$

It is the $z$-axis cycle, whose two points have coordinates
$z$ satisfying $z^2-Cz-D=0$.

If $X\ne0$, the first two equations give $q^2Z^2=1$. Choose
$\varepsilon\in\{1,-1\}$. Then

$$
Z=\varepsilon/q,\qquad Y=\varepsilon X,\qquad
X^2=\frac{1-\varepsilon Cq}{q^2},
\tag{4}
$$

and the last equation becomes

$$
h_\varepsilon(q):=
(D-2\varepsilon C)q^2+(3+\varepsilon C)q-1=0.
\tag{5}
$$

Let $Q_\varepsilon=K[q]/(h_\varepsilon)$ and let

$$
B_\varepsilon=
Q_\varepsilon[X]\Big/\left(
X^2-\frac{1-\varepsilon Cq}{q^2}\right).
\tag{6}
$$

They have dimensions two and four over $K$. They are finite étale:
the quadratic discriminant
$C^2-2\varepsilon C+9+4D$ is nonzero; $q$ and
$1-\varepsilon Cq$ are units at the generic point. The two signs
therefore contribute four cycle labels each.
Their phase functions are also nonzero: substituting $q=1/4$ in
$16h_\varepsilon(q)$ gives $D+2\varepsilon C-4\ne0$.

### 1.3 The omitted chart supplies two more cycles

FG2's row ratio $r=-1$ is omitted by the finite-$q$ chart. In physical
coordinates its second point is $(-x,-y,-z)$. The accepted first-return
equations specialize to

$$
yz=xz=0,\qquad xy=-C.
\tag{7}
$$

Since $C$ is nonzero in $K$, this forces $z=0$ and $xy=-C$.
The surface equation is $x^2+y^2=D$. Modulo the phase
$(x,y)\mapsto(-x,-y)$, the coordinate $\xi=x^2$ gives the two-cycle
algebra

$$
B_0=K[\xi]/(\xi^2-D\xi+C^2).
\tag{8}
$$

Indeed $y=-C/x$, so $\xi$ determines the unordered pair of points.
The discriminant $D^2-4C^2$ is nonzero. The point extension over
$B_0$ is obtained by adjoining $x$ with $x^2=\xi$.

Equations (3), (6) and (8) give eleven distinct generic cycle labels.
They exhaust the rank-$11$ étale pullback already established in
§1.1. Consequently its algebra is exactly

$$
B_\Sigma=K\times B_0\times B_+\times B_-.
\tag{9}
$$

No chart component or cycle multiplicity is discarded.

### 1.4 A trace-form calculation

Let $R/K$ be a finite étale algebra of dimension $b$, and let
$a\in R^\times$. For $R[s]/(s^2-a)$, use a $K$-basis $e_i$ of $R$
and the basis $e_i,se_i$ of the quadratic algebra. Its trace matrix
is block diagonal with blocks

$$
2\bigl(\operatorname{Tr}_{R/K}(e_ie_j)\bigr),\qquad
2\bigl(\operatorname{Tr}_{R/K}(ae_ie_j)\bigr).
$$

The second determinant is the first trace determinant multiplied
by $\operatorname{Norm}_{R/K}(a)$: its matrix is obtained by composing
with multiplication by $a$. Thus the discriminant squareclass of
the quadratic algebra over $K$ is

$$
\left[\operatorname{Norm}_{R/K}(a)\right],
\tag{10}
$$

because the other factors are $2^{2b}$ and a squared trace determinant.
Also, discriminants of direct-product algebras multiply, since their
trace matrices are block diagonal.

Apply (10) to (6). Modulo squares, the contribution is

$$
\operatorname{Norm}_{Q_\varepsilon/K}(1-\varepsilon Cq)
=\frac{D+\varepsilon C}{D-2\varepsilon C}.
\tag{11}
$$

To verify the equality, the roots $q_1,q_2$ of (5) satisfy

$$
q_1+q_2=-\frac{3+\varepsilon C}{D-2\varepsilon C},
\qquad q_1q_2=-\frac{1}{D-2\varepsilon C}.
$$

Expanding $(1-\varepsilon Cq_1)(1-\varepsilon Cq_2)$ gives (11).
The denominator $q^2$ in (6) contributes a square norm.
Combining (8), (9) and (11), the cycle discriminant is

$$
(D^2-4C^2)
\frac{D+C}{D-2C}\frac{D-C}{D+2C}
=D^2-C^2
\quad\bmod K^{\times2}.
\tag{12}
$$

### 1.5 The independent phase character

The discriminant character of the twenty-two-point permutation
representation equals FG2's total phase parity: exchanging two
two-point blocks is even, and a flip within one block is odd.
It therefore computes the restricted class of $p_2$ without
substituting $q=\infty$ in its original norm expression.

The point cover of (3) has discriminant $C^2+4D$. For (8), formula
(10) gives $\operatorname{Norm}_{B_0/K}(\xi)=C^2$, a square.
For each (6), the point phase has equation $\delta^2=1-4q$ and

$$
\operatorname{Norm}_{B_\varepsilon/K}(1-4q)
=\operatorname{Norm}_{Q_\varepsilon/K}(1-4q)^2,
$$

again a square. The total point discriminant class is consequently
$[C^2+4D]$, proving the second identity in (1).

The class $D^2-C^2$ has odd valuation on $D=C$, whereas $C^2+4D$
has valuation zero there. The latter has odd valuation on
$C^2+4D=0$, where the former has valuation zero. These distinct
prime divisors prove independence over both stated constant fields.
This completes the proof of Proposition 1. $\square$

## 2. The fully symmetric line is blind to the cycle sign

**Corollary 2.** On $\Lambda=\{A=B=C=0\}$, with generic parameter
$D$, the cycle-sign character is trivial. The phase character has
squareclass $[D]$.

**Proof.** The generic point of $\Lambda$ belongs to the same
étale locus by the FG2 point at $D=1$. Restricting (1) gives
$[D^2]=1$ and $[4D]=[D]$.

The direct cycle-label explanation is also explicit in FG2:
three axis cycles are defined over $\mathbb Q(D)$, and the other
eight labels are four copies of the two roots of
$Dq^2+3q-1=0$. Their nontrivial root interchange performs four
transpositions and has positive sign. $\square$

The limitation persists in formal transverse germs. For example,
over $\mathbb Q(D)[[C]]$ the unit $D^2-C^2$ has the square root
$D\sqrt{1-C^2/D^2}$, obtained uniquely by Hensel lifting the root
$D$ at $C=0$. Thus even the full formal germ at that symmetric
line does not certify global nontriviality or exclusion of $F_2$.
This is a failure of that test, not a counterexample to SF2.

## 3. A legitimate sufficient test on the two-parameter slice

For each $n\ge3$, let $M_n/K$ be the splitting field obtained by
restricting the generic exact-$n$ point cover to the generic point
of $\Sigma$. These are the specialized native-coordinate fields.
Their definition here does not assume any wreath-group attainment.

**Proposition 3.** If

$$
K(\sqrt{D^2-C^2})\not\subseteq M_3\cdots M_N
\quad\text{for every finite }N\ge3,
\tag{ST}
$$

then SF2 holds over $k$. The analogous geometric condition over
$\overline{\mathbb Q}(C,D)$ implies geometric SF2.

**Proof.** The accepted NI all-sheet theorem makes the entire splitting
normalization of each $L_n$, $n\ge3$, étale at $(0,0,0,4)$.
It also provides distinct exact-$n$ point continuations there.
Since this point lies on the irreducible $\Sigma$, the generic point
of $\Sigma$ belongs to the corresponding étale and distinct-sheet
locus. For any fixed finite $N$, intersecting those finitely many
open loci still contains that generic point. No common open locus
for infinitely many $n$ is asserted.

The $F_2$ cover is étale at the generic point of $\Sigma$ by
§1.1, and its pullback is the field $K(\sqrt{D^2-C^2})$ by
Proposition 1. Suppose $F_2\subseteq L_3\cdots L_N$. Normalize
a common open neighborhood of the generic point of $\Sigma$ in
these fields. The inclusion gives a morphism of finite étale
covers, which remains a morphism after restriction to $\Sigma$.
Any connected component of the higher restricted cover therefore
contains the restricted $F_2$ field in its function field.

For completeness, the residual splitting field of each component
is generated by the specialized point coordinates. A residual
automorphism fixing all those coordinates fixes every specialized
point. Their distinctness then makes its lift fix every generic
point label. The generic field was generated by those coordinates,
so that lift is the identity. Étaleness removes inertia. Hence
there is no additional residual subextension beyond the coordinate
splitting field. Applied simultaneously to $3,\ldots,N$, this
identifies the component field with $M_3\cdots M_N$, up to the
chosen compatible embedding.

Thus the hypothetical inclusion implies
$K(\sqrt{D^2-C^2})\subseteq M_3\cdots M_N$, contrary to (ST).
The geometric proof uses the same finite étale argument after
extending constants. $\square$

The use of the *whole* normal splitting cover and all distinct point
coordinates in this argument is necessary. One simple root or one
unramified place would not justify specializing the claimed inclusion.

## 4. A higher-layer character created by the slice symmetry

There is additional structure on $\Sigma$ which has no analogue
over the full four-parameter generic field. Define
$g(x,y,z)=(-x,-y,z)$. Substitution into the three Vieta involutions,
with $A=B=0$, shows that $g$ commutes with each one and hence with
$T$. Its fixed locus on the surface is $x=y=0$. There $T$ sends
$z$ to $C-z$, so every such point has native period at most two.

The specialized sheet set is preserved as well: on the full family,
$g$ accompanied by $(A,B,C,D)\mapsto(-A,-B,C,D)$ intertwines the
three involutions. It preserves the closure of the generic exact-$n$
incidence and fixes $\Sigma$ on the base. Thus it acts on the
restricted sheet set used to define $M_n$, without an assumption
about any extra vertical incidence components.

**Proposition 4.** For every odd $n\ge3$, the actions of $g$ and
$T$ generate a free cyclic action of order $2n$ on the specialized
exact-$n$ point set. Put $\nu_n=|P_n|$ and $s_n=\nu_n/(2n)$.
Besides the native cycle-sign character, there is a canonical
quadratic character $\psi_n$ given by the sign of the permutation
of the $s_n$ orbits of $\langle g,T\rangle$. Equivalently,
$\psi_n$ is the trace-discriminant character of that orbit algebra.
It is defined without any full Galois-group hypothesis; it is
allowed to be trivial on the actual Galois image.

**Proof.** If $gP=T^jP$, applying $g$ twice and using commutation
gives $T^{2j}P=P$. Since $n$ is odd, $n\mid j$, so $gP=P$.
The preceding fixed-locus calculation excludes this for $n\ge3$.
Thus no $g$-translate of a native cycle is the same native cycle.
The two native cycles together form one free orbit of
$\langle g,T\rangle=C_2\times C_n$.

More explicitly, $h=gT$ has order $2n$ on every point, with
$h^n=g$ and $h^{n+1}=T$. It gives the claimed free cyclic action.
All maps are defined over $K$, so the actual Galois image commutes
with $h$. It embeds into $C_{2n}\wr S_{s_n}$ in this labeling,
irrespective of whether that upper bound is attained. The sign
of the permutation on its $h$-orbits is the character $\psi_n$.
The quotient finite étale algebra is defined over $K$, and its
trace discriminant computes exactly this permutation sign.
$\square$

This has an exact character consequence. Write an element of the
ambient centralizer as $(a_1,\ldots,a_{s_n};\sigma)$, with
$a_i\in\mathbb Z/(2n)$. Then

$$
\chi_{\mathrm{native\ cycle},n}
=(-1)^{\sum_i a_i},\qquad
\psi_n=\operatorname{sgn}(\sigma).
\tag{13}
$$

Indeed, one $h$-orbit consists of two $T$-cycles, distinguished by
the parity of the $h$-exponent. Rotation by $a_i$ interchanges
them exactly when $a_i$ is odd. Permuting two whole $h$-orbits
interchanges two pairs of native cycle labels and is even on the
native cycle set. This proves (13).

In the ambient centralizer the two characters in (13) are
independent: a single odd rotation and a transposition of two
$h$-orbits give their separate signs. Here $s_n\ge2$ by the accepted
ordinary counts. In contrast, for odd $n$ the only nontrivial
quadratic character of the original native upper bound
$C_n\wr S_{2s_n}$ is native cycle sign, by the accepted R2
abelianization. Consequently the ambient pair-orbit sign
$\psi_n$ does not extend to that original upper bound.

No independence or nontriviality of $\psi_n$ on the actual
specialized Galois image follows. The precise point is that even
this actual Fricke symmetry supplies an additional canonical
character test which native phase and cycle signs alone do not
exhaust. It would be unsound to use their vanishing as a proof
of (ST).

## 5. Exact residual obligation and failed shortcuts

Condition (ST) is **not proved** in this package. Its quadratic
character ramifies at the two slice divisors $D=C$ and $D=-C$.
The phase character instead has branch $C^2+4D=0$. This distinction
locates the question but does not say how the actual higher fields
$M_n$ ramify at $D=\pm C$.

The following proposed shortcuts are not used:

- The full sign-symmetric line cannot detect $F_2$, by Corollary 2.
- The character identities in Proposition 1 do not classify all
  quadratic characters of unknown higher-layer groups.
- Even if every familiar higher cycle/phase character were trivial
  on a selected inertia element, that would not prove that the
  entire higher compositum has no quadratic quotient carrying it.
- An inclusion found only after specializing would not refute SF2.
  For instance, over $\mathbb Q(a,C,D)$ the quadratic fields
  obtained from $f=D^2-C^2$ and $f+a$ are distinct (their ratio has
  odd valuation on $a=-f$), but coincide on $a=0$. Both specialize
  étale at the generic point of that slice.
- A finite number of tested $M_n$ cannot establish (ST) for all $N$.

At the slice branch $D=-\varepsilon C$, the finite-$q$ equations
give $q=\varepsilon/C$, $X=Y=0$, $Z=C$. Two nonaxis labels meet
the axis label there. This is a symmetry-enhanced collision; it
is not by itself the isolated smooth fold of FG2. C4 separately
owns the global critical-divisor and whole-higher-cover argument.
No identification with that divisor is assumed in this proof.

## Ownership and execution

The symmetry family and special quadratic transformations are
source-owned by the literature recorded in REPORT. The FG2 cycle
chart and omitted-chart equations are accepted earlier inputs.
Trace-form determinants and specialization of finite étale covers
are classical. The new interface is the exact restricted pair
$(d_2,p_2)$ and its legitimate one-way use for the still-open SF2.
It is auxiliary, not a complete tower-independence theorem or a
new-paper admission.

Zero mathematical programs, old reruns, PDF builds, Git writes,
shared-index edits or external-model uploads were performed.
