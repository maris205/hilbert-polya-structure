---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--166-hamming-weight-translation-dynamics"
canonical_tex: "symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/main.pdf"
source_sha256: "a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Hamming-Weight Translation Dynamics on a Coupled Cyclic Cube

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/166-hamming-weight-translation-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/166-hamming-weight-translation-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $n\geq2$, consider the finite self-map $T_n(x)=x+\operatorname{wt}(x)\mathbf1$ on $(\mathbb Z/n\mathbb Z)^n$, where the Hamming weight is an integer before reduction modulo $n$. Diagonal translation reduces each invariant orbit exactly to the occupancy map $j\mapsto j+m_j$ of a weak composition of $n$. We show that a nontrivial cycle exhausts the entire occupancy mass. This gives every exact-period count, the recurrent census, and the dynamical zeta function. A separate no-wrap argument gives a closed Stirling-number formula for every exact preperiod, with sharp maximum $n-2$ and a complete description of the last shell. Independently, we determine the one-step fibre of every target, its global marked exponential generating function, and the sharp maximum fibre. The exact iterate reduction is retained as a target-local $n$-phase oracle, not called a closed global all-time fibre census. The binary member and all classical counting ingredients are explicitly subtracted from the contribution boundary.
author:
- Anonymous
bibliography:
- references.bib
title: 'Hamming-Weight Translation Dynamics on a Coupled Cyclic Cube'
```

## Markdown 正文

# The literal map and the subtraction boundary

Let $H_n=(\mathbb Z/n\mathbb Z)^n$, where $n\geq2$, and let $$\label{eq:literal}
 T_n(x)=x+\operatorname{wt}(x)\mathbf 1.$$ Here $\operatorname{wt}(x)=|\{i:x_i\ne0\}|$ is the integer Hamming weight and only the addition in (1) is reduced modulo $n$. The term "Hamming weight" is classical [@Hamming1950]. We write $P_{n,k}$ for the number of points of exact period $k$, and $D_{n,d}$ for the number of points of exact preperiod $d$; thus $D_{n,0}=|\operatorname{Rec}(T_n)|$.

The case $n=2$ is exactly the parity-controlled binary complement map used by Meyer and Pommersheim [@MeyerPommersheim2010]; it receives zero contribution credit here. We likewise assign zero credit to diagonal group-action language, multinomial and Stirling identities, ordered Bell/Fubini numbers, and the finite-map zeta conversion. One-ball siteswaps already give a weight-dependent cyclic update in a different carrier [@BuhlerEtAl1994]; occupancy and parking-function neighbours are classical [@KonheimWeiss1966; @LacknerPanholzer2016], including an ordered-Bell parking connection [@MeylesEtAl2023]. Those ingredients and neighbours receive zero credit. The claims below concern the exact conjunction forced by (1). The literature search was bounded, so no claim of novelty or priority is made.

Let $\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}$ denote a Stirling number of the second kind. Our formulas are $$\begin{aligned}
 P_{n,1}&=1+(n-1)^n,&
 P_{n,k}&=k!\left\{\begin{matrix}n\\k\end{matrix}\right\}
 &&(2\leq k\leq n),                                    \label{eq:period}\\
 D_{n,0}&=(n-1)^n+\sum_{k=1}^n
 k!\left\{\begin{matrix}n\\k\end{matrix}\right\},  \label{eq:rec}\\
 D_{n,d}&=d!\sum_{s=d}^{n-1}\binom ns
 \left\{\begin{matrix}s\\d\end{matrix}\right\}
 (n-d-1)^{n-s} &&(1\leq d\leq n-2),                   \label{eq:depth}\\
 D_{n,d}&=0 &&(d\geq n-1).\end{aligned}$$ The convention $0^0=1$ is used only where the displayed finite sum requires it.

# Exact diagonal phase reduction

Fix a target $y\in H_n$ and put $$m_j=m_j(y)=|\{i:y_i=j\}|,
 \qquad X_j=y-j\mathbf 1\quad(j\in\mathbb Z/n\mathbb Z).$$ The $n$ points $X_j$ are distinct: diagonal translation by a nonzero residue cannot fix a coordinate. Their occupancy vector $m=(m_0,\ldots,m_{n-1})$ is a weak composition of $n$. Since $X_j$ has $m_j$ zero coordinates, $$\label{eq:phase}
 T_n(X_j)=X_{g_m(j)},\qquad g_m(j)=j+m_j\pmod n.$$ This is an exact conjugacy on each diagonal orbit, not a quotient that forgets transitions.

[\[thm:oracle\]]{#thm:oracle label="thm:oracle"} For every $t\geq0$ and target $y$ as above, $$\label{eq:oracle}
 T_n^t(X_j)=X_{g_m^t(j)},\qquad
 |(T_n^t)^{-1}(y)|=|\{j:g_m^t(j)=0\}|.$$

The first identity follows from (6) by induction. Coordinate differences are invariant under (1), so every source mapping to $y$ lies in the same diagonal orbit and is one of the $X_j$. The second identity follows.

Formula (7) is an exact every-target, every-time algorithm on $n$ phases. It is not promoted to a closed global all-time fibre census.

# Mass exhaustion, periods, and zeta

[\[lem:cycle\]]{#lem:cycle label="lem:cycle"} If $C$ is a nontrivial cycle of $g_m$, then $m_j>0$ exactly on $C$, $\sum_{j\in C}m_j=n$, and the positive entries are the clockwise gaps between consecutive elements of $C$. Conversely, every nonempty support whose entries are its clockwise gaps gives that support as one cycle. There is at most one nontrivial cycle, and all phases outside it that are recurrent are fixed zero positions.

Every edge on a nontrivial cycle has positive increment. Lift one circuit to the integers. Its increment sum is a positive multiple of $n$, but is at most $\sum_jm_j=n$; hence it equals $n$. Equality exhausts the mass, so entries off the cycle vanish, and a single winding forces each entry to be the next clockwise gap. The converse is immediate. A second nontrivial cycle would require the same total mass. Finally, a phase is fixed precisely when $m_j\in\{0,n\}$.

[\[thm:period\]]{#thm:period label="thm:period"} The only possible exact periods are $1,\ldots,n$, and their point counts are (2). Consequently (3) holds, the exact number of $k$-cycles is $P_{n,k}/k$, and $$\begin{aligned}
 |\operatorname{Fix}(T_n^r)|&=\sum_{k\mid r,\,k\leq n}P_{n,k},\\
 \zeta_{T_n}(z)&=\prod_{k=1}^n(1-z^k)^{-P_{n,k}/k}.\end{aligned}$$

A fixed state either has no zero coordinate or is the zero vector, giving $P_{n,1}=1+(n-1)^n$. For $k\geq2$, anchor a period-$k$ state at phase zero. Lemma [\[lem:cycle\]](#lem:cycle){reference-type="ref" reference="lem:cycle"} says that its $k$ positive occupancies are a positive ordered composition $a_1+\cdots+a_k=n$ in clockwise order. For a fixed composition there are $n!/(a_1!\cdots a_k!)$ labelled states. Thus $$P_{n,k}=\sum_{\substack{a_1+\cdots+a_k=n\\a_i>0}}
 \frac{n!}{a_1!\cdots a_k!}
 =k!\left\{\begin{matrix}n\\k\end{matrix}\right\}.$$ Each such point has exact period $k$. Summing exact-period counts gives (3); divisor summation and the standard exponential definition of the dynamical zeta function give (8)--(9).

# Every transient depth and the sharp last shell

[\[thm:depth\]]{#thm:depth label="thm:depth"} Equations (4)--(5) hold. In particular the maximum preperiod is $n-2$, including the value zero at $n=2$. For $n\geq3$, a diagonal orbit has a point of depth $n-2$ exactly when its occupancy profile has one zero at $z$, one entry two at $e$, all other entries one, and $e\ne z-1\pmod n$. The phase $z+1$ always has maximum depth; $z+2$ is a second such phase exactly when $e=z+1$. Hence $$D_{n,n-2}=\frac{(n-1)n!}{2}.$$

Consider a transient phase path of length $d$ before it first reaches a zero position. Its positive increments have total strictly below $n$: equality would return to its initial phase, and a larger total is impossible because the whole profile has mass $n$. After a cyclic choice of lift, its partial sums therefore satisfy $$0=S_0<S_1<\cdots<S_d=s<n.$$ Writing $a_i=S_i-S_{i-1}$ fixes the $d$ visited occupancies to positive values summing to $s$, fixes the endpoint occupancy to zero, and leaves $n-s$ indistinguishable coordinate labels to occupy the other $n-d-1$ phases. The weighted multinomial sum for fixed $a_1,\ldots,a_d$ is $$\frac{n!}{a_1!\cdots a_d!}\,
 \frac{(n-d-1)^{n-s}}{(n-s)!}.$$ Summing over positive ordered compositions of $s$, using $$\sum_{\substack{a_1+\cdots+a_d=s\\a_i>0}}
 \frac{s!}{a_1!\cdots a_d!}
 =d!\left\{\begin{matrix}s\\d\end{matrix}\right\},$$ and then accounting for cyclic anchoring gives exactly (4). More explicitly, there are $n$ lifted starting phases and every literal state has $n$ choices of anchor, so these factors cancel. Formula (11) allows at most $n-2$ visited positive phases, proving (5).

Equality forces exactly one zero, one excess unit above the remaining ones, and excludes placing that excess immediately before the zero; tracing (11) gives precisely the phases stated in the theorem. Conversely those phases trace $n-2$ positive entries before the zero. There are $n(n-2)$ profile choices and $n$ extra maximum-depth phases when $e=z+1$. Each profile has $n!/2$ labelled realizations, while each state is represented by $n$ anchor--phase pairs. Division by $n$ proves (10). For $n=2$ the phase maps have no transient point, consistently giving maximum depth zero.

# Every-target one-step fibres

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For a target $y$ with multiplicities $m_j=m_j(y)$, $$|T_n^{-1}(y)|=\mathbf1_{\{y=0\}}+\mathbf1_{\{m_0=0\}}
 +\sum_{k=1}^{n-1}\mathbf1_{\{m_k=n-k\}}.             \label{eq:fibre}$$ If $I_n(u)=\sum_{y\in H_n}u^{|T_n^{-1}(y)|}$, then $$I_n(u)=(u-1)+n![z^n](e^z+u-1)
 \prod_{r=1}^{n-1}\left(e^z+(u-1)\frac{z^r}{r!}\right). \label{eq:egf}$$ In particular the image size is $n^n-[u^0]I_n(u)$. Put $$h_n=\left\lfloor\frac{\sqrt{8n+1}-1}{2}\right\rfloor.$$ Then $$\max_y|T_n^{-1}(y)|=
 \begin{cases}1,&n=2,\\1+h_n,&n\geq3.\end{cases}      \label{eq:maxfibre}$$ For $n\geq3$, equality holds exactly when $m_0=0$ and exactly $h_n$ of the conditions $m_k=n-k$, $1\leq k<n$, hold.

Every source has the form $x=y-k\mathbf 1$. It has $m_k$ zero coordinates and weight $n-m_k$. For $1\leq k<n$, the equation $T_n(x)=y$ is therefore equivalent to $m_k=n-k$. The identical residue shift at integer weights zero and $n$ must be separated before reduction: the former occurs only at $y=0$, while the latter occurs exactly when $m_0=0$. They cannot occur together, proving (12).

For the multinomial target sum, the factor $e^z+u-1$ marks $m_0=0$. After reindexing $r=n-k$, the factor $e^z+(u-1)z^r/r!$ marks $m_k=r$. The correction $u-1$ changes the otherwise unmarked all-zero target to indegree one. Coefficient extraction gives (13).

If $h$ middle conditions in (12) hold, their distinct positive prescribed counts sum to at least $1+\cdots+h$, so $h\leq h_n$. The full-support branch adds at most one. For $n\geq3$, assign the counts $1,\ldots,h_n$ to their corresponding symbols. When the remainder is zero, no extra bin is needed. Otherwise put it in symbol $1$: then $n\geq4$, this symbol is not among those already prescribed, and the remainder is at most $h_n<n-1$, so it triggers no new middle condition. This realizes $1+h_n$. Thus equality has exactly the stated form. Direct inspection at $n=2$ gives a permutation and maximum fibre one.

# Controls and scope

All proofs above are uniform in the composite or prime value of $n$; no field structure is used. A paper-local, standard-library exact program starts from (1), enumerates every state through $n=7$, checks the complete period, depth, one-step fibre, and target-local iterate formulas, and separately checks composition identities and boundary witnesses in larger boxes. Computation is a falsification control, not part of any proof.

The bounded source search does not establish novelty. In particular, the exact $n=2$ map, siteswap neighbour, Hamming terminology, occupancy language, Stirling and ordered-Bell identities, and generic finite-map zeta algebra contribute no claimed new ingredient. What remains under study is the coupled $n\geq3$ theorem package for (1).

**External status: HOLD\_EXTERNAL.**
