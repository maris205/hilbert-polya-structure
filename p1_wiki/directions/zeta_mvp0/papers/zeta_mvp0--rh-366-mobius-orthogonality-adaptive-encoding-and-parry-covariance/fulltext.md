---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance"
canonical_tex: "zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/main.pdf"
source_sha256: "7df165bd63d43f52dc217dea6691d231d8e40c00c148ab7e1aa4abcac55060fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Möbius orthogonality and adaptive encoding on a certified Hénon basic set: exact Parry covariance and a finite-capacity firewall

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-366-mobius-orthogonality-adaptive-encoding-and-parry-covariance/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On the certified local survivor of the area-preserving Hénon map $H_6(x,y)=(1-6x^2-y,x)$, we isolate a rigorous typical--exceptional Möbius dichotomy. The survivor is conjugate to a primitive four-state subshift whose scalar sign code forbids two plus signs at distance two. Every fixed periodic point is Möbius-orthogonal for every continuous observable, and Parry-almost every point is simultaneously orthogonal for all continuous observables. In contrast, an explicitly Möbius-adapted point, chosen after the full positive-time arithmetic sequence is read, has raw sign correlation $4/\pi^2$. For the centered variance-one sign observable we prove zero covariance at odd lags, covariance $(-\varphi^{-2})^k$ at lag $2k$, the exact finite-prefix variance formula, and the unconditional bound $V_N\leq\sqrt5N$. The density limit $V_N/N\to6/\pi^2$ remains conditional on ordinary Cesàro two-point Chowla. The finite-horizon adaptive capacity is exactly two path maximum-weight-independent-set problems, computable in $O(N)$, with $4/\pi^2\leq\liminf K_N/N\leq\limsup K_N/N\leq6/\pi^2$. A frozen $N=2^{20}$ ordering audit returns $p=0.4111$, a scoped negative finite result. Adaptive encoding is not spontaneous arithmetic coupling, an operator trace, or a zeta bridge. Gates A--E remain false/open.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Möbius orthogonality and adaptive encoding on a certified Hénon basic set:\
  exact Parry covariance and a finite-capacity firewall
```

## Markdown 正文

# Frozen object and claim boundary

The RH-1--RH-361 foundation is preserved by the four-volume synthesis [@WangRHMVP22026]. RH-364 froze a certified local hyperbolic survivor for the Hénon map and audited a separate engineered prime lift [@WangRH3642026]; RH-365 proved a return-bouquet height and radius theorem [@WangRH3652026]. Neither result supplies the Möbius statements below, which enter as an independent source-backed edge [@WangHenonMobius2026]. The physical route coordinate remains $$\texttt{actual\_same\_clock\_unnormalized\_head\_transport\_open}.
 \label{eq:physical-coordinate}$$

Consider $$H_6(x,y)=(1-6x^2-y,x).
 \label{eq:henon}$$ The frozen geometric input is a locally maximal mixing basic set $\Lambda_*$ conjugate to the subshift $\Sigma_A$ with state order $(--,-+,+-,++)$ and adjacency matrix $$A=
 \begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.
 \label{eq:adjacency}$$ This is an inherited theorem, not a conclusion from finite orbit tables [@WangHenonWeighted2026]. It concerns the local survivor $\Lambda_*$, not the full nonwandering set of $H_6$.

Writing a state as $w_n=(\varepsilon_n,\varepsilon_{n-1})$, admissibility is equivalent to $$\varepsilon_n\in\{-1,+1\},\qquad
 \text{there is no }n\text{ with }\varepsilon_n=\varepsilon_{n+2}=+1.
 \label{eq:distance-two}$$ The continuous clipping observable $$s(x,y)=
 \begin{cases}
 -1,&x\leq-1/3,\\
 3x,&\lvert x\rvert<1/3,\\
 +1,&x\geq1/3
 \end{cases}
 \label{eq:sign-observable}$$ equals the sign code on $\Lambda_*$. Indeed the certified survivor lies strictly inside $\lvert x\rvert>1/3$ on its two branches.

For $z\in\Lambda_*$ and $f\in C(\Lambda_*)$ define $$\mathcal C_N(z,f)=\frac1N\sum_{n=1}^{N}\mu(n)f(H_6^n z).
 \label{eq:correlation}$$ This is a time correlation along one orbit. It is not a sum over an orbit catalogue and is not an operator trace.

# Fixed periodic cancellation and an adaptive exceptional point

[\[thm:periodic\]]{#thm:periodic label="thm:periodic"} For every periodic $z\in\Lambda_*$ and every $f\in C(\Lambda_*)$, $$\mathcal C_N(z,f)\longrightarrow0.
 \label{eq:periodic-zero}$$ The point, and hence its period, is fixed before $N\to\infty$.

If the period is $p$, then $b_n=f(H_6^n z)$ is a bounded $p$-periodic sequence. Its finite Fourier expansion is $$b_n=\sum_{j=0}^{p-1}\widehat b_j e^{2\pi ijn/p}.$$ Davenport's uniform estimate gives, for each fixed $A_0>0$, $$\sup_{\theta\in\mathbb R}
 \lvert\sum_{n\leq N}\mu(n)e^{2\pi i n\theta}\rvert
 \ll_{A_0}N(\log N)^{-A_0}$$ [@Davenport1937; @IwaniecKowalski2004]. Applying it at the finitely many frequencies $j/p$ and dividing by $N$ proves the claim.

Positive entropy nevertheless gives enough symbolic freedom to encode an arithmetic sequence. Define a bi-infinite sign word by $\varepsilon_n=-1$ for $n\leq0$, and for $n\geq1$ set $$\varepsilon_n=+1
 \quad\Longleftrightarrow\quad
 \mu(n)=1\ \text{ and }\ n\bmod4\in\{1,2\}.
 \label{eq:adaptive-word}$$ Adding two maps the selected residue classes $1,2$ to the unselected classes $3,0$. Thus [\[eq:distance-two\]](#eq:distance-two){reference-type="eqref" reference="eq:distance-two"} holds, and the conjugacy supplies a unique point $z_{\mu}\in\Lambda_*$ with this itinerary.

[\[thm:exceptional\]]{#thm:exceptional label="thm:exceptional"} For the point selected by [\[eq:adaptive-word\]](#eq:adaptive-word){reference-type="eqref" reference="eq:adaptive-word"}, $$\lim_{N\to\infty}\mathcal C_N(z_{\mu},s)=\frac4{\pi^2}.
 \label{eq:four-over-pi2}$$

Let $M(N)=\sum_{n\leq N}\mu(n)$. From the definition, $$\sum_{n\leq N}\mu(n)\varepsilon_n
 =-M(N)+2\#\{n\leq N:\mu(n)=1,\ n\bmod4\in\{1,2\}\}.
 \label{eq:exceptional-identity}$$ For $r=1,2$ one has $$\frac1N\sum_{\substack{n\leq N\\n\equiv r\ (4)}}\mu(n)\to0,
 \qquad
 \frac1N\sum_{\substack{n\leq N\\n\equiv r\ (4)}}\mu(n)^2
 \to\frac2{\pi^2}.
 \label{eq:residue-density}$$ For $r=1$, these are the fixed-progression prime number theorem and the squarefree density. For $r=2$, write $n=2m$ with $m$ odd. Then $\mu(2m)=-\mu(m)$, while odd squarefree integers have density $4/\pi^2$; counting $m\leq N/2$ again gives $2/\pi^2$ after normalization by $N$ [@Mirsky1948]. Since $$\mathbf1_{\{\mu=1\}}=\frac{\mu^2+\mu}{2},$$ each selected residue class contributes density $1/\pi^2$. Finally $M(N)=o(N)$. Divide [\[eq:exceptional-identity\]](#eq:exceptional-identity){reference-type="eqref" reference="eq:exceptional-identity"} by $N$.

The complete positive-time Möbius sequence is read before $z_{\mu}$ is selected. Theorem [\[thm:exceptional\]](#thm:exceptional){reference-type="ref" reference="thm:exceptional"} proves offline encoding capacity. It does not prove a nonadaptive prediction rule, a dynamically preferred initial condition, or spontaneous arithmetic coupling. Moreover $\Lambda_*$ has positive entropy, so this is not a counterexample to Sarnak's zero-entropy conjecture [@Sarnak2010]. Positive-entropy systems can display either correlation or uniform decorrelation, and entropy alone is not a switch [@Karagulyan2017; @DownarowiczSerafin2019].

# Parry covariance, variance, and typical orthogonality

Let $\nu$ be the Parry measure on $\Sigma_A$, transported to $\Lambda_*$. Put $\varphi=(1+\sqrt5)/2$. In the state order of [\[eq:adjacency\]](#eq:adjacency){reference-type="eqref" reference="eq:adjacency"}, $$\pi=\left(\frac{3+\sqrt5}{10},\frac15,\frac15,
            \frac{3-\sqrt5}{10}\right)
 \label{eq:parry-pi}$$ and $$P=\begin{pmatrix}
 \varphi^{-1}&0&\varphi^{-2}&0\\
 1&0&0&0\\
 0&\varphi^{-1}&0&\varphi^{-2}\\
 0&1&0&0
 \end{pmatrix}.
 \label{eq:parry-P}$$ The raw sign has mean $-1/\sqrt5$. Hence $$F(w)=\frac{\sqrt5\,\varepsilon(w)+1}{2}
 \label{eq:F}$$ has mean zero and variance one.

[\[prop:covariance\]]{#prop:covariance label="prop:covariance"} For every $k\geq0$, $$\begin{aligned}
 \operatorname{Cov}_\nu(F,F\circ\sigma^{2k+1})&=0,\label{eq:odd-cov}\\
 \operatorname{Cov}_\nu(F,F\circ\sigma^{2k})&=(-\varphi^{-2})^k.\label{eq:even-cov}\end{aligned}$$

As a state vector, $$F=(-\varphi^{-1},-\varphi^{-1},\varphi,\varphi)^{\mathsf T}.$$ Direct multiplication gives $$P^2F=-\varphi^{-2}F,
 \qquad
 \pi\,\operatorname{diag}(F)PF=0.
 \label{eq:cov-algebra}$$ Since $\operatorname{Cov}_\nu(F,F\circ\sigma^\ell)=
 \pi\operatorname{diag}(F)P^\ell F$, the two identities follow. The executable artifact verifies this algebra exactly in $\mathbb Q(\sqrt5)$; no floating eigendecomposition is used.

For the fixed arithmetic weights define $$S_N(\omega)=\sum_{n=1}^{N}\mu(n)F(\sigma^n\omega),
 \qquad V_N=\operatorname{Var}_\nu S_N.
 \label{eq:SN}$$

[\[cor:variance\]]{#cor:variance label="cor:variance"} For every $N\geq1$, $$V_N=\sum_{n\leq N}\mu(n)^2
 +2\sum_{k\geq1}(-\varphi^{-2})^k
   \sum_{n\leq N-2k}\mu(n)\mu(n+2k),
 \label{eq:variance-formula}$$ where terms with $2k\geq N$ vanish. Unconditionally, $$0\leq V_N\leq\sqrt5\,N.
 \label{eq:sqrt5-bound}$$ If ordinary Cesàro two-point Chowla holds for every fixed even shift, then $$\frac{V_N}{N}\longrightarrow\frac6{\pi^2}.
 \label{eq:conditional-limit}$$

Expand [\[eq:SN\]](#eq:SN){reference-type="eqref" reference="eq:SN"}, group pairs by their lag, and insert Proposition [\[prop:covariance\]](#prop:covariance){reference-type="ref" reference="prop:covariance"}. This gives [\[eq:variance-formula\]](#eq:variance-formula){reference-type="eqref" reference="eq:variance-formula"}. Taking absolute values in the off-diagonal terms yields $$V_N\leq N\left(1+2\sum_{k\geq1}\varphi^{-2k}\right)
 =N(1+2\varphi^{-1})=\sqrt5N.$$ Variance is nonnegative by definition. Under ordinary Chowla, for each fixed $k$ the inner correlation in [\[eq:variance-formula\]](#eq:variance-formula){reference-type="eqref" reference="eq:variance-formula"} is $o(N)$. After division by $N$ it is bounded by one, while the coefficients are summable. Dominated convergence therefore passes through the $k$-sum, and $N^{-1}\sum_{n\leq N}\mu(n)^2\to6/\pi^2$ proves [\[eq:conditional-limit\]](#eq:conditional-limit){reference-type="eqref" reference="eq:conditional-limit"}. The logarithmically averaged theorem does not imply these ordinary Cesàro hypotheses [@Tao2016].

[\[thm:typical\]]{#thm:typical label="thm:typical"} For $\nu$-almost every $z\in\Lambda_*$, simultaneously for every $f\in C(\Lambda_*)$, $$\mathcal C_N(z,f)\longrightarrow0.
 \label{eq:typical-zero}$$

Work first on $\Sigma_A$. Let $g$ be a centered locally constant function. Exponential mixing of the finite-state Parry chain gives constants $C_g<\infty$ and $0<\rho_g<1$ with $$\lvert\operatorname{Cov}_\nu(g,g\circ\sigma^h)\rvert\leq C_g\rho_g^h.$$ Because $\lvert\mu(n)\rvert\leq1$, the weighted partial sums $T_N=\sum_{n\leq N}\mu(n)g\circ\sigma^n$ satisfy $\operatorname{Var}_\nu T_N=O_g(N)$. Chebyshev's inequality at $N=k^2$ gives, for every $\delta>0$, $$\sum_{k\geq1}
 \nu\{\lvert T_{k^2}\rvert>\delta k^2\}<\infty.$$ Borel--Cantelli yields $T_{k^2}/k^2\to0$ almost surely. Between $k^2$ and $(k+1)^2$ there are at most $2k+1$ additional bounded summands, so convergence holds for every $N$.

Choose a countable uniformly dense family of rational-valued locally constant functions. Intersect their full-measure convergence sets. For a noncentered function the constant component contributes a multiple of $M(N)/N$, which vanishes by the prime number theorem. Uniform approximation, together with $N^{-1}\sum_{n\leq N}\lvert\mu(n)\rvert\leq1$, extends the conclusion on this one full-measure set to every continuous function. Transport through the conjugacy.

The quantifier is important: one full-measure set works for all continuous observables, but the conclusion is not uniform over all $z\in\Lambda_*$ because Theorem [\[thm:exceptional\]](#thm:exceptional){reference-type="ref" reference="thm:exceptional"} supplies an explicit exception.

# Finite-horizon adaptive capacity

For $N\geq1$, define the open raw capacity $$K_N=\max_{\substack{\varepsilon_1,\ldots,\varepsilon_N\in\{-1,+1\}\\
              \varepsilon_n=\varepsilon_{n+2}=+1\ \mathrm{never}}}
 \lvert\sum_{n=1}^{N}\mu(n)\varepsilon_n\rvert.
 \label{eq:capacity}$$ The optimizing word may depend on $N$ and on the complete Möbius prefix.

[\[thm:capacity\]]{#thm:capacity label="thm:capacity"} The value $K_N$ and a witnessing word can be computed exactly in $O(N)$ time. Moreover $$\frac4{\pi^2}
 \leq\liminf_{N\to\infty}\frac{K_N}{N}
 \leq\limsup_{N\to\infty}\frac{K_N}{N}
 \leq\frac6{\pi^2}.
 \label{eq:capacity-bracket}$$

Start from the all-negative word. If $I$ is the set of positions changed to plus, then $$\sum_{n\leq N}\mu(n)\varepsilon_n=-M(N)+2\sum_{n\in I}\mu(n).
 \label{eq:capacity-baseline}$$ The constraint says exactly that $I$ is an independent set in the disjoint union of the odd-index path and the even-index path. For path weights $a_j$, the maximum-weight-independent-set recurrence is $$D_j=\max\{D_{j-1},D_{j-2}+a_j\},
 \qquad D_0=0,\quad D_1=\max\{0,a_1\}.
 \label{eq:mwis}$$ Run it on both paths with weights $\mu(n)$ to maximize [\[eq:capacity-baseline\]](#eq:capacity-baseline){reference-type="eqref" reference="eq:capacity-baseline"}, and with weights $-\mu(n)$ to minimize it. Traceback recovers witnesses. The total work is linear.

Every prefix of the word in [\[eq:adaptive-word\]](#eq:adaptive-word){reference-type="eqref" reference="eq:adaptive-word"} is feasible, so Theorem [\[thm:exceptional\]](#thm:exceptional){reference-type="ref" reference="thm:exceptional"} gives the lower bound in [\[eq:capacity-bracket\]](#eq:capacity-bracket){reference-type="eqref" reference="eq:capacity-bracket"}. For every sign word, $$\lvert\sum_{n\leq N}\mu(n)\varepsilon_n\rvert
 \leq\sum_{n\leq N}\mu(n)^2.$$ The squarefree density gives the upper bound.

No existence theorem for $\lim K_N/N$ follows. The optimizer can change with $N$, so a nonvanishing envelope also does not contradict Theorem [\[thm:periodic\]](#thm:periodic){reference-type="ref" reference="thm:periodic"}, which fixes one periodic point before taking the limit. Filling signs outside $[1,N]$ with $-1$ realizes each open optimizer by an $N$-dependent point of $\Lambda_*$.

# Frozen finite audit and numerical boundary

The source experiment fixed $N_{\max}=2^{20}$, 1024 stationary Parry paths, and 1023 conditional arithmetic surrogates before reading the production results [@WangHenonMobius2026]. The surrogates preserve the squarefree zero support and the numbers of positive and negative signs within frozen growing blocks; every surrogate undergoes the same adaptive optimization. The rank statistic is $$p_{\mathrm{cap}}=
 \frac{1+\#\{b:K_{N_{\max},b}\geq K_{N_{\max},\mathrm{real}}\}}{1024}.
 \label{eq:rank-p}$$

::: {#tab:finite}
  Quantity at $N=2^{20}$                                 Value
  ---------------------------------- -------------------------
  Exceptional raw integer score                       $425025$
  Exceptional raw correlation                    $0.405335426$
  Open maximum / minimum                  $515983\,/\,-516163$
  Open absolute capacity                         $0.492251396$
  Conditional-null exceedances                 $420$ of $1023$
  Rank $p$-value                       $421/1024=0.4111328125$
  Stored floating variance density               $0.608082565$

  : Locked endpoint diagnostics. These are finite reproduction facts, not asymptotic theorems.
:::

The rank test is a scoped negative result: the natural ordering is not exceptional under this frozen finite null. It is not a probability model for Möbius itself, and it does not prove any asymptotic ordering law.

The variance distinction is equally strict. Formula [\[eq:variance-formula\]](#eq:variance-formula){reference-type="eqref" reference="eq:variance-formula"} is exact. The upstream production routine, however, evaluates it in floating arithmetic and stops after the geometric coefficient falls below $10^{-15}$. The first omitted geometric tail has normalized absolute bound below $1.3\times10^{-15}$ before floating roundoff, but the stored decimal is still a tolerance-controlled diagnostic, not an exact algebraic evaluation. The RH-366 artifact instead checks small finite prefixes exactly in $\mathbb Q(\sqrt5)$.

The executable package also performs the following independent checks:

1.  all frozen source and Paper-3 dependency hashes;

2.  exhaustive equivalence of the sign rule and graph cycles through length eight;

3.  the exceptional integer identity on finite prefixes;

4.  exact $\mathbb Q(\sqrt5)$ covariance and variance rows;

5.  dynamic programming against brute force through length twelve;

6.  the four-volume replay, strict JSON parsing, fixed archive membership, and mutation rejection.

Finite checks reproduce identities and provenance. They are not evidence for the prime number theorem, ordinary Chowla, or a capacity limit.

# Route verdict and Gate ledger

::: {#tab:route}
  Route     Verdict
  --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route A   `GO`. Fixed periodic and Parry-typical orthogonality, the exact adaptive correlation, covariance and variance theorems, the linear-time capacity theorem, and the frozen scoped negative form a standalone theorem package.
  Route B   `STOP_SCOPED`. The first fatal mismatch is data type: $z_{\mu}$ is chosen after reading $\mu$. Its scalar time correlation is not a canonical determinant, operator trace, or signed von-Mangoldt prime-power ledger.

  : The strongest warranted route interpretation.
:::

The following boundaries are mandatory.

1.  $\Lambda_*$ is a certified local basic set, not the full Hénon dynamics.

2.  The exceptional point is an offline encoding, not an intrinsic or independently selected coupling.

3.  The Parry theorem is almost sure and simultaneous in $f$, not uniform over all points or measures.

4.  The variance-density limit is conditional on ordinary fixed-shift Cesàro Chowla.

5.  The finite capacity plateau is not a proved limit.

6.  Möbius-weighted orbit averages are not von-Mangoldt traces and do not define an Euler product or an L-function family.

Consequently the Gate ledger remains

   Gate  Status       First missing object
  ------ ------------ ----------------------------------------------------
    A    false/open   canonical intrinsic dynamical spectral determinant
    B    false/open   time-oriented scattering or unitary completion
    C    false/open   self-adjoint generator and intrinsic $T\log T$ law
    D    false/open   signed von-Mangoldt prime-power operator trace
    E    false/open   completed-zeta divisor equality

No Hilbert--Pólya operator, Riemann-zero spectral identification, completed-zeta divisor equality, or proof of the Riemann Hypothesis follows.

# Conclusion and next exact questions

One explicit positive-entropy Hénon subsystem supports both rigorous Möbius cancellation and rigorous arithmetic tracking. The distinction is selection: fixed periodic and Parry-typical points cancel, while a point chosen after reading the arithmetic sequence tracks it with correlation $4/\pi^2$. Exact covariance and linear-time capacity quantify the mechanism without promoting it to a spectral or zeta construction.

The shortest new theorem problems are correspondingly narrow: determine whether $K_N/N$ has a limit; classify nonadaptive invariant measures with quantitative Möbius cancellation; and generalize the graph-capacity theorem to other mixing subshifts. Independent breadth-first routes, including the cyclic-Ulam structural audit and the RH-365 primitive-divisor/radius problems, remain separate. Repackaging adaptive encoding as intrinsic coupling would not be a continuation.
