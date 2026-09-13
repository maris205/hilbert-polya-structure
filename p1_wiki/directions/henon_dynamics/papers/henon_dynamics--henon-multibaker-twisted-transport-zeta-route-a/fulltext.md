---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-multibaker-twisted-transport-zeta-route-a"
canonical_tex: "henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a/paper/main.pdf"
source_sha256: "cd970881039ef2239c8399dd3fae3de63049c95db3d37701a03bdbb5794518c6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Reversible Multibaker Transport: A Complete Boundary-Aware Primitive Orbit Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_multibaker_twisted_transport_zeta_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a complete source-system theorem for the reversible multibaker on a finite ring, with a domain convention that resolves the binary endpoint ambiguity. On the invariant set of non-dyadic coordinates, every geometric periodic point is reconstructed from a mixed binary word. A primitive necklace of length $d$ and displacement $S$ lifts to $\gcd(L,S)$ cycles of least period $dL/\gcd(L,S)$, with exact winding, reversal and reciprocal stability multipliers. \>0 The finite tilted transport determinant has a Chebyshev formula. Its weighted primitive product contains two homogeneous symbolic cycles absent from the geometric domain; removing them gives an explicit all-order correction. We distinguish inverse-unstable weights from two-dimensional flat-trace weights. \>1 We derive the diffusion constant, exact odd-ring relaxation and the even-ring period-two obstruction, including the one- and two-cell degeneracies. Independent exact and symbolic checks audit the formulas. These source results provide no target arithmetic or target-zero correspondence.
author:
- 'HCS-C379 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  Reversible Multibaker Transport:\
  A Complete Boundary-Aware Primitive Orbit Atlas
- |
  Reversible Multibaker Transport:\
  Primitive Orbits and the Corrected Twisted Zeta
- |
  Reversible Multibaker Transport:\
  Boundary-Corrected Zeta, Diffusion, and Parity-Sensitive Relaxation
```

## Markdown 正文

**Keywords:** multibaker map; primitive orbit; winding cocycle; boundary coding; twisted determinant; deterministic diffusion.

chinese-simplified

中文摘要

本文在明确排除二进制边界的不变满测集上，建立有限环可逆多面包师映射 的完整原始周期轨道分类。每个几何周期点由混合二进制词唯一重建；长度 和位移决定提升后的最小周期、轨道条数、整数环绕数、反演配对及互为 倒数的稳定乘子。 \>0 有限维扭转输运行列式具有切比雪夫闭式。它的符号周期乘积含有两条不在 几何定义域中的齐次边界轨道；精确去除这两项得到全阶校正公式，并明确 区分不稳定乘子的逆权重与二维平坦迹权重。 \>1 进一步得到扩散常数、奇数环的精确松弛率、偶数环的二周期阻碍，以及 单格和双格退化情形。独立精确程序与符号计算核对公式。这些源系统定理 不构成目标算术结构或目标零点对应。

关键词：多面包师映射；原始轨道；环绕余循环；边界编码；扭转行列式；确定性扩散。

# The phase space and the endpoint problem

The classical multibaker is a deterministic area-preserving realization of nearest-neighbor diffusion; the model and its transport interpretation are established in the literature [@gaspard; @wojcik]. The present contribution is an explicitly normalized proof and independent computational audit. We claim no priority for the classical diffusion mechanism. The point requiring particular care is that symbolic completeness and geometric completeness depend on the chosen boundary convention.

Let $\mathcal D$ denote the dyadic rationals in $[0,1]$, let $X=\{x\in(0,1):x\notin\mathcal D\}$, and set $$M_L=(\mathbb Z/L\mathbb Z)\times X\times X,\qquad L\geq1.$$ For $s=\lfloor2x\rfloor$ define $d_s=2s-1$ and $$\label{eq:map}
B(j,x,y)=(j+d_s\bmod L,\ 2x-s,\ (y+s)/2).$$ Both cell length and time step equal one. Normalized cell counting measure times Lebesgue area gives an invariant probability measure on $M_L$. Removing dyadic coordinates removes a null set; it does affect the exact periodic-orbit convention, which is why it is stated before any census.

On a half-open unit square the all-one periodic code reconstructs the excluded point $(1,1)$. Keeping that code while using a single-valued half-open baker therefore overcounts a geometric orbit. Our symmetric non-dyadic domain excludes both homogeneous codes and retains every mixed periodic code. This makes the reversal exact on the stated domain.

[\[lem:code\]]{#lem:code label="lem:code"} The map $B$ is bijectively conjugate to the two-sided binary shift with cell cocycle $d_s$, restricted to sequences whose two tails are not eventually constant. It preserves area on each branch. The involution $I(j,x,y)=(j,1-y,1-x)$ satisfies $IBI=B^{-1}$ and reverses the area form.

Use the unique expansions $x=.s_0s_1\cdots$ and $y=.s_{-1}s_{-2}\cdots$. Formula [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} shifts the symbolic sequence and adds $d_{s_0}$ to the cell. Non-dyadic expansions are unique and neither tail is eventually constant, so this coding and its inverse are defined without endpoint identifications. With $t=\lfloor2y\rfloor$ one computes $$B^{-1}(j,x,y)=(j-d_t,\ (x+t)/2,\ 2y-t).$$ Since $y\neq1/2$, the first symbol of $1-y$ is $1-t$; substitution proves $IBI=B^{-1}$. The derivative on each branch is $\operatorname{diag}(2,1/2)$, while $I^*(\,\mathrm dx\wedge\,\mathrm dy)=-\,\mathrm dx\wedge\,\mathrm dy$. The images of the two branches partition the full-measure domain, establishing measure preservation as well as the local Jacobian statement.

# All geometric periods, powers and winding

For a word $w=s_0\cdots s_{n-1}$, write $a(w)$ for its binary integer, $w^{\rm rev}$ for its reversal, and $S(w)=\sum_t(2s_t-1)$. A mixed word contains both symbols. A necklace is a word modulo cyclic rotation; it is primitive when its least word period equals its length.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Every length-$n$ mixed word satisfying $L\mid S(w)$ gives, for each cell $j$, exactly one point fixed by $B^n$, with $$\label{eq:coords}
x=\frac{a(w)}{2^n-1},\qquad y=\frac{a(w^{\rm rev})}{2^n-1}.$$ These are all fixed points. A primitive mixed necklace of length $d$ and displacement $S$ lifts to exactly $g=\gcd(L,S)$ geometric cycles, each with $$\label{eq:lift}
q=dL/g,\qquad W=S/g.$$ Here $q$ is the least geometric period, $W$ is winding, and $\gcd(L,0)=L$. Its $r$-fold repetition has time $rq$, winding $rW$, multipliers $2^{rq},2^{-rq}$ and phase $\mathrm e^{\mathrm ir\phi W}$.

Affine iteration gives $x_n=2^nx-a(w)$ and $y_n=2^{-n}y+2^{-n}a(w^{\rm rev})$. The fixed equations force [\[eq:coords\]](#eq:coords){reference-type="eqref" reference="eq:coords"}. For mixed $w$, the resulting fractions lie strictly between zero and one and have odd reduced denominators greater than one. They are non-dyadic, and their periodic expansions realize the specified word. The cell closes precisely when $L\mid S(w)$. Conversely every periodic point has periodic coding by Lemma [\[lem:code\]](#lem:code){reference-type="ref" reference="lem:code"}; the two homogeneous words would give corners outside the domain.

For a primitive necklace, the internal coordinates first return after $d$ steps. At that time the cell translates by $S$. The order of this translation is $h=L/g$, so the first full return occurs at $q=dh$. There are $Ld$ choices of cell and word phase; partition into cycles of length $dh$ gives $g$ distinct cycles. The total displacement is $hS$, yielding $W=hS/L=S/g$. Each derivative is diagonal, giving the stated powers and positive multipliers. No division by a reversal pairing has been made.

The involution sends a cycle to the complement of its reversed word, up to rotation. It sends $S,W$ to $-S,-W$ and keeps $q$ and multiplicity fixed. Self-reversing cycles are allowed. The distinction between word period and geometric period is substantial: the primitive word $001$ has $d=3$ and $S=-1$, so on an $L$-cell ring it gives one cycle of period $3L$, not $L$ cycles of period three. The word $01$ has $S=0$, and gives $L$ cycles of period two.

For every $L,n\geq1$, $$\label{eq:census}
F_{L,n}=L\left(\sum_{\substack{0\leq k\leq n\\L\mid(2k-n)}}
\binom nk-2\mathbf1_{L\mid n}\right).$$ The number of geometric primitive cycles of period $q$ is $q^{-1}\sum_{r\mid q}\mu(r)F_{L,q/r}$.

A length-$n$ word with $k$ ones has displacement $2k-n$ and there are $\binom nk$ such words. Each closing word permits all $L$ cells. The two homogeneous words close precisely when $L\mid n$ and must be subtracted. Every period-$n$ fixed point belongs to one unique primitive cycle whose period divides $n$; Möbius inversion gives the last assertion.

\>0

# The tilted transport determinant and geometric correction

For real $\phi$, define the finite backward transport operator $$\label{eq:transport}
(P_\phi f)_j=\tfrac12\mathrm e^{\mathrm i\phi/L}f_{j+1}
             +\tfrac12\mathrm e^{-\mathrm i\phi/L}f_{j-1}.$$ The two labelled transitions are added when their destination cells coincide. In particular, this definition does not discard either channel for $L=1,2$. We consider $D_L(z,\phi)=\det(I-zP_\phi)$. This is a finite source transport determinant with a specified observable space.

[\[thm:det\]]{#thm:det label="thm:det"} The full spectrum, with algebraic multiplicities, is $$\lambda_k(\phi)=\cos\frac{2\pi k+\phi}{L},\qquad0\leq k<L.$$ Writing $T_L$ for the Chebyshev polynomial, $$\label{eq:cheb}
D_L(z,\phi)=2^{1-L}z^L\bigl(T_L(1/z)-\cos\phi\bigr)
=\prod_{k=0}^{L-1}(1-z\lambda_k(\phi)).$$ The displayed Laurent expression is understood after cancellation as a polynomial. For every $n\geq1$, $$\label{eq:trace}
\operatorname{tr}P_\phi^n=L2^{-n}\sum_{\substack{w\in\{0,1\}^n\\L\mid S(w)}}
\mathrm e^{\mathrm i\phi S(w)/L}.$$

Fourier vectors $f_j=\mathrm e^{2\pi\mathrm ikj/L}$ diagonalize [\[eq:transport\]](#eq:transport){reference-type="eqref" reference="eq:transport"}, giving the spectrum. For generic $\phi$, these are distinct roots of $T_L(t)-\cos\phi$, since $T_L(\cos\theta)=\cos L\theta$. The leading coefficient is $2^{L-1}$, including $L=1$. Equality of the polynomials for generic $\phi$ extends by continuity to every real twist, including multiple roots. Substitution $t=1/z$ proves [\[eq:cheb\]](#eq:cheb){reference-type="eqref" reference="eq:cheb"}. Expanding the matrix power as labelled steps proves [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}: diagonal entries require cell closure, and the accumulated phase is $\mathrm e^{\mathrm i\phi S/L}$, not $\mathrm e^{\mathrm i\phi S}$.

Eigenvalues equal to zero do not produce finite determinant roots. Each nonzero eigenvalue contributes $z=1/\lambda_k$ with its multiplicity, so the formula also specifies every degree drop and every source root count. Replacing $\phi$ by $\phi+2\pi$ permutes the eigenvalue list.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} Let $p$ run over the geometric primitive cycles of Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}. For real $\phi$ and $|z|<1$, the absolutely convergent product is $$\label{eq:zeta}
\prod_p\left(1-(z/2)^{q_p}\mathrm e^{\mathrm i\phi W_p}\right)^{-1}
=\frac{(1-(z/2)^L\mathrm e^{\mathrm i\phi})(1-(z/2)^L\mathrm e^{-\mathrm i\phi})}
{D_L(z,\phi)}.$$ The quotient gives its rational continuation, retaining cancellations.

Since $|\operatorname{tr}P_\phi^n|\leq L$, the series $\sum_{n\geq1}z^n\operatorname{tr}P_\phi^n/n$ converges absolutely for $|z|<1$ and equals $-\log D_L$. Group each closed labelled walk by its unique primitive cycle and repetition. This yields the reciprocal Euler product over symbolic lattice cycles, with inverse-unstable weight $2^{-q}$ and phase $\mathrm e^{\mathrm i\phi W}$. Its only non-geometric cycles are the all-zero and all-one cycles. Each has least lattice period $L$, and their windings are $-1,+1$. Multiplying by the two corresponding factors removes them, proving [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. They remain distinct labelled cycles even for $L=1,2$. Alternatively the bound $F_{L,n}\leq L2^n$ controls the geometric logarithmic series directly. Both arguments justify regrouping without any cancellation being replaced by an absolute weight.

There is an additional weight boundary. The inverse unstable multiplier is $2^{-n}$, but the two-dimensional fixed-point denominator is $$\label{eq:flat}
|\det(I-DB^n)|=(2^n-1)^2/2^n.$$ Its inverse is different. The finite transport determinant therefore has not been proved to be a Fredholm determinant of the full phase-space Perron operator. Neither an infinite-dimensional trace-class claim nor a target divisor is licensed by [\[eq:cheb\]](#eq:cheb){reference-type="eqref" reference="eq:cheb"}.

\>1

# Hydrodynamic branch and exact ring relaxation

[\[thm:diffusion\]]{#thm:diffusion label="thm:diffusion"} On the integer-cell lift with invariant internal Lebesgue data, the displacement $X_n$ obeys $$\mathbb E X_n=0,\qquad \operatorname{Var}X_n=n,\qquad
\mathbb E\mathrm e^{tX_n}=(\cosh t)^n,\qquad D=\tfrac12.$$ The spatial Bloch branch is $\lambda(\kappa)=\cos\kappa$, and near zero $$\log\lambda(\kappa)=-\kappa^2/2-\kappa^4/12+O(\kappa^6).$$ For odd $L\geq3$, the exact norm of $P_0^n$ on mean-zero cell observables is $\cos(\pi/L)^n$. For even $L\geq2$, the eigenvalue $-1$ prevents convergence to the uniform cell distribution at every integer time. For even $L\geq4$, the two-step norm after removing both constant and parity modes is $\cos^2(2\pi/L)$.

A prescribed future word of length $n$ is an interval of width $2^{-n}$ in $x$, so future symbols are independent fair bits under the invariant measure. The increments $2s_t-1$ are independent, centered and have variance one. Multiplication of their moment-generating functions gives $(\cosh t)^n$, and the diffusion convention is $D=\lim_n\operatorname{Var}(X_n)/(2n)$. The Fourier characteristic function is $(\cos\kappa)^n$; Taylor expansion gives the displayed local logarithm. The ring branch near zero twist is $\cos(\phi/L)$, consistently using wave number $\kappa=\phi/L$.

At zero twist $P_0$ is real symmetric with eigenvalues $\cos(2\pi k/L)$. For odd $L$, the largest absolute value outside $k=0$ is $\cos(\pi/L)$; the spectral theorem makes the norm equality exact. For even $L$, the mode $k=L/2$ is $(-1)^j$ and has eigenvalue $-1$. After removing $k=0,L/2$, the largest squared eigenvalue is $\cos^2(2\pi/L)$. Squaring the operator restricts motion to parity classes, giving the asserted two-step relaxation factor on the mean-zero subspace of each parity class. No probabilistic approximation is involved.

## One cell, two cells, and the lazy control

For $L=1$, $P_\phi=[\cos\phi]$ and $D_1=1-z\cos\phi$. The untilted cell chain has only one invariant mode, so a nontrivial relaxation gap is not defined. Its internal baker dynamics is still nontrivial: $F_{1,1}=0$, $F_{1,2}=2$, and the primitive cycle $01$ survives. For $L=2$, both labelled transitions reach the other cell and add to $\cos(\phi/2)$; hence $$D_2=1-z^2\cos^2(\phi/2).$$ The untilted chain alternates deterministically, with eigenvalues $1,-1$. Each parity class is a singleton, so there is no remaining parity-class relaxation mode. These facts do not remove either homogeneous symbolic cycle from the correction in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The usual nonabsolute gap for $L\geq3$ is $1-\cos(2\pi/L)$, which differs from the odd-ring absolute gap. As a separate control, the lazy matrix $Q=(I+P_0)/2$ has eigenvalues $\cos^2(\pi k/L)$ and gap $\sin^2(\pi/L)$ for every $L\geq2$. This is an explicitly changed transport process. It is not used to hide the original even-ring obstruction.

# Independent evidence and limits of the Route-A claim

The all-period statements are proved above. The finite evidence contains 96 fixed-period rows, 188 winding-refined primitive rows, 2,296 necklace lift rows and 326 direct rational geometric witnesses. Fixed and primitive cutoffs are $n\leq12$, $L\leq8$; direct geometry uses $n\leq6$, $L\leq6$. The producer uses binomial counts and primitive-necklace enumeration. The checker independently uses signed-walk recursion, primitive-power inversion, direct inverse-map and reversal tests, and Newton/exponential series. It imports no producer code.

A third lane computes symbolic determinants of the actual tilted matrices, checks 18 exact identities, and tests 1,200 Fourier cells at 80 decimal digits with residual below $10^{-70}$. Two isolated working directories reproduce the evidence byte for byte. Twenty-four repaired-hash mathematical and metadata mutations and ten serialization attacks are rejected; three smoke tests audit endpoints, parity and code independence. Strict JSON and YAML reject ambiguous structure and type substitutions. No finite regression is presented as proof of an infinite orbit census.

The phase-space geometry supports a formal quantization clue: the branches are symplectic and $I$ is anti-symplectic. Quantum multibaker constructions have a primary literature owner [@wojcik]; this paper constructs no quantum operator or domain and claims no quantum orbit theorem. The integers $L$, word lengths and windings carry no intrinsic rational-prime data. The same identities hold for prime and composite ring sizes; parity governs the transport obstruction. Consequently the strict tuple is $$(A0_{\rm FAIL},A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},
 A4_{\rm FORMAL\_HINT}).$$ The source atlas and source determinant are fully proved, while target A1 arithmetic carrying and target A2--A3 requirements remain unmet. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; all target-claim flags and Route B are false.

# Conclusion and revision record

Round zero establishes the complete boundary-aware geometric orbit atlas, including least periods after the cell lift, powers, winding and reversal. Its exact census uses only mixed codes on the stated invariant domain. Round one adds the twisted transport determinant, its complete source spectrum and the geometric correction for the two omitted homogeneous cycles. It also separates the transport weight from the full flat-trace denominator, closing the principal determinant-convention ambiguity. Round two adds the exact diffusion law, parity-sensitive relaxation theorem, one- and two-cell boundary cases, and the independent evidence audit. The resulting source theorem is complete under its declared domain and weight conventions. An arithmetic carrier would be a new research requirement, rather than a consequence of the transport identities.

9 P. Gaspard, What is the role of chaotic scattering in irreversible processes?, *Chaos* **3** (1993), 427--442. [doi:10.1063/1.165950](https://doi.org/10.1063/1.165950). D. K. Wójcik and J. R. Dorfman, Quantum multibaker maps: Extreme quantum regime, *Physical Review E* **66** (2002), 036110. [arXiv:cond-mat/0203494](https://arxiv.org/abs/cond-mat/0203494); [doi:10.1103/PhysRevE.66.036110](https://doi.org/10.1103/PhysRevE.66.036110).
