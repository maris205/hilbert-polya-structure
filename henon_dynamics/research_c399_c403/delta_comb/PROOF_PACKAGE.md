# Proof Package

## Claim

Candidate B admission proof: fixed positive finite coupling on the harmonic
delta-comb, its two-term spectral counting law, and its singular Dirichlet limit.
This is a research proof draft, not a numbered paper, released paper package, or
independent-review receipt. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Let $h_0=0$, $h_n=\sum_{j=1}^n j^{-1}$, $x_n=\pi h_n$, and
$I_n=(x_{n-1},x_n)$, so that $\ell_n=|I_n|=\pi/n$. Fix
$0<\kappa<\infty$. On $\mathcal H=L^2(0,\infty;\mathbb C)$ impose a
Dirichlet condition at zero and define

$$
\begin{split}
\mathcal D_\delta&=\{f\in H^1_0(0,\infty):
                         \sum_{n=1}^\infty|f(x_n)|^2<\infty\},\\
q_\kappa[f]&=\|f'\|_2^2+\kappa\sum_{n=1}^\infty|f(x_n)|^2.
\end{split}                                                     \tag{1}
$$

The claims proved below are as follows.

1. The form domain equals
   $\mathcal D=H^1_0(0,\infty)\cap L^2((0,\infty),e^{x/\pi}dx)$.
   The form is densely defined, nonnegative and closed; its associated
   self-adjoint operator $H_\kappa$ has compact resolvent and positive simple
   eigenvalues $E_j(\kappa)$ tending to infinity. They give a complete
   orthonormal eigenbasis.
2. With the inclusive counting convention
   $N_\kappa(E)=\#\{j:E_j(\kappa)\le E\}$, for each fixed $\kappa$,

   $$
   N_\kappa(k^2)=2k\log k+C_\kappa k+O_\kappa(\log k),\qquad
   C_\kappa=\log(4\pi/\kappa)+\gamma-2,\quad k\longrightarrow\infty.
                                                                  \tag{2}
   $$

   More explicitly, there exist $k_0(\kappa)>1$ and
   $M(\kappa)<\infty$ such that the absolute error in (2) is at most
   $M(\kappa)\log k$ for every real $k\ge k_0(\kappa)$, including
   eigenvalue thresholds. No uniform estimate in $\kappa$ is asserted.
3. For $t\downarrow0$,

   $$
   \operatorname{Tr}(e^{-tH_\kappa})
   =\frac{\sqrt\pi}{2\sqrt t}\log\frac{\pi}{\kappa t}
      +O_\kappa(\log(1/t)).                                      \tag{3}
   $$

   The source spectral zeta function $Z_\kappa(s)=\sum_jE_j(\kappa)^{-s}$,
   initially absolutely convergent for $\operatorname{Re}s>1/2$, has a
   meromorphic continuation to $\operatorname{Re}s>0$. Its only pole in that
   half-plane is at $s=1/2$, with principal part

   $$
   \frac{1/2}{(s-1/2)^2}
       +\frac{1+C_\kappa/2}{s-1/2}.                              \tag{4}
   $$

4. For every real $p>0$, $H_\kappa^{-1}\in\mathcal S_p$ if and only if
   $p>1/2$. The same threshold holds for every fixed resolvent
   $(H_\kappa-z)^{-1}$, $z\in\rho(H_\kappa)$. In particular the ordinary
   Fredholm determinant $\det(I-zH_\kappa^{-1})$ exists.
5. As $\kappa\uparrow\infty$, $H_\kappa$ converges in norm resolvent sense
   to the direct sum of the Dirichlet Laplacians on the $I_n$.
   Eigenvalues, listed with multiplicity, increase to this endpoint spectrum.
   For every fixed $E$, the inclusive counts eventually equal the endpoint
   count, even when $E$ is an endpoint eigenvalue. At that endpoint,

   $$
   \begin{split}
   N_\infty(k^2)&=\sum_{1\le n\le k}\lfloor k/n\rfloor
      =k\log k+(2\gamma-1)k+O(\sqrt k),\\
   Z_\infty(s)&=\zeta(2s)^2\quad(\operatorname{Re}s>1/2).
   \end{split}                                                    \tag{5}
   $$

   Consequently the two iterated limits are different:

   $$
   \lim_{\kappa\to\infty}\lim_{k\to\infty}
          \frac{N_\kappa(k^2)}{k\log k}=2,\qquad
   \lim_{k\to\infty}\lim_{\kappa\to\infty}
          \frac{N_\kappa(k^2)}{k\log k}=1.                        \tag{6}
   $$

## Status

PROVABLE AS STATED

This status is the author's mathematical conclusion for the precisely quantified
claims above. Independent review is pending. It is not a novelty certificate.
The model, finite-positive-coupling discreteness, strong resolvent limit, and
Dirichlet divisor theory belong to Egger né Endres and Steiner. The proposed
increment is the finite-coupling two-term law with a controlled error, together
with its consequences and the comparison of limiting orders. See
[SOURCE_AUDIT.md](SOURCE_AUDIT.md) for the bounded literature search and its gaps.

## Assumptions

- $\kappa$ is a positive, finite, energy-independent real constant until the
  separate strong-coupling limit. The edge lengths and initial boundary
  condition are exactly those in (1).
- $H^1_0(0,\infty)$ denotes the Sobolev space of $L^2$ functions with $L^2$
  weak derivative and zero trace at zero. There is no imposed trace at infinity.
  Every such function has a continuous representative, used at the vertices.
- The form representation theorem, compact spectral theorem, min--max principle,
  one-dimensional local Rellich compactness, and monotone convergence of
  nonnegative closed forms are background Hilbert-space theorems. Their
  hypotheses are checked below; they are not conclusions of finite computation.
- The Bessel series and connection identity, decaying Bessel solution, and
  sectorial Gamma/digamma asymptotics used in Step 6 are classical identities
  [DLMF 10.25.2--3](https://dlmf.nist.gov/10.25),
  [10.27.4](https://dlmf.nist.gov/10.27.E4), and
  [5.11.1--2](https://dlmf.nist.gov/5.11). All parameter-uniform estimates
  needed here are derived below, rather than imported from a fixed-parameter
  asymptotic assertion.
- $k=\sqrt E$ is the source positive frequency. The physical quantum clock is
  $i\partial_t\psi=H_\kappa\psi$ with evolution $e^{-itH_\kappa}$.
  No prime-dependent lengths, target zeros, or clock fitted to such data enter
  the construction.

## Notation

$\gamma=\lim_n(h_n-\log n)$ is Euler's constant. Norms without a weight are
in $L^2(0,\infty)$. Define

$$
V_\kappa(x)=\frac{\kappa n}{\pi}\quad(x\in I_n),\qquad
C=\frac{\kappa e^{-\gamma}}{\pi},\qquad B=\frac{\kappa}{\pi}.
                                                                  \tag{7}
$$

For $a,C>0$, let $A_{a,C}$ be the operator associated with the closed form

$$
Q_{a,C}[f]=a\|f'\|_2^2+\int_0^\infty Ce^{x/\pi}|f(x)|^2dx,
\qquad f\in\mathcal D.                                          \tag{8}
$$

The symbol $O_\kappa$ permits constants depending on the fixed coupling;
$O_C$ permits dependence on $C$, but in Step 6 is uniform for
$a\in[1/2,3/2]$. The ideal $\mathcal S_p$ is defined by summability of the
$p$-th powers of singular values, also for $0<p<1$.

## Proof Strategy

First compare endpoint sampling with its cell average without losing control
as the cells shrink. Harmonic-number bounds turn the averaged potential into
an exponential potential with a bounded additive error. This proves the exact
form domain and compactness. A Bessel phase calculation gives a uniform
two-term count for the exponential comparators. Choosing the form comparison
parameter $\epsilon=1/k$ then costs only $O_\kappa(\log k)$ in counting.
Stieltjes transforms give the heat and zeta statements. Finally, monotone forms
and compact domination close the strong-coupling endpoint and its counting
thresholds.

## Dependency Map

| Step | Inputs | Output used later |
| --- | --- | --- |
| 1--2 | Fundamental theorem for $|f|^2$; harmonic sums | Global sampling estimate and exponential comparison |
| 3--5 | Steps 1--2; form representation and local compactness | Closed form, operator domain, simple discrete spectrum |
| 6 | Classical Bessel/Gamma identities plus explicit compact-parameter bounds | Uniform exponential-comparator count |
| 7 | Steps 3 and 6; min--max | Finite-coupling two-term law with $O_\kappa(\log k)$ |
| 8--10 | Step 7; absolutely convergent Stieltjes integrals | Heat trace, zeta principal part, Schatten/determinant |
| 11--13 | Monotone forms; Step 4 compactness; elementary divisor count | Endpoint eigenvalues, inclusive thresholds, unequal iterated limits |

## Proof

### 1. A sampling estimate valid before taking any infinite sum

Take $f\in H^1_0(0,\infty)$ and an integer $N\ge1$. On one cell the
absolutely continuous representative satisfies

$$
\big||f(x_n)|^2-|f(x)|^2\big|
\le 2\int_x^{x_n}|f(y)f'(y)|dy.
$$

Averaging in $x\in I_n$ and changing the order in this nonnegative integral
give

$$
\left||f(x_n)|^2-\frac1{\ell_n}\int_{I_n}|f|^2\right|
\le\frac2{\ell_n}\int_{I_n}(y-x_{n-1})|ff'|(y)dy
\le2\int_{I_n}|ff'|.
$$

Adding the first $N$ cells and applying Cauchy--Schwarz yields

$$
\left|\kappa\sum_{n=1}^N|f(x_n)|^2
             -\int_0^{x_N}V_\kappa|f|^2\right|
\le2\kappa\|f\|_2\|f'\|_2.                                    \tag{9}
$$

Both expressions on the left before subtraction are nonnegative and increase
with $N$. A uniform bound on their difference shows that one has a finite
limit if and only if the other does. Passing to their limits then proves

$$
\mathcal D_\delta=H^1_0\cap L^2(V_\kappa dx),\qquad
\left|\kappa\sum_{n\ge1}|f(x_n)|^2-\int V_\kappa|f|^2\right|
\le2\kappa\|f\|_2\|f'\|_2.                                    \tag{10}
$$

In particular (10) is not an exchange of two possibly divergent series.

### 2. The exact exponential coefficient and a global additive bound

The sequences $h_n-\log n$ and $h_n-\log(n+1)$ decrease and increase,
respectively, to the same limit $\gamma$. To check the signs, integrate $1/x$
over $[n,n+1]$ and $[n+1,n+2]$ and compare it with its endpoint values.
Their difference is $\log(1+1/n)\to0$. Hence for $n\ge1$,

$$
\log n+\gamma<h_n<\log(n+1)+\gamma.                             \tag{11}
$$

Also $0<\gamma<1$, as follows from the same integral comparisons and, for
strict positivity, $h_n-\log(n+1)\ge1-\log2>0$.
For $x\in I_n$ and $n\ge2$, (11) gives
$n-1<e^{x/\pi-\gamma}<n+1$. For $n=1$, its lower bound is replaced by
$0<e^{-\gamma}\le e^{x/\pi-\gamma}$ and its upper bound remains $2$.
Thus, on all cells,

$$
|n-e^{x/\pi-\gamma}|\le1,\qquad
|V_\kappa(x)-Ce^{x/\pi}|\le B.                                \tag{12}
$$

An additive bounded difference of nonnegative weights has the same weighted
$L^2$ domain after intersection with $L^2$. Combining (10) and (12) proves
$\mathcal D_\delta=\mathcal D$. This also fixes the factor
$e^{-\gamma}/\pi$ in $C$; losing that factor would give the wrong linear
coefficient in (2).

### 3. Closedness, density, and the operator represented by the form

For every $0<\epsilon<1$, Young's inequality in (10) gives, on the common
domain $\mathcal D$,

$$
Q_{1-\epsilon,C}[f]-d_\epsilon\|f\|_2^2
\le q_\kappa[f]
\le Q_{1+\epsilon,C}[f]+d_\epsilon\|f\|_2^2,
\qquad d_\epsilon=\kappa^2/\epsilon+B.                          \tag{13}
$$

The norm $\|f\|_2^2+Q_{1,C}[f]$ is complete: a Cauchy sequence converges
in $H^1_0$ and in the weighted $L^2$ space, and these limits agree as
unweighted $L^2$ functions. With $\epsilon=1/2$, (13) shows that this
norm and $\|f\|_2^2+q_\kappa[f]$ are equivalent. For example the lower
bound in (13) controls $Q_{1/2,C}$ by
$q_\kappa+(2\kappa^2+B)\|f\|_2^2$; $Q_{1,C}\le2Q_{1/2,C}$.
The upper bound gives the other comparison. The form is therefore closed.

The space $C_c^\infty(0,\infty)$ is a form core. Indeed, a smooth cutoff
equal to one on $[0,R]$, zero beyond $R+1$, and with uniformly bounded
derivative approximates any $f\in\mathcal D$ in weighted $H^1$ norm as
$R\to\infty$. On a fixed bounded interval the exponential weight is bounded
above and below by positive constants, so the usual $H^1_0$ approximation
by smooth compactly supported functions gives the second approximation.
This space is dense in $\mathcal H$, proving dense definition. The form
representation theorem produces the unique nonnegative self-adjoint
$H_\kappa$ associated with (1).

For completeness its domain has the following non-formal description:

$$
\begin{split}
D(H_\kappa)=\{f\in\mathcal D:;&f|_{I_n}\in H^2(I_n)\ (n\ge1),
\ \sum_n\|f''\|_{L^2(I_n)}^2<\infty,\\
&f'(x_n+)-f'(x_n-)=\kappa f(x_n)\ (n\ge1)\},\\
(H_\kappa f)|_{I_n}&=-f''|_{I_n}.                              \tag{14}
\end{split}
$$

Here continuity and $f(0)=0$ already follow from $f\in\mathcal D$.
To derive (14) from the weak form, use tests supported inside each cell to
obtain $-f''=g\in L^2$, hence $H^2$ regularity on that bounded cell.
Tests meeting one vertex and integration by parts give the displayed jump
with its positive sign. Conversely these local identities imply
$q_\kappa(f,v)=\langle g,v\rangle$ for every compactly supported smooth
test $v$: the endpoint derivative contribution at $x_n$ is
$f'(x_n-)-f'(x_n+)$ and cancels the $\kappa f(x_n)$ term.
The form-core approximation extends this identity to every
$v\in\mathcal D$, giving membership in the associated operator domain.
No unspecified boundary term at infinity is used.

### 4. Compactness and strict positivity

A sequence bounded in the form norm has uniformly bounded $H^1$ norm and
uniformly bounded $\int Ce^{x/\pi}|f|^2$ by (13). For every $R>0$,

$$
\int_R^\infty |f|^2\le C^{-1}e^{-R/\pi}
                            \int_R^\infty Ce^{x/\pi}|f|^2.       \tag{15}
$$

On $[0,R]$ local Rellich compactness gives an $L^2$-convergent subsequence.
A diagonal subsequence and the uniform tail bound (15) give convergence in
$\mathcal H$. Thus the form embedding is compact, and the associated
resolvent is compact. The compact spectral theorem gives a discrete
eigenvalue list tending to infinity and a complete orthonormal basis.
The list is infinite because $\mathcal H$ is infinite-dimensional and the
resolvent is injective. If $H_\kappa f=0$, (1) implies $f'=0$ almost
everywhere; the only such $L^2$ function is zero. Since zero is not a
finite accumulation point for a compact-resolvent spectrum, $E_1(\kappa)>0$.

### 5. Simplicity at finite coupling

For a fixed eigenvalue $E$, an eigenfunction satisfies $f''+Ef=0$ on
the first cell with $f(0)=0$. It is completely specified by $f'(0+)$.
Continuity and the jump in (14) propagate its two Cauchy data to the next
cell, successively for all $n$. If $f'(0+)=0$, this propagation gives the
zero function. Therefore the eigenspace has dimension at most one.
Self-adjointness rules out generalized eigenvectors, proving the claimed
simple spectrum. This argument does not apply to the decoupled endpoint,
where the eigenvalues have divisor multiplicities.

### 6. A parameter-uniform exponential-comparator counting lemma

We now prove the assertion needed later, not merely a fixed-parameter version:
for fixed $C>0$ there are $r_0(C)$ and $M_C$ such that for all
$a\in[1/2,3/2]$ and all real $r\ge r_0(C)$,

$$
\left|N_{A_{a,C}}(r^2)
 -\frac{2r}{\sqrt a}\left[\log\frac{2r}{\sqrt C}-1\right]\right|
\le M_C.                                                       \tag{16}
$$

The unitary change of variables $x=2\pi y$ transforms $A_{a,C}$ into

$$
\frac{a}{4\pi^2}\mathcal B_b,\qquad
\mathcal B_b=-\frac{d^2}{dy^2}+b^2e^{2y},\qquad
b=2\pi\sqrt{C/a},\qquad K=\frac{2\pi r}{\sqrt a}.              \tag{17}
$$

Its left boundary is Dirichlet. Here $b$ ranges in a fixed compact interval
$[b_-,b_+]\subset(0,\infty)$. The form argument used in Step 4 gives a
positive compact-resolvent operator for each $b$. The equation at energy
$K^2$ changes under $z=be^y$ to the modified Bessel equation of order
$iK$. Its unique square-integrable solution at infinity is proportional to
$K_{iK}(be^y)$: the decaying solution is asymptotic to
$\sqrt{\pi/(2be^y)}e^{-be^y}$, and the second independent solution grows
like $e^{be^y}/\sqrt{2\pi be^y}$. Consequently all positive comparator
eigenvalues, and no others, satisfy $K_{iK}(b)=0$.

Set $d=b^2/4$. The exact Bessel series and connection formula give, for
$K>0$,

$$
\begin{split}
I_{-iK}(b)&=\frac{(b/2)^{-iK}}{\Gamma(1-iK)}S_b(K),\\
S_b(K)&=\sum_{j=0}^\infty\frac{d^j}{j!(1-iK)_j},\\
K_{iK}(b)&=\frac{\pi\,\operatorname{Im}I_{-iK}(b)}{\sinh(\pi K)}.
\end{split}                                                     \tag{18}
$$

The rising product in the $j$-th term has modulus at least $K^j$.
Differentiating that term introduces a sum of $j$ factors of modulus at
most $1/K$. Normal convergence of the series and its derivative on
$K\ge K_0>0$ justifies termwise differentiation. In particular, for
$K\ge1$, uniformly in $b\in[b_-,b_+]$,

$$
|S_b(K)-1|\le e^{d_+/K}-1,\qquad
|S_b'(K)|\le\frac{d_+}{K^2}e^{d_+/K},\qquad d_+=b_+^2/4.       \tag{19}
$$

Choose $K_0$ so large that $e^{d_+/K_0}-1<1/2$. Then $S_b$ stays in
the disk $|z-1|<1/2$, with the single-valued logarithm there. Its argument
is $O_C(K^{-1})$ and its argument derivative is $O_C(K^{-2})$.
Use the continuous logarithm of $\Gamma(1+iK)$ obtained from the analytic
logarithm on the right half-plane, real at $1$. Sectorial Stirling and
digamma asymptotics give

$$
\begin{split}
\operatorname{Im}\log\Gamma(1+iK)
 &=K\log K-K+\pi/4+O(K^{-1}),\\
\operatorname{Re}\psi(1+iK)&=\log K+O(K^{-2}).
\end{split}                                                     \tag{20}
$$

The sector is fixed; no $b$ occurs in these two error bounds. Defining the
unwrapped phase

$$
\Psi_b(K)=K\log(2/b)+\operatorname{Im}\log\Gamma(1+iK)
                                      +\operatorname{Im}\log S_b(K),
$$

equations (19)--(20) imply

$$
\begin{split}
\Psi_b(K)&=K\log(2K/b)-K+\pi/4+O_C(K^{-1}),\\
\Psi_b'(K)&=\log(2K/b)+O_C(K^{-2})>0
\end{split}                                                     \tag{21}
$$

after one further increase of $K_0$, still independent of $b$ in its
compact interval. The nonzero amplitude in (18) shows that above $K_0$
the roots occur exactly once each time the increasing phase crosses an
integer multiple of $\pi$. At a root the convention $\le$ changes the
count by at most one. The roots below $K_0$ are uniformly bounded in
number by $N_{\mathcal B_{b_-}}(K_0^2)$, since
$\mathcal B_b\ge\mathcal B_{b_-}$. The phase at $K_0$ is also bounded
uniformly in $b$. We have proved

$$
N_{\mathcal B_b}(K^2)
=\frac{K}{\pi}\left[\log(2K/b)-1\right]+O_C(1)                 \tag{22}
$$

uniformly on the whole compact parameter interval. Substitution of (17)
gives $2K/b=2r/\sqrt C$ and proves (16). The uniformity is what permits
the moving value $a=1\pm1/k$ in the next step. A fixed-$a$ statement
alone would not suffice.

### 7. Min--max and the two-term finite-coupling count

Take $k\ge2$, set $\epsilon=1/k$, and put
$d_k=\kappa^2 k+B$. Inequality (13) and the min--max principle imply

$$
N_{A_{1+1/k,C}}(k^2-d_k)
\le N_\kappa(k^2)
\le N_{A_{1-1/k,C}}(k^2+d_k).                                  \tag{23}
$$

For $k$ sufficiently large depending on $\kappa$, both energies in (23)
are positive and $r_\pm=\sqrt{k^2\pm d_k}=k+O_\kappa(1)$.
Define

$$
F(a,r)=\frac{2r}{\sqrt a}\left[\log(2r/\sqrt C)-1\right].
$$

On $a\in[1/2,3/2]$ and $r=k+O_\kappa(1)$ its derivatives satisfy

$$
\partial_rF=\frac2{\sqrt a}\log(2r/\sqrt C)=O_\kappa(\log k),
\qquad
\partial_aF=-\frac r{a^{3/2}}[\log(2r/\sqrt C)-1]
                                      =O_\kappa(k\log k).       \tag{24}
$$

The mean value theorem, (16), and (23) therefore bound both counting
comparators by $F(1,k)+O_\kappa(\log k)$. Finally,

$$
F(1,k)=2k\log k+[\log(4/C)-2]k
      =2k\log k+[\log(4\pi/\kappa)+\gamma-2]k,
$$

which proves (2), including its real-$k$ and threshold quantifiers.

### 8. Heat trace and its two leading terms

Equation (2), now written with $E=k^2$, reads

$$
N_\kappa(E)=E^{1/2}\log E+C_\kappa E^{1/2}+R_\kappa(E),
\qquad R_\kappa(E)=O_\kappa(\log(E+2))\quad(E\ge1).            \tag{25}
$$

It implies summability of $e^{-tE_j}$ for each $t>0$. Stieltjes integration
by parts is justified by $N_\kappa(E)=0$ below the positive ground energy
and by exponential decay at infinity:

$$
\operatorname{Tr}(e^{-tH_\kappa})
=t\int_0^\infty e^{-tE}N_\kappa(E)dE.                          \tag{26}
$$

Extend $R_\kappa$ on $(0,1)$ by the equality in (25). There it is
integrable, since $E^{1/2}\log E$ is integrable and the counting function
is bounded. Its contribution to (26) is $O_\kappa(t)$ on this interval.
For $0<t\le1/2$, substitution $u=tE$ and
$\log(2+u/t)\le\log(1/t)+\log(2+u)$ show that the contribution of the
remainder on $[1,\infty)$ is $O_\kappa(\log(1/t))$.
Differentiation of the absolutely convergent Gamma integral at $3/2$
evaluates the remaining two terms:

$$
\frac{\Gamma(3/2)}{\sqrt t}
 [\log(1/t)+\psi(3/2)+C_\kappa].                              \tag{27}
$$

Using $\Gamma(3/2)=\sqrt\pi/2$ and
$\psi(3/2)=2-\gamma-2\log2$ gives
$\psi(3/2)+C_\kappa=\log(\pi/\kappa)$, proving (3).

### 9. Spectral zeta continuation, with its domain made explicit

For $\operatorname{Re}s>1/2$, absolute convergence from (25) permits
Stieltjes integration by parts:

$$
Z_\kappa(s)=s\int_0^\infty N_\kappa(E)E^{-s-1}dE.
$$

Splitting at $E=1$ and inserting (25) yields

$$
Z_\kappa(s)
=\frac{s}{(s-1/2)^2}+\frac{sC_\kappa}{s-1/2}
 +s\int_1^\infty R_\kappa(E)E^{-s-1}dE
 +s\int_0^1 N_\kappa(E)E^{-s-1}dE.                            \tag{28}
$$

The last integral is entire, since its integrand is zero below the positive
ground energy. The preceding integral is holomorphic on
$\operatorname{Re}s>0$: on each compact subset, (25) bounds the integrand
and every $s$-derivative by an integrable multiple of
$E^{-1-\eta}(\log E)^m$ for some $\eta>0$.
Equation (28) is thus the asserted meromorphic continuation. Expanding its
first two rational terms at $s=1/2$ proves (4), and the nonzero double-pole
coefficient shows that this is a genuine pole. No continuation to $s=0$
or formula for a zeta-regularized determinant is supplied by this estimate.

### 10. Sharp Schatten threshold and the ordinary determinant

For real $p>0$, the same positive Stieltjes integral gives
$\sum_j E_j^{-p}=p\int_0^\infty N_\kappa(E)E^{-p-1}dE$, with
both sides allowed to be infinite. The leading term in (25) is positive
and dominates its lower-order terms. Thus convergence is equivalent to
convergence of $\int_1^\infty E^{-p-1/2}\log E\,dE$, namely $p>1/2$.
At the endpoint $p=1/2$ this integral diverges like the integral of
$(\log E)/E$; no endpoint ideal membership is concealed.
The singular values of $H_\kappa^{-1}$ are the $E_j^{-1}$, so this proves
the assertion. For a fixed $z\in\rho(H_\kappa)$, the ratios
$|E_j-z|/E_j$ tend to one, proving the identical resolvent threshold.

In particular $\sum_jE_j^{-1}<\infty$, and the ordinary product

$$
D_\kappa(z)=\det(I-zH_\kappa^{-1})
           =\prod_{j=1}^\infty(1-z/E_j(\kappa))                 \tag{29}
$$

converges locally uniformly in $z\in\mathbb C$. Its zeros are precisely
the simple source eigenvalues. Formula (29) is not an explicit special
function evaluation of the comb determinant: the Bessel function in Step 6
belongs to a comparator, not to $H_\kappa$.

### 11. The increasing-form limit and norm resolvent convergence

Fix $\kappa_0>0$ and let $\kappa\ge\kappa_0$. The nonnegative closed
forms $q_\kappa$ increase. Their supremum is finite exactly on

$$
\mathcal D_\infty
=\{f\in H^1_0(0,\infty):f(x_n)=0\text{ for every }n\ge1\},
\qquad q_\infty[f]=\|f'\|_2^2.                               \tag{30}
$$

Every function in (30) is in $\mathcal D_\delta$, because its entire
sampled sum is zero; Step 1 therefore also shows it lies in $\mathcal D$.
The subspace is closed in $H^1_0$ by continuity of each finite-position
trace. It is dense in $L^2$: finite sums of smooth functions compactly
supported in individual open cells are dense in the orthogonal direct
sum $\bigoplus_n L^2(I_n)$. Thus the increasing-form convergence theorem
applies with a densely defined closed limit and yields strong resolvent
convergence to the operator in (30).

The limit form is exactly the direct sum of the forms of the Dirichlet
Laplacians on $I_n$: restricting a function gives the separate Dirichlet
traces, and conversely gluing zero-endpoint functions with summable $L^2$
and derivative norms gives a global $H^1_0$ function. Write
$R_\kappa=(H_\kappa+1)^{-1}$ and $R_\infty=(H_\infty+1)^{-1}$.
Order reversal for nonnegative forms gives

$$
0\le R_\kappa-R_\infty\le R_{\kappa_0},\qquad
R_\kappa-R_\infty\longrightarrow0\text{ strongly}.             \tag{31}
$$

The upper operator in (31) is compact by Step 4. Here is the compact
domination argument upgrading (31) to norm convergence. If
$0\le T_\kappa\le K$ with $K$ compact positive, choose a finite-rank
spectral projection $P$ of $K$ so that
$\|(I-P)K(I-P)\|<\delta$. Then
$\|(I-P)T_\kappa(I-P)\|<\delta$, and positivity plus
Cauchy--Schwarz for $\langle T_\kappa\cdot,\cdot\rangle$ bounds the
off-diagonal blocks by $\sqrt{\|K\|\delta}$. The block
$PT_\kappa P$ tends to zero in norm by strong convergence on a finite
dimensional space. Letting $\delta\downarrow0$ proves
$\|T_\kappa\|\to0$. Applied to (31), this proves norm resolvent
convergence. This norm conclusion is stronger than the strong-resolvent
statement already in the original model paper, but is a consequence of
compact domination, not a new general operator theorem.

### 12. Endpoint multiplicities, eigenvalue convergence, and thresholds

The Dirichlet eigenvalues on the $n$-th interval are
$(\pi m/\ell_n)^2=m^2n^2$, $m\ge1$. Counting all pairs shows that
the multiplicity of $j^2$ is the divisor count $d(j)$ and gives the first
identity in (5). It also shows directly that $R_\infty$ is compact.

Norm convergence of the compact positive resolvents in Step 11 and the
compact min--max principle give convergence of each of their eigenvalues
in decreasing order, including repetitions. Transforming back by
$r\mapsto r^{-1}-1$ yields

$$
E_j(\kappa)\uparrow E_j(\infty)\quad\text{for every fixed }j.
                                                                  \tag{32}
$$

Monotonicity follows also directly from increasing forms, and
$E_j(\kappa)\le E_j(\infty)$ from form-domain restriction.
Fix a real energy $E$ and put $J=N_\infty(E)$. For $j\le J$,
$E_j(\kappa)\le E_j(\infty)\le E$, so all those modes are counted for
every finite $\kappa$. The next endpoint eigenvalue satisfies
$E_{J+1}(\infty)>E$. By (32), $E_{J+1}(\kappa)>E$ once
$\kappa$ is sufficiently large. All following modes are then excluded.
Hence

$$
N_\kappa(E)=N_\infty(E)\quad\text{for all sufficiently large }\kappa
\quad\text{at every fixed }E.                                  \tag{33}
$$

This proof explicitly includes $E=j^2$. It uses the inclusive convention
$\le$ and convergence from below. For the alternative convention $<$,
convergence away from endpoint eigenvalues follows, but (33) at endpoint
thresholds does not follow and is not asserted: modes can approach a
threshold from below. There is no uniform choice of the coupling threshold
in (33) as $E\to\infty$.

### 13. Elementary divisor asymptotics and the unequal iterated limits

Let $L=\lfloor\sqrt k\rfloor$. Splitting the lattice pairs $mn\le k$
according to $m\le L$ or $n\le L$ gives the exact hyperbola identity

$$
\sum_{n\le k}\lfloor k/n\rfloor
 =2\sum_{n\le L}\lfloor k/n\rfloor-L^2
 =2kh_L-L^2+O(L).                                               \tag{34}
$$

Integral bounds refine (11) to $h_L=\log L+\gamma+O(1/L)$:
the two monotone bounds differ by $\log(1+1/L)\le1/L$.
Since $L=\sqrt k+O(1)$, substituting in (34) proves the second equality
in (5) for real $k\to\infty$. Absolute convergence for
$\operatorname{Re}s>1/2$ permits the separate sums in

$$
\sum_{m,n\ge1}(m^2n^2)^{-s}
 =\left(\sum_{n\ge1}n^{-2s}\right)^2,
$$

proving the endpoint zeta identity. Equations (2) and (33)--(34) now give
the two iterated limits in (6), in the indicated order.

## Corrections or Missing Assumptions

The original scout formula requires no weakening for fixed positive finite
$\kappa$, but several tempting stronger conclusions are not part of this
proof.

- The comparator remainder is uniform only when its positive parameters range
  in the compact set specified in Step 6. The final comb error is
  $O_\kappa(\log k)$, not $O(1)$ and not uniform as
  $\kappa\to0$ or $\kappa\to\infty$.
- Threshold convergence in Step 12 has an inclusive counting convention.
  It must not be relabelled as an assertion about strict counts at square
  thresholds.
- The value $\kappa=0$ is excluded from (1)--(4): its closed physical form
  is the free Dirichlet half-line form on $H^1_0$, whose spectrum is
  $[0,\infty)$ rather than a discrete list. One cannot substitute zero into
  $C_\kappa$ or into a claimed compact form domain.
- Equation (28) stops at $\operatorname{Re}s>0$. The ordinary determinant
  in (29) is valid, but $Z_\kappa'(0)$ is not obtained here.
- C398's bounded-remainder obstruction to an affine frequency comparison
  with target zero counting cannot be transported through the form
  comparison: the loss here is $O_\kappa(\log k)$. Neither a matching mean
  law nor this error proves or disproves equality of full target divisors.
- Dirichlet endpoint arithmetic is not a primitive rational-prime owner for
  finite $\kappa$. The coupling limit changes the leading coefficient, and
  no finite-coupling Euler product, target functional equation, root number,
  bad Euler factor, or Hilbert--Pólya operator is claimed.

## Open Risks

1. Independent mathematical review has not yet been performed on this draft.
   Priority review points are the common form domain, the uniform phase count,
   the $\epsilon=1/k$ error transfer, and inclusive strong-coupling thresholds.
2. The bounded source audit did not find the finite-coupling two-term formula
   in the sources actually inspected. It cannot certify global novelty or
   present-day openness. A full prior formula found later would eliminate the
   proposed independent contribution even if this derivation remains correct.
3. The accompanying sanity calculations compare two finite-interval numerical
   discretizations and check analytical constants. They are not interval
   certificates for the infinite spectrum, not an experimental proof of
   compactness, and not evidence of target arithmetic.
4. A finite-coupling trace formula with explicit orbit weights and continuation
   beyond the half-plane in (28) remains outside this admission package.
   No such result is hidden in the word “determinant”.
