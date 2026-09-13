---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-370-fold-compatible-ulam-spike-barrier"
canonical_tex: "zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/main.pdf"
source_sha256: "f1fa2b7890d67b86e0dd5716b9a9259264afec1c836bdb6d601dff19e9b05689"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fold-compatible Ulam quotients and the deterministic spike barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-370-fold-compatible-ulam-spike-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We audit the first continuation left open by RH-367 for the postcritically finite quadratic map $f(x)=1-u x^2$, where $u^3-2u^2+2u-2=0$ and $J=[-(u-1),1]$. Folding by $q(x)=|x|$ gives $T(y)=|1-u y^2|$ on $[0,1]$. For partitions that are genuinely compatible with this fold, the exact full cell-overlap matrix has a folded quotient and an annihilated mirror kernel; its characteristic polynomial is $z^m$ times the folded characteristic polynomial. Conditional expectations also give a real $L^1$ approximation and exterior resolvent convergence on $|z|>1$. These facts do not produce a Riesz contour around $-1$. Indeed, on the natural bounded-variation strong space the deterministic projection of the terminal square-root spike has an adjacent-cell jump $(2-\sqrt2)/\sqrt{u h}$, so its strong norm grows as $h^{-1/2}$. The positive strong-space bridge therefore remains a scoped negative. The exact finite quotient, the exterior weak bridge, and the spike obstruction form a standalone theorem edge. No continuum spectral limit, prime trace, Hilbert--Polya operator, or proof of RH is claimed.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: 'Fold-compatible Ulam quotients and the deterministic spike barrier'
```

## Markdown 正文

# Scope and frozen source

The source package fixes the real root $$u=1.543689012692076\ldots,\qquad u^3-2u^2+2u-2=0,
 \qquad r=u-1,$$ and the invariant interval and map $$J=[-r,1],\qquad f(x)=1-u x^2.
 \label{eq:map}$$ The postcritical relations are $f(0)=1$, $f(1)=-r$, $f(-r)=r$, and $f(r)=r$. The RH-367 source proves the two-band exchange $$\mathcal B_0=[-r,r],\qquad \mathcal B_1=[r,1],
 \qquad f(\mathcal B_0)=\mathcal B_1,\quad f(\mathcal B_1)=\mathcal B_0.
 \label{eq:bands}$$

Put $q(x)=|x|$. The factor map and its folded representative are $$q\circ f=T\circ q,\qquad T(y)=|1-u y^2|,\qquad 0\leq y\leq1.
 \label{eq:fold}$$ The source locks used by the executable artifact are the cyclic-Ulam source and RH-367 [@cycliculam2026; @rh3672026], together with RH-14, RH-52, RH-55, and the frozen four-volume verification [@rh14; @rh52; @rh55]. The hashes and commits are recorded in `results/result.json`. In particular, the finite matrices below are not reconstructed from a numerical eigensolver.

RH-367 proves a finite aligned sign mode. It does not identify that mode with an isolated continuum eigenvalue. RH-14 and RH-52 work on a declared tower/spike space, while RH-52 and RH-55 use a positive-noise schedule. This paper keeps the deterministic endpoint, the folded quotient, and the noisy results separate.

# Exact fold-compatible finite quotients

Let $\mathcal C=\{C_i\}$ be an interval partition of $[0,1]$ with $r$ as a cell boundary. Refine it, when needed, at the turning point and inverse branch breakpoints. A partition $\mathcal D=\{D_a\}$ of $J$ is *mirror-compatible* if every cell $C_i\subset[0,r]$ has the two cells $C_i^-= -C_i$ and $C_i^+=C_i$ in $\mathcal D$, while cells in $[r,1]$ have only their positive copy. Let $P_I$ and $P_J$ be the row-stochastic exact cell-overlap matrices for $T$ and $f$ respectively: $$(P_I)_{ij}=\frac{\operatorname{Leb}(C_i\cap T^{-1}C_j)}{\operatorname{Leb}(C_i)},\qquad
 (P_J)_{ab}=\frac{\operatorname{Leb}(D_a\cap f^{-1}D_b)}{\operatorname{Leb}(D_a)}.
 \label{eq:ulam}$$

Let $m_0$ be the number of paired cells and $m_1$ the number of unpaired terminal cells. Pullback of a folded observable by $q$ is denoted by $J_h$; pushforward of a density by $q$ (with the cell-length normalization) is denoted by $A_h$. These maps are dual under the cellwise Lebesgue pairing.

[\[thm:quotient\]]{#thm:quotient label="thm:quotient"} For every mirror-compatible partition, $$P_JJ_h=J_hP_I,\qquad A_hP_J^{\mathsf T}=P_I^{\mathsf T}A_h,
 \qquad A_hJ_h=I.
 \label{eq:intertwining}$$ Moreover, $$P_J^{\mathsf T}\ker A_h=\{0\},\qquad \dim\ker A_h=m_0,
 \label{eq:kernel}$$ and $$\det(zI-P_J)=z^{m_0}\det(zI-P_I).
 \label{eq:charfactor}$$ Thus the two matrices have exactly the same nonzero spectrum, algebraic multiplicities, and Jordan blocks at every nonzero eigenvalue. The zero eigenspace is enlarged by the mirror kernel and is not identified further.

For a cellwise constant $g$ on the folded partition, $g(q(f(x)))=g(T(q(x)))$. Integrating this identity over each mirror pair gives the first relation in [\[eq:intertwining\]](#eq:intertwining){reference-type="eqref" reference="eq:intertwining"}. The second relation is its adjoint under the cellwise Lebesgue pairing; the factor of two on a paired cell is exactly the pushforward multiplicity and is absorbed in $A_h$. A density whose two mirror values are opposite pushes forward to zero. Since $f(-x)=f(x)$, the two inverse-branch contributions of such a density cancel in the next transfer step. This proves $P_J^{\mathsf T}\ker A_h=0$. Choose a complement on which $A_h$ is an isomorphism. In the resulting basis the transpose has a zero block of dimension $m_0$ and the induced quotient block $P_I^{\mathsf T}$, up to an inessential triangular off-diagonal block. The determinant factorization [\[eq:charfactor\]](#eq:charfactor){reference-type="eqref" reference="eq:charfactor"} follows, and the Jordan assertion follows from the same block form.

If an aligned folded matrix has an exact eigenvalue $-1$, every mirror-compatible full matrix has that nonzero eigenvalue as well. The extra mirror degrees of freedom contribute only zero eigenvalues. This statement does not apply to an aligned partition whose cells are not mirror pairs.

# The genuine weak bridge outside the unit circle

Let $E_h$ be conditional expectation onto the folded cell partition, with mesh $h\to0$, and let $\mathcal P_T$ be the Perron--Frobenius operator of $T$ on $L^1([0,1])$. It is positive and $L^1$-contractive.

[\[prop:l1\]]{#prop:l1 label="prop:l1"} For every fixed $g\in L^1([0,1])$, $$\widehat P_hg:=E_h\mathcal P_TE_hg\longrightarrow\mathcal P_Tg
 \quad\text{in }L^1.
 \label{eq:l1bridge}$$ If $K$ is compact in $\{z:|z|>1\}$, then $$(zI-\widehat P_h)^{-1}g\longrightarrow(zI-\mathcal P_T)^{-1}g
 \label{eq:resbridge}$$ uniformly for $z\in K$, and $$\sup_{h\,\text{small}}\sup_{z\in K}
 \|(zI-\widehat P_h)^{-1}\|_{1\to1}
 \leq \sup_{z\in K}\frac1{|z|-1}.
 \label{eq:resbound}$$

Conditional expectations converge strongly to the identity in $L^1$ and are contractive. Hence $$\|E_h\mathcal P_TE_hg-\mathcal P_Tg\|_1
 \leq \|E_h(g)-g\|_1+\|(E_h-I)\mathcal P_Tg\|_1\to0.$$ Both $\mathcal P_T$ and $\widehat P_h$ are Markov contractions. For $|z|>1$ their resolvents are the norm-convergent Neumann series $z^{-1}\sum_{n\ge0}z^{-n}P^n$. The contraction bound gives [\[eq:resbound\]](#eq:resbound){reference-type="eqref" reference="eq:resbound"}; termwise convergence, followed by a uniform geometric tail bound on a compact $K$, gives [\[eq:resbridge\]](#eq:resbridge){reference-type="eqref" reference="eq:resbridge"}.

The eigenvalue of interest is $-1$, on the boundary of the domain in Proposition [\[prop:l1\]](#prop:l1){reference-type="ref" reference="prop:l1"}. The proposition supplies neither a common strong space nor a contour resolvent around $-1$. It is therefore not a Riesz-projector convergence theorem.

# The terminal deterministic spike

On the terminal band $r<y<1$, the folded map has one admissible inverse branch $x=((1-y)/u)^{1/2}$. Consequently $$(\mathcal P_T\mathbf1)(y)=\frac{1}{2\sqrt u}\,(1-y)^{-1/2},
 \qquad r<y<1.
 \label{eq:spike}$$

Consider a uniform terminal pair of cells $C_1=[1-h,1]$ and $C_2=[1-2h,1-h]$. Their cell averages of the right side of [\[eq:spike\]](#eq:spike){reference-type="eqref" reference="eq:spike"} are $$a_1=\frac{1}{\sqrt{u h}},\qquad
 a_2=\frac{\sqrt2-1}{\sqrt{u h}}.
 \label{eq:averages}$$

[\[thm:spike\]]{#thm:spike label="thm:spike"} The step function $E_h\mathcal P_T\mathbf1$ has a jump between the two terminal cells of size $$|a_1-a_2|=\frac{2-\sqrt2}{\sqrt{u h}}.
 \label{eq:jump}$$ In particular, for the standard norm $\|v\|_{\operatorname{BV}}=\|v\|_1+\operatorname{Var}(v)$, $$\|E_h\mathcal P_T\|_{\operatorname{BV}\to\operatorname{BV}}
 \geq \|E_h\mathcal P_T\mathbf1\|_{\operatorname{BV}}
 \geq \frac{2-\sqrt2}{\sqrt{u h}}.
 \label{eq:bvblowup}$$ The coefficient is $0.4714757998\ldots$.

Integrating $(1-y)^{-1/2}/(2\sqrt u)$ over $C_1$ and $C_2$ gives [\[eq:averages\]](#eq:averages){reference-type="eqref" reference="eq:averages"}. The variation of a step function includes the absolute value of every adjacent-cell jump, which proves [\[eq:jump\]](#eq:jump){reference-type="eqref" reference="eq:jump"}. Since $E_h\mathbf1=\mathbf1$, applying the operator to the unit BV function gives [\[eq:bvblowup\]](#eq:bvblowup){reference-type="eqref" reference="eq:bvblowup"}.

The bound rules out a uniform deterministic entry on this standard BV component. RH-14's tower/spike language records additional singular atoms, and a future mesh-dependent fractional space could in principle absorb the cell profile. No such space, uniform projector estimate, or contour around $-1$ is present in the frozen sources. The theorem is therefore a precise scoped negative, not an impossibility theorem for every conceivable Banach space.

# Why the positive-noise bridge cannot be specialized

The strong--weak results in RH-52 and RH-55 use a joint schedule of mesh and positive noise, with a condition of the form $h=o(\sigma^2)$. The estimate [\[eq:bvblowup\]](#eq:bvblowup){reference-type="eqref" reference="eq:bvblowup"} is a deterministic $\sigma=0$ statement. Substituting $\sigma=0$ into a hypothesis that requires a positive-noise smoothing scale is invalid; it removes precisely the smoothing that controls the terminal spike. Thus the following implications are not licensed: $$\begin{aligned}
 \text{finite aligned }-1\text{ mode}
 &\not\Rightarrow \text{continuum isolated }-1,\\
 \text{positive-noise contour}
 &\not\Rightarrow \text{deterministic contour}.\end{aligned}$$

For a merely band-aligned partition with one crossing cell, the quotient maps in Theorem [\[thm:quotient\]](#thm:quotient){reference-type="ref" reference="thm:quotient"} are not defined. The phase-dependent leakage identity of RH-367 remains a finite local identity, and phase scans do not repair either the missing mirror quotient or the BV bound.

# Executable audit

The artifact uses exact rational matrices. A folded cyclic test matrix is extended by two mirror rows per paired cell. The four audit sizes have $(m_0,m_1)=(2,1),(3,2),(4,3),(5,4)$; in every row the observable intertwiner and the mirror-kernel image are exactly zero, and the exact characteristic polynomial is the folded polynomial multiplied by the stated power of $z$. The spike rows check that $h^{1/2}$ times the jump is constant to floating tolerance. These are finite reproduction checks, not spectral limit evidence.

  check                         count     status
  ---------------------------- ------- ------------
  source-lock files               9        pass
  mirror quotient dimensions      4        pass
  spike scaling rows              4        pass
  named Gates A--E                5     false/open

  : Finite audit ledger (generated from `result.json`).

# Route verdict and Gate ledger

-   Route A is `GO`: Theorems [\[thm:quotient\]](#thm:quotient){reference-type="ref" reference="thm:quotient"} and [\[thm:spike\]](#thm:spike){reference-type="ref" reference="thm:spike"}, together with Proposition [\[prop:l1\]](#prop:l1){reference-type="ref" reference="prop:l1"}, are a new, independently typed quotient/weak-bridge/scoped-negative package.

-   Route B is `STOP_SCOPED`: the quotient is restricted to mirror-compatible finite partitions, the $L^1$ bridge is exterior to the unit circle, and the natural deterministic strong norm has no uniform bound at the terminal spike.

The five project Gates remain false/open. In particular, this paper does not construct a canonical intrinsic dynamical spectral determinant, a scattering completion, a self-adjoint generator, a von-Mangoldt weighted trace, or an equality with the completed-zeta divisor. It does not identify Riemann zeros, construct a Hilbert--Polya operator, or prove the Riemann Hypothesis.

# Conclusion

The fold supplies an exact algebraic reduction for a strict cofinal subclass of the RH-367 discretizations. It also supplies a genuine exterior weak resolvent statement. The terminal square-root singularity then pays for a sharp deterministic obstruction to the natural strong-space route. The remaining opening is explicit: a new fractional/tower-adapted strong space, or a theorem for non-mirror partitions, would be needed before a contour around $-1$ can be discussed.
