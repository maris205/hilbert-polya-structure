---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-irrational-ellipsoid-reeb-orbit-atlas"
canonical_tex: "henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas/paper/main.pdf"
source_sha256: "031067d0c86c8d4d24e419a546a98edb84e9b7a2bb870d18493ee3cd91e1987e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Irrational--Rational Reeb Orbit Atlas for Ellipsoids

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_irrational_ellipsoid_reeb_orbit_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the standard contact form on the boundary of the four-dimensional ellipsoid $E(a,b)=\{\pi|z_1|^2/a+\pi|z_2|^2/b\le1\}$. An elementary closure argument gives exactly two simple coordinate Reeb orbits when $a/b$ is irrational. Their actions and periods, transverse return multipliers, and Conley--Zehnder indices are recorded for twelve iterates, with every $\sqrt2$ floor certified by integer-square inequalities. For rational $a/b=p/q$ we instead expose the full-boundary Morse--Bott family and leave the pre-perturbation CZ index undefined. This is a source-local analytic A1 theorem; it has no arithmetic owner or target determinant.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'An Exact Irrational--Rational Reeb Orbit Atlas for Ellipsoids'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen contact model

Let $$E(a,b)=\left\{(z_1,z_2)\in\mathbb C^2:
 \frac{\pi|z_1|^2}{a}+\frac{\pi|z_2|^2}{b}\le1\right\},\qquad a,b>0,$$ and let $\lambda_0=\frac12\sum_j(x_jdy_j-y_jdx_j)$ on $\partial E(a,b)$. The Reeb flow and coordinate circles are $$\varphi_t(z_1,z_2)=\big(e^{2\pi it/a}z_1,e^{2\pi it/b}z_2\big),
 \quad \gamma_1=\{z_2=0\},\quad \gamma_2=\{z_1=0\}.$$ The actions equal the periods: $A(\gamma_1)=T(\gamma_1)=a$ and $A(\gamma_2)=T(\gamma_2)=b$. We use the coordinate complex-line trivialization used by Hutchings ($\xi|_{\gamma_1}$ is the second $\mathbb C$ summand and $\xi|_{\gamma_2}$ the first), rather than silently identifying it with a filling-disk framing.

If $a/b\notin\mathbb Q$, the only simple closed Reeb orbits are $\gamma_1$ and $\gamma_2$. For every $k\ge1$, $$\begin{aligned}
 A(\gamma_1^k)=T(\gamma_1^k)&=ka,&
 \rho_\perp(\gamma_1^k)&=e^{\pm2\pi i k a/b},&
 \mu_{\rm CZ}(\gamma_1^k)&=2\lfloor ka/b\rfloor+1,\\
 A(\gamma_2^k)=T(\gamma_2^k)&=kb,&
 \rho_\perp(\gamma_2^k)&=e^{\pm2\pi i k b/a},&
 \mu_{\rm CZ}(\gamma_2^k)&=2\lfloor kb/a\rfloor+1.\end{aligned}$$ All these returns are nondegenerate.

If both coordinates of a point are nonzero and it returns at time $t>0$, then $t/a$ and $t/b$ are integers, forcing $a/b\in\mathbb Q$. Thus an irrational slope leaves only the two axes. Along $\gamma_1^k$, the transverse complex line rotates by $2\pi k a/b$, and along $\gamma_2^k$ by $2\pi k b/a$. The rotation-index convention in Hutchings gives the displayed odd floor formulas; irrationality excludes an integer crossing, hence nondegeneracy. Integrating $\lambda_0$ over each coordinate circle gives its action, and the flow formula gives its period.

# The rational Morse--Bott boundary

Suppose $a/b=p/q$ in lowest terms. The common period is $L=qa=pb$. Every point of the boundary returns at $L$, so the Morse--Bott critical manifold is the full three-dimensional boundary and its orbit-space family has dimension two. The coordinate circles are degenerate members with transverse multiplier one. Consequently a nondegenerate CZ integer is not assigned before a perturbation; applying an irrational floor formula here would be a category error. The receipt contains rational controls $2/1$, $3/2$, and $5/3$, including the exact resonance equation.

# Integer-square certificates

For $a/b=\sqrt2$, the index of $\gamma_1^k$ uses the integer $m$ with $$m^2\le2k^2<(m+1)^2,$$ while the swapped transverse ratio $1/\sqrt2$ uses $$2m^2\le k^2<2(m+1)^2.$$ These inequalities are evaluated with integer arithmetic for $1\le k\le12$ and therefore certify every floor without a floating-point boundary test. A 90-digit calculation is used only to print the real and imaginary components of the unit multiplier; the independent checker verifies those displays.

  regime                                 rows                                    exact content
  ------------------------------------ ------ ------------------------------------------------
  irrational $\sqrt2$ and reciprocal       48     action, period, multiplier, CZ, square proof
  rational Morse--Bott controls             6   resonance, common period, unit return, null CZ

  : Finite receipt dimensions and locked route disposition.

\>0

# Independent audit

The producer is deterministic and emits the canonical JSON receipt. A producer-independent checker makes 2,000-plus exact assertions, a SymPy program checks the flow, rotation matrix, resonance, and square identities, and byte replay compares two fresh producer runs. A hostile suite rejects 29/29 repaired-hash mutations, including altered floors, multipliers, resonance rows, scope flags, and route verdicts.

\>1

# Route-A boundary

The geometric orbit theorem is an analytic A1 result. There is no intrinsic rational-prime carrier, prime-power clock, target weighted zeta, Fredholm determinant, or target-zero match. We therefore record $$(\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED` and Route B disabled. The source-local orbit product must not be reinterpreted as a target arithmetic structure.

9 M. Hutchings, *Lecture notes on embedded contact homology*, arXiv:1303.5789, <https://arxiv.org/abs/1303.5789>. H. Hofer, K. Wysocki and E. Zehnder, The dynamics on three-dimensional strictly convex energy surfaces, *Ann. of Math.* (2) 148 (1998), DOI: 10.2307/120994, <https://doi.org/10.2307/120994>.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero, determinant-matching, or Hilbert--Pólya claim. **Data and code.** The receipt and audits accompany HCS-C242. This is not external peer review. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checks the displayed formulas and metadata.
