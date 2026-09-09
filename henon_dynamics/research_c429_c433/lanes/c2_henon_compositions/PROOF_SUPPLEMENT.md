# C2 proof supplement

## Claim, status and dependency map

**Original claim:** integer native least periods of fixed-length compositions of integral generalized Hénon maps are bounded independently of their coefficients.

**Status: PROVABLE AS STATED — classical theorem application, not a new result.** In fact one bound works simultaneously for every length and degree. The sharper sign-dependent composition spectrum is **NOT CURRENTLY JUSTIFIED** by this lane.

Assumptions and notation: $r\ge1$; $a_i\in\{1,-1\}$; $p_i\in\mathbb Z[t]$ with arbitrary prescribed exact degree $d_i\ge2$; subscripts $i$ modulo $r$; $H_i(x,y)=(y,p_i(y)-a_i x)$; $W=H_{r-1}\circ\cdots\circ H_0$; $P\in\mathbb Z^2$. A native period is measured under $W$. Put $\varepsilon=\prod_{i=0}^{r-1}a_i$.

Dependency map:

1. Universal native bound: closure of integral polynomial maps under composition, and Pezda's Theorem 2.1.
2. Phase conversion: the exact phase-labelled lift identity, with no external theorem.
3. Phasewise secant bounds: the recurrence at each phase, integer polynomial divisibility, and interpolation between endpoint output values.
4. Affine-support necessary condition: phasewise equality to affine restrictions, centroid translation and elementary $2\times2$ linear algebra.

## 1. Universal bound, with every quantifier retained

**Imported theorem (Pezda 2002, Theorem 2.1).** The set of all least cycle lengths of maps $\Phi=(\Phi_1,\Phi_2)$ with $\Phi_j\in\mathbb Z[x,y]$ acting on $\mathbb Z^2$ is

$$
\mathcal P=\{1,2,3,4,6,8,9,12,16,18,24\}.
$$

The article defines a cycle as an ordered tuple of pairwise different lattice points satisfying every successive and closing edge. This is the least-period convention used here. Primary locator: [original article, printed pp.95–96](https://dml.cz/bitstream/handle/10338.dmlcz/120574/ActaOstrav_10-2002-1_10.pdf). The result is invoked as a published theorem, not reproved in this supplement.

**Corollary.** For every $r$, every exact degree vector, every sign vector, every coefficient choice, and every periodic $P\in\mathbb Z^2$, its native least period under $W$ belongs to $\mathcal P$.

**Proof.** Each coordinate of $H_i$ belongs to $\mathbb Z[x,y]$. Substituting integral polynomials into an integral polynomial again gives an integral polynomial, because addition and multiplication preserve integral coefficients. Induction on the number of factors therefore gives $W=(W_1,W_2)$ with $W_j\in\mathbb Z[x,y]$.

If $P$ has least positive return $n$, the states $P,W(P),\ldots,W^{n-1}(P)$ are pairwise distinct. Indeed, a repetition $W^j(P)=W^k(P)$ with $0\le j<k<n$ gives $W^{k-j}(P)=P$ after applying $W^{-j}$; each factor is invertible since

$$
H_i^{-1}(x,y)=\bigl(a_i(p_i(x)-y),x\bigr).
$$

Thus these states form precisely a cycle in Pezda's sense for the single map $W$. The theorem gives $n\in\mathcal P$. Since no step depended on bounds for $r,d_i,a_i$ or polynomial coefficients, the conclusion holds simultaneously for all of them. In particular $n\le24$. $\square$

This argument needs no phase lift and yields no assertion that all members of $\mathcal P$ are realized by Hénon compositions, by a specified word length, or by prescribed degrees/signs.

## 2. Exact phase-labelled native-clock interface

Define the auxiliary bijection

$$
F(i;x,y)=\bigl(i+1;y,p_i(y)-a_i x\bigr)
$$

on $(\mathbb Z/r\mathbb Z)\times\mathbb Z^2$. Its inverse is

$$
F^{-1}(i;x,y)=\bigl(i-1;a_{i-1}(p_{i-1}(x)-y),x\bigr).
$$

After exactly $r$ steps from phase zero, each factor has acted in the prescribed order, hence

$$
F^r(0;P)=(0;W(P)).
$$

**Lemma.** If $P$ has native least period $n$ under $W$, then $(0;P)$ has least period exactly $rn$ under $F$.

**Proof.** The displayed identity gives the return $rn$. Every return under $F$ must preserve its phase, so its length has the form $rk$ with $k\ge1$. The same identity then gives $W^k(P)=P$, which requires $n\mid k$. Thus no smaller positive lifted return exists. $\square$

The scalar coordinate sequence obtained by forgetting phase can have smaller period. Its unlabelled period is therefore not a substitute for $rn$, and intermediate-factor returns are not C2's native clock. This is the transferable part of the C425 phase-lift mechanism.

## 3. Phasewise secant lemma and its exact limitation

Write the coordinates along a lifted periodic orbit as

$$
F^t(0;P)=\bigl(t\bmod r;x_t,x_{t+1}\bigr).
$$

They satisfy the exact recurrence

$$
p_i(x_{t+1})=x_{t+2}+a_i x_t\quad(t\equiv i\pmod r).
$$

For each phase define the finite nonempty input support

$$
E_i=\{x_{i+1+kr}:k\in\mathbb Z\},\qquad
m_i=\min E_i,\qquad D_i=\max E_i-m_i.
$$

Set $U_i=E_i-m_i\subseteq[0,D_i]\cap\mathbb Z$ and

$$
g_i(t)=p_i(m_i+t)-m_{i+1}-a_i m_{i-1}\in\mathbb Z[t].
$$

The recurrence implies

$$
g_i(U_i)\subseteq U_{i+1}+a_i U_{i-1}.
$$

The right side is contained in an interval $J_i$ of length $C_i=D_{i-1}+D_{i+1}$: take $J_i=[0,C_i]$ for $a_i=1$, and $J_i=[-D_{i-1},D_{i+1}]$ for $a_i=-1$. If $r=1$ or $r=2$, repeated neighbouring phase indices in this formula are deliberately counted twice.

**Lemma (coupled secant bounds).** For every phase with $D_i>0$, put

$$
A_i=g_i(0),\qquad q_i=\frac{g_i(D_i)-g_i(0)}{D_i}.
$$

Then $q_i\in\mathbb Z$ and there is $h_i\in\mathbb Z[t]$ such that

$$
g_i(t)=A_i+q_i t+t(t-D_i)h_i(t).
$$

These data satisfy

$$
|q_i|D_i\le C_i,\qquad
|h_i(t)|\,t(D_i-t)\le C_i\quad(t\in U_i,\ 0<t<D_i),
$$

and $h_i(s)-h_i(t)\in(s-t)\mathbb Z$ for all distinct integers $s,t$.

**Proof.** The difference $g_i(D_i)-g_i(0)$ is divisible by $D_i$ because $g_i$ has integral coefficients. Both endpoint values lie in $J_i$, so their difference has absolute value at most $C_i$. This proves integrality and the slope bound.

The integral polynomial $g_i(t)-A_i-q_i t$ vanishes at $0$ and $D_i$. Divide by the monic linear factor $t$ and then by the monic factor $t-D_i$; both divisions have integral quotient and zero remainder. This gives $h_i\in\mathbb Z[t]$. The line $A_i+q_i t$ is a convex interpolation of the two endpoint values for $0\le t\le D_i$, so it lies in $J_i$. At every actual interior support point, $g_i(t)$ also lies in $J_i$. Their difference has absolute value at most $C_i$, giving the remainder bound. Finally, each monomial difference $s^k-t^k$ is divisible by $s-t$, which proves the last congruence for an integral polynomial. $\square$

If $D_i=\max_jD_j>0$, then $C_i\le2D_i$, so the C428 pointwise secant bound is valid for that phase. For $D_i\ge10$, the same elementary inequalities force $h_i(t)=0$ at actual letters with $3\le t\le D_i-3$. This conclusion does **not** state that the other phases have the same support or the same remainder polynomial. For general $i$, $C_i/D_i$ can be large; for $D_i=0$ the secant quotient is undefined and that singleton phase must be treated separately.

**Exact example of incomparable phase supports.** Let $r=2$, $M\ge1$, $a_0=a_1=1$, $p_0(t)=t^2+M$ and $p_1(t)=t(t-M)$. The four factor steps are

$$
(0,0)\xrightarrow{H_0}(0,M)
\xrightarrow{H_1}(M,0)
\xrightarrow{H_0}(0,0)
\xrightarrow{H_1}(0,0).
$$

Therefore $W(0,0)=(M,0)$ and $W(M,0)=(0,0)$; the two distinct native states give least period two. The phase-zero inputs are always $0$, whereas the phase-one inputs are $M$ and $0$. Thus $D_0=0$ and $D_1=M$. The repeated spatial state $(0,0)$ at different phases does not shorten the labelled four-step orbit. Both factors have exact degree two for every $M$. This proves only a phase-support warning, not failure of any period bound. $\square$

## 4. Necessary condition for a composition period outside the affine list

Say that the lifted orbit is **phasewise affine on its support** if for every $i$ there are $A_i,q_i\in\mathbb Z$ with

$$
p_i(t)=A_i+q_i t\quad\text{for every }t\in E_i.
$$

At a singleton support one may always take $q_i=0$. At a two-point support integer value-difference divisibility always supplies an integral slope. At larger supports the condition is substantive.

**Proposition.** A phasewise-affine-on-support native periodic orbit has least period in $\{1,2,3,4,6\}$ if $\varepsilon=1$, and in $\{1,2\}$ if $\varepsilon=-1$.

**Proof, Step 1 (replace restrictions, not degrees).** Define the affine integral maps

$$
T_i(x,y)=(y,A_i+q_i y-a_i x),\qquad T=T_{r-1}\circ\cdots\circ T_0.
$$

At every phase of the actual lifted orbit, $H_i$ and $T_i$ agree because their input $y$ lies in $E_i$. Induction along that orbit shows $T^k(P)=W^k(P)$ for every integer $k\ge0$. In particular their least periods at $P$ coincide. This replaces only restrictions to an actual finite orbit; it does not assert that any original nonlinear polynomial has become globally affine.

**Step 2 (remove the affine part).** Write $T(z)=Bz+b$ with $B\in\operatorname{GL}_2(\mathbb Z)$ and $\det B=\varepsilon$. Let the common least period be $n$ and let

$$
c=\frac1n\sum_{k=0}^{n-1}T^k(P)\in\mathbb Q^2.
$$

Affine linearity gives $T(c)=c$. Consequently $v=P-c$ satisfies $B^nv=v$, with the same period as $P$; $v=0$ gives period one.

**Step 3 (one-dimensional orbit span).** Suppose $v\ne0$ and the rational span $V=\operatorname{span}_{\mathbb Q}\{B^kv:k\ge0\}$ is one-dimensional. Then $Bv=\lambda v$ for $\lambda\in\mathbb Q$. The identity $B^nv=v$ implies $\lambda^n=1$, so $\lambda=1$ or $-1$, and the period is one or two.

**Step 4 (two-dimensional orbit span).** If $V=\mathbb Q^2$, the operator $B^n-I$ vanishes on a spanning set, hence $B^n=I$. Its minimal polynomial divides $X^n-1$, which has no repeated root in characteristic zero. Thus $B$ is diagonalizable over $\mathbb C$ with root-of-unity eigenvalues.

If $\det B=-1$, a nonreal eigenvalue would have its complex conjugate as the other eigenvalue because $B$ is real; the product would then have absolute-square value $1$, contradicting determinant $-1$. Both eigenvalues are real roots of unity, namely $1$ and $-1$, so $B^2=I$.

If $\det B=1$, its eigenvalues are $\lambda,\lambda^{-1}$ on the unit circle. Their sum $s=\operatorname{tr}B$ is an integer in $[-2,2]$. For $s=2$ or $-2$, diagonalizability gives $B=I$ or $-I$. For $s=-1,0,1$, the characteristic equations are respectively $B^2+B+I=0$, $B^2+I=0$, and $B^2-B+I=0$. They imply respectively $B^3=I$, $B^4=I$, and $B^6=I$. The least periods divide one of $1,2,3,4,6$, whose positive divisors give exactly the stated allowed list. $\square$

Thus an orbit whose native period is outside the relevant affine list must have at least one genuinely nonaffine phase restriction, on a support of at least three different input values. This is an elementary necessary condition; no sufficiency or sharp composition spectrum is claimed.

## Corrections, remaining gap and risks

The original bound does not need correction and has no identified gap once Pezda's published theorem is imported. Its proof is a classical consequence, so it contributes no new admission.

What remains unproved here is the stronger all-word sign-dependent exact-spectrum assertion. The phasewise secant lemma gives a necessary system but no complete propagation from one maximal-diameter phase to all phases. The example rules out one careless support identification, not every possible method. A finite table, individual witnesses or translating periods of a repeated power would not close that classification.

No primary-source theorem is applied to rational coefficients merely because they are integer-valued; no rational points are silently relabelled as integer points; no lifted factor-step period is identified with native composition time. This supplement has not received an independent nonauthor mathematical review, and no computation or formal proof-assistant verification is represented as having occurred.
