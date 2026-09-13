---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-compact-heisenberg-nilflow-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a/paper/main_body.tex"
canonical_pdf: "henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a/paper/main.pdf"
source_sha256: "b91c707461c6516ba38a470819eb51e00f9eb69f7256ddb9cd1a6fec81859ef6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Closed-Orbit Tori and the Complete Original-Clock Spectrum of Compact Heisenberg Nilflows

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a/paper/main_body.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_compact_heisenberg_nilflow_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the compact integer Heisenberg quotient, we study every member of the two-parameter family $W=X+\beta Y+\gamma Z$ without changing its physical clock. At irrational slope there are no closed orbits. At rational slope $p/q$, one invariant circle-valued phase gives every primitive period: a phase of reduced denominator $d$ has least period $dq$, and time $kq$ fixes exactly $k$ connected two-tori. The return maps are clean and unipotent, so a finite isolated-orbit census cannot represent these continuous families. \>0 An explicit signed-mode Weil--Brezin transform gives the full Hilbert-space decomposition. Chirp conjugation identifies the exact self-adjoint domains, the toral pure-point component, and the countably infinite multiplicity Lebesgue component; no singular-continuous spectrum remains. \>1 A skew-shift proof gives unique ergodicity for every irrational slope, while the whole time-one map is never ergodic. An explicit source involution reverses the original clock. The natural unitary, resolvent and heat owners are nevertheless noncompact, preventing ordinary global Fredholm determinants. Exact independent lattice computations audit 1,368 rational orbit rows. This is a source-local synthesis of classical nilflow mechanisms, not a literature-priority or target Riemann spectral claim.
author:
- 'HCS-C387 / HEN-O371'
date: 5 September 2026
title: |
  Closed-Orbit Tori and the Complete Original-Clock Spectrum\
  of Compact Heisenberg Nilflows
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<\>\<\>\]

**Keywords:** Heisenberg nilflows; closed orbits; clean fixed tori; Koopman spectrum; Weil--Brezin transform; \>1 Fredholm obstructionrational slope

中文摘要

本文在原物理时钟下研究紧海森堡商空间上的完整双参数流族。\
无理斜率没有闭轨；有理斜率的一个不变相位给出全部本原周期，\
固定集是连续二维环面而非孤立周期点，返回映射具有幂幺剪切。 \>0 显式正负中心模变换和啁啾共轭给出完整希尔伯特空间分解、\
自伴定义域、纯点及勒贝格谱重数，并排除奇异连续谱。 \>1 无理斜率下流唯一遍历，但全空间的时间一映射不遍历。\
同钟反演不消除自然算子的不紧性，故不能提升为目标行列式。\
精确整数格点复核仅作解析证明的回归验证，不声明文献首创。

# The frozen source and the contribution

Let $H=\mathbf R^3$ with $$(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy'),\qquad
 M=\mathbf Z^3\backslash H.$$ Haar measure has total mass one, represented by Lebesgue measure on the unit cube. The left-invariant fields are $X=\partial_x$, $Y=\partial_y+x\partial_z$, $Z=\partial_z$. We fix the coefficient of $X$ to one and allow all $\beta,\gamma\in\mathbf R$ in $W=X+\beta Y+\gamma Z$. This is a declared family, not a normalization performed at a vanishing coefficient. Our conventions are $U_tf=f\circ\phi_t=e^{\mathrm itA}f$ and $A=-\mathrm iW$.

Classical nilflow theory already distinguishes the toral factor from relative Lebesgue spectrum and mixing on its orthogonal complement; Avila--Forni--Ulcigrai explicitly recall these facts and the constant-roof skew-shift construction [@afu Sections 2.1--2.2]. Flaminio--Forni place invariant distributions and cohomological equations in the broader nilflow setting [@ff]. We reconstruct the source results needed here directly, including rational slopes and exact operator domains. We do not claim novelty for the classical spectral or ergodic mechanisms, and do not transfer any theorem about nontrivial time changes to this unchanged flow. Within the present research sequence this is a continuous right-translation owner, not the discrete Heisenberg automorphism of C146/C151/C156, nor the noncompact sub-Riemannian geodesic of C270.

# Every closed orbit and every fixed torus

**Round 0 advance.** A single source-invariant phase classifies all rational-slope primitive periods and exposes why an isolated-cycle determinant is not available.

The flow and the lattice identification are $$\begin{aligned}
 \phi_t(x,y,z)&=(x+t,y+\beta t,z+\gamma t+\beta xt+\beta t^2/2),\label{flow}\\
 (x,y,z)&\sim(x+r,y+s,z+k+ry),\qquad r,s,k\in\mathbf Z.\label{lattice}\end{aligned}$$ Equation [\[flow\]](#flow){reference-type="eqref" reference="flow"} is right multiplication by $(t,\beta t,\gamma t+\beta t^2/2)$, so it descends to $M$, is complete and preserves Haar measure. The $x$ velocity is one, hence no point is stationary. By [\[lattice\]](#lattice){reference-type="eqref" reference="lattice"}, a nonzero return requires $t\in\mathbf Z$ and $\beta t\in\mathbf Z$. Thus irrational $\beta$ has no closed orbit at any point or any nonzero time.

Let $\beta=p/q$ with $(p,q)=1$ and $q>0$, including $(p,q)=(0,1)$. The circle-valued function $$\theta(x,y)=\gamma q+px-qy+pq/2\pmod1$$ is well-defined and invariant on $M$. A point closes if and only if $\theta$ is rational. If its reduced denominator is $d$, its least positive period is $dq$. At time $kq>0$ the fixed set is exactly $k$ connected two-tori, and the set of points with least period $dq$ is exactly $\varphi(d)$ connected two-tori, with $\varphi(1)=1$.

Integer lattice changes add $pr-qs$ to $\theta$; its derivative along $W$ is $p-q\beta=0$. Any horizontal return time is $dq$ for an integer $d$. The central displacement after subtracting the required lattice action is $$\gamma dq+\beta x dq+\beta(dq)^2/2-dqy
 =d\theta+pq\,d(d-1)/2.$$ The last term is integral, so return is exactly $d\theta=0$ in $\mathbf R/\mathbf Z$. This gives the least-period assertion, including $\theta=0$. For time $kq$, the permissible phases are exactly $j/k$, $0\le j<k$. The base map $px-qy:\mathbf T^2\to\mathbf T$ has connected circle fibres because $(p,q)$ is primitive. The central circle bundle restricts trivially to such a base circle, hence its preimage is a connected two-torus. More explicitly, lift the base circle on an interval; its endpoint central shift can be absorbed by a linear change of the central coordinate. Finally precisely $\varphi(d)$ phases have reduced denominator $d$.

Each primitive torus contains continuum many distinct closed flow orbits, rather than a finite collection of primitive cycles. In local quotient coordinates the return derivative is $$D\phi_{kq}=
 \begin{pmatrix}1&0&0\\0&1&0\\pk&-qk&1\end{pmatrix}.$$ Indeed differentiating the lifted flow gives the entry $\beta t$ in the $x$ column, while undoing the lattice shift subtracts $t\,dy$ from the central coordinate. Its difference from the identity has rank one and kernel $\{p\,dx-q\,dy=0\}$, exactly the tangent plane of the fixed torus. The fixed set is therefore clean. All multipliers equal one, and quotienting out the flow direction leaves a nontrivial unipotent two-dimensional Poincaré return. In particular $\det(I-D\phi_{kq})=0$; a sampled torus cannot supply a finite isolated-orbit denominator.

For a strobe $h\ne0$ at rational slope, if $h/q$ is irrational, no positive iterate returns anywhere. If $h/q$ is rational, some positive iterate has an uncountable fixed set. Thus ordinary fixed-cardinality Artin--Mazur zeta functions are either one or undefined. Irrational slope always gives the former, for every nonzero strobe. This dichotomy does not compute a spectral determinant.

\>0

# The entire Hilbert space, including negative central modes

**Round 1 advance.** The orbit atlas is supplemented by a complete unitary decomposition, exact domains and multiplicities; it is not a finite-mode approximation.

Expand centrally, $f(x,y,z)=\sum_{m\in\mathbf Z}e^{2\pi\mathrm imz}f_m(x,y)$. The quotient convention imposes $$f_m(x+r,y+s)=e^{-2\pi\mathrm imry}f_m(x,y).$$ The $m=0$ space is $L^2(\mathbf T^2)$. For $m\ne0$, expand in $y$: $f_m(x,y)=\sum_k f_{m,k}(x)e^{2\pi\mathrm iky}$. The shift $x\mapsto x+1$ gives $f_{m,k}(x+1)=f_{m,k+m}(x)$.

Writing $k=j+m\ell$, where $0\le j<|m|$, gives the unique coefficient representation $f_{m,j+m\ell}(x)=g_j(x+\ell)$. Consequently define $$V_{m,j}g=e^{2\pi\mathrm imz}
 \sum_{\ell\in\mathbf Z}g(x+\ell)e^{2\pi\mathrm i(j+m\ell)y}.$$

For Schwartz $g$ this is a smooth lattice-invariant function; negative $m$ changes the residue ordering but not the representation. Parseval in $y$ and the tiling of $\mathbf R$ by $[0,1]+\ell$ give $\|V_{m,j}g\|_{L^2(M)}=\|g\|_{L^2(\mathbf R)}$. Orthogonality of residues and the reverse coefficient construction prove surjectivity, hence $$L^2(M)=L^2(\mathbf T^2)\oplus
 \bigoplus_{m\ne0}\bigoplus_{j=0}^{|m|-1}V_{m,j}L^2(\mathbf R).\label{decomp}$$ This proof identifies the entire space, rather than merely displaying some invariant subspaces.

On the torus block, $e^{2\pi\mathrm i(kx+ly)}$ has eigenvalue $2\pi(k+\beta l)$. On each noncentral block, $$A_{m,j}=-\mathrm i\frac{d}{du}+2\pi(\beta m u+\beta j+\gamma m).$$ Put $$\psi_{m,j}(u)=\pi\beta m u^2+2\pi(\beta j+\gamma m)u,\qquad
 C_{m,j}g=e^{-\mathrm i\psi_{m,j}}g.$$ The exact self-adjoint domain is $C_{m,j}H^1(\mathbf R)$. The toral spectral measure is pure point, each noncentral block has multiplicity-one Lebesgue spectrum, the total noncentral multiplicity is countably infinite, and there is no singular-continuous component. The spectrum of $A$ is $\mathbf R$ for every $\beta,\gamma$.

Substitute the transform into $-\mathrm i(\partial_x+\beta\partial_y+
(\gamma+\beta x)\partial_z)$. On the term indexed by $\ell$, use $u=x+\ell$ to obtain the stated affine potential. Since $\psi_{m,j}'=2\pi(\beta m u+\beta j+\gamma m)$, direct differentiation yields $A_{m,j}C_{m,j}=C_{m,j}(-\mathrm i\partial_u)$. Unitary conjugation of the momentum operator on $H^1(\mathbf R)$ proves the domain assertion and self-adjointness. In particular the domain is not replaced by a separate requirement that both $g'$ and $ug$ lie in $L^2$; cancellation under the chirp is part of the actual domain.

The toral domain is the set of Fourier coefficients satisfying $$\sum_{k,l}|2\pi(k+\beta l)|^2|\widehat f_{k,l}|^2<\infty.$$ Combine this with the noncentral domains using square-summable graph norms. Schwartz functions after chirp multiplication form smooth block cores. On these dense cores the generated unitary group and the actual Koopman flow agree by integration of the first-order equation. Their extensions agree by unitarity, so the assembled operator is the original generator.

Fourier transformation of $-\mathrm i\partial_u$ gives multiplication by $2\pi\xi$ on $L^2(\mathbf R)$, proving multiplicity-one Lebesgue spectrum. There are countably many blocks in [\[decomp\]](#decomp){reference-type="eqref" reference="decomp"}. The torus contributes only its character eigenvectors, which are a complete orthonormal basis. No other spectral type can occur.

For irrational $\beta$, the toral eigenvalues are distinct and dense in $\mathbf R$. For rational $\beta=p/q$, their set is $2\pi\mathbf Z/q$, and each has countably infinite multiplicity since $qk+pl$ takes every integer with infinitely many representations. These are assertions about the toral block; the full generator always also has its Lebesgue component.

A correlation in one noncentral block is the Fourier transform of an $L^1$ product of two $L^2$ Fourier transforms, so it tends to zero as $|t|\to\infty$ by the Riemann--Lebesgue lemma. Finite block approximation and Cauchy--Schwarz extend this conclusion to the whole noncentral subspace. The full flow is never weakly mixing, because the nonconstant toral eigenfunction $e^{2\pi\mathrm ix}$ survives for all parameters.

\>1

# Ergodicity with the correct phase space and clock

**Round 2 advance.** We prove the all-irrational ergodic statement without a Diophantine restriction, construct a same-clock reversal, and show that the natural operator owners still cannot give an ordinary global Fredholm determinant.

The global section $x=0\pmod1$ has roof exactly one. Undoing the unit $x$ displacement in [\[lattice\]](#lattice){reference-type="eqref" reference="lattice"} gives $$S(y,z)=(y+\beta,z-y+\gamma-\beta/2),\qquad
 S^n(y,z)=(y+n\beta,z-ny+n\gamma-\beta n^2/2).$$ The orbit phase of a nonconstant character $(k,l)$ is a constant plus $n(k\beta-ly+l\gamma)-l\beta n^2/2$. When $\beta$ is irrational and $l=0$, the geometric-series average tends to zero uniformly in the starting point. When $l\ne0$, the difference at fixed nonzero lag $h$ has irrational linear coefficient $-l\beta h$. Apply van der Corput at a fixed finite lag cutoff $H$. Each of the finitely many linear geometric averages tends uniformly to zero as $N\to\infty$; the remaining limsup of the squared average is $O(1/H)$. Now send $H\to\infty$. This order of limits does not assert a uniform Diophantine bound over all slopes. Trigonometric approximation gives uniform Birkhoff convergence for every continuous function on the section to its Haar integral. Every invariant probability has these same integrals, so $S$ is uniquely ergodic. The constant-roof suspension is exactly the original flow and gives its unique ergodicity. Conversely rational $\beta$ has the nonconstant invariant $\theta$, so is not Haar ergodic.

Crucially, the whole time-one map is not the section map: it acts on a three-manifold, and $e^{2\pi\mathrm ix}$ is invariant under $U_1$. The whole time-one map is therefore never ergodic, even at irrational slope. Unique ergodicity of the continuous flow, noncentral correlation decay, and failure of whole-space weak mixing are consistent statements.

# Same-clock reversal and HEN-O371

Right translation $T_c(x,y,z)=(x,y+c,z+cx)$ is well-defined on the left quotient and pushes $W_\gamma$ to $W_{\gamma+c}$. The lattice-preserving automorphism $I(x,y,z)=(-x,-y,z)$ sends $W_0$ to $-W_0$. Hence $$J_\gamma=T_\gamma I T_{-\gamma},\qquad
 J_\gamma(x,y,z)=(-x,-y+2\gamma,z-2\gamma x)$$ is a measure-preserving involution and $J_\gamma\phi_tJ_\gamma=\phi_{-t}$ with the original time. Thus $\Theta f=\overline{f\circ J_\gamma}$ is antiunitary and $\Theta U_t\Theta=U_{-t}$. Complex conjugation alone commutes with the real-coordinate Koopman flow; it is not substituted for this reversor.

Neither $U_t$, nor $(A-\mathrm i)^{-1}$, nor $e^{-\tau A^2}$ for $\tau>0$ is compact. The latter two are in no finite Schatten class, and the positive heat operator has infinite extended trace.

An infinite-dimensional unitary maps an orthonormal sequence to another orthonormal sequence, so is not compact. Even one noncentral block reduces the resolvent and heat operator to multiplication on $L^2(\mathbf R)$ by $$(2\pi\xi-\mathrm i)^{-1},\qquad e^{-4\pi^2\tau\xi^2}.$$ On $[-1,1]$ their moduli are bounded below respectively by $(4\pi^2+1)^{-1/2}$ and $e^{-4\pi^2\tau}$. Choose infinitely many orthonormal functions on pairwise disjoint positive-measure subsets of this interval. Their images remain orthogonal with norms uniformly bounded below, hence have no convergent subsequence. Restriction to one block already precludes compactness of the full operator. Every finite Schatten class consists of compact operators. For the positive heat operator, the same orthonormal sequence has diagonal entries bounded below by $e^{-4\pi^2\tau}$, so its extended trace is infinite.

The heat parameter $\tau$ is auxiliary: applying a spectral function to $A$ does not change $\tau$ into the physical clock $t$. Neither the self-adjoint generator nor the source reversor cures the trace obstruction. We exclude ordinary global Fredholm determinants for these natural owners; we do not prove that every conceivable relative or distributional regularization is impossible.

# Exact evidence and strict Route-A separation

The independently implemented lattice checker examines all integer times through $12q$ in 1,368 orbit rows, not only phase-predicted returns. The grid contains 19 primitive signed slopes, three central velocities, all 12 rational phases of reduced denominator at most six, and two base $x$ coordinates. It also contains 228 fixed-torus rows, 171 group-law and reversal rows, 126 signed Fourier-block rows, and 24 exact quadratic- irrational nonreturn controls. Independent symbolic identities verify the generic group law, skew-shift iteration, lattice phase cancellation and chirp conjugation. No floating-point Fourier approximation is offered as evidence for completeness or unique ergodicity.

The all-parameter theorems are proved above; the finite grid is regression. Integer lattice coordinates alone do not give an intrinsic rational-prime carrier. Irrational slope has no closed orbit, whereas rational slope has continuous families, not isolated prime-owned cycles. No target zero fitting or six-control A1 promotion is performed. The strict verdict is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Only the last layer records a source Hilbert space, domain and reversal. It does not claim a target quantization or Hilbert--Pólya operator.

# Scope and limitations

This is a theorem about a frozen continuous source, including zero and negative slopes and arbitrary central velocity, not a target spectral identification. Rational-slope periods use the same original clock as the irrational flow. The $X=0$ family is outside scope. Classical prior art is acknowledged; no time-change mixing theorem or quantitative equidistribution rate is asserted. No target arithmetic local data, Euler factors, root number, automorphy, divisor, functional equation, zero match or Hilbert--Pólya operator is claimed. Route B remains disabled.

This work used AI-assisted proof exposition and exact-code development. Separate same-family agents read the proof and manuscript and tested additional hostile inputs; these are internal reviews, not external human review or formal verification. No unpublished material was uploaded to an external model.

9 A. Avila, G. Forni and C. Ulcigrai, *Mixing for Time-Changes of Heisenberg Nilflows*, arXiv:1003.4636v3 (2010). <https://arxiv.org/abs/1003.4636>. L. Flaminio and G. Forni, *On the cohomological equation for nilflows*, Journal of Modern Dynamics **1**(1) (2007), 37--60. <https://doi.org/10.3934/jmd.2007.1.37>.
