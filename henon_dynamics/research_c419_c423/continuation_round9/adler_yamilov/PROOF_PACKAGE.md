# AY9: unit sections and complete quotient-order 3, 4 and 5 strata

2026-09-08 UTC. AI-assisted author work under the unchanged
[frozen attempt](FROZEN_ATTEMPT.md). This is an auxiliary partial proof,
not a nonauthor review, admission, new contract or full structural atlas.

## 1. Claim, retained domain and exact remaining gap

For every integer $k$ retain
$$
Y_k(p,q,r,s)=\left(r-\frac{kp}{1+ps},s,p,
q+\frac{ks}{1+ps}\right)
$$
and its displayed rational inverse. Every positive and negative iterate
must be defined; individual coordinate zeros are allowed, but neither
$1+ps=0$ nor the inverse pole $1+rq=0$ is filled. One application is one
native step. The original all-$k$ ordinary integral structural atlas is
**NOT CURRENTLY JUSTIFIED**.

The following partial conclusions are proved here, using the accepted
[eighth-pass quotient and lift theorem](../../continuation_round8/adler_yamilov/PROOF_PACKAGE.md)
and its [nonauthor review](../../continuation_round8/adler_yamilov/COORDINATOR_HELPER_REVIEW.md):

1. Every nonzero ordinary integral periodic state with $k\ne0$ has a
   unit coefficient $h_n=\pm1$ somewhere on its orbit. Two normalized
   invariant parameters $\gamma,\lambda$ defined below are consequently
   integers. All adjacent coefficient products divide $k$.
2. All integral states whose quotient has least period three are exactly
   the cyclic rotations of the two explicit families in Section 5. Their
   least native periods are three or six as specified there.
3. All integral states whose quotient has least period four occur only
   at $k=4$ or $k=-4$. They are exactly the families in Section 6, and
   their least native period is eight.
4. There is no ordinary integral periodic state whose quotient has
   least period five.

These conclusions do **not** exclude quotient orders
$6,7,8,9,10,12$, which remain among the accepted rational possibilities.
In particular they do not prove that native periods three, six and eight
are exhaustive. No unresolved relation between a Miller function and
the native scaling multiplier is used below.

The inherited origin and $k=0$ boundary are not new results: the origin
is fixed; at $k=0$ the ordinary pair swap has least period one or two,
with both native poles still excluded throughout the orbit.

## 2. Accepted quotient notation

At time $n$ write
$$
D_n=1+p_ns_n,\quad E_n=1+r_nq_n=D_{n-1},
\quad h_n=k/D_n.
$$
For $k\ne0$, on an integral periodic orbit all these denominators are
nonzero, $D_n\mid k$, and $h_n$ is a nonzero integer. The two scalar
channels satisfy
$$
p_{n+1}=p_{n-1}-h_np_n,\qquad
s_{n+1}=s_{n-1}+h_ns_n.                                      \tag{2.1}
$$
The accepted invariants and constants are
$$
I=pq+rs,\qquad J=pqrs+ps+qr+krs,
$$
$$
C=J+1,\quad L=J+1-kI,\quad a=C+L-k^2,\quad e=CL+k^2.
$$
The product coordinates are recovered without dividing by a coordinate:
$$
pq=\frac{DE-L}{k},\qquad rs=\frac{C-DE}{k},
\qquad ps=D-1,\qquad rq=E-1.                                \tag{2.2}
$$
They obey
$$
D^2E^2-aDE-k^2(D+E)+e=0,
\qquad (D,E)\longmapsto
\left(\frac aD+\frac{k^2}{D^2}-E,D\right).                    \tag{2.3}
$$
For a nonzero periodic state its product matrix is nonzero of rank one.
The quotient least period is
$m\in\{3,4,5,6,7,8,9,10,12\}$, and the native least period is $m$ or
$2m$. The accepted proof includes singular cubics and individual zero
coordinates. Its exclusion of quotient periods one and two is used in
the next lemma.

## 3. Every nonzero integral cycle meets a unit section

**Lemma 3.1.** On every such cycle there is an index with $|h_n|=1$.

**Proof.** First the $p$ channel cannot vanish identically on a nonzero
periodic orbit. If it did, $D_n=1$ and $h_n=k$ at every index. Multiply
the second equation of (2.1) by $s_n$ and sum over the native period.
The sums of $s_ns_{n+1}$ and $s_ns_{n-1}$ agree by cyclic reindexing,
so $k\sum_n s_n^2=0$. Since $k\ne0$, the $s$ channel also vanishes;
the lag identities $r_n=p_{n-1}$ and $q_n=s_{n-1}$ then give the origin.

Suppose instead that all $|h_n|\ge2$. Let
$M=\max_n|p_n|>0$, and choose $n$ with $|p_n|=M$. Equation (2.1) gives
$$
2M\le |h_np_n|=|p_{n-1}-p_{n+1}|\le2M.
$$
Thus $|h_n|=2$, both neighbors have absolute value $M$, and
$p_{n+1}=-p_{n-1}$. Applying the same equality argument to the neighbors
and propagating around the finite cycle shows these statements at every
index. In particular
$$
h_n=2p_{n-1}/p_n,\qquad h_{n+1}=-h_n.
$$
Therefore $h$, and hence $D=k/h$, is two-periodic. Its quotient period
is at most two, contrary to the accepted nonzero-periodic-state theorem.
Some nonzero integer $h_n$ must consequently have absolute value one.
$\square$

Define
$$
\lambda=L/k,\qquad \gamma=C/k=\lambda+I,
\qquad A=\gamma+\lambda-k,\qquad B=\gamma\lambda+1.            \tag{3.1}
$$
At a unit section $h=\varepsilon\in\{1,-1\}$ one has $D=\varepsilon k$.
Equation (2.2) becomes $pq=\varepsilon E-\lambda$, proving
$\lambda\in\mathbb Z$. Thus also $\gamma,A,B\in\mathbb Z$, and
$a=kA$, $e=k^2B$.

At every index (2.2) now gives $DE/k=pq+\lambda\in\mathbb Z$.
Since $D=k/h_n$ and $E=k/h_{n-1}$, this is the signed divisibility
$$
h_nh_{n-1}\mid k.                                           \tag{3.2}
$$
Substituting $D=\varepsilon k$ into (2.3) and dividing by $k^2$ gives
the useful integer section equation
$$
E^2-(\varepsilon A+1)E+B-\varepsilon k=0,
\qquad E\ne0,\quad E\mid k.                                \tag{3.3}
$$
In particular $E\mid B$. Neither this equation nor Lemma 3.1 is by
itself an exhaustion of the remaining quotient orders.

## 4. Low-order torsion equations, with no smooth-fibre shortcut

The accepted cubic model is
$$
Y^2=X^3+\frac{A^2-4B}{4}X^2+\frac{kA}{2}X+\frac{k^2}{4},
\qquad P=(0,k/2).
$$
Its quotient map is addition by $P$ in one native step. The shear
$Y=y+(AX+k)/2$, $x=X$, gives
$$
\mathcal E:\quad y^2+Axy+ky=x^3-Bx^2,
\qquad P=(0,0).                                            \tag{4.1}
$$
The curve is irreducible, and $P$ is nonsingular because $k\ne0$.
All computations below are chord computations in its nonsingular group,
so they also apply to any singular fibre which has a permitted periodic
quotient. The exceptional singular point was already excluded for a
nonzero periodic lift in the accepted proof.

The tangent at $P$ is $y=0$, whose third intersection has $x=B$.
The group inverse is $(x,y)\mapsto(x,-y-Ax-k)$. Consequently
$$
2P=(B,-AB-k).                                              \tag{4.2}
$$
If $B=0$, the tangent has intersection multiplicity three at $P$,
and $P$ has order three. Conversely $3P=O$ forces the third tangent
intersection to equal $P$, hence $B=0$.

For $B\ne0$ put $u=AB+k$. The line through $P$ and $2P$ has slope
$-u/B$. Its third intersection and the inverse formula give
$$
x(3P)=\frac{ku}{B^2},\qquad
y(3P)=k\left(\frac{x(3P)}{B}-1\right).                     \tag{4.3}
$$
It follows that the exact order-four condition is
$$
B\ne0,\qquad AB+k=0.                                     \tag{4.4}
$$
Indeed this is exactly the condition that $2P$ is a nonidentity
two-torsion point. Likewise the exact order-five condition is
$$
B\ne0,\qquad k(AB+k)=B^3.                                \tag{4.5}
$$
Under (4.5), (4.3) gives $3P=(B,0)=-2P$, hence $5P=O$;
the converse follows by the same equality. Orders one and two are
already impossible, so these conditions give the indicated exact orders.

## 5. Complete quotient-period-three stratum

Order three is equivalent to $B=0$, or $\gamma\lambda=-1$.
As both parameters are integers, write
$$
\gamma\in\{1,-1\},\qquad \lambda=-\gamma,
\qquad I=2\gamma,\qquad J=k\gamma-1.                       \tag{5.1}
$$
We next show that every integral quotient orbit here contains $D=1$.
Write its cyclic denominator word as $(u,v,w)$. Subtract the expressions
for $a$ furnished by (2.3) at the $u$ and $v$ entries:
$$
0=(u-v)\left(w+\frac{k^2}{uv}\right).
$$
Because the least quotient period is three, at least two entries differ.
After a cyclic relabeling the displayed identity gives $uvw=-k^2$.
Since $a=-k^2$, it also gives
$$
h_0h_1h_2=-k,\qquad h_0+h_1+h_2=k,
\quad h_i=k/D_i.                                          \tag{5.2}
$$
Every nonzero integer solution of $abc+a+b+c=0$ contains both $1$ and
$-1$. To see this, if $|a|,|b|\ge2$, then
$|(a+b)/(ab+1)|<1$: for equal signs use
$|ab|+1>|a|+|b|$, and for opposite signs use
$|ab|-1>\bigl||a|-|b|\bigr|$. Thus all three entries cannot have
absolute value at least two. If one is $1$, the equation factors as
$(b+1)(c+1)=0$; if one is $-1$, it factors as $(b-1)(c-1)=0$.
Combining with (5.2), the coefficient multiset is $(1,-1,k)$, and
the denominator multiset is $(k,-k,1)$, including the repetitions when
$k=\pm1$.

At a state with $D=1$, one has $ps=0$. Equations (2.2) and (5.1)
give exactly the following two possibilities, expressed as integral
rank-one factorizations:
$$
\boxed{\quad
A_{\gamma,q}(k)=
\left(\frac{2\gamma}{q},q,\frac{\gamma k-1}{q},0\right),
\quad q\in\mathbb Z\setminus\{0\},\quad
q\mid2,\quad q\mid(\gamma k-1),\quad}                       \tag{5.3}
$$
$$
\boxed{\quad
B_{\gamma,r}(k)=
\left(0,\frac{-\gamma k-1}{r},r,\frac{2\gamma}{r}\right),
\quad r\in\mathbb Z\setminus\{0\},\quad
r\mid2,\quad r\mid(-\gamma k-1).\quad}                    \tag{5.4}
$$
For necessity, if $s=0$ then $rs=0$, $pq=2\gamma$ and
$E=\gamma k$, giving (5.3). If $p=0$ then $pq=0$, $rs=2\gamma$
and $E=-\gamma k$, giving (5.4). The alternatives cannot overlap at
the same section state, since $p=s=0$ would give $I=0$.

For sufficiency, the denominators from (5.3) are, in order,
$(1,-\gamma k,\gamma k)$, with coefficients
$(k,-\gamma,\gamma)$. Those from (5.4) are
$(1,\gamma k,-\gamma k)$, with coefficients
$(k,\gamma,-\gamma)$. They are nonzero integers and all updates are
integral. The scalar-channel update matrices are
$$
\binom{p_{n+1}}{p_n}=
\begin{pmatrix}-h_n&1\\1&0\end{pmatrix}\binom{p_n}{p_{n-1}},
\qquad
\binom{s_{n+1}}{s_n}=
\begin{pmatrix}h_n&1\\1&0\end{pmatrix}\binom{s_n}{s_{n-1}}.
$$
Multiplying the respective three matrices and substituting (5.3) or
(5.4) gives, for either family,
$$
Y_k^3(v)=-\gamma v.                                      \tag{5.5}
$$
For example, for (5.3) the $p$-channel product is
$\left(\begin{smallmatrix}-\gamma&0\\1-\gamma k&\gamma\end{smallmatrix}\right)$,
and its action on $(2\gamma/q,(\gamma k-1)/q)^T$ is
$-\gamma$ times that vector. The $s$-channel product is
$\left(\begin{smallmatrix}\gamma&0\\1-\gamma k&-\gamma\end{smallmatrix}\right)$
and acts on $(0,q)^T$ in the same way. For (5.4) these products are
$\left(\begin{smallmatrix}\gamma&0\\1+\gamma k&-\gamma\end{smallmatrix}\right)$
and
$\left(\begin{smallmatrix}-\gamma&0\\1+\gamma k&\gamma\end{smallmatrix}\right)$,
respectively, and the same substitution proves (5.5).

The three-entry quotient words have least period three, since their
entries cannot all agree for $k\ne0$. The states are nonzero. Therefore
the exact native period is three for $\gamma=-1$ and six for
$\gamma=1$. Equation (5.5) and the denominator words also ensure all
negative iterates are ordinary. All cyclic rotations of (5.3) and (5.4)
give the complete stratum. Different presentations may name the same
cycle; no quotient by sign or scaling is taken in assigning its period.

## 6. Complete quotient-period-four stratum

Equation (4.4), with (3.1), is
$$
k\gamma\lambda=(\gamma\lambda+1)(\gamma+\lambda),
\qquad B\ne0.                                            \tag{6.1}
$$
If $\gamma\lambda=0$, this forces $\gamma=\lambda=0$.
Otherwise
$$
k=\gamma+\lambda+\frac1\gamma+\frac1\lambda.
$$
The last two terms must have integer sum. Opposite signs give a sum
strictly between $-1$ and $1$, so it must be zero; this would force
$\gamma+\lambda=0$ and then $k=0$, excluded here. With both parameters
positive the integer reciprocal sum is one or two. Sum two forces
$(\gamma,\lambda)=(1,1)$, while sum one is equivalent to
$(\gamma-1)(\lambda-1)=1$, hence $(2,2)$. Negating both gives the
negative cases. Thus the complete invariant list is
$$
(\gamma,\lambda)=(0,0)\ (k\ne0\text{ arbitrary}),
\quad (1,1),k=4;\quad (2,2),k=5,
\quad (-1,-1),k=-4;\quad (-2,-2),k=-5.                     \tag{6.2}
$$

For $(0,0)$, equation (3.3), with $t=\varepsilon k$, is
$E^2+(t-1)E+1-t=0$. The value $E=1$ is impossible, and otherwise
$$
t=-E-\frac1{E-1}.
$$
Integrality forces $E-1\mid1$, so $E=0$ or $2$. The first is a pole;
the second forces $t=-3$, contrary to $E\mid k$. This entire branch
has no ordinary integral periodic lift.

The involution
$$
U(p,q,r,s)=(s,r,q,p),\qquad Y_{-k}U=UY_k,                  \tag{6.3}
$$
preserves integrality, ordinary denominators and the native clock. On
normalized invariants it gives
$(\gamma,\lambda)\mapsto(-\lambda,-\gamma)$. It is therefore enough
to handle the two positive exceptional parameters.

At $(\gamma,\lambda,k)=(2,2,5)$, one has $A=-1$, $B=5$.
The two unit-section equations (3.3) are $E^2=0$ and
$E^2-2E+10=0$. Neither allows a nonzero real, hence integer, $E$.
This removes $k=5$ and by (6.3) $k=-5$.

At $(\gamma,\lambda,k)=(1,1,4)$, one has $A=-2$, $B=2$.
For $\varepsilon=1$, (3.3) gives
$(E-1)(E+2)=0$; for $\varepsilon=-1$ it gives
$E^2-3E+6=0$, with negative discriminant. Starting from either allowed
unit section, (2.3) produces the same cyclic denominator word
$(1,4,-2,4)$. At its $D=1$, $E=4$ section, (2.2) forces
$$
pq=ps=rs=0,\qquad rq=3.
$$
Thus necessarily $p=s=0$, and every integral factorization is
$$
\boxed{\qquad v=(0,q,r,0),\qquad q,r\in\mathbb Z,
\qquad qr=3.\qquad}                                      \tag{6.4}
$$
Conversely its first four iterates are
$$
(0,q,r,0)\longmapsto(r,0,0,q)
\longmapsto(-r,q,r,q)
\longmapsto(-r,q,-r,-q)
\longmapsto(0,-q,-r,0).
$$
All denominators are the nonzero word $(1,4,-2,4)$, and
$Y_4^4(v)=-v$. Its quotient has least period four, and $v\ne0$;
the least native period is exactly eight. All cyclic rotations of
(6.4), together with their images under $U$ at $k=-4$, exhaust the
order-four stratum, with no removal of zero coordinates or pole filling.

## 7. No quotient-period-five integral stratum

Write $d=\gamma\lambda$ and $S=\gamma+\lambda$, so $B=d+1$.
The order-five equation (4.5) is
$$
d k^2-BS k+B^3=0,\qquad B\ne0.                            \tag{7.1}
$$
For $d\ne0$, its discriminant as a quadratic in $k$ is
$$
\Delta=B^2\bigl((\gamma-\lambda)^2
                    -4\gamma^2\lambda^2\bigr).            \tag{7.2}
$$
For nonzero integers $\gamma,\lambda$,
$$
|\gamma-\lambda|\le |\gamma|+|\lambda|
                  \le2|\gamma\lambda|.
$$
Equality throughout requires opposite signs and
$|\gamma|=|\lambda|=1$, which would give $B=0$. Thus for the present
case $B\ne0$ the discriminant in (7.2) is strictly negative, ruling out
even real $k$.

For $d=0$, one has $B=1$, and (7.1) reduces to $kS=1$.
Thus $k=1$ or $-1$. Every integral ordinary denominator $D\mid k$
then belongs to $\{1,-1\}$. There are at most four possible ordered
quotient states $(D,E)$, so a least-period-five orbit is impossible.
This exhausts the order-five stratum for all integer $k$.

## 8. Exact stopping boundary and ownership

The new arithmetic ingredients are Lemma 3.1, the integer parameters
and section equation, and the complete low-order integral-family
reconstruction. The map, invariant quotient and classical elliptic
group framework are inherited sources/results, not claimed as new here.
The torsion conditions in Section 4 are elementary chord-law deductions;
no global novelty or substantial-increment clearance is asserted.

To close the original atlas it remains necessary to exclude or classify
all integral ordinary lifts of quotient orders $6,7,8,9,10,12$, with
their exact $\pm1$ return multipliers and integral rank-one
factorizations. An unproved proposed connection to torsion/Miller
functions is not an accepted shortcut across this boundary. A finite
period list, the three strata above or a bounded census is not the
requested full answer.

At this version: zero mathematical program executions in the ninth-pass
AY lane; zero old diagnostic reruns; no mathematical claim inferred
from a numerical table; no author/global/older-file edits outside the
owned ninth-pass lane. Further source checks, if performed, are to be
recorded separately rather than retroactively claimed by this proof.
