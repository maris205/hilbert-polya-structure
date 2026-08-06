# Derivation package: exact Hénon pinning and the C02D obstruction

Date: 2026-08-06  
Status: **frozen before computation**

## 1. Target

Determine whether the C02C length-\(N\) endpoint solvers naturally produce a
same-one-step-clock finite-memory approximation to a graph-directed
holomorphic operator whose ordinary traces equal

\[
T_n=\sum_{x\in\operatorname{Fix}(H_6^n)\cap\Lambda_*}
\frac1{\det(I-DH_6^n(x))}.
\]

The target is the exact implication required by the C02D pre-registration,
not a numerical spectral resemblance.

## 2. Status ledger

| Statement | Status |
|---|---|
| Four-state local survivor and C02C \(X\)-disk endpoint theorem | inherited `PROVED` |
| Mixed \(Y\times X\) one-step pinning-domain lemma below | `PROVED` and exactly checked |
| C02C windows equal iterated word-pinning data | `PROVED` on the common domain |
| Those windows are a C02D same-clock approximation | `REFUTED` under the frozen standard-kernel semantics |
| Raw BPS-kernel trace sign | `PROVED` under the stated contour/residual convention |
| Orbitwise repair by an ordinary scalar multiplicative edge cocycle | `REFUTED` by repetition |
| Repair by odd supertrace or reciprocal determinant | `PROVED` algebraically; classical prior art |
| New entire Fredholm determinant with the desired signed trace | `OPEN`; not supplied here |
| Alternative history-space or lifted construction | `OPEN`; outside this candidate |
| Hilbert--Pólya/arithmetic correspondence | `NOT_TESTABLE` |

## 3. Invariant object

Use the coordinate swap

\[
S(q,p)=(p,q),\qquad
F=SH_6S^{-1},\qquad
F(x,y)=(y,1-6y^2-x).
\]

A state is \(i=(s,t)=(\varepsilon_i,\varepsilon_{i-1})\) in the fixed order

\[
(--),\quad(-+),\quad(+-),\quad(++).
\]

There is an edge

\[
(s,t)\longrightarrow(r,s)
\quad\Longleftrightarrow\quad
\neg(t=r=+).
\]

Thus the six edges are

\[
--\to--,\quad --\to+-,\quad -+\to--,
\quad +-\to-+,\quad +-\to++,\quad ++\to-+.
\]

This retains chronological two-coordinate matching. No averaged transition
matrix is introduced.

## 4. Assumptions and source boundary

1. The frozen map parameter is \(a=6\); it was not selected from arithmetic
   or spectral target data.
2. Only the certified local survivor \(\Lambda_*\) is in scope.
3. The natural source object is the pure-hyperbolic BPS mixed
   exterior/interior Banach Cauchy kernel, not an assumed Hardy/Bergman
   composition operator.
4. BPS qualitative pinning, kernel composition, nuclearity, and trace theory
   are prior art. The project claims only the explicit \(H_6\) domain lemma,
   the exact semantic identification, and the scoped obstructions.
5. Rugh 1992 was not available for a direct page-by-page full-text audit in
   this environment. BPS's reconstruction and attribution were checked, as
   were other accessible primary sources. This unresolved source gate only
   weakens novelty claims; it cannot promote them.

## 5. Notation

For \(\sigma\in\{-1,+1\}\), set

\[
X_\sigma=\overline D(\sigma c_X,R_X),\quad
c_X=\frac{23}{48},\quad R_X=\frac7{48},
\]

\[
Y_\sigma=\overline D(\sigma c_Y,R_Y),\quad
c_Y=\frac{121}{256},\quad R_Y=\frac{41}{256}.
\]

For state \(i=(s,t)\), freeze the BPS coordinate domains

\[
D_i^1=Y_t,\qquad D_i^2=X_s.
\]

The first complex variable is the exterior variable and the second is the
interior variable.

## 6. Derivation strategy

The derivation has three independent parts:

1. certify the one-step square-root branches on domains satisfying strict
   BPS source/target inclusion;
2. compare the C02C crossed identity with BPS iterated pinning, keeping the
   dynamical clock explicit;
3. derive the periodic residue sign independently of the special Hénon
   formula, then apply the repetition law to orbitwise scalar edge cocycles.

## 7. Derivation map

\[
\text{rational disks}
\Longrightarrow
\text{holomorphic one-step pinning}
\Longrightarrow
\text{exact BPS kernel}
\Longrightarrow
\begin{cases}
\text{C02C windows}=\text{word data of }\mathcal L^N,\\
\operatorname{tr}K_{\rm raw}^n=-T_n.
\end{cases}
\]

The first branch triggers the approximation-semantics kill condition; the
second triggers the orbitwise scalar-sign kill condition.

## 8. Main derivation

### Lemma 1: strict coordinate nesting

For either sign,

\[
|c_X-c_Y|+R_X
=\frac5{768}+\frac{112}{768}
=\frac{39}{256}<\frac{41}{256}=R_Y.
\]

Hence \(X_\sigma\Subset Y_\sigma\), with exact boundary margin

\[
R_Y-(|c_X-c_Y|+R_X)=\frac1{128}.
\]

The ratio \(39/41\) is only a local geometric enclosure ratio. It is not an
operator-norm or aggregate nuclearity estimate.

### Lemma 2: exact one-step pinning domain

On an edge \((s,t)\to(r,s)\), fixing \(w\in Y_t\) and \(z\in X_r\) gives

\[
P_s(w,z)=s\sqrt{\frac{1-w-z}{6}},
\qquad
F(w,P_s(w,z))=(P_s(w,z),z).
\]

The radicand lies in one of the three allowed disks

\[
\overline D\!\left(\frac{763}{4608},\frac{235}{4608}\right),
\quad
\overline D\!\left(\frac{773}{4608},\frac{235}{4608}\right),
\quad
\overline D\!\left(\frac{1499}{4608},\frac{235}{4608}\right).
\]

The excluded pair \((t,r)=(+,+)\) would give center \(37/4608\) with the
same radius and would cross zero. The allowed disks have minimum modulus

\[
\frac{763-235}{4608}=\frac{11}{96}>0,
\]

so the principal square root and signed branches are holomorphic.

It remains to prove their images do not meet \(\partial X_s\). By symmetry
take \(s=+\), write \(c=23/48\), \(R=7/48\), and let \(a\) be a radicand
center. On \(w=c+Re^{i\theta}\), \(x=\cos\theta\),

\[
|w^2-a|^2=q_0+q_1x+q_2x^2,
\]

where, with \(A=c^2-a\),

\[
q_0=A^2+4c^2R^2+R^4-2AR^2,
\quad q_1=4cR(A+R^2),
\quad q_2=4AR^2.
\]

Exact endpoint/monotonicity checks give the boundary minima

| \(a\) | \(\min_{\partial X_+}|w^2-a|\) | radius | gap |
|---:|---:|---:|---:|
| \(763/4608\) | \(251/4608\) | \(235/4608\) | \(1/288\) |
| \(773/4608\) | \(261/4608\) | \(235/4608\) | \(13/2304\) |
| \(1499/4608\) | \(301/4608\) | \(235/4608\) | \(11/768\) |

Each disk center has its positive square root inside \(X_+\). Connectedness
and the absence of a boundary crossing therefore imply

\[
P_s(Y_t\times X_r)\Subset X_s.
\]

The two target disks are disjoint. The other algebraic root is \(-P_s\) and
lies in \(X_{-s}\), so \(P_s\) is the unique solution in \(X_s\). For fixed
one endpoint, equality of two pinning values can be squared to recover
equality of the other endpoint; hence both one-variable pinning maps are
injective as required by the hyperbolic pinning model. Moreover
\(F^1(Y_t\times X_s)=X_s\Subset Y_s\), which is the complementary strict
first-coordinate inclusion.

For a point \(u=P_s(w,z)\) in the image and \(b\in\partial X_s\), both have
modulus at most \(5/8\). Thus

\[
|b-u|=\frac{|b^2-u^2|}{|b+u|}
\ge \frac{1/288}{5/4}=\frac1{360}.
\]

Finally, since \(P_s^2=(1-w-z)/6\),

\[
|\partial_wP_s|^2=|\partial_zP_s|^2
=\frac1{144|P_s|^2}
\le\frac2{33},
\]

or \(|\partial_wP_s|,|\partial_zP_s|\le2/\sqrt{66}\).

### Lemma 3: the exact mixed Cauchy kernel

For state \(k\), let

\[
\mathcal B_k=A_0\bigl((\widehat{\mathbb C}\setminus D_k^1)
\times D_k^2\bigr)
\]

be the BPS sup-norm Banach space of functions holomorphic in the mixed
domain, continuous on its boundary, and vanishing at
\(\{\infty\}\times D_k^2\). Put \(\mathcal B=\bigoplus_k\mathcal B_k\).
For an edge \(k\to j\), BPS's elementary block is

\[
(\widehat{\mathcal L}_{kj}\psi)(z_1,z_2)
=\frac1{(2\pi i)^2}
\oint_{\partial D_k^1}\oint_{\partial D_k^2}
\frac{s_{kj}\,\partial_2P_s(w_1,z_2)\,\psi(w_1,w_2)}
{(w_2-P_s(w_1,z_2))(z_1-P_s(w_1,z_2))}
\,dw_1\,dw_2,
\]

with the BPS contour orientations and

\[
s_{kj}=\operatorname{sgn}(\partial_2P_s)=-s
\]

on the real branch. This is an exact one-step graph-directed kernel. It has
no infinite-memory coefficient for the C02C window length to truncate.
BPS's formal inverse-composition expression is not substituted for the
kernel, because it need not be defined on the mixed domain.

### Proposition 4: C02C windows change no one-step kernel coefficient

The C02C endpoint solver obeys, after the coordinate swap,

\[
F^N(u,Q_1(u,v))=(Q_N(u,v),v).
\]

Consequently, on the common endpoint domain,

\[
\phi_s^{(N)}=Q_1,\qquad \phi_u^{(N)}=Q_N.
\]

BPS Lemma 3.7 identifies these functions and \(\partial_vQ_1\) as the
iterated pinning data in each chronological word summand of
\(\mathcal L^N\). C02C itself proved these data on \(X\times X\); Lemma 2
above supplies the separate one-step \(Y\times X\) domain repair. This does
not retroactively make C02C a proof of the full mixed-space kernel or its
nuclearity.

There are two standard window interpretations:

- treat an \(N\)-step crossed map as one branch, which gives the time iterate
  \(\mathcal L^N\) and changes the clock;
- retain one-step time using history states, which gives an exact higher-block
  recoding/intertwining rather than an approximation converging to
  \(\mathcal L\).

Both are explicitly excluded by the frozen C02D definition of
\(\mathcal L^{[N]}\). This proves the first scoped `NO_GO`. It does not rule
out inventing a different lifted/history operator, which would be a new
candidate requiring a new source lock and pre-registration.

### Proposition 5: raw residue and the constant negative sign

At a periodic pinning fixed point write

\[
a=\partial_1\phi_u,\quad b=\partial_2\phi_u,
\quad c=\partial_1\phi_s,\quad d=\partial_2\phi_s.
\]

Differentiating
\(F(w_1,\phi_s(w_1,z_2))=(\phi_u(w_1,z_2),z_2)\) gives

\[
M=DF^n=
\begin{pmatrix}
a-bc/d & b/d\\
-c/d & 1/d
\end{pmatrix}.
\]

For the matching residual

\[
R=(w_1-\phi_u,\ w_2-\phi_s),
\]

direct expansion gives

\[
\det DR=(1-a)(1-d)-bc=-d\det(I-M).
\]

Deleting the BPS orientation sign leaves Cauchy numerator \(d\), hence, with
these fixed contour/residual conventions,

\[
\frac{d}{\det DR}=-\frac1{\det(I-M)}.
\]

Restoring \(s_d=\operatorname{sgn}d\) gives

\[
\frac{s_dd}{\det DR}=\frac1{|\det(I-M)|}
\]

for the real saddle branches, using the inherited orientation identity
\(\operatorname{sgn}\det(I-M)=-s_d\). Therefore

\[
\operatorname{tr}K_{\rm raw}^n=-T_n.
\]

The leading minus is convention-sensitive across different holomorphic
operator representations, so this proposition is scoped to the frozen BPS
pinning kernel. General signed fixed-point trace formulas are classical and
are part of the prior-art boundary, not contradicted here.

### Theorem 6: orbitwise scalar repetition obstruction

Suppose a one-step scalar multiplicative cocycle is intended to turn each raw
periodic-orbit residue into the desired signed residue. On a primitive cycle
\(\gamma\), its correction must be
\(c_\gamma=-1\). On the double repetition, multiplicativity forces

\[
c_{\gamma^2}=c_\gamma^2=+1,
\]

whereas the orbitwise required correction remains \(-1\). Contradiction.
This proves the second scoped `NO_GO` for an orbitwise scalar repair. By
itself, the argument does not exclude an accidental equality of aggregate
trace sums through cancellations between different periodic orbits; no such
aggregate-only repair is frozen or claimed here.

Algebraically honest alternatives are

\[
\operatorname{Tr}_{\rm signed}:=-\operatorname{tr},
\]

a pure-odd supertrace, or

\[
d_{\rm signed}(z)
=\exp\!\left(-\sum_{n\ge1}\frac{z^n}{n}T_n\right)
=\det(I-zK_{\rm raw})^{-1}.
\]

The last identity holds where the Fredholm determinant is nonzero and gives
a generally meromorphic reciprocal. Graded and alternating Fredholm
determinants are classical; this is not a new entire determinant theorem.

## 9. Independent checks

The producer and checker separately verify:

1. all six chronological edges and the single forbidden sign pair;
2. all rational radicand centers and the common radius;
3. strict \(X\Subset Y\) nesting;
4. the quadratic boundary minima and the \(1/360\) image clearance;
5. the exact derivative inequality;
6. the residual/monodromy determinant identity on a deterministic rational
   test basis;
7. the primitive/double-repeat orbitwise scalar contradiction;
8. certificate completeness and SHA-256 integrity.

The scripts intentionally compute no eigenvalues and consume no arithmetic or
Riemann-zero data.

## 10. Consequences and boundaries

- C02D, as pre-registered, is mechanically `NO_GO` before spectrum
  computation.
- A finite-rank Laurent--Taylor or Chebyshev projection of the exact one-step
  kernel would preserve the clock. Its index would be analytic mode degree,
  not memory length.
- Such a reframe requires new boundedness, common-space factorization, trace
  identity, and aggregate error proofs. General holomorphic approximation
  results create a strong prior-art ceiling, so a routine \(H_6\) substitution
  does not meet the manuscript promotion rule.
- The constants \(39/41\), \(1/360\), and local derivative bounds must not be
  advertised as a global trace-norm rate.
- No arithmetic primitive-orbit law, completed zeta, functional equation,
  Riemann--von Mangoldt law, self-adjoint operator, or RH implication follows.
