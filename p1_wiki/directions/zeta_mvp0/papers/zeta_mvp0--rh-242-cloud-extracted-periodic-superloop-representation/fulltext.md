---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-242-cloud-extracted-periodic-superloop-representation"
canonical_tex: "zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/main.pdf"
source_sha256: "e81280f198dc2987c04efa8d05dfc42e8f5dd8706922a7a8aa644048692a13f3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cloud-Extracted Traces as Finite-Noise Periodic Superloops

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-242-cloud-extracted-periodic-superloop-representation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an exact fixed-positive-noise periodic-loop realization of the cloud-extracted traces left open by RH-241. Let $A_\sigma$ be the folded Gaussian operator after the inherited Hardy scaling, and put its Perron, parity, and selected-cloud values in a finite diagonal atomic sector $S_\sigma$. For every $n\ge2$, $$\tau_n(\sigma)
   =\operatorname{tr}A_\sigma^n-\operatorname{tr}S_\sigma^n
   =\operatorname{Str}\bigl((A_\sigma\oplus S_\sigma)^n\bigr).$$ Thus the physical closed Gaussian loops are paired with finite spectral counterloops. For the continuum statement the selected multiset is an abstract exact spectral submultiset; the archived Arnoldi values enter only the finite-matrix audit. The construction is projection free and has an exact discrete counterpart for both archived matrix channels.

  This identity is not yet an all-order estimate. Among the 352 archived determinant-relevant residuals, 179 are negative and 173 positive, with both signs at every order $2$--$12$. Hence merely deleting a subset of nonnegative Markov loops cannot represent all cloud-extracted traces; signed or complex grouping is unavoidable. We also prove that a uniform all-order trace envelope and a deterministic-numerator coefficient anchor are logically independent obligations. Neither is supplied here, so Gate A and Gates B--E remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Cloud-Extracted Traces as Finite-Noise Periodic Superloops'
```

## Markdown 正文

# Fixed-noise folded loops

At the algebraic band-merging parameter, let $$f(x)=1-u_{\rm c}x^2,
 \qquad u_{\rm c}=1.543689012692076\ldots .$$ For $x,y\in[0,1]$ and $\sigma>0$, the folded normalized Gaussian kernel is $$\label{eq:kernel}
 p_\sigma(x,y)=\frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {\int_{-1}^{1}\phi_\sigma(t-f(x))\,dt},$$ where $\phi_\sigma(t)=(2\pi\sigma^2)^{-1/2}
e^{-t^2/(2\sigma^2)}$. Its rows integrate to one. Write $$(P_\sigma g)(x)=\int_0^1p_\sigma(x,y)g(y)\,dy,
 \qquad A_\sigma=r_H^{-1}P_\sigma,
 \qquad r_H=0.85.$$ The exact folding and the unscaled cycle trace were proved in RH-7 [@WangRH7]. We now insert the moving cloud without introducing a projector.

Let $$\mathcal S_\sigma=\{a_{\sigma,+},a_{\sigma,-}\}\sqcup C_\sigma$$ be a finite multiset, counted with algebraic multiplicity. In the spectral application, $a_{\sigma,+}$ and $a_{\sigma,-}$ are the Hardy-scaled Perron and parity values and $C_\sigma$ is the selected cloud. Let $S_\sigma$ be the diagonal matrix with this multiset on its diagonal.

[\[thm:superloop\]]{#thm:superloop label="thm:superloop"} For every fixed $\sigma>0$ and every integer $n\ge2$, $$\begin{aligned}
 \tau_n(\sigma;\mathcal S_\sigma)
 &:={\operatorname{tr}}A_\sigma^n-\sum_{s\in\mathcal S_\sigma}s^n
 \label{eq:tau}\\
 &=r_H^{-n}\int_{[0,1]^n}
   \prod_{j=0}^{n-1}p_\sigma(x_j,x_{j+1})\,
   dx_0\cdots dx_{n-1}
   -\sum_{s\in\mathcal S_\sigma}s^n,
 \qquad x_n=x_0,\label{eq:loops}\\
 &=\operatorname{Str}\bigl((A_\sigma\oplus S_\sigma)^n\bigr).\label{eq:supertrace}\end{aligned}$$ Here the physical sector is even and the finite atomic sector is odd. If $\mathcal S_\sigma$ is an exact spectral submultiset, then these are exactly the complementary power traces of the projection-free factor in RH-234.

The continuous kernel on the compact square is Hilbert--Schmidt. Hence $A_\sigma^n$ is trace class for $n\ge2$, and the trace of its iterated kernel is the cyclic integral in [\[eq:loops\]](#eq:loops){reference-type="eqref" reference="eq:loops"} by the product theorem for Hilbert--Schmidt kernels and Fubini's theorem [@Simon2005]. The atomic trace is $\operatorname{tr}S_\sigma^n=\sum_s s^n$. By definition, the supertrace of a block-diagonal graded operator is the even trace minus the odd trace, proving [\[eq:supertrace\]](#eq:supertrace){reference-type="eqref" reference="eq:supertrace"}. When the selected values belong to the spectrum, Lidskii's theorem identifies the difference with the complementary spectral power sum.

The theorem makes the removal location explicit. The physical sector still contains every positive Gaussian loop. Perron, parity, and cloud removal occurs in the atomic counterloop sector after complete cyclic traces are formed. No inverse left/right overlap is used.

# Exact finite-matrix counterpart

Let $M$ be either the fine folded matrix or the Haar-compressed matrix in the RH-222 atlas, and put $A=M/r_H$ [@WangRH222]. For a closed index word $\boldsymbol i=(i_0,\ldots,i_{n-1})$, set $$W_A(\boldsymbol i)=\prod_{j=0}^{n-1}A_{i_j,i_{j+1}},
 \qquad i_n=i_0.$$

[\[prop:discrete\]]{#prop:discrete label="prop:discrete"} For every square matrix $A$ and $n\ge1$, $$\operatorname{tr}A^n=\sum_{i_0,\ldots,i_{n-1}}W_A(\boldsymbol i).$$ Consequently, for any finite selected multiset $\mathcal S$, $$\tau_n(A;\mathcal S)
 =\sum_{\boldsymbol i}W_A(\boldsymbol i)-\sum_{s\in\mathcal S}s^n
 =\operatorname{Str}\bigl((A\oplus S)^n\bigr).$$ If $\mathcal S$ is an exact spectral submultiset, this equals the power sum of all omitted eigenvalues, including algebraic multiplicity.

Expand the diagonal entries of $A^n$ and sum the base index. The spectral statement follows from the finite-dimensional trace identity, without diagonalizability.

The right channel deserves one boundary statement. It uses $M_R=E^*M_LE$, so its loops are loops of the compressed one-step matrix. In general $(E^*M_LE)^n\ne E^*M_L^nE$; the right loops are not inherited fine loops with only their endpoints averaged.

For sufficiently small $z$, the relative logarithm is therefore $$\label{eq:log}
 \log R_{\sigma,\mathcal S}(z)
 =-\sum_{n=2}^{\infty}\frac{\tau_n(\sigma;\mathcal S)}{n}z^n.$$ When $\mathcal S$ is spectral, [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"} is the quotient of the full $\det_2$ by the selected finite canonical product [@WangRH234].

# Why positive loop deletion is insufficient

The representation above is signed: the atomic sector enters with a minus sign, and nonreal cloud points occur in conjugate pairs. This is not a cosmetic choice.

[\[thm:deletion\]]{#thm:deletion label="thm:deletion"} Let $a(x,y)\ge0$ be a physical kernel. Any residual obtained only by keeping a measurable fraction $0\le\chi\le1$ of its length-$n$ physical loops has the form $$\int\chi(x_0,\ldots,x_{n-1})
 \prod_{j=0}^{n-1}a(x_j,x_{j+1})\,d\boldsymbol x\ge0.$$ The same statement holds for an entrywise nonnegative matrix. Hence a negative cloud-extracted trace cannot be represented by merely deleting ordinary positive physical loops while retaining their original weights.

The retained integrand, or every retained discrete loop weight, is nonnegative.

This is a scoped obstruction. It does not rule out signed groupings, complex projected kernels, coboundary cancellation, or a dynamically adapted representation. It says precisely that absolute ungrouped loop estimates discard the sign mechanism already visible in the data.

# Envelope and coefficient anchor are independent

The two remaining obligations have different logical types. A uniform all-order envelope is a size statement: $$\label{eq:envelope}
 |\tau_n(\sigma)|\le Mq^n,
 \qquad n\ge2,$$ with $M,q$ independent of both $n$ and $\sigma$. RH-240 proves that this gives a locally bounded zero-free normal relative determinant family on $|z|<q^{-1}$ [@WangRH240].

A coefficient anchor is an identification statement. One must first specify an independently derived germ $$H_*(z)=\exp\left[-\sum_{n=2}^{\infty}\frac{a_n}{n}z^n\right]$$ and then prove $\tau_n(\sigma)\to a_n$ at every fixed order, or prove an equivalent coefficient bridge for the full and cloud factors. The symbol $H_*$ is deliberately abstract here. The numerator $G(z)$ of the earlier one-step germ and the numerator $H(w)$ of its symmetric two-step germ use different variables, while the present atlas also divides eigenvalues by $r_H$ [@WangRH46; @WangRH80]. Their coefficient conversion must be proved before either can be declared the current anchor.

[\[prop:independence\]]{#prop:independence label="prop:independence"} Neither obligation implies the other.

1.  For any prescribed anchor $(a_n)$, choose a different finite-support sequence $(b_n)$ and set $\tau_n(\sigma)=b_n$. It satisfies a geometric envelope but does not converge to the prescribed anchor.

2.  Let $j\to\infty$ and set $\tau_n^{(j)}=a_n$ except for $\tau_{j+1}^{(j)}=a_{j+1}+e^{(j+1)^2}(1+|a_{j+1}|)$. Every fixed coefficient converges eventually to $a_n$, but no constants $M,q$ give a uniform geometric envelope.

Finite support is bounded by $Mq^n$ after enlarging $M$. In the second example, every fixed order is altered at most once, while the spike root rates are at least $e^{j+1}$ and are therefore unbounded.

In particular, an over-extracted selector can drive all residual coefficients toward zero and satisfy an excellent envelope while converging to the wrong normalization. Conversely, fixed-order Gaussian localization can identify each coefficient without controlling a delayed long-order spike.

# Finite audit

We enumerate all closed loops for three small folded Gaussian matrices and orders two through five. The twelve loop identities, graded supertrace identities, and spectral partition identities agree to ordinary floating precision. A separate Gauss--Legendre audit checks the continuum row normalization in [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}.

The RH-236 archive contains $32\times11=352$ determinant-relevant residuals at orders $2$--$12$ [@WangRH236]. Their real signs split as follows:

  cases                             negative   positive   zero
  ------------------------------- ---------- ---------- ------
  all archived orders $2$--$12$          179        173      0

Every individual order has both signs. The minimum is $-0.0401513$ and the maximum is $0.129520$, both at order two. The archive also contains cancellations of more than fifteen decimal orders between a full trace and its extracted residual. That ratio is only a floating diagnostic, not a relative-error certificate, but it reinforces the theorem: the useful object is a cancellation-preserving signed sum.

In the independent finite audit, the largest closed-loop identity error is $1.33\times10^{-15}$, the largest spectral-partition error is $1.45\times10^{-14}$, and the continuum row-mass quadrature error is $7.33\times10^{-15}$. These are reproducibility checks for frozen floating objects, not interval bounds for the continuum family.

The archived sparse matrices use an eight-standard-deviation truncation and row renormalization. Proposition [\[prop:discrete\]](#prop:discrete){reference-type="ref" reference="prop:discrete"} is exact for those frozen matrices. The fixed-order Nyström convergence theorem of RH-7 uses the untruncated kernel and does not supply a bound uniform in order and noise for the present sparse atlas. Likewise the stored roots are floating Arnoldi values, not interval-certified continuum spectral data.

# Boundary and next theorem

RH-242 supplies the requested strict finite-noise periodic-loop object. It does not yet supply a useful absolute majorant, because taking absolute values before pairing the physical and atomic sectors destroys the observed cancellation. The next target is a canonical grouping of physical loops and counterloops whose grouped weights admit a long-order bound uniform in the noise.

The all-order envelope and the coefficient anchor remain separate open theorems. No Hilbert--Pólya operator, completed-zeta divisor, prime-power trace identity, or Riemann-hypothesis conclusion is asserted. Gates A--E remain open.
