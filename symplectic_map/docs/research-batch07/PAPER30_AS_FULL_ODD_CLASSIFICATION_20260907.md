# Quadratic Hénon: complete odd-characteristic Artin–Schreier classification

Date: 2026-09-07. This is an author proof consolidation and a new geometric
corollary, not an independent verdict, formal candidate, manuscript or experiment.
Frozen earlier records, including the incorrect multi-shift calculation and the
report that missed it, remain unchanged.

## Claim

Let $K$ be algebraically closed of prime characteristic $p>2$, let $c\in K$,
and set
$$
A=K[x,y],\quad F_c=(x^2+c-y,x),\quad \sigma=F_c^*,
\quad \wp(h)=h^p-h,\quad Q=A/\wp(A).
$$
Here $Q$ is an additive quotient, not a quotient ring. For every
$\lambda\in\mathbb F_p^*$, the complete eigenspace is
$$
\boxed{
Q^{\sigma=\lambda}=
\begin{cases}
\mathbb F_3[q^3xy],&p=3,\ c\ne0,\ \lambda=-1,\ q^2=-1/c,\\
0,&\text{otherwise}.
\end{cases}}
\tag{C1}
$$
The notation $\mathbb F_3[q^3xy]$ in (C1) means the one-dimensional
$\mathbb F_3$-linear span of the additive class $[q^3xy]$, not a polynomial
algebra. Either nonzero root $q$ gives the same line.

Consequently a connected cyclic degree-$p$ finite étale cover of
$\mathbb A^2_K$ to which $F_c$ lifts exists if and only if $p=3$ and $c\ne0$.
For each such $c$ there is exactly one such cover up to isomorphism over the
fixed base, after forgetting the choice of deck generator. It is
$$
Y_q:\ z^3-z=q^3xy,
\qquad
\widetilde F_c(x,y,z)=(x^2+c-y,x,-z+qx).
\tag{C2}
$$
No connected cyclic degree-$p$ cover admits a lift commuting with a chosen
deck generator, including in the exceptional case.

## Status

`PROVABLE AS STATED / AUTHOR PROOF COMPLETE`.
New independent mathematical checking is pending. The old full-mixed open
obligation is claimed to be closed by the new proof below, not retroactively
by the earlier auxiliary PASS. Paper30 has not been created or accepted.

## Assumptions and notation

Write
$$
\overline C_\lambda=A/((\sigma-\lambda)A+K),
\quad u=\langle x\rangle,\quad
\phi\langle h\rangle=\langle h^p\rangle.
$$
Angle brackets denote coinvariants and square brackets denote AS classes.
The operator $\phi$ is additive and $p$-semilinear. A lift in (C2) is an
automorphism of the cover inducing $F_c$ on the base. Covers are cyclic
Galois covers of degree $p$, not arbitrary degree-$p$ covers.

## Proof strategy and dependency map

1. The unchanged [coinvariant bridge, Step 2](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md)
   identifies $Q^{\sigma=\lambda}$ with $\operatorname{Fix}(\phi)$.
2. The new [odd-prime proof](PAPER30_AS_ODD_PRIME_EXCEPTION_PROBE_20260907.md),
   Steps 1–3, proves $\operatorname{Fix}(\phi)\subseteq Ku$ for every $p>2$.
   Its strong-balanced dependency is the repaired one-step argument in the
   [new erratum](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md), not the false
   arbitrary-shift formula in the old proof.
3. Steps 4–5 of that new proof exclude $Ku$ for every $p\ge5$.
4. The calculation below handles $p=3$ for every $c$, including both choices
   of $\lambda$; it also gives all explicit AS representatives.
5. The standard Artin–Schreier torsor description and elementary lift
   calculation below translate (C1) into the cover statement.

The separate [cubic zero-parameter author check](PAPER30_AS_CUBIC_ZERO_FIXED_PROBE_20260907.md)
supplies a redundant author-side check of that boundary, not an additional
independent-review certificate or an extra theorem to count for capacity.

## Proof

### Step 1. Reduction to characteristic three and the single-letter line

The bridge sends $[g]$ to $\langle h\rangle$ whenever
$(\sigma-\lambda)g=\wp(h)$. Constants cause no ambiguity because
$\wp(K)=K$. The repaired highest-orbit obstruction, followed by the new
dual-weight obstruction for every odd-reflection layer $D=3n+1$, $n\ge1$,
places every fixed vector in $Ku$. For $p\ge5$ the new proof exhibits a
nonzero non-single-letter component of $\phi(u)$, for every $c$ and
$\lambda\in\mathbb F_p^*$. Semilinearity therefore leaves no nonzero fixed
vector. It remains to calculate on $Ku$ when $p=3$.

### Step 2. The exact characteristic-three calculation

Use $X_0=x$, $X_{-1}=y$, $X_1=x^2+c-y$, so that
$X_0^2=X_{-1}+X_1-c$. Set $E=\langle X_0X_1\rangle$. Then
$$
\phi(u)=(1+\lambda^{-1})E-cu.
\tag{C3}
$$
Indeed $x^3=X_0X_{-1}+X_0X_1-cX_0$, and shifting
$X_0X_{-1}$ one step gives $X_0X_1$. The two directions $E$ and $u$
belong to different nonempty binary-word orbits and are linearly independent.

If $\lambda=1$, the $E$ coefficient of $\phi(tu)$ is $2t^3$, which is
nonzero for $t\ne0$. Thus there is no nonzero fixed vector. If
$\lambda=-1$, the equation $\phi(tu)=tu$ is exactly
$$
-ct^3=t.
\tag{C4}
$$
For $c=0$ it forces $t=0$. For $c\ne0$, algebraic closedness gives a
nonzero $q$ with $q^2=-1/c$; the solutions of (C4) are precisely
$0,q,-q$, a one-dimensional $\mathbb F_3$-space.

For each such $q$, put $g=q^3xy$. Direct substitution gives
$$
(\sigma+1)g=q^3(x^3+cx)=q^3x^3-qx=\wp(qx).
\tag{C5}
$$
Its bridge image is $qu\ne0$. Thus $[g]\ne0$, and the bridge
isomorphism proves both that this class exists and that no further mixed
classes are missing. This proves (C1).

### Step 3. Torsors, unmarked covers, and the lifting criterion

The Artin–Schreier exact sequence, together with vanishing of higher
structure-sheaf cohomology on the affine scheme $\operatorname{Spec}A$,
identifies $H^1_{\mathrm{et}}(\operatorname{Spec}A,\mathbb Z/p)$ with
$A/\wp(A)$. These are the standard facts used here, not a new method;
see [Stacks Project, §59.63](https://stacks.math.columbia.edu/tag/0A3J).
A class $[g]$ corresponds to the torsor
$B_g=A[z]/(z^p-z-g)$ with deck generator $\tau:z\mapsto z+1$.
It is finite free of degree $p$ and étale because the derivative in $z$
of its defining equation is $-1$.

A nonzero class gives a connected torsor. One elementary justification is
as follows. Over $K(x,y)$ an AS polynomial has splitting field generated
by any one root, with Galois group a subgroup of $\mathbb F_p$; hence it
is irreducible unless it has a root in $K(x,y)$. Such a root has no pole
on any irreducible divisor of $\mathbb A^2$: a pole of order $r>0$
would give a pole of order $pr$ in its AS difference, contradicting
$g\in A$. Since $A$ is a UFD, the root then belongs to $A$. Thus a
root would make $[g]=0$. Conversely the zero class gives the split torsor.

Changing the deck generator acts on nonzero AS classes by multiplication
by $\mathbb F_p^*$. Therefore unmarked connected cyclic degree-$p$
covers correspond to nonzero $\mathbb F_p$-lines in $Q$. A base lift
normalizes the deck group, so for a unique $\lambda\in\mathbb F_p^*$
its coordinate on the cover has the form
$$
z\longmapsto\lambda z+h(x,y).
\tag{C6}
$$
To justify the form, normalization gives that this coordinate minus
$\lambda z$ is deck invariant; the invariant subring of the torsor is
$A$. Alternatively, in the unique degree-$<p$ polynomial expansion in
$z$, translation by $1$ forces every nonconstant invariant coefficient
to vanish, by its highest nonzero finite-difference term.

Substitution into the defining equation shows that (C6) is a lift
exactly when
$$
\sigma g-\lambda g=\wp(h),
\quad\text{or equivalently}\quad [g]\in Q^{\sigma=\lambda}.
\tag{C7}
$$
The map is invertible: its base inverse is $F_c^{-1}$ and its fibre
inverse sends $z$ to $\lambda^{-1}(z-h\circ F_c^{-1})$.
Equation (C1) now gives no cover outside the exceptional case, and exactly
one unmarked base-isomorphism class in that case. A commuting lift would
require $\lambda=1$, whose eigenspace is zero in every case.

### Step 4. Explicit exceptional lift and its limits

Equation (C5) proves (C2). Its inverse is explicitly
$$
(x',y',z')\longmapsto
\bigl(y',(y')^2+c-x',qy'-z'\bigr).
$$
The three lifts of this fixed representative are obtained by adding
$a\in\mathbb F_3$ to the last coordinate: any two choices of $h$ in
(C7) differ by an element of $\ker\wp=\mathbb F_3$. They all satisfy
$\widetilde F_c\tau=\tau^{-1}\widetilde F_c$ and none commutes with
$\tau$. This completes the geometric corollary. $\square$

## Corrections, scope and open risks

- The corrected arbitrary-shift dependency is explicitly identified above.
  Neither old author record nor the old independent PASS is silently edited.
- This classifies all finite polynomial supports for this quadratic family,
  not general Hénon degrees, characteristic two, nonclosed base fields,
  noncyclic covers, higher $p$-power covers or lifts of an arbitrary iterate.
- The explicit exceptional surface has Danielewski form $xy=P(z)$; its
  existence must be compared with standard surface automorphism formulas.
  The claimed new content is the all-support classification, not merely
  this familiar type of surface or the standard AS torsor dictionary.
- No formal novelty/value/capacity score, manuscript, page measurement,
  Route result, local paper acceptance or external operation is implied.
- Independent checking of the new reduction, repaired dependency, the
  characteristic-three calculation and the geometric corollary remains
  required. Author completeness is not an independent PASS.
