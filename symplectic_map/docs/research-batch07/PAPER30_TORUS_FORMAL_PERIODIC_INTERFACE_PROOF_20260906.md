# Paper30 T branch: formal periodic interface and a conditional generic consequence

Date: 2026-09-06. Author proof-stage supplement, not a selected paper,
independent review, novelty PASS or capacity assessment. The two earlier
torus proof records remain unchanged.

## Claim

Let $\mathbb T^2=\mathbb R^2/\mathbb Z^2$ and set
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
F_\kappa(q,p)=A(q,p+\kappa\sin(2\pi q)),\quad t=\pi\kappa.
$$
Let $\mathcal T$ denote the complex finite Fourier polynomials and put
$\delta_t=F_{t/\pi}^*-1$. Each coefficient of a series in $\mathcal T[[t]]$
has finite Fourier support; there is no support bound uniform in its order.

**Theorem 1 (unconditional formal interface).** For $G\in\mathcal T[[t]]$,
the following are equivalent:

1. The formal orbit sum of $G$ vanishes on the analytic continuation at
   $t=0$ of every periodic point of $A$, with every positive return time.
2. There exists $H\in\mathcal T[[t]]$ such that $G=\delta_tH$.

The primitive is unique modulo $\mathbb C[[t]]$. Neither series is asserted
to converge at any nonzero parameter.

Define
$$
\mathcal B=\{f(q)-f(q-p): f\text{ is a one-variable finite Fourier polynomial}\}.
$$
For a finite Fourier support space $V$, write $B_V=V\cap\mathcal B$.
The unresolved fixed-support formal rigidity assertion is
$$
\tag{FR(V)}
G\in V[[t]],\ H\in\mathcal T[[t]],\ G=\delta_tH
\quad\Longrightarrow\quad G\in B_V[[t]].
$$

**Theorem 2 (explicitly conditional).** Fix a connected real open interval
$I\ni0$ on which every $F_\kappa$ is Anosov. If $\mathrm{FR}(V)$ holds,
there exist finitely many analytic periodic branches on $I$ and a real
analytic complex-valued function $D_V$ on $I$, not identically zero, such
that for every $\kappa\in I$ with $D_V(\kappa)\ne0$, the common kernel in
$V$ of these branches' orbit sums equals $B_V$. Consequently the kernel
of all actual periodic orbit sums in $V$ equals $B_V$ there.

If $\mathrm{FR}(V)$ holds for every finite support space, one may exclude
a countable subset $E\subset I$ and obtain this equality simultaneously
for all finite Fourier polynomials at every $\kappa\in I\setminus E$.
The latter set is residual and has full Lebesgue measure in $I$.

## Status

- Theorem 1: `PROVABLE AS STATED`; complete author proof below.
- Theorem 2 as the stated implication: `PROVABLE AS STATED`, with an
  explicitly unproved hypothesis; scientific status `CONDITIONAL_THEOREM`.
- $\mathrm{FR}(V)$ for arbitrary $V$: `OPEN` in this file.
- The original all-support assertion at every fixed sufficiently small
  nonzero real parameter: `OPEN`. Neither theorem proves it.

## Assumptions and notation

For $m=(r,s)\in\mathbb Z^2$, set $E_m=e^{2\pi i(rq+sp)}$ and $e=(1,0)$.
Because $A$ is symmetric, its pullback sends $E_m$ to $E_{Am}$.
The already derived formula is
$$
F_{t/\pi}^*E_m=E_{Am}\exp\{t(r+s)(z-z^{-1})\},\qquad z=e^{2\pi iq}.
\tag{1}
$$
Its coefficient at each order is a finite Fourier polynomial. Thus
$\delta_t$ acts on all of $\mathcal T[[t]]$ by coefficientwise finite
convolution in the parameter order.

For every $n\geq1$ and $x_0\in\operatorname{Fix}(A^n)$, choose a real
lift $\widetilde x_0$ and let $\ell=(A^n-I)\widetilde x_0\in\mathbb Z^2$.
The derivative in $x$ at $(0,\widetilde x_0)$ of
$$
\widetilde F_{t/\pi}^{\,n}(x)-x-\ell
\tag{2}
$$
is $A^n-I$, which is invertible. The real analytic implicit function
theorem gives a unique local analytic solution $x_{n,x_0}(t)$ reducing to
$x_0$ on the torus. Its Taylor series is the formal periodic branch used
in Theorem 1. Different lifts change no Fourier evaluation.

For $G=\sum_{k\geq0}t^kG_k$, define
$$
\mathscr L_{n,x_0}(G)=
\sum_{j=0}^{n-1}G(t,F_{t/\pi}^{\,j}x_{n,x_0}(t))\in\mathbb C[[t]].
\tag{3}
$$
At order $N$, (3) uses only $G_0,\ldots,G_N$, finitely many Fourier
terms from each, and finitely many Taylor coefficients of the branch.
This makes (3) well-defined and $\mathbb C[[t]]$-linear without convergence
of $G$. Periodic points are indexed with return times, not necessarily
their least periods; repetitions cause no problem.

## Proof strategy and dependency map

1. For the linear cat map, combine the classical additive Livšic theorem
   with decay of the Fourier coefficients of a continuous function.
   This proves that finite Fourier data with zero periodic sums have a
   finite Fourier primitive.
2. Subtract one finite primitive at a time from the formal data. Exact
   telescoping preserves every formal periodic condition. Division by
   $t$ reduces the next step to the same linear statement.
3. For Theorem 2 only, use the assumed rigidity to compute the common
   periodic-row kernel over $\mathbb C((t))$. Finite-dimensional linear
   algebra selects a nonzero analytic minor. Its zeros are isolated in
   a common real Anosov interval.

The finite-support classification of $\delta_0=A^*-1$ and the exact
identity $(q-p)\circ F_\kappa=q$ are proved in the two earlier local
torus records. No previous seven-dimensional rank computation or
third-order example is needed for this argument.

## Proof

### Step 1. Periodic detection at the linear parameter

Let $g\in\mathcal T$ have zero sums on every periodic orbit of $A$.
The additive Livšic theorem gives a continuous complex-valued $u$ with
$$
g=u\circ A-u.
\tag{4}
$$
Here the base is a smooth transitive Anosov diffeomorphism of a compact
manifold, and $g$ is Hölder. The complex additive group is $\mathbb R^2$
with its translation-invariant metric, so no noncommutative localization
restriction is needed. One precise primary-source version is de la
Llave--Windsor, Theorem 3.1 and Remark 3.2; its hypothesis and conclusion
were directly checked in the [authors' paper](https://arxiv.org/pdf/0711.3229).
For additive cocycles their comparison maps are translations and have
derivative norm one. Choose $1<\rho<\lambda^{-\alpha}$ in their notation.

For completeness, the required transitivity of this particular $A$ is
also elementary: $A$ preserves Haar measure, and a square-integrable
invariant function has constant Fourier coefficients along every
$A$-frequency orbit. All nonzero such orbits are infinite, so square
summability makes those coefficients zero. The resulting ergodicity and
full support of Haar measure imply that almost every point has a dense
forward orbit, by applying the ergodic theorem to a countable open basis.

Let $c_k=\widehat u(k)$. Fix $m\ne0$, and on its frequency orbit put
$a_j=\widehat g(A^jm)$, $b_j=c_{A^jm}$. Taking Fourier coefficients in
(4) gives
$$
a_j=b_{j-1}-b_j.
\tag{5}
$$
The eigenvalues of $A$ are $(3\pm\sqrt5)/2$. Its eigendirections have
irrational slope, and therefore a nonzero integer vector has nonzero
components in both eigendirections. It follows that $|A^jm|\to\infty$
as $j\to+\infty$ and as $j\to-\infty$. The Riemann--Lebesgue lemma,
applicable since $u$ is continuous on a compact torus, gives $b_j\to0$
at both ends. Because $(a_j)$ has finite support, telescoping (5) yields
$$
\sum_{j\in\mathbb Z}a_j=0.
\tag{6}
$$
The constant Fourier coefficient of $g$ is zero by integrating (4).
On each nonzero orbit define $d_j=\sum_{k>j}a_k$. Equation (6) ensures
that $(d_j)$ has finite support, and $d_{j-1}-d_j=a_j$. Only finitely
many orbits meet the support of $g$. Summing their finite primitives
constructs $h\in\mathcal T$ with $g=\delta_0h$.

Conversely, a finite primitive gives zero periodic sums by telescoping.
The kernel of $\delta_0$ on $\mathcal T$ is the constants: coefficients
of an invariant finite Fourier polynomial are constant on infinite
nonzero frequency orbits and hence vanish. A primitive is therefore
unique after setting its constant coefficient to zero.

### Step 2. Induction proving the formal interface

Suppose all (3) vanish. Set $R^{(0)}=G$. Its constant parameter
coefficient $R^{(0)}_0$ has zero sums on all $A$-periodic orbits, so Step 1
gives a zero-mean $H_0\in\mathcal T$ with $\delta_0H_0=R^{(0)}_0$.
The series
$$
R^{(1)}=\frac{R^{(0)}-\delta_tH_0}{t}
\tag{7}
$$
belongs to $\mathcal T[[t]]$. Each $\mathscr L_{n,x_0}(\delta_tH_0)$
is identically zero: the orbit sum is
$H_0(F_{t/\pi}^{\,n}x_{n,x_0}(t))-H_0(x_{n,x_0}(t))=0$.
Linearity of (3) and absence of $t$-torsion in $\mathbb C[[t]]$ show
that all formal periodic conditions also vanish for $R^{(1)}$.

Inductively, given $R^{(k)}$ with these properties, apply Step 1 to its
constant coefficient and obtain a zero-mean finite $H_k$. Set
$$
R^{(k+1)}=t^{-1}(R^{(k)}-\delta_tH_k).
\tag{8}
$$
The same reasoning proves that (8) is defined and retains every formal
periodic condition. For each $N\geq0$ the construction gives
$$
G-\delta_t\left(\sum_{k=0}^{N}t^kH_k\right)
=t^{N+1}R^{(N+1)}.
\tag{9}
$$
Passing coefficientwise through (9) proves $G=\delta_tH$ for
$H=\sum_{k\geq0}t^kH_k\in\mathcal T[[t]]$.

For the converse, apply the finite-order version of telescoping to each
truncation of $H$. Formula (1) ensures the omitted tail has order at
least $N+1$, so each coefficient of the formal orbit sum is zero.
Finally, if $\delta_tK=0$, its order-zero coefficient is constant by
Step 1. Subtract that constant and divide by $t$. Repetition proves that
all coefficients of $K$ are constants. This proves Theorem 1. $\square$

### Step 3. The finite-dimensional formal kernel under FR(V)

All periodic rows annihilate $B_V$ identically, since for every real
parameter and every one-variable finite $f$,
$$
\delta_t[f(q-p)]=f(q)-f(q-p).
\tag{10}
$$
The same identity holds formally. By Theorem 1, the common kernel of
the rows (3) on $V[[t]]$ is precisely the formal data in this space with
a primitive in $\mathcal T[[t]]$. Under $\mathrm{FR}(V)$ it equals
$B_V[[t]]$, including the reverse containment supplied by (10).

Let $W$ be any fixed complex vector-space complement of $B_V$ in $V$,
and put $r=\dim W$. Over the field $K=\mathbb C((t))$, the common
kernel of the same rows restricted to $W\otimes K$ is zero. Indeed,
multiplying any putative kernel vector by a sufficiently large power
of $t$ puts it in $W[[t]]$, where the preceding kernel statement applies.

In an $r$-dimensional vector space over a field, linear functionals with
zero common kernel span the full dual: otherwise the annihilator of
their span would have positive dimension. Hence $r$ of the periodic
rows form a basis of that dual and have nonzero determinant in $K$.
Their entries are convergent germs at $t=0$, so their determinant is
a nonzero convergent germ, not merely a nonzero formal expression.
For $r=0$ take the empty set of rows and $D_V=1$.

### Step 4. Real continuation and the conditional generic conclusion

For a fixed $n$, consider
$$
Z_n=\{(\kappa,x)\in I\times\mathbb T^2:F_\kappa^n x=x\}.
$$
At every point of $Z_n$, the derivative $D_xF_\kappa^n-I$ is invertible:
at an Anosov periodic point, stable multipliers have modulus less than
one and unstable multipliers have modulus greater than one. Thus the
analytic implicit function theorem makes projection $Z_n\to I$ a
local analytic isomorphism. Over any compact subinterval of $I$, $Z_n$
is closed in that subinterval times the compact torus, hence compact.
This proper local isomorphism is a finite covering. Since $I$ is an
interval, its branches extend uniquely throughout $I$, and all points
in each fiber are continuations of points at $\kappa=0$.

The finitely many rows selected in Step 3 consequently have real
analytic entries on the same $I$ after restoring $t=\pi\kappa$. Let
$D_V(\kappa)$ be their determinant in the chosen basis of $W$.
It has a nonzero germ at zero, so is not identically zero on connected
$I$. Its real zero set is discrete: an accumulation in $I$ would make
both real and imaginary analytic parts vanish identically. It follows
that outside this discrete set the selected rows have zero kernel on
$W$, and their kernel in $V$ is exactly $B_V$.

Zero sums on all periodic orbits imply zero sums on the selected ones.
Conversely, every element of $B_V$ has zero sums on all periodic orbits
by (10). This proves the first conclusion of Theorem 2.

There are countably many finite subsets of $\mathbb Z^2$. If
$\mathrm{FR}(V)$ holds for all their Fourier spans, take the union of
their discrete exceptional zero sets. Each such set is countable, so
their union $E$ is countable, has Lebesgue measure zero and is meagre.
Its complement is residual and of full measure. Every finite Fourier
polynomial lies in one of the listed spans, which proves the
simultaneous conditional conclusion. $\square$

## Corrections or missing assumptions

The crucial new scientific obligation is still $\mathrm{FR}(V)$, not
the finite-dimensional analytic rank deduction. No claim in this file
proves that obligation. Theorem 1 makes the formal algebraic obstruction
and all formal periodic conditions equivalent; it does not force their
common kernel to equal $\mathcal B[[t]]$ in fixed target support.

No analytic dependence or convergence of the primitive has been inferred
from scalar Livšic existence. That theorem is used only at $t=0$, once
per induction step. It also does not supply finite Fourier support in a
nonlinear system; the finite-support conclusion in Step 1 uses the
special linear frequency permutation of $A$.

## Open risks and contribution boundary

- The exceptional set in the conditional simultaneous statement may be
  dense. No common punctured neighborhood valid for all supports follows.
- Even for a fixed support, this file does not show $D_V\ne0$ without
  $\mathrm{FR}(V)$. A finite list of successful low-order tests cannot
  replace that hypothesis.
- Period-dependent complex radii of analyticity are harmless here:
  only finitely many germs form a selected determinant, and the global
  continuation used is real on the assumed common Anosov interval.
- Theorem 1 does not need nonzero parameters to be Anosov; its local
  branch construction only uses the invertibility at the linear base.
  The common-interval hypothesis belongs to Theorem 2 alone.
- Livšic existence, the linear Fourier orbit calculation, analytic
  continuation, finite-dimensional row selection and countable generic
  exclusion are prior/basic mechanisms, not a collection of new main
  contributions. No independent-paper capacity is claimed for them.

## Verification and inputs

The main agent fully read the proof-writer skill and both predecessor
torus proof records before writing this new file. The skill requires
retaining the original OPEN claim and labeling the conditional result.
The research-lit/novelty-check workflow is being used for a separate
bounded all-support prior report; it does not grant novelty here.
No configured GPT-5.4 Codex MCP reviewer is available; no such review
or cross-model verification has been asserted.

Direct source verification for the sole external existence theorem:
Rafael de la Llave and Alistair Windsor, *Livšic Theorems for
Non-Commutative Groups including Diffeomorphism Groups and Results on
the Existence of Conformal Structures for Anosov Systems*,
[arXiv:0711.3229v2](https://arxiv.org/abs/0711.3229), Theorem 3.1,
Remark 3.2 and §4.2.3. The original additive theory is credited there
to Livšic. The present use is the complex additive specialization only.

Verification in this author file consists of the exact frequency
recurrence, two-sided coefficient decay, finite telescoping primitive,
coefficientwise induction, Laurent-field denominator clearing, finite
row selection and real-analytic continuation. No numerical experiments,
old-file edits, manuscript drafting or external writes were performed.
Independent mathematical review of this new interface is still pending.
