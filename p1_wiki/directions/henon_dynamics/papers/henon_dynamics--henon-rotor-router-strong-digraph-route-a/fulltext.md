---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rotor-router-strong-digraph-route-a"
canonical_tex: "henon_dynamics/henon_rotor_router_strong_digraph_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rotor_router_strong_digraph_route_a/paper/main.pdf"
source_sha256: "669c532c9a80b53468f9ca16e10e9955c40753397920b1b18b6b75f565e5d84b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Rotor--Router Orbit and Frequency Theorem for Finite Strong Directed Multigraphs

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rotor_router_strong_digraph_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rotor_router_strong_digraph_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rotor_router_strong_digraph_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rotor_router_strong_digraph_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite nonempty strongly connected directed multigraph with distinguished arcs and arbitrary local cyclic rotor orders, we classify the rotor--router permutation on recurrent unicycle states. If $t_v$ counts directed spanning in-arborescences toward $v$, then $M=\gcd_vt_v$ is the number of recurrent orbits and $L=M^{-1}\sum_vd_v^+t_v$ is their common exact length. Every orbit visits $v$ exactly $d_v^+t_v/M$ times and traverses each distinguished outgoing arc at $v$ exactly $t_v/M$ times. We derive every fixed count, $\zeta_{\rm AM}=(1-z^L)^{-M}$, the finite Koopman determinant and spectrum, and the Eulerian edge-once degeneration. This is a sinkless unicycle theorem, not a sandpile translation. Its natural finite quantization is exact, but the absence of arithmetic labels forces a Route-A stop.
author:
- 'Route-A structural certificate HCS-C181'
title: |
  A Complete Rotor--Router Orbit and Frequency Theorem\
  for Finite Strong Directed Multigraphs
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** rotor--router; directed arborescence; unicycle; Eulerian digraph; dynamical zeta; permutation spectrum.

chinese-simplified

中文摘要

对任意有限非空强连通有向多重图及任意局部转子循环序，本文完整分类单环 状态上的转子路由置换。若 $t_v$ 是指向顶点 $v$ 的有向生成树数量，则 $M=\gcd_vt_v$ 等于循环轨道数，而 $L=M^{-1}\sum_vd_v^+t_v$ 是共同精确 周期。每条轨道对顶点及每条可区分弧的访问频率均有闭式公式，并由此得到 全部不动点计数、动力学泽塔、有限置换行列式、谱重数及欧拉图退化。本结果 研究无汇点的单环动力学，不把它改写为沙堆平移；自然有限量子化虽精确， 但缺少算术标签仍迫使甲路线停止。

# Frozen rotor system

Let $G=(V,A)$ be a finite nonempty strongly connected directed multigraph. Loops and parallel arcs are allowed, and every arc is distinguished. At each vertex fix a cyclic order of outgoing arcs. A state consists of a chip vertex and one currently selected outgoing arc at every vertex. One tick first advances the rotor at the chip vertex and then moves the chip along the newly selected arc.

The selected arcs form a functional digraph. A *unicycle state* has exactly one directed cycle and places the chip on that cycle. These are the recurrent states. This classical orbit framework and its spanning-tree connection are prior work; see Pham [@pham]. We claim no novelty for the classical rotor--router orbit theorem or directed matrix-tree theorem. In particular, Pham's Theorem 1 supplies the exact common orbit length and orbit count used below; our proof records that imported step before deriving the local distinguished-arc frequencies.

For $v\in V$, let $t_v$ be the number of spanning in-arborescences oriented toward $v$, equivalently the $v$-cofactor of the row Laplacian $\Delta=D_{\rm out}-A$. Put $$\label{eq:ML}
 M=\gcd_{v\in V}t_v,\qquad
 L=\frac1M\sum_{v\in V}d_v^+t_v.$$

# Orbit and local-frequency classification

[\[thm:main\]]{#thm:main label="thm:main"} For every frozen graph and every choice of cyclic rotor orders, the recurrent permutation has exactly $M$ orbits and every orbit has exact length $L$. On each orbit, $$\label{eq:freq}
 \#\{\text{departures from }v\}=\frac{d_v^+t_v}{M},\qquad
 \#\{\text{uses of each arc out of }v\}=\frac{t_v}{M}.$$ The recurrent phase has $ML=\sum_vd_v^+t_v$ states.

On a complete recurrent orbit every rotor returns to its starting arc. Let $x_v$ be the number of full turns made by the rotor at $v$. Every outgoing arc from $v$ is then used $x_v$ times, so flow balance gives $$\Delta^Tx=0.$$ Strong connectivity makes this kernel one-dimensional with a positive primitive integer generator. The directed matrix-tree theorem places the cofactor vector $t=(t_v)$ in the same kernel, so its primitive reduction is $t/M$. Thus $x=q(t/M)$ for some positive integer $q$. Pham's exact orbit-size theorem [@pham Theorem 1], for the same advance-then-move unicycle model and allowing loops and multiple arcs, gives orbit length $L$. But the length is also $\sum_vd_v^+x_v=qM^{-1}\sum_vd_v^+t_v=qL$, so $q=1$. This proves  [\[eq:freq\]](#eq:freq){reference-type="eqref" reference="eq:freq"} and shows how the imported exact-return theorem fixes the otherwise undetermined kernel multiple.

For the state count, fix the chip at $v$ and delete its selected rotor arc. The remaining selected arcs form an in-arborescence toward $v$. Conversely, an in-arborescence toward $v$ and a choice of one of its $d_v^+$ outgoing arcs reconstruct a unique unicycle state with chip on the unique cycle. Thus there are $d_v^+t_v$ states with chip $v$, and $ML$ in total. Division by Pham's exact common orbit length gives exactly $M$ orbits, consistently recovering the orbit-count clause of the same theorem.

## Primitive return and order independence {#primitive-return-and-order-independence .unnumbered}

The vector $t/M$ is independent of every local cyclic order. The order only decides when the outgoing arcs are used, while a full rotor turn uses each distinguished arc once. Flow balance alone proves only $x=q(t/M)$; it does not prove that the chip returns at the first formal completion of $t/M$. The missing primitivity is exactly the content of Pham's Theorem 1. In its proof one deletes all arcs leaving a chosen chip basepoint, acts by chip addition on the resulting acyclic rotors, and identifies the order of the deleted Laplacian row class in the quotient by the other row classes as $t_v/M$. That row-class order gives the first return and hence $q=1$. Citing this mechanism does not identify the frozen sinkless unicycle permutation with a sandpile stabilization or critical-group translation.

Loops enter both sides of the flow equation and cancel on the diagonal of $D_{\rm out}-A$, but they remain individual rotor choices and contribute to the degree-weighted state count. Parallel arcs likewise remain distinct in the local order and in [\[eq:freq\]](#eq:freq){reference-type="eqref" reference="eq:freq"}. The one-vertex graph with $q\ge1$ distinguished loops illustrates the boundary: $t_1=M=1$, $L=q$, and the rotor itself is one $q$-cycle, exactly as the theorem predicts.

# Fixed counts, zeta, and finite quantization

[\[cor:spectral\]]{#cor:spectral label="cor:spectral"} For every $n\ge1$, $$\#\operatorname{Fix}(R^n)=\begin{cases}ML,&L\mid n,\\0,&L\nmid n,\end{cases}
 \qquad \zeta_{\rm AM}(z)=(1-z^L)^{-M}.$$ On $\ell^2$ of recurrent states, the permutation Koopman unitary $U$ obeys $$\det(I-zU)=(1-z^L)^M,$$ and every $L$-th root of unity occurs with multiplicity $M$.

The recurrent permutation is a disjoint union of $M$ cycles of length $L$. The trace, logarithmic zeta, and characteristic polynomial statements follow cycle by cycle.

[\[cor:euler\]]{#cor:euler label="cor:euler"} If $G$ is Eulerian, all $t_v$ equal a common $\tau$, so $M=\tau$, $L=|A|$, there are $\tau$ recurrent orbits, and every orbit traverses every distinguished arc exactly once.

For an Eulerian graph, the all-ones vector lies in $\ker\Delta^T$. Uniqueness of its positive ray makes $t_v$ constant. Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} then gives the claims.

# Exact exhaustive validation

The theorem is global; finite enumeration is a regression sentinel rather than proof. The release nevertheless materializes the recurrent permutation, not just its predicted invariants.

  exact ledger                                            total
  -------------------------------------------- ----------------
  simple strong digraphs on $2,3,4$ vertices     $1+18+1{,}606$
  loop/parallel-arc multigraph sentinels                      4
  cyclic-order audits                                     1,697
  recurrent unicycle states audited                      43,267
  recurrent rotor orbits audited                          2,443
  independent-checker assertions                         93,786
  SymPy checks / full determinant graphs          $24{,}890/23$
  repaired/stale-hash mutation rejections                $25+1$

Every labeled simple loopless digraph through four vertices was filtered by strong connectivity. All cyclic orders were tested through three vertices, all orders were tested for the first 128 strong four-vertex graphs, and a canonical order was tested for every remaining graph. An independent checker uses Leibniz cofactors rather than the producer's elimination routine and reconstructs every state transition. Byte replay is exact.

# Source boundaries and Route-A decision

The system has no sink and no stabilization. Its proof does not identify unicycles with recurrent sandpiles and does not use a critical-group translation. The finite Koopman operator is a natural quantization, but abstract reversal of each cycle requires a chosen basepoint; the source graph does not canonically provide those basepoints.

This separation is structural rather than terminological. The phase space contains a moving chip and a selected arc at every vertex; recurrence is the single-cycle condition. Deleting the chip rotor is used only as a counting bijection to an arborescence, not as a stabilization map or a group action.

The strict tuple is $$(\texttt{A0\_FAIL},\texttt{A1\_WEAK},\texttt{A2\_FAIL},
 \texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION}).$$ The graph supplies complete primitive orbits and an exact finite unitary, but no rational-prime labels, prime-power weights, target amplitudes, target divisor, functional equation, or Weil compression. A0 failure therefore forces `ROUTE_A_REJECTED`; A4 cannot override the entry gate.

  -------------------------------------------------------------------------------------------------------
  gate                        decisive boundary
  --------------------------- ---------------------------------------------------------------------------
  A0\_FAIL                    graph invariants have no rational-prime labels or prime-power weights

  A1\_WEAK                    every recurrent orbit is classified, but no target amplitudes arise

  A2\_FAIL                    the exact divisor consists only of finite-cycle roots of unity

  A3\_FAIL                    there is no target functional equation, counting law, or Weil compression

  A4\_NATURAL\_QUANTIZATION   the recurrent permutation gives a canonical finite Koopman unitary
  -------------------------------------------------------------------------------------------------------

Strong connectivity and nonempty outgoing arc sets are structural hypotheses. For a reducible digraph the positive Laplacian kernel need not be one ray and the unicycle phase can split by terminal components, so the formulas above are not asserted unchanged. Loops and parallel arcs are included only because their arc identities and cyclic positions remain part of the frozen source.

The natural finite unitary resolves the spectrum of the recurrent permutation, not a self-adjoint arithmetic operator. Although each abstract cycle admits a reversor after choosing an origin, no source-canonical family of origins is available. We therefore do not promote abstract dihedral symmetry to a time-reversal theorem for the graph dynamics.

Pham's Theorem 1 is cited for the exact common orbit length and orbit count, including the chip-addition quotient/row-class-order step that establishes primitive return, as well as for classical ownership of the framework. The exhaustive census, local-frequency ledger, Route-A audit, and integrity artifacts are package contributions; no broad novelty claim is made for the classical orbit or matrix-tree theorems. The finite census can detect software faults but is not the proof of the all-graph result.

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. No prime table, arithmetic local factor, Euler factor, root number, automorphy, Hilbert--Pólya operator, Route-B authorization, external review, or acceptance rate is claimed.

1 T. V. Pham, *Orbits of rotor-router operation and stationary distribution of random walks on directed graphs*, Adv. Appl. Math. 70 (2015), 45--53, <https://arxiv.org/abs/1403.5875>.
