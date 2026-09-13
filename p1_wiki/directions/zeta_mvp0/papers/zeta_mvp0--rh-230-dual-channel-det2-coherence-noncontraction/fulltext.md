---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-230-dual-channel-det2-coherence-noncontraction"
canonical_tex: "zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/main.pdf"
source_sha256: "0e19f76ac5f18fa40f1070bfc94cc525a8f3c593b700135ad01be1b74a2aa71c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dual-Channel Regularized-Determinant Coherence Without Cross-Scale Contraction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-230-dual-channel-det2-coherence-noncontraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The full Frobenius complement bound fails, but the shell-complete selected clouds still define finite second-regularized determinant factors. This paper compares those factors without branch matching.

  On the closed unit disk all selected resonances satisfy $|z\lambda|<1$, so the principal logarithm $$L_\Lambda(z)=
   \sum_{\lambda\in\Lambda}
   [\log(1-z\lambda)+z\lambda]$$ is single valued and permutation invariant. It is evaluated on a 256-point grid for sixteen left/right channel pairs and thirty adjacent-scale pairs.

  All sixteen channel comparisons pass the predeclared sup-log gate $0.02$; the maximum difference is $0.017855$. Adjacent-scale differences are much larger, ranging from $0.042131$ to $0.183660$. Neither channel is strictly contracting over its last four transitions, and the final adjacent errors are approximately $0.0712$ and $0.0792$.

  Thus the two physical channels remain coherent at each frozen scale, but the selected factors do not form a visibly Cauchy small-noise family. This is a mixed finite result. It supports a shared dual-channel determinant renormalization while ruling out simple convergence of the selected factor as the current mechanism.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Dual-Channel Regularized-Determinant Coherence\
  Without Cross-Scale Contraction
```

## Markdown 正文

# Branch-free determinant comparison

Individual nonnormal eigenvalue branches can collide and exchange labels. A symmetric spectral function avoids that ambiguity. For a finite multiset $\Lambda$, define $$\label{eq:log}
 L_\Lambda(z)=
 \sum_{\lambda\in\Lambda}
 [\log(1-z\lambda)+z\lambda].$$ Whenever $|z|\max_{\lambda\in\Lambda}|\lambda|<1$, every logarithm is the branch analytic from zero and $$e^{L_\Lambda(z)}
 =\prod_{\lambda\in\Lambda}(1-z\lambda)e^{z\lambda}.$$

[\[prop:symmetry\]]{#prop:symmetry label="prop:symmetry"} The function $L_\Lambda$ is invariant under every permutation of the multiset. If $\Lambda$ is conjugate closed, then $$\overline{L_\Lambda(\overline z)}=L_\Lambda(z).$$

Both statements follow by permuting or conjugating the summands in [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"}.

No cross-level root assignment is required.

# Trace-power interpretation

Inside the same disk, $$\label{eq:trace}
 L_\Lambda(z)=
 -\sum_{m=2}^{\infty}\frac{z^m}{m}\tau_m(\Lambda),
 \qquad
 \tau_m(\Lambda)=\sum_{\lambda\in\Lambda}\lambda^m.$$ Hence comparison of two selected factors measures all finite-cloud power-trace differences simultaneously. The missing $m=1$ term suppresses barycentric drift but does not erase genuine higher-order spectral motion.

At fixed positive noise, the corresponding infinite trace series is the Hilbert--Schmidt determinant of RH-7 [@WangRH7]. Here [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} is used only for selected finite clouds.

# Common grid and gates

The grid consists of 64 angles on each radius $$0.25,\quad0.5,\quad0.75,\quad1,$$ for 256 points in total. The largest selected resonance modulus in the whole atlas is $0.86860$, so the closed unit disk remains strictly inside the logarithmic convergence disk.

For two clouds define $$\label{eq:metric}
 d_{\mathcal G}(\Lambda,\Gamma)
 =\max_{z\in\mathcal G}|L_\Lambda(z)-L_\Gamma(z)|.$$ The dual-channel gate is frozen at $$d_{\mathcal G}(\Lambda_{\sigma,L},
 \Lambda_{\sigma,R})<0.02.$$ No gate is imposed after seeing the adjacent-scale values. Their diagnostic is whether the last four transition errors are strictly decreasing.

# Dual-channel result

All sixteen channel pairs pass. Representative values are:

     $\sigma$   channel sup-log difference
  ----------- ----------------------------
    $0.04000$                   $0.003309$
    $0.02500$                   $0.009120$
    $0.01600$                   $0.014354$
    $0.00800$                   $0.017855$
    $0.00500$                   $0.003103$
    $0.00250$                   $0.008517$
    $0.00125$                   $0.014933$

The sequence is not monotone, but every value stays below the declared finite gate. This extends the dual-channel coherence of the quartet divisor to rank-growing selected regularized factors.

The ranks differ by one at several scales, so the agreement is not a trivial comparison of identical cardinalities. Second regularization and the small inner-shell moduli reduce the effect of those extra roots.

# Adjacent-scale result

For each channel, compare consecutive noise levels using the same metric [\[eq:metric\]](#eq:metric){reference-type="eqref" reference="eq:metric"}. Across 30 cases, $$0.042131\le d_{\mathcal G}\le0.183660.$$ These errors are all larger than the worst same-scale channel difference.

The final four left-channel transition errors are approximately $$0.12033,\quad0.06780,\quad0.05237,\quad0.07121,$$ and the right-channel values are $$0.11715,\quad0.08456,\quad0.04213,\quad0.07916.$$ Both sequences increase on the final transition. Therefore neither passes strict tail contraction.

  diagnostic                                       result
  ------------------------------ ------------------------
  dual-channel cases                                   16
  dual-channel gate passes                             16
  maximum channel error                        $0.017855$
  adjacent-scale cases                                 30
  adjacent error range             $0.042131$--$0.183660$
  last-four contraction, left                          no
  last-four contraction, right                         no

# Interpretation

The mixed verdict rules out two simplistic conclusions.

First, channel coherence does not imply scale convergence. The Haar-compressed and fine endpoints approximate one physical construction at a fixed noise, whereas changing $\sigma$ changes the operator and increases selected rank.

Second, noncontraction of the selected factor does not disprove convergence of a relative determinant. A moving near-unit cloud may need to be divided out, and the unresolved complement may contribute compensating terms. RH-80 gives the abstract factorization target [@WangRH80]; RH-229 shows why a raw Frobenius bound cannot supply its uniform complement estimate [@WangRH229].

# Claim boundary

The comparison is finite and grid based. Although [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"} is analytic on the whole unit disk, a grid maximum is only a sampled diagnostic, not a validated supremum. The products include selected clouds only and omit the unresolved determinant tail.

The justified conclusions are finite dual-channel coherence and absence of the tested cross-scale contraction. No locally uniform determinant, dynamical limit, self-adjoint generator, counting law, or arithmetic trace formula is proved. Gate A remains open.
