---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-symmetric-matrix-riccati-mobius-flow-route-a"
canonical_tex: "henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/paper/main.pdf"
source_sha256: "13abafaa5aa911db3f6c6c18d8e3d40431be10d7d53674446f56aa0639843286"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Möbius and Morse--Bott Atlas for a Symmetric Matrix Riccati Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite dimension we solve $\dot X=I-X^2$ on real symmetric matrices and classify its maximal classical chart, every signed-time pole, all forward limits, and the exact convergence remainder. \>0 We also prove a strict trace-gradient law, identify every involution component as a Grassmann Morse--Bott stratum with complete index, and derive the full Loewner formula for the nonlinear time map. \>1 A 1,502-leaf regression archive and independent adversarial lanes audit the formulas and their Route-A boundary without replacing proof.
author:
- 'Route-A source-local certificate HCS-C309'
date: 3 September 2026
title: 'A Complete Möbius and Morse--Bott Atlas for a Symmetric Matrix Riccati Flow'
```

## Markdown 正文

trailerid \[\<C3092026090300000000000000000000\>\<C3092026090300000000000000000000\>\]

# Exact flow and maximal chart

Let $X_0\in\operatorname{Sym}(n,\mathbb R)$ and consider $$\label{eq:ode}
 \dot X=I-X^2,\qquad X(0)=X_0.$$ Put $C=\cosh t$, $S=\sinh t$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} On the connected component through zero of $\{t:\det(CI+SX_0)\ne0\}$, the unique classical solution is $$\label{eq:flow}
 F_t(X_0)=(CX_0+SI)(CI+SX_0)^{-1}.$$ If $\lambda_1,\ldots,\lambda_n$ are the eigenvalues of $X_0$, the only finite chart singularities are $$\label{eq:poles}
 t_j=\operatorname{arctanh}(-1/\lambda_j),\qquad |\lambda_j|>1,$$ with their spectral multiplicities. Thus the flow is forward global iff $\lambda_{\min}(X_0)\ge-1$. In that case $$\label{eq:limit}
 F_t(X_0)\longrightarrow I-2P_{\ker(X_0+I)}.$$ For each $\lambda>-1$ the exact scalar remainder is $$\label{eq:rate}
 f_t(\lambda)-1=
 \frac{2(\lambda-1)e^{-2t}}
 {(1+\lambda)+(1-\lambda)e^{-2t}}.$$ Moreover $F_t\circ F_s=F_{t+s}$ whenever both expressions remain in one classical chart.

Solve the symmetric block-linear system $$\dot U=V,\qquad \dot V=U,\qquad U(0)=I,\quad V(0)=X_0.$$ It gives $U=CI+SX_0$ and $V=SI+CX_0$. While $U$ is invertible, $X=VU^{-1}$ obeys [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"}, proving [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"}; local uniqueness then gives maximality in that chart. The spectral theorem reduces $F_t$ to $f_t(\lambda)=(C\lambda+S)/(C+S\lambda)$. Its denominator vanishes exactly as in [\[eq:poles\]](#eq:poles){reference-type="eqref" reference="eq:poles"}. For $t>0$ this happens precisely when $\lambda<-1$. The values $-1$ and $1$ are fixed, every $\lambda>-1$ tends to $1$, and elementary exponential algebra yields [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"}. Multiplication of the two scalar Möbius matrices gives the addition law, hence the semigroup identity by functional calculus.

\>0

# Gradient geometry and the complete equilibrium index

Define $$\label{eq:phi}
 \Phi(X)=\operatorname{tr}(X^3/3-X).$$ The Frobenius gradient is $X^2-I$, so along [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} $$\label{eq:diss}
 \dot\Phi=-\|I-X^2\|_F^2.$$ In particular, continuity plus strict decrease rules out every nonconstant recurrent classical trajectory.

[\[thm:mb\]]{#thm:mb label="thm:mb"} The equilibria are exactly the symmetric involutions. The component with $p$ eigenvalues $+1$ and $q=n-p$ eigenvalues $-1$ is $$\mathcal E_{p,q}\simeq O(n)/(O(p)\times O(q)).$$ At every point of this component, the stable, unstable, and center dimensions of [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} are respectively $$\label{eq:index}
 \frac{p(p+1)}2,\qquad \frac{q(q+1)}2,\qquad pq.$$ The center space equals $T\mathcal E_{p,q}$, so the critical manifold of $\Phi$ is Morse--Bott.

An equilibrium satisfies $S^2=I$ and is orthogonally conjugate to $\operatorname{diag}(I_p,-I_q)$, which proves the homogeneous-space claim. The linearization is $H\mapsto-(SH+HS)$. Writing a symmetric perturbation in plus/minus blocks gives eigenvalue $-2$ on the symmetric $p$ block, $+2$ on the symmetric $q$ block, and zero on the $p\times q$ off-diagonal block. Their dimensions are [\[eq:index\]](#eq:index){reference-type="eqref" reference="eq:index"}; infinitesimal orthogonal conjugacy identifies the last block with the tangent space.

[\[thm:frechet\]]{#thm:frechet label="thm:frechet"} In an eigenbasis of $X_0$, on every regular chart, $$\label{eq:loewner}
 (DF_t(X_0)H)_{ij}=
 \frac{H_{ij}}{(C+\lambda_iS)(C+\lambda_jS)}.$$

For $i\ne j$, the divided difference of $f_t$ is $(f_t(x)-f_t(y))/(x-y)=((C+xS)(C+yS))^{-1}$ because $C^2-S^2=1$. Its diagonal limit is $f_t'(x)=(C+xS)^{-2}$. The standard spectral divided-difference formula, also valid across repeated eigenvalues by this limit, gives [\[eq:loewner\]](#eq:loewner){reference-type="eqref" reference="eq:loewner"}.

\>1

# Evidence, collisions, and Route-A boundary

Sixteen rational spectra test fixed points, heteroclinic and blow-up chambers, repeated roots, two-sided poles and pole ties. Signed-time probes record the flow, denominator, vector field and [\[eq:diss\]](#eq:diss){reference-type="eqref" reference="eq:diss"}; all Loewner entries at $t=0.7$ and all 44 signatures through $n=8$ give 1,502 audited leaves. A producer-independent checker performs 1,352 checks, SymPy proves 74 identities, isolated replay is byte exact, and 34 repaired-hash or parser attacks must fail. Three manuscript rounds are rebuilt twice at a fixed epoch. These are regression controls; the proofs above cover all finite dimensions.

C185 is an isospectral double-bracket flow, C298 evolves fixed-rank projections on a Grassmannian, and C297 has one scalar projective Riccati coordinate in a two-mode PT system. None owns the present moving-spectrum matrix Möbius flow with its complete pole and involution atlas.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the exact tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Matrix eigenvalues have no rational-prime ownership (A0); the gradient law excludes nontrivial recurrent primitive trajectories (A1); physical time is not a logarithmic-prime clock (A2); the chart determinant is not a target determinant or functional equation (A3). The finite symmetric block lift is an exact source linearization, but has no target-zero correspondence and is not a Hilbert--Pólya operator (A4). Hence the result is `ROUTE_A_REJECTED`; Route B stays locked. No target Euler factor, root number, automorphy statement, divisor law, functional equation, or zero match is asserted.

#### Reproducibility and AI use.

A generative language model assisted code scaffolding and prose. Exact proofs, independent executable checks, mutation tests, and deterministic artifacts define the auditable record; final responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

The citation supplies matrix-Riccati and symmetric-flow context, not a literature-priority claim for this packaging.

9 U. Helmke, "Isospectral flows on symmetric matrices and the Riccati equation," *Systems & Control Letters* 16 (1991), 159--165. DOI: [10.1016/0167-6911(91)90044-F](https://doi.org/10.1016/0167-6911(91)90044-F).
