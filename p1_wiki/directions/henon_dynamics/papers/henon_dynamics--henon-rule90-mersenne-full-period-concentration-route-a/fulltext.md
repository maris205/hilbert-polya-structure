---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rule90-mersenne-full-period-concentration-route-a"
canonical_tex: "henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a/paper/main.pdf"
source_sha256: "9650c5b74741d3761837a1ea76f560e0207b974d54b3f30832372787c2ee726d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Full-Period Concentration in Mersenne Rule 90

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rule90_mersenne_full_period_concentration_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For Rule 90 on Mersenne rings $L=2^r-1$, the periodic image contains $2^{L-1}$ states and every period divides $L$. We prove that exact period $L$ has probability tending to one, the total cycle count is asymptotic to $2^{L-1}/L$, and the cycle-averaged period is asymptotic to $L$. The neighboring power-of-two family remains nilpotent. These are all-size theorems, not extrapolations from the finite replay ledger.
author:
- 'Route-A structural certificate C155'
title: 'Full-Period Concentration in Mersenne Rule 90'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** cellular automaton; Rule 90; Mersenne circumference; exact period; fixed subspace; Burnside lemma; orbit concentration.

chinese-simplified

中文摘要

本文研究长度 $L=2^r-1$ 的环上 [Rule 90]{lang="en"}。其周期集是维数 $L-1$ 的线性像， 且所有轨道周期整除 $L$。我们证明任意非恒等时刻的固定子空间只依赖 $d=\gcd(j,L)$，其维数不超过 $2d\leq2L/3$。由此得到：在周期像上均匀取点时， 周期小于 $L$ 的概率至多为 $2L2^{-L/3}$，因而精确满周期的概率趋于一。 [Burnside]{lang="en"} 引理进一步给出总原始轨道数渐近于 $2^{L-1}/L$，并说明按轨道等权 计算的平均周期除以 $L$ 后趋于一。作为匹配对照，二次幂长度族仍为幂零系统。 这些结论是 [Mersenne]{lang="en"} 尺度上的精确有限体积定理，不是目标行列式匹配。

关键词：元胞自动机；[Rule 90]{lang="en"}； [Mersenne]{lang="en"} 周长；精确周期；固定子空间； [Burnside]{lang="en"} 引理；轨道集中。

# Periodic image and proper fixed spaces

On $R_L=\mathbb F_2[x,x^{-1}]/(x^L-1)$, Rule 90 is multiplication by $a=x+x^{-1}$. Frobenius gives $a^{L+1}=a$. Since $x^L+1$ is squarefree for odd $L$ and $gcd(x^L+1,(x+1)^2)=x+1$, multiplication by $a$ has a one-dimensional kernel. Thus the periodic set is $V=\operatorname{im}a$, with $|V|=2^{L-1}$, and $g=a|_V$ satisfies $g^L=I$. Conversely, a positive-time fixed state already belongs to $V$, so every realized period divides $L$.

For $1\leq j<L$, put $d=\gcd(j,L)$. The identity $\gcd(U^j-1,U^L-1)=U^d-1$ and Bézout give, after substitution $U=g$ and use of $g^L=I$, $$\ker(g^j-I)=\ker(g^d-I).$$ Clearing the Laurent multiplier for time $d$ gives $(x^2+1)^d+x^d$, of degree $2d$. Because a proper divisor of odd $L$ is at most $L/3$, $$\dim\ker(g^j-I)\leq2d\leq\frac{2L}{3}.\tag{1}$$

# Concentration and Burnside

Every state of period less than $L$ belongs to one of the proper-time fixed spaces because every realized period divides $L$. Hence $$\Pr_V(\operatorname{per}<L)
\leq\frac{(L-1)2^{2L/3}}{2^{L-1}}
\leq2L2^{-L/3}\longrightarrow0.\tag{2}$$ If $C_L$ is the total number of primitive cycles, Burnside gives $$C_L=\frac1L\sum_{j=0}^{L-1}\#\operatorname{Fix}_V(g^j),
\qquad
0\leq\frac{LC_L}{2^{L-1}}-1\leq2L2^{-L/3}.\tag{3}$$ The cycles partition $V$, so their mean length when each cycle is weighted once is $|V|/C_L=2^{L-1}/C_L$. After division by $L$, this is the reciprocal of $LC_L/2^{L-1}$ and tends to one.

The uniform estimate can be trivial at the smallest size: for $L=3$ the restriction is the identity and there is no exact period-three state. This finite exception is retained in the ledger and does not affect the limit. Exact polynomial-gcd and Möbius rows through $r=8$ contain 26 divisor-period and 494 proper-time cells. The independent checker passes 2,291 assertions, SymPy passes 2,255 checks, replay is byte-identical, and 54 hostile cases are rejected. For the matched control $L=2^s$, $a^{L/2}=0$, so only zero is periodic.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FAIL})$. We claim no thermodynamic determinant, target divisor, target functional equation or counting law, arithmetic/local factor, root number, automorphy, natural operator lift, Hilbert--Pólya operator, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

The package-local `results/c155_rule90_concentration_evidence.json` and `code/` directory contain the exact certificate, deterministic producer, independent checker, symbolic cross-check, replay, and mutation audit.

#### Ethics.

This mathematical and symbolic-computational study uses no human participants, animals, personal data, clinical records, or sensitive data; research ethics approval is not applicable.

#### Author contributions (CRediT).

This anonymous technical certificate does not assign individual authorship. Package provenance records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing at the artifact level. AI systems are not authors.

#### Conflicts of interest.

No conflict of interest is known.

#### Funding.

No external funding is reported for this technical certificate.

#### AI-use disclosure.

An AI coding assistant supported drafting, exact-code development, and internal proof checking. It was not an external reviewer. Released claims are exposed to deterministic reproduction, independent checking, symbolic cross-checking, and hostile mutation tests in the package.
