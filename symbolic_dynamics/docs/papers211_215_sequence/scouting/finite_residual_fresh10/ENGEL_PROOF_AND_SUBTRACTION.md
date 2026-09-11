# Fixed-involution Engel map: complete elementary reduction, no residual pair

## Claim

For every finite group $G$ and fixed $t\in G$ with $t^2=e$, consider
$E_t(x)=x^{-1}txt$ on all of $G$. Its image, recurrent set, pointwise entry
times, eventual periods, every one-step fibre and all maximum-fibre
targets are described and proved below.

This complete elementary classification is a negative subtraction
certificate, not a new-paper claim. In particular its inverse mechanism
is precisely the already-used fixed-centralizer-coset argument.

## Status

**PROVABLE AS STATED** for the displayed classification.

A materially separate new inverse/extremal axis is **NOT CURRENTLY
JUSTIFIED** after subtraction. No pilot is needed or proposed.

## Assumptions

The group $G$ is finite, its multiplication is associative, and $e$ is its
identity. The fixed parameter $t$ satisfies $t^2=e$; the special case
$t=e$ is included. The carrier is the entire group, not a conjugacy class
or an evolving pair. No commutativity, solvability or matrix realization
is assumed.

## Notation

Write $E=E_t$ and
$$
C=C_G(t)=\{c\in G:ct=tc\},\qquad
Y=\{st:s\text{ is conjugate in }G\text{ to }t\}.
$$
Let $\operatorname{ord}(x)$ be the finite order of $x$.
For a positive integer $r$, write $r=2^{v_2(r)}m$ with $m$ odd.
For odd $m>1$, $\operatorname{ord}_m(-2)$ is the multiplicative order of
$-2$ modulo $m$; define $\operatorname{ord}_1(-2)=1$.
The entry time $h(x)$ is the least nonnegative iterate index at which
the orbit enters its eventual cycle.

## Proof strategy

The first image is a product of two involutions. Conjugation by $t$
inverts every such image element, so further iterates are powers with
exponent $-2$. Solve equality of two commutator outputs separately to
obtain an exact left centralizer coset.

## Dependency map

1. The image description follows by ranging $x^{-1}tx$ over the conjugacy
   class of $t$.
2. Reversal by $t$ gives the exact first-image power law.
3. Element orders and elementary modular arithmetic give recurrence,
   entry times and periods.
4. Equality of conjugates gives each full target fibre and its size.
5. The identity parameter is checked directly at the end.

## Proof

### Step 1. Exact image and inversion on that image

By the definition of conjugacy,
$$
E(G)=\{(x^{-1}tx)t:x\in G\}=Y.
$$
If $y=st\in Y$, both $s$ and $t$ square to the identity, so
$$
tyt=ts=(st)^{-1}=y^{-1}.
$$
Consequently
$$
E(y)=y^{-1}(tyt)=y^{-2}\qquad(y\in Y).
$$
The set $Y$ is forward invariant because it is the image of a self-map.
For $y_0=E(x)$, induction therefore gives the literal identity
$$
E^{k+1}(x)=y_0^{(-2)^k}\qquad(k\ge0).
$$
This is an exact reduction after the first iterate. It is not a
conjugacy of the whole carrier with a power map.

### Step 2. Complete recurrent set

Every recurrent point must lie in the image $Y$. For $y\in Y$ of order
$r$, Step 1 gives $E^k(y)=y^{(-2)^k}$. If $r$ is odd, multiplication by
$-2$ is invertible modulo $r$, so some positive $k$ satisfies
$(-2)^k\equiv1\pmod r$ and $y$ is recurrent. If $r$ is even, every
positive $k$ has $(-2)^k-1$ odd and hence not divisible by $r$; no positive
iterate returns to $y$. Thus
$$
R=\{y\in Y:\operatorname{ord}(y)\text{ is odd}\}.
$$

There is also an image-free description:
$$
R=\{y\in G:\operatorname{ord}(y)\text{ is odd and }tyt=y^{-1}\}.
$$
The first inclusion follows from Step 1. For the reverse inclusion, let
$y$ satisfy the right-hand conditions and put $m=\operatorname{ord}(y)$.
Choose an integer $a$ with $-2a\equiv1\pmod m$; this exists because $m$
is odd and includes $m=1$. Since $t y^a t=y^{-a}$,
$$
E(y^a)=y^{-a}t y^a t=y^{-2a}=y.
$$
Hence $y\in Y$, and the first characterization makes it recurrent.

### Step 3. Exact entry times and eventual periods

For $y\in Y$ with order $r=2^v m$, $m$ odd, the order of its $k$-th
iterate is
$$
\operatorname{ord}\bigl(E^k(y)\bigr)
=\frac{r}{\gcd(r,2^k)}
=2^{\max(v-k,0)}m.
$$
It first becomes odd at $k=v$, and Step 2 proves that this is exactly the
entry time. If $x\notin Y$, no iterate at time zero is recurrent, and
its first image $E(x)$ lies in $Y$. Thus the complete pointwise formula is
$$
h(x)=
\begin{cases}
v_2(\operatorname{ord}(x)),&x\in Y,\\
1+v_2(\operatorname{ord}(E(x))),&x\notin Y.
\end{cases}
$$
Equivalently, $h(x)=0$ for $x\in R$, and otherwise
$h(x)=1+v_2(\operatorname{ord}(E(x)))$.

Once the element order is odd $m$, a return after $k>0$ occurs exactly
when $(-2)^k\equiv1\pmod m$. Therefore the eventual period of an arbitrary
$x$ is $\operatorname{ord}_m(-2)$, where $m$ is the odd part of
$\operatorname{ord}(E(x))$. This includes fixed points with $m=1$.
No classification of the possible element orders of every finite group
has been assumed; the formula is pointwise in the explicitly given
group and parameter.

### Step 4. All target fibres and all one-step maximizers

For a target $y\notin Y$, the fibre is empty by Step 1.
For $y\in Y$, choose any $x_0$ with $E(x_0)=y$.
For any $z\in G$,
$$
\begin{aligned}
E(z)=E(x_0)
&\Longleftrightarrow z^{-1}tz=x_0^{-1}tx_0\\
&\Longleftrightarrow (z x_0^{-1})t=t(z x_0^{-1})\\
&\Longleftrightarrow z\in Cx_0.
\end{aligned}
$$
Thus the complete fibre is the left coset $Cx_0$, with cardinality $|C|$.
The orientation is part of the statement: it is not asserted to be
$x_0C$. Therefore
$$
\#E^{-1}(y)=
\begin{cases}
|C|,&y\in Y,\\
0,&y\notin Y,
\end{cases}
\qquad |Y|=\frac{|G|}{|C|}.
$$
The last equality also follows by summing these disjoint fibres over
the image. Since the image is nonempty, the maximum one-step fibre
size is exactly $|C|$, attained at every target in $Y$ and nowhere else.

### Step 5. Degenerate boundary

If $t=e$, then $C=G$, $Y=R=\{e\}$, and $E$ is constant at $e$.
The point $e$ has entry time zero and all other elements have time one.
Every eventual period is one and the single nonempty fibre has size
$|G|$. All displayed formulas agree, including the trivial group.

## Source and internal subtraction

The literal fixed-second-entry commutator is the classical left Engel
iteration. [Khukhro–Shumyatsky, introduction and §2](https://arxiv.org/pdf/2010.08616)
define that iteration and the convention used here. Their Lemma 2.8
records the odd-abelian coprime-action sink mechanism; §3 uses odd-order
elements inverted by an involution. The elementary cyclic-power argument
above is supplied in full and does not import that paper's global
coprime-automorphism or Fitting-index theorems.

The older [P119 original manuscript, §3](../../../../papers/119-regular-engel-unitriangular-dynamics/main.tex)
already proves that fibres of $x\mapsto x^{-1}\phi(x)$ are left cosets of
the fixed subgroup of $\phi$. For $\phi(x)=txt$, that fixed subgroup is
exactly $C_G(t)$, so Step 4 is precisely the same proof mechanism.
P119's specific regular unitriangular parameter and filtration theorem
are not asserted to classify the present arbitrary finite group.

The involution assumption makes the post-image dynamics simpler:
Step 1 is only a product-of-involutions identity followed by powering.
A change from regular unitriangular parameters to involutions does not
make the generic coset inverse an independent new contribution. No
claim is made that a source states these pointwise formulas in this exact
packaging, nor that a search miss establishes novelty.

## Corrections or missing assumptions

The restriction $t^2=e$ is essential to the displayed power proof.
There is no extension here to arbitrary fixed second entries.
The reduction is only on $Y$, not a full-carrier power-map conjugacy.
The inverse formula is complete but fully subtracted; no new inverse,
fibre-population or extremal classification beyond centralizer-coset
bookkeeping has been supplied.

## Open risks

The proof has no finite-check dependency and has not received independent
review. Its elementary completeness does not meet the two-axis residual
admission gate. Disposition: **NO_NOMINATION / HOLD_EXTERNAL**.

