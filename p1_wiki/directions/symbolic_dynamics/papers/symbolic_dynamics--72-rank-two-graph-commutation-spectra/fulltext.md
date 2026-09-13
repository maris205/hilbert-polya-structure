---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--72-rank-two-graph-commutation-spectra"
canonical_tex: "symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra/main.tex"
canonical_pdf: "symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra/main.pdf"
source_sha256: "d23c4fc955b6f9a8956121fff1a1c3abe36df632bea9ea116cc4ffa5f244a4b2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rectangular Periodic Points and Commutation Transfer Spectra for One-Vertex $2$-Graph Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra/main.pdf>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/72-rank-two-graph-commutation-spectra/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the two-sided path action of a finite one-vertex $2$-graph, we reduce rectangular-sublattice fixed points to a finite commutation problem. At fixed horizontal period $a$, a single-red-letter transfer matrix $M_{\theta,a}$ satisfies $$|\operatorname{Fix}(\sigma^{(a,0)})\cap\operatorname{Fix}(\sigma^{(0,b)})|
   =\operatorname{tr}(M_{\theta,a}^{b}).$$ Consequently the vertical zeta function inside the horizontal-period-$a$ subsystem is $\det(I-zM_{\theta,a})^{-1}$. An explicit binary pair has the same vertex matrices and hence the same strictly-positive directional entropy, but different rectangular fixed-point data; this gives an entropy-blind obstruction to action-preserving $\mathbb Z^2$ conjugacy. The argument is factorization-theoretic, and an exhaustive finite control independently checks all $24$ binary commutation bijections through periods $a,b\leq3$.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Rectangular Periodic Points and Commutation Transfer Spectra for One-Vertex $2$-Graph Shifts'
```

## Markdown 正文

# Introduction

Higher-rank graphs package commuting factorizations into a category equipped with a degree functor. Their path spaces carry natural $\mathbb Z^k$ actions [@KumjianPask2000; @KumjianPask2003]; entropy for the canonical path shifts has been related to vertex matrices and their Perron--Frobenius data [@SkalskiZacharias2008]. In the one-vertex rank-two case, however, the vertex matrices remember only the numbers of blue and red generators. They do not remember the commutation bijection that fills each coloured square.

This note isolates a finite invariant that does remember that bijection. If $u$ is a blue word of length $a$ and $v$ a red word of length $b$, unique factorization writes $uv=v'u'$. A rectangular periodic path exists exactly when the boundary words close, $uv=vu$. Holding $a$ fixed and commuting one red letter at a time turns this condition into a closed walk in a finite multigraph on the $m^a$ blue boundary words. This yields the trace formula and the determinant zeta identity.

The scope is deliberately narrower than the established periodicity and orbit-equivalence theories. Higher-word commutation criteria already play a central role in rank-two graph periodicity [@DavidsonYang2009], while groupoid methods give broad orbit-equivalence frameworks [@CarlsenRout2021]. Most directly, recent work identifies full Mealy bijections with one-vertex rank-two graphs and two-sided Wang configurations, and relates aperiodicity to period-free configurations and anti-tori [@Pask2026]. We neither replace those results nor claim the first commutation/period dictionary. Our residual statement is quantitative: an exact rectangular fixed-point transfer formula and an explicit entropy-blind obstruction.

# One-vertex rank-two path shifts

Let $E=\{e_0,\ldots,e_{m-1}\}$ and $F=\{f_0,\ldots,f_{n-1}\}$. Fix a bijection $$\theta:E\times F\longrightarrow F\times E,
 \qquad \theta(e_i,f_j)=(f_{j'},e_{i'}),$$ and impose the relations $e_if_j=f_{j'}e_{i'}$. The resulting category $\Lambda_\theta$ is the one-vertex $2$-graph with degree $d(e_i)=(1,0)$ and $d(f_j)=(0,1)$. The defining property is unique factorization: whenever $d(\lambda)=p+q$, there are unique paths $\mu,\nu$ with $d(\mu)=p$, $d(\nu)=q$, and $\lambda=\mu\nu$ [@KumjianPask2000].

Let $X_\theta=\Lambda_\theta^\Delta$ be the two-sided path space, viewed as degree-preserving functors from $$\Delta_2=\{(p,q)\in\mathbb Z^2\times\mathbb Z^2:p\leq q\}$$ to $\Lambda_\theta$. Translation gives a $\mathbb Z^2$ action $(\sigma^g x)(p,q)=x(p+g,q+g)$ [@KumjianPask2003]. For $a,b\geq1$ set $$\operatorname{Per}_\theta(a,b)=
 \operatorname{Fix}(\sigma^{(a,0)})\cap\operatorname{Fix}(\sigma^{(0,b)}),
 \qquad P_\theta(a,b)=|\operatorname{Per}_\theta(a,b)|.$$ Thus $P_\theta(a,b)$ counts paths fixed by the rectangular sublattice $a\mathbb Z(1,0)+b\mathbb Z(0,1)$; it is not the fixed-point count of the single element $(a,b)$.

For $u\in E^a$ and $v\in F^b$, unique factorization gives unique $v'\in F^b$ and $u'\in E^a$ such that $uv=v'u'$. Write $$\Theta_{a,b}(u,v)=(v',u'),
 \qquad
 \widehat\Theta_{a,b}=\tau\circ\Theta_{a,b},$$ where $\tau(v',u')=(u',v')$. Thus $\widehat\Theta_{a,b}$ is a self-map of $E^a\times F^b$.

# Commuting boundary words

[\[thm:boundary\]]{#thm:boundary label="thm:boundary"} For every $a,b\geq1$, restriction to the lower and left boundary gives a bijection $$\operatorname{Per}_\theta(a,b)
 \longleftrightarrow
 \{(u,v)\in E^a\times F^b:uv=vu\}
 =\operatorname{Fix}(\widehat\Theta_{a,b}).$$

Let $x\in\operatorname{Per}_\theta(a,b)$, and put $u=x(0,(a,0))$, $v=x(0,(0,b))$. Horizontal periodicity identifies the red path on the right boundary with $v$, and vertical periodicity identifies the blue path on the top boundary with $u$. The two factorizations of $x(0,(a,b))$ are therefore $uv$ and $vu$, so $uv=vu$.

The pair $(u,v)$ determines the fundamental rectangle. Indeed, the path $uv$ has degree $(a,b)$, and unique factorization determines every subpath whose endpoints lie in that rectangle. Periodicity then determines all translates. This proves injectivity.

Conversely, suppose $uv=vu$. The words $u^rv^s$, $r,s\geq0$, form a compatible family: commutation makes $u^rv^s$ the prescribed-degree prefix of $u^{r'}v^{s'}$ whenever $r\leq r'$ and $s\leq s'$. Unique factorization therefore produces a one-sided path that is periodic by $(a,0)$ and $(0,b)$. Translate a finite subpath far enough into the nonnegative quadrant and use these two periods to define it; a common larger translate proves that the definition is independent of the choice. The resulting two-sided path lies in $\operatorname{Per}_\theta(a,b)$ and has boundary $(u,v)$.

The theorem separates two roles. Local coloured-square compatibility is already built into $\Lambda_\theta$; the sole global obstruction on a torus is closure of its two boundary words. It also avoids quotienting by spatial translation: $P_\theta(a,b)$ counts based periodic paths, as an ordinary fixed-point count should.

# The commutation transfer matrix

Fix $a\geq1$. For $u\in E^a$ and $0\leq j<n$, write $$u f_j=f_{\alpha_a(u,j)}\,\beta_a(u,j),
 \qquad \beta_a(u,j)\in E^a.$$ Define the $m^a\times m^a$ nonnegative integer matrix $$\label{eq:transfer}
 M_{\theta,a}(u,w)=
 \#\{j: \alpha_a(u,j)=j\ \text{and}\ \beta_a(u,j)=w\}.$$ The condition $\alpha_a(u,j)=j$ is essential: the red label must survive its passage across the blue boundary.

[\[thm:trace\]]{#thm:trace label="thm:trace"} For all $a,b\geq1$, $$P_\theta(a,b)=\operatorname{tr}(M_{\theta,a}^{b}).$$

Write $v=f_{j_1}\cdots f_{j_b}$ and set $u_0=u$. Commute the red letters successively: $$u_{t-1}f_{j_t}=f_{\ell_t}u_t,
 \qquad 1\leq t\leq b.$$ Then unique factorization gives $uv=f_{\ell_1}\cdots f_{\ell_b}u_b$. Equality with $vu$ holds exactly when $\ell_t=j_t$ for every $t$ and $u_b=u$. Thus commuting boundary pairs are in bijection with length-$b$ closed walks in the labelled multigraph whose adjacency matrix is [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. Summing the diagonal entries of $M_{\theta,a}^b$ proves the formula.

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} As a formal power series, $$Z_{\theta,a}(z)
 :=\exp\left(\sum_{b\geq1}\frac{P_\theta(a,b)}{b}z^b\right)
 =\frac{1}{\det(I-zM_{\theta,a})}.$$ The number of points in $\operatorname{Fix}(\sigma^{(a,0)})$ with least positive vertical period $b$ is $$Q_\theta(a,b)=\sum_{d\mid b}\mu(d)P_\theta(a,b/d).$$

The determinant identity follows from $-\log\det(I-zM)=\sum_{b\geq1}\operatorname{tr}(M^b)z^b/b$. The second formula is ordinary Möbius inversion in the vertical period, with $\mu$ the number-theoretic Möbius function. Here the horizontal period is only required to divide $a$.

This is a one-variable zeta function inside a fixed horizontal-period subsystem. We do not call it a full $\mathbb Z^2$ zeta function.

# An entropy-blind conjugacy obstruction

An action-preserving conjugacy carries every subgroup fixed set to the corresponding fixed set. Hence the full rectangular profile $\{P_\theta(a,b)\}_{a,b\geq1}$ is a $\mathbb Z^2$-conjugacy invariant.

Consider $m=n=2$. For the identity factorization $$e_i f_j=f_j e_i,$$ one has $M_{\mathrm{id},a}=2I_{2^a}$ and therefore $$\label{eq:idprofile}
 P_{\mathrm{id}}(a,b)=2^{a+b}.$$ Now take the explicit four-cycle $$\label{eq:cycle}
 e_i f_j=f_{i\oplus j}e_{1-i},\qquad i,j\in\{0,1\}.$$ Equivalently, $$\begin{array}{c@{\quad}c}
e_0f_0=f_0e_1,&e_0f_1=f_1e_1,\\
e_1f_0=f_1e_0,&e_1f_1=f_0e_0.
\end{array}$$ If $\theta(e_i,f_j)=(f_{j'},e_{i'})$ and $\pi(i,j)=(i',j')$, then this specific rule has $\pi=(00\ 10\ 01\ 11)$. The rule is fixed explicitly because the numerical conclusion below is not asserted for every four-cycle. In the word orders $(0,1)$ and $(00,01,10,11)$, respectively, $$M_{\mathrm{cyc},1}=
 \begin{pmatrix}0&2\\0&0\end{pmatrix},
 \qquad
 M_{\mathrm{cyc},2}=
 \begin{pmatrix}
 0&0&0&2\\0&0&0&0\\0&0&0&0\\2&0&0&0
 \end{pmatrix}.$$ Thus $$P_{\mathrm{cyc}}(1,1)=0,
 \qquad P_{\mathrm{cyc}}(2,2)=8,$$ whereas [\[eq:idprofile\]](#eq:idprofile){reference-type="eqref" reference="eq:idprofile"} gives $4$ and $16$.

Both examples have the same one-vertex coordinate matrices $[2]$ and $[2]$. For completeness, fix $p=(r,s)$ with $r,s\geq1$. Restriction to the bi-infinite $p$-diagonal gives a conjugacy $$(X_\theta,\sigma^p)\longrightarrow
 (\Lambda_\theta^p)^\mathbb Z,
 \qquad
 x\longmapsto\bigl(x(kp,(k+1)p)\bigr)_{k\in\mathbb Z}.$$ Strict positivity makes $\{kp:k\in\mathbb Z\}$ cofinal in both coordinate directions, so unique factorization reconstructs every finite subpath. Conversely, the one-vertex condition lets arbitrary degree-$p$ blocks concatenate. Since $|\Lambda_\theta^p|=2^{r+s}$, both examples have $$h_{\rm top}(\sigma^{(r,s)})=(r+s)\log2,
 \qquad r,s\geq1.$$ This direct argument is consistent with the broader positive-semigroup entropy theory [@SkalskiZacharias2008]. Nevertheless their rectangular fixed profiles differ.

Strictly-positive directional entropy and the two vertex matrices do not classify binary one-vertex $2$-graph shifts up to action-preserving $\mathbb Z^2$ conjugacy.

# Finite audit and scope

The accompanying exact control enumerates all $24$ bijections $\theta:\{0,1\}^2\to\{0,1\}^2$ and every $1\leq a,b\leq3$. For each of the $216$ triples it compares:

1.  direct block commutation of boundary words;

2.  the trace of $M_{\theta,a}^b$; and

3.  an independent enumeration of all $2^{2ab}$ blue/red edge labellings of the $(a,b)$ torus, checking only the local square relation.

All $216$ comparisons agree. The third implementation constructs neither boundary words nor transfer matrices, so it guards against a shared coding error in the first two. The calculation is regression evidence; the general proof is [\[thm:boundary,thm:trace\]](#thm:boundary,thm:trace){reference-type="ref" reference="thm:boundary,thm:trace"}.

Several nearby theories remain outside the claim surface. We do not claim the definition of a higher-rank path action, the general positive-semigroup entropy formula, the periodicity criterion of Davidson--Yang, a realization theorem for general two-dimensional SFTs [@PaskRaeburnWeaver2009], or a complete conjugacy invariant. The Mealy/square-complex/anti-torus dictionary and qualitative period-free criteria of @Pask2026 are also returned to their owner. Axis and mixed-sign directional entropy and general finite $k$-graphs are left open. Within those boundaries, the transfer matrix provides a concrete finite interface between categorical factorization and rectangular periodic dynamics.
