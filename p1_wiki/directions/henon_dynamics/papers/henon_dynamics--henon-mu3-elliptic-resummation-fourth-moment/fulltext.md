---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-elliptic-resummation-fourth-moment"
canonical_tex: "henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/paper/main.pdf"
source_sha256: "bd17a9754208ef6a01b490b0bb528e7934c98a0bc1ee7fa6b95c00ad60519996"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Elliptic Resummation and a Fivefold Fourth Moment for a Fourier--Cubic Hénon Euler Germ

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_elliptic_resummation_fourth_moment/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the Galois-normalized Euler germ attached to the split-prime Fourier--cubic quantization of an area-preserving Hénon kernel. Earlier work reached absolute convergence in $\operatorname{Re}s>1/4$, where the second chronological moment and the untreated fourth-moment tail met. We remove both obstructions without changing the prime clock or averaging the chronology. First, three explicit automorphisms of the genus-four cyclic cubic curve governing the second moment generate a $K$-rational subgroup $C_2\times S_3$, where $K=\mathbf Q(\sqrt{-3})$. Rational idempotents give $\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2$. This yields the exact integer-power extraction $$\exp(-\ell_2(s)/2)
   =\zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s),$$ with $H_2$ holomorphic and nonzero for $\operatorname{Re}s>0$. Modularity over $K$ continues the elliptic factors, with zeros allowed. Second, the ordered eight-step phase is stratified by a cubic sixfold, a split quadric, and a $(2,3)$ fivefold. An exact Gröbner certificate proves smoothness over $K$; $p=181$ is an explicit bad reduction. Primitive ranks $86$ and $168$, together with Deligne purity, imply $c_{p,4}=O(p^{-1/2})$. Consequently the original Euler germ continues holomorphically to $\operatorname{Re}s>1/5$ and admits a tenth-order graded regularized determinant in the normalized semifinite category. The corresponding classical Schatten order is $15$. No full functional equation, Riemann divisor, or self-adjoint Hilbert--Pólya operator is claimed.
author:
- Hénon Zeta Research Program
bibliography:
- references.bib
date: 14 August 2026
title: |
  Elliptic Resummation and a Fivefold Fourth Moment\
  for a Fourier--Cubic Hénon Euler Germ
```

## Markdown 正文

# Introduction {#sec:introduction}

The Hilbert--Pólya heuristic asks whether the ordinates of the nontrivial zeros of the Riemann zeta function arise from a natural spectral problem. A dynamical version seeks a source-defined orbit or transfer operator whose determinant has sufficiently rigid global analytic structure. This paper addresses a more modest, falsifiable gate in one arithmetic Hénon program: how far can its canonical normalized Euler germ be continued using structure already present in its chronological moments?

The object is not built by matching zeta zeros. Split rational primes index finite-field fibres of one fixed Fourier--cubic Hénon kernel, each prime retains the clock $\log p$, and Galois traces are divided by the real cyclotomic degree $d_p=(p-1)/2$. The resulting local logarithm has coefficients $c_{p,n}$, where $n$ is a genuine chronological repetition. Previous stages proved a normalized-semifinite determinant and identified the second and third moments with a genus-four curve and a Fano threefold, respectively. They left $$\operatorname{Re}s=\frac14$$ as a paired obstruction: the Weil-sized second moment met the first generic term of the untreated tail, $n=4$.

There is no reason for a pointwise improvement $a_p=o(\sqrt p)$ in the genus-four trace, and an attempt to force one would contradict the expected nondegenerate distribution of elliptic traces. The correct move is instead to recognize the complete second logarithm as a standard global factor. At the same time, the fourth moment must be computed from its eight ordered variables; replacing it by an averaged transition matrix would destroy precisely the endpoint and closing phase information that produces its arithmetic geometry.

## Main advances

The paper proves four linked statements.

1.  The C48 curve carries three explicit $K$-rational automorphisms generating an order-$12$ subgroup $C_2\times S_3$. Its differential representation is $\operatorname{Std}_+\oplus\operatorname{Std}_-$, and rational group-algebra idempotents yield $$\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2.$$

2.  The complete second counterterm, including its sign and split-prime multiplicity, is $$F_2(s)=\zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s).$$ The residual $H_2$ is holomorphic and nonzero in $\operatorname{Re}s>0$. Caraiani--Newton modularity continues the two elliptic factors [@CaraianiNewton2025]; standard automorphic theory supplies their completed functional equations [@GodementJacquet1972 Global Theory, pp. 136--184]. This statement does not extend a functional equation to $H_2$ or to the full Hénon product.

3.  The fourth chronological moment is controlled by a cubic sixfold and a smooth $(2,3)$ fivefold. Their primitive middle ranks are $86$ and $168$, which imply $c_{p,4}=O(p^{-1/2})$ at good split primes. A characteristic-zero Gröbner calculation proves the required cofinite smoothness statement; an explicit singular fibre at $p=181$ rules out an all-split strengthening.

4.  After extracting $F_2$, the untreated tail begins at $n=5$. The same source-defined Euler germ therefore has a canonical holomorphic continuation to $\operatorname{Re}s>1/5$, with zeros allowed, and an exact $\operatorname{Det}_{10,\tau,\mathrm{gr}}$ representation.

## Prior-art boundary {#sec:prior-firewall}

The group-algebra mechanism is classical [@KaniRosen1989]. Cyclic trigonal genus-four strata were classified by Izquierdo--Ying [@IzquierdoYing2009], and Moonen classified the positive-dimensional special families of cyclic covers [@Moonen2010]. Jiménez exhibited several completely decomposable trigonal Jacobians; in particular, two genus-four rows in her §5.1 and Theorem 3 table decompose into four elliptic curves [@Jimenez2016]. None of these sources identifies the present equation, its $K$-descent, or its Hénon logarithm. We claim novelty only for that explicit source-locked bridge and the analytic consequence obtained by combining it with the fourth moment.

The cohomological estimates use Deligne's purity theorem [@Deligne1974 Théorème 1.6] and weak Lefschetz [@SGA2 Exposé XIV, Corollaire 4.6]. Classical regularized determinants are discussed by Simon [@Simon2005 Chapter 9], but our trace is a field-degree-normalized faithful semifinite trace. We distinguish that category from the ordinary Hilbert trace throughout.

## Organization

freezes the dynamical object and states the main theorem. proves the $K$-rational Jacobian decomposition. extracts and continues the second counterterm. derives the fourth-moment geometry and Weil bound. proves the fifth-abscissa continuation and tenth-order determinant identity. gives a Route-A audit, and [8](#app:certificates){reference-type="ref" reference="app:certificates"} records exact symbolic certificates.

# Frozen source and main theorem {#sec:source}

Let $$K=\mathbf Q(\rho)=\mathbf Q(\sqrt{-3}),\qquad \rho^2+\rho+1=0.$$ For every rational prime $p>3$ with $p\equiv1\pmod3$, let $$d_p=[\mathbf Q(\zeta_p)^+:\mathbf Q]=\frac{p-1}{2}.$$ We retain the split-prime clock $z_p=p^{-s}$ and the normalized chronological moments $$c_{p,n}=\frac{C_{p,n}}{d_p}.$$ The local normalized logarithm is $$\log G_p(z)=-\sum_{n\ge1}\frac{c_{p,n}}{n}z^n,$$ where the branch is the source germ at $z=0$. The global source germ is $$\mathcal G(s)=\prod_{p\equiv1(3)}G_p(p^{-s}).                 \tag{2.1}$$ The chronological phases, Galois trace, and normalization are frozen before the present analysis. In particular, neither an averaged transition matrix nor a critical shift enters (2.1).

The second moment is governed by the smooth projective genus-four curve $$C:\quad y^3=f(x),\qquad
 f(x)=-\frac{x(\rho^2x-1)}{\rho(x^3+1)}.                \tag{2.2}$$ At a good split prime put $$a_p=p+1-\#C(\mathbf F_p).$$ The two reductions induced by $\rho$ and $\rho^{-1}$ are isomorphic and have the same trace. The inherited exact formula is $$c_{p,2}=-\frac{28+4a_p}{p-1}.                         \tag{2.3}$$

The new fourth-moment phase is $$\Phi_{p,4}(x_0,\ldots,x_7)
 =2\sum_{i=0}^7x_i^3+\sum_{i=0}^6x_ix_{i+1}
   +\rho x_7x_0.                                       \tag{2.4}$$ It is important that the closing edge remains $\rho x_7x_0$. Let $Z_{p,4}=\#\Phi_{p,4}^{-1}(0)$ and $$C_{p,4}=2p^{-3}Z_{p,4}-2p^4,\qquad
 c_{p,4}=\frac{2C_{p,4}}{p-1}.                         \tag{2.5}$$

[\[thm:main\]]{#thm:main label="thm:main"} For the frozen Hénon Euler germ $\mathcal G$, the following hold.

1.  The automorphisms in [\[prop:automorphisms\]](#prop:automorphisms){reference-type="ref" reference="prop:automorphisms"} generate a $K$-rational subgroup $G\simeq C_2\times S_3$, and there are elliptic curves $E_\pm/K$ such that $$\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2.                      \tag{2.6}$$

2.  If $$\ell_2(s)=\sum_{p\equiv1(3)}c_{p,2}p^{-2s},\qquad
     F_2(s)=\exp(-\ell_2(s)/2),$$ then a holomorphic nonvanishing $H_2$ on $\operatorname{Re}s>0$ satisfies $$F_2(s)=\zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s)          \tag{2.7}$$ initially on $\operatorname{Re}s>1/4$, and the right-hand side continues $F_2$ holomorphically to $\operatorname{Re}s>0$. This continuation may vanish.

3.  Outside a finite set of split primes, $$C_{p,4}=-2-\frac{2A_p}{p^3}-\frac{2B_p}{p^2},          \tag{2.8}$$ where $$|A_p|\le86p^3,\qquad |B_p|\le168p^{5/2}.$$ Consequently, $$|c_{p,4}|
     \le\frac{348+672\sqrt p}{p-1}=O(p^{-1/2}).             \tag{2.9}$$

4.  The germ (2.1) has a canonical holomorphic continuation $$\mathcal G^{\mathrm{cont}}(s)\quad\text{to}\quad
     \operatorname{Re}s>\frac15.                                    \tag{2.10}$$ It is represented there by the normalized-semifinite graded determinant in [\[thm:det10\]](#thm:det10){reference-type="ref" reference="thm:det10"}. The continuation is not asserted to be nonvanishing.

[\[rem:scope\]]{#rem:scope label="rem:scope"} The theorem does not identify rational primes with primitive periodic orbits of one real Hénon map. It gives no completion or functional equation for $\mathcal G^{\mathrm{cont}}$, no Riemann--von Mangoldt law, no Riemann-zero divisor, and no self-adjoint Hilbert--Pólya operator.

# A $K$-rational elliptic decomposition {#sec:elliptic}

The divisor of $f$ in (2.2) has simple zeros at $$0,\ \rho,\ \infty$$ and simple poles at $$-1,\ -\rho,\ -\rho^2.$$ Riemann--Hurwitz for the cyclic cubic cover gives $g(C)=4$. The symmetry of these two triples is larger than the deck group.

[\[prop:automorphisms\]]{#prop:automorphisms label="prop:automorphisms"} Put $$\begin{aligned}
 \delta(x,y)&=(x,\rho y),\\
 \iota(x,y)&=\left(\frac{\rho^2}{x},-y\right),\\
 T(x)&=-\frac{\rho^2(x+1)}{x+\rho^2},\qquad
 h=\frac{\rho-1}{3},\\
 \jmath(x,y)&=\left(T(x),\frac{h}{y}\right).
\end{aligned}                                           \tag{3.1}$$ These maps extend to $K$-rational automorphisms of $C$, and $$\begin{gathered}
 \delta^3=\iota^2=\jmath^2=1,\qquad
 [\iota,\delta]=[\iota,\jmath]=1,\\
 \jmath\delta\jmath=\delta^{-1}.
\end{gathered}                                          \tag{3.2}$$ They generate a subgroup $G\simeq C_2\times S_3$.

Reduction in $K(x)$, using $\rho^2+\rho+1=0$, gives $$\begin{aligned}
 f(\rho^2/x)&=-f(x),&
 T(T(x))&=x,\\
 f(T(x))f(x)&=h^3,&
 T(\rho^2/x)&=\rho^2/T(x).
\end{aligned}                                           \tag{3.3}$$ The first identity validates $\iota$; the middle two validate $\jmath$; and the last gives $[\iota,\jmath]=1$. The remaining relations follow directly. Thus $\langle\delta,\jmath\rangle\simeq S_3$. Its induced base maps are the identity and $T$, whereas $\iota$ induces $x\mapsto\rho^2/x$, which is distinct from both. Since $\iota$ is central, the generated subgroup has order $12$ and the stated product structure. This argument proves a subgroup statement; it does not determine the full automorphism group of $C$.

[\[lem:differentials\]]{#lem:differentials label="lem:differentials"} As a $C_2\times S_3$-representation, $$H^0(C,\Omega_C^1)\simeq\operatorname{Std}_+\oplus\operatorname{Std}_-.             \tag{3.4}$$

The quotient $C/\langle\delta\rangle$ is the $x$-line. Hence $$H^0(C,\Omega_C^1)^{\langle\delta\rangle}=0.            \tag{3.5}$$ The fixed base points of $x\mapsto\rho^2/x$ are $x=\rho$ and $x=-\rho$. They are, respectively, a zero branch and a pole branch of $f$, and each has a unique point above it. Thus $\iota$ has exactly two fixed points. Riemann--Hurwitz gives $$2g(C)-2=2\bigl(2g(C/\iota)-2\bigr)+2,
 \qquad g(C/\iota)=2.                                  \tag{3.6}$$

The trivial and sign representations of $S_3$ both have a nonzero $C_3$-fixed vector, whereas its rational two-dimensional standard representation does not. Since (3.5) holds and the differential space has dimension four, it is a sum of two standard representations. Its $\iota$-invariant subspace has dimension $g(C/\iota)=2$, so one standard block has positive central sign and the other has negative sign.

[\[thm:jac-decomposition\]]{#thm:jac-decomposition label="thm:jac-decomposition"} There are elliptic curves $E_+,E_-$ over $K$ for which $$\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2.                       \tag{3.7}$$

In $\mathbf Q[G]$, define $$\begin{aligned}
 e_{\mathrm{std}}
 &=1-\frac{1+\delta+\delta^2}{3},\\
 e_\pm&=\frac{1\pm\iota}{2},\\
 q_\pm&=e_\pm e_{\mathrm{std}}\frac{1+\jmath}{2}.
\end{aligned}                                           \tag{3.8}$$ The first two factors select the standard block and its central sign. Inside that block, which is $M_2(\mathbf Q)$, the last factor is a primitive rank-one idempotent. If $N$ clears denominators, put $$E_\pm=\operatorname{im}\!\left(Nq_\pm:\operatorname{Jac}(C)\longrightarrow\operatorname{Jac}(C)\right)^0.
                                                                  \tag{3.9}$$ By [\[lem:differentials\]](#lem:differentials){reference-type="ref" reference="lem:differentials"}, $q_\pm$ acts with rank one on differentials, so $E_\pm$ is elliptic. Primitive idempotents in $M_2(\mathbf Q)$ are equivalent. The off-diagonal matrix units, after clearing denominators, give mutually inverse $K$-quasi-isogenies between the two primitive images in each block. Each central standard block is therefore isogenous to $E_\pm^2$, proving (3.7). The construction is over $K$ because every automorphism in (3.1) is.

[\[rem:isogeny-boundary\]]{#rem:isogeny-boundary label="rem:isogeny-boundary"} Equation (3.7) is an unpolarized $K$-isogeny statement. It is not an isomorphism of principally polarized abelian varieties, and the labels $+$ and $-$ depend on the proved central involution.

Kani--Rosen provide the general idempotent-to-isogeny mechanism [@KaniRosen1989 Theorem A]. Jiménez's [@Jimenez2016 §5.1 and Theorem 3] table contains genus-four reduced-$D_3$ and reduced-$D_6$ rows whose Jacobians decompose into four elliptic curves, with kernel order $9$. The listed full groups are $D_3\times D_3$ and $(C_3\times C_3)\rtimes D_4$, not a determination made here. Our proof establishes only the subgroup in [\[prop:automorphisms\]](#prop:automorphisms){reference-type="ref" reference="prop:automorphisms"}; it neither identifies the C48 equation with those families nor computes $\operatorname{Aut}(C)$.

The monodromy datum of (2.2) is $(3,6,(1,1,1,2,2,2))$. It is absent from Moonen's list of positive-dimensional special families [@Moonen2010 §3.4, Table 1 and Theorem 3.6]. This does not obstruct extra endomorphisms at an individual fibre, but it prevents us from claiming a generic special or CM family.

# Exact resummation of the second logarithm {#sec:resummation}

The second moment (2.3) is too large for absolute convergence on every $\operatorname{Re}s>1/5$: the Weil bound gives only $a_p=O(\sqrt p)$. The elliptic decomposition permits an exact global resummation instead of a nonexistent pointwise improvement.

For $u\in\mathbf C$, use the cohomological convention $$L(H^1(C/K),u)=
 \prod_{\mathfrak p}
 \det\!\left(
 1-\operatorname{Frob}_{\mathfrak p}\operatorname{N}\mathfrak p^{-u}
 \mid H^1(C_{\overline K},\mathbf Q_\ell)
 \right)^{-1}.                                         \tag{4.1}$$ The finitely many bad factors use their standard inertia-invariant definition. Set $$\ell_2(s)=\sum_{p\equiv1(3)}c_{p,2}p^{-2s},
 \qquad F_2(s)=\exp\!\left(-\frac{\ell_2(s)}2\right)     \tag{4.2}$$ on $\operatorname{Re}s>1/4$.

[\[thm:second-extraction\]]{#thm:second-extraction label="thm:second-extraction"} There is a canonical holomorphic nonvanishing function $H_2$ on $\operatorname{Re}s>0$ such that $$F_2(s)=
 \zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s)                 \tag{4.3}$$ on $\operatorname{Re}s>1/4$. The right-hand side continues $F_2$ holomorphically to $\operatorname{Re}s>0$, but need not be nonvanishing there.

Put $u=2s+1$. Equation (2.3) gives $$\begin{aligned}
 \log F_2(s)
 &=\sum_{p\ {\rm split}}
   \frac{14+2a_p}{p-1}p^{-2s}\\
 &=\sum_{p\ {\rm split}}(14+2a_p)p^{-u}
   +R_{\mathrm{den}}(s).
\end{aligned}                                           \tag{4.4}$$ where $$R_{\mathrm{den}}(s)
 =\sum_{p\ {\rm split}}(14+2a_p)p^{-u}
   \sum_{j\ge1}p^{-j}.                                 \tag{4.5}$$ Every split rational prime gives two degree-one prime ideals of $K$. The first logarithmic coefficient of $\zeta_K(u)^7$ is therefore $14$. The reductions of $C$ at the two primes are isomorphic, so the first coefficient of $L(H^1(C/K),u)$ is $2a_p$. The sign and powers in (4.3) are consequently forced.

On the common absolute-convergence half-plane, define $$\log H_2(s)=
 \log F_2(s)-7\log\zeta_K(u)-\log L(H^1(C/K),u).
                                                               \tag{4.6}$$ We verify that the right side converges locally absolutely for $\operatorname{Re}u>1$. Since $g(C)=4$, $$|a_p|\le8\sqrt p.$$ The extra factor $p^{-1}$ in (4.5) makes the denominator correction summable. At a split prime, an $m$-th curve Euler term is $$O\!\left(p^{m/2}p^{-m\operatorname{Re}u}\right);$$ the terms $m\ge2$ are summable for $\operatorname{Re}u>1$. At an inert rational prime, $\operatorname{N}\mathfrak p=p^2$, and the first curve term is $$O\!\left(p^{1-2\operatorname{Re}u}\right),$$ with the same threshold. Higher zeta powers are smaller, while ramified and bad primes form a finite set. Thus (4.6) defines a holomorphic logarithm, and $H_2=\exp(\log H_2)$ is holomorphic and nonzero on $\operatorname{Re}s>0$.

By [\[thm:jac-decomposition\]](#thm:jac-decomposition){reference-type="ref" reference="thm:jac-decomposition"} and isogeny invariance, $$L(H^1(C/K),u)=L(E_+/K,u)^2L(E_-/K,u)^2.                \tag{4.7}$$ Caraiani--Newton's theorem applies to all elliptic curves over $K=\mathbf Q(\sqrt{-3})$ [@CaraianiNewton2025 Theorem 1.1 and the examples immediately following it]. Hence both elliptic $L$-functions are entire. Since $\zeta_K(u)$ is holomorphic for $\operatorname{Re}u>1$, equation (4.3) gives the asserted holomorphic continuation. The elliptic factors may vanish, so the continued product is not zero-free.

[\[rem:fe-firewall\]]{#rem:fe-firewall label="rem:fe-firewall"} The modular elliptic factors possess standard automorphic completions and functional equations [@GodementJacquet1972 Global Theory]. Neither the residual $H_2$ nor the remaining chronological product is identified with an automorphic $L$-function. We therefore do not multiply their individual Gamma factors into a conjectural completion of the Hénon object.

The original $\operatorname{Log}_0$ is also not continued through zeros. Equation (4.3) continues its exponential $F_2$, which is the single-valued object needed below.

# The ordered fourth moment {#sec:fourth}

Write $$\mathcal C(x)=\sum_{i=0}^7x_i^3,\qquad
 \mathcal Q(x)=\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0.             \tag{5.1}$$ In $\mathbf P^7$ define $$S=V(\mathcal C),\qquad Q=V(\mathcal Q),\qquad X=S\cap Q.             \tag{5.2}$$ Thus $S$ and $Q$ are sixfolds and $X$ is a fivefold when smooth.

## Projective directions

[\[prop:direction\]]{#prop:direction label="prop:direction"} For every split $p>3$, $$Z_{p,4}
 =1+\#\mathbf P^7(\mathbf F_p)-\#S(\mathbf F_p)-\#Q(\mathbf F_p)+p\#X(\mathbf F_p).          \tag{5.3}$$

For a nonzero projective direction $v$ and $\lambda\in\mathbf F_p^\times$, $$\Phi_{p,4}(\lambda v)
 =\lambda^2\bigl(2\lambda\mathcal C(v)+\mathcal Q(v)\bigr).           \tag{5.4}$$ If both $\mathcal C(v)$ and $\mathcal Q(v)$ are nonzero, there is one nonzero radial root. If exactly one vanishes, there are none. If both vanish, all $p-1$ nonzero radii are roots. Inclusion--exclusion over projective directions, followed by the affine origin, gives (5.3). No chronological variable has been permuted or averaged.

Let the even coordinates be $e=(x_0,x_2,x_4,x_6)^t$ and the odd coordinates $o=(x_1,x_3,x_5,x_7)^t$. Then $$\mathcal Q=e^tM_\rho o,\qquad
 M_\rho=
 \begin{pmatrix}
 1&0&0&\rho\\
 1&1&0&0\\
 0&1&1&0\\
 0&0&1&1
 \end{pmatrix},
 \qquad\det M_\rho=1-\rho\ne0.                          \tag{5.5}$$ Both coordinate four-planes are maximal totally isotropic subspaces, so $Q$ is the split smooth six-dimensional quadric. Therefore $$\#Q(\mathbf F_p)=P_6(p)+p^3,\qquad
 P_m(p)=1+p+\cdots+p^m.                                \tag{5.6}$$

## Smoothness and its exact scope

[\[prop:smoothness\]]{#prop:smoothness label="prop:smoothness"} The characteristic-zero fivefold $X/K$ is smooth. Consequently, its integral model is smooth outside a finite set $\Sigma_4$ of prime ideals. The qualifier is necessary: the split reduction at $(p,\rho)=(181,48)$ is singular.

At a projective singular point, the nondegeneracy of $\mathcal Q$ permits the gradient dependence to be written $$\nabla\mathcal C=\lambda\nabla\mathcal Q,\qquad \lambda\ne0.$$ After scaling every coordinate by $3/\lambda$, and renaming the coordinates, one obtains $$\begin{aligned}
 x_0^2&=x_1+\rho x_7,\\
 x_i^2&=x_{i-1}+x_{i+1}\quad(1\le i\le6),\\
 x_7^2&=x_6+\rho x_0.
\end{aligned}                                           \tag{5.7}$$ Multiplication by $x_i$ and summation gives $$\mathcal C(x)=2\mathcal Q(x).                                       \tag{5.8}$$ The exact reduced Gröbner basis of (5.7), $\mathcal Q=0$, and $\rho^2+\rho+1=0$, in the degree-reverse-lexicographic order specified in [8](#app:certificates){reference-type="ref" reference="app:certificates"}, is $$x_7,x_6,x_5,x_4,x_3,x_2,x_1,x_0,\rho^2+\rho+1.        \tag{5.9}$$ Hence the affine origin is the only recurrence solution over either characteristic-zero embedding, and no projective singular point exists. Only now do we invoke openness of smoothness to obtain the finite bad set.

For the negative control, $48^2+48+1=0$ in $\mathbf F_p$ at $p=181$, and $$v=(9,158,158,9,104,128,171,153)                       \tag{5.10}$$ satisfies all equations (5.7), as well as $$\mathcal C(v)=\mathcal Q(v)=0\quad\text{in }\mathbf F_{181}.$$ It is nonzero and therefore defines a projective singular point.

## Middle cohomology and the exact trace formula

For a cubic sixfold, $$c(TS)=\frac{(1+H)^8}{1+3H}.$$ The coefficient of $H^6$ is $31$; since $\deg S=3$, $$\chi(S)=93,\qquad b_6(S)=87,\qquad
 b_6^{\mathrm{prim}}(S)=86.                            \tag{5.11}$$ For the smooth $(2,3)$ fivefold, $$c(TX)=\frac{(1+H)^8}{(1+2H)(1+3H)}.$$ The coefficient of $H^5$ is $-27$; since $\deg X=6$, $$\chi(X)=-162=6-b_5(X),\qquad b_5(X)=168.               \tag{5.12}$$ Weak Lefschetz supplies the six nonmiddle even Tate classes in each ledger [@SGA2 Exposé XIV, Corollaire 4.6].

At a good split prime define $A_p,B_p$ by $$\#S(\mathbf F_p)=P_6(p)+A_p,\qquad
 \#X(\mathbf F_p)=P_5(p)-B_p.                                  \tag{5.13}$$ Here $A_p$ is the trace on primitive $H^6(S)$, and $B_p$ is the trace on $H^5(X)$. Deligne purity [@Deligne1974 Théorème 1.6] gives $$|A_p|\le86p^3,\qquad |B_p|\le168p^{5/2}.               \tag{5.14}$$

[\[prop:fourth-formula\]]{#prop:fourth-formula label="prop:fourth-formula"} At every good split prime, $$Z_{p,4}=p^7-p^3-A_p-pB_p,                             \tag{5.15}$$ $$C_{p,4}=-2-\frac{2A_p}{p^3}-\frac{2B_p}{p^2},         \tag{5.16}$$ and $$|c_{p,4}|\le
 \frac{348+672\sqrt p}{p-1}=O(p^{-1/2}).               \tag{5.17}$$

Substitute (5.6) and (5.13) into (5.3). The ambient Tate terms cancel: $$\begin{aligned}
 Z_{p,4}
 &=1+P_7-(P_6+A_p)-(P_6+p^3)+p(P_5-B_p)\\
 &=p^7-p^3-A_p-pB_p.
\end{aligned}$$ Equation (5.16) follows from the frozen normalization (2.5). Finally, (5.14) yields $$|C_{p,4}|\le174+336\sqrt p,$$ and division by $d_p=(p-1)/2$ gives (5.17).

The square-root gain is created only after the exact Tate cancellation and field-degree normalization. It is not an unnormalized bound for the eight-step trace. The finite bad set changes finitely many Euler factors and hence does not change an abscissa.

# Fifth-abscissa continuation and operator realization {#sec:continuation}

We now combine a global resummation at $n=2$ with absolute estimates at all other repetitions. The inherited coefficients satisfy $$c_{p,1}=-\frac{12}{p-1},\qquad
 c_{p,3}=O(p^{-1/2}),\qquad
 |c_{p,n}|\le4\cdot4^n.                                \tag{6.1}$$ The third estimate is uniform in $p,n$; for finitely many small primes it is replaced by the sharper local unitary-block bound when summing over $n$.

[\[lem:normal-convergence\]]{#lem:normal-convergence label="lem:normal-convergence"} After the $n=2$ term is replaced by $F_2^{\mathrm{cont}}$, the remaining logarithmic series converges locally normally on $\operatorname{Re}s>1/5$.

The $n=1$ series converges for $\operatorname{Re}s>0$. The inherited third moment converges absolutely when $$3\operatorname{Re}s+\frac12>1,$$ that is, for $\operatorname{Re}s>1/6$. By (5.17), the fourth moment converges for $\operatorname{Re}s>1/8$.

Fix a compact set in $\operatorname{Re}s\ge\sigma_0>1/5$. For sufficiently large $p$, arrange $4p^{-\sigma_0}\le1/2$. The $n\ge5$ contribution is then bounded by a constant multiple of $$\sum_p p^{-5\sigma_0}<\infty.                         \tag{6.2}$$ For the finitely many omitted primes, the local Hénon blocks are unitary, so $|c_{p,n}|\le\tau_p(I)$; because $p^{-\sigma_0}<1$, each remaining local logarithmic tail is geometric. This proves local normal convergence.

[\[thm:continuation\]]{#thm:continuation label="thm:continuation"} The source germ $\mathcal G(s)$ has a unique holomorphic continuation $$\mathcal G^{\mathrm{cont}}(s)
 \quad\text{to}\quad \operatorname{Re}s>\frac15.                 \tag{6.3}$$ It can have zeros, and no continuation through $\operatorname{Re}s=1/5$ is asserted.

On the original common half-plane, separate the $n=2$ logarithm: $$\mathcal G(s)=F_2(s)
 \exp\!\left(
 -\sum_{p\equiv1(3)}
  \sum_{\substack{n\ge1\\n\ne2}}
  \frac{c_{p,n}}n p^{-ns}
 \right).                                               \tag{6.4}$$ Replace $F_2$ by the continuation in [\[thm:second-extraction\]](#thm:second-extraction){reference-type="ref" reference="thm:second-extraction"}. The remaining exponential is holomorphic and nonzero on $\operatorname{Re}s>1/5$ by [\[lem:normal-convergence\]](#lem:normal-convergence){reference-type="ref" reference="lem:normal-convergence"}. Equality on the original half-plane and the identity theorem make the continuation canonical. Any zeros come from the continued second factor.

## Normalized semifinite determinant

We recall the operator typing because it is essential to the claim. The local source construction provides finite-dimensional unitary graded blocks $W_p$ whose normalized graded traces reproduce $c_{p,n}$. On their product von Neumann algebra $\mathcal M$, the faithful semifinite trace $\tau$ contains the factor $d_p^{-1}$. For $$X_s=\bigoplus_{p\equiv1(3)}p^{-s}W_p,$$ the inherited exact ideal ledger is $$\tau(|X_s|^q)
 =\sum_{p\equiv1(3)}\frac{8p+4}{3}p^{-q\operatorname{Re}s},
 \qquad
 X_s\in L^q(\mathcal M,\tau)
 \Longleftrightarrow q\operatorname{Re}s>2.                     \tag{6.5}$$

For $n\ne2$, put $$\ell_n(s)=\sum_{p\equiv1(3)}c_{p,n}p^{-ns}.$$ The analytic graded regularized determinant is normalized so that $$\log\operatorname{Det}_{10,\tau,\mathrm{gr}}(I-X_s)
 =-\sum_{n\ge10}\frac{\ell_n(s)}n.                     \tag{6.6}$$ Regularized-determinant background in the classical trace-ideal category may be found in [@Simon2005 Chapter 9]; equation (6.6) uses the specified semifinite trace rather than the ordinary Hilbert trace.

[\[thm:det10\]]{#thm:det10 label="thm:det10"} On $\operatorname{Re}s>1/5$, $$\boxed{
 \mathcal G^{\mathrm{cont}}(s)
 =F_2^{\mathrm{cont}}(s)
  \exp\!\left(
  -\sum_{\substack{1\le n\le9\\n\ne2}}
  \frac{\ell_n(s)}n
  \right)
  \operatorname{Det}_{10,\tau,\mathrm{gr}}(I-X_s).}                  \tag{6.7}$$ The order $10$ is the least fixed normalized-semifinite integer order valid on the entire half-plane.

If $\operatorname{Re}s>1/5$, then $10\operatorname{Re}s>2$, so (6.5) gives $X_s\in L^{10}(\mathcal M,\tau)$. Order $9$ fails arbitrarily close to the boundary. Expanding (6.6), restoring powers $1,\dots,9$ other than $n=2$, and inserting the exact continued factor $\exp(-\ell_2/2)=F_2^{\mathrm{cont}}$ gives (6.7).

[\[prop:classical\]]{#prop:classical label="prop:classical"} On the underlying ordinary Hilbert direct sum, $$X_s\in S^q(\mathcal H)\Longleftrightarrow q\operatorname{Re}s>3.       \tag{6.8}$$ Thus the least fixed classical Schatten order valid throughout $\operatorname{Re}s>1/5$ is $15$, not $10$. Its local trace records the ordinary Galois norm rather than the degree-normalized local root.

Removing the factor $d_p^{-1}\asymp p^{-1}$ from the local trace changes the summand in (6.5) from order $p^{1-q\sigma}$ to $p^{2-q\sigma}$. Prime summability is therefore equivalent to $q\sigma>3$. Since $15\sigma>3$ for every $\sigma>1/5$, while order $14$ fails near the boundary, the stated minimum follows. The same missing normalization multiplies the local graded logarithm by $d_p$, which is precisely the ordinary Galois norm.

Neither (6.7) nor (6.8) is an ordinary Fredholm determinant statement on $\operatorname{Re}s>1/5$. The unregularized normalized-semifinite trace-class domain is $\operatorname{Re}s>2$, and the ordinary Hilbert trace-class domain is $\operatorname{Re}s>3$. The cancellations retained by the graded trace are part of the source object, not an estimate for $|X_s|$.

# Route-A evaluation and next gate {#sec:route-a}

Route A asks whether a source-defined dynamical object acquires a credible dynamical determinant and global analytic structure before any attempt at a Hilbert--Pólya operator. The present result is an analytic advance, but it does not close that route.

  Layer   Verdict                Evidence and obstruction
  ------- ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A1      Weak                   Four-, six-, and eight-step phases retain exact chronology and complex weights. Primes are arithmetic fibres, not primitive cycles of one real map.
  A2      Analytic determinant   The normalized Euler germ has an exact $\tau$-regularized determinant and continues to $\operatorname{Re}s>1/5$. It is not classical Fredholm and may vanish.
  A3      Partial structure      Holomorphic continuation to $\operatorname{Re}s>1/5$ is proved. Only the extracted elliptic factors have standard completed functional equations; the complete Hénon object does not.
  A4      Natural quantization   The same unitary finite-place blocks and normalized Galois trace define the operator realization. No self-adjoint global generator is constructed.

In the evaluator's exact vocabulary, the tuple is $$\begin{gathered}
(\mathrm{A1\_WEAK},\ \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\
\mathrm{A4\_NATURAL\_QUANTIZATION}).
\end{gathered}$$ The overall status is $$\mathrm{ROUTE\_A\_EXPLORATORY}.$$ Route B is not authorized.

## What the continuation does and does not mean

The new half-plane is not obtained by dropping difficult local factors. The second moment is preserved as a full $K$-Euler object, including split, inert, higher-power, and bad-prime corrections. The fourth moment keeps the ordered closing edge and isolates its finite bad set. These are positive structural features.

On the other hand, (6.3) is a domain theorem, not a divisor theorem. There is no demonstrated symmetry $s\leftrightarrow1-s$ for the whole product, no Gamma factor, no pole-removal prescription, and no Riemann--von Mangoldt count. The extracted elliptic zeros are arithmetic data of $E_\pm$, not evidence that the zeros of $\mathcal G^{\mathrm{cont}}$ match the Riemann zeros.

## The next large gate

The next decisive question is global:

> Can the elliptic completions extracted at $n=2$ and the higher cohomological moment factors be assembled into one coherent completion that preserves the split-prime clock and chronological normalization?

A positive answer would require a source-derived residual completion for $H_2$ and compatible higher moments, with explicit Gamma factors and a functional equation. A proof that their weights, centers, or local monodromies are incompatible would be an equally useful obstruction. Computing a fifth moment without such a target would only move a local wall and is therefore a lower priority.

# Declarations and limitations {#declarations-and-limitations .unnumbered}

## Data and code availability {#data-and-code-availability .unnumbered}

The source equations, theorem packages, exact producer, independent checker, mutation tests, finite-field validation ledgers, and compiled manuscript are released together in the repository directory *henon\_dynamics/henon\_mu3\_elliptic\_resummation\_fourth\_moment*. The theorem does not depend on proprietary data, a Riemann-zero table, or floating-point fitting. Exact finite ledgers are controls; the all-prime claims rest on the displayed proofs and machine-replayable certificates.

## Ethics statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, personal data, animals, clinical intervention, or biological material. Ethics approval and informed consent were therefore not applicable.

## Author contributions (CRediT) {#author-contributions-credit .unnumbered}

The Hénon Zeta Research Program performed conceptualization, methodology, formal analysis, software, validation, investigation, data curation, visualization of exact ledgers, and writing of the original draft and revisions. Claim promotion followed independent producer/checker replay and source-audit rules.

## Funding {#funding .unnumbered}

No external funding was reported for this study.

## Conflict of interest {#conflict-of-interest .unnumbered}

The authoring research program reports no financial or nonfinancial conflict of interest.

## AI-use statement {#ai-use-statement .unnumbered}

AI systems were used for mathematical exploration, symbolic and finite-field code generation, adversarial review, primary-source triage, and manuscript drafting. AI output was not accepted as proof by itself. Every released theorem-level computational claim is backed by exact arithmetic, a replayable certificate, or a cited primary theorem, and the claim boundaries were independently red-teamed. No AI system is listed as a human author.

## Limitations {#limitations .unnumbered}

The construction has four principal limitations. First, split primes index arithmetic fibres rather than primitive orbits of one classical Hénon system. Second, the continuation in $\operatorname{Re}s>1/5$ may have zeros and has no proved full functional equation or Gamma factor. Third, the regularized determinant belongs to a normalized faithful semifinite graded category; it is not a classical Fredholm determinant on the claimed half-plane. Fourth, no self-adjoint operator, Riemann divisor, or zero-counting law is obtained. The explicit bad reduction at $p=181$ also shows that good-fibre formulas must retain a finite exceptional set.

# Exact symbolic and finite controls {#app:certificates}

## Characteristic-zero smoothness transcript

The coefficient-one recurrence used in [\[prop:smoothness\]](#prop:smoothness){reference-type="ref" reference="prop:smoothness"} is replayed by the following complete Singular input. The coefficient field is represented by adjoining $r^2+r+1$; the `dp` order is Singular's degree-reverse-lexicographic family.

    ring R=0,(x0,x1,x2,x3,x4,x5,x6,x7,r),dp;
    option(redSB);
    poly Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+x5*x6
           +x6*x7+r*x7*x0;
    ideal I=x0^2-x1-r*x7,
            x1^2-x0-x2,
            x2^2-x1-x3,
            x3^2-x2-x4,
            x4^2-x3-x5,
            x5^2-x4-x6,
            x6^2-x5-x7,
            x7^2-x6-r*x0,
            Q,
            r^2+r+1;
    std(I);

With Singular 4.2.1 and the reduced-standard-basis option, the exact output is

    _[1]=x7
    _[2]=x6
    _[3]=x5
    _[4]=x4
    _[5]=x3
    _[6]=x2
    _[7]=x1
    _[8]=x0
    _[9]=r^2+r+1

No numerical tolerance or finite-prime extrapolation enters this certificate.

## Bad-reduction control

For $p=181$, $r=48$, one has $$r^2+r+1\equiv0\pmod{181}.$$ At $$v=(9,158,158,9,104,128,171,153)$$ the eight recurrence residuals are $$(0,0,0,0,0,0,0,0)\quad\text{in }\mathbf F_{181},$$ and direct substitution gives $$\mathcal Q(v)=\mathcal C(v)=0.$$ This negative control is theorem-bearing: it refutes all-split smoothness. It does not contaminate the separate C48 curve factor.

## Chern coefficients

The two Euler-characteristic inputs can be checked without a classification table: $$[H^6]\frac{(1+H)^8}{1+3H}=31,\qquad
 [H^5]\frac{(1+H)^8}{(1+2H)(1+3H)}=-27.                \tag{A.1}$$ Multiplication by the degrees $3$ and $6$, followed by weak Lefschetz, gives $$\chi(S)=93,\quad b_6^{\mathrm{prim}}(S)=93-6-1=86,$$ $$\chi(X)=-162,\quad b_5(X)=6-(-162)=168.$$

## Finite factorization validation

Finite controls are separated from the representation-theoretic proof. For four split primes, exact extension-field counts reconstruct the full degree-eight genus-four numerator by Newton identities:

    $p$   $\#C(\mathbf F_p)$   $\#C(\mathbf F_{p^2})$   $\#C(\mathbf F_{p^3})$   $\#C(\mathbf F_{p^4})$   $(a_+,a_-)$
  ----- -------------------- ------------------------ ------------------------ ------------------------ -------------
      7                   12                       66                      372                     2586      $(-4,2)$
     13                   18                      270                     2046                    27414     $(-1,-1)$
     19                   24                      474                     6744                   129930      $(-4,2)$
     31                   24                     1050                    29640                   926970      $(-4,8)$

In each row the reconstructed numerator equals $$(1-a_+T+pT^2)^2(1-a_-T+pT^2)^2.$$ An additional 21-prime degree-one ledger validates the trace splitting. These ledgers confirm signs and normalizations; they do not replace [\[thm:jac-decomposition\]](#thm:jac-decomposition){reference-type="ref" reference="thm:jac-decomposition"}.
