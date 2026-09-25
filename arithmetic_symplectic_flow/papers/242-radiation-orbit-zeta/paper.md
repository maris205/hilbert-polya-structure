# The physical clock offset, a branched orbit zeta, and the full-field return boundary

**Paper ID:** `242-radiation-orbit-zeta`  
**Audit ID:** `ANG-AUDIT-20260918-DRZ01`  
**Underlying candidate:** `ANG-20260918-DRB01`.  
**Date:** 2026-09-18.  
**Status:** `ORDINARY ZETA ESTABLISHED; MEROMORPHIC/FREDHOLM PROMOTION STOP`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.  
**Written technical review:** Completed; see the [internal record](evidence/review.md).

## Abstract

The unchanged full oscillator/field owner of Paper 241 has one primitive
packet per prime, with actual physical period given by its rational-well
integral. This audit refines that period to
\(T_p=C\log p+D+O(p^{-2}\log p)\), where
\(C=2\sqrt2\) and \(D=C(\log4-1)\). Its ordinary unweighted
orbit zeta is holomorphic and nonvanishing for \(\operatorname{Re}s>1/C\).
At the first real convergence boundary it has fractional singular order
\(e/4\), so neither it nor its reciprocal is meromorphic through that
point. The same full-field owner has a continuous local prime section
return whose directional derivative at the closed orbit is the free-field
multiplier, but which is not Fréchet differentiable in the frozen Hilbert
norm. The genuine fixed-time field monodromy has no compactness, and
identity minus that monodromy has dense nonclosed range. These are scoped
obstructions to the proposed standard analytic/return-determinant promotion,
not a refutation of the complete packet theorem or every possible trace
construction. No state, clock, primitive weight or repetition is changed.

## 1. Exact owner, question and nonclaims

The [version-one analytic card](candidate-card.md) was frozen before this
work. Its sole dynamical owner is the complete mild flow on
\(M=\coprod_{n\ge2}\{H_n=1\}\) from
[241](../241-divisor-radiation-bath/paper.md). Its full fields are
\(z_d\in\mathfrak h=L^2((0,\infty),(1+\omega)d\omega;\mathbb C)\),
and its Hamiltonian is

\[
H_n=\frac{v^2}{2}+c_nW(q)
 +\sum_{d=1}^{n-1}\int_0^\infty
 \omega|z_d+\varepsilon_{n,d}q e^{-\omega}|^2d\omega,
\quad c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2}.
\tag{1}
\]

Here v is the momentum called p in 241; p below is reserved for a prime
index. The incidence, all channels, weak symplectic ambient form, actual
time and entire energy surface are unchanged. The lineage remains
proper-divisor symbolic exclusion to reciprocal conservative field
coupling. Static incidence and the designed barrier, energy and field
profile retain their source-naturalness gap.

The precise input is 241's Propositions 1--4: complete mild ownership,
one oriented primitive orbit per prime, no composite or stationary orbit
on M, and every repetition of time \(rT_p\). In particular, no field
space is replaced by the set of periodic centres. Its exact period is

\[
T_n=4\int_0^{A_n}\frac{dq}{\sqrt{2(1-c_nW(q))}},\qquad
A_n=\sqrt{c_n}-\sqrt{c_n-1}.
\tag{2}
\]

For composite n this remains a scalar comparison integral, not a full
closed-orbit period. The frozen analytic object is only

\[
L(s)=\sum_p\sum_{r\ge1}\frac{e^{-srT_p}}r,
\qquad Z(s)=e^{L(s)}.
\tag{3}
\]

| Item | Exact same-object relation | Boundary |
| --- | --- | --- |
| Full action and packets | Unchanged 241 theorem input | No new dynamics or retrospective re-scoring |
| Time | Integral (2), original units | Neither C nor the offset is removed |
| Orbit weights | One primitive weight and physical r-fold repeats | No stability, prime-power or compensating weight inserted |
| Z | Ordinary full-orbit product justified below | Not initially an operator determinant |
| Section | Actual prime-component hits of q=0, v>0, H=1 | All field coordinates retained; not the whole energy flow |
| Field multiplier | Actual fixed-time field action on the same Hilbert space | Its relation to a section derivative must be checked |
| Classical ASFS / Route B | Not constructed or evaluated | Classical A0--A2 NOT APPLICABLE; B NOT INVOKED |

The questions concern convergence, the first real singularity and the
standard return/determinant compatibility of this object. There is no
target-zero matching, quantum spectrum, universal no-trace theorem,
natural-boundary claim or proof of radiation decay.

## 2. A physical-time offset with a summable error

### Proposition 1. Two-term period refinement

Put \(C=2\sqrt2\) and \(D=C(\log4-1)>0\). For every integer
\(n\ge2\), the scalar integral (2) satisfies

\[
T_n=C\log n+D+R_n,\qquad
|R_n|\le\frac{C}{n^2}\left(\frac52\log n+14\right).
\tag{4}
\]

For prime n this is its actual full-state period; nothing is asserted
about a nonexistent composite packet.

**Proof.** Write \(c=1+n^{-2}\),
\(\delta=\sqrt{(c-1)/c}=(n^2+1)^{-1/2}\), and

\[
a(y)=\frac1{(1+y)\sqrt{1-y^2}},\qquad
I(\delta)=\int_\delta^1\frac{a(y)}{\sqrt{y^2-\delta^2}}\,dy.
\]

The exact change \(y=(1-q^2)/(1+q^2)\) in (2) gives
\(T_n=C I(\delta)/\sqrt c\). We retain the linear term of a,
not only its value at zero. Let

\[
h(y)=a(y)-1+y
=\frac{(1-y^2)^{-1/2}-(1-y^2)}{1+y}.
\tag{5}
\]

Then \(0\le h(y)\le2y^2\) on \([0,1/2]\), and
\(0\le h(y)\le a(y)\) on \([1/2,1)\). For the first bound,
the derivative of \((1-t)^{-1/2}\) on \(0\le t\le1/4\)
is at most \(1/(2(3/4)^{3/2})<1\); use \(t=y^2\).

The finite part can be evaluated without a special-function expansion.
With \(q_\epsilon=\sqrt{(1-\epsilon)/(1+\epsilon)}\), direct
substitution gives

\[
\int_\epsilon^1\frac{a(y)-1}{y}\,dy
=-q_\epsilon+
\log\frac{(1+q_\epsilon)^2}{1+q_\epsilon^2}
\longrightarrow\log2-1.
\tag{6}
\]

Thus \(H_0:=\int_0^1h(y)/y\,dy=\log2\). Integrating the
terms 1 and -y exactly gives

\[
I(\delta)=\operatorname{arcosh}(1/\delta)-\sqrt{1-\delta^2}
 +\int_\delta^1\frac{h(y)}{\sqrt{y^2-\delta^2}}\,dy
=\log(4/\delta)-1+E_\delta.
\tag{7}
\]

Here \(E_\delta=B_\delta+Q_\delta-M_\delta\), with

\[
\begin{aligned}
B_\delta&=\log\frac{1+\sqrt{1-\delta^2}}2+1-\sqrt{1-\delta^2},\\
Q_\delta&=\int_\delta^1h(y)
 \left(\frac1{\sqrt{y^2-\delta^2}}-\frac1y\right)dy,\\
M_\delta&=\int_0^\delta\frac{h(y)}y\,dy.
\end{aligned}
\tag{8}
\]

Both B and M lie in \([0,\delta^2]\): for B set
\(x=1-\sqrt{1-\delta^2}\), so it is \(x+\log(1-x/2)\),
between 0 and \(x\le\delta^2\); for M use (5). In particular
\(|B-M|\le\delta^2\), not twice that bound.

Rationalization gives, for \(y>\delta\),

\[
0\le\frac1{\sqrt{y^2-\delta^2}}-\frac1y
\le\frac{\delta^2}{y^2\sqrt{y^2-\delta^2}}.
\tag{9}
\]

The part of Q up to 1/2 is at most
\(2\delta^2\operatorname{arcosh}(1/(2\delta))
\le2\delta^2\log(1/\delta)\).
On the rest, \(\delta^2\le1/5\) implies
\(\sqrt{y^2-\delta^2}\ge y/\sqrt5\), and
\(\int_{1/2}^1a(y)dy=1/\sqrt3\). Therefore that part is at
most \(8\sqrt{5/3}\,\delta^2\). Since
\(1+8\sqrt{5/3}<12\),

\[
|E_\delta|\le\delta^2\bigl(2\log(1/\delta)+12\bigr).
\tag{10}
\]

Finally let \(u=n^{-2}\), \(b=(1+u)^{-1/2}\),
\(\ell=\log n\) and \(k=\log4-1\). The elementary integral
\(\log2=\int_1^2dx/x\) lies strictly between 1/2 and 1, so
\(0<k<1\). Equations (7)--(10) give exactly

\[
T_n/C=b\bigl(\ell+k+\tfrac12\log(1+u)+E_\delta\bigr).
\]

Use \(1-b\le u/2\), \(\log(1+u)\le u\),
\(\delta^2\le u\) and \(u\le1/4\). The difference from
\(\ell+k\) is at most
\(u(\tfrac52\ell+53/4)\), which proves (4). ∎

The derived positive D is part of the physical period, not a constant
that may be discarded when defining the analytic owner.

## 3. Owned ordinary product and its exact convergence boundary

### Proposition 2. Product, repetitions and logarithmic derivative

Let \(s_0=1/C\). Series (3) converges absolutely and locally uniformly
exactly for \(\operatorname{Re}s>s_0\). In that half-plane,

\[
Z(s)=\prod_p(1-e^{-sT_p})^{-1}
\quad\hbox{is holomorphic and nonzero},\qquad
-\frac{Z'(s)}{Z(s)}=\sum_p\frac{T_p}{e^{sT_p}-1}.
\tag{11}
\]

Every bounded physical-time window contains finitely many primitive
packets and finitely many repetitions. No operator trace is asserted.

**Proof.** The periods are positive and tend to infinity by (4), so
\(t_*:=\inf_pT_p>0\). Also \(|T_p-C\log p|\le B\) for
one finite B. For \(\sigma=\operatorname{Re}s>0\),

\[
\sum_{r\ge1}\frac{e^{-\sigma rT_p}}r
\le\frac{e^{-\sigma T_p}}{1-e^{-\sigma t_*}}.
\tag{12}
\]

When \(C\sigma>1\), comparison with the all-integer series
\(\sum_{n\ge2}n^{-C\sigma}\) proves convergence, uniformly
on compact subsets. The geometric logarithm proves the product identity.
The same estimates with a \(T_p=O(\log p)\) factor justify
differentiation and summation of repetitions, giving (11).

For \(0<\sigma\le s_0\), the r=1 sum dominates a positive
constant times \(\sum_p p^{-C\sigma}\ge\sum_p1/p\).
The last sum diverges: otherwise the finite products
\(\prod_{p\le N}(1-1/p)^{-1}\) would be uniformly bounded,
using \(-\log(1-1/p)\le2/p\); their geometric expansions and
unique factorization instead dominate \(\sum_{m\le N}1/m\).
For \(\sigma\le0\), even a single prime's repetition sum
fails absolute convergence. These claims concern absolute convergence,
not conditional convergence on every boundary point.

If \(T_p\le R\), then \(p\le\exp((R+B)/C)\); if
\(rT_p\le R\), also \(r\le R/t_*\). This proves local
finiteness. ∎

The coefficient \(T_p\) in (11) is obtained by differentiating this
owned repetition series. It is not an inserted von Mangoldt weight and
is not identified with \(\log p\).

## 4. The first real singularity is not meromorphic

### Lemma 3. Elementary comparison functions near one

For \(\operatorname{Re}w>1\) put
\(P(w)=\sum_p p^{-w}\), and define

\[
Q(w)=\sum_p\sum_{r\ge2}\frac{p^{-rw}}r.
\tag{13}
\]

Q is holomorphic for \(\operatorname{Re}w>1/2\), by normal
convergence. Near \(w=1\), on a sufficiently small slit disk,

\[
P(w)=-\operatorname{Log}(w-1)+B_0(w),
\tag{14}
\]

where \(B_0\) is holomorphic on the whole disk. This is continuation
of P from its right half-plane, not convergence of its original series
through that disk.

**Proof.** Unique factorization and absolute convergence give
\(\log\zeta(w)=P(w)+Q(w)\) for \(\operatorname{Re}w>1\),
with \(\zeta(w)=\sum_{m\ge1}m^{-w}\). One needs only its
elementary local pole, which can be derived here. For
\(\operatorname{Re}w>1\), integrating the counting function yields

\[
\zeta(w)=w\int_1^\infty\lfloor x\rfloor x^{-w-1}dx
=\frac{w}{w-1}-w\int_1^\infty\{x\}x^{-w-1}dx.
\tag{15}
\]

The last integral converges normally for \(\operatorname{Re}w>0\).
Thus \(J(w)=(w-1)\zeta(w)\) is holomorphic near one with
\(J(1)=1\). Shrink the disk so J is nonzero, choose its holomorphic
logarithm equal to zero at one, and set \(B_0=\log J-Q\).
Equation (14) follows on the right portion and defines the slit
continuation. ∎

The Dirichlet series, formula (15) and Euler product agree with the
standard references in [NIST DLMF, §25.2](https://dlmf.nist.gov/25.2),
specifically 25.2.1, 25.2.8 with N=1, and 25.2.11. These are calculation
background only: this argument does not import the Riemann zeta function
as the physical flow's operator or determinant, and uses no zero data.

### Proposition 4. Slit continuation and fractional boundary order

There is a disk about \(s_0=1/C\) and a holomorphic nonvanishing
function A on that whole disk such that, on its slit version reached
from \(\operatorname{Re}s>s_0\),

\[
Z(s)=A(s)\exp\bigl[-\alpha(s)\operatorname{Log}(Cs-1)\bigr],
\qquad \alpha(s)=e^{-Ds}.
\tag{16}
\]

Moreover \(A(s_0)>0\) and \(\alpha(s_0)=e/4\in(0,1)\).
Consequently, for real \(x\downarrow0\),

\[
Z(s_0+x)=A(s_0)(Cx)^{-e/4}
\bigl(1+O(x|\log x|)\bigr).
\tag{17}
\]

Neither Z nor its reciprocal has a meromorphic germ through \(s_0\).

**Proof.** The actual r=1 correction is

\[
E(s)=\sum_p\left[e^{-sT_p}-e^{-Ds}p^{-Cs}\right]
=\sum_p e^{-Ds}p^{-Cs}(e^{-sR_p}-1).
\tag{18}
\]

On every compact subset of \(\operatorname{Re}s>-1/C\), (4)
bounds its terms by a constant times
\((\log p)p^{-2-C\operatorname{Re}s}\). Hence E is normally
convergent and holomorphic there. The actual repetitions

\[
F(s)=\sum_p\sum_{r\ge2}\frac{e^{-srT_p}}r
\tag{19}
\]

converge normally for \(\operatorname{Re}s>1/(2C)\), using
\(t_*>0\) and the uniform \(T_p=C\log p+O(1)\). Thus

\[
L(s)=\alpha(s)P(Cs)+E(s)+F(s)
\tag{20}
\]

on its original half-plane. Apply (14) in a small disk about \(s_0\)
lying inside \(\operatorname{Re}s>1/(2C)\), and put

\[
G(s)=\alpha(s)B_0(Cs)+E(s)+F(s),\qquad A(s)=e^{G(s)}.
\]

All terms of G are holomorphic on the whole disk; along its real
portion they are real, so \(A(s_0)>0\). This proves (16).
Also
\(\alpha(s_0)=\exp[-(\log4-1)]=e/4\), strictly between zero
and one by \(\log4>1\). Since
\(\alpha(s_0+x)-\alpha(s_0)=O(x)\), (17) follows.

A nonzero meromorphic germ is an integer power of \(s-s_0\) times
a nonvanishing holomorphic germ. Its real logarithmic growth therefore
has integer order. Equation (17) has noninteger order \(-e/4\),
and the reciprocal has order \(e/4\). Neither is meromorphic. ∎

The variable exponent in (16) must not be replaced by a constant in an
identity; the constant exponent is the leading real asymptotic only.
For example, (16) also yields
\(-Z'/Z(s_0+x)=(e/4)/x+O(|\log x|)\). This is not a natural-
boundary theorem or a classification of other complex singularities.

Any identity through this point with a holomorphic determinant, its
meromorphic reciprocal, or a meromorphic quotient of holomorphic
determinants is therefore excluded. This includes a proposed ordinary
holomorphic trace-class Fredholm determinant identity on a neighborhood
of \(s_0\), and remains so after multiplication by a nonvanishing
holomorphic factor. It does not exclude a determinant identity confined
to \(\operatorname{Re}s>s_0\); no physical operator giving one is
supplied here. Weighted, relative or regularized objects are different
contracts, not outcomes disproved by (17).

## 5. The complete prime section return is continuous but not Fréchet differentiable

Fix a prime label \(\ell\). Write
\(\mathcal H_\ell=\mathfrak h^{\ell-1}\) and
\(Q(z)=\sum_d\int_0^\infty\omega|z_d|^2d\omega\).
All incidences vanish, but no field channel is removed.
Differentiability below is on the underlying real Hilbert space, as for
the Hamiltonian equations; no holomorphic state-map derivative is assumed.

### Proposition 5. Actual return and failure of uniform differentiation

The section \(q=0,v>0,H_\ell=1\) is parametrized by

\[
z\in\mathcal D_\ell:=\{Q(z)<1\},\qquad
(q,v,z)=(0,\sqrt{2(1-Q(z))},z).
\tag{21}
\]

Let \(\tau_\ell(E)\) be the least inner scalar period at energy
\(0<E<c_\ell\), with the same oscillator and time as (1).
The actual first return and roof on this entire section are

\[
\mathcal R_\ell(z)=U_{\tau_\ell(1-Q(z))}z,\qquad
\tau(z)=\tau_\ell(1-Q(z)),\qquad U_tz=e^{-i\omega t}z
\tag{22}
\]

in every channel. The return is a homeomorphism. At zero it has bounded
directional derivative \(U_{T_\ell}\), but is not Fréchet differentiable
in the frozen \(\mathcal H_\ell\) norm.

**Proof.** Q is a continuous quadratic form with \(Q(z)\le\|z\|^2\).
At a point of (21), the oscillator energy is \(1-Q(z)\in(0,1]\),
strictly below \(c_\ell>1\), and the initial positive crossing lies
on its inner oval. Fields evolve freely and preserve Q. This gives its
actual first positive crossing time and the endpoint (22). The roof is
continuous, and joint strong continuity of \((t,z)\mapsto U_tz\)
makes the return continuous. Its inverse uses the negative of the same
roof, because Q is preserved. No claim that this section covers all M
is needed or made; the full periodic classification comes from 241.

The scalar period is smooth and strictly increasing for \(0<E<c_\ell\).
To see this without an implicit differentiability assumption on fields,
set \(u=2q/(1+q^2)\) in the inner well. Its inverse has derivative

\[
k(u)=\frac{dq}{du}
=\frac1{\sqrt{1-u^2}(1+\sqrt{1-u^2})},
\quad
\tau_\ell(E)=\frac4{\sqrt{2c_\ell}}
\int_0^{\pi/2}k\left(\sqrt{E/c_\ell}\sin\theta\right)d\theta.
\tag{23}
\]

On a compact energy interval within \((0,c_\ell)\), all derivatives
are dominated. The derivative of k is strictly positive for \(u>0\),
so \(a_\ell:=\tau_\ell'(1)>0\).

For a fixed direction v and real t tending to zero, (22) gives
\(\mathcal R_\ell(tv)/t
=U_{\tau_\ell(1-t^2Q(v))}v\to U_{T_\ell}v\).
Any Fréchet derivative would therefore have to be \(U_{T_\ell}\).
This directional limit is not uniform in the unit direction.

Indeed choose a unit vector \(v_N\) supported in one retained channel
on \([N,N+1]\), constant there relative to the weighted measure
\(d\mu=(1+\omega)d\omega\). Then
\(m_N=Q(v_N)=(N+1/2)/(N+3/2)\to1\).
Put

\[
r_N^2=\frac{\pi}{a_\ell N},\qquad z_N=r_Nv_N,
\qquad \Delta_N=\tau_\ell(1-r_N^2m_N)-T_\ell.
\tag{24}
\]

For large N these are points of the full section tending to zero, and
smoothness in (23) implies \(N\Delta_N\to-\pi\). Uniformly
on their support, \(e^{-i\omega\Delta_N}\to-1\). Thus

\[
\frac{\|\mathcal R_\ell(z_N)-U_{T_\ell}z_N\|}{\|z_N\|}
=\|(U_{\Delta_N}-I)v_N\|\longrightarrow2,
\tag{25}
\]

contradicting Fréchet differentiability. Each probe even has bounded
frequency support; the obstruction is lack of uniformity in the frozen
Hilbert norm, not merely existence of rough individual fields. ∎

The positive continuous physical return survives. What fails is its
promotion to an ordinary C1 Hilbert Poincaré map in this norm. Replacing
the carrier by a stronger graph-norm domain or a finite frequency model
would require a new explicit contract and cannot repair this audit silently.

## 6. Fixed-time transverse monodromy and the determinant boundary

There is nevertheless a genuine fixed-time tangent object. On a prime
ambient component, \(\Phi^t\) is the product of a smooth scalar flow
with \(U_t\) on fields, and is smooth in initial data for each fixed t.
At the periodic crossing \(x_*=(0,\sqrt2,0)\), the energy tangent
condition is \(\delta v=0\). The flow direction is the nonzero
\(\delta q\) direction. Taking the quotient of that tangent space by
the flow direction identifies the full transverse space with
\(\mathcal H_\ell\); the induced fixed-time map at \(T_\ell\)
is exactly \(U_{T_\ell}\) in each channel. This is not the Fréchet
derivative of (22), which Proposition 5 shows does not exist.

### Proposition 6. Exact operator properties on the retained field space

For every \(T>0\), \(U_T\) is unitary, invertible and Fredholm
of index zero, but not compact or trace class. In contrast,
\(I-U_T\) is injective with dense nonclosed range and is not Fredholm.
It too is noncompact and non-trace-class. The same statements hold on
the finite direct sum of all channels at any prime.

**Proof.** The norm-preserving multiplier has bounded inverse \(U_{-T}\).
It sends an orthonormal sequence to an orthonormal sequence, excluding
compactness and therefore trace class. For
\(b_T(\omega)=1-e^{-i\omega T}\), its zero set on the positive
axis is countable and has weighted measure zero, so multiplication by
\(b_T\) is injective. Its range is dense: for any y, the functions
\(y_k=\mathbf1_{\{|b_T|\ge1/k\}}y\) converge to y and are
images of the Hilbert vectors \(y_k/b_T\).

For nonclosedness fix \(\omega_0=2\pi/T\) and
\(b=\min(\omega_0/2,1/T)\). On the disjoint intervals

\[
J_j=(\omega_0+b2^{-j-1},\omega_0+b2^{-j}),\qquad
e_j=\frac{\mathbf1_{J_j}}{\sqrt{\mu(J_j)}},\quad j\ge1,
\tag{26}
\]

the vectors are orthonormal and
\(\|(I-U_T)e_j\|\le Tb2^{-j}\le2^{-j}\).
The disjointly supported sum \(y=\sum_{j\ge1}(I-U_T)e_j\)
converges and is a limit of range elements. If it were the image of x,
the nonzero multiplier on each \(J_j\) would require
\(x=e_j\) there, forcing \(\|x\|^2\ge\sum_j1=\infty\).
The range is not closed, so the operator is not Fredholm.

Finally, choose a bounded interval away from the multiplier's zeros.
It contains infinitely many disjoint positive-measure subsets on which
\(|b_T|\) is bounded below. Their normalized indicators have
orthogonal images of norm bounded away from zero, excluding compactness
of \(I-U_T\) and therefore its trace class. A single retained
channel supplies all these witnesses in the full direct sum. ∎

Thus the usual expression \(\det_F(I-U_{T_\ell})\) is not
defined by the trace-class Fredholm determinant convention on this
field space. Nor is there a finite-dimensional nondegenerate stability
denominator to import. The statement that \(U_T\) itself is Fredholm
must not be confused with the false claim that \(I-U_T\) is Fredholm.
No renormalized, relative or weighted determinant has been constructed or
excluded in general. These classical operator checks invoke no Route B.

## 7. Controls and what the obstructions do not say

| Control / distinction | Exact consequence |
| --- | --- |
| Ideal comparison times C log p, not installed | The ordinary product would be \(\zeta(Cs)\), with a simple pole; it is a different timing object |
| Keep the actual additive physical offset | Its factor \(e^{-Ds}\) changes the local order to e/4; an O(1) timing error is not analytically innocuous |
| Keep all actual r-fold repetitions | Terms with r at least 2 are analytic near s0, so they do not remove the fractional first-order singularity |
| Different composite label p to a power | No packet is created there; actual repeats remain traversals of the prime orbit |
| Fixed field direction versus moving high frequencies | Directional differentiation exists, but the normalized error in (25) prevents Fréchet differentiation |
| Fixed-time flow versus state-dependent return time | The former supplies a valid tangent field multiplier; the latter lacks the asserted C1 map |
| Full continuous frequency measure | Isolated resonances have measure zero but arbitrarily nearby normalized fields give nonclosed range |
| Finite-mode, stronger-norm, outgoing or weighted replacements | Different analytic/owner contracts; not used to remove any obstruction |
| Independent ordinary product versus physical trace | Equation (3) is owned and valid on its domain; it is not by itself a trace or determinant identity |

The first real branch point does not prove a natural boundary, classify
all complex singularities, or rule out a determinant identity restricted
to the original half-plane. The section obstruction does not undo the
full continuous group action or its exact closed orbits. No theorem about
every possible regularization, observable space or trace framework is
claimed. Source-naturalness remains OPEN independently of these results.

## 8. Gate assessment and decision

| Layer | Exact outcome for this audit |
| --- | --- |
| DRB01 T0/T2 | The full-owner and packet theorems remain unchanged inputs, not erased by an analytic stop |
| T1 | Engineered source/clock evidence retained; naturalness OPEN, no exact log-prime equality |
| Ordinary T3 layer | Established product, exact absolute abscissa, logarithmic derivative and local slit continuation |
| Standard meromorphic promotion | STOP at the noninteger boundary order for Z and its reciprocal |
| Standard full-field return determinant | STOP: return not Fréchet differentiable in the frozen norm; fixed-time field block is not trace class and I minus it is not Fredholm |
| General trace or alternative analytic owner | NOT SUPPLIED / OPEN; no universal exclusion |
| Formal Route coordinates | UNASSIGNED; classical ASFS A0--A2 NOT APPLICABLE |
| Route B | NOT INVOKED |

**Portfolio decision:** advance the exact ordinary analytic record, but
stop the two proposed standard meromorphic/return-determinant promotions
for this unchanged contract. Preserve 241's positive conservative layer.
Any attempt using a new clock, weight, domain, observable representation
or regularized trace must first freeze its own owner/normalization contract;
it is not implicit completion of this paper's missing trace identity.

## Evidence, sources and disclosure

[Frozen audit card](candidate-card.md) · [Claim ledger](claim-ledger.md) ·
[Evidence and review provenance](evidence/README.md) · [Summary](README.md).

The exact mathematical inputs are (1)--(3), the full 241 packet theorem,
and elementary estimates and analytic arguments proved above. The only
external background used is the standard zeta series/pole/Euler-product
comparison, checked against the linked NIST reference; no external object
supplies physical dynamics, periods or a trace. There was no numerical
run, prime cutoff, fitting, PDF/LaTeX output or publication.

This theoretical Markdown record was developed with AI assistance. Clock
and local-return derivations were delegated separately from root's analytic
integration; a separate raw-card checker independently derived the branch
result before seeing a draft and then completed full written readback.
The actual report is linked above. These checks are not external peer review
or cross-family verification. Data availability: all definitions and
proofs are in the linked packages; there are no empirical data. No human
participants or personal data are involved. Human contributions, funding
and conflict-of-interest declarations have not been supplied and are not
inferred; no venue or submission-readiness claim is made.
