---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-relative-lind-full-ladder-counterterm"
canonical_tex: "henon_dynamics/henon_relative_lind_full_ladder_counterterm/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_relative_lind_full_ladder_counterterm/paper/paper.pdf"
source_sha256: "645411351e6f4cc5b6ef0dd147c93b85e6fa544f56fb1a4828a35a64b573aa79"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Order-Independent Full-Ladder Counterterm for the Hénon--Lind Relative Germ

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_relative_lind_full_ladder_counterterm>)
- [规范 TeX](<../../../../../henon_dynamics/henon_relative_lind_full_ladder_counterterm/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_relative_lind_full_ladder_counterterm/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_relative_lind_full_ladder_counterterm/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_relative_lind_full_ladder_counterterm/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The locally normalized ratio of the odd Hénon reflection-packet Euler product to the reverse-action Lind zeta has one rational singular channel for every positive integer. Its first positive singularity can be removed, but all later channels leave essential singularities. We construct an exact counterterm for the complete positive and complex ladder. A level $m$ has $2m$ poles $\alpha_{m,k}=2^{-1/(2m)}e^{\pi\mathrm ik/m}$ with principal coefficients $b_{m,k}=c_m(-1)^k/(\sqrt2m)$. Directly multiplying these pole factors is invalid: their absolute logarithmic mass diverges even at the origin. We subtract Taylor degrees $0,\ldots,m-1$ from each level-$m$ pole. Root orthogonality makes the subtractions cancel within each level, while the regularized double series becomes absolutely normally convergent and hence independent of every pole ordering. Its sum is exactly the full residual channel tail. After adding the remaining negative first-channel source factor and a base-point normalization, the resulting counterterm $K_{\rm all}$ satisfies $K_{\rm all}C_{\rm rel}=1$ on compatible branches. This theorem gives exact punctured analytic renormalization. It does not construct a transfer operator or attach arithmetic meaning to the channel index.
author:
- Anonymous
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  An Order-Independent Full-Ladder Counterterm for the\
  Hénon--Lind Relative Germ
```

## Markdown 正文

# Introduction

The full area-preserving Hénon horseshoe is conjugate to the full two-shift in the frozen hyperbolic regime [@DevaneyNitecki1979]. Reflection-fixed periodic words therefore define an exact symbolic packet inside the Hénon system. Uniform cyclic sampling of that packet leads to an orbit-resolved Euler product, while the reverse action on the full shift has the distinct Lind zeta calculated by @KimLeePark2003. Their locally normalized ratio is analytic across the first positive entropy boundary, but its exact continuation contains infinitely many later singular channels.

The remaining problem is not to locate another singularity. Every channel and every principal coefficient is already explicit. The problem is to turn the complete singularity ledger into one counterterm without imposing an arbitrary summation order. Splitting a rational channel into its complex simple poles initially makes matters worse: signed cancellation occurs only after all poles of a level are grouped, and the ungrouped absolute mass diverges. Thus a formal product over the complex divisor does not yet define an analytic object.

We resolve this ordering defect with a level-dependent Weierstrass regularization. At level $m$, each simple pole is stripped of its Taylor terms through degree $m-1$. The $2m$ roots annihilate all of those terms exactly, so the signed level remains unchanged. Each individual term now starts at degree $m$, which yields a geometric compact majorant. The same construction simultaneously proves arbitrary pole-order independence and recovers the original scalar-channel tail.

The contributions are concrete.

1.  We determine the full complex pole divisor and an exact simple-pole partial fraction for every scalar channel.

2.  We prove that the raw individual pole factors are not absolutely summable, so channel-grouped convergence cannot be promoted to arbitrary pole ordering without a new argument.

3.  We prove that genus $m-1$ regularization preserves every channel and makes the complete double series absolutely normally convergent.

4.  We include the negative first-channel source factor and prove the normalized identity $K_{\rm all}(t)C_{\rm rel}(t)=1$ on compatible branches.

The last identity is an analytic cancellation theorem, not an operator realization: $K_{\rm all}$ deliberately copies the channel ledger that it removes.

# The frozen relative germ

For the full two-shift with reverse flip, the source formula is $$\label{eq:lind}
 \zeta_{\rm flip}(t)=(1-2t^2)^{-1/2}
 \exp\!\left(\frac{2t+3t^2}{1-2t^2}\right).$$ The odd primitive reflection packet instead gives $$\label{eq:packet}
 \mathcal Z_{\rm orb}(t,1)=\prod_{\substack{n\ge1\\n\ \mathrm{odd}}}(1-t^n)^{-D_n},$$ where $D_n$ counts primitive marked reflection words. Equation [\[eq:packet\]](#eq:packet){reference-type="eqref" reference="eq:packet"} is not the full infinite-dihedral Lind zeta.

Put $u=1-\sqrt2t$. The first-boundary normalization is $$\label{eq:relative}
 C_{\rm rel}(t)=u^{1/2}e^{-3/(4u)}\frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}.$$ On a compatible local branch, this function extends holomorphically and nonvanishingly through $u=0$. The power $1/2$ and coefficient $3/4$ are forced within the power-exponential class.

The exact primitive/repetition regrouping uses $$\label{eq:phi-c}
 \Phi(x)=\frac{2x}{1-2x^2},\qquad
 c_m=\frac1m\sum_{\substack{d\mid m\\d\ \mathrm{odd}}}d\mu(d)
     =\frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}(1-p).$$ Every $c_m$ is nonzero and $|c_m|\le1$. Define the later-channel tail $$\label{eq:tail}
 \mathcal L(t)=\sum_{m\ge2}c_m\Phi(t^m).$$ Previous exact regrouping gives $$\label{eq:previous-cont}
 \log C_{\rm rel}(t)=H_{\rm rel}(1-\sqrt2t)-\mathcal L(t),
 \qquad
 H_{\rm rel}(u)=-\frac12\log(2-u)
 -\frac{3(2u-3)}{4(u-2)}.$$ The channel series is normally convergent on compact subsets of $\mathbb D$ after its poles are removed. That grouped statement does not yet justify a product over individual complex poles.

# The full complex divisor

For $m\ge2$, set $$\label{eq:roots}
 \rho_m=2^{-1/(2m)},\qquad
 \alpha_{m,k}=\rho_m e^{\pi\mathrm ik/m},\quad 0\le k<2m,$$ and $$\label{eq:bmk}
 b_{m,k}=\frac{c_m(-1)^k}{\sqrt2m}.$$ The points in [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"} are the roots of $1-2t^{2m}$. Their moduli $\rho_m$ increase strictly to one, so distinct levels have disjoint pole sets. Write $$\label{eq:singular-set}
 \mathcal S=\{\alpha_{m,k}:m\ge2,\ 0\le k<2m\},\qquad
 \Omega=\mathbb D\setminus\mathcal S.$$ The set $\mathcal S$ is locally finite in $\mathbb D$.

[\[thm:partial\]]{#thm:partial label="thm:partial"} For every $m\ge2$, $$\label{eq:partial}
 c_m\Phi(t^m)=\sum_{k=0}^{2m-1}
 \frac{b_{m,k}}{1-t/\alpha_{m,k}}.$$ At the pole $\alpha_{m,k}$, the coefficient of $(1-t/\alpha_{m,k})^{-1}$ is $b_{m,k}$.

Let $v=1-t/\alpha_{m,k}$. Since $\alpha_{m,k}^m=2^{-1/2}(-1)^k$, expansion of the denominator gives $$\Phi(t^m)=\frac{(-1)^k}{\sqrt2m}\frac1v+O(1).$$ Thus the two sides of [\[eq:partial\]](#eq:partial){reference-type="eqref" reference="eq:partial"} have identical principal parts. Their difference is a rational function without finite poles and vanishes at infinity, so it is zero.

For a coefficient-level check, put $\zeta=e^{\pi\mathrm i/m}$. The coefficient of $t^j$ on the right contains $$\sum_{k=0}^{2m-1}(-1)^k\zeta^{-jk}
 =\sum_{k=0}^{2m-1}\zeta^{(m-j)k}.$$ This root sum vanishes unless $j\equiv m\pmod{2m}$. At $j=m(2\ell+1)$, the surviving coefficient is $c_m2^{\ell+1}$, exactly the expansion of $c_m\Phi(t^m)$.

The theorem shows that each positive singularity belongs to a complete $2m$-point circle. Any counterterm confined to the positive ray omits $2m-1$ poles at level $m$.

# Why the raw pole product fails

A tempting construction is to exponentiate each summand in [\[eq:partial\]](#eq:partial){reference-type="eqref" reference="eq:partial"} and multiply over $(m,k)$. Channel by channel, this recovers $e^{\mathcal L(t)}$. The ungrouped product, however, has no order-independent meaning.

[\[prop:raw\]]{#prop:raw label="prop:raw"} The double series $$\label{eq:raw-series}
 \sum_{m\ge2}\sum_{k=0}^{2m-1}
 \frac{b_{m,k}}{1-t/\alpha_{m,k}}$$ is not absolutely summable at $t=0$. Consequently the associated raw exponential pole factors cannot be multiplied in arbitrary pole order.

At level $m$, the absolute logarithmic mass at the origin equals $$\label{eq:level-mass}
 \sum_{k=0}^{2m-1}|b_{m,k}|=\sqrt2|c_m|.$$ For every odd prime $p$, formula [\[eq:phi-c\]](#eq:phi-c){reference-type="eqref" reference="eq:phi-c"} gives $|c_p|=(p-1)/p\ge2/3$. The subsum of [\[eq:level-mass\]](#eq:level-mass){reference-type="eqref" reference="eq:level-mass"} over the infinitely many odd primes diverges.

The obstruction does not contradict the channel-grouped continuation in [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. Within each fixed $m$, the alternating roots cancel exactly. It proves that this grouping is mathematically active and cannot be silently discarded.

# Genus-dependent pole regularization

We now replace conditional level cancellation by an absolutely convergent double series. Define $$\begin{aligned}
 R_{m,k}(t)
 &=b_{m,k}\left[
   \frac1{1-t/\alpha_{m,k}}
   -\sum_{j=0}^{m-1}\left(\frac{t}{\alpha_{m,k}}\right)^j
   \right] \label{eq:R-def}\\
 &=b_{m,k}\frac{(t/\alpha_{m,k})^m}
 {1-t/\alpha_{m,k}}. \label{eq:R-tail}\end{aligned}$$ This is a genus-$m-1$ Weierstrass subtraction for the logarithm of an exponential pole factor. The increasing genus is essential: each individual term must begin at a degree that tends to infinity with $m$.

[\[lem:cancellation\]]{#lem:cancellation label="lem:cancellation"} For $0\le j<m$, $$\label{eq:root-cancel}
 \sum_{k=0}^{2m-1}b_{m,k}\alpha_{m,k}^{-j}=0.$$ Hence $$\label{eq:level-identity}
 \sum_{k=0}^{2m-1}R_{m,k}(t)=c_m\Phi(t^m).$$

After removing a nonzero factor independent of $k$, the sum in [\[eq:root-cancel\]](#eq:root-cancel){reference-type="eqref" reference="eq:root-cancel"} is $\sum_{k=0}^{2m-1}e^{\pi\mathrm i(m-j)k/m}$. For $0\le j<m$, its exponent is not divisible by $2m$, so the geometric root sum is zero. Summing [\[eq:R-def\]](#eq:R-def){reference-type="eqref" reference="eq:R-def"} over $k$ therefore removes all subtraction polynomials. The remaining pole terms equal $c_m\Phi(t^m)$ by [\[thm:partial\]](#thm:partial){reference-type="ref" reference="thm:partial"}.

[\[thm:normal\]]{#thm:normal label="thm:normal"} The double series $$\label{eq:regularized-double}
 \sum_{m\ge2}\sum_{k=0}^{2m-1}R_{m,k}(t)$$ converges absolutely and normally on compact subsets of $\Omega$. Its sum is $\mathcal L(t)$, and every enumeration of the individual pairs $(m,k)$ has the same sum. Consequently $$\label{eq:pole-product}
 \prod_{m\ge2}\prod_{k=0}^{2m-1}e^{R_{m,k}(t)}
 =e^{\mathcal L(t)}$$ is a locally uniform, nonzero, order-independent product on $\Omega$.

Fix a compact $K\subset\Omega$ and choose $r<q<1$ with $|t|\le r$ on $K$. Because $\rho_m\nearrow1$, all sufficiently large $m$ satisfy $|t/\alpha_{m,k}|\le q$ uniformly for $t\in K$ and all $k$. Equation [\[eq:R-tail\]](#eq:R-tail){reference-type="eqref" reference="eq:R-tail"}, $|c_m|\le1$, and the $2m$ poles give $$\label{eq:majorant}
 \sum_{k=0}^{2m-1}|R_{m,k}(t)|
 \le \frac{\sqrt2|c_m|q^m}{1-q}
 \le \frac{\sqrt2q^m}{1-q}.$$ The right side is summable in $m$. The finitely many earlier levels are bounded on $K$ because $K$ avoids their poles. The Weierstrass test proves absolute normal convergence. Arbitrary rearrangements preserve an absolutely convergent series, while [\[lem:cancellation\]](#lem:cancellation){reference-type="ref" reference="lem:cancellation"} identifies its sum with [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. Exponentiation yields [\[eq:pole-product\]](#eq:pole-product){reference-type="eqref" reference="eq:pole-product"}.

The proof distinguishes two statements that look similar in channel notation. P72 supplies normal convergence after each rational level is assembled. supplies absolute normal convergence before level assembly, which is precisely the property needed for an unordered product over the complex divisor.

# The normalized full-ladder counterterm

The tail product [\[eq:pole-product\]](#eq:pole-product){reference-type="eqref" reference="eq:pole-product"} removes all channels $m\ge2$, but the source remainder in [\[eq:previous-cont\]](#eq:previous-cont){reference-type="eqref" reference="eq:previous-cont"} still contains the negative first-channel boundary. Put $$\label{eq:w}
 w=1+\sqrt2t=2-u.$$ Direct substitution into $H_{\rm rel}$ gives $$\label{eq:H-w}
 H_{\rm rel}(u)=\frac{3}{4w}-\frac12\log w-\frac32.$$ Thus $w=0$ carries both an exponential singularity and a square-root branch.

Choose a simply connected slit subdomain $U\subset\Omega\setminus\{-1/\sqrt2\}$ that contains the origin and on which $\log w$ is defined, and take the compatible branch of $w^{1/2}$. Define $$\label{eq:Kall}
 K_{\rm all}(t)=e^{3/2}w^{1/2}e^{-3/(4w)}
 \prod_{m\ge2}\prod_{k=0}^{2m-1}e^{R_{m,k}(t)}.$$

[\[thm:main\]]{#thm:main label="thm:main"} The product in [\[eq:Kall\]](#eq:Kall){reference-type="eqref" reference="eq:Kall"} is locally uniform and independent of the enumeration of its individual complex pole factors. On every compatible branch, $$\label{eq:identity}
 \boxed{K_{\rm all}(t)C_{\rm rel}(t)=1.}$$ The normalization is fixed at the origin: $K_{\rm all}(0)=e^{3/4}$ and $C_{\rm rel}(0)=e^{-3/4}$.

By [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"}, the logarithm of the double product in [\[eq:Kall\]](#eq:Kall){reference-type="eqref" reference="eq:Kall"} is $\mathcal L(t)$. Equations [\[eq:previous-cont\]](#eq:previous-cont){reference-type="eqref" reference="eq:previous-cont"} and [\[eq:H-w\]](#eq:H-w){reference-type="eqref" reference="eq:H-w"} therefore give $$\begin{aligned}
 \log K_{\rm all}(t)+\log C_{\rm rel}(t)
 &=\left(\frac32+\frac12\log w-\frac{3}{4w}+\mathcal L(t)\right)\\
 &\quad+\left(\frac{3}{4w}-\frac12\log w-\frac32-\mathcal L(t)\right)=0.\end{aligned}$$ Exponentiating proves [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}. At $t=0$, one has $w=1$ and $\mathcal L(0)=0$, giving the two stated values.

The factor $w^{1/2}e^{-3/(4w)}$ is not another later channel. It removes the source-native negative boundary left after the positive local normalization in [\[eq:relative\]](#eq:relative){reference-type="eqref" reference="eq:relative"}. Omitting it would leave [\[eq:H-w\]](#eq:H-w){reference-type="eqref" reference="eq:H-w"} singular.

# Certification and claim boundary

The accompanying exact certificate checks the divisor and coefficients at three distinct layers. First, integer Möbius sums agree with the odd-radical product for $c_m$. Second, 96 formal coefficients of [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} agree with the primitive/repetition ledger after the first channel is removed. Third, the root cancellations and rational geometric majorants are recorded level by level. An independent program reconstructs 63 regularized levels at three complex sample points. Those floating checks audit signs and indexing; the proof of [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"} is the exact root sum and majorant, not a numerical extrapolation.

Six hashes bind the result to the P71 and P72 proof packages, certificates, and PDFs. Eight tests run under ordinary and optimized Python, and a hostile mutation audit rejects promotions of the analytic identity to an operator, an arithmetic trace, or Route B.

The scope restriction is structural. Formula [\[eq:Kall\]](#eq:Kall){reference-type="eqref" reference="eq:Kall"} is built by copying every scalar channel of $\mathcal L$ and reversing its sign in $\log C_{\rm rel}$. It supplies no independently defined Banach space, kernel, iteration law, or trace formula. A rank-one or diagonal operator could be reverse-engineered from almost any nonzero holomorphic function; such an encoding would not show that Hénon dynamics owns the determinant. The next operator test must define its state space and action before matching [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}.

Likewise, the integer $m$ labels a Möbius/repetition channel. Nothing in the construction identifies $m$ with a rational prime or prime power, and no von-Mangoldt amplitude or explicit formula follows. Route B is not authorized.

# Conclusion

The complete complex singularity ladder admits an exact counterterm, but only after its conditionally grouped pole decomposition is regularized. Genus $m-1$ subtraction preserves each rational channel by root orthogonality and makes the individual pole family absolutely normally convergent. The resulting order-independent product, together with the negative first-channel source factor, cancels the relative germ exactly.

This closes the analytic renormalization question raised by the infinite ladder. It does not close the ownership question. The counterterm knows the answer because it contains the full channel ledger. A substantive next step is therefore a rigidity theorem modulo holomorphic gauge, followed by a transfer model whose kernel and trace iterates are fixed independently of the target product.
