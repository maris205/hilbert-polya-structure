---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quantum-graph-unitary-scattering-route-a"
canonical_tex: "henon_dynamics/henon_quantum_graph_unitary_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quantum_graph_unitary_scattering_route_a/paper/main.pdf"
source_sha256: "2adc1a163484ca2dceca63cf52eeb8af4b11eb551b4af5b35d2d25cf3984163e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Unitary Scattering and Primitive-Orbit Secular Product for a Theta Metric Graph

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quantum_graph_unitary_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quantum_graph_unitary_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quantum_graph_unitary_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quantum_graph_unitary_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct an exact directed-bond quantum evolution for the theta graph with edge lengths $1,2,3$ and Kirchhoff vertices. The source determines a unitary family on $\mathbb C^6$, its metric clock, and an antiunitary bond reversal. Its secular determinant has a closed multivariate factorization and the same operator admits an all-period product over primitive directed-bond walks with signed scattering amplitudes. Wrong vertex normalization destroys unitarity, while direction-dependent reverse length destroys physical time reversal. This reaches a genuine Route-A unitary/scattering coordinate, but supplies no target divisor or Hilbert--Pólya claim.
author:
- 'Hénon Route-A Working Series, C133'
date: 24 August 2026
title: |
  Exact Unitary Scattering and Primitive-Orbit Secular Product\
  for a Theta Metric Graph
```

## Markdown 正文

# The structural advance

The preceding finite metaplectic construction supplied a natural quantization, but not a metric scattering system whose secular determinant is owned by its own primitive paths. Here the graph, vertex law, Hilbert space, clock, phases, and reversor are frozen before computation. The result reaches `A4_UNITARY_OR_SCATTERING_CANDIDATE`; this coordinate is not combined with any other candidate.

# Metric graph and bond map

Join vertices $L,R$ by three edges of lengths $\ell=(1,2,3)$. At either degree-three Kirchhoff vertex the incoming-to- outgoing matrix is $$C=\frac23\mathbf 1\mathbf 1^{T}-I_3
 =\begin{pmatrix}-1/3&2/3&2/3\\2/3&-1/3&2/3\\2/3&2/3&-1/3\end{pmatrix}.$$ Order directed bonds first from $L$ to $R$ and then from $R$ to $L$, and set $$S=\begin{pmatrix}0&C\\C&0\end{pmatrix},\qquad
 J=\begin{pmatrix}0&I_3\\I_3&0\end{pmatrix}.$$ On $\mathcal H=\mathbb C^6$, let $$P_{bb}(k)=e^{ik\ell_b/2},\qquad U(k)=P(k)S P(k).$$ The symmetric split assigns half of the incoming and outgoing bond phase to a scattering step. On a closed walk these halves accumulate exactly one $e^{ik\ell_b}$ per traversed bond; the metric clock is unchanged.

[\[thm:unitary\]]{#thm:unitary label="thm:unitary"} For real $k$, $U(k)$ is unitary. If $K$ is coefficient conjugation and $\Theta=JK$, then $$\Theta U(k)\Theta^{-1}=U(k)^{-1}.$$

$C$ has eigenvalue $1$ on the constant vector and $-1$ on its orthogonal complement. Thus $C^2=I$, $S^2=I$, and $S$ is real orthogonal. The diagonal $P(k)$ is unitary. Since reverse bonds share one undirected length, $J$ commutes with $P$ and $S$. Hence $J\overline{U(k)}J=P^{-1}SP^{-1}=U(k)^{-1}$.

# Exact secular determinant

Put $x_j=e^{ik\ell_j}$ and $M(k)=S\,\operatorname{diag}(x_1,x_2,x_3,x_1,x_2,x_3)$. Sylvester's identity gives $$D(\rho,k):=\det(I-\rho U(k))=\det(I-\rho M(k)).$$ At $\rho=1$, exact elimination gives $$\begin{aligned}
 D(1,k)=-\frac19&\bigl(3x_1x_2x_3-x_1x_2-x_1x_3-x_1-x_2x_3-x_2-x_3+3\bigr)\\
 &\times\bigl(3x_1x_2x_3+x_1x_2+x_1x_3-x_1+x_2x_3-x_2-x_3-3\bigr).\end{aligned}$$ For $t=e^{ik}$, so $(x_1,x_2,x_3)=(t,t^2,t^3)$, this becomes $$\begin{aligned}
\label{eq:factor}
 -\frac19&(t-1)^3(t+1)(t^2+1)(t^2+t+1)\nonumber\\
 &\qquad\times(3t^2-2t+3)(3t^2+5t+3).\end{aligned}$$ The factorization is a property of this graph; no external zeros were used.

# All-period primitive product

For $|\rho|$ small, finite-dimensional trace algebra gives $$\label{eq:trace}
 D(\rho,k)=\exp\!\left(-\sum_{n\ge1}\frac{\rho^n}{n}\operatorname{Tr}M(k)^n\right)
 =\prod_{[p]}\left(1-\rho^{n_p}A_p e^{ikL_p}\right).$$ Here $[p]$ is a primitive cyclic directed-bond walk, $n_p$ its topological period, $L_p$ its metric length, and $A_p$ the ordered product of Kirchhoff amplitudes. Thus repetitions, orientation, multiplicity, phases, and the negative backscatter amplitude are retained. The certificate records $14{,}760$ rooted walks and $1{,}905$ primitive cycles through period eight as replay sentinels; equation [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} is the all-order theorem.

# Controls and exact boundary

Replacing $2/3$ by $1/2$ gives $C_{\rm bad}^{T}C_{\rm bad}-I=-\frac14\mathbf1\mathbf1^T$, so the candidate is not unitary. In a second control, assigning reverse lengths $(1,2,4)$ while forward lengths remain $(1,2,3)$ produces eight nonzero entries in the $JK$-reversal defect. These failures bind Theorem [\[thm:unitary\]](#thm:unitary){reference-type="ref" reference="thm:unitary"} to a genuine Kirchhoff metric graph.

An independent checker reconstructs every headline field, a separate block determinant verifies [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"}, canonical replay is byte-identical, and forty-eight repaired-hash semantic mutations plus one stale-hash mutation are rejected. The strict result is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_UNITARY\_OR\_SCATTERING\_CANDIDATE}).$$ There is no prime-like orbit law, target divisor census, functional equation, or target counting law. No Hilbert--Pólya, automorphy, Euler-factor, or root-number claim is made under the `NO_BAD_EULER_OR_ROOT_NUMBER` firewall, and Route B remains unauthorized.

# Conclusion

C133 closes a source-owned unitary/scattering gate: one metric graph now owns its Hilbert space, clock, reversal, determinant, and primitive orbit product. Whether any separately authorized target comparison survives is an open and distinct question.
