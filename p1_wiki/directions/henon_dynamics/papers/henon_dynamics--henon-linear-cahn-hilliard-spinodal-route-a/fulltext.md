---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-linear-cahn-hilliard-spinodal-route-a"
canonical_tex: "henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a/paper/main.pdf"
source_sha256: "7659e8dcee85d4b279bee8d205c2e189b358bcb89f852b8a15d7d985ba2804b4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Full-Dimensional Linear Cahn--Hilliard Spinodal Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_linear_cahn_hilliard_spinodal_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite $d\ge1$, $\kappa>0$, and $\alpha\in\mathbb R$, we classify the linear Cahn--Hilliard flow $u_t=-\kappa\Delta^2u-\alpha\Delta u$ on the $2\pi$-periodic torus. The result gives the self-adjoint analytic trace-class semigroup, exact lattice-shell spectrum, and the complete stable/critical/spinodal atlas. \>0 It also closes the energy law, Morse index and kernel, all fastest-shell ties, actual-support asymptotics, recurrence, and the singular $\kappa=0$ face. \>1 A 1653-cell archive with independent checker, symbolic, replay, mutation, and deterministic-build lanes is regression evidence; it is not the proof.
author:
- 'Route-A source-local certificate HCS-C304'
date: 3 September 2026
title: 'The Full-Dimensional Linear Cahn--Hilliard Spinodal Atlas'
```

## Markdown 正文

trailerid \[\<C3042026090300000000000000000000\>\<C3042026090300000000000000000000\>\]

# One theorem for the entire parameter space

Let $\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d$, $H=L^2_0(\mathbb T^d)$, and $$A=-\kappa\Delta^2-\alpha\Delta,\qquad
 D(A)=H^4(\mathbb T^d)\cap H,
 \quad \kappa>0,\quad\alpha\in\mathbb R.$$ Write $r_d(n)=\#\{k\in\mathbb Z^d:|k|^2=n\}$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every finite $d\ge1$ the operator $A$ is self-adjoint, bounded above, and has compact resolvent. It generates a self-adjoint analytic semigroup $S(t)$, trace class for every $t>0$. On shell $n>0$, $$\label{eq:rate}
 Ae_k=\sigma_ne_k,\qquad \sigma_n=\alpha n-\kappa n^2,$$ with multiplicity $r_d(n)$. The mean-zero equilibrium is exponentially stable iff $\alpha<\kappa$, critical iff $\alpha=\kappa$, and spinodally unstable iff $\alpha>\kappa$. Its unstable Morse index and kernel dimension are $$\label{eq:index}
 M=\sum_{n<\alpha/\kappa}r_d(n),\qquad
 K=\sum_{n=\alpha/\kappa}r_d(n),$$ where absent shells contribute zero. At criticality $K=r_d(1)=2d$.

The spectral bound is attained precisely on $$\label{eq:fast}
 \mathcal N_*=\operatorname*{argmax}_{n\ge1,\ r_d(n)>0}
 (\alpha n-\kappa n^2),$$ including every tie. For $u_0\ne0$, let $\lambda_*=\max\{\sigma_n:P_nu_0\ne0\}$. Then $$\label{eq:limit}
 e^{-\lambda_*t}S(t)u_0\longrightarrow
 \sum_{\sigma_n=\lambda_*}P_nu_0\quad\hbox{in }L^2.$$ Every recurrent state is stationary; hence there is no nonstationary periodic solution.

For $e_k=(2\pi)^{-d/2}e^{ik\cdot x}$, $\Delta e_k=-|k|^2e_k$, so [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"} follows. The real diagonal values tend to $-\infty$ as $|k|\to\infty$, proving self-adjointness, compact resolvent, and an upper bound. The spectral theorem yields the analytic semigroup, while $$\sum_{k\ne0}e^{t(\alpha|k|^2-\kappa|k|^4)}<\infty\qquad(t>0)$$ by quartic domination, proving trace class. The sign factorization $\sigma_n=n(\alpha-\kappa n)$ proves the chamber and index formulas.

The maximization in [\[eq:fast\]](#eq:fast){reference-type="eqref" reference="eq:fast"} is over the whole represented spectrum, not a numerical cutoff. Indeed $$\label{eq:square}
 \sigma_n=\frac{\alpha^2}{4\kappa}
 -\kappa\left(n-\frac{\alpha}{2\kappa}\right)^2.$$ If $\alpha/\kappa\le1$, then for $n>1$, $\sigma_n-\sigma_1=(n-1)[\alpha-\kappa(n+1)]<0$. If $\alpha/\kappa>1$, shell one has positive rate whereas every $n\ge\alpha/\kappa$ has nonpositive rate. Thus an explicit finite set of represented integers contains every maximizer, and all ties are retained. For a fixed datum the same decay at infinity gives a largest rate in its actual support. Factoring $e^{\lambda_*t}$ and dominated convergence prove [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"}. Finally, recurrence along $t_j\to\infty$ forces $e^{t_j\sigma_n}\widehat u_0(k)\to\widehat u_0(k)$ coefficientwise; every nonzero coefficient must have $\sigma_n=0$, so the state is stationary.

\>0

# Gradient-flow law and singular faces

Set $$\mathcal F(u)=\frac12\int_{\mathbb T^d}
 (\kappa|\nabla u|^2-\alpha|u|^2)\,\mathrm dx,
 \qquad \mu=-\kappa\Delta u-\alpha u.$$ The equation is $u_t=\Delta\mu$. Periodic integration by parts gives the exact dissipation identity $$\label{eq:energy}
 \frac{\,\mathrm d}{\,\mathrm dt}\mathcal F(u(t))
 =\langle\mu,\Delta\mu\rangle=-\|\nabla\mu\|_2^2.$$ This explains the energy signature without turning linear instability into a nonlinear saturation or coarsening theorem.

[\[prop:boundary\]]{#prop:boundary label="prop:boundary"} On full $L^2$, the constant mode is stationary and equals the conserved mean. On the mean-zero space $H$, the singular face $\kappa=0$ is interpreted with its natural generator domain: for $\alpha\ne0$, the operator $-\alpha\Delta$ has domain $H^2(\mathbb T^d)\cap H$, while for $\alpha=0$ the zero generator has domain all of $H$. It gives forward heat when $\alpha<0$, the identity when $\alpha=0$, and no bounded $L^2$ $C_0$ semigroup when $\alpha>0$.

The zero shell has rate zero. On the stated natural domains, the $\kappa=0$ positive shells have rates $\alpha n$. Negative $\alpha$ gives heat, zero gives identity, and positive $\alpha$ makes $\sup_ne^{t\alpha n}=\infty$ for every $t>0$.

  ----------------------------------------------------------------------------------------------------
  Face                     Exact conclusion
  ------------------------ ---------------------------------------------------------------------------
  $\alpha<\kappa$          every mean-zero shell decays exponentially.

  $\alpha=\kappa$          only shell one is neutral; its dimension is $2d$.

  $\alpha>\kappa$          finitely many represented shells are unstable.

  fastest tie              retain the entire tied spectral projection.

  missing ambient leader   use the largest rate in the actual support of $u_0$.

  $\kappa\downarrow0$      heat / identity / no bounded semigroup according to the sign of $\alpha$.
  ----------------------------------------------------------------------------------------------------

\>1

# Finite evidence, hostile audit, and scope

The deterministic archive contains 18 rational cases in dimensions one through six, 216 shell rows, six actual-support probes, three singular-face rows, and six boundary rows: 1653 audited leaves. Each case records the analytic exhaustion cutoff from the proof; the 12 displayed receipt shells do not prove [\[eq:fast\]](#eq:fast){reference-type="eqref" reference="eq:fast"}. An independent checker reconstructs all shell multiplicities and values in 1930 assertions. A separate symbolic lane checks 36 identities, isolated replay demands two byte-identical outputs, and 72 repaired-hash or parser mutations must all be rejected.

Hostile tests alter the fastest set, exhaustion statement and cutoff, Morse/kernel dimensions, canonical rationals and decimals, exact JSON/YAML trees and types, and Route-A claims. They also attack duplicate keys, nonfinite tokens, YAML anchors, aliases, and merges. The three round variants are each rebuilt in two fresh directories at a fixed epoch and audited for warnings, text, pages, and fonts; the final PDF is a byte-identical alias of round 2.

#### Collision and claim boundaries.

Earlier Fourier packages C206/C213/C217/C218/C261/C277 use different transport, hyperbolic, dispersive, fractional, or damping generators; C195 is nonlinear viscous Burgers. Here the theorem is the fourth-order conserved linear spinodal atlas in every finite dimension. It claims neither nonlinear Cahn--Hilliard saturation/coarsening nor literature novelty.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Lattice shells are source Fourier geometry, not arithmetic local data (A0); stationary recurrence supplies no primitive-orbit bridge (A1); physical time is not a prime clock (A2); no target determinant or functional equation is constructed (A3). Self-adjointness is only a source-side formal hint, not a Hilbert--Pólya or target-zero result (A4). The overall verdict is `ROUTE_A_REJECTED`; Route B remains locked. No target Euler factor, root number, automorphy, divisor law, functional equation, or zero match is claimed.

#### Reproducibility and AI use.

The release retains producer-independent validation, exact evidence, three substantive manuscript revisions, and a self-excluding manifest. A generative language model assisted with drafting and code scaffolding; independent executable lanes check formulas, artifacts, and scope, and final responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

Cahn and Hilliard introduced the nonuniform free-energy model, and Cahn's spinodal paper is the historical owner token for the instability language. Elliott and Zheng provide classical analytical context. These references establish lineage only.

9 J. W. Cahn and J. E. Hilliard, "Free Energy of a Nonuniform System. I. Interfacial Free Energy," *J. Chem. Phys.* 28 (1958), 258--267. DOI: [10.1063/1.1744102](https://doi.org/10.1063/1.1744102). J. W. Cahn, "On spinodal decomposition," *Acta Metallurgica* 9 (1961), 795--801. DOI: [10.1016/0001-6160(61)90182-1](https://doi.org/10.1016/0001-6160(61)90182-1). C. M. Elliott and S. Zheng, "On the Cahn--Hilliard equation," *Arch. Rational Mech. Anal.* 96 (1986), 339--357. DOI: [10.1007/BF00251803](https://doi.org/10.1007/BF00251803).
