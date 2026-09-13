---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-genus4-second-moment"
canonical_tex: "henon_dynamics/henon_mu3_genus4_second_moment/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_genus4_second_moment/paper/main.pdf"
source_sha256: "560b77d5561549a695890f36d960e497862de0a63347cf3e3c59e6fc7a73c9cf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Genus-Four Second Moment for the Fourier--Cubic Hénon Kernel

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_genus4_second_moment>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_genus4_second_moment/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_genus4_second_moment/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_genus4_second_moment/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_genus4_second_moment/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We identify the Galois-normalized second chronological moment of a Fourier--cubic Hénon kernel with the Frobenius trace of an explicit smooth genus-four curve. Projective direction counting reduces the four-variable zero fibre to a $(2,3)$ complete intersection, which becomes a smooth $(3,3)$ divisor on a split quadric. If $a_p$ is its Frobenius trace, the descended moment is exactly $C_{p,2}=-14-2a_p$. The Weil bound supplies a square-root gain after field-degree normalization. It extends the associated Euler germ and its regularized graded operator determinant from $\operatorname{Re}s>1/2$ to $\operatorname{Re}s>1/3$; the operator formula now uses a sixth-order determinant relative to the normalized semifinite trace and five explicit chronological counterterms. This is not a classical Fredholm determinant on that half-plane: unregularized semifinite trace class begins at $\operatorname{Re}s>2$, and classical Hilbert trace class begins at $\operatorname{Re}s>3$ and encodes the ordinary Galois norm. No continuation, functional equation, or Riemann-divisor identification is claimed.
author:
- Hénon Zeta Research Program
bibliography:
- references.bib
date: 13 August 2026
title: 'A Genus-Four Second Moment for the Fourier--Cubic Hénon Kernel'
```

## Markdown 正文

# Introduction

The full Fourier--cubic quantization of the homogeneous area-preserving Hénon map produces exact finite-field trace moments. Pairing the additive character with its inverse and averaging over the maximal real cyclotomic field yields rational logarithmic moments $c_{p,n}$. Earlier work gives a normally convergent Euler germ on $\operatorname{Re}s>1/2$ and realizes it as a fourth-order regularized graded determinant relative to a normalized semifinite trace. That threshold comes from using a uniform bound for every $n\ge2$.

Here the second moment is evaluated geometrically. The main result is the following.

[\[thm:main\]]{#thm:main label="thm:main"} For every prime $p>3$, $p\equiv1\pmod3$, the second descended Hénon moment has the form $$C_{p,2}=-14-2a_p,
 \qquad |a_p|\le8\sqrt p,$$ where $a_p=p+1-\#X_\rho(\mathbf F_p)$ is the Frobenius trace of an explicit smooth genus-four curve. Consequently the normalized Euler germ is holomorphic and nonzero on $\operatorname{Re}s>1/3$, and on that half-plane $$\mathcal G(s)=
 \exp\!\left(-\sum_{n=1}^{5}\frac{\ell_n(s)}n\right)
 \operatorname{Det}_{6,\tau,\mathrm{gr}}(I-X_s).$$ Order six is the least fixed integer order in $L^q(\mathcal M,\tau)$ valid on the whole half-plane. More precisely, $$X_s\in L^q(\mathcal M,\tau)\iff q\operatorname{Re}s>2,
 \qquad
 X_s\in S^q(\mathcal H)\iff q\operatorname{Re}s>3.$$ Thus the unregularized $\tau$-associated determinant begins at $\operatorname{Re}s>2$, whereas the classical Fredholm domain begins at $\operatorname{Re}s>3$. The latter realizes the ordinary Galois norm, not the field-degree-normalized root $\mathcal G$.

The geometric facts used below are classical: the split Fermat-cubic count [@Massarenti2026 Cor. 8.3], split quadrics, adjunction on $\mathbf P^1\times\mathbf P^1$ [@Hartshorne1977 Ch. V, Prop. 1.5], and the Weil bound for curves [@Stichtenoth2009 Thm. 5.2.3]. The new content is the exact bridge from the frozen chronological Hénon phase to this curve and the resulting analytic abscissa. Regularized determinant background is recorded in [@Simon2005 Chapter 9].

# The chronological zero fibre

Fix an element $\rho\in\mathbf F_p^\times$ of order three. The four-step phase is $$\label{eq:phase}
 \Phi(x)=2\sum_{i=0}^{3}x_i^3+
 x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0.$$ Let $Z_p=\#\Phi^{-1}(0)$. The exact Galois trace normalization is $$\label{eq:moment}
 C_{p,2}=\frac{2Z_p}{p}-2p^2,
 \qquad c_{p,2}=\frac{2C_{p,2}}{p-1}.$$

Write $\mathcal C=\sum x_i^3$ and $\mathcal Q=x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0$, and denote by $S,R\subset\mathbf P^3$ their zero loci and by $X=S\cap R$.

[\[prop:direction\]]{#prop:direction label="prop:direction"} One has $$Z_p=1+\#\mathbf P^3(\mathbf F_p)-\#S(\mathbf F_p)-\#R(\mathbf F_p)+p\#X(\mathbf F_p).$$

For a projective direction (\[v\]), $$\Phi(\lambda v)=\lambda^2(2\lambda\mathcal C(v)+\mathcal Q(v)).$$ If neither homogeneous value vanishes there is one nonzero root. If exactly one vanishes there is none. If both vanish all $p-1$ nonzero scalars work. Adding the origin proves the formula.

Because $\mu_3\subset\mathbf F_p$, the Fermat cubic surface is split; its blow-up description gives $$\#S(\mathbf F_p)=\#\mathbf P^2(\mathbf F_p)+6p=p^2+7p+1.$$ See also [@Massarenti2026 Corollary 8.3]; since an odd prime congruent to one modulo three is congruent to one modulo six, its split case applies. The invertible change $y=x_1+\rho x_3,\ w=x_1+x_3$ turns $\mathcal Q$ into $x_0y+x_2w$. Hence $R$ is a split quadric, $R\simeq\mathbf P^1\times\mathbf P^1$, and $\#R=(p+1)^2$. Therefore $$\label{eq:zcount}
 Z_p=p^3-p^2-8p+p\#X(\mathbf F_p).$$

# The genus-four intersection

The construction is uniform over $\mathcal R=\mathbf Z[\rho,1/6]/(\rho^2+\rho+1)$. Since $N(\rho-1)=3$, the element $\rho-1$ is a unit in $\mathcal R$. With $y=x_1+\rho x_3$ and $w=x_1+x_3$, the standard Segre parametrization of $x_0y+x_2w=0$ is $$x_0=rt,\quad x_2=ru,\quad y=-su,\quad w=st.$$ Equivalently, $$x_0=rt,\quad x_2=ru,\quad
x_1=\frac{s(\rho t+u)}{\rho-1},\quad
x_3=-\frac{s(t+u)}{\rho-1}.$$ Using $(\rho-1)^2=-3\rho$, direct substitution gives the exact identity $\rho\mathcal C|_R=F$, where $$\label{eq:curve}
 X_\rho:\quad
 \rho r^3(t^3+u^3)+\rho^2s^3t^2u-s^3tu^2=0
 \quad\subset\mathbf P^1\times\mathbf P^1.$$

[\[prop:smooth\]]{#prop:smooth label="prop:smooth"} The curve $X_\rho$ is smooth and geometrically irreducible for every allowed $p$, and it has genus four.

Smoothness is proved uniformly in [6](#sec:smooth){reference-type="ref" reference="sec:smooth"}. Equation [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"} has bidegree $(3,3)$. Over an algebraic closure, suppose its components could be partitioned into nonzero effective divisors of bidegrees $(a,b)$ and $(3-a,3-b)$. Components of a smooth curve are disjoint, but their intersection number is $$a(3-b)+b(3-a)>0$$ for every nontrivial partition. This contradiction proves geometric connectedness and hence geometric irreducibility. Adjunction [@Hartshorne1977 Chapter V, Section 1, Proposition 1.5 and Example 1.5.2] gives $g=(3-1)(3-1)=4$.

Put $a_p=p+1-\#X_\rho(\mathbf F_p)$. Substitution of [\[eq:zcount\]](#eq:zcount){reference-type="eqref" reference="eq:zcount"} into [\[eq:moment\]](#eq:moment){reference-type="eqref" reference="eq:moment"} proves $$\label{eq:ap}
 \boxed{C_{p,2}=-14-2a_p},
 \qquad
 \boxed{c_{p,2}=-\frac{28+4a_p}{p-1}}.$$ The Weil bound now gives $$\label{eq:weil}
 |a_p|\le8\sqrt p,
 \qquad
 |c_{p,2}|\le\frac{28+32\sqrt p}{p-1}.$$ The point count is independent of the choice between $\rho$ and $\rho^{-1}=\rho^2$. Indeed, for $$T([r:s],[t:u])=([r:-s],[u:t])$$ one checks directly that $F_{\rho^{-1}}=\rho F_\rho\circ T$. Thus $T$ is an $\mathbf F_p$-isomorphism between the two presentations.

# The third abscissa and two trace categories

The logarithm of the normalized Euler product is $$-\sum_{p\equiv1(3)}\sum_{n\ge1}\frac{c_{p,n}}n p^{-ns}.$$ The exact first moment $c_{p,1}=-12/(p-1)$ is summable for $\operatorname{Re}s>0$. By [\[eq:weil\]](#eq:weil){reference-type="eqref" reference="eq:weil"}, the $n=2$ contribution is summable for $\operatorname{Re}s>1/4$. For $n\ge3$, the inherited estimate $|c_{p,n}|\le4\cdot4^n$ gives the large-prime majorant, but a finite-prime step is needed to sum over $n$. Fix a compact set with $\operatorname{Re}s\ge\sigma_0>1/3$, and choose $P_0$ so that $4p^{-\sigma_0}\le1/2$ for $p>P_0$. Then $$\sum_{p>P_0}\sum_{n\ge3}\frac{|c_{p,n}|}{n}p^{-n\sigma_0}
 \ll\sum_{p>P_0}p^{-3\sigma_0}<\infty.$$ For the finitely many $p\le P_0$, the unitary-block estimate $|c_{p,n}|\le\tau_p(I)=(8p+4)/3$ makes the logarithmic series converge geometrically because $p^{-\sigma_0}<1$. This proves local normal convergence and the Euler assertion in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

The operator interpretation is equally exact, but the trace category must be specified. Let $(\mathcal M,\tau)$ be the inherited product algebra with its normalized faithful semifinite trace, and let $X_s$ be the Galois-sector block. Since each local block is unitary, $$\tau(|X_s|^q)
 =\sum_{p\equiv1(3)}\frac{8p+4}{3}p^{-q\operatorname{Re}s},
 \qquad
 X_s\in L^q(\mathcal M,\tau)
 \quad\Longleftrightarrow\quad q\operatorname{Re}s>2.$$ In particular, $X_s$ is $\tau$-trace class exactly for $\operatorname{Re}s>2$; only there does the unregularized $\tau$-associated analytic graded determinant exist. On the larger half-plane $\operatorname{Re}s>1/3$, $L^6(\mathcal M,\tau)$ is the first fixed integer ideal covering every point. With $$\ell_n(s)=\sum_pc_{p,n}p^{-ns},\qquad1\le n\le5,$$ the $n=1$ and $n=2$ estimates above, together with the uniform bound for $3\le n\le5$, show that every counterterm converges there. Removing the first five logarithmic terms produces the trace-associated graded regularized determinant $$\operatorname{Det}_{6,\tau,\mathrm{gr}}(I-X_s)
 =\exp\!\left(-\sum_{n\ge6}\frac{\operatorname{str}(X_s^n)}n\right),$$ equivalently the quotient of the $\tau$-associated sixth-order regularized determinants in the positive and negative grades [@Simon2005 Chapter 9]. This gives the factorization in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Order six is the least fixed integer order forced by positive $L^q(\mathcal M,\tau)$-membership on the whole half-plane; the claim does not classify unrelated regularization schemes.

The ordinary Hilbert trace gives a different threshold and a different local object. Let $\mathcal H=\bigoplus_p\mathcal H_p$ be the underlying Hilbert direct sum and $d_p=(p-1)/2$. Since $$\dim\mathcal H_p
 =d_p\tau_p(I)=\frac{(p-1)(4p+2)}3,$$ one has $$\operatorname{Tr}_{\mathcal H}(|X_s|^q)
 =\sum_{p\equiv1(3)}\frac{(p-1)(4p+2)}3p^{-q\operatorname{Re}s},
 \qquad
 X_s\in S^q(\mathcal H)
 \quad\Longleftrightarrow\quad q\operatorname{Re}s>3.$$ At equality the series is a positive constant multiple of the divergent split-prime harmonic series; the two strict inequalities follow by the same prime-series comparison. Thus classical Hilbert trace class begins only at $\operatorname{Re}s>3$. Furthermore, $$\operatorname{Str}_{\mathcal H_p}(W_p^n)
 =d_pc_{p,n}=C_{p,n},$$ Writing $G_p$ for the local normalized root and $N_p=G_p^{d_p}$ for its ordinary Galois norm, the canonical local logarithm satisfies $$\exp\operatorname{Str}_{\mathcal H_p}\operatorname{Log}_0(I-zW_p)
 =G_p(z)^{d_p}=N_p(z).$$ The classical Fredholm determinant therefore encodes the ordinary Galois norm $N_p$, rather than the normalized root $G_p$ used in $\mathcal G$. The larger regularization order in the normalized category is the transparent price of reaching a larger half-plane; it is not a loss of Hénon chronology.

# Route-A audit and the next wall

The formal evaluation is $$\begin{gathered}
\mathrm{A1\_WEAK},\quad
\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\quad
\mathrm{A4\_NATURAL\_QUANTIZATION}.
\end{gathered}$$

The advance is exact: a chronological Hénon moment has become a Frobenius trace, the Euler germ reaches $\operatorname{Re}s>1/3$, and a canonical regularized operator determinant relative to the normalized semifinite trace realizes it. It is neither an unregularized $\tau$-determinant there---that domain starts at $\operatorname{Re}s>2$---nor a classical Fredholm determinant, whose trace-class domain starts at $\operatorname{Re}s>3$ and whose local trace gives the ordinary norm. A1 remains weak because primes label finite arithmetic fibres rather than primitive cycles of a single real map. A3 remains partial because there is no continuation, Gamma factor, functional equation, zero-counting law, or Riemann-divisor match. A4 is natural at each finite place, but no global self-adjoint spectral generator has been built.

The first unresolved logarithmic term is now $n=3$. Its direction stratification involves a cubic fourfold, a split quadric fourfold, and their $(2,3)$ threefold intersection. Isolating the non-Tate middle cohomology and proving a second square-root gain is the next decisive gate; absent that gain, $\operatorname{Re}s=1/3$ remains the certified wall.

# Uniform smoothness {#sec:smooth}

We give a literal four-chart Jacobian certificate. Work over an algebraic closure of a field of characteristic different from two and three. On the charts $U_{rt},U_{ru},U_{st},U_{su}$, use affine coordinates $(\xi,\eta)=(s,u),(s,t),(r,u),(r,t)$, respectively. Equation [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"} becomes $$\begin{aligned}
 f_{rt}&=\rho(1+\eta^3)+\xi^3\eta(\rho^2-\eta),\\
 f_{ru}&=\rho(\eta^3+1)+\xi^3\eta(\rho^2\eta-1),\\
 f_{st}&=\rho\xi^3(1+\eta^3)+\eta(\rho^2-\eta),\\
 f_{su}&=\rho\xi^3(\eta^3+1)+\eta(\rho^2\eta-1).\end{aligned}$$

On $U_{rt}$, the equation $\partial_\xi f_{rt}=3\xi^2\eta(\rho^2-\eta)=0$ leaves $\xi=0$, $\eta=0$, or $\eta=\rho^2$. If $\xi=0$, then $\partial_\eta f_{rt}=3\rho\eta^2=0$, hence $\eta=0$, but $f_{rt}=\rho$. The other two cases give $f_{rt}=\rho$ and $f_{rt}=2\rho$, respectively. Thus this chart has no singular point.

On $U_{ru}$, the equation $\partial_\xi f_{ru}=3\xi^2\eta(\rho^2\eta-1)=0$ leaves $\xi=0$, $\eta=0$, or $\eta=\rho$. The first case, together with $\partial_\eta f_{ru}=0$, reduces to $\eta=0$ and $f_{ru}=\rho$; the remaining cases give $f_{ru}=\rho$ and $f_{ru}=2\rho$. Again there is no singular point.

On $U_{st}$, the equation $\partial_\xi f_{st}=3\rho\xi^2(1+\eta^3)=0$ leaves $\xi=0$ or $\eta^3=-1$. In the first case, $f_{st}=0$ forces $\eta=0$ or $\eta=\rho^2$, whereas $\partial_\eta f_{st}$ is respectively $\rho^2$ or $-\rho^2$. In the second case, $f_{st}=0$ forces $\eta=\rho^2$, whose cube is one, contradicting characteristic different from two.

Finally, on $U_{su}$, the equation $\partial_\xi f_{su}=3\rho\xi^2(1+\eta^3)=0$ leaves $\xi=0$ or $\eta^3=-1$. If $\xi=0$, then $f_{su}=0$ forces $\eta=0$ or $\eta=\rho$, where $\partial_\eta f_{su}$ equals $-1$ or $1$. If $\eta^3=-1$, then $f_{su}=0$ forces $\eta=\rho$, whose cube is one, another contradiction.

The four charts cover $\mathbf P^1\times\mathbf P^1$, so the curve is geometrically smooth in every characteristic other than two and three. Together with $N(\rho-1)=3$, this is an all-prime certificate whose only excluded denominators are supported on two and three; no numerical Jacobian test is used.
