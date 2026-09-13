---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kronig-penney-band-gap-atlas-route-a"
canonical_tex: "henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a/paper/main.pdf"
source_sha256: "002592468e61845b4d7215f0ca6737a50b09688bb8f131dcdf5e910b80920606"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Band--Gap Atlas for the Delta-Comb Kronig--Penney Hamiltonian

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kronig_penney_band_gap_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We realize the one-dimensional periodic delta comb by a closed quadratic form for every real coupling and compute its monodromy discriminant without a formal-potential shortcut. Floquet reduction gives an exact spectral criterion, pure absolute continuity, and a complete negative-energy atlas; the coupling $ga=-4$ is the precise zero-energy threshold. This is the operator and discriminant owner. \>0 All positive bands and gaps are then indexed on both sides of every Bragg point. Every nonzero coupling opens every Bragg gap, with an explicit high-energy width expansion, and the integrated and ordinary densities of states are obtained with their edge conventions. \>1 Independent transfer, edge, density, replay, and hostile receipts audit the formulas. The Hamiltonian is a natural quantization, but it has no target arithmetic payload and Route A is rejected.
author:
- 'Route-A source-local certificate HCS-C327'
date: 3 September 2026
title: 'An Exact Band--Gap Atlas for the Delta-Comb Kronig--Penney Hamiltonian'
```

## Markdown 正文

trailerid \[\<C3272026090300000000000000000000\>\<C3272026090300000000000000000000\>\]

# Closed form, matching owner, and Floquet discriminant

Fix a period $a>0$ and a coupling $g\in\mathbb R$. On $L^2(\mathbb R)$ define $$\label{eq:form}
 \mathfrak h_{a,g}[u]=\int_{\mathbb R}|u'(x)|^2\,dx
       +g\sum_{n\in\mathbb Z}|u(na)|^2,
 \qquad \operatorname{dom}\mathfrak h_{a,g}=H^1(\mathbb R).$$ The periodized trace inequality makes the sum finite and infinitesimally form bounded relative to the kinetic term. Thus [\[eq:form\]](#eq:form){reference-type="eqref" reference="eq:form"} is closed and lower semibounded for either sign of $g$ and defines a unique self-adjoint operator $H_{a,g}$.

[\[prop:owner\]]{#prop:owner label="prop:owner"} The operator acts as $-u''$ off $a\mathbb Z$ and has domain characterized by $u\in H^1(\mathbb R)$, cellwise $H^2$ regularity with $u''\in L^2(\mathbb R\setminus a\mathbb Z)$, and $$\label{eq:jump}
 u'(na+)-u'(na-)=g u(na).$$ For $E=k^2>0$, propagation from one right limit to the next is conjugate to the determinant-one matrix $$\label{eq:transfer}
 M(E)=(\begin{matrix}1&0\\g&1\end{matrix})
 (\begin{matrix}\cos(ka)&\sin(ka)/k\\-k\sin(ka)&\cos(ka)\end{matrix}).$$ Its half trace is $$\label{eq:delta}
 \Delta(E)=\cos(ka)+\frac{g}{2k}\sin(ka).$$ At $E=0$ this means $\Delta(0)=1+ga/2$ by continuity. At $E=-\kappa^2<0$ it means $$\label{eq:negative-delta}
 \Delta(-\kappa^2)=\cosh(\kappa a)
       +\frac{g}{2\kappa}\sinh(\kappa a).$$

On every centered cell $I_n$ the one-dimensional trace estimate gives, for each $\varepsilon>0$, $$|u(na)|^2\leq \varepsilon\|u'\|_{L^2(I_n)}^2
                 +C_{a,\varepsilon}\|u\|_{L^2(I_n)}^2.$$ Summing the disjoint-cell estimates proves the asserted form bound; choosing $\varepsilon$ after $g$ proves lower semiboundedness and closedness by the form perturbation theorem. Integration by parts identifies the associated operator and [\[eq:jump\]](#eq:jump){reference-type="eqref" reference="eq:jump"}. Free propagation followed by the jump gives [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}; direct multiplication gives determinant one and [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"}. Replacing $k$ by $\mathrm{i}\kappa$ gives [\[eq:negative-delta\]](#eq:negative-delta){reference-type="eqref" reference="eq:negative-delta"}, including the displayed limit at zero.

The Floquet transform decomposes $H_{a,g}$ over $\theta\in[-\pi,\pi)$ into compact-resolvent fibres on $[-a/2,a/2]$. The fibre functions are quasi-periodic at the endpoints and obey [\[eq:jump\]](#eq:jump){reference-type="eqref" reference="eq:jump"} at the origin. A fibre eigenvalue satisfies $$\label{eq:floquet}
 \Delta(E)=\cos\theta.$$

[\[thm:floquet\]]{#thm:floquet label="thm:floquet"} For every $a>0$ and $g\in\mathbb R$, $$\label{eq:spectrum}
 \operatorname{spec}(H_{a,g})=\{E\in\mathbb R:|\Delta(E)|\leq1\},
 \qquad \operatorname{spec}(H_{a,g})=\operatorname{spec}_{\mathrm{ac}}(H_{a,g}).$$ There is neither point nor singular-continuous spectrum. The full-line Bloch multiplicity is two in every band interior. If $g\ne0$, each band edge is a simple periodic or antiperiodic fibre eigenvalue. If $g=0$, the positive Bragg contacts $(n\pi/a)^2$, $n\geq1$, are double fibre eigenvalues; $E=0$ is the simple free bottom.

Equation [\[eq:floquet\]](#eq:floquet){reference-type="eqref" reference="eq:floquet"} and unimodularity give [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"}. The fibre eigenvalue branches are nonconstant real-analytic functions, with local analytic relabelling at crossings. Their critical points are isolated, so pushing Lebesgue measure in $\theta$ through the branches is absolutely continuous; this is also the standard periodic-singular Floquet theorem. Thus their direct integral has neither point nor singular-continuous part. Interior energies have the two distinct angles $\pm\theta$. At an edge the fibre multiplicity is the dimension of $\ker(M\mp I)$. For $g\ne0$, $M$ cannot equal $\pm I$: at a Bragg point the jump factor is nontrivial, while away from a Bragg point the upper-right entry in [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"} is nonzero. Hence the kernel is one-dimensional. For $g=0$, free propagation equals $(-1)^nI$ at every positive Bragg contact, giving dimension two. The constant periodic mode is the sole zero-energy fibre eigenfunction.

# Negative spectrum and the zero threshold

Put $$\label{eq:scaled}
 q=ga,\qquad z=Ea^2.$$ This scaling removes $a$ from the atlas. For $g<0$ write $h=-q>0$ and $y=\kappa a$. Then $$\begin{aligned}
 \Delta_- (y)-1
 &=2\sinh(y/2)[\sinh(y/2)-\frac{h}{2y}\cosh(y/2)],\label{eq:nplus}\\
 \Delta_- (y)+1
 &=2\cosh(y/2)[\cosh(y/2)-\frac{h}{2y}\sinh(y/2)].\label{eq:nminus}\end{aligned}$$ The functions $2y\tanh(y/2)$ and $2y\coth(y/2)$ are strictly increasing; their ranges are respectively $(0,\infty)$ and $(4,\infty)$.

[\[thm:negative\]]{#thm:negative label="thm:negative"} If $g>0$, there is no nonpositive spectrum. If $g=0$, the spectrum begins at zero. Suppose $g<0$, and let $y_+>0$ be the unique solution $$\label{eq:yplus}
 h=2y_+\tanh(y_+/2).$$ The first band has lower edge $-y_+^2/a^2$, where $\Delta=1$.

1.  If $0<h<4$, zero lies in the interior of this band; its upper edge is positive\>0; it is specified in Theorem [\[thm:positive\]](#thm:positive){reference-type="ref" reference="thm:positive"}.

2.  If $h=4$ (equivalently $ga=-4$), zero is its simple antiperiodic upper edge, with $\Delta(0)=-1$.

3.  If $h>4$, there is a unique $y_->0$ satisfying $$\label{eq:yminus}
     h=2y_-\coth(y_-/2),$$ with $y_-<y_+$. The first band is exactly $[-y_+^2/a^2,-y_-^2/a^2]$, and $(-y_-^2/a^2,0]$ lies in a gap.

For $g>0$, [\[eq:negative-delta\]](#eq:negative-delta){reference-type="eqref" reference="eq:negative-delta"} is greater than one at every nonpositive energy. For $g<0$, equations [\[eq:nplus\]](#eq:nplus){reference-type="eqref" reference="eq:nplus"} and [\[eq:nminus\]](#eq:nminus){reference-type="eqref" reference="eq:nminus"} reduce the two edge equations to [\[eq:yplus\]](#eq:yplus){reference-type="eqref" reference="eq:yplus"} and [\[eq:yminus\]](#eq:yminus){reference-type="eqref" reference="eq:yminus"}. The derivative of the first edge function is positive. After multiplication by $\sinh^2(y/2)$, the derivative of the second has numerator $\sinh y-y>0$; its left limit is four. The factor signs show that $|\Delta_-|\leq1$ for $0\leq y\leq y_+$ when $h\leq4$, and for $y_-\leq y\leq y_+$ when $h>4$. Reversing $E=-y^2/a^2$ proves every case.

\>0

# Complete sign atlas and gap asymptotic

For $x=a\sqrt E>0$ the two factorizations $$\begin{aligned}
 \Delta-1&=2\sin(x/2)[\frac{q}{2x}\cos(x/2)-\sin(x/2)],\label{eq:pplus}\\
 \Delta+1&=2\cos(x/2)[\cos(x/2)+\frac{q}{2x}\sin(x/2)]\label{eq:pminus}\end{aligned}$$ show both the fixed edges $x=n\pi$ and their partners. A partner adjacent to $n\pi$ obeys the single parity-free equation $$\label{eq:partner}
 q=2x_n\tan\frac{x_n-n\pi}{2}.$$ Its left-hand side as a function of $x$ has derivative $(x+\sin(x-n\pi))/\cos^2((x-n\pi)/2)>0$ on the relevant open cell.

[\[thm:positive\]]{#thm:positive label="thm:positive"} The positive spectrum is as follows.

1.  If $q>0$, equation [\[eq:partner\]](#eq:partner){reference-type="eqref" reference="eq:partner"} has a unique $x_n\in(n\pi,(n+1)\pi)$ for every $n\geq0$. The bands are $$B_n=[x_n^2/a^2,((n+1)\pi/a)^2],\qquad n\geq0,$$ and the gaps are $((n\pi/a)^2,x_n^2/a^2)$ for $n\geq1$, together with the gap below $B_0$.

2.  If $q=0$, $\operatorname{spec}(H_{a,0})=[0,\infty)$; the folded free bands meet at every Bragg energy and no gap is open.

3.  If $-4<q<0$, there is a unique $x_1\in(0,\pi)$ and the first band is $[-y_+^2/a^2,x_1^2/a^2]$. If $q=-4$, set $x_1=0$ and the first band is $[-y_+^2/a^2,0]$. If $q<-4$, there is no positive $x_1$ and the first band is the negative interval in Theorem [\[thm:negative\]](#thm:negative){reference-type="ref" reference="thm:negative"}. In all three cases, for every $n\geq1$ there is a unique $x_{n+1}\in(n\pi,(n+1)\pi)$ and $$B_n=[(n\pi/a)^2,x_{n+1}^2/a^2].$$ For $-4\leq q<0$ the first positive gap is $(x_1^2/a^2,(\pi/a)^2)$. For $q<-4$ it is the single gap $(-y_-^2/a^2,(\pi/a)^2)$ crossing zero. All later gaps are $(x_n^2/a^2,(n\pi/a)^2)$, $n\geq2$.

Consequently every Bragg gap is open for every $g\ne0$.

The monotonicity following [\[eq:partner\]](#eq:partner){reference-type="eqref" reference="eq:partner"} gives uniqueness. On the right cell the edge function ranges from zero to $+\infty$; on a left cell it ranges from $-\infty$ to zero. The exceptional first left cell instead has limiting value $-4$ at zero. The signs in [\[eq:pplus\]](#eq:pplus){reference-type="eqref" reference="eq:pplus"} and [\[eq:pminus\]](#eq:pminus){reference-type="eqref" reference="eq:pminus"} then distinguish the allowed and forbidden intervals and give the displayed ordering. A nonzero $q$ cannot solve [\[eq:partner\]](#eq:partner){reference-type="eqref" reference="eq:partner"} with $x_n=n\pi$, so none of the stated gaps collapses.

[\[cor:width\]]{#cor:width label="cor:width"} For fixed $q=ga\ne0$, let $G_n$ be the gap adjacent to $(n\pi/a)^2$ and not containing lower-energy exceptional structure. As $n\to\infty$, $$\begin{aligned}
 x_n-n\pi
 &=\frac{q}{n\pi}-\frac{q^2+q^3/12}{(n\pi)^3}
      +O_q(n^{-5}),\label{eq:displacement}\\
 |G_n|
 &=\frac{2|g|}{a}
 -\frac{\operatorname{sgn}(q)(q^2+q^3/6)}{(n\pi)^2a^2}
      +O_q(n^{-4}a^{-2}).\label{eq:gapwidth}\end{aligned}$$ In particular, there are computable $n_0(q)$ and $C(q)$ for which the absolute remainder in [\[eq:gapwidth\]](#eq:gapwidth){reference-type="eqref" reference="eq:gapwidth"} is at most $C(q)/(n^4a^2)$ for $n\geq n_0(q)$.

Put $N=n\pi$ and $x_n=N+\delta_n$. Equation [\[eq:partner\]](#eq:partner){reference-type="eqref" reference="eq:partner"} is $q=2(N+\delta_n)\tan(\delta_n/2)$. With $u=N^{-1}$ and $\delta_n=u v$, the equation is analytic at $(u,v)=(0,q)$ and its $v$-derivative there is one. The analytic implicit-function theorem and Taylor expansion give $v=q-(q^2+q^3/12)u^2+O_q(u^4)$, proving [\[eq:displacement\]](#eq:displacement){reference-type="eqref" reference="eq:displacement"} with a locally bounded Taylor remainder. Expanding $|(N+\delta_n)^2-N^2|/a^2$ gives [\[eq:gapwidth\]](#eq:gapwidth){reference-type="eqref" reference="eq:gapwidth"} and the stated bound.

# Integrated density of states and edge density

Enumerate the closed bands increasingly as $B_0,B_1,\ldots$, including the negative first band when $g<0$. Their lower and upper discriminants are $(-1)^j$ and $(-1)^{j+1}$. On the interior of $B_j$ define the unwrapped phase $$\label{eq:phase}
 K(E)=\frac{j\pi+\arccos((-1)^j\Delta(E))}{a}.$$

[\[thm:ids\]]{#thm:ids label="thm:ids"} The integrated density of states per unit length is zero below $B_0$, equals $$\label{eq:ids}
 N(E)=\frac{K(E)}{\pi}
 =\frac1a[j+\frac1\pi\arccos((-1)^j\Delta(E))]$$ on $B_j$, and is $(j+1)/a$ in the gap following $B_j$. It is continuous at all edges. In every open band, $$\label{eq:dos}
 \rho(E)=N'(E)=\frac{|\Delta'(E)|}
 {\pi a\sqrt{1-\Delta(E)^2}}.$$ For $E=k^2>0$, $$\label{eq:deltaprime}
 \Delta'(E)=-\frac{a\sin(ka)}{2k}
 +\frac{g(ak\cos(ka)-\sin(ka))}{4k^3},$$ with $\Delta'(0)=-a^2/2-ga^3/12$. For $g\ne0$ every finite edge has the usual one-sided inverse-square-root DOS singularity. For $g=0$ the folded formula is interpreted continuously and reduces to $N(E)=\sqrt E/\pi$ and $\rho(E)=1/(2\pi\sqrt E)$ for $E>0$.

Each fibre band supplies one state per cell as its Bloch angle traverses $[0,\pi]$. The orientation alternates, which is exactly corrected by $(-1)^j$ in [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"}. This proves [\[eq:ids\]](#eq:ids){reference-type="eqref" reference="eq:ids"} and the constant gap values. Differentiating yields [\[eq:dos\]](#eq:dos){reference-type="eqref" reference="eq:dos"}; direct differentiation of [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} yields [\[eq:deltaprime\]](#eq:deltaprime){reference-type="eqref" reference="eq:deltaprime"} and its Taylor limit. The edge equations and their strict monotonicity imply $\Delta'(E_*)\ne0$ for $g\ne0$, hence the square-root law. Direct simplification gives the free formulas.

\>1

# Density evidence and Route boundary

The machine-readable certificate contains 216 nonzero-coupling Bragg rows, 150 independently reconstructible transfer matrices at three lattice scales, 70 band-indexed IDS/DOS rows, five negative-atlas cases, and nine low-edge cases: 5,428 scalar leaves in total. The independent checker owns every field and performs 5,607 checks. SymPy verifies 295 exact identities; two isolated producer runs replay byte for byte; 55 repaired-hash, parser, nonfinite, duplicate-key, semantic, authority, and evidence-status attacks must fail. These finite receipts are regression evidence only; the form, factorization, monotonicity, and implicit-function arguments prove the all-parameter claims.

Kronig and Penney own the original periodic crystal band model [@kronigpenney]. Albeverio, Gesztesy, Høegh-Krohn, and Holden give the authoritative point-interaction framework, including infinitely many one-dimensional centres [@albeverio]. Hryniv and Mykytyuk establish self-adjointness, pure absolute continuity, and band--gap structure for a larger class of periodic singular potentials [@hryniv]. The exact sign-atlas reconstruction here makes no literature-priority claim.

The owner is distinct from C288, which treats one isolated point interaction and its scattering/resolvent data; C308, a non-Hermitian Hatano--Nelson lattice; C318, a dimerized finite-range SSH bulk--edge chain; and C323, a finite complete-graph oracle Hamiltonian. Here the object is an infinite self-adjoint continuum delta comb and its Bloch-band atlas.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ The physical Hamiltonian is a source-native natural quantization. But the real parameters $a,g$, repeated cells, transfer determinant, and Bloch phase contain no rational-prime payload, arithmetic primitive-orbit ledger, Euler product, target divisor, functional equation, or target-zero match. The transfer determinant is not an Euler factor, and $H_{a,g}$ is not claimed to be a Hilbert--Pólya operator. Route A is rejected and Route B remains locked.

9 R. de L. Kronig and W. G. Penney, "Quantum mechanics of electrons in crystal lattices," *Proceedings of the Royal Society A* **130** (1931), 499--513. [doi:10.1098/rspa.1931.0019](https://doi.org/10.1098/rspa.1931.0019).

S. Albeverio, F. Gesztesy, R. Høegh-Krohn, and H. Holden, *Solvable Models in Quantum Mechanics*, second edition, AMS Chelsea, 2005. [doi:10.1090/chel/350](https://doi.org/10.1090/chel/350).

R. O. Hryniv and Ya. V. Mykytyuk, "Schrödinger operators with periodic singular potentials," 2001. [arXiv:math/0109129](https://arxiv.org/abs/math/0109129).
