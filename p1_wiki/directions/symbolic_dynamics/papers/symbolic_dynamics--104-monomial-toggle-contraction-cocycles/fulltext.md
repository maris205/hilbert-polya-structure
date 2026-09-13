---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--104-monomial-toggle-contraction-cocycles"
canonical_tex: "symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/main.tex"
canonical_pdf: "symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/main.pdf"
source_sha256: "4eb81b8ca08c8689ee0418309ac787a126fae701669ffff6733d8ae4c2d3dedc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Singular Spectra and Folded Fluctuations for Monomial Toggle Contraction Cocycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/104-monomial-toggle-contraction-cocycles/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $0<a<1$. Independently at each time, choose either the coordinate contraction $D=\operatorname{diag}(a,1)$ or the toggle contraction $R=\left(\begin{smallmatrix}0&1\\a&0\end{smallmatrix}\right)$, with toggle probability $q$. We give an exact finite-word normal form for the left product $M_n$: an orientation bit selects a coordinate swap, while a two-state occupation count gives both diagonal exponents. Consequently, the two singular values, determinant, and condition number are explicit for every environment and every finite time. For $0<q<1$, both quenched Lyapunov exponents equal $\frac12\log a$, but their centered $\sqrt n$-scale separation converges to a folded normal law with variance parameter $(1-q)/q$. The endpoint $q=0$ instead retains two distinct exponents, whereas $q=1$ has bounded parity splitting. For every moment order $s>0$, a two-state tilted transfer matrix gives the exact annealed log-moment exponent $$\frac{s}{2}\log a+
   \log\!\left((1-q)\cosh\vartheta+
   \sqrt{(1-q)^2\cosh^2\vartheta-(1-2q)}\right),
   \qquad \vartheta=-\frac{s}{2}\log a.$$ It lies strictly above the quenched value for $0<q<1$ and agrees with it at both deterministic endpoints. The note explicitly subtracts general random-product and generalized-Lyapunov theory, and external release remains on hold pending specialist direct-owner review.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: Exact Singular Spectra and Folded Fluctuations for Monomial Toggle Contraction Cocycles
```

## Markdown 正文

# Introduction

A product of two sparse $2\times2$ contractions can preserve more temporal information than its determinant records. In the family studied here, one generator keeps the coordinate axes fixed and the other swaps them. The product is noncommutative, yet a single orientation bit determines which coordinate receives the next factor of $a$. This turns the full singular spectrum into an occupation statistic of a two-state Markov chain.

Almost-sure growth rates for random matrix products belong to the general Furstenberg--Kesten theory [@FurstenbergKesten1960]. Generalized Lyapunov exponents and transfer methods for fluctuations of random matrix products also have a broad established literature [@Texier2020]. Those theories, the existence of Lyapunov exponents, and the general use of tilted transfer operators are not claims of this note.

The auditable residual calculation is the exact conjunction for one two-point monomial cocycle. We prove four statements. First, every finite product has a coordinate-swap normal form whose two exponents are occupation counts. Second, this form gives the complete finite-time singular spectrum. Third, the singular-value splitting has a folded central limit law with an explicit variance. Fourth, the annealed $s$-moment exponent is the logarithm of an explicit Perron root and has a strict interior gap from the quenched exponent.

External release is **HOLD**. A bounded source search did not locate this exact conjunction for the two matrices below, but search absence is not evidence of novelty. No absolute novelty or priority statement is made.

# The cocycle and its finite-word normal form {#sec:normal}

Fix $a\in(0,1)$ and set $$\label{eq:generators}
 D=\begin{pmatrix}a&0\\0&1\end{pmatrix},\qquad
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 R=SD=\begin{pmatrix}0&1\\a&0\end{pmatrix}.$$ Let $(A_t)_{t\geq1}$ be iid with $$\label{eq:law}
 \mathbb P(A_t=R)=q,\qquad \mathbb P(A_t=D)=r:=1-q,
 \qquad 0\leq q\leq1.$$ Our composition convention is the left product $$\label{eq:left-product}
 M_0=\operatorname{Id},\qquad M_n=A_nA_{n-1}\cdots A_1.$$ Thus $A_1$ acts first. This convention is part of the theorem statements.

Write $\epsilon_t=\mathbf 1_{\{A_t=R\}}$ and define the orientation process $$\label{eq:orientation}
 J_0=0,\qquad J_t=J_{t-1}\mathbin{\oplus}\epsilon_t,$$ where $\oplus$ is addition modulo two. The occupation and signed occupation variables are $$\label{eq:occupation}
 U_n=\sum_{t=0}^{n-1}\mathbf 1_{\{J_t=0\}},\qquad
 Z_n=2U_n-n=\sum_{t=0}^{n-1}(-1)^{J_t}.$$ The occupation is taken *before* the next matrix acts. For example, $M_1=R$ has $(J_1,U_1)=(1,1)$, which fixes the convention at the first nontrivial word.

[\[thm:normal\]]{#thm:normal label="thm:normal"} For every finite word and every $n\geq0$, $$\label{eq:normal-form}
 \boxed{\quad
 M_n=S^{J_n}\operatorname{diag}\!\left(a^{U_n},a^{n-U_n}\right).
 \quad}$$ In particular, $$\label{eq:determinant}
 \det M_n=(-1)^{J_n}a^n.$$

The formula holds at $n=0$. Suppose it holds at time $n$. If $J_n=0$, left multiplication by either $D$ or $R=SD$ adds one factor of $a$ to the first diagonal entry; multiplication by $R$ also changes the new orientation from zero to one. If $J_n=1$, use $$\label{eq:swap-identities}
 DS=S\operatorname{diag}(1,a),\qquad RS=SDS=\operatorname{diag}(1,a).$$ Thus either generator adds one factor of $a$ to the second diagonal entry, and only $R$ toggles the orientation. These two cases give $$U_{n+1}=U_n+\mathbf 1_{\{J_n=0\}},\qquad
 J_{n+1}=J_n\mathbin{\oplus}\epsilon_{n+1},$$ which is exactly the induction step for [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"}. Taking determinants and using $\det S=-1$ proves [\[eq:determinant\]](#eq:determinant){reference-type="eqref" reference="eq:determinant"}.

Because $S$ is orthogonal, the normal form immediately yields the full singular spectrum.

[\[cor:singular\]]{#cor:singular label="cor:singular"} Let $\sigma_{\max}(M_n)\geq\sigma_{\min}(M_n)>0$ be the Euclidean singular values. Then $$\begin{aligned}
 \sigma_{\max}(M_n)&=a^{(n-|Z_n|)/2},
 &\sigma_{\min}(M_n)&=a^{(n+|Z_n|)/2},\label{eq:singular-values}\\
 |\det M_n|&=a^n,
 &\kappa_2(M_n)&=a^{-|Z_n|}.\label{eq:condition}\end{aligned}$$

The unordered singular values in [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"} are $a^{U_n}$ and $a^{n-U_n}$. Since $0<a<1$, the larger value corresponds to the smaller exponent. The identities $$\min\{U_n,n-U_n\}=\frac{n-|Z_n|}{2},\qquad
 \max\{U_n,n-U_n\}=\frac{n+|Z_n|}{2}$$ give [\[eq:singular-values\]](#eq:singular-values){reference-type="eqref" reference="eq:singular-values"}; division gives [\[eq:condition\]](#eq:condition){reference-type="eqref" reference="eq:condition"}.

# Quenched exponents and folded fluctuations {#sec:quenched}

When $0<q<1$, $(J_t)$ is an irreducible aperiodic Markov chain with transition matrix $$\label{eq:P}
 P=\begin{pmatrix}r&q\\q&r\end{pmatrix}$$ and stationary law $(1/2,1/2)$. The endpoint $q=1$ is periodic and the endpoint $q=0$ is reducible, so both must be handled separately.

[\[thm:quenched\]]{#thm:quenched label="thm:quenched"} The ordered almost-sure Lyapunov exponents $$\lambda_1(q)=\lim_{n\to\infty}\frac1n\log\sigma_{\max}(M_n),
 \qquad
 \lambda_2(q)=\lim_{n\to\infty}\frac1n\log\sigma_{\min}(M_n)$$ exist and satisfy $$\label{eq:quenched-exponents}
 (\lambda_1(q),\lambda_2(q))=
 \begin{cases}
 (0,\log a),&q=0,\\[2pt]
 (\frac12\log a,\frac12\log a),&0<q\leq1.
 \end{cases}$$ For $q=1$, more precisely, $Z_n=0$ for even $n$ and $Z_n=1$ for odd $n$.

If $q=0$, then $M_n=D^n$ and the first line of [\[eq:quenched-exponents\]](#eq:quenched-exponents){reference-type="eqref" reference="eq:quenched-exponents"} follows. If $0<q<1$, the ergodic theorem for the finite chain [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"} gives $U_n/n\to1/2$ almost surely. Substitution in [\[cor:singular\]](#cor:singular){reference-type="ref" reference="cor:singular"} gives the second line. If $q=1$, the orientation alternates deterministically from $J_0=0$, so $U_n=\lceil n/2\rceil$ and the stated parity formula follows.

The next result resolves the sublinear singular-value separation. Put $$\label{eq:variance}
 v_q=\frac{1-q}{q},\qquad 0<q<1.$$

[\[thm:clt\]]{#thm:clt label="thm:clt"} For $0<q<1$, $$\label{eq:Z-clt}
 \frac{Z_n}{\sqrt n}\ \Longrightarrow\ N(0,v_q).$$ Consequently, $$\begin{aligned}
 \frac{\log\sigma_{\max}(M_n)-\frac n2\log a}{\sqrt n}
 &\Longrightarrow \frac{|\log a|}{2}\,|N(0,v_q)|,
 \label{eq:max-clt}\\
 \frac{\log\sigma_{\min}(M_n)-\frac n2\log a}{\sqrt n}
 &\Longrightarrow-\frac{|\log a|}{2}\,|N(0,v_q)|,
 \label{eq:min-clt}\\
 \frac{\log\kappa_2(M_n)}{\sqrt n}
 &\Longrightarrow |\log a|\,|N(0,v_q)|.
 \label{eq:kappa-clt}\end{aligned}$$

Set $Y_t=(-1)^{J_t}$ and $\rho=1-2q$. Then $$\mathbb E(Y_t\mid J_{t-1})=\rho Y_{t-1}.$$ For $t\geq1$, define $\xi_t=Y_t-\rho Y_{t-1}$. Relative to the natural filtration, $(\xi_t)$ is a bounded martingale-difference sequence and $$\label{eq:martingale-variance}
 \mathbb E(\xi_t^2\mid J_{t-1})=1-\rho^2.$$ Summing the definition of $\xi_t$ from $t=1$ to $n-1$ gives $$\label{eq:martingale-decomposition}
 (1-\rho)Z_n=\sum_{t=1}^{n-1}\xi_t+Y_0-\rho Y_{n-1}.$$ The last two terms are bounded. The martingale central limit theorem applies because the increments are bounded and their conditional quadratic variation is the deterministic quantity $(n-1)(1-\rho^2)$ [@Brown1971]. Hence the variance in [\[eq:Z-clt\]](#eq:Z-clt){reference-type="eqref" reference="eq:Z-clt"} is $$\frac{1-\rho^2}{(1-\rho)^2}
 =\frac{1+\rho}{1-\rho}=\frac{1-q}{q}.$$ The continuous mapping theorem and the logarithms of [\[eq:singular-values\]](#eq:singular-values){reference-type="eqref" reference="eq:singular-values"}--[\[eq:condition\]](#eq:condition){reference-type="eqref" reference="eq:condition"} prove [\[eq:max-clt\]](#eq:max-clt){reference-type="eqref" reference="eq:max-clt"}--[\[eq:kappa-clt\]](#eq:kappa-clt){reference-type="eqref" reference="eq:kappa-clt"}.

At $q=0$, $Z_n=n$ and the splitting is linear rather than of order $\sqrt n$. At $q=1$, $|Z_n|\leq1$ and the splitting is bounded. Thus the two deterministic endpoints are genuinely different from every $0<q<1$, even though $v_q\downarrow0$ as $q\uparrow1$.

# Annealed moment exponent {#sec:annealed}

Fix $s>0$ and define the order-$s$ annealed log-moment exponent by $$\label{eq:Gamma-definition}
 \Gamma_s(q)=\lim_{n\to\infty}\frac1n
 \log\mathbb E\lVert M_n\rVert_2^s,$$ provided the limit exists. This normalization keeps the factor $s$ inside the exponent; some generalized-Lyapunov conventions divide the right-hand side by $s$.

Put $$\label{eq:theta}
 \vartheta=-\frac{s}{2}\log a>0,$$ and define the tilted transfer matrix $$\label{eq:tilted}
 K_{\vartheta}
 =\operatorname{diag}(e^{\vartheta},e^{-\vartheta})P.$$ Its trace and determinant are $$\label{eq:trace-det}
 \operatorname{tr}K_{\vartheta}=2r\cosh\vartheta,
 \qquad \det K_{\vartheta}=r-q=1-2q.$$

[\[thm:annealed\]]{#thm:annealed label="thm:annealed"} For every $0\leq q\leq1$ and $s>0$, the limit [\[eq:Gamma-definition\]](#eq:Gamma-definition){reference-type="eqref" reference="eq:Gamma-definition"} exists and equals $$\label{eq:annealed-formula}
 \boxed{\quad
 \Gamma_s(q)=\frac{s}{2}\log a+\log\varrho_s(q),
 \quad}$$ where $$\label{eq:perron-root}
 \varrho_s(q)=
 r\cosh\vartheta+
 \sqrt{r^2\cosh^2\vartheta-(r-q)}.$$ For $0<q<1$, $$\label{eq:strict-gap}
 \Gamma_s(q)>s\lambda_1(q)=\frac{s}{2}\log a.$$ At the deterministic endpoints the gap closes: $$\label{eq:endpoint-moments}
 \Gamma_s(0)=0=s\lambda_1(0),\qquad
 \Gamma_s(1)=\frac{s}{2}\log a=s\lambda_1(1).$$

Let $e_+=(1,0)^{\mathsf T}$ and $\mathbf 1=(1,1)^{\mathsf T}$. Since $Z_n$ weights the state before each transition, the finite-time signed occupation transforms are exactly $$\label{eq:signed-mgf}
 \mathbb Ee^{\pm\vartheta Z_n}
 =e_+^{\mathsf T}K_{\pm\vartheta}^{n}\mathbf 1.$$ The two tilted matrices have the same trace and determinant, hence the same eigenvalues. Their larger eigenvalue is [\[eq:perron-root\]](#eq:perron-root){reference-type="eqref" reference="eq:perron-root"} by [\[eq:trace-det\]](#eq:trace-det){reference-type="eqref" reference="eq:trace-det"}.

Suppose first that $0<q<1$. Both tilted matrices have strictly positive entries. Perron--Frobenius theory applied to [\[eq:signed-mgf\]](#eq:signed-mgf){reference-type="eqref" reference="eq:signed-mgf"} gives $$\lim_{n\to\infty}\frac1n\log \mathbb Ee^{\pm\vartheta Z_n}
 =\log\varrho_s(q).$$ For every real $z$, $$\label{eq:absolute-bound}
 e^{\vartheta|z|}
 \leq e^{\vartheta z}+e^{-\vartheta z}
 \leq2e^{\vartheta|z|}.$$ Therefore the absolute transform has the same exponential rate. By [\[cor:singular\]](#cor:singular){reference-type="ref" reference="cor:singular"}, $$\lVert M_n\rVert_2^s=a^{sn/2}e^{\vartheta|Z_n|},$$ which proves [\[eq:annealed-formula\]](#eq:annealed-formula){reference-type="eqref" reference="eq:annealed-formula"} in the open interval.

To prove strictness, let $\chi$ be the characteristic polynomial of $K_{\vartheta}$. From [\[eq:trace-det\]](#eq:trace-det){reference-type="eqref" reference="eq:trace-det"}, $$\chi(1)=1-2r\cosh\vartheta+(r-q)
 =2r(1-\cosh\vartheta)<0.$$ Thus the larger root satisfies $\varrho_s(q)>1$, proving [\[eq:strict-gap\]](#eq:strict-gap){reference-type="eqref" reference="eq:strict-gap"}.

If $q=0$, then $Z_n=n$ and $\lVert M_n\rVert_2=1$; formula [\[eq:perron-root\]](#eq:perron-root){reference-type="eqref" reference="eq:perron-root"} reduces to $e^{\vartheta}$ and gives $\Gamma_s(0)=0$. If $q=1$, then $|Z_n|\leq1$ and $n^{-1}\log\mathbb Ee^{\vartheta|Z_n|}\to0$; the root in [\[eq:perron-root\]](#eq:perron-root){reference-type="eqref" reference="eq:perron-root"} is one. This proves [\[eq:endpoint-moments\]](#eq:endpoint-moments){reference-type="eqref" reference="eq:endpoint-moments"} and completes the proof.

Equation [\[eq:signed-mgf\]](#eq:signed-mgf){reference-type="eqref" reference="eq:signed-mgf"} also supplies an exact finite-time recurrence. If $m_n(\vartheta)=\mathbb Ee^{\vartheta Z_n}$, then $$\label{eq:mgf-recurrence}
 m_{n+2}(\vartheta)=2r\cosh\vartheta\,m_{n+1}(\vartheta)
 -(r-q)m_n(\vartheta),
 \quad m_0=1,\quad m_1=e^{\vartheta}.$$ This recurrence is not needed for the limiting proof, but it separates the finite-time transfer identity from the Perron asymptotic.

# Exact controls, collision firewall, and owner boundary

The standard-library verifier compares exhaustive literal rational products with [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"}, then checks determinants and Gram matrices independently. Separate dynamic programs verify occupation laws, singular moments, the transfers [\[eq:signed-mgf\]](#eq:signed-mgf){reference-type="eqref" reference="eq:signed-mgf"}--[\[eq:mgf-recurrence\]](#eq:mgf-recurrence){reference-type="eqref" reference="eq:mgf-recurrence"}, and the finite moments of $Z_n$. The stored output gives the exact assertion count. These finite controls falsify errors; they do not prove limits.

Two internal collision boundaries are fixed explicitly.

-   P91 studies reverser shifts through periodic points, zeta data, and recovery. Here the swap belongs to an invertible linear cocycle whose observables are singular values and moment pressure; no shift is built.

-   P93 studies a noninvertible push--pop stack with reflected maxima and fiber loss. Here every matrix is invertible, $|\det M_n|=a^n$, and no stack boundary or reflected extremum occurs.

The shared two-state additive structure is not claimed as new. P91 remains a disclosed medium internal collision risk.

Furstenberg--Kesten theory owns the random-product framework [@FurstenbergKesten1960]; tilted generalized-Lyapunov methods are also established [@Texier2020]; and [\[thm:clt\]](#thm:clt){reference-type="ref" reference="thm:clt"} uses the standard martingale CLT [@Brown1971]. The residual package is only the displayed specialization. Direct-owner review is still required.

# Conclusion

The orientation--occupation reduction determines every finite-time singular value, the endpoint dichotomy, and the folded fluctuation law. A tilted transfer gives the annealed moment exponent and its strict interior gap. External circulation remains on hold until the owner and collision audits are closed.
