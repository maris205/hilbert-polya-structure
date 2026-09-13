# Forward/backward degree asymmetry and real first-hit parameters

Date: 2026-09-05. Author-side supplement to the coefficient-cancellation
candidate. It addresses the same fixed map, not a new paper. No candidate
PASS or scientific/publication lock is granted. The forward proof and
parameter V2 are unchanged while being reviewed.

## Claim

Let
$$
F_\delta(x,y,p,z)=(X,Y,P,Z),\qquad\delta\in\mathbb C^*,
$$
where
$$
P=p+x^3+2xy,\quad Z=z+x^2,\quad
X=x+P^2,\quad Y=y+\delta Z^6.
$$
Write $d_n^-=\deg(F_\delta^{-n})$, so $d_0^-=1$. For a nonzero
parameter $\epsilon$, let $m(\epsilon)$ be the first positive time at
which the coefficient orbit
$$
r_0=0,\qquad r_{j+1}=\frac{\epsilon}{(1+2r_j)^4}
$$
hits $-1/2$; set $m(\epsilon)=\infty$ if it never does.

1. If $m(-\delta)=\infty$, then
   $$
   d_n^-=8\cdot6^{n-1}\quad(n\ge1),\qquad
   \sum_{n\ge0}d_n^-t^n=\frac{1+2t}{1-6t}.
   $$
2. If $m(-\delta)=m<\infty$ and $L=m+2$, then
   $$
   \boxed{\sum_{n\ge0}d_n^-t^n=
   \frac{1+2t-24t^L}{(1-6t)(1-16t^L)}.}
   $$
   The minimal eventual constant-coefficient recurrence has characteristic
   polynomial $(T-6)(T^L-16)$ and order $L+1$. The displayed recurrence
   $d_{n+L+1}^-=6d_{n+L}^-+16d_{n+1}^--96d_n^-$ holds from $n=0$.
3. Put $a_*=4^4/5^5$. For every integer $m\ge1$ there is exactly one
   real parameter $a_m$ with
   $$
   a_1=1,\qquad a_*<a_m<a_{m-1}\quad(m\ge2)
   $$
   such that the orbit of $1$ under $u\mapsto1-a_m/u^4$ stays positive
   until its first zero at time $m$. These $a_m$ decrease to $a_*$ and
   are algebraic. Consequently, for
   $$
   \delta_m=-a_m/2,\qquad L=m+2,
   $$
   the forward minimal eventual degree-recurrence order is $L+1$ and the
   backward order is $1$. Changing the parameter sign interchanges these
   two orders. Both time directions have first dynamical degree $6$.

The uniqueness in item3 concerns this all-positive pre-zero orbit branch;
it does not classify every real first-hit parameter. No simultaneous
classification of the pairs $(m(\delta),m(-\delta))$ for arbitrary complex
parameters is claimed beyond the exact individual tests above.

## Status and assumptions

**Author status: PROVABLE AS STATED. Independent review: requested.**

The field is $\mathbb C$ for the degree theorem; the real branch uses the
usual real order and intermediate value theorem. Coefficients are nonzero,
and all multivariate degrees are actual ordinary total degrees in the four
independent initial variables. Polynomial conjugacy does not preserve these
exact sequences, so the proof below does not transfer them by conjugacy.

## Dependencies and strategy

The supplement uses the normal-wall and three-step restart lemmas proved in
[the forward author proof](PAPER29_BOUNDARY_VIABILITY_20260905.md), Sections2–3.
It verifies their hypotheses for a different actual seed and calculates the
final extra shear's visible degree. The real parameter branch is an
independent elementary construction, not an application of the complex
root-count formula.

1. An explicit linear involution identifies the reverse phase order and
   changes the coefficient sign.
2. Two actual seeded forward steps enter the certified error-layer state.
3. The final shear converts cancellation events into different degree pulses.
4. Pole noncancellation proves minimum order, not just an upper bound.
5. A monotone positive scalar branch realizes every first hit over the reals.

## Proof

### 1. Reverse phase order and the exact seed

Let $S=S_V$ and $T_\epsilon=T_{W_\epsilon}$, so $F_\epsilon=T_\epsilon S$.
The linear involution
$$
J(x,y,p,z)=(-x,y,p,-z)
$$
is anti-symplectic, but preserves ordinary degree under conjugation. Direct
substitution, including both signs, gives
$$
J S^{-1}J=S,\qquad JT_\delta^{-1}J=T_{-\delta}.
$$
Thus with $\epsilon=-\delta$,
$$
JF_\delta^{-n}J=(ST_\epsilon)^n
=S F_\epsilon^{n-1}T_\epsilon\qquad(n\ge1).
$$
The last identity is an equality of composed maps. It does not imply that
the degree of the right side equals that of $F_\epsilon^{n-1}$.

Set $H_k=F_\epsilon^kT_\epsilon$ for $k\ge0$. Then the reverse degree
is precisely the degree of $S H_{n-1}$. The initial seed is
$$
H_0=(x+p^2,\ y+\epsilon z^6,\ p,\ z).
$$
Its position degrees are $2,6$. Its two positions have distinct leading
variables; they are not initially a normal-wall state.

### 2. Two seeded steps enter the proven error-layer regime

Let the position coordinates of $H_1$ be $\xi,\eta$, and its momentum
coordinates be $\pi,\zeta$. Applying $F_\epsilon$ to $H_0$ gives
$$
\deg(\xi,\eta,\pi,\zeta)=(16,24,8,4),
$$
where degree of a tuple in this display is componentwise. Indeed, in its
first momentum update the mixed term has degree $2+6=8$, strictly above
the pure cube's degree $6$ and old momentum's degree $1$. The second
momentum update has degree $4$. The position powers then give $16,24$.
In the original independent variables,
$$
\operatorname{top}(\xi)=4\epsilon^2p^4z^{12},\qquad
\operatorname{top}(\eta)=\epsilon p^{24}.
$$
Both are nonzero for every allowed coefficient.

In the next step the first momentum's pure cube has degree $48$, strictly
above the mixed term's $40$ and old momentum's $8$. The second momentum
has degree $32$. Thus $H_2$ has degrees $(96,192,48,32)$ and leading
position ratio $\epsilon$.

Write its positions as $x_2,y_2$ and put $E_2=y_2-\epsilon x_2^2$.
The exact expression before collecting is
$$
E_2=\eta+\epsilon(\zeta+\xi^2)^6
-\epsilon\bigl(\xi+(\pi+\xi^3+2\xi\eta)^2\bigr)^2.
$$
The degree192 layer cancels. The unique next layer is
$$
-8\epsilon\xi^{10}\eta,
\qquad\deg=184.
$$
Terms at least quadratic in $\eta$ have degree at most176; terms containing
$\zeta$ have degree at most164; terms containing $\pi$ have degree at
most152. The external additions are smaller as well. Hence this error is
nonzero, and the certified state for $H_2$ is
$$
(a,s,r)=(96,8,\epsilon),\qquad a\ge6s.
$$
All hypotheses of the forward normal-wall and restart lemmas now hold.

### 3. The last shear and the reverse degree pulses

At a normal-wall state with $r\ne-1/2$, the extra map $S$ has first
momentum degree $3a$, strictly larger than the position degrees $a,2a$,
the second momentum degree $2a$ and the old first momentum degree $a/2$.
Therefore $\deg(SH_k)=3a$ there.

At a critical state $(a,s,-1/2)$, this momentum is instead $p+2xE$,
so its degree is $3a-s$. It is still strictly largest because $s\le a/6$.
At the next two states B and C of the forward three-step lemma, the extra
shear is respectively mixed-dominated and pure-dominated. The reverse
degrees read off at these three states are
$$
3a-s,\qquad18a-2s,\qquad108a-12s.
$$
The first momentum is strictly larger than every other component in each
case, using the explicit B/C inequalities in that lemma. Thus the list
records actual map degrees, not degrees of an invisible component.

The next state returns to the normal-wall orbit at coefficient $\epsilon$,
with $(a,s)$ changed by the already proved restart. If $\epsilon=-1/2$,
this is immediately the next critical state; otherwise normal steps
precede the next hit. Both situations are covered by the same pulse rule.

Before a first hit, the initial two reverse degrees are $8,48$; subsequent
normal steps multiply by6. If $m(\epsilon)=\infty$, this proves
$d_n^-=8\cdot6^{n-1}$ for all $n\ge1$.

If $m(\epsilon)=m<\infty$, the first critical state is $H_{m+1}$,
since $H_2$ has ratio $r_1=\epsilon$. Hence the first reverse-degree drop
is at time $n=m+2=L$. Its state has
$$
a=96\cdot6^{m-1},\qquad s=8.
$$
After one entire length-L cycle the error gap is multiplied by16.

Put $e_n=d_n^--6d_{n-1}^-$ for $n\ge1$. The initial value is $e_1=2$.
At each critical time the pulse is $-s$; one step later it is $+4s$,
because $(18a-2s)-6(3a-s)=4s$. The subsequent C-state pulse is zero,
and all normal-state pulses are zero. The first gap is8. Therefore
$$
\sum_{n\ge1}e_nt^n
=2t+\frac{-8t^L+32t^{L+1}}{1-16t^L}
=\frac{2t-8t^L}{1-16t^L}.
$$
Multiplication by $1-6t$ and $d_0^-=1$ now give the claimed inverse
generating function.

### 4. Minimum order and common exponential rate

At $t=1/6$, the inverse numerator is
$4/3-24/6^L>0$. At a zero of $1-16t^L$, it becomes $2t-1/2$.
A common zero would require $t=1/4$ and then $L=2$, excluded here.
Thus no factor of the displayed denominator cancels, even over $\mathbb C$.
Its degree is $L+1$, which is exactly the minimal eventual recurrence
order. Because the numerator degree is smaller, this recurrence already
holds at every $n\ge0$ in the stated forward-indexed form.

The noncancelled pole at $1/6$ has positive leading coefficient, and the
other pole moduli are $16^{-1/L}>1/6$. Thus the inverse first dynamical
degree is6. The forward proof gives the same rate. These equal rates
were computed, not inferred from symplecticity or polynomial conjugacy.

### 5. A real, monotone first-hit branch for every time

Write $R_{-a}(u)=1-a/u^4$ with $a>0$. Set
$$
u_0(a)=1,\qquad u_{j+1}(a)=1-a/u_j(a)^4
$$
as long as the preceding value is positive. Whenever all these values are
positive, induction gives strict monotonicity with respect to $a$:
$$
u_{j+1}'(a)=-u_j(a)^{-4}+4a u_j(a)^{-5}u_j'(a)<0
\quad(j\ge1),\qquad u_1'(a)=-1.
$$
Each $u_j$ is a continuous rational function on the positive-orbit interval.

The number $u_*=4/5$ is a fixed point for $a_*=4^4/5^5$, since
$(1-u_*)u_*^4=a_*$. The map $R_{-a_*}$ is strictly increasing in its
positive argument. Starting at1 therefore gives $u_j(a_*)>u_*$ for each
finite $j$: if an iterate is larger than $u_*$, its next value is larger
than $R_{-a_*}(u_*)=u_*$. In particular every finite iterate is positive.

Now $u_1(a)=1-a$ has its unique zero at $a_1=1$, and is positive on
$(0,a_1)$. Suppose $a_{m-1}>a_*$ has been constructed, and all earlier
values are positive on $(0,a_{m-1})$. On $(a_*,a_{m-1})$, $u_m$ is
continuous and strictly decreasing. Its value at $a_*$ is positive, whereas
$$
u_{m-1}(a)\longrightarrow0^+\quad(a\longrightarrow a_{m-1}^-)
\quad\Longrightarrow\quad u_m(a)\longrightarrow-\infty.
$$
The intermediate value theorem and strict monotonicity give exactly one
zero $a_m$ in $(a_*,a_{m-1})$. All preceding values are positive there.
The same monotonicity shows $u_m>0$ on $(0,a_m)$, closing the induction.
Uniqueness concerns precisely the branch with positive preceding iterates.

The decreasing sequence $a_m$ has a limit $a_\infty\ge a_*$. If this
limit were greater, choose $a\in(a_*,a_\infty)$. Then $u_j(a)>0$ for
every $j$. Moreover the time sequence is strictly decreasing: its first
step is below1, and the map is strictly increasing on positive arguments,
so each successive comparison propagates. Its limit $u$ cannot be zero,
as $1-a/u_j^4$ would then become negative. Thus $0<u<1$, and continuity
gives $a=(1-u)u^4$.

On $[0,1]$, the function $(1-u)u^4$ has derivative $u^3(4-5u)$ and
unique interior maximum $a_*$ at $u=4/5$. This contradicts $a>a_*$.
Hence $a_m\downarrow a_*$.

The relation $u_m(a_m)=0$ makes $-a_m$ a root of the integer polynomial
$A_m$ from the corrected parameter proof. Therefore $a_m$ is algebraic.
No root-count formula or simplicity assertion is required for the real
existence argument.

### 6. Unbounded directional asymmetry

For $\delta_m=-a_m/2<0$, the coefficient map is conjugate to $R_{-a_m}$
and first hits $-1/2$ at time $m$. The forward theorem gives minimum
eventual order $L+1$, where $L=m+2$. On the other hand $-\delta_m>0$,
and its ratio sequence starts at zero and stays strictly positive after
the first step; it cannot hit $-1/2$. Items1–2 therefore give backward
order1. Replacing $\delta_m$ by $-\delta_m$ interchanges the two tests.
This proves the directional statement for real polynomial symplectic maps
in the same fixed family. $\square$

## Targeted diagnostic, not a proof dependency

As a check on the sign and the first inverse-drop index, the inverse map
was evaluated in univariate polynomials modulo1009 along the line
$(x,y,p,z)=(2t,3t,5t,7t)$ at $\delta=1/2$. The coordinate degrees for
$n=1,\ldots,6$ were
$$
(2,6,8,4),\ (16,24,48,32),\ (96,192,280,192),
$$
$$
(560,1152,1712,1120),\ (3424,6720,10272,6848),\
(20544,41088,61504,41088).
$$
The maxima agree with the inverse generating function for $L=3$.
Finite-field/line specialization cannot prove the complex multivariate
statement; the actual proof is the strict-degree seed calculation above.

## Boundaries and remaining checks

- The supplement requires independent verification before entering a final
  candidate theorem package. It must be supplied explicitly to reviewers,
  not counted silently as if already reviewed with the earlier two files.
- No claim is made that exact ordinary degrees are invariant under polynomial
  or symplectic conjugacy. The extra seed and final-shear calculations are
  necessary, not optional details.
- This is not a classification of all real exceptional parameters or all
  possible pairs of forward/backward hitting times.
- Real critical-orbit parameter methods and recurrence/degree asymmetry are
  established topics. Novelty must be assessed for the precise fixed-family
  theorem, after comparison with those sources and the root-of-unity control.
- No physical periodic-orbit, integrability, topological-entropy, higher
  dynamical-degree, or cohomological-stabilization assertion is made.
