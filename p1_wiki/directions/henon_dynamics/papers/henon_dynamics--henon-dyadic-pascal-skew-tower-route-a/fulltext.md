---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dyadic-pascal-skew-tower-route-a"
canonical_tex: "henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/paper/main.pdf"
source_sha256: "f969ae406d517d307a967bca16b7784bf2ae387ed200fc7dba500589c305550c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Clocks and Time Reversal in Dyadic Pascal Skew Towers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dyadic_pascal_skew_tower_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $q=2^r$ and every $d\ge2$, consider the finite affine tower $T(x_1,\ldots,x_d)=(x_1+x_2,\ldots,x_{d-1}+x_d,x_d+1)$. With $a=\lfloor\log_2d\rfloor$ and $M=2^{r+a}$, we prove that $\operatorname{Fix}(T^n)$ is the entire $q^d$-state space exactly when $M\mid n$, and is empty otherwise. Thus every state has least period $M$, there are $q^d/M$ primitive cycles, and $\zeta_T(z)=(1-z^M)^{-q^d/M}$. The finite Koopman determinant is its reciprocal. In truncated-polynomial coordinates, $T$ is multiplication by $1+t$ and substitution $t\mapsto-t/(1+t)$ is an involutive reversor, yielding an exact antiunitary time reversal. The proof uses Pascal coefficients and a sharp binary-valuation witness; finite sweeps are only regression sentinels. No complexity, target determinant, arithmetic, or Hilbert--Pólya claim is made.
author:
- 'Route-A structural certificate C166'
title: Exact Clocks and Time Reversal in Dyadic Pascal Skew Towers
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** affine dynamics; Pascal tower; dyadic valuation; exact period; Artin--Mazur zeta; Koopman unitary; time reversal.

# Pascal ownership of every iterate

In $R=(\mathbb Z/q\mathbb Z)[t]/(t^{d+1})$, encode a state by the unit $$p_x(t)=1+x_dt+x_{d-1}t^2+\cdots+x_1t^d.                    \tag{1}$$ Multiplication by $1+t$ is exactly $T$, so $$p_{T^nx}=(1+t)^np_x,\qquad
T^nx=x\Longleftrightarrow q\mid\binom nk\quad(1\le k\le d). \tag{2}$$ The last equivalence is independent of $x$: the unit $p_x$ cancels in $R$. It already shows that every fixed set is either the whole state space or empty.

# The sharp dyadic clock

Let $a=\lfloor\log_2d\rfloor$ and $M=2^{r+a}$. Since $$\binom nk=\frac nk\binom{n-1}{k-1},
\qquad v_2\!\left(\binom nk\right)\ge v_2(n)-v_2(k),        \tag{3}$$ for $1\le k\le n$. Coefficients with $k>n$ vanish and are automatically divisible by $q$. Thus $M\mid n$ implies divisibility by $q$ for every $k\le d$ without assigning a valuation to zero.

Conversely, $q\nmid n$ is detected by $k=1$. If $q\mid n$ but $M\nmid n$, write $v_2(n)=r+b$ with $0\le b<a$ and choose $$k=2^{b+1}\le2^a\le d.                                    \tag{4}$$ The low $r+b$ binary digits of $n-1$ are all one, and the low $b+1$ digits of $k-1$ are all one. Lucas reduction modulo two makes $\binom{n-1}{k-1}$ odd; hence $$v_2\!\left(\binom nk\right)=r+b-(b+1)=r-1.                \tag{5}$$ This coefficient violates (2). Therefore, for every parameter and iterate, $$\operatorname{Fix}(T^n)=
\begin{cases}(\mathbb Z/q\mathbb Z)^d,&M\mid n,\\
\varnothing,&M\nmid n.
\end{cases}                                                \tag{6}$$ This is the all-parameter proof; the 25,200 coefficient checks and 27,788 direct state periods packaged with C166 are finite regression sentinels.

# Cycles, zeta, and the finite Koopman owner

Equation (6) gives least period $M$ for all $q^d$ states and exactly $q^d/M$ primitive cycles. Thus $$\log\zeta_T(z)=\sum_{n\ge1}\frac{\#\operatorname{Fix}(T^n)}n z^n
=-\frac{q^d}{M}\log(1-z^M),
\quad \zeta_T(z)=(1-z^M)^{-q^d/M}.                         \tag{7}$$ On $\mathcal H=\ell^2((\mathbb Z/q\mathbb Z)^d)$ let $U_Tf=f\circ T$. Its cycle decomposition immediately gives the same-clock identity $$\det(I-zU_T)=(1-z^M)^{q^d/M}=\zeta_T(z)^{-1}.              \tag{8}$$

# A truncated-ring reversor and scope

Nilpotence of $t$ makes $$\sigma(t)=-\frac{t}{1+t}=-t+t^2-\cdots+(-1)^dt^d          \tag{9}$$ a well-defined substitution automorphism of $R$. Direct composition gives $\sigma^2(t)=t$ and $1+\sigma(t)=(1+t)^{-1}$; consequently $$\sigma T\sigma=T^{-1}.                                    \tag{10}$$ If $P_\sigma f=f\circ\sigma$ and $J$ is complex conjugation, then $\Theta=P_\sigma J$ satisfies $$\Theta^2=I,\qquad \Theta U_T\Theta^{-1}=U_T^{-1}.          \tag{11}$$ The standalone shear is absorbed as $d=2$; no product-rotation branch is presented as new progress. The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_NATURAL\_QUANTIZATION})$. This finite source theorem supplies no complexity result, target trace/divisor/counting law, arithmetic local or Euler datum, root number, automorphy statement, Hilbert--Pólya operator, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing evidence and programs are in the release; no external dataset is used. **Ethics.** No human participants, animals, or sensitive personal data are involved. **Author contributions/CRediT.** Anonymous technical certificate; Conceptualization, Formal analysis, Software, Validation, and Writing are recorded at package level. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported derivation planning, drafting, and code review. Packaged exact checks validate quantitative claims; the assistant was not treated as an external peer reviewer.
