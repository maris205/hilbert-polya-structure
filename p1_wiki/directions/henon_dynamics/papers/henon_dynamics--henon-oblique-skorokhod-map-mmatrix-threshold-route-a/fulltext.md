---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-oblique-skorokhod-map-mmatrix-threshold-route-a"
canonical_tex: "henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a/paper/main.pdf"
source_sha256: "b74e124b2217c29bf44a91c57fdccc61a3258c557d7c313a364bc3c89706bae1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sharp M-Matrix Threshold for a Two-Dimensional Oblique Skorokhod Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_oblique_skorokhod_map_mmatrix_threshold_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For oblique regulation in the quadrant with the stated two-axis reflection matrix $R$, we prove the *fixed point and sharp M-matrix chamber*: every càdlàg input has one and only one regulated path precisely when $\rho\sigma<1$. \>0 We add *weighted stability, Picard, and time change*: the natural norm has contraction factor $\sqrt{\rho\sigma}$, explicit solution stability, monotone geometric iteration, causality and reparameterization covariance. \>1 Finally, *sharp wall, executable audit, and Route-A boundary* close critical nonuniqueness, critical/supercritical nonexistence, triangular and post-jump faces without upgrading finite evidence to an all-path proof.
author:
- 'Route-A source-local certificate HCS-C346'
date: 3 September 2026
title: |
  A Sharp M-Matrix Threshold for a Two-Dimensional\
  Oblique Skorokhod Map
```

## Markdown 正文

trailerid \[\<C3462026090300000000000000000000\>\<C3462026090300000000000000000000\>\]

# Convention and the sharp existence theorem

Fix $T<\infty$, $\rho,\sigma\geq0$, and $$R=\begin{pmatrix}1&-\rho\\-\sigma&1\end{pmatrix}.$$ Let $x=(x_1,x_2)\in D([0,T],\mathbb R^2)$ with $x(0)\geq0$ coordinatewise. A solution consists of càdlàg $z,y$ such that $$\label{eq:sp}
 z=x+Ry\geq0,\qquad y(0)=0,\qquad y_i\text{ is nondecreasing},
 \qquad \int_{[0,t]}z_i(s)\,dy_i(s)=0.$$ The integrand is the *post-jump* state. Thus a regulator jump is supported on an axis after the jump, including simultaneous corner jumps.

For scalar càdlàg $f$, write $$(\mathcal Lf)(t)=\sup_{0\leq s\leq t}[-f(s)]_+.$$

[\[lem:scalar\]]{#lem:scalar label="lem:scalar"} If $f(0)\geq0$, the unique nondecreasing càdlàg $r$, with $r(0)=0$, for which $g=f+r\geq0$ and $\int g\,dr=0$ is $r=\mathcal Lf$. Moreover, $$\label{eq:Llip}
 \lVert\mathcal Lf-\mathcal Lh\rVert_\infty\leq\lVert f-h\rVert_\infty.$$

The running supremum is the least nondecreasing correction making $f+r$ nonnegative. It increases only at a new negative running minimum, where the post-jump corrected state is zero. Conversely, feasibility forces every regulator to dominate $\mathcal Lf$. A first strict excess would be an increase with positive corrected state, contradicting complementarity. Finally, positive part and running supremum are one-Lipschitz, proving [\[eq:Llip\]](#eq:Llip){reference-type="eqref" reference="eq:Llip"}.

[\[thm:main\]]{#thm:main label="thm:main"} Problem [\[eq:sp\]](#eq:sp){reference-type="eqref" reference="eq:sp"} has exactly one solution for every admissible input and every finite horizon if and only if $$\label{eq:chamber}
 \rho\sigma<1.$$ Inside this chamber, its regulator is the unique solution of $$\label{eq:fixed}
 y_1=\mathcal L(x_1-\rho y_2),\qquad
 y_2=\mathcal L(x_2-\sigma y_1).$$

With the other coordinate held fixed, each line of [\[eq:sp\]](#eq:sp){reference-type="eqref" reference="eq:sp"} is the scalar problem in Lemma [\[lem:scalar\]](#lem:scalar){reference-type="ref" reference="lem:scalar"}; hence [\[eq:sp\]](#eq:sp){reference-type="eqref" reference="eq:sp"} and [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} are equivalent. Conversely, at time zero the fixed-point equations and $x(0)\geq0$ imply $y_1(0)\leq\rho y_2(0)$ and $y_2(0)\leq\sigma y_1(0)$; since $\rho\sigma<1$, both values vanish. Thus the fixed point has the required initial condition.

First suppose $\rho,\sigma>0$, put $w_1=\sqrt\rho$, $w_2=\sqrt\sigma$, $q=\sqrt{\rho\sigma}$, and define $$\lVert u\rVert_w=\max_{i=1,2}\frac{\lVert u_i\rVert_\infty}{w_i}.$$ For the right side $\Phi_x$ of [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}, inequality [\[eq:Llip\]](#eq:Llip){reference-type="eqref" reference="eq:Llip"} gives $$\lVert\Phi_x(u)-\Phi_x(v)\rVert_w\leq q\lVert u-v\rVert_w.$$ Thus [\[eq:chamber\]](#eq:chamber){reference-type="eqref" reference="eq:chamber"} makes $\Phi_x$ a contraction on the complete space of bounded càdlàg pairs. Its unique fixed point is càdlàg and solves the problem. The constant $q$ is the best uniform coefficient: each weighted cross-coordinate estimate can be attained by a constant difference after a suitable downward input shift.

If $\rho=0$, solve successively $y_1=\mathcal Lx_1$ and $y_2=\mathcal L(x_2-\sigma y_1)$; if $\sigma=0$, reverse the order. This also covers $\rho=\sigma=0$ and proves sufficiency.

For necessity, let $\rho\sigma=1$. Then $R(\rho,1)^\mathsf T=0$, so zero input has the distinct solutions $$\label{eq:null}
 y=(\rho h,h),\qquad z=0,$$ for every nondecreasing càdlàg $h$ with $h(0)=0$. More strongly, whenever $\rho\sigma\geq1$, an input jumping from zero to $(-1,-1)$ cannot be feasible: the post-jump values would obey $$y_1\geq1+\rho y_2,\qquad y_2\geq1+\sigma y_1,$$ and hence $(1-\rho\sigma)y_1\geq1+\rho$, an impossibility. Therefore no point on or beyond the wall is well posed for every input.

\>0

# Quantitative stability and path structure

[\[thm:stable\]]{#thm:stable label="thm:stable"} Assume $\rho,\sigma>0$ and $q<1$. If inputs $x,x'$ have solutions $(z,y),(z',y')$, then $$\label{eq:stability}
 \lVert y-y'\rVert_w\leq\frac{\lVert x-x'\rVert_w}{1-q},
 \qquad
 \lVert z-z'\rVert_w\leq\frac{2\lVert x-x'\rVert_w}{1-q}.$$ Starting with $y^{(0)}=0$ and setting $y^{(n+1)}=\Phi_x(y^{(n)})$ gives a coordinatewise increasing sequence and $$\begin{aligned}
 \lVert y^{(n+1)}-y^{(n)}\rVert_w&\leq
 q^n\lVert y^{(1)}\rVert_w,\label{eq:successive}\\
 \lVert y-y^{(n)}\rVert_w&\leq
 \frac{q^n}{1-q}\lVert y^{(1)}\rVert_w.\label{eq:tail}\end{aligned}$$ The solution map is causal, preserves continuity, and commutes with continuous nondecreasing onto time changes that preserve the endpoints.

For two inputs, the scalar estimate gives $$\lVert\Phi_x(u)-\Phi_{x'}(v)\rVert_w
 \leq\lVert x-x'\rVert_w+q\lVert u-v\rVert_w.$$ Evaluate it at the two fixed points for the first inequality in [\[eq:stability\]](#eq:stability){reference-type="eqref" reference="eq:stability"}. Each normalized row of $R$ has weighted absolute sum $1+q$, whence $$\lVert R(y-y')\rVert_w\leq(1+q)\lVert y-y'\rVert_w.$$ Using $z-z'=x-x'+R(y-y')$ yields the second inequality. The map $\Phi_x$ is order preserving and $0\leq\Phi_x(0)$, so Picard iterates increase. Contraction gives [\[eq:successive\]](#eq:successive){reference-type="eqref" reference="eq:successive"}, and summing its geometric tail gives [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}.

Running suprema use only the past, so uniqueness gives causality. They map continuous functions to continuous functions; uniform Picard convergence then preserves continuity. If $\lambda:[0,T']\to[0,T]$ is continuous, nondecreasing, onto, and endpoint preserving, its initial images satisfy $\lambda([0,t])=[0,\lambda(t)]$. Consequently $$\mathcal L(f\circ\lambda)=(\mathcal Lf)\circ\lambda.$$ Compose [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} with $\lambda$ and use uniqueness. Flat pieces of $\lambda$ simply pause both state and regulator.

When one weight vanishes, the weighted norm is not defined. The triangular formulas in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} are the correct boundary statement; no singular limiting norm is smuggled into that face.

\>1

# Boundary closure and executable receipt

At the critical wall, equation [\[eq:null\]](#eq:null){reference-type="eqref" reference="eq:null"} proves nonuniqueness even for the smoothest possible input, whereas the negative jump proves nonexistence. These are separate failures. At normal reflection the solution is $(\mathcal Lx_1,\mathcal Lx_2)$; a one-sided coupling is triangular. The post-jump convention resolves a step input through the linear complementarity problem for $d=y-y^-$ and the new state $x+R(y^-+d)$. Strict inequality in [\[eq:chamber\]](#eq:chamber){reference-type="eqref" reference="eq:chamber"}, the off-diagonal signs, and simultaneous cascades are all therefore essential.

The machine-readable receipt has six rational matrices, 36 original events, 72 pause-expanded events, 27 Picard rows, three critical nonunique regulators, three no-solution witnesses, and 693 audited scalar leaves. An independent implementation performs 886 checks; a separate SymPy lane closes 5,125 exact identities; two isolated reproductions are byte-identical; and 68 parser, semantic, stale-hash and repaired-hash attacks are rejected. These checks audit conventions. Theorems [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}--[\[thm:stable\]](#thm:stable){reference-type="ref" reference="thm:stable"}, not finite enumeration, prove the all-input result.

The nearest workspace owners are scalar Moreau play (C332), one-interface skew Brownian motion (C266), total-variation flow (C279), and dry-friction capture (C238). None owns a two-axis oblique reflection map or its sharp M-matrix threshold.

The strict evaluation is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Free couplings and driven contacts have no rational-prime taxonomy; $\det R$ is not an Euler product or target determinant; and the dissipative regulator provides no natural target-zero quantization. Route A is rejected and Route B is locked under `NO_BAD_EULER_OR_ROOT_NUMBER`. No target arithmetic local data, Euler factor, root number, automorphy, divisor or counting law, functional equation, zero match, or Hilbert--Pólya operator is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The self-contained proof, independent reconstruction, hostile mutations and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

This source-local reconstruction makes no literature-priority claim.

9 J. M. Harrison and M. I. Reiman, "Reflected Brownian Motion on an Orthant," *Annals of Probability* 9 (1981), 302--308. DOI: [10.1214/aop/1176994471](https://doi.org/10.1214/aop/1176994471). P. Dupuis and H. Ishii, "On Lipschitz Continuity of the Solution Mapping to the Skorokhod Problem, with Applications," *Stochastics and Stochastics Reports* 35 (1991), 31--62. DOI: [10.1080/17442509108833688](https://doi.org/10.1080/17442509108833688).
