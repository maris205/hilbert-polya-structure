---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--9-cat-prime-shell-multiplicity"
canonical_tex: "symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/manuscript.pdf"
source_sha256: "fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Multiplicity Audit for Prime-Torsion Euler Products of the Cat Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity>)
- [规范 TeX](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the cat matrix $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$, we audit whether the complete nonzero prime-torsion shell can supply one Riemann-style local denominator. We first re-derive the classical prime-lattice orbit structure. Every odd unramified shell has a common least period, with primitive-orbit multiplicity $m_p=(p+1)h_p$ in the split case and $m_p=(p-1)h_p$ in the inert case. The binary shell is one three-cycle, whereas the ramified shell at five has two two-cycles and two ten-cycles. We then separate two products: a point-potential return product retains the primitive length $|\gamma|$, while a one-time orbit label produces $(1-p^{-s})^{-m_p}$. Fixed nonzero scalar coefficients independent of the local variable cannot reduce this pure denominator degree to one for any odd prime. Equal coefficients repair only the first logarithmic repeat. Fractional orbit-mass exponents do give exactly one factor, but only as shell-global normalized counting that extends mechanically to composite-order shells. One development-seen exact audit at $p=2,3,5,7,11$ reproduces $m_p=1,2,4,6,24$; it is a finite control, not evidence for the all-prime theorem. This low-novelty negative audit therefore closes only the direct scalar normalization attempt; centralizer, matrix, numerator, and Fredholm mechanisms remain open.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'Pre-review manuscript, August 14, 2026'
title: 'A Multiplicity Audit for Prime-Torsion Euler Products of the Cat Map'
```

## Markdown 正文

**Keywords:** cat map; prime torsion; finite-field orbit; dynamical Euler product; scalar weight; multiplicity obstruction.

# Introduction and bounded question {#sec:introduction}

Let $T_A\colon\mathbb{T}^{2}\to\mathbb{T}^{2}$ be the automorphism induced by $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
  \label{eq:cat-matrix}$$ For each rational prime $p$, the nonzero $p$-torsion shell is $\mathbb{F}_p^2\setminus\{0\}$. The bounded question of this note is whether the complete shell, with one label $p$, can produce exactly one local denominator $(1-p^{-s})^{-1}$ without discarding or globally renormalizing its primitive orbits. This diagnostic is not the ordinary Artin--Mazur zeta function of the toral automorphism, and it is not a proposal for a new dynamical zeta function.

The arithmetic entering the question is classical. Modular and quadratic descriptions of cat-map periods go back at least to @PercivalVivaldi1987 and @DysonFalk1992. @Gaspari1994 directly studies the same cat map on prime lattices, including the common nonzero period away from the ramified prime and the resulting orbit decomposition. The cycle-generating formulas of @BaakeNeumaerkerRoberts2013, especially their Appendix A.1, directly cover the binary and ramified boundaries used below. We therefore present the finite-field classification only as a self-contained re-derivation needed to expose multiplicity, not as a new orbit theorem.

Finite and rational-lattice orbit products are likewise established objects [@BaakeRobertsWeiss2008], while the ordinary toral dynamical zeta function has an arithmetic formulation independent of the prime-shell relabeling used here [@BaakeLauPaskunas2010]. The fixed-point exponential, primitive-orbit grouping, weighted products, and analytic operator framework are classical [@ArtinMazur1965; @Ruelle1976; @ParryPollicott1990]. Recent prime-power cycle work further limits any broad finite-ring novelty claim [@TanLi2025]; recent finite-permutation determinant packaging for the cat map likewise precludes a generic claim of new cycle-product machinery [@Chandra2026].

Against that prior art, the note makes a deliberately modest contribution that is primarily diagnostic. It juxtaposes known prime-shell arithmetic with elementary product algebra and records where a specific one-factor construction changes semantics. More precisely, we:

1.  re-derive the split, inert, binary, and ramified orbit counts and isolate the uniform lower bound $m_p\ge p-1$ for odd primes;

2.  distinguish a genuine point-potential return product from an externally assigned one-time orbit-label product;

3.  prove a denominator-degree obstruction only for fixed nonzero scalar factors, then record the zero-weight, equal-weight, fractional, and selector boundaries; and

4.  give safe global convergence strips and a provenance-closed finite audit without promoting five development-seen rows to all-prime evidence.

The negative statement is intentionally narrow. It does not exclude matrix-valued factors, numerator or alternating cancellation, transfer or Fredholm determinants, cohomological superdeterminants, variable-dependent weights, enriched selectors, or centralizer quotients. It gives no result in $2<\operatorname{Re}s\le3$, no exact abscissa, analytic continuation, functional equation, or zero statement. It gives no prime-orbit or prime-zero correspondence, no quantization, no historical priority claim, and no Route B construction.

Section [2](#sec:arithmetic){reference-type="ref" reference="sec:arithmetic"} proves the prime-shell theorem. Section [3](#sec:products){reference-type="ref" reference="sec:products"} separates the two products. Section [4](#sec:scalar){reference-type="ref" reference="sec:scalar"} states the scalar obstruction and its exact normalization boundary. Section [5](#sec:global){reference-type="ref" reference="sec:global"} gives the safe analytic strips and the open escape mechanisms. Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} records the fixed exact audit and its proof/computation firewall.

# Prime-shell arithmetic {#sec:arithmetic}

For a prime $p$, set $$V_p=\mathbb{F}_p^2\setminus\{0\},\qquad
  \Gamma_p=V_p/\langle A\rangle,\qquad
  m_p=|\Gamma_p|.
  \label{eq:shell-definitions}$$ Thus $\Gamma_p$ is the set of primitive $A$-orbits partitioning $V_p$, and $|\gamma|$ denotes the least dynamical period of $\gamma$. The characteristic polynomial is $$f(X)=X^2-3X+1,\qquad \operatorname{disc}(f)=5.
  \label{eq:characteristic}$$ For $p\ne5$, let $\tau_p$ be the order of $A$ in $\mathrm{GL}_2(\mathbb{F}_p)$. For odd $p\ne5$, the Legendre symbol $\left(\frac5p\right)$ separates the split and inert cases.

[\[thm:prime-shell\]]{#thm:prime-shell label="thm:prime-shell"} For the matrix in [\[eq:cat-matrix\]](#eq:cat-matrix){reference-type="eqref" reference="eq:cat-matrix"}, the following statements hold.

1.  At $p=2$, the three points of $V_2$ form one orbit of length three, so $m_2=1$.

2.  If $p$ is odd, $p\ne5$, and $\left(\frac5p\right)=1$, every point of $V_p$ has exact period $\tau_p$, where $\tau_p\mid p-1$. With $h_p=(p-1)/\tau_p$, $$m_p=(p+1)h_p\ge p+1.
              \label{eq:split-multiplicity}$$ The two eigenlines contribute $2h_p$ cycles, and their complement contributes $(p-1)h_p$ cycles.

3.  If $p$ is odd and $\left(\frac5p\right)=-1$, every point of $V_p$ has exact period $\tau_p$, where $\tau_p\mid p+1$. With $h_p=(p+1)/\tau_p$, $$m_p=(p-1)h_p\ge p-1.
              \label{eq:inert-multiplicity}$$

4.  At $p=5$, four points have exact period two and twenty points have exact period ten. They form two cycles of each length, so $m_5=4$.

Consequently $p=2$ is the unique prime shell with $m_p=1$, and $m_p\ge p-1$ for every odd prime.

The common-period and orbit-decomposition content of Theorem [\[thm:prime-shell\]](#thm:prime-shell){reference-type="ref" reference="thm:prime-shell"} directly overlaps the classical prime-lattice analysis of @Gaspari1994; the two exceptional boundary profiles are also directly represented in @BaakeNeumaerkerRoberts2013. We give the full proof because the later product audit depends on the exact number and lengths of primitive factors.

Suppose first that $p$ is odd, $p\ne5$, and $\left(\frac5p\right)=1$. The polynomial $f$ has distinct roots $\lambda$ and $\lambda^{-1}$ in $\mathbb{F}_p$, so a change of basis conjugates $A$ to $\operatorname{diag}(\lambda,\lambda^{-1})$. Both diagonal entries have the same multiplicative order; call it $\tau_p$. A nonzero vector $(x,y)$ has at least one nonzero coordinate. The equality $$A^k(x,y)=(x,y)$$ therefore forces $\lambda^k=1$ on every nonzero coordinate, and that condition also suffices. Every nonzero vector consequently has least period $\tau_p$. Since $\lambda\in\mathbb{F}_p^\times$, one has $\tau_p\mid p-1$.

The $p^2-1$ nonzero vectors split into $$m_p=\frac{p^2-1}{\tau_p}
      =(p+1)\frac{p-1}{\tau_p}=(p+1)h_p$$ cycles. Each eigenline contains $p-1$ nonzero points, so the two eigenlines contribute $2(p-1)/\tau_p=2h_p$ cycles. Their complement has $(p-1)^2$ points and contributes $(p-1)^2/\tau_p=(p-1)h_p$ cycles. This proves the split statement and its lower bound without assuming that $\tau_p$ is maximal.

Now suppose $\left(\frac5p\right)=-1$. The polynomial $f$ is irreducible over $\mathbb{F}_p$. Identify the two-dimensional $\mathbb{F}_p$-space with $\mathbb{F}_{p^2}$ so that $A$ acts as multiplication by a root $\lambda$ of $f$. Frobenius sends $\lambda$ to the other root, so $$\lambda^p=\lambda^{-1},\qquad \lambda^{p+1}=1.$$ Thus $\tau_p=\operatorname{ord}(\lambda)\mid p+1$. For every nonzero $v\in\mathbb{F}_{p^2}$, $$A^kv=v
  \quad\Longleftrightarrow\quad
  (\lambda^k-1)v=0
  \quad\Longleftrightarrow\quad
  \lambda^k=1.$$ Every nonzero vector again has exact period $\tau_p$, and hence $$m_p=\frac{p^2-1}{\tau_p}
      =(p-1)\frac{p+1}{\tau_p}=(p-1)h_p\ge p-1.$$

At $p=2$, the reduction of $f$ is $X^2+X+1$, which is irreducible. Cayley--Hamilton gives $A^2+A+I=0$, and multiplication by $A-I$ gives $A^3=I$. The polynomial has no root one, so there is no nonzero fixed vector. The three nonzero vectors must therefore form a single three-cycle.

It remains to treat the ramified prime. Modulo five, put $$N=A+I=\begin{pmatrix}3&1\\1&2\end{pmatrix}.
  \label{eq:nilpotent-N}$$ Direct multiplication gives $A=-I+N$, $N^2=0$, and $\operatorname{rank}N=1$. The kernel of $N$ has five elements. On its four nonzero elements, $A=-I$, so every such point has exact period two and the four points form two cycles.

For every $k\ge1$, the nilpotent binomial formula gives $$A^k=(-1)^k(I-kN).
  \label{eq:nilpotent-power}$$ Take $v\notin\ker N$. If odd $k$ fixed $v$, applying $N$ to $A^kv=v$ would give $-Nv=Nv$, hence $Nv=0$ in characteristic five, a contradiction. For even $k$, equation [\[eq:nilpotent-power\]](#eq:nilpotent-power){reference-type="eqref" reference="eq:nilpotent-power"} fixes $v$ exactly when $kNv=0$, or equivalently when $5\mid k$. The least positive even multiple of five is ten. The twenty vectors outside $\ker N$ therefore have exact period ten and form two cycles. Thus $m_5=2+2=4$.

The four cases exhaust the primes. The split and inert bounds are at least two for odd primes, while $m_5=4$; only $p=2$ has one cycle.

![Exact profiles on the five frozen prime shells. Panel A partitions nonzero points by least return period; Panel B gives $m_p=1,2,4,6,24$ for $p=2,3,5,7,11$; and Panel C isolates the binary one-orbit boundary, the mixed ramified shell, and the split $p=11$ strata. All five rows were visible during development and serve only as exact implementation controls. Uniqueness of $p=2$ and the all-odd lower bound come from Theorem [\[thm:prime-shell\]](#thm:prime-shell){reference-type="ref" reference="thm:prime-shell"}, not from the finite display.](fig1_shell_profiles.pdf){#fig:prime-shell-profiles width="99%"}

# Two products that must not be identified {#sec:products}

The orbit count alone does not determine which local variable a dynamical construction assigns to an orbit. We distinguish a point observable from a one-time orbit label before manipulating either product.

## The point-potential return product

On the fixed shell $V_p$, take the point observable $$L(x)=\log p.
  \label{eq:point-observable}$$ Its Birkhoff sum along a primitive orbit $\gamma$ of length $\ell=|\gamma|$ is $\ell\log p$. Consider the fixed-point exponential $$Z_{\mathrm{raw},p}(s)
  =\exp\!\left(
    \sum_{n\ge1}\frac1n
    \sum_{x\in V_p\cap\operatorname{Fix}(A^n)}
       \exp\bigl(-sS_nL(x)\bigr)
  \right).
  \label{eq:raw-fixed-point}$$ This is a finite-permutation instance of the classical fixed-point and primitive-orbit ledger [@ArtinMazur1965; @Ruelle1976; @ParryPollicott1990]. We use it only to derive the shell-local formal factor.

A primitive orbit of length $\ell$ contributes to the $n$-th return sum only when $n=r\ell$. At that return it supplies $\ell$ fixed points, each with $S_{r\ell}L=r\ell\log p$. Its logarithmic contribution is $$\sum_{r\ge1}\frac{\ell}{r\ell}p^{-sr\ell}
  =\sum_{r\ge1}\frac{p^{-sr\ell}}r
  =-\log(1-p^{-s\ell}).
  \label{eq:raw-orbit-contribution}$$ Grouping over primitive cycles therefore gives $$Z_{\mathrm{raw},p}(s)
  =\prod_{\gamma\in\Gamma_p}
    (1-p^{-s|\gamma|})^{-1}.
  \label{eq:raw-product}$$ For the binary, split, and inert cases, all primitive lengths equal $\tau_p$, so the factor is $(1-p^{-s\tau_p})^{-m_p}$. At the ramified prime, the two cycle lengths remain separate: $$Z_{\mathrm{raw},5}(s)
  =(1-5^{-2s})^{-2}(1-5^{-10s})^{-2}.
  \label{eq:raw-five}$$ This mixed factor is the sharpest finite reminder that a genuine return retains dynamical length.

## The externally assigned orbit-label product

Now identify the primitive cycles first and assign the shell label $\log p$ once to each of them, independently of length. This different definition gives $$Z_{\mathrm{lab},p}(s)
  =\prod_{\gamma\in\Gamma_p}(1-p^{-s})^{-1}
  =(1-p^{-s})^{-m_p}.
  \label{eq:label-product}$$ Its formal logarithm is $$\log Z_{\mathrm{lab},p}(s)
  =m_p\sum_{r\ge1}\frac{p^{-rs}}r,
  \label{eq:label-logarithm}$$ so the coefficient at repetition $r$ is exactly $m_p/r$. Dividing a raw orbit sum by its primitive period can change $|\gamma|\log p$ into $\log p$, but it does not remove any of the $m_p$ primitive factors. Period normalization changes the label; it does not quotient the orbit set.

The label product in [\[eq:label-product\]](#eq:label-product){reference-type="eqref" reference="eq:label-product"} is therefore not silently identified with [\[eq:raw-product\]](#eq:raw-product){reference-type="eqref" reference="eq:raw-product"}, with the finite-lattice Euler products of @BaakeRobertsWeiss2008, or with the ordinary toral zeta function studied by @BaakeLauPaskunas2010. The point of the audit is precisely to keep these constructions separate.

![The point-potential return product and the externally relabeled orbit product are different constructions. Panel A shows that a genuine return retains $|\gamma|$, while assigning $\log p$ once per primitive orbit imports $m_p$. Panel B displays the ramified stress test: $Z_{\mathrm{raw},5}$ has separate length-two and length-ten monomials, whereas $Z_{\mathrm{lab},5}$ has degree four in the one-time shell label. Panel C gives the exact formal coefficient $m_p/r$ for $r=1,2,3$. No numerical value of $s$, $p^{-s}$, or $\log p$ is evaluated.](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/figures/fig2_product_semantics.pdf>){#fig:raw-versus-label width="99%"}

# Scalar obstruction and exact normalization boundary {#sec:scalar}

Write $z=p^{-s}$ as a formal local variable. The next theorem concerns only finite pure-denominator products with fixed scalar coefficients. This scope is part of the statement, not a later qualification.

[\[thm:scalar-obstruction\]]{#thm:scalar-obstruction label="thm:scalar-obstruction"} Let $p$ be an odd prime. For each $\gamma\in\Gamma_p$, let $w_\gamma\in\mathbb{C}\setminus\{0\}$ be fixed and independent of $z$. Then $$\prod_{\gamma\in\Gamma_p}(1-w_\gamma z)^{-1}
  \ne (1-z)^{-1}
  \label{eq:scalar-no-go}$$ as rational functions, equivalently as formal power series at $z=0$. If zero coefficients are admitted, equality holds if and only if the multiset of weights is $\{1,0,\ldots,0\}$.

An equality in [\[eq:scalar-no-go\]](#eq:scalar-no-go){reference-type="eqref" reference="eq:scalar-no-go"} would imply, after clearing denominators, $$\prod_{\gamma\in\Gamma_p}(1-w_\gamma z)=1-z.
  \label{eq:cleared-denominators}$$ If every $w_\gamma$ is nonzero, the polynomial on the left has degree $m_p$ and nonzero leading coefficient. The polynomial on the right has degree one. Theorem [\[thm:prime-shell\]](#thm:prime-shell){reference-type="ref" reference="thm:prime-shell"} gives $m_p\ge2$ for every odd prime, so equality is impossible.

If zeros are allowed, omit their unit factors. The degree comparison shows that exactly one nonzero weight can remain. Comparing the coefficient of $z$ then forces that weight to equal one. Conversely the multiset $\{1,0,\ldots,0\}$ plainly gives $(1-z)^{-1}$.

For a finite scalar potential $\phi$, an orbit weight of the form $w_\gamma=\exp(S_\gamma\phi)$ is nonzero. Thus Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} applies when those weights are placed in the same finite pure-denominator product. The theorem is not a theorem about the full weighted-zeta or transfer-operator frameworks of @Ruelle1976 and @ParryPollicott1990. It does not address matrix weights, vector bundles, $z$-dependent weights, numerator cancellation, alternating products, Fredholm determinants, or cohomological superdeterminants.

## Repetition detects the equal-weight failure

Taking formal logarithms in a hypothetical scalar identity shows that the necessary and sufficient power-sum conditions are $$\sum_{\gamma\in\Gamma_p}w_\gamma^r=1
  \qquad (r\ge1).
  \label{eq:power-sum-condition}$$ The tempting equal choice $w_\gamma=1/m_p$ repairs the first coefficient, but gives $$\sum_{\gamma\in\Gamma_p}w_\gamma^r
  =m_p^{\,1-r}.
  \label{eq:equal-weight-sums}$$ When $m_p>1$, the value differs from one for every $r\ge2$. The registered repetitions $r=1,2,3$ are exact examples of this formal identity, not a numerical approximation to an infinite product.

## Fractional outer exponents succeed globally

The primitive cycles partition $V_p$, so $$\sum_{\gamma\in\Gamma_p}|\gamma|=|V_p|=p^2-1.
  \label{eq:shell-partition}$$ Interpret fractional powers as formal germs at $z=0$, using $(1-z)^{-a}=\exp(-a\log(1-z))$. Equation [\[eq:shell-partition\]](#eq:shell-partition){reference-type="eqref" reference="eq:shell-partition"} then gives the exact identity $$\prod_{\gamma\in\Gamma_p}
    (1-p^{-s})^{-|\gamma|/(p^2-1)}
  =(1-p^{-s})^{-1}.
  \label{eq:fractional-prime-identity}$$ This is a successful repair. It is nevertheless a different construction from Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"}: the exponent is applied outside the common factor and depends on the complete shell cardinality and complete cycle partition. We call it *global normalized counting*.

The same argument is not specific to primes. For an integer $q\ge2$, let $E_q\subset\mathbb{T}^{2}$ be the points of exact additive order $q$. The integral automorphism $A$ permutes $E_q$, whose cardinality is the Jordan totient $$|E_q|=J_2(q)
  =q^2\prod_{\substack{\ell\mid q\\ \ell\ \mathrm{prime}}}
     (1-\ell^{-2}).
  \label{eq:jordan-totient}$$ If $\Gamma(E_q)$ denotes its cycle set, then symbolically $$\prod_{\gamma\in\Gamma(E_q)}
    (1-q^{-s})^{-|\gamma|/J_2(q)}
  =(1-q^{-s})^{-1}.
  \label{eq:fractional-composite-identity}$$ No value of $q$ is selected or enumerated here. Equation [\[eq:fractional-composite-identity\]](#eq:fractional-composite-identity){reference-type="eqref" reference="eq:fractional-composite-identity"} records only that normalized cycle mass works for every finite permutation of an exact-order shell, so the mechanism has no intrinsic prime specificity.

## A selector has an exact discard cost

Keeping one orbit produces one factor by definition. On the complete shell it also discards exactly $m_p-1$ primitive cycles and adds a global symmetry-breaking choice. The frozen construction supplies no canonical selector. We record this cost without claiming that no enriched or canonical selector can exist.

![Mechanism boundary for collapsing shell multiplicity. Panel A separates the fixed nonzero scalar obstruction, the equal-weight repeat failure, exact fractional counting, the one-orbit selector, and the untested centralizer escape. Panel B gives the exact equal-weight power sums at $r=1,2,3$. Panel C gives fractional outer exponents and selector costs on the five fixed shells. The symbolic $J_2(q)$ control states a partition identity only; no composite shell was enumerated. Matrix, numerator, alternating, Fredholm, and cohomological mechanisms are not excluded by the scalar theorem.](<../../../../../symplectic_map/papers/9-cat-prime-shell-multiplicity/paper/figures/fig3_mechanism_boundary.pdf>){#fig:mechanism-boundary width="99%"}

# Global bounds and the escape boundary {#sec:global}

The one-time label factors define the formal prime-indexed product $$Z_{\mathrm{lab}}(s)=\prod_p(1-p^{-s})^{-m_p}.
  \label{eq:global-label-product}$$ The finite audit in Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} supplies no analytic evidence for this product. The only global conclusions used here come from the all-prime bounds in Theorem [\[thm:prime-shell\]](#thm:prime-shell){reference-type="ref" reference="thm:prime-shell"}.

[\[prop:convergence\]]{#prop:convergence label="prop:convergence"} Let $s=\sigma+it$.

1.  For real $1<s\le2$, the positive logarithmic series for $Z_{\mathrm{lab}}(s)$ diverges.

2.  For complex $s$ with $1<\sigma\le2$, the logarithmic series is not absolutely convergent.

3.  For $\sigma>3$, the logarithmic series is absolutely convergent.

No statement is made for $2<\sigma\le3$.

For $1<\sigma\le2$, the first repetition and the odd-prime lower bound give $$\sum_p m_pp^{-\sigma}
  \ge \sum_{p\ \mathrm{odd}}(p-1)p^{-\sigma}.
  \label{eq:convergence-lower}$$ For odd $p$, the summand on the right is at least $\tfrac12p^{1-\sigma}$, which is at least $1/(2p)$ when $\sigma\le2$. Euler's divergence of $\sum_p1/p$ proves divergence. When $s$ is real, every term in $$\sum_p m_p\sum_{r\ge1}\frac{p^{-rs}}r$$ is positive. For complex $s$, the same first-repetition estimate proves failure of absolute convergence.

For $\sigma>3$, use $m_p\le|V_p|=p^2-1$. For all sufficiently large $p$, $$\sum_{r\ge1}\frac{|p^{-rs}|}{r}
  =-\log(1-p^{-\sigma})
  \le C_\sigma p^{-\sigma}.$$ The absolute logarithmic series is therefore bounded, up to finitely many terms, by a constant multiple of $$\sum_p p^{2-\sigma}
  \le \sum_{n\ge2}n^{2-\sigma}<\infty.$$ This proves the stated upper strip and nothing sharper.

Proposition [\[prop:convergence\]](#prop:convergence){reference-type="ref" reference="prop:convergence"} does not determine an exact abscissa. It does not address conditional convergence in the gap, meromorphic continuation, a functional equation, or zeros. These omissions are substantive boundaries rather than missing numerical experiments.

## Mechanisms not closed by the theorem

The degree proof uses commutative scalar factors with no numerator. A matrix determinant can combine eigenchannels; an alternating or cohomological product can place factors in a numerator; and a Fredholm or transfer determinant can encode cancellations not visible in a finite product of scalar linear denominators. Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} excludes none of these possibilities. The classical weighted and operator-theoretic literature is precisely why the scope must remain narrow [@Ruelle1976; @ParryPollicott1990].

A centralizer quotient is another genuine escape. In the inert case, the finite-field centralizer can be identified with $\mathbb{F}_{p^2}^{\times}$, which acts transitively on the nonzero shell. In the split case, the two nonzero eigenlines and their complement form three natural centralizer strata. At $p=5$, the Jordan kernel minus zero and its complement form two natural strata. Such symmetry structure is standard context for rational-lattice orbit analysis [@BaakeNeumaerkerRoberts2013]. The present audit neither constructs nor rules out such a quotient. A successful quotient would still depend on the $p$-shell centralizer, and the label $p$ would still come from the externally specified additive-order shell. The centralizer route remains follow-up work.

# Development-seen exact audit and provenance {#sec:audit}

After the theorem and product contracts were frozen and independently reviewed, one registered exact audit was run at exactly $$p\in\{2,3,5,7,11\}.
  \label{eq:registered-primes}$$ These five rows were inherited from earlier development and were not blind test points. Their role was to falsify discrepancies between two exact implementations: a formula/classification engine and a direct permutation engine over every nonzero vector. They do not prove an all-prime theorem or a global analytic statement.

C0.07 Y C0.18 C0.18 C0.09 $p$ & case & point-period profile & cycle profile & $m_p$\
& binary inert boundary & $3:3$ & $3:1$ & 1\
3 & inert & $4:8$ & $4:2$ & 2\
5 & ramified Jordan & $2:4,\ 10:20$ & $2:2,\ 10:2$ & 4\
7 & inert & $8:48$ & $8:6$ & 6\
11 & split & $5:120$ & $5:24$ & 24\

Across the five shells, the direct engine partitions all $203$ nonzero vectors into $37$ primitive cycles. The independent classification engine returns the same shell cardinalities, point-period histograms, cycle histograms, multiplicities, and, at $p=11$, the same four eigenline and twenty off-eigenline cycles. The twelve locked controls all pass. At the formal repetitions $r=1,2,3$, the label coefficients are respectively $$(1,\tfrac12,\tfrac13),\quad
  (2,1,\tfrac23),\quad
  (4,2,\tfrac43),\quad
  (6,3,2),\quad
  (24,12,8).$$ The selector discard costs are $0,1,3,5,23$.

The registered lifecycle contains exactly one exact audit and one registered run. Candidate numerical runs are zero. No numerical value of $s$, $p^{-s}$, or $\log p$ was evaluated. No prime outside [\[eq:registered-primes\]](#eq:registered-primes){reference-type="eqref" reference="eq:registered-primes"}, composite shell, external prime table, generated prime target array, Riemann-zero datum, centralizer computation, parameter search, normalization search, or selector search entered the run. The result was closed by an independent integrity review and a strict manifest before manuscript production. No candidate or test was rerun for this manuscript.

# Limitations and conclusion {#sec:conclusion}

The strongest conclusion of this audit is a scoped incompatibility, not a new dynamical system. The complete nonzero $p$-torsion shell has $m_p>1$ primitive orbits for every odd prime. A point-potential return retains their lengths; an external one-time label retains their count. Fixed nonzero scalar denominator weights cannot collapse that count to one. Equal weights fail under repetition. Fractional orbit masses succeed exactly, but only by using the complete shell as a normalized counting space, a mechanism that also works symbolically for composite order.

Most ingredients have direct prior collisions. Prime-lattice common periods and orbit decompositions are classical [@Gaspari1994]; the binary and ramified cycle boundaries and their symmetry context are already explicit in the rational-lattice literature [@BaakeNeumaerkerRoberts2013]; finite-lattice Euler products and primitive/repetition formalisms are also established [@BaakeRobertsWeiss2008; @ArtinMazur1965; @Ruelle1976; @ParryPollicott1990]. The value of the note is therefore a transparent semantic and mechanism audit, not classification, zeta, determinant, or priority novelty.

The exact terminal decision is

`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED`\
`A0_FAIL_GLOBAL_NORMALIZATION_ONLY`\
`ROUTE_B_NOT_OPENED`.

The first label certifies only the frozen prime-shell multiplicity and pure scalar obstruction. The second admits the exact fractional identity and rejects it only as global, tautological, and non-prime-specific. The third records that no spectral or quantization route was opened. The next bounded question is whether a centralizer-enriched quotient can compress shell multiplicity without merely hiding a global selector. This note neither answers nor experimentally investigates that question.

# Formal product ledger {#app:products}

For completeness, this appendix records the exact local factors used in the finite audit. It is a transcription of the frozen cycle partitions, not a new computation.

C0.05 p0.38 p0.22 p0.19

\
$p$ & raw-return factor & orbit-label factor & fractional masses\
$p$ & raw-return factor & orbit-label factor & fractional masses\
& $(1-2^{-3s})^{-1}$ & $(1-2^{-s})^{-1}$ & $1$\
3 & $(1-3^{-4s})^{-2}$ & $(1-3^{-s})^{-2}$ & $1/2,1/2$\
5 & $\begin{gathered}(1-5^{-2s})^{-2}\\
    {}\cdot(1-5^{-10s})^{-2}\end{gathered}$ & $(1-5^{-s})^{-4}$ & $\begin{gathered}1/12,1/12,\\5/12,5/12\end{gathered}$\
7 & $(1-7^{-8s})^{-6}$ & $(1-7^{-s})^{-6}$ & $6\times(1/6)$\
11 & $(1-11^{-5s})^{-24}$ & $(1-11^{-s})^{-24}$ & $24\times(1/24)$\

The raw factor in each row follows from $$\sum_{\substack{\gamma\in\Gamma_p\\|\gamma|=\ell}}
  \sum_{r\ge1}\frac{p^{-sr\ell}}r
  =-c_{p,\ell}\log(1-p^{-s\ell}),$$ where $c_{p,\ell}$ is the number of primitive length-$\ell$ cycles. The label factor instead replaces every length-dependent monomial by $p^{-s}$ after the orbit set is known. The fractional masses in the last column sum to one because their numerators are cycle lengths and their common denominator is $p^2-1$.

The zero-weight boundary in Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} also has a direct coefficient formulation. Expanding a formal logarithm gives $$\log\prod_\gamma(1-w_\gamma z)^{-1}
  =\sum_{r\ge1}\frac{z^r}{r}\sum_\gamma w_\gamma^r.$$ Equality with $(1-z)^{-1}$ is equivalent to all power sums being one. The polynomial-degree argument shows that a finite multiset satisfying these conditions and allowing zeros must be $\{1,0,\ldots,0\}$; hence the apparently algebraic zero-weight repair is exactly the one-orbit selector.

# Claim--evidence and computation firewall {#app:firewall}

C0.08 p0.38 p0.43

\
claim & authority & boundary\
claim & authority & boundary\
C1 & Theorem [\[thm:prime-shell\]](#thm:prime-shell){reference-type="ref" reference="thm:prime-shell"} and its proof & classical re-derivation; the five rows are controls only\
C2 & equations [\[eq:raw-product\]](#eq:raw-product){reference-type="eqref" reference="eq:raw-product"}--[\[eq:label-logarithm\]](#eq:label-logarithm){reference-type="eqref" reference="eq:label-logarithm"} & raw returns retain $|\gamma|$; external labels retain $m_p$\
C3 & Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} & fixed nonzero, $z$-independent scalar pure denominators only\
C4 & equations [\[eq:power-sum-condition\]](#eq:power-sum-condition){reference-type="eqref" reference="eq:power-sum-condition"}--[\[eq:equal-weight-sums\]](#eq:equal-weight-sums){reference-type="eqref" reference="eq:equal-weight-sums"} & symbolic for all $r$; registered $r=1,2,3$ are controls\
C5 & equations [\[eq:shell-partition\]](#eq:shell-partition){reference-type="eqref" reference="eq:shell-partition"}-- [\[eq:fractional-composite-identity\]](#eq:fractional-composite-identity){reference-type="eqref" reference="eq:fractional-composite-identity"} & global counting; composite $q$ is symbolic and unenumerated\
C6 & Section 4.3 selector count & discards $m_p-1$ cycles; no selector impossibility theorem\
C7 & Proposition [\[prop:convergence\]](#prop:convergence){reference-type="ref" reference="prop:convergence"} & proof-only; no finite analytic evidence, and $2<\operatorname{Re}s\le3$ remains open\
C8 & Table [\[tab:registered-ledger\]](#tab:registered-ledger){reference-type="ref" reference="tab:registered-ledger"} and certified result package & one development-seen audit; no all-prime or analytic inference\
C9 & Section 5.1 outside-theorem boundary & centralizer and richer determinant mechanisms remain live\

The registered data consist of exact finite-field permutations and rational or symbolic coefficients. There are no samples, random seeds, fitted parameters, tolerances, confidence intervals, or residual estimates. The two exact engines can falsify a row-level implementation; they cannot replace the split/inert/binary/ramified proof. Conversely, the proof cannot certify that the software actually preserved the mixed $p=5$ factor or the development-time input boundary. The one-shot audit and theorem therefore have complementary, explicitly separated roles.

# Frozen provenance and disclosure {#app:provenance}

Manuscript production was bound to the following independently reviewed artifacts:

Source lock

:   `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`.

Proof package

:   `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa`.

Independent source review

:   `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f`.

Registered exact result

:   `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab`.

Independent result review

:   `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd`.

Strict result manifest

:   `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92`.

Independent plan/figure/citation review

:   `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06`.

Figure manifest

:   `8ae2709444e6e06286b061635352d2ba0c419c04d313edf1272cb57ab41b2b83`.

The independently reviewed figure gate bound an explicit 24-file asset allowlist with framed-tree digest `312c4b095b58acb9e8047d7113308d28870e3db7633f37d17bd904ca2c7ebfaa`. The manuscript files added later are not retroactively included in that digest; they receive a separate pre-review integrity record.

The exact audit was run once before manuscript production. No experiment, candidate, unit test, prime or modulus scan, composite enumeration, centralizer calculation, or numerical analytic evaluation was rerun for writing or compilation. The bibliography contains exactly the eleven independently verified sources cited in the text. The submission is anonymous, and no identifying repository link, acknowledgment, grant, or affiliation appears in the source or PDF.
