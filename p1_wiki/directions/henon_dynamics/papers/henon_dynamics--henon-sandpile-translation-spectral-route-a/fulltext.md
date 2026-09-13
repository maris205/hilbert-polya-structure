---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-sandpile-translation-spectral-route-a"
canonical_tex: "henon_dynamics/henon_sandpile_translation_spectral_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_sandpile_translation_spectral_route_a/paper/main.pdf"
source_sha256: "8730a2dae1ab874398054b82333f7f2ef02da2003b87a3722ae282879b1a91de"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Critical-Group Translation, Exact Spectrum, and Reversal for Recurrent Abelian Sandpiles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_sandpile_translation_spectral_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_sandpile_translation_spectral_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_sandpile_translation_spectral_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_sandpile_translation_spectral_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite connected undirected loopless multigraph with a sink and every nonnegative chip vector, we identify addition--stabilization on recurrent stable configurations with translation on the reduced-Laplacian critical group. Smith and adjugate formulas compute the translation order $L$ exactly. All recurrent orbits then have length $L$, giving closed fixed counts, Artin--Mazur zeta, finite Koopman determinant, and character spectrum. Group inversion supplies an antiunitary reversal, and the Koopman unitary is self-adjoint exactly when $L\le2$. A two-state path example shows why the positive theorem cannot be extended to all stable configurations.
author:
- 'Route-A structural certificate C176'
title: |
  Critical-Group Translation, Exact Spectrum, and Reversal\
  for Recurrent Abelian Sandpiles
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Abelian sandpile; recurrent configuration; critical group; Smith normal form; dynamical zeta; Koopman permutation.

chinese-simplified

中文摘要

本文对任意有限连通无向无环多重图、指定汇点和非负加砂向量，证明复现稳定构型上的 加砂与稳定化严格等同于约化[Laplacian]{lang="en"}临界群平移。 [Smith]{lang="en"}标准形和伴随矩阵给出平移阶 $L$ 的两套精确公式。 所有复现轨道均具有长度 $L$，从而得到不动点、动力 $\zeta$ 函数、有限维 [Koopman]{lang="en"}行列式和字符谱。群反演提供反酉时间反演，且 [Koopman]{lang="en"}算子自伴当且仅当 $L\le2$。一个两状态路径例子说明， 所有稳定构型上的映射不能被混同为复现置换。

关键词：阿贝尔沙堆；复现构型；临界群；[Smith]{lang="en"}标准形； 动力 $\zeta$ 函数；[Koopman]{lang="en"}置换。

# Sink stabilization and the recurrent bridge

Let $G$ be a finite connected undirected loopless multigraph with designated sink $s$. Write $V^\circ=V(G)\setminus\{s\}$ and $r=|V^\circ|$. With edge multiplicity $a_{vw}$, the reduced Laplacian is $$\Delta_{vv}=\deg(v),\qquad \Delta_{vw}=-a_{vw}\quad(v\ne w).$$ A stable configuration satisfies $0\le\eta_v<\deg(v)$ for every $v\in V^\circ$. Toppling $v$ sends one chip along every incident edge and loses chips entering the sink. Connectivity to the sink gives termination; commuting toppling vectors and the least-action argument give a unique stable result. For $b\in\mathbb N^r$, one clock step is $$T_b(\eta)=\operatorname{stab}(\eta+b).$$

The critical group and its order are $$K(G,s)=\mathbb Z^r/\Delta\mathbb Z^r,
\qquad D=|K(G,s)|=\det\Delta.$$ The next lemma owns the passage from physical height vectors to this quotient.

Start with the sink burned. A stable configuration is recurrent exactly when the remaining vertices can be burned successively whenever $$\eta_v\ge \#\{\text{edges from $v$ to currently unburned vertices}\}.$$ Every class in $K(G,s)$ contains exactly one recurrent stable configuration.

To see the dynamical content, let $\beta_v=a_{vs}$ count edges to the sink. Then $\beta=\Delta\mathbf1$. After adding $\beta$, a burning order is exactly a legal sequence in which each nonsink topples once: before $v$ topples, sink edges and edges from earlier burned vertices have supplied the threshold missing from the displayed inequality. The final height is $\eta+\beta-\Delta\mathbf1=\eta$. Conversely, a nonempty unburnable set is a forbidden subconfiguration and cannot belong to the recurrent communicating class.

For counting and uniqueness, fix local orders of parallel edges. Recording one earlier-burned predecessor edge for each vertex produces a spanning tree oriented to the sink; the height records the number and local rank of earlier edges, so the construction is invertible. The Laplacian cofactor expansion counts these trees by $\det\Delta=D$. The least-action comparison of two complete burning scripts shows that equivalent recurrent stable configurations coincide. Since the quotient also has $D$ classes, every class has exactly one recurrent representative.

Thus the recurrent set $\mathcal R(G,s)$ is canonically a $K(G,s)$-torsor; the recurrent representative of zero supplies its sandpile-group identity. Stabilization of a recurrent state after any nonnegative addition remains recurrent and satisfies $$[T_b(\eta)]=[\eta]+[b].$$ Actual addition--stabilization is therefore translation by $[b]$, rather than an abstract group substituted for the source dynamics.

# Two exact formulas for the translation order

Define $$L=\operatorname{ord}_{K(G,s)}([b])
=\min\{\ell\ge1:\ell b\in\Delta\mathbb Z^r\}.$$ Suppose a Smith decomposition is frozen as $$U\Delta V=\operatorname{diag}(d_1,\ldots,d_r),$$ with $U,V$ unimodular. Then $\ell[b]=0$ exactly when $d_i\mid\ell(Ub)_i$ for every coordinate. Hence $$\label{eq:smith}
L=\operatorname{lcm}_{1\le i\le r}
\frac{d_i}{\gcd(d_i,(Ub)_i)}.$$

The adjugate gives a coordinate-free alternative. Put $w=\operatorname{adj}(\Delta)b$. Since $\Delta^{-1}=\operatorname{adj}(\Delta)/D$, $$\ell b\in\Delta\mathbb Z^r
\quad\Longleftrightarrow\quad
D\mid\ell w_i\quad\text{for every }i.$$ Taking prime valuations in the coordinate conditions yields $$\label{eq:adj}
L=\operatorname{lcm}_{i}\frac{D}{\gcd(D,w_i)}
=\frac{D}{\gcd(D,w_1,\ldots,w_r)}.$$ For $b=0$, both [\[eq:smith\]](#eq:smith){reference-type="eqref" reference="eq:smith"} and [\[eq:adj\]](#eq:adj){reference-type="eqref" reference="eq:adj"} give $L=1$. If $r=0$, the empty determinant convention gives $D=L=1$ and one empty recurrent state.

# Cycles, zeta, characters, and reversal

Every recurrent orbit has exact length $L$, and there are $D/L$ primitive cycles. For every $n\ge1$, $$\#\operatorname{Fix}(T_b^n|\mathcal R)=
\begin{cases}D,&L\mid n,\\0,&L\nmid n.\end{cases}$$ Moreover $$\zeta_{T_b}(z)=(1-z^L)^{-D/L},\qquad
\det(I-zU_b)=(1-z^L)^{D/L},$$ and every $L$-th root of unity occurs in the spectrum of $U_b$ with multiplicity $D/L$.

A return at any recurrent state is exactly the equation $n[b]=0$, whose least positive solution is $L$ and is independent of the state. Dividing $D$ by the common orbit length gives the cycle count, fixed counts, and reciprocal zeta and determinant factors. For the spectral statement, the characters of $K(G,s)$ diagonalize $U_bf=f\circ T_b$. Restriction to the cyclic subgroup $\langle[b]\rangle$ is onto, and each character of that subgroup has $D/L$ extensions. Its values on $[b]$ are precisely the $L$-th roots.

Let $R(\eta)=\eta^{-1}$ in the recurrent sandpile group. Then $$R^2=I,\qquad RT_bR=T_b^{-1}.$$ Consequently $\Theta f=\overline{f\circ R}$ is antiunitary and $\Theta U_b\Theta=U_b^{-1}$. Since $U_b^*=U_b^{-1}$, $$U_b=U_b^*\Longleftrightarrow T_b=T_b^{-1}
\Longleftrightarrow 2[b]=0
\Longleftrightarrow L\le2.$$

# The full stable-state boundary

The preceding theorem is intentionally restricted to $\mathcal R(G,s)$. Consider the path $0$--$1$--$2$ with sink $2$ and nonsink addition $b=(1,0)$. Its stable states are $(0,0)$ and $(0,1)$. Direct toppling gives $$T_b(0,0)=(0,1),\qquad T_b(0,1)=(0,1).$$ Thus the full stable-state map is noninjective. The reduced Laplacian has determinant one, and the recurrent set is the singleton $\{(0,1)\}$, where the theorem correctly gives $D=L=1$.

No all-stable-state cycle classification or eventual-recurrence assertion is made for arbitrary $b$. Such a blanket statement would also fail at $b=0$, where every stable state is fixed. The natural Koopman unitary below belongs to the explicitly frozen recurrent phase space, not to a silently enlarged full stable space.

# Evidence and Route-A decision

The regression ledger contains all 30 connected simple-graph isomorphism types on two through five vertices, 137 sink choices, 780 labelled additions, 8,704 fixed rows, 32,938 full-stable transitions, 13,764 recurrent transitions, and 212,504 fixed-state comparisons. Among these labelled tests, 610 full stable maps are noninjective. A producer-independent checker passes 135,049 assertions, including opposite toppling orders, class signatures, every cycle and inversion identity. SymPy passes 5,248 Smith, adjugate, cyclic-spectrum and reversal checks; byte replay is exact; all 17 hostile mutations are rejected. These rows are sentinels; the multigraph scope rests on the proofs. Citation and reference registries each have population zero, and no external novelty or priority claim is made.

  Gate   Verdict                  Reason
  ------ ------------------------ ------------------------------------------------------
  A0     `FAIL`                   no intrinsic arithmetic origin
  A1     `WEAK`                   complete recurrent cycles, no arithmetic information
  A2     `FAIL`                   exact source zeta, no target divisor comparison
  A3     `FAIL`                   finite rational source, no target global structure
  A4     `NATURAL_QUANTIZATION`   same-clock recurrent permutation and reversal

The v0.2 tuple is $$\begin{aligned}
(&\texttt{A0\_FAIL},\texttt{A1\_WEAK},\texttt{A2\_FAIL},\\
 &\texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION}).
\end{aligned}$$ The overall verdict is `ROUTE_A_REJECTED`; Route B is false. A4 records a genuine finite same-clock unitary but cannot repair the failed arithmetic gate.

#### Limitations.

The graph is undirected, finite, connected and loopless; directed graphs need additional hypotheses. Finite character spectra do not supply prime semantics. There is no target divisor, functional equation, counting law, continuation, Weil compression, arithmetic local factor, Euler factor, root number, automorphy claim, or Hilbert--Pólya operator. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal, or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.
