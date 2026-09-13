---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--116-max-plus-switching-induced-growth"
canonical_tex: "symbolic_dynamics/papers/116-max-plus-switching-induced-growth/main.tex"
canonical_pdf: "symbolic_dynamics/papers/116-max-plus-switching-induced-growth/main.pdf"
source_sha256: "0566bb95c4ed241f310505db5d8812cc600773a1ae3f04f65318ebdf84953e6b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Switching-Induced Growth for a Neutral Max-Plus Pair

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/116-max-plus-switching-induced-growth>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/116-max-plus-switching-induced-growth/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/116-max-plus-switching-induced-growth/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/116-max-plus-switching-induced-growth/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/116-max-plus-switching-induced-growth/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Consider the two max-plus matrices $$A=\begin{pmatrix}-2&-1\\1&-1\end{pmatrix},\qquad
   B=\begin{pmatrix}-1&1\\-1&-2\end{pmatrix}.$$ Each generator has tropical spectral radius zero, tropical rank two, and bounded powers, although four switching words of minimal length three have tropical rank one and reset the projective state. Nevertheless, if iid switching chooses $A$ with probability $p$ and $B$ with probability $1-p$, then every $0<p<1$ produces the strictly positive height rate $$\mu_p=\frac{3p(1-p)}{2+p(1-p)}.$$ We prove this anomaly by reducing the literal five-valued projective gap to an exact three-state Markov-additive process. The reduction gives the full finite-time height law, a cubic equation for its tilted Perron root, and a martingale central limit theorem with variance $$\sigma_p^2=
   \frac{4p(1-p)[1-p(1-p)][5-2p(1-p)]}{[2+p(1-p)]^3}.$$ The same cubic yields the analytic pressure and a large-deviation principle. Exact word geometry gives every parity-compatible height $n\bmod2,n\bmod2+2,\ldots,n$, with precisely two alternating maximizers, and determines both zero-temperature pressure edges. The deterministic endpoints $p=0,1$ are treated separately and have bounded height and zero growth. General max-plus laws of large numbers, central limit theorems, and large-deviation theory are prior framework rather than claims here. The note records only the explicit pair-specific conjunction; external circulation and all novelty or priority statements remain on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Switching-Induced Growth for a Neutral Max-Plus Pair'
```

## Markdown 正文

# Introduction {#sec:introduction}

Switching can create growth that neither deterministic mode possesses. The example in this paper makes that statement exact in the max-plus semiring: two full tropical-rank matrices have bounded powers and zero individual cycle time, but every nondegenerate Bernoulli mixture has positive linear height growth. The growth rate is not estimated numerically. It is the rational function $3p(1-p)/(2+p(1-p))$.

Max-plus products are a standard language for synchronized discrete-event systems [@BaccelliEtAl1992]. Finite projective automata and induced Markov chains, random max-plus Lyapunov exponents, coupling and memory loss, spectral-radius questions, and randomly switching max-plus systems already have substantial direct literatures [@Gaubert1995; @Mairesse1997; @BaccelliHong2000; @BlondelGaubertTsitsiklis2000; @MerletProjective2010; @GoverdeHeidergottMerlet2011; @vanDenBoomDeSchutter2012; @KordonisMaragosPapavassilopoulos2018]. General laws of large numbers, central and local limit theorems, renewal results, and large deviations for random topical operators are developed in [@Merlet2005; @Merlet2007; @Merlet2010]. All those general mechanisms and theorems are owner-subtracted background. Our purpose is narrower: for one displayed pair, we calculate its literal five-gap process, exact reward table and finite transfer formula, pair-specific rational drift and variance, cubic pressure, word extremes, and temperature constants.

Let $X_1,X_2,\ldots$ be iid, with $\mathbb{P}(X_t=A)=p$ and $\mathbb{P}(X_t=B)=q=1-p$. We use the chronological left product $$M_n=X_n\otimes\cdots\otimes X_1,
 \qquad H_n=\max_{i,j}(M_n)_{ij},
 \qquad H_0=0,$$ so $X_1$ acts first. This orientation matters at the matrix level. The central mechanism is a five-valued row-max gap. Negative gaps, zero, and positive gaps are strongly lumpable, including their height rewards, into a three-state chain. Four words of minimal length three have tropical rank one and reset the projective state. Such reset/coupling mechanisms are classical max-plus background; the calculations below use the explicit finite reward kernel rather than a regeneration decomposition.

The paper establishes four concrete claims.

1.  It proves literal strong lumping and the exact finite-time probability generating function $\mathbb{E}[y^{H_n}]=\mathbf e_{Z}^{\mathsf T}Q_p(y)^n\mathbf{1}$.

2.  It derives the stationary projective law, the positive drift $\mu_p$, and the nonzero CLT variance $\sigma_p^2$ in the interior. An explicit Poisson solution and Perron-root differentiation give two independent calculations of the variance once the literal kernel has been fixed.

3.  It identifies the analytic pressure, proves the corresponding LDP, and determines the exact word support and its two maximizers.

4.  It proves the two zero-temperature limits $$\Lambda_p(t)-t\longrightarrow\tfrac12\log(pq),\qquad
           \Lambda_p(t)\longrightarrow\tfrac12\log(1-2pq),$$ as $t\to+\infty$ and $t\to-\infty$, respectively.

Two complementary proof routes are kept visible. The tropical route uses raw matrix and vector multiplication to control orientation, rank, gaps, and word extrema. The Markov-additive route consumes that literal identification; it uses a tilted finite kernel for the stationary law, CLT, pressure, LDP, and temperature edges. Thus the routes are not logically independent. Their agreement is an internal correctness mechanism, not a novelty argument. The endpoints $p=0,1$ are never inferred by silently substituting into a primitive-chain proof.

handles the neutral generators and endpoints. proves the projective reduction and finite law. derive the interior limit and pressure packages. records ownership, internal comparisons, and exact controls. External release remains **HOLD**.

# Neutral generators and deterministic endpoints {#sec:generators}

On $\mathbb{R}\cup\{-\infty\}$, write $u\oplus v=\max\{u,v\}$ and $u\otimes v=u+v$. For compatible matrices, $$(C\otimes D)_{ij}=\max_k(C_{ik}+D_{kj}).$$ The max-plus identity has zero on the diagonal and $-\infty$ off the diagonal. Both generators in this paper have finite entries.

For a finite $2\times2$ matrix $C$, the tropical spectral radius is the maximum mean weight of a directed cycle: $$\rho_{\max}(C)=
 \max\left\{C_{11},C_{22},\frac{C_{12}+C_{21}}2\right\}.$$ Such a matrix has tropical rank one precisely when $C_{11}+C_{22}=C_{12}+C_{21}$, equivalently when its two rows differ by an additive scalar.

[\[prop:generators\]]{#prop:generators label="prop:generators"} For $$A=\begin{pmatrix}-2&-1\\1&-1\end{pmatrix},\qquad
 B=\begin{pmatrix}-1&1\\-1&-2\end{pmatrix},$$ one has $$\rho_{\max}(A)=\rho_{\max}(B)=0,
 \qquad \operatorname{rank}_{\mathrm{trop}}(A)=\operatorname{rank}_{\mathrm{trop}}(B)=2.$$ Both max-plus power sequences are bounded. More precisely, for $m\geq1$, $$\begin{aligned}
 A^{\otimes 2m}&=\begin{pmatrix}0&-2\\0&0\end{pmatrix},&
 A^{\otimes(2m+1)}&=\begin{pmatrix}-1&-1\\1&-1\end{pmatrix},\\
 B^{\otimes 2m}&=\begin{pmatrix}0&0\\-2&0\end{pmatrix},&
 B^{\otimes(2m+1)}&=\begin{pmatrix}-1&1\\-1&-1\end{pmatrix},\end{aligned}$$ where the two odd formulas apply for $m\geq1$; the first odd powers are $A$ and $B$ themselves. Consequently, $$\max_{i,j}(A^{\otimes n})_{ij}
 =\max_{i,j}(B^{\otimes n})_{ij}=n\bmod2,
 \qquad n\geq1.$$

For $A$, the two loop weights are $-2,-1$ and the two-cycle mean is $(-1+1)/2=0$. For $B$, the corresponding values are $-1,-2$ and $(1-1)/2=0$. This proves both spectral-radius statements. In each matrix the diagonal cross-sum is $-3$, whereas the off-diagonal cross-sum is zero; neither matrix has tropical rank one.

Direct multiplication gives the displayed second and third powers. Left multiplication by the same generator swaps its displayed even and stable odd forms. Induction proves all four power identities. Taking the largest entry gives the last assertion.

[\[prop:reset-words\]]{#prop:reset-words label="prop:reset-words"} Neither generator, and no word of length two, has tropical rank one. At length three, exactly four chronological words do: $$\begin{array}{c@{\qquad}c@{\qquad}c}
\toprule
\text{word}&X_3\otimes X_2\otimes X_1&
 \text{forced output gap}\\
\midrule
ABA&\begin{pmatrix}0&-2\\3&1\end{pmatrix}&-3\\[3pt]
ABB&\begin{pmatrix}1&-1\\1&-1\end{pmatrix}&0\\[3pt]
BAA&\begin{pmatrix}-1&1\\-1&1\end{pmatrix}&0\\[3pt]
BAB&\begin{pmatrix}1&3\\-2&0\end{pmatrix}&3\\
\bottomrule
\end{array}$$ Here a displayed word is in sampling order, so, for example, $ABB=B\otimes B\otimes A$. Each listed product sends every finite input vector to the stated projective gap.

For a finite $2\times2$ matrix $C$, set $\delta(C)=C_{11}+C_{22}-C_{12}-C_{21}$; tropical rank one is equivalent to $\delta(C)=0$. Direct chronological multiplication gives defects $$\begin{array}{c|cc}
\text{length one}&A&B\\ \hline
\delta&-3&-3
\end{array},\qquad
\begin{array}{c|cccc}
\text{length two}&AA&AB&BA&BB\\ \hline
\delta&2&1&1&2
\end{array},$$ and, in lexicographic order $AAA,AAB,ABA,ABB,BAA,BAB,BBA,BBB$, the length-three defects are $$-2,-1,0,0,0,0,-1,-2.$$ Thus the four displayed words are precisely the shortest rank-one words. Their products are obtained by the same literal multiplication. In those four matrices the first row minus the second is respectively $-3,0,0,3$ in both columns. Taking maxima after adding any finite input therefore gives the asserted constant output gaps.

[\[cor:endpoints\]]{#cor:endpoints label="cor:endpoints"} If $p=1$, then $M_n=A^{\otimes n}$; if $p=0$, then $M_n=B^{\otimes n}$. At either endpoint, $$H_n=n\bmod2,\qquad \frac{H_n}{n}\longrightarrow0,
 \qquad
 \lim_{n\to\infty}\frac1n\log\mathbb{E}e^{tH_n}=0
 \quad(t\in\mathbb{R}).$$ The centered fluctuation $(H_n-n\cdot0)/\sqrt n$ converges deterministically to zero.

The environment contains only one generator. The power calculation in [\[prop:generators\]](#prop:generators){reference-type="ref" reference="prop:generators"} gives every statement directly.

The endpoint proof uses neither a stationary projective distribution nor an irreducible Markov chain. Those interior tools enter only after the literal reduction below.

# Literal projective dynamics and the finite-time law {#sec:finite-law}

Set $\mathbf{0}=(0,0)^{\mathsf T}$ and write $$M_n\otimes\mathbf{0}=(u_n,v_n)^{\mathsf T},\qquad
 \Delta_n=u_n-v_n.$$ Because the two coordinates are the row maxima of $M_n$, $$\label{eq:height-vector}
 H_n=\max\{u_n,v_n\}.$$ To update the projective state, normalize a vector to $(d,0)^{\mathsf T}$. Literal max-plus multiplication gives $$\begin{aligned}
 A\otimes(d,0)^{\mathsf T}
 &=\bigl(\max\{d-2,-1\},\max\{d+1,-1\}\bigr)^{\mathsf T},
 \label{eq:A-gap-action}\\
 B\otimes(d,0)^{\mathsf T}
 &=\bigl(\max\{d-1,1\},\max\{d-1,-2\}\bigr)^{\mathsf T}.
 \label{eq:B-gap-action}\end{aligned}$$ The reward is the change in the coordinate maximum.

[\[thm:lumping\]]{#thm:lumping label="thm:lumping"} Starting from $\Delta_0=0$, the literal gap belongs to $$\mathcal D=\{-3,-2,0,2,3\}$$ at every time. Its next gap and height reward are as follows.

   current gap $d$   choose $A$: $(d',H'-H)$   choose $B$: $(d',H'-H)$
  ----------------- ------------------------- -------------------------
        $-3$                $(0,-1)$                  $(3,+1)$
        $-2$                $(0,-1)$                  $(3,+1)$
         $0$                $(-2,+1)$                 $(2,+1)$
         $2$                $(-3,+1)$                 $(0,-1)$
         $3$                $(-3,+1)$                 $(0,-1)$

Group the negative gaps as $N$, zero as $Z$, and the positive gaps as $P$. Then this partition is strongly lumpable jointly with the reward, and the lumped table is

   current state   choose $A$   choose $B$
  --------------- ------------ ------------
        $N$         $(Z,-1)$     $(P,+1)$
        $Z$         $(N,+1)$     $(P,+1)$
        $P$         $(N,+1)$     $(Z,-1)$

The accumulated reward equals the literal matrix height $H_n$ for every chronological word.

Evaluate [\[eq:A-gap-action\]](#eq:A-gap-action){reference-type="eqref" reference="eq:A-gap-action"}--[\[eq:B-gap-action\]](#eq:B-gap-action){reference-type="eqref" reference="eq:B-gap-action"} at the five values in $\mathcal D$ and subtract the old maximum $\max\{d,0\}$. This gives the first table. Every listed next gap again lies in $\mathcal D$, so induction proves confinement. All five values really occur: the empty word has gap $0$, the one-letter words $A,B$ have gaps $-2,2$, and the words $AB,BA$ have gaps $3,-3$, respectively.

The two representatives of $N$ have the same target lump and reward under each generator; the same is true for the two representatives of $P$. The singleton $Z$ causes no ambiguity. This proves strong reward lumping and the second table. Finally, [\[eq:height-vector\]](#eq:height-vector){reference-type="eqref" reference="eq:height-vector"} identifies each literal maximum increment with the table reward. Since $H_0=0$, summing the rewards gives $H_n$.

The orientation is fixed before this reduction. For example, the word $A,A,B$ means $B\otimes A\otimes A$ and gives $$\begin{pmatrix}1&1\\-1&-2\end{pmatrix},$$ whereas the reversed word gives a different matrix. Thus the construction does not silently commute the generators.

[\[thm:finite-pgf\]]{#thm:finite-pgf label="thm:finite-pgf"} Let $0\leq p\leq1$, $q=1-p$, and $y>0$. With state order $(N,Z,P)$, define $$\label{eq:Q}
 Q_p(y)=
 \begin{pmatrix}
 0&p/y&qy\\
 py&0&qy\\
 py&q/y&0
 \end{pmatrix}.$$ Then, for every $n\geq0$, $$\label{eq:finite-pgf}
 \boxed{\quad
 \mathbb{E}[y^{H_n}]=\mathbf e_{Z}^{\mathsf T}Q_p(y)^n\mathbf{1}.
 \quad}$$ Writing $a=pq$, one also has $$\label{eq:cubic}
 \boxed{\quad
 \det(rI-Q_p(y))
 =r^3+(2a-1-ay^2)r-ay.
 \quad}$$

For a transition of probability $w$ and reward $g$, put $wy^g$ in its matrix entry. The reward table in [\[thm:lumping\]](#thm:lumping){reference-type="ref" reference="thm:lumping"} gives exactly [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. If the row vector $m_n$ records $\mathbb{E}[y^{H_n}\mathbf 1_{\{S_n=s\}}]$, then $m_0=\mathbf e_{Z}^{\mathsf T}$ and $m_{n+1}=m_nQ_p(y)$. Summing over the terminal state proves [\[eq:finite-pgf\]](#eq:finite-pgf){reference-type="eqref" reference="eq:finite-pgf"}, including $n=0$.

For the determinant, the three two-cycles contribute $p^2$, $q^2$, and $pqy^2$ to the coefficient of $-r$. The two oriented three-cycles have total weight $p^2qy+pq^2y=pqy$. Hence $$\det(rI-Q_p(y))
 =r^3-(p^2+q^2+pqy^2)r-pqy.$$ Using $p^2+q^2=1-2pq$ gives [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"}.

For $0<p<1$, $Q_p(y)$ is primitive for every $y>0$: its directed graph has positive two-cycles and three-cycles. This observation supplies all finite-dimensional spectral hypotheses used below.

# Interior drift and Gaussian fluctuations {#sec:limits}

Throughout this section, $0<p<1$, $q=1-p$, and $a=pq$. At zero tilt, $P_p:=Q_p(1)$ is the transition matrix of the lumped projective chain.

[\[lem:stationary\]]{#lem:stationary label="lem:stationary"} The unique stationary row vector of $P_p$ is $$\label{eq:stationary}
 \boxed{\quad
 \pi_N=\frac{p}{1+p},\qquad
 \pi_Z=\frac{1-a}{2+a},\qquad
 \pi_P=\frac{q}{1+q}.
 \quad}$$ Its stationary mean reward is $$\label{eq:drift}
 \boxed{\quad \mu_p=\frac{3a}{2+a}>0.\quad}$$

Every transition into $N$ uses $A$, except the transition from $N$ itself. Stationarity therefore gives $\pi_N=p(1-\pi_N)$ and hence $\pi_N=p/(1+p)$. Likewise, $\pi_P=q(1-\pi_P)$, so $\pi_P=q/(1+q)$. The remaining mass is $$1-\frac{p}{1+p}-\frac{q}{1+q}=\frac{1-a}{2+a}.$$ Only $N\xrightarrow{A}Z$ and $P\xrightarrow{B}Z$ carry reward $-1$. All other transitions carry reward $+1$. Thus $$\begin{aligned}
 \mu_p
 &=1-2(p\pi_N+q\pi_P)\\
 &=1-2\left(\frac{p^2}{1+p}+\frac{q^2}{1+q}\right)
 =1-\frac{2(1-a)}{2+a}=\frac{3a}{2+a}.\end{aligned}$$

[\[thm:slln-clt\]]{#thm:slln-clt label="thm:slln-clt"} For every $0<p<1$, $$\label{eq:slln}
 \frac{H_n}{n}\longrightarrow\mu_p=\frac{3a}{2+a}
 \qquad\text{almost surely}.$$ Moreover, $$\label{eq:clt}
 \frac{H_n-n\mu_p}{\sqrt n}
 \xrightarrow{\mathrm d}\mathcal N(0,\sigma_p^2),$$ where $$\label{eq:variance}
 \boxed{\quad
 \sigma_p^2=
 \frac{4a(1-a)(5-2a)}{(2+a)^3}>0.
 \quad}$$

Let $g(i,\ell)\in\{-1,+1\}$ be the reward from state $i$ when the letter is $\ell\in\{A,B\}$. The conditional reward means are $$f_N=q-p,\qquad f_Z=1,\qquad f_P=p-q.$$ The finite chain is irreducible and aperiodic. The ergodic theorem applied to its transition rewards proves [\[eq:slln\]](#eq:slln){reference-type="eqref" reference="eq:slln"} with the stationary mean in [\[lem:stationary\]](#lem:stationary){reference-type="ref" reference="lem:stationary"}.

To calculate fluctuations rather than cite an unspecified variance, solve the Poisson equation $$(I-P_p)h=f-\mu_p\mathbf{1}.$$ Direct substitution gives the bounded solution $$\label{eq:poisson-solution}
 h_N=-\frac{2p}{1+p},\qquad h_Z=0,
 \qquad h_P=-\frac{2q}{1+q}.$$ If $S_k$ is the projective state after $k$ letters, then $$\label{eq:martingale-difference}
 D_k=g(S_{k-1},X_k)-\mu_p+h(S_k)-h(S_{k-1})$$ has conditional mean zero. Indeed, conditioning on $S_{k-1}=i$ gives $f_i-\mu_p+(P_ph)_i-h_i=0$. The six state--letter values of $D_k$ are

   state          letter $A$                letter $B$
  ------- -------------------------- -------------------------
    $N$          $-2q/(1+q)$                $2p/(1+q)$
    $Z$    $-2q(2p-1)/[(1+p)(1+q)]$   $2p(2p-1)/[(1+p)(1+q)]$
    $P$           $2q/(1+p)$                $-2p/(1+p)$

Consequently, the stationary conditional second moment is $$\begin{aligned}
 \sum_i\pi_i\mathbb{E}(D_k^2\mid S_{k-1}=i)
 &=4a\left[
 \frac{\pi_N}{(1+q)^2}
 +\frac{\pi_Z(2p-1)^2}{(1+p)^2(1+q)^2}
 +\frac{\pi_P}{(1+p)^2}\right] \notag\\
 &=\frac{4a(1-a)(5-2a)}{(2+a)^3}.
 \label{eq:variance-derivation}\end{aligned}$$ The last equality uses $(1+p)(1+q)=2+a$ and $(2p-1)^2=1-4a$.

Summing [\[eq:martingale-difference\]](#eq:martingale-difference){reference-type="eqref" reference="eq:martingale-difference"} yields $$H_n-n\mu_p=\sum_{k=1}^nD_k+h(S_0)-h(S_n).$$ The final difference is bounded. The conditional quadratic variation of the martingale, divided by $n$, converges almost surely to [\[eq:variance-derivation\]](#eq:variance-derivation){reference-type="eqref" reference="eq:variance-derivation"} by the finite-chain ergodic theorem. The increments are bounded, so the conditional Lindeberg condition holds. The martingale central limit theorem [@HallHeyde1980 Theorem 3.2] proves [\[eq:clt\]](#eq:clt){reference-type="eqref" reference="eq:clt"}. Since $0<a\leq1/4$, every factor in [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"} is positive.

The tilted cubic gives an additional algebraic check. Once the literal kernel is fixed, its variance calculation is independent of the Poisson calculation above; the two proof routes as a whole are complementary.

[\[prop:perron-derivatives\]]{#prop:perron-derivatives label="prop:perron-derivatives"} Let $\rho_p(t)=\rho_{\mathrm{PF}}(Q_p(e^t))$ for $0<p<1$. Then $$\rho_p(0)=1,\qquad
 (\log\rho_p)'(0)=\mu_p,\qquad
 (\log\rho_p)''(0)=\sigma_p^2.$$

Set $$F(r,t)=r^3+(2a-1-ae^{2t})r-ae^t.$$ At $(r,t)=(1,0)$, $$F_r=2+a,\quad F_t=-3a,\quad
 F_{rr}=6,\quad F_{rt}=-2a,\quad F_{tt}=-5a.$$ Implicit differentiation of $F(\rho_p(t),t)=0$ gives $$\rho_p'(0)=\frac{3a}{2+a}=\mu_p$$ and $$(2+a)\rho_p''(0)+6\mu_p^2-4a\mu_p-5a=0.$$ Therefore $$\begin{aligned}
 (\log\rho_p)''(0)
 &=\rho_p''(0)-\mu_p^2\\
 &=\frac{5a+4a\mu_p-(8+a)\mu_p^2}{2+a}
 =\frac{4a(1-a)(5-2a)}{(2+a)^3}.\end{aligned}$$ This independently agrees with the martingale variance calculation in [\[eq:variance-derivation\]](#eq:variance-derivation){reference-type="eqref" reference="eq:variance-derivation"}.

# Pressure, exact words, and temperature edges {#sec:pressure}

For $0<p<1$, define the height pressure $$\label{eq:pressure-definition}
 \Lambda_p(t)=\lim_{n\to\infty}\frac1n
 \log\mathbb{E}e^{tH_n},\qquad t\in\mathbb{R}.$$

[\[thm:pressure-ldp\]]{#thm:pressure-ldp label="thm:pressure-ldp"} For $0<p<1$, the limit in [\[eq:pressure-definition\]](#eq:pressure-definition){reference-type="eqref" reference="eq:pressure-definition"} exists and equals $$\label{eq:pressure}
 \boxed{\quad
 \Lambda_p(t)=\log\rho_{\mathrm{PF}}(Q_p(e^t)),
 \quad}$$ where the Perron root is the largest positive root of $$\label{eq:pressure-cubic}
 r^3+(2a-1-ae^{2t})r-ae^t=0.$$ The function $\Lambda_p$ is real analytic on $\mathbb{R}$. The variables $H_n/n$ satisfy a full LDP with speed $n$ and good convex rate $$\label{eq:rate}
 I_p(x)=\sup_{t\in\mathbb{R}}\{tx-\Lambda_p(t)\},$$ with $I_p(x)=+\infty$ outside $[0,1]$ and $I_p(\mu_p)=0$.

By [\[thm:finite-pgf\]](#thm:finite-pgf){reference-type="ref" reference="thm:finite-pgf"}, the exponential moment is $\mathbf e_{Z}^{\mathsf T}Q_p(e^t)^n\mathbf{1}$. The matrix is primitive for every real $t$, so Perron--Frobenius theory gives the exponential rate [\[eq:pressure\]](#eq:pressure){reference-type="eqref" reference="eq:pressure"}; the initial and terminal vectors have nonzero pairing with the positive Perron eigenvectors. Simplicity of the Perron root and analytic perturbation of a finite matrix give real analyticity. The cubic is [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"} with $y=e^t$.

The height is bounded between $0$ and $n$, as proved more sharply in [\[prop:word-geometry\]](#prop:word-geometry){reference-type="ref" reference="prop:word-geometry"}; hence $H_n/n$ is supported on the compact set $[0,1]$ and the sequence is exponentially tight. The limiting cumulant generating function is finite and differentiable on its entire effective domain $\mathbb{R}$ (indeed analytic there). Its domain has no boundary, so the steepness condition is vacuous, and lower semicontinuity follows from continuity. These are the essential-smoothness hypotheses of the Gärtner--Ellis theorem [@DemboZeitouni2010]; together with exponential tightness they give the full LDP with the good Legendre transform [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"}. The support bound gives infinite rate outside $[0,1]$, and [\[prop:perron-derivatives\]](#prop:perron-derivatives){reference-type="ref" reference="prop:perron-derivatives"} gives $\Lambda_p'(0)=\mu_p$, so $I_p(\mu_p)=0$.

[\[prop:word-geometry\]]{#prop:word-geometry label="prop:word-geometry"} For every word of length $n$, $$\label{eq:word-bounds}
 \boxed{\quad n\bmod2\leq H_n\leq n.\quad}$$ More precisely, the set of attainable heights is $$\label{eq:exact-height-support}
 \boxed{\quad
 \{H_n(w):w\in\{A,B\}^n\}
 =\{n-2k:0\leq k\leq\lfloor n/2\rfloor\}.
 \quad}$$ For each $n\geq1$, exactly the two alternating words attain $H_n=n$; the two constant words attain $H_n=n\bmod2$.

For $0<p<1$ and $a=pq$, $$\label{eq:max-mass}
 \mathbb{P}(H_n=n)=
 \begin{cases}
 2a^{n/2},&n\text{ even},\\
 a^{(n-1)/2},&n\text{ odd}.
 \end{cases}$$ For $m\geq0$, $$\label{eq:min-mass}
 \mathbb{P}(H_{2m}=0)=(p^2+q^2)^m=(1-2a)^m.$$

Every reward in [\[thm:lumping\]](#thm:lumping){reference-type="ref" reference="thm:lumping"} is $+1$ or $-1$. A negative reward always lands in $Z$, and every transition out of $Z$ has reward $+1$. Thus negative rewards are isolated. Among $n$ rewards there are at most $\lfloor n/2\rfloor$ negative ones, proving the lower bound; the upper bound is immediate. Constant words alternate rewards $+1,-1,+1,-1,\ldots$ and attain the lower edge.

Every reward is odd, so $H_n\equiv n\pmod2$. Conversely, fix $0\leq k\leq\lfloor n/2\rfloor$. The prefix $(AA)^k$ consists of $k$ reward pairs $(+1,-1)$ and returns the state to $Z$ after every block. Append an alternating suffix of length $n-2k$, beginning with either letter. From $Z$ this suffix has reward $+1$ at every step. The resulting word has height $n-2k$, proving [\[eq:exact-height-support\]](#eq:exact-height-support){reference-type="eqref" reference="eq:exact-height-support"}.

To attain the upper edge, a word must avoid every negative transition. After an initial $A$, the state is $N$, so the next letter must be $B$; the state is then $P$, so the next letter must be $A$. This forces alternation. Starting with $B$ forces the other alternating word. Their Bernoulli masses give [\[eq:max-mass\]](#eq:max-mass){reference-type="eqref" reference="eq:max-mass"}.

For $H_{2m}=0$, every successive reward pair must be $(+1,-1)$. Starting from $Z$, such a pair is produced precisely by the blocks $AA$ and $BB$, each returning to $Z$. Independent blocks have total mass $p^2+q^2$, which proves [\[eq:min-mass\]](#eq:min-mass){reference-type="eqref" reference="eq:min-mass"}.

[\[thm:temperature\]]{#thm:temperature label="thm:temperature"} For $0<p<1$, $$\begin{aligned}
 \Lambda_p(t)-t&\longrightarrow\frac12\log(pq)
 &&\text{as }t\to+\infty,\label{eq:positive-edge}\\
 \Lambda_p(t)&\longrightarrow\frac12\log(1-2pq)
 &&\text{as }t\to-\infty.\label{eq:negative-edge}\end{aligned}$$

Put $y=e^t$. At the positive edge, $$\frac{Q_p(y)}{y}\longrightarrow
 L_+=\begin{pmatrix}0&0&q\\p&0&q\\p&0&0\end{pmatrix}
 \qquad(y\to\infty).$$ The characteristic polynomial of $L_+$ is $r(r^2-pq)$, so $\rho_{\mathrm{PF}}(L_+)=\sqrt{pq}$. Continuity of the spectral radius gives $\rho_{\mathrm{PF}}(Q_p(y))/y\to\sqrt{pq}$, which is [\[eq:positive-edge\]](#eq:positive-edge){reference-type="eqref" reference="eq:positive-edge"}. The alternating-word probability in [\[eq:max-mass\]](#eq:max-mass){reference-type="eqref" reference="eq:max-mass"} independently exhibits the same exponential coefficient.

At the negative edge, first remove the singular weights by setting $$D_y=\operatorname{diag}(y^{-1},1,y^{-1}).$$ Then $$\label{eq:negative-similarity}
 D_y^{-1}Q_p(y)D_y
 =\begin{pmatrix}0&p&qy\\p&0&q\\py&q&0\end{pmatrix}
 \longrightarrow
 L_-:=\begin{pmatrix}0&p&0\\p&0&q\\0&q&0\end{pmatrix}$$ as $y\downarrow0$. Similar matrices have the same spectrum, and the characteristic polynomial of $L_-$ is $r(r^2-p^2-q^2)$. Therefore $$\rho_{\mathrm{PF}}(Q_p(y))\longrightarrow\sqrt{p^2+q^2}
 =\sqrt{1-2pq},$$ which proves [\[eq:negative-edge\]](#eq:negative-edge){reference-type="eqref" reference="eq:negative-edge"}. The minimum-event identity [\[eq:min-mass\]](#eq:min-mass){reference-type="eqref" reference="eq:min-mass"} gives the same exponential constant.

At $p=0,1$, [\[cor:endpoints\]](#cor:endpoints){reference-type="ref" reference="cor:endpoints"} gives $\Lambda_p(t)=0$ for every fixed $t$. These deterministic pressures are not obtained by inserting an endpoint into [\[eq:positive-edge\]](#eq:positive-edge){reference-type="eqref" reference="eq:positive-edge"}, whose hypothesis is $0<p<1$. The deterministic sequence $H_n/n$ also has the elementary LDP with rate zero at $0$ and $+\infty$ elsewhere.

# Proof architecture, ownership, and exact controls {#sec:scope}

## Two complementary proof routes

The argument separates primitive data before comparing conclusions.

  route                         primitive calculation                                                                                                                                                                                                                                           outputs and failure controls
  ----------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
  Tropical literal/projective   Raw chronological matrix products, row maxima, and the gap formulas [\[eq:A-gap-action\]](#eq:A-gap-action){reference-type="eqref" reference="eq:A-gap-action"}--[\[eq:B-gap-action\]](#eq:B-gap-action){reference-type="eqref" reference="eq:B-gap-action"}.   Generator powers and ranks, orientation, shortest reset words, five reachable gaps, reward lumping, exact word support, and forced alternating maximizers.
  Markov-additive spectral      The reward-tilted kernel [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}, its stationary chain, Poisson equation, and characteristic cubic.                                                                                                          Finite PGF, drift, martingale variance, Perron derivatives, pressure, LDP, and both scaled spectral limits.

The first route supplies the reward kernel used by the second; the routes are therefore complementary, not independent. The first can fail if the chronological product or row maximum is reversed, while the second can fail if a reward sign or Bernoulli weight is placed in the wrong entry. Once the kernel is fixed, the Poisson-equation and Perron-derivative calculations of the variance are independent checks.

## Owner subtraction

The max-plus algebra and its discrete-event interpretation are established background [@BaccelliEtAl1992]. Direct prior owners include Gaubert's performance evaluation of max-plus automata [@Gaubert1995], Mairesse's theory of irreducible random max-plus products [@Mairesse1997], and the analytic treatment of max-plus Lyapunov exponents by Baccelli and Hong [@BaccelliHong2000]. Spectral-radius questions for sets of max-algebraic matrices are treated by Blondel, Gaubert, and Tsitsiklis [@BlondelGaubertTsitsiklis2000]; projective semigroups and memory-loss mechanisms are treated by Merlet [@MerletProjective2010; @Merlet2010]. Coupling-based Lyapunov estimation, random and deterministic switching models, and Markov-jump max-plus systems appear respectively in [@GoverdeHeidergottMerlet2011; @vanDenBoomDeSchutter2012; @KordonisMaragosPapavassilopoulos2018]. Broad topical-operator SLLNs, CLTs, and LDPs are likewise available [@Merlet2005; @Merlet2007]. We assign zero credit here to all of those general engines and to the following consequences:

-   existence of a cycle time or law of large numbers for a generic random max-plus product;

-   a generic central or local limit theorem under memory loss;

-   a generic large-deviation principle or spectral-gap method;

-   Perron--Frobenius theory for a finite tilted kernel.

-   reset-word, coupling, or regeneration mechanisms for random max-plus products, and switching max-plus terminology.

The residual scope is only the explicit calculation for the displayed pair: its five literal gaps, three-state reward table, rational drift and variance, cubic transfer/pressure equation, exact word support and extreme masses, and the two temperature constants. We have not exhausted equivalence classes under row or column scalings, permutations, transpose, or additive normalization, so even pair-level distinctness is not asserted. This scope description and any bounded owner search are not novelty or priority evidence. Specialist owner review is required before any external use.

## Internal mechanism comparisons

  paper   occupied mechanism                                                                                        separation in the present system
  ------- --------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  P89     Bernoulli reset in a random subshift and regeneration structure.                                          The present pair also has reset words: precisely four shortest rank-one words occur at length three. The distinction is the finite max-plus projective state, additive height reward, and direct three-state-kernel proof; it is not absence of coupling or regeneration.
  P93     Push--pop/free-reduction dynamics and reflected stack height.                                             The projective gap has five literal values and no unbounded stack; the height is a max-plus matrix maximum.
  P101    Random cap--floor synchronization and order-statistic coalescence.                                        There is no cap, floor, coalescence time, or synchronized particle system.
  P104    Contracting ordinary monomial cocycle, occupation parity, singular values, and multiplicative pressure.   The matrices are finite max-plus and non-monomial; the observable is an additive global maximum with a three-state reward process.
  P111    Positive Heisenberg product whose central entry is a quadratic ordered-subword area.                      The current matrices are not unipotent; $H_n$ is order $n$, has $\sqrt n$ fluctuations, and is not a scattered-subword count.

## Exact finite controls and limitations

The standard-library program `code/verify.py` uses only integers and `fractions.Fraction`. A fresh author run passed **1,183,356 exact assertions**. It includes:

-   literal products, literal vector actions, five-gap updates, and lumped rewards for all $131{,}071$ words through length $16$;

-   a nonpalindromic orientation sentinel, the empty word, deterministic powers through exponent $64$, both generator-rank tests, and exhaustive reset-word classification through length three with exact matrices and constant output gaps;

-   exhaustive histograms versus an independent dynamic program, plus explicit witnesses for every parity-compatible height, biased finite laws, and PGFs through time $32$ at seven probabilities;

-   exact stationarity, Poisson, variance, implicit-derivative, cubic, similarity, endpoint, and rare-event identities.

The stored stdout is `code/verify.out`. These checks can falsify a finite formula or convention. They do not prove an asymptotic theorem, external ownership, novelty, or priority. No simulation or floating-point output is used as evidence.

# Conclusion {#sec:conclusion}

The displayed max-plus pair has a sharp switching boundary. Each generator alone has bounded powers and zero height rate, yet every iid mixture with $0<p<1$ grows at the positive rate $3p(1-p)/(2+p(1-p))$. A literal five-gap calculation explains the mechanism and proves the exact three-state finite-time law. Four shortest length-three products are rank-one projective resets, a classical kind of coupling mechanism whose occurrence is explicitly separated from the pair-specific calculation. The tilted kernel then yields the explicit Gaussian variance, analytic pressure, LDP, exact word support, and both zero-temperature constants.

The result is intentionally pair-specific. It does not classify neutral max-plus pairs, quantify robustness under perturbations, or replace generic topical-operator limit theory. A natural next mathematical question is to characterize which finite families of zero-cycle-time, non-rank-one generators admit a finite projective quotient with positive switching rate. That question is outside the present proof package.

This manuscript is anonymous. Public posting, submission, specialist contact, and every novelty or priority claim remain **HOLD**.
