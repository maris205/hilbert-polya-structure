# HCS-C257 theorem package

## Frozen object

Let $a\in\mathbb C^*$, $p_a(z)=z^2-a^2$, and let

\[
N_a(z)=z-\frac{p_a(z)}{p_a'(z)}=\frac{z^2+a^2}{2z}
\]

act on the Riemann sphere.  Set

\[
C_a(z)=\frac{z-a}{z+a},\qquad
C_a^{-1}(w)=a\frac{1+w}{1-w}.
\]

## Global Newton--Cayley theorem

For every $a\ne0$:

1. $C_a\circ N_a\circ C_a^{-1}(w)=w^2$, hence
   $C_a(N_a^n z)=C_a(z)^{2^n}$ for all $n\ge0$.
2. The basins of $+a$ and $-a$ are respectively

   \[
   |C_a(z)|<1\iff\Re(z/a)>0,\qquad
   |C_a(z)|>1\iff\Re(z/a)<0.
   \]
   Their common boundary
   $\Re(z/a)=0\cup\{\infty\}$ is the Julia set.
3. If $w=C_a(z)$ lies in the $+a$ basin, then

   \[
   N_a^n(z)-a=\frac{2a w^{2^n}}{1-w^{2^n}}.
   \]
   If $v=w^{-1}$ lies in the $-a$ basin, then

   \[
   N_a^n(z)+a=-\frac{2a v^{2^n}}{1-v^{2^n}}.
   \]
   Thus the exact Cayley error is squared at every step.
4. Apart from $w=0,\infty$, a point is preperiodic exactly when $w$ is a
   root of unity.  If its order is $m=2^e q$ with $q$ odd, its exact tail
   is $e=v_2(m)$ and its eventual exact period is
   $\operatorname{ord}_q(2)$, with $\operatorname{ord}_1(2)=1$.  It is
   periodic exactly when $e=0$.
5. The fixed-point, exact-period-point, and primitive-cycle counts are

   \[
   F_n=2^n+1,\quad
   P_n=\sum_{d\mid n}\mu(n/d)(2^d+1),\quad
   O_n=P_n/n.
   \]
   Both root fixed points have multiplier $0$; every exact $n$-cycle on
   the Julia set has multiplier $2^n$.  Consequently

   \[
   \zeta_{AM}(t)=\exp\!\left(\sum_{n\ge1}\frac{F_n}{n}t^n\right)
   =\frac1{(1-t)(1-2t)}.
   \]
6. Haar measure on $|w|=1$ pushes under
   $z=ia\cot(\theta/2)$ to

   \[
   d\nu(s)=\frac{ds}{\pi(1+s^2)},\qquad z=ias.
   \]
   The induced boundary map is $s\mapsto(s^2-1)/(2s)$; the measure is
   invariant and mixing, and its Cayley-angle Lyapunov exponent is $\log2$.

## Proof

Substitution of $N_a$ into $C_a$ gives $C_a(N_a(z))=C_a(z)^2$.
Iteration proves item 1.  The two basin inequalities reduce to
$|z-a|<|z+a|$, equivalently $\Re(z/a)>0$; the Julia statement is the
Möbius image of the unit circle.  Inverting $C_a$ proves the two exact
error identities.

For $D(w)=w^2$, $D^n(w)=w^{2^n}$.  A nonzero finite periodic point has
$w^{2^n-1}=1$, so its order is odd; repeated squaring removes exactly one
factor of $2$ from the root order at each step and then cycles by
multiplication by $2$ in $(\mathbb Z/q\mathbb Z)^*$.  This proves item 4.
The equation $D^n(w)=w$ contributes $0$, $\infty$, and $2^n-1$
nonzero finite roots, proving $F_n$; Möbius inversion proves $P_n,O_n$.
At a nonzero periodic point,
$(D^n)'(w)=2^n w^{2^n-1}=2^n$; at $0,\infty$ the multiplier is zero.
Summing the geometric logarithms gives the zeta formula.  Finally write
$w=e^{i\theta}$: angle doubling preserves and mixes Haar measure, while
$z=ia\cot(\theta/2)$ gives the standard Cauchy density and the stated
rational boundary map.

## Boundary and ownership ledger

- $N_a(au)=aN_1(u)$; changing $a$ to $-a$ swaps root labels.
- At $a=0$, $N_0(z)=z/2$ for finite $z$, and the degree-two theorem is
  not silently extended across this degree drop.
- C141 owns a Hardy-space inverse-branch Ruelle operator for $z^2-6$.
  C257 builds no such operator.
- C177 owns degree-$b$ circle Wold/mixing theory.  C257 owns the Newton
  sphere, two root basins, exact root error, and even-order preperiodic tails.

These are workspace ownership distinctions, not literature-priority claims.
The source-local zeta is not an arithmetic Euler product and does not license
Route B.
