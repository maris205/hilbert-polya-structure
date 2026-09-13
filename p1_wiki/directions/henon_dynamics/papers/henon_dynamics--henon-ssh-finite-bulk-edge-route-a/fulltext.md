---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-ssh-finite-bulk-edge-route-a"
canonical_tex: "henon_dynamics/henon_ssh_finite_bulk_edge_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_ssh_finite_bulk_edge_route_a/paper/main.pdf"
source_sha256: "50283eb298a04d040bcfa5849bfdb125b7b4d6a33ff075470a81a479bd94798c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Finite-Size Bulk--Edge and Quench Atlas for the SSH Chain

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_ssh_finite_bulk_edge_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_ssh_finite_bulk_edge_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_ssh_finite_bulk_edge_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_ssh_finite_bulk_edge_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the balanced open Su--Schrieffer--Heeger chain of $M$ cells, we derive the full characteristic polynomial and prove that a strictly hyperbolic edge pair exists if and only if $w/v>(M+1)/M$. We give its exact splitting, two-ended eigenvectors, decay bound, critical linear taper, and fixed-ratio asymptotic. \>0 We then separate this finite threshold from the periodic bulk transition, resolve finite-ring parity and every hopping face, and derive an entire matrix-sinc propagator valid at singular couplings. \>1 An exact mode-quench corollary retains the finite momentum-grid caveat; independent symbolic, numerical, replay, and hostile tests define the claim boundary.
author:
- 'Route-A source-local certificate HCS-C318'
date: 3 September 2026
title: 'An Exact Finite-Size Bulk--Edge and Quench Atlas for the SSH Chain'
```

## Markdown 正文

trailerid \[\<C3182026090300000000000000000000\>\<C3182026090300000000000000000000\>\]

# Finite hyperbolic edge threshold

Let $M\geq2$ and $v,w\geq0$. In the ordered basis $(A_1,\ldots,A_M,B_1,\ldots,B_M)$, the open Hamiltonian is $$\label{eq:block}
 H_O=\begin{pmatrix}0&T\\T^*&0\end{pmatrix},\qquad
 T=vI+wS_-,\qquad (S_-)_{j,j-1}=1.$$ Thus $\Gamma=\operatorname{diag}(I,-I)$ obeys $\Gamma H_O\Gamma=-H_O$.

[\[thm:edge\]]{#thm:edge label="thm:edge"} Put $q_M(y)=\det(yI-TT^*)$. Then $$\label{eq:recurrence}
 q_0=1,\quad q_1=y-v^2,\quad
 q_m=(y-v^2-w^2)q_{m-1}-v^2w^2q_{m-2}.$$ For $v,w>0$, set $x=(E^2-v^2-w^2)/(2vw)$. With $U_m$ the Chebyshev polynomial of the second kind, $$\label{eq:characteristic}
 \det(EI-H_O)=(vw)^M
 \left[U_M(x)+\frac{w}{v}U_{M-1}(x)\right].$$ There is exactly one secular root $x=-\cosh\kappa<-1$, and hence exactly one eigenvalue pair $\pm E_{\rm e}$ outside the trigonometric sector, if and only if $$\label{eq:threshold}
 \frac{w}{v}>\frac{M+1}{M}.$$ For the unique $\kappa>0$ determined by $$\label{eq:kappa}
 \frac{w}{v}=\frac{\sinh((M+1)\kappa)}{\sinh(M\kappa)},$$ the positive energy and one unnormalised positive-energy vector are $$\begin{aligned}
 E_{\rm e}
 &=v\frac{\sinh\kappa}{\sinh(M\kappa)}
 =w\frac{\sinh\kappa}{\sinh((M+1)\kappa)},\label{eq:energy}\\
 a_j&=(-1)^{j-1}\sinh((M+1-j)\kappa),\qquad
 b_j=(-1)^{j-1}\sinh(j\kappa).\label{eq:vectors}\end{aligned}$$ Thus $(a,b)$ has energy $E_{\rm e}$ and $(a,-b)$ has energy $-E_{\rm e}$. The profiles decay strictly inward: $$\label{eq:decay}
 \frac{|a_{j+1}|}{|a_j|}<e^{-\kappa},\qquad
 \frac{|b_j|}{|b_{j+1}|}<e^{-\kappa}\quad(1\leq j<M).$$ At equality in [\[eq:threshold\]](#eq:threshold){reference-type="eqref" reference="eq:threshold"}, $x=-1$ and $E=v/M$. After common division of $a,b$ by $\kappa$ (equivalently, after overall normalisation), the $\kappa\downarrow0$ profiles are $a_j=(-1)^{j-1}(M+1-j)$ and $b_j=(-1)^{j-1}j$.

The leading diagonal entry of $TT^*$ is $v^2$; every subsequent one is $v^2+w^2$, and the off-diagonal entries are $vw$. Its continuant is [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Normalising this recurrence gives [\[eq:characteristic\]](#eq:characteristic){reference-type="eqref" reference="eq:characteristic"}; in particular, the factor $(vw)^M$ cannot be dropped. The $M$ roots are real and simple because $TT^*$ is an irreducible Jacobi matrix. Also $\det T=v^M$, so $E=0$ is impossible when $v>0$.

For $x=-\cosh\kappa$, the identity $U_m(-\cosh\kappa)=(-1)^m\sinh((m+1)\kappa)/\sinh\kappa$ reduces the secular equation to [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}. Its logarithmic derivative is $$(M+1)\coth((M+1)\kappa)-M\coth(M\kappa)>0,$$ because $s\mapsto s\coth(s\kappa)$ is strictly increasing. The ratio therefore rises from $(M+1)/M$ to infinity. No root lies above $x=1$, where both Chebyshev terms are positive, so this proves the iff statement and uniqueness. Direct hyperbolic addition verifies $Tb=E_{\rm e}a$ and $T^*a=E_{\rm e}b$, including both expressions in [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}. Finally, $$\frac{\sinh(n\kappa)}{\sinh((n+1)\kappa)}
 =e^{-\kappa}\frac{1-e^{-2n\kappa}}
 {1-e^{-2(n+1)\kappa}}<e^{-\kappa},$$ which proves [\[eq:decay\]](#eq:decay){reference-type="eqref" reference="eq:decay"}. Taking $\kappa\downarrow0$ gives the threshold energy; applying the common $1/\kappa$ rescaling before that limit gives the nonzero tapers.

[\[cor:splitting\]]{#cor:splitting label="cor:splitting"} For fixed $r=w/v>1$ and all sufficiently large $M$, the hyperbolic root exists, $\kappa_M\to\log r$, and $$\label{eq:asymptotic}
 E_{\rm e}\sim w(1-r^{-2})r^{-M}.$$ Consequently the finite pair is never exactly zero for $v>0$, although its splitting is exponentially small.

Writing $z=e^{-\kappa}$ turns [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"} into $r=z^{-1}(1-z^{2M+2})/(1-z^{2M})$, hence $z\to r^{-1}$. Equation [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} becomes $E_{\rm e}=v z^{M-1}(1-z^2)/(1-z^{2M})$, which gives [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref" reference="eq:asymptotic"}.

\>0

# Bulk winding, boundary faces, and unitary propagation

Close the chain and use momenta $k_n=2\pi n/M$. Our orientation convention is $$\label{eq:bloch}
 q(k)=v+we^{\mathrm{i}k},\qquad
 h(k)=\begin{pmatrix}0&\overline{q(k)}\\q(k)&0\end{pmatrix}.$$

[\[thm:bulk\]]{#thm:bulk label="thm:bulk"} The Bloch energies are $$\label{eq:dispersion}
 E_\pm(k)=\pm\sqrt{v^2+w^2+2vw\cos k}.$$ For the continuum symbol and the sampled $M$-cell ring, respectively, let $\Delta_\infty$ and $\Delta_M$ denote the minimum positive-band distance to zero. Then $$\label{eq:gaps}
 \Delta_\infty=|v-w|,\qquad
 \Delta_M=
 \begin{cases}
 |v-w|,&M\ \text{even},\\
 \sqrt{v^2+w^2-2vw\cos(\pi/M)},&M\ \text{odd}.
 \end{cases}$$ The corresponding central band gaps are $2\Delta_\infty$ and $2\Delta_M$. Whenever the loop avoids zero, its counterclockwise winding is $1$ for $w>v$ and $0$ for $v>w$; at $v=w>0$ it is undefined. At this critical line a finite ring has a two-dimensional zero sector if and only if $M$ is even. For odd $M$ it instead has $\Delta_M=2v\sin(\pi/(2M))>0$.

Squaring [\[eq:bloch\]](#eq:bloch){reference-type="eqref" reference="eq:bloch"} gives $|q(k)|^2I$, proving the dispersion. Over the continuum, $\cos k$ is minimized at $k=\pi$. The finite grid samples that point exactly for even $M$; for odd $M$ its nearest points are $\pi\pm\pi/M$, which proves [\[eq:gaps\]](#eq:gaps){reference-type="eqref" reference="eq:gaps"}. The curve $q(k)$ is the counterclockwise circle of radius $w$ centred at $v$. It encloses zero exactly when $w>v$. On the critical line it reaches zero only at $k=\pi$, which belongs to the finite grid exactly for even $M$; the corresponding $2\times2$ fiber is zero.

Theorems [\[thm:edge\]](#thm:edge){reference-type="ref" reference="thm:edge"} and [\[thm:bulk\]](#thm:bulk){reference-type="ref" reference="thm:bulk"} exhibit a finite separation: the bulk is topological for $w/v>1$, but the open pair is strictly hyperbolic only for $w/v>(M+1)/M$. Equality in the latter condition is a band-edge taper, not an exponentially localized state.

[\[thm:faces\]]{#thm:faces label="thm:faces"} For the open chain the following statements are exact.

1.  If $w=0<v$, there are $M$ dimers and $\pm v$ each has multiplicity $M$.

2.  If $v=0<w$, there are $M-1$ dimers, $\pm w$ each has multiplicity $M-1$, and $A_1,B_M$ span a two-dimensional zero sector.

3.  If $v=w=0$, the kernel has dimension $2M$.

4.  If $v=w>0$, then $\operatorname{spec}(H_O)=\{2v\cos(\ell\pi/(2M+1)):1\leq\ell\leq2M\}$, so zero is absent.

For $M=1$, declared separately, the open intercell bond is absent and the energies are $\pm v$; the periodic wrap merges with the intracell bond and the energies are $\pm(v+w)$.

The first three statements follow by listing the isolated sites and bonds. The fourth is the sine diagonalisation of the uniform path on $2M$ sites; its denominator $2M+1$ prevents a zero cosine. The last statement follows from the two explicit $2\times2$ matrices.

[\[thm:propagator\]]{#thm:propagator label="thm:propagator"} Let $\operatorname{sinc}z=\sin(z)/z$ with $\operatorname{sinc}0=1$. Entire matrix functional calculus gives, on every face in Theorem [\[thm:faces\]](#thm:faces){reference-type="ref" reference="thm:faces"}, $$\label{eq:propagator}
 e^{-\mathrm{i}tH_O}=\begin{pmatrix}
 \cos(t\sqrt{TT^*})&-\mathrm{i}t\,\operatorname{sinc}(t\sqrt{TT^*})T\\
 -\mathrm{i}t\,\operatorname{sinc}(t\sqrt{T^*T})T^*&\cos(t\sqrt{T^*T})
 \end{pmatrix}.$$ It is unitary and satisfies $\Gamma e^{-\mathrm{i}tH_O}\Gamma=e^{\mathrm{i}tH_O}=(e^{-\mathrm{i}tH_O})^*$.

The even and odd powers have block forms $$H_O^{2n}=\operatorname{diag}((TT^*)^n,(T^*T)^n),\qquad
 H_O^{2n+1}=\begin{pmatrix}0&(TT^*)^nT\\(T^*T)^nT^*&0\end{pmatrix}.$$ Separating the exponential series proves [\[eq:propagator\]](#eq:propagator){reference-type="eqref" reference="eq:propagator"}. Because cosine and sinc are entire in the squared operators, no inverse or positive singular-value assumption enters. Unitarity follows from self-adjointness, and the last identity from chirality.

\>1

# Quench corollary, evidence, and Route-A boundary

Consider strictly positive, gapped initial and final hoppings. Let $q_i(k),q_f(k)$ use [\[eq:bloch\]](#eq:bloch){reference-type="eqref" reference="eq:bloch"}, and start in the lower initial Bloch state.

[\[cor:quench\]]{#cor:quench label="cor:quench"} Its final-evolution amplitude is $$\label{eq:loschmidt}
 g_k(t)=\cos(E_f(k)t)+\mathrm{i}c(k)\sin(E_f(k)t),\qquad
 c(k)=\frac{\operatorname{Re}(\overline{q_i(k)}q_f(k))}
 {|q_i(k)||q_f(k)|}.$$ A continuum mode vanishes at a real time if and only if $$\label{eq:cross}
 (v_i-w_i)(v_f-w_f)<0.$$ In that case $$\label{eq:criticalmode}
 \cos k_*=-\frac{v_iv_f+w_iw_f}{v_iw_f+w_iv_f},\qquad
 t_n=\frac{\pi/2+n\pi}{E_f(k_*)}.$$ A finite ring has such an exact mode zero only if a sampled $k_m=2\pi m/M$ has this cosine.

Pauli-matrix exponentiation gives [\[eq:loschmidt\]](#eq:loschmidt){reference-type="eqref" reference="eq:loschmidt"}. A complex zero requires both $\cos(E_ft)=0$ and $c(k)=0$. The numerator of $c$ is $$A+B\cos k,\qquad A=v_iv_f+w_iw_f,\quad B=v_iw_f+w_iv_f>0.$$ It has a root in $[-1,1]$ exactly when $A<B$, since $A,B>0$; but $A-B=(v_i-w_i)(v_f-w_f)$. Gapped endpoints make the inequality strict, giving [\[eq:cross\]](#eq:cross){reference-type="eqref" reference="eq:cross"}--[\[eq:criticalmode\]](#eq:criticalmode){reference-type="eqref" reference="eq:criticalmode"}. A finite Fourier decomposition contains only its sampled momenta, proving the last sentence.

For example, the quench $(v_i,w_i)=(3,1)$ to $(v_f,w_f)=(1,5)$ has $\cos k_*=-1/2$. In the audited range, and in general, the finite ring hits that value exactly when $3$ divides $M$. Opposite bulk phases alone do not guarantee an exact zero for an arbitrary finite ring. This is a single-particle mode statement, not a many-body dynamical-phase-transition claim.

#### Evidence.

The content-addressed evidence has 55 open-polynomial rows, 33 rational hyperbolic witnesses, 11 threshold rows, 70 periodic rows containing 595 momentum cells, 33 boundary rows, 30 propagator rows, and six quench rows: 7,161 audited scalar leaves. A producer-independent checker performs 10,948 checks using exact Sturm sequences and a separate matrix exponential. SymPy closes 9,181 identities, two isolated runs replay byte for byte, and 53 repaired-hash/parser mutations must fail. These finite grids are regressions; Theorems [\[thm:edge\]](#thm:edge){reference-type="ref" reference="thm:edge"}--[\[thm:propagator\]](#thm:propagator){reference-type="ref" reference="thm:propagator"} and Corollary [\[cor:quench\]](#cor:quench){reference-type="ref" reference="cor:quench"} have the stated analytic domains.

#### Collision boundary.

C308 studies a one-site non-Hermitian nonreciprocal Hatano--Nelson skin chain and excludes topology. The present object is balanced, Hermitian, bipartite, and chiral; its distinguishing theorem is the strict finite bulk--edge threshold separation. C267 is an infinite uniform-field Wannier--Stark ladder, C297 a two-site PT dimer, and C138 a metric-graph flux winding problem. No resolvent, pseudospectral, or skin-effect claim is reused here.

#### Route-A result and nonclaims.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ The cells and Bloch momentum carry no rational-prime payload (A0); the momentum loop is not a primitive-orbit ledger (A1); the finite determinant is not an Euler product (A2); and no target functional equation, counting law, or divisor appears (A3). The finite Hermitian matrix is already a natural source quantization (A4), but its lattice levels are not target zeros and it is not a Hilbert--Pólya operator. Route A is rejected and Route B remains locked. No target Euler factor, root number, automorphy, zero correspondence, disorder, interaction, or self-consistent phonon claim is made.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed derivations, independent recomputation, adversarial tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 W. P. Su, J. R. Schrieffer, and A. J. Heeger, "Solitons in Polyacetylene," *Physical Review Letters* 42 (1979), 1698--1701. DOI: [10.1103/PhysRevLett.42.1698](https://doi.org/10.1103/PhysRevLett.42.1698).

W. P. Su, J. R. Schrieffer, and A. J. Heeger, "Soliton excitations in polyacetylene," *Physical Review B* 22 (1980), 2099--2111. DOI: [10.1103/PhysRevB.22.2099](https://doi.org/10.1103/PhysRevB.22.2099).

J. K. Asbóth, L. Oroszlány, and A. Pályi, "The Su--Schrieffer--Heeger Model," in *A Short Course on Topological Insulators* (Springer, 2016). DOI: [10.1007/978-3-319-25607-8\_1](https://doi.org/10.1007/978-3-319-25607-8_1).
