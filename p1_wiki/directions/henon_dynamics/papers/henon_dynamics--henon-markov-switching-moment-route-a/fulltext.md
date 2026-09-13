---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-markov-switching-moment-route-a"
canonical_tex: "henon_dynamics/henon_markov_switching_moment_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_markov_switching_moment_route_a/paper/main.pdf"
source_sha256: "784c8fecd3baa7c6787ad3408f38408e6facc63150562133f166d597053f5093"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Tangent Moment Operators for a Markov-Switching Hénon Cocycle

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_markov_switching_moment_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_markov_switching_moment_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_markov_switching_moment_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_markov_switching_moment_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a two-state Markov cocycle of dissipative polynomial Hénon maps sharing the origin. Once the environment chronology is fixed, the tangent cocycle owns exact operators on environment-conditioned first and symmetric second moments, of dimensions four and six. We give their matrices, traces through power six, and full determinant polynomials over $\mathbb Q$. A stationary control shows that averaging and taking a symmetric square differ by a rank-one matrix. These are local finite moment owners, not a global nonlinear Fredholm construction.
author:
- 'Route-A finite certificate C117'
title: |
  Exact Tangent Moment Operators for a\
  Markov-Switching Hénon Cocycle
```

## Markdown 正文

# Frozen random dynamics and chronology

Consider $$F_0(x,y)=(x^2+\tfrac12x-\tfrac13y,x),\qquad
 F_1(x,y)=(x^2-x-\tfrac12y,x),$$ with transition matrix $$P=\begin{pmatrix}2/3&1/3\\1/4&3/4\end{pmatrix},\qquad
 \pi=(3/7,4/7).$$ Rows of $P$ are the old mode and columns the new mode. Our load-bearing convention is: $s_n=i$ changes to $s_{n+1}=j$ with probability $P_{ij}$, then $F_j$ is applied. Both maps fix the origin, and their tangent matrices are $$B_0=\begin{pmatrix}1/2&-1/3\\1&0\end{pmatrix},\qquad
 B_1=\begin{pmatrix}-1&-1/2\\1&0\end{pmatrix},
 \quad (\det B_0,\det B_1)=(1/3,1/2).$$ Every statement below concerns this common-fixed-point tangent cocycle.

# Source-owned conditional moment operators

Let $m_i=\mathbb E[(x,y)^\mathsf T\mathbf1_{s=i}]$. The exact update is $$m'_j=\sum_iP_{ij}B_jm_i,$$ so the block $[j,i]$ of the first-moment owner is $P_{ij}B_j$. In the basis $(0{:}x,0{:}y,1{:}x,1{:}y)$ this is $$A_1=\begin{pmatrix}
 1/3&-2/9&1/8&-1/12\\2/3&0&1/4&0\\
 -1/3&-1/6&-3/4&-3/8\\1/3&0&3/4&0
 \end{pmatrix}.$$ For $(x',y')=(ax-by,x)$, the pullback on $(x^2,xy,y^2)$ is $$S(a,b)=\begin{pmatrix}a^2&-2ab&b^2\\a&-b&0\\1&0&0\end{pmatrix}.$$ Replacing $B_j$ by $S_j=S(a_j,b_j)$ gives the six-dimensional operator $[A_2]_{j,i}=P_{ij}S_j$. Thus the spaces and actions precede all coefficient calculations; neither matrix is fitted to a target sequence.

# Exact trace and determinant data

The first six traces are $$\begin{aligned}
 \operatorname{tr}(A_1^n):\;&-5/12,-11/27,95/384,
 -35249/373248,\\[-2pt]
 &-130525/8957952,3363181/80621568,\\
 \operatorname{tr}(A_2^n):\;&23/72,269/1728,110897/373248,
 1465921/8957952,\\[-2pt]
 &152582093/1934917632,2458516129/46438023168.\end{aligned}$$ Independent determinant expansion and Newton reconstruction agree exactly: $$\begin{aligned}
 \det(I-zA_1)={}&1+\tfrac5{12}z+\tfrac{251}{864}z^2
 +\tfrac{25}{1728}z^3+\tfrac{25}{864}z^4,\\
 \det(I-zA_2)={}&1-\tfrac{23}{72}z-\tfrac{139}{5184}z^2
 -\tfrac{29713}{373248}z^3\\
 &-\tfrac{14605}{1492992}z^4-\tfrac{925}{1492992}z^5
 +\tfrac{125}{373248}z^6.\end{aligned}$$

# A stationary averaging control

Stationary averaging gives $$\bar B=\begin{pmatrix}-5/14&-3/7\\1&0\end{pmatrix}.$$ However, with $\bar S=\sum_j\pi_jS_j$, $$\bar S-\operatorname{Sym}^2(\bar B)=
 \begin{pmatrix}27/49&6/49&1/147\\0&0&0\\0&0&0\end{pmatrix},$$ a nonzero rank-one gap. The exact quadratic moment lift therefore retains a switching-variance term discarded by the naive averaged-map control.

# Reproducibility and boundary

From the package directory run

    python3 code/c117_markov_producer.py
    python3 code/c117_markov_checker.py
    python3 code/c117_sympy_crosscheck.py
    python3 code/c117_replay.py
    python3 code/c117_mutation.py

The independent checker reconstructs both operators; SymPy performs 26 exact Newton/trace checks, canonical replay passes, and all 12 hostile semantic mutations are rejected.

The honest verdict is $A1=\texttt{A1\_WEAK}$ and $A2=\texttt{A2\_CERTIFIED\_PREFIX}$, qualified as source-owned finite tangent-moment operators only; $A3$ is not addressed and $A4$ fails. We do not claim a complete nonlinear random-orbit atlas, a global nonlinear transfer/Fredholm/nuclear owner, arithmetic local data, Euler factors, root numbers, automorphy, a Hilbert--Pólya operator, or Route B. The literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
