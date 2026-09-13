---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-16-endpoint-gaussian-resolution-rank"
canonical_tex: "zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/endpoint-centered-gaussian-resolution-rank.pdf"
source_sha256: "f4b4cf95ad43b71b805ac8c7561afab849ee7dde26dfde2259cd33ae473557c2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint-Centered Gaussian Resolution at a Quadratic Band-Merging Map: A Singular-Value Theorem for the Half-Logarithmic Rank

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/endpoint-centered-gaussian-resolution-rank.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the first algebraic band-merging parameter of $f_u(x)=1-u x^2$, parity extraction leaves a small-noise bulk resonance cloud whose observed degree grows on the scale $\log(1/\sigma)/(2\log\lambda)$. The preceding determinant analysis derived this scale geometrically but did not realize it as an operator rank. We give such a realization for the canonical endpoint row family.

  Let $p_{2k}\to1$ be the distinguished boundary cycles and put $\delta_k=1-p_{2k}$. Their exact inverse-branch construction gives $$\delta_k=C_{\mathrm b}\lambda^{-2k}(1+o(1)),
   \qquad C_{\mathrm b}>0.$$ For a Gaussian transition row with mean $1-\delta$, conditioned not to cross the upper state boundary, let $\psi_{\sigma,\delta}$ be its unit Hellinger fingerprint. If $t=\delta/\sigma$ and $s=\varepsilon/\sigma$, their affinity is exactly $$\langle\psi_{\sigma,\delta},\psi_{\sigma,\varepsilon}\rangle
   =A(t,s)
   =e^{-(t-s)^2/8}
   \frac{\Phi((t+s)/2)}{\sqrt{\Phi(t)\Phi(s)}}.$$ The uncentered synthesis of these rows is unbounded because every fingerprint converges to the same endpoint vector. Orthogonally removing that vector defines the compact resolution operator $$\mathcal R_\sigma e_k
   =\bigl(\mathrm I-|\psi_{\sigma,0}\rangle
   \langle\psi_{\sigma,0}|\bigr)\psi_{\sigma,\delta_k}.$$ We prove $$\|\mathcal R_\sigma\|_{S_2}^2
   =\frac{\log(1/\sigma)}{2\log\lambda}+O(1)$$ and, for every fixed $0<\eta<1$, $$\boxed{
   \#\{j:s_j(\mathcal R_\sigma)>\eta\}
   =\frac{\log(1/\sigma)}{2\log\lambda}+O_\eta(1).}$$ The same law holds for the finite-interval and folded Gaussian row families; it also holds for $L^2$-normalized linear kernel rows. The omitted lower-boundary and reflected masses are exponentially small. Thus the half-logarithmic clock is a singular-value theorem, not a fitted resonance count.

  High-precision boundary cycles and exact Gram matrices audit the result over $10^{-14}\le\sigma\le10^{-2}$. At the parameter-free half-energy threshold $s_j^2>1/2$, the endpoint rank agrees with the independently selected bulk cloud degree at six of the seven archived noise levels and differs by one at the coarsest level. This agreement is numerical evidence only. Identifying the endpoint row rank with the actual Markov resonance count still requires a dynamical block factorization and the finite-shift reduction; neither is claimed here.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Endpoint-Centered Gaussian Resolution**\
  **at a Quadratic Band-Merging Map:**\
  A Singular-Value Theorem for the Half-Logarithmic Rank
```

## Markdown 正文

**Keywords:** transfer operator; Gaussian perturbation; Hellinger affinity; singular values; effective rank; endpoint boundary layer; resonance cloud; quadratic map.

**MSC 2020:** 37E05; 37D25; 47B10; 47B35; 60J05; 65P30.

# Introduction {#sec:introduction}

An entire finite-noise determinant can approach a deterministic meromorphic germ only by developing an increasing spectral complexity. At the quadratic band-merging map, the deterministic parity-extracted bulk determinant has the exact factor $$\label{eq:previous-pole}
 \frac1{1-z^2/\lambda}.$$ Its negative leading moments rule out every fixed finite set of limiting resonances. Sparse spectra show a growing cloud near $|\mu|=\lambda^{-1/2}$, with phases close to the roots-of-unity grid of a geometric pole section [@WangBulkScattering2026].

The missing integer in that picture is the degree of the section. A boundary cycle approaches the state endpoint like $\lambda^{-m}$ at original time $m$. At two-step component time $k=m/2$, the equality $\lambda^{-2k}\asymp\sigma$ suggests $$\label{eq:heuristic-clock}
 k\asymp\frac{\log(1/\sigma)}{2\log\lambda}.$$ This argument locates a scale but does not define a rank. In particular, a count of visually separated eigenvalues would be circular: it would insert the numerical cloud into the definition one is trying to explain.

We instead ask how many boundary contacts remain distinguishable under the actual Gaussian resolution. Transition probabilities are compared in Hellinger geometry, where square-root densities are unit vectors and their inner product is the Hellinger affinity [@LeCamYang2000]. The endpoint rows share a nonzero limiting vector, which must be extracted before a compact operator appears. After that projection, the geometric boundary ladder becomes a Hilbert--Schmidt synthesis operator with a growing plateau of singular values near one.

This distinction is central: $$\label{eq:three-levels}
 \boxed{
 \begin{gathered}
 \text{endpoint row rank}
 \quad\Longrightarrow?\quad
 \text{dynamical endpoint-block rank}\\
 \phantom{\text{endpoint row rank}}\quad\Longrightarrow?\quad
 \text{bulk resonance-cloud degree}
 \end{gathered}}$$ The first quantity is constructed and analyzed here. The two arrows remain proof obligations. The paper therefore advances the effective-rank step without silently promoting a row-resolution theorem into an eigenvalue theorem.

## Main results and logical status {#main-results-and-logical-status .unnumbered}

1.  The boundary-cycle asymptotic is sharpened to a ratio and gap law: $$\frac{\delta_{k+1}}{\delta_k}\to\lambda^{-2},
      \qquad
      \delta_k-\delta_{k+1}
      \sim C_{\mathrm b}(1-\lambda^{-2})\lambda^{-2k}.$$

2.  Conditioned Gaussian rows have the exact scale-free Hellinger kernel $A(t,s)$ displayed in the abstract. Endpoint projection leaves energy $$F(t)=\|\mathcal Q\psi_t\|_2^2
      =\frac{\pi-2}{4\pi}t^2+O(t^3)$$ as $t\downarrow0$, while $F(t)\to1$ exponentially as $t\to\infty$.

3.  The unprojected row synthesis has no bounded extension from $\ell^2$. The endpoint-projected synthesis is Hilbert--Schmidt and has an explicit Gram matrix.

4.  The squared Hilbert--Schmidt norm and every fixed subunit threshold rank obey the half-logarithmic law in [\[eq:heuristic-clock\]](#eq:heuristic-clock){reference-type="eqref" reference="eq:heuristic-clock"}. These are analytic theorems proved without finite matrices.

5.  The theorem extends from Hellinger fingerprints to every fixed positive power of the Gaussian density. In particular it holds for $L^2$-normalized linear kernel rows. Conditioning on $[-1,1]$ and folding by $y\mapsto|y|$ preserve the same rank law.

6.  High-precision computations evaluate $C_{\mathrm b}=0.4608051492\ldots$, test the exact Gram kernel and show a bounded staircase defect down to $\sigma=10^{-14}$. These decimals and finite spectra are numerical diagnostics.

7.  With the fixed half-energy threshold $\eta=2^{-1/2}$, the model ranks are $2,3,4,5,5,6,7$ on the seven RH-15 noise levels. The archived cloud degrees are $3,3,4,5,5,6,7$. This close match does not prove either arrow in [\[eq:three-levels\]](#eq:three-levels){reference-type="eqref" reference="eq:three-levels"}.

# The geometric boundary ladder {#sec:boundary-ladder}

Let $u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and put $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r=1.678573510428322\ldots,
 \qquad
 a=\lambda^{-2}=0.354910844401770\ldots.$$ For $f(x)=1-u_{\mathrm c}x^2$, the postcritical orbit is $$\label{eq:critical-orbit}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r.$$

The two positive inverse-branch compositions used by the boundary word are $$\label{eq:h-q}
 h=g_+\circ g_+,
 \qquad
 q=g_+\circ g_-,
 \qquad
 g_\pm(y)=\pm\sqrt{\frac{1-y}{u_{\mathrm c}}}.$$ They satisfy $$\label{eq:h-q-data}
 h(r)=r,
 \quad h'(r)=a,
 \quad q(r)=1,
 \quad q'(r)=-\frac1{2u_{\mathrm c}\lambda}.$$ For $k\ge1$, let $p_{2k}$ be the unique fixed point of $$\label{eq:boundary-fixed-point}
 p_{2k}=q\bigl(h^{k-1}(p_{2k})\bigr),
 \qquad
 \delta_k=1-p_{2k}.$$ It is the primitive orbit coded by $CA(CB)^{k-1}$.

The boundary-crowding theorem of @WangLongCycle2026, proved using the Koenigs coordinate of $h$ at $r$, gives $$\label{eq:boundary-asymptotic}
 \delta_k=C_{\mathrm b}a^k(1+o(1)),
 \qquad C_{\mathrm b}>0.$$ Only this analytic asymptotic, not its decimal constant, is needed below.

[\[cor:ratio-spacing\]]{#cor:ratio-spacing label="cor:ratio-spacing"} As $k\to\infty$, $$\begin{aligned}
 \frac{\delta_{k+1}}{\delta_k}&\longrightarrow a,
 \label{eq:ratio-law}\\
 p_{2(k+1)}-p_{2k}
 =\delta_k-\delta_{k+1}
 &=C_{\mathrm b}(1-a)a^k(1+o(1)).
 \label{eq:spacing-law}\end{aligned}$$ In particular, for some $k_0$, constants $c_\pm>0$ and $0<q<1$, $$\label{eq:geometric-bounds}
 c_-a^k\le\delta_k\le c_+a^k,
 \qquad
 \frac{\delta_{k+1}}{\delta_k}\le q
 \quad(k\ge k_0).$$

The first two statements follow by dividing and subtracting [\[eq:boundary-asymptotic\]](#eq:boundary-asymptotic){reference-type="eqref" reference="eq:boundary-asymptotic"}. The uniform bounds follow by increasing $k_0$ and absorbing the finitely many earlier indices into the constants.

The deterministic ladder therefore has one new scale whenever $\sigma$ is multiplied by $a$. Define its continuous clock $$\label{eq:clock}
 H_\sigma
 :=\frac{\log(1/\sigma)}{|\log a|}
 =\frac{\log(1/\sigma)}{2\log\lambda}.$$ The purpose of the next sections is to show that $H_\sigma$ counts singular directions of a canonical Gaussian operator up to a bounded error.

# Exact conditioned-Gaussian geometry {#sec:gaussian-geometry}

Let $$\label{eq:normal-density}
 \phi_\sigma(x)=\frac1{\sqrt{2\pi}\sigma}
 e^{-x^2/(2\sigma^2)},$$ and let $\Phi$ be the standard normal distribution function. A Gaussian row with mean $1-\delta$, conditioned not to cross the upper boundary, is the probability measure on $(-\infty,1]$ given by $$\label{eq:conditioned-row}
 \frac{d\nu_{\sigma,\delta}}{dy}(y)
 =\frac{\phi_\sigma(y-(1-\delta))}{\Phi(\delta/\sigma)}
 \mathbf1_{(-\infty,1]}(y),
 \qquad \delta\ge0.$$ Its Hellinger fingerprint is the unit vector $$\label{eq:fingerprint}
 \psi_{\sigma,\delta}(y)
 =\sqrt{\frac{d\nu_{\sigma,\delta}}{dy}(y)}
 \in L^2((-infty,1]).$$

[\[thm:affinity\]]{#thm:affinity label="thm:affinity"} For $\delta,\varepsilon\ge0$, put $t=\delta/\sigma$ and $s=\varepsilon/\sigma$. Then $$\label{eq:affinity}
 \boxed{
 \left\langle\psi_{\sigma,\delta},
 \psi_{\sigma,\varepsilon}\right\rangle
 =A(t,s)
 :=e^{-(t-s)^2/8}
 \frac{\Phi((t+s)/2)}{\sqrt{\Phi(t)\Phi(s)}}.}$$ In particular, the row geometry depends on $\delta$ and $\sigma$ only through their ratio.

Use the boundary coordinate $x=(y-1)/\sigma\le0$. Taking square roots in [\[eq:conditioned-row\]](#eq:conditioned-row){reference-type="eqref" reference="eq:conditioned-row"} gives $$\begin{aligned}
 \left\langle\psi_{\sigma,\delta},
 \psi_{\sigma,\varepsilon}\right\rangle
 &=\frac1{\sqrt{2\pi\Phi(t)\Phi(s)}}
 \int_{-\infty}^0
 \exp\left[-\frac{(x+t)^2+(x+s)^2}{4}\right]dx.\end{aligned}$$ Completing the square separates the factor $e^{-(t-s)^2/8}$; the remaining integral is $\sqrt{2\pi}\Phi((t+s)/2)$. This proves [\[eq:affinity\]](#eq:affinity){reference-type="eqref" reference="eq:affinity"}.

Let $\psi_{\sigma,0}$ be the limiting endpoint fingerprint and define the orthogonal projection $$\label{eq:endpoint-projection}
 \mathcal Q_\sigma
 =\mathrm I-|\psi_{\sigma,0}\rangle\langle\psi_{\sigma,0}|.$$ The energy that remains after endpoint extraction is $$\label{eq:F-definition}
 F(t)
 :=\|\mathcal Q_\sigma\psi_{\sigma,\sigma t}\|_2^2
 =1-A(t,0)^2.$$

[\[lem:F-bounds\]]{#lem:F-bounds label="lem:F-bounds"} The function $F$ is continuous, $0\le F(t)<1$, and $$\begin{aligned}
 F(t)
 &=\frac{\pi-2}{4\pi}t^2+O(t^3)
 &&(t\downarrow0),
 \label{eq:F-small}\\
 1-F(t)
 &=2e^{-t^2/4}(1+o(1))
 &&(t\to\infty).
 \label{eq:F-large}\end{aligned}$$ Consequently there are $C,c>0$ such that $$\label{eq:F-global-bounds}
 F(t)\le Ct^2\quad(0\le t\le1),
 \qquad
 1-F(t)\le Ce^{-ct^2}\quad(t\ge1).$$

From [\[eq:affinity\]](#eq:affinity){reference-type="eqref" reference="eq:affinity"}, $$\label{eq:endpoint-overlap}
 A(t,0)=e^{-t^2/8}
 \frac{\Phi(t/2)}{\sqrt{\Phi(t)\Phi(0)}}.$$ Taylor expansion of $\log A(t,0)$ at zero gives $$\log A(t,0)
 =-\frac{\pi-2}{8\pi}t^2+O(t^3).$$ Substitution in [\[eq:F-definition\]](#eq:F-definition){reference-type="eqref" reference="eq:F-definition"} proves [\[eq:F-small\]](#eq:F-small){reference-type="eqref" reference="eq:F-small"}. As $t\to\infty$, both distribution functions in the numerator and the nonconstant denominator tend to one, while $\Phi(0)=1/2$. Thus $A(t,0)^2=2e^{-t^2/4}(1+o(1))$, proving [\[eq:F-large\]](#eq:F-large){reference-type="eqref" reference="eq:F-large"}. Compactness of the transition region supplies the global bounds.

The coefficient in [\[eq:F-small\]](#eq:F-small){reference-type="eqref" reference="eq:F-small"} is not fitted. It quantifies the loss of one endpoint row against another when their means differ by much less than one noise width.

## Power fingerprints and linear kernel rows

Hellinger geometry is useful for comparing probability rows, but the square root is nonlinear. To connect the resolution count to the linear kernel row space, fix $\beta>0$ and define $$\label{eq:power-fingerprint}
 \psi^{(\beta)}_{\sigma,\delta}
 =\frac{(d\nu_{\sigma,\delta}/dy)^\beta}
 {\|(d\nu_{\sigma,\delta}/dy)^\beta\|_2}.$$ The Hellinger vector is $\beta=1/2$, while $\beta=1$ is the $L^2$-normalized linear Gaussian kernel row. The $L^1$ conditioning normalizer cancels from the latter direction.

[\[prop:powered-affinity\]]{#prop:powered-affinity label="prop:powered-affinity"} For every fixed $\beta>0$, $$\label{eq:powered-affinity}
 \left\langle
 \psi^{(\beta)}_{\sigma,\delta},
 \psi^{(\beta)}_{\sigma,\varepsilon}
 \right\rangle
 =A_\beta(t,s)
 :=e^{-\beta(t-s)^2/4}
 \frac{\Phi(\sqrt{\beta/2}\,(t+s))}
 {\sqrt{\Phi(\sqrt{2\beta}\,t)
 \Phi(\sqrt{2\beta}\,s)}}.$$ For $\beta=1/2$, this is [\[eq:affinity\]](#eq:affinity){reference-type="eqref" reference="eq:affinity"}.

In the boundary coordinate, the normalized vector is proportional to $e^{-\beta(x+t)^2/2}\mathbf1_{x\le0}$. Complete the square in the product of the two vectors. Its normalization integrals are $\sqrt{\pi/\beta}\,\Phi(\sqrt{2\beta}\,t)$ and the corresponding expression with $s$, which gives [\[eq:powered-affinity\]](#eq:powered-affinity){reference-type="eqref" reference="eq:powered-affinity"}.

For each fixed $\beta$, the projected energy $F_\beta(t)=1-A_\beta(t,0)^2$ is $O_\beta(t^2)$ at zero and approaches one with a Gaussian tail. These are exactly the two properties used in the rank proof.

## The physical interval and folding

The normal form above omits the lower state boundary. For the present ladder this omission is exponentially accurate because $p_{2k}\ge p_2=0.9010184\ldots$. Let $\nu^I_{\sigma,\delta}$ be the Gaussian with mean $1-\delta$, conditioned on $[-1,1]$, and let $\psi^I_{\sigma,\delta}$ be its Hellinger fingerprint, extended by zero to $(-\infty,1]$.

[\[prop:physical-rows\]]{#prop:physical-rows label="prop:physical-rows"} There are $C,c,\sigma_0>0$ such that, uniformly for $0\le\delta\le\delta_1$ and $0<\sigma<\sigma_0$, $$\label{eq:interval-row-error}
 \|\psi^I_{\sigma,\delta}-\psi_{\sigma,\delta}\|_2
 \le Ce^{-c/\sigma^2}.$$ After folding the conditioned row by $y\mapsto|y|$, its Hellinger affinity matrix differs from the positive half-line affinity matrix by the same type of exponentially small bound on every block of $O(H_\sigma)$ resolved rows.

Under the upper-conditioned law, the omitted mass below $-1$ is bounded by the Gaussian tail at distance $1+p_2>1.9$ from the mean. It is therefore $O(e^{-c/\sigma^2})$, uniformly in the ladder. Conditioning once more on $y\ge-1$ changes the square-root density by the square root of this tail, which is still of the stated form after changing $c$. Folding adds the reflected density from $y<0$. Its mass is bounded by the Gaussian tail at distance $p_2$ and is again exponentially small. Hellinger distance controls the change of affinity, and a block with $O(H_\sigma)$ entries retains an exponentially small total error.

This proposition will let the rank theorem transfer to the physical row family. It does not insert the deterministic Jacobian or time ordering of the transfer operator; those are dynamical data beyond row resolution.

# Endpoint extraction and the compact resolution operator {#sec:resolution-operator}

One might first try the row synthesis $$\label{eq:uncentered-synthesis}
 \mathcal U_\sigma c
 =\sum_{k\ge1}c_k\psi_{\sigma,\delta_k}$$ on finitely supported sequences. This is the wrong object.

[\[prop:unbounded\]]{#prop:unbounded label="prop:unbounded"} The map in [\[eq:uncentered-synthesis\]](#eq:uncentered-synthesis){reference-type="eqref" reference="eq:uncentered-synthesis"} has no bounded extension from $\ell^2(\mathbb N)$ to $L^2((-infty,1])$.

Since $\delta_k\to0$, [\[thm:affinity\]](#thm:affinity){reference-type="ref" reference="thm:affinity"} gives $\psi_{\sigma,\delta_k}\to\psi_{\sigma,0}$ in $L^2$. Given $N$, choose a block of $N$ sufficiently late rows, and put $c_k=N^{-1/2}$ on that block. Then $\|c\|_{\ell^2}=1$, while $$\mathcal U_\sigma c
 =\sqrt N\,\psi_{\sigma,0}+o(1)$$ after choosing the block far enough along the ladder. The operator norm on finitely supported sequences is therefore unbounded.

The common endpoint vector is the row-space analogue of a peripheral mode: it must be removed before a compact residual object can exist.

[\[def:resolution-operator\]]{#def:resolution-operator label="def:resolution-operator"} For $\sigma>0$, define $$\label{eq:R-definition}
 \mathcal R_\sigma:\ell^2(\mathbb N)\longrightarrow L^2((-infty,1]),
 \qquad
 \mathcal R_\sigma e_k
 =\mathcal Q_\sigma\psi_{\sigma,\delta_k}.$$

[\[prop:gram\]]{#prop:gram label="prop:gram"} The operator $\mathcal R_\sigma$ is Hilbert--Schmidt. If $t_k=\delta_k/\sigma$, then $$\begin{aligned}
 \|\mathcal R_\sigma\|_{S_2}^2
 &=\sum_{k\ge1}F(t_k),
 \label{eq:HS-exact}\\
 (\mathcal R_\sigma^*\mathcal R_\sigma)_{jk}
 &=A(t_j,t_k)-A(t_j,0)A(0,t_k).
 \label{eq:Gram-exact}\end{aligned}$$

The Gram identity follows from the rank-one projection [\[eq:endpoint-projection\]](#eq:endpoint-projection){reference-type="eqref" reference="eq:endpoint-projection"}. For fixed $\sigma$, the geometric bound [\[eq:geometric-bounds\]](#eq:geometric-bounds){reference-type="eqref" reference="eq:geometric-bounds"} and [\[eq:F-global-bounds\]](#eq:F-global-bounds){reference-type="eqref" reference="eq:F-global-bounds"} give $$\sum_{k\ge1}\|\mathcal R_\sigma e_k\|_2^2
 =\sum_{k\ge1}F(\delta_k/\sigma)<\infty.$$ This is the Hilbert--Schmidt criterion [@Simon2005] and proves [\[eq:HS-exact\]](#eq:HS-exact){reference-type="eqref" reference="eq:HS-exact"}.

# Hilbert--Schmidt energy and the half-logarithmic clock {#sec:HS-law}

The first rank law is already visible in the trace of the Gram operator.

[\[thm:HS-law\]]{#thm:HS-law label="thm:HS-law"} As $\sigma\downarrow0$, $$\label{eq:HS-law}
 \boxed{
 \|\mathcal R_\sigma\|_{S_2}^2
 =H_\sigma+O(1)
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1).}$$

Let $$\label{eq:J-definition}
 J_\sigma=\max\{k:\delta_k\ge\sigma\}.$$ The two-sided bounds in [\[eq:geometric-bounds\]](#eq:geometric-bounds){reference-type="eqref" reference="eq:geometric-bounds"} give $$\label{eq:J-clock}
 J_\sigma=H_\sigma+O(1).$$ Choose $0<a_-<a<a_+<1$ so that, after increasing $k_0$, $$\label{eq:ratio-bracket}
 a_-\le\frac{\delta_{k+1}}{\delta_k}\le a_+
 \qquad(k\ge k_0).$$ Maximality in [\[eq:J-definition\]](#eq:J-definition){reference-type="eqref" reference="eq:J-definition"} makes $1\le t_{J_\sigma}<a_-^{-1}$. Moving backward and forward from that index therefore gives, up to finitely many initial terms, $$\label{eq:t-geometric}
 t_{J_\sigma-m}\ge a_+^{-m},
 \qquad
 t_{J_\sigma+m}\le a_-^{-1}a_+^m.$$

By [\[eq:F-global-bounds\]](#eq:F-global-bounds){reference-type="eqref" reference="eq:F-global-bounds"}, $$\begin{aligned}
 \left|
 \sum_{k\ge1}F(t_k)-J_\sigma
 \right|
 &\le
 \sum_{k\le J_\sigma}(1-F(t_k))
 +\sum_{k>J_\sigma}F(t_k)\\
 &\le C\sum_{m\ge0}e^{-c a_+^{-2m}}
 +C\sum_{m\ge1}a_+^{2m}+O(1).\end{aligned}$$ Both series are finite independently of $\sigma$. Combine this bound with [\[eq:HS-exact\]](#eq:HS-exact){reference-type="eqref" reference="eq:HS-exact"} and [\[eq:J-clock\]](#eq:J-clock){reference-type="eqref" reference="eq:J-clock"}.

The bounded remainder need not converge. An exact geometric ladder already has a discrete scaling phase.

[\[prop:geometric-renormalization\]]{#prop:geometric-renormalization label="prop:geometric-renormalization"} If $\delta_k=C a^k$ exactly and $$\label{eq:geometric-energy}
 E(\sigma)=\sum_{k\ge1}F(Ca^k/\sigma),$$ then $$\label{eq:energy-renormalization}
 E(a\sigma)-E(\sigma)=F(C/\sigma)\longrightarrow1.$$

Shift the summation index in $E(a\sigma)$ and use $F(t)\to1$.

Thus one unit of Hilbert--Schmidt energy is released whenever the noise is reduced by the deterministic factor $a=\lambda^{-2}$. The bounded staircase seen numerically is a consequence of discrete endpoint scaling, not an anomalous fitted exponent.

# The threshold singular-value theorem {#sec:rank-law}

Let $$\label{eq:singular-values}
 s_1(\mathcal R_\sigma)\ge s_2(\mathcal R_\sigma)\ge\cdots\ge0$$ be the singular values, repeated with multiplicity, and for $\eta>0$ put $$\label{eq:threshold-count}
 \mathfrak n_\eta(\sigma)
 =\#\{j:s_j(\mathcal R_\sigma)>\eta\}.$$

[\[thm:rank-law\]]{#thm:rank-law label="thm:rank-law"} For every fixed $0<\eta<1$, $$\label{eq:rank-law}
 \boxed{
 \mathfrak n_\eta(\sigma)
 =H_\sigma+O_\eta(1)
 =\frac{\log(1/\sigma)}{2\log\lambda}+O_\eta(1)}
 \qquad(\sigma\downarrow0).$$

We prove the upper and lower bounds separately.

*Upper bound.* Split $\mathcal R_\sigma=R_{\le J}+R_{>J}$ at $J=J_\sigma$ from [\[eq:J-definition\]](#eq:J-definition){reference-type="eqref" reference="eq:J-definition"}. The first operator has rank at most $J$. The tail estimate in the proof of [\[thm:HS-law\]](#thm:HS-law){reference-type="ref" reference="thm:HS-law"} gives $$\label{eq:tail-HS}
 \|R_{>J}\|_{S_2}^2\le C.$$ The approximation-number inequality followed by the Hilbert--Schmidt Chebyshev bound yields $$\label{eq:rank-upper}
 \mathfrak n_\eta(\sigma)
 \le J+\eta^{-2}\|R_{>J}\|_{S_2}^2
 \le H_\sigma+O_\eta(1).$$

*Lower bound.* Fix $q<1$ and $k_0$ as in [\[eq:geometric-bounds\]](#eq:geometric-bounds){reference-type="eqref" reference="eq:geometric-bounds"}. For a constant $K>1$ to be chosen, let $$\label{eq:M-definition}
 M_\sigma=\max\{k:\delta_k\ge K\sigma\}.$$ Again $M_\sigma=H_\sigma+O_K(1)$. For $k_0\le k<M_\sigma$, $$\label{eq:resolved-spacing}
 \frac{\delta_k-\delta_{k+1}}\sigma
 \ge(1-q)K=:L.$$ Hence the dimensionless centers $t_k$ in this block are ordered with spacing at least $L$.

For $t,s\ge K$, the exact affinity obeys $$\label{eq:affinity-majorants}
 A(t,s)\le\Phi(K)^{-1}e^{-(t-s)^2/8},
 \qquad
 A(t,0)\le
 \sqrt{\frac2{\Phi(K)}}e^{-t^2/8}.$$ Let $G$ be the Gram matrix [\[eq:Gram-exact\]](#eq:Gram-exact){reference-type="eqref" reference="eq:Gram-exact"} restricted to $k_0\le k\le M_\sigma$. The off-diagonal row sums of the first term are bounded by $$\label{eq:off-diagonal-bound}
 \frac2{\Phi(K)}\sum_{m\ge1}e^{-L^2m^2/8},$$ while the operator norm of the endpoint rank-one subtraction is bounded by $$\label{eq:endpoint-vector-bound}
 C\sum_{m\ge0}e^{-(K+mL)^2/4}.$$ Both bounds tend to zero as $K\to\infty$, because $L=(1-q)K$. Choose $K=K(\eta)$ so large that their sum is less than $1-\eta^2$. Gershgorin's theorem, or equivalently the Schur bound, then gives $$\label{eq:riesz-lower}
 G\ge\eta^2\mathrm I.$$ Thus $\mathcal R_\sigma$ is bounded below by $\eta$ on a subspace of dimension $M_\sigma-k_0+1$. The min--max characterization of singular values gives $$\label{eq:rank-lower}
 \mathfrak n_\eta(\sigma)
 \ge M_\sigma-k_0+1
 =H_\sigma-O_\eta(1).$$ Together with [\[eq:rank-upper\]](#eq:rank-upper){reference-type="eqref" reference="eq:rank-upper"}, this proves [\[eq:rank-law\]](#eq:rank-law){reference-type="eqref" reference="eq:rank-law"}.

[\[cor:half-energy\]]{#cor:half-energy label="cor:half-energy"} At the fixed threshold $$\label{eq:half-energy-threshold}
 \eta_*=2^{-1/2},$$ the number of singular directions retaining more than half their squared energy satisfies $$\label{eq:half-energy-law}
 \mathfrak n_{\eta_*}(\sigma)
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1).$$

The special threshold is used only for a parameter-free numerical audit. The theorem itself holds at every fixed threshold strictly between zero and one.

[\[cor:power-universality\]]{#cor:power-universality label="cor:power-universality"} Let $\mathcal R_\sigma^{(\beta)}$ be defined as in [\[eq:R-definition\]](#eq:R-definition){reference-type="eqref" reference="eq:R-definition"}, using the power fingerprints [\[eq:power-fingerprint\]](#eq:power-fingerprint){reference-type="eqref" reference="eq:power-fingerprint"} and projection away from $\psi^{(\beta)}_{\sigma,0}$. For every fixed $\beta>0$, $$\begin{aligned}
 \|\mathcal R_\sigma^{(\beta)}\|_{S_2}^2
 &=H_\sigma+O_\beta(1),
 \label{eq:power-HS-law}\\
 \#\{j:s_j(\mathcal R_\sigma^{(\beta)})>\eta\}
 &=H_\sigma+O_{\beta,\eta}(1),
 \qquad 0<\eta<1.
 \label{eq:power-rank-law}\end{aligned}$$ In particular, the half-logarithmic law holds for the linear kernel-row directions $\beta=1$.

The exact kernel [\[eq:powered-affinity\]](#eq:powered-affinity){reference-type="eqref" reference="eq:powered-affinity"} gives $F_\beta(t)\le C_\beta t^2$ near zero and $1-F_\beta(t)\le C_\beta e^{-c_\beta t^2}$ at infinity. For separated resolved rows, its off-diagonal affinity is bounded by $C_{\beta,K}e^{-\beta(t-s)^2/4}$. The proofs of [\[thm:HS-law,thm:rank-law\]](#thm:HS-law,thm:rank-law){reference-type="ref" reference="thm:HS-law,thm:rank-law"} therefore apply verbatim with constants depending on $\beta$.

[\[cor:physical-rank\]]{#cor:physical-rank label="cor:physical-rank"} Define the endpoint-projected resolution operators from either the Hellinger fingerprints or the $L^2$-normalized linear Gaussian rows conditioned on $[-1,1]$, and likewise from their folded versions on $[0,1]$. Their Hilbert--Schmidt energy and threshold rank obey the corresponding laws above.

For unresolved rows $\delta_k\le\sigma$, smooth dependence of the normalized finite-interval fingerprint on $t=\delta/\sigma$ gives the same bound $\|\mathcal Q\psi_t\|^2\le Ct^2$. This supplies the Hilbert--Schmidt tail and the upper rank bound. The $O(H_\sigma)$ resolved Gram block differs from the half-line block by $O(H_\sigma e^{-c/\sigma^2})$ in row-sum norm by [\[prop:physical-rows\]](#prop:physical-rows){reference-type="ref" reference="prop:physical-rows"}. Hence the Riesz lower bound [\[eq:riesz-lower\]](#eq:riesz-lower){reference-type="eqref" reference="eq:riesz-lower"} persists for small $\sigma$. The finitely many remaining noise values are absorbed into the $O(1)$ constants.

# What the theorem supplies to bulk scattering {#sec:bulk-bridge}

The pole section in the preceding paper was $$\label{eq:pole-section}
 \Pi_N(q)=1+q+\cdots+q^N,
 \qquad q=z^2/\lambda.$$ It resolves the deterministic pole through $2N$ reciprocal resonances. The integer $N$ was numerically selected from the noisy spectrum and conjectured to obey the half-logarithmic clock. The present theorem provides an intrinsic candidate that is independent of eigenvalue selection: $$\label{eq:intrinsic-degree}
 N_\sigma^{\mathrm{row}}
 :=\mathfrak n_{2^{-1/2}}(\sigma).$$

Three conclusions are now rigorous.

1.  The factor $1/2$ in the logarithmic clock comes from the deterministic component contraction $a=\lambda^{-2}$, not from fitting the cloud.

2.  The integer counts stable Gaussian row directions, rather than merely counting cycle clearances above a manually chosen distance.

3.  Endpoint extraction is structurally necessary: without it the row synthesis is not even bounded, whereas after extraction it is compact with the exact rank law.

What is not yet rigorous is equally important. Singular values of a row dictionary are not eigenvalues of the Markov operator. The deterministic Jacobians, transitions between successive contacts, and coupling to the interior component have not entered $\mathcal R_\sigma$. Consequently this paper does not prove $$\label{eq:not-proved}
 N_\sigma^{\mathrm{cloud}}
 =N_\sigma^{\mathrm{row}},$$ nor does it prove the roots-of-unity phases of the cloud.

The next operator proof can now be stated more precisely:

1.  Construct a Feshbach/Grushin endpoint block after the RH-14 peripheral boundary layers are removed [@WangBoundaryLayer2026].

2.  Compare its linear row-resolution part with $\mathcal R_\sigma^{(1)}$ using pre- and post-maps whose condition numbers are uniform on the $H_\sigma+O(1)$ transition subspace.

3.  Prove that time ordering on those resolved directions is a unilateral shift plus an operator-norm remainder small on the $H_\sigma^{-1}$ spectral scale.

The first two items would transfer the linear-row rank law to the actual dynamical block; the third would turn rank into the characteristic polynomial $\Pi_{N_\sigma}$. This separates the remaining dynamical problem from the Gaussian resolution problem solved here.

# Numerical audit {#sec:numerics}

The computations use no large transfer matrix. Boundary points are evaluated from [\[eq:boundary-fixed-point\]](#eq:boundary-fixed-point){reference-type="eqref" reference="eq:boundary-fixed-point"} with 110-decimal arithmetic. Singular values come from the exact Gram matrix [\[eq:Gram-exact\]](#eq:Gram-exact){reference-type="eqref" reference="eq:Gram-exact"}. NumPy, SciPy, mpmath and Matplotlib provide the implementation [@HarrisEtAl2020; @VirtanenEtAl2020; @Mpmath2026; @Hunter2007].

## Boundary constant and singular-value staircase

The scaled clearances stabilize to $$\label{eq:boundary-constant-numerical}
 \delta_k\lambda^{2k}\longrightarrow
 C_{\mathrm b}=0.4608051492217\ldots.$$ This is a high-precision evaluation of the analytic constant in [\[eq:boundary-asymptotic\]](#eq:boundary-asymptotic){reference-type="eqref" reference="eq:boundary-asymptotic"}, not an interval enclosure.

shows the two mechanisms in the proof. The boundary clearances form a geometric ladder. The exact projected energy is quadratic for $\delta\ll\sigma$ and saturates for $\delta\gg\sigma$. The resulting Gram spectra contain a plateau near one whose length increases by roughly one whenever the noise is multiplied by $a$.

![Endpoint resolution audit. Top left: high-precision boundary clearances and their asymptotic geometric law. Top right: the exact endpoint-projected Hellinger energy and its parameter-free quadratic tangent. Bottom left: singular-value plateaux at six noise levels; the horizontal line is the half-energy threshold. Bottom right: the analytic clock, Hilbert--Schmidt energy, threshold rank and independently archived RH-15 cloud degrees.](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/figures/endpoint_gaussian_resolution_rank.pdf>){#fig:rank-audit width="\\textwidth"}

Over $10^{-14}\le\sigma\le10^{-2}$, sampled at 49 logarithmic points, the observed defects are $$\begin{aligned}
 -2.067
 &\le \|\mathcal R_\sigma\|_{S_2}^2-H_\sigma
 \le-1.838,
 \label{eq:energy-defect-range}\\
 -2.558
 &\le \mathfrak n_{2^{-1/2}}(\sigma)-H_\sigma
 \le-1.449.
 \label{eq:rank-defect-range}\end{aligned}$$ For the $\beta=1$ normalized linear rows, the corresponding energy defect lies in $[-1.708,-1.503]$ and the half-energy rank defect lies in $[-2.115,-1.115]$. Thus power universality is visible at the finite scales as well as in the theorem. The bounded ranges are diagnostics consistent with the $O(1)$ theorems, not the source of those theorems. At $\sigma=10^{-8}$, changing the retained unresolved tail from $\delta_k/\sigma\ge10^{-4}$ to $10^{-12}$ leaves the half-energy rank equal to 16 in all five truncations.

## Comparison with the archived resonance cloud

No cloud eigenvalue is used to build $\mathcal R_\sigma$. After the half-energy threshold is fixed, the model can therefore be compared out of sample with the automatically selected cloud degrees from RH-15. The result is [1](#tab:cloud-comparison){reference-type="ref" reference="tab:cloud-comparison"}.

::: {#tab:cloud-comparison}
            $\sigma$   $H_\sigma$   row rank   cloud degree   difference   phase RMS
  ------------------ ------------ ---------- -------------- ------------ -----------
           $10^{-2}$        4.446          2              3         $-1$     0.07933
    $4\times10^{-3}$        5.330          3              3            0     0.07773
    $2\times10^{-3}$        5.999          4              4            0     0.02431
           $10^{-3}$        6.668          5              5            0     0.02184
    $5\times10^{-4}$        7.338          5              5            0     0.04522
    $2\times10^{-4}$        8.222          6              6            0     0.02636
           $10^{-4}$        8.891          7              7            0     0.01124

  : Endpoint row rank versus the archived RH-15 bulk cloud. The model uses the exact boundary ladder and the fixed threshold $s_j^2>1/2$.
:::

The six smallest-noise values agree exactly and the coarsest differs by one. The count is unchanged throughout the threshold interval $0.6\le\eta\le0.8$ at every level except that this statement does not repair the coarsest mismatch. Thus the comparison is not a threshold-tuning artifact. It is nevertheless a comparison of two finite numerical procedures, and no probability or validation claim is attached to the six matches.

![Left: bounded staircase defects against the fractional half-logarithmic phase. Right: half-energy row rank against the independently selected RH-15 cloud degree. Two noise levels occupy the same point at degree five.](<../../../../../zeta_mvp0/papers/RH-16-endpoint-gaussian-resolution-rank/figures/rank_defect_cloud_comparison.pdf>){#fig:defect-cloud width="\\textwidth"}

## Numerical status

The boundary fixed points are ordinary high-precision computations and the Gram eigenvalues are ordinary double-precision computations. The test suite checks the first seven clearances against the independent RH-10 archive, verifies the affinity by direct quadrature, checks the exact small-$t$ coefficient, the $\beta=1$ linear-row kernel, Gram positivity, tail stability, and the two logarithmic laws. No finite computation is used to certify a theorem constant or an actual Markov resonance.

# Conclusion

The half-logarithmic endpoint clock now has an intrinsic operator meaning. The geometric boundary cycles supply conditioned Gaussian transition rows; after their common endpoint vector is removed, those rows form a Hilbert--Schmidt resolution operator. Its exact Hellinger Gram kernel yields both $$\|\mathcal R_\sigma\|_{S_2}^2
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1)$$ and $$\#\{j:s_j(\mathcal R_\sigma)>\eta\}
 =\frac{\log(1/\sigma)}{2\log\lambda}+O_\eta(1),
 \qquad 0<\eta<1.$$ The proof explains the factor $1/2$, the bounded staircase defect, and the necessity of endpoint extraction. Power-row universality includes the $L^2$-normalized linear kernel rows, and the result also survives the finite state interval and folding used by the physical Gaussian operator.

The numerical agreement with the resonance-cloud degree is unusually clean, but the logical boundary remains firm: row singular values are not Markov eigenvalues. The next gate is to factor the actual endpoint transfer block through this resolution operator and then recover the unilateral shift. If that factorization fails, the rank theorem remains valid while the geometric cloud mechanism must be revised; if it succeeds, the degree of the pole section will no longer be an empirical input.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript, exact formulas, high-precision boundary ladder, Gram spectra, rank and tail audits, archived-cloud comparison, tests, figures and machine-readable summary are archived with this paper [@WangEndpointRankCode2026].
