# R058 Hyperbolic-Survivor Theorem Audit

## Claim

Let

$$
H(x,y)=(1-6x^2-y,x)
$$

and define

$$
X_-=[-5/8,-1/3],\qquad X_+=[1/3,5/8],
$$

$$
Y_-=[-81/128,-5/16],\qquad
Y_+=[5/16,81/128].
$$

For $s,t\in\{-,+\}$ put $N_{st}=X_s\times Y_t$.  In the state order
$--,-+,+-,++$, let

$$
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
$$

Then there is a nonempty compact $H$-invariant set

$$
\Lambda\subset \bigcup_{s,t}N_{st}
$$

such that:

1. $\Lambda$ is uniformly hyperbolic;
2. the state itinerary defines a continuous surjection

   $$
   \pi:(\Lambda,H)\longrightarrow(\Sigma_A,\sigma);
   $$

3. consequently,

   $$
   h_{\mathrm{top}}(H|_\Lambda)
   \ge \log\rho(A)
   =\log\frac{1+\sqrt5}{2}.
   $$

Here $\Sigma_A$ is the two-sided subshift of finite type defined by $A$.

## Status

**PROVABLE AS STATED.**

The R058 claim survives unchanged.  The proof needs four logically separate
ingredients: exact rectangular covering relations, exact exclusion of all
other one-step transitions, a finite-chain-to-bi-infinite realization
argument, and a two-sided strict cone criterion.  None of these ingredients
may be replaced by finite graph incidence alone.

## Assumptions

- The four rectangles are treated as h-sets with one horizontal exit
  coordinate and one vertical entry coordinate.
- A covering relation uses the standard homotopy/degree definition.  In
  normalized coordinates, the homotopy must avoid the target entry boundary,
  and the source exit boundary must remain outside the target rectangle.
- The finite-chain theorem for covering relations is used in its usual form:
  a finite chain of h-set coverings with nonzero degree realizes an orbit
  segment through the listed h-sets.
- Uniform hyperbolicity is measured in the fixed anisotropic max norm induced
  by the common horizontal and vertical half-widths.  This norm is equivalent
  to the Euclidean norm.
- The ambient survivor box is

  $$
  \Omega_R=[-R,R]^2,\qquad
  R=\frac{3190032397181517}{5000000000000000}.
  $$

## Notation

The common half-widths of the h-sets are

$$
\alpha=\frac7{48},\qquad \beta=\frac{41}{256},
$$

and their ratio is

$$
r=\frac\beta\alpha=\frac{123}{112}.
$$

For a tangent vector $(\delta x,\delta y)$ write its normalized coordinates
as

$$
(u,v)=\left(\frac{\delta x}{\alpha},
             \frac{\delta y}{\beta}\right),
\qquad
\|(u,v)\|_\infty=\max(|u|,|v|).
$$

With $\kappa=1/2$, define the constant cones

$$
\mathcal C^u=\{(u,v):|v|\le\kappa|u|\},
\qquad
\mathcal C^s=\{(u,v):|u|\le\kappa|v|\}.
$$

The two cones meet only at the zero vector.

## Proof Strategy

First prove the six directed h-set coverings by exact endpoint inequalities
and an explicit normalized homotopy.  Then exclude the remaining ten state
pairs by the exact identity $H_y=x$ and one exact upper bound on $H_x$.
Finite covering chains give orbit segments; compactness upgrades these to
orbits for every admissible bi-infinite word.  Finally, strict forward and
backward cone invariance supplies a continuous invariant splitting and
uniform expansion/contraction.  The itinerary map is then a factor map onto
the four-state subshift, yielding the entropy lower bound.

## Dependency Map

1. Lemma 1 proves that all four h-sets are disjoint and lie inside $\Omega_R$.
2. Lemma 2 gives the exact horizontal endpoint ranges and the six covering
   relations.
3. Lemma 3 excludes the ten forbidden transitions.
4. Lemma 4 constructs an explicit covering homotopy and records its nonzero
   degree.
5. Lemma 5 proves the exact forward unstable cone bound and expansion.
6. Lemma 6 proves the exact backward stable cone bound and expansion.
7. Lemma 7 applies finite-chain realization and compactness to every
   bi-infinite admissible word.
8. Lemma 8 constructs the invariant splitting and proves uniform
   hyperbolicity.
9. The factor-entropy inequality and the exact characteristic polynomial of
   $A$ give the final entropy bound.

## Proof

### Lemma 1: h-set geometry and ambient containment

The four rectangles are pairwise disjoint, $X_s$ is strictly contained in
the interior of $Y_s$ for each sign, and every rectangle lies in $\Omega_R$.

**Proof.** The positive-side endpoint comparisons are

$$
\frac5{16}<\frac13<\frac58<\frac{81}{128},
$$

because $15/48<16/48$ and $80/128<81/128$.  Reflection gives the
negative-side comparisons.  The positive and negative $X$ intervals are
disjoint, as are the positive and negative $Y$ intervals, so the four product
rectangles are pairwise disjoint.

The largest absolute endpoint is $81/128$.  Exact cross multiplication gives

$$
128\cdot3190032397181517
=408324146839234176
>405000000000000000
=81\cdot5000000000000000.
$$

Thus $81/128<R$, proving that every $N_{st}$ is contained in the interior of
$\Omega_R$.  The smaller of the two same-sign entry margins is

$$
\min\left(\frac13-\frac5{16},
          \frac{81}{128}-\frac58\right)
=\min\left(\frac1{48},\frac1{128}\right)
=\frac1{128}.
$$

$\square$

### Lemma 2: exact exit crossing

The following six coverings hold:

$$
N_{--}\Longrightarrow N_{--},\ N_{+-},
\qquad
N_{-+}\Longrightarrow N_{--},
$$

$$
N_{+-}\Longrightarrow N_{-+},\ N_{++},
\qquad
N_{++}\Longrightarrow N_{-+}.
$$

Their smallest horizontal exit-crossing margin is $1/48$.

**Proof.** At either inner horizontal endpoint $|x|=1/3$,

$$
H_x(x,y)=\frac13-y,
$$

whereas at either outer endpoint $|x|=5/8$,

$$
H_x(x,y)=-\frac{43}{32}-y.
$$

For $y\in Y_-$ these ranges are

$$
\frac13-Y_-
=\left[\frac{31}{48},\frac{371}{384}\right],
\tag{1}
$$

$$
-\frac{43}{32}-Y_-
=\left[-\frac{33}{32},-\frac{91}{128}\right].
\tag{2}
$$

The whole interval in (1) lies to the right of $X_+$ because

$$
\frac{31}{48}-\frac58=\frac1{48}>0,
$$

and the whole interval in (2) lies to the left of $X_-$ because

$$
-\frac58-\left(-\frac{91}{128}\right)
=\frac{11}{128}>0.
$$

Hence a source with $y$-sign negative crosses both target $X$ intervals.

For $y\in Y_+$ the corresponding ranges are

$$
\frac13-Y_+
=\left[-\frac{115}{384},\frac1{48}\right],
\tag{3}
$$

$$
-\frac{43}{32}-Y_+
=\left[-\frac{253}{128},-\frac{53}{32}\right].
\tag{4}
$$

The lower endpoint in (3) lies to the right of the right endpoint of $X_-$:

$$
-\frac{115}{384}-\left(-\frac13\right)
=\frac{13}{384}>0,
$$

while (4) lies strictly to the left of $X_-$.  Therefore a source with
$y$-sign positive crosses $X_-$.

The second image coordinate is $H_y=x$.  Lemma 1 gives

$$
H_y(N_{st})=X_s\subset\operatorname{int}Y_s,
$$

with minimum margin $1/128$.  Thus the target entry sign must equal the source
$x$-sign.  Combining this fact with (1)--(4) gives exactly the six listed
state pairs.  Among their horizontal inequalities, the smallest margin is
$1/48$.  $\square$

### Lemma 3: exact exclusion of the other ten transitions

If $A_{ij}=0$, then $H(N_i)\cap N_j=\varnothing$.

**Proof.** Eight forbidden pairs have target entry sign different from the
source $x$-sign.  They are impossible because $H_y=x\in X_s$ and $X_s$ is
disjoint from the opposite-sign $Y$ interval.

The remaining two forbidden pairs have a positive source $y$-sign, the
correct target entry sign, and target horizontal interval $X_+$.  On either
such source rectangle, the maximum possible first image coordinate occurs at
$|x|=1/3$ and $y=5/16$ and equals

$$
1-6\left(\frac13\right)^2-\frac5{16}
=\frac1{48}<\frac13=\inf X_+.
$$

Thus these two images do not meet $X_+$, with exact gap $5/16$.  This excludes
all ten zero entries of $A$.  $\square$

### Lemma 4: the crossings are covering relations of nonzero degree

Each of the six crossings in Lemma 2 is an h-set covering relation.  Its
degree is $+1$ for a source with $x$-sign negative and $-1$ for a source with
$x$-sign positive.

**Proof.** Map every source and target rectangle affinely to
$[-1,1]^2$, preserving the horizontal and vertical coordinate orientations.
Write the normalized map as $F=(F_u,F_s)$.

For a negative-$x$ source, the left exit edge is $x=-5/8$ and Lemma 2 gives
$F_u<-1$ there; the right exit edge is $x=-1/3$ and gives $F_u>1$ there.
For a positive-$x$ source the order reverses: $F_u>1$ on the left exit edge
$x=1/3$ and $F_u<-1$ on the right exit edge $x=5/8$.  On the entire source,
Lemma 1 gives $|F_s|<1$.

Let $\varepsilon=+1$ for a negative-$x$ source and $\varepsilon=-1$ for a
positive-$x$ source.  The explicit homotopy

$$
\mathcal H_\tau(u,v)
=\bigl((1-\tau)F_u(u,v)+2\tau\varepsilon u,
       (1-\tau)F_s(u,v)\bigr),
\qquad 0\le\tau\le1,
\tag{5}
$$

keeps the source exit edges horizontally outside the target because each
convex combination in the first component remains on the same strict side of
$[-1,1]$.  Its second component stays strictly inside $(-1,1)$, so the
homotopy never meets the target entry boundary.  At $\tau=1$ the map is

$$
(u,v)\longmapsto(2\varepsilon u,0),
$$

whose one-dimensional Brouwer degree is $\varepsilon\ne0$.  These are exactly
the defining conditions of the covering relation.  $\square$

### Lemma 5: forward unstable cone invariance and expansion

For every $z=(x,y)$ in the union of the four h-sets,

$$
DH_z(\mathcal C^u\setminus\{0\})
\subset\operatorname{int}\mathcal C^u,
$$

and every vector in $\mathcal C^u$ expands in the normalized max norm by at
least

$$
\lambda_u=\frac{773}{224}>1.
$$

**Proof.** In normalized tangent coordinates,

$$
\widehat {DH}_z
=\begin{pmatrix}
-12x&-r\\
r^{-1}&0
\end{pmatrix}
=\begin{pmatrix}
-12x&-123/112\\
112/123&0
\end{pmatrix}.
$$

If $(u,v)\in\mathcal C^u$, then $|v|\le|u|/2$ and $|x|\ge1/3$, so

$$
|u'|
\ge \left(4-\frac{123}{224}\right)|u|
=\frac{773}{224}|u|,
\tag{6}
$$

while

$$
|v'|=\frac{112}{123}|u|.
$$

Consequently,

$$
\frac{|v'|}{|u'|}
\le
\frac{112/123}{773/224}
=\frac{25088}{95079}
<\frac12.
\tag{7}
$$

For a nonzero vector in $\mathcal C^u$,
$\|(u,v)\|_\infty=|u|$; (6) proves the stated expansion.  $\square$

### Lemma 6: backward stable cone invariance and expansion

For every $Z=(X,Y)$ in the union of the four h-sets,

$$
DH_Z^{-1}(\mathcal C^s\setminus\{0\})
\subset\operatorname{int}\mathcal C^s,
$$

and every vector in $\mathcal C^s$ expands under $DH^{-1}$ by at least

$$
\lambda_s=\frac{1621}{492}>1.
$$

**Proof.** Since

$$
H^{-1}(X,Y)=(Y,1-6Y^2-X),
$$

its normalized derivative is

$$
\widehat {DH^{-1}}_Z
=\begin{pmatrix}
0&r\\
-r^{-1}&-12Y
\end{pmatrix}.
$$

For $(u,v)\in\mathcal C^s$, $|u|\le|v|/2$.  Since every h-set has
$|Y|\ge5/16$,

$$
|v'|
\ge\left(\frac{15}{4}-\frac{56}{123}\right)|v|
=\frac{1621}{492}|v|,
\tag{8}
$$

and $|u'|=(123/112)|v|$.  Hence

$$
\frac{|u'|}{|v'|}
\le
\frac{123/112}{1621/492}
=\frac{15129}{45388}
<\frac12.
\tag{9}
$$

Because $\|(u,v)\|_\infty=|v|$ on $\mathcal C^s$, (8) is the claimed
backward expansion.  $\square$

### Lemma 7: realization of every admissible bi-infinite itinerary

For every $\omega=(\omega_n)_{n\in\mathbb Z}\in\Sigma_A$, there is a point
$z\in N_{\omega_0}$ such that

$$
H^n(z)\in N_{\omega_n}
\qquad\text{for every }n\in\mathbb Z.
\tag{10}
$$

**Proof.** Fix $m\ge1$.  Every adjacent pair in the finite word

$$
\omega_{-m},\omega_{-m+1},\ldots,\omega_m
$$

is one of the six covering relations from Lemma 4.  The finite-chain theorem
for h-set covering relations, which is the composition property of the
nonzero Brouwer degrees in (5), therefore supplies an orbit segment
$z^{(m)}_{-m},\ldots,z^{(m)}_m$ with

$$
z^{(m)}_k\in N_{\omega_k},
\qquad
H(z^{(m)}_k)=z^{(m)}_{k+1}.
$$

Put $w_m=z^{(m)}_0$.  The compact rectangle $N_{\omega_0}$ contains a
convergent subsequence $w_{m_j}\to w$.  For any fixed integer $k$, once
$m_j\ge|k|$ one has

$$
H^k(w_{m_j})\in N_{\omega_k}.
$$

The map $H$ is a polynomial diffeomorphism with the displayed polynomial
inverse, so $H^k$ is continuous for positive and negative $k$.  Since each
$N_{\omega_k}$ is closed, taking the limit gives
$H^k(w)\in N_{\omega_k}$.  Thus $w$ satisfies (10).  $\square$

### Lemma 8: compact invariant set, coding, and hyperbolicity

Let

$$
\mathcal N=\bigcup_{s,t}N_{st},
\qquad
\Lambda=\bigcap_{n\in\mathbb Z}H^{-n}(\mathcal N).
\tag{11}
$$

Then $\Lambda$ is nonempty, compact, invariant, uniformly hyperbolic, and its
itinerary map is a continuous surjection onto $\Sigma_A$.

**Proof.** Equation (11) defines a closed subset of the compact set
$\mathcal N$, so $\Lambda$ is compact.  Since $H$ is invertible, shifting the
integer index in (11) gives $H(\Lambda)=\Lambda$.  Lemma 7 gives at least one
point in $\Lambda$ for every word in $\Sigma_A$, so $\Lambda$ is nonempty.

The h-sets are pairwise disjoint compact sets.  Thus every $z\in\Lambda$ has a
unique state at every integer time.  Lemma 3 shows that consecutive states
must be an allowed pair, so the itinerary map $\pi:\Lambda\to\Sigma_A$ is
well-defined.  Lemma 7 makes it surjective.  Positive separation between the
four h-sets implies that every fixed itinerary coordinate is locally constant
on $\Lambda$; hence $\pi$ is continuous in the product topology.  By
construction,

$$
\pi\circ H=\sigma\circ\pi.
\tag{12}
$$

It remains to justify that the cone inequalities produce an invariant
splitting rather than only pointwise expansion.  For an unstable normalized
slope $m=v/u$, the projective action of $DH_z$ is

$$
T_x(m)=\frac{r^{-1}}{-12x-rm}.
$$

On $|m|\le1/2$, (6) gives

$$
|T_x'(m)|
=\frac1{|-12x-rm|^2}
\le\left(\frac{224}{773}\right)^2<1.
\tag{13}
$$

Therefore the successive projective images of the unstable cone along the
full past of $z$ contract to a unique line $E_z^u\subset\mathcal C^u$.
Uniform contraction in (13) and continuity of $DH$ make $E_z^u$ continuous
in $z$, and its construction gives

$$
DH_z E_z^u=E_{H(z)}^u.
$$

The same argument for a stable slope $n=u/v$ under $DH^{-1}$ uses

$$
S_Y(n)=\frac{r}{-r^{-1}n-12Y}
$$

and (8) to obtain

$$
|S_Y'(n)|
\le\left(\frac{492}{1621}\right)^2<1.
\tag{14}
$$

It yields a continuous invariant line $E_z^s\subset\mathcal C^s$.  Since the
two cones are disjoint away from zero,

$$
T_z\mathbb R^2=E_z^u\oplus E_z^s.
$$

Lemmas 5--6 give, in the fixed normalized max norm,

$$
\|DH_z v^u\|\ge\lambda_u\|v^u\|,
\qquad v^u\in E_z^u,
$$

and

$$
\|DH^{-1}_z v^s\|\ge\lambda_s\|v^s\|,
\qquad v^s\in E_z^s.
$$

Equivalently, forward iteration contracts $E^s$ by at most
$\lambda_s^{-1}<1$.  This is a continuous invariant uniformly hyperbolic
splitting on $\Lambda$.  $\square$

### Completion of the proof

Direct determinant expansion gives

$$
\det(\lambda I-A)
=(\lambda^2-\lambda-1)(\lambda^2+1).
$$

Its eigenvalues are

$$
\frac{1+\sqrt5}{2},\quad
\frac{1-\sqrt5}{2},\quad i,\quad -i,
$$

so

$$
\rho(A)=\frac{1+\sqrt5}{2}=\varphi.
$$

The entropy of the two-sided subshift is
$h_{\mathrm{top}}(\sigma|_{\Sigma_A})=\log\rho(A)$.  Equation (12) makes
$(\Sigma_A,\sigma)$ a topological factor of $(\Lambda,H)$.  Topological
entropy cannot increase under a continuous factor map, and therefore

$$
h_{\mathrm{top}}(H|_\Lambda)
\ge h_{\mathrm{top}}(\sigma|_{\Sigma_A})
=\log\varphi.
$$

Together with Lemma 8 this proves the claim. $\square$

## Corrections or Missing Assumptions

- No correction to the frozen R058 claim is required.
- The proof must explicitly invoke the finite-chain covering-relation theorem;
  checking the six one-step crossings without this composition theorem would
  not justify bi-infinite itinerary realization.
- Exact exclusion of the ten forbidden transitions is needed if $\Lambda$ is
  defined as the full survivor in the union of all four h-sets.  Without that
  exclusion, one could instead define a smaller itinerary-selected set, but
  the simple maximal-survivor coding statement would need modification.

## Open Risks

- This proof gives a surjective semiconjugacy, not injectivity.  It does not
  justify topological conjugacy, entropy equality, or a Markov partition.
- The certified set is contained in the four frozen h-sets; it is not proved
  to coincide with the R056/R058 finite-grid SCC lineage or to exhaust the
  full $a=6$ horseshoe.
- The graph-refinement and symbolic-bridge parts of R058 are independent
  finite diagnostics.  Their success or failure does not enter the theorem
  above.
- A computational checker should recompute every rational inequality and the
  characteristic polynomial independently, but such a checker validates the
  arithmetic inputs rather than replacing the covering-chain theorem.
