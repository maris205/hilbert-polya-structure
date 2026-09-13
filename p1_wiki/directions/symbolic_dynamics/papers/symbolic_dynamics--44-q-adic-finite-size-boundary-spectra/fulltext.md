---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--44-q-adic-finite-size-boundary-spectra"
canonical_tex: "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/main.tex"
canonical_pdf: "symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/main.pdf"
source_sha256: "4135879d386fc3b19c969c16d6e7cceb7f61ab1b526832e27a34d64f16f0d4ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# $q$-adic Finite-Size Boundary Spectra of Multiplicative Shifts of Finite Type Exact General Remainders and Golden Cantor Boundaries

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/44-q-adic-finite-size-boundary-spectra/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a primitive finite zero--one adjacency matrix $A$ and an integer radix $q\ge2$, we determine the entire order-one finite-size boundary of the multiplicative shift constrained along the chains $i,qi,q^2i,\ldots$. Adding a site at cutoff $N$ changes exactly one chain, so the logarithmic increment depends only on the valuation $\nu_q(N)$. Exact summation by parts then expresses the centered prefix count as a uniformly convergent real series in the residues $N\bmod q^v$. This series extends continuously to the inverse limit $\mathbb Z_q$, including composite $q$, and its image is exactly the complete accumulation set of the finite-size remainder.

  For the binary golden adjacency, Binet's formula turns the boundary map into an alternating digit series. An exact inequality in $\mathbb Q(\sqrt5)$ proves that every coefficient dominates its full tail. The image is therefore a strongly separated Cantor set, with Hausdorff and box dimensions both equal to $\log 2/(2\log\varphi)$. The same coefficient tails are the nonzero radial leading coefficients of the ordinary cutoff generating function at primitive dyadic roots; their density forces the unit circle to be a natural boundary. Earlier work supplies the multiplicative-shift framework, chain products, leading entropy and dimensions, and boundary-complexity theory. Our results concern the exact subleading boundary and, in the golden case, its geometric and analytic structure.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  **$q$-adic Finite-Size Boundary Spectra**\
  of Multiplicative Shifts of Finite Type\
  Exact General Remainders and Golden Cantor Boundaries
```

## Markdown 正文

# Introduction {#sec:introduction}

Leading entropy records how fast a language grows, but it deliberately forgets the bounded arithmetic left by an integer cutoff. That loss is especially visible for multiplicative shifts. Their constraints do not run along consecutive sites; they run along the chains $$i,\;qi,\;q^2i,\ldots,\qquad q\nmid i.$$ The standard chain product gives the leading term, yet a prefix ending at $N$ cuts the chains at different depths according to the base-$q$ digits of $N$. The natural question is therefore finite rather than asymptotic: after subtracting the entropy term, which order-one values can actually occur?

We answer this question exactly for every integer $q\ge2$ and every finite primitive zero--one adjacency matrix $A$. Let $Z(N)$ be the number of admissible labelings of $\{1,\ldots,N\}$, let $h$ be the leading prefix entropy, and set $E(N)=\log Z(N)-hN$. The inverse limit $$\mathbb Z_q:=\varprojlim_n \mathbb Z/q^n\mathbb Z$$ is used as a compact state space even when $q$ is composite; the boundary map is real-valued, not $q$-adic-valued. We prove that $E(N)$ extends to a continuous function $E_{A,q}\colon\mathbb Z_q\to\mathbb R$ and that its image is precisely the complete set of subsequential limits of $E(N)$ as $N\to\infty$.

The binary golden adjacency exposes additional geometry. Its boundary function is a signed digit series whose coefficients alternate and dominate their entire future tails. This all-level estimate makes the real boundary image a strongly separated Cantor set and determines its Hausdorff and box dimensions. The same coefficient tails control an ordinary generating function at primitive dyadic roots, producing a dense family of nonzero radial leading coefficients and therefore a natural boundary.

#### Theorem contributions.

The mathematical results are the following.

1.  An exact finite-$N$ increment and residue identity, followed by the equality $$\operatorname{Acc}_{N\to\infty}\{\log Z(N)-hN\}=E_{A,q}(\mathbb Z_q).$$

2.  For the binary golden control, a full-tail separation theorem and $$\dim_H E_{A,2}(\mathbb Z_2)
        =\dim_B E_{A,2}(\mathbb Z_2)
        =\frac{\log2}{2\log\varphi}.$$

3.  For the ordinary cutoff series $G(z)=\sum_{N\ge0}E(N)z^N$, the exact radial leading coefficient at every primitive dyadic root and the resulting unit-circle natural boundary.

The multiplicative-shift object and its leading theory are established in earlier work [@fan2012level; @kenyon2012hausdorff; @ban2019pattern]. Accordingly, Fibonacci word counts, the chain product, leading entropy and dimensions, and valid boundary-complexity results are background rather than contributions of this paper. gives the direct source comparison and reconciles a one-dimensional author-manuscript specialization of @ban2023boundary, with an explicit version-of-record caveat.

The general boundary law, golden Cantor theorem, and natural-boundary theorem appear in [\[sec:exact,sec:golden,sec:natural\]](#sec:exact,sec:golden,sec:natural){reference-type="ref" reference="sec:exact,sec:golden,sec:natural"}; scientific limitations are collected in [6](#sec:scope){reference-type="ref" reference="sec:scope"}. Two independent exact evaluators also replay finite consequences of the formulas. This reproducibility material is placed in [8](#sec:replay){reference-type="ref" reference="sec:replay"}: agreement checks implementations only and is not used to prove uniform convergence, the accumulation equality, separation, or the natural boundary. Artifact-specific Route and chronology records are confined to [9.5](#app:route-chronology){reference-type="ref" reference="app:route-chronology"}.

# Relation to earlier work and a same-object correction {#sec:prior}

#### Multiplicative shifts and leading geometry.

The multiplicative golden-mean system and its leading counts and dimensions belong to the early literature [@fan2012level]. The broader multiplicative-integer framework and leading Hausdorff/Minkowski theory were developed by @kenyon2012hausdorff. Direct admissible-chain pattern products, chain-length densities, entropy, and leading error control are likewise established in @ban2019pattern. Recent affine extensions broaden that leading dimension theory [@ban2025affine]. We use these objects and formulas as inputs and assign them zero contribution credit.

#### Digital fluctuations as a neighboring method family.

Summatory functions of digit-additive sequences often carry periodic or fractal fluctuations. The literature represented by @madritsch2012summatory is therefore a methodological neighbor. Its real periodic fluctuations do not, by themselves, state the exact valuation increment, the continuous inverse-limit remainder, or the same-object accumulation theorem proved below. The distinction matters: our coordinate $x\bmod q^v$ is first selected in the finite quotient and then evaluated as a real number; no fractional-part substitution or $q$-adic-valued analytic function is involved.

#### Boundary complexity.

@ban2023boundary introduce boundary complexity and surface entropy for multiplicative integer systems. Their valid leading and boundary results, together with that terminology, are established prior work. The present paper asks a narrower question: an exact bounded remainder at every integer cutoff and the closure of all its subsequential values. The ownership separation is summarized in [1](#tab:ownership){reference-type="ref" reference="tab:ownership"}.

::: {#tab:ownership}
  Component                                                                 Source/status                                                                                                              Credit in this paper
  ------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  Multiplicative SFT, $q$-adic chain partition, chain product               standard/elementary                                                                                                        zero
  Fibonacci word counts; leading entropy and shift dimensions               @fan2012level [@kenyon2012hausdorff; @ban2019pattern]                                                                      zero
  Boundary-complexity and surface-entropy framework                         @ban2023boundary                                                                                                           zero
  Affine multiplicative-shift dimensions                                    @ban2025affine                                                                                                             zero
  Exact valuation increment and continuous real boundary on $\mathbb Z_q$   proved in [3](#sec:exact){reference-type="ref" reference="sec:exact"}                                                      theorem result; no priority claim
  Golden full-tail separation, image dimension, radial coefficient          proved in [\[sec:golden,sec:natural\]](#sec:golden,sec:natural){reference-type="ref" reference="sec:golden,sec:natural"}   theorem result; golden case only

  : Direct attribution of ingredients and results. Previously established components receive zero credit here. "Proved here" records mathematical location only and is not a priority assertion.
:::

## The author-manuscript specialization {#sec:bhl-correction}

The checked artifact is the author manuscript [arXiv:2210.09115v1](https://arxiv.org/abs/2210.09115v1), submitted 17 October 2022. Theorem 3.3(2), the proof to which it reduces, and Remark 3.4 in that artifact give the relevant locator and hypotheses. The proof of Theorem 3.3 says its proofs are similar to that of Theorem 3.1 after the corresponding replacements; the proof of Theorem 3.1(2) explicitly specializes $\Omega$ to a one-dimensional mixing SFT with transition matrix $A$ and Perron eigenvalue $\lambda_A$. Remark 3.4 then takes spatial dimension one, $p\ge2$, $k\in\mathbb N$, and $N=p^{kn}$, and displays $$\log\lvert\mathcal P([1,p^{kn}],X_{\Sigma_A}^{p})\rvert
  -p^{kn}h
  =-(1-p^{-1})\log(\lambda_A)\,kn+o(kn).
  \label{eq:bhl-displayed}$$ The dictionary needed to compare [\[eq:bhl-displayed\]](#eq:bhl-displayed){reference-type="eqref" reference="eq:bhl-displayed"} with our object is explicit:

  author-manuscript symbol                                present symbol   specialization       meaning
  ------------------------------------------------------- ---------------- -------------------- --------------------
  $X_{\Sigma_A}^{p}$                                      $X_A^{(q)}$      $p=q$                multiplicative SFT
  $\lvert\mathcal P([1,p^{kn}],X_{\Sigma_A}^{p})\rvert$   $Z(N)$           $N=p^{kn}$           prefix count
  $\lambda_A$                                             $\rho(A)$        same adjacency       Perron eigenvalue
  $h$                                                     $h$              same normalization   prefix entropy

Take the full shift $A=J_D$, the $D\times D$ all-one matrix, with $D>1$. This matrix is positive, hence primitive, and its edge shift is mixing; it therefore satisfies the proof specialization just stated. Every site is free, hence $$W_\ell=D^\ell,\qquad Z(N)=D^N,\qquad h=\log D.$$ The left side of [\[eq:bhl-displayed\]](#eq:bhl-displayed){reference-type="eqref" reference="eq:bhl-displayed"} is therefore identically zero, whereas its displayed main term equals $-(1-p^{-1})\log D\,kn$, which is nonzero. More generally, the exact identity in [\[thm:qadic-boundary\]](#thm:qadic-boundary){reference-type="ref" reference="thm:qadic-boundary"} gives $d_v=0$ and $E(N)=0$ for this control. Thus the displayed one-dimensional specialization cannot hold with the stated quantifiers. The bounded order-one identity below is the compatible same-object correction under our present primitive one-dimensional definition.

> We checked only the author manuscript arXiv:2210.09115v1, submitted 17 October 2022. We did not line-check the version of record or any erratum, and make no claim about their displayed formulas.

Accordingly, we do not transfer [\[eq:bhl-displayed\]](#eq:bhl-displayed){reference-type="eqref" reference="eq:bhl-displayed"} to the journal version. We preserve every valid leading and boundary result of @ban2023boundary, assign this correction zero prior-ownership credit, and make no first-discovery claim. A primary source containing the exact $\mathbb Z_q$ extension and complete accumulation theorem, or the same golden separation theorem, would trigger the conditional duplicate stop recorded in [9.5](#app:route-chronology){reference-type="ref" reference="app:route-chronology"}.

# Exact finite-$N$ calculus and the $q$-adic boundary {#sec:exact}

Fix an integer $q\ge2$ and a finite $d\times d$ primitive matrix $A\in\{0,1\}^{d\times d}$. On the alphabet $\mathcal A=\{1,\ldots,d\}$, define $$X_A^{(q)}
  =\{x\in\mathcal A^{\mathbb N}: A_{x_n,x_{qn}}=1
    \text{ for every }n\ge1\}.$$ The cutoff $N$ always means the prefix $\{1,\ldots,N\}$; only constraints with both endpoints in this prefix are imposed. Write $Z(N)$ for its number of admissible labelings and set $Z(0)=1$. For ordinary $A$-admissible words, put $$W_0=1,\qquad
  W_\ell=\mathbf 1^{T}A^{\ell-1}\mathbf 1\quad(\ell\ge1).$$

## Chains and increments

Every positive integer has a unique representation $n=q^vi$ with $q\nmid i$. Consequently, the nonempty truncated chains $$\mathcal C_i(N)=\{i,qi,\ldots,q^{\ell_i(N)-1}i\},
  \qquad
  \ell_i(N)=1+\lfloor\log_q(N/i)\rfloor ,$$ partition the prefix. Constraints never cross two such chains, so the standard chain product is the exact identity $$Z(N)=\prod_{\substack{1\le i\le N\\q\nmid i}}W_{\ell_i(N)}
      =\prod_{\ell\ge1}W_\ell^{C_\ell(N)},
  \label{eq:chain-product}$$ where the finite histogram is $$C_\ell(N)=
  \lfloor N/q^{\ell-1}\rfloor
  -2\lfloor N/q^\ell\rfloor
  +\lfloor N/q^{\ell+1}\rfloor .$$

Let $\nu_q(N)=\max\{v\ge0:q^v\mid N\}$. Adding the site $N$ extends only the chain rooted at $N/q^{\nu_q(N)}$, from length $\nu_q(N)$ to length $\nu_q(N)+1$. Define $$c_v=\log\frac{W_{v+1}}{W_v},\qquad
  \rho=\rho(A),\qquad d_v=c_v-\log\rho .$$ Then $$\log Z(N)-\log Z(N-1)=c_{\nu_q(N)}.
  \label{eq:increment}$$ The convention $W_0=1$ covers $\nu_q(N)=0$, when a new one-site chain appears.

Primitivity supplies a Perron spectral gap. Thus for constants $C_0>0$, $0<\theta<1$, and an integer $m\ge0$, $$W_\ell=C_0\rho^{\ell-1}
  (1+O(\ell^m\theta^\ell)).$$ It follows that $d_v=O(v^m\theta^v)$, and hence both $\sum_v|d_v|$ and $\sum_{v\ge1}|d_v-d_{v-1}|$ converge. The natural mean increment is $$h=\sum_{v\ge0}\frac{q-1}{q^{v+1}}c_v
   =\log\rho+\sum_{v\ge0}\frac{q-1}{q^{v+1}}d_v .
  \label{eq:entropy}$$

## The exact residue identity

The number of $n\le N$ with valuation $v$ is $$A_v(N)=\lfloor N/q^v\rfloor-\lfloor N/q^{v+1}\rfloor .$$ For $r_v(N)=N\bmod q^v\in\{0,\ldots,q^v-1\}$, this becomes $$A_v(N)=N\frac{q-1}{q^{v+1}}
         -\frac{r_v(N)}{q^v}
         +\frac{r_{v+1}(N)}{q^{v+1}}.
  \label{eq:valuation-census}$$ Summing [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} by valuations and substituting [\[eq:valuation-census\]](#eq:valuation-census){reference-type="eqref" reference="eq:valuation-census"} gives the following result.

[\[thm:qadic-boundary\]]{#thm:qadic-boundary label="thm:qadic-boundary"} For every $N\ge1$, $$E(N):=\log Z(N)-hN
  =-\sum_{v\ge1}(d_v-d_{v-1})\frac{N\bmod q^v}{q^v}.
  \label{eq:exact-remainder}$$ For $x\in\mathbb Z_q$, let $x\bmod q^v$ denote the canonical integer representative of its level-$v$ coordinate. The series $$E_{A,q}(x)
  :=-\sum_{v\ge1}(d_v-d_{v-1})
       \frac{x\bmod q^v}{q^v}
  \label{eq:boundary-map}$$ converges uniformly to a continuous real-valued map on $\mathbb Z_q$. Moreover, $$\begin{aligned}
  \operatorname{Acc}_{N\to\infty}E(N)&=E_{A,q}(\mathbb Z_q), \label{eq:acc-log}\\
  \operatorname{Acc}_{N\to\infty}(Z(N)e^{-hN})
    &=\exp(E_{A,q}(\mathbb Z_q)). \label{eq:acc-exp}\end{aligned}$$

Equation [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} yields $\log Z(N)=\sum_{v\ge0}c_vA_v(N)$. Substitute [\[eq:valuation-census\]](#eq:valuation-census){reference-type="eqref" reference="eq:valuation-census"}, separate $c_v=\log\rho+d_v$, and use $\sum_vA_v(N)=N$ together with [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"}. An index shift gives [\[eq:exact-remainder\]](#eq:exact-remainder){reference-type="eqref" reference="eq:exact-remainder"}; it is justified by the absolute summability of $(d_v)$.

For $x\in\mathbb Z_q$, each coordinate $x\bmod q^v$ is locally constant and $0\le(x\bmod q^v)/q^v<1$. The summable majorant $\sum_{v\ge1}|d_v-d_{v-1}|$ proves uniform convergence and continuity.

If $E(N_j)\to y$ with $N_j\to\infty$, compactness of $\mathbb Z_q$ provides a $q$-adically convergent subsequence $N_{j_k}\to x$. Continuity then gives $y=E_{A,q}(x)$. Conversely, for fixed $x\in\mathbb Z_q$, the explicit integers $$N_j=(x\bmod q^j)+q^j$$ tend to infinity and converge to $x$ in $\mathbb Z_q$. Hence $E(N_j)\to E_{A,q}(x)$, proving the reverse inclusion. Finally, exponentiation is continuous and injective on $\mathbb R$, which gives [\[eq:acc-exp\]](#eq:acc-exp){reference-type="eqref" reference="eq:acc-exp"}.

The fractions $(x\bmod q^v)/q^v$ in [\[eq:boundary-map\]](#eq:boundary-map){reference-type="eqref" reference="eq:boundary-map"} are evaluated in $\mathbb R$ after selecting compatible finite-quotient coordinates. Thus $\mathbb Z_q$ is a compact inverse-limit domain, not the codomain of the series. No field structure is used, so composite $q$ is included.

For $A=J_d$, $W_\ell=d^\ell$, $c_v=\log d$, and $d_v=0$. Therefore $Z(N)=d^N$ and $E_{A,q}\equiv0$. The case $A=[1]$ gives the same zero boundary with $d=1$. These exact controls detect a spurious chain multiplicity or an omitted $W_0$.

# Golden boundary geometry {#sec:golden}

Specialize to $$q=2,\qquad
  A=\begin{pmatrix}1&1\\[1mm]1&0\end{pmatrix},
  \qquad
  \varphi=\frac{1+\sqrt5}{2}.$$ With $F_0=0,F_1=1$, the word counts are $W_\ell=F_{\ell+2}$. Set $$t=\varphi^{-2}=\frac{3-\sqrt5}{2},\qquad r=-t.$$ Binet's formula in the form $$F_n=\frac{\varphi^n}{\sqrt5}(1-r^n)$$ gives $$d_v=\log\frac{1-r^{v+3}}{1-r^{v+2}}.
  \label{eq:golden-d}$$

Every $x\in\mathbb Z_2$ has a unique expansion $x=\sum_{k\ge0}\varepsilon_k2^k$, with $\varepsilon_k\in\{0,1\}$. Substituting $x\bmod2^v=\sum_{k=0}^{v-1}\varepsilon_k2^k$ into [\[eq:boundary-map\]](#eq:boundary-map){reference-type="eqref" reference="eq:boundary-map"} and reordering an absolutely convergent double series yields $$E_{A,2}(x)=\sum_{k\ge0}\gamma_k\varepsilon_k,\qquad
  \gamma_k=-\sum_{v\ge k+1}(d_v-d_{v-1})2^{k-v}.
  \label{eq:gamma-residue}$$ Expanding the logarithms in [\[eq:golden-d\]](#eq:golden-d){reference-type="eqref" reference="eq:golden-d"} gives a second exact formula: $$\gamma_k=\sum_{m\ge1}a_m r^{m(k+2)},\qquad
  a_m=\frac{(1-r^m)^2}{m(2-r^m)}>0.
  \label{eq:gamma-modes}$$ The second expression separates one dominant signed mode from a certified tail.

[\[thm:golden\]]{#thm:golden label="thm:golden"} The coefficients in [\[eq:gamma-residue\]](#eq:gamma-residue){reference-type="eqref" reference="eq:gamma-residue"} satisfy $$\operatorname{sgn}(\gamma_k)=(-1)^k,\qquad
  |\gamma_k|>\sum_{j>k}|\gamma_j|,\qquad
  \frac{\gamma_{k+1}}{\gamma_k}\longrightarrow-\varphi^{-2}.$$ Consequently $$K:=E_{A,2}(\mathbb Z_2)
  =\{\sum_{k\ge0}\varepsilon_k\gamma_k:
          \varepsilon_k\in\{0,1\}\}$$ is a Cantor set, and $$\dim_HK=\dim_BK=\frac{\log2}{2\log\varphi}.$$

The algebraic number $t$ satisfies $0<t<1/2$ and $t^2-3t+1=0$. For $m\ge2$, $$a_m\le\frac Km,\qquad
  K=\frac{(1+t^2)^2}{2-t^2}=-6+3\sqrt5.$$ Define $$S=\sum_{m\ge2}\frac{a_mt^{2m}}{1-t^m}.$$ The elementary bounds $1/(1-t^m)\le1/(1-t^2)$ and $1/m\le1/2$ give the exact certificate $$\begin{aligned}
  S
  &\le \frac{Kt^4}{2(1-t^2)^2}
    =\frac{-87+39\sqrt5}{20} \notag\\
  &<a_1t^3=\frac{280-125\sqrt5}{11}.
  \label{eq:separation-certificate}\end{aligned}$$ The strict comparison is certified without decimals: $$a_1t^3-\frac{Kt^4}{2(1-t^2)^2}
   =\frac{6557-2929\sqrt5}{220}>0,\qquad
  6557^2-5\cdot2929^2=99044>0.$$

Write $\gamma_k=a_1r^{k+2}+R_k$, where the modes $m\ge2$ form $R_k$. Equation [\[eq:separation-certificate\]](#eq:separation-certificate){reference-type="eqref" reference="eq:separation-certificate"} implies, for every $k\ge0$, $$|R_k|+\sum_{j>k}|R_j|
  \le t^kS<a_1t^{k+3}.$$ The first mode alone has the exact gap $$a_1t^{k+2}-\sum_{j>k}a_1t^{j+2}
  =a_1t^{k+2}\frac{1-2t}{1-t}
  =a_1t^{k+3}.$$ Subtracting the higher-mode error proves full-tail domination. It also fixes the sign, while geometric decay of every $m\ge2$ mode proves the ratio limit.

If two binary digit sequences first differ at $k$, their images differ by at least $|\gamma_k|-\sum_{j>k}|\gamma_j|>0$. The digit map is therefore a continuous injection from compact $\mathbb Z_2$ into $\mathbb R$, hence a homeomorphism onto $K$. This proves the Cantor topology.

The ratio limit and the uniform gap give constants $C_1,C_2>0$ such that level-$n$ cylinders have diameter at most $C_2t^n$ and distinct level-$n$ cylinders are separated by at least $C_1t^{n-1}$. There are $2^n$ such cylinders. If $\mathcal N(K,\delta)$ is the least number of intervals of diameter at most $\delta$ needed to cover $K$, these two estimates give constants $c,C>0$, independent of $n$, for which $$c\,2^n\le \mathcal N(K,t^n)\le C\,2^n.$$ Thus both box dimensions equal $s_0=\log2/(-\log t)$, and the same cylinders give the Hausdorff upper bound. For the reverse Hausdorff bound, push the fair Bernoulli measure to $K$. Every level-$n$ cylinder has mass $2^{-n}$, and the separation estimate implies that an interval of radius comparable to $t^n$ meets at most a fixed number of them. Hence $\mu(I)\le C'|I|^{s_0}$, and the mass-distribution principle gives $\dim_HK\ge s_0$. Since $t=\varphi^{-2}$, $s_0=\log2/(2\log\varphi)$.

The set $K\subset\mathbb R$ is the image of the finite-size boundary map. It is not the original multiplicative shift, and its dimension is not a restatement of the leading shift dimensions in [@fan2012level; @kenyon2012hausdorff]. Nor does the argument analyze ordinary Minkowski content over all continuous covering scales.

# Dense radial singularities {#sec:natural}

Keep the binary golden control and set $E(0)=0$. The variable in $$G(z)=\sum_{N\ge0}E(N)z^N$$ marks the prefix cutoff $N$. Because [\[thm:qadic-boundary\]](#thm:qadic-boundary){reference-type="ref" reference="thm:qadic-boundary"} makes $E(N)$ bounded, $G$ is analytic on the open unit disk.

For an integer $Q\ge2$, periodicity gives the rational residue series $$R_Q(z):=\sum_{N\ge0}(N\bmod Q)z^N
  =\frac{P_Q(z)}{1-z^Q},\qquad
  P_Q(z)=\sum_{a=0}^{Q-1}az^a.
  \label{eq:residue-generating}$$ Writing $\Delta_v=d_v-d_{v-1}$, absolute convergence of $\sum_v|\Delta_v|$ permits the exact rearrangement $$G(z)=-\sum_{v\ge1}\frac{\Delta_v}{2^v}R_{2^v}(z),
  \qquad |z|<1.
  \label{eq:G-residue}$$

[\[thm:natural\]]{#thm:natural label="thm:natural"} Let $\xi$ be a primitive $2^v$-th root of unity, $v\ge1$. Then $$\lim_{s\uparrow1}(1-s)G(s\xi)
  =-\frac{\gamma_{v-1}}{2^{v-1}(1-\xi)}\ne0.
  \label{eq:radial-coefficient}$$ The unit circle is a natural boundary for $G$.

If $w<v$, then $1-\xi^{2^w}\ne0$, so the radial leading coefficient of $R_{2^w}$ vanishes. If $w\ge v$, set $Q=2^w$. Since $\xi^Q=1$ and $\xi\ne1$, differentiating the finite geometric sum gives $$P_Q(\xi)=-\frac{Q}{1-\xi}.$$ Together with $1-s^Q\sim Q(1-s)$, this implies $$\lim_{s\uparrow1}(1-s)R_Q(s\xi)=-\frac1{1-\xi}.
  \label{eq:residue-radial}$$ The limit may pass through [\[eq:G-residue\]](#eq:G-residue){reference-type="eqref" reference="eq:G-residue"}. Indeed, $$\frac{1-s}{Q}|R_Q(s\xi)|
  \le\frac{1-s}{Q}\sum_{N\ge0}Qs^N=1,$$ so the level-$w$ contribution is dominated by $|\Delta_w|$. Dominated convergence now yields $$\lim_{s\uparrow1}(1-s)G(s\xi)
  =\frac1{1-\xi}\sum_{w\ge v}\frac{\Delta_w}{2^w}.$$ By [\[eq:gamma-residue\]](#eq:gamma-residue){reference-type="eqref" reference="eq:gamma-residue"}, $\sum_{w\ge v}\Delta_w/2^w=-\gamma_{v-1}/2^{v-1}$, which proves [\[eq:radial-coefficient\]](#eq:radial-coefficient){reference-type="eqref" reference="eq:radial-coefficient"}; nonvanishing follows from [\[thm:golden\]](#thm:golden){reference-type="ref" reference="thm:golden"}.

Primitive dyadic roots are dense on the unit circle. If $G$ admitted analytic continuation across any boundary point, the continuation domain would contain an open boundary arc and hence a primitive dyadic root $\xi$. More explicitly, let $H$ be holomorphic on a neighborhood $U\ni\xi$ and agree with $G$ on $U\cap\mathbb D$, as forced by the identity theorem. Holomorphy makes $H$ bounded on some closed disk about $\xi$ contained in $U$. Equation [\[eq:radial-coefficient\]](#eq:radial-coefficient){reference-type="eqref" reference="eq:radial-coefficient"} instead makes $G(s\xi)=H(s\xi)$ unbounded like a nonzero multiple of $(1-s)^{-1}$ as $s\uparrow1$, a contradiction.

#### Normalization control.

The first nonreal control prevents a silent phase error. For $Q=4$ and $\xi=i$, $$P_4(i)=-2-2i=-\frac4{1-i},\qquad
  \lim_{s\uparrow1}(1-s)R_4(si)
  =-\frac1{1-i}=\frac{-1-i}{2}.$$ This differs from $i/(1-i)=(-1+i)/2$. The exact coefficient in [\[eq:radial-coefficient\]](#eq:radial-coefficient){reference-type="eqref" reference="eq:radial-coefficient"}, rather than a merely proportional expression, is therefore essential.

Equation [\[eq:radial-coefficient\]](#eq:radial-coefficient){reference-type="eqref" reference="eq:radial-coefficient"} is an Abelian radial statement. Because the singular boundary points are dense, they are not isolated poles of a meromorphic continuation. The conclusion is precisely the natural boundary and no stronger meromorphic assertion.

# Scope and conclusion {#sec:scope}

#### Scientific limits.

The primitive hypothesis is essential to the supplied Perron-gap proof. We do not infer the same theorem for reducible, irreducible-periodic, countable-state, or higher-step presentations. The Cantor and natural-boundary theorems belong only to the binary golden control, not to all $q,A$. The dimension is that of the real boundary image $E_{A,2}(\mathbb Z_2)$, not the original multiplicative shift, and no ordinary continuous-scale Minkowski-content statement is made. Finally, $G$ is an ordinary prefix-cutoff generating function: it is neither an Artin--Mazur zeta function nor a determinant or transfer trace.

#### Conclusion.

The subleading structure is a precise finite-size theorem. A one-site update reads the valuation of the cutoff; the summable deviations of ordinary word-count ratios turn those updates into a continuous real function on $\mathbb Z_q$; and explicit diverging representatives show that no boundary value is missed. In the golden case, the same coefficients control both a strongly separated Cantor image of dimension $\log2/(2\log\varphi)$ and dense radial obstruction to analytic continuation. These conclusions are exact, scoped, and independent of the finite replay that checks their implementations. The release-specific Route record and retrospective chronology are separated from the mathematical narrative in [9.5](#app:route-chronology){reference-type="ref" reference="app:route-chronology"}.

# Proof details {#app:proofs}

This appendix records the algebra suppressed from the main-text proofs. Every infinite conclusion is derived here or in [\[thm:qadic-boundary,thm:golden,thm:natural\]](#thm:qadic-boundary,thm:golden,thm:natural){reference-type="ref" reference="thm:qadic-boundary,thm:golden,thm:natural"}; finite computations are not used to close a limiting argument.

## Chain census and Perron decay

[\[lem:histogram\]]{#lem:histogram label="lem:histogram"} For every $N\ge1$ and $\ell\ge1$, the number of roots $i$ with $q\nmid i$ whose truncated chain has length exactly $\ell$ is $$C_\ell(N)=
  \lfloor N/q^{\ell-1}\rfloor
  -2\lfloor N/q^\ell\rfloor
  +\lfloor N/q^{\ell+1}\rfloor .$$ Moreover, $\sum_{\ell\ge1}\ell C_\ell(N)=N$.

The roots with chain length at least $\ell$ are the $i\le
N/q^{\ell-1}$ not divisible by $q$. Their number is $$\lfloor N/q^{\ell-1}\rfloor-\lfloor N/q^\ell\rfloor.$$ Subtracting the corresponding count at level $\ell+1$ gives the formula. Every site belongs to one chain, so summing chain lengths counts $\{1,\ldots,N\}$ once.

[\[lem:perron\]]{#lem:perron label="lem:perron"} For primitive $A$, the sequence $d_v=c_v-\log\rho(A)$ satisfies $$\sum_{v\ge0}|d_v|<\infty,\qquad
  \sum_{v\ge1}|d_v-d_{v-1}|<\infty.$$

Let $u,w$ be positive right and left Perron vectors, normalized by $w^Tu=1$. Finite-dimensional Jordan decomposition gives constants $C_1>0$, $0<\theta<1$, and $m\ge0$ for which $$A^{\ell-1}=\rho^{\ell-1}uw^T+
  O(\ell^m(\theta\rho)^\ell)$$ in any fixed matrix norm. Multiplication by $\mathbf 1^T$ and $\mathbf 1$ yields $$W_\ell=(\mathbf 1^Tu)(w^T\mathbf 1)\rho^{\ell-1}
  (1+O(\ell^m\theta^\ell)),$$ where the leading coefficient is positive. For sufficiently large $\ell$, the relative error has modulus below $1/2$; the logarithm is Lipschitz on that interval. Hence $$\log\frac{W_{v+1}}{W_v}=\log\rho+O(v^m\theta^v).$$ The first series follows after absorbing finitely many initial terms, and the second follows from $|d_v-d_{v-1}|\le|d_v|+|d_{v-1}|$.

## Exact summation by parts

Starting from [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"}, group cutoffs according to their valuation: $$\log Z(N)=\sum_{v\ge0}c_vA_v(N).$$ Only finitely many $A_v(N)$ are nonzero. Equation [\[eq:valuation-census\]](#eq:valuation-census){reference-type="eqref" reference="eq:valuation-census"} and $\sum_vA_v(N)=N$ give $$\log Z(N)-hN
  =\sum_{v\ge0}d_v
   (-\frac{r_v(N)}{q^v}
         +\frac{r_{v+1}(N)}{q^{v+1}}),$$ with $r_0(N)=0$. By [\[lem:perron\]](#lem:perron){reference-type="ref" reference="lem:perron"}, the index shift is absolutely convergent, so $$\log Z(N)-hN
  =-\sum_{v\ge1}(d_v-d_{v-1})\frac{r_v(N)}{q^v}.$$ This also gives a coefficientwise check. If $p_j=(q-1)/q^{j+1}$, then the coefficient of the formal variable $d_j$ on the left is $A_j(N)-Np_j$. On the right it is $$\begin{cases}
    r_1(N)/q,&j=0,\\[1mm]
    -r_j(N)/q^j+r_{j+1}(N)/q^{j+1},&j\ge1,
  \end{cases}$$ and [\[eq:valuation-census\]](#eq:valuation-census){reference-type="eqref" reference="eq:valuation-census"} makes the two expressions identical for every $j$.

## Both accumulation inclusions

The inverse limit $\mathbb Z_q$ is a closed subset of the product of the finite discrete spaces $\mathbb Z/q^v\mathbb Z$; it is compact. The partial sums in [\[eq:boundary-map\]](#eq:boundary-map){reference-type="eqref" reference="eq:boundary-map"} are continuous because each coordinate is locally constant. The majorant from [\[lem:perron\]](#lem:perron){reference-type="ref" reference="lem:perron"} is independent of $x$, so the Weierstrass test gives a continuous uniform limit.

Suppose $E(N_j)\to y$ along $N_j\to\infty$. Compactness supplies a further subsequence $N_{j_k}\to x$ in $\mathbb Z_q$. Since $E(N)=E_{A,q}(N)$ for positive integer states, continuity gives $y=E_{A,q}(x)$. This proves one inclusion without assuming that the original integer sequence converges $q$-adically.

For the other inclusion, fix $x\in\mathbb Z_q$ and define $$N_j=(x\bmod q^j)+q^j.$$ Then $N_j\ge q^j\to\infty$. For fixed $v$ and $j\ge v$, $$N_j\equiv x\bmod q^j\equiv x\bmod q^v\pmod{q^v},$$ so $N_j\to x$ in the inverse limit. Continuity proves $E(N_j)\to E_{A,q}(x)$. These two arguments establish [\[eq:acc-log\]](#eq:acc-log){reference-type="eqref" reference="eq:acc-log"}; applying the real exponential establishes [\[eq:acc-exp\]](#eq:acc-exp){reference-type="eqref" reference="eq:acc-exp"}.

## Derivation of the golden modes

Let $\Delta_v=d_v-d_{v-1}$. Substitution of the binary digits into [\[eq:boundary-map\]](#eq:boundary-map){reference-type="eqref" reference="eq:boundary-map"} is justified by $$\sum_{v\ge1}|\Delta_v|2^{-v}
  \sum_{k=0}^{v-1}2^k
  \le\sum_{v\ge1}|\Delta_v|<\infty.$$ It yields [\[eq:gamma-residue\]](#eq:gamma-residue){reference-type="eqref" reference="eq:gamma-residue"}. Define $$B_k=\sum_{j\ge1}\frac{d_{k+j}}{2^j}.$$ An index shift in [\[eq:gamma-residue\]](#eq:gamma-residue){reference-type="eqref" reference="eq:gamma-residue"} gives $$\gamma_k=\frac12(d_k-B_k).
  \label{eq:gamma-B}$$ Since $|r|<1$, $$d_k
  =\log(1-r^{k+3})-\log(1-r^{k+2})
  =\sum_{m\ge1}\frac{1-r^m}{m}r^{m(k+2)}.$$ For each $m$, $$\sum_{j\ge1}\frac{r^{mj}}{2^j}
  =\frac{r^m}{2-r^m}.$$ Absolute convergence permits the $j,m$ sums to be interchanged in $B_k$. Substituting the last two identities into [\[eq:gamma-B\]](#eq:gamma-B){reference-type="eqref" reference="eq:gamma-B"} gives $$\gamma_k=\sum_{m\ge1}
  \frac{(1-r^m)^2}{m(2-r^m)}r^{m(k+2)},$$ which is [\[eq:gamma-modes\]](#eq:gamma-modes){reference-type="eqref" reference="eq:gamma-modes"}.

## All-level separation and dimension

For completeness, we verify every algebraic comparison in [\[eq:separation-certificate\]](#eq:separation-certificate){reference-type="eqref" reference="eq:separation-certificate"}. Since $|1-r^m|\le1+t^m\le1+t^2$ and $2-r^m\ge2-t^2$ for $m\ge2$, $$a_m\le\frac1m\frac{(1+t^2)^2}{2-t^2}=\frac Km.$$ Therefore $$S\le\frac{K}{1-t^2}\sum_{m\ge2}\frac{t^{2m}}m
  \le\frac{K}{1-t^2}\frac12\sum_{m\ge2}t^{2m}
  =\frac{Kt^4}{2(1-t^2)^2}.$$ Reducing in $\mathbb Q(\sqrt5)$ gives the two displayed values in [\[eq:separation-certificate\]](#eq:separation-certificate){reference-type="eqref" reference="eq:separation-certificate"}. Both $6557$ and $2929\sqrt5$ are positive, and $$6557^2-(2929\sqrt5)^2=99044>0,$$ so the difference is strictly positive.

For $R_k=\sum_{m\ge2}a_mr^{m(k+2)}$, $$|R_k|+\sum_{j>k}|R_j|
  \le\sum_{m\ge2}\frac{a_mt^{m(k+2)}}{1-t^m}
  \le t^kS<a_1t^{k+3}.$$ The first-mode gap is also $a_1t^{k+3}$, because $1-2t=t(1-t)$. The difference is positive at every $k$, proving strong separation, while $|R_k|<a_1t^{k+2}$ proves $\operatorname{sgn}\gamma_k=(-1)^k$. Dividing by $a_1r^{k+2}$ and applying dominated convergence to the modes $m\ge2$ proves $\gamma_{k+1}/\gamma_k\to r$.

The ratio limit lets us choose $b_1,b_2>0$ with $$b_1t^k\le|\gamma_k|\le b_2t^k$$ for every $k$, after modifying the constants for finitely many initial indices. The level-$n$ tail diameter is at most $C_2t^n$, while the first-difference argument gives separation at least $C_1t^{n-1}$. For $s>s_0=\log2/(-\log t)$, the $2^n$ cylinders have total $s$-content at most $$2^n(C_2t^n)^s=C_2^s(2t^s)^n\longrightarrow0.$$ This proves the Hausdorff upper bound and the upper box bound.

For completeness, let $\mathcal N(K,\delta)$ be the minimum number of intervals of diameter at most $\delta$ covering $K$. A level-$n$ cylinder requires at most a fixed number of intervals of diameter $t^n$, while such an interval can meet at most a fixed number of the mutually $C_1t^{n-1}$-separated cylinders. Thus there are constants $c,C>0$ such that $$c\,2^n\le \mathcal N(K,t^n)\le C\,2^n \qquad(n\ge1).$$ Monotonicity for $t^{n+1}<\delta\le t^n$ proves both box dimensions are $s_0$.

Push the fair Bernoulli measure on $\{0,1\}^{\mathbb N}$ to $K$. Choose $n$ so that $t^{n+1}<R\le t^n$. Separation implies that an interval of radius $R$ meets at most a constant number $M$ of level-$n$ cylinders. Hence $$\mu(I)\le M2^{-n}=M(t^n)^{s_0}
  \le Mt^{-s_0}R^{s_0}.$$ The mass-distribution principle gives $\dim_HK\ge s_0$, while the same separation gives the lower box bound. This completes the proof of [\[thm:golden\]](#thm:golden){reference-type="ref" reference="thm:golden"}.

## Interchange and dominated radial passage

For $|z|<1$, $$\sum_{v\ge1}\frac{|\Delta_v|}{2^v}
  \sum_{N\ge0}(N\bmod2^v)|z|^N
  \le\frac1{1-|z|}\sum_{v\ge1}|\Delta_v|<\infty.$$ Thus the $N,v$ sums may be interchanged to obtain [\[eq:G-residue\]](#eq:G-residue){reference-type="eqref" reference="eq:G-residue"}. At a primitive $2^v$-th root $\xi$, the finite geometric derivative gives $$P_Q(\xi)=\sum_{a=0}^{Q-1}a\xi^a=-\frac Q{1-\xi}
  \qquad(Q=2^w,\;w\ge v).$$ For $s\in(0,1)$, $$(1-s)\frac{|R_Q(s\xi)|}{Q}\le1.$$ After multiplication by $|\Delta_w|/2^w=|\Delta_w|/Q$, this supplies the summable dominating sequence $(|\Delta_w|)$. Dominated convergence therefore proves [\[eq:radial-coefficient\]](#eq:radial-coefficient){reference-type="eqref" reference="eq:radial-coefficient"}. Its coefficient is nonzero by strong separation, and density plus the identity theorem gives the continuation contradiction in [\[thm:natural\]](#thm:natural){reference-type="ref" reference="thm:natural"}.

# Exact computational replay {#sec:replay}

This appendix is a reproducibility record for the non-anonymous release copy; it may be detached or anonymized for a venue using double-blind review. The mathematical results and proofs do not depend on it.

The computational layer checks finite consequences of the theorem package without supplying any step of its infinite proofs. Evaluator A enumerates labelings on literal source-graph components. Evaluator B independently expands the neutral inputs and uses the closed chain histogram, exact word counts, a positive Binet interval series, and cyclotomic quotient arithmetic. Their sources have distinct hashes, share no project-local imports, fixtures, or expected tables, and are compared by strict recursive type and value equality.

::: {#tab:canonical-replay}
  Field                            Exact stored value
  -------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Finite comparison                $580$ cases $=548$ theorem-domain $+32$ scope rejections; strict recursive type/value equality $=$ true; projection SHA-256 `a4d487bafa038c65526514f4f99811cb765dc390b7f952bdb651b963838ecaca`.
  Golden intervals and algebra     $33$ independently certified interval pairs, all overlapping; exact square-difference control $99044>0$.
  Positive controls                one-symbol `PASS`; full shifts `PASS`; golden prefix ledger `PASS_10_ROWS`.
  Evaluator source/output hashes   source A `87a71880cf49ea66fd4a9b71bfeef8466b6db60fe7597926c3767ff456f4d0a6`; source B `3c57736972f857b8fc239b58d9fe95b6900650dae1f6ff761662744b9f1d4fc5`; output A `0871d9c05f8bb32e05544ae2a690be3a2b0f052398f2efed3cd4fe180d1f1e6b`; output B `0b6f41f86008e48679a70e1485cb18a36463b8735baf440cfc6054d09b8898c9`.
  Adversarial replay               $19$ frozen mutation families, $20$ concrete instances, $52$ designated consumer invocations, $0$ survivors; $8$ frozen external-auditor mutations, $0$ survivors.
  Infinite-proof audit             uniform Perron majorant, reverse accumulation inclusion, all-level separation certificate, and dominated Abelian passage all certified; finite-grid-as-proof $=$ false.
  Source boundary                  Ban--Hu--Lai author-manuscript correction excerpt SHA-256 `b7c4aaf6c75e5a1790fc17f311242a8c56d6d23fd153657baed7dd93421c022f`; version-of-record line-checked $=$ false; leading-result novelty credit $=0$.
  Route                            primary $6/6$, independent $6/6$; tuple $[\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\mathrm{A4\_FAIL}]$; verdict $\mathrm{ROUTE\_A\_REJECTED}$; Route B invocation $=$ false; external $\mathrm{STOP\_DUPLICATE}$ remains live conditional and is not a Route terminal.
  Ledger and integrity             result ledger $22$ entries, SHA-256 `2397a01fb66e42980b9a71a6861350afe52ceb258d3ae119dcbeef58b4d3086e`; final integrity $15/15$; science SHA-256 `c988d083cbdd05a84f698497bfb6b8c13f9540fe3801497da9c7ce05d09f8e10`.
  Authority state                  State A; source commit `PREAUTHORITY_NO_COMMIT`; code commit `NONE`; authority writes $0$; Git operations $0$; paper manifest absent.

  : Canonical post-output block, transcribed from the protected authority artifacts identified in [9.3](#app:artifact-bindings){reference-type="ref" reference="app:artifact-bindings"}. Every value is retrospective. The block is an implementation audit only; it is not evidence for [\[thm:qadic-boundary,thm:golden,thm:natural\]](#thm:qadic-boundary,thm:golden,thm:natural){reference-type="ref" reference="thm:qadic-boundary,thm:golden,thm:natural"}.
:::

The finite cases include the exact golden prefix ledger $$Z(0),\ldots,Z(10)
  =1,2,3,6,10,20,30,60,96,192,288$$ and the one-symbol and full-shift zero boundaries. Coefficient intervals are certified with analytic tails rather than fitted from target values. The proof auditor, not either evaluator, owns the four infinite obligations listed in [2](#tab:canonical-replay){reference-type="ref" reference="tab:canonical-replay"}.

The literal evidence boundary stored by the comparison is $$\mathrm{FINITE\_RESULTS\_DO\_NOT\_PROVE\_INFINITE\_THEOREMS}.$$ Accordingly, the audit supports reproducibility and catches source, normalization, residue, interval, analytic-type, and ownership mutations; it does not upgrade numerical agreement into a proof or a novelty claim.

# Types, provenance, and reproducibility {#app:types}

The artifact-specific material in this appendix belongs to the non-anonymous reproducibility copy. It is deliberately separated from the theorem narrative and should be detached or anonymized for double-blind review.

## Object and marker firewall

::: {#tab:types}
  Symbol              Type and meaning                     Forbidden identification
  ------------------- ------------------------------------ -----------------------------------------------------------
  $X_A^{(q)}$         one-sided multiplicative SFT         additive shift or orbit ledger
  $N$                 positive prefix cutoff               orbit period or return time
  $Z(N)$              finite admissible prefix count       fixed-point count
  $x\in\mathbb Z_q$   inverse-limit residue state          real fractional part or a field element for composite $q$
  $E_{A,q}(x)$        real order-one boundary value        point of the original shift
  $z$ in $G(z)$       ordinary cutoff marker               zeta, norm, roof, or trace marker
  $\xi$               dyadic root used in a radial limit   isolated meromorphic pole

  : The objects used by the theorem have distinct types.
:::

The prefix convention is fixed as $\{1,\ldots,N\}$, and the source edge is $n\mapsto qn$. Replacing the prefix by $\{0,\ldots,N-1\}$, replacing the edge by $n\mapsto n+q$, or imposing an edge whose second endpoint lies outside the prefix changes [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"}. Likewise, $\operatorname{Acc}$ means subsequential limits along cutoffs tending to infinity, not the closure of values below a fixed bound.

## Source reconciliation

The source audit assigned zero novelty credit to the object, chain decomposition, product, Fibonacci counts, leading entropy and dimensions, boundary-complexity terminology, and valid results of @fan2012level [@kenyon2012hausdorff; @ban2019pattern; @ban2023boundary; @ban2025affine]. The digital-summatory literature provides a method neighbor [@madritsch2012summatory]; no priority inference is drawn from source searches.

For the correction in [2.1](#sec:bhl-correction){reference-type="ref" reference="sec:bhl-correction"}, the checked artifact was arXiv:2210.09115v1 and the bound excerpt has SHA-256 `b7c4aaf6c75e5a1790fc17f311242a8c56d6d23fd153657baed7dd93421c022f`. The source audit records $\mathrm{CORRECTION\_NOT\_NOVELTY\_NOT\_EXACT\_DUPLICATE}$ and version-of-record-line-checked $=$ false. This source distinction is part of the claim, not an editorial aside.

## Canonical artifact bindings {#app:artifact-bindings}

is mechanically traceable to the following protected files. Paths are relative to the Paper-44 authority package.

::: {#tab:bindings}
  Relative path   SHA-256
  --------------- --------------------------------------------------------------------
  Relative path   SHA-256
                  `1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd`
                  `a49bbc392e21a25e7f36ab8c0c5426bbec510aa30bc6d2d6943b0e81c5347984`
                  `9367109c025c885c11f2e49b9bdef0353b867efd618eb4698f171be8161757e0`
                  `1de200d9757fab8107bc5d11791c7a903034e97307d27f060a1b6b07b04130f0`
                  `059ecbc4edcd097cb9eb83a0452591735fc25ca6d6d8da5a3ce10f4cff15330f`
                  `a41d0e856d6f0473714f7c3e905e44a0b6832da0db9937ac07b16e8ce6d5a1e9`
                  `c988d083cbdd05a84f698497bfb6b8c13f9540fe3801497da9c7ce05d09f8e10`
                  `2397a01fb66e42980b9a71a6861350afe52ceb258d3ae119dcbeef58b4d3086e`
                  `f0185ab27834d8ebfe158c57cf8a25a46e745493d5a331ea459e582ebe4835e3`
                  `afd17de5efd811a90645efaf5aadf96cec0881a6b73d25966c1b081204708cde`
                  `9fffd522fe108d3c6cf9580a835757192020abbe967ef61354d1a1a8314ea0a3`
                  `966dee537ef56ae904ea09f9c8383d2f4092bc043224fff2b0fba436cf200e08`
                  `d9eb6ab3e767654e84d723bbe09ad21ddceccd8079ff2c042ab8584e53822a51`
                  `6d6d92202f299fa38328a156c9e0874d5fe649312b55403e25d845297c79eba7`
                  `95136972f0c9d0b554f3d7920bc470771bcb6c8cea4fa16a24880d8aec3f7b8e`
                  `66ae3af081047fa9f896346a1d0c4698b933f85de0812188b3df79db78817b86`
                  `21f9238294305d6adcff2c0afa66576c878f8a3d5b964b540a2372872261f9d6`
                  `32b37ae129c606fba2f12826379295232188809f0e75478b3c3149f37385a65f`

  : Protected source and result bindings used by the manuscript.
:::

## Protected-input and writer chronology

Before any writer-candidate file was created, all 62 regular files in the post-output authority package were enumerated with relative path, kind, mode, UID, GID, size, modification time, inode, link count, and SHA-256. There were no symbolic links. The resulting protected snapshot has SHA-256 `a364048f5be1f9b88dedae5cde2f92d69295e4f403d92da310bdda301479539a`. The repository baseline was commit `6e5658649d2eab0fce077cbcdcc00070dd54095f`; the Paper-44 authority directory was an untracked tree at that moment. Writing, review, figure generation, and compilation occur only in a temporary candidate directory.

Candidate selection was retrospective. An earlier finite-prime-square periodic census and an all-$k$ perfect-power operator candidate were stopped after source ownership was subtracted. The present position was assigned only after the exact remainder and golden controls were already known. Numerical adjacency among candidate or paper labels carries no scientific meaning.

## Route record and retrospective chronology {#app:route-chronology}

The exact strict Route tuple is $$[\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\mathrm{A4\_FAIL}],$$ with overall verdict $\mathrm{ROUTE\_A\_REJECTED}$; Route B was not invoked. The single positive coordinate, $\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE}$, records only the golden natural boundary. It does not create a periodic-orbit ledger, completed divisor, determinant comparison, or fixed self-adjoint Hilbert--Pólya operator. The external $\mathrm{STOP\_DUPLICATE}$ condition remains live but is not a Route terminal: locating a primary source with the exact theorem and quantifiers would end a standalone publication claim without invalidating the internal derivation.

The present candidate was chosen after the multiplicative-SFT literature, the exact remainder identity, the golden Binet control, the source subtractions, and the failures of earlier candidate assignments were known. Its survival after subtraction is not prospective selection, outcome-independent ranking, novelty, priority, or authorization. A proportional expression in an earlier Phase-2 note used $\xi/(1-\xi)$ for the residue bracket. Direct evaluation gives $-1/(1-\xi)$, as shown in [5](#sec:natural){reference-type="ref" reference="sec:natural"}; the corrected phase changes the coefficient but not nonvanishing or the natural-boundary conclusion. The paper uses only the corrected exact normalization.

## Reproducibility and disclosure

The canonical computations are CPU-only exact integer, rational, algebraic, and outward-rounded interval checks; there is no model training, target fitting, stochastic seed, or GPU dependence. A reproduction must use a disposable copy of the sealed package and must not run in the protected authority tree. The State-A integration command, namespace, and hostile environment checks are documented in the protected package README. The paper reports stored outputs rather than rerunning or modifying them.

Bibliographic metadata were checked against the DOI records and the frozen source audit; the six entries in `references.bib` are the six entries cited by the manuscript. Automated language-model reviews were used to stress-test the outline and presentation. They supplied no theorem premise, proof step, experimental value, source priority, or authorization claim.
