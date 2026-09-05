# Complete bounded Lozi dynamics and its instability-clock obstruction

## Claim and status

**PROVABLE AS STATED.** Fix $a>4$ and
$F_a(x,y)=(1-a|x|-y,x)$. On its entire set $K_a$ of bounded two-sided
orbits, $F_a$ is conjugate to the full two-shift, is uniformly hyperbolic,
and has the complete periodic and stability atlas below. For integral
$a\ge5$, every periodic expanding multiplier is a quadratic unit and
no positive rational multiple of its logarithmic modulus is the logarithm
of a positive integer greater than one.

This is a sufficient parameter chamber, not a sharp horseshoe boundary.
It does not settle the pruned parameter of C116. The map is nonsmooth on
$x=0$, but the entire set being differentiated stays a positive distance
from that line.

## Assumptions and notation

Let $\Sigma=\{-1,+1\}^{\mathbb Z}$ with left shift $\sigma$.
Set $R=(a-2)^{-1}$, $q=2/a$, $\delta=(a-4)/(a(a-2))$ and
$r=(a-\sqrt{a^2-4})/2$. Thus $0<q,r<1$, $a-r=r^{-1}$.
For $s\in\Sigma$, define the map on bounded real sequences
$$ (\mathcal T_s x)_j=\frac{s_j}{a}(1-x_{j-1}-x_{j+1}). $$
Symbols encode the sign of the first coordinate. A based word is read in
forward time; cyclic rotations of a primitive word describe one oriented
orbit. The original clock is one application of $F_a$. A separately
defined instability roof below is a change of clock, not physical time.

## Dependency map

1. Banach contraction on $\ell^\infty(\mathbb Z)$ gives all bounded orbits.
2. Positive sign margin and local dependence give the topological conjugacy.
3. Strictly contracting projective maps give continuous invariant lines and
   a uniform hyperbolic splitting.
4. The coding and affine returns give all periods, matrices and reversal.
5. An integral determinant-one matrix gives a quadratic-unit obstruction.
6. Symbolic periodic counts give an unweighted source zeta only; a bounded
   flat-trace germ is separately defined with its actual stability weights.

## 1. All bounded orbits, not a selected invariant subset

The map $\mathcal T_s$ has Lipschitz constant $q$ and takes the closed
radius-$R$ ball to itself since $(1+2R)/a=R$. Its unique fixed point
$x(s)$ therefore obeys $|x_j|\le R$ and
$$ s_j x_j=\frac{1-x_{j-1}-x_{j+1}}a\ge\delta>0. $$
It consequently solves
$x_{j+1}=1-a|x_j|-x_{j-1}$ with exactly the prescribed signs.
Conversely, for any bounded two-sided orbit let $M=\sup_j|x_j|$.
The recurrence implies $aM\le1+2M$, hence $M\le R$ and the same positive
sign bound. Its sign sequence is defined and uniqueness identifies the
orbit with $x(s)$. This proves exhaustion of $K_a$.

Define $\pi(s)=(x_0(s),x_{-1}(s))$. Iterating $\mathcal T_s$ from zero
$N$ times uses only a finite window of symbols for each output coordinate,
and its uniform error is at most $Rq^N$. Thus $\pi$ is continuous in the
product topology. It is injective because $F_a$ has the global continuous
inverse $(x,y)\mapsto(y,1-a|y|-x)$, so a state determines every sign.
It is surjective by exhaustion. Compactness of $\Sigma$ makes $\pi$ a
homeomorphism onto compact $K_a$, and $F_a\pi=\pi\sigma$.

For two parameters $a,b>4$, comparing their fixed-point equations also gives
$$ \|x_a(s)-x_b(s)\|_\infty
\le \frac{|a-b|}{(a-2)(b-2)}. $$
Indeed, $(1-2/a)\|x_a-x_b\|_\infty$ is bounded by
$|a^{-1}-b^{-1}|(1+2/(b-2))$. The symbolic conjugacies are therefore
uniformly parameter-continuous inside this sufficient chamber.

## 2. Uniform hyperbolicity with variable matrices

On sign $s$ the derivative is
$$ A_s=\begin{pmatrix}-as&-1\\1&0\end{pmatrix},\qquad\det A_s=1. $$
For the unstable cone $|v|\le r|u|$, the image satisfies
$|u'|\ge(a-r)|u|=r^{-1}|u|$ and $|v'|\le r|u'|$.
The projective slope map $t=v/u$ is
$t\mapsto(-as-t)^{-1}$. It preserves $[-r,r]$ and its derivative in
absolute value is at most $r^2$. Compositions from the infinite past
therefore have a unique uniform limit, defining a continuous invariant
unstable slope $t^u_j$. The first-coordinate expansion on this line is at
least $r^{-1}$ at every step.

Apply the same construction to $A_s^{-1}$ on the stable cone
$|u|\le r|v|$ using the infinite future. This gives a continuous invariant
stable line with inverse-time expansion at least $r^{-1}$. The two cones
are disjoint except at zero because $r<1$, so their lines form a uniformly
transverse splitting. On the stable line, forward contraction follows by
inverting the inverse-time expansion. In the max norm the bounds have
constant one. A neighborhood of $K_a$ avoids the switching line at each
base point, so these are genuine derivatives of the original map, not a
formal matrix cocycle across a singular orbit.

## 3. The complete periodic atlas

The conjugacy yields $\#\operatorname{Fix}(F_a^n)=2^n$ for every $n\ge1$,
with no periodic point elsewhere in $\mathbb R^2$ since a periodic orbit
is bounded. The number of least-period-$n$ oriented cycles is
$$ P_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d}. $$
Every based word $w=s_0\ldots s_{n-1}$ gives the affine return
$F_w(v)=M_w v+c_w$, where
$$ M_w=A_{s_{n-1}}\cdots A_{s_0},\quad
c_w=\sum_{j=0}^{n-1}A_{s_{n-1}}\cdots A_{s_{j+1}}\binom10. $$
The empty matrix product is the identity. Hyperbolicity excludes the
eigenvalue one, so $v_w=(I-M_w)^{-1}c_w$. Its orbit has exactly the word's
least symbolic period. This is an exact rational formula whenever $a$ is
rational; no numerical sign decision is needed.

Put $\tau_w=\operatorname{tr}M_w$. The eigenvalues are real and reciprocal;
write $\lambda_u(w)$ for the one with modulus greater than one.
Then $|\lambda_u(w)|\ge r^{-n}$ and
$$ \operatorname{sign}\lambda_u(w)=(-1)^n\prod_{j=0}^{n-1}s_j,\quad
\lambda_s(w)=\lambda_u(w)^{-1},\quad
\det(I-M_w)=2-\tau_w. $$
For repetition $w^k$, $M_{w^k}=M_w^k$ and multipliers are raised to the
$k$th power. Traces obey $\tau_{k+1}=\tau_w\tau_k-\tau_{k-1}$ with
$\tau_0=2$, $\tau_1=\tau_w$. Sign and reciprocal cancellation are retained.

The involution $J(x,y)=(y,x)$ satisfies $JF_aJ=F_a^{-1}$.
It reverses words up to a cyclic rotation and conjugates their monodromy
to an inverse matrix. Reversal is not quotiented out of the oriented
primitive count. The Jacobian is one on each smooth branch; the global
map is piecewise affine and preserves area. Neither fact supplies a
Hilbert–Pólya operator.

## 4. Two honest source generating objects

The unweighted Artin–Mazur zeta is
$$ Z_a(z)=\exp\left(\sum_{n\ge1}\frac{2^n z^n}{n}\right)
=\frac1{1-2z},\qquad |z|<\tfrac12, $$
with its elementary meromorphic continuation. Its primitive product is
$\prod_\gamma(1-z^{n_\gamma})^{-1}$. It discards the variable stability
matrices and is not called a stability determinant.

Separately set
$$ b_n=\sum_{F_a^n x=x}\frac1{|\det(I-DF_a^n(x))|},\qquad
d_a(z)=\exp\left(-\sum_{n\ge1}\frac{b_n z^n}{n}\right). $$
For any eigenvalue with modulus $L\ge r^{-n}$,
$|\det(I-M)|\ge L(1-L^{-1})^2$, whence
$$ 0<b_n\le \frac{(2r)^n}{(1-r^n)^2}
\le\frac{(2r)^n}{(1-r)^2}. $$
Thus $d_a$ is a well-defined nonzero holomorphic germ on
$|z|<(2r)^{-1}$, with logarithmic truncation error after $N$ bounded by
$$ \frac{(2r|z|)^{N+1}}{(N+1)(1-r)^2(1-2r|z|)}. $$
Regrouping its absolutely convergent logarithm by primitive orbits uses
the actual factors $|\det(I-M_\gamma^k)|^{-1}$ at repetition $k$.
It does not replace them by powers of a single diagnostic edge weight.
No trace-class operator realization or continuation outside this disk is
asserted for this germ.

## 5. A derived instability clock and an exact arithmetic obstruction

The invariant unstable slope supplies the positive roof
$$ \ell(s)=\log|-a s_0-t^u_0(s)|\ge\log r^{-1}>0. $$
It is continuous, is obtained from the derivative without prime data, and
its sum on a periodic orbit is exactly $\log|\lambda_u(w)|$ by telescoping
the first-coordinate scaling. This roof defines a new suspension clock;
it is not the one-step clock used in $Z_a$ and $d_a$.

Suppose now $a\in\mathbb Z$, $a\ge5$. Then $M_w\in SL_2(\mathbb Z)$
and $|\tau_w|>2$. The integer $\tau_w^2-4$ is not a square: for
$T=|\tau_w|\ge3$, it lies strictly between $(T-1)^2$ and $T^2$.
Consequently the expanding eigenvalue is a quadratic algebraic integer
unit with conjugate inverse. If $|\lambda_u|^k$ were a rational number
for $k\ge1$, applying the nontrivial conjugation would equate this number
with its reciprocal. Positivity forces it to be one, contradicting
expansion. If $c=h/j>0$ is rational and
$c\log|\lambda_u|=\log m$ for an integer $m>1$, then
$|\lambda_u|^h=m^j$ gives the same contradiction.

This excludes every rationally rescaled exact integer/prime-power clock
match for each periodic instability period. It does not exclude approximate
matching, irrational rescalings, different arithmetic fields at rational
nonintegral $a$, or a different roof. Those are not conclusions here.

## Boundaries, controls and open risks

The sign-margin proof fails at $a=4$ and is not used there. Below that
chamber pruning is possible; the old C116 parameter is not covered.
Constant-symbol words, period one, repetition and negative multipliers are
included. The same symbolic count $2^n$ holds throughout this chamber while
the multiplier data change, so symbolic counts alone cannot validate an
arithmetic bridge. The integer-clock exclusion applies equally to primes
and composites. Finite exact rows audit formulas; they do not prove the
unbounded statements. Literature priority for horseshoe coding, cone
methods or algebraic-unit arguments is not claimed.
